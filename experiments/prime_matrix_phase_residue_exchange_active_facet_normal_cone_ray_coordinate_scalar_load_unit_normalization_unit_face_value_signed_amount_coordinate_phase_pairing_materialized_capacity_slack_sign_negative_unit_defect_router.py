#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing negative-unit-defect 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_negative_unit_defect_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.md
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
    "phase-pairing-materialized-capacity-slack-sign-negative-unit-defect"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-materialized-capacity-slack-sign-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}MaterializedCircuitNegativeSlackPDECCap"
INTEGRALITY_TARGET = f"{PREFIX}MaterializedCircuitCapacityValueUnitIntegralityPDECCap"
UNIT_DEFECT_TARGET = f"{PREFIX}MaterializedCircuitUnitNegativeDefectPDECCap"
NEW_TARGET = f"{INTEGRALITY_TARGET}Or{UNIT_DEFECT_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSlackSignImportedForNegativeUnitDefectLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterNegativeUnitDefectLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterNegativeUnitDefectLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterNegativeUnitDefectLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterNegativeUnitDefectLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterNegativeUnitDefectLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterNegativeUnitDefectLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterNegativeUnitDefectLedger"
BOUNDARY_EQUALITY = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterNegativeUnitDefectLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterNegativeUnitDefectLedger"

NEGATIVE_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackImportedForUnitDefectLedger"
SAME_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackSameActualObjectLedger"
AMOUNT_UNIT = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackAmountUnitCountLedger"
CAPACITY_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackCapacityValueLedger"
UNIT_INTEGRALITY_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeCapacityValueUnitIntegralityGateLedger"
DEFICIT_FORMULA = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackDeficitFormulaLedger"
POSITIVE_DEFICIT = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackPositiveDeficitLedger"
UNIT_DEFECT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitNegativeDefectLedger"
NO_EPSILON = "StableLadderEndpointOrbitPhaseResidueExchangeNoInfinitesimalNegativeSlackLedger"
NO_REAL_ESCAPE = "NoAnonymousRealNegativeSlackAfterUnitDefectLedger"


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
    """把 negative-slack 硬点替换为单位整数容量门或单位负缺口。"""
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
        BOUNDARY_EQUALITY,
        NEGATIVE_IMPORT,
        SAME_OBJECT,
        AMOUNT_UNIT,
        CAPACITY_VALUE,
        UNIT_INTEGRALITY_GATE,
        DEFICIT_FORMULA,
        POSITIVE_DEFICIT,
        UNIT_DEFECT,
        NO_EPSILON,
        NO_REAL_ESCAPE,
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


def unit_defect_records() -> list[dict[str, str]]:
    """给出负 slack 单位化记录。"""
    return [
        {
            "field": "negative_slack",
            "meaning": "导入 Sigma(O)=C(O)-A<0，且容量和负载仍在同一 actual object 上读取。",
        },
        {
            "field": "deficit",
            "meaning": "定义 D(O)=A-C(O)=-Sigma(O)>0。",
        },
        {
            "field": "unit_integrality_gate",
            "meaning": "若 C(O) 不能作为单位面值下的同对象整数容量计数，则回流 capacity-value unit-integrality PDEC/cap。",
        },
        {
            "field": "unit_negative_defect",
            "meaning": "若 A 与 C(O) 都是单位整数计数，则 D(O) 为正整数，因此 D(O)>=1。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 negative-unit-defect 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeSlackSignImportedForNegativeUnitDefect",
            imported,
            False,
            "上一层已把 materialized capacity slack 化为 positive absorption、negative slack 或 boundary equality atom。",
            old_target or OLD_TARGET,
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterNegativeUnitDefect", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("MultiplicityCapCarriedForwardAfterNegativeUnitDefect", True, False, "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterNegativeUnitDefect", True, False, "endpoint singleton atom/SAE 继续前传。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterNegativeUnitDefect", True, False, "full-cycle mean atom/SAE 继续前传。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterNegativeUnitDefect", True, False, "bridge-cancellation PDEC/cap 继续前传。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterNegativeUnitDefect", True, False, "amplitude-depth PDEC/cap 继续前传。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterNegativeUnitDefect", True, False, "variation-boundary flux PDEC/cap 继续前传。", BOUNDARY),
        row("BoundaryEqualityAtomCarriedForwardAfterNegativeUnitDefect", True, False, "零 slack 临界等号原子不被本步误判为负缺口，继续作为独立硬点。", BOUNDARY_EQUALITY),
        row("PhaseResidueExchangeNegativeSlackImportedForUnitDefect", imported, False, "导入 Sigma(O)=C(O)-A<0 的负 slack 分支。", NEGATIVE_IMPORT),
        row("PhaseResidueExchangeNegativeSlackSameActualObject", True, True, "D(O)、A 与 C(O) 都绑定同一 actual object；不允许换对象补容量。", SAME_OBJECT),
        row("PhaseResidueExchangeNegativeSlackAmountUnitCount", True, True, "A 由 price-one signed amount coordinate 和 payment value 导入为单位负载计数。", AMOUNT_UNIT),
        row("PhaseResidueExchangeNegativeSlackCapacityValue", True, False, "C(O) 必须由同一 materialized circuit 的容量槽给出。", CAPACITY_VALUE),
        row("PhaseResidueExchangeCapacityValueUnitIntegralityGate", True, False, "若 C(O) 不是单位整数容量计数，则成为 capacity-value unit-integrality PDEC/cap。", UNIT_INTEGRALITY_GATE),
        row("PhaseResidueExchangeNegativeSlackDeficitFormula", True, True, "负 slack 等价于 D(O)=A-C(O)=-Sigma(O)>0。", DEFICIT_FORMULA),
        row("PhaseResidueExchangeNegativeSlackPositiveDeficit", True, True, "在单位整数容量门通过后，D(O) 是正整数，故 D(O)>=1。", POSITIVE_DEFICIT),
        row("PhaseResidueExchangeUnitNegativeDefect", True, False, "单位负缺口是至少一单位的真实容量赤字；本步登记但不排斥它。", UNIT_DEFECT),
        row("PhaseResidueExchangeNoInfinitesimalNegativeSlack", True, True, "负 slack 不能再作为实数无穷小误差逃逸；只能是容量值非整数或单位负缺口。", NO_EPSILON),
        row("NoAnonymousRealNegativeSlackAfterUnitDefect", True, True, "negative slack 不再是匿名实数缺陷；它被压成 integrality defect 或 D>=1。", NO_REAL_ESCAPE),
        row("SparseScaleLadderSAECarriedForwardAfterNegativeUnitDefect", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeNegativeUnitDefectStillOpen", False, False, "仍未排斥 actual-object predicate、capacity-value integrality defect、unit negative defect、boundary equality、endpoint 出口或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 actual-object predicate、unit negative defect、boundary equality 或 parallel outlets。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "slack-sign 层已经把正 slack 吸收，负 slack 写成 Sigma(O)=C(O)-A<0，"
        "零 slack 保留为 boundary equality atom。本步只处理负支：定义 "
        "D(O)=A-C(O)=-Sigma(O)。若 C(O) 不能在单位面值下作为同对象整数容量计数，"
        "则这是 capacity-value unit-integrality PDEC/cap；若该门通过，则 D(O) 是正整数，"
        "所以至少为一单位缺口。负 slack 不再能作为匿名实数微小误差保留。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_negative_unit_defect_router",
        "status": "phase_residue_exchange_negative_slack_reduced_to_capacity_integrality_or_unit_deficit_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_negative_slack_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_negative_slack_same_actual_object_closed": True,
        "phase_residue_exchange_negative_slack_deficit_formula_closed": True,
        "phase_residue_exchange_negative_slack_no_infinitesimal_escape_closed": True,
        "phase_residue_exchange_negative_slack_amount_unit_count_imported": True,
        "phase_residue_exchange_capacity_value_unit_integrality_proved": False,
        "phase_residue_exchange_unit_negative_defect_pdec_cap_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
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
        "new_exits": [INTEGRALITY_TARGET, UNIT_DEFECT_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "unit_defect_records": unit_defect_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange phase-pairing negative-unit-defect 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_negative_slack_imported={fmt_bool(cert['phase_residue_exchange_negative_slack_imported'])}",
        f"phase_residue_exchange_negative_slack_same_actual_object_closed={fmt_bool(cert['phase_residue_exchange_negative_slack_same_actual_object_closed'])}",
        f"phase_residue_exchange_negative_slack_deficit_formula_closed={fmt_bool(cert['phase_residue_exchange_negative_slack_deficit_formula_closed'])}",
        f"phase_residue_exchange_negative_slack_no_infinitesimal_escape_closed={fmt_bool(cert['phase_residue_exchange_negative_slack_no_infinitesimal_escape_closed'])}",
        f"phase_residue_exchange_capacity_value_unit_integrality_proved={fmt_bool(cert['phase_residue_exchange_capacity_value_unit_integrality_proved'])}",
        f"phase_residue_exchange_unit_negative_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_unit_negative_defect_pdec_cap_proved'])}",
        f"phase_residue_exchange_boundary_equality_atom_exclusion_proved={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_exclusion_proved'])}",
        f"phase_residue_exchange_actual_object_incidence_predicate_proved={fmt_bool(cert['phase_residue_exchange_actual_object_incidence_predicate_proved'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 负 slack 输入",
        "",
        "```text",
        "Sigma(O)=C(O)-A<0",
        "D(O)=A-C(O)=-Sigma(O)>0",
        "same_actual_object=true",
        "zero_slack_boundary_equality_atom=carried_forward",
        "```",
        "",
        "## 2. 单位缺口规整",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["unit_defect_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "负支路由为：",
            "",
            "```text",
            "Sigma(O)<0",
            "  -> if C(O) is not a same-object unit integer capacity:",
            "       MaterializedCircuitCapacityValueUnitIntegralityPDECCap",
            "  -> otherwise D(O)=A-C(O) in Z_{>=1}:",
            "       MaterializedCircuitUnitNegativeDefectPDECCap",
            "anonymous_real_epsilon_negative_slack=0",
            "```",
            "",
            "## 3. 新硬点",
            "",
            "```text",
            cert["previous_direct_attack_target"],
            "  -> " + " AND ".join(reduced_target(cert["next_direct_attack_target"]).split(" AND ")),
            "```",
            "",
            "## 4. 判定表",
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
            "## 5. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书没有证明 capacity-value unit-integrality PDEC/cap。",
            "- 本证书没有排斥 unit negative defect PDEC/cap。",
            "- 本证书没有排斥 boundary equality atom。",
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
