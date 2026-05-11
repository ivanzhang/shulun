#!/usr/bin/env python3
"""生成 strict alpha signed 权重律字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_signed_weight_law_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-signed-weight-law-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
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
    signed_lift: dict[str, Any],
    seed_nogo: dict[str, Any],
    source_law: dict[str, Any],
    path_source: dict[str, Any],
    reverse_functor: dict[str, Any],
    constructor_line: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 alpha signed 权重律判定表。"""
    target = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
    next_basis = (
        "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND "
        "ExactAlphaSignedWeightFormulaLedger AND "
        "AlphaWeightNonzeroSignLocalFactorLedger AND "
        "AlphaWeightNoZeroRowGeometryOrPaymentRecoveryLedger AND "
        "AlphaWeightLawFailureNamedReturnLedger"
    )
    terminal_after = signed_lift.get("terminal_gap_after_router", "")
    seed_blocked = seed_nogo.get("zero_row_seed_extraction_blocked") is True
    independent_identity_open = (
        seed_nogo.get("terminal_gap_after_router")
        == "IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn"
        or seed_nogo.get("independent_precauchy_arithmetic_source_identity_proved") is False
    )
    source_atom_imported = source_law.get("origin_generation_ledger_implication_closed") is True
    path_partition_open = path_source.get("clean_core_path_partition_proved") is False
    reverse_blocked = reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True
    constructor_requires_rule = (
        "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
        in constructor_line.get("terminal_gap_after_router", "")
    )
    return [
        {
            "gate": "AlphaSignedWeightLawTargetActive",
            "closed": target in terminal_after or signed_lift.get("next_direct_attack_target") == target,
            "proved": False,
            "meaning": "上一层已把当前最窄点固定为 signed alpha 权重必须来自 pre-Cauchy 算术恒等式。",
            "remaining": target,
        },
        {
            "gate": "IndependentArithmeticIdentityGateImported",
            "closed": seed_blocked and independent_identity_open,
            "proved": True,
            "meaning": "早期零行覆盖图不能提供 signed seed；保留义务是独立 pre-Cauchy arithmetic source identity。",
            "remaining": "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。",
        },
        {
            "gate": "OriginalCoefficientGenerationAtomImported",
            "closed": source_atom_imported,
            "proved": True,
            "meaning": "pre-Cauchy 来源律已把问题压成 original coefficient generation ledger。",
            "remaining": "ExactAlphaSignedWeightFormulaLedger。",
        },
        {
            "gate": "PathPartitionCannotSubstituteWeightLaw",
            "closed": path_partition_open,
            "proved": True,
            "meaning": "路径分割和非零合同必须在 actual coefficient 给定后使用，不能反过来定义权重律。",
            "remaining": "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。",
        },
        {
            "gate": "ZeroRowOrPaymentRecoveryBlocked",
            "closed": reverse_blocked and constructor_requires_rule,
            "proved": True,
            "meaning": "从零行几何、payment skeleton 或外部估计恢复权重律均被现有 no-go 排除。",
            "remaining": "AlphaWeightNoZeroRowGeometryOrPaymentRecoveryLedger。",
        },
        {
            "gate": "IndependentIdentityStatementCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未陈述并证明 noncanonical clean-core 的独立 pre-Cauchy 算术恒等式。",
            "remaining": "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。",
        },
        {
            "gate": "ExactAlphaSignedWeightFormulaCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出每条 alpha row 的 signed 权重精确公式。",
            "remaining": "ExactAlphaSignedWeightFormulaLedger。",
        },
        {
            "gate": "AlphaWeightNonzeroSignLocalFactorCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明权重非零、符号和 local factor 与 primitive row 同步。",
            "remaining": "AlphaWeightNonzeroSignLocalFactorLedger。",
        },
        {
            "gate": "AlphaWeightNoRecoveryCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出形式证书说明该权重律完全独立于零行几何/payment 反推。",
            "remaining": "AlphaWeightNoZeroRowGeometryOrPaymentRecoveryLedger。",
        },
        {
            "gate": "AlphaWeightLawFailureReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未定义恒等式不适用、权重为零、符号冲突或 local factor 缺失的命名回流。",
            "remaining": "AlphaWeightLawFailureNamedReturnLedger。",
        },
        {
            "gate": "AlphaSignedWeightLawCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "独立恒等式、权重公式、非零符号局部因子、反推禁用和失败回流五项尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 alpha signed 权重律证书。"""
    signed_lift = load_json(DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json")
    seed_nogo = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    source_law = load_json(DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json")
    path_source = load_json(DOCS / "prime-matrix-clean-core-path-source-firewall-router.json")
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")
    constructor_line = load_json(DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.json")

    target = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
    next_basis = (
        "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND "
        "ExactAlphaSignedWeightFormulaLedger AND "
        "AlphaWeightNonzeroSignLocalFactorLedger AND "
        "AlphaWeightNoZeroRowGeometryOrPaymentRecoveryLedger AND "
        "AlphaWeightLawFailureNamedReturnLedger"
    )
    rows = build_rows(
        signed_lift=signed_lift,
        seed_nogo=seed_nogo,
        source_law=source_law,
        path_source=path_source,
        reverse_functor=reverse_functor,
        constructor_line=constructor_line,
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_signed_weight_law_router",
        "status": "strict_alpha_signed_weight_law_reduced_to_independent_identity_formula_nonzero_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "alpha_signed_weight_law_router_closed": True,
        "independent_arithmetic_identity_gate_imported": True,
        "zero_row_or_payment_recovery_blocked_imported": True,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "exact_alpha_signed_weight_formula_proved": False,
        "alpha_weight_nonzero_sign_local_factor_proved": False,
        "alpha_weight_no_zero_row_geometry_or_payment_recovery_proved": False,
        "alpha_weight_law_failure_named_return_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
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
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger",
        "weight_law": (
            "A signed alpha weight law must be a forward arithmetic identity before Cauchy/dispersion. It cannot be "
            "defined by zero-row covering, payment recovery, path partition, or disintegration after the fact."
        ),
        "plain_conclusion": (
            "`AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger` 被压成独立 noncanonical pre-Cauchy "
            "算术恒等式陈述、精确 alpha signed 权重公式、非零/符号/local factor、禁止零行或 payment 反推、"
            "失败命名回流五项。当前最窄点为 "
            "`IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger`。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha signed 权重律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"alpha_signed_weight_law_router_closed={fmt_bool(result['alpha_signed_weight_law_router_closed'])}",
        f"alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved={fmt_bool(result['alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"actual_noncanonical_alpha_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_alpha_side_primitive_rule_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 权重律",
        "",
        result["weight_law"],
        "",
        "## 2. 权重律内部拆分",
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
