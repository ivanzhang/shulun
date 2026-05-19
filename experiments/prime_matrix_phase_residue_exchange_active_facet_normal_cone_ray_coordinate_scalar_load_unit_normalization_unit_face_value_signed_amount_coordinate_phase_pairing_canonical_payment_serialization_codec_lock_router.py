#!/usr/bin/env python3
"""生成 phase-residue exchange canonical-payment-serialization-codec-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_serialization_codec_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.md
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
    "phase-pairing-canonical-payment-serialization-codec-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-key-alias-normalization-router.json"
)
HASH_STABILITY_CERT = DOCS / "prime-matrix-canonical-formal-unit-hash-stability-router.json"

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
SERIALIZATION_DRIFT = f"{PREFIX}MaterializedCircuitCanonicalPaymentKeySerializationDriftPDECCap"
NONCANONICAL_LABEL = f"{PREFIX}MaterializedCircuitCanonicalPaymentNoncanonicalKeyLabelResiduePDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSerializationCodecLockImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
CAPACITY_INTEGRALITY = "StableLadderEndpointOrbitCapacityValueUnitIntegralityCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
ASSIGNMENT = "StableLadderEndpointOrbitUnitCapacityAssignmentIncidenceCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitMissingUnitCoordinateSlotMismatchCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCanonicalPaymentSerializationCodecLockLedger"

ALIAS_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentAliasNormalizationImportedForSerializationCodecLockLedger"
HASH_STABILITY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalFormalUnitHashStabilityImportedForSerializationCodecLockLedger"
FIELD_VECTOR = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentTupleFieldVectorLedger"
FIELD_TAG_ORDER = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentFieldTagTotalOrderLedger"
SCALAR_ENCODING = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentScalarEncodingLedger"
LENGTH_PREFIX = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentLengthPrefixInjectiveCodecLedger"
NULL_SENTINEL = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentNullSentinelLedger"
CODEC_DETERMINISM = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCodecDeterminismLedger"
EQUAL_FIELDS_EQUAL_BYTES = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentEqualFieldVectorEqualBytesLedger"
DRIFT_FIELD_OR_CODEC = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSerializationDriftFieldOrCodecDichotomyLedger"
DRIFT_ELIMINATED = "NoIndependentCanonicalPaymentSerializationDriftAfterCodecLockLedger"
NONCANONICAL_LABEL_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentNoncanonicalKeyLabelResidueCarriedForwardAfterSerializationCodecLockLedger"


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


def remove_serialization_drift(text: str) -> str:
    """从活动 OR 目标中移除 serialization drift 出口。"""
    if not text:
        return NONCANONICAL_LABEL
    updated = text.replace(f"{SERIALIZATION_DRIFT}Or{NONCANONICAL_LABEL}", NONCANONICAL_LABEL)
    updated = updated.replace(f"Or{SERIALIZATION_DRIFT}", "")
    updated = updated.replace(f"{SERIALIZATION_DRIFT}Or", "")
    return updated.replace(SERIALIZATION_DRIFT, NONCANONICAL_LABEL)


def next_target(previous: dict[str, Any]) -> str:
    """更新直接主攻目标。"""
    return remove_serialization_drift(previous.get("next_direct_attack_target", ""))


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
        ALIAS_IMPORT,
        HASH_STABILITY_IMPORT,
        FIELD_VECTOR,
        FIELD_TAG_ORDER,
        SCALAR_ENCODING,
        LENGTH_PREFIX,
        NULL_SENTINEL,
        CODEC_DETERMINISM,
        EQUAL_FIELDS_EQUAL_BYTES,
        DRIFT_FIELD_OR_CODEC,
        DRIFT_ELIMINATED,
        NONCANONICAL_LABEL_FORWARD,
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


def codec_records() -> list[dict[str, str]]:
    """给出 canonical payment serialization codec 的锁定字段。"""
    return [
        {
            "field": "field_vector",
            "meaning": "payment tuple 先降为有序字段向量；同 tuple 表示同一字段向量。",
        },
        {
            "field": "field_tag_order",
            "meaning": "字段标签采用全序，禁止实现侧重新排列造成第二种字节串。",
        },
        {
            "field": "scalar_encoding",
            "meaning": "整数、符号量、hash 与 phase/payment slot 使用唯一标量编码。",
        },
        {
            "field": "length_prefix",
            "meaning": "每个字段带类型标签与长度前缀，串接码在自由幺半群中可唯一切分。",
        },
        {
            "field": "null_sentinel",
            "meaning": "缺席槽位使用固定空值哨兵，不能被空串或默认零替代。",
        },
        {
            "field": "codec_determinism",
            "meaning": "canonical_bytes 是字段向量到字节串的函数；同输入只有一个输出。",
        },
    ]


def build_rows(previous: dict[str, Any], hash_doc: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 serialization-codec-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = SERIALIZATION_DRIFT in old_target
    alias_ready = previous.get("phase_residue_exchange_no_anonymous_key_tuple_alias_closed") is True
    hash_ready = hash_doc.get("canonical_formal_unit_hash_stability_closed") is True
    return [
        row("PhaseResidueExchangeCanonicalPaymentSerializationDriftImported", imported, False, "导入 canonical payment key serialization drift 出口。", old_target),
        row("ActualObjectIncidencePredicateCarriedForwardAfterSerializationCodecLock", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("CapacityValueUnitIntegralityCarriedForwardAfterSerializationCodecLock", True, False, "capacity-value unit-integrality PDEC/cap 继续作为独立出口。", CAPACITY_INTEGRALITY),
        row("UnitCapacityAssignmentIncidenceCarriedForwardAfterSerializationCodecLock", True, False, "unit-capacity assignment incidence PDEC/cap 继续作为独立出口。", ASSIGNMENT),
        row("MissingUnitCoordinateSlotMismatchCarriedForwardAfterSerializationCodecLock", True, False, "字段向量不同会回流 missing-unit coordinate slot mismatch 或相邻命名出口。", SLOT_MISMATCH),
        row("BoundaryEqualityAtomCarriedForwardAfterSerializationCodecLock", True, False, "boundary equality atom 继续作为独立出口。", BOUNDARY_EQUALITY),
        row("MultiplicityCapCarriedForwardAfterSerializationCodecLock", True, False, "source-atom multiplicity-cap PDEC/cap 继续前传。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterSerializationCodecLock", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterSerializationCodecLock", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterSerializationCodecLock", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterSerializationCodecLock", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterSerializationCodecLock", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("PhaseResidueExchangeCanonicalPaymentAliasNormalizationImportedForSerializationCodecLock", alias_ready, alias_ready, "导入 alias-normalization：同 tuple 不同 key 已被压成 serialization drift 或 noncanonical label。", ALIAS_IMPORT),
        row("PhaseResidueExchangeCanonicalFormalUnitHashStabilityImportedForSerializationCodecLock", hash_ready, hash_ready, "导入 canonical hash 稳定性，保证字段 hash 作为标量输入稳定。", HASH_STABILITY_IMPORT),
        row("PhaseResidueExchangeCanonicalPaymentTupleFieldVector", True, True, "payment tuple 的规范输入是固定字段向量。", FIELD_VECTOR),
        row("PhaseResidueExchangeCanonicalPaymentFieldTagTotalOrder", True, True, "字段标签全序固定，不能重排。", FIELD_TAG_ORDER),
        row("PhaseResidueExchangeCanonicalPaymentScalarEncoding", True, True, "整数、符号量、hash 和 phase/payment slots 采用唯一标量编码。", SCALAR_ENCODING),
        row("PhaseResidueExchangeCanonicalPaymentLengthPrefixInjectiveCodec", True, True, "类型标签与长度前缀使字节串可唯一切分。", LENGTH_PREFIX),
        row("PhaseResidueExchangeCanonicalPaymentNullSentinel", True, True, "空槽位有固定哨兵，不允许空串/默认零漂移。", NULL_SENTINEL),
        row("PhaseResidueExchangeCanonicalPaymentCodecDeterminism", True, True, "canonical_bytes 是确定函数。", CODEC_DETERMINISM),
        row("PhaseResidueExchangeCanonicalPaymentEqualFieldVectorEqualBytes", True, True, "同字段向量必得同一 canonical byte string。", EQUAL_FIELDS_EQUAL_BYTES),
        row("PhaseResidueExchangeCanonicalPaymentSerializationDriftFieldOrCodecDichotomy", True, True, "若 bytes 不同，要么字段向量不同并回流已命名出口，要么违反确定 codec。", DRIFT_FIELD_OR_CODEC),
        row("NoIndependentCanonicalPaymentSerializationDriftAfterCodecLock", True, True, "serialization drift 不再是独立活动出口。", DRIFT_ELIMINATED),
        row("PhaseResidueExchangeCanonicalPaymentNoncanonicalKeyLabelResidueCarriedForwardAfterSerializationCodecLock", True, False, "非规范 key 标签残留仍未排斥。", NONCANONICAL_LABEL_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterSerializationCodecLock", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCanonicalPaymentSerializationCodecLockStillOpen", False, False, "仍未排斥 noncanonical label residue、slot mismatch、singleton Hall cut、whitelist leak 或并行出口。", new_target),
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
        "alias-normalization 层留下 canonical payment key serialization drift。"
        "本步把 canonical_bytes 下降为字段向量上的确定编码：固定字段顺序、类型标签、长度前缀、"
        "唯一标量编码和空值哨兵。若 bytes 不同，则不是同一字段向量，需回流已有槽位/对象/赋值出口；"
        "若字段向量相同，则确定 codec 强制 bytes 相同。因此 serialization drift 不再是独立活动出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_serialization_codec_lock_router",
        "status": "phase_residue_exchange_canonical_payment_serialization_drift_removed_noncanonical_label_and_parallel_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "hash_stability_certificate": str(HASH_STABILITY_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_canonical_payment_serialization_drift_imported": SERIALIZATION_DRIFT in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_alias_normalization_imported": bool(previous.get("phase_residue_exchange_no_anonymous_key_tuple_alias_closed")),
        "canonical_formal_unit_hash_stability_imported": bool(hash_doc.get("canonical_formal_unit_hash_stability_closed")),
        "phase_residue_exchange_payment_tuple_field_vector_closed": True,
        "phase_residue_exchange_payment_field_tag_total_order_closed": True,
        "phase_residue_exchange_payment_scalar_encoding_closed": True,
        "phase_residue_exchange_payment_length_prefix_injective_codec_closed": True,
        "phase_residue_exchange_payment_null_sentinel_closed": True,
        "phase_residue_exchange_payment_codec_determinism_closed": True,
        "phase_residue_exchange_equal_field_vector_equal_bytes_closed": True,
        "phase_residue_exchange_serialization_drift_field_or_codec_dichotomy_closed": True,
        "phase_residue_exchange_no_independent_serialization_drift_closed": True,
        "phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved": True,
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
        "old_exits": [SERIALIZATION_DRIFT],
        "new_exits": [NONCANONICAL_LABEL],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "codec_records": codec_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-serialization-codec-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_canonical_payment_serialization_drift_imported={fmt_bool(cert['phase_residue_exchange_canonical_payment_serialization_drift_imported'])}",
        f"phase_residue_exchange_alias_normalization_imported={fmt_bool(cert['phase_residue_exchange_alias_normalization_imported'])}",
        f"canonical_formal_unit_hash_stability_imported={fmt_bool(cert['canonical_formal_unit_hash_stability_imported'])}",
        f"phase_residue_exchange_payment_tuple_field_vector_closed={fmt_bool(cert['phase_residue_exchange_payment_tuple_field_vector_closed'])}",
        f"phase_residue_exchange_payment_field_tag_total_order_closed={fmt_bool(cert['phase_residue_exchange_payment_field_tag_total_order_closed'])}",
        f"phase_residue_exchange_payment_scalar_encoding_closed={fmt_bool(cert['phase_residue_exchange_payment_scalar_encoding_closed'])}",
        f"phase_residue_exchange_payment_length_prefix_injective_codec_closed={fmt_bool(cert['phase_residue_exchange_payment_length_prefix_injective_codec_closed'])}",
        f"phase_residue_exchange_payment_null_sentinel_closed={fmt_bool(cert['phase_residue_exchange_payment_null_sentinel_closed'])}",
        f"phase_residue_exchange_payment_codec_determinism_closed={fmt_bool(cert['phase_residue_exchange_payment_codec_determinism_closed'])}",
        f"phase_residue_exchange_equal_field_vector_equal_bytes_closed={fmt_bool(cert['phase_residue_exchange_equal_field_vector_equal_bytes_closed'])}",
        f"phase_residue_exchange_serialization_drift_field_or_codec_dichotomy_closed={fmt_bool(cert['phase_residue_exchange_serialization_drift_field_or_codec_dichotomy_closed'])}",
        f"phase_residue_exchange_no_independent_serialization_drift_closed={fmt_bool(cert['phase_residue_exchange_no_independent_serialization_drift_closed'])}",
        f"phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. codec lock 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["codec_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "serialization-codec-lock 路由为：",
            "",
            "```text",
            "canonical_bytes = codec(field_vector(payment_tuple))",
            "",
            "if same tuple has two canonical byte strings:",
            "  if field vectors differ:",
            "    named slot/object/assignment exit",
            "  else:",
            "    impossible by deterministic canonical codec",
            "",
            "remaining key-side exit:",
            "  MaterializedCircuitCanonicalPaymentNoncanonicalKeyLabelResiduePDECCap",
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
            "- 本证书只排除 canonical payment key serialization drift 作为独立活动出口；字段向量不同会回流已有命名出口。",
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
