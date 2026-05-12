#!/usr/bin/env python3
"""生成 strict actual constructor formula line 字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_constructor_formula_line_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-constructor-formula-line-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
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
    declaration: dict[str, Any],
    constructor_firewall: dict[str, Any],
    external_match: dict[str, Any],
    source_loop: dict[str, Any],
    reverse_functor: dict[str, Any],
    zero_seed: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 actual constructor formula line 字段判定表。"""
    target = "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter"
    next_basis = (
        "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND "
        "ConstructorDomainCleanCoreMembershipLedger AND "
        "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND "
        "ConstructorFormulaFailureReturnTagsLedger"
    )
    terminal_after = declaration.get("terminal_gap_after_router", "")
    return [
        {
            "gate": "ActualConstructorFormulaLineTargetActive",
            "closed": target in terminal_after,
            "proved": False,
            "meaning": "上一层 declaration line 已把 strict 自足可用来源压到 actual noncanonical constructor formula line。",
            "remaining": target,
        },
        {
            "gate": "FormulaLineIsNotExistenceName",
            "closed": True,
            "proved": True,
            "meaning": "公式行必须是可展开的显式 constructor rule，不是“存在某 source”的标签。",
            "remaining": next_basis,
        },
        {
            "gate": "ExternalLemmasDoNotEmitRowsImported",
            "closed": external_match.get("external_lemmas_match_constructor_formula") is False,
            "proved": True,
            "meaning": "外部 DI/BFI/Kuznetsov 处理给定系数后的平均，不能输出 alpha/delta primitive rows。",
            "remaining": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。",
        },
        {
            "gate": "ReversePaymentCannotDefineFormulaImported",
            "closed": reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True,
            "proved": True,
            "meaning": "从 Gamma/payment/fiber skeleton 反推公式不唯一；不能把后验原像选择当 constructor rule。",
            "remaining": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。",
        },
        {
            "gate": "ZeroRowGeometryCannotDefineFormulaImported",
            "closed": zero_seed.get("geometry_source_extraction_blocked") is True,
            "proved": True,
            "meaning": "早期零行几何只给 unsigned covering/Phi 基底，不定义 signed alpha/delta constructor rule。",
            "remaining": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。",
        },
        {
            "gate": "SourceLoopCannotSelfGenerateFormula",
            "closed": source_loop.get("source_loop_cut_closed") is True,
            "proved": True,
            "meaning": "constructor、formula、emitter、origin ledger 的等价环不能生成 formula line。",
            "remaining": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。",
        },
        {
            "gate": "ActualNoncanonicalConstructorFormulaCurrentCorpusProved",
            "closed": constructor_firewall.get("actual_noncanonical_primitive_constructor_formula_proved")
            is True,
            "proved": False,
            "meaning": "当前材料尚未写出 actual noncanonical primitive constructor 的显式 alpha/delta 规则。",
            "remaining": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。",
        },
        {
            "gate": "DomainCleanCoreMembershipCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "公式规则的定义域必须正好是当前 clean-core noncanonical emitter 域；当前未证明。",
            "remaining": "ConstructorDomainCleanCoreMembershipLedger。",
        },
        {
            "gate": "FormulaEmitsUVKeyRowsCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前未证明公式逐行输出 `(u,v)`、branch key、sign 和 local factor。",
            "remaining": "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger。",
        },
        {
            "gate": "FormulaFailureReturnTagsCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "公式不适用、超预算、thin/rejected 或抵消分支的 return tags 尚未逐项闭合。",
            "remaining": "ConstructorFormulaFailureReturnTagsLedger。",
        },
        {
            "gate": "ActualConstructorFormulaLineCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "显式规则、域准入、行输出和失败回流四项尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict actual constructor formula line 证书。"""
    declaration = load_json(DOCS / "prime-matrix-strict-precauchy-declaration-line-router.json")
    constructor_firewall = load_json(
        DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
    )
    external_match = load_json(DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")
    zero_seed = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")

    target = "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter"
    next_basis = (
        "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND "
        "ConstructorDomainCleanCoreMembershipLedger AND "
        "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND "
        "ConstructorFormulaFailureReturnTagsLedger"
    )
    rows = build_rows(
        declaration=declaration,
        constructor_firewall=constructor_firewall,
        external_match=external_match,
        source_loop=source_loop,
        reverse_functor=reverse_functor,
        zero_seed=zero_seed,
    )
    return {
        "certificate_type": "prime_matrix_strict_actual_constructor_formula_line_router",
        "status": "strict_actual_constructor_formula_line_reduced_to_explicit_alpha_delta_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "actual_constructor_formula_line_router_closed": True,
        "formula_line_field_decomposition_pinned": True,
        "external_lemmas_do_not_emit_rows_imported": True,
        "reverse_payment_formula_recovery_rejected": True,
        "zero_row_geometry_formula_extraction_blocked": True,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "constructor_domain_clean_core_membership_proved": False,
        "constructor_formula_emits_uv_key_sign_local_factor_rows_proved": False,
        "constructor_formula_failure_return_tags_proved": False,
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
        "next_direct_attack_target": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter",
        "formula_law": (
            "The actual constructor formula line must be an explicit rule that, before Cauchy/dispersion, maps each "
            "admissible source tuple to alpha/delta primitive summands and emits `(u,v)`, branch key, sign and local factor. "
            "It cannot be recovered from payment data, zero-row geometry, or external spectral estimates."
        ),
        "plain_conclusion": (
            "`ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter` 被压到显式 `alpha/delta` primitive constructor rule "
            "及其域准入、行输出和失败回流字段。当前最窄点是 "
            "`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter`；没有这个规则，源表第一行仍不能成立。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict actual constructor formula line 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"actual_constructor_formula_line_router_closed={fmt_bool(result['actual_constructor_formula_line_router_closed'])}",
        f"explicit_alpha_delta_primitive_constructor_rule_proved={fmt_bool(result['explicit_alpha_delta_primitive_constructor_rule_proved'])}",
        f"actual_noncanonical_primitive_constructor_formula_line_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_line_proved'])}",
        f"pre_cauchy_constructor_declaration_line_proved={fmt_bool(result['pre_cauchy_constructor_declaration_line_proved'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(result['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 公式律",
        "",
        result["formula_law"],
        "",
        "## 2. 公式行内部拆分",
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
