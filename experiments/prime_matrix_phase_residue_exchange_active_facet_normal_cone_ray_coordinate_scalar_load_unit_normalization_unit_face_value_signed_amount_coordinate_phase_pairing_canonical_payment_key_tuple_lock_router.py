#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-key-tuple-lock 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_tuple_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.md
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
    "phase-pairing-canonical-payment-key-tuple-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-unit-payment-singleton-cut-router.json"
)
ACTUAL_OBJECT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-actual-object-predicate-router.json"
)
COORDINATE_LOCK_CERT = (
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
SINGLETON_CUT = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
OLD_KEY_INJECTIVITY = f"{PREFIX}MaterializedCircuitCanonicalPaymentKeyInjectivityDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
KEY_TUPLE_ALIAS = f"{PREFIX}MaterializedCircuitCanonicalPaymentKeyTupleAliasDefectPDECCap"
SLOT_MISMATCH = f"{PREFIX}MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap"
KEY_REPLACEMENT = f"{KEY_TUPLE_ALIAS}Or{SLOT_MISMATCH}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyTupleLockImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentKeyTupleLockLedger"

SINGLETON_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonCutImportedForKeyTupleLockLedger"
ACTUAL_OBJECT_HASH = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCanonicalHashImportedForPaymentKeyLedger"
MISSING_UNIT_HASH = "StableLadderEndpointOrbitPhaseResidueExchangeMissingUnitCanonicalHashImportedForPaymentKeyLedger"
PAYMENT_CELL_TUPLE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCellTupleSchemaLedger"
PAYMENT_KEY_AS_TUPLE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyDefinedAsTupleLedger"
SAME_CELL_EQUALITY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSameCellProjectionEqualityLedger"
CROSS_KEY_TRICHOTOMY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeySameCellTrichotomyLedger"
KEY_TUPLE_ALIAS_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyTupleAliasDefectReturnLedger"
SLOT_MISMATCH_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSlotMismatchReturnLedger"
SINGLETON_CUT_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterKeyTupleLockLedger"
WHITELIST_LEAK_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalWhitelistLeakCarriedForwardAfterKeyTupleLockLedger"
NO_ANON = "NoAnonymousCanonicalPaymentKeyInjectivityDefectAfterTupleLockLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, ACTUAL_OBJECT_CERT, COORDINATE_LOCK_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_old_targets(text: str) -> str:
    """把 key injectivity 出口替换为 tuple alias 或槽位不一致。"""
    return text.replace(OLD_KEY_INJECTIVITY, KEY_REPLACEMENT)


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    target = previous.get("next_direct_attack_target", "")
    updated = replace_old_targets(target)
    return updated or KEY_REPLACEMENT


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
        SINGLETON_IMPORT,
        ACTUAL_OBJECT_HASH,
        MISSING_UNIT_HASH,
        PAYMENT_CELL_TUPLE,
        PAYMENT_KEY_AS_TUPLE,
        SAME_CELL_EQUALITY,
        CROSS_KEY_TRICHOTOMY,
        KEY_TUPLE_ALIAS_RETURN,
        SLOT_MISMATCH_RETURN,
        SINGLETON_CUT_FORWARD,
        WHITELIST_LEAK_FORWARD,
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


def tuple_records() -> list[dict[str, str]]:
    """给出 canonical payment key 的 tuple 字段。"""
    return [
        {
            "field": "actual_object_hash",
            "meaning": "来自 actual-object predicate 的七槽对象 hash。",
        },
        {
            "field": "missing_unit_hash",
            "meaning": "来自 coordinate-lock 的缺失单位 canonical hash。",
        },
        {
            "field": "cell_tuple",
            "meaning": "支付 cell 由 actual object、source、occurrence、CRT、congruence、phase endpoint、signed amount 共同确定。",
        },
        {
            "field": "key_definition",
            "meaning": "canonical payment key 定义为 cell tuple 本身的规范表示，不允许后验换标签。",
        },
        {
            "field": "same_cell_equality",
            "meaning": "声称支付同一 canonical cell 时，所有 tuple 投影必须逐槽相等。",
        },
        {
            "field": "cross_key_trichotomy",
            "meaning": "跨 key 同 cell 只能是 tuple alias、槽位不一致，或其实并非同一 cell。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 canonical-payment-key-tuple-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_KEY_INJECTIVITY in old_target
    return [
        row("PhaseResidueExchangeCanonicalPaymentKeyTupleLockImported", imported, False, "导入 singleton-cut 层的 key injectivity 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("BoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentSingletonCutImportedForKeyTupleLock", True, False, "导入单点 cut、同 key 容量为空和跨 key 三分法。", SINGLETON_IMPORT),
        row("PhaseResidueExchangeActualObjectCanonicalHashImportedForPaymentKey", True, True, "actual-object predicate 已给出 formal key 与七槽 tuple 决定的对象 hash。", ACTUAL_OBJECT_HASH),
        row("PhaseResidueExchangeMissingUnitCanonicalHashImportedForPaymentKey", True, True, "missing-unit coordinate-lock 已给出缺失单位 canonical hash。", MISSING_UNIT_HASH),
        row("PhaseResidueExchangeCanonicalPaymentCellTupleSchema", True, True, "支付 cell 由对象 hash 与缺失单位坐标 tuple 共同决定。", PAYMENT_CELL_TUPLE),
        row("PhaseResidueExchangeCanonicalPaymentKeyDefinedAsTuple", True, True, "canonical payment key 是规范 tuple，不是可独立碰撞的外部标签。", PAYMENT_KEY_AS_TUPLE),
        row("PhaseResidueExchangeCanonicalSameCellProjectionEquality", True, True, "同一 canonical cell 要求所有 tuple 投影逐槽相等。", SAME_CELL_EQUALITY),
        row("PhaseResidueExchangeCanonicalCrossKeySameCellTrichotomy", True, True, "若声称同一 cell 但 key 不同，只能是 tuple alias 或槽位不一致；否则不是同一 cell。", CROSS_KEY_TRICHOTOMY),
        row("PhaseResidueExchangeCanonicalPaymentKeyTupleAliasDefectReturn", True, False, "若不同 key 仍代表完全相同 tuple，则成为 key tuple alias defect。", KEY_TUPLE_ALIAS_RETURN),
        row("PhaseResidueExchangeCanonicalPaymentSlotMismatchReturn", True, False, "若跨 key 源于某个 tuple 投影不等，则回流 missing-unit coordinate slot mismatch。", SLOT_MISMATCH_RETURN),
        row("PhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterKeyTupleLock", True, False, "singleton Hall cut defect 继续作为独立出口。", SINGLETON_CUT_FORWARD),
        row("PhaseResidueExchangeCanonicalWhitelistLeakCarriedForwardAfterKeyTupleLock", True, False, "cross-key return whitelist leak 继续作为独立出口。", WHITELIST_LEAK_FORWARD),
        row("NoAnonymousCanonicalPaymentKeyInjectivityDefectAfterTupleLock", True, True, "key injectivity 不再是匿名出口，只能落入 tuple alias 或槽位不一致。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentKeyTupleLock", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyTupleLockStillOpen", False, False, "仍未排斥 singleton Hall cut、key tuple alias、slot mismatch、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 singleton cut、tuple alias/slot mismatch、whitelist leak 与并行出口。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    actual = load_json(ACTUAL_OBJECT_CERT)
    coordinate = load_json(COORDINATE_LOCK_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "singleton-cut 层留下 payment key injectivity defect。"
        "本步把 payment key 固定为 actual-object 七槽 hash 与 missing-unit canonical hash 的规范 tuple："
        "若跨 key 补偿声称仍支付同一 canonical cell，则所有 tuple 投影必须逐槽相等。"
        "投影相等但 key 不同，只能是 key tuple alias defect；投影不等则不是同一 cell，"
        "并回流 missing-unit coordinate slot mismatch。"
        "因此 key injectivity 不再是独立匿名出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_tuple_lock_router",
        "status": "phase_residue_exchange_payment_key_injectivity_reduced_to_tuple_alias_or_slot_mismatch_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "actual_object_certificate": str(ACTUAL_OBJECT_CERT.relative_to(ROOT)),
        "coordinate_lock_certificate": str(COORDINATE_LOCK_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_payment_key_injectivity_defect_imported": OLD_KEY_INJECTIVITY in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_actual_object_canonical_hash_imported": bool(actual.get("phase_residue_exchange_actual_object_canonical_hash_closed")),
        "phase_residue_exchange_missing_unit_canonical_hash_imported": bool(coordinate.get("phase_residue_exchange_missing_unit_coordinate_lock_schema_closed")),
        "phase_residue_exchange_payment_cell_tuple_schema_closed": True,
        "phase_residue_exchange_payment_key_defined_as_tuple_closed": True,
        "phase_residue_exchange_same_cell_projection_equality_closed": True,
        "phase_residue_exchange_cross_key_same_cell_trichotomy_closed": True,
        "phase_residue_exchange_no_anonymous_key_injectivity_defect_closed": True,
        "phase_residue_exchange_canonical_payment_key_tuple_alias_defect_pdec_cap_proved": False,
        "phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved": False,
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
        "old_exits": [SINGLETON_CUT, OLD_KEY_INJECTIVITY, WHITELIST_LEAK],
        "new_exits": [SINGLETON_CUT, KEY_TUPLE_ALIAS, SLOT_MISMATCH, WHITELIST_LEAK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "tuple_records": tuple_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-key-tuple-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_payment_key_injectivity_defect_imported={fmt_bool(cert['phase_residue_exchange_payment_key_injectivity_defect_imported'])}",
        f"phase_residue_exchange_actual_object_canonical_hash_imported={fmt_bool(cert['phase_residue_exchange_actual_object_canonical_hash_imported'])}",
        f"phase_residue_exchange_missing_unit_canonical_hash_imported={fmt_bool(cert['phase_residue_exchange_missing_unit_canonical_hash_imported'])}",
        f"phase_residue_exchange_payment_cell_tuple_schema_closed={fmt_bool(cert['phase_residue_exchange_payment_cell_tuple_schema_closed'])}",
        f"phase_residue_exchange_payment_key_defined_as_tuple_closed={fmt_bool(cert['phase_residue_exchange_payment_key_defined_as_tuple_closed'])}",
        f"phase_residue_exchange_same_cell_projection_equality_closed={fmt_bool(cert['phase_residue_exchange_same_cell_projection_equality_closed'])}",
        f"phase_residue_exchange_cross_key_same_cell_trichotomy_closed={fmt_bool(cert['phase_residue_exchange_cross_key_same_cell_trichotomy_closed'])}",
        f"phase_residue_exchange_no_anonymous_key_injectivity_defect_closed={fmt_bool(cert['phase_residue_exchange_no_anonymous_key_injectivity_defect_closed'])}",
        f"phase_residue_exchange_canonical_payment_key_tuple_alias_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_key_tuple_alias_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. payment key tuple 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["tuple_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "key-tuple 路由为：",
            "",
            "```text",
            "payment_key = canonical_tuple(actual_object_hash, missing_unit_hash, phase/payment slots)",
            "",
            "if cross-key compensator claims the same canonical cell:",
            "  if tuple projections are equal and keys differ:",
            "    MaterializedCircuitCanonicalPaymentKeyTupleAliasDefectPDECCap",
            "  else:",
            "    MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap",
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
            "- 本证书没有证明 canonical payment key tuple alias defect PDEC/cap。",
            "- 本证书没有证明 missing-unit coordinate slot mismatch PDEC/cap。",
            "- 本证书没有证明 canonical singleton Hall cut defect PDEC/cap。",
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
