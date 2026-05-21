#!/usr/bin/env python3
"""生成 constructor-latest signed atom trace-sync 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_signed_atom_trace_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR_FIELD_CUT_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json"
)
TRACE_SYNC_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

SIGNED_ATOM_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
TRACE_SYNC = "PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
NONZERO_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
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
    """返回 constructor 最新分支携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_CONSTRUCTOR_FIELD_CUT_CERT,
        TRACE_SYNC_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_slot_sample(trace_sync: dict[str, Any]) -> dict[str, Any]:
    """抽取 trace-sync 证书的最大 slot 样本。"""
    samples = trace_sync.get("sample_slot_counts", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出本层同步链。"""
    atoms = source_atoms()
    return [
        {
            "from": SIGNED_ATOM_FIELDS,
            "to": TRACE_SYNC,
            "meaning": "逐 edge signed fields 必须落在同一 pre-Cauchy trace key；否则进入命名 split/PDEC return。",
        },
        {
            "from": TRACE_SYNC,
            "to": NEW_PAYLOAD,
            "meaning": "命名 return 矩阵关闭匿名缺口后，生产性入口只剩新 primitive payload/trace 工件。",
        },
        {
            "from": "constructor carried source and side ledgers",
            "to": f"{atoms}, {ROW_MASS}, {NONZERO_SURVIVAL}, {COMPLETE_KEY}, {FIXED_KEY}",
            "meaning": "trace-sync 只关闭 same-key/return 路由，不证明 constructor source 三原子、signed survival 或 key 账本。",
        },
        {
            "from": SIGNED_ATOM_FIELDS,
            "to": f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}",
            "meaning": "若不提交新 payload/trace，则只能走 terminal descent、same-set PDEC 或逐点 signed table 旁路。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    trace_sync: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor 最新 signed atom trace-sync 同步判定表。"""
    atoms = source_atoms()
    return [
        row(
            "LatestConstructorSignedAtomFieldsImported",
            latest.get("next_primary_attack_target") == SIGNED_ATOM_FIELDS,
            False,
            "上一层 constructor field-cut 已把直接硬点定位到 signed atom fields 或 named return tag。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "ConstructorSideGatesCarried",
            latest.get("parallel_constructor_side_gates") == f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
            False,
            "本层只替换 signed atom fields；signed survival、row-mass/no-heavy-row 与 key 账本继续保留。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "TraceSyncRouterImported",
            trace_sync.get("target_input_before_router") == SIGNED_ATOM_FIELDS
            and trace_sync.get("same_trace_key_requirement_closed") is True,
            True,
            "既有 signed atom trace-sync 证书可直接作用在 constructor 最新 signed atom fields 入口。",
            TRACE_SYNC,
        ),
        row(
            "ClosedUnsignedLabelsCarried",
            latest.get("closed_unsigned_edge_label_ledger_synced") is True
            and trace_sync.get("closed_unsigned_edge_labels_imported") is True,
            True,
            "无符号 edge label 只作为 trace-sync 输入域携带，不产生 signed payload。",
            latest.get("closed_unsigned_subledger", "closed unsigned edge label ledger"),
        ),
        row(
            "SameTraceKeyAndNamedReturnMatrixSynced",
            trace_sync.get("same_trace_key_requirement_closed") is True
            and trace_sync.get("named_return_matrix_closed") is True,
            True,
            "缺失、冲突、零因子、超预算或跨 key 读取均进入命名 return，不再是匿名出口。",
            TRACE_SYNC,
        ),
        row(
            "ConstructorSourceAtomsCarriedForward",
            atoms in latest.get("paired_required_attack_targets", []),
            False,
            "source 三原子仍是 constructor payload 分支的携带义务，本步不证明它们。",
            atoms,
        ),
        row(
            "ConstructorSideGatesNotPaidByTraceSync",
            latest.get("nonzero_signed_row_survival_proved") is False
            and latest.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "same-trace/return 矩阵不支付 signed survival、row mass、complete key 或 fixed-key multiplicity。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "TraceSelfProofCycleCutSynced",
            trace_sync.get("signed_lane_self_proof_eliminated") is True
            and trace_sync.get("branch_trace_self_proof_eliminated") is True,
            True,
            "branch/atomic trace 不能在当前内部语料中自证 signed atom payload。",
            NEW_PAYLOAD,
        ),
        row(
            "LatestConstructorBasisReplacesSignedAtomFieldsWithNewPayloadOrExits",
            trace_sync.get("next_primary_attack_target") == NEW_PAYLOAD,
            False,
            "constructor 最新 signed atom fields 被收窄为新 primitive payload/trace 或受控旁路出口。",
            NEW_PAYLOAD,
        ),
        row(
            "NewPrimitivePayloadStillOpen",
            trace_sync.get("new_primitive_payload_or_trace_artifact_present") is False,
            False,
            "当前语料没有提交新 primitive atomic signed payload 或 trace formula 工件。",
            NEW_PAYLOAD,
        ),
        row(
            "EdgeLocalSignedAtomFieldsStillOpen",
            trace_sync.get("edge_local_signed_atom_fields_proved") is False,
            False,
            "trace-sync 关闭路由与 return 命名，不给 signed value/local factor 公式。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "PointwiseSignedTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 仍是并行旁路，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ExactUVPairStillRequired",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or EXACTUV_PAIR in trace_sync.get("parallel_attack_targets", []),
            False,
            "trace-sync 不替代 source entropy 与 ExactUV fiber 有界性。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 signed atom trace-sync；未证明三命题无条件闭合。",
            (
                f"(({atoms} AND {ROW_MASS} AND {NEW_PAYLOAD}) OR {TERMINAL_DESCENT} "
                f"OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {NONZERO_SURVIVAL} "
                f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 constructor 最新 signed atom trace-sync 同步证书。"""
    latest = load_json(LATEST_CONSTRUCTOR_FIELD_CUT_CERT)
    trace_sync = load_json(TRACE_SYNC_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest, trace_sync, pointwise, exactuv)
    atoms = source_atoms()
    latest_basis = (
        f"(({atoms} AND {ROW_MASS} AND {NEW_PAYLOAD}) OR {TERMINAL_DESCENT} "
        f"OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_signed_atom_trace_sync_router",
        "status": "phi_lpf_latest_constructor_signed_atom_fields_synced_to_trace_payload_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_constructor_signed_atom_fields_imported": rows[0]["closed"],
        "constructor_side_gates_carried": rows[1]["closed"],
        "trace_sync_router_imported": rows[2]["closed"],
        "closed_unsigned_labels_carried": rows[3]["closed"],
        "same_trace_key_and_named_return_matrix_synced": rows[4]["closed"],
        "constructor_source_atoms_carried_forward": rows[5]["closed"],
        "constructor_side_gates_not_paid_by_trace_sync": rows[6]["closed"],
        "trace_self_proof_cycle_cut_synced": rows[7]["closed"],
        "latest_constructor_basis_replaces_signed_atom_fields_with_new_payload_or_exits": rows[8][
            "closed"
        ],
        "new_primitive_payload_or_trace_artifact_present": False,
        "edge_local_signed_atom_fields_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exactuv_local_multiplicity_o1_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_ATOM_FIELDS,
        "closed_routing_subledger": TRACE_SYNC,
        "next_primary_attack_target": NEW_PAYLOAD,
        "parallel_attack_targets": trace_sync.get(
            "parallel_attack_targets",
            [TERMINAL_DESCENT, PDEC_SCOPE, POINTWISE_TABLE, EXACTUV_PAIR],
        ),
        "paired_constructor_required_targets": [
            atoms,
            ROW_MASS,
            NONZERO_SURVIVAL,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "parallel_constructor_side_gates": f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "imported_largest_slot_sample": largest_slot_sample(trace_sync),
        "imported_return_matrix": trace_sync.get("return_matrix", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 最新 `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` "
            "接入 signed atom trace-sync。LPF/Phi/Ferrers 的无符号 label 只给出输入域；"
            "signed value、local factor、orientation、alpha/delta side、ExactUV fixed pair 与 source row "
            "必须同属一个 pre-Cauchy trace key。匿名失败已被命名 return 矩阵吸收；"
            "当前最新生产性硬点收窄为新 primitive atomic signed payload/trace 工件，或 terminal descent、"
            "same-set PDEC、逐点 signed table 旁路；constructor source 三原子、signed survival、"
            "row-mass/no-heavy-row、complete/fixed key、ExactUV、模型、Rate 与 DStructure 仍需携带。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor signed atom trace-sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_constructor_signed_atom_fields_imported={fmt_bool(cert['latest_constructor_signed_atom_fields_imported'])}",
        f"constructor_side_gates_carried={fmt_bool(cert['constructor_side_gates_carried'])}",
        f"trace_sync_router_imported={fmt_bool(cert['trace_sync_router_imported'])}",
        f"closed_unsigned_labels_carried={fmt_bool(cert['closed_unsigned_labels_carried'])}",
        f"same_trace_key_and_named_return_matrix_synced={fmt_bool(cert['same_trace_key_and_named_return_matrix_synced'])}",
        f"constructor_source_atoms_carried_forward={fmt_bool(cert['constructor_source_atoms_carried_forward'])}",
        f"constructor_side_gates_not_paid_by_trace_sync={fmt_bool(cert['constructor_side_gates_not_paid_by_trace_sync'])}",
        f"trace_self_proof_cycle_cut_synced={fmt_bool(cert['trace_self_proof_cycle_cut_synced'])}",
        f"latest_constructor_basis_replaces_signed_atom_fields_with_new_payload_or_exits={fmt_bool(cert['latest_constructor_basis_replaces_signed_atom_fields_with_new_payload_or_exits'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(cert['new_primitive_payload_or_trace_artifact_present'])}",
        f"edge_local_signed_atom_fields_proved={fmt_bool(cert['edge_local_signed_atom_fields_proved'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(cert['nonzero_signed_row_survival_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(cert['same_formal_unit_row_mass_normalization_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
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
    sample = cert.get("imported_largest_slot_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 3. 导入 slot 样本",
                "",
                "| N | canonical edges | unsigned labels | open fields/edge | open slots | trace packets |",
                "| --- | ---: | ---: | ---: | ---: | ---: |",
                (
                    f"| {sample['N']} | {sample['canonical_edges']} | "
                    f"{sample['closed_unsigned_labels']} | {sample['open_signed_fields_per_edge']} | "
                    f"{sample['open_signed_field_slots']} | {sample['same_trace_packets_required']} |"
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
            "并行出口：",
            "",
            "```text",
            "\n".join(cert["parallel_attack_targets"]),
            "```",
            "",
            "constructor 携带义务：",
            "",
            "```text",
            "\n".join(cert["paired_constructor_required_targets"]),
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
