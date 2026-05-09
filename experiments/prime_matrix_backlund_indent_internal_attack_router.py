#!/usr/bin/env python3
"""Prime Matrix Backlund 凹口成本内部攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_indent_internal_attack_router.py

输出：
  docs/monograph/prime-matrix-backlund-indent-internal-attack-router.json
  docs/monograph/prime-matrix-backlund-indent-internal-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-lowheight-xi-backlund-integration-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_SEPARATION = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_VARIATION = MONO / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_ZERO_DISTANCE = MONO / "prime-matrix-b3-zero-distance-constant-aggregation-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-indent-internal-attack-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-indent-internal-attack-router.md"

OLD_PACKAGE = "(BacklundZeroAvoidingShiftWithoutJumpLedger OR BacklundNearZeroJumpCancellationSubHalfLedger)"
SHIFT_ATOM = "BacklundZeroAvoidingShiftWithoutJumpLedger"
CANCEL_ATOM = "BacklundNearZeroJumpCancellationSubHalfLedger"
TRACE_ATOM = "BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger"
TRACE_CLOSED = "BacklundLocalZeroCrossingTraceAndIndentHomotopyClosed"
INDENT_COST = "BacklundZeroProximityIndentationCostLedger"
CS8 = "BacklundCS8SlackAfterBridgeLedger"
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


def crossing_trace_schema() -> list[dict[str, str]]:
    """定义局部零点穿越 trace 的必要字段。"""
    return [
        {
            "field": "window_id",
            "meaning": "Backlund 短窗口编号，与 h=1/512 的窗口尺度一致。",
        },
        {
            "field": "zero_cluster_box",
            "meaning": "近零点核心 |s-rho|<eta 的区间盒与 multiplicity 账本。",
        },
        {
            "field": "contour_side",
            "meaning": "零点相对移动 contour 的左右/上下侧，决定缩进方向。",
        },
        {
            "field": "homotopy_arc",
            "meaning": "局部缩进圆弧或避让平移的参数化区间。",
        },
        {
            "field": "branch_jump",
            "meaning": "arg zeta 或 arg xi 的局部跳变量，带符号和重数。",
        },
        {
            "field": "paired_cancellation",
            "meaning": "若不避让，必须登记与相邻零点/边界/对称点的抵消配对。",
        },
        {
            "field": "residual_cost",
            "meaning": "抵消后仍需扣除的成本，必须小于全局稳定余量。",
        },
        {
            "field": "trace_hash",
            "meaning": "窗口、零点盒、缩进弧、跳变量和剩余成本的 canonical hash。",
        },
    ]


def reduction_laws() -> list[dict[str, str]]:
    """写出二选一到统一 trace 的压缩律。"""
    return [
        {
            "old": SHIFT_ATOM,
            "new": TRACE_ATOM,
            "reason": "选择避让平移本身必须证明穿越零点集合为空；这正是 crossing trace 的空穿越特例。",
        },
        {
            "old": CANCEL_ATOM,
            "new": TRACE_ATOM,
            "reason": "跳变抵消必须登记每个近零点的符号、重数和配对；这正是 crossing trace 的非空穿越特例。",
        },
        {
            "old": INDENT_COST,
            "new": TRACE_ATOM,
            "reason": "凹口成本不能由零点数量粗付关闭，只能由局部同伦 trace 证明残余成本可预算。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    indent: dict[str, Any],
    separation: dict[str, Any],
    endpoint: dict[str, Any],
    variation: dict[str, Any],
    zero_distance: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成内部凹口攻坚判定表。"""
    active = previous.get("next_priority") == OLD_PACKAGE
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    lowheight_closed = previous.get("lowheight_xi_rectangle_count_closed") is True
    near_zero_partition = separation.get("near_zero_indent_separation_external_closed") is True
    endpoint_convention = (
        endpoint.get("endpoint_zero_avoidance_multiplicity_convention_closed") is True
        or endpoint.get("endpoint_multiplicity_convention_closed") is True
        or endpoint.get("endpoint_multiplicity_convention_self_contained_closed") is True
    )
    variation_ready = variation.get("variation_window_scale_external_closed") is True
    zero_distance_ready = zero_distance.get("zero_distance_constant_aggregation_external_closed") is True
    naive_deficit = float(indent.get("naive_margin_deficit", math.inf))
    trace_proved = False
    return [
        row(
            "IndentInternalAttackActive",
            active,
            True,
            "低高度 xi 子包闭合后，当前严格自足解析最窄点正是凹口成本内部替代包。",
            OLD_PACKAGE,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析记账，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "LowHeightAnchorImported",
            lowheight_closed,
            True,
            "0<t<=14 的低高度零点计数已闭合，可作为 Backlund/Jensen 低端 anchor。",
            "LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed。",
        ),
        row(
            "NearZeroPartitionImported",
            near_zero_partition,
            False,
            "eta=1/16 内近零点已从倒距离和切出，交给凹口成本账本。",
            INDENT_COST,
        ),
        row(
            "EndpointMultiplicityConventionImported",
            endpoint_convention,
            True,
            "端点碰零按重数与极限 convention 处理，但这不提供数量级预算。",
            "EndpointZeroAvoidanceMultiplicityConventionClosed。",
        ),
        row(
            "SafeAnnuliAndWindowImported",
            variation_ready and zero_distance_ready,
            False,
            "eta 外倒距离和与窗口尺度已有外部分支账本；内部缺口只剩 eta 内穿越 trace。",
            TRACE_ATOM,
        ),
        row(
            "NaiveCostContradictionLocked",
            naive_deficit > 0,
            True,
            f"朴素逐零点凹口成本缺口为 {naive_deficit:.12f}，所以粗数量界路线被排除。",
            TRACE_ATOM,
        ),
        row(
            "ShiftOrCancellationUnified",
            True,
            True,
            "零避让是空穿越 trace；跳变抵消是非空穿越 trace。二选一可压成同一个局部同伦账本。",
            TRACE_ATOM,
        ),
        row(
            TRACE_ATOM,
            trace_proved,
            False,
            "当前尚未给出每个近零窗口的零点盒、缩进弧、跳变量和残余成本 hash 账本。",
            TRACE_ATOM,
        ),
        row(
            "BacklundIndentCostSelfContainedClosed",
            trace_proved,
            False,
            "只有 crossing trace 证明残余成本小于稳定余量后，内部凹口成本才可关闭。",
            TRACE_CLOSED,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行内部凹口攻坚路由。"""
    previous = load_json(paths["previous"])
    indent = load_json(paths["indent"])
    separation = load_json(paths["separation"])
    endpoint = load_json(paths["endpoint"])
    variation = load_json(paths["variation"])
    zero_distance = load_json(paths["zero_distance"])
    rows = build_rows(previous, indent, separation, endpoint, variation, zero_distance)
    trace_closed = next(item["closed"] for item in rows if item["gate"] == TRACE_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_indent_internal_attack_router",
        "status": "backlund_indent_internal_reduced_to_crossing_trace_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "indent_or_package_compressed": True,
        "backlund_local_crossing_trace_closed": trace_closed,
        "backlund_indent_self_contained_closed": trace_closed,
        "row_column_self_contained_closed": False,
        "naive_indentation_coefficient": indent.get("naive_indentation_coefficient"),
        "available_stability_margin": indent.get("available_stability_margin"),
        "naive_margin_deficit": indent.get("naive_margin_deficit"),
        "replacement_self_contained": {
            OLD_PACKAGE: TRACE_ATOM,
            INDENT_COST: TRACE_ATOM,
        },
        "crossing_trace_schema": crossing_trace_schema(),
        "reduction_laws": reduction_laws(),
        "rows": rows,
        "next_priority": TRACE_ATOM,
        "post_trace_priority": CS8,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "Backlund 凹口成本的内部二选一已压成一个更窄的统一原子："
            f"`{TRACE_ATOM}`。零避让只是该 trace 的空穿越特例；跳变抵消是非空穿越特例。"
            "当前仍未自足闭合，因为还缺每个近零窗口的零点盒、缩进弧、跳变量、抵消配对和残余成本 hash 账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 凹口成本内部攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"indent_or_package_compressed={fmt_bool(result['indent_or_package_compressed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"backlund_indent_self_contained_closed={fmt_bool(result['backlund_indent_self_contained_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"naive_indentation_coefficient={result['naive_indentation_coefficient']:.12f}",
        f"available_stability_margin={result['available_stability_margin']:.12f}",
        f"naive_margin_deficit={result['naive_margin_deficit']:.12f}",
        "```",
        "",
        "## 1. 二选一压缩律",
        "",
        "| old | new | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["reduction_laws"]:
        lines.append(
            "| `{old}` | `{new}` | {reason} |".format(
                old=table_cell(item["old"]),
                new=table_cell(item["new"]),
                reason=table_cell(item["reason"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. crossing trace 字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["crossing_trace_schema"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
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
            f"当前严格自足最窄点：`{result['next_priority']}`。",
            f"该 trace 完成后进入：`{result['post_trace_priority']}`。",
            f"并行保留晋级门：`{result['parallel_priority']}`。",
            "",
            "判定：凹口成本从二选一缩成单原子 trace；尚未完成自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--separation-json", type=Path, default=DEFAULT_SEPARATION)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--variation-json", type=Path, default=DEFAULT_VARIATION)
    parser.add_argument("--zero-distance-json", type=Path, default=DEFAULT_ZERO_DISTANCE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "indent": args.indent_json,
        "separation": args.separation_json,
        "endpoint": args.endpoint_json,
        "variation": args.variation_json,
        "zero_distance": args.zero_distance_json,
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
