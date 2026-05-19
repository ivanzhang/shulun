#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-key-alias-normalization 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_alias_normalization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.md
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
    "phase-pairing-canonical-payment-key-alias-normalization"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-key-tuple-lock-router.json"
)
HASH_STABILITY_CERT = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_ALIAS = f"{PREFIX}MaterializedCircuitCanonicalPaymentKeyTupleAliasDefectPDECCap"
SERIALIZATION_DRIFT = f"{PREFIX}MaterializedCircuitCanonicalPaymentKeySerializationDriftPDECCap"
NONCANONICAL_LABEL = f"{PREFIX}MaterializedCircuitCanonicalPaymentNoncanonicalKeyLabelResiduePDECCap"
NEW_ALIAS_TARGET = f"{SERIALIZATION_DRIFT}Or{NONCANONICAL_LABEL}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyAliasNormalizationImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitMissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentAliasNormalizationLedger"

TUPLE_LOCK_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyTupleLockImportedForAliasNormalizationLedger"
HASH_STABILITY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalFormalUnitHashStabilityImportedForPaymentKeyLedger"
DOMAIN_SEPARATOR = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyDomainSeparatorLedger"
SERIALIZATION_SCHEMA = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeySerializationSchemaLedger"
EQUAL_TUPLE_EQUAL_BYTES = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentEqualTupleEqualSerializationLedger"
PAYMENT_KEY_HASH = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeyHashFormulaLedger"
ALIAS_TRICHOTOMY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAliasNormalizationTrichotomyLedger"
SERIALIZATION_DRIFT_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentKeySerializationDriftReturnLedger"
NONCANONICAL_LABEL_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentNoncanonicalKeyLabelResidueReturnLedger"
NO_ANON = "NoAnonymousCanonicalPaymentKeyTupleAliasAfterNormalizationLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, HASH_STABILITY_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_old_targets(text: str) -> str:
    """把 key tuple alias 出口替换为规范序列化漂移或非规范标签残留。"""
    return text.replace(OLD_ALIAS, NEW_ALIAS_TARGET)


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    target = previous.get("next_direct_attack_target", "")
    updated = replace_old_targets(target)
    return updated or NEW_ALIAS_TARGET


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
        TUPLE_LOCK_IMPORT,
        HASH_STABILITY_IMPORT,
        DOMAIN_SEPARATOR,
        SERIALIZATION_SCHEMA,
        EQUAL_TUPLE_EQUAL_BYTES,
        PAYMENT_KEY_HASH,
        ALIAS_TRICHOTOMY,
        SERIALIZATION_DRIFT_RETURN,
        NONCANONICAL_LABEL_RETURN,
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


def normalization_records() -> list[dict[str, str]]:
    """给出 payment key 规范化字段。"""
    return [
        {
            "field": "domain_separator",
            "meaning": "payment key 使用固定 domain separator，不能复用 source/return/hash 标签空间。",
        },
        {
            "field": "canonical_serialization",
            "meaning": "actual-object hash、missing-unit hash 与 phase/payment slots 以排序字段和规范空值序列化。",
        },
        {
            "field": "equal_tuple_equal_bytes",
            "meaning": "同一 tuple 的规范序列化字节串唯一，因此不会产生两个合法 key。",
        },
        {
            "field": "payment_key_hash",
            "meaning": "payment_key = H('canonical_payment_key', canonical_bytes(tuple))。",
        },
        {
            "field": "serialization_drift",
            "meaning": "若同一 tuple 产生不同 canonical bytes，则是序列化漂移缺陷。",
        },
        {
            "field": "noncanonical_label",
            "meaning": "若不同 key 来自外部标签而非 canonical hash，则是非规范标签残留。",
        },
    ]


def build_rows(previous: dict[str, Any], hash_doc: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 canonical-payment-key-alias-normalization 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_ALIAS in old_target
    hash_ready = hash_doc.get("canonical_formal_unit_hash_stability_closed") is True
    return [
        row("PhaseResidueExchangeCanonicalPaymentKeyAliasNormalizationImported", imported, False, "导入 key tuple alias 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("MissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "missing-unit coordinate slot mismatch PDEC/cap 继续作为独立出口。", SLOT_MISMATCH),
        row("BoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentKeyTupleLockImportedForAliasNormalization", imported, False, "导入 tuple-lock：同 cell 要求 tuple 投影逐槽相等。", TUPLE_LOCK_IMPORT),
        row("PhaseResidueExchangeCanonicalFormalUnitHashStabilityImportedForPaymentKey", hash_ready, hash_ready, "导入已闭合的分层 canonical hash 稳定性与 no-loss return 继承纪律。", HASH_STABILITY_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentKeyDomainSeparator", True, True, "payment key 使用独立 domain separator。", DOMAIN_SEPARATOR),
        row("PhaseResidueExchangeCanonicalPaymentKeySerializationSchema", True, True, "payment tuple 以规范字段顺序、规范空值和规范字节串序列化。", SERIALIZATION_SCHEMA),
        row("PhaseResidueExchangeCanonicalPaymentEqualTupleEqualSerialization", True, True, "同一 tuple 的规范序列化字节串唯一。", EQUAL_TUPLE_EQUAL_BYTES),
        row("PhaseResidueExchangeCanonicalPaymentKeyHashFormula", True, True, "payment key 由固定 hash 公式生成。", PAYMENT_KEY_HASH),
        row("PhaseResidueExchangeCanonicalPaymentAliasNormalizationTrichotomy", True, True, "同 tuple 不同 key 只能是 canonical serialization drift 或 noncanonical label residue。", ALIAS_TRICHOTOMY),
        row("PhaseResidueExchangeCanonicalPaymentKeySerializationDriftReturn", True, False, "若同 tuple 得到两个 canonical bytes，则回流 serialization drift PDEC/cap。", SERIALIZATION_DRIFT_RETURN),
        row("PhaseResidueExchangeCanonicalPaymentNoncanonicalKeyLabelResidueReturn", True, False, "若某 key 不是规范 hash 输出，则回流 noncanonical key label residue PDEC/cap。", NONCANONICAL_LABEL_RETURN),
        row("NoAnonymousCanonicalPaymentKeyTupleAliasAfterNormalization", True, True, "key tuple alias 不再是匿名出口，只能落入序列化漂移或非规范标签残留。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentAliasNormalization", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentAliasNormalizationStillOpen", False, False, "仍未排斥 serialization drift、noncanonical label residue、slot mismatch、singleton Hall cut、whitelist leak 或并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    hash_doc = load_json(HASH_STABILITY_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, hash_doc, new_target)
    plain = (
        "canonical-payment-key-tuple-lock 层留下 key tuple alias defect。"
        "本步把 payment key 规范化为固定 domain separator 加 canonical tuple bytes 的 hash："
        "若同一 tuple 出现不同 key，要么规范序列化本身发生漂移，要么某条边仍携带非规范外部标签。"
        "因此 key tuple alias 不再是独立匿名出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_alias_normalization_router",
        "status": "phase_residue_exchange_payment_key_tuple_alias_reduced_to_serialization_drift_or_noncanonical_label_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "hash_stability_certificate": str(HASH_STABILITY_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_payment_key_tuple_alias_imported": OLD_ALIAS in previous.get("next_direct_attack_target", ""),
        "canonical_formal_unit_hash_stability_imported": bool(hash_doc.get("canonical_formal_unit_hash_stability_closed")),
        "phase_residue_exchange_payment_key_domain_separator_closed": True,
        "phase_residue_exchange_payment_key_serialization_schema_closed": True,
        "phase_residue_exchange_equal_tuple_equal_serialization_closed": True,
        "phase_residue_exchange_payment_key_hash_formula_closed": True,
        "phase_residue_exchange_alias_normalization_trichotomy_closed": True,
        "phase_residue_exchange_no_anonymous_key_tuple_alias_closed": True,
        "phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved": False,
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
        "old_exits": [OLD_ALIAS],
        "new_exits": [SERIALIZATION_DRIFT, NONCANONICAL_LABEL],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "normalization_records": normalization_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-key-alias-normalization 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_payment_key_tuple_alias_imported={fmt_bool(cert['phase_residue_exchange_payment_key_tuple_alias_imported'])}",
        f"canonical_formal_unit_hash_stability_imported={fmt_bool(cert['canonical_formal_unit_hash_stability_imported'])}",
        f"phase_residue_exchange_payment_key_domain_separator_closed={fmt_bool(cert['phase_residue_exchange_payment_key_domain_separator_closed'])}",
        f"phase_residue_exchange_payment_key_serialization_schema_closed={fmt_bool(cert['phase_residue_exchange_payment_key_serialization_schema_closed'])}",
        f"phase_residue_exchange_equal_tuple_equal_serialization_closed={fmt_bool(cert['phase_residue_exchange_equal_tuple_equal_serialization_closed'])}",
        f"phase_residue_exchange_payment_key_hash_formula_closed={fmt_bool(cert['phase_residue_exchange_payment_key_hash_formula_closed'])}",
        f"phase_residue_exchange_alias_normalization_trichotomy_closed={fmt_bool(cert['phase_residue_exchange_alias_normalization_trichotomy_closed'])}",
        f"phase_residue_exchange_no_anonymous_key_tuple_alias_closed={fmt_bool(cert['phase_residue_exchange_no_anonymous_key_tuple_alias_closed'])}",
        f"phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. alias normalization 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["normalization_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "alias-normalization 路由为：",
            "",
            "```text",
            "payment_key = H('canonical_payment_key', canonical_bytes(payment_tuple))",
            "",
            "if same tuple has two keys:",
            "  if canonical_bytes differ:",
            "    MaterializedCircuitCanonicalPaymentKeySerializationDriftPDECCap",
            "  else:",
            "    MaterializedCircuitCanonicalPaymentNoncanonicalKeyLabelResiduePDECCap",
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
            "- 本证书没有证明 canonical payment key serialization drift PDEC/cap。",
            "- 本证书没有证明 canonical payment noncanonical key label residue PDEC/cap。",
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
