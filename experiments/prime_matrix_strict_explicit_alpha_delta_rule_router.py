#!/usr/bin/env python3
"""生成 strict 显式 alpha/delta 构造规则字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_explicit_alpha_delta_rule_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-explicit-alpha-delta-rule-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-explicit-alpha-delta-rule-router.json"
OUT_MD = DOCS / "prime-matrix-strict-explicit-alpha-delta-rule-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-disintegration-automaticity-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
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
    formula_line: dict[str, Any],
    source_law: dict[str, Any],
    path_source: dict[str, Any],
    alpha_delta: dict[str, Any],
    disintegration_auto: dict[str, Any],
    source_record: dict[str, Any],
    source_tuple: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成显式 alpha/delta 规则字段判定表。"""
    target = "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
    next_basis = (
        "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND "
        "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND "
        "AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND "
        "PrimitiveRuleNonzeroSignLocalFactorLedger"
    )
    terminal_after = formula_line.get("terminal_gap_after_router", "")
    return [
        {
            "gate": "ExplicitAlphaDeltaRuleTargetActive",
            "closed": target in terminal_after,
            "proved": False,
            "meaning": "上一层 actual constructor formula line 已把当前最窄点压成显式 alpha/delta primitive constructor rule。",
            "remaining": target,
        },
        {
            "gate": "SourceRecordSchemaAvailableButNotRule",
            "closed": source_record.get("formal_unit_source_record_schema_closed") is True,
            "proved": True,
            "meaning": "formal unit source record 和 source tuple 字段可用，但它们只给参数容器，不给 alpha/delta 生成算子。",
            "remaining": "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger。",
        },
        {
            "gate": "SourceTupleParametersAvailableButNotRows",
            "closed": source_tuple.get("concrete_source_tuple_anchor_parameter_closed") is True
            or source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True,
            "proved": True,
            "meaning": "source tuple/anchor 参数账本可复算几何参数；不能自动生成 signed primitive rows。",
            "remaining": "两侧 primitive rule。",
        },
        {
            "gate": "PreCauchySourceLawFieldImported",
            "closed": source_law.get("origin_generation_ledger_implication_closed") is True,
            "proved": True,
            "meaning": "pre-Cauchy 来源律已说明规则必须输出 branch key、u/v、sign、local factor 和回流。",
            "remaining": next_basis,
        },
        {
            "gate": "PathPartitionCannotReplaceRule",
            "closed": path_source.get("clean_core_path_partition_proved") is False,
            "proved": True,
            "meaning": "路径分割依赖已有 alpha/delta 规则；不能反过来作为规则本身。",
            "remaining": next_basis,
        },
        {
            "gate": "DisintegrationFormalButNeedsMeasure",
            "closed": disintegration_auto.get("signed_fiber_disintegration_formal") is True
            or alpha_delta.get("alpha_delta_disintegration_boundary_closed") is True,
            "proved": True,
            "meaning": "给定 signed source 后解积分形式闭合；但该形式步骤不生成 actual noncanonical signed source measure。",
            "remaining": "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger。",
        },
        {
            "gate": "AlphaSideRuleCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料未给出 source tuple 到 alpha-side primitive summand 的确定性规则。",
            "remaining": "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger。",
        },
        {
            "gate": "DeltaSideRuleCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料未给出 source tuple 到 delta-side primitive summand 的确定性规则。",
            "remaining": "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger。",
        },
        {
            "gate": "PairingCompatibilityCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料未证明 alpha/delta 两侧规则在 Cauchy 前配对成同一个 actual emitter 系数。",
            "remaining": "AlphaDeltaPairingCompatibilityBeforeCauchyLedger。",
        },
        {
            "gate": "PrimitiveRuleNonzeroSignLocalFactorCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料未证明每条 primitive row 的非零、符号和 local factor 规则。",
            "remaining": "PrimitiveRuleNonzeroSignLocalFactorLedger。",
        },
        {
            "gate": "ExplicitAlphaDeltaRuleCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "两侧规则、配对兼容和行级非零/符号/local factor 尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造显式 alpha/delta 规则证书。"""
    formula_line = load_json(DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.json")
    source_law = load_json(DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json")
    path_source = load_json(DOCS / "prime-matrix-clean-core-path-source-firewall-router.json")
    alpha_delta = load_json(DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json")
    disintegration_auto = load_json(DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.json")
    source_record = load_json(DOCS / "prime-matrix-formal-unit-source-record-router.json")
    source_tuple = load_json(DOCS / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")

    target = "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
    next_basis = (
        "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND "
        "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND "
        "AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND "
        "PrimitiveRuleNonzeroSignLocalFactorLedger"
    )
    rows = build_rows(
        formula_line=formula_line,
        source_law=source_law,
        path_source=path_source,
        alpha_delta=alpha_delta,
        disintegration_auto=disintegration_auto,
        source_record=source_record,
        source_tuple=source_tuple,
    )
    return {
        "certificate_type": "prime_matrix_strict_explicit_alpha_delta_rule_router",
        "status": "strict_explicit_alpha_delta_rule_reduced_to_two_side_rules_pairing_nonzero_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "explicit_alpha_delta_rule_router_closed": True,
        "source_tuple_container_imported": True,
        "disintegration_formal_not_rule_imported": True,
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
        "next_direct_attack_target": "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger",
        "rule_law": (
            "A genuine alpha/delta primitive constructor rule must be two-sided: one rule emits alpha-side primitive rows, "
            "one emits delta-side primitive rows, and a pre-Cauchy pairing identity proves they form the actual emitter "
            "coefficient. Source tuples and formal-unit records are only containers; signed disintegration is formal only "
            "after the source measure exists."
        ),
        "plain_conclusion": (
            "`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` 被继续压成 alpha-side 规则、"
            "delta-side 规则、Cauchy 前配对兼容和 primitive row 非零/符号/local factor 四项。当前最窄点是 "
            "`ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger`；没有 alpha 侧行生成规则，显式构造规则不能开始。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 显式 alpha/delta 规则路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"explicit_alpha_delta_rule_router_closed={fmt_bool(result['explicit_alpha_delta_rule_router_closed'])}",
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
        "## 1. 规则律",
        "",
        result["rule_law"],
        "",
        "## 2. 显式规则内部拆分",
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
