#!/usr/bin/env python3
"""生成 strict 中段 psi 百万网格节点表分块。

用法示例：
  python3 experiments/prime_matrix_middle_psi_node_batch_runner.py \
    --psi-exe /tmp/PsiTheta/psi \
    --output /tmp/middle-psi-nodes-000000.jsonl \
    --start-index 0 \
    --count 10

  python3 experiments/prime_matrix_middle_psi_node_batch_runner.py \
    --psi-exe /tmp/PsiTheta/psi \
    --output data/middle-psi-fine-mesh-node-table.jsonl \
    --start-index 0 \
    --count 646258 \
    --append

该脚本只生成机器可审计节点记录；完整数学闭合仍需后续 hash、全表验收和 Dusart 口径匹配。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


TARGET_RATIO = Decimal("1.00002841")
X_LEFT = 800_000_000_000
X_RIGHT_FLOAT = math.exp(28)
MESH_H = 1_000_000
EXPECTED_NODE_COUNT = math.ceil((X_RIGHT_FLOAT - float(X_LEFT)) / float(MESH_H))
REQUIRED_NODE_SLACK_FLOOR = Decimal("3073386.85452651")
DEFAULT_SOURCE_COMMIT = "21f4f6553851f218801a733f607426c3dba9ba11"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_x(index: int) -> int:
    """返回第 index 个百万网格起点。"""
    return X_LEFT + index * MESH_H


def decimal_step_from_scientific(text: str, precision_digits: int) -> Decimal:
    """估计 mpfr_out_str 科学计数输出的一个末位单位。"""
    lowered = text.lower()
    if "e" not in lowered:
        return Decimal(10) ** Decimal(-precision_digits + 1)
    _, exponent_text = lowered.split("e", 1)
    exponent = int(exponent_text)
    return Decimal(10) ** Decimal(exponent - precision_digits + 1)


def run_psi(psi_exe: Path, x_i: int, precision: int, timeout: int) -> tuple[Decimal, str, Decimal]:
    """调用外部 psi 程序，并给出保守向上误差界。"""
    completed = subprocess.run(
        [str(psi_exe), str(x_i), str(precision)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or f"psi failed for x={x_i}")
    raw = completed.stdout.strip()
    value = Decimal(raw)
    # 输出是最近舍入；为了得到 slack 下界，按一个末位单位向上包住 psi。
    rounding_error_bound = decimal_step_from_scientific(raw, precision)
    return value, raw, rounding_error_bound


def build_record(
    psi_exe: Path,
    index: int,
    precision: int,
    timeout: int,
    source_commit: str,
    psi_exe_hash: str,
) -> dict[str, Any]:
    """生成单个节点记录。"""
    x_i = expected_x(index)
    psi_value, raw, rounding_error_bound = run_psi(psi_exe, x_i, precision, timeout)
    psi_upper = psi_value + rounding_error_bound
    slack_lower = TARGET_RATIO * Decimal(x_i) - psi_upper
    return {
        "i": index,
        "x_i": x_i,
        "psi_value": str(psi_value),
        "psi_raw_output": raw,
        "psi_rounding_mode": "MPFR_RNDN_output_wrapped_up_by_one_ulp_for_slack_lower_bound",
        "psi_precision_decimal_digits": precision,
        "psi_rounding_error_bound": str(rounding_error_bound),
        "psi_upper_for_slack": str(psi_upper),
        "slack_lower_bound": str(slack_lower),
        "slack_ge_required_floor": slack_lower >= REQUIRED_NODE_SLACK_FLOOR,
        "required_node_slack_floor": str(REQUIRED_NODE_SLACK_FLOOR),
        "source_commit": source_commit,
        "psi_exe_sha256": psi_exe_hash,
    }


def run_batch(args: argparse.Namespace) -> dict[str, Any]:
    """生成一段节点表。"""
    getcontext().prec = 80
    psi_exe = args.psi_exe
    if not psi_exe.exists():
        raise FileNotFoundError(psi_exe)
    if args.start_index < 0 or args.count < 0:
        raise ValueError("start-index and count must be nonnegative")
    if args.start_index + args.count > EXPECTED_NODE_COUNT:
        raise ValueError("requested range exceeds certified mesh")

    psi_hash = sha256(psi_exe)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if args.append else "w"
    min_slack: Decimal | None = None
    min_slack_index: int | None = None
    failures = 0

    with args.output.open(mode, encoding="utf-8") as handle:
        for offset in range(args.count):
            index = args.start_index + offset
            record = build_record(
                psi_exe=psi_exe,
                index=index,
                precision=args.precision,
                timeout=args.timeout,
                source_commit=args.source_commit,
                psi_exe_hash=psi_hash,
            )
            if not record["slack_ge_required_floor"]:
                failures += 1
            slack = Decimal(record["slack_lower_bound"])
            if min_slack is None or slack < min_slack:
                min_slack = slack
                min_slack_index = index
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    return {
        "output": str(args.output),
        "start_index": args.start_index,
        "count": args.count,
        "end_index_exclusive": args.start_index + args.count,
        "psi_exe": str(psi_exe),
        "psi_exe_sha256": psi_hash,
        "precision": args.precision,
        "source_commit": args.source_commit,
        "min_slack": str(min_slack) if min_slack is not None else None,
        "min_slack_index": min_slack_index,
        "slack_failures": failures,
        "output_sha256": sha256(args.output),
    }


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--psi-exe", type=Path, required=True, help="PsiTheta 编译出的 psi 可执行文件")
    parser.add_argument("--output", type=Path, required=True, help="输出 JSONL 分块")
    parser.add_argument("--start-index", type=int, required=True, help="起始节点索引")
    parser.add_argument("--count", type=int, required=True, help="生成节点数")
    parser.add_argument("--precision", type=int, default=30, help="psi 输出十进制有效位数")
    parser.add_argument("--timeout", type=int, default=180, help="单节点超时秒数")
    parser.add_argument("--source-commit", default=DEFAULT_SOURCE_COMMIT, help="PsiTheta 源提交")
    parser.add_argument("--append", action="store_true", help="追加写入而不是覆盖")
    args = parser.parse_args()

    result = run_batch(args)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(0 if result["slack_failures"] == 0 else 1)


if __name__ == "__main__":
    main()
