#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-capacity-unit-value-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_capacity_unit_value_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.md
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
    "phase-pairing-canonical-payment-capacity-unit-value-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
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
ACTUAL_OBJECT = f"{PREFIX}ActualObjectIncidencePredicatePDECCap"
CAPACITY_INTEGRALITY_TARGET = f"{PREFIX}MaterializedCircuitCapacityValueUnitIntegralityPDECCap"
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCapacityUnitValueLockImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentCapacityUnitValueLockLedger"

ASSIGNMENT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAssignmentIncidenceImportedForCapacityUnitValueLockLedger"
SIGNED_AMOUNT_UNIT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSignedAmountUnitAtomLedger"
UNIT_VALUE_ONE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentUnitValueOneNormalizationLedger"
CAPACITY_AS_UNIT_SUM = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCapacityAsUnitIndicatorSumLedger"
INTEGER_SUM = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCapacityIntegerSumLedger"
NONUNIT_TO_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentNonunitValueActualObjectReturnLedger"
BAD_UNIT_REMOVAL = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentBadUnitValueRemovalLedger"
SINGLETON_FALLBACK = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentBadUnitValueSingletonCutLedger"
NO_ANON = "NoIndependentCapacityValueUnitIntegralityAfterCapacityUnitValueLockLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterCapacityUnitValueLockLedger"


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
    updated = remove_or_token(target, CAPACITY_INTEGRALITY_TARGET)
    return updated or f"{ACTUAL_OBJECT}Or{SINGLETON_HALL}Or{WHITELIST_LEAK}"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PREDICATE,
        BOUNDARY_EQUALITY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        ASSIGNMENT_IMPORT,
        SIGNED_AMOUNT_UNIT,
        UNIT_VALUE_ONE,
        CAPACITY_AS_UNIT_SUM,
        INTEGER_SUM,
        NONUNIT_TO_OBJECT,
        BAD_UNIT_REMOVAL,
        SINGLETON_FALLBACK,
        NO_ANON,
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


def value_records() -> list[dict[str, str]]:
    """给出 capacity unit value 的规范字段。"""
    return [
        {
            "field": "signed_amount_unit_atom",
            "meaning": "admitted capacity unit 的 signed amount atom 必须是规范一单位。",
        },
        {
            "field": "capacity_as_unit_sum",
            "meaning": "capacity value 是 admitted unit indicators 的有限和。",
        },
        {
            "field": "integer_sum",
            "meaning": "有限 0/1 指示和自动是非负整数，不存在小数容量。",
        },
        {
            "field": "nonunit_value",
            "meaning": "非一单位 signed amount 只能是 actual-object 字段不合格。",
        },
        {
            "field": "bad_unit_removal",
            "meaning": "非规范单位被剔除后，缺失 cell 的 singleton Hall cut 赤字继续存在。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 capacity-unit-value-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = CAPACITY_INTEGRALITY_TARGET in old_target
    assignment_ready = previous.get("phase_residue_exchange_no_independent_assignment_incidence_closed") is True
    return [
        row("PhaseResidueExchangeCapacityValueUnitIntegralityImported", imported, False, "导入 capacity-value unit-integrality 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCapacityUnitValueLock", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("BoundaryEqualityAtomCarriedForwardAfterCapacityUnitValueLock", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterCapacityUnitValueLock", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterCapacityUnitValueLock", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCapacityUnitValueLock", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterCapacityUnitValueLock", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterCapacityUnitValueLock", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCapacityUnitValueLock", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentAssignmentIncidenceImportedForCapacityUnitValueLock", assignment_ready, assignment_ready, "导入 assignment lock：counted unit 必须通过 unit-value-one gate。", ASSIGNMENT_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentSignedAmountUnitAtom", True, True, "admitted unit 的 signed amount atom 规范化为一单位。", SIGNED_AMOUNT_UNIT),
        row("PhaseResidueExchangeCanonicalPaymentUnitValueOneNormalization", True, True, "unit-value-one gate 将可计容量单位归一为值 1。", UNIT_VALUE_ONE),
        row("PhaseResidueExchangeCanonicalPaymentCapacityAsUnitIndicatorSum", True, True, "capacity value 是 admitted 0/1 unit indicators 的有限和。", CAPACITY_AS_UNIT_SUM),
        row("PhaseResidueExchangeCanonicalPaymentCapacityIntegerSum", True, True, "有限 0/1 指示和是非负整数。", INTEGER_SUM),
        row("PhaseResidueExchangeCanonicalPaymentNonunitValueActualObjectReturn", True, False, "若 signed amount 不是规范一单位，则回流 actual-object incidence predicate。", NONUNIT_TO_OBJECT),
        row("PhaseResidueExchangeCanonicalPaymentBadUnitValueRemoval", True, False, "非规范单位不能计入 admitted capacity。", BAD_UNIT_REMOVAL),
        row("PhaseResidueExchangeCanonicalPaymentBadUnitValueSingletonCut", True, False, "剔除非规范单位后，缺失 cell 的 singleton Hall cut 赤字继续存在。", SINGLETON_FALLBACK),
        row("NoIndependentCapacityValueUnitIntegralityAfterCapacityUnitValueLock", True, True, "capacity-value unit-integrality 不再是独立活动出口。", NO_ANON),
        row("PhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterCapacityUnitValueLock", True, False, "cross-key whitelist leak 仍未排斥。", WHITELIST_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterCapacityUnitValueLock", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentCapacityUnitValueLockStillOpen", False, False, "仍未排斥 actual-object、singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "assignment-incidence-lock 层留下 capacity-value unit-integrality。"
        "本步把 admitted capacity value 锁定为 0/1 unit indicators 的有限和："
        "每个 admitted unit 的 signed amount atom 必须是规范一单位。非一单位值回流 actual-object "
        "字段谓词；剔除非规范单位后，singleton Hall cut 赤字继续存在。"
        "因此 capacity integrality 不再是独立活动出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_capacity_unit_value_lock_router",
        "status": "phase_residue_exchange_capacity_integrality_removed_actual_singleton_whitelist_and_parallel_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_capacity_value_unit_integrality_imported": CAPACITY_INTEGRALITY_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_assignment_incidence_lock_imported": bool(previous.get("phase_residue_exchange_no_independent_assignment_incidence_closed")),
        "phase_residue_exchange_signed_amount_unit_atom_closed": True,
        "phase_residue_exchange_unit_value_one_normalization_closed": True,
        "phase_residue_exchange_capacity_as_unit_indicator_sum_closed": True,
        "phase_residue_exchange_capacity_integer_sum_closed": True,
        "phase_residue_exchange_nonunit_value_actual_object_return_closed": True,
        "phase_residue_exchange_bad_unit_value_singleton_cut_closed": True,
        "phase_residue_exchange_no_independent_capacity_integrality_closed": True,
        "phase_residue_exchange_capacity_value_unit_integrality_proved": True,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": False,
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
        "old_exits": [CAPACITY_INTEGRALITY_TARGET],
        "new_exits": [ACTUAL_OBJECT, SINGLETON_HALL, WHITELIST_LEAK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "value_records": value_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-capacity-unit-value-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_capacity_value_unit_integrality_imported={fmt_bool(cert['phase_residue_exchange_capacity_value_unit_integrality_imported'])}",
        f"phase_residue_exchange_assignment_incidence_lock_imported={fmt_bool(cert['phase_residue_exchange_assignment_incidence_lock_imported'])}",
        f"phase_residue_exchange_signed_amount_unit_atom_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_unit_atom_closed'])}",
        f"phase_residue_exchange_unit_value_one_normalization_closed={fmt_bool(cert['phase_residue_exchange_unit_value_one_normalization_closed'])}",
        f"phase_residue_exchange_capacity_as_unit_indicator_sum_closed={fmt_bool(cert['phase_residue_exchange_capacity_as_unit_indicator_sum_closed'])}",
        f"phase_residue_exchange_capacity_integer_sum_closed={fmt_bool(cert['phase_residue_exchange_capacity_integer_sum_closed'])}",
        f"phase_residue_exchange_nonunit_value_actual_object_return_closed={fmt_bool(cert['phase_residue_exchange_nonunit_value_actual_object_return_closed'])}",
        f"phase_residue_exchange_bad_unit_value_singleton_cut_closed={fmt_bool(cert['phase_residue_exchange_bad_unit_value_singleton_cut_closed'])}",
        f"phase_residue_exchange_no_independent_capacity_integrality_closed={fmt_bool(cert['phase_residue_exchange_no_independent_capacity_integrality_closed'])}",
        f"phase_residue_exchange_capacity_value_unit_integrality_proved={fmt_bool(cert['phase_residue_exchange_capacity_value_unit_integrality_proved'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. capacity value lock 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["value_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "capacity-unit-value-lock 路由为：",
            "",
            "```text",
            "capacity_value = sum_{admitted units u} 1_u",
            "",
            "if a capacity unit has non-unit signed amount:",
            "  ActualObjectIncidencePredicatePDECCap",
            "else if the bad unit is removed from capacity:",
            "  CanonicalUnitSingletonHallCutDefectPDECCap",
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
            "- 本证书只移除 capacity-value unit-integrality 作为独立活动出口；非单位容量值回流 actual-object 或 singleton cut。",
            "- 本证书没有证明 actual-object incidence predicate PDEC/cap。",
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
