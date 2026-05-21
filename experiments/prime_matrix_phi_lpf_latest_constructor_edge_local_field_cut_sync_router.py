#!/usr/bin/env python3
"""生成 constructor-latest edge-local field-cut 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_edge_local_field_cut_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_NO_SWAP_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.json"
)
FIELD_CUT_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json"
SOURCE_PACKET_CYCLE_CERT = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
EDGE_LABEL_LEDGER = "PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward"
SIGNED_FIELD_TABLE = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
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
    """返回 constructor 最新基底中携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_CONSTRUCTOR_NO_SWAP_CERT,
        FIELD_CUT_CERT,
        SOURCE_PACKET_CYCLE_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_sample(field_cut: dict[str, Any]) -> dict[str, Any]:
    """抽取 field-cut 证书的最大样本。"""
    samples = field_cut.get("sample_edge_local_field_audit", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    return [
        {
            "from": EDGE_LOCAL_FORMULA,
            "to": f"{EDGE_LABEL_LEDGER} AND {SIGNED_FIELD_TABLE}",
            "meaning": "constructor edge-local formula 先剥离 LPF/Phi/Ferrers 无符号 edge label，剩余才是 signed atom fields 或命名 return。",
        },
        {
            "from": EDGE_LABEL_LEDGER,
            "to": "closed owner p, first q, product pq, row/column degree, multiplicity one",
            "meaning": "这些字段由 LPF bucket、pure-pair Ferrers 支撑与 product label 唯一支付。",
        },
        {
            "from": "constructor carried side gates",
            "to": f"{NONZERO_SURVIVAL}, {ROW_MASS}, {COMPLETE_KEY}, {FIXED_KEY}",
            "meaning": "field-cut 只处理 edge label，不吸收 signed survival、row mass/no-heavy-row 或 key partition 义务。",
        },
        {
            "from": "latest constructor carried source packet",
            "to": source_atoms(),
            "meaning": "constructor no-swap 基底已经把 common packet 义务显式携带为 source 三原子。",
        },
        {
            "from": EDGE_LOCAL_FORMULA,
            "to": (
                f"{SIGNED_FIELD_TABLE} plus {OFFDIAG_ORIENTATION}, {OFFDIAG_EXACTUV}, "
                f"{INTERNAL_TRANSITION}, constructor side gates, and carried source atoms"
            ),
            "meaning": "constructor 最新 edge-local 入口被收窄为逐 edge signed fields/return 与配套字段。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    field_cut: dict[str, Any],
    packet: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最新 edge-local field-cut 同步判定表。"""
    atoms = source_atoms()
    return [
        row(
            "LatestConstructorEdgeLocalFormulaImported",
            latest.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA,
            False,
            "上一层 constructor no-swap sync 已把直接硬点定位到 edge-local formula-or-return。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "本层只替换 edge-local formula；signed survival、row-mass/no-heavy-row 与 key 账本仍是 constructor 侧门。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "FieldCutRouterImported",
            field_cut.get("target_input_before_router") == EDGE_LOCAL_FORMULA
            and field_cut.get("edge_local_closed_unsigned_label_ledger_proved") is True,
            True,
            "既有 edge-local field-cut 证书可直接作用在 constructor 最新 edge-local 入口。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "ClosedUnsignedEdgeLabelLedgerSynced",
            field_cut.get("edge_label_bijection_proved") is True
            and field_cut.get("lpf_bucket_product_fields_proved") is True
            and field_cut.get("ferrers_rank_degree_fields_proved") is True,
            True,
            "owner、first q、product、LPF bucket 与 Ferrers rank/degree 字段同步闭合。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "EdgeAtomMultiplicityOneSynced",
            field_cut.get("edge_atom_multiplicity_one_proved") is True,
            True,
            "每个 canonical product `pq` 只有一个 pure-pair source atom label。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "LPFPhiUnsignedScopeExhaustedForEdgeLocal",
            field_cut.get("signed_atom_field_table_proved") is False,
            True,
            "LPF/Phi/Ferrers 只支付无符号 label，不产生 sign、local factor、orientation 或 ExactUV return。",
            SIGNED_FIELD_TABLE,
        ),
        row(
            "ConstructorSideGatesNotPaidByFieldCut",
            field_cut.get("edge_local_closed_unsigned_label_ledger_proved") is True,
            True,
            "closed edge label 不包含 signed survival、primitive row mass、complete key 或 fixed-key multiplicity。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}",
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
            "LatestConstructorBasisReplacesEdgeLocalFormulaWithSignedAtomFields",
            field_cut.get("next_primary_attack_target") == SIGNED_FIELD_TABLE,
            False,
            "constructor 最新 edge-local formula 被收窄为 signed atom fields 或命名 return tag。",
            SIGNED_FIELD_TABLE,
        ),
        row(
            "SignedAtomFieldTableStillOpen",
            field_cut.get("signed_atom_field_table_proved") is False,
            False,
            "当前语料没有提交逐 edge signed seed/local factor 表或命名 return tag 表。",
            SIGNED_FIELD_TABLE,
        ),
        row(
            "OrientationParityStillOpen",
            field_cut.get("orientation_parity_branch_side_proved") is False,
            False,
            "orientation parity、branch side 与 alpha/delta 侧别仍是独立 signed 字段。",
            OFFDIAG_ORIENTATION,
        ),
        row(
            "ExactUVReturnStillOpen",
            field_cut.get("exactuv_fixed_pair_return_tag_proved") is False
            or exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "ExactUV fixed pair、fiber 与 return tag 仍是独立门。",
            OFFDIAG_EXACTUV,
        ),
        row(
            "InternalTransitionStillPaired",
            INTERNAL_TRANSITION in latest.get("paired_required_attack_targets", []),
            False,
            "tail-lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。",
            INTERNAL_TRANSITION,
        ),
        row(
            "ConstructorSideGatesStillOpen",
            latest.get("nonzero_signed_row_survival_proved") is False
            and latest.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "constructor 侧的 signed survival 与 same-unit row-mass/no-heavy-row 未被本 field-cut 证明。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
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
            "本步只同步 edge label field-cut；未证明三命题无条件闭合。",
            (
                f"{SIGNED_FIELD_TABLE} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
                f"AND {INTERNAL_TRANSITION} AND {ROW_MASS} AND {NONZERO_SURVIVAL} AND {atoms}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 constructor 最新 edge-local field-cut 同步证书。"""
    latest = load_json(LATEST_CONSTRUCTOR_NO_SWAP_CERT)
    field_cut = load_json(FIELD_CUT_CERT)
    packet = load_json(SOURCE_PACKET_CYCLE_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest, field_cut, packet, pointwise, exactuv)
    atoms = source_atoms()
    latest_basis = (
        f"(({atoms} AND {SIGNED_FIELD_TABLE} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {ROW_MASS}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {TERMINAL_DESCENT} "
        f"OR {PDEC_SCOPE} OR {NEW_JOINT}) AND {NONZERO_SURVIVAL} AND {COMPLETE_KEY} "
        f"AND {FIXED_KEY} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_edge_local_field_cut_sync_router",
        "status": "phi_lpf_latest_constructor_edge_local_formula_synced_to_unsigned_field_cut_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_edge_local_formula_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "field_cut_router_imported": rows[2]["closed"],
        "closed_unsigned_edge_label_ledger_synced": rows[3]["closed"],
        "edge_atom_multiplicity_one_synced": rows[4]["closed"],
        "lpf_phi_unsigned_scope_exhausted_for_edge_local": rows[5]["closed"],
        "constructor_side_gates_not_paid_by_field_cut": rows[6]["closed"],
        "source_atoms_carried_forward": rows[7]["closed"],
        "latest_constructor_basis_replaces_edge_local_formula_with_signed_atom_fields": rows[8]["closed"],
        "signed_atom_field_table_proved": False,
        "orientation_parity_branch_side_proved": False,
        "exactuv_fixed_pair_return_tag_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exactuv_local_multiplicity_o1_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EDGE_LOCAL_FORMULA,
        "closed_unsigned_subledger": EDGE_LABEL_LEDGER,
        "next_primary_attack_target": SIGNED_FIELD_TABLE,
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
        "imported_largest_sample": largest_sample(field_cut),
        "imported_closed_edge_fields": field_cut.get("closed_edge_fields", []),
        "imported_open_signed_fields_or_returns": field_cut.get("open_signed_fields_or_returns", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 最新 `PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward` "
            "接入 edge-local field-cut。LPF/Phi/Ferrers 已经支付每条 canonical `(p,q)` "
            "edge 的 owner、first prime、product、rank/degree 与 multiplicity-one label；"
            "剩余不再是支撑、容量或交换对称，而是逐 edge 的 signed atom fields 或命名 return tag，"
            "并仍需 orientation、ExactUV return、internal transition、source 三原子、signed survival "
            "与 row-mass/no-heavy-row 等 constructor 侧门。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor edge-local field-cut sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_edge_local_formula_imported={fmt_bool(cert['latest_constructor_edge_local_formula_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"field_cut_router_imported={fmt_bool(cert['field_cut_router_imported'])}",
        f"closed_unsigned_edge_label_ledger_synced={fmt_bool(cert['closed_unsigned_edge_label_ledger_synced'])}",
        f"edge_atom_multiplicity_one_synced={fmt_bool(cert['edge_atom_multiplicity_one_synced'])}",
        f"lpf_phi_unsigned_scope_exhausted_for_edge_local={fmt_bool(cert['lpf_phi_unsigned_scope_exhausted_for_edge_local'])}",
        f"constructor_side_gates_not_paid_by_field_cut={fmt_bool(cert['constructor_side_gates_not_paid_by_field_cut'])}",
        f"latest_constructor_basis_replaces_edge_local_formula_with_signed_atom_fields={fmt_bool(cert['latest_constructor_basis_replaces_edge_local_formula_with_signed_atom_fields'])}",
        f"signed_atom_field_table_proved={fmt_bool(cert['signed_atom_field_table_proved'])}",
        f"orientation_parity_branch_side_proved={fmt_bool(cert['orientation_parity_branch_side_proved'])}",
        f"exactuv_fixed_pair_return_tag_proved={fmt_bool(cert['exactuv_fixed_pair_return_tag_proved'])}",
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
                "| N | canonical edges | labels | products | LPF ok | row deg ok | col deg ok | atom x1 | open signed slots/edge |",
                "| --- | ---: | ---: | ---: | --- | --- | --- | --- | ---: |",
                (
                    f"| {sample['N']} | {sample['canonical_edges']} | "
                    f"{sample['unique_edge_labels']} | {sample['unique_products']} | "
                    f"`{fmt_bool(sample['lpf_bucket_identity_holds'])}` | "
                    f"`{fmt_bool(sample['row_degree_formula_holds'])}` | "
                    f"`{fmt_bool(sample['column_degree_formula_holds'])}` | "
                    f"`{fmt_bool(sample['atom_multiplicity_one_holds'])}` | "
                    f"{sample['open_signed_field_count_per_edge']} |"
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
