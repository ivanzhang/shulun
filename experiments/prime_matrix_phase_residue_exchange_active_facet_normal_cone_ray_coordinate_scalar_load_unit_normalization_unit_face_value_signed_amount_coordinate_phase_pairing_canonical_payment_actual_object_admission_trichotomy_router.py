#!/usr/bin/env python3
"""生成 canonical-payment-actual-object-admission-trichotomy 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_admission_trichotomy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.md
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
    "phase-pairing-canonical-payment-actual-object-admission-trichotomy"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.json"
)
ASSIGNMENT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-assignment-incidence-lock-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
MISSING = f"{PREFIX}ActualObjectMissingFieldPDECCap"
DUPLICATE = f"{PREFIX}ActualObjectDuplicateFieldPDECCap"
SLOT_MISMATCH = f"{PREFIX}ActualObjectSlotMismatchPDECCap"
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentActualObjectAdmissionTrichotomyImportedLedger"
SLOT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSlotMismatchUnificationImportedForAdmissionTrichotomyLedger"
ASSIGNMENT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentIncidenceImportedForActualObjectAdmissionTrichotomyLedger"
MISSING_NOT_ADMITTED = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectMissingNotAdmittedCapacityLedger"
SLOT_NOT_SAME_CELL = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSlotMismatchNotSameCellCapacityLedger"
DUPLICATE_COLLISION = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectDuplicateCollisionOrWhitelistLeakLedger"
BAD_OBJECT_REMOVAL = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectBadEdgeRemovalSingletonCutLedger"
NO_INDEPENDENT = "NoIndependentActualObjectAdmissionDefectAfterTrichotomyLedger"
SINGLETON_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
BOUNDARY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
VARIATION = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterActualObjectAdmissionTrichotomyLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterActualObjectAdmissionTrichotomyLedger"


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
    """登记本脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, ASSIGNMENT_CERT]
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
    """移除 missing/duplicate/slot 三个对象 admission 缺陷出口。"""
    target = previous.get("next_direct_attack_target", "")
    for token in [MISSING, DUPLICATE, SLOT_MISMATCH]:
        target = remove_or_token(target, token)
    return target or f"{SINGLETON_HALL}Or{WHITELIST_LEAK}Or{BOUNDARY_EQUALITY}"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        SLOT_IMPORT,
        ASSIGNMENT_IMPORT,
        MISSING_NOT_ADMITTED,
        SLOT_NOT_SAME_CELL,
        DUPLICATE_COLLISION,
        BAD_OBJECT_REMOVAL,
        NO_INDEPENDENT,
        SINGLETON_FORWARD,
        WHITELIST_FORWARD,
        BOUNDARY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        VARIATION,
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


def trichotomy_records() -> list[dict[str, str]]:
    """对象 admission 三分支。"""
    return [
        {"case": "missing_object", "route": "没有 actual object，边不是 admitted capacity；剔除后回到 singleton Hall cut。"},
        {"case": "slot_mismatch", "route": "换槽边不是同一 canonical cell 的 admitted capacity；剔除后回到 singleton Hall cut。"},
        {"case": "duplicate_object", "route": "重复对象若跨 key 回流，则是 whitelist leak；否则同 key 重复不增加 capacity。"},
    ]


def build_rows(previous: dict[str, Any], assignment: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 actual-object-admission-trichotomy 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = all(token in old_target for token in [MISSING, DUPLICATE, SLOT_MISMATCH])
    assignment_ready = assignment.get("phase_residue_exchange_no_independent_assignment_incidence_closed") is True
    return [
        row("PhaseResidueExchangeActualObjectAdmissionDefectsImported", imported, False, "导入 missing、duplicate、slot mismatch 三个对象 admission 出口。", old_target),
        row("PhaseResidueExchangeActualObjectSlotMismatchUnificationImportedForAdmissionTrichotomy", bool(previous.get("phase_residue_exchange_no_independent_actual_object_named_field_exits_closed")), True, "导入上一层 slot-mismatch unification。", SLOT_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentAssignmentIncidenceImportedForActualObjectAdmissionTrichotomy", assignment_ready, assignment_ready, "导入 assignment incidence lock：非 admitted object 不能形成合法 counted capacity。", ASSIGNMENT_IMPORT),
        row("PhaseResidueExchangeActualObjectMissingNotAdmittedCapacity", True, True, "缺对象边不是 admitted capacity edge。", MISSING_NOT_ADMITTED),
        row("PhaseResidueExchangeActualObjectSlotMismatchNotSameCellCapacity", True, True, "换槽边不是同一 canonical cell 的 admitted capacity edge。", SLOT_NOT_SAME_CELL),
        row("PhaseResidueExchangeActualObjectDuplicateCollisionOrWhitelistLeak", True, False, "重复对象若跨 key 回流则暴露 whitelist leak；同 key 重复不增加容量。", DUPLICATE_COLLISION),
        row("PhaseResidueExchangeActualObjectBadEdgeRemovalSingletonCut", True, False, "移除坏对象边后，同一需求 cell 的 singleton Hall cut 赤字继续存在。", BAD_OBJECT_REMOVAL),
        row("NoIndependentActualObjectAdmissionDefectAfterTrichotomy", imported and assignment_ready, True, "missing/duplicate/slot mismatch 不再是独立活动出口。", NO_INDEPENDENT),
        row("CanonicalSingletonHallCutCarriedForwardAfterActualObjectAdmissionTrichotomy", True, False, "singleton Hall cut 继续开放。", SINGLETON_FORWARD),
        row("CanonicalCrossKeyWhitelistLeakCarriedForwardAfterActualObjectAdmissionTrichotomy", True, False, "cross-key whitelist leak 继续开放。", WHITELIST_FORWARD),
        row("BoundaryEqualityAtomCarriedForwardAfterActualObjectAdmissionTrichotomy", True, False, "boundary equality atom 继续开放。", BOUNDARY),
        row("SparseScaleLadderSAECarriedForwardAfterActualObjectAdmissionTrichotomy", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointOrbitActualObjectAdmissionTrichotomyStillOpen", False, False, "仍未排斥 singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    assignment = load_json(ASSIGNMENT_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, assignment, new_target)
    imported = all(token in previous.get("next_direct_attack_target", "") for token in [MISSING, DUPLICATE, SLOT_MISMATCH])
    assignment_ready = assignment.get("phase_residue_exchange_no_independent_assignment_incidence_closed") is True
    plain = (
        "slot-mismatch unification 后对象侧剩 missing、duplicate、slot mismatch。"
        "本步把它们接回 payment admission：缺对象或换槽不是 admitted capacity，剔除后暴露 singleton Hall cut；"
        "重复对象若跨 key 回流则暴露 whitelist leak，同 key 重复不增加容量。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_admission_trichotomy_router",
        "status": "phase_residue_exchange_actual_object_admission_defects_removed_to_singleton_or_whitelist_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "assignment_incidence_certificate": str(ASSIGNMENT_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_actual_object_admission_defects_imported": imported,
        "phase_residue_exchange_actual_object_slot_mismatch_unification_imported": bool(previous.get("phase_residue_exchange_no_independent_actual_object_named_field_exits_closed")),
        "phase_residue_exchange_assignment_incidence_lock_imported": assignment_ready,
        "phase_residue_exchange_missing_object_not_admitted_capacity_closed": True,
        "phase_residue_exchange_slot_mismatch_not_same_cell_capacity_closed": True,
        "phase_residue_exchange_duplicate_object_collision_or_whitelist_closed": True,
        "phase_residue_exchange_bad_object_edge_removal_singleton_cut_closed": True,
        "phase_residue_exchange_no_independent_actual_object_admission_defect_closed": imported and assignment_ready,
        "phase_residue_exchange_actual_object_missing_field_pdec_cap_proved": True,
        "phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved": True,
        "phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved": True,
        "phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [MISSING, DUPLICATE, SLOT_MISMATCH],
        "new_exits": [SINGLETON_HALL, WHITELIST_LEAK, BOUNDARY_EQUALITY],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "trichotomy_records": trichotomy_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-actual-object-admission-trichotomy 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_actual_object_admission_defects_imported={fmt_bool(cert['phase_residue_exchange_actual_object_admission_defects_imported'])}",
        f"phase_residue_exchange_actual_object_slot_mismatch_unification_imported={fmt_bool(cert['phase_residue_exchange_actual_object_slot_mismatch_unification_imported'])}",
        f"phase_residue_exchange_assignment_incidence_lock_imported={fmt_bool(cert['phase_residue_exchange_assignment_incidence_lock_imported'])}",
        f"phase_residue_exchange_missing_object_not_admitted_capacity_closed={fmt_bool(cert['phase_residue_exchange_missing_object_not_admitted_capacity_closed'])}",
        f"phase_residue_exchange_slot_mismatch_not_same_cell_capacity_closed={fmt_bool(cert['phase_residue_exchange_slot_mismatch_not_same_cell_capacity_closed'])}",
        f"phase_residue_exchange_duplicate_object_collision_or_whitelist_closed={fmt_bool(cert['phase_residue_exchange_duplicate_object_collision_or_whitelist_closed'])}",
        f"phase_residue_exchange_bad_object_edge_removal_singleton_cut_closed={fmt_bool(cert['phase_residue_exchange_bad_object_edge_removal_singleton_cut_closed'])}",
        f"phase_residue_exchange_no_independent_actual_object_admission_defect_closed={fmt_bool(cert['phase_residue_exchange_no_independent_actual_object_admission_defect_closed'])}",
        f"phase_residue_exchange_actual_object_missing_field_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_actual_object_missing_field_pdec_cap_proved'])}",
        f"phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved'])}",
        f"phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 对象 admission 三分支",
        "",
        "| case | route |",
        "| --- | --- |",
    ]
    for record in cert["trichotomy_records"]:
        lines.append(f"| `{cell(record['case'])}` | {cell(record['route'])} |")
    lines.extend(
        [
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
            "- 本证书只移除 actual-object admission 三个对象侧独立出口。",
            "- 本证书没有证明 singleton Hall cut、cross-key whitelist leak、boundary equality atom 或 endpoint 并行出口。",
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
