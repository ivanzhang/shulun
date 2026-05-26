#!/usr/bin/env python3
"""归档 product-window modelgap 下游前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_modelgap_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-modelgap-downstream-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-modelgap-downstream-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-modelgap-downstream-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-modelgap-downstream-sync-router.md

本证书承接 product-window terminal/modelgap frontier 证书。它不宣称三命题
无条件闭合，只把该证书留下的 ExplicitModelGapAndFiniteDPRCLedger 接入
仓库中已经完成的下游拆分、调和窗口、动态骨架、B3/Mertens 尾段同步证书，
从而把 product-window 的第一硬点从模型缺口账本推进到 signed payload、
RatePreservation 与 DStructure/Rankin 等仍开放的真实门。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-modelgap-downstream-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.json"
EXPLICIT = DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json"
HIGH = DOCS / "prime-matrix-high-segment-model-gap-factorization-router.json"
HARMONIC = DOCS / "prime-matrix-harmonic-window-dusart-ledger-router.json"
DYNAMIC = DOCS / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"
LINEAR = DOCS / "prime-matrix-linear-lower-sieve-tail-margin-router.json"
B3_BRIDGE = DOCS / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json"
RATE_MERTENS = DOCS / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"

MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
HIGH_ATOM = "HighSegmentModelGapAlpha043C3AnalyticLedger"
HARMONIC_ATOM = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
DYNAMIC_ATOM = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
LINEAR_TAIL = "LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger"
TEN_PERCENT_TAIL = "LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger"
CLOSED_MODELGAP_ATOM = "ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync"

CANONICAL_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
RATE_PDEC = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"

ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
PHI_LPF_POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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
    """登记本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        EXPLICIT,
        HIGH,
        HARMONIC,
        DYNAMIC,
        LINEAR,
        B3_BRIDGE,
        RATE_MERTENS,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本次非循环下游同步链。"""
    return [
        {
            "from": MODEL,
            "to": HIGH_ATOM,
            "meaning": "低段有限 DPRC 证书已闭合，模型缺口混合账本先压成高段模型余量。",
        },
        {
            "from": HIGH_ATOM,
            "to": f"{HARMONIC_ATOM} AND {DYNAMIC_ATOM}",
            "meaning": "高段模型余量被拆成调和窗口上界与动态粗骨架下界，桥接段 2003<=P<3001 已闭合。",
        },
        {
            "from": HARMONIC_ATOM,
            "to": "DusartPrimeReciprocalWindowAlpha043Upper0850Closed",
            "meaning": "调和窗口由有限枚举加 Dusart 素数倒数和显式估计关闭。",
        },
        {
            "from": DYNAMIC_ATOM,
            "to": LINEAR_TAIL,
            "meaning": "动态粗骨架有限段 3001<=P<100000 已闭合，尾段压成一维 lower-sieve。",
        },
        {
            "from": LINEAR_TAIL,
            "to": TEN_PERCENT_TAIL,
            "meaning": "P=100000 处 10% 模型主项已超过 401，尾段义务压成显式 10% 主项包。",
        },
        {
            "from": "B3/Mertens tail package",
            "to": "closed for current strict rate-bearing tail sync",
            "meaning": "后续 rate-bearing Mertens 同步已把自足 Mertens 尾段移出活动剩余；但 Rate、PDEC 与 DStructure 门仍开放。",
        },
        {
            "from": "product-window modelgap side",
            "to": f"{CLOSED_MODELGAP_ATOM}",
            "meaning": "模型缺口不再是 product-window 当前第一主攻；第一硬点转回 signed payload、Rate 与 DStructure。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成下游同步判定表。"""
    previous = data["previous"]
    explicit = data["explicit"]
    high = data["high"]
    harmonic = data["harmonic"]
    dynamic = data["dynamic"]
    linear = data["linear"]
    b3 = data["b3"]
    rate_mertens = data["rate_mertens"]

    previous_model_active = (
        previous.get("next_primary_attack_target") == MODEL
        and previous.get("explicit_model_gap_and_finite_dprc_ledger_proved") is False
        and previous.get("row_column_unconditional_closed") is False
    )
    explicit_split = (
        explicit.get("explicit_model_gap_and_finite_dprc_ledger_split_closed") is True
        and explicit.get("finite_dprc_alpha043_p_below_2003_certificate_closed") is True
        and explicit.get("next_priority") == HIGH_ATOM
    )
    high_factorized = (
        high.get("high_segment_model_gap_factorized") is True
        and high.get("bridge_finite_model_gap_certificate_closed") is True
        and high.get("replacement", {}).get(HIGH_ATOM)
        == f"({HARMONIC_ATOM} AND {DYNAMIC_ATOM})"
    )
    harmonic_closed = (
        harmonic.get("harmonic_window_alpha043_upper0850_closed") is True
        and harmonic.get("next_priority") == DYNAMIC_ATOM
    )
    dynamic_factorized = (
        dynamic.get("dynamic_skeleton_lower_factorized") is True
        and dynamic.get("finite_dynamic_skeleton_certificate_closed") is True
        and dynamic.get("next_priority") == LINEAR_TAIL
    )
    linear_compressed = (
        linear.get("tail_linear_sieve_input_compressed") is True
        and linear.get("next_priority") == TEN_PERCENT_TAIL
    )
    b3_tail_bridge = (
        b3.get("tail_object_interface_closed") is True
        and b3.get("tail_ledger_external_or_standard_closed") is True
        and b3.get("tail_ledger_strict_self_contained_proved") is False
    )
    strict_mertens_closed = (
        rate_mertens.get("strict_self_contained_mertens_tail_proved") is True
        and rate_mertens.get("row_column_unconditional_closed") is False
    )
    downstream_removed = all(
        [
            previous_model_active,
            explicit_split,
            high_factorized,
            harmonic_closed,
            dynamic_factorized,
            linear_compressed,
            b3_tail_bridge,
            strict_mertens_closed,
        ]
    )

    return [
        row(
            "ProductWindowModelGapGateActiveBeforeSync",
            previous_model_active,
            False,
            "上一 product-window 证书的第一硬点确为 ExplicitModelGapAndFiniteDPRCLedger。",
            MODEL,
        ),
        row(
            "ExplicitModelGapFiniteSplitImported",
            explicit_split,
            False,
            "P<2003 有限 DPRC 已闭合，混合模型缺口账本被拆成高段模型余量。",
            HIGH_ATOM,
        ),
        row(
            "HighSegmentFactorizationImported",
            high_factorized,
            False,
            "2003<=P<3001 桥接段已闭合；P>=3001 只剩调和窗口与动态骨架两输入。",
            f"{HARMONIC_ATOM} AND {DYNAMIC_ATOM}",
        ),
        row(
            "HarmonicWindowDusartClosed",
            harmonic_closed,
            True,
            "调和窗口上界已由有限段与 Dusart 素数倒数和显式估计关闭。",
            "closed; keep DynamicRoughSkeleton side only",
        ),
        row(
            "DynamicSkeletonLowerFactorizationImported",
            dynamic_factorized,
            False,
            "动态粗骨架有限段已闭合，尾段改写为 P>=100000 的一维 lower-sieve 账本。",
            LINEAR_TAIL,
        ),
        row(
            "LinearTailTenPercentMarginCompressed",
            linear_compressed,
            False,
            "尾段 lower-sieve 输入已压成 10% 模型主项显式余量包。",
            TEN_PERCENT_TAIL,
        ),
        row(
            "B3TailBridgeImportedWithStrictGuard",
            b3_tail_bridge,
            False,
            "B3 粗筛接口、lower weights 支配和 10% 容量代数已对齐；该桥本身仍保留严格自足守卫。",
            "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 before latest Mertens sync",
        ),
        row(
            "StrictMertensTailClosedByLatestRateSync",
            strict_mertens_closed,
            True,
            "后续 rate-bearing Mertens 最新同步已关闭旧自足 Mertens 尾段原子；本证书只导入该尾段事实。",
            f"{RATE_PDEC} AND {RATE} AND {DSTRUCTURE} still open in the rate-bearing branch",
        ),
        row(
            "ProductWindowModelGapDownstreamRemovedFromActiveBasis",
            downstream_removed,
            False,
            "模型缺口下游链已足够同步，不能再把 ExplicitModelGap 作为 product-window 第一主攻。",
            CLOSED_MODELGAP_ATOM,
        ),
        row(
            "ProductWindowSignedPayloadStillOpen",
            False,
            False,
            "真正破奇偶性仍需要推前前 signed payload、pre-Cauchy identity、same-unit rank/ExactUV 与 internal transition。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {ARITH_ID} AND {SAME_UNIT_RANK}",
        ),
        row(
            "RateAndDStructureStillOpen",
            False,
            False,
            "RatePreservation 与 DStructure/Rankin 独立验收没有被模型缺口下游同步关闭。",
            f"{RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书是下游前沿同步，不是三命题无条件闭合证明。",
            "row_column_unconditional_closed=false",
        ),
    ]


def replace_modelgap(text: str, replacement: str) -> str:
    """在保留基中把模型缺口原子替换为闭合接口原子。"""
    return text.replace(MODEL, replacement)


def build_certificate() -> dict[str, Any]:
    """组装 product-window modelgap 下游同步证书。"""
    data = {
        "previous": load_json(PREVIOUS),
        "explicit": load_json(EXPLICIT),
        "high": load_json(HIGH),
        "harmonic": load_json(HARMONIC),
        "dynamic": load_json(DYNAMIC),
        "linear": load_json(LINEAR),
        "b3": load_json(B3_BRIDGE),
        "rate_mertens": load_json(RATE_MERTENS),
    }
    rows = build_rows(data)
    downstream_removed = rows[8]["closed"]
    previous_basis = data["previous"].get("latest_retained_basis_after_router", "")
    latest_basis_with_closed_atom = replace_modelgap(previous_basis, CLOSED_MODELGAP_ATOM)
    latest_open_basis = replace_modelgap(previous_basis, "MODEL_GAP_DOWNSTREAM_SYNC_CLOSED")
    terminal_side = f"{CANONICAL_TERMINAL} AND {CLOSED_MODELGAP_ATOM} AND {DSTRUCTURE}"
    open_basis_summary = (
        f"{OFFDIAG_SIGNED_FORMULA} AND {ARITH_ID} AND {SAME_UNIT_RANK} AND "
        f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND "
        f"{RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_modelgap_downstream_sync_router",
        "status": "product_window_modelgap_downstream_synced_signed_payload_and_terminal_gates_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "counterexample_absence_not_used": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_modelgap_gate_active_before_sync": rows[0]["closed"],
        "explicit_model_gap_finite_split_imported": rows[1]["closed"],
        "high_segment_factorization_imported": rows[2]["closed"],
        "harmonic_window_dusart_closed": rows[3]["closed"],
        "dynamic_skeleton_lower_factorization_imported": rows[4]["closed"],
        "linear_tail_ten_percent_margin_compressed": rows[5]["closed"],
        "b3_tail_bridge_imported_with_strict_guard": rows[6]["closed"],
        "strict_mertens_tail_closed_by_latest_rate_sync": rows[7]["closed"],
        "product_window_modelgap_downstream_removed_from_active_basis": downstream_removed,
        "product_window_signed_payload_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "row_column_unconditional_closed": False,
        "modelgap_atom_before_router": MODEL,
        "modelgap_closed_interface_after_router": CLOSED_MODELGAP_ATOM,
        "latest_terminal_side_after_router": terminal_side,
        "latest_retained_basis_after_router": latest_basis_with_closed_atom,
        "latest_open_basis_after_router": latest_open_basis,
        "next_primary_attack_target": OFFDIAG_SIGNED_FORMULA,
        "secondary_attack_target": ARITH_ID,
        "terminal_parallel_attack_targets": [
            RATE,
            DSTRUCTURE,
            RATE_PDEC,
        ],
        "parallel_direct_attack_targets": [
            ARITH_ID,
            SAME_UNIT_RANK,
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            PHI_LPF_POINTWISE_TABLE,
            TRACE_BRIDGE,
            SQRT_INPUT,
            EXTERNAL_DIBFI,
        ],
        "latest_open_basis_summary": open_basis_summary,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window terminal/modelgap frontier 留下的 "
            "`ExplicitModelGapAndFiniteDPRCLedger` 接入既有下游证书链：低段有限 DPRC、"
            "高段模型余量因子化、Dusart 调和窗口、动态粗骨架有限桥、P>=100000 lower-sieve "
            "尾段、B3/Mertens 最新同步。结论是模型缺口不再应作为 product-window 当前第一硬点。"
            "但这不是三命题无条件闭合：product-window signed payload、pre-Cauchy identity、"
            "same-unit rank/ExactUV、RatePreservation、DStructure/Rankin 以及 admissible trace/Type-II "
            "通道仍未证明。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window modelgap downstream sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        (
            "product_window_modelgap_gate_active_before_sync="
            f"{fmt_bool(cert['product_window_modelgap_gate_active_before_sync'])}"
        ),
        (
            "explicit_model_gap_finite_split_imported="
            f"{fmt_bool(cert['explicit_model_gap_finite_split_imported'])}"
        ),
        (
            "high_segment_factorization_imported="
            f"{fmt_bool(cert['high_segment_factorization_imported'])}"
        ),
        f"harmonic_window_dusart_closed={fmt_bool(cert['harmonic_window_dusart_closed'])}",
        (
            "dynamic_skeleton_lower_factorization_imported="
            f"{fmt_bool(cert['dynamic_skeleton_lower_factorization_imported'])}"
        ),
        (
            "strict_mertens_tail_closed_by_latest_rate_sync="
            f"{fmt_bool(cert['strict_mertens_tail_closed_by_latest_rate_sync'])}"
        ),
        (
            "product_window_modelgap_downstream_removed_from_active_basis="
            f"{fmt_bool(cert['product_window_modelgap_downstream_removed_from_active_basis'])}"
        ),
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下游同步链",
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
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "终端侧：",
            "",
            "```text",
            cert["latest_terminal_side_after_router"],
            "```",
            "",
            "product-window 总保留基：",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "仍开放的实际负载摘要：",
            "",
            "```text",
            cert["latest_open_basis_summary"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(cert["parallel_direct_attack_targets"] + cert["terminal_parallel_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只同步模型缺口下游链，不证明 signed payload、Rate、DStructure 或行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(
        "product_window_modelgap_downstream_removed_from_active_basis="
        f"{fmt_bool(cert['product_window_modelgap_downstream_removed_from_active_basis'])}"
    )
    print(
        "strict_mertens_tail_closed_by_latest_rate_sync="
        f"{fmt_bool(cert['strict_mertens_tail_closed_by_latest_rate_sync'])}"
    )
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
