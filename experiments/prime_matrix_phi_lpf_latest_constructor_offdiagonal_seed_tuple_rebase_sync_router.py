#!/usr/bin/env python3
"""生成 latest constructor offdiagonal seed tuple 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_TUPLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json"
)
TUPLE_FIELDS_CERT = DOCS / "prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
OFFDIAG_TUPLE_FIELDS = "PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward"
OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SOURCE_EXACTUV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
TERMINAL_WFD = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
    """返回本层依赖证书。"""
    return [
        LATEST_REBASE_CERT,
        OLD_CONSTRUCTOR_TUPLE_CERT,
        TUPLE_FIELDS_CERT,
        SOURCE_PACKET_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_atoms() -> str:
    """返回 common packet 已携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({source_atoms()} AND {OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) OR "
        f"{POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {TERMINAL_WFD} OR {NEW_JOINT}) AND {SIGNED_SURVIVAL} "
        f"AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {HARMONIC} "
        f"AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def largest_sample(tuple_cert: dict[str, Any]) -> dict[str, Any]:
    """抽取 tuple-fields 证书的最大样本读数。"""
    samples = tuple_cert.get("sample_offdiagonal_tuple_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def build_rows(
    latest: dict[str, Any],
    old_tuple: dict[str, Any],
    tuple_cert: dict[str, Any],
    source_packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 offdiagonal tuple rebase 判定表。"""
    latest_offdiag_active = (
        latest.get("next_primary_attack_target") == OFFDIAG_SEED
        and latest.get("semiprime_seed_diagonal_rebased") is True
    )
    old_tuple_reusable = (
        old_tuple.get("target_input_before_router") == OFFDIAG_SEED
        and old_tuple.get("latest_basis_replaces_offdiag_seed_with_tuple_payload") is True
        and old_tuple.get("next_primary_attack_target") == OFFDIAG_SIGNED_FORMULA
    )
    tuple_router_imported = (
        tuple_cert.get("target_input_before_router") == OFFDIAG_SEED
        and tuple_cert.get("offdiagonal_semiprime_seed_tuple_fields_router_closed") is True
    )
    tuple_bijection = tuple_cert.get("offdiagonal_source_tuple_bijection_proved") is True
    tail_mass = tuple_cert.get("offdiagonal_phi_tail_fiber_mass_proved") is True
    unsigned_closed = tuple_cert.get("offdiagonal_unsigned_tuple_fields_closed") is True
    source_cycle_guard = (
        source_packet.get("common_packet_self_proof_blocked") is True
        or source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    rebase_closed = (
        latest_offdiag_active
        and old_tuple_reusable
        and tuple_router_imported
        and tuple_bijection
        and tail_mass
        and unsigned_closed
    )
    return [
        row(
            "LatestRebasedOffDiagonalSeedImported",
            latest_offdiag_active,
            False,
            "上一层 rebase 已把最新 constructor seed-side 窄口压到 offdiagonal ordered semiprime seed。",
            OFFDIAG_SEED,
        ),
        row(
            "ExistingConstructorOffDiagonalTupleReusable",
            old_tuple_reusable,
            False,
            "旧 constructor offdiagonal tuple 同步证书的输入相同，可在新 rebase 前沿复用。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
        row(
            "OffDiagonalTupleFieldsRouterImported",
            tuple_router_imported,
            True,
            "tuple-fields 证书把 offdiagonal seed 拆成无符号 tuple 字段和 signed payload 字段。",
            OFFDIAG_TUPLE_FIELDS,
        ),
        row(
            "OffDiagonalSourceTupleBijectionSynced",
            tuple_bijection,
            True,
            "每个 offdiagonal occurrence 唯一写成 owner p、first rough q 与 q-rough tail。",
            OFFDIAG_TUPLE_FIELDS,
        ),
        row(
            "OffDiagonalPhiTailFiberMassSynced",
            tail_mass,
            True,
            "Phi-LPF 桶恒等式只支付 q-rough tail occurrence mass。",
            "PhiLPFOffDiagonalQRoughTailFiberMassLedger",
        ),
        row(
            "LPFPhiUnsignedScopeExhausted",
            unsigned_closed,
            True,
            "LPF/Phi 无符号信息已用尽，不能推出 signed seed、orientation 或 ExactUV return。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
        row(
            "SourceAtomsCarriedForward",
            latest.get("carried_source_packet_attack_target") == source_atoms() and source_cycle_guard,
            False,
            "diagonal/common packet 义务仍由 source 三原子携带。",
            source_atoms(),
        ),
        row(
            "OffDiagonalSeedTupleRebased",
            rebase_closed,
            False,
            "最新 offdiagonal seed 入口已同步为 source tuple signed formula 与配套字段。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
        row(
            "OffDiagonalSignedFormulaStillOpen",
            tuple_cert.get("offdiagonal_signed_seed_formula_proved") is False,
            False,
            "当前材料没有给出 source tuple signed seed formula。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "OrientationAndExactUVStillOpen",
            tuple_cert.get("offdiagonal_orientation_parity_law_proved") is False
            and tuple_cert.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False,
            False,
            "orientation parity、branch side、ExactUV fixed pair 与 return tag 仍未证明。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
        row(
            "InternalTransitionStillPaired",
            latest.get("paired_required_attack_target") == INTERNAL_TRANSITION
            or INTERNAL_TRANSITION in old_tuple.get("paired_required_attack_targets", []),
            False,
            "tail 非单位 continuation 仍需要 internal prime-adjoin signed transition。",
            INTERNAL_TRANSITION,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 signed formula、orientation、ExactUV、internal transition 或 source 三原子。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_REBASE_CERT)
    old_tuple = load_json(OLD_CONSTRUCTOR_TUPLE_CERT)
    tuple_cert = load_json(TUPLE_FIELDS_CERT)
    source_packet = load_json(SOURCE_PACKET_CERT)
    rows = build_rows(latest, old_tuple, tuple_cert, source_packet)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_offdiagonal_seed_tuple_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_offdiagonal_seed_imported": rows[0]["closed"],
        "existing_constructor_offdiagonal_tuple_reusable": rows[1]["closed"],
        "offdiagonal_tuple_fields_router_imported": rows[2]["closed"],
        "offdiagonal_source_tuple_bijection_synced": rows[3]["closed"],
        "offdiagonal_phi_tail_fiber_mass_synced": rows[4]["closed"],
        "lpf_phi_unsigned_scope_exhausted_for_offdiag_seed": rows[5]["closed"],
        "source_atoms_carried_forward": rows[6]["closed"],
        "offdiagonal_seed_tuple_rebased": rows[7]["closed"],
        "offdiagonal_signed_seed_formula_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": OFFDIAG_SEED,
        "closed_unsigned_subledger": OFFDIAG_TUPLE_FIELDS,
        "next_primary_attack_target": OFFDIAG_SIGNED_FORMULA,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            ROW_MASS,
            source_atoms(),
        ],
        "parallel_constructor_side_gates": f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": retained_basis(),
        "imported_largest_sample": largest_sample(tuple_cert),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` "
            "接入既有 tuple-fields 证书。LPF/Phi 已关闭 owner prime、first rough prime、q-rough tail 与 "
            "Phi tail-fiber mass 的无符号支撑账，但这些字段不能推出 signed seed、orientation 或 ExactUV return。"
            "最新直接主攻推进到 `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor offdiagonal seed tuple rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_offdiagonal_seed_imported={fmt_bool(result['latest_rebased_offdiagonal_seed_imported'])}",
        f"existing_constructor_offdiagonal_tuple_reusable={fmt_bool(result['existing_constructor_offdiagonal_tuple_reusable'])}",
        f"offdiagonal_tuple_fields_router_imported={fmt_bool(result['offdiagonal_tuple_fields_router_imported'])}",
        f"offdiagonal_source_tuple_bijection_synced={fmt_bool(result['offdiagonal_source_tuple_bijection_synced'])}",
        f"offdiagonal_phi_tail_fiber_mass_synced={fmt_bool(result['offdiagonal_phi_tail_fiber_mass_synced'])}",
        f"lpf_phi_unsigned_scope_exhausted_for_offdiag_seed={fmt_bool(result['lpf_phi_unsigned_scope_exhausted_for_offdiag_seed'])}",
        f"source_atoms_carried_forward={fmt_bool(result['source_atoms_carried_forward'])}",
        f"offdiagonal_seed_tuple_rebased={fmt_bool(result['offdiagonal_seed_tuple_rebased'])}",
        f"offdiagonal_signed_seed_formula_proved={fmt_bool(result['offdiagonal_signed_seed_formula_proved'])}",
        f"offdiagonal_orientation_parity_law_proved={fmt_bool(result['offdiagonal_orientation_parity_law_proved'])}",
        f"offdiagonal_exactuv_fixed_pair_return_ledger_proved={fmt_bool(result['offdiagonal_exactuv_fixed_pair_return_ledger_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(result['internal_prime_adjoin_signed_transition_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    sample = result.get("imported_largest_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 2. 导入样本读数",
                "",
                "| N | offdiag types | tuple occ | Phi sum | tail=1 | tail>1 | max tail | ok |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['offdiagonal_seed_types']} | "
                    f"{sample['offdiagonal_tuple_occurrences']} | "
                    f"{sample['offdiagonal_phi_fiber_formula_sum']} | "
                    f"{sample['pure_semiprime_tail1_occurrences']} | "
                    f"{sample['tail_nonunit_occurrences']} | {sample['max_tail']} | "
                    f"`{fmt_bool(sample['tuple_phi_bijection_holds'])}` |"
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            "\n".join(result["paired_required_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
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
