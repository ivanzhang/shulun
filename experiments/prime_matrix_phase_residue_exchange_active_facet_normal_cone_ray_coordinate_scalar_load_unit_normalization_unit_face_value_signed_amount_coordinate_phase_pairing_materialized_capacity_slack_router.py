#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing materialized-capacity-slack 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.md
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
    "phase-pairing-materialized-capacity-slack"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
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
OLD_TARGET = f"{PREFIX}MaterializedCircuitCapacityPDECCap"
NEW_TARGET = f"{PREFIX}MaterializedCircuitCapacitySlackPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeMaterializedCircuitCapacityImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterCapacitySlackLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeCapacitySlackLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeCapacitySlackLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCapacitySlackLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCapacitySlackLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCapacitySlackLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCapacitySlackLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeCapacitySlackLedger"

CAPACITY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeMaterializedCapacityImportedForSlackLedger"
SAME_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackSameActualObjectLedger"
ACTUAL_LOAD = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackActualLoadLedger"
CAPACITY_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackCapacityValueLedger"
SLACK_FORMULA = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackFormulaLedger"
POSITIVE_BRANCH = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackPositiveAbsorptionLedger"
NEGATIVE_BRANCH = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackNegativeDefectLedger"
ZERO_BRANCH = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackBoundaryEqualityAtomLedger"
NO_FORMAL_ENVELOPE = "StableLadderEndpointOrbitPhaseResidueExchangeNoFormalEnvelopeAfterCapacitySlackLedger"
NO_LOAD_SWITCH = "StableLadderEndpointOrbitPhaseResidueExchangeNoLoadSwitchAfterCapacitySlackLedger"
SLACK_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeMaterializedCapacitySlackPacketLedger"
NO_ANON = "NoAnonymousMaterializedCapacityAfterSlackLedger"


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
    """把 materialized-circuit capacity 硬点替换为 capacity-slack 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PREDICATE,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        CAPACITY_IMPORT,
        SAME_OBJECT,
        ACTUAL_LOAD,
        CAPACITY_VALUE,
        SLACK_FORMULA,
        POSITIVE_BRANCH,
        NEGATIVE_BRANCH,
        ZERO_BRANCH,
        NO_FORMAL_ENVELOPE,
        NO_LOAD_SWITCH,
        SLACK_PACKET,
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


def slack_records() -> list[dict[str, str]]:
    """给出 materialized-capacity slack 字段。"""
    return [
        {
            "field": "actual_load",
            "meaning": "同一 actual object 的负载为 L(O)=A=<W,phi>，不能改用 formal envelope。",
        },
        {
            "field": "capacity_value",
            "meaning": "同一 actual object 的容量记为 C(O)，必须由 materialized circuit 的真实槽位给出。",
        },
        {
            "field": "slack",
            "meaning": "定义 Sigma(O)=C(O)-A。",
        },
        {
            "field": "positive_slack",
            "meaning": "若 Sigma(O)>0，则该对象在容量内，被吸收。",
        },
        {
            "field": "negative_slack",
            "meaning": "若 Sigma(O)<0，则真实负载超容量，必须是 PDEC/cap 缺陷。",
        },
        {
            "field": "zero_slack",
            "meaning": "若 Sigma(O)=0，则是临界等号原子，必须命名登记，不能当作严格矛盾。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 materialized-capacity-slack 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeMaterializedCircuitCapacityImported",
            imported,
            False,
            "上一层剩余含 actual-object predicate、materialized-circuit capacity 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterCapacitySlack", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("MultiplicityCapCarriedForwardAfterExchangeCapacitySlack", True, False, "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterExchangeCapacitySlack", True, False, "同点退化或零负载继续回流 singleton atom/SAE。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCapacitySlack", True, False, "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCapacitySlack", True, False, "反号债或镜像互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCapacitySlack", True, False, "同号跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCapacitySlack", True, False, "边界迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("PhaseResidueExchangeMaterializedCapacityImportedForSlack", True, True, "导入同一 actual object 上的 materialized-circuit capacity 门。", CAPACITY_IMPORT),
        row("PhaseResidueExchangeCapacitySlackSameActualObject", True, True, "容量与负载必须读取同一个 actual object。", SAME_OBJECT),
        row("PhaseResidueExchangeCapacitySlackActualLoad", True, True, "实际负载固定为 A=<W,phi>=amount=payment_value=||W||_1/2。", ACTUAL_LOAD),
        row("PhaseResidueExchangeCapacitySlackCapacityValue", True, False, "容量 C(O) 必须由同一 materialized circuit 的真实槽位给出。", CAPACITY_VALUE),
        row("PhaseResidueExchangeCapacitySlackFormula", True, True, "slack 定义为 Sigma(O)=C(O)-A。", SLACK_FORMULA),
        row("PhaseResidueExchangeCapacitySlackPositiveAbsorption", True, False, "若 Sigma(O)>0，则容量侧吸收；仍需证明全局均为该分支或命名回流。", POSITIVE_BRANCH),
        row("PhaseResidueExchangeCapacitySlackNegativeDefect", True, False, "若 Sigma(O)<0，则是真实超容量 PDEC/cap。", NEGATIVE_BRANCH),
        row("PhaseResidueExchangeCapacitySlackBoundaryEqualityAtom", True, False, "若 Sigma(O)=0，则是临界等号原子，必须命名登记或排斥持久复现。", ZERO_BRANCH),
        row("PhaseResidueExchangeNoFormalEnvelopeAfterCapacitySlack", True, True, "容量比较不得使用 formal envelope 替代 actual load A。", NO_FORMAL_ENVELOPE),
        row("PhaseResidueExchangeNoLoadSwitchAfterCapacitySlack", True, True, "容量比较不得把 A 换成另一 actual object 的负载。", NO_LOAD_SWITCH),
        row("PhaseResidueExchangeMaterializedCapacitySlackPacket", True, False, "若已有回流不支付，剩余就是 materialized capacity slack PDEC/cap。", SLACK_PACKET),
        row("NoAnonymousMaterializedCapacityAfterSlack", True, True, "materialized capacity 不再是匿名黑箱；它只剩同对象 slack 不等式。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterExchangeCapacitySlack", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeCapacitySlackStillOpen", False, False, "仍未排斥 actual-object predicate、capacity slack、singleton、full-cycle mean、multiplicity cap、bridge、amplitude、boundary 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 actual-object predicate 或 materialized capacity slack。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "actual-object-predicate 层之后，容量侧只有在同一 actual object 已物化时才有意义。"
        "本步把 materialized-circuit capacity 压成同对象 slack：L(O)=A，C(O) 为同一对象容量，"
        "Sigma(O)=C(O)-A。正 slack 吸收，负 slack 是真实超容量 PDEC/cap，零 slack 是临界等号原子。"
        "formal envelope、其他对象负载或后验换载不再是可用出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_router",
        "status": "phase_residue_exchange_materialized_circuit_capacity_reduced_to_same_object_slack_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_materialized_circuit_capacity_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_capacity_slack_same_actual_object_closed": True,
        "phase_residue_exchange_capacity_slack_actual_load_closed": True,
        "phase_residue_exchange_capacity_slack_formula_closed": True,
        "phase_residue_exchange_no_formal_envelope_after_capacity_slack_closed": True,
        "phase_residue_exchange_no_load_switch_after_capacity_slack_closed": True,
        "anonymous_materialized_capacity_removed_after_slack": True,
        "phase_residue_exchange_capacity_value_bound_proved": False,
        "phase_residue_exchange_materialized_capacity_slack_pdec_cap_proved": False,
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
        "old_exit": OLD_TARGET,
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "slack_records": slack_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix phase-residue exchange phase-pairing materialized-capacity-slack 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_materialized_circuit_capacity_imported={fmt_bool(cert['phase_residue_exchange_materialized_circuit_capacity_imported'])}",
        f"phase_residue_exchange_capacity_slack_same_actual_object_closed={fmt_bool(cert['phase_residue_exchange_capacity_slack_same_actual_object_closed'])}",
        f"phase_residue_exchange_capacity_slack_actual_load_closed={fmt_bool(cert['phase_residue_exchange_capacity_slack_actual_load_closed'])}",
        f"phase_residue_exchange_capacity_slack_formula_closed={fmt_bool(cert['phase_residue_exchange_capacity_slack_formula_closed'])}",
        f"phase_residue_exchange_no_formal_envelope_after_capacity_slack_closed={fmt_bool(cert['phase_residue_exchange_no_formal_envelope_after_capacity_slack_closed'])}",
        f"phase_residue_exchange_no_load_switch_after_capacity_slack_closed={fmt_bool(cert['phase_residue_exchange_no_load_switch_after_capacity_slack_closed'])}",
        "phase_residue_exchange_capacity_value_bound_proved=false",
        "phase_residue_exchange_materialized_capacity_slack_pdec_cap_proved=false",
        "phase_residue_exchange_actual_object_incidence_predicate_proved=false",
        "linear_witness_existence_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. materialized capacity 输入",
        "",
        "上一层 actual object 通过后，容量比较必须读取同一个对象：",
        "",
        "```text",
        "O=(source_atom, occurrence_unit, crt_coordinate, canonical_congruence, phase_evaluation, signed_mass, calibrated_pairing)",
        "L(O)=A=<W,phi>",
        "A=amount=payment_value=||W||_1/2",
        "C(O)=capacity of the same materialized circuit",
        "```",
        "",
        "## 2. slack 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["slack_records"]:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "同对象 slack 形式为：",
        "",
        "```text",
        "Sigma(O)=C(O)-A",
        "Sigma(O)>0 -> absorbed by capacity",
        "Sigma(O)<0 -> materialized capacity slack PDEC/cap",
        "Sigma(O)=0 -> boundary equality atom",
        "formal_envelope_load=forbidden",
        "load_switch=0",
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
        "- 本证书没有证明 materialized capacity slack PDEC/cap。",
        "- 本证书没有证明 actual-object incidence predicate PDEC/cap。",
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
