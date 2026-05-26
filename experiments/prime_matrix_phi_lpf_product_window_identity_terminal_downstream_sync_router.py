#!/usr/bin/env python3
"""归档 product-window pre-Cauchy identity 到终端接口的下游同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_identity_terminal_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-identity-terminal-downstream-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-identity-terminal-downstream-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-identity-terminal-downstream-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-identity-terminal-downstream-sync-router.md

本证书承接 product-window signed payload downstream sync。它把当前第一硬点
`IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger` 接入 strict
identity taxonomy、moving-block/NC-BLK 终端路由、canonical terminal promotion
以及 product-window modelgap downstream 接口。结论只是一条非循环同步：identity
旧名不应继续作为 product-window 第一目标；它不证明行/列命题。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-identity-terminal-downstream-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-signed-payload-downstream-sync-router.json"
STRICT_IDENTITY = DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.json"
MOVING_BLOCK = DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"
ALPHA_DOWNSTREAM = DOCS / "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"
CURRENT_TERMINAL = DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.json"
MOVING_DPRC = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"
PRODUCT_TERMINAL = DOCS / "prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.json"
PRODUCT_MODELGAP = DOCS / "prime-matrix-phi-lpf-product-window-modelgap-downstream-sync-router.json"

IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
MOVING = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
NO_FURTHER_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
CLOSED_MODELGAP = "ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync"

SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
SIGNED_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """布尔值小写格式。"""
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
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        STRICT_IDENTITY,
        MOVING_BLOCK,
        ALPHA_DOWNSTREAM,
        CURRENT_TERMINAL,
        MOVING_DPRC,
        PRODUCT_TERMINAL,
        PRODUCT_MODELGAP,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出 identity 到 product-window 终端接口的同步链。"""
    return [
        {
            "from": IDENTITY,
            "to": MOVING,
            "meaning": "strict identity taxonomy 排除 canonical/generic/AP/external 偷渡后，identity 黑箱只能落到 actual moving-block/NC-BLK。",
        },
        {
            "from": MOVING,
            "to": f"{PDEC_CLEAN_KLS} AND {MODEL}",
            "meaning": "strict moving-block 路由删除无名 NC-BLK 出口，压到全局 PDEC/CleanKLS 终端门与模型账本。",
        },
        {
            "from": PDEC_CLEAN_KLS,
            "to": NO_FURTHER_TERMINAL,
            "meaning": "current terminal promotion 在 canonical-source 自足边界内关闭 PDEC/CleanKLS 晋级为新数学门。",
        },
        {
            "from": MODEL,
            "to": CLOSED_MODELGAP,
            "meaning": "product-window modelgap downstream sync 已把模型缺口接入有限 DPRC、高段因子化、Dusart、动态骨架和 B3/Mertens 下游闭合接口。",
        },
        {
            "from": "product-window first identity target",
            "to": f"{SAME_UNIT_RANK} plus orientation/ExactUV/internal transition/Rate/DStructure",
            "meaning": "identity 旧名移出第一主攻；剩余转到同表 rank、signed side fields 和终端验收门。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    previous = data["previous"]
    identity = data["identity"]
    moving = data["moving"]
    alpha = data["alpha"]
    current = data["current"]
    dprc = data["dprc"]
    product_terminal = data["product_terminal"]
    product_modelgap = data["product_modelgap"]

    previous_identity_active = (
        previous.get("next_primary_attack_target") == IDENTITY
        and previous.get("old_source_tuple_gate_removed_from_product_window_first_target") is True
    )
    strict_identity_imported = (
        identity.get("terminal_gap_before_router") == IDENTITY
        and identity.get("terminal_gap_after_router") == MOVING
        and identity.get("strict_identity_statement_taxonomy_adapter_closed") is True
    )
    moving_terminal_imported = (
        moving.get("terminal_gap_before_router") == MOVING
        and PDEC_CLEAN_KLS in str(moving.get("terminal_gap_after_router"))
        and MODEL in str(moving.get("terminal_gap_after_router"))
        and moving.get("strict_actual_moving_block_router_closed") is True
    )
    alpha_downstream_consistent = (
        alpha.get("next_direct_attack_target") == PDEC_CLEAN_KLS
        and alpha.get("independent_identity_taxonomy_reduced_to_actual_moving") is True
        and alpha.get("actual_moving_block_no_unnamed_exit") is True
    )
    canonical_terminal_imported = (
        current.get("terminal_gap_before_router") == PDEC_CLEAN_KLS
        and current.get("terminal_gap_after_router") == NO_FURTHER_TERMINAL
        and current.get("canonical_source_terminal_promotion_closed") is True
        and product_terminal.get("canonical_source_terminal_promotion_imported") is True
    )
    dprc_compat_imported = (
        dprc.get("exact_model_gap_dprc_compatibility_proved") is True
        and product_terminal.get("moving_block_dprc_compatibility_imported") is True
    )
    modelgap_downstream_imported = (
        product_modelgap.get("product_window_modelgap_downstream_removed_from_active_basis") is True
        and product_modelgap.get("modelgap_closed_interface_after_router") == CLOSED_MODELGAP
    )
    identity_removed = all(
        [
            previous_identity_active,
            strict_identity_imported,
            moving_terminal_imported,
            alpha_downstream_consistent,
            canonical_terminal_imported,
            dprc_compat_imported,
            modelgap_downstream_imported,
        ]
    )

    return [
        row(
            "ProductWindowIdentityGateActiveBeforeSync",
            previous_identity_active,
            False,
            "上一 product-window signed payload downstream 证书把第一硬点推进到 IndependentNoncanonicalPreCauchy identity。",
            IDENTITY,
        ),
        row(
            "StrictIdentityTaxonomyImported",
            strict_identity_imported,
            False,
            "strict identity taxonomy 已穷尽 canonical/generic/AP/external 来源类，identity 黑箱压到 actual moving-block/NC-BLK。",
            MOVING,
        ),
        row(
            "MovingBlockTerminalImported",
            moving_terminal_imported,
            False,
            "actual moving-block/NC-BLK 不能作为无名出口，已压到 PDEC/CleanKLS 与模型账本。",
            f"{PDEC_CLEAN_KLS} AND {MODEL}",
        ),
        row(
            "AlphaDownstreamConsistencyImported",
            alpha_downstream_consistent,
            False,
            "alpha signed-weight 下游同步给出同一条 identity -> moving -> terminal/modelgap 链。",
            f"{PDEC_CLEAN_KLS} AND {MODEL}",
        ),
        row(
            "CanonicalTerminalPromotionImported",
            canonical_terminal_imported,
            False,
            "在 canonical-source 自足边界内，PDEC/CleanKLS 终端晋级已无新数学开门；product-window 已导入该接口。",
            NO_FURTHER_TERMINAL,
        ),
        row(
            "MovingBlockDPRCCompatibilityImported",
            dprc_compat_imported,
            True,
            "moving-block 替换只作用在终端原子，不新增模型余量兼容门。",
            "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock closed",
        ),
        row(
            "ProductWindowModelGapDownstreamImported",
            modelgap_downstream_imported,
            False,
            "模型缺口在 product-window 线上已同步到有限 DPRC/B3/Mertens 下游闭合接口。",
            CLOSED_MODELGAP,
        ),
        row(
            "IdentityRemovedFromProductWindowFirstTarget",
            identity_removed,
            False,
            "identity 旧名不应再作为 product-window 第一主攻；它只把负载转回终端接口和仍开放的 rank/signed 字段。",
            f"{SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "SameUnitRankStillOpen",
            previous.get("same_unit_exactuv_rank_multiplicity_certificate_proved") is False,
            False,
            "same-unit ExactUV rank/multiplicity 未由 identity 下游同步证明。",
            SAME_UNIT_RANK,
        ),
        row(
            "OrientationExactUVInternalStillOpen",
            previous.get("orientation_parity_branch_side_proved") is False
            and previous.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False
            and previous.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "orientation、ExactUV return 与 internal transition 仍是 signed payload 的配套硬点。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "RateAndDStructureStillOpen",
            previous.get("rate_preservation_ledger_proved") is False
            and previous.get("dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved") is False,
            False,
            "RatePreservation 与 DStructure/Rankin 仍是终端验收门。",
            f"{RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 identity 下游前沿，不证明三命题无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    data = {
        "previous": load_json(PREVIOUS),
        "identity": load_json(STRICT_IDENTITY),
        "moving": load_json(MOVING_BLOCK),
        "alpha": load_json(ALPHA_DOWNSTREAM),
        "current": load_json(CURRENT_TERMINAL),
        "dprc": load_json(MOVING_DPRC),
        "product_terminal": load_json(PRODUCT_TERMINAL),
        "product_modelgap": load_json(PRODUCT_MODELGAP),
    }
    rows = build_rows(data)
    identity_removed = rows[7]["closed"]
    terminal_side = f"{NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE}"
    latest_open_summary = (
        f"{SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND "
        f"{INTERNAL_TRANSITION} AND {RATE} AND {DSTRUCTURE}"
    )
    latest_basis = (
        f"(({NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE} AND "
        f"{SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} "
        f"AND {INTERNAL_TRANSITION}) OR {SIGNED_FIELDS} OR {POINTWISE_TABLE} OR "
        f"{PRIMITIVE_ORIGIN} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {TRACE_BRIDGE} "
        f"OR {SQRT_INPUT} OR {EXTERNAL_DIBFI}) AND {EXACTUV_PAIR} AND {RATE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_identity_terminal_downstream_sync_router",
        "status": "product_window_identity_synced_to_terminal_interface_rank_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "product_window_identity_gate_active_before_sync": rows[0]["closed"],
        "strict_identity_taxonomy_imported": rows[1]["closed"],
        "moving_block_terminal_imported": rows[2]["closed"],
        "alpha_downstream_consistency_imported": rows[3]["closed"],
        "canonical_terminal_promotion_imported": rows[4]["closed"],
        "moving_block_dprc_compatibility_imported": rows[5]["closed"],
        "product_window_modelgap_downstream_imported": rows[6]["closed"],
        "identity_removed_from_product_window_first_target": identity_removed,
        "same_unit_exactuv_rank_multiplicity_certificate_proved": False,
        "orientation_parity_branch_side_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "row_column_unconditional_closed": False,
        "old_primary_attack_target": IDENTITY,
        "next_primary_attack_target": SAME_UNIT_RANK,
        "parallel_primary_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            RATE,
            DSTRUCTURE,
            SIGNED_FIELDS,
        ],
        "parallel_bypass_attack_targets": [
            POINTWISE_TABLE,
            PRIMITIVE_ORIGIN,
            TRACE_BRIDGE,
            SQRT_INPUT,
            EXTERNAL_DIBFI,
        ],
        "latest_terminal_side_after_router": terminal_side,
        "latest_retained_basis_after_router": latest_basis,
        "latest_open_basis_summary": latest_open_summary,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window signed payload downstream sync 留下的 "
            "`IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger` "
            "接入 strict identity taxonomy、actual moving-block/NC-BLK 终端路由、canonical terminal "
            "promotion 与 product-window modelgap downstream 接口。结论是：identity 旧名不应再作为 "
            "product-window 第一主攻；它只把负载转到已经同步的终端接口，并留下 same-unit rank、"
            "orientation、ExactUV return、internal transition、RatePreservation 与 DStructure/Rankin。"
            "本证书不证明三命题无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window identity terminal downstream sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"strict_identity_taxonomy_imported={fmt_bool(cert['strict_identity_taxonomy_imported'])}",
        f"moving_block_terminal_imported={fmt_bool(cert['moving_block_terminal_imported'])}",
        f"canonical_terminal_promotion_imported={fmt_bool(cert['canonical_terminal_promotion_imported'])}",
        f"product_window_modelgap_downstream_imported={fmt_bool(cert['product_window_modelgap_downstream_imported'])}",
        (
            "identity_removed_from_product_window_first_target="
            f"{fmt_bool(cert['identity_removed_from_product_window_first_target'])}"
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
            "\n".join(cert["parallel_primary_attack_targets"] + cert["parallel_bypass_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只同步 identity 到终端接口，不证明行/列命题。",
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
        "identity_removed_from_product_window_first_target="
        f"{fmt_bool(cert['identity_removed_from_product_window_first_target'])}"
    )
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
