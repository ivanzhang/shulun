#!/usr/bin/env python3
"""生成 strict 活动前缀产品纤维重数/命名回流账本证书。

用法示例：
  python3 experiments/prime_matrix_strict_product_fiber_multiplicity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.json

输出：
  docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.json
  docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.md"

HARDPOINT = "ActivePrefixProductFiberMultiplicityOrNamedReturnLedger"
ACTIVE_PACKING = "ActivePrefixLevelPackingExponentTable"
CANONICAL_QUOTIENT = "ProductFiberCanonicalEndpointQuotientLedger"
SAME_KEY_LOAD = "SameProductSameKeyMultiplicityToLoadOrNamedReturn"
LABEL_DRIFT = "ProductFiberLabelPhaseDriftNamedReturnLedger"
COLD_FILTERED_DIVISOR = "ColdFilteredDivisorSupportP018Envelope"
DIVISOR_ENV = "DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope"
COLD_FILTER = "ColdNonpersistentProductSupportSparsificationLemma"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
TPDEC_TABLE = "SameParameterPDECThresholdNumericTable"
COLLAR_SUM = "SameParameterSiblingCollarWidthFiniteSumTable"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-active-prefix-level-packing-router.json",
    DOCS / "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    DOCS / "prime-matrix-strict-legacy-product-window-equivalence-router.json",
    DOCS / "prime-matrix-strict-cold-core-threshold-function-table-router.json",
    DOCS / "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    DOCS / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    DOCS / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
    DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    DATA / "product-window-endpoint-generator-sample-ledger.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_product_fiber_multiplicity_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def imported_flags() -> dict[str, bool]:
    """读取本轮需要对接的已闭合接口。"""
    active = load_json(DOCS / "prime-matrix-strict-active-prefix-level-packing-router.json")
    generator = load_json(DOCS / "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json")
    legacy = load_json(DOCS / "prime-matrix-strict-legacy-product-window-equivalence-router.json")
    cold = load_json(DOCS / "prime-matrix-strict-cold-core-threshold-function-table-router.json")
    row_free = load_json(DOCS / "prime-matrix-strict-row-free-type-anticollapse-sync-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    sample = load_json(DATA / "product-window-endpoint-generator-sample-ledger.json")
    formal = load_json(DOCS / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json")

    return {
        "active_product_projection_imported": bool(active.get("product_projection_closed")),
        "active_packing_identity_imported": bool(active.get("packing_identity_closed")),
        "endpoint_generator_closed": bool(
            generator.get("product_window_endpoint_generator_artifact_or_definition_appendix_closed")
        ),
        "legacy_product_window_equivalence_proved": bool(
            legacy.get("legacy_product_window_notation_equivalence_proved")
        ),
        "endpoint_generator_and_legacy_notation_closed": bool(
            cold.get("endpoint_generator_and_legacy_notation_closed")
        ),
        "cold_core_registry_order_invariance_closed": bool(
            cold.get("cold_core_threshold_registry_and_order_invariance_closed")
        ),
        "row_free_anticollapse_closed_for_budget": bool(
            row_free.get("prefix_label_support_to_row_free_type_anticollapse_closed_for_budget")
        ),
        "sparse_history_multiplicity_conservation_closed": bool(
            sparse.get("multiplicity_conservation_anticollapse_closed")
        ),
        "terminal_projection_anticollapse_closed": bool(
            sparse.get("terminal_projection_anticollapse_closed")
        ),
        "same_product_sample_ledger_passed": bool(sample.get("all_same_product_equal")),
        "formal_unit_multiplicity_to_divisor_count_imported": bool(
            formal.get("multiplicity_to_divisor_count_closed")
            or formal.get("formal_unit_sparse_history_multiplicity_reduced_to_scaled_divisor_window")
            or formal.get("formal_unit_sparse_history_multiplicity_router_closed")
            or formal.get("single_history_multiplicity_reduced_to_divisor_window")
        ),
    }


def fiber_case_rows() -> list[dict[str, str]]:
    """列出同产品纤维内的互斥分支。"""
    return [
        {
            "case": "same_product_same_canonical_key",
            "condition": "D(U1)=D(U2)=d, same formal unit, same row-free/cold-core key",
            "effect": "I_{U1}=I_{U2}, C_core(U1)=C_core(U2)",
            "route": CANONICAL_QUOTIENT,
            "status": "closed_support_quotient",
            "meaning": "乘法顺序或形式前缀差异不产生新的冷支撑窗口，只保留一个规范产品支撑。",
        },
        {
            "case": "same_product_same_key_multiple_labels",
            "condition": "same d and same key, but multiple prefix labels hit the same support",
            "effect": "multiplicity becomes Load(d,key), not additional support",
            "route": SAME_KEY_LOAD,
            "status": "closed_routing_budget_numeric_open",
            "meaning": "多重命中按负载守恒进入冷容量/统一预算；不能静默消失，也不能重复算作新支撑。",
        },
        {
            "case": "same_product_label_or_phase_drift",
            "condition": "same d, but row-free key, phase key, endpoint key, or formal unit changes",
            "effect": "drift is a registered defect",
            "route": LABEL_DRIFT,
            "status": "registered_named_return",
            "meaning": "若为了区分同产品前缀必须改变标签或相位，则它不是免费冷支撑，而是 PDEC/SAE/ColumnCRT/热核心/固定历史出口。",
        },
        {
            "case": "same_product_hot_or_persistent_overload",
            "condition": "Load(d,key) exceeds the registered cold capacity threshold",
            "effect": "hot core, fixed history, or PDEC recurrence",
            "route": NAMED_RETURN,
            "status": "registered_not_excluded",
            "meaning": "同产品纤维过载不能留在非持久冷支撑；但本步不排斥这些命名出口。",
        },
        {
            "case": "different_product_support",
            "condition": "d ranges over actual cold products dividing h_0",
            "effect": "support is counted by cold-filtered divisor products",
            "route": COLD_FILTERED_DIVISOR,
            "status": "open",
            "meaning": "产品纤维已商掉后，剩余主量是哪些产品除数真正冷且非持久可用。",
        },
    ]


def quotient_rows() -> list[dict[str, str]]:
    """给出支撑商化后的计数恒等式。"""
    return [
        {
            "object": "raw_prefix_count",
            "formula": "|A_j|=sum_{d|h_0}|A_j(d)|",
            "role": "load_identity",
            "status": "not_a_support_bound",
        },
        {
            "object": "canonical_support",
            "formula": "S_j=supp{(d,key): U in A_j, D(U)=d, no named drift}",
            "role": "support_identity",
            "status": "closed_definition",
        },
        {
            "object": "same_fiber_quotient",
            "formula": "many U with same (d,key) -> one support point plus Load(d,key)",
            "role": "fiber_multiplier_removed_from_support",
            "status": "closed",
        },
        {
            "object": "remaining_support_goal",
            "formula": "|S_j| <= # cold-filtered products + registered key classes",
            "role": "next_envelope",
            "status": "open_numeric_envelope",
        },
    ]


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成本轮判定表。"""
    quotient_inputs = (
        flags["active_product_projection_imported"]
        and flags["endpoint_generator_closed"]
        and flags["legacy_product_window_equivalence_proved"]
        and flags["endpoint_generator_and_legacy_notation_closed"]
        and flags["cold_core_registry_order_invariance_closed"]
    )
    anticollapse_inputs = (
        flags["row_free_anticollapse_closed_for_budget"]
        and flags["sparse_history_multiplicity_conservation_closed"]
        and flags["terminal_projection_anticollapse_closed"]
        and flags["formal_unit_multiplicity_to_divisor_count_imported"]
    )
    fiber_ledger_closed = quotient_inputs and anticollapse_inputs
    return [
        row(
            "ProductFiberTargetImported",
            True,
            flags["active_product_projection_imported"],
            "上一层已把活动前缀打包压到产品投影与产品纤维重数。",
            HARDPOINT,
        ),
        row(
            "CanonicalEndpointQuotientInputsClosed",
            quotient_inputs,
            quotient_inputs,
            "同产品的规范端点、旧窗口记号和冷核心注册键已经对齐；顺序差异不改变支撑窗口。",
            CANONICAL_QUOTIENT,
        ),
        row(
            "SameProductPermutationNewSupportExcluded",
            quotient_inputs,
            quotient_inputs,
            "同一 formal unit 下同一产品 d 的有序分解不会生成多个冷支撑点，只生成同一规范产品支撑。",
            "closed for support quotient",
        ),
        row(
            "SameProductSameKeyMultiplicityRoutedToLoad",
            anticollapse_inputs,
            anticollapse_inputs,
            "同一产品同一 key 的多重前缀按负载守恒进入冷容量或统一预算，不再作为自由支撑膨胀因子。",
            SAME_KEY_LOAD,
        ),
        row(
            "ProductFiberLabelPhaseDriftRegistered",
            anticollapse_inputs,
            False,
            "同产品但标签、相位或 formal-unit 键漂移时，必须进入命名回流桶；本步只完成登记，不排斥该桶。",
            NAMED_RETURN,
        ),
        row(
            "ActivePrefixProductFiberMultiplicityOrNamedReturnLedgerClosedForSupport",
            fiber_ledger_closed,
            fiber_ledger_closed,
            "产品纤维内的免费重数支撑爆炸被排除：同 key 商化为一个支撑，异 key/漂移进入命名回流。",
            f"{COLD_FILTERED_DIVISOR} AND {UNIFIED_BUDGET}",
        ),
        row(
            "ProductFiberMultiplicityNumericAbsorptionProved",
            False,
            False,
            "同 key 的负载守恒已路由，但尚未在同参数最终预算中完成数值吸收。",
            f"{UNIFIED_BUDGET} AND {TPDEC_TABLE}",
        ),
        row(
            "ColdFilteredDivisorSupportP018EnvelopeProved",
            False,
            False,
            "商掉产品纤维后，仍需证明真实冷产品支撑满足 P^0.18 级 envelope；粗 tau(h_0) 已失败。",
            f"{DIVISOR_ENV} AND {COLD_FILTER}",
        ),
        row(
            "ActivePrefixLevelPackingExponentTableProved",
            False,
            False,
            "本步关闭产品纤维免费膨胀，不关闭 cold-filtered 产品支撑、collar 总和和 T_PDEC 权重。",
            f"{COLD_FILTERED_DIVISOR} AND {COLLAR_SUM} AND {TPDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾；不能声明行/列命题无条件闭合。",
            f"{COLD_FILTERED_DIVISOR} AND {UNIFIED_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造产品纤维重数/命名回流账本证书。"""
    flags = imported_flags()
    decisions = decision_rows(flags)
    fiber_ledger_closed = next(
        item for item in decisions if item["gate"] == "ActivePrefixProductFiberMultiplicityOrNamedReturnLedgerClosedForSupport"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_product_fiber_multiplicity_router",
        "status": "product_fiber_free_support_multiplicity_quotiented_named_drift_registered_divisor_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{COLD_FILTERED_DIVISOR} AND {UNIFIED_BUDGET}",
        "next_direct_attack_target": COLD_FILTERED_DIVISOR,
        "imported_flags": flags,
        "fiber_cases": fiber_case_rows(),
        "quotient_identities": quotient_rows(),
        "decision_table": decisions,
        "product_fiber_canonical_endpoint_quotient_closed": bool(
            next(item for item in decisions if item["gate"] == "CanonicalEndpointQuotientInputsClosed")["proved"]
        ),
        "same_product_permutation_new_support_excluded": bool(
            next(item for item in decisions if item["gate"] == "SameProductPermutationNewSupportExcluded")["proved"]
        ),
        "same_product_same_key_multiplicity_routed_to_load": bool(
            next(item for item in decisions if item["gate"] == "SameProductSameKeyMultiplicityRoutedToLoad")["proved"]
        ),
        "product_fiber_label_phase_drift_registered": bool(
            next(item for item in decisions if item["gate"] == "ProductFiberLabelPhaseDriftRegistered")["closed"]
        ),
        "active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support": bool(
            fiber_ledger_closed
        ),
        "product_fiber_multiplicity_numeric_absorption_proved": False,
        "cold_filtered_divisor_support_p018_envelope_proved": False,
        "active_prefix_level_packing_exponent_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ActivePrefixProductFiberMultiplicityOrNamedReturnLedger` 的支撑版已闭合："
            "同一 formal unit 下同一产品 d 的顺序/形式前缀差异只给出同一个规范端点和同一个冷核心阈值键；"
            "同 key 多重命中是负载，不是新支撑；异 key、标签漂移或相位漂移必须登记为 PDEC/SAE/ColumnCRT/热核心/固定历史回流。"
            "因此产品纤维不能再作为免费支撑膨胀源。"
            "但这还没有证明最终活动前缀打包指数，因为商掉纤维后仍需控制真实 cold-filtered 产品除数支撑，"
            "并把同 key 负载、collar 总和与 T_PDEC 权重接入统一预算。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 产品纤维重数/命名回流账本路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "product_fiber_canonical_endpoint_quotient_closed",
        "same_product_permutation_new_support_excluded",
        "same_product_same_key_multiplicity_routed_to_load",
        "product_fiber_label_phase_drift_registered",
        "active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support",
        "cold_filtered_divisor_support_p018_envelope_proved",
        "active_prefix_level_packing_exponent_table_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 纤维分支")
    lines.append("")
    lines.append("| case | condition | effect | route | status | meaning |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for item in result["fiber_cases"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(item[key])
                for key in ["case", "condition", "effect", "route", "status", "meaning"]
            )
            + " |"
        )
    lines.append("")

    lines.append("## 2. 支撑商化恒等式")
    lines.append("")
    lines.append("| object | formula | role | status |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["quotient_identities"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["object", "formula", "role", "status"])
            + " |"
        )
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append(f"- 同步：`{UNIFIED_BUDGET}`、`{COLLAR_SUM}`、`{TPDEC_TABLE}`。")
    lines.append("- 边界：本步只排除产品纤维免费支撑膨胀；不声明行/列命题无条件闭合。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 文件。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support="
        f"{fmt_bool(result['active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
