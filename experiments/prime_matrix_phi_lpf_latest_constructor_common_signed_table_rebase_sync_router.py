#!/usr/bin/env python3
"""生成 latest constructor common signed-table rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_common_signed_table_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-router.json"
)
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json"
TRACE_EXIT_CERT = DOCS / "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json"
EXACTUV_FIBER_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"
SOURCE_ENTROPY_CERT = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
FIXED_PAIR_CERT = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
COMPLETE_KEY_CERT = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
ROW_ORIGIN_BUCKET_CERT = DOCS / "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json"
PHI_RECURSIVE_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"

BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
SOURCE_EXACTUV = f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
NEW_TRACE = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
BUCKET_SIGNED_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
ROW_SUPPORT = "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger"
COMPLETE_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ACTUAL_SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
TRACE_BUDGET = "CompleteEmitterTraceKeyBudgetLedger"
SIGN_REFINEMENT = "SignLocalFactorRefinementNoCancellationLedger"
OVERBUDGET_RETURN = "OverBudgetOrUnregisteredReturnLedger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
EXTERNAL_KZ = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ROUGH_STEP = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
ROUGH_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
BETA_APPENDIX = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
BETA_99 = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
SAWTOOTH = "ExactResidueWeightedFloorSawtoothTenPercentBound"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖按未闭合处理。"""
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
        LATEST_CONSTRUCTOR_CERT,
        BUILTIN_TRACE_CERT,
        TRACE_EXIT_CERT,
        EXACTUV_FIBER_CERT,
        SOURCE_ENTROPY_CERT,
        FIXED_PAIR_CERT,
        COMPLETE_KEY_CERT,
        ROW_ORIGIN_BUCKET_CERT,
        PHI_RECURSIVE_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def tail_package() -> str:
    """给出高段 beta-sieve/sawtooth 自足尾包。"""
    return f"{BETA_APPENDIX} AND {BETA_99} AND {SAWTOOTH}"


def pointwise_kernel_atoms() -> str:
    """给出 trace-exit 后同 formal unit 核表的三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {SAME_RANK}"


def exactuv_source_atoms() -> str:
    """给出 ExactUV source/no-collapse 的实际原子。"""
    return f"{BUCKET_SIGNED_LAW} AND {ROW_MASS} AND {ROW_SUPPORT} AND {COMPLETE_KEY} AND {FIXED_KEY}"


def complete_key_source_atoms() -> str:
    """给出 complete-key 进一步实际化后的源表原子。"""
    return f"{ACTUAL_SOURCE_TABLE} AND {TRACE_BUDGET} AND {SIGN_REFINEMENT} AND {OVERBUDGET_RETURN}"


def common_table_frontier() -> str:
    """给出本层压缩后的共同 primitive-emitter 表字段。"""
    return f"{pointwise_kernel_atoms()} AND {exactuv_source_atoms()}"


def latest_basis_after_router() -> str:
    """给出 latest constructor 共同表前沿。"""
    return f"{common_table_frontier()} AND {tail_package()} AND {RATE} AND {DSTRUCTURE}"


def retained_basis() -> str:
    """给出旁路和并行门保留后的基。"""
    alternatives = (
        f"({common_table_frontier()}) OR {POINTWISE_TABLE} OR {PDEC_SCOPE} "
        f"OR {TERMINAL_DESCENT} OR {EXTERNAL_KZ} OR ({ROUGH_STEP} AND {ROUGH_COHERENCE})"
    )
    return (
        f"(({alternatives}) AND {tail_package()}) AND {RATE} AND {DSTRUCTURE} "
        f"AND ({complete_key_source_atoms()})"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 common signed-table rebase 判定表。"""
    latest = data["latest"]
    builtin = data["builtin"]
    trace = data["trace"]
    exactuv = data["exactuv"]
    entropy = data["entropy"]
    fixed_pair = data["fixed_pair"]
    complete_key = data["complete_key"]
    row_origin = data["row_origin"]
    phi_recursive = data["phi_recursive"]

    latest_triple = (
        latest.get("latest_internal_route_reduced_to_builtin_pairing_and_exactuv") is True
        and latest.get("next_primary_attack_target") == BUILTIN_PAIRING
        and latest.get("parallel_primary_attack_target") == SOURCE_EXACTUV
    )
    builtin_trace_exit = (
        builtin.get("next_primary_attack_target") == NEW_TRACE
        and builtin.get("exact_atomic_joint_branch_trace_signed_coefficient_formula_proved") is False
    )
    trace_convergence = (
        trace.get("next_primary_attack_target") == ALPHA_ANCHOR
        and trace.get("alpha_row_anchor_phase_emission_formula_proved") is False
        and trace.get("same_unit_exact_uv_rank_multiplicity_certificate_proved") is False
    )
    exactuv_atomized = (
        exactuv.get("deterministic_source_atom_implication_closed") is True
        and exactuv.get("source_entropy_reduced_to_signed_rows") is True
        and exactuv.get("fixed_pair_fiber_formal_inequality_closed") is True
    )
    entropy_atoms = (
        entropy.get("actual_source_domain_entropy_atomization_closed") is True
        and entropy.get("same_formal_unit_row_mass_normalization_proved") is False
        and entropy.get("primitive_row_support_lower_bound_proved") is False
    )
    fixed_pair_atoms = (
        fixed_pair.get("fixed_pair_fiber_bound_router_closed") is True
        and fixed_pair.get("registered_complete_primitive_emitter_key_partition_polylog_proved") is False
        and fixed_pair.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False
    )
    complete_key_boundary = (
        complete_key.get("complete_emitter_key_partition_router_closed") is True
        and complete_key.get("source_table_to_complete_key_implication_closed") is True
        and complete_key.get("registered_complete_primitive_emitter_key_partition_polylog_proved") is False
    )
    phi_unsigned = (
        phi_recursive.get("phi_recursive_lpf_bucket_formula_proved") is True
        and phi_recursive.get("prime_count_identity_from_phi_lpf_proved") is True
        and phi_recursive.get("large_prime_layer_zero_mass_proved") is True
    )
    bucket_signed_law = (
        row_origin.get("phi_lpf_support_and_capacity_closed") is True
        and row_origin.get("row_origin_table_reduced_to_phi_lpf_bucket_signed_law") is True
        and row_origin.get("phi_lpf_bucket_signed_coefficient_law_proved") is False
    )
    common_table = all(
        [
            latest_triple,
            builtin_trace_exit,
            trace_convergence,
            exactuv_atomized,
            entropy_atoms,
            fixed_pair_atoms,
            complete_key_boundary,
            phi_unsigned,
            bucket_signed_law,
        ]
    )
    finite_boundary = latest.get("threshold_finite_verification_boundary_preserved") is True
    tail_open = (
        latest.get("self_contained_beta_sieve_appendix_proved") is False
        and latest.get("beta_sieve_main_coefficient_99_proved") is False
        and latest.get("exact_residue_weighted_floor_sawtooth_bound_proved") is False
    )

    return [
        row(
            "LatestConstructorPairingExactUVTripleImported",
            latest_triple,
            False,
            "上一层已把 constructor 下游压成 built-in signed pairing 与 ExactUV source/fixed-fiber 合取。",
            f"{BUILTIN_PAIRING} AND {SOURCE_EXACTUV}",
        ),
        row(
            "BuiltInPairingTraceExitImported",
            builtin_trace_exit,
            False,
            "built-in pairing 不能由环内 signed lane 自证；环外生产性出口是 new primitive trace/payload 或受控返回。",
            f"{NEW_TRACE} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "TraceExitSourceRankConvergenceImported",
            trace_convergence,
            False,
            "new primitive trace/payload 若真是新工件，必须携带 source-rank/no-collapse 并汇入逐 primitive 核表。",
            pointwise_kernel_atoms(),
        ),
        row(
            "ExactUVFiberAtomizationImported",
            exactuv_atomized,
            False,
            "ExactUV fiber 已被形式化为 source entropy、complete key 与 fixed-key O(1) multiplicity。",
            f"{SOURCE_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "SourceEntropySignedRowsImported",
            entropy_atoms,
            False,
            "source entropy 不是 CRT 位置计数；它需要 signed rows、row-mass/no-heavy-row 与发射前支撑下界。",
            f"{BUCKET_SIGNED_LAW} AND {ROW_MASS} AND {ROW_SUPPORT}",
        ),
        row(
            "FixedPairFiberCompleteKeyAtomized",
            fixed_pair_atoms,
            False,
            "fixed-pair fiber 的形式不等式已闭合，实际仍需 complete key polylog 与 fixed-key 局部 O(1)。",
            f"{COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "CompleteKeySourceTableBoundaryImported",
            complete_key_boundary,
            False,
            "complete key 不能后验贴标签；它必须由 actual primitive emitter source table 产生并带预算/回流。",
            complete_key_source_atoms(),
        ),
        row(
            "PhiLPFRecursiveUnsignedOwnershipClosed",
            phi_unsigned,
            True,
            "LPF/Phi 递推严格关闭 least-prime-factor ownership、容量、素数计数恒等式和 p>sqrt(N) 零质量。",
            "closed unsigned owner/support/capacity",
        ),
        row(
            "RowOriginReducedToBucketSignedLaw",
            bucket_signed_law,
            False,
            "无符号 support/capacity 已剥离；真正剩余是每个 LPF/Phi bucket 的 signed coefficient law。",
            BUCKET_SIGNED_LAW,
        ),
        row(
            "CommonSameFormalUnitSignedTableAligned",
            common_table,
            False,
            "pairing、entropy、ExactUV 三线现在必须在同一 pre-Cauchy primitive-emitter 表中共同支付。",
            common_table_frontier(),
        ),
        row(
            "ThresholdFiniteVerificationBoundaryPreserved",
            finite_boundary,
            True,
            "充分大阈值加有限验证只关闭已登记有限桥，不能替代 beta-sieve/sawtooth 尾段。",
            tail_package(),
        ),
        row(
            "BetaSieveSawtoothTailStillOpen",
            tail_open,
            False,
            "当前语料仍未证明 Rosser--Iwaniec beta-sieve、99% 主系数和 exact sawtooth。",
            tail_package(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做共同表 rebase；未证明 bucket signed law、alpha anchor、row mass/support、key multiplicity 或尾段。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "latest": load_json(LATEST_CONSTRUCTOR_CERT),
        "builtin": load_json(BUILTIN_TRACE_CERT),
        "trace": load_json(TRACE_EXIT_CERT),
        "exactuv": load_json(EXACTUV_FIBER_CERT),
        "entropy": load_json(SOURCE_ENTROPY_CERT),
        "fixed_pair": load_json(FIXED_PAIR_CERT),
        "complete_key": load_json(COMPLETE_KEY_CERT),
        "row_origin": load_json(ROW_ORIGIN_BUCKET_CERT),
        "phi_recursive": load_json(PHI_RECURSIVE_CERT),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_common_signed_table_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_common_signed_table_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_constructor_pairing_exactuv_triple_imported": rows[0]["closed"],
        "built_in_pairing_trace_exit_imported": rows[1]["closed"],
        "trace_exit_source_rank_convergence_imported": rows[2]["closed"],
        "exactuv_fiber_atomization_imported": rows[3]["closed"],
        "source_entropy_signed_rows_imported": rows[4]["closed"],
        "fixed_pair_fiber_complete_key_atomized": rows[5]["closed"],
        "complete_key_source_table_boundary_imported": rows[6]["closed"],
        "phi_lpf_recursive_unsigned_ownership_closed": rows[7]["closed"],
        "row_origin_reduced_to_bucket_signed_law": rows[8]["closed"],
        "common_same_formal_unit_signed_table_aligned": rows[9]["closed"],
        "threshold_finite_verification_boundary_preserved": rows[10]["closed"],
        "beta_sieve_sawtooth_tail_still_open": rows[11]["closed"],
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "phi_lpf_bucket_signed_coefficient_law_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "primitive_row_support_lower_bound_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": f"{BUILTIN_PAIRING} AND {SOURCE_EXACTUV} AND {tail_package()}",
        "latest_internal_basis_after_router": latest_basis_after_router(),
        "latest_retained_basis_after_router": retained_basis(),
        "common_same_formal_unit_signed_table_frontier": common_table_frontier(),
        "next_primary_attack_target": BUCKET_SIGNED_LAW,
        "parallel_primary_attack_target": pointwise_kernel_atoms(),
        "next_direct_attack_target": (
            f"{common_table_frontier()} AND {BETA_APPENDIX}_THEN_ExactSawtooth"
        ),
        "parallel_attack_targets": [
            ALPHA_ANCHOR,
            ARITH_ID,
            SAME_RANK,
            ROW_MASS,
            ROW_SUPPORT,
            COMPLETE_KEY,
            FIXED_KEY,
            complete_key_source_atoms(),
            POINTWISE_TABLE,
            PDEC_SCOPE,
            TERMINAL_DESCENT,
            EXTERNAL_KZ,
            f"{ROUGH_STEP} AND {ROUGH_COHERENCE}",
            BETA_APPENDIX,
            BETA_99,
            SAWTOOTH,
            RATE,
            DSTRUCTURE,
        ],
        "structural_chain": [
            f"{BUILTIN_PAIRING} AND {SOURCE_EXACTUV} AND {tail_package()}",
            f"{BUILTIN_PAIRING} -> {NEW_TRACE} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
            f"{NEW_TRACE} -> {pointwise_kernel_atoms()}",
            f"{SOURCE_ENTROPY} -> {BUCKET_SIGNED_LAW} AND {ROW_MASS} AND {ROW_SUPPORT}",
            f"{FIXED_FIBER} -> {COMPLETE_KEY} AND {FIXED_KEY}",
            "PhiRecursiveLPFOwnershipRoughCountLedger -> closed unsigned owner/support/capacity only",
            f"common table -> {common_table_frontier()}",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor 的 built-in pairing / source entropy / fixed-pair ExactUV 三线"
            "重接到同一个 pre-Cauchy LPF/Phi primitive-emitter 表。LPF/Phi 精准桶恒等式已严格支付"
            "无符号 ownership、support、capacity、p>sqrt(N) 零质量与素数计数恒等式；但这些读数不产生"
            " signed coefficient、orientation/local factor、row-mass、complete key 或 fixed-key multiplicity。"
            "因此最新剩余从三个分散黑箱压成同 formal unit 的 signed-table 字段包，并继续携带 beta-sieve/"
            "sawtooth 尾段。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor common signed-table rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_pairing_exactuv_triple_imported={fmt_bool(result['latest_constructor_pairing_exactuv_triple_imported'])}",
        f"built_in_pairing_trace_exit_imported={fmt_bool(result['built_in_pairing_trace_exit_imported'])}",
        f"trace_exit_source_rank_convergence_imported={fmt_bool(result['trace_exit_source_rank_convergence_imported'])}",
        f"exactuv_fiber_atomization_imported={fmt_bool(result['exactuv_fiber_atomization_imported'])}",
        f"source_entropy_signed_rows_imported={fmt_bool(result['source_entropy_signed_rows_imported'])}",
        f"fixed_pair_fiber_complete_key_atomized={fmt_bool(result['fixed_pair_fiber_complete_key_atomized'])}",
        f"complete_key_source_table_boundary_imported={fmt_bool(result['complete_key_source_table_boundary_imported'])}",
        f"phi_lpf_recursive_unsigned_ownership_closed={fmt_bool(result['phi_lpf_recursive_unsigned_ownership_closed'])}",
        f"row_origin_reduced_to_bucket_signed_law={fmt_bool(result['row_origin_reduced_to_bucket_signed_law'])}",
        f"common_same_formal_unit_signed_table_aligned={fmt_bool(result['common_same_formal_unit_signed_table_aligned'])}",
        f"threshold_finite_verification_boundary_preserved={fmt_bool(result['threshold_finite_verification_boundary_preserved'])}",
        f"beta_sieve_sawtooth_tail_still_open={fmt_bool(result['beta_sieve_sawtooth_tail_still_open'])}",
        f"phi_lpf_bucket_signed_coefficient_law_proved={fmt_bool(result['phi_lpf_bucket_signed_coefficient_law_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(result['same_formal_unit_row_mass_normalization_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(result['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
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
            "## 3. 同 formal unit 共同表前沿",
            "",
            "```text",
            result["common_same_formal_unit_signed_table_frontier"],
            "```",
            "",
            "## 4. 最新内部基",
            "",
            "```text",
            result["latest_internal_basis_after_router"],
            "```",
            "",
            "## 5. 保留条件基",
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
            "## 6. 依赖哈希",
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
