#!/usr/bin/env python3
"""归档 product-window signed payload 下游同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_signed_payload_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-signed-payload-downstream-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-signed-payload-downstream-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-signed-payload-downstream-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-signed-payload-downstream-sync-router.md

本证书承接 product-window modelgap downstream sync。它不宣称行/列命题
无条件闭合，只把该证书留下的 offdiagonal source-tuple signed payload 接入
仓库中已经存在的 pure-pair、Ferrers、two-prime no-swap、edge-local field-cut
以及 product-window signed-fields/source-rank/alpha/terminal 链，防止后续研究
继续停在已经可下钻的旧硬点名上。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-signed-payload-downstream-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-modelgap-downstream-sync-router.json"
LATEST_PURE_ATOM = DOCS / "prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.json"
LATEST_FERRERS = DOCS / "prime-matrix-phi-lpf-latest-pure-pair-ferrers-support-sync-router.json"
LATEST_NO_SWAP = DOCS / "prime-matrix-phi-lpf-latest-two-prime-no-swap-sync-router.json"
LATEST_FIELD_CUT = DOCS / "prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-router.json"
PRODUCT_FIELDS = DOCS / "prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel-router.json"
PRODUCT_ALPHA = DOCS / "prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-router.json"
PRODUCT_TERMINAL = DOCS / "prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.json"
POINTWISE_FRONTIER = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
PURE_SEMIPRIME_ATOM = "PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward"
TWO_PRIME_KERNEL = "PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward"
EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
SIGNED_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"

ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"

NO_FURTHER_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
CLOSED_MODELGAP = "ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync"
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
    """读取 JSON 证书；缺失只产生 false 诊断，不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写成小写文本。"""
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
    """返回 product-window signed payload 下游携带的 source 三原子。"""
    return f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {SAME_UNIT_RANK}"


def source_hashes() -> dict[str, str]:
    """登记本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        LATEST_PURE_ATOM,
        LATEST_FERRERS,
        LATEST_NO_SWAP,
        LATEST_FIELD_CUT,
        PRODUCT_FIELDS,
        PRODUCT_ALPHA,
        PRODUCT_TERMINAL,
        POINTWISE_FRONTIER,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本轮 product-window signed payload 非循环同步链。"""
    return [
        {
            "from": OFFDIAG_SIGNED_FORMULA,
            "to": PURE_SEMIPRIME_ATOM,
            "meaning": "source-tuple first-seed 部分先收窄到 tail=1 pure semiprime pair；tail>1 只进入 internal transition。",
        },
        {
            "from": PURE_SEMIPRIME_ATOM,
            "to": TWO_PRIME_KERNEL,
            "meaning": "Ferrers 支撑、degree 和 multiplicity label 已支付，剩余是每条 canonical edge 的 two-prime signed kernel。",
        },
        {
            "from": TWO_PRIME_KERNEL,
            "to": EDGE_LOCAL_FORMULA,
            "meaning": "ordered no-swap 删除 `pq=qp` 交换对称伪出口，只保留 LPF owner canonical edge。",
        },
        {
            "from": EDGE_LOCAL_FORMULA,
            "to": SIGNED_FIELDS,
            "meaning": "edge-local field-cut 再剥离 owner/product/Ferrers 等无符号 label，剩余为 signed atom fields 或命名 return。",
        },
        {
            "from": SIGNED_FIELDS,
            "to": source_atoms(),
            "meaning": "product-window signed-fields/source-rank 链把匿名 signed fields 吸收到同 trace-key source-rank/alpha 三原子。",
        },
        {
            "from": ALPHA_ANCHOR,
            "to": f"{NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE}",
            "meaning": "alpha/terminal/modelgap 下游已同步；它删除 alpha 和模型缺口旧名，但不证明 source identity、rank、orientation、ExactUV、internal transition、Rate 或 DStructure。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成下游同步判定表。"""
    previous = data["previous"]
    pure = data["pure"]
    ferrers = data["ferrers"]
    no_swap = data["no_swap"]
    field_cut = data["field_cut"]
    fields = data["fields"]
    alpha = data["alpha"]
    terminal = data["terminal"]
    pointwise = data["pointwise"]
    exactuv = data["exactuv"]

    old_gate_active = (
        previous.get("next_primary_attack_target") == OFFDIAG_SIGNED_FORMULA
        and previous.get("product_window_modelgap_downstream_removed_from_active_basis") is True
    )
    source_tuple_reduced = (
        pure.get("target_input_before_router") == OFFDIAG_SIGNED_FORMULA
        and pure.get("next_primary_attack_target") == PURE_SEMIPRIME_ATOM
        and pure.get("pure_pair_atom_bijection_synced") is True
    )
    ferrers_reduced = (
        ferrers.get("target_input_before_router") == PURE_SEMIPRIME_ATOM
        and ferrers.get("next_primary_attack_target") == TWO_PRIME_KERNEL
        and ferrers.get("ferrers_support_rule_synced") is True
    )
    no_swap_reduced = (
        no_swap.get("target_input_before_router") == TWO_PRIME_KERNEL
        and no_swap.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA
        and no_swap.get("lpf_owner_ordered_no_swap_synced") is True
    )
    field_cut_reduced = (
        field_cut.get("target_input_before_router") == EDGE_LOCAL_FORMULA
        and field_cut.get("next_primary_attack_target") == SIGNED_FIELDS
        and field_cut.get("latest_basis_replaces_edge_local_formula_with_signed_atom_fields") is True
    )
    source_rank_synced = (
        fields.get("target_input_before_router") == SIGNED_FIELDS
        and fields.get("next_primary_attack_target") == ALPHA_ANCHOR
        and fields.get("same_trace_key_and_named_return_matrix_synced") is True
    )
    alpha_terminal_synced = (
        alpha.get("target_input_before_router") == ALPHA_ANCHOR
        and alpha.get("next_primary_attack_target") == "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
        and terminal.get("next_primary_attack_target") == "ExplicitModelGapAndFiniteDPRCLedger"
    )
    old_payload_removed = all(
        [
            old_gate_active,
            source_tuple_reduced,
            ferrers_reduced,
            no_swap_reduced,
            field_cut_reduced,
            source_rank_synced,
            alpha_terminal_synced,
        ]
    )

    return [
        row(
            "ProductWindowOldSourceTupleGateActiveBeforeSync",
            old_gate_active,
            False,
            "上一 product-window modelgap downstream 证书把第一 signed payload 硬点停在 source-tuple formula。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "SourceTupleToPurePairAtomImported",
            source_tuple_reduced,
            False,
            "既有 latest pure-pair atom sync 可把 source tuple first-seed 收窄到 pure pair atom。",
            PURE_SEMIPRIME_ATOM,
        ),
        row(
            "PurePairFerrersSupportImported",
            ferrers_reduced,
            False,
            "Ferrers 支撑/degree 已闭合；pure-pair atom 的自由部分只剩 two-prime signed kernel。",
            TWO_PRIME_KERNEL,
        ),
        row(
            "TwoPrimeNoSwapImported",
            no_swap_reduced,
            False,
            "ordered no-swap 已排除交换对称伪 signed 来源。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "EdgeLocalFieldCutImported",
            field_cut_reduced,
            False,
            "edge-local 入口的无符号 label 已耗尽，剩 signed atom fields 或命名 return。",
            SIGNED_FIELDS,
        ),
        row(
            "ProductWindowSignedFieldsSourceRankImported",
            source_rank_synced,
            False,
            "product-window signed fields 已接入 same trace-key/source-rank/alpha 三原子链。",
            source_atoms(),
        ),
        row(
            "AlphaTerminalModelgapAlreadySynced",
            alpha_terminal_synced and previous.get("product_window_modelgap_downstream_removed_from_active_basis") is True,
            False,
            "alpha 旧入口与模型缺口旧名已经由上一批 product-window 证书同步到终端闭合接口和剩余验收门。",
            f"{NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE}",
        ),
        row(
            "OldSourceTupleGateRemovedFromProductWindowFirstTarget",
            old_payload_removed,
            False,
            "source-tuple formula 不能再作为 product-window 当前第一主攻；它已沿下游链压到 source identity/rank 与 edge signed fields 负载。",
            f"{ARITH_ID} AND {SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "SignedAtomFieldsStillOpenAsDirectAlternative",
            field_cut.get("signed_atom_field_table_proved") is False
            and fields.get("edge_local_signed_atom_fields_proved") is False,
            False,
            "若选择直接构造 signed payload，仍需逐 edge signed value/local factor/orientation/ExactUV/source row 或命名 return。",
            SIGNED_FIELDS,
        ),
        row(
            "PreCauchyIdentityAndRankStillOpen",
            fields.get("independent_noncircular_precauchy_arithmetic_identity_statement_proved") is False
            and fields.get("same_unit_exact_uv_rank_multiplicity_certificate_proved") is False,
            False,
            "source-rank/alpha 链没有证明 pre-Cauchy 算术恒等式或 same-unit ExactUV rank/multiplicity。",
            f"{ARITH_ID} AND {SAME_UNIT_RANK}",
        ),
        row(
            "OrientationExactUVInternalTransitionStillOpen",
            field_cut.get("orientation_parity_branch_side_proved") is False
            and field_cut.get("exactuv_fixed_pair_return_tag_proved") is False
            and field_cut.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "orientation、ExactUV return 与 internal prime-adjoin transition 仍是同一 signed payload 的配套字段。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "PointwiseTraceSqrtBypassesStillOpen",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            or exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "逐点 signed table、trace/Type-II、ExactUV 与平方根行尺度旁路仍未由本同步证明。",
            f"{POINTWISE_TABLE} OR {TRACE_BRIDGE} OR {SQRT_INPUT}",
        ),
        row(
            "RateAndDStructureStillOpen",
            previous.get("rate_preservation_ledger_proved") is False
            and previous.get("dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved") is False,
            False,
            "RatePreservation 与 DStructure/Rankin 独立验收仍是终端侧剩余。",
            f"{RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 signed payload 下游前沿，不证明三命题无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 product-window signed payload 下游同步证书。"""
    data = {
        "previous": load_json(PREVIOUS),
        "pure": load_json(LATEST_PURE_ATOM),
        "ferrers": load_json(LATEST_FERRERS),
        "no_swap": load_json(LATEST_NO_SWAP),
        "field_cut": load_json(LATEST_FIELD_CUT),
        "fields": load_json(PRODUCT_FIELDS),
        "alpha": load_json(PRODUCT_ALPHA),
        "terminal": load_json(PRODUCT_TERMINAL),
        "pointwise": load_json(POINTWISE_FRONTIER),
        "exactuv": load_json(EXACTUV_CERT),
    }
    rows = build_rows(data)
    old_payload_removed = rows[7]["closed"]
    latest_terminal_side = f"{NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE}"
    latest_core = (
        f"{ARITH_ID} AND {SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} AND "
        f"{OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {RATE} AND {DSTRUCTURE}"
    )
    latest_basis = (
        f"(({NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE} AND "
        f"{ARITH_ID} AND {SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} AND "
        f"{OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}) OR {SIGNED_FIELDS} OR "
        f"{POINTWISE_TABLE} OR {PRIMITIVE_ORIGIN} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} "
        f"OR {TRACE_BRIDGE} OR {SQRT_INPUT} OR {EXTERNAL_DIBFI}) AND {EXACTUV_PAIR} "
        f"AND {RATE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_signed_payload_downstream_sync_router",
        "status": "product_window_signed_payload_synced_downstream_source_identity_rank_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "product_window_old_source_tuple_gate_active_before_sync": rows[0]["closed"],
        "source_tuple_to_pure_pair_atom_imported": rows[1]["closed"],
        "pure_pair_ferrers_support_imported": rows[2]["closed"],
        "two_prime_no_swap_imported": rows[3]["closed"],
        "edge_local_field_cut_imported": rows[4]["closed"],
        "product_window_signed_fields_source_rank_imported": rows[5]["closed"],
        "alpha_terminal_modelgap_already_synced": rows[6]["closed"],
        "old_source_tuple_gate_removed_from_product_window_first_target": old_payload_removed,
        "signed_atom_fields_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exactuv_rank_multiplicity_certificate_proved": False,
        "orientation_parity_branch_side_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "row_column_unconditional_closed": False,
        "old_primary_attack_target": OFFDIAG_SIGNED_FORMULA,
        "productive_signed_payload_frontier_before_source_rank_absorption": SIGNED_FIELDS,
        "next_primary_attack_target": ARITH_ID,
        "parallel_primary_attack_targets": [
            SAME_UNIT_RANK,
            SIGNED_FIELDS,
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            RATE,
            DSTRUCTURE,
        ],
        "parallel_bypass_attack_targets": [
            POINTWISE_TABLE,
            PRIMITIVE_ORIGIN,
            TRACE_BRIDGE,
            SQRT_INPUT,
            EXTERNAL_DIBFI,
        ],
        "latest_terminal_side_after_router": latest_terminal_side,
        "latest_retained_basis_after_router": latest_basis,
        "latest_open_basis_summary": latest_core,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window modelgap downstream sync 留下的 "
            "`PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` "
            "接入既有 pure-pair、Ferrers、two-prime no-swap、edge-local field-cut 与 "
            "product-window signed-fields/source-rank/alpha/terminal 下游链。结论是："
            "source-tuple formula 不应再作为 product-window 第一主攻；若直接构造 signed payload，"
            "最前沿是逐 edge signed atom fields 或命名 return。沿现有 source-rank/alpha 链继续下钻后，"
            "当前更小的实际剩余包是 pre-Cauchy 算术恒等式、same-unit rank、orientation、ExactUV return、"
            "internal transition、RatePreservation 与 DStructure/Rankin。本证书不证明三命题无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window signed payload downstream sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        (
            "old_source_tuple_gate_removed_from_product_window_first_target="
            f"{fmt_bool(cert['old_source_tuple_gate_removed_from_product_window_first_target'])}"
        ),
        f"source_tuple_to_pure_pair_atom_imported={fmt_bool(cert['source_tuple_to_pure_pair_atom_imported'])}",
        f"pure_pair_ferrers_support_imported={fmt_bool(cert['pure_pair_ferrers_support_imported'])}",
        f"two_prime_no_swap_imported={fmt_bool(cert['two_prime_no_swap_imported'])}",
        f"edge_local_field_cut_imported={fmt_bool(cert['edge_local_field_cut_imported'])}",
        (
            "product_window_signed_fields_source_rank_imported="
            f"{fmt_bool(cert['product_window_signed_fields_source_rank_imported'])}"
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
            "严格含义：本证书只同步旧 signed payload 名称的下游前沿，不证明行/列命题。",
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
        "old_source_tuple_gate_removed_from_product_window_first_target="
        f"{fmt_bool(cert['old_source_tuple_gate_removed_from_product_window_first_target'])}"
    )
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
