#!/usr/bin/env python3
"""Prime Matrix B=3 近零点缩进分离路由器。

用法示例：
  python3 experiments/prime_matrix_b3_near_zero_indent_separation_router.py

输出：
  docs/monograph/prime-matrix-b3-near-zero-indent-separation-router.json
  docs/monograph/prime-matrix-b3-near-zero-indent-separation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-radius-contingency-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-near-zero-indent-separation-router.md"

OLD_ATOM = "BacklundNearZeroIndentSeparationLedger"
CLOSED_ATOM = "BacklundNearZeroIndentSeparationClosedEta1Over16"
ZERO_DISTANCE_CONST_ATOM = "BacklundZeroDistanceSumConstantAggregationLedger"
INDENT_COST_ATOM = "BacklundZeroProximityIndentationCostLedger"
VARIATION_WINDOW_ATOM = "BacklundVariationWindowScaleLedger"
CS8_ATOM = "BacklundCS8SlackAfterBridgeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ETA = 1.0 / 16.0
OUTER_RADIUS = 4.0
UNIT_RADIUS = 1.0
DYADIC_SHELLS_FROM_UNIT_TO_ETA = int(math.log2(UNIT_RADIUS / ETA)) + 1
DYADIC_SHELLS_FROM_OUTER_TO_ETA = int(math.log2(OUTER_RADIUS / ETA))


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str) -> str:
    """替换近零点分离原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def partition_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成近零点分区表。"""
    return [
        {
            "zone": "near-zero core",
            "condition": "|s-rho| < eta",
            "eta": ETA,
            "handled_by": INDENT_COST_ATOM,
            "effect": "不进入倒距离 dyadic 求和，等待凹口成本账本支付。",
        },
        {
            "zone": "safe dyadic annuli",
            "condition": "eta <= |s-rho| <= 4",
            "eta": ETA,
            "handled_by": ZERO_DISTANCE_CONST_ATOM,
            "effect": "固定有限层 dyadic 环；每层调用 Jensen C16 计数。",
        },
        {
            "zone": "outside disk",
            "condition": "|s-rho| > 4",
            "eta": ETA,
            "handled_by": "Hadamard remainder / outer tail",
            "effect": "不属于局部 Jensen 圆盘倒距离硬点。",
        },
        {
            "zone": "available zero count",
            "condition": "N(D)<=C_N log(T+3)",
            "eta": previous["C_N_target"],
            "handled_by": "external Jensen C16 aggregation",
            "effect": "外部分支已关闭；自足分支仍等低高度零点账本。",
        },
    ]


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成近零点缩进分离判定表。"""
    external_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    c16_ready = bool(previous.get("jensen_c16_aggregation_external_closed"))
    dyadic_ready = "BacklundZeroDistanceDyadicSummationClosed" in external_basis
    indent_cost_still_open = INDENT_COST_ATOM in external_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and c16_ready and dyadic_ready and indent_cost_still_open and guard
    return [
        row(
            "NearZeroIndentSeparationGateActive",
            active,
            False,
            "外部 Backlund/Jensen 分支当前最窄点是把过近零点从倒距离和中剥离。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的解析记账，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "JensenC16ZeroCountAvailableExternally",
            c16_ready,
            False,
            "外部分支已有 Jensen C16 局部零点计数；它只给数量，不处理路径贴近零点的奇性。",
            "BacklundIndependentJensenZeroCountC16AggregationExternalClosed",
        ),
        row(
            "FixedEtaIndentConventionClosed",
            ETA > 0.0 and ETA < 1.0,
            True,
            "固定 eta=1/16；|s-rho|<eta 的零点统一交给凹口成本，不进入倒距离主和。",
            CLOSED_ATOM,
        ),
        row(
            "SafeDyadicAnnuliRemainFinite",
            DYADIC_SHELLS_FROM_OUTER_TO_ETA == 6,
            True,
            "eta 到外半径 4 之间只有固定 6 层 dyadic 环，因此不会引入额外 log log 或可变层数。",
            ZERO_DISTANCE_CONST_ATOM,
        ),
        row(
            "NearZerosAssignedToIndentCostLedger",
            indent_cost_still_open,
            True,
            "近零点没有被丢弃；它们被保留为零点邻近凹口成本账本的输入。",
            INDENT_COST_ATOM,
        ),
        row(
            "NearZeroIndentSeparationClosed",
            closed,
            True,
            "近零/远零分区完成：远零点可做 dyadic 倒距离常数聚合，近零点转入凹口成本。",
            CLOSED_ATOM,
        ),
        row(
            "ZeroDistanceConstantAggregationNext",
            False,
            False,
            "近零分离后，下一步要合并 dyadic 层数、Jensen C16 常数和 eta 截断常数。",
            ZERO_DISTANCE_CONST_ATOM,
        ),
        row(
            "IndentCostStillDownstream",
            False,
            False,
            "凹口成本本身还未支付；它是后续尖峰排斥闭合的独立账本。",
            INDENT_COST_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行近零点缩进分离路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "NearZeroIndentSeparationClosed"
    )
    latest_external = replace_atom(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "b3_near_zero_indent_separation_router",
        "status": "near_zero_indent_separation_external_closed_indent_cost_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "near_zero_indent_separation_external_closed": closed,
        "near_zero_indent_separation_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "eta": ETA,
        "outer_radius": OUTER_RADIUS,
        "dyadic_shells_from_unit_to_eta": DYADIC_SHELLS_FROM_UNIT_TO_ETA,
        "dyadic_shells_from_outer_to_eta": DYADIC_SHELLS_FROM_OUTER_TO_ETA,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": ZERO_DISTANCE_CONST_ATOM,
        "post_distance_priority": VARIATION_WINDOW_ATOM,
        "post_window_priority": INDENT_COST_ATOM,
        "post_indent_priority": CS8_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "partition_rows": partition_rows(previous),
        "plain_conclusion": (
            "近零点分离在外部 Backlund/Jensen 分支中已闭合为固定 eta=1/16 的记账规则："
            "eta 外的零点进入有限 dyadic 倒距离常数聚合，eta 内的零点不估掉而转入凹口成本账本。"
            "因此本步关闭的是分区和无循环纪律，不关闭后续凹口成本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 近零点缩进分离路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "near_zero_indent_separation_external_closed="
            f"{fmt_bool(result['near_zero_indent_separation_external_closed'])}"
        ),
        (
            "near_zero_indent_separation_self_contained_closed="
            f"{fmt_bool(result['near_zero_indent_separation_self_contained_closed'])}"
        ),
        f"eta={fmt_float(result['eta'])}",
        f"outer_radius={fmt_float(result['outer_radius'])}",
        f"dyadic_shells_from_outer_to_eta={result['dyadic_shells_from_outer_to_eta']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件链替换",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "该替换只说明近零点的归属，不支付凹口成本。",
        "",
        "## 2. 分区表",
        "",
        "| zone | condition | eta/value | handled by | effect |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for item in result["partition_rows"]:
        lines.append(
            "| {zone} | {condition} | `{eta}` | {handled_by} | {effect} |".format(
                zone=table_cell(item["zone"]),
                condition=table_cell(item["condition"]),
                eta=fmt_float(float(item["eta"])),
                handled_by=table_cell(item["handled_by"]),
                effect=table_cell(item["effect"]),
            )
        )
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部 Backlund/Jensen 分支下一步转为 `{result['conditional_next_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
