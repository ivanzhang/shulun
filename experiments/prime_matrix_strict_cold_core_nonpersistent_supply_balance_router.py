#!/usr/bin/env python3
"""生成 strict 冷核心非持久供给与 Lambda 平衡证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_core_nonpersistent_supply_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.md",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
    MONOGRAPH / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.md",
    MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-budget-inequality-attack-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md",
]

COLD_BALANCE = "ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance"
MARGIN = "SingleParameterTerminalBudgetMarginLedger"
PREFIX_DEMAND = "NormalizedPrefixResidualPotentialLowerBound"
FINITE_SYNC = "FiniteBoundaryAndCommonParameterSynchronizationLedger"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
B3_SELF = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
UNIFIED_GAP = "UnifiedTerminalBudgetStrictInequality"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def balance_components() -> list[dict[str, str]]:
    """列出同参数冷供给平衡组件。"""
    return [
        {
            "component": "demand",
            "formula": "D_prefix=((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)",
            "discipline": "same z,D and same lower-weight convention",
            "status": "open_margin_input",
        },
        {
            "component": "named deduction",
            "formula": "E_named=E_PDEC+E_SAE+E_ColumnCRT+E_hot+E_fixed+E_quotient",
            "discipline": "same return alphabet, no hidden exit",
            "status": "registered_open",
        },
        {
            "component": "cold supply",
            "formula": "U_cold<=sum_W (T_PDEC(W)-1) C_core(W)",
            "discipline": "same Lambda schedule and same PDEC threshold",
            "status": "upper_envelope_closed",
        },
        {
            "component": "strict margin",
            "formula": "D_prefix-E_named-U_cold>0",
            "discipline": "all three terms evaluated under one parameter ledger",
            "status": "open_positive_margin",
        },
    ]


def tradeoff_rows() -> list[dict[str, str]]:
    """列出 Lambda/阈值调节的结构性二分。"""
    return [
        {
            "knob": "Lambda_i smaller",
            "gain": "history alphabet A_i<=8 Lambda_i^2 shrinks",
            "cost": "more core windows cross hot threshold and enter E_named",
            "no_free_lunch": "cannot lower U_cold without increasing named-return obligations.",
        },
        {
            "knob": "Lambda_i larger",
            "gain": "fewer hot-core returns after coarser cold classification",
            "cost": "history alphabet and U_cold grow at least through product A_i",
            "no_free_lunch": "cannot suppress E_named by moving mass into an unbounded cold budget.",
        },
        {
            "knob": "T_PDEC(W) larger",
            "gain": "fewer histories become persistent PDEC",
            "cost": "nonpersistent allowance (T_PDEC(W)-1)C_core(W) grows",
            "no_free_lunch": "raising persistence threshold weakens the desired strict margin.",
        },
        {
            "knob": "T_PDEC(W) smaller",
            "gain": "cold supply allowance decreases",
            "cost": "more histories become fixed-history PDEC or ColumnCRT named returns",
            "no_free_lunch": "the saved supply reappears as E_named unless that return is excluded.",
        },
    ]


def theorem_rows() -> list[dict[str, Any]]:
    """给出本轮可审查定理边界。"""
    return [
        {
            "name": "SameParameterColdSupplyLedger",
            "proved": True,
            "statement": (
                "冷供给、历史数、PDEC 阈值、命名扣除与 prefix demand 必须在同一 z,D,Lambda,T 账本下比较。"
            ),
            "role": "禁止用不同参数口径分别优化需求和供给。",
        },
        {
            "name": "AdaptiveLambdaNoFreeLunchDichotomy",
            "proved": True,
            "statement": (
                "调小 Lambda 或阈值会增加命名回流，调大 Lambda 或阈值会增加 U_cold；"
                "两类变化都必须进入同一个余量式。"
            ),
            "role": "把调参自由度转成显式预算守恒，而不是新出口。",
        },
        {
            "name": "ColdBalancePositiveMargin",
            "proved": False,
            "statement": "尚未证明 D_prefix-E_named-U_cold>0。",
            "role": "这是反例链与真实链终端矛盾的剩余标量目标。",
        },
    ]


def decision_rows(anticollapse: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    anticollapse_closed = anticollapse.get("terminal_projection_anticollapse_closed") is True
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只在早期零行反例链内比较终端需求与冷供给。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "TerminalNoSilentCollapseImported",
            "closed": anticollapse_closed,
            "proved": anticollapse_closed,
            "meaning": "prefix 标签投影到稀疏终端历史时按重数守恒，未投影部分进入命名回流。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "ColdSupplyEnvelopeClosed",
            "closed": True,
            "proved": True,
            "meaning": "非持久冷供给可统一写成 sum_W (T_PDEC(W)-1)C_core(W)。",
            "remaining": COLD_BALANCE,
        },
        {
            "gate": "AdaptiveLambdaDisciplineClosed",
            "closed": True,
            "proved": True,
            "meaning": "Lambda 与 PDEC 阈值调节不能作为自由优化，必须同步进入 E_named 或 U_cold。",
            "remaining": MARGIN,
        },
        {
            "gate": "SingleParameterMarginLedgerClosed",
            "closed": True,
            "proved": False,
            "meaning": "终局矛盾已固定为同参数余量 D_prefix-E_named-U_cold>0。",
            "remaining": f"{PREFIX_DEMAND} AND {FINITE_SYNC} AND {NAMED_RETURN}",
        },
        {
            "gate": "ColdBalancePositiveMarginProved",
            "closed": False,
            "proved": False,
            "meaning": "当前仍未证明该余量严格为正。",
            "remaining": f"{MARGIN} AND {HOT_CORE} AND {FIXED_HISTORY}",
        },
        {
            "gate": "UnifiedBudgetStrictInequalityProved",
            "closed": False,
            "proved": False,
            "meaning": "同参数纪律已闭合，但最终供需反超还缺正下界、命名回流排斥和有限同步。",
            "remaining": UNIFIED_GAP,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造冷核心非持久供给平衡证书。"""
    anticollapse = load_json(MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    anticollapse_closed = anticollapse.get("terminal_projection_anticollapse_closed") is True
    return {
        "certificate_type": "prime_matrix_strict_cold_core_nonpersistent_supply_balance_router",
        "status": "cold_core_nonpersistent_supply_balance_same_parameter_ledger_closed_positive_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "terminal_no_silent_collapse_imported": anticollapse_closed,
        "cold_supply_upper_envelope_closed": True,
        "same_parameter_lambda_schedule_closed": True,
        "adaptive_lambda_no_free_lunch_dichotomy_closed": True,
        "single_parameter_margin_ledger_closed": True,
        "cold_core_nonpersistent_supply_upper_bound_and_adaptive_lambda_balance_proved": False,
        "cold_supply_upper_bound_beats_load": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLD_BALANCE,
        "hardpoint_after_router": f"{MARGIN} AND {PREFIX_DEMAND} AND {FINITE_SYNC} AND {NAMED_RETURN}",
        "next_direct_attack_target": MARGIN,
        "parallel_attack_targets": [PREFIX_DEMAND, FINITE_SYNC, NAMED_RETURN, HOT_CORE, FIXED_HISTORY, B3_SELF, DSTRUCTURE],
        "balance_components": balance_components(),
        "tradeoff_rows": tradeoff_rows(),
        "theorem_rows": theorem_rows(),
        "decision_rows": decision_rows(anticollapse),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "冷核心非持久供给侧的自由调参已经被锁入同一个终端预算余量。"
            "缩小 Lambda 或 PDEC 阈值会减少 U_cold，但会把更多质量推入命名回流；"
            "放大 Lambda 或阈值会减少回流，却增大历史字母表或单历史允许容量。"
            "因此冷供给平衡不再是独立黑箱，而是同参数标量 "
            "D_prefix-E_named-U_cold>0 的正余量问题。当前仍未证明该余量为正，"
            "所以无条件闭合仍未达成。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 冷核心非持久供给与 Lambda 平衡路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_no_silent_collapse_imported={fmt_bool(result['terminal_no_silent_collapse_imported'])}",
        f"cold_supply_upper_envelope_closed={fmt_bool(result['cold_supply_upper_envelope_closed'])}",
        f"same_parameter_lambda_schedule_closed={fmt_bool(result['same_parameter_lambda_schedule_closed'])}",
        f"adaptive_lambda_no_free_lunch_dichotomy_closed={fmt_bool(result['adaptive_lambda_no_free_lunch_dichotomy_closed'])}",
        f"single_parameter_margin_ledger_closed={fmt_bool(result['single_parameter_margin_ledger_closed'])}",
        f"cold_core_nonpersistent_supply_upper_bound_and_adaptive_lambda_balance_proved={fmt_bool(result['cold_core_nonpersistent_supply_upper_bound_and_adaptive_lambda_balance_proved'])}",
        f"cold_supply_upper_bound_beats_load={fmt_bool(result['cold_supply_upper_bound_beats_load'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同参数余量",
        "",
        "当前终端矛盾只允许在同一组参数下比较：",
        "",
        "```text",
        "D_prefix = ((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)",
        "U_cold  <= sum_W (T_PDEC(W)-1) C_core(W)",
        "contradiction if D_prefix - E_named - U_cold > 0.",
        "```",
        "",
        "不能用一组参数放大 `D_prefix`，再用另一组参数缩小 `U_cold`。",
        "",
        "## 2. 组件表",
        "",
        "| component | formula | discipline | status |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["balance_components"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['component'])}`",
                    table_cell(row["formula"]),
                    table_cell(row["discipline"]),
                    f"`{table_cell(row['status'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 调参二分",
            "",
            "| knob | gain | cost | no_free_lunch |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["tradeoff_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['knob'])}`",
                    table_cell(row["gain"]),
                    table_cell(row["cost"]),
                    table_cell(row["no_free_lunch"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 定理边界",
            "",
            "| name | proved | statement | role |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["statement"]),
                    table_cell(row["role"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本文件关闭冷供给与 Lambda 调参纪律；尚未证明统一预算正余量。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"status={result['status']}")


if __name__ == "__main__":
    main()
