#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing actual-object-predicate 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_actual_object_predicate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.md
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
    "phase-pairing-actual-object-predicate"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-circuit-materialization-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}ActualCircuitMaterializationPDECCap"
NEW_TARGET = f"{PREFIX}ActualObjectIncidencePredicatePDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualCircuitMaterializationImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeActualObjectPredicateLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeActualObjectPredicateLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeActualObjectPredicateLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeActualObjectPredicateLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeActualObjectPredicateLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeActualObjectPredicateLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeActualObjectPredicateLedger"

MATERIALIZATION_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualCircuitMaterializationImportedForPredicateLedger"
OBJECT_TUPLE = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectTupleSchemaLedger"
OBJECT_HASH = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCanonicalHashLedger"
SOURCE_INCIDENCE = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSourceIncidencePredicateLedger"
OCCURRENCE_INCIDENCE = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectOccurrenceIncidencePredicateLedger"
CRT_REPRESENTATIVE = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCRTRepresentativePredicateLedger"
CONGRUENCE_EVAL = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCongruenceEvaluationPredicateLedger"
PHASE_ENDPOINT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectPhaseEndpointPredicateLedger"
SIGNED_MASS_MATCH = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSignedMassPredicateLedger"
PAIRING_MATCH = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectCalibratedPairingPredicateLedger"
MISSING_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeMissingActualObjectReturnLedger"
DUPLICATE_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeDuplicateActualObjectReturnLedger"
SLOT_MISMATCH = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSlotMismatchReturnLedger"
PREDICATE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectIncidencePredicatePacketLedger"
NO_ANON = "NoAnonymousActualCircuitMaterializationAfterObjectPredicateLedger"


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
    """把 actual-circuit materialization 硬点替换为 actual-object predicate 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        MATERIALIZATION_IMPORT,
        OBJECT_TUPLE,
        OBJECT_HASH,
        SOURCE_INCIDENCE,
        OCCURRENCE_INCIDENCE,
        CRT_REPRESENTATIVE,
        CONGRUENCE_EVAL,
        PHASE_ENDPOINT,
        SIGNED_MASS_MATCH,
        PAIRING_MATCH,
        MISSING_OBJECT,
        DUPLICATE_OBJECT,
        SLOT_MISMATCH,
        PREDICATE_PACKET,
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


def predicate_records() -> list[dict[str, str]]:
    """给出 actual-object predicate 字段。"""
    return [
        {
            "predicate": "source_incidence",
            "meaning": "actual source atom 必须等于 formal key 指定的 source-atom multiplicity fiber。",
        },
        {
            "predicate": "occurrence_incidence",
            "meaning": "occurrence unit 必须真实落在该 source atom 的 signed occurrence incidence cell。",
        },
        {
            "predicate": "crt_representative",
            "meaning": "CRT coordinate 必须是 occurrence unit 的 primitive witness coordinate。",
        },
        {
            "predicate": "canonical_congruence_eval",
            "meaning": "canonical congruence equation 在该 CRT coordinate 上为真。",
        },
        {
            "predicate": "phase_endpoint_eval",
            "meaning": "phase-residue evaluation 必须给出同一端点对 r0,r* 与单位相位差。",
        },
        {
            "predicate": "signed_mass_match",
            "meaning": "actual signed mass 必须等于 W=A(delta_{r0}-delta_{r*})。",
        },
        {
            "predicate": "calibrated_pairing_match",
            "meaning": "actual phase pairing 必须等于 <W,phi>=A。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 actual-object-predicate 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeActualCircuitMaterializationImported",
            imported,
            False,
            "上一层剩余含 actual-circuit materialization、materialized capacity 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row("MultiplicityCapCarriedForwardAfterExchangeActualObjectPredicate", True, False, "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterExchangeActualObjectPredicate", True, False, "同点退化或零负载继续回流 singleton atom/SAE。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeActualObjectPredicate", True, False, "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeActualObjectPredicate", True, False, "反号债或镜像互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeActualObjectPredicate", True, False, "同号跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeActualObjectPredicate", True, False, "边界迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("PhaseResidueExchangeActualCircuitMaterializationImportedForPredicate", True, True, "导入同一 formal-unit key 与同一对象物化门。", MATERIALIZATION_IMPORT),
        row("PhaseResidueExchangeActualObjectTupleSchema", True, True, "实际对象写成一个七槽 tuple：source、occurrence、CRT、congruence、phase、signed mass、pairing。", OBJECT_TUPLE),
        row("PhaseResidueExchangeActualObjectCanonicalHash", True, True, "实际对象 hash 由 formal key 与七槽 tuple 确定，禁止后验换槽。", OBJECT_HASH),
        row("PhaseResidueExchangeActualObjectSourceIncidencePredicate", True, True, "source atom 槽必须满足 formal key 指定的 source incidence。", SOURCE_INCIDENCE),
        row("PhaseResidueExchangeActualObjectOccurrenceIncidencePredicate", True, True, "occurrence 槽必须真实落在同一 source incidence cell。", OCCURRENCE_INCIDENCE),
        row("PhaseResidueExchangeActualObjectCRTRepresentativePredicate", True, True, "CRT coordinate 槽必须是同一 occurrence 的 primitive witness representative。", CRT_REPRESENTATIVE),
        row("PhaseResidueExchangeActualObjectCongruenceEvaluationPredicate", True, True, "canonical congruence 槽必须在该 CRT representative 上求值为真。", CONGRUENCE_EVAL),
        row("PhaseResidueExchangeActualObjectPhaseEndpointPredicate", True, True, "phase evaluation 槽必须返回 r0,r* 与单位相位差。", PHASE_ENDPOINT),
        row("PhaseResidueExchangeActualObjectSignedMassPredicate", True, True, "signed mass 槽必须等于 W=A(delta_{r0}-delta_{r*})。", SIGNED_MASS_MATCH),
        row("PhaseResidueExchangeActualObjectCalibratedPairingPredicate", True, True, "calibrated pairing 槽必须等于 <W,phi>=A。", PAIRING_MATCH),
        row("PhaseResidueExchangeMissingActualObjectReturn", True, False, "若七槽 tuple 无 actual 代表，则回流 missing-object PDEC/cap。", MISSING_OBJECT),
        row("PhaseResidueExchangeDuplicateActualObjectReturn", True, False, "若同一 key 有两个不等 actual object，则回流 duplicate-object PDEC/cap。", DUPLICATE_OBJECT),
        row("PhaseResidueExchangeActualObjectSlotMismatchReturn", True, False, "若某槽不匹配，则回流 slot-mismatch PDEC/cap。", SLOT_MISMATCH),
        row("PhaseResidueExchangeActualObjectIncidencePredicatePacket", True, False, "若已有回流不支付，剩余就是 actual-object incidence predicate PDEC/cap。", PREDICATE_PACKET),
        row("NoAnonymousActualCircuitMaterializationAfterObjectPredicate", True, True, "actual-circuit materialization 不再是匿名黑箱；它只剩显式 incidence predicate 或已有回流。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterExchangeActualObjectPredicate", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeActualObjectPredicateStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、multiplicity cap、actual-object predicate、materialized capacity、bridge、amplitude、boundary 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 actual-object incidence predicate 或 materialized-circuit capacity。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "上一层把 phase-pairing circuit 压成 actual materialization 或 materialized capacity。"
        "本步继续打开 actual materialization：同一对象必须是一个七槽 actual tuple，"
        "并逐槽满足 source incidence、occurrence incidence、CRT representative、canonical congruence、"
        "phase endpoint、signed mass 与 calibrated pairing 谓词。缺对象、重复对象或槽位不匹配"
        "都被命名为 PDEC/cap 回流；若这些回流都不支付，剩余就是 actual-object incidence predicate "
        "PDEC/cap，或已经物化后的 capacity PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_actual_object_predicate_router",
        "status": "phase_residue_exchange_actual_circuit_materialization_reduced_to_object_incidence_predicate_or_materialized_capacity_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_actual_circuit_materialization_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_actual_object_tuple_schema_closed": True,
        "phase_residue_exchange_actual_object_canonical_hash_closed": True,
        "phase_residue_exchange_actual_object_source_incidence_predicate_closed": True,
        "phase_residue_exchange_actual_object_occurrence_incidence_predicate_closed": True,
        "phase_residue_exchange_actual_object_crt_representative_predicate_closed": True,
        "phase_residue_exchange_actual_object_congruence_evaluation_predicate_closed": True,
        "phase_residue_exchange_actual_object_phase_endpoint_predicate_closed": True,
        "phase_residue_exchange_actual_object_signed_mass_predicate_closed": True,
        "phase_residue_exchange_actual_object_calibrated_pairing_predicate_closed": True,
        "phase_residue_exchange_missing_actual_object_return_registered": True,
        "phase_residue_exchange_duplicate_actual_object_return_registered": True,
        "phase_residue_exchange_slot_mismatch_return_registered": True,
        "anonymous_actual_circuit_materialization_removed": True,
        "phase_residue_exchange_actual_object_incidence_predicate_proved": False,
        "phase_residue_exchange_materialized_circuit_capacity_pdec_cap_proved": False,
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
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "actual_object_predicates": predicate_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix phase-residue exchange phase-pairing actual-object-predicate 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_actual_circuit_materialization_imported={fmt_bool(cert['phase_residue_exchange_actual_circuit_materialization_imported'])}",
        f"phase_residue_exchange_actual_object_tuple_schema_closed={fmt_bool(cert['phase_residue_exchange_actual_object_tuple_schema_closed'])}",
        f"phase_residue_exchange_actual_object_canonical_hash_closed={fmt_bool(cert['phase_residue_exchange_actual_object_canonical_hash_closed'])}",
        f"phase_residue_exchange_actual_object_source_incidence_predicate_closed={fmt_bool(cert['phase_residue_exchange_actual_object_source_incidence_predicate_closed'])}",
        f"phase_residue_exchange_actual_object_occurrence_incidence_predicate_closed={fmt_bool(cert['phase_residue_exchange_actual_object_occurrence_incidence_predicate_closed'])}",
        f"phase_residue_exchange_actual_object_crt_representative_predicate_closed={fmt_bool(cert['phase_residue_exchange_actual_object_crt_representative_predicate_closed'])}",
        f"phase_residue_exchange_actual_object_phase_endpoint_predicate_closed={fmt_bool(cert['phase_residue_exchange_actual_object_phase_endpoint_predicate_closed'])}",
        f"phase_residue_exchange_actual_object_signed_mass_predicate_closed={fmt_bool(cert['phase_residue_exchange_actual_object_signed_mass_predicate_closed'])}",
        f"phase_residue_exchange_actual_object_calibrated_pairing_predicate_closed={fmt_bool(cert['phase_residue_exchange_actual_object_calibrated_pairing_predicate_closed'])}",
        "phase_residue_exchange_actual_object_incidence_predicate_proved=false",
        "phase_residue_exchange_materialized_circuit_capacity_pdec_cap_proved=false",
        "linear_witness_existence_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. actual materialization 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "same_formal_unit_key=true",
        "source_atom_slot=same key",
        "occurrence_unit_slot=same key",
        "crt_coordinate_slot=same key",
        "canonical_congruence_slot=same key",
        "phase_evaluation_slot=same key",
        "signed_mass_slot=W=A(delta_{r0}-delta_{r*})",
        "calibrated_pairing_slot=<W,phi>=A",
        "object_switch=0",
        "```",
        "",
        "## 2. actual-object 谓词",
        "",
        "| predicate | meaning |",
        "| --- | --- |",
    ]
    for record in cert["actual_object_predicates"]:
        lines.append(f"| `{record['predicate']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "实际对象 tuple 为：",
        "",
        "```text",
        "O=(source_atom, occurrence_unit, crt_coordinate, canonical_congruence, phase_evaluation, signed_mass, calibrated_pairing)",
        "actual_object_hash=H(formal_unit_key,O)",
        "missing_object -> ActualObjectIncidencePredicatePDECCap",
        "duplicate_object -> ActualObjectIncidencePredicatePDECCap",
        "slot_mismatch -> ActualObjectIncidencePredicatePDECCap",
        "all_predicates_hold -> materialized circuit capacity gate",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["previous_direct_attack_target"],
        "  -> " + reduced_target(cert["next_direct_attack_target"]).replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines += [
        "",
        "## 5. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 6. 诚实边界",
        "",
        "- 本证书没有证明 actual-object incidence predicate PDEC/cap。",
        "- 本证书没有证明 materialized-circuit capacity PDEC/cap。",
        "- 本证书没有证明 source-atom multiplicity-cap、endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 本证书没有证明线性相位/容量见证本身存在。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 7. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
