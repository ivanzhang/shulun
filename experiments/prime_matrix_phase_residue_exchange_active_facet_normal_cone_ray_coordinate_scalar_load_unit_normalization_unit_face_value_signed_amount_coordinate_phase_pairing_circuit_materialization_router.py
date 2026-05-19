#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing circuit-materialization 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_materialization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.md
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
    "phase-pairing-circuit-materialization"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}CircuitPDECCap"
MATERIALIZATION_TARGET = f"{PREFIX}ActualCircuitMaterializationPDECCap"
CAPACITY_TARGET = f"{PREFIX}MaterializedCircuitCapacityPDECCap"
NEW_TARGET = f"{MATERIALIZATION_TARGET}Or{CAPACITY_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeCircuitMaterializationLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeCircuitMaterializationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCircuitMaterializationLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCircuitMaterializationLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCircuitMaterializationLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCircuitMaterializationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeCircuitMaterializationLedger"

PAIRING_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingImportedForCircuitMaterializationLedger"
SAME_KEY = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationSameFormalUnitKeyLedger"
SOURCE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationSourceAtomSlotLedger"
OCCURRENCE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationOccurrenceUnitSlotLedger"
CRT_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationCRTCoordinateSlotLedger"
CONGRUENCE_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationCanonicalCongruenceSlotLedger"
PHASE_EVAL_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationPhaseEvaluationSlotLedger"
SIGNED_MASS_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationSignedMassSlotLedger"
PAIRING_SLOT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationCalibratedPairingSlotLedger"
SAME_ACTUAL_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeCircuitMaterializationSameActualObjectGateLedger"
NO_OBJECT_SWITCH = "StableLadderEndpointOrbitPhaseResidueExchangeNoObjectSwitchAfterPhasePairingLedger"
MATERIALIZATION_DEFECT = "StableLadderEndpointOrbitPhaseResidueExchangeActualCircuitMaterializationDefectReturnLedger"
CAPACITY_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeMaterializedCircuitCapacityGateLedger"
CAPACITY_INPUT = "StableLadderEndpointOrbitPhaseResidueExchangeMaterializedCircuitCapacityInputLedger"
NO_ANON = "NoAnonymousPhasePairingCircuitAfterMaterializationGateLedger"


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
    """把 phase-pairing circuit 硬点替换为物化门与容量门。"""
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
        PAIRING_IMPORT,
        SAME_KEY,
        SOURCE_SLOT,
        OCCURRENCE_SLOT,
        CRT_SLOT,
        CONGRUENCE_SLOT,
        PHASE_EVAL_SLOT,
        SIGNED_MASS_SLOT,
        PAIRING_SLOT,
        SAME_ACTUAL_OBJECT,
        NO_OBJECT_SWITCH,
        MATERIALIZATION_DEFECT,
        CAPACITY_GATE,
        CAPACITY_INPUT,
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


def materialization_records() -> list[dict[str, str]]:
    """给出同一对象物化门字段。"""
    return [
        {
            "field": "same_formal_unit_key",
            "meaning": "source atom、occurrence unit、CRT coordinate、canonical congruence、phase evaluation、signed mass 与 phase pairing 必须共享同一个 formal-unit key。",
        },
        {
            "field": "source_atom_slot",
            "meaning": "source-atom multiplicity fiber 是 phase-pairing circuit 的源槽，不可替换为另一条链的源。",
        },
        {
            "field": "occurrence_unit_slot",
            "meaning": "signed occurrence unit incidence cell 必须是同一源槽的实际出现单元。",
        },
        {
            "field": "crt_coordinate_slot",
            "meaning": "primitive witness CRT coordinate 必须承载同一 occurrence unit 的相位坐标。",
        },
        {
            "field": "canonical_congruence_slot",
            "meaning": "canonical congruence equation 必须在同一 CRT coordinate 上求值。",
        },
        {
            "field": "phase_evaluation_slot",
            "meaning": "phase-residue evaluation atom 必须给出同一二端点相位差 phi(r0)-phi(r*)=1。",
        },
        {
            "field": "signed_mass_slot",
            "meaning": "signed mass 必须仍是 W=A(delta_{r0}-delta_{r*})，不能换成另一个二点对。",
        },
        {
            "field": "calibrated_pairing_slot",
            "meaning": "待支付值必须仍为 <W,phi>=A，与 amount、payment value、half-L1 相同。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 circuit-materialization 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    rows = [
        row(
            "PhaseResidueExchangePhasePairingCircuitImported",
            imported,
            False,
            "上一层剩余含 phase-pairing circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row("MultiplicityCapCarriedForwardAfterExchangeCircuitMaterialization", True, False, "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterExchangeCircuitMaterialization", True, False, "同点退化或零负载继续回流 singleton atom/SAE。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCircuitMaterialization", True, False, "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCircuitMaterialization", True, False, "反号债或镜像互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCircuitMaterialization", True, False, "同号跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCircuitMaterialization", True, False, "边界迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("PhaseResidueExchangePhasePairingImportedForCircuitMaterialization", True, True, "导入 W=A(delta_{r0}-delta_{r*}) 与 <W,phi>=A 的校准 phase-pairing 证书。", PAIRING_IMPORT),
        row("PhaseResidueExchangeCircuitMaterializationSameFormalUnitKey", True, True, "所有 circuit 字段必须挂在同一个 formal-unit key 上。", SAME_KEY),
        row("PhaseResidueExchangeCircuitMaterializationSourceAtomSlot", True, True, "source atom 槽位被固定，不能从另一条源链借用。", SOURCE_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationOccurrenceUnitSlot", True, True, "signed occurrence unit incidence cell 必须是同一 source atom 的实际出现槽。", OCCURRENCE_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationCRTCoordinateSlot", True, True, "primitive witness CRT coordinate 必须与 occurrence unit 同对象。", CRT_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationCanonicalCongruenceSlot", True, True, "canonical congruence equation 必须在同一 CRT coordinate 上求值。", CONGRUENCE_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationPhaseEvaluationSlot", True, True, "phase-residue evaluation atom 必须给出同一端点对的单位相位差。", PHASE_EVAL_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationSignedMassSlot", True, True, "signed mass 槽仍为 W=A(delta_{r0}-delta_{r*})。", SIGNED_MASS_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationCalibratedPairingSlot", True, True, "calibrated pairing 槽仍为 <W,phi>=A。", PAIRING_SLOT),
        row("PhaseResidueExchangeCircuitMaterializationSameActualObjectGate", True, False, "同一 formal-unit key 还必须证明为同一个 actual CRT/fiber 对象；这是新的物化门。", MATERIALIZATION_TARGET),
        row("PhaseResidueExchangeNoObjectSwitchAfterPhasePairing", True, True, "若对象切换，则不能留在 phase-pairing circuit 内，只能转入命名物化缺陷。", NO_OBJECT_SWITCH),
        row("PhaseResidueExchangeActualCircuitMaterializationDefectReturn", True, False, "若任一槽不能实际同物化，则剩余是 actual-circuit materialization PDEC/cap。", MATERIALIZATION_DEFECT),
        row("PhaseResidueExchangeMaterializedCircuitCapacityGate", True, False, "若同物化成立，仍需证明 materialized circuit 的容量帽。", CAPACITY_TARGET),
        row("PhaseResidueExchangeMaterializedCircuitCapacityInput", True, False, "容量帽必须使用同一 actual circuit 上的 A，而非 formal envelope 或外部替代负载。", CAPACITY_INPUT),
        row("NoAnonymousPhasePairingCircuitAfterMaterializationGate", True, True, "phase-pairing circuit 不再是匿名黑箱；它只剩实际物化缺陷或物化后容量帽。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterExchangeCircuitMaterialization", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCircuitMaterializationStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、multiplicity cap、actual materialization、materialized capacity、bridge、amplitude、boundary 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 actual-circuit materialization 或 materialized-circuit capacity。", new_target),
    ]
    return rows


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "phase-pairing 已把非退化剩余校准为同一二端点数值 A。"
        "本步不排斥该 circuit PDEC/cap，而是把 circuit 黑箱拆成同一对象纪律："
        "source atom、occurrence unit、CRT coordinate、canonical congruence、phase evaluation、"
        "signed mass 与 calibrated pairing 必须共享同一个 formal-unit key，并且必须物化为同一个 "
        "actual CRT/fiber 对象。若不能同物化，剩余是 actual-circuit materialization PDEC/cap；"
        "若能同物化，剩余是 materialized-circuit capacity PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_materialization_router",
        "status": "phase_residue_exchange_phase_pairing_circuit_reduced_to_actual_materialization_or_materialized_capacity_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_phase_pairing_circuit_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_circuit_same_formal_unit_key_schema_closed": True,
        "phase_residue_exchange_circuit_source_atom_slot_closed": True,
        "phase_residue_exchange_circuit_occurrence_unit_slot_closed": True,
        "phase_residue_exchange_circuit_crt_coordinate_slot_closed": True,
        "phase_residue_exchange_circuit_canonical_congruence_slot_closed": True,
        "phase_residue_exchange_circuit_phase_evaluation_slot_closed": True,
        "phase_residue_exchange_circuit_signed_mass_slot_closed": True,
        "phase_residue_exchange_circuit_calibrated_pairing_slot_closed": True,
        "phase_residue_exchange_no_object_switch_after_phase_pairing_closed": True,
        "anonymous_phase_pairing_circuit_removed_after_materialization_gate": True,
        "phase_residue_exchange_actual_circuit_materialization_proved": False,
        "phase_residue_exchange_materialized_circuit_capacity_pdec_cap_proved": False,
        "phase_residue_exchange_phase_pairing_circuit_pdec_cap_proved": False,
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
        "new_exits": [MATERIALIZATION_TARGET, CAPACITY_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "materialization_records": materialization_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix phase-residue exchange phase-pairing circuit-materialization 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_phase_pairing_circuit_imported={fmt_bool(cert['phase_residue_exchange_phase_pairing_circuit_imported'])}",
        f"phase_residue_exchange_circuit_same_formal_unit_key_schema_closed={fmt_bool(cert['phase_residue_exchange_circuit_same_formal_unit_key_schema_closed'])}",
        f"phase_residue_exchange_circuit_source_atom_slot_closed={fmt_bool(cert['phase_residue_exchange_circuit_source_atom_slot_closed'])}",
        f"phase_residue_exchange_circuit_occurrence_unit_slot_closed={fmt_bool(cert['phase_residue_exchange_circuit_occurrence_unit_slot_closed'])}",
        f"phase_residue_exchange_circuit_crt_coordinate_slot_closed={fmt_bool(cert['phase_residue_exchange_circuit_crt_coordinate_slot_closed'])}",
        f"phase_residue_exchange_circuit_phase_evaluation_slot_closed={fmt_bool(cert['phase_residue_exchange_circuit_phase_evaluation_slot_closed'])}",
        f"phase_residue_exchange_circuit_signed_mass_slot_closed={fmt_bool(cert['phase_residue_exchange_circuit_signed_mass_slot_closed'])}",
        f"phase_residue_exchange_circuit_calibrated_pairing_slot_closed={fmt_bool(cert['phase_residue_exchange_circuit_calibrated_pairing_slot_closed'])}",
        f"phase_residue_exchange_no_object_switch_after_phase_pairing_closed={fmt_bool(cert['phase_residue_exchange_no_object_switch_after_phase_pairing_closed'])}",
        "phase_residue_exchange_actual_circuit_materialization_proved=false",
        "phase_residue_exchange_materialized_circuit_capacity_pdec_cap_proved=false",
        "phase_residue_exchange_phase_pairing_circuit_pdec_cap_proved=false",
        "linear_witness_existence_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. phase-pairing 输入",
        "",
        "上一层已经锁定：",
        "",
        "```text",
        "W=A(delta_{r0}-delta_{r*})",
        "phi(r0)-phi(r*)=1",
        "<W,phi>=A(phi(r0)-phi(r*))=A",
        "phase_pairing_value=A",
        "amount=A",
        "payment_value=A",
        "||W||_1/2=A",
        "phase_rescale=0",
        "sign_mismatch=0",
        "phase_pairing_support={r0,r*}",
        "```",
        "",
        "## 2. circuit materialization 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["materialization_records"]:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "同一对象物化门为：",
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
        "若任一槽不能在同一个 actual CRT/fiber 对象上物化，则回流 actual-circuit materialization PDEC/cap。若同物化成立，剩余就是 materialized-circuit capacity PDEC/cap。",
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
        "- 本证书没有证明 actual-circuit materialization PDEC/cap。",
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
