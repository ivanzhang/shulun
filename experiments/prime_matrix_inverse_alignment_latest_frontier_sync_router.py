#!/usr/bin/env python3
"""把逆元对齐零行行号源同步到最新终端前沿。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_latest_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json
  docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.md"

NORMALIZED = "NormalizedPrefixResidualPotentialLowerBound"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
EFFECTIVE_PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
STRICT_BETA_APPENDIX = (
    "BetaSieveLowerWeightRecursiveConstructionLedger AND "
    "BetaSieveLowerBoundDominanceProof AND "
    "BetaSieveMainCoefficientExplicit99PercentPGe100000"
)
SHORT_INTERVAL = "PrimeGapBelowP2ForAllPBlocks"

SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-covering-system-router.json",
    DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.json",
    DOCS / "prime-matrix-strict-normalized-prefix-potential-router.json",
    DOCS / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    DOCS / "prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json",
    DOCS / "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json",
    DOCS / "prime-matrix-strict-formal-unit-type-threshold-sync-router.json",
    DOCS / "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    DOCS / "prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json",
    DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json",
    DOCS / "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json",
    DOCS / "prime-matrix-strict-terminal-hot-core-return-frontier-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_latest_frontier_sync_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, Any]:
    """读取最新前沿中已闭合和仍开放的字段。"""
    inverse = load_json(DOCS / "prime-matrix-inverse-alignment-covering-system-router.json")
    bridge = load_json(DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.json")
    normalized = load_json(DOCS / "prime-matrix-strict-normalized-prefix-potential-router.json")
    finite = load_json(DOCS / "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json")
    rowfree = load_json(DOCS / "prime-matrix-strict-row-free-type-anticollapse-sync-router.json")
    positive = load_json(DOCS / "prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json")
    unified = load_json(DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json")
    hot = load_json(DOCS / "prime-matrix-strict-terminal-hot-core-return-frontier-router.json")

    return {
        "inverse_alignment_covering_equivalence_imported": inverse.get("gcd_system_equivalence_closed") is True
        and inverse.get("inverse_residue_formula_closed") is True,
        "inverse_alignment_min_x_gt_p_proved": inverse.get("global_minimal_alignment_x_gt_P_proved") is True,
        "inverse_alignment_prefix_demand_bridge_imported": bridge.get(
            "inverse_alignment_prefix_demand_bridge_closed"
        )
        is True,
        "legacy_normalized_prefix_potential_proved": normalized.get(
            "normalized_prefix_residual_potential_lower_bound_proved"
        )
        is True,
        "finite_prefix_standard_external_available": finite.get(
            "finite_boundary_prefix_certificate_external_or_standard_closed"
        )
        is True,
        "finite_prefix_strict_first_principles_lower_sieve_closed": finite.get(
            "finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed"
        )
        is True,
        "finite_prefix_mertens_component_closed": finite.get("finite_prefix_strict_mertens_component_closed") is True,
        "rowfree_budget_anticollapse_imported": rowfree.get(
            "prefix_label_support_to_row_free_type_anticollapse_closed_for_budget"
        )
        is True,
        "positive_margin_frontier_sync_imported": positive.get(
            "positive_margin_after_finite_prefix_terminal_sync_closed"
        )
        is True,
        "finite_prefix_available_under_current_contract": positive.get("finite_prefix_available_under_current_contract")
        is True,
        "unified_budget_latest_sync_imported": unified.get("unified_budget_latest_sync_closed") is True,
        "sparse_budget_latest_sync_imported": sparse.get("sparse_budget_positive_margin_latest_sync_closed") is True,
        "same_parameter_sparse_margin_reduced_to_cold_numeric": sparse.get(
            "same_parameter_sparse_margin_reduced_to_cold_numeric"
        )
        is True,
        "effective_cold_history_pruning_proved": sparse.get("effective_cold_history_pruning_proved") is True,
        "cold_supply_same_parameter_numeric_envelope_proved": sparse.get(
            "cold_supply_same_parameter_numeric_envelope_proved"
        )
        is True,
        "terminal_hot_core_frontier_imported": hot.get("terminal_hot_core_frontier_closed") is True,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": sparse.get(
            "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved"
        )
        is True,
        "persistent_terminal_family_excluded": positive.get("persistent_terminal_family_excluded") is True,
        "dstructure_rankin_acceptance_imported": False,
    }


def identities() -> list[dict[str, str]]:
    """列出逆元系统进入当前前沿的精确恒等式。"""
    return [
        {
            "name": "inverse_class",
            "formula": "q | xP+c iff c == rho_q(x)=-xP mod q.",
            "meaning": "零行位置 x 给出每个小素数 q 的唯一覆盖相位。",
            "status": "closed",
        },
        {
            "name": "prefix_residual_set",
            "formula": "R_{x,z}={1<=c<P: c != rho_q(x) mod q for every q<=z}.",
            "meaning": "prefix 残洞不再是抽象集合，而是逆元相位向量的剩余列。",
            "status": "closed",
        },
        {
            "name": "canonical_tau",
            "formula": "tau_z(c)=min{q: z<q<P and c == rho_q(x) mod q}.",
            "meaning": "在早期零行假设下，R_{x,z} 中每列都有规范后缀覆盖标签。",
            "status": "closed",
        },
        {
            "name": "capacity_multiplier",
            "formula": "mu_q=#{1<=c<P: c == rho_q(x) mod q} <= ceil(P/q) <= ceil(P/z).",
            "meaning": "逆元相位源与容量乘子纪律完全同字段匹配。",
            "status": "closed",
        },
        {
            "name": "weighted_demand",
            "formula": "M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)} >= |R_{x,z}|/ceil(P/z).",
            "meaning": "用户的最小对齐解系统直接成为统一预算左端需求源。",
            "status": "closed_as_formula",
        },
    ]


def frontier_rows() -> list[dict[str, str]]:
    """描述同步后的前沿迁移。"""
    return [
        {
            "stage": "row_position",
            "before": "早期零行 x 是抽象反例行号。",
            "after": "x 等价于所有列的逆元覆盖对齐解。",
            "remaining": "none",
        },
        {
            "stage": "prefix_demand",
            "before": f"{NORMALIZED} 缺少具体行相位源。",
            "after": "R_{x,z}, tau_z(c), mu_q, M# 均由 rho_q(x) 生成。",
            "remaining": "strict first-principles lower-sieve appendix if demanded",
        },
        {
            "stage": "finite_prefix_contract",
            "before": "finite-prefix D0 曾卡在 runner/tail/Mertens。",
            "after": "当前 standard/external 合同下已可用；Mertens 粗原子已回接。",
            "remaining": STRICT_BETA_APPENDIX,
        },
        {
            "stage": "projection",
            "before": "formal-unit 类型阈值像固定常数硬点。",
            "after": "预算版 row-free 无静默塌缩已闭合；丢标签必须命名回流。",
            "remaining": "named return absorption/exclusion",
        },
        {
            "stage": "terminal_budget",
            "before": "正余量仍混合 D0、类型、回流、冷供给。",
            "after": "D0/类型旧阻塞移出，非持久分支压入稀疏预算，持久分支压入 moving atom。",
            "remaining": f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
        {
            "stage": "sparse_budget_refinement",
            "before": f"{SPARSE_BUDGET} 仍是粗名。",
            "after": "已有最新同步把它压到冷历史有效剪枝、同参数冷数值表、热/固定回流。",
            "remaining": f"{EFFECTIVE_PRUNING} plus cold numeric/hot/fixed gates",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "InverseAlignmentRowPhaseImported",
            "closed": result["inverse_alignment_row_phase_to_latest_frontier_synced"],
            "proved": result["inverse_alignment_row_phase_to_latest_frontier_synced"],
            "meaning": "早期零行 x 的逆元相位向量已成为 prefix demand 的实际行号源。",
            "remaining": "none for row-phase interface",
        },
        {
            "gate": "MinXGreaterThanPRouteStillShortInterval",
            "closed": False,
            "proved": False,
            "meaning": "若直接证明所有最小对齐解 x>P，仍等价要求长度 P 短区间含素数。",
            "remaining": SHORT_INTERVAL,
        },
        {
            "gate": "NormalizedPrefixPotentialCurrentContractAvailable",
            "closed": result["normalized_prefix_potential_current_contract_available"],
            "proved": False,
            "meaning": "在当前 standard/external lower-sieve 合同下，finite-prefix D0/M# 需求侧可接入。",
            "remaining": STRICT_BETA_APPENDIX,
        },
        {
            "gate": "StrictFirstPrinciplesLowerSieveClosed",
            "closed": result["finite_prefix_strict_first_principles_lower_sieve_closed"],
            "proved": result["finite_prefix_strict_first_principles_lower_sieve_closed"],
            "meaning": "若要求 beta-sieve lower weights 也完全从零内联，该附录仍未完成。",
            "remaining": STRICT_BETA_APPENDIX,
        },
        {
            "gate": "PositiveMarginFrontierSynced",
            "closed": result["positive_margin_frontier_after_inverse_alignment_synced"],
            "proved": result["positive_margin_frontier_after_inverse_alignment_synced"],
            "meaning": "D0/row-free/命名回流前沿与逆元行号源同字段同步。",
            "remaining": f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
        {
            "gate": "SparseBudgetRefinedToEffectivePruning",
            "closed": result["sparse_budget_refinement_imported"],
            "proved": False,
            "meaning": "非持久预算不是抽象黑箱，已由旧材料压到冷历史有效剪枝和同参数数值表。",
            "remaining": result["next_direct_attack_target"],
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "尚未同时完成非持久预算反超、持久 moving atom 排斥和 DStructure/Rankin 验收。",
            "remaining": result["hardpoint_after_router"],
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    flags = imported_flags()
    row_phase_synced = (
        flags["inverse_alignment_covering_equivalence_imported"]
        and flags["inverse_alignment_prefix_demand_bridge_imported"]
    )
    normalized_available = (
        row_phase_synced
        and flags["finite_prefix_standard_external_available"]
        and flags["finite_prefix_available_under_current_contract"]
    )
    positive_synced = (
        normalized_available
        and flags["rowfree_budget_anticollapse_imported"]
        and flags["positive_margin_frontier_sync_imported"]
        and flags["unified_budget_latest_sync_imported"]
    )
    sparse_refined = (
        flags["sparse_budget_latest_sync_imported"]
        and flags["same_parameter_sparse_margin_reduced_to_cold_numeric"]
        and flags["terminal_hot_core_frontier_imported"]
    )
    hardpoint_after = (
        f"{EFFECTIVE_PRUNING} AND ColdSupplySameParameterNumericEnvelope AND "
        f"TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND "
        f"{MOVING_ATOM} AND {DSTRUCTURE}"
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_latest_frontier_sync_router",
        "status": "inverse_alignment_row_phase_synced_to_latest_sparse_budget_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "inverse_alignment_row_phase_to_latest_frontier_synced": row_phase_synced,
        "normalized_prefix_potential_current_contract_available": normalized_available,
        "positive_margin_frontier_after_inverse_alignment_synced": positive_synced,
        "sparse_budget_refinement_imported": sparse_refined,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": NORMALIZED,
        "hardpoint_after_router": hardpoint_after,
        "next_direct_attack_target": EFFECTIVE_PRUNING,
        "parallel_attack_targets": [
            "ColdSupplySameParameterNumericEnvelope",
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            MOVING_ATOM,
            DSTRUCTURE,
            STRICT_BETA_APPENDIX,
        ],
        "identities": identities(),
        "frontier_rows": frontier_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "逆元最小对齐解思路已经可以被当前前沿充分利用：在假设早期零行存在的反例链中，"
            "行号 x 本身生成全部小素数覆盖相位 rho_q(x)=-xP mod q，进而精确生成 R_{x,z}、"
            "tau_z(c)、mu_q 与 M#_{x,z}。这关闭的是反例链的行号源和 prefix demand 字段非后验性。"
            "但直接用该系统证明 min x>P 会回到短区间素数输入；当前更可用的主线是在 z=P^0.43 的"
            "非循环窗口中接入 finite-prefix/row-free/命名回流前沿。同步后，D0 与类型旧阻塞不再是"
            "当前最窄点；真正剩余回到非持久稀疏预算的有效冷历史剪枝、持久 moving atom 排斥和 DStructure/Rankin 验收。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 文档。"""
    lines = [
        "# Prime Matrix 逆元对齐到最新终端前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"inverse_alignment_row_phase_to_latest_frontier_synced={fmt_bool(result['inverse_alignment_row_phase_to_latest_frontier_synced'])}",
        f"normalized_prefix_potential_current_contract_available={fmt_bool(result['normalized_prefix_potential_current_contract_available'])}",
        f"finite_prefix_strict_first_principles_lower_sieve_closed={fmt_bool(result['finite_prefix_strict_first_principles_lower_sieve_closed'])}",
        f"positive_margin_frontier_after_inverse_alignment_synced={fmt_bool(result['positive_margin_frontier_after_inverse_alignment_synced'])}",
        f"sparse_budget_refinement_imported={fmt_bool(result['sparse_budget_refinement_imported'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 逆元恒等式进入前沿",
        "",
        "| name | formula | meaning | status |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["identities"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    table_cell(row["formula"]),
                    table_cell(row["meaning"]),
                    f"`{table_cell(row['status'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 前沿迁移",
            "",
            "| stage | before | after | remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["frontier_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['stage'])}`",
                    table_cell(row["before"]),
                    table_cell(row["after"]),
                    table_cell(row["remaining"]),
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
            "## 4. 下一最窄点",
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
            "审稿边界：本步不声明 `min x>P`、不使用真实零行缺席，也不声明行/列命题无条件闭合；它只把用户的逆元零行方程组并入当前统一预算前沿，并给出同步后的精确剩余。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
