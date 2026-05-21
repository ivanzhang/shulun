#!/usr/bin/env python3
"""生成 constructor-latest two-prime signed kernel 到 no-swap 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_FERRERS_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-sync-router.json"
)
NO_SWAP_CERT = DOCS / "prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json"
SOURCE_PACKET_CYCLE_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

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
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
NONZERO_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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


def source_atoms() -> str:
    """返回 common packet 在 constructor 最新基中携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_CONSTRUCTOR_FERRERS_CERT,
        NO_SWAP_CERT,
        SOURCE_PACKET_CYCLE_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_sample(no_swap: dict[str, Any]) -> dict[str, Any]:
    """抽取 no-swap 证书的最大样本。"""
    samples = no_swap.get("sample_ordered_no_swap_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    atoms = source_atoms()
    return [
        {
            "from": TWO_PRIME_KERNEL,
            "to": f"{ORDERED_NO_SWAP} AND {EDGE_LOCAL_FORMULA}",
            "meaning": "constructor two-prime kernel 先剥离 LPF owner canonical order；交换对称不能供应 signed kernel。",
        },
        {
            "from": ORDERED_NO_SWAP,
            "to": "closed canonical edge (p,q), p<q, with no reverse source row",
            "meaning": "`p*q=q*p` 在 signed source 前已被 LPF owner 顺序擦除。",
        },
        {
            "from": COMMON_PACKET,
            "to": atoms,
            "meaning": "no-swap 不处理 common packet；该义务仍由 source 三原子携带。",
        },
        {
            "from": TWO_PRIME_KERNEL,
            "to": (
                f"{EDGE_LOCAL_FORMULA} plus {OFFDIAG_ORIENTATION}, {OFFDIAG_EXACTUV}, "
                f"{INTERNAL_TRANSITION}, {ROW_MASS}, signed survival, and carried source atoms"
            ),
            "meaning": "constructor 最新 two-prime kernel 被收窄为 canonical edge-local signed interaction formula 或命名 return。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    no_swap: dict[str, Any],
    packet: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor 最新 no-swap 同步判定表。"""
    atoms = source_atoms()
    return [
        row(
            "LatestConstructorTwoPrimeKernelImported",
            latest.get("next_primary_attack_target") == TWO_PRIME_KERNEL
            and latest.get("latest_basis_replaces_pure_atom_with_two_prime_kernel") is True,
            False,
            "上一层 constructor Ferrers sync 已把直接硬点定位到 two-prime signed interaction kernel。",
            TWO_PRIME_KERNEL,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "本层只替换 two-prime kernel；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "NoSwapRouterImported",
            no_swap.get("target_input_before_router") == TWO_PRIME_KERNEL
            and no_swap.get("two_prime_ordered_no_swap_router_closed") is True,
            True,
            "既有 ordered no-swap 证书可直接作用在 constructor 最新 two-prime kernel 入口。",
            ORDERED_NO_SWAP,
        ),
        row(
            "LPFOwnerOrderedNoSwapSynced",
            no_swap.get("lpf_owner_ordered_no_swap_identity_proved") is True,
            True,
            "每个 semiprime product 只有 canonical `(p,q)` source edge，没有 reverse `(q,p)` source edge。",
            ORDERED_NO_SWAP,
        ),
        row(
            "ProductSymmetryCannotEmitSignedKernel",
            no_swap.get("product_symmetry_signed_emission_proved") is False,
            True,
            "`p*q=q*p` 只是同一整数值，不提供第二个 pre-Cauchy signed source row。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "SourceAtomsCarriedForward",
            atoms in latest.get("paired_required_attack_targets", [])
            and (
                packet.get("common_packet_self_proof_rejected_after_lpf") is True
                or packet.get("common_packet_self_proof_blocked") is True
            ),
            False,
            "common packet 义务继续以 source 三原子携带，本步不证明这三原子。",
            atoms,
        ),
        row(
            "LatestBasisReplacesTwoPrimeKernelWithEdgeLocalFormula",
            no_swap.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA,
            False,
            "constructor 最新 two-prime kernel 被收窄为 canonical edge-local signed formula 或命名 return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "EdgeLocalFormulaStillOpen",
            no_swap.get("edge_local_two_prime_signed_formula_proved") is False,
            False,
            "当前语料没有为 canonical ordered edge `(p,q)` 提交 signed interaction formula 或 return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "TwoPrimeSignedKernelStillOpen",
            no_swap.get("two_prime_signed_interaction_kernel_proved") is False,
            False,
            "no-swap 只删除交换伪出口，不证明 two-prime signed kernel。",
            TWO_PRIME_KERNEL,
        ),
        row(
            "OrientationParityStillOpen",
            no_swap.get("paired_required_attack_targets", [None])[0] == OFFDIAG_ORIENTATION,
            False,
            "edge-local formula 仍需 orientation parity、branch side 与 local factor law。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "ExactUVReturnStillOpen",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or no_swap.get("paired_required_attack_targets", [None, None])[1] == OFFDIAG_EXACTUV,
            False,
            "ExactUV fixed pair、source entropy/fiber 与 return tag 仍是独立门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "InternalTransitionStillPaired",
            no_swap.get("paired_required_attack_targets", [None, None, None])[2]
            == INTERNAL_TRANSITION,
            False,
            "tail-lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。",
            INTERNAL_TRANSITION,
        ),
        row(
            "PointwiseSignedTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed value table 仍是并行旁路，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 constructor ordered no-swap 剥离；未证明三命题无条件闭合。",
            (
                f"{EDGE_LOCAL_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
                f"AND {INTERNAL_TRANSITION} AND {ROW_MASS} AND {NONZERO_SURVIVAL} AND {atoms}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 constructor 最新 no-swap 同步证书。"""
    latest = load_json(LATEST_CONSTRUCTOR_FERRERS_CERT)
    no_swap = load_json(NO_SWAP_CERT)
    packet = load_json(SOURCE_PACKET_CYCLE_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest, no_swap, packet, pointwise, exactuv)
    atoms = source_atoms()
    latest_basis = (
        f"(({atoms} AND {EDGE_LOCAL_FORMULA} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {NEW_JOINT}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} "
        f"AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_sync_router",
        "status": "phi_lpf_latest_constructor_two_prime_kernel_synced_to_ordered_no_swap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_two_prime_kernel_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "no_swap_router_imported": rows[2]["closed"],
        "lpf_owner_ordered_no_swap_synced": rows[3]["closed"],
        "product_symmetry_signed_emission_proved": False,
        "source_atoms_carried_forward": rows[5]["closed"],
        "latest_basis_replaces_two_prime_kernel_with_edge_local_formula": rows[6]["closed"],
        "edge_local_two_prime_signed_formula_proved": False,
        "two_prime_signed_interaction_kernel_proved": False,
        "offdiagonal_orientation_parity_law_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_arithmetic_identity_proved": False,
        "same_unit_exactuv_rank_multiplicity_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TWO_PRIME_KERNEL,
        "closed_unsigned_subledger": ORDERED_NO_SWAP,
        "next_primary_attack_target": EDGE_LOCAL_FORMULA,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            ROW_MASS,
            atoms,
        ],
        "parallel_constructor_side_gates": f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        "parallel_direct_bypass": POINTWISE_TABLE,
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "imported_largest_sample": largest_sample(no_swap),
        "imported_ordered_no_swap_fields": no_swap.get("ordered_no_swap_fields", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 最新 `PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward` "
            "接入 ordered no-swap 拆解。LPF owner source domain 只保留 canonical ordered edge `(p,q)`，"
            "`p<q`；交换对称 `p*q=q*p` 在 signed source 前已经被擦除，不能供应反向 signed row "
            "或 cancellation partner。因此最新 hardpoint 收窄为 edge-local two-prime signed interaction "
            "formula 或命名 return，并仍需 orientation、ExactUV return、internal transition、source 三原子、"
            "signed survival 与 row-mass/no-heavy-row。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor two-prime no-swap sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_two_prime_kernel_imported={fmt_bool(cert['latest_constructor_two_prime_kernel_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"no_swap_router_imported={fmt_bool(cert['no_swap_router_imported'])}",
        f"lpf_owner_ordered_no_swap_synced={fmt_bool(cert['lpf_owner_ordered_no_swap_synced'])}",
        f"product_symmetry_signed_emission_proved={fmt_bool(cert['product_symmetry_signed_emission_proved'])}",
        f"latest_basis_replaces_two_prime_kernel_with_edge_local_formula={fmt_bool(cert['latest_basis_replaces_two_prime_kernel_with_edge_local_formula'])}",
        f"edge_local_two_prime_signed_formula_proved={fmt_bool(cert['edge_local_two_prime_signed_formula_proved'])}",
        f"two_prime_signed_interaction_kernel_proved={fmt_bool(cert['two_prime_signed_interaction_kernel_proved'])}",
        f"offdiagonal_orientation_parity_law_proved={fmt_bool(cert['offdiagonal_orientation_parity_law_proved'])}",
        f"offdiagonal_exactuv_fixed_pair_return_ledger_proved={fmt_bool(cert['offdiagonal_exactuv_fixed_pair_return_ledger_proved'])}",
        f"internal_prime_adjoin_signed_transition_law_proved={fmt_bool(cert['internal_prime_adjoin_signed_transition_law_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(cert['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(cert['same_formal_unit_row_mass_normalization_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    sample = cert.get("imported_largest_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 3. 导入样本读数",
                "",
                "| N | ordered edges | unordered products | reverse edges | duplicates | small-q | large-q | no-swap ok |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['ordered_edges']} | "
                    f"{sample['unordered_distinct_semiprime_products']} | "
                    f"{sample['reverse_edges_present']} | {sample['duplicate_product_count']} | "
                    f"{sample['small_q_edges']} | {sample['large_q_edges']} | "
                    f"`{fmt_bool(sample['lpf_owner_no_swap_identity_holds'])}` |"
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            "\n".join(cert["paired_required_attack_targets"]),
            "```",
            "",
            "并行 constructor 侧门：",
            "",
            "```text",
            cert["parallel_constructor_side_gates"],
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
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
