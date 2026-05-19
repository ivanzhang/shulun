#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-same-cell-slot-admission 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_same_cell_slot_admission_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.md
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
    "phase-pairing-canonical-payment-same-cell-slot-admission"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-key-label-admission-lock-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
SLOT_MISMATCH = f"{PREFIX}MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap"
ASSIGNMENT = f"{PREFIX}MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap"
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSameCellSlotAdmissionImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
ASSIGNMENT_FORWARD = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentSameCellSlotAdmissionLedger"

KEY_LABEL_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyLabelAdmissionImportedForSameCellSlotAdmissionLedger"
SAME_CELL_CLAIM = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSameCellClaimRequiresSlotVectorLedger"
SLOT_VECTOR_EQUALITY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSlotVectorEqualityGateLedger"
MISMATCH_NOT_EDGE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSlotMismatchNotSameCellEdgeLedger"
COUNTED_MISMATCH_ASSIGNMENT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCountedSlotMismatchAssignmentIncidenceLedger"
UNCOUNTED_MISMATCH_SINGLETON = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentUncountedSlotMismatchSingletonCutLedger"
NO_ANON = "NoIndependentMissingUnitCoordinateSlotMismatchAfterSameCellAdmissionLedger"
SINGLETON_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterSameCellSlotAdmissionLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterSameCellSlotAdmissionLedger"


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
    """登记本脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def remove_or_token(text: str, token: str) -> str:
    """从长 OR 目标中移除一个 token 的全部出现。"""
    updated = text
    while f"{token}Or" in updated:
        updated = updated.replace(f"{token}Or", "")
    while f"Or{token}" in updated:
        updated = updated.replace(f"Or{token}", "")
    updated = updated.replace(token, "")
    return updated or f"{ASSIGNMENT}Or{SINGLETON_HALL}"


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    return remove_or_token(previous.get("next_direct_attack_target", ""), SLOT_MISMATCH)


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PREDICATE,
        CAPACITY_INTEGRALITY,
        ASSIGNMENT_FORWARD,
        BOUNDARY_EQUALITY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        KEY_LABEL_IMPORT,
        SAME_CELL_CLAIM,
        SLOT_VECTOR_EQUALITY,
        MISMATCH_NOT_EDGE,
        COUNTED_MISMATCH_ASSIGNMENT,
        UNCOUNTED_MISMATCH_SINGLETON,
        NO_ANON,
        SINGLETON_FORWARD,
        WHITELIST_FORWARD,
        SPARSE,
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


def admission_records() -> list[dict[str, str]]:
    """给出 same-cell slot admission 的字段。"""
    return [
        {
            "field": "same_cell_claim",
            "meaning": "声称补偿同一 canonical missing unit cell 必须给出同一 slot vector。",
        },
        {
            "field": "slot_vector_equality",
            "meaning": "source atom、occurrence、CRT coordinate、congruence、phase endpoint、signed amount 均需逐槽相等。",
        },
        {
            "field": "mismatch_not_edge",
            "meaning": "槽位不同的候选边不是该 missing cell 的 admitted same-cell edge。",
        },
        {
            "field": "counted_mismatch",
            "meaning": "若槽位不一致仍被计入容量，就是 unit-capacity assignment incidence 缺陷。",
        },
        {
            "field": "uncounted_mismatch",
            "meaning": "若不计入容量，则单点缺口仍是 singleton Hall cut。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 same-cell-slot-admission 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported_count = old_target.count(SLOT_MISMATCH)
    key_label_ready = previous.get("phase_residue_exchange_no_independent_noncanonical_label_residue_closed") is True
    return [
        row("PhaseResidueExchangeMissingUnitCoordinateSlotMismatchImported", imported_count > 0, False, "导入 missing-unit coordinate slot mismatch 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterSameCellSlotAdmission", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterSameCellSlotAdmission", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterSameCellSlotAdmission", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT_FORWARD),
        row("BoundaryEqualityAtomCarriedForwardAfterSameCellSlotAdmission", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterSameCellSlotAdmission", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterSameCellSlotAdmission", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterSameCellSlotAdmission", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterSameCellSlotAdmission", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterSameCellSlotAdmission", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterSameCellSlotAdmission", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentKeyLabelAdmissionImportedForSameCellSlotAdmission", key_label_ready, key_label_ready, "导入 key-label admission：只有 admitted edge 能参与 payment graph。", KEY_LABEL_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentSameCellClaimRequiresSlotVector", True, True, "同 cell 补偿要求同一 slot vector。", SAME_CELL_CLAIM),
        row("PhaseResidueExchangeCanonicalPaymentSlotVectorEqualityGate", True, True, "所有 missing-unit coordinate slots 必须逐槽相等。", SLOT_VECTOR_EQUALITY),
        row("PhaseResidueExchangeCanonicalPaymentSlotMismatchNotSameCellEdge", True, True, "槽位不一致的候选边不是 admitted same-cell edge。", MISMATCH_NOT_EDGE),
        row("PhaseResidueExchangeCanonicalPaymentCountedSlotMismatchAssignmentIncidence", True, False, "若错槽边仍被计入容量，则回流 assignment-incidence PDEC/cap。", COUNTED_MISMATCH_ASSIGNMENT),
        row("PhaseResidueExchangeCanonicalPaymentUncountedSlotMismatchSingletonCut", True, False, "若错槽边不计入容量，则单点 Hall cut 赤字继续存在。", UNCOUNTED_MISMATCH_SINGLETON),
        row("NoIndependentMissingUnitCoordinateSlotMismatchAfterSameCellAdmission", True, True, "slot mismatch 不再是独立活动出口。", NO_ANON),
        row("PhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterSameCellSlotAdmission", True, False, "singleton Hall cut 仍未排斥。", SINGLETON_FORWARD),
        row("PhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterSameCellSlotAdmission", True, False, "cross-key whitelist leak 仍未排斥。", WHITELIST_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterSameCellSlotAdmission", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentSameCellSlotAdmissionStillOpen", False, False, "仍未排斥 singleton Hall cut、assignment incidence、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    old_target = previous.get("next_direct_attack_target", "")
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "key-label-admission 层仍保留 missing-unit coordinate slot mismatch。"
        "本步把 same-cell compensation 的 admitted edge 条件显式化：同一 missing unit cell 必须逐槽相等。"
        "槽位不一致的候选边不能补该 cell；若仍计入容量，则是 assignment-incidence 缺陷；"
        "若不计入容量，则 singleton Hall cut 继续暴露。因此 slot mismatch 不再是独立活动出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_same_cell_slot_admission_router",
        "status": "phase_residue_exchange_missing_unit_slot_mismatch_removed_singleton_assignment_whitelist_and_parallel_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": old_target,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_missing_unit_coordinate_slot_mismatch_imported": SLOT_MISMATCH in old_target,
        "phase_residue_exchange_missing_unit_coordinate_slot_mismatch_occurrences_removed": old_target.count(SLOT_MISMATCH),
        "phase_residue_exchange_key_label_admission_lock_imported": bool(previous.get("phase_residue_exchange_no_independent_noncanonical_label_residue_closed")),
        "phase_residue_exchange_same_cell_claim_requires_slot_vector_closed": True,
        "phase_residue_exchange_slot_vector_equality_gate_closed": True,
        "phase_residue_exchange_slot_mismatch_not_same_cell_edge_closed": True,
        "phase_residue_exchange_counted_slot_mismatch_assignment_incidence_closed": True,
        "phase_residue_exchange_uncounted_slot_mismatch_singleton_cut_closed": True,
        "phase_residue_exchange_no_independent_slot_mismatch_closed": True,
        "phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved": True,
        "phase_residue_exchange_unit_capacity_assignment_incidence_proved": False,
        "phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_unit_payment_graph_closed": False,
        "phase_residue_exchange_canonical_payment_return_whitelist_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": False,
        "phase_residue_exchange_capacity_value_unit_integrality_proved": False,
        "linear_witness_existence_proved": False,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_carried_forward": True,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_carried_forward": True,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [SLOT_MISMATCH],
        "new_exits": [ASSIGNMENT, SINGLETON_HALL, WHITELIST_LEAK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "admission_records": admission_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-same-cell-slot-admission 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_missing_unit_coordinate_slot_mismatch_imported={fmt_bool(cert['phase_residue_exchange_missing_unit_coordinate_slot_mismatch_imported'])}",
        f"phase_residue_exchange_missing_unit_coordinate_slot_mismatch_occurrences_removed={cert['phase_residue_exchange_missing_unit_coordinate_slot_mismatch_occurrences_removed']}",
        f"phase_residue_exchange_key_label_admission_lock_imported={fmt_bool(cert['phase_residue_exchange_key_label_admission_lock_imported'])}",
        f"phase_residue_exchange_same_cell_claim_requires_slot_vector_closed={fmt_bool(cert['phase_residue_exchange_same_cell_claim_requires_slot_vector_closed'])}",
        f"phase_residue_exchange_slot_vector_equality_gate_closed={fmt_bool(cert['phase_residue_exchange_slot_vector_equality_gate_closed'])}",
        f"phase_residue_exchange_slot_mismatch_not_same_cell_edge_closed={fmt_bool(cert['phase_residue_exchange_slot_mismatch_not_same_cell_edge_closed'])}",
        f"phase_residue_exchange_counted_slot_mismatch_assignment_incidence_closed={fmt_bool(cert['phase_residue_exchange_counted_slot_mismatch_assignment_incidence_closed'])}",
        f"phase_residue_exchange_uncounted_slot_mismatch_singleton_cut_closed={fmt_bool(cert['phase_residue_exchange_uncounted_slot_mismatch_singleton_cut_closed'])}",
        f"phase_residue_exchange_no_independent_slot_mismatch_closed={fmt_bool(cert['phase_residue_exchange_no_independent_slot_mismatch_closed'])}",
        f"phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. same-cell slot admission 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["admission_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "same-cell-slot-admission 路由为：",
            "",
            "```text",
            "if compensator claims the same canonical missing unit cell:",
            "  require equal slot_vector(source, occurrence, CRT, congruence, endpoint, signed_amount)",
            "",
            "if slot_vector differs:",
            "  edge is not an admitted same-cell payment",
            "  if it is counted as capacity:",
            "    MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap",
            "  else:",
            "    MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap",
            "```",
            "",
            "## 2. 新硬点",
            "",
            "```text",
            cert["previous_direct_attack_target"],
            "  -> " + reduced_target(cert["next_direct_attack_target"]),
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
            "- 本证书只移除 missing-unit coordinate slot mismatch 作为独立活动出口；错槽边要么不入图，要么回流 assignment-incidence 缺陷。",
            "- 本证书没有证明 unit-capacity assignment incidence PDEC/cap。",
            "- 本证书没有证明 canonical singleton Hall cut defect PDEC/cap。",
            "- 本证书没有证明 canonical cross-key return whitelist leak PDEC/cap。",
            "- 本证书没有证明 canonical payment graph 全局闭合，也没有证明 return whitelist。",
            "- 本证书没有证明 capacity-value unit-integrality 或 actual-object incidence predicate。",
            "- 本证书没有排斥 boundary equality atom，也没有证明 endpoint 并行出口或 sparse SAE 求和。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
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
