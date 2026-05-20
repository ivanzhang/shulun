#!/usr/bin/env python3
"""生成 Phi-LPF 最新 new-payload 到 source-atom alignment 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_payload_source_atom_alignment_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_TRACE_SYNC_CERT = DOCS / "prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json"
STRICT_ALIGNMENT_CERT = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
SIGNED_LANE_CYCLE_CERT = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
SOURCE_ATOM_CERT = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK_ATOM = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_ATOM_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
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
        LATEST_TRACE_SYNC_CERT,
        STRICT_ALIGNMENT_CERT,
        SIGNED_LANE_CYCLE_CERT,
        SOURCE_ATOM_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def source_atom_contract() -> list[dict[str, str]]:
    """列出 latest new-payload 若要破环必须携带的 source 原子字段。"""
    return [
        {
            "field": "same_trace_key_lock",
            "requirement": "继承 latest signed atom trace-sync 的同一 pre-Cauchy trace key。",
            "remaining": NEW_PAYLOAD,
        },
        {
            "field": "actual_source_object",
            "requirement": "在 Cauchy/Phi/payment 前声明同一 actual noncanonical primitive source object。",
            "remaining": SOURCE_RANK_ATOM,
        },
        {
            "field": "source_domain_absolute_entropy",
            "requirement": "排除 actual source 质量坍缩到少数 primitive rows、key 或 fiber。",
            "remaining": DOMAIN_ENTROPY,
        },
        {
            "field": "complete_key_partition",
            "requirement": "发射前给出 complete primitive emitter key partition，禁止后验补标签。",
            "remaining": COMPLETE_KEY,
        },
        {
            "field": "fixed_key_exact_uv_local_multiplicity",
            "requirement": "固定 complete key 与 exact `(u,v)` 后控制 primitive source 原像局部重数。",
            "remaining": FIXED_KEY_MULT,
        },
        {
            "field": "named_nonproductive_exits",
            "requirement": "若只调用 signed-lane 环、terminal 回流、same-set PDEC 或逐点表，则必须作为命名出口。",
            "remaining": f"{TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}",
        },
    ]


def largest_slot_sample(latest_trace: dict[str, Any]) -> dict[str, Any]:
    """抽取 latest trace-sync 的最大 slot 样本。"""
    return latest_trace.get("imported_largest_slot_sample", {})


def build_rows(
    latest_trace: dict[str, Any],
    strict_alignment: dict[str, Any],
    signed_cycle: dict[str, Any],
    source_atom: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest new-payload/source-atom 同步判定表。"""
    strict_agg = strict_alignment.get("aggregate", {})
    source_rank_imported = (
        strict_agg.get("source_rank_atom_imported") is True
        or source_atom.get("terminal_gap_after_router") == SOURCE_RANK_ATOM
    )
    return [
        row(
            "LatestNewPayloadImported",
            latest_trace.get("next_primary_attack_target") == NEW_PAYLOAD,
            False,
            "上一层 latest trace-sync 已把生产性硬点定位到 new primitive payload/trace。",
            NEW_PAYLOAD,
        ),
        row(
            "LatestUnsignedLabelsCannotPayPayload",
            latest_trace.get("closed_unsigned_labels_carried") is True,
            True,
            "LPF/Phi/Ferrers 的 latest 无符号 labels 只给输入域，不产生 signed coefficient、local factor 或 orientation。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "SignedLaneCycleCutCarried",
            signed_cycle.get("signed_lane_cycle_closed") is True
            and signed_cycle.get("signed_lane_self_proof_eliminated") is True
            and latest_trace.get("trace_self_proof_cycle_cut_synced") is True,
            True,
            "latest trace-sync 继承 signed-lane 自证环删除；new payload 不能只是环内改名。",
            NEW_PAYLOAD,
        ),
        row(
            "StrictNewPayloadAlignmentImported",
            strict_alignment.get("status")
            == "strict_new_primitive_payload_reduced_to_actual_source_rank_atom_open",
            False,
            "strict 证书已说明 new primitive 工件若要破环，必须携带 actual source-rank/no-collapse 包。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "LatestNewPayloadReducedToSourceRankAtom",
            source_rank_imported
            and strict_agg.get("new_primitive_artifact_reduced_to_source_rank_atom") is True,
            False,
            "source-rank/no-collapse 包展开为 source entropy、complete key 与 fixed-key ExactUV local multiplicity。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "IndependentNewPayloadTerminalRejected",
            strict_agg.get("new_primitive_artifact_independent_terminal_present") is False
            and latest_trace.get("new_primitive_payload_or_trace_artifact_present") is False,
            True,
            "当前语料没有独立 new primitive 工件；缺三原子时只能是改名或命名出口。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "SourceEntropyStillFirstAtom",
            strict_agg.get("actual_source_domain_entropy_proved") is False,
            False,
            "三原子包的第一直接硬点仍是 actual pre-Cauchy source-domain absolute entropy。",
            DOMAIN_ENTROPY,
        ),
        row(
            "CompleteKeyStillOpen",
            strict_agg.get("complete_primitive_emitter_key_partition_proved") is False,
            False,
            "complete key partition 仍未证明，不能由 Phi-LPF label 后验补齐。",
            COMPLETE_KEY,
        ),
        row(
            "FixedKeyMultiplicityStillOpen",
            strict_agg.get("fixed_key_exact_uv_local_multiplicity_proved") is False,
            False,
            "fixed-key ExactUV local multiplicity 仍未证明，不能由单条 edge label 排除 fiber 坍缩。",
            FIXED_KEY_MULT,
        ),
        row(
            "PointwiseTableStillAlternative",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 仍是并行替代，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ExactUVStillIndependent",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "source entropy 与 fixed exact-pair fiber 控制不能由 latest trace-sync 自动推出。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 latest new-payload 到 source-rank/no-collapse 三原子；未证明三命题无条件闭合。",
            (
                f"({DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
                f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest new-payload/source-atom alignment 同步证书。"""
    latest_trace = load_json(LATEST_TRACE_SYNC_CERT)
    strict_alignment = load_json(STRICT_ALIGNMENT_CERT)
    signed_cycle = load_json(SIGNED_LANE_CYCLE_CERT)
    source_atom = load_json(SOURCE_ATOM_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(latest_trace, strict_alignment, signed_cycle, source_atom, pointwise, exactuv)
    latest_basis = (
        f"(({DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) "
        f"AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_payload_source_atom_alignment_sync_router",
        "status": "phi_lpf_latest_new_payload_reduced_to_source_atom_package_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_new_payload_imported": rows[0]["closed"],
        "latest_unsigned_labels_cannot_pay_payload": rows[1]["closed"],
        "signed_lane_cycle_cut_carried": rows[2]["closed"],
        "strict_new_payload_alignment_imported": rows[3]["closed"],
        "latest_new_payload_reduced_to_source_rank_atom": rows[4]["closed"],
        "independent_new_payload_terminal_present": False,
        "actual_source_domain_entropy_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": NEW_PAYLOAD,
        "absorbed_to": SOURCE_RANK_ATOM,
        "next_primary_attack_target": DOMAIN_ENTROPY,
        "parallel_attack_targets": [
            COMPLETE_KEY,
            FIXED_KEY_MULT,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": latest_basis,
        "source_atom_contract": source_atom_contract(),
        "imported_largest_slot_sample": largest_slot_sample(latest_trace),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` "
            "接到 strict source-atom alignment。最新 Phi-LPF/trace-sync 已说明无符号 label "
            "只给输入域，signed payload 不能由 LPF/Phi/Ferrers 自动产生；signed-lane 自证环也已删除。"
            "因此 new-payload 若要成为真正新工件，必须携带 actual pre-Cauchy source-rank/no-collapse "
            "三原子：source-domain entropy、complete key partition、fixed-key ExactUV local multiplicity。"
            "当前第一直接硬点为 source-domain absolute entropy，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest new-payload source-atom alignment sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_new_payload_imported={fmt_bool(cert['latest_new_payload_imported'])}",
        f"latest_unsigned_labels_cannot_pay_payload={fmt_bool(cert['latest_unsigned_labels_cannot_pay_payload'])}",
        f"signed_lane_cycle_cut_carried={fmt_bool(cert['signed_lane_cycle_cut_carried'])}",
        f"strict_new_payload_alignment_imported={fmt_bool(cert['strict_new_payload_alignment_imported'])}",
        f"latest_new_payload_reduced_to_source_rank_atom={fmt_bool(cert['latest_new_payload_reduced_to_source_rank_atom'])}",
        f"independent_new_payload_terminal_present={fmt_bool(cert['independent_new_payload_terminal_present'])}",
        f"actual_source_domain_entropy_proved={fmt_bool(cert['actual_source_domain_entropy_proved'])}",
        f"complete_primitive_emitter_key_partition_proved={fmt_bool(cert['complete_primitive_emitter_key_partition_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. source-atom 合同",
        "",
        "| field | requirement | remaining |",
        "| --- | --- | --- |",
    ]
    for item in cert["source_atom_contract"]:
        lines.append(
            f"| `{cell(item['field'])}` | {cell(item['requirement'])} | {cell(item['remaining'])} |"
        )
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
                "## 3. 导入 latest slot 样本",
                "",
                "| N | canonical edges | open slots | trace packets |",
                "| --- | ---: | ---: | ---: |",
                (
                    f"| {sample['N']} | {sample['canonical_edges']} | "
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
        lines.append(f"| `{cell(path)}` | `{digest}` |")
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
