#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-key-label-admission-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_label_admission_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.md
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
    "phase-pairing-canonical-payment-key-label-admission-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-serialization-codec-lock-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
NONCANONICAL_LABEL = f"{PREFIX}MaterializedCircuitCanonicalPaymentNoncanonicalKeyLabelResiduePDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyLabelAdmissionLockImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitMissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentKeyLabelAdmissionLockLedger"

CODEC_LOCK_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSerializationCodecLockImportedForKeyLabelAdmissionLedger"
CANONICAL_KEY_FORMULA = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAdmittedKeyFormulaLedger"
EXTERNAL_LABEL_ERASURE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentExternalLabelErasureLedger"
EDGE_ADMISSION = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentEdgeAdmissionPredicateLedger"
RETURN_WHITELIST_BINDING = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentReturnWhitelistBindingLedger"
NONCANONICAL_NOT_EDGE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentNoncanonicalLabelNotAdmittedEdgeLedger"
NONCANONICAL_TO_WHITELIST = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentNoncanonicalLabelReturnWhitelistLeakLedger"
NO_ANON = "NoIndependentCanonicalPaymentNoncanonicalKeyLabelResidueAfterAdmissionLockLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyReturnWhitelistLeakCarriedForwardAfterKeyLabelAdmissionLockLedger"


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


def remove_noncanonical_label(text: str) -> str:
    """从活动 OR 目标中移除 noncanonical label residue 出口。"""
    if not text:
        return WHITELIST_LEAK
    updated = text.replace(f"{NONCANONICAL_LABEL}Or", "")
    updated = updated.replace(f"Or{NONCANONICAL_LABEL}", "")
    updated = updated.replace(NONCANONICAL_LABEL, WHITELIST_LEAK)
    return updated


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    return remove_noncanonical_label(previous.get("next_direct_attack_target", ""))


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
        CODEC_LOCK_IMPORT,
        CANONICAL_KEY_FORMULA,
        EXTERNAL_LABEL_ERASURE,
        EDGE_ADMISSION,
        RETURN_WHITELIST_BINDING,
        NONCANONICAL_NOT_EDGE,
        NONCANONICAL_TO_WHITELIST,
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


def admission_records() -> list[dict[str, str]]:
    """给出 canonical payment edge admission 的字段。"""
    return [
        {
            "field": "admitted_key",
            "meaning": "admitted key 必须等于 H('canonical_payment_key', canonical_bytes(payment_tuple))。",
        },
        {
            "field": "external_label_erasure",
            "meaning": "外部传入标签不参与 canonical graph 身份判定。",
        },
        {
            "field": "edge_admission",
            "meaning": "只有通过 canonical key、actual object、unit assignment 与 capacity gate 的边才进入 payment graph。",
        },
        {
            "field": "return_whitelist_binding",
            "meaning": "跨 key return 必须显式列入 whitelist；未列入即是 whitelist leak。",
        },
        {
            "field": "noncanonical_label_not_edge",
            "meaning": "非规范 key 标签不是有效支付边，只能作为非法 return 证据出现。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 key-label-admission-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = NONCANONICAL_LABEL in old_target
    codec_ready = previous.get("phase_residue_exchange_no_independent_serialization_drift_closed") is True
    return [
        row("PhaseResidueExchangeCanonicalPaymentNoncanonicalLabelImported", imported, False, "导入 noncanonical key label residue 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterKeyLabelAdmissionLock", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterKeyLabelAdmissionLock", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterKeyLabelAdmissionLock", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("MissingUnitCoordinateSlotMismatchCarriedForwardAfterKeyLabelAdmissionLock", True, False, "missing-unit coordinate slot mismatch PDEC/cap 继续作为独立出口。", SLOT_MISMATCH),
        row("BoundaryEqualityAtomCarriedForwardAfterKeyLabelAdmissionLock", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterKeyLabelAdmissionLock", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterKeyLabelAdmissionLock", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterKeyLabelAdmissionLock", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterKeyLabelAdmissionLock", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterKeyLabelAdmissionLock", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterKeyLabelAdmissionLock", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentSerializationCodecLockImportedForKeyLabelAdmission", codec_ready, codec_ready, "导入 codec-lock：canonical bytes 与 key 公式已确定。", CODEC_LOCK_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentAdmittedKeyFormula", True, True, "admitted payment key 必须等于 canonical hash 公式。", CANONICAL_KEY_FORMULA),
        row("PhaseResidueExchangeCanonicalPaymentExternalLabelErasure", True, True, "外部标签不参与 canonical graph 身份。", EXTERNAL_LABEL_ERASURE),
        row("PhaseResidueExchangeCanonicalPaymentEdgeAdmissionPredicate", True, True, "只有通过 canonical key 与对象/容量 gate 的边进入 graph。", EDGE_ADMISSION),
        row("PhaseResidueExchangeCanonicalPaymentReturnWhitelistBinding", True, True, "跨 key return 必须绑定 whitelist。", RETURN_WHITELIST_BINDING),
        row("PhaseResidueExchangeCanonicalPaymentNoncanonicalLabelNotAdmittedEdge", True, True, "非规范 key 标签不是有效支付边。", NONCANONICAL_NOT_EDGE),
        row("PhaseResidueExchangeCanonicalPaymentNoncanonicalLabelReturnWhitelistLeak", True, False, "若非规范标签仍作为 return 生效，则回流 cross-key whitelist leak。", NONCANONICAL_TO_WHITELIST),
        row("NoIndependentCanonicalPaymentNoncanonicalKeyLabelResidueAfterAdmissionLock", True, True, "noncanonical label residue 不再是独立活动出口。", NO_ANON),
        row("PhaseResidueExchangeCanonicalCrossKeyReturnWhitelistLeakCarriedForwardAfterKeyLabelAdmissionLock", True, False, "cross-key return whitelist leak 仍未排斥。", WHITELIST_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterKeyLabelAdmissionLock", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyLabelAdmissionLockStillOpen", False, False, "仍未排斥 slot mismatch、singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "serialization-codec-lock 层留下 noncanonical key label residue。"
        "本步把 payment edge admission 固定为 canonical key 公式与 return whitelist 的合取。"
        "外部标签不进入 canonical graph；若它仍被当作跨 key return 使用，则就是 whitelist leak。"
        "因此 noncanonical key label residue 不再是独立活动出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_label_admission_lock_router",
        "status": "phase_residue_exchange_noncanonical_key_label_residue_removed_whitelist_and_parallel_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_imported": NONCANONICAL_LABEL in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_serialization_codec_lock_imported": bool(previous.get("phase_residue_exchange_no_independent_serialization_drift_closed")),
        "phase_residue_exchange_payment_admitted_key_formula_closed": True,
        "phase_residue_exchange_payment_external_label_erasure_closed": True,
        "phase_residue_exchange_payment_edge_admission_predicate_closed": True,
        "phase_residue_exchange_payment_return_whitelist_binding_closed": True,
        "phase_residue_exchange_payment_noncanonical_label_not_admitted_edge_closed": True,
        "phase_residue_exchange_noncanonical_label_to_whitelist_leak_closed": True,
        "phase_residue_exchange_no_independent_noncanonical_label_residue_closed": True,
        "phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved": True,
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
        "old_exits": [NONCANONICAL_LABEL],
        "new_exits": [WHITELIST_LEAK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "admission_records": admission_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-key-label-admission-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_imported={fmt_bool(cert['phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_imported'])}",
        f"phase_residue_exchange_serialization_codec_lock_imported={fmt_bool(cert['phase_residue_exchange_serialization_codec_lock_imported'])}",
        f"phase_residue_exchange_payment_admitted_key_formula_closed={fmt_bool(cert['phase_residue_exchange_payment_admitted_key_formula_closed'])}",
        f"phase_residue_exchange_payment_external_label_erasure_closed={fmt_bool(cert['phase_residue_exchange_payment_external_label_erasure_closed'])}",
        f"phase_residue_exchange_payment_edge_admission_predicate_closed={fmt_bool(cert['phase_residue_exchange_payment_edge_admission_predicate_closed'])}",
        f"phase_residue_exchange_payment_return_whitelist_binding_closed={fmt_bool(cert['phase_residue_exchange_payment_return_whitelist_binding_closed'])}",
        f"phase_residue_exchange_payment_noncanonical_label_not_admitted_edge_closed={fmt_bool(cert['phase_residue_exchange_payment_noncanonical_label_not_admitted_edge_closed'])}",
        f"phase_residue_exchange_noncanonical_label_to_whitelist_leak_closed={fmt_bool(cert['phase_residue_exchange_noncanonical_label_to_whitelist_leak_closed'])}",
        f"phase_residue_exchange_no_independent_noncanonical_label_residue_closed={fmt_bool(cert['phase_residue_exchange_no_independent_noncanonical_label_residue_closed'])}",
        f"phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. key admission 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["admission_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "key-label-admission-lock 路由为：",
            "",
            "```text",
            "admitted_key = H('canonical_payment_key', canonical_bytes(payment_tuple))",
            "admitted_edge = canonical_key_ok AND object_gate_ok AND unit_capacity_gate_ok",
            "",
            "if external key label differs from admitted_key:",
            "  edge is not admitted to the canonical graph",
            "  if it is still used as a return:",
            "    MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap",
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
            "- 本证书只排除 noncanonical key label residue 作为独立活动出口；非法标签若仍生效会回流 whitelist leak。",
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
