#!/usr/bin/env python3
"""生成 strict 确定性 alpha row 发射映射字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_deterministic_alpha_row_emission_map_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-deterministic-alpha-row-emission-map-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"
OUT_MD = DOCS / "prime-matrix-strict-deterministic-alpha-row-emission-map-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


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


def build_rows(
    alpha_rule: dict[str, Any],
    source_tuple: dict[str, Any],
    anchor_recon: dict[str, Any],
    source_law: dict[str, Any],
    reverse_functor: dict[str, Any],
    source_loop: dict[str, Any],
    constructor_line: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成确定性 alpha row 发射映射判定表。"""
    target = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
    next_basis = (
        "AlphaPrimitiveRowIndexSetLedger AND "
        "AlphaRowAnchorPhaseEmissionFormulaLedger AND "
        "AlphaRowFiniteMultiplicityOrderingLedger AND "
        "AlphaEmissionMapNoDownstreamChoiceLedger AND "
        "AlphaEmissionMapNamedReturnLedger"
    )
    terminal_after = alpha_rule.get("terminal_gap_after_router", "")
    source_tuple_ready = source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    anchor_ready = anchor_recon.get("anchor_set_reconstruction_certificate_ledger") is True
    source_fields_imported = source_law.get("origin_generation_ledger_implication_closed") is True
    reverse_blocked = reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True
    source_loop_cut = source_loop.get("source_loop_cut_closed") is True
    formula_line_targeted = (
        constructor_line.get("terminal_gap_after_router", "").find(
            "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
        )
        >= 0
    )
    return [
        {
            "gate": "DeterministicAlphaEmissionMapTargetActive",
            "closed": target in terminal_after or alpha_rule.get("next_direct_attack_target") == target,
            "proved": False,
            "meaning": "上一层 alpha 侧规则已把当前最窄点固定为确定性 alpha primitive row 发射映射。",
            "remaining": target,
        },
        {
            "gate": "ConcreteSourceTupleDataImportedButNotMap",
            "closed": source_tuple_ready and anchor_ready,
            "proved": True,
            "meaning": "source tuple 已锁定 P/window、A、D0/K/Omega、phase_rule 与哈希。",
            "remaining": "这些字段不是 row index set，也不是 row formula。",
        },
        {
            "gate": "PreCauchyOutputContractImported",
            "closed": source_fields_imported and formula_line_targeted,
            "proved": True,
            "meaning": "pre-Cauchy 合同要求发射映射在 Cauchy/dispersion 前输出 rows，而非后验解释。",
            "remaining": next_basis,
        },
        {
            "gate": "ReversePaymentChoiceBlocked",
            "closed": reverse_blocked,
            "proved": True,
            "meaning": "不能从 Gamma/payment fiber 反选 alpha rows；反选会破坏确定性。",
            "remaining": "AlphaEmissionMapNoDownstreamChoiceLedger。",
        },
        {
            "gate": "SourceLoopSelfDefinitionBlocked",
            "closed": source_loop_cut,
            "proved": True,
            "meaning": "constructor/formula/emitter/origin ledger 等价环不能自定义发射映射。",
            "remaining": "AlphaRowAnchorPhaseEmissionFormulaLedger。",
        },
        {
            "gate": "AlphaPrimitiveRowIndexSetCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未定义 alpha primitive rows 的有限索引集合及其与 source tuple 的关系。",
            "remaining": "AlphaPrimitiveRowIndexSetLedger。",
        },
        {
            "gate": "AlphaRowAnchorPhaseFormulaCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出由 A、D0/K/Omega、phase_rule 到 alpha row 的显式发射公式。",
            "remaining": "AlphaRowAnchorPhaseEmissionFormulaLedger。",
        },
        {
            "gate": "AlphaRowFiniteMultiplicityOrderingCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明每个 source tuple 只发射有限/polylog 个 rows 且有 canonical ordering。",
            "remaining": "AlphaRowFiniteMultiplicityOrderingLedger。",
        },
        {
            "gate": "AlphaEmissionNoDownstreamChoiceCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 row 选择完全在推前前确定，不依赖 payment 纤维或外部谱后处理。",
            "remaining": "AlphaEmissionMapNoDownstreamChoiceLedger。",
        },
        {
            "gate": "AlphaEmissionMapNamedReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出发射公式不可用、索引超预算或字段缺失时的命名回流。",
            "remaining": "AlphaEmissionMapNamedReturnLedger。",
        },
        {
            "gate": "DeterministicAlphaEmissionMapCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "索引集合、发射公式、有限重数、无后验选择和回流五项尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造确定性 alpha row 发射映射证书。"""
    alpha_rule = load_json(DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json")
    source_tuple = load_json(DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    anchor_recon = load_json(DOCS / "prime-matrix-anchor-set-reconstruction-certificate-router.json")
    source_law = load_json(DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json")
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    constructor_line = load_json(DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.json")

    target = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
    next_basis = (
        "AlphaPrimitiveRowIndexSetLedger AND "
        "AlphaRowAnchorPhaseEmissionFormulaLedger AND "
        "AlphaRowFiniteMultiplicityOrderingLedger AND "
        "AlphaEmissionMapNoDownstreamChoiceLedger AND "
        "AlphaEmissionMapNamedReturnLedger"
    )
    rows = build_rows(
        alpha_rule=alpha_rule,
        source_tuple=source_tuple,
        anchor_recon=anchor_recon,
        source_law=source_law,
        reverse_functor=reverse_functor,
        source_loop=source_loop,
        constructor_line=constructor_line,
    )
    return {
        "certificate_type": "prime_matrix_strict_deterministic_alpha_row_emission_map_router",
        "status": "strict_deterministic_alpha_row_emission_map_reduced_to_index_formula_multiplicity_choice_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "deterministic_alpha_row_emission_map_router_closed": True,
        "concrete_source_tuple_data_imported_but_not_map": True,
        "reverse_payment_choice_blocked_imported": True,
        "source_loop_self_definition_blocked_imported": True,
        "alpha_primitive_row_index_set_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "alpha_row_finite_multiplicity_ordering_proved": False,
        "alpha_emission_map_no_downstream_choice_proved": False,
        "alpha_emission_map_named_return_proved": False,
        "deterministic_alpha_primitive_row_emission_map_proved": False,
        "actual_noncanonical_alpha_side_primitive_rule_proved": False,
        "actual_noncanonical_delta_side_primitive_rule_proved": False,
        "alpha_delta_pairing_compatibility_before_cauchy_proved": False,
        "primitive_rule_nonzero_sign_local_factor_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "AlphaRowAnchorPhaseEmissionFormulaLedger",
        "emission_map_law": (
            "A deterministic alpha row emission map must be a pre-pushforward function, not a choice made after payment. "
            "It has to define the alpha row index set, provide an explicit anchor/phase emission formula, prove finite "
            "multiplicity and canonical ordering, forbid downstream recovery, and return every missing or over-budget case by name."
        ),
        "plain_conclusion": (
            "`DeterministicAlphaPrimitiveRowEmissionMapLedger` 被继续压成 alpha row 索引集合、A/D0/K/Omega/phase_rule "
            "到 row 的显式发射公式、有限重数/规范排序、禁止后验选择和命名回流五项。当前最窄点是 "
            "`AlphaRowAnchorPhaseEmissionFormulaLedger`；已有 source tuple 字段仍只是输入参数，缺少把参数变成 "
            "alpha primitive rows 的实际公式。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 确定性 alpha row 发射映射路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"deterministic_alpha_row_emission_map_router_closed={fmt_bool(result['deterministic_alpha_row_emission_map_router_closed'])}",
        f"deterministic_alpha_primitive_row_emission_map_proved={fmt_bool(result['deterministic_alpha_primitive_row_emission_map_proved'])}",
        f"actual_noncanonical_alpha_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_alpha_side_primitive_rule_proved'])}",
        f"actual_noncanonical_delta_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_delta_side_primitive_rule_proved'])}",
        f"explicit_alpha_delta_primitive_constructor_rule_proved={fmt_bool(result['explicit_alpha_delta_primitive_constructor_rule_proved'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(result['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 发射映射律",
        "",
        result["emission_map_law"],
        "",
        "## 2. 映射内部拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
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
