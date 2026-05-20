#!/usr/bin/env python3
"""生成 Phi-LPF edge-local signed atom trace-sync 前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_edge_local_signed_atom_trace_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json

输出：
  data/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FIELD_CUT_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json"
ORIENTATION_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
ATOMIC_PAYLOAD_CERT = DOCS / "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"
BRANCH_TRACE_CYCLE_CERT = DOCS / "prime-matrix-strict-branch-trace-signed-payload-cycle-router.json"
SIGNED_LANE_CYCLE_CERT = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
GLOBAL_AFTER_TRACE_CERT = DOCS / "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"

SIGNED_ATOM_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
TRACE_SYNC = "PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
ATOMIC_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
        FIELD_CUT_CERT,
        ORIENTATION_CERT,
        BUILTIN_CERT,
        ATOMIC_PAYLOAD_CERT,
        BRANCH_TRACE_CYCLE_CERT,
        SIGNED_LANE_CYCLE_CERT,
        GLOBAL_AFTER_TRACE_CERT,
        EXACTUV_CERT,
        POINTWISE_FRONTIER_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def return_matrix() -> list[dict[str, str]]:
    """列出 edge-local signed 字段的同 trace key 与命名回流要求。"""
    return [
        {
            "field": "same_trace_key",
            "same_key_requirement": "edge label、source row、signed value、local factor、orientation、ExactUV 必须属于同一 pre-Cauchy trace key。",
            "named_return": "SameTraceKeySplitPDEC",
            "productive_input": NEW_PAYLOAD,
        },
        {
            "field": "signed_seed_value",
            "same_key_requirement": "signed seed value 必须由同一 trace 的 payload 字段正向输出。",
            "named_return": "MissingSignedAtomValueReturn OR SignedValueConflictPDEC",
            "productive_input": ATOMIC_PAYLOAD,
        },
        {
            "field": "local_factor_multiplier",
            "same_key_requirement": "local factor 乘积必须与 signed value 和 truncation state 同源。",
            "named_return": "ZeroLocalFactorNamedReturn OR LocalFactorTraceMismatchPDEC",
            "productive_input": ATOMIC_PAYLOAD,
        },
        {
            "field": "orientation_parity",
            "same_key_requirement": "orientation parity 与 branch side 必须从同一 ordered branch operations 读取。",
            "named_return": "OrientationBranchSideMismatchReturn",
            "productive_input": BRANCH_TRACE,
        },
        {
            "field": "alpha_delta_side",
            "same_key_requirement": "alpha/delta payload 必须与 signed coefficient 的 formal unit 相同。",
            "named_return": "AlphaDeltaSideMismatchReturn",
            "productive_input": ATOMIC_PAYLOAD,
        },
        {
            "field": "exactuv_fixed_pair",
            "same_key_requirement": "exact `(u,v)`、branch key 与 return tag 必须在 Cauchy/Phi/payment 前同步输出。",
            "named_return": "ExactUVMissingOrOverBudgetReturn",
            "productive_input": EXACTUV_RETURN,
        },
        {
            "field": "pre_cauchy_source_row",
            "same_key_requirement": "source row 必须先于 pushforward 登记；不能从下游 payment 或 fiber 反推。",
            "named_return": "PreCauchySourceRowAbsentReturn",
            "productive_input": COMMON_PACKET,
        },
    ]


def sample_slot_counts(field_cut: dict[str, Any]) -> list[dict[str, Any]]:
    """从上一层样本读出 signed field slot 规模。"""
    result = []
    for item in field_cut.get("sample_edge_local_field_audit", []):
        edges = int(item["canonical_edges"])
        open_fields = int(item["open_signed_field_count_per_edge"])
        result.append(
            {
                "N": item["N"],
                "canonical_edges": edges,
                "closed_unsigned_labels": int(item["unique_edge_labels"]),
                "open_signed_fields_per_edge": open_fields,
                "open_signed_field_slots": edges * open_fields,
                "same_trace_packets_required": edges,
                "field_slot_matrix_is_schema_only": True,
            }
        )
    return result


def build_rows(
    field_cut: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    atomic_payload: dict[str, Any],
    branch_cycle: dict[str, Any],
    signed_cycle: dict[str, Any],
    global_after_trace: dict[str, Any],
    exactuv: dict[str, Any],
    pointwise: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 trace-sync 前沿判定表。"""
    return [
        row(
            "SignedAtomFieldsTargetImported",
            field_cut.get("next_primary_attack_target") == SIGNED_ATOM_FIELDS,
            False,
            "上一层已把 edge-local 剩余压到 signed atom fields 或 named return tag。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "ClosedUnsignedEdgeLabelsImported",
            field_cut.get("edge_local_closed_unsigned_label_ledger_proved") is True,
            True,
            "LPF/Ferrers edge labels 已闭合，可作为 trace-sync 输入域。",
            field_cut.get("closed_unsigned_subledger", "closed unsigned edge labels"),
        ),
        row(
            "SameTraceKeyRequirementClosed",
            True,
            True,
            "若 signed 字段属于不同 trace/source key，则不是 edge-local formula，而是 named split/PDEC return。",
            TRACE_SYNC,
        ),
        row(
            "NamedReturnMatrixClosed",
            True,
            True,
            "每个 signed 字段的缺失、零因子、冲突、超预算或后验读取都有命名 return，不再保留匿名缺口。",
            TRACE_SYNC,
        ),
        row(
            "BranchTraceWouldSupplyOrientationConditionally",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 若作为新输入存在，可同时提供 orientation/local factor/ExactUV return 字段。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceReducedToSignedPayload",
            atomic_payload.get("next_direct_attack_target") == ATOMIC_PAYLOAD
            and atomic_payload.get("atomic_signed_payload_constructor_proved") is False,
            False,
            "atomic trace 的可见坐标不产生 signed payload；生产性字段压到 payload constructor。",
            ATOMIC_PAYLOAD,
        ),
        row(
            "SignedLaneSelfProofEliminated",
            signed_cycle.get("signed_lane_cycle_closed") is True
            and signed_cycle.get("signed_lane_self_proof_eliminated") is True,
            True,
            "common packet -> builtin pairing -> branch trace -> payload -> origin identity 已成闭环，不能自证。",
            NEW_PAYLOAD,
        ),
        row(
            "BranchTraceSelfProofEliminatedGlobally",
            global_after_trace.get("branch_trace_self_proof_eliminated") is True
            and branch_cycle.get("branch_trace_route_counts_as_independent_proof") is False,
            True,
            "全局 strict 前沿已排除 branch trace 作为当前内部语料的独立证明路线。",
            f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "BuiltinPairingStillConditional",
            builtin.get("branch_trace_conditionally_suffices") is True
            and builtin.get("builtin_signed_coefficient_pairing_proved") is False,
            False,
            "built-in signed pairing 仍只被条件性压到 exact atomic branch trace。",
            ATOMIC_TRACE,
        ),
        row(
            "ExactUVStillIndependent",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "trace-sync 可登记 edge UV 字段，但 source entropy/fiber 有界性仍是独立门。",
            EXACTUV_PAIR,
        ),
        row(
            "PointwiseTableStillAlternativeButOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 可作为替代新工件，但当前未提交。",
            POINTWISE_TABLE,
        ),
        row(
            "SignedAtomTraceSyncCurrentCorpusProved",
            False,
            False,
            "当前语料没有新 primitive payload/trace 工件来填充 same-trace signed atom 字段。",
            NEW_PAYLOAD,
        ),
        row(
            "EdgeLocalSignedAtomFieldsCurrentCorpusProved",
            False,
            False,
            "命名 return 矩阵只排除匿名缺口，不给 signed value/local factor 公式。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明三命题无条件闭合；仍需新 payload/trace、terminal descent 或 PDEC scope，并合取 ExactUV 与晋级门。",
            f"({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {EXACTUV_PAIR}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 edge-local signed atom trace-sync 前沿证书。"""
    field_cut = load_json(FIELD_CUT_CERT)
    orientation = load_json(ORIENTATION_CERT)
    builtin = load_json(BUILTIN_CERT)
    atomic_payload = load_json(ATOMIC_PAYLOAD_CERT)
    branch_cycle = load_json(BRANCH_TRACE_CYCLE_CERT)
    signed_cycle = load_json(SIGNED_LANE_CYCLE_CERT)
    global_after_trace = load_json(GLOBAL_AFTER_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    rows = build_rows(
        field_cut,
        orientation,
        builtin,
        atomic_payload,
        branch_cycle,
        signed_cycle,
        global_after_trace,
        exactuv,
        pointwise,
    )
    retained_basis = (
        f"(({NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) "
        f"AND {EXACTUV_PAIR} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE})"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_edge_local_signed_atom_trace_sync_router",
        "status": "phi_lpf_edge_local_signed_atom_fields_reduced_to_new_payload_or_named_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "signed_atom_fields_target_imported": field_cut.get("next_primary_attack_target")
        == SIGNED_ATOM_FIELDS,
        "closed_unsigned_edge_labels_imported": field_cut.get(
            "edge_local_closed_unsigned_label_ledger_proved"
        )
        is True,
        "same_trace_key_requirement_closed": True,
        "named_return_matrix_closed": True,
        "branch_trace_would_supply_orientation_conditionally": orientation.get(
            "complete_branch_trace_would_imply_orientation_law"
        )
        is True,
        "atomic_trace_reduced_to_signed_payload": atomic_payload.get("next_direct_attack_target")
        == ATOMIC_PAYLOAD,
        "signed_lane_cycle_imported": signed_cycle.get("signed_lane_cycle_closed") is True,
        "signed_lane_self_proof_eliminated": signed_cycle.get("signed_lane_self_proof_eliminated")
        is True,
        "branch_trace_self_proof_eliminated": global_after_trace.get(
            "branch_trace_self_proof_eliminated"
        )
        is True,
        "new_primitive_payload_or_trace_artifact_present": False,
        "edge_local_signed_atom_fields_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_ATOM_FIELDS,
        "closed_routing_subledger": TRACE_SYNC,
        "next_primary_attack_target": NEW_PAYLOAD,
        "parallel_attack_targets": [
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
        ],
        "retained_basis_after_router": retained_basis,
        "return_matrix": return_matrix(),
        "sample_slot_counts": sample_slot_counts(field_cut),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "edge-local signed atom fields 不能由 LPF/Phi/Ferrers label 推出。它们必须在同一 "
            "pre-Cauchy trace key 上一次性给出 signed value、local factor、orientation/branch side、"
            "alpha/delta payload、ExactUV fixed pair 与 source row；任何缺失、冲突、零因子、超预算或后验读取都进入命名 return。"
            "现有 branch-trace/atomic-trace 线已闭成 signed-lane 自证环，因此当前非循环剩余压到新 primitive payload/trace 工件，"
            "或 terminal descent/PDEC scope/逐点 signed table，并仍需 ExactUV、模型、Rate 与 DStructure。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF edge-local signed atom trace-sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"signed_atom_fields_target_imported={fmt_bool(cert['signed_atom_fields_target_imported'])}",
        f"closed_unsigned_edge_labels_imported={fmt_bool(cert['closed_unsigned_edge_labels_imported'])}",
        f"same_trace_key_requirement_closed={fmt_bool(cert['same_trace_key_requirement_closed'])}",
        f"named_return_matrix_closed={fmt_bool(cert['named_return_matrix_closed'])}",
        f"atomic_trace_reduced_to_signed_payload={fmt_bool(cert['atomic_trace_reduced_to_signed_payload'])}",
        f"signed_lane_cycle_imported={fmt_bool(cert['signed_lane_cycle_imported'])}",
        f"signed_lane_self_proof_eliminated={fmt_bool(cert['signed_lane_self_proof_eliminated'])}",
        f"branch_trace_self_proof_eliminated={fmt_bool(cert['branch_trace_self_proof_eliminated'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(cert['new_primitive_payload_or_trace_artifact_present'])}",
        f"edge_local_signed_atom_fields_proved={fmt_bool(cert['edge_local_signed_atom_fields_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 同 trace key / return 矩阵",
            "",
            "| field | same-key requirement | named return | productive input |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in cert["return_matrix"]:
        lines.append(
            f"| `{item['field']}` | {cell(item['same_key_requirement'])} | "
            f"{cell(item['named_return'])} | {cell(item['productive_input'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. slot 规模审计",
            "",
            "| N | canonical edges | unsigned labels | open fields/edge | open slots | trace packets |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in cert["sample_slot_counts"]:
        lines.append(
            f"| {item['N']} | {item['canonical_edges']} | {item['closed_unsigned_labels']} | "
            f"{item['open_signed_fields_per_edge']} | {item['open_signed_field_slots']} | "
            f"{item['same_trace_packets_required']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["retained_basis_after_router"],
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
    """写出 edge-local signed atom trace-sync 前沿证书。"""
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
