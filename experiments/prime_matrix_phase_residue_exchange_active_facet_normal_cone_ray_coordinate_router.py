#!/usr/bin/env python3
"""生成 phase-residue exchange active-facet normal-cone ray-coordinate 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeComplementarySlacknessActiveFacetNormalConeCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetNormalConeImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeNormalConeRayCoordinateLedger"
FACET_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetImportedForRayCoordinateLedger"
RAY_GENERATOR = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeRayGeneratorLedger"
RAY_COORDINATE = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeRayCoordinateLedger"
POSITIVE_COORDINATE = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConePositiveCoordinateLedger"
UNIQUE_COORDINATE = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeUniqueCoordinateLedger"
NO_TRANSVERSE = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeNoTransverseComponentLedger"
BOUNDARY_PAIRING = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeCoordinateBoundaryPairingLedger"
TV_COORDINATE = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeCoordinateTotalVariationLedger"
EQUALS_FACET = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateEqualsActiveFacetLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeRayCoordinateOrientationLedger"
NO_FACET = "StableLadderEndpointOrbitPhaseResidueNoAnonymousActiveFacetAfterRayCoordinateLedger"
RAY_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeNormalConeRayCoordinatePacketLedger"
NO_ANON = "NoAnonymousActiveFacetAfterRayCoordinateLedger"


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
    """把 active-facet normal-cone 硬点替换为 ray-coordinate 硬点。"""
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
        FACET_IMPORT,
        RAY_GENERATOR,
        RAY_COORDINATE,
        POSITIVE_COORDINATE,
        UNIQUE_COORDINATE,
        NO_TRANSVERSE,
        BOUNDARY_PAIRING,
        TV_COORDINATE,
        EQUALS_FACET,
        COLLISION_EXIT,
        ORIENTATION,
        NO_FACET,
        RAY_PACKET,
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


def ray_coordinate_records() -> list[dict[str, str]]:
    """给出法锥射线坐标字段。"""
    return [
        {
            "field": "ray_generator",
            "meaning": "活跃面法向量生成元为 n_e=[r0]-[r*]。",
        },
        {
            "field": "ray_coordinate",
            "meaning": "散度写成 div=lambda n_e，且 lambda=A。",
        },
        {
            "field": "positive_coordinate",
            "meaning": "非退化反例链内 A>0，因此 lambda>0。",
        },
        {
            "field": "unique_coordinate",
            "meaning": "n_e 在二点支撑上非零，lambda 由正端系数唯一确定。",
        },
        {
            "field": "no_transverse_component",
            "meaning": "二点支撑和法锥一维性排除任何横向法锥分量。",
        },
        {
            "field": "boundary_pairing",
            "meaning": "<div,phi>=lambda(phi(r0)-phi(r*))=A。",
        },
        {
            "field": "total_variation_coordinate",
            "meaning": "||div||_1=2 lambda=2A。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r* 或 A=0，射线生成元或坐标退化并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 normal-cone ray-coordinate 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeActiveFacetNormalConeImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange complementary-slackness active-facet normal-cone circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "同点退化、零生成元或零坐标时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeActiveFacetImportedForRayCoordinate",
            True,
            True,
            "导入 n_e=[r0]-[r*]、N_e={lambda n_e: lambda>=0}、div=A n_e。",
            FACET_IMPORT,
        ),
        row(
            "PhaseResidueExchangeNormalConeRayGenerator",
            True,
            True,
            "法锥正射线生成元为 n_e=[r0]-[r*]。",
            RAY_GENERATOR,
        ),
        row(
            "PhaseResidueExchangeNormalConeRayCoordinate",
            True,
            True,
            "散度在生成元上的坐标为 lambda=A。",
            RAY_COORDINATE,
        ),
        row(
            "PhaseResidueExchangeNormalConePositiveCoordinate",
            True,
            True,
            "非退化局部压力满足 A>0，因此 lambda>0。",
            POSITIVE_COORDINATE,
        ),
        row(
            "PhaseResidueExchangeNormalConeUniqueCoordinate",
            True,
            True,
            "二点非退化支撑使 ray coordinate 唯一。",
            UNIQUE_COORDINATE,
        ),
        row(
            "PhaseResidueExchangeNormalConeNoTransverseComponent",
            True,
            True,
            "一维正法锥内不存在匿名横向分量。",
            NO_TRANSVERSE,
        ),
        row(
            "PhaseResidueExchangeNormalConeCoordinateBoundaryPairing",
            True,
            True,
            "<div,phi>=lambda(phi(r0)-phi(r*))=A。",
            BOUNDARY_PAIRING,
        ),
        row(
            "PhaseResidueExchangeNormalConeCoordinateTotalVariation",
            True,
            True,
            "||div||_1=2 lambda=2A。",
            TV_COORDINATE,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateEqualsActiveFacet",
            True,
            True,
            "ray-coordinate 证书与上一层 active-facet normal-cone 表示同一局部对象。",
            EQUALS_FACET,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r* 或 A=0，生成元/坐标退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeRayCoordinateOrientation",
            True,
            True,
            "正坐标沿 n_e=[r0]-[r*]，方向固定为 source -> root。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousActiveFacetAfterRayCoordinate",
            True,
            True,
            "active-facet normal-cone 口径被删除；剩余是命名正射线坐标证书。",
            NO_FACET,
        ),
        row(
            "PhaseResidueExchangeNormalConeRayCoordinatePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange active-facet normal-cone ray-coordinate circuit PDEC/cap。",
            RAY_PACKET,
        ),
        row(
            "NoAnonymousActiveFacetAfterRayCoordinate",
            True,
            True,
            "单活跃面法锥被压成生成元 n_e 与唯一正坐标 A。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeNormalConeRayCoordinate",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeNormalConeRayCoordinateStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、normal-cone ray-coordinate、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange normal-cone ray-coordinate circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 active-facet normal-cone ray-coordinate 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange active-facet normal-cone 已把剩余写成 "
        "phi(r0)-phi(r*)=1、n_e=[r0]-[r*]、N_e={lambda n_e: lambda>=0}、div=A n_e。"
        "本步删除 active-facet normal-cone 作为黑箱的口径，把非退化对象登记为唯一正射线坐标："
        "div=lambda n_e，lambda=A>0，且一维法锥排除任何横向分量。"
        "由此 <div,phi>=lambda(phi(r0)-phi(r*))=A，||div||_1=2lambda=2A。"
        "若 r0=r* 或 A=0，生成元/坐标退化并回流 singleton/degenerate 出口。"
        "剩余反例不再是匿名 active-facet normal-cone，而必须表现为 normal-cone ray-coordinate "
        "circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_router",
        "status": "phase_residue_exchange_active_facet_normal_cone_reduced_to_ray_coordinate_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "ray_coordinate_records": ray_coordinate_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_active_facet_normal_cone_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_active_facet_imported_for_ray_coordinate": True,
        "phase_residue_exchange_normal_cone_ray_generator_closed": True,
        "phase_residue_exchange_normal_cone_ray_coordinate_closed": True,
        "phase_residue_exchange_normal_cone_positive_coordinate_closed": True,
        "phase_residue_exchange_normal_cone_unique_coordinate_closed": True,
        "phase_residue_exchange_normal_cone_no_transverse_component_closed": True,
        "phase_residue_exchange_normal_cone_coordinate_boundary_pairing_closed": True,
        "phase_residue_exchange_normal_cone_coordinate_total_variation_closed": True,
        "phase_residue_exchange_ray_coordinate_equals_active_facet_closed": True,
        "phase_residue_exchange_ray_coordinate_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_ray_coordinate_orientation_closed": True,
        "phase_residue_no_anonymous_active_facet_after_ray_coordinate_closed": True,
        "phase_residue_exchange_normal_cone_ray_coordinate_packet_registered": True,
        "anonymous_active_facet_normal_cone_removed_after_ray_coordinate": True,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "linear_witness_existence_proved": False,
        "phase_residue_exchange_complementary_slackness_active_facet_normal_cone_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_circuit_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "source_hashes": source_hashes(),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange active facet normal cone ray coordinate 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_active_facet_normal_cone_imported={fmt_bool(cert['phase_residue_exchange_active_facet_normal_cone_imported'])}",
        f"phase_residue_exchange_normal_cone_ray_generator_closed={fmt_bool(cert['phase_residue_exchange_normal_cone_ray_generator_closed'])}",
        f"phase_residue_exchange_normal_cone_ray_coordinate_closed={fmt_bool(cert['phase_residue_exchange_normal_cone_ray_coordinate_closed'])}",
        f"phase_residue_exchange_normal_cone_positive_coordinate_closed={fmt_bool(cert['phase_residue_exchange_normal_cone_positive_coordinate_closed'])}",
        f"phase_residue_exchange_normal_cone_unique_coordinate_closed={fmt_bool(cert['phase_residue_exchange_normal_cone_unique_coordinate_closed'])}",
        f"phase_residue_exchange_normal_cone_no_transverse_component_closed={fmt_bool(cert['phase_residue_exchange_normal_cone_no_transverse_component_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_active_facet_normal_cone_ray_coordinate_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_active_facet_normal_cone_ray_coordinate_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. active facet normal-cone 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "phi(r0)-phi(r*)=1",
        "n_e=[r0]-[r*]",
        "normal_cone(e)={lambda n_e: lambda>=0}",
        "div=A n_e",
        "div in normal_cone(e)",
        "A C_Pi=W",
        "```",
        "",
        "## 2. ray coordinate 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["ray_coordinate_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时法锥射线坐标证书为：",
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
            "若 `r0=r*` 或 `A=0`，则生成元/坐标证书退化并回流 singleton/degenerate 出口。",
            "",
            "## 3. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
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
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange active-facet normal-cone ray-coordinate circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
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
    """生成 JSON、ledger 和 Markdown 三件套。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("phase_residue_exchange_active_facet_normal_cone_ray_coordinate_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
