#!/usr/bin/env python3
"""生成 inverse alignment 到既有 C_core/Rankin 终端链的对齐证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_cold_core_chain_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json
  docs/monograph/prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.md"

INVERSE_COLD = "ColdRestrictedInverseAlignmentSiblingChargeEnvelope"
CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json",
    "prime-matrix-strict-cold-core-threshold-function-table-router.json",
    "prime-matrix-strict-same-parameter-core-threshold-summation-router.json",
    "prime-matrix-strict-core-history-weighted-support-measure-router.json",
    "prime-matrix-strict-cold-support-depth-telescoping-router.json",
    "prime-matrix-strict-same-parameter-per-level-support-exponent-router.json",
    "prime-matrix-strict-active-prefix-level-packing-router.json",
    "prime-matrix-strict-product-fiber-multiplicity-router.json",
    "prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.json",
    "prime-matrix-strict-cold-filtered-divisor-support-router.json",
    "prime-matrix-strict-cold-product-support-sparsification-router.json",
    "prime-matrix-strict-primitive-product-support-rankin-router.json",
    "prime-matrix-strict-primitive-product-rankin-manifest-router.json",
    "prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json",
    "prime-matrix-strict-primitive-product-rankin-p018-table-router.json",
    "prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json",
    "prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json",
    "prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json",
    "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json",
    "prime-matrix-strict-terminal-hot-core-return-frontier-router.json",
    "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json",
    "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_cold_core_chain_reconciliation_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def required_flags() -> list[dict[str, Any]]:
    """读取主链每一段的可复核闭合/路由标志。"""
    inv = load_json("prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json")
    core = load_json("prime-matrix-strict-cold-core-threshold-function-table-router.json")
    summation = load_json("prime-matrix-strict-same-parameter-core-threshold-summation-router.json")
    support = load_json("prime-matrix-strict-core-history-weighted-support-measure-router.json")
    depth = load_json("prime-matrix-strict-cold-support-depth-telescoping-router.json")
    per_level = load_json("prime-matrix-strict-same-parameter-per-level-support-exponent-router.json")
    active = load_json("prime-matrix-strict-active-prefix-level-packing-router.json")
    product = load_json("prime-matrix-strict-product-fiber-multiplicity-router.json")
    active_product = load_json("prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.json")
    cold_filter = load_json("prime-matrix-strict-cold-filtered-divisor-support-router.json")
    sparsify = load_json("prime-matrix-strict-cold-product-support-sparsification-router.json")
    rankin = load_json("prime-matrix-strict-primitive-product-support-rankin-router.json")
    manifest = load_json("prime-matrix-strict-primitive-product-rankin-manifest-router.json")
    weight = load_json("prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json")
    p018 = load_json("prime-matrix-strict-primitive-product-rankin-p018-table-router.json")
    h0 = load_json("prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json")
    enum = load_json("prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json")
    pass_return = load_json("prime-matrix-strict-no-return-rankin-p018-pass-return-sync-router.json")
    exact_hot = load_json("prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json")
    hot = load_json("prime-matrix-strict-terminal-hot-core-return-frontier-router.json")
    cycle = load_json("prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json")
    sparse = load_json("prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json")

    return [
        {
            "stage": "inverse_alignment_cold_return",
            "ok": inv.get("cold_restricted_inverse_alignment_envelope_synced_to_return_frontier") is True,
            "evidence": "逆元 tau/cold 限制已接入 C_core/T_PDEC/回流前沿。",
            "next": CORE_TABLE,
        },
        {
            "stage": "cold_core_schema",
            "ok": core.get("cold_core_function_table_schema_closed") is True,
            "evidence": "C_core 端点、注册键、顺序不变性与长度 cap 已闭合为函数表口径。",
            "next": "SameParameterCoreThresholdSummationDominanceTable",
        },
        {
            "stage": "core_summation_to_weighted_support",
            "ok": summation.get("weighted_support_reduction_closed") is True,
            "evidence": "点态 cap 不足已认证，求和优势压成加权支撑测度。",
            "next": "CoreHistoryWeightedSupportMeasureTable",
        },
        {
            "stage": "weighted_support_single_layer",
            "ok": support.get("single_layer_support_envelope_closed") is True,
            "evidence": "同父兄弟层 envelope 闭合，但全深度伸缩仍需下钻。",
            "next": "ColdSupportDepthTelescopingContractionOrLogAbsorptionTable",
        },
        {
            "stage": "depth_log_absorption",
            "ok": depth.get("log_absorption_criterion_closed") is True,
            "evidence": "深度 log P 可由 P^(1/4) 吸收，剩每层支撑指数表。",
            "next": "SameParameterPerLevelColdSupportExponentTable",
        },
        {
            "stage": "per_level_to_active_prefix",
            "ok": per_level.get("per_level_charge_decomposition_closed") is True,
            "evidence": "每层冷支撑分解为活动前缀、collar debit 与命名回流。",
            "next": "ActivePrefixLevelPackingExponentTable",
        },
        {
            "stage": "active_prefix_packing",
            "ok": active.get("packing_identity_closed") is True and active.get("product_projection_closed") is True,
            "evidence": "活动前缀层打包投影到同一 formal unit 的产品除数纤维。",
            "next": "ActivePrefixProductFiberMultiplicityOrNamedReturnLedger",
        },
        {
            "stage": "product_fiber_quotient",
            "ok": product.get("active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support")
            is True,
            "evidence": "同产品顺序冗余和同 key 重复已商化或回流。",
            "next": "ColdFilteredDivisorSupportP018Envelope",
        },
        {
            "stage": "active_prefix_product_supplement",
            "ok": active_product.get("product_fiber_multiplicity_independent_hardpoint_removed") is True,
            "evidence": "补档证书同步确认产品纤维不再是独立硬点。",
            "next": "ColdNonpersistentProductSupportSparsificationLemma",
        },
        {
            "stage": "cold_filtered_support",
            "ok": cold_filter.get("cold_filtered_support_domain_closed") is True
            and cold_filter.get("prime_power_ordered_cascade_removed_for_support") is True,
            "evidence": "冷过滤产品支撑域压实，素数幂有序爆炸不再给新支撑。",
            "next": "ColdProductSupportSparsificationBeyondTauLedger",
        },
        {
            "stage": "product_sparsification_split",
            "ok": sparsify.get("dyadic_overload_certificate_closed") is True
            and sparsify.get("overload_block_structural_split_closed") is True,
            "evidence": "产品支撑超预算被拆成热窗口、共同核或 primitive Rankin。",
            "next": "PrimitiveProductSupportRankinLedger",
        },
        {
            "stage": "primitive_rankin_schema",
            "ok": rankin.get("existing_rankin_verifier_schema_reusable") is True
            and manifest.get("primitive_product_rankin_embedding_manifest_schema_closed") is True
            and weight.get("primitive_product_local_rankin_weight_formula_closed") is True
            and p018.get("p018_table_schema_closed") is True,
            "evidence": "primitive 产品 Rankin schema、manifest schema、局部权重和 P^0.18 表口径已闭合。",
            "next": "ActualColdProductBlockParameterLedgerForP018Table",
        },
        {
            "stage": "actual_h0_no_return_rankin",
            "ok": h0.get("no_return_h0_emitter_for_rankin_parameter_closed") is True
            and enum.get("actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed") is True
            and pass_return.get("no_return_rankin_p018_pass_or_return_schema_closed") is True,
            "evidence": "no-return h0、dyadic 枚举器与 pass/return 规则已接入。",
            "next": "PrimitiveProductRankinFailureReturnPacketLedger",
        },
        {
            "stage": "exact_count_to_hot_return",
            "ok": exact_hot.get("exact_count_pass_or_hot_return_dichotomy_closed") is True
            and exact_hot.get("clean_exact_overbudget_without_named_return_excluded") is True,
            "evidence": "clean exact overbudget 不能无名停留，必须登记为热核心回流。",
            "next": "TerminalCoreHotDivisorWindowPDECorSAE",
        },
        {
            "stage": "terminal_hot_frontier",
            "ok": hot.get("terminal_hot_core_frontier_closed") is True
            and hot.get("terminal_core_hot_divisor_window_independent_hardpoint_removed") is True,
            "evidence": "热核心不是独立第三出口，拆成非持久预算或持久终端族。",
            "next": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        },
        {
            "stage": "return_cycle_budget_sync",
            "ok": cycle.get("unified_budget_after_return_cycle_sync_closed") is True
            and sparse.get("sparse_budget_positive_margin_latest_sync_closed") is True,
            "evidence": "共同核/命名回流不能免费循环，非持久侧回到同参数稀疏预算。",
            "next": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "InverseAlignmentColdCoreChainReconciled",
            "closed": result["inverse_alignment_cold_core_chain_reconciled"],
            "proved": result["inverse_alignment_cold_core_chain_reconciled"],
            "meaning": "逆元冷限制出口已严格接到既有 C_core/产品支撑/Rankin/热核心终端链。",
            "remaining": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        },
        {
            "gate": "ColdCoreNumericIndependentHardpointRemovedForInverseAlignment",
            "closed": result["cold_core_numeric_independent_hardpoint_removed_for_inverse_alignment"],
            "proved": result["cold_core_numeric_independent_hardpoint_removed_for_inverse_alignment"],
            "meaning": "C_core 不再作为逆元路线的新独立硬点；其失败已沿既有链回流到终端预算。",
            "remaining": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        },
        {
            "gate": "ColdCoreThresholdNumericTableProved",
            "closed": False,
            "proved": False,
            "meaning": "本步是链路对齐，不是单独证明 C_core 数值表。",
            "remaining": CORE_TABLE,
        },
        {
            "gate": "SameParameterPDECThresholdNumericTableProved",
            "closed": False,
            "proved": False,
            "meaning": "持久阈值表仍需随持久终端族一起排斥或吸收。",
            "remaining": PDEC_TABLE,
        },
        {
            "gate": "SparseBudgetTerminalContradictionProved",
            "closed": False,
            "proved": False,
            "meaning": "非持久预算严格反超仍未闭合。",
            "remaining": SPARSE_BUDGET,
        },
        {
            "gate": "PersistentTerminalFamilyExcluded",
            "closed": False,
            "proved": False,
            "meaning": "持久热/固定/相位复现终端族仍未排斥。",
            "remaining": PERSISTENT_TERMINAL,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "尚未得到早期零行反例链与真实链的终端矛盾。",
            "remaining": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造对齐证书。"""
    stages = required_flags()
    chain_ok = all(item["ok"] for item in stages)
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_cold_core_chain_reconciliation_router",
        "status": "inverse_alignment_cold_core_chain_reconciled_to_terminal_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "inverse_alignment_cold_core_chain_reconciled": chain_ok,
        "cold_core_numeric_independent_hardpoint_removed_for_inverse_alignment": chain_ok,
        "product_fiber_supplement_archived": any(
            item["stage"] == "active_prefix_product_supplement" and item["ok"] for item in stages
        ),
        "cold_core_threshold_numeric_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "dstructure_rankin_independent_acceptance_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": (
            f"{INVERSE_COLD} -> {CORE_TABLE} AND {PDEC_TABLE}"
        ),
        "hardpoint_after_router": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        "next_direct_attack_target": SPARSE_BUDGET,
        "parallel_attack_targets": [PERSISTENT_TERMINAL, DSTRUCTURE],
        "stage_rows": stages,
        "decision_rows": [],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "逆元最小对齐解产生的 cold-restricted tau/envelope 不再形成新的 C_core 孤立硬点。"
            "沿现有 C_core 函数表、同参数求和、加权支撑、深度伸缩、活动前缀打包、产品纤维商化、"
            "冷过滤产品支撑、primitive Rankin、精确计数与热核心回流链，失败已经被统一路由到两条终端线："
            "非持久侧的稀疏预算严格反超，和持久侧的 actual noncanonical moving atom/PDEC/固定历史终端族排斥。"
            "这一步只是消除逆元路线回到 C_core 后的重复硬点，不证明最终矛盾；行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix inverse alignment 到 C_core/Rankin 终端链对齐证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"inverse_alignment_cold_core_chain_reconciled={fmt_bool(result['inverse_alignment_cold_core_chain_reconciled'])}",
        f"cold_core_numeric_independent_hardpoint_removed_for_inverse_alignment={fmt_bool(result['cold_core_numeric_independent_hardpoint_removed_for_inverse_alignment'])}",
        f"sparse_history_demand_exceeds_nonpersistent_supply_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_nonpersistent_supply_budget_proved'])}",
        f"persistent_terminal_family_excluded={fmt_bool(result['persistent_terminal_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 链路分段",
        "",
        "| stage | ok | evidence | next |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["stage_rows"]:
        lines.append(
            "| `{stage}` | `{ok}` | {evidence} | {next} |".format(
                stage=table_cell(item["stage"]),
                ok=fmt_bool(item["ok"]),
                evidence=table_cell(item["evidence"]),
                next=table_cell(item["next"]),
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
    for item in result["decision_rows"]:
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
            "## 3. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行：`{PERSISTENT_TERMINAL}` 与 `{DSTRUCTURE}`。",
            "- 边界：本证书不宣称 C_core 数值表、PDEC 阈值表或最终反例矛盾已证明。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
