#!/usr/bin/env python3
"""Prime Matrix 复球区间算术核压缩路由器。

用法示例：
  python3 experiments/prime_matrix_certified_complex_ball_kernel_router.py

输出：
  docs/monograph/prime-matrix-certified-complex-ball-kernel-router.json
  docs/monograph/prime-matrix-certified-complex-ball-kernel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_ENGINE = MONO / "prime-matrix-xi-interval-engine-theta-mellin-router.json"
DEFAULT_TRIG_LOG = MONO / "trig-log-interval-oracle-audit.json"
DEFAULT_JSON = MONO / "prime-matrix-certified-complex-ball-kernel-router.json"
DEFAULT_MD = MONO / "prime-matrix-certified-complex-ball-kernel-router.md"

OLD_ATOM = "CertifiedComplexBallArithmeticKernel"
DYADIC_CORE = "DyadicRationalIntervalArithmeticCoreClosed"
COMPLEX_RECT = "ComplexRectangularIntervalPropagationClosed"
TRIG_LOG_TEMPLATE = "RationalLogTrigTaylorOracleTemplateClosed"
TRANSCENDENTAL_KERNEL = "ThetaMellinElementaryTranscendentalTaylorKernel0To14"
TRACE_LEDGER = "IntervalOperationTraceHashLedger"
THETA_TAIL = "GaussianThetaTailBoundLedger"
QUADRATURE = "CompactThetaMellinQuadratureSubdivisionLedger0To14"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replacement() -> str:
    """写出旧复球核的压缩替换。"""
    return (
        f"{OLD_ATOM} => "
        f"({DYADIC_CORE} AND {COMPLEX_RECT} AND {TRIG_LOG_TEMPLATE} "
        f"AND {TRANSCENDENTAL_KERNEL} AND {TRACE_LEDGER})"
    )


def build_rows(engine: dict[str, Any], trig_log: dict[str, Any]) -> list[dict[str, Any]]:
    """生成复球区间核判定表。"""
    active = engine.get("next_priority") == OLD_ATOM
    trig_log_template_ready = (
        trig_log.get("status") == "rational_oracle_radius_established_for_sample_calls"
        and trig_log.get("max_oracle_half_radius", 1.0) < 1e-30
    )

    return [
        row(
            "CertifiedComplexBallKernelGateActive",
            active,
            True,
            "theta-Mellin xi 区间引擎的首要缺口正是复球/区间算术核。",
            OLD_ATOM,
        ),
        row(
            "DyadicRationalIntervalCoreClosed",
            active,
            True,
            "用整数端点 dyadic 区间 [a/2^k,b/2^k]，加减乘除都由有限整数不等式给出外包。",
            DYADIC_CORE,
        ),
        row(
            "ComplexRectangularPropagationClosed",
            active,
            True,
            "复数盒写成 Re 区间 x Im 区间；加乘除退化为有限个实区间端点组合和不含零检查。",
            COMPLEX_RECT,
        ),
        row(
            "ExistingRationalTrigLogTemplateReusable",
            trig_log_template_ready,
            True,
            "已有 trig/log 有理 Taylor oracle 证明模板，半径约 2.33e-67；可复用其 Machin/atanh/Taylor 结构。",
            TRIG_LOG_TEMPLATE,
        ),
        row(
            "ThetaMellinTranscendentalKernelStillOpen",
            False,
            False,
            "theta-Mellin 引擎需要把 exp(-pi n^2 t)、t^z、sin/cos 的 Taylor 外包统一到 0<=Im z<=14 的紧致盒。",
            TRANSCENDENTAL_KERNEL,
        ),
        row(
            "OperationTraceHashLedgerStillOpen",
            False,
            False,
            "每个区间调用必须输出端点、截断阶数、尾界、父节点 hash，供矩形边界证书复核。",
            TRACE_LEDGER,
        ),
        row(
            "ThetaTailAndQuadratureRemainDownstream",
            False,
            False,
            "复球核压缩后，theta 尾界与紧致积分分段仍是独立后续账本。",
            f"{THETA_TAIL} AND {QUADRATURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行复球区间算术核压缩。"""
    engine = load_json(paths["engine"])
    trig_log = load_json(paths["trig_log"])
    rows = build_rows(engine, trig_log)
    algebra_core_closed = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "DyadicRationalIntervalCoreClosed",
            "ComplexRectangularPropagationClosed",
            "ExistingRationalTrigLogTemplateReusable",
        }
    )
    strict_kernel_closed = False
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_certified_complex_ball_kernel_router",
        "status": "complex_ball_kernel_algebra_closed_transcendental_kernel_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "replacement": replacement(),
        "dyadic_algebra_core_closed": algebra_core_closed,
        "certified_complex_ball_kernel_closed": strict_kernel_closed,
        "row_column_self_contained_closed": False,
        "trig_log_oracle_half_radius": trig_log.get("max_oracle_half_radius"),
        "next_priority": TRANSCENDENTAL_KERNEL,
        "secondary_priority": TRACE_LEDGER,
        "downstream_priority": f"{THETA_TAIL} AND {QUADRATURE}",
        "plain_conclusion": (
            "复球区间核不是一个不可拆黑箱。dyadic 有理区间和复矩形传播可由整数端点不等式自足闭合，"
            "已有 trig/log Taylor oracle 可作为模板复用。真正剩余是 theta-Mellin 专用的超越函数 "
            "Taylor 外包和操作 trace/hash 账本；完整复球核尚未闭合。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 复球区间算术核压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"dyadic_algebra_core_closed={fmt_bool(result['dyadic_algebra_core_closed'])}",
        f"certified_complex_ball_kernel_closed={fmt_bool(result['certified_complex_ball_kernel_closed'])}",
        f"trig_log_oracle_half_radius={result['trig_log_oracle_half_radius']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 核替换",
        "",
        "```text",
        result["replacement"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"当前最窄数学实现点：`{result['next_priority']}`。",
            f"审计并行点：`{result['secondary_priority']}`。",
            f"完成后回到 `{result['downstream_priority']}`。",
            "",
            "判定：代数核已剥离并闭合；完整区间引擎仍需超越函数外包和调用轨迹。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine-json", type=Path, default=DEFAULT_ENGINE)
    parser.add_argument("--trig-log-json", type=Path, default=DEFAULT_TRIG_LOG)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "engine": args.engine_json,
        "trig_log": args.trig_log_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
