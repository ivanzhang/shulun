#!/usr/bin/env python3
"""生成 strict 统一预算严格不等式主攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_unified_budget_inequality_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unified-budget-inequality-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-unified-budget-inequality-attack-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unified-budget-inequality-attack-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md",
    MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.md",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "claim-status-table.md",
]

UNIFIED_GAP = "UnifiedTerminalBudgetStrictInequality"
PREFIX_DEMAND = "PrefixDemandNumeratorSurplusLedger"
ANTICOLLAPSE = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
COLD_BALANCE = "ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance"
FINITE_SYNC = "FiniteBoundaryAndCommonParameterSynchronizationLedger"
B3_SELF = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
B3_EXTERNAL = "ExternalMertensDusartB3TVAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def normal_form_rows() -> list[dict[str, str]]:
    """列出严格预算不等式的同参数标准形。"""
    return [
        {
            "component": "prefix demand",
            "symbol": "D_prefix=((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)",
            "closed_part": "统一方程和容量乘子归一化已闭合。",
            "open_part": PREFIX_DEMAND,
        },
        {
            "component": "terminal projection",
            "symbol": "L_forced >= D_prefix-E_named",
            "closed_part": "no-loss 投影和命名回流字母表已闭合。",
            "open_part": ANTICOLLAPSE,
        },
        {
            "component": "cold supply",
            "symbol": "U_cold <= sum_W (T_PDEC(W)-1)C_core(W)",
            "closed_part": "非持久历史供给公式和冷/热分裂已闭合。",
            "open_part": COLD_BALANCE,
        },
        {
            "component": "strict gap",
            "symbol": "D_prefix-E_named-U_cold>0",
            "closed_part": "代数组合已闭合，若该式成立即 L_forced>U_cold。",
            "open_part": FINITE_SYNC,
        },
    ]


def attack_rows(
    b3_tv: dict[str, Any],
    forced_load: dict[str, Any],
    cold_core: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成当前攻击判定。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "统一预算只在假设早期零行反例链内比较需求与供给。",
            "remaining": "无。",
        },
        {
            "gate": "SameParameterNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "同一 z、D、Lambda schedule、PDEC 阈值下的预算标准形已固定为 D_prefix-E_named-U_cold>0。",
            "remaining": UNIFIED_GAP,
        },
        {
            "gate": "PrefixDemandExternalLaneAvailable",
            "closed": b3_tv.get("b3_tv_budget_conditional_external_closed") is True,
            "proved": False,
            "meaning": "接受外部 Mertens/Dusart 时，B3 TV 项可条件关闭；严格自足仍缺 Mertens 尾段。",
            "remaining": B3_SELF,
        },
        {
            "gate": "TerminalProjectionAntiCollapseClosed",
            "closed": forced_load.get("terminal_history_anticollapse_proved") is True,
            "proved": forced_load.get("terminal_history_anticollapse_proved") is True,
            "meaning": "当前仍需证明 prefix 标签支撑不会在 sparse terminal history 投影下大量塌缩。",
            "remaining": ANTICOLLAPSE,
        },
        {
            "gate": "ColdSupplyLambdaBalanceClosed",
            "closed": cold_core.get("cold_supply_upper_bound_beats_load") is True,
            "proved": cold_core.get("cold_supply_upper_bound_beats_load") is True,
            "meaning": "当前仍需给出冷核心阈值、历史数和 Lambda schedule 的同参数反超。",
            "remaining": COLD_BALANCE,
        },
        {
            "gate": "UnifiedBudgetStrictInequalityProved",
            "closed": False,
            "proved": False,
            "meaning": "需求下界、投影抗塌缩、命名扣除和冷供给上界尚未合成正余量。",
            "remaining": f"{ANTICOLLAPSE} AND {COLD_BALANCE} AND {FINITE_SYNC}",
        },
    ]


def theorem_rows() -> list[dict[str, Any]]:
    """给出本轮可审查定理边界。"""
    return [
        {
            "name": "UnifiedBudgetNormalFormTheorem",
            "proved": True,
            "statement": (
                "早期零行反例链的终端预算严格矛盾等价于同参数正余量 "
                "D_prefix-E_named-U_cold>0。"
            ),
            "role": "把统一预算从口头供需矛盾改写为单一标量不等式。",
        },
        {
            "name": "ExternalB3PrefixDemandLane",
            "proved": False,
            "statement": (
                "若接受外部 Mertens/Dusart 输入，prefix demand 的 B3/TV 部分可条件进入该标量式；"
                "严格自足版仍需内联 Mertens 尾段。"
            ),
            "role": "区分外部条件路线与严格自足路线。",
        },
        {
            "name": "UnconditionalUnifiedBudgetGap",
            "proved": False,
            "statement": (
                f"要证明 {UNIFIED_GAP}，还必须补齐 {ANTICOLLAPSE}、"
                f"{COLD_BALANCE} 与 {FINITE_SYNC}。"
            ),
            "role": "这是当前终端矛盾的真剩余输入基。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造统一预算严格不等式攻击证书。"""
    b3_tv = load_json(MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json")
    forced_load = load_json(MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json")
    cold_core = load_json(MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.json")
    return {
        "certificate_type": "prime_matrix_strict_unified_budget_inequality_attack_router",
        "status": "unified_budget_strict_inequality_normal_form_closed_margin_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "same_parameter_budget_normal_form_closed": True,
        "external_b3_prefix_demand_lane_available": b3_tv.get("b3_tv_budget_conditional_external_closed") is True,
        "strict_self_contained_prefix_demand_closed": b3_tv.get("b3_tv_budget_strict_self_contained_proved") is True,
        "terminal_projection_anticollapse_closed": forced_load.get("terminal_history_anticollapse_proved") is True,
        "cold_supply_lambda_balance_closed": cold_core.get("cold_supply_upper_bound_beats_load") is True,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ANTICOLLAPSE,
        "parallel_attack_targets": [COLD_BALANCE, FINITE_SYNC, B3_SELF, DSTRUCTURE],
        "normal_form_rows": normal_form_rows(),
        "theorem_rows": theorem_rows(),
        "attack_rows": attack_rows(b3_tv, forced_load, cold_core),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "统一预算严格不等式已压成同参数单标量余量：D_prefix-E_named-U_cold>0。"
            "外部 B3/TV 路线可条件供给 prefix demand，但终端投影抗塌缩和冷供给 Lambda 平衡仍未闭合。"
            "当前最窄结构硬点是 PrefixLabelSupportToSparseTerminalHistoryAntiCollapse。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 统一预算严格不等式主攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_parameter_budget_normal_form_closed={fmt_bool(result['same_parameter_budget_normal_form_closed'])}",
        f"external_b3_prefix_demand_lane_available={fmt_bool(result['external_b3_prefix_demand_lane_available'])}",
        f"strict_self_contained_prefix_demand_closed={fmt_bool(result['strict_self_contained_prefix_demand_closed'])}",
        f"terminal_projection_anticollapse_closed={fmt_bool(result['terminal_projection_anticollapse_closed'])}",
        f"cold_supply_lambda_balance_closed={fmt_bool(result['cold_supply_lambda_balance_closed'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 标准形",
        "",
        "```text",
        "D_prefix = ((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)",
        "L_forced >= D_prefix-E_named",
        "U_cold <= sum_W (T_PDEC(W)-1)C_core(W)",
        "terminal contradiction if D_prefix-E_named-U_cold > 0",
        "```",
        "",
        "| component | symbol | closed_part | open_part |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["normal_form_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['component'])}`",
                    table_cell(row["symbol"]),
                    table_cell(row["closed_part"]),
                    table_cell(row["open_part"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 定理边界",
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
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["attack_rows"]:
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
            "## 4. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本文件闭合统一预算的同参数标准形；尚未证明正余量，因此不能声明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"status={result['status']}")


if __name__ == "__main__":
    main()
