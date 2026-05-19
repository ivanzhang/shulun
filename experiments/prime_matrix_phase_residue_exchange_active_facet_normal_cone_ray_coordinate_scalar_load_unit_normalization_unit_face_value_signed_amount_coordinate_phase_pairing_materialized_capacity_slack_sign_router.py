#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing materialized-capacity-slack-sign 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.md
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
    "phase-pairing-materialized-capacity-slack-sign"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-materialized-capacity-slack-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
OLD_TARGET = f"{PREFIX}MaterializedCircuitCapacitySlackPDECCap"
NEGATIVE_TARGET = f"{PREFIX}MaterializedCircuitNegativeSlackPDECCap"
ZERO_TARGET = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"
NEW_TARGET = f"{NEGATIVE_TARGET}Or{ZERO_TARGET}"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeMaterializedCapacitySlackImportedLedger"
PREDICATE = "StableLadderEndpointOrbitActualObjectIncidencePredicateCarriedForwardAfterSlackSignLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeSlackSignLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeSlackSignLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSlackSignLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSlackSignLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSlackSignLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSlackSignLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeSlackSignLedger"

SLACK_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackImportedForSignLedger"
SIGN_TRICHOTOMY = "StableLadderEndpointOrbitPhaseResidueExchangeCapacitySlackSignTrichotomyLedger"
POSITIVE_ABSORB = "StableLadderEndpointOrbitPhaseResidueExchangePositiveSlackAbsorptionLedger"
NEGATIVE_DEFECT = "StableLadderEndpointOrbitPhaseResidueExchangeNegativeSlackDefectPacketLedger"
ZERO_EQUALITY = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityAtomPacketLedger"
NO_EQUALITY_CONTRADICTION = "StableLadderEndpointOrbitPhaseResidueExchangeNoStrictContradictionFromEqualityLedger"
NO_SIGN_MERGE = "StableLadderEndpointOrbitPhaseResidueExchangeNoSlackSignMergeLedger"
SIGN_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeSlackSignPacketLedger"
NO_ANON = "NoAnonymousMaterializedCapacitySlackAfterSignLedger"


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
    """把 capacity-slack 硬点替换为负 slack 或等号原子。"""
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
        SLACK_IMPORT,
        SIGN_TRICHOTOMY,
        POSITIVE_ABSORB,
        NEGATIVE_DEFECT,
        ZERO_EQUALITY,
        NO_EQUALITY_CONTRADICTION,
        NO_SIGN_MERGE,
        SIGN_PACKET,
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


def sign_records() -> list[dict[str, str]]:
    """给出 slack sign 字段。"""
    return [
        {"sign": "Sigma(O)>0", "meaning": "同一 actual object 的容量严格大于负载，直接容量吸收。"},
        {"sign": "Sigma(O)<0", "meaning": "同一 actual object 的真实负载超过容量，成为 negative-slack PDEC/cap。"},
        {"sign": "Sigma(O)=0", "meaning": "同一 actual object 正好临界，成为 boundary equality atom。"},
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 materialized-capacity-slack-sign 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeMaterializedCapacitySlackImported",
            imported,
            False,
            "上一层剩余含 actual-object predicate、materialized capacity slack 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row("ActualObjectIncidencePredicateCarriedForwardAfterSlackSign", True, False, "actual-object incidence predicate PDEC/cap 继续作为独立出口。", PREDICATE),
        row("MultiplicityCapCarriedForwardAfterExchangeSlackSign", True, False, "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterExchangeSlackSign", True, False, "同点退化或零负载继续回流 singleton atom/SAE。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSlackSign", True, False, "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSlackSign", True, False, "反号债或镜像互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSlackSign", True, False, "同号跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSlackSign", True, False, "边界迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("PhaseResidueExchangeCapacitySlackImportedForSign", True, True, "导入同一对象 slack Sigma(O)=C(O)-A。", SLACK_IMPORT),
        row("PhaseResidueExchangeCapacitySlackSignTrichotomy", True, True, "实数 slack 只有正、负、零三种符号分支。", SIGN_TRICHOTOMY),
        row("PhaseResidueExchangePositiveSlackAbsorption", True, True, "若 Sigma(O)>0，则该对象严格在容量内，本分支被吸收。", POSITIVE_ABSORB),
        row("PhaseResidueExchangeNegativeSlackDefectPacket", True, False, "若 Sigma(O)<0，则是真实超容量 negative-slack PDEC/cap。", NEGATIVE_DEFECT),
        row("PhaseResidueExchangeBoundaryEqualityAtomPacket", True, False, "若 Sigma(O)=0，则是临界等号原子，必须命名登记或排斥持久复现。", ZERO_EQUALITY),
        row("PhaseResidueExchangeNoStrictContradictionFromEquality", True, True, "等号不能被当作严格矛盾；必须单独处理。", NO_EQUALITY_CONTRADICTION),
        row("PhaseResidueExchangeNoSlackSignMerge", True, True, "正、负、零三支不能合并成匿名 capacity slack。", NO_SIGN_MERGE),
        row("PhaseResidueExchangeSlackSignPacket", True, False, "若正 slack 不吸收且已有回流不支付，剩余就是 negative slack 或 boundary equality atom。", SIGN_PACKET),
        row("NoAnonymousMaterializedCapacitySlackAfterSign", True, True, "materialized capacity slack 不再是匿名黑箱；它只剩负 slack 或等号原子。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterExchangeSlackSign", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangeSlackSignStillOpen", False, False, "仍未排斥 actual-object predicate、negative slack、boundary equality、singleton、full-cycle mean、multiplicity cap、bridge、amplitude、boundary 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 actual-object predicate、negative slack 或 boundary equality atom。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "materialized-capacity-slack 已把容量比较压成同一实际对象的 "
        "Sigma(O)=C(O)-A。本步把 slack 再按符号三分：正 slack 被容量吸收，"
        "负 slack 是真实超容量 PDEC/cap，零 slack 是临界等号原子。"
        "因此 capacity slack 不再能匿名保留，也不能把等号当成严格矛盾。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_router",
        "status": "phase_residue_exchange_materialized_capacity_slack_reduced_to_negative_slack_or_boundary_equality_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_materialized_capacity_slack_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_capacity_slack_sign_trichotomy_closed": True,
        "phase_residue_exchange_positive_slack_absorption_closed": True,
        "phase_residue_exchange_no_strict_contradiction_from_equality_closed": True,
        "phase_residue_exchange_no_slack_sign_merge_closed": True,
        "anonymous_materialized_capacity_slack_removed_after_sign": True,
        "phase_residue_exchange_negative_slack_pdec_cap_proved": False,
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
        "new_exits": [NEGATIVE_TARGET, ZERO_TARGET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "sign_records": sign_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix phase-residue exchange phase-pairing materialized-capacity-slack-sign 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_materialized_capacity_slack_imported={fmt_bool(cert['phase_residue_exchange_materialized_capacity_slack_imported'])}",
        f"phase_residue_exchange_capacity_slack_sign_trichotomy_closed={fmt_bool(cert['phase_residue_exchange_capacity_slack_sign_trichotomy_closed'])}",
        f"phase_residue_exchange_positive_slack_absorption_closed={fmt_bool(cert['phase_residue_exchange_positive_slack_absorption_closed'])}",
        f"phase_residue_exchange_no_strict_contradiction_from_equality_closed={fmt_bool(cert['phase_residue_exchange_no_strict_contradiction_from_equality_closed'])}",
        f"phase_residue_exchange_no_slack_sign_merge_closed={fmt_bool(cert['phase_residue_exchange_no_slack_sign_merge_closed'])}",
        "phase_residue_exchange_negative_slack_pdec_cap_proved=false",
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved=false",
        "phase_residue_exchange_actual_object_incidence_predicate_proved=false",
        "linear_witness_existence_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. slack 输入",
        "",
        "上一层已经给出同一对象 slack：",
        "",
        "```text",
        "L(O)=A=<W,phi>",
        "C(O)=capacity of the same materialized circuit",
        "Sigma(O)=C(O)-A",
        "formal_envelope_load=forbidden",
        "load_switch=0",
        "```",
        "",
        "## 2. 符号三分",
        "",
        "| sign | meaning |",
        "| --- | --- |",
    ]
    for record in cert["sign_records"]:
        lines.append(f"| `{record['sign']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "符号路由为：",
        "",
        "```text",
        "Sigma(O)>0 -> PositiveSlackAbsorption",
        "Sigma(O)<0 -> MaterializedCircuitNegativeSlackPDECCap",
        "Sigma(O)=0 -> MaterializedCircuitBoundaryEqualityAtomPDEC",
        "equality_is_not_strict_contradiction=true",
        "anonymous_slack_sign_merge=0",
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
        "- 本证书没有证明 materialized negative-slack PDEC/cap。",
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
