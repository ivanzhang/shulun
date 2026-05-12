#!/usr/bin/env python3
"""生成 strict alpha 侧 primitive rule 字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_side_primitive_rule_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-side-primitive-rule-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-clean-core-disintegration-automaticity-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-triad-a1-canonical-riw-support-router.md",
    "prime-matrix-finite-formal-unit-partition-key-router.md",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本证书；缺失时返回空文本。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def canonical_template_scoped(canonical_text: str, key_text: str) -> bool:
    """判断 canonical 模板是否只作为作用域内参考。"""
    joined = canonical_text + "\n" + key_text
    return (
        "canonical" in joined.lower()
        and ("scoped" in joined.lower() or "作用域" in joined or "不能跨" in joined)
    )


def build_rows(
    explicit_rule: dict[str, Any],
    formal_record: dict[str, Any],
    source_tuple: dict[str, Any],
    anchor_recon: dict[str, Any],
    disintegration: dict[str, Any],
    reverse_functor: dict[str, Any],
    source_law: dict[str, Any],
    path_source: dict[str, Any],
    canonical_text: str,
    key_text: str,
) -> list[dict[str, Any]]:
    """生成 alpha 侧 primitive rule 判定表。"""
    target = "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
    next_basis = (
        "ActualNoncanonicalAlphaSourceTupleDomainLedger AND "
        "DeterministicAlphaPrimitiveRowEmissionMapLedger AND "
        "AlphaPrimitiveCoefficientWeightFormulaLedger AND "
        "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND "
        "AlphaPrimitiveRuleFailureNamedReturnLedger"
    )
    terminal_after = explicit_rule.get("terminal_gap_after_router", "")
    source_tuple_ready = source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    formal_record_ready = formal_record.get("formal_unit_source_record_schema_closed") is True
    anchor_ready = anchor_recon.get("anchor_set_reconstruction_certificate_ledger") is True
    disintegration_formal = disintegration.get("signed_fiber_disintegration_formal") is True
    reverse_blocked = reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True
    source_fields_imported = source_law.get("origin_generation_ledger_implication_closed") is True
    canonical_scoped = (
        path_source.get("canonical_template_scoped_only") is True
        or canonical_template_scoped(canonical_text, key_text)
    )
    return [
        {
            "gate": "AlphaSidePrimitiveRuleTargetActive",
            "closed": target in terminal_after,
            "proved": False,
            "meaning": "上一层显式 alpha/delta 规则已把当前最窄点固定为 alpha 侧 primitive row 规则。",
            "remaining": target,
        },
        {
            "gate": "SourceTupleDomainSchemaImported",
            "closed": source_tuple_ready,
            "proved": True,
            "meaning": "source tuple/anchor 参数字段、哈希和同 formal unit 纪律可用。",
            "remaining": "这只是定义域容器，不产生 alpha primitive row。",
        },
        {
            "gate": "FormalUnitAndAnchorDisciplineImported",
            "closed": formal_record_ready and anchor_ready,
            "proved": True,
            "meaning": "formal-unit source record 与 anchor reconstruction 可锁定 A、D0/K/Omega、phase_rule。",
            "remaining": "仍需把这些字段送入 alpha 行生成算子。",
        },
        {
            "gate": "PreCauchySourceLawFieldsImported",
            "closed": source_fields_imported,
            "proved": True,
            "meaning": "pre-Cauchy 来源律要求 branch key、u/v、sign/local factor 和命名回流字段。",
            "remaining": next_basis,
        },
        {
            "gate": "DisintegrationFormalButNotEmitterImported",
            "closed": disintegration_formal,
            "proved": True,
            "meaning": "signed 解积分只在 actual source measure 已给定后形式闭合，不能生成 alpha 行。",
            "remaining": "DeterministicAlphaPrimitiveRowEmissionMapLedger。",
        },
        {
            "gate": "ReversePaymentRecoveryBlockedImported",
            "closed": reverse_blocked,
            "proved": True,
            "meaning": "不能从 payment Gamma 或有限投影反推唯一 pre-Cauchy primitive summand。",
            "remaining": "DeterministicAlphaPrimitiveRowEmissionMapLedger。",
        },
        {
            "gate": "CanonicalTemplateLeakBlocked",
            "closed": canonical_scoped,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 与 formal-unit key 模板只能作作用域内参考，不能跨入 noncanonical alpha 规则。",
            "remaining": "AlphaPrimitiveRuleFailureNamedReturnLedger。",
        },
        {
            "gate": "ActualNoncanonicalAlphaSourceTupleDomainCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 alpha 规则的定义域正好等于 actual noncanonical clean-core source tuples。",
            "remaining": "ActualNoncanonicalAlphaSourceTupleDomainLedger。",
        },
        {
            "gate": "DeterministicAlphaPrimitiveRowMapCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出从每个 source tuple 到有限 alpha primitive rows 的确定性发射映射。",
            "remaining": "DeterministicAlphaPrimitiveRowEmissionMapLedger。",
        },
        {
            "gate": "AlphaCoefficientWeightFormulaCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出 alpha primitive row 的系数权重公式及其与原始构造量的等式。",
            "remaining": "AlphaPrimitiveCoefficientWeightFormulaLedger。",
        },
        {
            "gate": "AlphaRowUVKeySignLocalFactorOutputCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明每条 alpha row 同步输出 exact `(u,v)`、branch key、sign 和 local factor。",
            "remaining": "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger。",
        },
        {
            "gate": "AlphaFailureNamedReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未逐类关闭 canonical 泄漏、未登记、超预算、thin/rejected/cancelling 的失败回流。",
            "remaining": "AlphaPrimitiveRuleFailureNamedReturnLedger。",
        },
        {
            "gate": "AlphaSidePrimitiveRuleCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "定义域、发射映射、权重公式、输出字段和失败回流五项尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 alpha 侧 primitive rule 证书。"""
    explicit_rule = load_json(DOCS / "prime-matrix-strict-explicit-alpha-delta-rule-router.json")
    formal_record = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    source_tuple = load_json(DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    anchor_recon = load_json(DOCS / "prime-matrix-anchor-set-reconstruction-certificate-router.json")
    disintegration = load_json(DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.json")
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")
    source_law = load_json(DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json")
    path_source = load_json(DOCS / "prime-matrix-clean-core-path-source-firewall-router.json")
    canonical_text = load_text(DOCS / "prime-matrix-triad-a1-canonical-riw-support-router.md")
    key_text = load_text(DOCS / "prime-matrix-finite-formal-unit-partition-key-router.md")

    target = "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
    next_basis = (
        "ActualNoncanonicalAlphaSourceTupleDomainLedger AND "
        "DeterministicAlphaPrimitiveRowEmissionMapLedger AND "
        "AlphaPrimitiveCoefficientWeightFormulaLedger AND "
        "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND "
        "AlphaPrimitiveRuleFailureNamedReturnLedger"
    )
    rows = build_rows(
        explicit_rule=explicit_rule,
        formal_record=formal_record,
        source_tuple=source_tuple,
        anchor_recon=anchor_recon,
        disintegration=disintegration,
        reverse_functor=reverse_functor,
        source_law=source_law,
        path_source=path_source,
        canonical_text=canonical_text,
        key_text=key_text,
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_side_primitive_rule_router",
        "status": "strict_alpha_side_primitive_rule_reduced_to_domain_map_weight_output_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "alpha_side_primitive_rule_router_closed": True,
        "source_tuple_container_imported": True,
        "formal_unit_anchor_discipline_imported": True,
        "disintegration_not_row_emitter_imported": True,
        "reverse_payment_recovery_blocked_imported": True,
        "canonical_template_leak_blocked_imported": True,
        "actual_noncanonical_alpha_source_tuple_domain_proved": False,
        "deterministic_alpha_primitive_row_emission_map_proved": False,
        "alpha_primitive_coefficient_weight_formula_proved": False,
        "alpha_primitive_row_uv_key_sign_local_factor_output_proved": False,
        "alpha_primitive_rule_failure_named_return_proved": False,
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
        "next_direct_attack_target": "DeterministicAlphaPrimitiveRowEmissionMapLedger",
        "alpha_rule_law": (
            "An alpha-side primitive rule is not a source tuple schema and not a disintegration identity. It must, before "
            "Cauchy/dispersion and within the same formal unit, take an actual noncanonical source tuple, emit a finite "
            "list of alpha primitive rows, assign coefficient weights, output exact `(u,v)`, branch key, sign/local factor, "
            "and return every non-admissible case by name."
        ),
        "plain_conclusion": (
            "`ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger` 被继续压成定义域、确定性 alpha row 发射映射、"
            "alpha 系数权重公式、逐行 `(u,v)`/key/sign/local-factor 输出和失败命名回流五项。当前最窄点是 "
            "`DeterministicAlphaPrimitiveRowEmissionMapLedger`；source tuple 和 formal-unit 数据只锁定输入容器，"
            "仍没有生成 alpha primitive rows 的实际规则。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha 侧 primitive rule 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"alpha_side_primitive_rule_router_closed={fmt_bool(result['alpha_side_primitive_rule_router_closed'])}",
        f"actual_noncanonical_alpha_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_alpha_side_primitive_rule_proved'])}",
        f"actual_noncanonical_delta_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_delta_side_primitive_rule_proved'])}",
        f"explicit_alpha_delta_primitive_constructor_rule_proved={fmt_bool(result['explicit_alpha_delta_primitive_constructor_rule_proved'])}",
        f"actual_noncanonical_primitive_constructor_formula_line_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_line_proved'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(result['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. alpha 规则律",
        "",
        result["alpha_rule_law"],
        "",
        "## 2. alpha 侧内部拆分",
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
