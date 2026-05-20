#!/usr/bin/env python3
"""生成 endpoint pivot low-carrier payment-injection-lock 证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_pivot_low_carrier_payment_injection_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-"
    "payment-injection-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-"
    "support-ladder-router.json"
)
ACTUAL_SOURCE_CUT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-"
    "source-cut-router.json"
)
AP_TABLE_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-"
    "fixed-residue-ap-table-router.json"
)
CANONICAL_PAYMENT_CONSERVATION_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-unit-payment-conservation-router.json"
)
CANONICAL_ASSIGNMENT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-assignment-incidence-lock-router.json"
)
NO_LOSS_CERT = DOCS / "prime-matrix-no-loss-return-accounting-router.json"
PARTITION_NO_LOSS_CERT = DOCS / "prime-matrix-partition-coverage-no-loss-equation-router.json"
ACTUAL_PAYMENT_STITCHING_CERT = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"

ENDPOINT_PAYMENT_INJECTION = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierActualPaymentInjectionWithoutEnvelopeReuse"
SAME_AP_LOCK = "EndpointOrbitAlternatingCyclePivotPrimeSameAPTablePaymentInjectionLock"
CROSS_TABLE_SWITCH = "EndpointOrbitAlternatingCyclePivotPrimeCrossTableSwitchPDECOrMovingPivot"
DUPLICATE_COLLISION = "EndpointOrbitAlternatingCyclePivotPrimeDuplicatePaymentCollisionOrSparseSAE"
BOUNDED_SUPPORT = "EndpointOrbitAlternatingCyclePivotPrimeBoundedSourceSupportEndpointSingletonFullMeanOrSparseSAE"
LONG_TRANSFER = "EndpointOrbitAlternatingCyclePivotPrimeLongSourceSupportMassTransferToLowCarrierDemandOrPDEC"
ENDPOINT_STRICT_GAP = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierAPEnvelopeStrictGapOrDenseTablePDEC"
DENSE_TABLE = "EndpointOrbitAlternatingCyclePivotPrimeDenseLowCarrierResidueTablePDECExclusion"
SPARSE_CELL = "EndpointOrbitAlternatingCyclePivotPrimeSparseLowCarrierResidueCellSAESummability"
LOW_SAE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "EndpointOrbitAlternatingCyclePivotPrimeHighCarrierRankDeficitOrSingletonSAE"
NONREPLAY_SAE = "EndpointOrbitAlternatingCyclePivotPrimeNonreplaySparseSAESummability"
MOVING_PIVOT = "EndpointOrbitAlternatingCycleMovingPivotPrimePhaseSlipPDECExclusion"
SOURCE_MULTIPLICITY = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
SPARSE_SCALE = "SparseScaleLadderSAESummability"
ENDPOINT_SINGLETON = "StableLadderEndpointSingletonAtomSAE"
FULL_CYCLE_MEAN = "EndpointOrbitFullCycleMeanAtomSAE"

REDUCED_PAYMENT = f"{SAME_AP_LOCK} AND {CROSS_TABLE_SWITCH} AND {DUPLICATE_COLLISION}"

IMPORT = "StableLadderEndpointOrbitPivotPrimeLowCarrierPaymentInjectionImportedForLockLedger"
NO_ENVELOPE_REUSE = "StableLadderEndpointOrbitPivotPrimePaymentNoEnvelopeReuseCarriedForwardLedger"
AP_TABLE_KEY = "StableLadderEndpointOrbitPivotPrimeLowCarrierSameAPTableKeyTupleLedger"
PAYMENT_DOMAIN = "StableLadderEndpointOrbitPivotPrimeLowCarrierActualPaymentDomainLedger"
CANONICAL_ASSIGNMENT = "StableLadderEndpointOrbitPivotPrimeCanonicalAssignmentIncidenceImportedLedger"
NO_HIDDEN_CROSS_KEY = "StableLadderEndpointOrbitPivotPrimeNoHiddenCrossKeyPaymentImportedLedger"
NO_LOSS_RETURN = "StableLadderEndpointOrbitPivotPrimeNoLossReturnAccountingImportedLedger"
ACTUAL_STITCHING = "StableLadderEndpointOrbitPivotPrimeActualPaymentStitchingDisciplineImportedLedger"
SAME_TABLE_LEDGER = "StableLadderEndpointOrbitPivotPrimeSameAPTablePaymentInjectionLockLedger"
CROSS_TABLE_LEDGER = "StableLadderEndpointOrbitPivotPrimeCrossTableSwitchRouteLedger"
DUPLICATE_LEDGER = "StableLadderEndpointOrbitPivotPrimeDuplicatePaymentCollisionRouteLedger"
NO_PAYMENT = "NoIndependentEndpointPivotPrimeLowCarrierPaymentInjectionAfterLockLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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
    """登记本脚本与上游证书哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        ACTUAL_SOURCE_CUT_CERT,
        AP_TABLE_CERT,
        CANONICAL_PAYMENT_CONSERVATION_CERT,
        CANONICAL_ASSIGNMENT_CERT,
        NO_LOSS_CERT,
        PARTITION_NO_LOSS_CERT,
        ACTUAL_PAYMENT_STITCHING_CERT,
    ]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 payment-injection 硬点替换为同表锁与两个失败出口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_PAYMENT})"
    if ENDPOINT_PAYMENT_INJECTION in target:
        return target.replace(ENDPOINT_PAYMENT_INJECTION, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        NO_ENVELOPE_REUSE,
        AP_TABLE_KEY,
        PAYMENT_DOMAIN,
        CANONICAL_ASSIGNMENT,
        NO_HIDDEN_CROSS_KEY,
        NO_LOSS_RETURN,
        ACTUAL_STITCHING,
        SAME_TABLE_LEDGER,
        CROSS_TABLE_LEDGER,
        DUPLICATE_LEDGER,
        NO_PAYMENT,
        new_target,
    ]
    return " AND ".join(ledgers)


def replace_latest_basis(previous: dict[str, Any], reduced: str) -> str:
    """更新长活动基。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    old = previous.get("next_direct_attack_target", "")
    if basis and old and old in basis:
        return basis.replace(old, reduced)
    return reduced


def payment_key_records() -> list[dict[str, str]]:
    """列出 endpoint 同表支付键字段。"""
    return [
        {"field": "endpoint_packet_id", "meaning": "同一个 endpoint signed-depth/flux packet 的源侧单位。"},
        {"field": "pivot_prime_q", "meaning": "同一个低 carrier pivot prime，且 q<P 时 AP 公式有效。"},
        {"field": "fixed_residue_a", "meaning": "同一个 low-carrier residue cell。"},
        {"field": "row_ap_class", "meaning": "同一个行 AP 类 t==-aP^{-1} mod q。"},
        {"field": "support_window_H", "meaning": "同一个 endpoint 支撑窗口与 AP envelope。"},
        {"field": "source_support_atom", "meaning": "支付单位必须来自源侧 finite support，不来自 envelope reuse。"},
        {"field": "canonical_payment_key", "meaning": "上述字段的 canonical key；跨 key 支付不是同表支付。"},
    ]


def build_rows(
    previous: dict[str, Any],
    actual_source_cut: dict[str, Any],
    ap_table: dict[str, Any],
    conservation: dict[str, Any],
    assignment: dict[str, Any],
    no_loss: dict[str, Any],
    partition_no_loss: dict[str, Any],
    actual_stitching: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 endpoint payment-injection-lock 判定表。"""
    imported = ENDPOINT_PAYMENT_INJECTION in previous.get("next_direct_attack_target", "")
    no_reuse = actual_source_cut.get("endpoint_no_ap_envelope_recycling_guard") is True
    ap_key = (
        ap_table.get("endpoint_pivot_residue_to_row_ap_formula_closed") is True
        and ap_table.get("endpoint_pivot_selected_table_exact_envelope_closed") is True
    )
    assignment_ready = assignment.get("phase_residue_exchange_no_independent_assignment_incidence_closed") is True
    no_hidden_cross_key = conservation.get("phase_residue_exchange_no_hidden_cross_key_payment_closed") is True
    no_loss_ready = (
        no_loss.get("no_loss_return_accounting_closed") is True
        and partition_no_loss.get("partition_coverage_no_loss_equation_closed") is True
    )
    stitching_available = actual_stitching.get("route") == "ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS"
    same_table_ready = imported and no_reuse and ap_key and assignment_ready and no_hidden_cross_key and no_loss_ready
    return [
        row("EndpointLowCarrierPaymentInjectionImportedForLock", imported, False, "导入 low-carrier actual payment injection 硬点。", ENDPOINT_PAYMENT_INJECTION),
        row("EndpointPaymentNoEnvelopeReuseCarriedForward", imported and no_reuse, True, "支付义务必须来自 source-tagged actual incidence，不能从 AP envelope 复用。", NO_ENVELOPE_REUSE),
        row("EndpointLowCarrierSameAPTableKeyTupleClosed", imported and ap_key, True, "同一 payment table 被规范为同一个 (q,a,row AP class,H,source atom) canonical key。", AP_TABLE_KEY),
        row("EndpointLowCarrierActualPaymentDomainClosed", imported and ap_key, True, "合法支付域只含同 endpoint packet 内的 source-support actual units。", PAYMENT_DOMAIN),
        row("EndpointCanonicalAssignmentIncidenceImported", assignment_ready, assignment_ready, "canonical assignment-incidence lock 排除坏计数产生的新容量。", CANONICAL_ASSIGNMENT),
        row("EndpointNoHiddenCrossKeyPaymentImported", no_hidden_cross_key, no_hidden_cross_key, "canonical payment conservation 层已排除隐藏跨 key 支付冒充同 key 支付。", NO_HIDDEN_CROSS_KEY),
        row("EndpointNoLossReturnAccountingImported", no_loss_ready, no_loss_ready, "no-loss/partition 账本保证未进入同表支付的义务必须保留为命名 return。", NO_LOSS_RETURN),
        row("EndpointActualPaymentStitchingDisciplineImported", stitching_available, False, "ActualPaymentStitching 只作为 actual payment 图纪律导入，不替代 endpoint 同表注入证明。", ACTUAL_STITCHING),
        row("EndpointSameAPTablePaymentInjectionLockRegistered", same_table_ready, False, "若 payment injection 成立，它必须落在同一 AP table canonical key 上。", SAME_AP_LOCK),
        row("EndpointCrossTableSwitchRouteRegistered", imported, False, "若支付改换 q、residue、AP 类或 endpoint packet，则不是同表注入，而是 cross-table switch/PDEC 或 moving-pivot。", CROSS_TABLE_SWITCH),
        row("EndpointDuplicatePaymentCollisionRouteRegistered", imported, False, "若多个源单位声称使用同一已付 canonical slot，则进入 duplicate-payment collision 或 sparse SAE 计费。", DUPLICATE_COLLISION),
        row("NoIndependentEndpointLowCarrierPaymentInjectionAfterLock", imported, True, "low-carrier payment injection 不再作为匿名单出口保留。", NO_PAYMENT),
        row("EndpointLowCarrierPaymentInjectionReduced", imported, False, "本步只锁定注入口径；同表注入、跨表切换与重复碰撞出口仍未排斥。", REDUCED_PAYMENT),
        row("EndpointLowCarrierPaymentInjectionProved", False, False, "未证明 endpoint low-carrier payment injection 已经完成。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    actual_source_cut = load_json(ACTUAL_SOURCE_CUT_CERT)
    ap_table = load_json(AP_TABLE_CERT)
    conservation = load_json(CANONICAL_PAYMENT_CONSERVATION_CERT)
    assignment = load_json(CANONICAL_ASSIGNMENT_CERT)
    no_loss = load_json(NO_LOSS_CERT)
    partition_no_loss = load_json(PARTITION_NO_LOSS_CERT)
    actual_stitching = load_json(ACTUAL_PAYMENT_STITCHING_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(
        previous,
        actual_source_cut,
        ap_table,
        conservation,
        assignment,
        no_loss,
        partition_no_loss,
        actual_stitching,
        new_target,
    )
    imported = any(item["gate"] == "EndpointLowCarrierPaymentInjectionImportedForLock" and item["closed"] for item in rows)
    reduced_closed = any(
        item["gate"] == "NoIndependentEndpointLowCarrierPaymentInjectionAfterLock" and item["closed"]
        for item in rows
    )
    same_table_registered = any(
        item["gate"] == "EndpointSameAPTablePaymentInjectionLockRegistered" and item["closed"]
        for item in rows
    )
    plain = (
        "endpoint low-carrier actual payment injection 已被压成注入口径锁："
        "有效支付不能复用 AP envelope，必须以同一个 endpoint packet、pivot prime、residue、"
        "row AP class、窗口和 source atom 形成 canonical same-AP-table key。"
        "跨 key 或跨表支付进入 switch/PDEC 或 moving-pivot；同槽重复支付进入 collision 或 sparse SAE。"
        "本步不证明同表注入存在，也不排斥这些失败出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_low_carrier_payment_injection_lock_router",
        "status": "endpoint_pivot_low_carrier_payment_injection_reduced_to_same_ap_table_lock_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "actual_source_cut_certificate": str(ACTUAL_SOURCE_CUT_CERT.relative_to(ROOT)),
        "ap_table_certificate": str(AP_TABLE_CERT.relative_to(ROOT)),
        "canonical_payment_conservation_certificate": str(CANONICAL_PAYMENT_CONSERVATION_CERT.relative_to(ROOT)),
        "canonical_assignment_certificate": str(CANONICAL_ASSIGNMENT_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_low_carrier_payment_injection_imported": imported,
        "endpoint_no_envelope_reuse_guard_imported": actual_source_cut.get("endpoint_no_ap_envelope_recycling_guard") is True,
        "endpoint_same_ap_table_key_tuple_closed": ap_table.get("endpoint_pivot_selected_table_exact_envelope_closed") is True,
        "endpoint_canonical_assignment_incidence_imported": assignment.get("phase_residue_exchange_no_independent_assignment_incidence_closed") is True,
        "endpoint_no_hidden_cross_key_payment_imported": conservation.get("phase_residue_exchange_no_hidden_cross_key_payment_closed") is True,
        "endpoint_no_loss_return_accounting_imported": no_loss.get("no_loss_return_accounting_closed") is True,
        "endpoint_partition_no_loss_imported": partition_no_loss.get("partition_coverage_no_loss_equation_closed") is True,
        "endpoint_actual_payment_stitching_discipline_imported": actual_stitching.get("route") == "ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS",
        "endpoint_same_ap_table_payment_injection_lock_registered": same_table_registered,
        "endpoint_cross_table_switch_route_registered": imported,
        "endpoint_duplicate_payment_collision_route_registered": imported,
        "endpoint_payment_injection_reduced_to_lock": reduced_closed,
        "endpoint_same_ap_table_payment_injection_lock_proved": False,
        "endpoint_cross_table_switch_pdec_or_moving_pivot_proved": False,
        "endpoint_duplicate_payment_collision_or_sparse_sae_proved": False,
        "endpoint_low_carrier_payment_injection_proved": False,
        "endpoint_bounded_source_support_sae_proved": False,
        "endpoint_long_source_support_mass_transfer_proved": False,
        "endpoint_pivot_ap_envelope_strict_gap_proved": False,
        "endpoint_pivot_dense_low_carrier_residue_table_pdec_proved": False,
        "endpoint_pivot_sparse_low_carrier_residue_cell_sae_proved": False,
        "endpoint_pivot_low_carrier_nonpersistent_sparse_sae_proved": False,
        "endpoint_pivot_high_carrier_rank_deficit_proved": False,
        "endpoint_pivot_nonreplay_sparse_sae_proved": False,
        "endpoint_pivot_moving_prime_phase_slip_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ENDPOINT_PAYMENT_INJECTION,
        "hardpoint_after_router": REDUCED_PAYMENT,
        "old_exits": [ENDPOINT_PAYMENT_INJECTION],
        "new_exits": [SAME_AP_LOCK, CROSS_TABLE_SWITCH, DUPLICATE_COLLISION],
        "parallel_open_exits": [
            BOUNDED_SUPPORT,
            LONG_TRANSFER,
            ENDPOINT_STRICT_GAP,
            DENSE_TABLE,
            SPARSE_CELL,
            LOW_SAE,
            HIGH_RANK,
            NONREPLAY_SAE,
            MOVING_PIVOT,
            SPARSE_SCALE,
            ENDPOINT_SINGLETON,
            FULL_CYCLE_MEAN,
            SOURCE_MULTIPLICITY,
        ],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "payment_key_records": payment_key_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot low-carrier payment-injection-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_low_carrier_payment_injection_imported={fmt_bool(cert['endpoint_low_carrier_payment_injection_imported'])}",
        f"endpoint_no_envelope_reuse_guard_imported={fmt_bool(cert['endpoint_no_envelope_reuse_guard_imported'])}",
        f"endpoint_same_ap_table_key_tuple_closed={fmt_bool(cert['endpoint_same_ap_table_key_tuple_closed'])}",
        f"endpoint_canonical_assignment_incidence_imported={fmt_bool(cert['endpoint_canonical_assignment_incidence_imported'])}",
        f"endpoint_no_hidden_cross_key_payment_imported={fmt_bool(cert['endpoint_no_hidden_cross_key_payment_imported'])}",
        f"endpoint_no_loss_return_accounting_imported={fmt_bool(cert['endpoint_no_loss_return_accounting_imported'])}",
        f"endpoint_partition_no_loss_imported={fmt_bool(cert['endpoint_partition_no_loss_imported'])}",
        f"endpoint_actual_payment_stitching_discipline_imported={fmt_bool(cert['endpoint_actual_payment_stitching_discipline_imported'])}",
        f"endpoint_same_ap_table_payment_injection_lock_registered={fmt_bool(cert['endpoint_same_ap_table_payment_injection_lock_registered'])}",
        f"endpoint_cross_table_switch_route_registered={fmt_bool(cert['endpoint_cross_table_switch_route_registered'])}",
        f"endpoint_duplicate_payment_collision_route_registered={fmt_bool(cert['endpoint_duplicate_payment_collision_route_registered'])}",
        f"endpoint_payment_injection_reduced_to_lock={fmt_bool(cert['endpoint_payment_injection_reduced_to_lock'])}",
        f"endpoint_same_ap_table_payment_injection_lock_proved={fmt_bool(cert['endpoint_same_ap_table_payment_injection_lock_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同表支付键",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["payment_key_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "payment injection 的非循环口径为：",
            "",
            "```text",
            "valid endpoint low-carrier payment injection",
            "  => same canonical AP-table key",
            "  => source-support actual unit, not AP-envelope reuse",
            "",
            "key switch     => CrossTableSwitchPDECOrMovingPivot",
            "duplicate slot => DuplicatePaymentCollisionOrSparseSAE",
            "```",
            "",
            "## 2. 出口更新",
            "",
            "```text",
            cert["hardpoint_before_router"],
            f"  -> {SAME_AP_LOCK}",
            f"  AND {CROSS_TABLE_SWITCH}",
            f"  AND {DUPLICATE_COLLISION}",
            "```",
            "",
            "## 3. 判定表",
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
            "## 4. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书不证明同一 AP table payment injection 存在或足量。",
            "- 本证书只排除 AP envelope reuse、跨 key 混付和同槽重复支付作为匿名注入。",
            "- cross-table switch/moving-pivot 与 duplicate-payment collision/sparse SAE 仍未排斥。",
            "- bounded support、long support mass-transfer、strict gap、dense-table、sparse-cell、高秩、nonreplay 与 endpoint 并行出口仍未排斥。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
    """写出 ledger、JSON 与 Markdown。"""
    cert = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_md(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
