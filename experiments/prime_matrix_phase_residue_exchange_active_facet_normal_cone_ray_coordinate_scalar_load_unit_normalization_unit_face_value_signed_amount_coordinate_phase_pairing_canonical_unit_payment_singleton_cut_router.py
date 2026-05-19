#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-unit-payment-singleton-cut 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_singleton_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.md
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
    "phase-pairing-canonical-unit-payment-singleton-cut"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-unit-payment-conservation-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_CONSERVATION = f"{PREFIX}MaterializedCircuitCanonicalUnitPaymentConservationDefectPDECCap"
OLD_KEY_COLLISION = f"{PREFIX}MaterializedCircuitCanonicalUnitCompensatorKeyCollisionPDECCap"
SINGLETON_CUT = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
KEY_INJECTIVITY = f"{PREFIX}MaterializedCircuitCanonicalPaymentKeyInjectivityDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
NEW_TARGET = f"{SINGLETON_CUT}Or{KEY_INJECTIVITY}Or{WHITELIST_LEAK}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalUnitPaymentSingletonCutImportedLedger"
PAYMENT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalUnitPaymentConservationImportedForSingletonCutLedger"
SINGLETON_KEY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonKeyLedger"
DEMAND_ONE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonDemandOneLedger"
CAPACITY_ZERO = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonCapacityZeroLedger"
CUT_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonCutBalanceLedger"
SAME_KEY_EMPTY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSameKeyCapacityEdgeEmptyOnSingletonCutLedger"
NAMED_RETURN_BOUNDARY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalNamedReturnBoundaryLedger"
HALL_CUT_DEFECT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutDefectReturnLedger"
KEY_COLLISION_TRICHOTOMY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalKeyCollisionTrichotomyLedger"
KEY_INJECTIVITY_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyInjectivityDefectReturnLedger"
WHITELIST_LEAK_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyReturnWhitelistLeakReturnLedger"
NO_ANON = "NoAnonymousCanonicalPaymentConservationDefectAfterSingletonCutLedger"

PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitMissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentSingletonCutLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentSingletonCutLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentSingletonCutLedger"


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
    """把支付守恒/跨 key 碰撞出口替换为单点 cut 三出口。"""
    if OLD_CONSERVATION in text and OLD_KEY_COLLISION in text:
        text = text.replace(f"{OLD_CONSERVATION}Or{OLD_KEY_COLLISION}", NEW_TARGET)
        text = text.replace(OLD_CONSERVATION, NEW_TARGET)
        text = text.replace(OLD_KEY_COLLISION, NEW_TARGET)
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
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        PAYMENT_IMPORT,
        SINGLETON_KEY,
        DEMAND_ONE,
        CAPACITY_ZERO,
        CUT_BALANCE,
        SAME_KEY_EMPTY,
        NAMED_RETURN_BOUNDARY,
        HALL_CUT_DEFECT,
        KEY_COLLISION_TRICHOTOMY,
        KEY_INJECTIVITY_RETURN,
        WHITELIST_LEAK_RETURN,
        NO_ANON,
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


def cut_records() -> list[dict[str, str]]:
    """给出单点 Hall cut 字段。"""
    return [
        {
            "field": "singleton_key_cut",
            "meaning": "取 canonical 支付图中只含缺失 key k 的单点 cut。",
        },
        {
            "field": "cut_demand",
            "meaning": "由上游余额证书，cut 内需求单位数为 I_A(k)=1。",
        },
        {
            "field": "cut_capacity",
            "meaning": "同 key 容量端为 I_C(k)=0，故直接同 key 支付容量为 0。",
        },
        {
            "field": "named_return_boundary",
            "meaning": "只有 boundary equality、bridge、assignment、slot mismatch 等命名 return 可离开单点 cut。",
        },
        {
            "field": "singleton_hall_slack",
            "meaning": "若命名 return 也为空，则 Hall cut 余量为 1-0=1。",
        },
        {
            "field": "cross_key_claim",
            "meaning": "跨 key 补偿若声称同一 cell，则破坏 key 注入性；若非同一 cell，则必须是已白名单 return。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 canonical-unit-payment-singleton-cut 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_CONSERVATION in old_target or OLD_KEY_COLLISION in old_target
    return [
        row("PhaseResidueExchangeCanonicalPaymentSingletonCutImported", imported, False, "导入 canonical payment conservation defect 或 compensator key collision。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("MissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "missing-unit coordinate slot mismatch PDEC/cap 继续作为独立出口。", SLOT_MISMATCH),
        row("BoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalUnitPaymentConservationImportedForSingletonCut", imported, False, "导入同 key 支付守恒图和无隐藏跨 key 支付条件。", PAYMENT_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentSingletonKey", True, True, "选择缺失单位的 canonical key k 作为单点 cut。", SINGLETON_KEY),
        row("PhaseResidueExchangeCanonicalPaymentSingletonDemandOne", True, True, "cut 内需求为 I_A(k)=1。", DEMAND_ONE),
        row("PhaseResidueExchangeCanonicalPaymentSingletonCapacityZero", True, True, "cut 内同 key 容量为 I_C(k)=0。", CAPACITY_ZERO),
        row("PhaseResidueExchangeCanonicalPaymentSingletonCutBalance", True, True, "单点 cut 的形式余额为 I_A(k)-I_C(k)=1。", CUT_BALANCE),
        row("PhaseResidueExchangeCanonicalSameKeyCapacityEdgeEmptyOnSingletonCut", True, True, "同 key 容量边为空；若存在则会给出 I_C(k)=1，与上游容量排除冲突。", SAME_KEY_EMPTY),
        row("PhaseResidueExchangeCanonicalNamedReturnBoundary", True, False, "离开单点 cut 的非同 key 支付必须落在已命名 return 边界中。", NAMED_RETURN_BOUNDARY),
        row("PhaseResidueExchangeCanonicalSingletonHallCutDefectReturn", True, False, "若无命名 return，单点 Hall cut 保留 1 个未支付单位。", HALL_CUT_DEFECT),
        row("PhaseResidueExchangeCanonicalKeyCollisionTrichotomy", True, True, "跨 key 补偿只能是同 cell 多 key、合法命名 return，或未白名单泄漏。", KEY_COLLISION_TRICHOTOMY),
        row("PhaseResidueExchangeCanonicalPaymentKeyInjectivityDefectReturn", True, False, "若跨 key 补偿声称仍是同一 canonical cell，则成为 key 注入性缺陷。", KEY_INJECTIVITY_RETURN),
        row("PhaseResidueExchangeCanonicalCrossKeyReturnWhitelistLeakReturn", True, False, "若跨 key 补偿不是同一 cell 又未命名，则成为 return whitelist 泄漏。", WHITELIST_LEAK_RETURN),
        row("NoAnonymousCanonicalPaymentConservationDefectAfterSingletonCut", True, True, "payment defect/key collision 不再是匿名出口，只能落入单点 cut、key 注入性或白名单泄漏。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentSingletonCut", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonCutStillOpen", False, False, "仍未排斥单点 Hall cut defect、key injectivity defect 或 whitelist leak。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点已压成单点 Hall cut 或跨 key 白名单/注入性泄漏。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "canonical-unit-payment-conservation 层留下 payment defect 或 compensator key collision。"
        "本步取缺失 key k 的单点 Hall cut：I_A(k)=1、I_C(k)=0，所以同 key 直接容量为 0。"
        "若没有已命名 return，余额缺口就是显式 1 单位 cut defect；若跨 key 补偿声称支付同一 cell，"
        "则为 canonical key 注入性缺陷；若它不是同一 cell 又没有进入白名单，则为跨 key return whitelist 泄漏。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_singleton_cut_router",
        "status": "phase_residue_exchange_canonical_payment_defect_reduced_to_singleton_cut_or_whitelist_leak_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_canonical_payment_defect_or_collision_imported": OLD_CONSERVATION in previous.get("next_direct_attack_target", "") or OLD_KEY_COLLISION in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_singleton_key_cut_closed": True,
        "phase_residue_exchange_singleton_cut_demand_one_closed": True,
        "phase_residue_exchange_singleton_cut_capacity_zero_closed": True,
        "phase_residue_exchange_singleton_cut_balance_closed": True,
        "phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed": True,
        "phase_residue_exchange_cross_key_collision_trichotomy_closed": True,
        "phase_residue_exchange_no_anonymous_payment_conservation_defect_closed": True,
        "phase_residue_exchange_named_return_boundary_proved": False,
        "phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_payment_key_injectivity_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_unit_payment_graph_closed": False,
        "phase_residue_exchange_canonical_payment_return_whitelist_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": False,
        "phase_residue_exchange_unit_capacity_assignment_incidence_proved": False,
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
        "old_exits": [OLD_CONSERVATION, OLD_KEY_COLLISION],
        "new_exits": [SINGLETON_CUT, KEY_INJECTIVITY, WHITELIST_LEAK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "cut_records": cut_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-unit-payment-singleton-cut 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_canonical_payment_defect_or_collision_imported={fmt_bool(cert['phase_residue_exchange_canonical_payment_defect_or_collision_imported'])}",
        f"phase_residue_exchange_singleton_key_cut_closed={fmt_bool(cert['phase_residue_exchange_singleton_key_cut_closed'])}",
        f"phase_residue_exchange_singleton_cut_demand_one_closed={fmt_bool(cert['phase_residue_exchange_singleton_cut_demand_one_closed'])}",
        f"phase_residue_exchange_singleton_cut_capacity_zero_closed={fmt_bool(cert['phase_residue_exchange_singleton_cut_capacity_zero_closed'])}",
        f"phase_residue_exchange_singleton_cut_balance_closed={fmt_bool(cert['phase_residue_exchange_singleton_cut_balance_closed'])}",
        f"phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed={fmt_bool(cert['phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed'])}",
        f"phase_residue_exchange_cross_key_collision_trichotomy_closed={fmt_bool(cert['phase_residue_exchange_cross_key_collision_trichotomy_closed'])}",
        f"phase_residue_exchange_no_anonymous_payment_conservation_defect_closed={fmt_bool(cert['phase_residue_exchange_no_anonymous_payment_conservation_defect_closed'])}",
        f"phase_residue_exchange_named_return_boundary_proved={fmt_bool(cert['phase_residue_exchange_named_return_boundary_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_payment_key_injectivity_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_key_injectivity_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_unit_payment_graph_closed={fmt_bool(cert['phase_residue_exchange_canonical_unit_payment_graph_closed'])}",
        f"phase_residue_exchange_canonical_payment_return_whitelist_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_return_whitelist_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单点 Hall cut 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["cut_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "单点 cut 路由为：",
            "",
            "```text",
            "singleton cut S={k}",
            "cut_demand = I_A(k)=1",
            "cut_capacity = I_C(k)=0",
            "",
            "if no named return leaves S:",
            "  MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap",
            "otherwise if a cross-key compensator claims the same canonical cell:",
            "  MaterializedCircuitCanonicalPaymentKeyInjectivityDefectPDECCap",
            "otherwise if a cross-key compensator is not whitelisted:",
            "  MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap",
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
            "- 本证书没有证明 canonical singleton Hall cut defect PDEC/cap。",
            "- 本证书没有证明 canonical payment key injectivity defect PDEC/cap。",
            "- 本证书没有证明 canonical cross-key return whitelist leak PDEC/cap。",
            "- 本证书没有证明 canonical payment graph 全局闭合，也没有证明 return whitelist。",
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
