#!/usr/bin/env python3
"""生成 constructor built-in trace 出口到 source-rank/pointwise-kernel 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_trace_source_rank_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CONSTRUCTOR_TRACE = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.json"
)
PRIOR_TRACE_SOURCE_RANK = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-router.json"
)
NEW_PAYLOAD_SOURCE_ATOM = DOCS / (
    "prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json"
)
POST_ANTISPLIT_CONVERGENCE = DOCS / (
    "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
)
SOURCE_PACKET_GUARD = DOCS / "prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json"
POINTWISE_KERNEL = DOCS / "prime-matrix-strict-pointwise-primitive-kernel-table-router.json"

NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
POINTWISE_KERNEL_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
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
    """读取 JSON 证书；缺失文件不能被当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希，方便归档复核。"""
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


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        CONSTRUCTOR_TRACE,
        PRIOR_TRACE_SOURCE_RANK,
        NEW_PAYLOAD_SOURCE_ATOM,
        POST_ANTISPLIT_CONVERGENCE,
        SOURCE_PACKET_GUARD,
        POINTWISE_KERNEL,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def pointwise_basis() -> str:
    """返回共同核表的三原子基。"""
    return f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}"


def retained_basis() -> str:
    """返回本层保留的最新活动基。"""
    return (
        f"(({pointwise_basis()}) OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI} "
        f"OR {POINTWISE_TABLE} OR {EXACTUV_PAIR} OR ({TRANSPORT_COHERENCE})) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def sync_chain() -> list[dict[str, str]]:
    """列出从 constructor trace 出口到共同核表前沿的同步链。"""
    return [
        {
            "from": "constructor built-in trace exit",
            "to": NEW_PAYLOAD,
            "meaning": "上一层已删除 branch-trace/payload/origin/common-packet 自证环，留下 new primitive payload/trace。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": SOURCE_RANK,
            "meaning": "new primitive 若不是环内改名，必须携带 actual pre-Cauchy source-rank/no-collapse 包。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
            "meaning": "source-rank 包拆成源域熵、complete key 分区和 fixed-key ExactUV 局部重数。",
        },
        {
            "from": f"{DOMAIN_ENTROPY} / {COMPLETE_KEY} / {REGISTERED_KEY} / {FIXED_KEY}",
            "to": POINTWISE_KERNEL_TABLE,
            "meaning": "这些 source/no-collapse 线在同 formal-unit 的逐 primitive alpha/delta 核表上汇合。",
        },
        {
            "from": POINTWISE_KERNEL_TABLE,
            "to": pointwise_basis(),
            "meaning": "核表当前最窄前沿是 alpha row anchor、pre-Cauchy 算术恒等式与同表 rank/multiplicity 三原子。",
        },
    ]


def build_rows(
    constructor: dict[str, Any],
    prior_source_rank: dict[str, Any],
    new_payload: dict[str, Any],
    post_antisplit: dict[str, Any],
    packet_guard: dict[str, Any],
    pointwise: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 constructor trace/source-rank 同步判定表。"""
    prior_parallel = set(prior_source_rank.get("parallel_primary_attack_targets", []))
    current_basis = constructor.get("latest_retained_basis_after_router", "")
    return [
        row(
            "ConstructorTraceExitImported",
            constructor.get("next_primary_attack_target") == NEW_PAYLOAD
            and constructor.get("signed_lane_cycle_guard_imported") is True
            and constructor.get("new_primitive_payload_or_trace_artifact_present") is False,
            False,
            "上一层 constructor built-in trace 已把 branch trace 自证误出口删去，留下 new primitive payload/trace。",
            NEW_PAYLOAD,
        ),
        row(
            "ControlledExitBasisCarried",
            TERMINAL_DESCENT in current_basis and PDEC_SCOPE in current_basis,
            False,
            "terminal descent 与 same-set PDEC scope 在 constructor 口径中仍只是受控出口。",
            f"{TERMINAL_DESCENT} OR {PDEC_SCOPE}",
        ),
        row(
            "PriorTraceSourceRankAbsorberImported",
            prior_source_rank.get("target_input_before_router") == NEW_PAYLOAD
            and prior_source_rank.get("absorbed_to") == POINTWISE_KERNEL_TABLE
            and prior_source_rank.get("next_primary_attack_target") == ALPHA_ROW,
            False,
            "已有 trace-exit/source-rank 同步层对同一 NewPrimitive 目标给出共同核表 absorber。",
            POINTWISE_KERNEL_TABLE,
        ),
        row(
            "LatestNewPayloadSourceAtomAlignmentImported",
            new_payload.get("target_input_before_router") == NEW_PAYLOAD
            and new_payload.get("latest_new_payload_reduced_to_source_rank_atom") is True,
            False,
            "new payload 若非环内改名，必须提交 source-rank/no-collapse 三原子。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "PostAntiSplitConvergenceImported",
            post_antisplit.get("new_primitive_exit_absorbed_to_source_rank") is True
            and post_antisplit.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True,
            False,
            "post-antisplit 收敛证书已把 new primitive、terminal、source entropy、complete key 与 fixed-key 线汇入逐点核表。",
            POINTWISE_KERNEL_TABLE,
        ),
        row(
            "LPFPhiUnsignedBucketNoSignedShortcut",
            packet_guard.get("common_packet_self_proof_rejected_after_lpf") is True
            and packet_guard.get("lpf_unsigned_data_not_primitive_signed_artifact") is True,
            True,
            "LPF/Phi 桶恒等式只支付最小素因子 owner、support/capacity/root，不能自动生成 signed payload。",
            ALPHA_ROW,
        ),
        row(
            "PointwiseKernelFrontierImported",
            pointwise.get("next_direct_attack_target") == ALPHA_ROW
            and pointwise.get("alpha_row_anchor_phase_emission_formula_proved") is False,
            False,
            "逐点 primitive alpha/delta 核表的第一实际字段仍是 alpha row anchor/phase emission。",
            pointwise_basis(),
        ),
        row(
            "ExactUVEntropyFiberPairCarried",
            constructor.get("parallel_primary_attack_target") == EXACTUV_PAIR
            and constructor.get("exactuv_parallel_carried") is True
            and EXACTUV_PAIR in prior_parallel,
            False,
            "constructor trace 口径与既有 source-rank 同步层保留同一 ExactUV entropy/fiber 并行门。",
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
            post_antisplit.get("independent_noncircular_precauchy_arithmetic_identity_statement_proved")
            is False,
            False,
            "同 formal-unit 的 pre-Cauchy 算术恒等式仍需独立证明。",
            INDEPENDENT_IDENTITY,
        ),
        row(
            "SameUnitRankMultiplicityStillParallel",
            post_antisplit.get("same_unit_exact_uv_rank_multiplicity_certificate_proved") is False,
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
            "本步只把 constructor trace 的 NewPrimitive 出口接到 source-rank/pointwise-kernel 前沿；未证明三命题无条件闭合。",
            pointwise_basis(),
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装并写出同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    constructor = load_json(CONSTRUCTOR_TRACE)
    prior_source_rank = load_json(PRIOR_TRACE_SOURCE_RANK)
    new_payload = load_json(NEW_PAYLOAD_SOURCE_ATOM)
    post_antisplit = load_json(POST_ANTISPLIT_CONVERGENCE)
    packet_guard = load_json(SOURCE_PACKET_GUARD)
    pointwise = load_json(POINTWISE_KERNEL)
    rows = build_rows(
        constructor, prior_source_rank, new_payload, post_antisplit, packet_guard, pointwise
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_trace_source_rank_sync_router",
        "status": "phi_lpf_latest_constructor_trace_exit_synced_to_source_rank_pointwise_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "constructor_trace_exit_imported": rows[0]["closed"],
        "controlled_exit_basis_carried": rows[1]["closed"],
        "prior_trace_source_rank_absorber_imported": rows[2]["closed"],
        "latest_new_payload_source_atom_alignment_imported": rows[3]["closed"],
        "post_antisplit_convergence_imported": rows[4]["closed"],
        "lpf_phi_unsigned_bucket_no_signed_shortcut": rows[5]["closed"],
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
        "absorbed_to": POINTWISE_KERNEL_TABLE,
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
        "latest_retained_basis_after_router": retained_basis(),
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 constructor 口径的 latest trace 出口 "
            f"`{NEW_PAYLOAD}` 接入已有 source-rank/pointwise-kernel 收敛链。"
            "LPF/Phi 的最小素因子桶恒等式提供 owner/support/capacity/root 账本，"
            "但不产生 primitive signed payload；若 new payload 不是 signed-lane 环内改名，"
            "就必须提交 actual source-rank/no-collapse 三原子，随后这些线在同 formal-unit 的逐点核表汇合。"
            f"因此最新直接主攻推进为 `{ALPHA_ROW}`；并行仍需 `{INDEPENDENT_IDENTITY}`、"
            f"`{SAME_UNIT_RANK}`、terminal/PDEC、逐点 Phi-LPF signed 表、ExactUV entropy/fiber 与 "
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
        "# Prime Matrix Phi-LPF latest constructor trace source-rank sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"constructor_trace_exit_imported={fmt_bool(cert['constructor_trace_exit_imported'])}",
        f"controlled_exit_basis_carried={fmt_bool(cert['controlled_exit_basis_carried'])}",
        (
            "prior_trace_source_rank_absorber_imported="
            f"{fmt_bool(cert['prior_trace_source_rank_absorber_imported'])}"
        ),
        (
            "latest_new_payload_source_atom_alignment_imported="
            f"{fmt_bool(cert['latest_new_payload_source_atom_alignment_imported'])}"
        ),
        f"post_antisplit_convergence_imported={fmt_bool(cert['post_antisplit_convergence_imported'])}",
        (
            "lpf_phi_unsigned_bucket_no_signed_shortcut="
            f"{fmt_bool(cert['lpf_phi_unsigned_bucket_no_signed_shortcut'])}"
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
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
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
