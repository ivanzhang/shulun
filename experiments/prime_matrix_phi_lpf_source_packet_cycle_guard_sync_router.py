#!/usr/bin/env python3
"""生成 Phi-LPF source packet cycle guard sync 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_source_packet_cycle_guard_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json

输出：
  data/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-source-packet-cycle-guard-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SQUARE_PACKET_CERT = DOCS / "prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json"
SIGNED_CYCLE_CERT = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
POST_SOURCE_PDEC_CERT = DOCS / "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json"
TERMINAL_SYNC_CERT = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
POST_ANTISPLIT_CONVERGENCE_CERT = DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
POINTWISE_VALUE_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"

COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
NEW_PRIMITIVE_ARTIFACT = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
SOURCE_RANK_PACKAGE = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
POINTWISE_KERNEL_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
PRECAUCHY_ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
STEP_UPDATE = "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward"
ORDERED_COHERENCE = "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"


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


def noncycle_exit_rows() -> list[dict[str, str]]:
    """列出 LPF/Phi 回流后保留的非循环出口。"""
    return [
        {
            "exit": NEW_PRIMITIVE_ARTIFACT,
            "role": "直接新增 primitive trace/payload signed 公式；既有下游已要求它携带 source-rank/no-collapse 包。",
            "status": "absorbed_open",
        },
        {
            "exit": TERMINAL_DESCENT,
            "role": "不提交新公式时，把 signed-lane 回流改造成 well-founded strict terminal descent。",
            "status": "open",
        },
        {
            "exit": PDEC_SCOPE,
            "role": "提交同 formal unit、同坏窗集合、同推前口径的 same-set PDEC scope 证书。",
            "status": "open",
        },
        {
            "exit": EXACTUV_PAIR,
            "role": "独立补足 source entropy 与 fixed exact pair fiber 控制。",
            "status": "open",
        },
        {
            "exit": POINTWISE_TABLE,
            "role": "绕过递推 source packet，直接给 Phi-LPF support 上逐点 signed value table。",
            "status": "open",
        },
        {
            "exit": f"{ALPHA_ROW_ANCHOR} AND {PRECAUCHY_ARITH_ID} AND {SAME_UNIT_RANK}",
            "role": "既有 post-antisplit 收敛证书给出的当前共同逐点核表三原子。",
            "status": "open",
        },
        {
            "exit": f"{STEP_UPDATE} AND {ORDERED_COHERENCE}",
            "role": "若走递推 signed transport，仍需每步 local factor 更新与有序分解相容。",
            "status": "open",
        },
    ]


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SQUARE_PACKET_CERT,
        SIGNED_CYCLE_CERT,
        POST_SOURCE_PDEC_CERT,
        TERMINAL_SYNC_CERT,
        POST_ANTISPLIT_CONVERGENCE_CERT,
        POINTWISE_VALUE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(
    square_packet: dict[str, Any],
    signed_cycle: dict[str, Any],
    post_source_pdec: dict[str, Any],
    terminal_sync: dict[str, Any],
    post_antisplit: dict[str, Any],
    pointwise_value: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 cycle guard 判定表。"""
    square_packet_imported = square_packet.get("next_direct_attack_target") == COMMON_PACKET
    signed_cycle_imported = signed_cycle.get("signed_lane_cycle_closed") is True
    return [
        row(
            "SquareBaseReductionImported",
            square_packet_imported,
            False,
            "LPF/Phi square-base route 已把剩余 source declaration 并回 common packet。",
            COMMON_PACKET,
        ),
        row(
            "SignedLaneCycleImported",
            signed_cycle_imported,
            True,
            "common packet -> built-in pairing -> branch trace -> payload -> origin identity -> common packet 已形成闭环。",
            "remove common packet self-proof",
        ),
        row(
            "CommonPacketSelfProofRejectedAfterLPF",
            square_packet_imported and signed_cycle_imported,
            True,
            "LPF/Phi 几何只固定 support 地址，不能把 common packet 当作非循环自证入口。",
            NEW_PRIMITIVE_ARTIFACT,
        ),
        row(
            "NewPrimitiveExitDownstreamAlreadyImported",
            post_antisplit.get("next_direct_attack_target") == ALPHA_ROW_ANCHOR,
            False,
            "既有 post-antisplit 收敛证书已把 NewPrimitive/terminal 出口吸收到 source-rank 与逐点核表。",
            f"{ALPHA_ROW_ANCHOR} AND {PRECAUCHY_ARITH_ID} AND {SAME_UNIT_RANK}",
        ),
        row(
            "LPFUnsignedDataNotPrimitiveSignedArtifact",
            True,
            True,
            "Phi/LPF 的 support/capacity/root 审计不产生 primitive signed payload 或 trace 公式。",
            NEW_PRIMITIVE_ARTIFACT,
        ),
        row(
            "TerminalDescentStillOpen",
            terminal_sync.get("terminal_descent_macro_cycle_guarded") is not True,
            False,
            "terminal descent 可作为非循环替代，但当前统一前沿仍未给出 well-founded 下降证书。",
            TERMINAL_DESCENT,
        ),
        row(
            "PDECScopeStillOpen",
            post_source_pdec.get("acyclic_same_set_scope_match_proved") is not True,
            False,
            "same-set PDEC scope 分支可保留，但当前内部语料未证明同口径 scope match。",
            PDEC_SCOPE,
        ),
        row(
            "ExactUVStillIndependent",
            True,
            False,
            "ExactUV source entropy / fixed-pair fiber 不从 signed-lane cycle guard 或 LPF root 推出。",
            EXACTUV_PAIR,
        ),
        row(
            "PointwiseBucketValueTableStillOpen",
            pointwise_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "直接逐点 signed value table 仍是绕开 common packet 闭环的并行入口。",
            POINTWISE_TABLE,
        ),
        row(
            "TransportStepCoherenceStillOpen",
            True,
            False,
            "递推 signed transport 还缺 step local factor update 与 ordered factorization coherence。",
            f"{STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 LPF 回流后的 cycle guard 和既有 post-antisplit 下游，不证明 alpha 发射、算术恒等式、rank/multiplicity、ExactUV 或 transport coherence。",
            f"({ALPHA_ROW_ANCHOR} AND {PRECAUCHY_ARITH_ID} AND {SAME_UNIT_RANK}) OR {PDEC_SCOPE} OR {POINTWISE_TABLE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi-LPF source packet cycle guard sync 证书。"""
    square_packet = load_json(SQUARE_PACKET_CERT)
    signed_cycle = load_json(SIGNED_CYCLE_CERT)
    post_source_pdec = load_json(POST_SOURCE_PDEC_CERT)
    terminal_sync = load_json(TERMINAL_SYNC_CERT)
    post_antisplit = load_json(POST_ANTISPLIT_CONVERGENCE_CERT)
    pointwise_value = load_json(POINTWISE_VALUE_CERT)
    rows = build_rows(square_packet, signed_cycle, post_source_pdec, terminal_sync, post_antisplit, pointwise_value)
    return {
        "certificate_type": "prime_matrix_phi_lpf_source_packet_cycle_guard_sync_router",
        "status": "phi_lpf_source_packet_self_proof_cycle_guarded_noncycle_exits_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "phi_lpf_source_packet_cycle_guard_sync_closed": True,
        "square_base_reduction_to_common_packet_imported": rows[0]["closed"],
        "signed_lane_cycle_imported": rows[1]["closed"],
        "common_packet_self_proof_rejected_after_lpf": rows[2]["closed"],
        "new_primitive_exit_downstream_already_imported": rows[3]["closed"],
        "lpf_unsigned_data_not_primitive_signed_artifact": True,
        "new_primitive_payload_or_trace_artifact_present": False,
        "source_rank_package_imported": post_antisplit.get("source_rank_package_atomized") is True,
        "pointwise_kernel_table_imported": post_antisplit.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "acyclic_noncanonical_terminal_return_well_founded_descent_proved": False,
        "acyclic_same_set_scope_match_for_direct_pdec_cap_proved": False,
        "exactuv_entropy_fiber_pair_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_rough_cofactor_transport_coherence_proved": False,
        "row_column_unconditional_closed": False,
        "noncycle_exits": noncycle_exit_rows(),
        "gates": rows,
        "next_direct_attack_target": ALPHA_ROW_ANCHOR,
        "parallel_direct_attack_targets": [
            PRECAUCHY_ARITH_ID,
            SAME_UNIT_RANK,
            PDEC_SCOPE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            f"{STEP_UPDATE} AND {ORDERED_COHERENCE}",
        ],
        "hardpoint_after_router": (
            f"(({ALPHA_ROW_ANCHOR} AND {PRECAUCHY_ARITH_ID} AND {SAME_UNIT_RANK}) "
            f"OR {PDEC_SCOPE} OR {POINTWISE_TABLE}) AND {EXACTUV_PAIR} AND {STEP_UPDATE} AND {ORDERED_COHERENCE}"
        ),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "LPF/Phi square-base route 把 source declaration 并回 common packet 后，不能继续把 common packet "
            "当作非循环证明入口：既有 signed-lane cycle 已说明该 packet 会经 built-in pairing、branch trace、"
            "payload 与 origin identity 回到自身。Phi/LPF 当前只固定 support/capacity/root 与 prime-row guard，"
            "不产生 primitive signed payload/trace 公式。并且既有 post-antisplit 收敛证书已把 NewPrimitive/terminal "
            "出口吸收到 source-rank/no-collapse 与逐点 primitive 核表。因此最新非循环主攻同步为 "
            "`AlphaRowAnchorPhaseEmissionFormulaLedger`；并行还需 pre-Cauchy 算术恒等式、同表 rank/multiplicity、"
            "same-set PDEC scope、Phi-LPF pointwise signed value table、ExactUV entropy/fiber 与 transport step/coherence。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF source packet cycle guard sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"square_base_reduction_to_common_packet_imported={fmt_bool(cert['square_base_reduction_to_common_packet_imported'])}",
        f"signed_lane_cycle_imported={fmt_bool(cert['signed_lane_cycle_imported'])}",
        f"common_packet_self_proof_rejected_after_lpf={fmt_bool(cert['common_packet_self_proof_rejected_after_lpf'])}",
        f"new_primitive_exit_downstream_already_imported={fmt_bool(cert['new_primitive_exit_downstream_already_imported'])}",
        f"pointwise_kernel_table_imported={fmt_bool(cert['pointwise_kernel_table_imported'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(cert['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(cert['new_primitive_payload_or_trace_artifact_present'])}",
        f"pointwise_phi_lpf_bucket_signed_value_table_proved={fmt_bool(cert['pointwise_phi_lpf_bucket_signed_value_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非循环出口",
        "",
        "| exit | role | status |",
        "| --- | --- | --- |",
    ]
    for item in cert["noncycle_exits"]:
        lines.append(f"| `{cell(item['exit'])}` | {cell(item['role'])} | `{cell(item['status'])}` |")
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
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 下一真正单点",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "并行出口：",
            "",
            "```text",
            "\n".join(cert["parallel_direct_attack_targets"]),
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
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
