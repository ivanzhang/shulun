#!/usr/bin/env python3
"""生成 latest constructor two-prime no-swap 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_NO_SWAP_CERT = DOCS / "prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.json"
NO_SWAP_CERT = DOCS / "prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json"
SOURCE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"

TWO_PRIME_KERNEL = "PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward"
ORDERED_NO_SWAP = "PhiLPFOffDiagonalTwoPrimeOrderedLPFOwnerNoSwapSymmetryLedgerBeforePushforward"
EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
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
    """读取 JSON 证书；缺失不能当成闭合证明。"""
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
    return [LATEST_REBASE_CERT, OLD_CONSTRUCTOR_NO_SWAP_CERT, NO_SWAP_CERT, SOURCE_PACKET_CERT]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_atoms() -> str:
    """返回 source-packet 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    return (
        f"(({source_atoms()} AND {EDGE_LOCAL_FORMULA} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) OR "
        f"{POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {TERMINAL_WFD} OR {NEW_JOINT}) AND {SIGNED_SURVIVAL} "
        f"AND {SOURCE_EXACTUV} AND {COMPLETE_KEY} AND {FIXED_KEY} AND {HARMONIC} "
        f"AND {SKELETON} AND {RATE} AND {DSTRUCTURE}"
    )


def largest_sample(no_swap: dict[str, Any]) -> dict[str, Any]:
    """抽取 no-swap 证书最大样本读数。"""
    samples = no_swap.get("sample_ordered_no_swap_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def build_rows(
    latest: dict[str, Any],
    old_no_swap: dict[str, Any],
    no_swap: dict[str, Any],
    source_packet: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 no-swap rebase 判定表。"""
    latest_kernel_active = (
        latest.get("next_primary_attack_target") == TWO_PRIME_KERNEL
        and latest.get("pure_pair_ferrers_support_rebased") is True
    )
    old_no_swap_reusable = (
        old_no_swap.get("target_input_before_router") == TWO_PRIME_KERNEL
        and old_no_swap.get("latest_basis_replaces_two_prime_kernel_with_edge_local_formula") is True
        and old_no_swap.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA
    )
    no_swap_imported = (
        no_swap.get("target_input_before_router") == TWO_PRIME_KERNEL
        and no_swap.get("two_prime_ordered_no_swap_router_closed") is True
    )
    no_swap_closed = no_swap.get("lpf_owner_ordered_no_swap_identity_proved") is True
    source_cycle_guard = (
        source_packet.get("common_packet_self_proof_blocked") is True
        or source_packet.get("common_packet_self_proof_rejected_after_lpf") is True
    )
    rebase_closed = latest_kernel_active and old_no_swap_reusable and no_swap_imported and no_swap_closed
    return [
        row(
            "LatestRebasedTwoPrimeKernelImported",
            latest_kernel_active,
            False,
            "上一层 rebase 已把最新 constructor 窄口压到 two-prime signed interaction kernel。",
            TWO_PRIME_KERNEL,
        ),
        row(
            "ExistingConstructorNoSwapReusable",
            old_no_swap_reusable,
            False,
            "旧 constructor no-swap 同步证书输入相同，可在新 rebase 前沿复用。",
            f"{ORDERED_NO_SWAP} AND {EDGE_LOCAL_FORMULA}",
        ),
        row(
            "NoSwapRouterImported",
            no_swap_imported,
            True,
            "no-swap 证书剥离 LPF owner canonical order。",
            ORDERED_NO_SWAP,
        ),
        row(
            "LPFOwnerOrderedNoSwapClosed",
            no_swap_closed,
            True,
            "每个 distinct semiprime product 只有 canonical `(p,q)` source edge，无 reverse `(q,p)` source row。",
            ORDERED_NO_SWAP,
        ),
        row(
            "ProductSymmetryDoesNotEmitSignedKernel",
            no_swap.get("product_symmetry_signed_emission_proved") is False,
            True,
            "`pq=qp` 只识别整数值，不能供应第二个 pre-Cauchy signed source。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "SourceAtomsCarriedForward",
            source_atoms() in latest.get("paired_required_attack_targets", []) and source_cycle_guard,
            False,
            "source 三原子仍作为 carried input 保留，不能由 no-swap 自证。",
            source_atoms(),
        ),
        row(
            "TwoPrimeNoSwapRebased",
            rebase_closed,
            False,
            "最新 two-prime kernel 已同步为 canonical edge-local signed formula 或 named return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "EdgeLocalFormulaStillOpen",
            no_swap.get("edge_local_two_prime_signed_formula_proved") is False,
            False,
            "当前材料没有给出 canonical `(p,q)` edge-local signed formula 或 named return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "OrientationExactUVTransitionStillOpen",
            no_swap.get("paired_required_attack_targets", [])[:3]
            == [OFFDIAG_ORIENTATION, OFFDIAG_EXACTUV, INTERNAL_TRANSITION],
            False,
            "orientation、ExactUV return 与 internal transition 仍是独立门。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做 rebase 同步；未证明 edge-local formula、orientation、ExactUV、internal transition 或 source 三原子。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json(LATEST_REBASE_CERT)
    old_no_swap = load_json(OLD_CONSTRUCTOR_NO_SWAP_CERT)
    no_swap = load_json(NO_SWAP_CERT)
    source_packet = load_json(SOURCE_PACKET_CERT)
    rows = build_rows(latest, old_no_swap, no_swap, source_packet)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_two_prime_no_swap_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_two_prime_kernel_imported": rows[0]["closed"],
        "existing_constructor_no_swap_reusable": rows[1]["closed"],
        "no_swap_router_imported": rows[2]["closed"],
        "lpf_owner_ordered_no_swap_closed": rows[3]["closed"],
        "product_symmetry_does_not_emit_signed_kernel": rows[4]["closed"],
        "source_atoms_carried_forward": rows[5]["closed"],
        "two_prime_no_swap_rebased": rows[6]["closed"],
        "edge_local_two_prime_signed_formula_proved": False,
        "two_prime_signed_interaction_kernel_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TWO_PRIME_KERNEL,
        "closed_unsigned_subledger": ORDERED_NO_SWAP,
        "next_primary_attack_target": EDGE_LOCAL_FORMULA,
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
        "imported_largest_sample": largest_sample(no_swap),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward` "
            "接入 ordered no-swap 证书。LPF owner source domain 只保留 canonical ordered edge `(p,q)`，"
            "`p<q`；交换对称 `pq=qp` 不能供应反向 signed row 或 cancellation partner。最新直接主攻推进到 "
            "`PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor two-prime no-swap rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_two_prime_kernel_imported={fmt_bool(result['latest_rebased_two_prime_kernel_imported'])}",
        f"existing_constructor_no_swap_reusable={fmt_bool(result['existing_constructor_no_swap_reusable'])}",
        f"no_swap_router_imported={fmt_bool(result['no_swap_router_imported'])}",
        f"lpf_owner_ordered_no_swap_closed={fmt_bool(result['lpf_owner_ordered_no_swap_closed'])}",
        f"product_symmetry_does_not_emit_signed_kernel={fmt_bool(result['product_symmetry_does_not_emit_signed_kernel'])}",
        f"source_atoms_carried_forward={fmt_bool(result['source_atoms_carried_forward'])}",
        f"two_prime_no_swap_rebased={fmt_bool(result['two_prime_no_swap_rebased'])}",
        f"edge_local_two_prime_signed_formula_proved={fmt_bool(result['edge_local_two_prime_signed_formula_proved'])}",
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
                "| N | ordered edges | unordered products | reverse edges | duplicates | no-swap ok |",
                "| --- | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['ordered_edges']} | "
                    f"{sample['unordered_distinct_semiprime_products']} | {sample['reverse_edges_present']} | "
                    f"{sample['duplicate_product_count']} | `{fmt_bool(sample['lpf_owner_no_swap_identity_holds'])}` |"
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
