#!/usr/bin/env python3
"""Prime Matrix B=3 零点邻近凹口成本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zero_proximity_indentation_cost_router.py

输出：
  docs/monograph/prime-matrix-b3-zero-proximity-indentation-cost-router.json
  docs/monograph/prime-matrix-b3-zero-proximity-indentation-cost-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zero-proximity-indentation-cost-router.md"

OLD_ATOM = "BacklundZeroProximityIndentationCostLedger"
EXTERNAL_CLOSED_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
INTERNAL_SHIFT_ATOM = "BacklundZeroAvoidingShiftWithoutJumpLedger"
INTERNAL_CANCELLATION_ATOM = "BacklundNearZeroJumpCancellationSubHalfLedger"
CS8_ATOM = "BacklundCS8SlackAfterBridgeLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_ZERO_COUNT = 16.0
PER_ZERO_NAIVE_COST = math.pi
NAIVE_INDENT_COEFFICIENT = C_ZERO_COUNT * PER_ZERO_NAIVE_COST
AVAILABLE_STABILITY_MARGIN = 0.078125
NAIVE_MARGIN_DEFICIT = NAIVE_INDENT_COEFFICIENT - AVAILABLE_STABILITY_MARGIN

EXTERNAL_SOURCES = [
    {
        "name": "Trudgian 2012 Backlund method",
        "url": "https://doi.org/10.1090/S0025-5718-2011-02537-8",
        "claim": "Explicit S(T) bounds are obtained by Backlund/Rosser-McCurley style contour handling.",
    },
    {
        "name": "Trudgian 2014 Backlund method II",
        "url": "https://arxiv.org/abs/1208.5846",
        "claim": "External reference for modern explicit Backlund argument bounds and zero-handling conventions.",
    },
]


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


def internal_replacement() -> str:
    """写出内部自足路线的替换包。"""
    return f"({INTERNAL_SHIFT_ATOM} OR {INTERNAL_CANCELLATION_ATOM})"


def replace_external(text: str) -> str:
    """替换外部凹口成本原子。"""
    return text.replace(OLD_ATOM, EXTERNAL_CLOSED_ATOM)


def cost_rows() -> list[dict[str, Any]]:
    """生成凹口成本压力表。"""
    return [
        {
            "item": "Jensen zero-count coefficient",
            "value": C_ZERO_COUNT,
            "meaning": "近零点数量的当前粗上界。",
        },
        {
            "item": "naive per-zero indentation cost",
            "value": PER_ZERO_NAIVE_COST,
            "meaning": "每个近零点按 pi 级跳变粗付的成本。",
        },
        {
            "item": "naive indentation coefficient",
            "value": NAIVE_INDENT_COEFFICIENT,
            "meaning": "只靠数量粗付会产生的 log(T) 系数。",
        },
        {
            "item": "available stability margin",
            "value": AVAILABLE_STABILITY_MARGIN,
            "meaning": "窗口尺度后距离 1/2 稳定预算的剩余。",
        },
        {
            "item": "naive deficit",
            "value": NAIVE_MARGIN_DEFICIT,
            "meaning": "说明内部路线必须有零避让或跳变抵消，不能用粗付费。",
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
    """生成零点邻近凹口成本判定表。"""
    external_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    window_ready = bool(previous.get("variation_window_scale_external_closed"))
    endpoint_convention_available = ENDPOINT_ATOM in external_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    naive_fails = NAIVE_INDENT_COEFFICIENT > AVAILABLE_STABILITY_MARGIN
    external_closed = active and window_ready and endpoint_convention_available and guard
    return [
        row(
            "ZeroProximityIndentationCostGateActive",
            active,
            False,
            "外部 Backlund/Jensen 分支当前最窄点是近零点凹口成本。",
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
            "VariationWindowScaleAvailable",
            window_ready,
            True,
            "窗口尺度已给出 0.078125 的半稳定余量。",
            "BacklundVariationWindowScaleClosedH1Over512C192",
        ),
        row(
            "NaiveMultiplicityIndentCostFails",
            naive_fails,
            True,
            "若每个近零点粗付 pi，系数约 50.265，远超剩余余量；内部路线不能这样闭合。",
            internal_replacement(),
        ),
        row(
            "EndpointConventionAvailableButNotQuantitative",
            endpoint_convention_available,
            True,
            "端点避零 convention 解决定义与极限，不自动给出局部跳变预算。",
            ENDPOINT_ATOM,
        ),
        row(
            "ExternalBacklundIndentationCostAccepted",
            external_closed,
            False,
            "若接受经典 Backlund 轮廓缩进处理作为外部引理，本凹口成本门可关闭。",
            EXTERNAL_CLOSED_ATOM,
        ),
        row(
            "SelfContainedIndentCostStillOpen",
            False,
            False,
            "完全自足路线必须证明零避让不跨越跳变，或证明近零跳变有额外抵消。",
            internal_replacement(),
        ),
        row(
            "CS8SlackNext",
            False,
            False,
            "外部凹口成本接受后，下一步统一验收 C_S=8 余量。",
            CS8_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点邻近凹口成本路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    external_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ExternalBacklundIndentationCostAccepted"
    )
    latest_external = replace_external(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "b3_zero_proximity_indentation_cost_router",
        "status": "zero_proximity_indentation_cost_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_proximity_indentation_cost_external_closed": external_closed,
        "zero_proximity_indentation_cost_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "naive_indentation_coefficient": NAIVE_INDENT_COEFFICIENT,
        "available_stability_margin": AVAILABLE_STABILITY_MARGIN,
        "naive_margin_deficit": NAIVE_MARGIN_DEFICIT,
        "replacement_self_contained": {OLD_ATOM: internal_replacement()},
        "replacement_external": {OLD_ATOM: EXTERNAL_CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": CS8_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "external_sources": EXTERNAL_SOURCES,
        "cost_rows": cost_rows(),
        "plain_conclusion": (
            "近零点凹口成本在外部 Backlund 分支中可由经典轮廓缩进引理接受关闭；"
            "但自足路线没有闭合。关键障碍是朴素按零点个数付费给出约 50.265 的 log(T) 系数，"
            "远超当前 0.078125 的稳定余量，必须另证零避让或跳变抵消。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_repl = next(iter(result["replacement_self_contained"].items()))
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 零点邻近凹口成本路由器",
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
            "zero_proximity_indentation_cost_external_closed="
            f"{fmt_bool(result['zero_proximity_indentation_cost_external_closed'])}"
        ),
        (
            "zero_proximity_indentation_cost_self_contained_closed="
            f"{fmt_bool(result['zero_proximity_indentation_cost_self_contained_closed'])}"
        ),
        f"naive_indentation_coefficient={fmt_float(result['naive_indentation_coefficient'])}",
        f"available_stability_margin={fmt_float(result['available_stability_margin'])}",
        f"naive_margin_deficit={fmt_float(result['naive_margin_deficit'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拆分律",
        "",
        "完全自足路线：",
        "",
        "```text",
        self_repl[0],
        "  =>",
        self_repl[1],
        "```",
        "",
        "外部 Backlund 路线：",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 成本压力",
        "",
        "| item | value | meaning |",
        "| --- | ---: | --- |",
    ]
    for item in result["cost_rows"]:
        lines.append(
            "| {item} | `{value}` | {meaning} |".format(
                item=table_cell(item["item"]),
                value=fmt_float(float(item["value"])),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 外部来源",
            "",
            "| source | url | claim used |",
            "| --- | --- | --- |",
        ]
    )
    for source in result["external_sources"]:
        lines.append(
            "| {name} | {url} | {claim} |".format(
                name=table_cell(source["name"]),
                url=table_cell(source["url"]),
                claim=table_cell(source["claim"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 最新输入基",
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
            "## 6. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部 Backlund 分支下一步转为 `{result['conditional_next_priority']}`。"
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
