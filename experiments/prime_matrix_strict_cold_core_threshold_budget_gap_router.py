#!/usr/bin/env python3
"""生成 strict 冷核心阈值预算缺口路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_core_threshold_budget_gap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-core-threshold-budget-gap-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
]

COLD_GAP = "ColdCoreThresholdBudgetGapComparison"
COLD_SUPPLY = "ColdCoreNonpersistentSupplyUpperBound"
FORCED_LOAD = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
ADAPTIVE_LAMBDA = "AdaptiveLambdaBalanceForIteratedCoreDensity"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY_PDEC = "FixedTypeHistoryPDECExclusion"
UNIFIED_UPDATE = "UnifiedContradictionFieldTerminalHistorySupplyDemandUpdate"


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


def lemmas() -> list[dict[str, str]]:
    """列出冷核心预算缺口引理。"""
    return [
        {
            "name": "cold_supply_upper_bound",
            "formula": "U_cold <= sum_{W cold} (T_PDEC(W)-1) C_core(W).",
            "status": "closed",
            "meaning": "冷核心非持久供给有显式上界。",
        },
        {
            "name": "history_sum_envelope",
            "formula": "sum_{W cold} <= sum_{r<=R} prod_{i<=r} A_{Lambda_i}, with A_{Lambda_i}<=8Lambda_i^2.",
            "status": "closed",
            "meaning": "历史词计数已进入供给预算。",
        },
        {
            "name": "cold_budget_contradiction_criterion",
            "formula": "If L_forced > U_cold, then early-zero-row terminal obligations exceed all nonpersistent cold supply.",
            "status": "closed_criterion",
            "meaning": "这是当前最直接的供需矛盾口。",
        },
        {
            "name": "not_gap_then_named_escape",
            "formula": "If the gap fails, then either L_forced is too small, cold supply is too large, or hot/PDEC escape occurred.",
            "status": "closed_dichotomy",
            "meaning": "预算未反超时，失败原因也被命名，不允许成为自由缺口。",
        },
        {
            "name": "cold_supply_too_large_route",
            "formula": "Large U_cold must come from large history count, large C_core(W), or large T_PDEC(W).",
            "status": "closed_reduction",
            "meaning": "供给过大被拆成 Lambda、核心阈值、持久阈值三类具体输入。",
        },
        {
            "name": "terminal_history_supply_demand_field",
            "formula": "Early zero row forces demand; cold sparse histories provide finite supply; hot histories return to PDEC/LCM.",
            "status": "registered_unified_field",
            "meaning": "该供需结构已作为新矛盾因子接入统一矛盾场。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的冷核心 SAE 预算分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ColdSupplyUpperBoundClosed",
            "closed": True,
            "proved": True,
            "meaning": "非持久冷历史供给 `U_cold` 已有显式求和上界。",
            "remaining": COLD_SUPPLY,
        },
        {
            "gate": "SupplyDemandContradictionCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "`L_forced>U_cold` 时形成反例链供需矛盾。",
            "remaining": FORCED_LOAD,
        },
        {
            "gate": "FailureReasonsNamed",
            "closed": True,
            "proved": True,
            "meaning": "预算未反超时只能归因于需求弱、冷供给大、热核心或持久 PDEC。",
            "remaining": f"{FORCED_LOAD} OR {COLD_SUPPLY} OR {HOT_CORE} OR {FIXED_HISTORY_PDEC}",
        },
        {
            "gate": "ColdCoreBudgetGapProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 `L_forced` 严格超过 `U_cold`。",
            "remaining": f"{FORCED_LOAD} AND {COLD_SUPPLY} AND {ADAPTIVE_LAMBDA}",
        },
        {
            "gate": "UnifiedFieldUpdatedButNotClosed",
            "closed": True,
            "proved": False,
            "meaning": "新供需因子已进入统一矛盾场，但尚未产生最终直接矛盾。",
            "remaining": UNIFIED_UPDATE,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_cold_core_threshold_budget_gap_router",
        "status": "cold_core_budget_gap_reduced_to_forced_load_vs_nonpersistent_supply_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "cold_supply_upper_bound_closed": True,
        "history_sum_envelope_closed": True,
        "cold_budget_contradiction_criterion_closed": True,
        "failure_reasons_named": True,
        "unified_field_terminal_history_factor_registered": True,
        "cold_core_threshold_budget_gap_proved": False,
        "forced_load_lower_bound_proved": False,
        "cold_supply_upper_bound_beats_load": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": FORCED_LOAD,
        "secondary_attack_target": COLD_SUPPLY,
        "parallel_targets": [ADAPTIVE_LAMBDA, HOT_CORE, FIXED_HISTORY_PDEC, UNIFIED_UPDATE],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "冷核心预算缺口已经压成单一供需不等式。非持久冷历史的总供给 "
            "U_cold 至多为 sum_W (T_PDEC(W)-1) C_core(W)，历史数由有限深度和 "
            "有限字母表控制。若早期零行反例链强制终端负载 L_forced 大于 U_cold，"
            "则非持久冷供给无法支付反例义务，形成直接矛盾。若该不等式失败，"
            "失败原因只能是需求下界不足、冷供给预算过大、热核心回流或固定历史 PDEC。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 冷核心阈值预算缺口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cold_supply_upper_bound_closed={fmt_bool(result['cold_supply_upper_bound_closed'])}",
        f"history_sum_envelope_closed={fmt_bool(result['history_sum_envelope_closed'])}",
        f"cold_budget_contradiction_criterion_closed={fmt_bool(result['cold_budget_contradiction_criterion_closed'])}",
        f"failure_reasons_named={fmt_bool(result['failure_reasons_named'])}",
        f"unified_field_terminal_history_factor_registered={fmt_bool(result['unified_field_terminal_history_factor_registered'])}",
        f"cold_core_threshold_budget_gap_proved={fmt_bool(result['cold_core_threshold_budget_gap_proved'])}",
        f"forced_load_lower_bound_proved={fmt_bool(result['forced_load_lower_bound_proved'])}",
        f"cold_supply_upper_bound_beats_load={fmt_bool(result['cold_supply_upper_bound_beats_load'])}",
        f"terminal_core_hot_divisor_window_excluded={fmt_bool(result['terminal_core_hot_divisor_window_excluded'])}",
        f"fixed_type_history_pdec_excluded={fmt_bool(result['fixed_type_history_pdec_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 供给上界",
        "",
        "非持久冷历史供给满足",
        "",
        "```text",
        "U_cold <= sum_W (T_PDEC(W)-1) C_core(W).",
        "```",
        "",
        "历史词数量由",
        "",
        "```text",
        "#W <= sum_{r<=R} prod_{i<=r} A_{Lambda_i},",
        "A_{Lambda_i} <= 8 Lambda_i^2",
        "```",
        "",
        "控制。",
        "",
        "## 2. 供需矛盾口",
        "",
        "当前最窄矛盾判据是",
        "",
        "```text",
        "L_forced > U_cold.",
        "```",
        "",
        "若成立，早期零行反例链要求的终端义务超过所有非持久冷历史可提供的供给。",
        "",
        "## 3. 引理表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["lemmas"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
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
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一步最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并列供给侧目标：",
            "",
            "```text",
            result["secondary_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步闭合冷核心预算公式和供需判据；未证明需求反超供给，也未排斥热核心或固定历史 PDEC。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
