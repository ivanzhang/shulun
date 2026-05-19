#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing missing-unit-coordinate-lock 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_missing_unit_coordinate_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.md
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
    "phase-pairing-missing-unit-coordinate-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-unit-defect-witness-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}MaterializedCircuitMissingCapacityUnitWitnessPDECCap"
SLOT_MISMATCH_TARGET = f"{PREFIX}MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap"
CANONICAL_TARGET = f"{PREFIX}MaterializedCircuitCanonicalMissingCapacityUnitWitnessPDECCap"
NEW_TARGET = f"{SLOT_MISMATCH_TARGET}Or{CANONICAL_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitWitnessImportedForCoordinateLockLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterMissingUnitCoordinateLockLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterMissingUnitCoordinateLockLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterMissingUnitCoordinateLockLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterMissingUnitCoordinateLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterMissingUnitCoordinateLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterMissingUnitCoordinateLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterMissingUnitCoordinateLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterMissingUnitCoordinateLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterMissingUnitCoordinateLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterMissingUnitCoordinateLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterMissingUnitCoordinateLockLedger"

WITNESS_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingCapacityUnitWitnessImportedLedger"
DEMAND_MEMBERSHIP = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitDemandMembershipLedger"
CAPACITY_EXCLUSION = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitCapacityExclusionLedger"
SOURCE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitSourceAtomSlotLedger"
OCCURRENCE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitOccurrenceSlotLedger"
CRT_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitCRTCoordinateSlotLedger"
CONGRUENCE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitCanonicalCongruenceSlotLedger"
PHASE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitPhaseEndpointSlotLedger"
SIGNED_AMOUNT_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitSignedAmountSlotLedger"
CANONICAL_HASH = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitCanonicalHashLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitCoordinateSlotMismatchReturnLedger"
CANONICAL_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingCapacityUnitWitnessPacketLedger"
NO_MOVING_WITNESS = "NoAnonymousMovingMissingUnitWitnessAfterCoordinateLockLedger"


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


def next_target(previous: dict[str, Any]) -> str:
    """把 missing unit witness 硬点替换为槽位不一致或 canonical witness。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PREDICATE,
        CAPACITY_INTEGRALITY,
        ASSIGNMENT,
        BOUNDARY_EQUALITY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        WITNESS_IMPORT,
        DEMAND_MEMBERSHIP,
        CAPACITY_EXCLUSION,
        SOURCE_SLOT,
        OCCURRENCE_SLOT,
        CRT_SLOT,
        CONGRUENCE_SLOT,
        PHASE_SLOT,
        SIGNED_AMOUNT_SLOT,
        CANONICAL_HASH,
        SLOT_MISMATCH,
        CANONICAL_PACKET,
        NO_MOVING_WITNESS,
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


def coordinate_records() -> list[dict[str, str]]:
    """给出 canonical missing unit witness 的坐标字段。"""
    return [
        {"slot": "demand_membership", "meaning": "u* 必须满足 u* in U_A。"},
        {"slot": "capacity_exclusion", "meaning": "u* 必须满足 u* notin U_C。"},
        {"slot": "source_atom", "meaning": "u* 的 source atom 必须等于 actual-object predicate 链中的 source atom。"},
        {"slot": "occurrence_unit", "meaning": "u* 的 occurrence unit 必须落在同一 signed occurrence incidence cell。"},
        {"slot": "crt_coordinate", "meaning": "u* 的 CRT coordinate 必须是 occurrence unit 的 primitive witness coordinate。"},
        {"slot": "canonical_congruence", "meaning": "canonical congruence equation 必须在该 CRT coordinate 上成立。"},
        {"slot": "phase_endpoint", "meaning": "phase-residue evaluation 必须给出同一端点对。"},
        {"slot": "signed_amount", "meaning": "signed amount 槽位必须继承 price-one signed unit。"},
        {"slot": "canonical_hash", "meaning": "所有槽位合成唯一 canonical missing-unit key。"},
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 missing-unit-coordinate-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeMissingUnitWitnessImportedForCoordinateLock",
            imported,
            False,
            "上一层已把单位负缺口压成 assignment incidence 或 missing capacity unit witness。",
            old_target or OLD_TARGET,
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterMissingUnitCoordinateLock", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterMissingUnitCoordinateLock", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterMissingUnitCoordinateLock", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("BoundaryEqualityAtomCarriedForwardAfterMissingUnitCoordinateLock", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterMissingUnitCoordinateLock", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterMissingUnitCoordinateLock", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterMissingUnitCoordinateLock", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterMissingUnitCoordinateLock", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterMissingUnitCoordinateLock", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterMissingUnitCoordinateLock", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeMissingCapacityUnitWitnessImported", imported, False, "导入 u* in U_A \\ U_C 的缺失单位见证。", WITNESS_IMPORT),
        row("PhaseResidueExchangeMissingUnitDemandMembership", True, True, "u* 属于需求单位集合 U_A。", DEMAND_MEMBERSHIP),
        row("PhaseResidueExchangeMissingUnitCapacityExclusion", True, True, "u* 不属于容量已接纳单位集合 U_C。", CAPACITY_EXCLUSION),
        row("PhaseResidueExchangeMissingUnitSourceAtomSlot", True, False, "u* 必须绑定同一 source atom。", SOURCE_SLOT),
        row("PhaseResidueExchangeMissingUnitOccurrenceSlot", True, False, "u* 必须绑定同一 occurrence unit。", OCCURRENCE_SLOT),
        row("PhaseResidueExchangeMissingUnitCRTCoordinateSlot", True, False, "u* 必须绑定同一 CRT coordinate。", CRT_SLOT),
        row("PhaseResidueExchangeMissingUnitCanonicalCongruenceSlot", True, False, "u* 必须满足 canonical congruence equation。", CONGRUENCE_SLOT),
        row("PhaseResidueExchangeMissingUnitPhaseEndpointSlot", True, False, "u* 必须绑定同一 phase endpoint。", PHASE_SLOT),
        row("PhaseResidueExchangeMissingUnitSignedAmountSlot", True, False, "u* 必须绑定 price-one signed amount unit。", SIGNED_AMOUNT_SLOT),
        row("PhaseResidueExchangeMissingUnitCanonicalHash", True, False, "所有槽位合成唯一 canonical missing-unit key。", CANONICAL_HASH),
        row("PhaseResidueExchangeMissingUnitCoordinateSlotMismatchReturn", True, False, "若任一槽缺失或换槽，则回流 coordinate slot mismatch PDEC/cap。", SLOT_MISMATCH),
        row("PhaseResidueExchangeCanonicalMissingCapacityUnitWitnessPacket", True, False, "若槽位一致，则剩余为 canonical missing capacity unit witness。", CANONICAL_PACKET),
        row("NoAnonymousMovingMissingUnitWitnessAfterCoordinateLock", True, True, "missing unit witness 不再能移动、换槽或匿名保留。", NO_MOVING_WITNESS),
        row("SparseScaleLadderSAECarriedForwardAfterMissingUnitCoordinateLock", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeMissingUnitCoordinateLockStillOpen", False, False, "仍未排斥 actual-object predicate、capacity integrality、assignment incidence、canonical missing unit witness、boundary equality 或 parallel outlets。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 canonical missing unit witness 或相关命名出口。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "unit-defect-witness 层已给出缺失单位 u* in U_A\\U_C。"
        "本步把 u* 锁成同一 actual object 的 canonical coordinate tuple："
        "需求成员、容量排除、source atom、occurrence unit、CRT coordinate、canonical congruence、"
        "phase endpoint 与 signed amount 槽位必须同时一致。若任一槽缺失或换槽，"
        "就是 coordinate slot mismatch PDEC/cap；若全部一致，剩余为 canonical missing capacity unit witness。"
        "因此 missing-unit witness 不再能作为可移动或可换槽对象保留。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_missing_unit_coordinate_lock_router",
        "status": "phase_residue_exchange_missing_unit_witness_reduced_to_slot_mismatch_or_canonical_missing_unit_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_missing_capacity_unit_witness_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_missing_unit_demand_membership_closed": True,
        "phase_residue_exchange_missing_unit_capacity_exclusion_closed": True,
        "phase_residue_exchange_missing_unit_coordinate_lock_schema_closed": True,
        "phase_residue_exchange_no_moving_missing_unit_witness_closed": True,
        "phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_missing_capacity_unit_witness_pdec_cap_proved": False,
        "phase_residue_exchange_unit_capacity_assignment_incidence_proved": False,
        "phase_residue_exchange_capacity_value_unit_integrality_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": False,
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
        "old_exit": OLD_TARGET,
        "new_exits": [SLOT_MISMATCH_TARGET, CANONICAL_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "coordinate_records": coordinate_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange phase-pairing missing-unit-coordinate-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_missing_capacity_unit_witness_imported={fmt_bool(cert['phase_residue_exchange_missing_capacity_unit_witness_imported'])}",
        f"phase_residue_exchange_missing_unit_demand_membership_closed={fmt_bool(cert['phase_residue_exchange_missing_unit_demand_membership_closed'])}",
        f"phase_residue_exchange_missing_unit_capacity_exclusion_closed={fmt_bool(cert['phase_residue_exchange_missing_unit_capacity_exclusion_closed'])}",
        f"phase_residue_exchange_missing_unit_coordinate_lock_schema_closed={fmt_bool(cert['phase_residue_exchange_missing_unit_coordinate_lock_schema_closed'])}",
        f"phase_residue_exchange_no_moving_missing_unit_witness_closed={fmt_bool(cert['phase_residue_exchange_no_moving_missing_unit_witness_closed'])}",
        f"phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_missing_capacity_unit_witness_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_missing_capacity_unit_witness_pdec_cap_proved'])}",
        f"phase_residue_exchange_unit_capacity_assignment_incidence_proved={fmt_bool(cert['phase_residue_exchange_unit_capacity_assignment_incidence_proved'])}",
        f"phase_residue_exchange_capacity_value_unit_integrality_proved={fmt_bool(cert['phase_residue_exchange_capacity_value_unit_integrality_proved'])}",
        f"phase_residue_exchange_boundary_equality_atom_exclusion_proved={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_exclusion_proved'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 缺失单位输入",
        "",
        "```text",
        "u* in U_A",
        "u* notin U_C",
        "same_actual_object=true",
        "```",
        "",
        "## 2. canonical 坐标锁",
        "",
        "| slot | meaning |",
        "| --- | --- |",
    ]
    for record in cert["coordinate_records"]:
        lines.append(f"| `{cell(record['slot'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "缺失单位路由为：",
            "",
            "```text",
            "u* in U_A \\ U_C",
            "  -> if any actual-object coordinate slot is missing or switched:",
            "       MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap",
            "  -> otherwise canonicalize by the coordinate tuple:",
            "       MaterializedCircuitCanonicalMissingCapacityUnitWitnessPDECCap",
            "anonymous_moving_missing_unit_witness=0",
            "```",
            "",
            "## 3. 新硬点",
            "",
            "```text",
            cert["previous_direct_attack_target"],
            "  -> " + reduced_target(cert["next_direct_attack_target"]),
            "```",
            "",
            "## 4. 判定表",
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
            "## 5. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书没有证明 missing-unit coordinate slot mismatch PDEC/cap。",
            "- 本证书没有排斥 canonical missing capacity unit witness PDEC/cap。",
            "- 本证书没有证明 unit-capacity assignment incidence PDEC/cap。",
            "- 本证书没有证明 capacity-value unit-integrality PDEC/cap。",
            "- 本证书没有排斥 boundary equality atom。",
            "- 本证书没有证明 actual-object incidence predicate PDEC/cap。",
            "- 本证书没有证明 source-atom multiplicity-cap、endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 7. 依赖哈希",
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
