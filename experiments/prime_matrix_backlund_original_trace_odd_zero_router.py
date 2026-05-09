#!/usr/bin/env python3
"""Prime Matrix Backlund 原始 trace 奇部为零审查路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_original_trace_odd_zero_router.py

输出：
  docs/monograph/prime-matrix-backlund-original-trace-odd-zero-router.json
  docs/monograph/prime-matrix-backlund-original-trace-odd-zero-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-half-mirror-average-obstruction-router.json"
DEFAULT_TRANSPORT = MONO / "prime-matrix-backlund-zeta-xi-branch-jump-transport-router.json"
DEFAULT_LOWH = MONO / "prime-matrix-lowheight-xi-backlund-integration-router.json"
DEFAULT_NEAR = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-original-trace-odd-zero-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-original-trace-odd-zero-router.md"

ODD_ZERO_ATOM = "BacklundOriginalTraceOddPartZeroLedger"
ZERO_AVOIDING_ATOM = "BacklundZeroAvoidingShiftWithoutJumpLedger"
ODD_CORRECTION_ATOM = "BacklundOddMirrorCorrectionCostLedger"
INDENT_COST_ATOM = "BacklundZeroProximityIndentationCostLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
HALF_AVERAGE_ATOM = "BacklundOriginalTraceHalfMirrorAverageIdentityLedger"
TRACE_ATOM = "BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def impossibility_reasons() -> list[dict[str, str]]:
    """列出原始奇部为零不能作为全局目标的原因。"""
    return [
        {
            "reason": "actual_zeros_exist",
            "detail": "zeta/xi 的非平凡零点存在；当高度命中零点 ordinates 时，原始 trace 的 branch jump 不能被宣布为 0。",
        },
        {
            "reason": "endpoint_convention_is_not_absence",
            "detail": "端点 convention 只规定避开后取极限并按重数计数，不证明 jump 消失。",
        },
        {
            "reason": "near_zero_separation_is_assignment",
            "detail": "eta=1/16 近零分离只是把近零点交给凹口成本账本，不证明近零点集合为空。",
        },
        {
            "reason": "jensen_count_allows_zeros",
            "detail": "Jensen C16 是数量上界，允许 O(log T) 个局部零点；它不支持奇部恒为 0。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    transport: dict[str, Any],
    lowheight: dict[str, Any],
    near: dict[str, Any],
    endpoint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成原始奇部为零审查判定表。"""
    active = previous.get("next_priority") == ODD_ZERO_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    transport_ready = transport.get("zeta_xi_branch_jump_transport_closed") is True
    lowheight_closed = lowheight.get("lowheight_xi_rectangle_count_closed") is True
    near_assigned = near.get("near_zero_indent_separation_external_closed") is True
    endpoint_ready = (
        endpoint.get("endpoint_multiplicity_convention_closed") is True
        or endpoint.get("endpoint_multiplicity_convention_self_contained_closed") is True
    )
    global_odd_zero_rejected = active and guard and transport_ready and lowheight_closed and near_assigned and endpoint_ready
    return [
        row(
            "OriginalTraceOddZeroGateActive",
            active,
            True,
            "半镜像平均障碍后，当前候选最窄点是证明原始 trace 奇部为 0。",
            ODD_ZERO_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只审查假设链条中的解析输入，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "ZetaXiJumpTransportAvailable",
            transport_ready,
            True,
            "branch jump 已可无损搬运到 xi，因此奇部为零等价于原始 trace 没有 crossing jump。",
            ZERO_AVOIDING_ATOM,
        ),
        row(
            "LowHeightClosedButIrrelevantToHighTrace",
            lowheight_closed,
            True,
            "0<t<=14 低高度已闭合，但 Backlund 高度 trace 的零点 crossing 仍可能存在。",
            INDENT_COST_ATOM,
        ),
        row(
            "NearZeroAssignedNotEliminated",
            near_assigned,
            True,
            "近零分离把 eta 内零点交给凹口账本，不证明原始奇部为 0。",
            INDENT_COST_ATOM,
        ),
        row(
            "EndpointConventionCountsJumps",
            endpoint_ready,
            True,
            "端点避零与重数 convention 处理落零极限，但按重数保留 jump，而不是删除 jump。",
            INDENT_COST_ATOM,
        ),
        row(
            "GlobalOddPartZeroRejected",
            global_odd_zero_rejected,
            True,
            "原始奇部为零不能作为全局自足定理；它只有在额外零避让或缩进成本已处理后才成立。",
            ODD_CORRECTION_ATOM,
        ),
        row(
            ODD_ZERO_ATOM,
            False,
            False,
            "该目标与高高度零点 crossing 的真实解析结构不兼容，不能关闭父级半平均路线。",
            f"{ZERO_AVOIDING_ATOM} with cost control OR {ODD_CORRECTION_ATOM}",
        ),
        row(
            ODD_CORRECTION_ATOM,
            False,
            False,
            "剩余必须转为奇部修正成本，也就是 Backlund 凹口成本的自足证明或外部引理。",
            f"{INDENT_COST_ATOM} OR {EXTERNAL_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行原始 trace 奇部为零审查。"""
    previous = load_json(paths["previous"])
    transport = load_json(paths["transport"])
    lowheight = load_json(paths["lowheight"])
    near = load_json(paths["near"])
    endpoint = load_json(paths["endpoint"])
    rows = build_rows(previous, transport, lowheight, near, endpoint)
    rejected = next(item["closed"] for item in rows if item["gate"] == "GlobalOddPartZeroRejected")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_original_trace_odd_zero_router",
        "status": "backlund_original_trace_odd_zero_rejected_indent_correction_next",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "original_trace_odd_zero_rejected": rejected,
        "original_trace_odd_zero_closed": False,
        "half_average_identity_closed": False,
        "backlund_local_crossing_trace_closed": False,
        "row_column_self_contained_closed": False,
        "impossibility_reasons": impossibility_reasons(),
        "replacement_self_contained": {
            ODD_ZERO_ATOM: f"rejected_as_global_target; use ({ODD_CORRECTION_ATOM} OR {EXTERNAL_ATOM})"
        },
        "next_priority": ODD_CORRECTION_ATOM,
        "equivalent_cost_priority": INDENT_COST_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "blocked_parent": HALF_AVERAGE_ATOM,
        "trace_parent": TRACE_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "`BacklundOriginalTraceOddPartZeroLedger` 不能作为全局闭合目标。"
            "它等价于原始 Backlund trace 没有 crossing branch jump；但高高度零点、端点重数 convention、"
            "近零分离和 Jensen 计数都说明 jump 必须被记账而不是删除。"
            "因此内部路线必须回到 `BacklundOddMirrorCorrectionCostLedger`，也就是凹口成本的自足证明；"
            "若接受外部经典 Backlund 缩进引理，则可由外部路线继续闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund 原始 trace 奇部为零审查路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"original_trace_odd_zero_rejected={fmt_bool(result['original_trace_odd_zero_rejected'])}",
        f"original_trace_odd_zero_closed={fmt_bool(result['original_trace_odd_zero_closed'])}",
        f"half_average_identity_closed={fmt_bool(result['half_average_identity_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 不可作为全局目标的原因",
        "",
        "| reason | detail |",
        "| --- | --- |",
    ]
    for item in result["impossibility_reasons"]:
        lines.append(f"| `{table_cell(item['reason'])}` | {table_cell(item['detail'])} |")
    lines.extend(
        [
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "## 3. 判定表",
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
            "## 4. 下一步",
            "",
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"等价成本目标：`{result['equivalent_cost_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            f"被阻断父级：`{result['blocked_parent']}`。",
            "",
            "判定：奇部为零路线被全局解析结构阻断；必须证明奇部修正成本或接受外部 Backlund 缩进引理。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--transport-json", type=Path, default=DEFAULT_TRANSPORT)
    parser.add_argument("--lowheight-json", type=Path, default=DEFAULT_LOWH)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "transport": args.transport_json,
        "lowheight": args.lowheight_json,
        "near": args.near_json,
        "endpoint": args.endpoint_json,
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
