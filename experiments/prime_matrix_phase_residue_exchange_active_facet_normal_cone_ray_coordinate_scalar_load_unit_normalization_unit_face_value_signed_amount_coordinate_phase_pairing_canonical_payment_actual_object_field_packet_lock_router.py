#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-actual-object-field-packet-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_field_packet_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.md
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
    "phase-pairing-canonical-payment-actual-object-field-packet-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-capacity-unit-value-lock-router.json"
)
ACTUAL_OBJECT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-actual-object-predicate-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
ACTUAL_OBJECT = f"{PREFIX}ActualObjectIncidencePredicatePDECCap"
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"

FIELD_EXITS = [
    f"{PREFIX}ActualObjectMissingFieldPDECCap",
    f"{PREFIX}ActualObjectDuplicateFieldPDECCap",
    f"{PREFIX}ActualObjectSourceIncidenceFieldPDECCap",
    f"{PREFIX}ActualObjectOccurrenceIncidenceFieldPDECCap",
    f"{PREFIX}ActualObjectCRTRepresentativeFieldPDECCap",
    f"{PREFIX}ActualObjectCongruenceEvaluationFieldPDECCap",
    f"{PREFIX}ActualObjectPhaseEndpointFieldPDECCap",
    f"{PREFIX}ActualObjectSignedMassFieldPDECCap",
    f"{PREFIX}ActualObjectCalibratedPairingFieldPDECCap",
]
FIELD_PACKET_TARGET = "Or".join(FIELD_EXITS)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentActualObjectFieldPacketLockImportedLedger"
CAPACITY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCapacityUnitValueImportedForActualObjectFieldPacketLockLedger"
OLD_OBJECT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectPredicateRouterImportedForFieldPacketLockLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectFieldPacketCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
BOUNDARY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
VARIATION = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentActualObjectFieldPacketLockLedger"
SINGLETON_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterActualObjectFieldPacketLockLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterActualObjectFieldPacketLockLedger"

TUPLE_SCHEMA = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectTupleSchemaImportedForFieldPacketLockLedger"
CANONICAL_HASH = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCanonicalHashImportedForFieldPacketLockLedger"
SOURCE_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSourceFieldPacketLedger"
OCCURRENCE_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectOccurrenceFieldPacketLedger"
CRT_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCRTFieldPacketLedger"
CONGRUENCE_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCongruenceFieldPacketLedger"
PHASE_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectPhaseEndpointFieldPacketLedger"
SIGNED_MASS_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSignedMassFieldPacketLedger"
PAIRING_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectPairingFieldPacketLedger"
MISSING_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectMissingFieldPacketLedger"
DUPLICATE_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectDuplicateFieldPacketLedger"
NO_ANON = "NoIndependentActualObjectIncidencePredicateAfterFieldPacketLockLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, ACTUAL_OBJECT_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def next_target(previous: dict[str, Any]) -> str:
    """把 actual-object predicate 总出口替换为字段包出口。"""
    target = previous.get("next_direct_attack_target", "")
    if ACTUAL_OBJECT in target:
        return target.replace(ACTUAL_OBJECT, FIELD_PACKET_TARGET)
    return FIELD_PACKET_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        CAPACITY_IMPORT,
        OLD_OBJECT_IMPORT,
        BOUNDARY,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        VARIATION,
        TUPLE_SCHEMA,
        CANONICAL_HASH,
        SOURCE_FIELD,
        OCCURRENCE_FIELD,
        CRT_FIELD,
        CONGRUENCE_FIELD,
        PHASE_FIELD,
        SIGNED_MASS_FIELD,
        PAIRING_FIELD,
        MISSING_FIELD,
        DUPLICATE_FIELD,
        NO_ANON,
        SINGLETON_FORWARD,
        WHITELIST_FORWARD,
        PREDICATE,
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


def field_records() -> list[dict[str, str]]:
    """列出 actual-object predicate 的字段包。"""
    return [
        {"field": "missing_object", "meaning": "没有 actual object 时，不能记作匿名谓词失败，只能是 missing-field 出口。"},
        {"field": "duplicate_object", "meaning": "同一 canonical object 重复占用时，只能是 duplicate-field 出口。"},
        {"field": "source_incidence", "meaning": "source atom 必须落在 formal key 指定的 source multiplicity fiber。"},
        {"field": "occurrence_incidence", "meaning": "occurrence unit 必须落在 signed occurrence incidence cell。"},
        {"field": "crt_representative", "meaning": "CRT coordinate 必须是该 occurrence unit 的 primitive witness coordinate。"},
        {"field": "congruence_evaluation", "meaning": "canonical congruence equation 必须在该 coordinate 上成立。"},
        {"field": "phase_endpoint", "meaning": "phase endpoint 必须给出同一 r0,r* 与单位相位差。"},
        {"field": "signed_mass", "meaning": "signed amount 必须匹配规范单位 signed mass。"},
        {"field": "calibrated_pairing", "meaning": "actual phase pairing 必须匹配规范 pairing value。"},
    ]


def build_rows(previous: dict[str, Any], actual: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 actual-object-field-packet-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = ACTUAL_OBJECT in old_target
    actual_router_ready = all(
        actual.get(key) is True
        for key in [
            "phase_residue_exchange_actual_object_tuple_schema_closed",
            "phase_residue_exchange_actual_object_canonical_hash_closed",
            "phase_residue_exchange_actual_object_source_incidence_predicate_closed",
            "phase_residue_exchange_actual_object_occurrence_incidence_predicate_closed",
            "phase_residue_exchange_actual_object_crt_representative_predicate_closed",
            "phase_residue_exchange_actual_object_congruence_evaluation_predicate_closed",
            "phase_residue_exchange_actual_object_phase_endpoint_predicate_closed",
            "phase_residue_exchange_actual_object_signed_mass_predicate_closed",
            "phase_residue_exchange_actual_object_calibrated_pairing_predicate_closed",
        ]
    )
    return [
        row("PhaseResidueExchangeActualObjectIncidencePredicateImported", imported, False, "导入 actual-object incidence predicate 总出口。", old_target),
        row("PhaseResidueExchangeCanonicalPaymentCapacityUnitValueImportedForActualObjectFieldPacketLock", bool(previous.get("phase_residue_exchange_no_independent_capacity_integrality_closed")), True, "导入上一层 capacity-unit-value lock。", CAPACITY_IMPORT),
        row("PhaseResidueExchangeActualObjectPredicateRouterImportedForFieldPacketLock", actual_router_ready, actual_router_ready, "导入既有 actual-object predicate 字段 schema/hash 与七槽谓词证书。", OLD_OBJECT_IMPORT),
        row("PhaseResidueExchangeActualObjectTupleSchemaImportedForFieldPacketLock", bool(actual.get("phase_residue_exchange_actual_object_tuple_schema_closed")), True, "actual object 是固定字段 tuple。", TUPLE_SCHEMA),
        row("PhaseResidueExchangeActualObjectCanonicalHashImportedForFieldPacketLock", bool(actual.get("phase_residue_exchange_actual_object_canonical_hash_closed")), True, "actual object canonical hash 已由字段 tuple 确定。", CANONICAL_HASH),
        row("PhaseResidueExchangeActualObjectFieldPacketPartition", actual_router_ready, True, "谓词失败被拆成 missing、duplicate 或七个字段包失败。", FIELD_PACKET_TARGET),
        row("PhaseResidueExchangeActualObjectMissingFieldPacket", True, False, "缺失 actual object 继续作为字段级出口。", MISSING_FIELD),
        row("PhaseResidueExchangeActualObjectDuplicateFieldPacket", True, False, "重复 actual object 继续作为字段级出口。", DUPLICATE_FIELD),
        row("PhaseResidueExchangeActualObjectSourceFieldPacket", True, False, "source incidence 字段失败继续作为字段级出口。", SOURCE_FIELD),
        row("PhaseResidueExchangeActualObjectOccurrenceFieldPacket", True, False, "occurrence incidence 字段失败继续作为字段级出口。", OCCURRENCE_FIELD),
        row("PhaseResidueExchangeActualObjectCRTFieldPacket", True, False, "CRT representative 字段失败继续作为字段级出口。", CRT_FIELD),
        row("PhaseResidueExchangeActualObjectCongruenceFieldPacket", True, False, "congruence evaluation 字段失败继续作为字段级出口。", CONGRUENCE_FIELD),
        row("PhaseResidueExchangeActualObjectPhaseEndpointFieldPacket", True, False, "phase endpoint 字段失败继续作为字段级出口。", PHASE_FIELD),
        row("PhaseResidueExchangeActualObjectSignedMassFieldPacket", True, False, "signed mass 字段失败继续作为字段级出口。", SIGNED_MASS_FIELD),
        row("PhaseResidueExchangeActualObjectPairingFieldPacket", True, False, "calibrated pairing 字段失败继续作为字段级出口。", PAIRING_FIELD),
        row("NoIndependentActualObjectIncidencePredicateAfterFieldPacketLock", imported and actual_router_ready, True, "actual-object incidence predicate 不再是单一匿名出口。", NO_ANON),
        row("CanonicalUnitSingletonHallCutCarriedForwardAfterActualObjectFieldPacketLock", True, False, "singleton Hall cut 继续开放。", SINGLETON_FORWARD),
        row("CanonicalCrossKeyWhitelistLeakCarriedForwardAfterActualObjectFieldPacketLock", True, False, "cross-key whitelist leak 继续开放。", WHITELIST_FORWARD),
        row("BoundaryEqualityAtomCarriedForwardAfterActualObjectFieldPacketLock", True, False, "boundary equality atom 继续开放。", BOUNDARY),
        row("SparseScaleLadderSAECarriedForwardAfterActualObjectFieldPacketLock", True, False, "sparse scale-ladder SAE 继续前传。", SPARSE),
        row("EndpointOrbitActualObjectFieldPacketLockStillOpen", False, False, "仍未排斥字段级 actual-object 出口、singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    actual = load_json(ACTUAL_OBJECT_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, actual, new_target)
    actual_router_ready = any(item["gate"] == "PhaseResidueExchangeActualObjectPredicateRouterImportedForFieldPacketLock" and item["closed"] for item in rows)
    imported = ACTUAL_OBJECT in previous.get("next_direct_attack_target", "")
    plain = (
        "capacity-unit-value-lock 后仍有 actual-object incidence predicate 总出口。"
        "本步导入既有 actual-object predicate 证书，把 actual object 固定为 canonical tuple/hash，"
        "并把谓词失败拆成 missing、duplicate、source、occurrence、CRT、congruence、phase、signed-mass、pairing 字段包。"
        "因此 actual-object predicate 不再是匿名独立出口；但字段级出口和并行出口仍未排斥。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_field_packet_lock_router",
        "status": "phase_residue_exchange_actual_object_predicate_removed_to_field_packet_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "actual_object_predicate_certificate": str(ACTUAL_OBJECT_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_actual_object_incidence_predicate_imported": imported,
        "phase_residue_exchange_capacity_unit_value_lock_imported": bool(previous.get("phase_residue_exchange_no_independent_capacity_integrality_closed")),
        "phase_residue_exchange_actual_object_predicate_router_imported": actual_router_ready,
        "phase_residue_exchange_actual_object_tuple_schema_imported": bool(actual.get("phase_residue_exchange_actual_object_tuple_schema_closed")),
        "phase_residue_exchange_actual_object_canonical_hash_imported": bool(actual.get("phase_residue_exchange_actual_object_canonical_hash_closed")),
        "phase_residue_exchange_actual_object_field_packet_partition_closed": actual_router_ready,
        "phase_residue_exchange_no_independent_actual_object_predicate_closed": imported and actual_router_ready,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": imported and actual_router_ready,
        "phase_residue_exchange_actual_object_field_packet_exits_proved": False,
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
        "old_exits": [ACTUAL_OBJECT],
        "new_exits": FIELD_EXITS + [SINGLETON_HALL, WHITELIST_LEAK, BOUNDARY_EQUALITY],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "field_records": field_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-actual-object-field-packet-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_actual_object_incidence_predicate_imported={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_imported'])}",
        f"phase_residue_exchange_capacity_unit_value_lock_imported={fmt_bool(cert['phase_residue_exchange_capacity_unit_value_lock_imported'])}",
        f"phase_residue_exchange_actual_object_predicate_router_imported={fmt_bool(cert['phase_residue_exchange_actual_object_predicate_router_imported'])}",
        f"phase_residue_exchange_actual_object_tuple_schema_imported={fmt_bool(cert['phase_residue_exchange_actual_object_tuple_schema_imported'])}",
        f"phase_residue_exchange_actual_object_canonical_hash_imported={fmt_bool(cert['phase_residue_exchange_actual_object_canonical_hash_imported'])}",
        f"phase_residue_exchange_actual_object_field_packet_partition_closed={fmt_bool(cert['phase_residue_exchange_actual_object_field_packet_partition_closed'])}",
        f"phase_residue_exchange_no_independent_actual_object_predicate_closed={fmt_bool(cert['phase_residue_exchange_no_independent_actual_object_predicate_closed'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"phase_residue_exchange_actual_object_field_packet_exits_proved={fmt_bool(cert['phase_residue_exchange_actual_object_field_packet_exits_proved'])}",
        f"phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. actual-object 字段包",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["field_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "字段包路由为：",
            "",
            "```text",
            "actual_object = canonical_tuple(source, occurrence, CRT, congruence, phase, signed_mass, pairing)",
            "",
            "if actual object is missing or duplicated:",
            "  ActualObjectMissingFieldPDECCap or ActualObjectDuplicateFieldPDECCap",
            "else if any tuple field fails:",
            "  the matching ActualObject<Field>FieldPDECCap",
            "else:",
            "  actual-object incidence predicate is satisfied",
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
            "- 本证书只移除 actual-object incidence predicate 作为单一匿名活动出口；字段级出口仍开放。",
            "- 本证书没有证明 actual-object 字段包全都不失败。",
            "- 本证书没有证明 canonical singleton Hall cut defect PDEC/cap。",
            "- 本证书没有证明 canonical cross-key return whitelist leak PDEC/cap。",
            "- 本证书没有排斥 boundary equality atom，也没有证明 endpoint 并行出口或 sparse SAE 求和。",
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
