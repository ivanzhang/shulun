#!/usr/bin/env python3
"""生成 constructor-latest source-tuple 到 pure-pair atom 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_TUPLE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json"
)
PURE_ATOM_CERT = DOCS / "prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json"
SOURCE_PACKET_CYCLE_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

OFFDIAG_SIGNED_FORMULA = (
    "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
)
PURE_SEMIPRIME_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
TAIL_LIFT = "PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
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
        LATEST_CONSTRUCTOR_TUPLE_CERT,
        PURE_ATOM_CERT,
        SOURCE_PACKET_CYCLE_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_sample(pure_atom: dict[str, Any]) -> dict[str, Any]:
    """抽取 pure atom 证书的最大样本。"""
    samples = pure_atom.get("sample_pure_seed_atom_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    atoms = source_atoms()
    return [
        {
            "from": OFFDIAG_SIGNED_FORMULA,
            "to": f"{PURE_SEMIPRIME_ATOM} AND {TAIL_LIFT}",
            "meaning": "constructor source tuple signed formula 的 first-seed 部分强制落到 tail=1 pure pair；tail>1 是 continuation lift。",
        },
        {
            "from": TAIL_LIFT,
            "to": INTERNAL_TRANSITION,
            "meaning": "`Phi(floor(N/(p*q)),q)-1` 的 tail-lift 质量不是新 first seed，只能交给 internal transition compatibility。",
        },
        {
            "from": COMMON_PACKET,
            "to": atoms,
            "meaning": "pure-pair 路线中的 common packet 义务在 constructor 最新基中仍由 source 三原子携带。",
        },
        {
            "from": OFFDIAG_SIGNED_FORMULA,
            "to": (
                f"{PURE_SEMIPRIME_ATOM} plus {OFFDIAG_ORIENTATION}, {OFFDIAG_EXACTUV}, "
                f"{INTERNAL_TRANSITION}, {ROW_MASS}, signed survival, and carried source atoms"
            ),
            "meaning": "constructor 最新 source tuple formula 被收窄为 pure-pair signed atom 与配套 signed/ExactUV/transition/source 字段。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    pure_atom: dict[str, Any],
    packet: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor 最新 pure-pair atom 同步判定表。"""
    atoms = source_atoms()
    return [
        row(
            "LatestConstructorSourceTupleSignedFormulaImported",
            latest.get("next_primary_attack_target") == OFFDIAG_SIGNED_FORMULA
            and latest.get("latest_basis_replaces_offdiag_seed_with_tuple_payload") is True,
            False,
            "上一层 constructor tuple sync 已把直接硬点定位到 source tuple signed seed formula。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "本层只替换 source tuple formula；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "PurePairAtomRouterImported",
            pure_atom.get("target_input_before_router") == OFFDIAG_SIGNED_FORMULA
            and pure_atom.get("offdiagonal_pure_semiprime_seed_atom_router_closed") is True,
            True,
            "既有 pure semiprime atom 证书可直接作用在 constructor 最新 source tuple formula 入口。",
            f"{PURE_SEMIPRIME_ATOM} AND {TAIL_LIFT}",
        ),
        row(
            "PurePairAtomBijectionSynced",
            pure_atom.get("pure_semiprime_pair_seed_atom_bijection_proved") is True,
            True,
            "每个 ordered type `(p,q), p<q` 恰有一个 tail=1 pure pair seed atom。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "TailLiftPhiMinusOneSynced",
            pure_atom.get("tail_lift_phi_minus_one_mass_formula_proved") is True,
            True,
            "tail continuation 质量为 `Phi(floor(N/(p*q)),q)-1`。",
            TAIL_LIFT,
        ),
        row(
            "TailLiftNoNewFirstSeedClosed",
            pure_atom.get("tail_nonunit_reduced_to_internal_transition_lift") is True,
            True,
            "tail>1 occurrence 不是新 first seed，只能作为同一 pure atom 的 internal transition lift。",
            INTERNAL_TRANSITION,
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
            "LatestBasisReplacesTupleFormulaWithPureAtom",
            pure_atom.get("next_primary_attack_target") == PURE_SEMIPRIME_ATOM,
            False,
            "constructor 最新 source tuple formula 被收窄为 pure-pair signed atom 与 tail-lift/internal-transition 配套。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "PurePairSignedAtomStillOpen",
            pure_atom.get("pure_semiprime_pair_signed_seed_atom_proved") is False,
            False,
            "LPF/Phi 和 tail=1 定位不给 pure pair 的 signed seed value。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "OrientationParityStillOpen",
            pure_atom.get("offdiagonal_orientation_parity_law_proved") is False,
            False,
            "pure atom 仍需 orientation parity、branch side 与 local factor law。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "ExactUVReturnStillOpen",
            pure_atom.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False
            or exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "ExactUV fixed pair、source entropy/fiber 与 return tag 仍是独立门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "InternalTransitionStillPaired",
            pure_atom.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "tail-lift compatibility 仍依赖 internal prime-adjoin signed transition law。",
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
            "本步只同步 constructor pure-pair atom 拆解；未证明三命题无条件闭合。",
            (
                f"{PURE_SEMIPRIME_ATOM} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
                f"AND {INTERNAL_TRANSITION} AND {ROW_MASS} AND {NONZERO_SURVIVAL} AND {atoms}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 constructor 最新 pure-pair atom 同步证书。"""
    latest = load_json(LATEST_CONSTRUCTOR_TUPLE_CERT)
    pure_atom = load_json(PURE_ATOM_CERT)
    packet = load_json(SOURCE_PACKET_CYCLE_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest, pure_atom, packet, pointwise, exactuv)
    atoms = source_atoms()
    latest_basis = (
        f"(({atoms} AND {PURE_SEMIPRIME_ATOM} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {NEW_JOINT}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} "
        f"AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_sync_router",
        "status": "phi_lpf_latest_constructor_source_tuple_synced_to_pure_pair_atom_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_source_tuple_signed_formula_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "pure_pair_atom_router_imported": rows[2]["closed"],
        "pure_pair_atom_bijection_synced": rows[3]["closed"],
        "tail_lift_phi_minus_one_synced": rows[4]["closed"],
        "tail_lift_no_new_first_seed_closed": rows[5]["closed"],
        "source_atoms_carried_forward": rows[6]["closed"],
        "latest_basis_replaces_tuple_formula_with_pure_atom": rows[7]["closed"],
        "pure_semiprime_pair_signed_seed_atom_proved": False,
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
        "target_input_before_router": OFFDIAG_SIGNED_FORMULA,
        "closed_unsigned_subledgers": [
            f"{PURE_SEMIPRIME_ATOM}_unsigned_domain",
            TAIL_LIFT,
        ],
        "next_primary_attack_target": PURE_SEMIPRIME_ATOM,
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
        "imported_largest_sample": largest_sample(pure_atom),
        "imported_pure_atom_fields": pure_atom.get("pure_semiprime_atom_fields", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 最新 `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` "
            "接入 pure semiprime atom 拆解。每个 ordered type `(p,q), p<q` 的 first seed 原子是唯一 "
            "`tail=1` pure pair `p*q`；`tail>1` 的 Phi 质量为 `Phi(floor(N/(p*q)),q)-1`，"
            "只能作为 internal transition lift，而不是新 first seed。剩余直接硬点收窄为 pure pair "
            "signed seed atom，并仍需 orientation、ExactUV return、internal transition、source 三原子、"
            "signed survival 与 row-mass/no-heavy-row。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor pure-pair atom sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_source_tuple_signed_formula_imported={fmt_bool(cert['latest_constructor_source_tuple_signed_formula_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"pure_pair_atom_router_imported={fmt_bool(cert['pure_pair_atom_router_imported'])}",
        f"pure_pair_atom_bijection_synced={fmt_bool(cert['pure_pair_atom_bijection_synced'])}",
        f"tail_lift_phi_minus_one_synced={fmt_bool(cert['tail_lift_phi_minus_one_synced'])}",
        f"tail_lift_no_new_first_seed_closed={fmt_bool(cert['tail_lift_no_new_first_seed_closed'])}",
        f"latest_basis_replaces_tuple_formula_with_pure_atom={fmt_bool(cert['latest_basis_replaces_tuple_formula_with_pure_atom'])}",
        f"pure_semiprime_pair_signed_seed_atom_proved={fmt_bool(cert['pure_semiprime_pair_signed_seed_atom_proved'])}",
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
                "| N | types | pure atoms | tail lift | total occ | pure share | tail share | ok |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
                (
                    f"| {sample['N']} | {sample['offdiagonal_seed_types']} | "
                    f"{sample['pure_semiprime_pair_seed_atoms']} | {sample['tail_lift_occurrences']} | "
                    f"{sample['offdiagonal_total_occurrences']} | {sample['pure_atom_share_of_occurrences']} | "
                    f"{sample['tail_lift_share_of_occurrences']} | "
                    f"`{fmt_bool(sample['pure_atom_type_bijection_holds'] and sample['tail_lift_decomposition_holds'])}` |"
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
