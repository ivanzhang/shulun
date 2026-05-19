#!/usr/bin/env python3
"""生成 phase-residue exchange normal-cone ray-coordinate scalar-load 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeRayCoordinateImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeRayCoordinateScalarLoadLedger"
RAY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateImportedForScalarLoadLedger"
POSITIVE_SCALAR = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinatePositiveScalarLoadLedger"
RANK_ONE = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateRankOneSupportLedger"
PAIRING_EQUALS_LOAD = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateScalarPairingEqualsLoadLedger"
HALF_TV_EQUALS_LOAD = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateHalfTotalVariationEqualsLoadLedger"
UNIT_RATIO = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateUnitSaturationRatioLedger"
NO_VECTOR_GEOMETRY = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateNoResidualVectorGeometryLedger"
SCALAR_PAYMENT = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinatePDECCapReducedToScalarLoadLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadCollisionOrZeroExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadOrientationLedger"
NO_RAY = "StableLadderEndpointOrbitPhaseResidueNoAnonymousRayCoordinateAfterScalarLoadLedger"
SCALAR_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateScalarLoadPacketLedger"
NO_ANON = "NoAnonymousRayCoordinateAfterScalarLoadLedger"


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
    """把 ray-coordinate 硬点替换为 scalar-load 硬点。"""
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
        RAY_IMPORT,
        POSITIVE_SCALAR,
        RANK_ONE,
        PAIRING_EQUALS_LOAD,
        HALF_TV_EQUALS_LOAD,
        UNIT_RATIO,
        NO_VECTOR_GEOMETRY,
        SCALAR_PAYMENT,
        COLLISION_EXIT,
        ORIENTATION,
        NO_RAY,
        SCALAR_PACKET,
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


def scalar_load_records() -> list[dict[str, str]]:
    """给出 scalar-load 字段。"""
    return [
        {
            "field": "positive_scalar_load",
            "meaning": "ray coordinate 的唯一正坐标就是 A=lambda>0。",
        },
        {
            "field": "rank_one_support",
            "meaning": "所有几何自由度冻结在同一个生成元 n_e=[r0]-[r*] 上。",
        },
        {
            "field": "pairing_equals_load",
            "meaning": "<div,phi>=A，因此势函数配对负载等于标量 A。",
        },
        {
            "field": "half_total_variation_equals_load",
            "meaning": "||div||_1/2=A，因此边界总变差的一半等于同一标量 A。",
        },
        {
            "field": "unit_saturation_ratio",
            "meaning": "<div,phi>/(||div||_1/2)=1，剩余不是松弛比例问题。",
        },
        {
            "field": "no_residual_vector_geometry",
            "meaning": "无横向法锥分量、无第二方向、无隐藏相位几何参数。",
        },
        {
            "field": "scalar_payment_reduction",
            "meaning": "若并行出口不支付，PDEC/cap 必须直接支付这个一维正标量负载。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r* 或 A=0，标量负载退化并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 scalar-load 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeNormalConeRayCoordinateImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange active-facet normal-cone ray-coordinate circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "同点退化或零负载时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateImportedForScalarLoad",
            True,
            True,
            "导入 div=lambda n_e、lambda=A>0、<div,phi>=A、||div||_1=2A。",
            RAY_IMPORT,
        ),
        row(
            "PhaseResidueExchangeRayCoordinatePositiveScalarLoad",
            True,
            True,
            "唯一 ray coordinate 是正标量 A=lambda>0。",
            POSITIVE_SCALAR,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateRankOneSupport",
            True,
            True,
            "法锥对象只有一个生成元 n_e，不再携带多方向几何选择。",
            RANK_ONE,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateScalarPairingEqualsLoad",
            True,
            True,
            "边界势函数配对等于同一 scalar load：<div,phi>=A。",
            PAIRING_EQUALS_LOAD,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateHalfTotalVariationEqualsLoad",
            True,
            True,
            "边界总变差的一半等于同一 scalar load：||div||_1/2=A。",
            HALF_TV_EQUALS_LOAD,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateUnitSaturationRatio",
            True,
            True,
            "配对负载与 half-TV 负载比例为 1，排除匿名松弛比例。",
            UNIT_RATIO,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateNoResidualVectorGeometry",
            True,
            True,
            "无横向法锥分量、无第二方向、无隐藏相位几何参数。",
            NO_VECTOR_GEOMETRY,
        ),
        row(
            "PhaseResidueExchangeRayCoordinatePDECCapReducedToScalarLoad",
            True,
            True,
            "若已有出口不支付，PDEC/cap 的待支付对象就是一维正标量负载 A。",
            SCALAR_PAYMENT,
        ),
        row(
            "PhaseResidueExchangeScalarLoadCollisionOrZeroExit",
            True,
            True,
            "若 r0=r* 或 A=0，标量负载退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeScalarLoadOrientation",
            True,
            True,
            "标量 A 仍沿 source -> root 的已定向生成元 n_e 支付。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousRayCoordinateAfterScalarLoad",
            True,
            True,
            "ray-coordinate 口径被删除；剩余是命名 scalar-load 支付证书。",
            NO_RAY,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateScalarLoadPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange ray-coordinate scalar-load circuit PDEC/cap。",
            SCALAR_PACKET,
        ),
        row(
            "NoAnonymousRayCoordinateAfterScalarLoad",
            True,
            True,
            "唯一正射线坐标被压成标量负载 A 及两个等价支付读数。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeRayCoordinateScalarLoad",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeScalarLoadStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、scalar-load、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange scalar-load circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    latest_basis = replace_latest_basis(previous, reduced)
    rows = build_rows(previous, new_target)

    plain = (
        "phase-residue exchange normal-cone ray-coordinate 已把剩余写成 "
        "div=lambda n_e、lambda=A>0、<div,phi>=A、||div||_1=2A。"
        "本步删除 ray-coordinate 作为黑箱的口径，把非退化对象登记为单一正标量负载 A："
        "pairing_load=<div,phi>=A，variation_load=||div||_1/2=A，二者比例为 1，"
        "并且无横向法锥分量、无第二方向、无隐藏相位几何参数。若 r0=r* 或 A=0，"
        "标量负载退化并回流 singleton/degenerate 出口。剩余反例不再是匿名 ray-coordinate，"
        "而必须表现为 scalar-load circuit PDEC/cap 或已有出口。"
    )

    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_router",
        "status": "phase_residue_exchange_normal_cone_ray_coordinate_reduced_to_scalar_load_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_normal_cone_ray_coordinate_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_ray_coordinate_positive_scalar_load_closed": True,
        "phase_residue_exchange_ray_coordinate_rank_one_support_closed": True,
        "phase_residue_exchange_ray_coordinate_scalar_pairing_equals_load_closed": True,
        "phase_residue_exchange_ray_coordinate_half_total_variation_equals_load_closed": True,
        "phase_residue_exchange_ray_coordinate_unit_saturation_ratio_closed": True,
        "phase_residue_exchange_ray_coordinate_no_residual_vector_geometry_closed": True,
        "phase_residue_exchange_ray_coordinate_pdec_cap_reduced_to_scalar_load_closed": True,
        "phase_residue_no_anonymous_ray_coordinate_after_scalar_load_closed": True,
        "anonymous_ray_coordinate_removed_after_scalar_load": True,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_circuit_pdec_cap_proved": False,
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
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": latest_basis,
        "scalar_load_records": scalar_load_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    rows = cert["gates"]
    records = cert["scalar_load_records"]
    lines = [
        "# Prime Matrix phase-residue exchange active facet normal cone ray coordinate scalar load 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_normal_cone_ray_coordinate_imported={fmt_bool(cert['phase_residue_exchange_normal_cone_ray_coordinate_imported'])}",
        f"phase_residue_exchange_ray_coordinate_positive_scalar_load_closed={fmt_bool(cert['phase_residue_exchange_ray_coordinate_positive_scalar_load_closed'])}",
        f"phase_residue_exchange_ray_coordinate_rank_one_support_closed={fmt_bool(cert['phase_residue_exchange_ray_coordinate_rank_one_support_closed'])}",
        f"phase_residue_exchange_ray_coordinate_scalar_pairing_equals_load_closed={fmt_bool(cert['phase_residue_exchange_ray_coordinate_scalar_pairing_equals_load_closed'])}",
        f"phase_residue_exchange_ray_coordinate_half_total_variation_equals_load_closed={fmt_bool(cert['phase_residue_exchange_ray_coordinate_half_total_variation_equals_load_closed'])}",
        f"phase_residue_exchange_ray_coordinate_unit_saturation_ratio_closed={fmt_bool(cert['phase_residue_exchange_ray_coordinate_unit_saturation_ratio_closed'])}",
        f"phase_residue_exchange_ray_coordinate_no_residual_vector_geometry_closed={fmt_bool(cert['phase_residue_exchange_ray_coordinate_no_residual_vector_geometry_closed'])}",
        "linear_witness_existence_proved=false",
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_circuit_pdec_cap_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. ray-coordinate 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "n_e=[r0]-[r*]",
        "N_e={lambda n_e: lambda>=0}",
        "div=lambda n_e",
        "lambda=A>0",
        "transverse_component=0",
        "<div,phi>=lambda(phi(r0)-phi(r*))=A",
        "||div||_1=2lambda=2A",
        "A C_Pi=W",
        "```",
        "",
        "## 2. scalar load 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in records:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "非退化时 scalar-load 证书为：",
        "",
        "```text",
        "scalar_load=A=lambda>0",
        "rank_one_generator=n_e=[r0]-[r*]",
        "pairing_load=<div,phi>=A",
        "variation_load=||div||_1/2=A",
        "unit_saturation_ratio=pairing_load/variation_load=1",
        "residual_vector_geometry=0",
        "A C_Pi=W",
        "```",
        "",
        "若 `r0=r*` 或 `A=0`，则 scalar load 退化并回流 singleton/degenerate 出口。",
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
    for item in rows:
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
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 phase-residue exchange active-facet normal-cone ray-coordinate scalar-load circuit PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
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
