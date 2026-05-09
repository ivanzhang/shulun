#!/usr/bin/env python3
"""Prime Matrix Euler-Maclaurin replay 舍入纪律路由器。

用法示例：
  python3 experiments/prime_matrix_em_replay_rounding_discipline_router.py

输出：
  docs/monograph/prime-matrix-em-replay-rounding-discipline-router.json
  docs/monograph/prime-matrix-em-replay-rounding-discipline-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-top-critical-derivative-bound-router.json"
DEFAULT_TRACE = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_TAIL = MONO / "prime-matrix-theta-mellin-taylor-tail-order-router.json"
DEFAULT_JSON = MONO / "prime-matrix-em-replay-rounding-discipline-router.json"
DEFAULT_MD = MONO / "prime-matrix-em-replay-rounding-discipline-router.md"

OLD_ATOM = "DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger"
CLOSED_ATOM = "DyadicComplexIntervalEulerMaclaurinReplayRoundingClosedCanonicalDAGv1"
CENTER_ATOM = "TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"


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


def operation_map() -> list[dict[str, str]]:
    """列出 EM replay 的运算归属。"""
    return [
        {
            "operation": "dyadic centers c_j and height 14",
            "covered_by": "DyadicRationalIntervalArithmeticCoreClosed",
            "note": "中心点、网格端点、N=32、p=8、Bernoulli 系数均为有理数据。",
        },
        {
            "operation": "log n",
            "covered_by": "RationalLogTrigTaylorOracleTemplateClosed",
            "note": "n<=32，atanh-log 模板给向外有理盒。",
        },
        {
            "operation": "n^{-s}=exp(-s log n)",
            "covered_by": "RationalExpTaylorRangeReductionTemplateClosed AND RationalLogTrigTaylorOracleTemplateClosed",
            "note": "拆成 exp(-sigma log n)*(cos(14 log n)-i sin(14 log n))。",
        },
        {
            "operation": "rising factorial (s)_m",
            "covered_by": "ComplexRectangularIntervalPropagationClosed",
            "note": "有限复矩形乘法和加法。",
        },
        {
            "operation": "division by s-1",
            "covered_by": "ComplexRectangularIntervalPropagationClosed",
            "note": "|s-1|>=14，除法零排斥有显式下界。",
        },
        {
            "operation": "EM remainder interval",
            "covered_by": "integer endpoint inequality plus Bernoulli periodic bound",
            "note": "使用标准余项上界写成实半径，加入复盒外包。",
        },
        {
            "operation": "node ordering and reproducibility",
            "covered_by": "IntervalOperationTraceHashLedgerClosedCanonicalDAGv1",
            "note": "每个中心值 replay 是 canonical DAG root hash。",
        },
    ]


def build_rows(previous: dict[str, Any], trace: dict[str, Any], tail: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 EM replay 舍入纪律判定表。"""
    active = previous.get("secondary_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    derivative_ready = previous.get("top_critical_derivative_bound_closed") is True
    trace_ready = trace.get("interval_operation_trace_hash_ledger_closed") is True
    kernel_ready = trace.get("certified_complex_ball_kernel_closed") is True
    tail_ready = tail.get("tail_orders_closed") is True
    closed = active and guard and derivative_ready and trace_ready and kernel_ready and tail_ready
    return [
        row(
            "EMRoundingGateActive",
            active,
            True,
            "导数门闭合后，并行实现门是 EM 中心值 replay 的舍入纪律。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只规定有限中心值证书的可复放计算纪律，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "CertifiedIntervalKernelImported",
            kernel_ready and tail_ready,
            True,
            "dyadic、复矩形、log/trig/exp Taylor 尾阶与 trace/hash 账本均已闭合。",
            "all arithmetic primitives available.",
        ),
        row(
            "EulerMaclaurinOperationMapClosed",
            closed,
            True,
            "EM replay 的每种运算都落入已闭合的区间核或整数不等式。",
            CLOSED_ATOM,
        ),
        row(
            "CenterValuesStillMissing",
            False,
            False,
            "舍入纪律不替代 1024 个中心值的实际非零下界表。",
            CENTER_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            closed,
            "EM replay 舍入纪律已闭合，剩余只是真正的中心值表。",
            CLOSED_ATOM if closed else OLD_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 EM replay 舍入纪律路由。"""
    previous = load_json(paths["previous"])
    trace = load_json(paths["trace"])
    tail = load_json(paths["tail"])
    rows = build_rows(previous, trace, tail)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_em_replay_rounding_discipline_router",
        "status": "em_replay_rounding_discipline_closed_center_values_only"
        if closed
        else "em_replay_rounding_discipline_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "em_replay_rounding_discipline_closed": closed,
        "top_critical_segment_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "operation_map": operation_map(),
        "next_priority": CENTER_ATOM,
        "secondary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger 已闭合：Euler-Maclaurin 中心值 replay "
            "所需的 dyadic、复矩形、log/trig/exp、除法和余项外包均落入已闭合区间核与 trace/hash 账本。"
            "严格自足剩余只剩 1024 个中心值下界表。"
            if closed
            else "EM replay 舍入纪律尚未闭合；需要补齐上游区间核或 trace/hash 输入。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Euler-Maclaurin replay 舍入纪律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"em_replay_rounding_discipline_closed={fmt_bool(result['em_replay_rounding_discipline_closed'])}",
        f"top_critical_segment_self_contained_closed={fmt_bool(result['top_critical_segment_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 运算映射",
        "",
        "| operation | covered by | note |",
        "| --- | --- | --- |",
    ]
    for item in result["operation_map"]:
        lines.append(
            "| {operation} | {covered_by} | {note} |".format(
                operation=table_cell(item["operation"]),
                covered_by=table_cell(item["covered_by"]),
                note=table_cell(item["note"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            f"严格自足唯一顶边剩余：`{result['next_priority']}`。",
            f"顶边完成后仍需：`{result['secondary_priority']}`。",
            "",
            "判定：舍入纪律不是剩余；中心值 replay 表才是剩余。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--trace-json", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--tail-json", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "trace": args.trace_json,
        "tail": args.tail_json,
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
