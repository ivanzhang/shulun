#!/usr/bin/env python3
"""生成 strict 非递归破环包最新闭环同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_nonrecursive_breaker_latest_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.md"

NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
KERNEL_IDENTITY = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
POINTWISE_KERNEL_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json",
    "prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-global-internal-cycle-frontier-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象以显式保留缺口。"""
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


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不被解释为证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def row(stage: str, closed: bool, proved: bool, evidence: str, next_gap: str) -> dict[str, Any]:
    """构造同步判定行。"""
    return {
        "stage": stage,
        "closed": closed,
        "proved": proved,
        "evidence": evidence,
        "next_gap": next_gap,
    }


def build_chain_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把非递归破环线同步到当前真实闭环边界。"""
    terminal = data["terminal"]
    nonrecursive = data["nonrecursive"]
    kernel = data["kernel"]
    pointwise = data["pointwise"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    signed_value = data["signed_value"]
    signed_weight = data["signed_weight"]
    primitive_expr = data["primitive_expr"]
    origin = data["origin"]
    row_level = data["row_level"]
    seed_cycle = data["seed_cycle"]
    terminal_descent = data["terminal_descent"]
    explicit_joint = data["explicit_joint"]
    pdec = data["pdec"]

    return [
        row(
            "TerminalFamilyPrimaryTarget",
            terminal.get("next_primary_target") == NONRECURSIVE_BREAKER,
            terminal.get("nonrecursive_breaker_proved") is True,
            "终端家族最新饱和证书把主攻点钉为非递归 constructor/signed-lift 破环包。",
            NONRECURSIVE_BREAKER,
        ),
        row(
            "NonrecursiveBreakerToKernelIdentity",
            nonrecursive.get("next_direct_attack_target") == KERNEL_IDENTITY,
            nonrecursive.get("nonrecursive_breaker_package_proved") is True,
            "六个内部基已定位，但逐腿会回流；必须合取成同 formal-unit 核恒等式。",
            KERNEL_IDENTITY,
        ),
        row(
            "KernelIdentityToPointwiseTable",
            kernel.get("next_direct_attack_target") == POINTWISE_KERNEL_TABLE,
            kernel.get("same_formal_unit_kernel_identity_proved") is True,
            "formal-unit/no-loss/source-record 只保证对象不丢失，不给逐点 signed coefficient。",
            POINTWISE_KERNEL_TABLE,
        ),
        row(
            "PointwiseTableToAlphaRowFormula",
            pointwise.get("next_direct_attack_target") == "AlphaRowAnchorPhaseEmissionFormulaLedger",
            pointwise.get("pointwise_primitive_kernel_table_proved") is True,
            "逐点 primitive 核表被拆成行发射、权重恒等式和同表 rank 证书。",
            "AlphaRowAnchorPhaseEmissionFormulaLedger",
        ),
        row(
            "UnsignedSkeletonClosedButSignedLiftOpen",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            unsigned.get("alpha_row_anchor_phase_emission_formula_proved") is True,
            "unsigned carry-shell/phase/P列锚 skeleton 已闭合，但 signed lift 与 collar overload 未证。",
            "AlphaFormulaSignedCoefficientLiftLedger",
        ),
        row(
            "SignedLiftToPointwiseValueTable",
            signed_lift.get("next_direct_attack_target")
            == "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is True,
            "signed lift 等价于逐 skeleton row 给出 signed alpha value table。",
            "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
        ),
        row(
            "ValueTableToSignedWeightFormula",
            signed_value.get("next_direct_attack_target")
            == "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow",
            signed_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is True,
            "值表首字段是非递归 signed weight；Phi/variation 只能在 weight 已给出后验证。",
            "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow",
        ),
        row(
            "SignedWeightToPrimitiveExpression",
            signed_weight.get("next_direct_attack_target")
            == "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward",
            signed_weight.get("pointwise_nonrecursive_signed_alpha_weight_formula_proved") is True,
            "逐行权重公式压成推前前 primitive summand 的 signed weight 表达式。",
            "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward",
        ),
        row(
            "PrimitiveExpressionToOriginIdentity",
            primitive_expr.get("next_direct_attack_target")
            == "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward",
            primitive_expr.get("primitive_summand_signed_weight_expression_proved") is True,
            "表达式本身不是来源证明；必须给出 pre-Cauchy source tuple 的正向来源恒等式。",
            "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward",
        ),
        row(
            "OriginIdentityToRowLevelTable",
            origin.get("next_direct_attack_target")
            == "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
            origin.get("primitive_summand_signed_coefficient_origin_identity_proved") is True,
            "来源恒等式继续压成逐行 clean-core 原始生成表。",
            "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
        ),
        row(
            "RowLevelTableToAcyclicSeedEmitter",
            row_level.get("next_direct_attack_target")
            == "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity",
            row_level.get("row_level_clean_core_origin_generation_table_proved") is True,
            "row-level 表进入 acyclic seed signed-row emitter，随后已登记为坐标-来源闭环。",
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity",
        ),
        row(
            "SeedCoordinateSourceCycleGuard",
            seed_cycle.get("seed_coordinate_source_cycle_detected") is True,
            seed_cycle.get("primitive_basis_and_coefficient_source_input_proved") is True,
            "signed weight coordinate、coefficient assignment、basis word origin、row emitter 与 word coordinate 形成闭合依赖环。",
            SEED_CYCLE_CUT,
        ),
        row(
            "TerminalDescentReturnAlreadyMacrocycle",
            terminal_descent.get("terminal_descent_macrocycle_detected") is True,
            terminal_descent.get("acyclic_terminal_return_well_founded_descent_proved") is True,
            "若无 seed cycle-cut，回流 terminal descent；但当前 terminal descent 直攻脊柱已是宏循环。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "ExplicitJointFormulaStillAbsent",
            explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            explicit_joint.get("new_explicit_joint_constructor_formula_artifact_present") is True,
            "显式 joint 构造器直接展开会回到 signed-source 固定点；需要新的公式工件。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "DirectPDECScopeStillOpen",
            pdec.get("scope_audit_closed") is True or pdec.get("same_set_pdec_protocol_imported") is True,
            pdec.get("acyclic_same_set_scope_match_proved") is True,
            "direct PDEC 手臂仍缺 acyclic/canonical same-set 作用域匹配。",
            PDEC_SCOPE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造最新闭环同步证书。"""
    data = {
        "terminal": load_json("prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"),
        "nonrecursive": load_json("prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json"),
        "kernel": load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "signed_value": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "signed_weight": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "primitive_expr": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "signed_fixed": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "seed_cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "terminal_descent": load_json("prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"),
        "explicit_joint": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
        "pdec": load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"),
        "global_cycle": load_json("prime-matrix-strict-global-internal-cycle-frontier-sync-router.json"),
    }
    rows = build_chain_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    chain_synced = all(item["closed"] for item in rows)
    any_proved_breaker = any(
        item["proved"]
        for item in rows
        if item["stage"]
        in {
            "SeedCoordinateSourceCycleGuard",
            "ExplicitJointFormulaStillAbsent",
            "DirectPDECScopeStillOpen",
        }
    )
    strict_basis = (
        f"({SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    fallback_note = (
        f"{TERMINAL_DESCENT} 仍可作为独立新证书输入；但当前已归档的 terminal-descent 直攻脊柱"
        "回到 terminal-source-pair-joint 宏循环，所以在没有新 WFD 工件时不计入已证破环。"
    )
    return {
        "certificate_type": "prime_matrix_strict_nonrecursive_breaker_latest_cycle_sync_router",
        "status": "nonrecursive_breaker_synced_to_seed_cycle_cut_or_pdec_or_new_joint_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "latest_terminal_primary_target": data["terminal"].get("next_primary_target"),
        "nonrecursive_breaker_package_proved": data["nonrecursive"].get(
            "nonrecursive_breaker_package_proved"
        )
        is True,
        "same_formal_unit_kernel_identity_proved": data["kernel"].get(
            "same_formal_unit_kernel_identity_proved"
        )
        is True,
        "pointwise_primitive_kernel_table_proved": data["pointwise"].get(
            "pointwise_primitive_kernel_table_proved"
        )
        is True,
        "seed_coordinate_source_cycle_detected": data["seed_cycle"].get(
            "seed_coordinate_source_cycle_detected"
        )
        is True,
        "current_nonrecursive_attack_chain_synced": chain_synced,
        "current_chain_contains_nonproof_cycle": data["seed_cycle"].get(
            "raw_cycle_counts_as_closure"
        )
        is False,
        "seed_cycle_cut_input_proved": data["seed_cycle"].get(
            "primitive_basis_and_coefficient_source_input_proved"
        )
        is True,
        "acyclic_same_set_scope_match_proved": data["pdec"].get(
            "acyclic_same_set_scope_match_proved"
        )
        is True,
        "new_explicit_joint_constructor_formula_artifact_present": data["explicit_joint"].get(
            "new_explicit_joint_constructor_formula_artifact_present"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": (
            f"{SEED_CYCLE_CUT}_OR_{PDEC_SCOPE}_OR_{NEW_JOINT_FORMULA}"
        ),
        "strict_active_basis_after_router": strict_basis,
        "terminal_descent_fallback_note": fallback_note,
        "independent_acceptance_gates_retained": [MODEL_LEDGER, RATE_LEDGER, DSTRUCTURE],
        "chain_rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步把 `NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage` "
            "从同 formal-unit 核恒等式一路下钻到 signed 坐标-来源闭环：当前材料能说明每个字段缺什么，"
            "但不能从现有链条推出 signed coefficient 的非递归来源。这个环不能闭合命题。"
            "严格自足线现在只剩三个真正破环输入：无环 seed cycle-cut primitive source、direct PDEC same-set "
            "作用域匹配，或新的显式 joint alpha/delta 构造公式；模型余量、RatePreservation 与 DStructure/Rankin "
            "仍是独立守门项。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 非递归破环包最新闭环同步",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_terminal_primary_target={result['latest_terminal_primary_target']}",
        f"nonrecursive_breaker_package_proved={fmt_bool(result['nonrecursive_breaker_package_proved'])}",
        f"same_formal_unit_kernel_identity_proved={fmt_bool(result['same_formal_unit_kernel_identity_proved'])}",
        f"pointwise_primitive_kernel_table_proved={fmt_bool(result['pointwise_primitive_kernel_table_proved'])}",
        f"seed_coordinate_source_cycle_detected={fmt_bool(result['seed_coordinate_source_cycle_detected'])}",
        f"current_nonrecursive_attack_chain_synced={fmt_bool(result['current_nonrecursive_attack_chain_synced'])}",
        f"current_chain_contains_nonproof_cycle={fmt_bool(result['current_chain_contains_nonproof_cycle'])}",
        f"seed_cycle_cut_input_proved={fmt_bool(result['seed_cycle_cut_input_proved'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下钻同步表",
        "",
        "| stage | closed | proved | evidence | next gap |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["chain_rows"]:
        lines.append(
            "| `{stage}` | `{closed}` | `{proved}` | {evidence} | {next_gap} |".format(
                stage=table_cell(item["stage"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                evidence=table_cell(item["evidence"]),
                next_gap=table_cell(item["next_gap"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 最新严格活动基",
            "",
            "```text",
            result["strict_active_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            result["terminal_descent_fallback_note"],
            "",
            "独立守门项：",
            "",
            "```text",
            *result["independent_acceptance_gates_retained"],
            "```",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 3. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
