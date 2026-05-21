#!/usr/bin/env python3
"""生成 latest constructor pure-pair atom 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_PURE_CERT = DOCS / "prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.json"
PURE_ATOM_CERT = DOCS / "prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
PURE_SEMIPRIME_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
TAIL_LIFT = "PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward"
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
    """读取 JSON 证书；缺失不能当作已证明。"""
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
    return [LATEST_REBASE_CERT, OLD_CONSTRUCTOR_PURE_CERT, PURE_ATOM_CERT, SOURCE_PACKET_CERT]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_atoms() -> str:
    """返回 source-packet 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({source_atoms()} AND {PURE_SEMIPRIME_ATOM} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) OR "
        f"{POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {TERMINAL_WFD} OR {NEW_JOINT}) AND {SIGNED_SURVIVAL} "
        f"AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {HARMONIC} "
        f"AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def largest_sample(pure_atom: dict[str, Any]) -> dict[str, Any]:
    """抽取 pure atom 证书的最大样本读数。"""
    samples = pure_atom.get("sample_pure_seed_atom_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def build_rows(
    latest: dict[str, Any],
    old_pure: dict[str, Any],
    pure_atom: dict[str, Any],
    source_packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 pure-pair atom rebase 判定表。"""
    latest_formula_active = (
        latest.get("next_primary_attack_target") == OFFDIAG_SIGNED_FORMULA
        and latest.get("offdiagonal_seed_tuple_rebased") is True
    )
    old_pure_reusable = (
        old_pure.get("target_input_before_router") == OFFDIAG_SIGNED_FORMULA
        and old_pure.get("latest_basis_replaces_tuple_formula_with_pure_atom") is True
        and old_pure.get("next_primary_attack_target") == PURE_SEMIPRIME_ATOM
    )
    pure_router_imported = (
        pure_atom.get("target_input_before_router") == OFFDIAG_SIGNED_FORMULA
        and pure_atom.get("offdiagonal_pure_semiprime_seed_atom_router_closed") is True
    )
    atom_bijection = pure_atom.get("pure_semiprime_pair_seed_atom_bijection_proved") is True
    tail_mass = pure_atom.get("tail_lift_phi_minus_one_mass_formula_proved") is True
    tail_reduced = pure_atom.get("tail_nonunit_reduced_to_internal_transition_lift") is True
    source_cycle_guard = (
        source_packet.get("common_packet_self_proof_blocked") is True
        or source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    rebase_closed = (
        latest_formula_active
        and old_pure_reusable
        and pure_router_imported
        and atom_bijection
        and tail_mass
        and tail_reduced
    )
    return [
        row(
            "LatestRebasedSourceTupleSignedFormulaImported",
            latest_formula_active,
            False,
            "上一层 rebase 已把最新 constructor 窄口压到 offdiagonal source tuple signed formula。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "ExistingConstructorPurePairReusable",
            old_pure_reusable,
            False,
            "旧 constructor pure-pair atom 同步证书输入相同，可在新 rebase 前沿复用。",
            f"{PURE_SEMIPRIME_ATOM} AND {TAIL_LIFT}",
        ),
        row(
            "PurePairAtomRouterImported",
            pure_router_imported,
            True,
            "pure atom 证书把 source tuple formula 的 first-seed 部分定位到 tail=1 pure pair。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "PurePairAtomBijectionSynced",
            atom_bijection,
            True,
            "每个 ordered `(p,q), p<q` 只有一个 tail=1 pure semiprime seed atom。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "TailLiftPhiMinusOneSynced",
            tail_mass,
            True,
            "tail>1 continuation 质量为 `Phi(floor(N/(p*q)),q)-1`。",
            TAIL_LIFT,
        ),
        row(
            "TailLiftNoNewFirstSeedClosed",
            tail_reduced,
            True,
            "tail>1 不是新 first seed，必须归入 internal transition lift。",
            INTERNAL_TRANSITION,
        ),
        row(
            "SourceAtomsCarriedForward",
            latest.get("paired_required_attack_targets", [])[-1:] == [source_atoms()] and source_cycle_guard,
            False,
            "source 三原子仍作为 carried input 保留，不能由 pure atom 层自证。",
            source_atoms(),
        ),
        row(
            "PurePairAtomRebased",
            rebase_closed,
            False,
            "最新 source tuple formula 已同步为 pure-pair signed atom 与 tail-lift/internal-transition 配套。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "PurePairSignedAtomStillOpen",
            pure_atom.get("pure_semiprime_pair_signed_seed_atom_proved") is False,
            False,
            "tail=1 定位不给 pure pair signed seed value。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "OrientationExactUVTransitionStillOpen",
            pure_atom.get("offdiagonal_orientation_parity_law_proved") is False
            and pure_atom.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False
            and pure_atom.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "orientation、ExactUV return 与 internal transition 仍是独立门。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 pure-pair signed atom、orientation、ExactUV、internal transition 或 source 三原子。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_REBASE_CERT)
    old_pure = load_json(OLD_CONSTRUCTOR_PURE_CERT)
    pure_atom = load_json(PURE_ATOM_CERT)
    source_packet = load_json(SOURCE_PACKET_CERT)
    rows = build_rows(latest, old_pure, pure_atom, source_packet)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_pure_pair_atom_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_source_tuple_signed_formula_imported": rows[0]["closed"],
        "existing_constructor_pure_pair_reusable": rows[1]["closed"],
        "pure_pair_atom_router_imported": rows[2]["closed"],
        "pure_pair_atom_bijection_synced": rows[3]["closed"],
        "tail_lift_phi_minus_one_synced": rows[4]["closed"],
        "tail_lift_no_new_first_seed_closed": rows[5]["closed"],
        "source_atoms_carried_forward": rows[6]["closed"],
        "pure_pair_atom_rebased": rows[7]["closed"],
        "pure_semiprime_pair_signed_seed_atom_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": OFFDIAG_SIGNED_FORMULA,
        "next_primary_attack_target": PURE_SEMIPRIME_ATOM,
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
        "imported_largest_sample": largest_sample(pure_atom),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor "
            "`PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` "
            "接入既有 pure-pair atom 证书。`tail=1` 是唯一 pure semiprime pair seed atom；"
            "`tail>1` 的 Phi-minus-one 质量不是新 first seed，只能进入 internal transition lift。"
            "最新直接主攻推进到 `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor pure-pair atom rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_source_tuple_signed_formula_imported={fmt_bool(result['latest_rebased_source_tuple_signed_formula_imported'])}",
        f"existing_constructor_pure_pair_reusable={fmt_bool(result['existing_constructor_pure_pair_reusable'])}",
        f"pure_pair_atom_router_imported={fmt_bool(result['pure_pair_atom_router_imported'])}",
        f"pure_pair_atom_bijection_synced={fmt_bool(result['pure_pair_atom_bijection_synced'])}",
        f"tail_lift_phi_minus_one_synced={fmt_bool(result['tail_lift_phi_minus_one_synced'])}",
        f"tail_lift_no_new_first_seed_closed={fmt_bool(result['tail_lift_no_new_first_seed_closed'])}",
        f"source_atoms_carried_forward={fmt_bool(result['source_atoms_carried_forward'])}",
        f"pure_pair_atom_rebased={fmt_bool(result['pure_pair_atom_rebased'])}",
        f"pure_semiprime_pair_signed_seed_atom_proved={fmt_bool(result['pure_semiprime_pair_signed_seed_atom_proved'])}",
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
                "| N | pure atoms | tail lift mass | ok |",
                "| --- | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['pure_semiprime_pair_seed_atoms']} | "
                    f"{sample['tail_lift_occurrences']} | "
                    f"`{fmt_bool(sample['pure_atom_type_bijection_holds'] and sample['tail_lift_decomposition_holds'])}` |"
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
