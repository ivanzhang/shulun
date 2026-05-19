#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing canonical-missing-unit-balance 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_missing_unit_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.md
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
    "phase-pairing-canonical-missing-unit-balance"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-missing-unit-coordinate-lock-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}MaterializedCircuitCanonicalMissingCapacityUnitWitnessPDECCap"
UNPAID_TARGET = f"{PREFIX}MaterializedCircuitCanonicalMissingUnitUnpaidDemandCellPDECCap"
COMPENSATION_MISMATCH_TARGET = f"{PREFIX}MaterializedCircuitCanonicalMissingUnitCompensationMismatchPDECCap"
NEW_TARGET = f"{UNPAID_TARGET}Or{COMPENSATION_MISMATCH_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitImportedForBalanceLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitMissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalMissingUnitBalanceLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalMissingUnitBalanceLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalMissingUnitBalanceLedger"

CANONICAL_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingCapacityUnitWitnessImportedLedger"
CANONICAL_KEY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitKeyLedger"
DEMAND_INDICATOR = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitDemandIndicatorLedger"
CAPACITY_INDICATOR = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitCapacityIndicatorLedger"
UNIT_FACE_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitFaceValueLedger"
CELL_DEFICIT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitCellDeficitLedger"
COMPENSATOR_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitCompensatorGateLedger"
UNPAID_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitUnpaidDemandCellReturnLedger"
COMPENSATION_MISMATCH = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitCompensationMismatchReturnLedger"
NO_FREE_COMPENSATION = "NoAnonymousCanonicalMissingUnitCompensationAfterBalanceLedger"


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
    """把 canonical missing witness 替换为未支付单位或补偿不匹配出口。"""
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
        SLOT_MISMATCH,
        BOUNDARY_EQUALITY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        CANONICAL_IMPORT,
        CANONICAL_KEY,
        DEMAND_INDICATOR,
        CAPACITY_INDICATOR,
        UNIT_FACE_VALUE,
        CELL_DEFICIT,
        COMPENSATOR_GATE,
        UNPAID_RETURN,
        COMPENSATION_MISMATCH,
        NO_FREE_COMPENSATION,
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


def balance_records() -> list[dict[str, str]]:
    """给出 canonical missing unit 的单位余额字段。"""
    return [
        {
            "field": "canonical_key",
            "meaning": "k=hash(source, occurrence, CRT, congruence, phase endpoint, signed amount)。",
        },
        {
            "field": "demand_indicator",
            "meaning": "缺失单位属于需求集合，所以 I_A(k)=1。",
        },
        {
            "field": "capacity_indicator",
            "meaning": "缺失单位不属于容量接纳集合，所以 I_C(k)=0。",
        },
        {
            "field": "unit_face_value",
            "meaning": "signed amount 已单位化；该 canonical cell 的面值为 1。",
        },
        {
            "field": "cell_deficit",
            "meaning": "同一 canonical key 上的单位赤字为 I_A(k)-I_C(k)=1。",
        },
        {
            "field": "legal_compensator",
            "meaning": "任何声称补偿该赤字的对象必须同对象、同 key，或进入已命名的 boundary/bridge/assignment 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 canonical-missing-unit-balance 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeCanonicalMissingUnitImportedForBalance",
            imported,
            False,
            "上一层已把 missing unit witness 锁成 canonical missing capacity unit witness 或槽位不匹配。",
            old_target or OLD_TARGET,
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("MissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "missing-unit coordinate slot mismatch PDEC/cap 继续作为独立出口。", SLOT_MISMATCH),
        row("BoundaryEqualityAtomCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterCanonicalMissingUnitBalance", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalMissingUnitBalance", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalMissingCapacityUnitWitnessImported", imported, False, "导入 canonical missing capacity unit witness。", CANONICAL_IMPORT),
        row("PhaseResidueExchangeCanonicalMissingUnitKey", True, True, "所有坐标槽合成唯一 canonical key k。", CANONICAL_KEY),
        row("PhaseResidueExchangeCanonicalMissingUnitDemandIndicator", True, True, "u* in U_A 给出 I_A(k)=1。", DEMAND_INDICATOR),
        row("PhaseResidueExchangeCanonicalMissingUnitCapacityIndicator", True, True, "u* notin U_C 给出 I_C(k)=0。", CAPACITY_INDICATOR),
        row("PhaseResidueExchangeCanonicalMissingUnitFaceValue", True, True, "signed amount 槽已单位化，canonical cell 面值为 1。", UNIT_FACE_VALUE),
        row("PhaseResidueExchangeCanonicalMissingUnitCellDeficit", True, True, "同一 key 上出现不可匿名化的单位赤字 I_A(k)-I_C(k)=1。", CELL_DEFICIT),
        row("PhaseResidueExchangeCanonicalMissingUnitCompensatorGate", True, False, "若声称存在补偿单元，它必须同对象同 key；否则回流补偿槽位不匹配或 boundary/bridge/assignment 出口。", COMPENSATOR_GATE),
        row("PhaseResidueExchangeCanonicalMissingUnitUnpaidDemandCellReturn", True, False, "若无合法补偿，剩余就是 canonical unpaid demand cell PDEC/cap。", UNPAID_RETURN),
        row("PhaseResidueExchangeCanonicalMissingUnitCompensationMismatchReturn", True, False, "若补偿对象缺槽、换槽或跨 key，则回流 compensation mismatch PDEC/cap。", COMPENSATION_MISMATCH),
        row("NoAnonymousCanonicalMissingUnitCompensationAfterBalance", True, True, "canonical missing unit 不再能以未登记补偿或相位滑移形式匿名保留。", NO_FREE_COMPENSATION),
        row("SparseScaleLadderSAECarriedForwardAfterCanonicalMissingUnitBalance", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalMissingUnitBalanceStillOpen", False, False, "仍未排斥 unpaid demand cell、compensation mismatch、boundary equality 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 canonical missing unit 的单位余额出口或相关命名出口。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "missing-unit-coordinate-lock 层已把缺失单位锁成同一 actual object 的 canonical key。"
        "本步把该 key 上的单位余额显式化：u* in U_A 给出 I_A(k)=1，u* notin U_C 给出 "
        "I_C(k)=0，且 signed amount 已单位化，所以同一 canonical cell 上有单位赤字 1。"
        "若没有合法同对象同 key 补偿，剩余就是 unpaid demand cell；若声称有补偿但换槽、"
        "跨 key 或缺少合法边界/桥接登记，则是 compensation mismatch。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_missing_unit_balance_router",
        "status": "phase_residue_exchange_canonical_missing_unit_reduced_to_unpaid_cell_or_compensation_mismatch_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_canonical_missing_capacity_unit_witness_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_canonical_missing_unit_key_closed": True,
        "phase_residue_exchange_canonical_missing_unit_demand_indicator_closed": True,
        "phase_residue_exchange_canonical_missing_unit_capacity_indicator_closed": True,
        "phase_residue_exchange_canonical_missing_unit_face_value_closed": True,
        "phase_residue_exchange_canonical_missing_unit_cell_deficit_closed": True,
        "phase_residue_exchange_no_anonymous_canonical_missing_unit_compensation_closed": True,
        "phase_residue_exchange_canonical_missing_unit_unpaid_demand_cell_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_missing_unit_compensation_mismatch_pdec_cap_proved": False,
        "phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved": False,
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
        "new_exits": [UNPAID_TARGET, COMPENSATION_MISMATCH_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "balance_records": balance_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange phase-pairing canonical-missing-unit-balance 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_canonical_missing_capacity_unit_witness_imported={fmt_bool(cert['phase_residue_exchange_canonical_missing_capacity_unit_witness_imported'])}",
        f"phase_residue_exchange_canonical_missing_unit_key_closed={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_key_closed'])}",
        f"phase_residue_exchange_canonical_missing_unit_demand_indicator_closed={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_demand_indicator_closed'])}",
        f"phase_residue_exchange_canonical_missing_unit_capacity_indicator_closed={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_capacity_indicator_closed'])}",
        f"phase_residue_exchange_canonical_missing_unit_face_value_closed={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_face_value_closed'])}",
        f"phase_residue_exchange_canonical_missing_unit_cell_deficit_closed={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_cell_deficit_closed'])}",
        f"phase_residue_exchange_no_anonymous_canonical_missing_unit_compensation_closed={fmt_bool(cert['phase_residue_exchange_no_anonymous_canonical_missing_unit_compensation_closed'])}",
        f"phase_residue_exchange_canonical_missing_unit_unpaid_demand_cell_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_unpaid_demand_cell_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_missing_unit_compensation_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_missing_unit_compensation_mismatch_pdec_cap_proved'])}",
        f"phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved'])}",
        f"phase_residue_exchange_unit_capacity_assignment_incidence_proved={fmt_bool(cert['phase_residue_exchange_unit_capacity_assignment_incidence_proved'])}",
        f"phase_residue_exchange_capacity_value_unit_integrality_proved={fmt_bool(cert['phase_residue_exchange_capacity_value_unit_integrality_proved'])}",
        f"phase_residue_exchange_boundary_equality_atom_exclusion_proved={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_exclusion_proved'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. canonical 单元余额",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["balance_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "余额路由为：",
            "",
            "```text",
            "canonical key k",
            "I_A(k)=1",
            "I_C(k)=0",
            "unit_face_value=1",
            "cell_deficit=1",
            "",
            "if no legal same-object same-key compensator exists:",
            "  MaterializedCircuitCanonicalMissingUnitUnpaidDemandCellPDECCap",
            "otherwise if the compensator switches object/key/slot or lacks a named outlet:",
            "  MaterializedCircuitCanonicalMissingUnitCompensationMismatchPDECCap",
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
            "- 本证书没有证明 canonical unpaid demand cell PDEC/cap。",
            "- 本证书没有证明 canonical compensation mismatch PDEC/cap。",
            "- 本证书没有证明 missing-unit coordinate slot mismatch PDEC/cap。",
            "- 本证书没有证明 unit-capacity assignment incidence PDEC/cap。",
            "- 本证书没有证明 capacity-value unit-integrality PDEC/cap。",
            "- 本证书没有排斥 boundary equality atom。",
            "- 本证书没有证明 actual-object incidence predicate PDEC/cap。",
            "- 本证书没有证明 source-atom multiplicity-cap、endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
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
