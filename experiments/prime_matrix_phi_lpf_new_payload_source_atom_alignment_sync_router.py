#!/usr/bin/env python3
"""生成 Phi-LPF new-payload 到 source-atom alignment 的桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_new_payload_source_atom_alignment_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.json

输出：
  data/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TRACE_SYNC_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json"
STRICT_ALIGNMENT_CERT = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
SIGNED_LANE_CYCLE_CERT = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
SOURCE_ATOM_CERT = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

SIGNED_ATOM_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK_ATOM = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能被当作证明。"""
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


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        TRACE_SYNC_CERT,
        STRICT_ALIGNMENT_CERT,
        SIGNED_LANE_CYCLE_CERT,
        SOURCE_ATOM_CERT,
        POINTWISE_FRONTIER_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def bridge_contract() -> list[dict[str, str]]:
    """列出 Phi-LPF signed atom 若走 new-payload 出口必须携带的字段。"""
    return [
        {
            "field": "same_trace_key_lock",
            "requirement": "继承 edge-local trace-sync 的同一 pre-Cauchy trace key；不能从多个下游表拼接 signed 字段。",
            "remaining": NEW_PAYLOAD,
        },
        {
            "field": "pre_cauchy_actual_source_object",
            "requirement": "在 Cauchy/Phi/payment 前声明同一 actual noncanonical primitive source object。",
            "remaining": SOURCE_RANK_ATOM,
        },
        {
            "field": "source_domain_absolute_entropy",
            "requirement": "排除 actual source 质量坍缩到少数 primitive rows/key/fiber。",
            "remaining": DOMAIN_ENTROPY,
        },
        {
            "field": "complete_key_partition",
            "requirement": "发射前给出 complete primitive emitter key partition，禁止后验补标签。",
            "remaining": COMPLETE_KEY,
        },
        {
            "field": "fixed_key_exact_uv_local_multiplicity",
            "requirement": "固定 complete key 与 exact `(u,v)` 后控制 actual primitive source 原像局部重数。",
            "remaining": FIXED_KEY_MULT,
        },
        {
            "field": "signed_payload_fields",
            "requirement": "正向输出 signed value、local factor、orientation/branch side、alpha/delta side 与 return tag。",
            "remaining": NEW_PAYLOAD,
        },
        {
            "field": "no_cycle_or_named_exit",
            "requirement": "若使用 signed-lane 环、terminal 回流或 same-set PDEC，则必须作为命名出口，不得当作独立证明。",
            "remaining": f"{TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        },
    ]


def build_rows(
    trace_sync: dict[str, Any],
    strict_alignment: dict[str, Any],
    signed_cycle: dict[str, Any],
    source_atom: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 Phi-LPF/strict alignment 桥接判定表。"""
    strict_agg = strict_alignment.get("aggregate", {})
    source_rank_imported = (
        strict_agg.get("source_rank_atom_imported") is True
        or source_atom.get("terminal_gap_after_router") == SOURCE_RANK_ATOM
    )
    return [
        row(
            "PhiLPFTraceSyncImported",
            trace_sync.get("next_primary_attack_target") == NEW_PAYLOAD
            and trace_sync.get("same_trace_key_requirement_closed") is True,
            False,
            "上一层已把 edge-local signed atom fields 压到同 trace key 的 new primitive payload/trace 或命名出口。",
            NEW_PAYLOAD,
        ),
        row(
            "UnsignedLPFDataCannotPaySignedPayload",
            trace_sync.get("closed_unsigned_edge_labels_imported") is True,
            True,
            "LPF/Phi/Ferrers 只支付 owner/product/support/capacity 等无符号字段，不产生 signed coefficient 或 local factor。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "SignedLaneCycleImported",
            signed_cycle.get("signed_lane_cycle_closed") is True
            and signed_cycle.get("signed_lane_self_proof_eliminated") is True,
            True,
            "trace、payload、origin 与 common packet 的环已被排除为自证路线。",
            NEW_PAYLOAD,
        ),
        row(
            "StrictNewPayloadAlignmentImported",
            strict_alignment.get("status")
            == "strict_new_primitive_payload_reduced_to_actual_source_rank_atom_open",
            False,
            "已有 strict 证书说明 new primitive 工件若要破环，必须携带 actual source-rank/no-collapse 包。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "SourceRankAtomPackageImported",
            source_rank_imported,
            False,
            "source-rank/no-collapse 包的实际内容是 source entropy、complete key 与 fixed-key exact-UV local multiplicity。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "PhiLPFNewPayloadIndependentTerminalRejected",
            strict_agg.get("new_primitive_artifact_independent_terminal_present") is False,
            True,
            "Phi-LPF edge-local 不能把 new-payload 名称当作独立终点；缺三原子时只能是改名或命名出口。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "PointwiseTableStillAlternative",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 仍可作为并行替代，但当前没有提交。",
            POINTWISE_TABLE,
        ),
        row(
            "ExactUVStillIndependent",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "source entropy 与 fixed exact-pair fiber 控制不能由 LPF 支撑或 trace-sync 自动推出。",
            EXACTUV_PAIR,
        ),
        row(
            "SourceEntropyFirstAtomStillOpen",
            strict_agg.get("actual_source_domain_entropy_proved") is False,
            False,
            "三原子包的第一直接硬点仍是 actual pre-Cauchy source-domain absolute entropy。",
            DOMAIN_ENTROPY,
        ),
        row(
            "CompleteKeyStillOpen",
            strict_agg.get("complete_primitive_emitter_key_partition_proved") is False,
            False,
            "complete key partition 仍未证明，不能由 LPF/Phi label 后验补齐。",
            COMPLETE_KEY,
        ),
        row(
            "FixedKeyMultiplicityStillOpen",
            strict_agg.get("fixed_key_exact_uv_local_multiplicity_proved") is False,
            False,
            "fixed-key exact-UV local multiplicity 仍未证明，不能由单条 edge label 排除 fiber 坍缩。",
            FIXED_KEY_MULT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 Phi-LPF new-payload 出口接到 source-rank/no-collapse 三原子；不证明三命题无条件闭合。",
            (
                f"({DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
                f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}"
            ),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装桥接证书。"""
    trace_sync = load_json(TRACE_SYNC_CERT)
    strict_alignment = load_json(STRICT_ALIGNMENT_CERT)
    signed_cycle = load_json(SIGNED_LANE_CYCLE_CERT)
    source_atom = load_json(SOURCE_ATOM_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(trace_sync, strict_alignment, signed_cycle, source_atom, pointwise, exactuv)
    latest_basis = (
        f"(({DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) "
        f"AND {EXACTUV_PAIR} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_new_payload_source_atom_alignment_sync_router",
        "status": "phi_lpf_new_payload_exit_reduced_to_source_atom_package_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "phi_lpf_trace_sync_imported": any(
            item["gate"] == "PhiLPFTraceSyncImported" and item["closed"] for item in rows
        ),
        "unsigned_lpf_data_cannot_pay_signed_payload": any(
            item["gate"] == "UnsignedLPFDataCannotPaySignedPayload" and item["closed"]
            for item in rows
        ),
        "strict_new_payload_alignment_imported": any(
            item["gate"] == "StrictNewPayloadAlignmentImported" and item["closed"]
            for item in rows
        ),
        "phi_lpf_new_payload_independent_terminal_present": False,
        "phi_lpf_new_payload_reduced_to_source_rank_atom": any(
            item["gate"] == "SourceRankAtomPackageImported" and item["closed"]
            for item in rows
        ),
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
            MODEL_LEDGER,
            RATE_LEDGER,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": latest_basis,
        "bridge_contract": bridge_contract(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 Phi-LPF edge-local trace-sync 的 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` "
            "接到已有 strict source-atom alignment。LPF/Phi/Ferrers 已闭合的是无符号支撑、容量、"
            "tuple/fiber 标签；它们不能自动生成 signed value、local factor、orientation 或 alpha/delta payload。"
            "因此 new-payload 出口不是独立终点：若它不是 signed-lane 环内改名，就必须提交 actual pre-Cauchy "
            "source-rank/no-collapse 三原子；否则转入 terminal descent、PDEC scope、逐点 signed table 或外部晋级门。"
            "当前第一直接硬点为 source-domain absolute entropy，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF new-payload source-atom alignment sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_lpf_trace_sync_imported={fmt_bool(cert['phi_lpf_trace_sync_imported'])}",
        f"unsigned_lpf_data_cannot_pay_signed_payload={fmt_bool(cert['unsigned_lpf_data_cannot_pay_signed_payload'])}",
        f"strict_new_payload_alignment_imported={fmt_bool(cert['strict_new_payload_alignment_imported'])}",
        f"phi_lpf_new_payload_independent_terminal_present={fmt_bool(cert['phi_lpf_new_payload_independent_terminal_present'])}",
        f"phi_lpf_new_payload_reduced_to_source_rank_atom={fmt_bool(cert['phi_lpf_new_payload_reduced_to_source_rank_atom'])}",
        f"actual_source_domain_entropy_proved={fmt_bool(cert['actual_source_domain_entropy_proved'])}",
        f"complete_primitive_emitter_key_partition_proved={fmt_bool(cert['complete_primitive_emitter_key_partition_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_proved={fmt_bool(cert['fixed_key_exact_uv_local_multiplicity_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 桥接字段合同",
        "",
        "| field | requirement | remaining |",
        "| --- | --- | --- |",
    ]
    for item in cert["bridge_contract"]:
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
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
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
            "## 4. 依赖哈希",
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
    """写出桥接证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
