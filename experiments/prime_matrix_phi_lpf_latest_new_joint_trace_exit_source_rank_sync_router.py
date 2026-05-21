#!/usr/bin/env python3
"""生成 Phi-LPF latest new-joint trace-exit 到 source-rank/pointwise-kernel 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_trace_exit_source_rank_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_TRACE_EXIT = (
    DOCS / "prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-router.json"
)
LATEST_NEW_PAYLOAD_SOURCE = (
    DOCS / "prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json"
)
OLDER_TRACE_EXIT_CONVERGENCE = (
    DOCS / "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json"
)
POST_ANTISPLIT_CONVERGENCE = (
    DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
)
SOURCE_PACKET_GUARD = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_KERNEL = DOCS / "prime-matrix-strict-pointwise-primitive-kernel-table-router.json"

NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
INDEPENDENT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
TRANSPORT_COHERENCE = (
    "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND "
    "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
)
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失证书不能解释为证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值渲染为小写文本。"""
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


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        CURRENT_TRACE_EXIT,
        LATEST_NEW_PAYLOAD_SOURCE,
        OLDER_TRACE_EXIT_CONVERGENCE,
        POST_ANTISPLIT_CONVERGENCE,
        SOURCE_PACKET_GUARD,
        POINTWISE_KERNEL,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def convergence_chain() -> list[dict[str, str]]:
    """列出从当前 new-joint trace exit 到共同核表前沿的非循环同步链。"""
    return [
        {
            "from": "current latest built-in pairing trace exit",
            "to": NEW_PAYLOAD,
            "meaning": "新 joint built-in pairing 已接到 branch trace；自证环删除后只剩 new primitive payload/trace 或受控出口。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": SOURCE_RANK,
            "meaning": "new primitive 若不是环内改名，必须携带 actual source-rank/no-collapse 包。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
            "meaning": "source-rank 包拆成源域熵、complete key 分区和 fixed-key ExactUV 局部重数。",
        },
        {
            "from": f"{DOMAIN_ENTROPY} / {COMPLETE_KEY} / {REGISTERED_KEY} / {FIXED_KEY}",
            "to": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
            "meaning": "这些 source/no-collapse 线在同 formal-unit 的逐 primitive alpha/delta 核表汇合。",
        },
        {
            "from": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
            "to": f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}",
            "meaning": "核表首攻点是 alpha row anchor/phase 发射公式，并行还需算术恒等式与同表 rank/multiplicity。",
        },
    ]


def build_rows(
    current: dict[str, Any],
    latest_new: dict[str, Any],
    older_sync: dict[str, Any],
    convergence: dict[str, Any],
    packet_guard: dict[str, Any],
    pointwise: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 new-joint trace-exit/source-rank 同步判定表。"""
    controlled_exits = set(current.get("controlled_exit_targets", []))
    return [
        row(
            "CurrentNewJointTraceExitImported",
            current.get("next_primary_attack_target") == NEW_PAYLOAD
            and current.get("branch_trace_self_proof_rejected") is True,
            False,
            "刚提交的 new-joint built-in pairing 层已经把 branch trace 自证环删除，留下 new primitive payload/trace。",
            NEW_PAYLOAD,
        ),
        row(
            "ControlledTraceExitsCarried",
            TERMINAL_DESCENT in controlled_exits and PDEC_SCOPE in controlled_exits,
            False,
            "terminal descent 与 same-set PDEC scope 是受控出口，不是当前已证明的闭合边。",
            f"{TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "LatestNewPayloadSourceAtomAlignmentImported",
            latest_new.get("target_input_before_router") == NEW_PAYLOAD
            and latest_new.get("latest_new_payload_reduced_to_source_rank_atom") is True,
            False,
            "已有 latest new-payload/source-atom 同步证书说明 new payload 必须携带 source-rank/no-collapse 三原子。",
            SOURCE_RANK,
        ),
        row(
            "OlderTraceExitConvergenceSameAbsorberImported",
            older_sync.get("target_input_before_router") == NEW_PAYLOAD
            and older_sync.get("absorbed_to")
            == "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
            False,
            "旧 latest trace-exit 收敛层与当前 new-joint trace-exit 拥有同一 absorber，可无换题复用其下游。",
            "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        ),
        row(
            "PostAntiSplitConvergenceImported",
            convergence.get("new_primitive_exit_absorbed_to_source_rank") is True
            and convergence.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True,
            False,
            "post-antisplit 收敛证书已把 new primitive、terminal、source entropy、complete key 与 fixed-key 线汇入逐点核表。",
            convergence.get("pointwise_kernel_table", "pointwise primitive kernel table"),
        ),
        row(
            "SourcePacketGuardConfirmsNoLPFSignedShortcut",
            packet_guard.get("common_packet_self_proof_rejected_after_lpf") is True
            and packet_guard.get("lpf_unsigned_data_not_primitive_signed_artifact") is True,
            True,
            "LPF/Phi 桶只支付 support/capacity/root，不能从无符号桶反推 signed payload。",
            ALPHA_ROW,
        ),
        row(
            "PointwiseKernelFrontierImported",
            pointwise.get("next_direct_attack_target") == ALPHA_ROW,
            False,
            "逐点 primitive alpha/delta 核表自身的第一字段是 alpha row anchor/phase emission。",
            ALPHA_ROW,
        ),
        row(
            "ExactUVEntropyFiberPairCarried",
            current.get("parallel_primary_attack_target") == EXACTUV_PAIR
            and current.get("exactuv_entropy_fiber_pair_carried") is True,
            False,
            "当前 new-joint trace-exit 的 ExactUV 并行门仍是 source entropy/fixed fiber 合取。",
            EXACTUV_PAIR,
        ),
        row(
            "AlphaRowAnchorCurrentCorpusProved",
            False,
            False,
            "当前语料没有证明 alpha row anchor/phase emission formula。",
            ALPHA_ROW,
        ),
        row(
            "IndependentArithmeticIdentityStillParallel",
            convergence.get("independent_noncircular_precauchy_arithmetic_identity_statement_proved")
            is False,
            False,
            "同 formal-unit 的 pre-Cauchy 算术恒等式仍需独立证明。",
            INDEPENDENT_IDENTITY,
        ),
        row(
            "SameUnitRankMultiplicityStillParallel",
            convergence.get("same_unit_exact_uv_rank_multiplicity_certificate_proved") is False,
            False,
            "同表 ExactUV rank/multiplicity 仍需独立证明。",
            SAME_UNIT_RANK,
        ),
        row(
            "PointwiseAndTransportAlternativesStillOpen",
            packet_guard.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            and packet_guard.get("phi_lpf_rough_cofactor_transport_coherence_proved") is False,
            False,
            "逐点 Phi-LPF signed 表与 rough-cofactor transport/coherence 仍不是由本同步自动推出。",
            f"{POINTWISE_TABLE} OR {TRANSPORT_COHERENCE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把当前 new-joint trace-exit 接到已有 source-rank/pointwise-kernel 收敛前沿；未证明三命题无条件闭合。",
            f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    current = load_json(CURRENT_TRACE_EXIT)
    latest_new = load_json(LATEST_NEW_PAYLOAD_SOURCE)
    older_sync = load_json(OLDER_TRACE_EXIT_CONVERGENCE)
    convergence = load_json(POST_ANTISPLIT_CONVERGENCE)
    packet_guard = load_json(SOURCE_PACKET_GUARD)
    pointwise = load_json(POINTWISE_KERNEL)
    rows = build_rows(current, latest_new, older_sync, convergence, packet_guard, pointwise)
    pointwise_basis = f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}"
    retained_basis = (
        f"(({pointwise_basis}) OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI} "
        f"OR {POINTWISE_TABLE} OR {EXACTUV_PAIR} OR ({TRANSPORT_COHERENCE})) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_trace_exit_source_rank_sync_router",
        "status": "phi_lpf_latest_new_joint_trace_exit_synced_to_source_rank_pointwise_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_new_joint_trace_exit_imported": rows[0]["closed"],
        "controlled_trace_exits_carried": rows[1]["closed"],
        "latest_new_payload_source_atom_alignment_imported": rows[2]["closed"],
        "older_trace_exit_convergence_same_absorber_imported": rows[3]["closed"],
        "post_antisplit_convergence_imported": rows[4]["closed"],
        "source_packet_guard_confirms_no_lpf_signed_shortcut": rows[5]["closed"],
        "pointwise_kernel_frontier_imported": rows[6]["closed"],
        "exactuv_entropy_fiber_pair_carried": rows[7]["closed"],
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_rough_cofactor_transport_coherence_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": NEW_PAYLOAD,
        "absorbed_to": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        "next_primary_attack_target": ALPHA_ROW,
        "parallel_primary_attack_targets": [
            INDEPENDENT_IDENTITY,
            SAME_UNIT_RANK,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            TRANSPORT_COHERENCE,
        ],
        "latest_retained_basis_after_router": retained_basis,
        "convergence_chain": convergence_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把当前 new-joint latest trace-exit 的 "
            f"`{NEW_PAYLOAD}` 接到已有 source-rank/pointwise-kernel 收敛链。"
            "若 new primitive 不是 signed-lane 环内改名，就必须提交 actual source-rank/no-collapse 三原子；"
            "这些线已经在同 formal-unit 的逐 primitive alpha/delta 核表上汇合。"
            f"因此最新直接主攻推进为 `{ALPHA_ROW}`，并行仍需 `{INDEPENDENT_IDENTITY}`、"
            f"`{SAME_UNIT_RANK}`、terminal/PDEC 出口、逐点 Phi-LPF signed 表、ExactUV entropy/fiber 与 "
            "rough-cofactor transport/coherence。行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest new-joint trace-exit source-rank sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"current_new_joint_trace_exit_imported={fmt_bool(cert['current_new_joint_trace_exit_imported'])}",
        f"controlled_trace_exits_carried={fmt_bool(cert['controlled_trace_exits_carried'])}",
        (
            "latest_new_payload_source_atom_alignment_imported="
            f"{fmt_bool(cert['latest_new_payload_source_atom_alignment_imported'])}"
        ),
        (
            "older_trace_exit_convergence_same_absorber_imported="
            f"{fmt_bool(cert['older_trace_exit_convergence_same_absorber_imported'])}"
        ),
        f"post_antisplit_convergence_imported={fmt_bool(cert['post_antisplit_convergence_imported'])}",
        (
            "source_packet_guard_confirms_no_lpf_signed_shortcut="
            f"{fmt_bool(cert['source_packet_guard_confirms_no_lpf_signed_shortcut'])}"
        ),
        f"pointwise_kernel_frontier_imported={fmt_bool(cert['pointwise_kernel_frontier_imported'])}",
        f"exactuv_entropy_fiber_pair_carried={fmt_bool(cert['exactuv_entropy_fiber_pair_carried'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(cert['alpha_row_anchor_phase_emission_formula_proved'])}",
        (
            "independent_noncircular_precauchy_arithmetic_identity_statement_proved="
            f"{fmt_bool(cert['independent_noncircular_precauchy_arithmetic_identity_statement_proved'])}"
        ),
        (
            "same_unit_exact_uv_rank_multiplicity_certificate_proved="
            f"{fmt_bool(cert['same_unit_exact_uv_rank_multiplicity_certificate_proved'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 收敛链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["convergence_chain"]:
        lines.append(
            f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最新活动基",
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
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "## 4. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    cert = build_certificate()
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
