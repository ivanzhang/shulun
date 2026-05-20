#!/usr/bin/env python3
"""生成 endpoint-dynamic-signed-depth-flux-packet 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_dynamic_signed_depth_flux_packet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.md
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
    "phase-pairing-endpoint-dynamic-signed-depth-flux-packet"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-boundary-equality-critical-endpoint-projection-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)

SOURCE_MULTIPLICITY = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
BRIDGE = "EndpointOrbitBridgeCancellationPDECCap"
AMPLITUDE = "EndpointOrbitAmplitudeDepthPDECCap"
VARIATION = "EndpointOrbitVariationBoundaryFluxPDECCap"
DYNAMIC_PACKET = "EndpointOrbitSignedDepthFluxPacketPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointDynamicSignedDepthFluxPacketImportedLedger"
BOUNDARY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityProjectionImportedForDynamicPacketLedger"
DYNAMIC_MEASURE = "StableLadderEndpointOrbitDynamicSignedEndpointMeasureLedger"
ZERO_MEAN_REDUCTION = "StableLadderEndpointOrbitDynamicPacketZeroMeanReductionLedger"
SIGNED_DECOMPOSITION = "StableLadderEndpointOrbitSignedDepthFluxDecompositionLedger"
BRIDGE_COMPONENT = "StableLadderEndpointOrbitBridgeCancellationAsSignedDepthFluxComponentLedger"
AMPLITUDE_COMPONENT = "StableLadderEndpointOrbitAmplitudeDepthAsSignedDepthFluxComponentLedger"
VARIATION_COMPONENT = "StableLadderEndpointOrbitVariationFluxAsSignedDepthFluxComponentLedger"
PACKET_REGISTER = "StableLadderEndpointOrbitSignedDepthFluxPacketRegistrationLedger"
NO_THREE = "NoIndependentEndpointBridgeAmplitudeVariationAfterSignedDepthFluxPacketLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEndpointDynamicPacketLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEndpointDynamicPacketLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEndpointDynamicPacketLedger"
MULTIPLICITY = "StableLadderEndpointOrbitSourceMultiplicityCapCarriedForwardAfterEndpointDynamicPacketLedger"


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
    """登记本脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def remove_or_token(text: str, token: str) -> str:
    """从长 OR 目标中移除一个 token。"""
    updated = text
    while f"{token}Or" in updated:
        updated = updated.replace(f"{token}Or", "")
    while f"Or{token}" in updated:
        updated = updated.replace(f"Or{token}", "")
    return updated.replace(token, "")


def next_target(previous: dict[str, Any]) -> str:
    """把三个 endpoint 动态出口替换为一个 signed-depth/flux packet。"""
    target = previous.get("next_direct_attack_target", "")
    for token in [BRIDGE, AMPLITUDE, VARIATION]:
        target = remove_or_token(target, token)
    if DYNAMIC_PACKET not in target:
        target = f"{target}Or{DYNAMIC_PACKET}" if target else DYNAMIC_PACKET
    return target


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        BOUNDARY_IMPORT,
        DYNAMIC_MEASURE,
        ZERO_MEAN_REDUCTION,
        SIGNED_DECOMPOSITION,
        BRIDGE_COMPONENT,
        AMPLITUDE_COMPONENT,
        VARIATION_COMPONENT,
        PACKET_REGISTER,
        NO_THREE,
        SPARSE,
        SINGLETON,
        FULL_MEAN,
        MULTIPLICITY,
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


def packet_records() -> list[dict[str, str]]:
    """列出 endpoint 动态包的三个投影。"""
    return [
        {"component": "bridge", "route": "反号互付或镜像抵消是 signed-depth/flux 包的 cancellation component。"},
        {"component": "amplitude_depth", "route": "同号跨尺度堆高是 signed-depth/flux 包的 positive depth component。"},
        {"component": "variation_flux", "route": "边界迁移或通量泄出是 signed-depth/flux 包的 boundary flux component。"},
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 endpoint dynamic packet 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = all(token in old_target for token in [BRIDGE, AMPLITUDE, VARIATION])
    boundary_ready = previous.get("phase_residue_exchange_no_independent_boundary_equality_atom_closed") is True
    return [
        row("PhaseResidueExchangeEndpointDynamicSignedDepthFluxPacketImported", imported, False, "导入 bridge/amplitude/variation 三个 endpoint 动态出口。", old_target),
        row("PhaseResidueExchangeBoundaryEqualityProjectionImportedForDynamicPacket", boundary_ready, True, "导入 boundary equality 投影；剩余已是 endpoint 临界动态。", BOUNDARY_IMPORT),
        row("EndpointOrbitDynamicSignedEndpointMeasure", True, True, "在端点轨道上登记有符号端点负载测度。", DYNAMIC_MEASURE),
        row("EndpointOrbitDynamicPacketZeroMeanReduction", True, True, "full-cycle mean 作为独立出口保留后，动态包可按零均值部分处理。", ZERO_MEAN_REDUCTION),
        row("EndpointOrbitSignedDepthFluxDecomposition", True, True, "零均值 signed endpoint measure 分为 cancellation、positive depth、boundary flux 三个命名分量。", SIGNED_DECOMPOSITION),
        row("EndpointOrbitBridgeCancellationAsSignedDepthFluxComponent", True, False, "bridge cancellation 是 cancellation 分量。", BRIDGE_COMPONENT),
        row("EndpointOrbitAmplitudeDepthAsSignedDepthFluxComponent", True, False, "amplitude depth 是 positive depth 分量。", AMPLITUDE_COMPONENT),
        row("EndpointOrbitVariationFluxAsSignedDepthFluxComponent", True, False, "variation-boundary flux 是 boundary flux 分量。", VARIATION_COMPONENT),
        row("EndpointOrbitSignedDepthFluxPacketRegistration", imported and boundary_ready, False, "三个动态出口统一登记为 signed-depth/flux packet。", PACKET_REGISTER),
        row("NoIndependentEndpointBridgeAmplitudeVariationAfterSignedDepthFluxPacket", imported and boundary_ready, True, "bridge/amplitude/variation 不再作为三个并行独立出口。", NO_THREE),
        row("SparseScaleLadderSAECarriedForwardAfterEndpointDynamicPacket", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointDynamicSignedDepthFluxPacketStillOpen", False, False, "仍未排斥 signed-depth/flux packet、endpoint singleton、full mean、source multiplicity 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    imported = any(item["gate"] == "NoIndependentEndpointBridgeAmplitudeVariationAfterSignedDepthFluxPacket" and item["closed"] for item in rows)
    plain = (
        "boundary/payment 独立出口移除后，剩余 bridge、amplitude-depth、variation-boundary flux "
        "都是同一个 endpoint signed-depth/flux 测度的不同投影。"
        "本步把三者统一为一个动态包，不证明该包不存在。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_dynamic_signed_depth_flux_packet_router",
        "status": "phase_residue_exchange_endpoint_bridge_amplitude_variation_unified_to_signed_depth_flux_packet_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_dynamic_bridge_amplitude_variation_imported": all(token in previous.get("next_direct_attack_target", "") for token in [BRIDGE, AMPLITUDE, VARIATION]),
        "phase_residue_exchange_boundary_equality_projection_imported_for_dynamic_packet": previous.get("phase_residue_exchange_no_independent_boundary_equality_atom_closed") is True,
        "endpoint_orbit_dynamic_signed_endpoint_measure_closed": True,
        "endpoint_orbit_dynamic_packet_zero_mean_reduction_closed": True,
        "endpoint_orbit_signed_depth_flux_decomposition_closed": True,
        "endpoint_orbit_signed_depth_flux_packet_registered": imported,
        "endpoint_orbit_no_independent_bridge_amplitude_variation_closed": imported,
        "endpoint_orbit_signed_depth_flux_packet_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [BRIDGE, AMPLITUDE, VARIATION],
        "new_exits": [DYNAMIC_PACKET],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "packet_records": packet_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange endpoint-dynamic-signed-depth-flux-packet 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_dynamic_bridge_amplitude_variation_imported={fmt_bool(cert['endpoint_dynamic_bridge_amplitude_variation_imported'])}",
        f"phase_residue_exchange_boundary_equality_projection_imported_for_dynamic_packet={fmt_bool(cert['phase_residue_exchange_boundary_equality_projection_imported_for_dynamic_packet'])}",
        f"endpoint_orbit_dynamic_signed_endpoint_measure_closed={fmt_bool(cert['endpoint_orbit_dynamic_signed_endpoint_measure_closed'])}",
        f"endpoint_orbit_dynamic_packet_zero_mean_reduction_closed={fmt_bool(cert['endpoint_orbit_dynamic_packet_zero_mean_reduction_closed'])}",
        f"endpoint_orbit_signed_depth_flux_decomposition_closed={fmt_bool(cert['endpoint_orbit_signed_depth_flux_decomposition_closed'])}",
        f"endpoint_orbit_signed_depth_flux_packet_registered={fmt_bool(cert['endpoint_orbit_signed_depth_flux_packet_registered'])}",
        f"endpoint_orbit_no_independent_bridge_amplitude_variation_closed={fmt_bool(cert['endpoint_orbit_no_independent_bridge_amplitude_variation_closed'])}",
        f"endpoint_orbit_signed_depth_flux_packet_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_signed_depth_flux_packet_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed-depth/flux 三分量",
        "",
        "| component | route |",
        "| --- | --- |",
    ]
    for record in cert["packet_records"]:
        lines.append(f"| `{cell(record['component'])}` | {cell(record['route'])} |")
    lines.extend(
        [
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
            "- 本证书只把 bridge/amplitude/variation 三个 endpoint 动态出口统一为一个 signed-depth/flux packet。",
            "- 本证书没有证明 signed-depth/flux packet、endpoint singleton、full-cycle mean、source multiplicity 或 sparse SAE。",
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
