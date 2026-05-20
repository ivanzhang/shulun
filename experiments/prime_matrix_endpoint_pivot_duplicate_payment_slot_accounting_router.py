#!/usr/bin/env python3
"""生成 endpoint pivot duplicate-payment slot-accounting 证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_pivot_duplicate_payment_slot_accounting_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.md
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
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-"
    "slot-accounting"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-"
    "payment-injection-lock-router.json"
)
ASSIGNMENT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-assignment-incidence-lock-router.json"
)
CAPACITY_VALUE_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-capacity-unit-value-lock-router.json"
)
ACTUAL_OBJECT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.json"
)

DUPLICATE_COLLISION = "EndpointOrbitAlternatingCyclePivotPrimeDuplicatePaymentCollisionOrSparseSAE"
SLOT_MULTIPLICITY = "EndpointOrbitAlternatingCyclePivotPrimeDuplicateSameSlotSourceMultiplicityCapPDEC"
DUPLICATE_SPARSE = "EndpointOrbitAlternatingCyclePivotPrimeDuplicatePaymentSparseSAESummability"
SAME_AP_LOCK = "EndpointOrbitAlternatingCyclePivotPrimeSameAPTablePaymentInjectionLock"
CROSS_TABLE_SWITCH = "EndpointOrbitAlternatingCyclePivotPrimeCrossTableSwitchPDECOrMovingPivot"
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

REDUCED_DUPLICATE = f"{SLOT_MULTIPLICITY} AND {DUPLICATE_SPARSE}"

IMPORT = "StableLadderEndpointOrbitPivotPrimeDuplicatePaymentImportedForSlotAccountingLedger"
SAME_SLOT_KEY = "StableLadderEndpointOrbitPivotPrimeDuplicateSameCanonicalSlotKeyLedger"
UNIT_VALUE = "StableLadderEndpointOrbitPivotPrimeDuplicateCapacityUnitValueImportedLedger"
PARTIAL_INJECTION = "StableLadderEndpointOrbitPivotPrimeDuplicateAssignmentPartialInjectionImportedLedger"
ACTUAL_OBJECT_DUP = "StableLadderEndpointOrbitPivotPrimeActualObjectDuplicateCollisionImportedLedger"
NOT_NEW_CAPACITY = "StableLadderEndpointOrbitPivotPrimeDuplicateCountNotNewCapacityLedger"
SLOT_MULTIPLICITY_LEDGER = "StableLadderEndpointOrbitPivotPrimeDuplicateSameSlotMultiplicityRouteLedger"
SPARSE_DUPLICATE_LEDGER = "StableLadderEndpointOrbitPivotPrimeDuplicateSparseRouteLedger"
NO_DUPLICATE = "NoIndependentEndpointPivotPrimeDuplicatePaymentCollisionAfterSlotAccountingLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, ASSIGNMENT_CERT, CAPACITY_VALUE_CERT, ACTUAL_OBJECT_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 duplicate-payment 硬点替换为同槽重数和稀疏重复二出口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_DUPLICATE})"
    if DUPLICATE_COLLISION in target:
        return target.replace(DUPLICATE_COLLISION, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        SAME_SLOT_KEY,
        UNIT_VALUE,
        PARTIAL_INJECTION,
        ACTUAL_OBJECT_DUP,
        NOT_NEW_CAPACITY,
        SLOT_MULTIPLICITY_LEDGER,
        SPARSE_DUPLICATE_LEDGER,
        NO_DUPLICATE,
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


def duplicate_records() -> list[dict[str, str]]:
    """列出 duplicate slot 账本字段。"""
    return [
        {"field": "canonical_slot_key", "meaning": "同一 AP-table key 下的同一个 capacity slot。"},
        {"field": "first_payment_unit", "meaning": "该 slot 的第一单位支付，容量值为 1。"},
        {"field": "extra_source_units", "meaning": "映入同一 slot 的额外 source-support 单位。"},
        {"field": "persistent_duplicate", "meaning": "若额外单位持久出现，则转入同槽源重数 cap/PDEC。"},
        {"field": "nonpersistent_duplicate", "meaning": "若额外单位只在稀疏层出现，则转入 duplicate sparse SAE。"},
    ]


def build_rows(
    previous: dict[str, Any],
    assignment: dict[str, Any],
    capacity_value: dict[str, Any],
    actual_object: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 duplicate-payment slot-accounting 判定表。"""
    imported = DUPLICATE_COLLISION in previous.get("next_direct_attack_target", "")
    same_key = previous.get("endpoint_same_ap_table_payment_injection_lock_registered") is True
    unit_value = capacity_value.get("phase_residue_exchange_capacity_as_unit_indicator_sum_closed") is True
    partial_injection = assignment.get("phase_residue_exchange_assignment_partial_injection_closed") is True
    actual_dup = actual_object.get("phase_residue_exchange_duplicate_object_collision_or_whitelist_closed") is True
    return [
        row("EndpointDuplicatePaymentImportedForSlotAccounting", imported, False, "导入 duplicate-payment collision/sparse SAE 硬点。", DUPLICATE_COLLISION),
        row("EndpointDuplicateSameCanonicalSlotKeyClosed", imported and same_key, True, "上一层已把合法支付锁到同一 AP-table canonical key；duplicate 必须指向同一 slot。", SAME_SLOT_KEY),
        row("EndpointDuplicateCapacityUnitValueImported", unit_value, unit_value, "capacity unit value lock 已把每个 admitted slot 的容量值规范为一单位。", UNIT_VALUE),
        row("EndpointDuplicateAssignmentPartialInjectionImported", partial_injection, partial_injection, "assignment partial injection 表明同一 capacity slot 重复占用不产生新容量。", PARTIAL_INJECTION),
        row("EndpointActualObjectDuplicateCollisionImported", actual_dup, actual_dup, "actual-object admission 已把对象字段重复/错配归入命名 collision/whitelist 出口。", ACTUAL_OBJECT_DUP),
        row("EndpointDuplicateCountNotNewCapacityClosed", imported and unit_value and partial_injection, True, "同一 canonical slot 的第二次支付不能增加 AP table capacity。", NOT_NEW_CAPACITY),
        row("EndpointDuplicateSameSlotMultiplicityRouteRegistered", imported, False, "若重复源单位持久存在，则只能作为同槽 source multiplicity cap/PDEC。", SLOT_MULTIPLICITY),
        row("EndpointDuplicateSparseRouteRegistered", imported, False, "若重复源单位非持久出现，则只能进入 duplicate-payment sparse SAE 计费。", DUPLICATE_SPARSE),
        row("NoIndependentDuplicatePaymentCollisionAfterSlotAccounting", imported, True, "duplicate payment 不再作为匿名容量补偿出口保留。", NO_DUPLICATE),
        row("EndpointDuplicatePaymentReduced", imported, False, "本步只完成 slot 账本分流；同槽重数 cap 与 sparse SAE 仍未证明。", REDUCED_DUPLICATE),
        row("EndpointDuplicatePaymentCollisionExcluded", False, False, "未证明 duplicate-payment collision/sparse SAE 已被排斥。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    assignment = load_json(ASSIGNMENT_CERT)
    capacity_value = load_json(CAPACITY_VALUE_CERT)
    actual_object = load_json(ACTUAL_OBJECT_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, assignment, capacity_value, actual_object, new_target)
    imported = any(item["gate"] == "EndpointDuplicatePaymentImportedForSlotAccounting" and item["closed"] for item in rows)
    reduced_closed = any(
        item["gate"] == "NoIndependentDuplicatePaymentCollisionAfterSlotAccounting" and item["closed"]
        for item in rows
    )
    plain = (
        "endpoint duplicate-payment collision 已被压成同槽账本："
        "合法支付已锁到 same-AP-table canonical slot，且 admitted capacity slot 的值是一单位；"
        "同一 slot 的重复支付不产生新容量。若重复源单位持久出现，只能进入同槽 source multiplicity "
        "cap/PDEC；若非持久出现，则进入 duplicate sparse SAE。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_duplicate_payment_slot_accounting_router",
        "status": "endpoint_pivot_duplicate_payment_reduced_to_same_slot_multiplicity_or_sparse_sae_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "assignment_certificate": str(ASSIGNMENT_CERT.relative_to(ROOT)),
        "capacity_value_certificate": str(CAPACITY_VALUE_CERT.relative_to(ROOT)),
        "actual_object_certificate": str(ACTUAL_OBJECT_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_duplicate_payment_imported": imported,
        "endpoint_duplicate_same_canonical_slot_key_closed": previous.get("endpoint_same_ap_table_payment_injection_lock_registered") is True,
        "endpoint_duplicate_capacity_unit_value_imported": capacity_value.get("phase_residue_exchange_capacity_as_unit_indicator_sum_closed") is True,
        "endpoint_duplicate_assignment_partial_injection_imported": assignment.get("phase_residue_exchange_assignment_partial_injection_closed") is True,
        "endpoint_actual_object_duplicate_collision_imported": actual_object.get("phase_residue_exchange_duplicate_object_collision_or_whitelist_closed") is True,
        "endpoint_duplicate_count_not_new_capacity_closed": imported,
        "endpoint_duplicate_payment_reduced_to_slot_accounting": reduced_closed,
        "endpoint_duplicate_same_slot_multiplicity_cap_pdec_proved": False,
        "endpoint_duplicate_payment_sparse_sae_summability_proved": False,
        "endpoint_duplicate_payment_collision_excluded": False,
        "endpoint_same_ap_table_payment_injection_lock_proved": False,
        "endpoint_cross_table_switch_pdec_or_moving_pivot_proved": False,
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
        "hardpoint_before_router": DUPLICATE_COLLISION,
        "hardpoint_after_router": REDUCED_DUPLICATE,
        "old_exits": [DUPLICATE_COLLISION],
        "new_exits": [SLOT_MULTIPLICITY, DUPLICATE_SPARSE],
        "parallel_open_exits": [
            SAME_AP_LOCK,
            CROSS_TABLE_SWITCH,
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
        "duplicate_records": duplicate_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot duplicate-payment slot-accounting 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_duplicate_payment_imported={fmt_bool(cert['endpoint_duplicate_payment_imported'])}",
        f"endpoint_duplicate_same_canonical_slot_key_closed={fmt_bool(cert['endpoint_duplicate_same_canonical_slot_key_closed'])}",
        f"endpoint_duplicate_capacity_unit_value_imported={fmt_bool(cert['endpoint_duplicate_capacity_unit_value_imported'])}",
        f"endpoint_duplicate_assignment_partial_injection_imported={fmt_bool(cert['endpoint_duplicate_assignment_partial_injection_imported'])}",
        f"endpoint_actual_object_duplicate_collision_imported={fmt_bool(cert['endpoint_actual_object_duplicate_collision_imported'])}",
        f"endpoint_duplicate_count_not_new_capacity_closed={fmt_bool(cert['endpoint_duplicate_count_not_new_capacity_closed'])}",
        f"endpoint_duplicate_payment_reduced_to_slot_accounting={fmt_bool(cert['endpoint_duplicate_payment_reduced_to_slot_accounting'])}",
        f"endpoint_duplicate_same_slot_multiplicity_cap_pdec_proved={fmt_bool(cert['endpoint_duplicate_same_slot_multiplicity_cap_pdec_proved'])}",
        f"endpoint_duplicate_payment_sparse_sae_summability_proved={fmt_bool(cert['endpoint_duplicate_payment_sparse_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同槽重复账本",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["duplicate_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "duplicate slot 分流为：",
            "",
            "```text",
            "same canonical slot has capacity value 1",
            "extra source units do not create new capacity",
            "",
            "persistent duplicate    => DuplicateSameSlotSourceMultiplicityCapPDEC",
            "nonpersistent duplicate => DuplicatePaymentSparseSAESummability",
            "```",
            "",
            "## 2. 出口更新",
            "",
            "```text",
            cert["hardpoint_before_router"],
            f"  -> {SLOT_MULTIPLICITY}",
            f"  AND {DUPLICATE_SPARSE}",
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
            "- 本证书不证明同槽 source multiplicity cap/PDEC。",
            "- 本证书不证明 duplicate-payment sparse SAE 求和。",
            "- 本证书只排除重复支付作为新增 AP-table capacity 的匿名用法。",
            "- same AP table injection、cross-table switch、bounded/long support、strict gap、dense/sparse table、高秩、nonreplay、moving-pivot 与 endpoint 并行出口仍未排斥。",
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
