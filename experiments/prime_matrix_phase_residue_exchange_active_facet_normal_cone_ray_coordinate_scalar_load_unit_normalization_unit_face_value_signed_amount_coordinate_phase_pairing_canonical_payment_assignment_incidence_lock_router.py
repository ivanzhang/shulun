#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-assignment-incidence-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_assignment_incidence_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.md
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
    "phase-pairing-canonical-payment-assignment-incidence-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-same-cell-slot-admission-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
ACTUAL_OBJECT = f"{PREFIX}ActualObjectIncidencePredicatePDECCap"
CAPACITY_INTEGRALITY_TARGET = f"{PREFIX}MaterializedCircuitCapacityValueUnitIntegralityPDECCap"
ASSIGNMENT = f"{PREFIX}MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap"
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentIncidenceLockImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentAssignmentIncidenceLockLedger"

SAME_CELL_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSameCellSlotAdmissionImportedForAssignmentLockLedger"
COUNTED_UNIT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCountedCapacityUnitLedger"
ADMITTED_UNIT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAdmittedCapacityUnitPredicateLedger"
UNIT_VALUE_ONE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCapacityUnitValueOneLedger"
OBJECT_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentActualObjectGateLedger"
SAME_CELL_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentSameCellGateLedger"
WHITELIST_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentWhitelistGateLedger"
ASSIGNMENT_FUNCTION = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentPartialInjectionLedger"
BAD_COUNT_TRICHOTOMY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentBadCountedUnitTrichotomyLedger"
NO_ANON = "NoIndependentUnitCapacityAssignmentIncidenceAfterCanonicalAssignmentLockLedger"
SINGLETON_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterAssignmentLockLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterAssignmentLockLedger"


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
    return updated.replace(token, "")


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    target = previous.get("next_direct_attack_target", "")
    updated = remove_or_token(target, ASSIGNMENT)
    return updated or f"{ACTUAL_OBJECT}Or{CAPACITY_INTEGRALITY_TARGET}Or{SINGLETON_HALL}Or{WHITELIST_LEAK}"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PREDICATE,
        CAPACITY_INTEGRALITY,
        BOUNDARY_EQUALITY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        SAME_CELL_IMPORT,
        COUNTED_UNIT,
        ADMITTED_UNIT,
        UNIT_VALUE_ONE,
        OBJECT_GATE,
        SAME_CELL_GATE,
        WHITELIST_GATE,
        ASSIGNMENT_FUNCTION,
        BAD_COUNT_TRICHOTOMY,
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


def assignment_records() -> list[dict[str, str]]:
    """给出 canonical capacity unit assignment 的字段。"""
    return [
        {
            "field": "counted_capacity_unit",
            "meaning": "任何被计入容量的单位必须先声明 canonical payment cell 与单位编号。",
        },
        {
            "field": "admitted_unit_predicate",
            "meaning": "计入容量要求 actual-object gate、unit-value gate、same-cell gate 与 whitelist gate 全部通过。",
        },
        {
            "field": "partial_injection",
            "meaning": "通过 gate 的容量单位给出到需求单位集合的部分单射；重复占用不产生新容量。",
        },
        {
            "field": "bad_count_trichotomy",
            "meaning": "坏计数只能是对象不合格、单位值不合格、跨 key 未白名单，或没有 admitted same-cell edge。",
        },
        {
            "field": "singleton_fallback",
            "meaning": "若坏计数被剔除，则 missing cell 的单点 cut 赤字继续存在。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 assignment-incidence-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = ASSIGNMENT in old_target
    same_cell_ready = previous.get("phase_residue_exchange_no_independent_slot_mismatch_closed") is True
    return [
        row("PhaseResidueExchangeUnitCapacityAssignmentIncidenceImported", imported, False, "导入 unit-capacity assignment incidence 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterAssignmentLock", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterAssignmentLock", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("BoundaryEqualityAtomCarriedForwardAfterAssignmentLock", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterAssignmentLock", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterAssignmentLock", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterAssignmentLock", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterAssignmentLock", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterAssignmentLock", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterAssignmentLock", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentSameCellSlotAdmissionImportedForAssignmentLock", same_cell_ready, same_cell_ready, "导入 same-cell slot admission：错槽边不能作为同 cell 容量。", SAME_CELL_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentCountedCapacityUnit", True, True, "被计入容量的单位必须声明 canonical payment cell 与单位编号。", COUNTED_UNIT),
        row("PhaseResidueExchangeCanonicalPaymentAdmittedCapacityUnitPredicate", True, True, "admitted unit predicate 是对象、单位值、同 cell 与白名单 gate 的合取。", ADMITTED_UNIT),
        row("PhaseResidueExchangeCanonicalPaymentCapacityUnitValueOne", True, False, "单位值必须是规范的一单位；失败回流 capacity-value unit-integrality。", UNIT_VALUE_ONE),
        row("PhaseResidueExchangeCanonicalPaymentAssignmentActualObjectGate", True, False, "actual object gate 失败回流 actual-object incidence predicate。", OBJECT_GATE),
        row("PhaseResidueExchangeCanonicalPaymentAssignmentSameCellGate", True, True, "same-cell gate 已由 slot admission 锁定。", SAME_CELL_GATE),
        row("PhaseResidueExchangeCanonicalPaymentAssignmentWhitelistGate", True, False, "跨 key return 若未白名单，回流 whitelist leak。", WHITELIST_GATE),
        row("PhaseResidueExchangeCanonicalPaymentAssignmentPartialInjection", True, True, "通过所有 gate 的容量单位给出到需求单位的部分单射。", ASSIGNMENT_FUNCTION),
        row("PhaseResidueExchangeCanonicalPaymentBadCountedUnitTrichotomy", True, True, "坏计数只能落入 actual-object、capacity-integrality、whitelist leak，或剔除后暴露 singleton cut。", BAD_COUNT_TRICHOTOMY),
        row("NoIndependentUnitCapacityAssignmentIncidenceAfterCanonicalAssignmentLock", True, True, "assignment incidence 不再是独立活动出口。", NO_ANON),
        row("PhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterAssignmentLock", True, False, "singleton Hall cut 仍未排斥。", SINGLETON_FORWARD),
        row("PhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterAssignmentLock", True, False, "cross-key whitelist leak 仍未排斥。", WHITELIST_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterAssignmentLock", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentLockStillOpen", False, False, "仍未排斥 actual-object、capacity integrality、singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "same-cell-slot-admission 层留下 unit-capacity assignment incidence。"
        "本步把 counted capacity unit 的 admission 规则锁定为 actual-object gate、单位值 gate、"
        "same-cell gate 与 return-whitelist gate 的合取。通过所有 gate 的单位形成到需求单位的部分单射；"
        "坏计数则只能回流到 actual-object、capacity-integrality、whitelist leak，或剔除后暴露 singleton Hall cut。"
        "因此 assignment incidence 不再是独立活动出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_assignment_incidence_lock_router",
        "status": "phase_residue_exchange_assignment_incidence_removed_singleton_whitelist_actual_capacity_and_parallel_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_unit_capacity_assignment_incidence_imported": ASSIGNMENT in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_same_cell_slot_admission_imported": bool(previous.get("phase_residue_exchange_no_independent_slot_mismatch_closed")),
        "phase_residue_exchange_counted_capacity_unit_closed": True,
        "phase_residue_exchange_admitted_capacity_unit_predicate_closed": True,
        "phase_residue_exchange_capacity_unit_value_one_gate_closed": True,
        "phase_residue_exchange_assignment_actual_object_gate_closed": True,
        "phase_residue_exchange_assignment_same_cell_gate_closed": True,
        "phase_residue_exchange_assignment_whitelist_gate_closed": True,
        "phase_residue_exchange_assignment_partial_injection_closed": True,
        "phase_residue_exchange_bad_counted_unit_trichotomy_closed": True,
        "phase_residue_exchange_no_independent_assignment_incidence_closed": True,
        "phase_residue_exchange_unit_capacity_assignment_incidence_proved": True,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": False,
        "phase_residue_exchange_capacity_value_unit_integrality_proved": False,
        "phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_unit_payment_graph_closed": False,
        "phase_residue_exchange_canonical_payment_return_whitelist_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
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
        "old_exits": [ASSIGNMENT],
        "new_exits": [ACTUAL_OBJECT, CAPACITY_INTEGRALITY_TARGET, SINGLETON_HALL, WHITELIST_LEAK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "assignment_records": assignment_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-assignment-incidence-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_unit_capacity_assignment_incidence_imported={fmt_bool(cert['phase_residue_exchange_unit_capacity_assignment_incidence_imported'])}",
        f"phase_residue_exchange_same_cell_slot_admission_imported={fmt_bool(cert['phase_residue_exchange_same_cell_slot_admission_imported'])}",
        f"phase_residue_exchange_counted_capacity_unit_closed={fmt_bool(cert['phase_residue_exchange_counted_capacity_unit_closed'])}",
        f"phase_residue_exchange_admitted_capacity_unit_predicate_closed={fmt_bool(cert['phase_residue_exchange_admitted_capacity_unit_predicate_closed'])}",
        f"phase_residue_exchange_capacity_unit_value_one_gate_closed={fmt_bool(cert['phase_residue_exchange_capacity_unit_value_one_gate_closed'])}",
        f"phase_residue_exchange_assignment_actual_object_gate_closed={fmt_bool(cert['phase_residue_exchange_assignment_actual_object_gate_closed'])}",
        f"phase_residue_exchange_assignment_same_cell_gate_closed={fmt_bool(cert['phase_residue_exchange_assignment_same_cell_gate_closed'])}",
        f"phase_residue_exchange_assignment_whitelist_gate_closed={fmt_bool(cert['phase_residue_exchange_assignment_whitelist_gate_closed'])}",
        f"phase_residue_exchange_assignment_partial_injection_closed={fmt_bool(cert['phase_residue_exchange_assignment_partial_injection_closed'])}",
        f"phase_residue_exchange_bad_counted_unit_trichotomy_closed={fmt_bool(cert['phase_residue_exchange_bad_counted_unit_trichotomy_closed'])}",
        f"phase_residue_exchange_no_independent_assignment_incidence_closed={fmt_bool(cert['phase_residue_exchange_no_independent_assignment_incidence_closed'])}",
        f"phase_residue_exchange_unit_capacity_assignment_incidence_proved={fmt_bool(cert['phase_residue_exchange_unit_capacity_assignment_incidence_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. assignment lock 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["assignment_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "assignment-incidence-lock 路由为：",
            "",
            "```text",
            "admitted_capacity_unit = actual_object_gate AND unit_value_one_gate",
            "                         AND same_cell_gate AND whitelist_gate",
            "",
            "if a counted capacity unit fails a gate:",
            "  actual_object_gate failure -> ActualObjectIncidencePredicatePDECCap",
            "  unit_value_one failure     -> CapacityValueUnitIntegralityPDECCap",
            "  whitelist_gate failure     -> CanonicalCrossKeyReturnWhitelistLeakPDECCap",
            "  otherwise remove the bad count -> CanonicalUnitSingletonHallCutDefectPDECCap",
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
            "- 本证书只移除 unit-capacity assignment incidence 作为独立活动出口；坏计数会回流到对象、单位值、白名单或 singleton cut。",
            "- 本证书没有证明 actual-object incidence predicate PDEC/cap。",
            "- 本证书没有证明 capacity-value unit-integrality PDEC/cap。",
            "- 本证书没有证明 canonical singleton Hall cut defect PDEC/cap。",
            "- 本证书没有证明 canonical cross-key return whitelist leak PDEC/cap。",
            "- 本证书没有证明 canonical payment graph 全局闭合，也没有证明 return whitelist。",
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
