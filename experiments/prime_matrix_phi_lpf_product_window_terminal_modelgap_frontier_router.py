#!/usr/bin/env python3
"""归档 product-window terminal/modelgap 前沿桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_terminal_modelgap_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.md

本证书承接 product-window alpha/kernel 前沿证书。它不宣称行/列命题闭合，
只把该证书留下的旧终端名 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`
接入当前 canonical-source 终端晋级闭合路由，并导入 moving-block/DPRC
兼容性闭合接口。由此 product-window 路线的终端侧最新主攻点应改为
`ExplicitModelGapAndFiniteDPRCLedger` 本身。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ALPHA_FRONTIER = DOCS / "prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-router.json"
TERMINAL_PROMOTION = DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.json"
DPRC_COMPAT = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"
EXTERNAL_LIVE = DOCS / "prime-matrix-external-live-frontier-applicability-sync-20260525.json"

OLD_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
CANONICAL_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
COMPAT_ATOM = "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
CLOSED_COMPAT = "NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"

ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
PHI_LPF_POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
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
        ALPHA_FRONTIER,
        TERMINAL_PROMOTION,
        DPRC_COMPAT,
        EXTERNAL_LIVE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def replace_terminal_atom(text: str) -> str:
    """把旧终端名替换为 canonical-source 终端闭合名。"""
    return text.replace(OLD_TERMINAL, CANONICAL_TERMINAL)


def sync_chain() -> list[dict[str, str]]:
    """列出本次非循环同步链。"""
    return [
        {
            "from": "product-window alpha/kernel frontier",
            "to": f"{OLD_TERMINAL} AND {MODEL} AND {DSTRUCTURE}",
            "meaning": "上一 product-window 证书把 alpha 入口下钻到旧终端容量门、模型余量和 DStructure。",
        },
        {
            "from": OLD_TERMINAL,
            "to": CANONICAL_TERMINAL,
            "meaning": "当前终端晋级调和证书在 canonical-source 自足边界内关闭旧终端晋级缺口。",
        },
        {
            "from": COMPAT_ATOM,
            "to": CLOSED_COMPAT,
            "meaning": "moving-block/DPRC 兼容性证书说明终端替换没有引入新的 DPRC 账本对象。",
        },
        {
            "from": "product-window terminal side",
            "to": f"{CANONICAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE}",
            "meaning": "旧终端名不再是 product-window 第一主攻；真正剩余主门是模型余量/有限 DPRC 账本。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成桥接判定表。"""
    alpha = data["alpha"]
    terminal = data["terminal"]
    dprc = data["dprc"]
    latest_alpha_basis = alpha.get("latest_retained_basis_after_router", "")

    alpha_terminal_active = (
        alpha.get("next_primary_attack_target") == OLD_TERMINAL
        and OLD_TERMINAL in latest_alpha_basis
        and alpha.get("row_column_unconditional_closed") is False
    )
    canonical_terminal_imported = (
        terminal.get("current_terminal_promotion_reconciled") is True
        and terminal.get("terminal_gap_before_router") == OLD_TERMINAL
        and terminal.get("terminal_gap_after_router") == CANONICAL_TERMINAL
        and terminal.get("row_column_unconditional_closed") is False
    )
    external_guard = (
        terminal.get("generic_external_dibfi_open") is True
        and terminal.get("external_gap_after_router") == EXTERNAL_DIBFI
        and terminal.get("row_column_unconditional_closed") is False
    )
    dprc_compat_imported = (
        dprc.get("exact_model_gap_dprc_compatibility_proved") is True
        and dprc.get("closed_input_removed") == COMPAT_ATOM
        and dprc.get("next_priority") == MODEL
        and dprc.get("explicit_model_gap_and_finite_dprc_ledger_proved") is False
    )
    return [
        row(
            "ProductWindowOldTerminalGateActive",
            alpha_terminal_active,
            False,
            "product-window alpha/kernel 前沿的最新直接主攻仍登记为旧终端容量门。",
            OLD_TERMINAL,
        ),
        row(
            "CanonicalSourceTerminalPromotionImported",
            canonical_terminal_imported,
            True,
            "旧终端门已在 canonical-source 自足边界内接到无进一步终端晋级缺口。",
            CANONICAL_TERMINAL,
        ),
        row(
            "GenericExternalDIBFIBranchKeptOpen",
            external_guard,
            True,
            "generic/external DI-BFI 宽口径没有被 canonical 闭合吸收，防止外推成全局定理。",
            EXTERNAL_DIBFI,
        ),
        row(
            "MovingBlockDPRCCompatibilityImported",
            dprc_compat_imported,
            True,
            "moving-block 到终端晋级的替换不改变 ExplicitModelGapAndFiniteDPRCLedger 的对象口径。",
            CLOSED_COMPAT,
        ),
        row(
            "ExplicitModelGapAndFiniteDPRCLedgerStillOpen",
            False,
            False,
            "本步没有证明模型余量/有限 DPRC 账本本身；它成为 product-window 终端侧第一硬点。",
            MODEL,
        ),
        row(
            "DStructureRankinStillOpen",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            DSTRUCTURE,
        ),
        row(
            "ProductWindowSignedPayloadStillOpen",
            False,
            False,
            "pre-Cauchy identity、same-unit rank、offdiagonal signed formula、orientation、ExactUV 与 internal transition 仍未闭合。",
            f"{ARITH_ID} AND {SAME_UNIT_RANK} AND {OFFDIAG_SIGNED_FORMULA}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只完成 product-window 终端/模型余量前沿同步；三命题仍未无条件闭合。",
            f"{MODEL} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 product-window terminal/modelgap 前沿证书。"""
    data = {
        "alpha": load_json(ALPHA_FRONTIER),
        "terminal": load_json(TERMINAL_PROMOTION),
        "dprc": load_json(DPRC_COMPAT),
        "external": load_json(EXTERNAL_LIVE),
    }
    rows = build_rows(data)
    latest_basis = replace_terminal_atom(data["alpha"].get("latest_retained_basis_after_router", ""))
    terminal_side = f"{CANONICAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE}"
    parallel = [
        ARITH_ID,
        SAME_UNIT_RANK,
        OFFDIAG_SIGNED_FORMULA,
        OFFDIAG_ORIENTATION,
        OFFDIAG_EXACTUV,
        INTERNAL_TRANSITION,
        PHI_LPF_POINTWISE_TABLE,
        PRIMITIVE_ORIGIN,
        TERMINAL_DESCENT,
        PDEC_SCOPE,
        TRACE_BRIDGE,
        SQRT_INPUT,
        EXTERNAL_DIBFI,
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_terminal_modelgap_frontier_router",
        "status": "product_window_terminal_modelgap_frontier_synced_modelgap_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_old_terminal_gate_active": rows[0]["closed"],
        "canonical_source_terminal_promotion_imported": rows[1]["closed"],
        "generic_external_dibfi_branch_kept_open": rows[2]["closed"],
        "moving_block_dprc_compatibility_imported": rows[3]["closed"],
        "pdec_cap_or_internal_clean_kls_large_sieve_replaced_by_canonical_terminal": rows[1]["closed"],
        "exact_model_gap_dprc_compatibility_proved": rows[3]["closed"],
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "trace_or_typeii_admissible_signed_family_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_TERMINAL,
        "terminal_gap_after_router": CANONICAL_TERMINAL,
        "external_gap_after_router": EXTERNAL_DIBFI,
        "closed_interface_removed": COMPAT_ATOM,
        "closed_interface_atom": CLOSED_COMPAT,
        "absorbed_to": terminal_side,
        "latest_terminal_side_after_router": terminal_side,
        "latest_retained_basis_after_router": latest_basis,
        "next_primary_attack_target": MODEL,
        "parallel_direct_attack_targets": parallel,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window alpha/kernel 前沿留下的旧终端门 "
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 接入当前 canonical-source 终端晋级闭合路由，"
            "并导入 moving-block/DPRC 兼容性闭合接口。这样 product-window 路线不应继续把旧终端名"
            "作为第一主攻；终端侧真正剩余是 `ExplicitModelGapAndFiniteDPRCLedger`。"
            "这仍不是三命题无条件闭合，因为模型余量账本、DStructure/Rankin、pre-Cauchy identity、"
            "same-unit rank/multiplicity 与 product-window signed payload 仍未证明。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window terminal/modelgap frontier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        (
            "product_window_old_terminal_gate_active="
            f"{fmt_bool(cert['product_window_old_terminal_gate_active'])}"
        ),
        (
            "canonical_source_terminal_promotion_imported="
            f"{fmt_bool(cert['canonical_source_terminal_promotion_imported'])}"
        ),
        (
            "moving_block_dprc_compatibility_imported="
            f"{fmt_bool(cert['moving_block_dprc_compatibility_imported'])}"
        ),
        (
            "explicit_model_gap_and_finite_dprc_ledger_proved="
            f"{fmt_bool(cert['explicit_model_gap_and_finite_dprc_ledger_proved'])}"
        ),
        f"terminal_gap_before_router={cert['terminal_gap_before_router']}",
        f"terminal_gap_after_router={cert['terminal_gap_after_router']}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
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
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(cert["parallel_direct_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只删除旧终端名作为 product-window 第一主攻，并不证明模型余量、signed payload 或行/列命题。",
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
    print(f"product_window_old_terminal_gate_active={fmt_bool(cert['product_window_old_terminal_gate_active'])}")
    print(
        "canonical_source_terminal_promotion_imported="
        f"{fmt_bool(cert['canonical_source_terminal_promotion_imported'])}"
    )
    print(
        "moving_block_dprc_compatibility_imported="
        f"{fmt_bool(cert['moving_block_dprc_compatibility_imported'])}"
    )
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
