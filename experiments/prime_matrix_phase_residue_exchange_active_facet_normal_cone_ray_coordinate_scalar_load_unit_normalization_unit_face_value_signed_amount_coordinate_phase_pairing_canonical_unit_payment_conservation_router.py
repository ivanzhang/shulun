#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing canonical-unit-payment-conservation 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_conservation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.md
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
    "phase-pairing-canonical-unit-payment-conservation"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-missing-unit-balance-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_UNPAID = f"{PREFIX}MaterializedCircuitCanonicalMissingUnitUnpaidDemandCellPDECCap"
OLD_MISMATCH = f"{PREFIX}MaterializedCircuitCanonicalMissingUnitCompensationMismatchPDECCap"
CONSERVATION_TARGET = f"{PREFIX}MaterializedCircuitCanonicalUnitPaymentConservationDefectPDECCap"
KEY_COLLISION_TARGET = f"{PREFIX}MaterializedCircuitCanonicalUnitCompensatorKeyCollisionPDECCap"
NEW_TARGET = f"{CONSERVATION_TARGET}Or{KEY_COLLISION_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalUnitPaymentConservationImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitMissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
COMPENSATION_MISMATCH = "StableLadderEndpointOrbitCanonicalMissingUnitCompensationMismatchCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalUnitPaymentConservationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalUnitPaymentConservationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalUnitPaymentConservationLedger"

BALANCE_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalMissingUnitBalanceImportedLedger"
PAYMENT_GRAPH = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalUnitPaymentGraphLedger"
DEMAND_KEY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalDemandKeyLedger"
CAPACITY_KEY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCapacityKeyLedger"
PAYMENT_EDGE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSameKeyPaymentEdgeObligationLedger"
RETURN_WHITELIST = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentReturnWhitelistLedger"
NO_HIDDEN_EDGE = "StableLadderEndpointOrbitPhaseResidueExchangeNoHiddenCrossKeyPaymentEdgeLedger"
CONSERVATION_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalUnitPaymentConservationDefectReturnLedger"
KEY_COLLISION_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalUnitCompensatorKeyCollisionReturnLedger"
NO_ANON_PAYMENT = "NoAnonymousCanonicalUnitPaymentEscapeAfterConservationLedger"


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


def replace_old_targets(text: str) -> str:
    """把 unpaid/mismatch 双出口替换为支付守恒/跨 key 碰撞出口。"""
    if OLD_UNPAID in text and OLD_MISMATCH in text:
        text = text.replace(f"{OLD_UNPAID}Or{OLD_MISMATCH}", NEW_TARGET)
        text = text.replace(OLD_UNPAID, NEW_TARGET)
        text = text.replace(OLD_MISMATCH, NEW_TARGET)
    return text


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    target = previous.get("next_direct_attack_target", "")
    updated = replace_old_targets(target)
    return updated or NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PREDICATE,
        CAPACITY_INTEGRALITY,
        ASSIGNMENT,
        SLOT_MISMATCH,
        BOUNDARY_EQUALITY,
        COMPENSATION_MISMATCH,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        BALANCE_IMPORT,
        PAYMENT_GRAPH,
        DEMAND_KEY,
        CAPACITY_KEY,
        PAYMENT_EDGE,
        RETURN_WHITELIST,
        NO_HIDDEN_EDGE,
        CONSERVATION_RETURN,
        KEY_COLLISION_RETURN,
        NO_ANON_PAYMENT,
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


def payment_records() -> list[dict[str, str]]:
    """给出 canonical 单位支付守恒字段。"""
    return [
        {
            "field": "payment_graph",
            "meaning": "需求单位和容量单位在同一 actual object 内按 canonical key 建立有限支付图。",
        },
        {
            "field": "demand_key",
            "meaning": "缺失单元的需求端 key 为 k，且 I_A(k)=1。",
        },
        {
            "field": "capacity_key",
            "meaning": "容量端同 key 没有接纳单位，I_C(k)=0。",
        },
        {
            "field": "same_key_edge_obligation",
            "meaning": "合法直接支付必须给出同对象同 key 的容量边；否则必须进入已命名 return。",
        },
        {
            "field": "return_whitelist",
            "meaning": "允许的非同 key 支付只包括 boundary equality、bridge、assignment、slot mismatch 等已登记出口。",
        },
        {
            "field": "no_hidden_cross_key_edge",
            "meaning": "未登记的跨 key 补偿不能被当作同一 canonical cell 的支付。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 canonical-unit-payment-conservation 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_UNPAID in old_target or OLD_MISMATCH in old_target
    return [
        row(
            "PhaseResidueExchangeCanonicalUnitPaymentConservationImported",
            imported,
            False,
            "上一层已把 canonical missing unit 压成 unpaid demand cell 或 compensation mismatch。",
            old_target or f"{OLD_UNPAID}Or{OLD_MISMATCH}",
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("MissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "missing-unit coordinate slot mismatch PDEC/cap 继续作为独立出口。", SLOT_MISMATCH),
        row("BoundaryEqualityAtomCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("CanonicalMissingUnitCompensationMismatchCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "已登记 compensation mismatch 继续作为独立出口。", COMPENSATION_MISMATCH),
        row("MultiplicityCapCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalMissingUnitBalanceImported", imported, False, "导入 canonical key k 上的单位余额赤字。", BALANCE_IMPORT),
        row("PhaseResidueExchangeCanonicalUnitPaymentGraph", True, False, "同一 actual object 的需求/容量单位必须在 canonical key 支付图中核算。", PAYMENT_GRAPH),
        row("PhaseResidueExchangeCanonicalDemandKey", True, True, "需求端 key 为 k，I_A(k)=1。", DEMAND_KEY),
        row("PhaseResidueExchangeCanonicalCapacityKey", True, True, "容量端同 key 为 0，I_C(k)=0。", CAPACITY_KEY),
        row("PhaseResidueExchangeCanonicalSameKeyPaymentEdgeObligation", True, False, "直接支付必须是同对象同 key 容量边；否则不能支付该 canonical cell。", PAYMENT_EDGE),
        row("PhaseResidueExchangeCanonicalPaymentReturnWhitelist", True, False, "非同 key 支付必须进入 boundary/bridge/assignment/slot-mismatch 等已命名出口。", RETURN_WHITELIST),
        row("PhaseResidueExchangeNoHiddenCrossKeyPaymentEdge", True, True, "隐藏跨 key 补偿不能冒充同 key 支付。", NO_HIDDEN_EDGE),
        row("PhaseResidueExchangeCanonicalUnitPaymentConservationDefectReturn", True, False, "若无同 key 容量边也无命名 return，则为 canonical unit payment conservation defect。", CONSERVATION_RETURN),
        row("PhaseResidueExchangeCanonicalUnitCompensatorKeyCollisionReturn", True, False, "若补偿边存在但 key 不同，则为 canonical unit compensator key collision。", KEY_COLLISION_RETURN),
        row("NoAnonymousCanonicalUnitPaymentEscapeAfterConservation", True, True, "unpaid cell 不再能以未登记支付边或跨 key 补偿形式匿名保留。", NO_ANON_PAYMENT),
        row("SparseScaleLadderSAECarriedForwardAfterCanonicalUnitPaymentConservation", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalUnitPaymentConservationStillOpen", False, False, "仍未排斥 payment conservation defect、key collision、boundary equality 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 canonical payment conservation 或 key collision 出口。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "canonical-missing-unit-balance 层把同一 key k 上的余额锁成 I_A(k)=1、I_C(k)=0。"
        "本步把 unpaid demand cell 与 compensation mismatch 统一放入 canonical 单位支付图："
        "直接支付只能来自同对象同 key 的容量边；非同 key 的补偿必须进入已命名 boundary、bridge、"
        "assignment 或 slot-mismatch 出口。若没有同 key 支付也没有命名 return，就是 payment "
        "conservation defect；若补偿边跨 key，则是 compensator key collision。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_conservation_router",
        "status": "phase_residue_exchange_canonical_unpaid_cell_reduced_to_payment_conservation_or_key_collision_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_canonical_unpaid_or_mismatch_imported": OLD_UNPAID in previous.get("next_direct_attack_target", "") or OLD_MISMATCH in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_canonical_unit_demand_key_closed": True,
        "phase_residue_exchange_canonical_unit_capacity_key_closed": True,
        "phase_residue_exchange_no_hidden_cross_key_payment_closed": True,
        "phase_residue_exchange_canonical_unit_payment_graph_closed": False,
        "phase_residue_exchange_same_key_payment_edge_obligation_proved": False,
        "phase_residue_exchange_canonical_payment_return_whitelist_proved": False,
        "phase_residue_exchange_canonical_unit_payment_conservation_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_unit_compensator_key_collision_pdec_cap_proved": False,
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
        "old_exits": [OLD_UNPAID, OLD_MISMATCH],
        "new_exits": [CONSERVATION_TARGET, KEY_COLLISION_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "payment_records": payment_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange phase-pairing canonical-unit-payment-conservation 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_canonical_unpaid_or_mismatch_imported={fmt_bool(cert['phase_residue_exchange_canonical_unpaid_or_mismatch_imported'])}",
        f"phase_residue_exchange_canonical_unit_demand_key_closed={fmt_bool(cert['phase_residue_exchange_canonical_unit_demand_key_closed'])}",
        f"phase_residue_exchange_canonical_unit_capacity_key_closed={fmt_bool(cert['phase_residue_exchange_canonical_unit_capacity_key_closed'])}",
        f"phase_residue_exchange_no_hidden_cross_key_payment_closed={fmt_bool(cert['phase_residue_exchange_no_hidden_cross_key_payment_closed'])}",
        f"phase_residue_exchange_canonical_unit_payment_graph_closed={fmt_bool(cert['phase_residue_exchange_canonical_unit_payment_graph_closed'])}",
        f"phase_residue_exchange_same_key_payment_edge_obligation_proved={fmt_bool(cert['phase_residue_exchange_same_key_payment_edge_obligation_proved'])}",
        f"phase_residue_exchange_canonical_payment_return_whitelist_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_return_whitelist_proved'])}",
        f"phase_residue_exchange_canonical_unit_payment_conservation_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_unit_payment_conservation_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_unit_compensator_key_collision_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_unit_compensator_key_collision_pdec_cap_proved'])}",
        f"phase_residue_exchange_boundary_equality_atom_exclusion_proved={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_exclusion_proved'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. canonical 支付守恒字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["payment_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "支付守恒路由为：",
            "",
            "```text",
            "canonical key k",
            "I_A(k)=1",
            "I_C(k)=0",
            "",
            "if no same-object same-key capacity edge and no named return exists:",
            "  MaterializedCircuitCanonicalUnitPaymentConservationDefectPDECCap",
            "otherwise if a compensator uses another key:",
            "  MaterializedCircuitCanonicalUnitCompensatorKeyCollisionPDECCap",
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
            "- 本证书没有证明 canonical payment conservation defect PDEC/cap。",
            "- 本证书没有证明 canonical compensator key collision PDEC/cap。",
            "- 本证书没有证明 canonical payment graph 完全闭合。",
            "- 本证书没有证明 same-key payment edge obligation。",
            "- 本证书没有证明 canonical payment return whitelist。",
            "- 本证书没有证明 unit-capacity assignment incidence、capacity-value unit-integrality 或 actual-object incidence predicate。",
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
