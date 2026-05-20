#!/usr/bin/env python3
"""生成 Phi-LPF latest trace-exit 到 source-rank 收敛同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_trace_exit_source_rank_convergence_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_TRACE_EXIT = DOCS / "prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json"
LATEST_NEW_PAYLOAD_SOURCE = (
    DOCS / "prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json"
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
    """读取 JSON 证书；缺失不能当作证明。"""
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
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_TRACE_EXIT,
        LATEST_NEW_PAYLOAD_SOURCE,
        POST_ANTISPLIT_CONVERGENCE,
        SOURCE_PACKET_GUARD,
        POINTWISE_KERNEL,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def convergence_chain() -> list[dict[str, str]]:
    """列出从 latest trace exit 到当前共同核表前沿的链。"""
    return [
        {
            "from": NEW_PAYLOAD,
            "to": SOURCE_RANK,
            "meaning": "new primitive trace/payload 若要破 signed-lane 环，必须携带 source-rank/no-collapse 包。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
            "meaning": "source-rank 包拆成源域熵、complete key 分区和 fixed-key local multiplicity。",
        },
        {
            "from": f"{DOMAIN_ENTROPY} / {COMPLETE_KEY} / {REGISTERED_KEY} / {FIXED_KEY}",
            "to": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
            "meaning": "这些 source/no-collapse 线在同 formal-unit 的逐 primitive alpha/delta 核表上汇合。",
        },
        {
            "from": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
            "to": f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}",
            "meaning": "核表首攻点是 alpha row anchor/phase 发射公式，并行需要算术恒等式与同表 rank/multiplicity。",
        },
    ]


def build_rows(
    latest_trace: dict[str, Any],
    latest_new: dict[str, Any],
    convergence: dict[str, Any],
    packet_guard: dict[str, Any],
    pointwise: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest trace-exit/source-rank 收敛同步判定表。"""
    return [
        row(
            "LatestTraceExitImported",
            latest_trace.get("next_primary_attack_target") == NEW_PAYLOAD,
            False,
            "刚提交的 latest built-in trace 同步层已把环外生产性出口压到 new primitive payload/trace。",
            NEW_PAYLOAD,
        ),
        row(
            "LatestNewPayloadSourceAtomAlignmentImported",
            latest_new.get("target_input_before_router") == NEW_PAYLOAD
            and latest_new.get("next_primary_attack_target") == DOMAIN_ENTROPY,
            False,
            "既有 latest new-payload/source-atom 证书把该出口吸收到 source-rank/no-collapse 三原子包。",
            SOURCE_RANK,
        ),
        row(
            "SourceRankPackageAtomsCarried",
            latest_new.get("latest_new_payload_reduced_to_source_rank_atom") is True,
            False,
            "new-payload 若要成为真新工件，必须同时给出 source entropy、complete key 与 fixed-key ExactUV multiplicity。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "PostAntiSplitConvergenceImported",
            convergence.get("new_primitive_exit_absorbed_to_source_rank") is True
            and convergence.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True,
            False,
            "post-antisplit 收敛证书已把 new primitive、terminal descent、source entropy、complete key 与 fixed-key 线汇入逐 primitive 核表。",
            convergence.get("pointwise_kernel_table", "pointwise primitive kernel table"),
        ),
        row(
            "SourcePacketGuardDownstreamImported",
            packet_guard.get("new_primitive_exit_downstream_already_imported") is True
            and packet_guard.get("next_direct_attack_target") == ALPHA_ROW,
            False,
            "LPF/Phi common-packet cycle guard 已登记 NewPrimitive/terminal 出口下游，并把最新非循环主攻同步到 alpha row anchor。",
            ALPHA_ROW,
        ),
        row(
            "PointwiseKernelFrontierImported",
            pointwise.get("next_direct_attack_target") == ALPHA_ROW,
            False,
            "逐点 primitive alpha/delta 核表自身的第一字段也是 alpha row anchor/phase emission。",
            ALPHA_ROW,
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
            "同 formal-unit 的 pre-Cauchy 算术恒等式仍需独立给出。",
            INDEPENDENT_IDENTITY,
        ),
        row(
            "SameUnitRankMultiplicityStillParallel",
            convergence.get("same_unit_exact_uv_rank_multiplicity_certificate_proved") is False,
            False,
            "同表 ExactUV rank/multiplicity 证书仍是并行门。",
            SAME_UNIT_RANK,
        ),
        row(
            "LPFPhiPointwiseAndTransportStillParallel",
            packet_guard.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            and packet_guard.get("phi_lpf_rough_cofactor_transport_coherence_proved") is False,
            False,
            "Phi-LPF 逐点 signed 表与 rough-cofactor transport/coherence 仍不能由 latest trace-exit 自动推出。",
            f"{POINTWISE_TABLE} OR {TRANSPORT_COHERENCE}",
        ),
        row(
            "ExactUVEntropyFiberStillParallel",
            packet_guard.get("exactuv_entropy_fiber_pair_proved") is False,
            False,
            "ExactUV source entropy/fiber 门仍开放。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 latest trace-exit 接到已有 source-rank/pointwise-kernel 收敛前沿；未证明三命题无条件闭合。",
            f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest trace-exit/source-rank 收敛同步证书。"""
    latest_trace = load_json(LATEST_TRACE_EXIT)
    latest_new = load_json(LATEST_NEW_PAYLOAD_SOURCE)
    convergence = load_json(POST_ANTISPLIT_CONVERGENCE)
    packet_guard = load_json(SOURCE_PACKET_GUARD)
    pointwise = load_json(POINTWISE_KERNEL)
    rows = build_rows(
        latest_trace=latest_trace,
        latest_new=latest_new,
        convergence=convergence,
        packet_guard=packet_guard,
        pointwise=pointwise,
    )
    pointwise_basis = f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}"
    retained_basis = (
        f"(({pointwise_basis}) OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI} OR {POINTWISE_TABLE} "
        f"OR {EXACTUV_PAIR} OR ({TRANSPORT_COHERENCE})) AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_trace_exit_source_rank_convergence_sync_router",
        "status": "phi_lpf_latest_trace_exit_synced_to_source_rank_pointwise_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_trace_exit_imported": rows[0]["closed"],
        "latest_new_payload_source_atom_alignment_imported": rows[1]["closed"],
        "source_rank_package_atoms_carried": rows[2]["closed"],
        "post_antisplit_convergence_imported": rows[3]["closed"],
        "source_packet_guard_downstream_imported": rows[4]["closed"],
        "pointwise_kernel_frontier_imported": rows[5]["closed"],
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_rough_cofactor_transport_coherence_proved": False,
        "exactuv_entropy_fiber_pair_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": NEW_PAYLOAD,
        "absorbed_to": "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        "next_primary_attack_target": ALPHA_ROW,
        "parallel_primary_attack_targets": [
            INDEPENDENT_IDENTITY,
            SAME_UNIT_RANK,
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
            "本步把刚推进出的 latest `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` "
            "接到已有 source-rank 收敛前沿。new primitive 出口若不是 signed-lane 环内改名，就必须携带 "
            "source-rank/no-collapse 三原子；而 post-antisplit 和 LPF/Phi source-packet guard 证书已说明这些线"
            "在同 formal-unit 的逐 primitive alpha/delta 核表上汇合。当前最新直接主攻同步为 "
            f"`{ALPHA_ROW}`，并行仍需 `{INDEPENDENT_IDENTITY}`、`{SAME_UNIT_RANK}`、PDEC、"
            "逐点 Phi-LPF signed 表、ExactUV entropy/fiber 与 rough-cofactor transport/coherence。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest trace-exit source-rank convergence sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_trace_exit_imported={fmt_bool(cert['latest_trace_exit_imported'])}",
        f"latest_new_payload_source_atom_alignment_imported={fmt_bool(cert['latest_new_payload_source_atom_alignment_imported'])}",
        f"source_rank_package_atoms_carried={fmt_bool(cert['source_rank_package_atoms_carried'])}",
        f"post_antisplit_convergence_imported={fmt_bool(cert['post_antisplit_convergence_imported'])}",
        f"source_packet_guard_downstream_imported={fmt_bool(cert['source_packet_guard_downstream_imported'])}",
        f"pointwise_kernel_frontier_imported={fmt_bool(cert['pointwise_kernel_frontier_imported'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(cert['alpha_row_anchor_phase_emission_formula_proved'])}",
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved="
        f"{fmt_bool(cert['independent_noncircular_precauchy_arithmetic_identity_statement_proved'])}",
        f"same_unit_exact_uv_rank_multiplicity_certificate_proved={fmt_bool(cert['same_unit_exact_uv_rank_multiplicity_certificate_proved'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"phi_lpf_rough_cofactor_transport_coherence_proved={fmt_bool(cert['phi_lpf_rough_cofactor_transport_coherence_proved'])}",
        f"exactuv_entropy_fiber_pair_proved={fmt_bool(cert['exactuv_entropy_fiber_pair_proved'])}",
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
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
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
