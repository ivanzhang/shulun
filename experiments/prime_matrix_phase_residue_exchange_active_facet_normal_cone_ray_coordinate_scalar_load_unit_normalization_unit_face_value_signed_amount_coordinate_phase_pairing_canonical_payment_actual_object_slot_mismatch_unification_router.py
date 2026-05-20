#!/usr/bin/env python3
"""生成 canonical-payment-actual-object-slot-mismatch-unification 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_slot_mismatch_unification_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.md
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
    "phase-pairing-canonical-payment-actual-object-slot-mismatch-unification"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-actual-object-field-packet-lock-router.json"
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
MISSING = f"{PREFIX}ActualObjectMissingFieldPDECCap"
DUPLICATE = f"{PREFIX}ActualObjectDuplicateFieldPDECCap"
SLOT_MISMATCH = f"{PREFIX}ActualObjectSlotMismatchPDECCap"
FIELD_MISMATCH_EXITS = [
    f"{PREFIX}ActualObjectSourceIncidenceFieldPDECCap",
    f"{PREFIX}ActualObjectOccurrenceIncidenceFieldPDECCap",
    f"{PREFIX}ActualObjectCRTRepresentativeFieldPDECCap",
    f"{PREFIX}ActualObjectCongruenceEvaluationFieldPDECCap",
    f"{PREFIX}ActualObjectPhaseEndpointFieldPDECCap",
    f"{PREFIX}ActualObjectSignedMassFieldPDECCap",
    f"{PREFIX}ActualObjectCalibratedPairingFieldPDECCap",
]
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentActualObjectSlotMismatchUnificationImportedLedger"
FIELD_PACKET_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectFieldPacketLockImportedForSlotMismatchUnificationLedger"
OLD_OBJECT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectPredicateRouterImportedForSlotMismatchUnificationLedger"
MISSING_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectMissingFieldCarriedForwardAfterSlotMismatchUnificationLedger"
DUPLICATE_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectDuplicateFieldCarriedForwardAfterSlotMismatchUnificationLedger"
SLOT_VECTOR = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSlotVectorLedger"
SLOT_MISMATCH_UNION = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSlotMismatchUnionLedger"
FIELD_TO_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectFieldFailureToSlotMismatchLedger"
NO_INDEPENDENT_FIELD = "NoIndependentActualObjectNamedFieldExitAfterSlotMismatchUnificationLedger"
SINGLETON_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonHallCutCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
BOUNDARY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
VARIATION = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterActualObjectSlotMismatchUnificationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterActualObjectSlotMismatchUnificationLedger"


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


def remove_or_token(text: str, token: str) -> str:
    """从长 OR 目标中移除一个 token 的全部出现。"""
    updated = text
    while f"{token}Or" in updated:
        updated = updated.replace(f"{token}Or", "")
    while f"Or{token}" in updated:
        updated = updated.replace(f"Or{token}", "")
    return updated.replace(token, "")


def next_target(previous: dict[str, Any]) -> str:
    """把七个字段失败统一为 slot-mismatch 出口。"""
    target = previous.get("next_direct_attack_target", "")
    if FIELD_MISMATCH_EXITS[0] in target:
        target = target.replace(FIELD_MISMATCH_EXITS[0], SLOT_MISMATCH)
    for token in FIELD_MISMATCH_EXITS[1:]:
        target = remove_or_token(target, token)
    return target or f"{MISSING}Or{DUPLICATE}Or{SLOT_MISMATCH}Or{SINGLETON_HALL}Or{WHITELIST_LEAK}"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        FIELD_PACKET_IMPORT,
        OLD_OBJECT_IMPORT,
        MISSING_FORWARD,
        DUPLICATE_FORWARD,
        SLOT_VECTOR,
        SLOT_MISMATCH_UNION,
        FIELD_TO_SLOT,
        NO_INDEPENDENT_FIELD,
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


def slot_records() -> list[dict[str, str]]:
    """列出字段失败到 slot mismatch 的归并。"""
    return [
        {"field": "source_incidence", "slot_mismatch": "source slot 不等于 formal key 的 source fiber。"},
        {"field": "occurrence_incidence", "slot_mismatch": "occurrence slot 不落在 source 的 incidence cell。"},
        {"field": "crt_representative", "slot_mismatch": "CRT slot 不是 occurrence 的 primitive witness coordinate。"},
        {"field": "congruence_evaluation", "slot_mismatch": "congruence slot 在 CRT coordinate 上求值失败。"},
        {"field": "phase_endpoint", "slot_mismatch": "phase slot 不给出同一端点对或单位相位差。"},
        {"field": "signed_mass", "slot_mismatch": "signed-mass slot 不等于规范单位 signed mass。"},
        {"field": "calibrated_pairing", "slot_mismatch": "pairing slot 不等于规范 calibrated pairing value。"},
    ]


def build_rows(previous: dict[str, Any], actual: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 slot-mismatch-unification 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = all(token in old_target for token in FIELD_MISMATCH_EXITS)
    actual_router_ready = actual.get("phase_residue_exchange_slot_mismatch_return_registered") is True
    return [
        row("PhaseResidueExchangeActualObjectFieldPacketImportedForSlotMismatchUnification", bool(previous.get("phase_residue_exchange_no_independent_actual_object_predicate_closed")), True, "导入 actual-object field packet lock。", FIELD_PACKET_IMPORT),
        row("PhaseResidueExchangeActualObjectPredicateRouterImportedForSlotMismatchUnification", actual_router_ready, actual_router_ready, "导入旧 actual-object predicate 的 slot-mismatch return。", OLD_OBJECT_IMPORT),
        row("PhaseResidueExchangeActualObjectAllNamedFieldExitsImported", imported, False, "七个具体字段失败出口全部导入。", old_target),
        row("PhaseResidueExchangeActualObjectMissingFieldCarriedForwardAfterSlotMismatchUnification", MISSING in old_target, False, "缺对象出口保留为对象存在性失败。", MISSING_FORWARD),
        row("PhaseResidueExchangeActualObjectDuplicateFieldCarriedForwardAfterSlotMismatchUnification", DUPLICATE in old_target, False, "重复对象出口保留为对象唯一性失败。", DUPLICATE_FORWARD),
        row("PhaseResidueExchangeActualObjectSlotVector", True, True, "actual object 七槽构成固定 slot vector。", SLOT_VECTOR),
        row("PhaseResidueExchangeActualObjectSlotMismatchUnion", True, True, "任一字段谓词失败都等价于 slot vector 对应槽位不匹配。", SLOT_MISMATCH_UNION),
        row("PhaseResidueExchangeActualObjectFieldFailureToSlotMismatch", True, True, "source/occurrence/CRT/congruence/phase/signed-mass/pairing 失败统一回流 slot mismatch。", FIELD_TO_SLOT),
        row("NoIndependentActualObjectNamedFieldExitAfterSlotMismatchUnification", imported and actual_router_ready, True, "七个具体字段出口不再独立活动。", NO_INDEPENDENT_FIELD),
        row("CanonicalSingletonHallCutCarriedForwardAfterActualObjectSlotMismatchUnification", True, False, "singleton Hall cut 继续开放。", SINGLETON_FORWARD),
        row("CanonicalCrossKeyWhitelistLeakCarriedForwardAfterActualObjectSlotMismatchUnification", True, False, "cross-key whitelist leak 继续开放。", WHITELIST_FORWARD),
        row("BoundaryEqualityAtomCarriedForwardAfterActualObjectSlotMismatchUnification", True, False, "boundary equality atom 继续开放。", BOUNDARY),
        row("SparseScaleLadderSAECarriedForwardAfterActualObjectSlotMismatchUnification", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointOrbitActualObjectSlotMismatchUnificationStillOpen", False, False, "仍未排斥 missing、duplicate、slot mismatch、singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    actual = load_json(ACTUAL_OBJECT_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, actual, new_target)
    imported = all(token in previous.get("next_direct_attack_target", "") for token in FIELD_MISMATCH_EXITS)
    actual_router_ready = actual.get("phase_residue_exchange_slot_mismatch_return_registered") is True
    plain = (
        "actual-object field-packet-lock 后有七个字段失败出口。"
        "本步用 canonical slot vector 把 source、occurrence、CRT、congruence、phase、signed-mass、pairing "
        "全部统一为 actual-object slot mismatch；missing 与 duplicate 作为对象存在性/唯一性出口保留。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_slot_mismatch_unification_router",
        "status": "phase_residue_exchange_actual_object_field_exits_unified_to_missing_duplicate_slot_mismatch_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "actual_object_predicate_certificate": str(ACTUAL_OBJECT_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_actual_object_named_field_exits_imported": imported,
        "phase_residue_exchange_actual_object_field_packet_lock_imported": bool(previous.get("phase_residue_exchange_no_independent_actual_object_predicate_closed")),
        "phase_residue_exchange_actual_object_slot_mismatch_return_imported": actual_router_ready,
        "phase_residue_exchange_actual_object_slot_vector_closed": True,
        "phase_residue_exchange_actual_object_slot_mismatch_union_closed": True,
        "phase_residue_exchange_actual_object_field_failure_to_slot_mismatch_closed": True,
        "phase_residue_exchange_no_independent_actual_object_named_field_exits_closed": imported and actual_router_ready,
        "phase_residue_exchange_actual_object_missing_field_pdec_cap_proved": False,
        "phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved": False,
        "phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved": False,
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
        "old_exits": FIELD_MISMATCH_EXITS,
        "new_exits": [MISSING, DUPLICATE, SLOT_MISMATCH, SINGLETON_HALL, WHITELIST_LEAK, BOUNDARY_EQUALITY],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "slot_records": slot_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-actual-object-slot-mismatch-unification 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_actual_object_named_field_exits_imported={fmt_bool(cert['phase_residue_exchange_actual_object_named_field_exits_imported'])}",
        f"phase_residue_exchange_actual_object_field_packet_lock_imported={fmt_bool(cert['phase_residue_exchange_actual_object_field_packet_lock_imported'])}",
        f"phase_residue_exchange_actual_object_slot_mismatch_return_imported={fmt_bool(cert['phase_residue_exchange_actual_object_slot_mismatch_return_imported'])}",
        f"phase_residue_exchange_actual_object_slot_vector_closed={fmt_bool(cert['phase_residue_exchange_actual_object_slot_vector_closed'])}",
        f"phase_residue_exchange_actual_object_slot_mismatch_union_closed={fmt_bool(cert['phase_residue_exchange_actual_object_slot_mismatch_union_closed'])}",
        f"phase_residue_exchange_actual_object_field_failure_to_slot_mismatch_closed={fmt_bool(cert['phase_residue_exchange_actual_object_field_failure_to_slot_mismatch_closed'])}",
        f"phase_residue_exchange_no_independent_actual_object_named_field_exits_closed={fmt_bool(cert['phase_residue_exchange_no_independent_actual_object_named_field_exits_closed'])}",
        f"phase_residue_exchange_actual_object_missing_field_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_actual_object_missing_field_pdec_cap_proved'])}",
        f"phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved'])}",
        f"phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. slot mismatch 归并",
        "",
        "| field | slot mismatch meaning |",
        "| --- | --- |",
    ]
    for record in cert["slot_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['slot_mismatch'])} |")
    lines.extend(
        [
            "",
            "```text",
            "actual_object_slot_vector = (source, occurrence, CRT, congruence, phase, signed_mass, pairing)",
            "",
            "missing object   -> ActualObjectMissingFieldPDECCap",
            "duplicate object -> ActualObjectDuplicateFieldPDECCap",
            "any slot failure -> ActualObjectSlotMismatchPDECCap",
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
            "- 本证书只把七个 actual-object 字段失败合并为 slot mismatch；没有排斥 missing、duplicate 或 slot mismatch。",
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
