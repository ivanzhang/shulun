#!/usr/bin/env python3
"""生成 Phi-LPF 最新 signed atom trace-sync 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_signed_atom_trace_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-signed-atom-trace-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_FIELD_CUT_CERT = DOCS / "prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-router.json"
TRACE_SYNC_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

SIGNED_ATOM_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
TRACE_SYNC = "PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
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


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_FIELD_CUT_CERT,
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
    """生成最新 signed atom trace-sync 同步判定表。"""
    return [
        row(
            "LatestSignedAtomFieldsImported",
            latest.get("next_primary_attack_target") == SIGNED_ATOM_FIELDS,
            False,
            "上一层最新 field-cut 已把直接硬点定位到 signed atom fields 或 named return tag。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "TraceSyncRouterImported",
            trace_sync.get("target_input_before_router") == SIGNED_ATOM_FIELDS
            and trace_sync.get("same_trace_key_requirement_closed") is True,
            True,
            "既有 signed atom trace-sync 证书可直接作用在最新 signed atom fields 入口。",
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
            "TraceSelfProofCycleCutSynced",
            trace_sync.get("signed_lane_self_proof_eliminated") is True
            and trace_sync.get("branch_trace_self_proof_eliminated") is True,
            True,
            "branch/atomic trace 不能在当前内部语料中自证 signed atom payload。",
            NEW_PAYLOAD,
        ),
        row(
            "LatestBasisReplacesSignedAtomFieldsWithNewPayloadOrExits",
            trace_sync.get("next_primary_attack_target") == NEW_PAYLOAD,
            False,
            "最新 signed atom fields 被收窄为新 primitive payload/trace 或受控旁路出口。",
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
            f"({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {EXACTUV_PAIR}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装最新 signed atom trace-sync 同步证书。"""
    latest = load_json(LATEST_FIELD_CUT_CERT)
    trace_sync = load_json(TRACE_SYNC_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest, trace_sync, pointwise, exactuv)
    latest_basis = (
        trace_sync.get("retained_basis_after_router")
        or f"(({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) "
        f"AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE})"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_signed_atom_trace_sync_router",
        "status": "phi_lpf_latest_signed_atom_fields_synced_to_trace_payload_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_signed_atom_fields_imported": rows[0]["closed"],
        "trace_sync_router_imported": rows[1]["closed"],
        "closed_unsigned_labels_carried": rows[2]["closed"],
        "same_trace_key_and_named_return_matrix_synced": rows[3]["closed"],
        "trace_self_proof_cycle_cut_synced": rows[4]["closed"],
        "latest_basis_replaces_signed_atom_fields_with_new_payload_or_exits": rows[5][
            "closed"
        ],
        "new_primitive_payload_or_trace_artifact_present": False,
        "edge_local_signed_atom_fields_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_ATOM_FIELDS,
        "closed_routing_subledger": TRACE_SYNC,
        "next_primary_attack_target": NEW_PAYLOAD,
        "parallel_attack_targets": trace_sync.get(
            "parallel_attack_targets",
            [TERMINAL_DESCENT, PDEC_SCOPE, POINTWISE_TABLE, EXACTUV_PAIR],
        ),
        "latest_retained_basis_after_router": latest_basis,
        "sync_chain": sync_chain(),
        "imported_largest_slot_sample": largest_slot_sample(trace_sync),
        "imported_return_matrix": trace_sync.get("return_matrix", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` "
            "接入 signed atom trace-sync。LPF/Phi/Ferrers 的无符号 label 只给出输入域；"
            "signed value、local factor、orientation、alpha/delta side、ExactUV fixed pair 与 source row "
            "必须同属一个 pre-Cauchy trace key。匿名失败已被命名 return 矩阵吸收；"
            "当前最新生产性硬点收窄为新 primitive atomic signed payload/trace 工件，或 terminal descent、"
            "same-set PDEC、逐点 signed table 旁路，并仍需 ExactUV、模型、Rate 与 DStructure。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest signed atom trace-sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_signed_atom_fields_imported={fmt_bool(cert['latest_signed_atom_fields_imported'])}",
        f"trace_sync_router_imported={fmt_bool(cert['trace_sync_router_imported'])}",
        f"closed_unsigned_labels_carried={fmt_bool(cert['closed_unsigned_labels_carried'])}",
        f"same_trace_key_and_named_return_matrix_synced={fmt_bool(cert['same_trace_key_and_named_return_matrix_synced'])}",
        f"trace_self_proof_cycle_cut_synced={fmt_bool(cert['trace_self_proof_cycle_cut_synced'])}",
        f"latest_basis_replaces_signed_atom_fields_with_new_payload_or_exits={fmt_bool(cert['latest_basis_replaces_signed_atom_fields_with_new_payload_or_exits'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(cert['new_primitive_payload_or_trace_artifact_present'])}",
        f"edge_local_signed_atom_fields_proved={fmt_bool(cert['edge_local_signed_atom_fields_proved'])}",
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
