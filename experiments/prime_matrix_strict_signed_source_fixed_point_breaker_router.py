#!/usr/bin/env python3
"""生成 strict signed-source 固定点切断证书。

用法示例：
  python3 experiments/prime_matrix_strict_signed_source_fixed_point_breaker_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-signed-source-fixed-point-breaker-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"
OUT_MD = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.md"

TARGET = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
NEXT_TARGET = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
    "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
    "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json",
    "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json",
    "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json",
    "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def kernel_contract() -> list[dict[str, str]]:
    """列出非循环 signed coefficient emission kernel 的必要字段。"""
    return [
        {
            "field": "domain",
            "meaning": "只读取 actual noncanonical seed/source tuple 及已闭合 primitive basis word 坐标。",
        },
        {
            "field": "signed_coefficient_formula",
            "meaning": "在 Cauchy/payment/Phi 推前之前正向输出 signed coefficient。",
        },
        {
            "field": "sign_and_local_factor",
            "meaning": "同步给出 sign、local factor、非零条件和 branch key。",
        },
        {
            "field": "prepushforward_sum_identity",
            "meaning": "证明输出 rows 的求和已等于目标 alpha/delta 贡献。",
        },
        {
            "field": "no_self_reference",
            "meaning": "公式不得读取 row-level 表、来源恒等式、payment/Phi 下游结果或早期零行覆盖。",
        },
        {
            "field": "named_return_tags",
            "meaning": "缺 seed、零局部因子、符号冲突、超预算或作用域冲突必须命名回流。",
        },
    ]


def spine_edges() -> list[dict[str, str]]:
    """记录 signed-source 依赖脊柱。"""
    return [
        {"from": TARGET, "to": "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"},
        {"from": "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity", "to": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"},
        {"from": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward", "to": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"},
        {"from": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows", "to": "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"},
        {"from": "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy", "to": "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"},
        {"from": "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger", "to": "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment"},
        {"from": "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment", "to": "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility"},
        {"from": "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility", "to": "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility"},
        {"from": "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility", "to": "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"},
        {"from": "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters", "to": "AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates"},
        {"from": "AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates", "to": "AcyclicSeedSignedWeightCoordinateSlotLedger"},
        {"from": "AcyclicSeedSignedWeightCoordinateSlotLedger", "to": "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"},
        {"from": "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords", "to": "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"},
        {"from": "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger", "to": "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"},
        {"from": "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula", "to": "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"},
        {"from": "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward", "to": TARGET},
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 signed-source 路线是否已经回到同一原始生成表。"""
    row_table = data["row_table"]
    emitter = data["emitter"]
    primitive_law = data["primitive_law"]
    basis_source = data["basis_source"]
    internal = data["internal"]
    alphabet = data["alphabet"]
    word_generation = data["word_generation"]
    constructor = data["constructor"]
    basis_word = data["basis_word"]
    word_coord = data["word_coord"]
    anchor = data["anchor"]
    signed_slot = data["signed_slot"]
    slot_value = data["slot_value"]
    assignment = data["assignment"]
    value_map = data["value_map"]
    origin = data["origin"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    upstream_spine_materialized = all(
        [
            row_table.get("row_level_origin_generation_table_router_closed") is True,
            emitter.get("acyclic_seed_signed_row_emitter_router_closed") is True,
            primitive_law.get("acyclic_seed_primitive_coefficient_law_router_closed") is True,
            basis_source.get("acyclic_seed_basis_weight_source_formula_router_closed") is True,
            internal.get("acyclic_seed_internal_arithmetic_basis_expansion_router_closed") is True,
            alphabet.get("acyclic_seed_basis_alphabet_ledger_router_closed") is True,
            word_generation.get("primitive_basis_word_generation_router_closed") is True,
            constructor.get("source_tuple_word_constructor_router_closed") is True,
            basis_word.get("basis_word_formula_router_closed") is True,
            word_coord.get("word_coordinate_formula_router_closed") is True,
        ]
    )
    geometry_closed = anchor.get("anchor_input_rule_proved") is True
    signed_spine_returns = all(
        [
            signed_slot.get("signed_weight_coordinate_slot_router_closed") is True,
            slot_value.get("signed_slot_value_formula_router_closed") is True,
            assignment.get("coefficient_assignment_router_closed") is True,
            value_map.get("coefficient_value_map_router_closed") is True,
            origin.get("basis_word_origin_identity_router_closed") is True,
            origin.get("basis_word_origin_equals_row_level_generation") is True,
        ]
    )
    reverse_blocked = (
        source_loop.get("source_loop_cut_closed") is True
        and source_loop.get("circular_reverse_derivation_rejected") is True
        and reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
        and zero_nogo.get("zero_row_seed_extraction_blocked") is True
    )
    fixed_point = upstream_spine_materialized and geometry_closed and signed_spine_returns

    return [
        row(
            "RowLevelGenerationTableIsActiveTarget",
            origin.get("next_direct_attack_target") == TARGET,
            False,
            "最新 basis word 来源恒等式已回收到逐行 clean-core 原始生成表。",
            TARGET,
        ),
        row(
            "SignedSourceSpineMaterialized",
            upstream_spine_materialized,
            True,
            "从 row-level 表到 seed/emitter、coefficient law、basis source、basis word 构造的依赖脊柱已全部登记。",
            "登记脊柱不等于生成 signed coefficient。",
        ),
        row(
            "GeometricAnchorBranchClosed",
            geometry_closed,
            True,
            "锚选择、窗口端点、phase pullback 和低重叠收费已闭合。",
            "几何闭合只给 unsigned word 输入，不给 signed coefficient。",
        ),
        row(
            "SignedAssignmentSpineReturnsToRowLevel",
            signed_spine_returns,
            True,
            "signed slot、assignment、value map、origin identity 最终回到同一逐行原始生成表。",
            TARGET,
        ),
        row(
            "ReverseAndZeroRowRecoveryBlocked",
            reverse_blocked,
            True,
            "来源环、payment 反推、早期零行 unsigned cover 均不能生成 signed seed/rows。",
            NEXT_TARGET,
        ),
        row(
            "CurrentInternalRouteIsSignedSourceFixedPoint",
            fixed_point,
            True,
            "现有内部路线形成 RowLevel -> ... -> RowLevel 的 signed-source 固定点。",
            "固定点切断后必须提交非循环 signed coefficient emission kernel。",
        ),
        row(
            "NoncircularSignedCoefficientEmissionKernelCurrentCorpusProved",
            False,
            False,
            "当前材料没有不读取下游表/来源恒等式/payment 的 pre-Cauchy signed coefficient 发射核。",
            NEXT_TARGET,
        ),
        row(
            "RowLevelOriginalGenerationTableCurrentCorpusProved",
            False,
            False,
            "没有非循环发射核，逐行原始生成表仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 signed-source 固定点切断证书。"""
    data = {
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "emitter": load_json("prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"),
        "primitive_law": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "basis_source": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
        "internal": load_json("prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"),
        "alphabet": load_json("prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"),
        "word_generation": load_json("prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json"),
        "constructor": load_json("prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json"),
        "basis_word": load_json("prime-matrix-strict-acyclic-seed-basis-word-formula-router.json"),
        "word_coord": load_json("prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"),
        "anchor": load_json("prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"),
        "signed_slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "slot_value": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "assignment": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "value_map": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "origin": load_json("prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    fixed_point = next(
        item["closed"] for item in rows if item["gate"] == "CurrentInternalRouteIsSignedSourceFixedPoint"
    )
    return {
        "certificate_type": "prime_matrix_strict_signed_source_fixed_point_breaker_router",
        "status": "signed_source_fixed_point_cut_to_noncircular_emission_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "signed_source_fixed_point_breaker_closed": True,
        "current_internal_route_is_signed_source_fixed_point": fixed_point,
        "geometric_anchor_branch_closed": data["anchor"].get("anchor_input_rule_proved") is True,
        "signed_assignment_returns_to_row_level_generation_table": fixed_point,
        "reverse_and_zero_row_recovery_blocked": next(
            item["closed"] for item in rows if item["gate"] == "ReverseAndZeroRowRecoveryBlocked"
        ),
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "terminal_return_if_no_kernel": TERMINAL_RETURN,
        "spine_edges": spine_edges(),
        "kernel_contract": kernel_contract(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的当前内部证明脊柱已经形成 signed-source 固定点；"
            f"真正非循环破坏输入是 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步没有改换命题，而是把最新一圈下钻结果合并审查。"
            "几何锚输入已经闭合，但 signed coefficient 来源链从逐行原始表出发，"
            "经 seed/emitter、basis word、assignment、value map、origin identity 后又回到同一逐行原始表。"
            "因此不能把这条链当作证明；必须新增一个不读取下游 payment/来源表/早期零行覆盖的 pre-Cauchy signed coefficient 发射核。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict signed-source 固定点切断证书",
        "",
        "## 1. 结论",
        "",
        result["plain_conclusion"],
        "",
        "## 2. 状态",
        "",
        f"- same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"- current_internal_route_is_signed_source_fixed_point={fmt_bool(result['current_internal_route_is_signed_source_fixed_point'])}",
        f"- geometric_anchor_branch_closed={fmt_bool(result['geometric_anchor_branch_closed'])}",
        f"- reverse_and_zero_row_recovery_blocked={fmt_bool(result['reverse_and_zero_row_recovery_blocked'])}",
        f"- noncircular_signed_coefficient_emission_kernel_proved={fmt_bool(result['noncircular_signed_coefficient_emission_kernel_proved'])}",
        f"- row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"- direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"- row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "",
        "## 3. 固定点判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 非循环发射核合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["kernel_contract"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 5. 下一真正单点",
            "",
            result["next_direct_attack_target"],
            "",
            "若该 kernel 不能提交，则按命名纪律回流：",
            "",
            result["terminal_return_if_no_kernel"],
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "signed_source_fixed_point="
        f"{fmt_bool(result['current_internal_route_is_signed_source_fixed_point'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
