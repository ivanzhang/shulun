#!/usr/bin/env python3
"""生成 constructor-latest offdiagonal seed 到 tuple-fields 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_SEED_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.json"
)
TUPLE_FIELDS_CERT = DOCS / "prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json"
SOURCE_PACKET_CYCLE_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
OFFDIAG_TUPLE_FIELDS = "PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward"
OFFDIAG_SIGNED_FORMULA = (
    "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
)
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
    """读取 JSON 证书；缺失不能当作已证明。"""
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
    """返回 common packet 已携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_CONSTRUCTOR_SEED_CERT,
        TUPLE_FIELDS_CERT,
        SOURCE_PACKET_CYCLE_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_sample(tuple_cert: dict[str, Any]) -> dict[str, Any]:
    """抽取 tuple-fields 证书的最大样本。"""
    samples = tuple_cert.get("sample_offdiagonal_tuple_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    atoms = source_atoms()
    return [
        {
            "from": OFFDIAG_SEED,
            "to": (
                f"{OFFDIAG_TUPLE_FIELDS} AND {OFFDIAG_SIGNED_FORMULA} "
                f"AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}"
            ),
            "meaning": "constructor 最新 offdiagonal seed 黑箱拆成无符号 tuple 字段和仍开放的 signed/trace/ExactUV 字段。",
        },
        {
            "from": OFFDIAG_TUPLE_FIELDS,
            "to": "closed owner_p, first_q, q_rough_tail_t and Phi tail fiber mass",
            "meaning": "LPF/Phi 在此处只支付 owner、first rough prime、tail 纤维和 occurrence 容量。",
        },
        {
            "from": COMMON_PACKET,
            "to": atoms,
            "meaning": "diagonal/common packet 义务继续由 source 三原子携带；本层不把 common packet 当作自证终点。",
        },
        {
            "from": OFFDIAG_SEED,
            "to": (
                f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
                f"plus {INTERNAL_TRANSITION}, {ROW_MASS}, signed survival and carried source atoms"
            ),
            "meaning": "剥去 LPF/Phi 无符号层后，constructor 最新基只保留真正 signed/ExactUV/source 义务。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    tuple_cert: dict[str, Any],
    packet: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor-latest offdiagonal seed tuple 同步判定表。"""
    atoms = source_atoms()
    return [
        row(
            "LatestConstructorOffDiagonalSeedHardpointImported",
            latest.get("next_primary_attack_target") == OFFDIAG_SEED
            and latest.get("latest_basis_replaces_first_seed_with_offdiag_seed") is True,
            False,
            "上一层 constructor semiprime seed diagonal sync 已把新增 seed 口定位到 offdiagonal 表。",
            OFFDIAG_SEED,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "本层只剥离 OFFDIAG_SEED 的无符号 tuple 字段；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "OffDiagonalTupleFieldsRouterImported",
            tuple_cert.get("target_input_before_router") == OFFDIAG_SEED
            and tuple_cert.get("offdiagonal_semiprime_seed_tuple_fields_router_closed") is True,
            True,
            "既有 tuple-fields 证书可直接作用在 constructor 最新 offdiagonal seed 入口。",
            OFFDIAG_TUPLE_FIELDS,
        ),
        row(
            "OffDiagonalSourceTupleBijectionSynced",
            tuple_cert.get("offdiagonal_source_tuple_bijection_proved") is True,
            True,
            "每个 offdiagonal occurrence 唯一写成 `(owner_p, first_q, q_rough_tail_t)`。",
            OFFDIAG_TUPLE_FIELDS,
        ),
        row(
            "PhiTailFiberMassSynced",
            tuple_cert.get("offdiagonal_phi_tail_fiber_mass_proved") is True,
            True,
            "`sum_{p<q} Phi(floor(N/(p*q)),q)` 正好支付 tuple occurrence 质量。",
            "PhiLPFOffDiagonalQRoughTailFiberMassLedger",
        ),
        row(
            "LPFPhiUnsignedScopeExhausted",
            tuple_cert.get("offdiagonal_unsigned_tuple_fields_closed") is True,
            True,
            "LPF/Phi 桶恒等式已用尽：它只给支撑、tuple 字段和容量，不能产生 signed coefficient。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION}",
        ),
        row(
            "SourceAtomsCarriedForward",
            latest.get("carried_source_packet_attack_target") == atoms
            and (
                packet.get("common_packet_self_proof_rejected_after_lpf") is True
                or packet.get("common_packet_self_proof_blocked") is True
            ),
            False,
            "diagonal/common packet 义务在 constructor 最新基中仍以 source 三原子携带，尚未由本步证明。",
            atoms,
        ),
        row(
            "LatestBasisReplacesOffdiagSeedWithTuplePayload",
            tuple_cert.get("next_primary_attack_target") == OFFDIAG_SIGNED_FORMULA,
            False,
            "constructor 最新 offdiagonal seed 表被收窄为 source tuple signed formula 与配套字段。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV}",
        ),
        row(
            "OffDiagonalSignedFormulaStillOpen",
            tuple_cert.get("offdiagonal_signed_seed_formula_proved") is False,
            False,
            "当前语料没有给出 prepushforward source tuple signed seed 公式。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "OrientationParityStillOpen",
            tuple_cert.get("offdiagonal_orientation_parity_law_proved") is False,
            False,
            "orientation parity、branch side 与 local factor 仍不能由 LPF/Phi 字段推出。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "ExactUVReturnStillOpen",
            tuple_cert.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False
            or exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "ExactUV fixed pair、source entropy/fiber 与 return tag 仍是独立门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "InternalTransitionStillPaired",
            latest.get("internal_prime_adjoin_signed_transition_law_proved") is False
            and tuple_cert.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "tail 非单位 continuation 仍要求 internal prime-adjoin signed transition law。",
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
            "本步只同步 constructor offdiagonal seed 的 tuple-fields 剥离；未证明三命题无条件闭合。",
            (
                f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
                f"AND {INTERNAL_TRANSITION} AND {ROW_MASS} AND {NONZERO_SURVIVAL} AND {atoms}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 constructor 最新 offdiagonal seed tuple 同步证书。"""
    latest = load_json(LATEST_CONSTRUCTOR_SEED_CERT)
    tuple_cert = load_json(TUPLE_FIELDS_CERT)
    packet = load_json(SOURCE_PACKET_CYCLE_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest, tuple_cert, packet, pointwise, exactuv)
    atoms = source_atoms()
    latest_basis = (
        f"(({atoms} AND {OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {NEW_JOINT}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} "
        f"AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_sync_router",
        "status": "phi_lpf_latest_constructor_offdiagonal_seed_synced_to_tuple_fields_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_offdiagonal_seed_hardpoint_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "offdiagonal_tuple_fields_router_imported": rows[2]["closed"],
        "offdiagonal_source_tuple_bijection_synced": rows[3]["closed"],
        "offdiagonal_phi_tail_fiber_mass_synced": rows[4]["closed"],
        "offdiagonal_unsigned_tuple_fields_closed": rows[5]["closed"],
        "lpf_phi_unsigned_scope_exhausted_for_offdiag_seed": rows[5]["closed"],
        "source_atoms_carried_forward": rows[6]["closed"],
        "latest_basis_replaces_offdiag_seed_with_tuple_payload": rows[7]["closed"],
        "offdiagonal_signed_seed_formula_proved": False,
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
        "target_input_before_router": OFFDIAG_SEED,
        "closed_unsigned_subledger": OFFDIAG_TUPLE_FIELDS,
        "next_primary_attack_target": OFFDIAG_SIGNED_FORMULA,
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
        "imported_largest_sample": largest_sample(tuple_cert),
        "imported_tuple_fields": tuple_cert.get("offdiagonal_tuple_fields", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 最新 `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` "
            "接入既有 tuple-fields 证书。LPF/Phi 桶恒等式已关闭 offdiagonal source tuple 的 owner、"
            "first rough prime、q-rough tail 与 Phi fiber mass；因此 offdiagonal seed 口不再是未解析黑箱。"
            "剩余不能由 LPF/Phi 反推，必须正向提交 source tuple signed seed formula、orientation parity/"
            "branch side、ExactUV fixed pair/return tag，并保留 internal transition、source 三原子、"
            "signed survival 与 row-mass/no-heavy-row。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor offdiagonal seed tuple sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_offdiagonal_seed_hardpoint_imported={fmt_bool(cert['latest_constructor_offdiagonal_seed_hardpoint_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"offdiagonal_tuple_fields_router_imported={fmt_bool(cert['offdiagonal_tuple_fields_router_imported'])}",
        f"offdiagonal_source_tuple_bijection_synced={fmt_bool(cert['offdiagonal_source_tuple_bijection_synced'])}",
        f"offdiagonal_phi_tail_fiber_mass_synced={fmt_bool(cert['offdiagonal_phi_tail_fiber_mass_synced'])}",
        f"offdiagonal_unsigned_tuple_fields_closed={fmt_bool(cert['offdiagonal_unsigned_tuple_fields_closed'])}",
        f"lpf_phi_unsigned_scope_exhausted_for_offdiag_seed={fmt_bool(cert['lpf_phi_unsigned_scope_exhausted_for_offdiag_seed'])}",
        f"latest_basis_replaces_offdiag_seed_with_tuple_payload={fmt_bool(cert['latest_basis_replaces_offdiag_seed_with_tuple_payload'])}",
        f"offdiagonal_signed_seed_formula_proved={fmt_bool(cert['offdiagonal_signed_seed_formula_proved'])}",
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
