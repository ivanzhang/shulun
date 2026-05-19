#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing unit-defect-witness 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_unit_defect_witness_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.md
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
    "phase-pairing-unit-defect-witness"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}MaterializedCircuitUnitNegativeDefectPDECCap"
ASSIGNMENT_TARGET = f"{PREFIX}MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap"
MISSING_UNIT_TARGET = f"{PREFIX}MaterializedCircuitMissingCapacityUnitWitnessPDECCap"
NEW_TARGET = f"{ASSIGNMENT_TARGET}Or{MISSING_UNIT_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeUnitDefectImportedForWitnessLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterUnitDefectWitnessLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterUnitDefectWitnessLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterUnitDefectWitnessLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterUnitDefectWitnessLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterUnitDefectWitnessLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterUnitDefectWitnessLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterUnitDefectWitnessLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterUnitDefectWitnessLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterUnitDefectWitnessLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterUnitDefectWitnessLedger"

UNIT_DEFECT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitNegativeDefectImportedLedger"
DEMAND_SET = "StableLadderEndpointOrbitPhaseResidueExchangeDemandUnitSetLedger"
CAPACITY_SET = "StableLadderEndpointOrbitPhaseResidueExchangeCapacityAdmittedUnitSetLedger"
ASSIGNMENT_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeUnitCapacityAssignmentIncidenceGateLedger"
DEFICIT_CARDINALITY = "StableLadderEndpointOrbitPhaseResidueExchangeUnitDefectCardinalityGapLedger"
NONEMPTY_COMPLEMENT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitDefectNonemptyComplementLedger"
MISSING_WITNESS = "StableLadderEndpointOrbitPhaseResidueExchangeMissingCapacityUnitWitnessLedger"
WITNESS_COORDINATES = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitWitnessCoordinateTupleLedger"
NO_AGGREGATE = "NoAnonymousAggregateUnitNegativeDefectAfterWitnessLedger"


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
    """把 unit negative defect 硬点替换为分配谓词缺陷或缺失单位见证。"""
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
        BOUNDARY_EQUALITY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        UNIT_DEFECT_IMPORT,
        DEMAND_SET,
        CAPACITY_SET,
        ASSIGNMENT_GATE,
        DEFICIT_CARDINALITY,
        NONEMPTY_COMPLEMENT,
        MISSING_WITNESS,
        WITNESS_COORDINATES,
        NO_AGGREGATE,
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


def witness_records() -> list[dict[str, str]]:
    """给出缺失单位见证的字段。"""
    return [
        {
            "field": "demand_unit_set",
            "meaning": "需求侧单位集合 U_A 由 price-one amount/payment value 给出，|U_A|=A。",
        },
        {
            "field": "capacity_admitted_unit_set",
            "meaning": "容量侧已接纳单位集合 U_C 由同一 actual object 的 materialized circuit 给出，|U_C|=C(O)。",
        },
        {
            "field": "assignment_incidence_gate",
            "meaning": "若 U_C 不能作为 U_A 的同对象单位分配子集合物化，则回流 unit-capacity assignment incidence PDEC/cap。",
        },
        {
            "field": "missing_unit",
            "meaning": "若分配门通过且 D=A-C(O)>=1，则 U_A \\ U_C 非空，可取缺失单位见证 u*。",
        },
        {
            "field": "witness_coordinates",
            "meaning": "u* 必须携带 source atom、occurrence unit、CRT coordinate、canonical congruence、phase endpoint 与 signed amount 槽位。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 unit-defect-witness 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeNegativeUnitDefectImportedForWitness",
            imported,
            False,
            "上一层已把负 slack 压成 capacity integrality defect 或 D=A-C(O)>=1 的 unit negative defect。",
            old_target or OLD_TARGET,
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterUnitDefectWitness", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterUnitDefectWitness", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("BoundaryEqualityAtomCarriedForwardAfterUnitDefectWitness", True, False, "boundary equality atom 继续作为独立出口；本步只处理负单位缺口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterUnitDefectWitness", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterUnitDefectWitness", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterUnitDefectWitness", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterUnitDefectWitness", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterUnitDefectWitness", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterUnitDefectWitness", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeUnitNegativeDefectImported", imported, False, "导入 D=A-C(O)>=1 的同对象单位负缺口分支。", UNIT_DEFECT_IMPORT),
        row("PhaseResidueExchangeDemandUnitSet", True, True, "需求侧单位集合 U_A 已由 price-one amount/payment value 锁定，|U_A|=A。", DEMAND_SET),
        row("PhaseResidueExchangeCapacityAdmittedUnitSet", True, False, "容量侧已接纳单位集合 U_C 必须由同一 materialized circuit 的容量槽物化。", CAPACITY_SET),
        row("PhaseResidueExchangeUnitCapacityAssignmentIncidenceGate", True, False, "若 U_C 不是 U_A 的同对象分配子集合，则成为 unit-capacity assignment incidence PDEC/cap。", ASSIGNMENT_GATE),
        row("PhaseResidueExchangeUnitDefectCardinalityGap", True, True, "unit negative defect 给出 |U_A|-|U_C|=D>=1。", DEFICIT_CARDINALITY),
        row("PhaseResidueExchangeUnitDefectNonemptyComplement", True, True, "分配门通过后 U_A \\ U_C 非空。", NONEMPTY_COMPLEMENT),
        row("PhaseResidueExchangeMissingCapacityUnitWitness", True, False, "非空补集给出缺失单位见证 u*；本步登记但不排斥它。", MISSING_WITNESS),
        row("PhaseResidueExchangeMissingUnitWitnessCoordinateTuple", True, False, "u* 必须携带 source、occurrence、CRT、congruence、phase endpoint 与 signed amount 坐标。", WITNESS_COORDINATES),
        row("NoAnonymousAggregateUnitNegativeDefectAfterWitness", True, True, "unit negative defect 不再能停留为总量赤字；它必须物化为分配缺陷或缺失单位见证。", NO_AGGREGATE),
        row("SparseScaleLadderSAECarriedForwardAfterUnitDefectWitness", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeUnitDefectWitnessStillOpen", False, False, "仍未排斥 actual-object predicate、capacity integrality、assignment incidence、missing unit witness、boundary equality 或 parallel outlets。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 missing unit witness 或相关命名出口。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "negative-unit-defect 层已经把负 slack 压成 D=A-C(O)>=1 的单位容量赤字。"
        "本步把这个总量赤字物化：若容量侧接纳单位集合 U_C 不能作为需求单位集合 U_A 的同对象"
        "分配子集合，则是 unit-capacity assignment incidence PDEC/cap；若分配门通过，"
        "则 |U_A\\U_C|=D>=1，必须存在缺失单位见证 u*。因此 unit negative defect "
        "不再能作为匿名总量缺口保留。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_unit_defect_witness_router",
        "status": "phase_residue_exchange_unit_negative_defect_reduced_to_assignment_incidence_or_missing_unit_witness_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_unit_negative_defect_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_demand_unit_set_locked": True,
        "phase_residue_exchange_unit_defect_cardinality_gap_closed": True,
        "phase_residue_exchange_unit_defect_nonempty_complement_closed": True,
        "phase_residue_exchange_no_aggregate_unit_defect_escape_closed": True,
        "phase_residue_exchange_unit_capacity_assignment_incidence_proved": False,
        "phase_residue_exchange_missing_capacity_unit_witness_pdec_cap_proved": False,
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
        "new_exits": [ASSIGNMENT_TARGET, MISSING_UNIT_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "witness_records": witness_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange phase-pairing unit-defect-witness 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_unit_negative_defect_imported={fmt_bool(cert['phase_residue_exchange_unit_negative_defect_imported'])}",
        f"phase_residue_exchange_demand_unit_set_locked={fmt_bool(cert['phase_residue_exchange_demand_unit_set_locked'])}",
        f"phase_residue_exchange_unit_defect_cardinality_gap_closed={fmt_bool(cert['phase_residue_exchange_unit_defect_cardinality_gap_closed'])}",
        f"phase_residue_exchange_unit_defect_nonempty_complement_closed={fmt_bool(cert['phase_residue_exchange_unit_defect_nonempty_complement_closed'])}",
        f"phase_residue_exchange_no_aggregate_unit_defect_escape_closed={fmt_bool(cert['phase_residue_exchange_no_aggregate_unit_defect_escape_closed'])}",
        f"phase_residue_exchange_unit_capacity_assignment_incidence_proved={fmt_bool(cert['phase_residue_exchange_unit_capacity_assignment_incidence_proved'])}",
        f"phase_residue_exchange_missing_capacity_unit_witness_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_missing_capacity_unit_witness_pdec_cap_proved'])}",
        f"phase_residue_exchange_capacity_value_unit_integrality_proved={fmt_bool(cert['phase_residue_exchange_capacity_value_unit_integrality_proved'])}",
        f"phase_residue_exchange_boundary_equality_atom_exclusion_proved={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_exclusion_proved'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单位赤字输入",
        "",
        "```text",
        "D(O)=A-C(O)>=1",
        "|U_A|=A",
        "|U_C|=C(O)",
        "same_actual_object=true",
        "```",
        "",
        "## 2. 缺失单位见证",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["witness_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "单位赤字路由为：",
            "",
            "```text",
            "D(O)=A-C(O)>=1",
            "  -> if U_C is not materialized as a same-object assigned subset of U_A:",
            "       MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap",
            "  -> otherwise choose u* in U_A \\ U_C:",
            "       MaterializedCircuitMissingCapacityUnitWitnessPDECCap",
            "anonymous_aggregate_unit_negative_defect=0",
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
            "- 本证书没有证明 unit-capacity assignment incidence PDEC/cap。",
            "- 本证书没有排斥 missing capacity unit witness PDEC/cap。",
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
