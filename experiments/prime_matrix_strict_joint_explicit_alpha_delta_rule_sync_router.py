#!/usr/bin/env python3
"""生成 strict joint 显式 alpha/delta 规则同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_joint_explicit_alpha_delta_rule_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.md"

TARGET = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
NEXT_TARGET = "JointAlphaSidePrimitiveWordCoefficientRuleLedger"
DELTA_TARGET = "JointDeltaSidePrimitiveWordCoefficientRuleLedger"
PAIRING_TARGET = "JointAlphaDeltaPairingCompatibilityBeforeCauchyLedger"
NONZERO_TARGET = "JointPrimitiveWordCoefficientNonzeroSignLocalFactorLedger"
RETURN_TARGET = "JointAlphaDeltaRuleFailureNamedReturnLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
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


def joint_rule_fields() -> list[dict[str, str]]:
    """列出 joint alpha/delta 规则的字段。"""
    return [
        {
            "field": "joint_alpha_side_rule",
            "meaning": "从同一 source tuple 正向发射 alpha-side primitive basis word、signed coefficient 与 row payload。"
        },
        {
            "field": "joint_delta_side_rule",
            "meaning": "从同一 source tuple 正向发射 delta-side primitive basis word、signed coefficient 与 row payload。"
        },
        {
            "field": "same_word_coefficient_payload",
            "meaning": "每条 primitive row 的 word、coefficient、branch key、u/v、sign 和 local factor 同时产生。"
        },
        {
            "field": "pre_cauchy_pairing_identity",
            "meaning": "alpha/delta 两侧在 Cauchy 前配对为同一个 actual emitter 系数。"
        },
        {
            "field": "nonzero_and_return_discipline",
            "meaning": "零 local factor、符号冲突、多值、超预算、后验读取或 unmatched pair 必须命名回流。"
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 joint 显式规则与已有 alpha/delta 两侧拆分。"""
    previous = data["previous"]
    explicit = data["explicit"]
    alpha_side = data["alpha_side"]
    alpha_map = data["alpha_map"]
    unsigned = data["unsigned"]
    anchor_formula = data["anchor_formula"]
    signed_weight = data["signed_weight"]
    pointwise_weight = data["pointwise_weight"]
    formal = data["formal"]
    source_tuple = data["source_tuple"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    broad_two_side_split_imported = (
        explicit.get("explicit_alpha_delta_rule_router_closed") is True
        and explicit.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False
        and explicit.get("next_direct_attack_target") == "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
    )
    source_tuple_container_ready = (
        formal.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    alpha_side_open = (
        alpha_side.get("actual_noncanonical_alpha_side_primitive_rule_proved") is False
        or alpha_map.get("deterministic_alpha_primitive_row_emission_map_proved") is False
    )
    unsigned_alpha_material_imported = (
        unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
        or anchor_formula.get("alpha_row_anchor_phase_formula_router_closed") is True
    )
    signed_payload_open = (
        signed_weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False
        or pointwise_weight.get("primitive_summand_signed_weight_expression_proved") is False
    )
    downstream_blocked = (
        reverse.get("pushforward_reverse_uniqueness_rejected") is True
        and zero_nogo.get("zero_row_seed_extraction_blocked") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "ExplicitJointRuleTargetActive",
            target_active,
            False,
            "上一层 joint declaration/constructor 同步已把首个生产性公式压成 explicit joint alpha/delta rule。",
            TARGET,
        ),
        row(
            "BroadAlphaDeltaTwoSideSplitImported",
            broad_two_side_split_imported,
            True,
            "已有显式 alpha/delta 规则证书说明普通规则必须拆成 alpha-side、delta-side、pairing 和 nonzero/sign/local factor。",
            "joint 版继承此两侧结构。",
        ),
        row(
            "SourceTupleContainerStillOnlyContainer",
            source_tuple_container_ready,
            True,
            "formal unit/source tuple 只给输入容器和锚参数，不自动给 primitive row 规则。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedAlphaGeometryImportedButNotSignedPayload",
            unsigned_alpha_material_imported,
            True,
            "carry-shell、anchor/phase、P列锚与层叠轮等 unsigned alpha 几何可登记，但不产生 signed coefficient。",
            "signed payload 仍需 joint alpha-side 规则。",
        ),
        row(
            "AlphaSideGenericRuleStillOpen",
            alpha_side_open,
            False,
            "普通 alpha-side primitive rule 和 deterministic alpha row emission map 尚未证明。",
            NEXT_TARGET,
        ),
        row(
            "SignedPayloadStillOpen",
            signed_payload_open,
            False,
            "alpha signed weight law 与逐点 signed weight expression 仍未给出 exact signed coefficient。",
            NEXT_TARGET,
        ),
        row(
            "DownstreamRecoveryStillBlocked",
            downstream_blocked,
            True,
            "payment 反推、零行覆盖和终端证书不能替代 joint alpha/delta 规则。",
            RETURN_TARGET,
        ),
        row(
            "JointRuleNeedsPayloadStrongerThanBroadRule",
            True,
            True,
            "joint 规则比普通 alpha/delta 规则更强：每侧发射时必须同时带 basis word 与 signed coefficient payload。",
            NEXT_TARGET,
        ),
        row(
            "JointAlphaSidePrimitiveRuleCurrentCorpusProved",
            False,
            False,
            "当前材料尚未给出 source tuple 到 alpha-side joint primitive word/coefficient row 的正向规则。",
            NEXT_TARGET,
        ),
        row(
            "ExplicitJointAlphaDeltaRuleCurrentCorpusProved",
            False,
            False,
            "缺 joint alpha-side 首规则时，delta-side、pairing、nonzero/local factor 和回流不能合取闭合。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 joint 显式 alpha/delta 规则同步证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-joint-declaration-constructor-sync-router.json"),
        "explicit": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "alpha_side": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "alpha_map": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "anchor_formula": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "signed_weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "pointwise_weight": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "formal": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    productive_basis = (
        f"{NEXT_TARGET} AND {DELTA_TARGET} AND {PAIRING_TARGET} AND "
        f"{NONZERO_TARGET} AND {RETURN_TARGET}"
    )
    return {
        "certificate_type": "prime_matrix_strict_joint_explicit_alpha_delta_rule_sync_router",
        "status": "explicit_joint_alpha_delta_rule_reduced_to_joint_alpha_side_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "joint_explicit_alpha_delta_rule_sync_router_closed": True,
        "broad_alpha_delta_two_side_split_imported": True,
        "source_tuple_container_imported_but_not_rule": True,
        "unsigned_alpha_geometry_imported_but_not_signed_payload": True,
        "joint_alpha_side_primitive_word_coefficient_rule_proved": False,
        "joint_delta_side_primitive_word_coefficient_rule_proved": False,
        "joint_alpha_delta_pairing_compatibility_before_cauchy_proved": False,
        "joint_primitive_word_coefficient_nonzero_sign_local_factor_proved": False,
        "joint_alpha_delta_rule_failure_named_return_proved": False,
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_basis_word_coefficient_emitter_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            DELTA_TARGET,
            PAIRING_TARGET,
            NONZERO_TARGET,
            RETURN_TARGET,
            TERMINAL_DESCENT,
        ],
        "productive_basis_after_router": productive_basis,
        "strict_basis_after_router": f"(({productive_basis}) OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}",
        "joint_rule_fields": joint_rule_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 不是普通 alpha/delta 规则的简单复述；它要求 alpha/delta 两侧每条 primitive row "
            "都携带同一 source tuple 下的 basis word 与 signed coefficient payload。"
            f"因此第一真正单点压成 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把 explicit joint alpha/delta rule 与已有普通 explicit alpha/delta 两侧拆分同步："
            "source tuple 与 unsigned alpha 几何只能提供输入和骨架，不能生成 signed payload。"
            "joint 规则必须先给 alpha-side 的 primitive word/coefficient 正向发射规则；没有它，"
            "delta-side、Cauchy 前配对、非零/local factor 和回流都无对象。当前仍未闭合行/列命题。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict joint 显式 alpha/delta 规则同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_explicit_alpha_delta_rule_sync_router_closed={fmt_bool(result['joint_explicit_alpha_delta_rule_sync_router_closed'])}",
        f"joint_alpha_side_primitive_word_coefficient_rule_proved={fmt_bool(result['joint_alpha_side_primitive_word_coefficient_rule_proved'])}",
        f"explicit_joint_alpha_delta_constructor_rule_proved={fmt_bool(result['explicit_joint_alpha_delta_constructor_rule_proved'])}",
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(result['pre_cauchy_joint_declaration_line_proved'])}",
        f"joint_basis_word_coefficient_emitter_proved={fmt_bool(result['joint_basis_word_coefficient_emitter_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. joint 规则字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["joint_rule_fields"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")

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
            "完整 joint explicit alpha/delta 生产性基：",
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
            "审稿边界：本文件只完成 joint 显式规则的两侧同步和首字段定位；"
            "没有证明 joint alpha-side 规则，也没有证明行/列命题无条件闭合。",
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
