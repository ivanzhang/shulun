#!/usr/bin/env python3
"""生成 strict 非递归逐点 primitive 核表字段合同证书。

用法示例：
  python3 experiments/prime_matrix_strict_nonrecursive_pointwise_kernel_table_field_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json"
OUT_MD = DOCS / "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.md"

TARGET = "NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn"
POINTWISE_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
JOINT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
JOINT_DOMAIN = "JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger"
JOINT_EMIT = "JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger"
TIMESTAMP = "SameFormalUnitPreCauchyTimestampLockLedger"
NO_LEAK = "NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger"
JOINT_RETURN = "JointConstructorFormulaFailureReturnTagsLedger"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
ACYCLIC_SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
ALPHA_INDEX = "AlphaPrimitiveRowIndexSetLedger"
ALPHA_FORMULA = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ALPHA_ORDERING = "AlphaRowFiniteMultiplicityOrderingLedger"
ALPHA_NO_CHOICE = "AlphaEmissionMapNoDownstreamChoiceLedger"
ALPHA_RETURN = "AlphaEmissionMapNamedReturnLedger"
WEIGHT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
WEIGHT_FORMULA = "ExactAlphaSignedWeightFormulaLedger"
WEIGHT_NONZERO = "AlphaWeightNonzeroSignLocalFactorLedger"
WEIGHT_NORECOVERY = "AlphaWeightNoZeroRowGeometryOrPaymentRecoveryLedger"
WEIGHT_RETURN = "AlphaWeightLawFailureNamedReturnLedger"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
SOURCE_RETURN = "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-kernel-table-three-leg-return-sync-router.json",
    "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json",
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-global-internal-cycle-frontier-sync-router.json",
    "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
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
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记引用证据哈希。"""
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


def field_contract() -> list[dict[str, str]]:
    """列出非递归逐点表必须一次性提交的字段。"""
    return [
        {
            "field": "primitive_row_index_set",
            "meaning": "同一 formal unit 内 primitive rows 的有限索引集合。",
            "atom": ALPHA_INDEX,
        },
        {
            "field": "source_tuple_to_anchor_phase_row_formula",
            "meaning": "从 actual source tuple 到 anchor/phase row 的显式发射公式。",
            "atom": ALPHA_FORMULA,
        },
        {
            "field": "same_row_word_coefficient_payload",
            "meaning": "同一行同时输出 basis word、signed coefficient、branch key、u/v、sign/local factor。",
            "atom": JOINT_RULE,
        },
        {
            "field": "signed_weight_arithmetic_identity",
            "meaning": "推前前 signed 权重必须来自独立 noncanonical 算术恒等式。",
            "atom": WEIGHT_IDENTITY,
        },
        {
            "field": "exact_uv_phi_atom_output",
            "meaning": "每行同步输出 exact `(u,v)` 与 Phi/payment atom，不能后验补配。",
            "atom": JOINT_EMIT,
        },
        {
            "field": "local_factor_nonzero_and_sign",
            "meaning": "非零 local factor、符号和 branch refinement 与 row 同步。",
            "atom": WEIGHT_NONZERO,
        },
        {
            "field": "rank_multiplicity_certificate",
            "meaning": "同一张表上证明 exact-UV bounded multiplicity/rank。",
            "atom": UV_INCIDENCE,
        },
        {
            "field": "named_return_discipline",
            "meaning": "缺行、零权、跨来源、后验读取、超预算等失败必须命名回流。",
            "atom": f"{JOINT_RETURN} AND {SOURCE_RETURN}",
        },
    ]


def build_result() -> dict[str, Any]:
    """把非递归逐点表压到共同字段合同和第一生产性原子。"""
    kernel_sync = load_json("prime-matrix-strict-kernel-table-three-leg-return-sync-router.json")
    joint = load_json("prime-matrix-strict-joint-declaration-constructor-sync-router.json")
    row_level = load_json("prime-matrix-strict-row-level-origin-generation-table-router.json")
    emission = load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json")
    weight = load_json("prime-matrix-strict-alpha-signed-weight-law-router.json")
    same_row = load_json("prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json")
    precauchy = load_json("prime-matrix-strict-precauchy-declaration-line-router.json")
    source_table = load_json("prime-matrix-strict-actual-emitter-source-table-router.json")
    uv_rank = load_json("prime-matrix-strict-exact-uv-map-rank-incidence-router.json")
    fixed_pair = load_json("prime-matrix-strict-fixed-pair-fiber-bound-router.json")
    key = load_json("prime-matrix-strict-complete-emitter-key-partition-router.json")
    global_cycle = load_json("prime-matrix-strict-global-internal-cycle-frontier-sync-router.json")
    dstructure = load_json("prime-matrix-dstructure-rankin-promotion-acceptance-router.json")

    target_active = (
        kernel_sync.get("kernel_table_three_leg_return_sync_closed") is True
        and kernel_sync.get("next_direct_attack_target") == TARGET
    )
    joint_constructor_open = (
        joint.get("joint_declaration_constructor_sync_router_closed") is True
        and joint.get("explicit_joint_alpha_delta_constructor_rule_proved") is False
        and joint.get("next_direct_attack_target") == JOINT_RULE
    )
    row_table_open = (
        row_level.get("row_level_origin_generation_table_router_closed") is True
        and row_level.get("row_level_clean_core_origin_generation_table_proved") is False
        and row_level.get("next_direct_attack_target") == ACYCLIC_SEED
    )
    alpha_emission_open = (
        emission.get("deterministic_alpha_row_emission_map_router_closed") is True
        and emission.get("alpha_primitive_row_index_set_proved") is False
        and emission.get("alpha_row_anchor_phase_emission_formula_proved") is False
    )
    signed_weight_open = (
        weight.get("alpha_signed_weight_law_router_closed") is True
        and weight.get("independent_noncanonical_precauchy_arithmetic_identity_statement_proved") is False
        and weight.get("exact_alpha_signed_weight_formula_proved") is False
    )
    same_row_open = (
        same_row.get("joint_alpha_same_row_origin_identity_router_closed") is True
        and same_row.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    precauchy_line_open = (
        precauchy.get("precauchy_declaration_line_router_closed") is True
        and precauchy.get("actual_noncanonical_primitive_constructor_formula_line_proved") is False
    )
    source_table_open = (
        source_table.get("actual_emitter_source_table_router_closed") is True
        and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
    )
    rank_open = (
        uv_rank.get("exact_uv_map_rank_incidence_router_closed") is True
        and uv_rank.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False
        and fixed_pair.get("fixed_pair_fiber_bound_router_closed") is True
        and key.get("complete_emitter_key_partition_router_closed") is True
    )
    terminal_cycle_detected = (
        global_cycle.get("internal_terminal_source_cycle_detected") is True
        or kernel_sync.get("three_leg_separate_attack_is_fixed_point") is True
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    field_contract_boundary_closed = all(
        [
            target_active,
            joint_constructor_open,
            row_table_open,
            alpha_emission_open,
            signed_weight_open,
            same_row_open,
            precauchy_line_open,
            source_table_open,
            rank_open,
            terminal_cycle_detected,
        ]
    )

    rows = [
        row(
            "NonrecursivePointwiseTableTargetActive",
            target_active,
            False,
            "上一层三腿回流已把核表缺口压成非递归逐点表。",
            TARGET,
        ),
        row(
            "FieldContractBoundaryPinned",
            field_contract_boundary_closed,
            True,
            "所有合法字段必须在同一 formal unit、Cauchy/dispersion/Phi 推前之前一次性给出。",
            "字段边界闭合，不等于表构造已证明。",
        ),
        row(
            "SameSourceTupleContainerReady",
            joint.get("same_source_tuple_container_closed") is True,
            True,
            "formal unit/source tuple 容器可承载同一行 word/coefficient/u/v/hash。",
            "容器不产生 primitive row。",
        ),
        row(
            "ActualJointConstructorRuleMissing",
            joint_constructor_open and precauchy_line_open,
            False,
            "actual noncanonical constructor 必须显式把 source tuple 映到 joint primitive row；当前没有公式。",
            JOINT_RULE,
        ),
        row(
            "AlphaIndexAndEmissionFormulaMissing",
            alpha_emission_open,
            False,
            "alpha row 索引集合、anchor/phase 发射公式、有限排序和无后验选择仍未证明。",
            f"{ALPHA_INDEX} AND {ALPHA_FORMULA} AND {ALPHA_ORDERING} AND {ALPHA_NO_CHOICE} AND {ALPHA_RETURN}",
        ),
        row(
            "SameRowWordCoefficientOriginMissing",
            same_row_open and row_table_open,
            False,
            "unsigned skeleton 与 signed coefficient 不能分别拼接；必须同一 row 同源。",
            f"{ROW_TABLE} -> {ACYCLIC_SEED}",
        ),
        row(
            "SignedWeightArithmeticIdentityMissing",
            signed_weight_open,
            False,
            "signed 权重律仍缺独立 pre-Cauchy 算术恒等式、精确权重公式和非零 local factor。",
            f"{WEIGHT_IDENTITY} AND {WEIGHT_FORMULA} AND {WEIGHT_NONZERO} AND {WEIGHT_NORECOVERY} AND {WEIGHT_RETURN}",
        ),
        row(
            "ExactUVRankMultiplicityStillOpen",
            rank_open,
            False,
            "fixed-pair/key 形式门已定位，但 actual bounded multiplicity incidence 未证明。",
            f"{UV_INCIDENCE} AND {RANK_CERT}",
        ),
        row(
            "NamedReturnDisciplineIncomplete",
            source_table_open and joint_constructor_open,
            False,
            "缺行、零 local factor、跨来源、超预算或后验读取的回流栏尚未与同一公式行合取。",
            f"{JOINT_RETURN} AND {SOURCE_RETURN} AND {ALPHA_RETURN} AND {WEIGHT_RETURN}",
        ),
        row(
            "NoTerminalReturnCurrentlyUnproved",
            terminal_cycle_detected,
            False,
            "现有内部路线仍会回到 terminal/source 固定点；非递归表必须由正向公式破环。",
            JOINT_RULE,
        ),
        row(
            "NonrecursivePointwiseTableCurrentCorpusProved",
            False,
            False,
            "当前语料只闭合字段边界和伪出口排除，没有提交同一张非递归 primitive 核表。",
            TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未推出早期零行反例链与真实结构链的终端矛盾。",
            f"{JOINT_RULE} AND {UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_nonrecursive_pointwise_kernel_table_field_contract_router",
        "status": "nonrecursive_pointwise_kernel_table_field_contract_closed_constructor_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "field_contract_boundary_closed": field_contract_boundary_closed,
        "nonrecursive_pointwise_table_proved": False,
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False if dstructure_open else dstructure.get("promotion_package_independently_accepted") is True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": JOINT_RULE,
        "parallel_required_inputs_after_constructor": [UV_INCIDENCE, RATE, DSTRUCTURE],
        "minimal_productive_basis_after_router": (
            f"({JOINT_RULE} AND {JOINT_DOMAIN} AND {JOINT_EMIT} AND {TIMESTAMP} AND "
            f"{NO_LEAK} AND {JOINT_RETURN} AND {UV_INCIDENCE}) AND {RATE} AND {DSTRUCTURE}"
        ),
        "nonrecursive_field_contract": field_contract(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 不能由 alpha/weight/rank 三腿后验拼装；它要求同一 formal unit 的一张正向 primitive 表。"
            f"所有活动链条交到同一个第一生产性原子 `{JOINT_RULE}`：没有这条显式 joint constructor rule，"
            "primitive row index、signed weight、exact-UV/Phi atom、local factor、rank/multiplicity 和 named return 都没有共同载体。"
        ),
        "plain_conclusion": (
            "本步把非递归逐点 primitive 核表从单一标签压成字段合同，并确认字段边界已闭合："
            "合法证明必须在同一 formal unit、Cauchy/dispersion/Phi 推前之前一次性给出 rows、权重、"
            "`(u,v)`、Phi atom、local factor、rank 证书和回流栏。当前语料没有这张表；"
            f"真正第一生产性硬点是 `{JOINT_RULE}`。因此行/列命题仍未无条件自足闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 非递归逐点 primitive 核表字段合同证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"field_contract_boundary_closed={fmt_bool(result['field_contract_boundary_closed'])}",
        f"nonrecursive_pointwise_table_proved={fmt_bool(result['nonrecursive_pointwise_table_proved'])}",
        f"explicit_joint_alpha_delta_constructor_rule_proved={fmt_bool(result['explicit_joint_alpha_delta_constructor_rule_proved'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 非递归表字段合同",
        "",
        "| field | meaning | atom |",
        "| --- | --- | --- |",
    ]
    for item in result["nonrecursive_field_contract"]:
        lines.append(
            "| `{field}` | {meaning} | {atom} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
                atom=table_cell(item["atom"]),
            )
        )
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
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "构造器之后仍需并行验收：",
            "",
            "```text",
            *result["parallel_required_inputs_after_constructor"],
            "```",
            "",
            "当前最小生产性基：",
            "",
            "```text",
            result["minimal_productive_basis_after_router"],
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
