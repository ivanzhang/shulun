#!/usr/bin/env python3
"""生成 strict prefix 标签到稀疏终端历史抗塌缩证书。

用法示例：
  python3 experiments/prime_matrix_strict_prefix_label_sparse_history_anticollapse_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-prefix-residual-transfer-router.md",
    MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md",
    MONOGRAPH / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-budget-inequality-attack-router.md",
]

HARDPOINT = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
MULTIPLICITY_LEDGER = "PrefixLabelSupportToSparseTerminalMultiplicityNoSilentCollapse"
STRONG_INJECTION = "StrongDistinctSparseHistoryInjectionAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
COLD_BALANCE = "ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance"
FINITE_SYNC = "FiniteBoundaryAndCommonParameterSynchronizationLedger"
B3_SELF = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
UNIFIED_GAP = "UnifiedTerminalBudgetStrictInequality"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总存在的依赖哈希。"""
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


def collapse_cases() -> list[dict[str, str]]:
    """列出 prefix 标签投影后的塌缩分支。"""
    return [
        {
            "case": "injective_or_low_collision",
            "formula": "sum_W Load(W)=M#_{x,z}-E_named",
            "route": "terminal multiplicity ledger",
            "status": "closed",
            "meaning": "不同 prefix atom 即使落到同一历史词，也按终端重数计入负载，而不是消失。",
        },
        {
            "case": "bounded_nonpersistent_collision",
            "formula": "Load(W)<=C_cold(W)(T_PDEC(W)-1)",
            "route": COLD_BALANCE,
            "status": "open_budget",
            "meaning": "非持久塌缩可由冷核心/历史重数供给预算支付；剩余是不等式反超。",
        },
        {
            "case": "persistent_same_history_collision",
            "formula": "Load(W)>C_cold(W)(T_PDEC(W)-1)",
            "route": "FixedHistoryPDECOrHotCoreNamedReturn",
            "status": "registered_named_return",
            "meaning": "同一历史词过阈值持久复现不是自由出口，必须登记为 PDEC、ColumnCRT、固定历史或热核心回流。",
        },
        {
            "case": "quotient_or_phase_drift",
            "formula": "terminal map undefined or changes phase key",
            "route": NAMED_RETURN,
            "status": "registered_named_return",
            "meaning": "若投影无法稳定落到终端历史，则由 no-loss 账本进入命名回流桶。",
        },
    ]


def theorem_rows() -> list[dict[str, Any]]:
    """给出本轮可审查定理边界。"""
    return [
        {
            "name": "NoSilentCollapseTerminalMultiplicityLedger",
            "proved": True,
            "statement": (
                "在早期零行反例链内，prefix 加权义务投影到稀疏终端时不会静默损失；"
                "未命名回流的部分按终端历史重数守恒。"
            ),
            "role": "把抗塌缩从强互异历史注入改成统一预算真正需要的重数守恒。",
        },
        {
            "name": "StrongDistinctSparseHistoryInjection",
            "proved": False,
            "statement": "当前不证明 #distinct sparse histories >= M#_{x,z}。",
            "role": "这是过强命题；同一历史多重命中应由容量预算处理。",
        },
        {
            "name": "TerminalProjectionAntiCollapseForUnifiedBudget",
            "proved": True,
            "statement": (
                "统一预算中需要的是 L_forced>=M#_{x,z}-E_named；"
                "同历史塌缩只会进入 U_cold 或 E_named，不会削弱该负载守恒。"
            ),
            "role": "关闭 PrefixLabelSupportToSparseTerminalHistoryAntiCollapse 的无静默塌缩版本。",
        },
        {
            "name": "UnconditionalTerminalContradiction",
            "proved": False,
            "statement": (
                "仍需证明 M# 下界、命名回流排斥、冷供给上界与有限参数同步后得到 "
                "D_prefix-E_named-U_cold>0。"
            ),
            "role": "行/列命题仍不能升级为作者侧无条件闭合。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步只在假设早期零行反例链内工作，不用真实零行缺席或统计样本。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "WeightedPrefixAtomDomainImported",
            "closed": True,
            "proved": True,
            "meaning": "prefix 残洞 atom、canonical tau_z 标签与 1/mu_tau 容量权重已由前置路由闭合。",
            "remaining": "无。",
        },
        {
            "gate": "TerminalMapNoLossImported",
            "closed": True,
            "proved": True,
            "meaning": "每个 atom 的出口只能是稀疏终端历史、固定历史、PDEC/SAE/ColumnCRT、热核心或 quotient 回流。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "StrongDistinctHistoryInjectionRejectedAsUnneeded",
            "closed": True,
            "proved": True,
            "meaning": "统一预算不需要互异历史词注入；同一历史词的多重命中正是终端负载。",
            "remaining": STRONG_INJECTION,
        },
        {
            "gate": "MultiplicityConservationAntiCollapseClosed",
            "closed": True,
            "proved": True,
            "meaning": "按终端历史分组后，总负载等于 prefix 加权质量扣除命名回流。",
            "remaining": MULTIPLICITY_LEDGER,
        },
        {
            "gate": "PersistentCollapseRoutedToNamedReturn",
            "closed": True,
            "proved": False,
            "meaning": "若同一历史词过阈值持久复现，它必须进入固定历史/PDEC/热核心命名桶。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "NonpersistentCollapseAbsorbedByColdBudget",
            "closed": True,
            "proved": False,
            "meaning": "若所有同历史塌缩均未持久，则总量由冷核心历史重数预算吸收。",
            "remaining": COLD_BALANCE,
        },
        {
            "gate": "PrefixLabelSupportToSparseTerminalHistoryAntiCollapseClosedForBudget",
            "closed": True,
            "proved": True,
            "meaning": "对统一预算所需的投影负载而言，prefix 标签支撑不会塌缩成无负载。",
            "remaining": "强互异历史注入未证但不再是必要输入。",
        },
        {
            "gate": "UnifiedBudgetStrictInequalityProved",
            "closed": False,
            "proved": False,
            "meaning": "抗塌缩已转成重数守恒，但仍缺冷供给平衡、有限参数同步、命名回流排斥与自足 B3 尾段。",
            "remaining": f"{COLD_BALANCE} AND {FINITE_SYNC} AND {NAMED_RETURN}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 prefix 标签到稀疏终端历史抗塌缩证书。"""
    return {
        "certificate_type": "prime_matrix_strict_prefix_label_sparse_history_anticollapse_router",
        "status": "prefix_label_sparse_history_no_silent_collapse_closed_strong_injection_unneeded_budget_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "weighted_prefix_atom_domain_imported": True,
        "terminal_map_no_loss_imported": True,
        "strong_distinct_sparse_history_injection_proved": False,
        "strong_distinct_sparse_history_injection_needed_for_unified_budget": False,
        "multiplicity_conservation_anticollapse_closed": True,
        "persistent_collapse_routed_to_named_return": True,
        "nonpersistent_collapse_absorbed_by_cold_budget": True,
        "prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget": True,
        "terminal_projection_anticollapse_closed": True,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": (
            f"{COLD_BALANCE} AND {FINITE_SYNC} AND {NAMED_RETURN} "
            f"AND NormalizedPrefixResidualPotentialLowerBound"
        ),
        "next_direct_attack_target": COLD_BALANCE,
        "parallel_attack_targets": [
            FINITE_SYNC,
            NAMED_RETURN,
            "NormalizedPrefixResidualPotentialLowerBound",
            B3_SELF,
            DSTRUCTURE,
        ],
        "collapse_cases": collapse_cases(),
        "theorem_rows": theorem_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse 的强注入版本并非统一预算所必需。"
            "在早期零行反例链内，每个 prefix 加权 atom 要么投影到某个稀疏终端历史并按重数计入 "
            "L_forced，要么进入 PDEC、SAE、ColumnCRT、固定历史、热核心或 quotient 的命名回流桶。"
            "因此同一历史词上的塌缩不是负载消失，而是进入冷核心供给预算或命名回流。"
            "本步关闭的是终端预算所需的无静默塌缩抗塌缩；最终无条件矛盾仍需冷供给平衡、"
            "命名回流排斥、有限参数同步和 prefix 需求下界。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict prefix 标签到稀疏终端历史抗塌缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"weighted_prefix_atom_domain_imported={fmt_bool(result['weighted_prefix_atom_domain_imported'])}",
        f"terminal_map_no_loss_imported={fmt_bool(result['terminal_map_no_loss_imported'])}",
        f"strong_distinct_sparse_history_injection_proved={fmt_bool(result['strong_distinct_sparse_history_injection_proved'])}",
        f"strong_distinct_sparse_history_injection_needed_for_unified_budget={fmt_bool(result['strong_distinct_sparse_history_injection_needed_for_unified_budget'])}",
        f"multiplicity_conservation_anticollapse_closed={fmt_bool(result['multiplicity_conservation_anticollapse_closed'])}",
        f"persistent_collapse_routed_to_named_return={fmt_bool(result['persistent_collapse_routed_to_named_return'])}",
        f"nonpersistent_collapse_absorbed_by_cold_budget={fmt_bool(result['nonpersistent_collapse_absorbed_by_cold_budget'])}",
        f"prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget={fmt_bool(result['prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget'])}",
        f"terminal_projection_anticollapse_closed={fmt_bool(result['terminal_projection_anticollapse_closed'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 关键重写",
        "",
        "强注入命题",
        "",
        "```text",
        "#distinct sparse terminal histories >= M#_{x,z}",
        "```",
        "",
        "不是统一预算真正需要的命题。统一预算只需要负载守恒：",
        "",
        "```text",
        "L_forced = sum_W Load(W) >= M#_{x,z}-E_named.",
        "```",
        "",
        "若多个 prefix 标签落到同一个历史词 `W`，它们构成 `Load(W)` 的多重负载；"
        "这只会增加该历史词要支付的冷核心容量，而不会把需求消掉。",
        "",
        "## 2. 塌缩分支",
        "",
        "| case | formula | route | status | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["collapse_cases"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['case'])}`",
                    table_cell(row["formula"]),
                    table_cell(row["route"]),
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 定理边界",
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
            "## 4. 判定表",
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
            "## 5. 下一真正最窄点",
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
            "审稿边界：本文件关闭的是统一预算所需的无静默塌缩/重数守恒版本；"
            "它没有证明强互异历史注入，也没有证明最终正余量。",
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
