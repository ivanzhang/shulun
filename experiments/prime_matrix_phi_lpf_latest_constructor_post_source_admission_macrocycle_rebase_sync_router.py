#!/usr/bin/env python3
"""生成 latest constructor post-source-admission macrocycle rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_post_source_admission_macrocycle_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_SOURCE_ADMISSION_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-router.json"
)
STRICT_SOURCE_ADMISSION_MACROCYCLE_CERT = (
    DOCS / "prime-matrix-strict-post-source-admission-macrocycle-sync-router.json"
)
STRICT_SOURCE_ADMISSION_ABSORPTION_CERT = (
    DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.json"
)
TRIAD_BRANCH_COVERAGE_CERT = DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
STRICT_HIGH_TAIL_CERT = DOCS / "prime-matrix-strict-high-model-tail-update-router.json"

A1 = "A1CleanBranchCanonicalSourceAdmission"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_PRIMITIVE = "NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle"
EXTERNAL_KZ = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
BETA_APPENDIX = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
BETA_99 = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
SAWTOOTH = "ExactResidueWeightedFloorSawtoothTenPercentBound"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖不能当成闭合。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        LATEST_SOURCE_ADMISSION_CERT,
        STRICT_SOURCE_ADMISSION_MACROCYCLE_CERT,
        STRICT_SOURCE_ADMISSION_ABSORPTION_CERT,
        TRIAD_BRANCH_COVERAGE_CERT,
        STRICT_HIGH_TAIL_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tail_package() -> str:
    """给出高段模型余量的严格自足尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def outside_cycle_break_package() -> str:
    """给出 A1 宏循环之后的循环外破口。"""
    return f"{SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_PRIMITIVE} OR {EXTERNAL_KZ}"


def latest_internal_basis() -> str:
    """给出当前 latest constructor 内部非循环基。"""
    return f"({outside_cycle_break_package()}) AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出保留旁路线后的 latest constructor 基。"""
    return (
        f"(({outside_cycle_break_package()} OR {A1}) AND {tail_package()}) "
        f"AND {RATE} AND {DSTRUCTURE} AND {JOINT_ROWS} AND {JOINT_IDENTITY} "
        f"AND {JOINT_RETURN} AND {SOURCE_EXACTUV} AND {SIGNED_SURVIVAL} "
        f"AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 post-source-admission macrocycle rebase 判定表。"""
    latest = data["latest"]
    macro = data["macro"]
    absorption = data["absorption"]
    branch = data["branch"]
    high_tail = data["high_tail"]

    latest_a1_active = (
        latest.get("next_primary_attack_target") == A1
        and latest.get("a1_clean_branch_canonical_source_admission_proved") is False
    )
    branch_absorbed = (
        absorption.get("source_admission_reduced_to_branch_statement") is True
        and absorption.get("source_admission_standalone_global_contradiction") is False
        and absorption.get("source_admission_absorbed_from_active_or") is True
    )
    branch_statement_closed = (
        branch.get("canonical_internal_branch_statement_adopted") is True
        and branch.get("canonical_source_branch_internal_gap_closed") is True
        and branch.get("generic_wfd_self_contained_gap_closed") is False
    )
    macrocycle_detected = (
        macro.get("a1_pdec_kz_macrocycle_detected") is True
        and macro.get("a1_source_admission_proved_as_global_contradiction") is False
        and macro.get("next_direct_attack_target") == SEED_CYCLE_CUT
    )
    outside_break_basis_imported = (
        SEED_CYCLE_CUT in str(macro.get("latest_noncircular_break_basis_after_router", ""))
        or SEED_CYCLE_CUT in str(macro.get("strict_break_basis_after_router", ""))
        or SEED_CYCLE_CUT in str(macro.get("strict_basis_after_router", ""))
        or macro.get("next_direct_attack_target") == SEED_CYCLE_CUT
    )
    finite_bridge_closed = (
        high_tail.get("dynamic_skeleton_finite_bridge_closed_imported") is True
        and high_tail.get("terminal_gap_after_router") == tail_package()
    )
    threshold_tail_boundary_kept = (
        high_tail.get("tail_linear_sieve_ten_percent_imported") is True
        or high_tail.get("strict_high_model_tail_boundary_closed") is True
    )
    chain_rebased = all(
        [
            latest_a1_active,
            branch_absorbed,
            branch_statement_closed,
            macrocycle_detected,
            outside_break_basis_imported,
            finite_bridge_closed,
        ]
    )

    return [
        row(
            "LatestConstructorA1SourceAdmissionImported",
            latest_a1_active,
            False,
            "上一层 latest constructor 已把 KZ-E/no-cycle 内部路线压到 A1 clean branch canonical source admission。",
            A1,
        ),
        row(
            "A1SourceAdmissionAbsorbedAsBranchBoundary",
            branch_absorbed,
            True,
            "A1 source admission 只是 canonical/generic 分支陈述边界，不能作为独立全局排斥原子。",
            "canonical branch scoped; generic/noncanonical branch still active",
        ),
        row(
            "CanonicalBranchStatementCoverageImported",
            branch_statement_closed,
            True,
            "canonical RIW/Buchstab 分支内部链条已闭合；generic WFD 宽口径仍只能外部化或回流。",
            "NoFurtherInternalGapForCanonicalSourceBranch; generic branch external/PDEC-SAE",
        ),
        row(
            "PostSourceAdmissionMacrocycleImported",
            macrocycle_detected,
            True,
            "A1 source-admission 深挖后回到 A1/PDEC/new-joint/KZ/KZ-E 宏循环；它不是下降量。",
            outside_cycle_break_package(),
        ),
        row(
            "OutsideCycleBreakBasisImported",
            outside_break_basis_imported,
            False,
            "继续无条件化必须提交循环外输入，而不是在 A1/PDEC/KZ 宏循环内重命名。",
            outside_cycle_break_package(),
        ),
        row(
            "ThresholdFiniteVerificationBoundaryPreserved",
            finite_bridge_closed,
            True,
            "高阈值加有限验证只关闭已登记有限桥；P>=100000 尾段仍落到 beta-sieve/sawtooth 自足包。",
            tail_package(),
        ),
        row(
            "TenPercentTailStillNeedsBetaAndSawtooth",
            threshold_tail_boundary_kept,
            False,
            "10% 主项包和有限验证不能替代 Rosser-Iwaniec lower weights、99% 系数与 exact sawtooth 余项。",
            tail_package(),
        ),
        row(
            "LatestInternalRouteReducedToOutsideCycleBreak",
            chain_rebased,
            False,
            "latest constructor 的当前内部非循环主攻已从 A1 admission 改写为循环外 seed/PDEC/payload/external-KZ 输入加尾包。",
            latest_internal_basis(),
        ),
        row(
            "SeedCycleCutStillOpen",
            True,
            False,
            "首选破环输入 AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput 当前尚未证明。",
            SEED_CYCLE_CUT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步并排除 A1/PDEC/KZ 宏循环伪出口；没有证明循环外输入、beta-sieve/sawtooth、Rate 或 DStructure。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "latest": load_json(LATEST_SOURCE_ADMISSION_CERT),
        "macro": load_json(STRICT_SOURCE_ADMISSION_MACROCYCLE_CERT),
        "absorption": load_json(STRICT_SOURCE_ADMISSION_ABSORPTION_CERT),
        "branch": load_json(TRIAD_BRANCH_COVERAGE_CERT),
        "high_tail": load_json(STRICT_HIGH_TAIL_CERT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_post_source_admission_macrocycle_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_post_source_admission_macrocycle_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_a1_source_admission_imported": rows[0]["closed"],
        "a1_source_admission_absorbed_as_branch_boundary": rows[1]["closed"],
        "canonical_branch_statement_coverage_imported": rows[2]["closed"],
        "post_source_admission_macrocycle_imported": rows[3]["closed"],
        "outside_cycle_break_basis_imported": rows[4]["closed"],
        "threshold_finite_verification_boundary_preserved": rows[5]["closed"],
        "ten_percent_tail_still_needs_beta_and_sawtooth": rows[6]["closed"],
        "latest_internal_route_reduced_to_outside_cycle_break": rows[7]["closed"],
        "acyclic_seed_cycle_cut_primitive_basis_and_coefficient_source_input_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "new_primitive_joint_payload_artifact_outside_signed_lane_cycle_present": False,
        "exact_external_dibfi_kuznetsov_no_projection_certificate_accepted": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": f"{A1} AND {tail_package()}",
        "absorbed_to": latest_internal_basis(),
        "latest_internal_basis_after_router": latest_internal_basis(),
        "latest_retained_basis_after_router": retained_basis(),
        "next_primary_attack_target": SEED_CYCLE_CUT,
        "next_direct_attack_target": f"{SEED_CYCLE_CUT} AND {BETA_APPENDIX}_THEN_ExactSawtooth",
        "parallel_attack_targets": [
            PDEC_SCOPE,
            NEW_PRIMITIVE,
            EXTERNAL_KZ,
            BETA_APPENDIX,
            BETA_99,
            SAWTOOTH,
            RATE,
            DSTRUCTURE,
            JOINT_ROWS,
            JOINT_IDENTITY,
            JOINT_RETURN,
            SOURCE_EXACTUV,
            SIGNED_SURVIVAL,
            ROW_MASS,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "structural_chain": [
            f"{A1} AND {tail_package()}",
            "A1CanonicalSourceBranchStatementAndCoverage",
            "A1/PDEC/new-joint/KZ/KZ-E macrocycle",
            f"{outside_cycle_break_package()}",
            f"({outside_cycle_break_package()}) AND {tail_package()}",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的 A1 source-admission 前沿接入 strict post-source-admission "
            "macrocycle 与 source-admission branch absorption。A1 准入只是一条 scoped 分支边界；"
            "继续沿内部链下钻会回到 A1/PDEC/new-joint/KZ/KZ-E 宏循环。非循环推进必须提交循环外输入："
            "seed cycle-cut primitive source、direct PDEC same-set scope、新 joint/payload 工件，或外部 "
            "no-projection KZ/DI/BFI。高阈值加有限验证只吸收有限桥；P>=100000 尾段仍需自足 "
            "beta-sieve、99% 主系数和 exact sawtooth。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor post-source-admission macrocycle rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_a1_source_admission_imported={fmt_bool(result['latest_constructor_a1_source_admission_imported'])}",
        f"a1_source_admission_absorbed_as_branch_boundary={fmt_bool(result['a1_source_admission_absorbed_as_branch_boundary'])}",
        f"canonical_branch_statement_coverage_imported={fmt_bool(result['canonical_branch_statement_coverage_imported'])}",
        f"post_source_admission_macrocycle_imported={fmt_bool(result['post_source_admission_macrocycle_imported'])}",
        f"outside_cycle_break_basis_imported={fmt_bool(result['outside_cycle_break_basis_imported'])}",
        f"threshold_finite_verification_boundary_preserved={fmt_bool(result['threshold_finite_verification_boundary_preserved'])}",
        f"ten_percent_tail_still_needs_beta_and_sawtooth={fmt_bool(result['ten_percent_tail_still_needs_beta_and_sawtooth'])}",
        f"latest_internal_route_reduced_to_outside_cycle_break={fmt_bool(result['latest_internal_route_reduced_to_outside_cycle_break'])}",
        f"acyclic_seed_cycle_cut_primitive_basis_and_coefficient_source_input_proved={fmt_bool(result['acyclic_seed_cycle_cut_primitive_basis_and_coefficient_source_input_proved'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"beta_sieve_main_coefficient_99_proved={fmt_bool(result['beta_sieve_main_coefficient_99_proved'])}",
        f"exact_residue_weighted_floor_sawtooth_bound_proved={fmt_bool(result['exact_residue_weighted_floor_sawtooth_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
        "\n".join(result["structural_chain"]),
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新内部基",
            "",
            "```text",
            result["latest_internal_basis_after_router"],
            "```",
            "",
            "## 4. 保留条件基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
