#!/usr/bin/env python3
"""生成 latest constructor signed atom trace 的 rebase 同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_constructor_signed_atom_trace_rebase_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_FIELD_CUT_REBASE_CERT = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.json"
)
OLD_CONSTRUCTOR_TRACE_CERT = DOCS / "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.json"
TRACE_SYNC_CERT = DOCS / "prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json"
POINTWISE_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
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


def source_atoms() -> str:
    """返回 constructor rebase 分支携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        CURRENT_FIELD_CUT_REBASE_CERT,
        OLD_CONSTRUCTOR_TRACE_CERT,
        TRACE_SYNC_CERT,
        POINTWISE_CERT,
        EXACTUV_CERT,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def retained_basis() -> str:
    """给出本层同步后的完整保留基。"""
    atoms = source_atoms()
    return (
        f"(({atoms} AND {ROW_MASS} AND {NEW_PAYLOAD}) OR {TERMINAL_DESCENT} "
        f"OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {NONZERO_SURVIVAL} "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {EXACTUV_PAIR} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def largest_slot_sample(trace_sync: dict[str, Any]) -> dict[str, Any]:
    """抽取 trace-sync 证书的最大 slot 样本。"""
    samples = trace_sync.get("sample_slot_counts", [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def build_rows(
    current: dict[str, Any],
    old_constructor_trace: dict[str, Any],
    trace_sync: dict[str, Any],
    pointwise: dict[str, Any],
    exactuv: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 signed atom trace rebase 判定表。"""
    atoms = source_atoms()
    current_signed_atom_active = (
        current.get("next_primary_attack_target") == SIGNED_ATOM_FIELDS
        and current.get("edge_local_field_cut_rebased") is True
    )
    old_trace_reusable = (
        old_constructor_trace.get("target_input_before_router") == SIGNED_ATOM_FIELDS
        and old_constructor_trace.get(
            "latest_constructor_basis_replaces_signed_atom_fields_with_new_payload_or_exits"
        )
        is True
        and old_constructor_trace.get("next_primary_attack_target") == NEW_PAYLOAD
    )
    trace_imported = (
        trace_sync.get("target_input_before_router") == SIGNED_ATOM_FIELDS
        and trace_sync.get("same_trace_key_requirement_closed") is True
    )
    same_trace_return = (
        trace_sync.get("same_trace_key_requirement_closed") is True
        and trace_sync.get("named_return_matrix_closed") is True
    )
    source_carried = (
        current.get("source_atoms_carried_forward") is True
        and atoms in current.get("paired_required_attack_targets", [])
    )
    side_gates_not_paid = (
        current.get("nonzero_signed_row_survival_proved") is False
        and current.get("same_formal_unit_row_mass_normalization_proved") is False
    )
    trace_cycle_cut = (
        trace_sync.get("signed_lane_self_proof_eliminated") is True
        and trace_sync.get("branch_trace_self_proof_eliminated") is True
    )
    signed_atom_trace_rebased = (
        current_signed_atom_active
        and old_trace_reusable
        and trace_imported
        and same_trace_return
        and trace_cycle_cut
    )
    return [
        row(
            "LatestRebasedSignedAtomFieldsImported",
            current_signed_atom_active,
            False,
            "上一层 rebase 已把 constructor 直接硬点定位到 signed atom fields 或 named return tag。",
            SIGNED_ATOM_FIELDS,
        ),
        row(
            "ExistingConstructorSignedAtomTraceReusable",
            old_trace_reusable,
            False,
            "旧 constructor signed atom trace-sync 输入相同，可在新 rebase 前沿复用。",
            NEW_PAYLOAD,
        ),
        row(
            "TraceSyncRouterImported",
            trace_imported,
            True,
            "signed atom trace-sync 要求逐 edge signed fields 落在同一 pre-Cauchy trace key。",
            TRACE_SYNC,
        ),
        row(
            "ClosedUnsignedLabelsCarried",
            current.get("closed_unsigned_edge_fields_exhausted") is True
            and current.get("unsigned_label_does_not_emit_signed_atom") is True
            and trace_sync.get("closed_unsigned_edge_labels_imported") is True,
            True,
            "无符号 edge label 只作为 trace-sync 输入域携带，不产生 signed payload。",
            current.get("closed_unsigned_subledger", "closed unsigned edge label ledger"),
        ),
        row(
            "SameTraceKeyAndNamedReturnMatrixSynced",
            same_trace_return,
            True,
            "缺失、冲突、零因子、超预算或跨 key 读取均进入命名 return。",
            TRACE_SYNC,
        ),
        row(
            "ConstructorSourceAtomsCarriedForward",
            source_carried,
            False,
            "source 三原子仍是 constructor payload 分支的携带义务，本步不证明它们。",
            atoms,
        ),
        row(
            "ConstructorSideGatesNotPaidByTraceSync",
            side_gates_not_paid,
            False,
            "same-trace/return 矩阵不支付 signed survival、row mass、complete key 或 fixed-key multiplicity。",
            f"{NONZERO_SURVIVAL} AND {ROW_MASS} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "TraceSelfProofCycleCutSynced",
            trace_cycle_cut,
            True,
            "branch/atomic trace 不能在当前内部语料中自证 signed atom payload。",
            NEW_PAYLOAD,
        ),
        row(
            "SignedAtomTraceRebased",
            signed_atom_trace_rebased,
            False,
            "最新 signed atom fields 已同步为新 primitive payload/trace 或受控旁路出口。",
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
            "本步只做 rebase 同步；未证明三命题无条件闭合。",
            retained_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    current = load_json(CURRENT_FIELD_CUT_REBASE_CERT)
    old_constructor_trace = load_json(OLD_CONSTRUCTOR_TRACE_CERT)
    trace_sync = load_json(TRACE_SYNC_CERT)
    pointwise = load_json(POINTWISE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    rows = build_rows(current, old_constructor_trace, trace_sync, pointwise, exactuv)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_constructor_signed_atom_trace_rebase_sync_router",
        "status": "phi_lpf_latest_constructor_signed_atom_trace_rebased_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "missing_sources": missing_sources(),
        "latest_rebased_signed_atom_fields_imported": rows[0]["closed"],
        "existing_constructor_signed_atom_trace_reusable": rows[1]["closed"],
        "trace_sync_router_imported": rows[2]["closed"],
        "closed_unsigned_labels_carried": rows[3]["closed"],
        "same_trace_key_and_named_return_matrix_synced": rows[4]["closed"],
        "constructor_source_atoms_carried_forward": rows[5]["closed"],
        "constructor_side_gates_not_paid_by_trace_sync": rows[6]["closed"],
        "trace_self_proof_cycle_cut_synced": rows[7]["closed"],
        "signed_atom_trace_rebased": rows[8]["closed"],
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
        "parallel_attack_targets": [
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
        ],
        "paired_constructor_required_targets": [
            source_atoms(),
            ROW_MASS,
            NONZERO_SURVIVAL,
            COMPLETE_KEY,
            FIXED_KEY,
        ],
        "parallel_constructor_side_gates": f"{NONZERO_SURVIVAL} AND {ROW_MASS}",
        "latest_retained_basis_after_router": retained_basis(),
        "imported_largest_slot_sample": largest_slot_sample(trace_sync),
        "imported_return_matrix": trace_sync.get("return_matrix", []),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 rebase 后的 constructor `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` "
            "接入 signed atom trace-sync。无符号 label 只给输入域；signed value、local factor、"
            "orientation、alpha/delta side、ExactUV fixed pair 与 source row 必须同属一个 pre-Cauchy trace key。"
            "匿名失败已被命名 return 矩阵吸收；当前生产性硬点推进到 "
            "`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor signed atom trace rebase sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_rebased_signed_atom_fields_imported={fmt_bool(result['latest_rebased_signed_atom_fields_imported'])}",
        f"existing_constructor_signed_atom_trace_reusable={fmt_bool(result['existing_constructor_signed_atom_trace_reusable'])}",
        f"trace_sync_router_imported={fmt_bool(result['trace_sync_router_imported'])}",
        f"closed_unsigned_labels_carried={fmt_bool(result['closed_unsigned_labels_carried'])}",
        f"same_trace_key_and_named_return_matrix_synced={fmt_bool(result['same_trace_key_and_named_return_matrix_synced'])}",
        f"constructor_source_atoms_carried_forward={fmt_bool(result['constructor_source_atoms_carried_forward'])}",
        f"constructor_side_gates_not_paid_by_trace_sync={fmt_bool(result['constructor_side_gates_not_paid_by_trace_sync'])}",
        f"trace_self_proof_cycle_cut_synced={fmt_bool(result['trace_self_proof_cycle_cut_synced'])}",
        f"signed_atom_trace_rebased={fmt_bool(result['signed_atom_trace_rebased'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(result['new_primitive_payload_or_trace_artifact_present'])}",
        f"edge_local_signed_atom_fields_proved={fmt_bool(result['edge_local_signed_atom_fields_proved'])}",
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
    sample = result.get("imported_largest_slot_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 2. 导入 slot 样本",
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
            "并行出口：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "constructor 携带义务：",
            "",
            "```text",
            "\n".join(result["paired_constructor_required_targets"]),
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
