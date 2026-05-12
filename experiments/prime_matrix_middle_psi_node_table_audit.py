#!/usr/bin/env python3
"""审计 strict 中段 psi 百万网格节点表。

用法示例：
  python3 experiments/prime_matrix_middle_psi_node_table_audit.py \
    --table docs/monograph/prime-matrix-strict-middle-psi-fine-mesh-node-table.jsonl

  python3 experiments/prime_matrix_middle_psi_node_table_audit.py \
    --table data/middle-psi-fine-mesh-node-table.jsonl \
    --expect-hash <sha256>

节点表采用 JSONL：每行一个对象，至少包含 i、x_i、psi_value、slack_lower_bound。
本脚本只做机械验收，不生成数学结论；行/列命题状态仍由路由证书控制。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


TARGET_RATIO = Decimal("1.00002841")
X_LEFT = 800_000_000_000
X_RIGHT_FLOAT = math.exp(28)
MESH_H = 1_000_000
EXPECTED_NODE_COUNT = math.ceil((X_RIGHT_FLOAT - float(X_LEFT)) / float(MESH_H))
REQUIRED_NODE_SLACK_FLOOR = Decimal("3073386.85452651")
SLACK_RECOMPUTE_TOLERANCE = Decimal("0.000001")


def sha256(path: Path) -> str:
    """计算表文件的原始字节 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decimal_from_record(record: dict[str, Any], key: str) -> Decimal:
    """从 JSON 记录中读取十进制数，避免浮点二次舍入。"""
    if key not in record:
        raise ValueError(f"missing field {key}")
    return Decimal(str(record[key]))


def expected_x(index: int) -> int:
    """返回第 index 个百万网格起点。"""
    return X_LEFT + index * MESH_H


def iter_jsonl(path: Path):
    """逐行读取 JSONL。"""
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            stripped = line.strip()
            if not stripped:
                continue
            yield line_no, json.loads(stripped)


def audit_table(path: Path, expect_hash: str | None = None, sample_limit: int = 5) -> dict[str, Any]:
    """审计节点表排序、字段、余量和 hash。"""
    getcontext().prec = 50
    errors: list[str] = []
    samples: list[dict[str, Any]] = []
    count = 0
    min_slack: Decimal | None = None
    min_slack_index: int | None = None
    previous_i = -1

    for line_no, record in iter_jsonl(path):
        try:
            i = int(record["i"])
            x_i = int(record["x_i"])
            psi_value = decimal_from_record(record, "psi_value")
            declared_slack = decimal_from_record(record, "slack_lower_bound")
        except (KeyError, ValueError, TypeError, ArithmeticError) as exc:
            errors.append(f"line {line_no}: malformed record: {exc}")
            continue

        if i != previous_i + 1:
            errors.append(f"line {line_no}: non-contiguous index {i}, expected {previous_i + 1}")
        if x_i != expected_x(i):
            errors.append(f"line {line_no}: x_i={x_i}, expected {expected_x(i)}")

        recomputed_slack = TARGET_RATIO * Decimal(x_i) - psi_value
        # C++ runner 以 long double 计算并用科学计数法落盘；这里允许亚微量级的文本舍入差。
        if declared_slack - recomputed_slack > SLACK_RECOMPUTE_TOLERANCE:
            errors.append(f"line {line_no}: declared slack exceeds recomputed slack")
        audited_slack = min(declared_slack, recomputed_slack)
        if audited_slack < REQUIRED_NODE_SLACK_FLOOR:
            errors.append(f"line {line_no}: slack below required floor")

        if min_slack is None or audited_slack < min_slack:
            min_slack = audited_slack
            min_slack_index = i

        if len(samples) < sample_limit:
            samples.append(
                {
                    "i": i,
                    "x_i": x_i,
                    "psi_value": str(psi_value),
                    "slack_lower_bound": str(declared_slack),
                }
            )
        previous_i = i
        count += 1

    file_hash = sha256(path)
    if count != EXPECTED_NODE_COUNT:
        errors.append(f"node count {count}, expected {EXPECTED_NODE_COUNT}")
    if previous_i != EXPECTED_NODE_COUNT - 1:
        errors.append(f"last index {previous_i}, expected {EXPECTED_NODE_COUNT - 1}")
    if expect_hash is not None and file_hash != expect_hash:
        errors.append(f"sha256 mismatch: {file_hash} != {expect_hash}")

    return {
        "table": str(path),
        "sha256": file_hash,
        "expect_hash": expect_hash,
        "passed": not errors,
        "errors": errors[:50],
        "error_count": len(errors),
        "node_count": count,
        "expected_node_count": EXPECTED_NODE_COUNT,
        "min_slack": str(min_slack) if min_slack is not None else None,
        "min_slack_index": min_slack_index,
        "required_node_slack_floor": str(REQUIRED_NODE_SLACK_FLOOR),
        "slack_recompute_tolerance": str(SLACK_RECOMPUTE_TOLERANCE),
        "samples": samples,
    }


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", type=Path, required=True, help="待审计的 JSONL 节点表")
    parser.add_argument("--expect-hash", default=None, help="可选的预期 SHA256")
    args = parser.parse_args()

    result = audit_table(args.table, args.expect_hash)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
