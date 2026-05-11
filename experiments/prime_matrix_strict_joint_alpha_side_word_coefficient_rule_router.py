#!/usr/bin/env python3
"""生成 strict joint alpha-side word/coefficient 规则路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_joint_alpha_side_word_coefficient_rule_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"
OUT_MD = DOCS / "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.md"

TARGET = "JointAlphaSidePrimitiveWordCoefficientRuleLedger"
NEXT_TARGET = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
WORD_BINDING = "JointAlphaCarryShellSkeletonToPrimitiveBasisWordBindingLedger"
SIGNED_IDENTITY = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
UV_PAYLOAD = "JointAlphaPrimitiveRowUVKeySignLocalFactorOutputLedger"
OVERLOAD_RETURN = "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"
FAILURE_RETURN = "JointAlphaSideRuleFailureNamedReturnLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
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


def bridge_fields() -> list[dict[str, str]]:
    """列出 same-row word/coefficient 桥接字段。"""
    return [
        {
            "field": "same_source_tuple_row_id",
            "meaning": "同一 formal unit/source tuple 下的 alpha primitive row 标识。",
        },
        {
            "field": "carry_shell_word_binding",
            "meaning": "把 unsigned carry-shell/anchor/phase skeleton 绑定为 primitive basis word。",
        },
        {
            "field": "signed_coefficient_origin_identity",
            "meaning": "同一行给出 signed coefficient 的 pre-Cauchy 来源恒等式。",
        },
        {
            "field": "uv_key_sign_local_factor_payload",
            "meaning": "同一行同步输出 exact `(u,v)`、branch key、sign 和 local factor。",
        },
        {
            "field": "prepushforward_validity",
            "meaning": "word 与 coefficient 在 Phi/payment 推前之前已经同源成立。",
        },
        {
            "field": "named_return",
            "meaning": "缺 word、缺 coefficient、零 local factor、过载、后验读取或跨来源泄漏必须命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 joint alpha-side 规则的下一原子。"""
    previous = data["previous"]
    alpha_side = data["alpha_side"]
    alpha_map = data["alpha_map"]
    anchor_phase = data["anchor_phase"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    pointwise_weight = data["pointwise_weight"]
    signed_expr = data["signed_expr"]
    kernel = data["kernel"]
    formal = data["formal"]
    source_tuple = data["source_tuple"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    broad_alpha_rule_imported = (
        alpha_side.get("alpha_side_primitive_rule_router_closed") is True
        and alpha_side.get("actual_noncanonical_alpha_side_primitive_rule_proved") is False
    )
    deterministic_map_open = (
        alpha_map.get("deterministic_alpha_row_emission_map_router_closed") is True
        and alpha_map.get("deterministic_alpha_primitive_row_emission_map_proved") is False
    )
    unsigned_skeleton_registered = (
        unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
        and unsigned.get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
    )
    signed_side_open = (
        signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False
        and pointwise_weight.get("primitive_summand_signed_weight_expression_proved") is False
        and signed_expr.get("origin_identity_proved") is not True
    )
    signed_expr_to_origin = (
        signed_expr.get("next_direct_attack_target") == SIGNED_IDENTITY
        and signed_expr.get("primitive_summand_signed_expression_router_closed") is True
    )
    same_source_tuple_closed = (
        formal.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    downstream_blocked = (
        source_loop.get("circular_reverse_derivation_rejected") is True
        and reverse.get("pushforward_reverse_uniqueness_rejected") is True
        and zero_nogo.get("zero_row_seed_extraction_blocked") is True
    )
    kernel_requires_same_rows = (
        kernel.get("pointwise_kernel_table_router_closed") is True
        and kernel.get("pointwise_primitive_kernel_table_proved") is False
    )

    return [
        row(
            "JointAlphaSideTargetActive",
            target_active,
            False,
            "上一层 joint explicit alpha/delta 规则已把首字段压成 joint alpha-side word/coefficient rule。",
            TARGET,
        ),
        row(
            "BroadAlphaSideRuleImported",
            broad_alpha_rule_imported,
            True,
            "普通 alpha-side primitive rule 已拆成定义域、发射映射、权重公式、row payload 和回流。",
            "joint 版需要把 word 与 coefficient 同行合并。",
        ),
        row(
            "DeterministicAlphaMapStillOpen",
            deterministic_map_open,
            False,
            "确定性 alpha row map 仍未给出完整 row 发射，但后续 unsigned skeleton 已说明几何骨架可登记。",
            WORD_BINDING,
        ),
        row(
            "UnsignedCarryShellSkeletonRegistered",
            unsigned_skeleton_registered,
            True,
            "carry-shell、P列锚、anchor-collar 和 layered-wheel 已给出 alpha row 的 unsigned skeleton。",
            "只给 word/skeleton 形状，不给 signed coefficient。",
        ),
        row(
            "AnchorPhaseFormulaStillNeedsSignedLiftAndReturn",
            anchor_phase.get("alpha_row_anchor_phase_formula_router_closed") is True
            and anchor_phase.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "alpha anchor/phase 公式已压到 signed coefficient lift 与 anchor-collar overload return。",
            f"{SIGNED_IDENTITY} AND {OVERLOAD_RETURN}",
        ),
        row(
            "SignedExpressionReducedToOriginIdentity",
            signed_expr_to_origin,
            False,
            "逐 summand signed expression 已被压成 signed coefficient origin identity。",
            SIGNED_IDENTITY,
        ),
        row(
            "SignedPayloadStillOpen",
            signed_side_open,
            False,
            "signed lift、逐点 signed weight expression 和 origin identity 都未证明。",
            SIGNED_IDENTITY,
        ),
        row(
            "SameSourceTupleContainerAvailable",
            same_source_tuple_closed,
            True,
            "formal unit/source tuple 容器可用于同行绑定 word 与 coefficient。",
            "容器不是桥接证明。",
        ),
        row(
            "PointwiseKernelNeedsSameRows",
            kernel_requires_same_rows,
            False,
            "逐点 primitive 核表同样要求行公式、权重恒等式和 rank 证书在同一行上对齐。",
            NEXT_TARGET,
        ),
        row(
            "DownstreamReverseRecoveryBlocked",
            downstream_blocked,
            True,
            "payment、零行覆盖、来源环和有限投影不能反推出 same-row signed payload。",
            NEXT_TARGET,
        ),
        row(
            "SameRowBridgeCurrentCorpusProved",
            False,
            False,
            "当前材料没有证明 unsigned primitive word skeleton 与 signed coefficient origin identity 是同一 pre-Cauchy row。",
            NEXT_TARGET,
        ),
        row(
            "JointAlphaSideRuleCurrentCorpusProved",
            False,
            False,
            "没有 same-row 桥接，joint alpha-side primitive word/coefficient rule 仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 joint alpha-side word/coefficient 规则证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json"),
        "alpha_side": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "alpha_map": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "anchor_phase": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "pointwise_weight": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "signed_expr": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "kernel": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
        "formal": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    productive_basis = (
        f"{NEXT_TARGET} AND {WORD_BINDING} AND {SIGNED_IDENTITY} AND "
        f"{UV_PAYLOAD} AND {OVERLOAD_RETURN} AND {FAILURE_RETURN}"
    )
    return {
        "certificate_type": "prime_matrix_strict_joint_alpha_side_word_coefficient_rule_router",
        "status": "joint_alpha_side_rule_reduced_to_same_row_word_coefficient_origin_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "joint_alpha_side_word_coefficient_rule_router_closed": True,
        "broad_alpha_side_rule_imported": True,
        "unsigned_carry_shell_skeleton_registered": (
            data["unsigned"].get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
        ),
        "signed_expression_reduced_to_origin_identity": data["signed_expr"].get("next_direct_attack_target") == SIGNED_IDENTITY,
        "joint_alpha_same_row_word_coefficient_origin_identity_proved": False,
        "joint_alpha_carry_shell_skeleton_to_primitive_basis_word_binding_proved": False,
        "primitive_summand_signed_coefficient_origin_identity_proved": False,
        "joint_alpha_primitive_row_uv_key_sign_local_factor_output_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_proved": False,
        "joint_alpha_side_rule_failure_named_return_proved": False,
        "joint_alpha_side_primitive_word_coefficient_rule_proved": False,
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_basis_word_coefficient_emitter_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            WORD_BINDING,
            SIGNED_IDENTITY,
            UV_PAYLOAD,
            OVERLOAD_RETURN,
            FAILURE_RETURN,
            TERMINAL_DESCENT,
        ],
        "productive_basis_after_router": productive_basis,
        "strict_basis_after_router": f"(({productive_basis}) OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}",
        "bridge_fields": bridge_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的真正难点不是单独生成 alpha unsigned row，也不是单独命名 signed coefficient；"
            f"而是证明二者在同一 pre-Cauchy primitive row 上同源。因此下一原子为 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步继续下钻 joint alpha-side 规则：已有材料可登记 carry-shell/anchor/phase 的 unsigned skeleton，"
            "也已把 signed expression 压到 origin identity，但二者尚未在同一 primitive row 上桥接。"
            "joint 规则必须证明同一 source tuple 同时产生 primitive basis word、signed coefficient、"
            "`(u,v)`、branch key、sign/local factor，并在失败时命名回流。该 same-row 桥接当前未证明，"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict joint alpha-side word/coefficient 规则路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_alpha_side_word_coefficient_rule_router_closed={fmt_bool(result['joint_alpha_side_word_coefficient_rule_router_closed'])}",
        f"unsigned_carry_shell_skeleton_registered={fmt_bool(result['unsigned_carry_shell_skeleton_registered'])}",
        f"signed_expression_reduced_to_origin_identity={fmt_bool(result['signed_expression_reduced_to_origin_identity'])}",
        f"joint_alpha_same_row_word_coefficient_origin_identity_proved={fmt_bool(result['joint_alpha_same_row_word_coefficient_origin_identity_proved'])}",
        f"joint_alpha_side_primitive_word_coefficient_rule_proved={fmt_bool(result['joint_alpha_side_primitive_word_coefficient_rule_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. same-row 桥接字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["bridge_fields"]:
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
            "完整 joint alpha-side 生产性基：",
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
            "审稿边界：本文件只证明 joint alpha-side 规则的最窄剩余是 same-row word/coefficient 桥接；"
            "它没有证明该桥接，也没有证明行/列命题无条件闭合。",
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
