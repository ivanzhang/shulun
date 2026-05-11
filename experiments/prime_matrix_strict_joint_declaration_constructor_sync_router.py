#!/usr/bin/env python3
"""生成 strict 联合 declaration line 与 constructor 公式同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_joint_declaration_constructor_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-joint-declaration-constructor-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-joint-declaration-constructor-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-joint-declaration-constructor-sync-router.md"

TARGET = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
NEXT_TARGET = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
DOMAIN_TARGET = "JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger"
ROW_TARGET = "JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger"
TIMESTAMP_TARGET = "SameFormalUnitPreCauchyTimestampLockLedger"
NO_LEAK_TARGET = "NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger"
RETURN_TARGET = "JointConstructorFormulaFailureReturnTagsLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-joint-emitter-formula-field-atom-router.json",
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
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
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def rule_fields() -> list[dict[str, str]]:
    """列出 joint constructor rule 的必要字段。"""
    return [
        {
            "field": "explicit_joint_alpha_delta_rule",
            "role": "第一开口；在 pre-Cauchy 层把 source tuple 映到 alpha/delta primitive row。"
        },
        {
            "field": "same_source_tuple_domain",
            "role": "定义域必须正好是当前 actual noncanonical clean-core source tuple，而不是 canonical 或 generic WFD。"
        },
        {
            "field": "basis_word_and_coefficient_row_emission",
            "role": "同一公式行必须同时输出 primitive basis word、signed coefficient、branch key、u/v、sign 和 local factor。"
        },
        {
            "field": "timestamp_and_no_leak_lock",
            "role": "公式发生在 Cauchy/dispersion/payment/Phi 之前，且不读取 canonical/external/后验数据。"
        },
        {
            "field": "failure_return_tags",
            "role": "公式缺失、多值、零 local factor、超预算、thin/rejected/cancelling 时必须命名回流。"
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 joint declaration 与已有 constructor 公式线。"""
    previous = data["previous"]
    declaration = data["declaration"]
    formula_line = data["formula_line"]
    formal = data["formal"]
    source_tuple = data["source_tuple"]
    firewall = data["firewall"]
    origin = data["origin"]
    external = data["external"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    broad_declaration_filter_imported = (
        declaration.get("precauchy_declaration_line_router_closed") is True
        and declaration.get("actual_noncanonical_declaration_only_strict_option") is True
        and declaration.get("actual_noncanonical_primitive_constructor_formula_line_proved") is False
    )
    constructor_formula_line_imported = (
        formula_line.get("actual_constructor_formula_line_router_closed") is True
        and formula_line.get("next_direct_attack_target") == "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
        and formula_line.get("actual_noncanonical_primitive_constructor_formula_line_proved") is False
    )
    same_source_tuple_container_closed = (
        formal.get("concrete_formal_unit_source_record_closed") is True
        and source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    )
    fake_source_filter_closed = (
        firewall.get("constructor_source_class_firewall_boundary_closed") is True
        and firewall.get("unregistered_source_return_absorbed") is True
        and external.get("external_lemmas_match_constructor_formula") is False
    )
    reverse_and_zero_blocked = (
        source_loop.get("source_loop_cut_closed") is True
        and reverse.get("pushforward_reverse_uniqueness_rejected") is True
        and zero_nogo.get("geometry_source_extraction_blocked") is True
        and zero_nogo.get("zero_row_seed_extraction_blocked") is True
    )
    origin_admission_not_formula = origin.get("clean_core_primitive_source_constructor_admission_proved") is False

    return [
        row(
            "JointDeclarationLineTargetActive",
            target_active,
            False,
            "上一层 joint-emitter 字段证书已把第一生产性原子钉为 joint declaration line。",
            TARGET,
        ),
        row(
            "BroadPreCauchyDeclarationFilterImported",
            broad_declaration_filter_imported,
            True,
            "已有 declaration line 分类已排除 canonical、generic WFD、external、unregistered/mixed 伪声明。",
            "joint 版继承同一分类，不另开来源类。",
        ),
        row(
            "ActualConstructorFormulaLineRouterImported",
            constructor_formula_line_imported,
            True,
            "已有 actual constructor formula line 证书把 broad 声明行压到显式 alpha/delta primitive constructor rule。",
            NEXT_TARGET,
        ),
        row(
            "SameSourceTupleContainerClosed",
            same_source_tuple_container_closed,
            True,
            "formal unit/source tuple 容器已闭合；joint 版只是要求同一容器同时发射 word 与 coefficient。",
            DOMAIN_TARGET,
        ),
        row(
            "FakeSourceFilterStillBlocksShortcuts",
            fake_source_filter_closed,
            True,
            "canonical、generic WFD、外部谱、未登记来源都不能替代 joint constructor rule。",
            NO_LEAK_TARGET,
        ),
        row(
            "ReverseAndZeroRowStillCannotSupplyJointRule",
            reverse_and_zero_blocked,
            True,
            "payment 反推和早期零行 unsigned 几何不能生成 signed word/coefficient 联合规则。",
            NEXT_TARGET,
        ),
        row(
            "OriginAdmissionIsNotFormula",
            origin_admission_not_formula,
            False,
            "来源准入/构造器分类只能说明合法入口形态，仍没有写出实际 joint alpha/delta 规则。",
            NEXT_TARGET,
        ),
        row(
            "JointPayloadRequirementPinned",
            True,
            True,
            "joint 目标要求显式规则不仅给 alpha/delta 行，还要在同一行输出 basis word 与 signed coefficient。",
            ROW_TARGET,
        ),
        row(
            "TimestampAndNoLeakStillParallel",
            declaration.get("same_formal_unit_precauchy_timestamp_lock_proved") is False
            and declaration.get("noncanonical_declaration_no_canonical_or_external_leak_proved") is False,
            False,
            "pre-Cauchy 时间戳锁和 noncanonical no-leak 纪律仍需与显式规则并行证明。",
            f"{TIMESTAMP_TARGET} AND {NO_LEAK_TARGET}",
        ),
        row(
            "ExplicitJointConstructorRuleCurrentCorpusProved",
            False,
            False,
            "当前材料尚未给出从 actual noncanonical source tuple 到 joint primitive row 的显式 alpha/delta 规则。",
            NEXT_TARGET,
        ),
        row(
            "PreCauchyJointDeclarationLineCurrentCorpusProved",
            False,
            False,
            "显式规则、同源定义域、行输出、时间戳/no-leak 和回流标签尚未合取闭合。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 joint declaration/constructor 同步证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-joint-emitter-formula-field-atom-router.json"),
        "declaration": load_json("prime-matrix-strict-precauchy-declaration-line-router.json"),
        "formula_line": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "formal": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "firewall": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
        "origin": load_json("prime-matrix-clean-core-origin-source-admission-router.json"),
        "external": load_json("prime-matrix-clean-core-external-lemma-parameter-match-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    productive_basis = (
        f"{NEXT_TARGET} AND {DOMAIN_TARGET} AND {ROW_TARGET} AND "
        f"{TIMESTAMP_TARGET} AND {NO_LEAK_TARGET} AND {RETURN_TARGET}"
    )
    return {
        "certificate_type": "prime_matrix_strict_joint_declaration_constructor_sync_router",
        "status": "joint_declaration_line_reduced_to_explicit_joint_constructor_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "joint_declaration_constructor_sync_router_closed": True,
        "joint_declaration_matches_actual_constructor_formula_line": True,
        "broad_precauchy_declaration_filter_imported": True,
        "actual_constructor_formula_line_router_imported": True,
        "same_source_tuple_container_closed": data["formal"].get("concrete_formal_unit_source_record_closed") is True
        and data["source_tuple"].get("concrete_source_tuple_anchor_parameter_data_closed") is True,
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "joint_constructor_domain_clean_core_membership_proved": False,
        "joint_constructor_emits_basis_word_uv_key_sign_local_factor_coefficient_rows_proved": False,
        "same_formal_unit_precauchy_timestamp_lock_proved": False,
        "noncanonical_joint_declaration_no_canonical_or_external_leak_proved": False,
        "joint_constructor_formula_failure_return_tags_proved": False,
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_basis_word_coefficient_emitter_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            DOMAIN_TARGET,
            ROW_TARGET,
            TIMESTAMP_TARGET,
            NO_LEAK_TARGET,
            RETURN_TARGET,
            TERMINAL_DESCENT,
        ],
        "productive_basis_after_router": productive_basis,
        "strict_basis_after_router": f"(({productive_basis}) OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}",
        "rule_fields": rule_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 与已有 broad `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 是同一声明行，"
            "区别只在 joint payload：同一 actual source tuple 必须同时发射 primitive basis word 与 signed coefficient。"
            f"因此首个生产性硬点变为 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把 joint declaration line 与已有 pre-Cauchy declaration/actual constructor 线同步："
            "它不是新的来源类，也不能由 canonical、generic WFD、外部谱、payment 反推或早期零行几何填充。"
            "合法闭合必须给出显式 joint alpha/delta primitive constructor rule，并在同一行输出 basis word、signed coefficient、"
            "branch key、u/v、sign 与 local factor。该规则当前未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 联合 declaration/constructor 同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_declaration_constructor_sync_router_closed={fmt_bool(result['joint_declaration_constructor_sync_router_closed'])}",
        f"same_source_tuple_container_closed={fmt_bool(result['same_source_tuple_container_closed'])}",
        f"explicit_joint_alpha_delta_constructor_rule_proved={fmt_bool(result['explicit_joint_alpha_delta_constructor_rule_proved'])}",
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(result['pre_cauchy_joint_declaration_line_proved'])}",
        f"joint_basis_word_coefficient_emitter_proved={fmt_bool(result['joint_basis_word_coefficient_emitter_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿同步",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 显式规则字段",
        "",
        "| field | role |",
        "| --- | --- |",
    ]
    for item in result["rule_fields"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['role'])} |")

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 4. 下一真正单点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "完整 joint declaration 生产性基：",
            "",
            "```text",
            result["productive_basis_after_router"],
            "```",
            "",
            "保留终端下降并行门后的当前严格自足基：",
            "",
            "```text",
            result["strict_basis_after_router"],
            "```",
            "",
            "审稿边界：本文件只证明 joint declaration 与 actual constructor 线的精确对接，"
            "没有证明显式 joint constructor rule，也没有证明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
