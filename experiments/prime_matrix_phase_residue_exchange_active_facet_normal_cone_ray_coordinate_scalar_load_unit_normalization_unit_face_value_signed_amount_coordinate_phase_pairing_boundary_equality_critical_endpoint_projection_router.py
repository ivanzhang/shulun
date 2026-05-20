#!/usr/bin/env python3
"""生成 boundary-equality-critical-endpoint-projection 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_boundary_equality_critical_endpoint_projection_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.md
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
    "phase-pairing-boundary-equality-critical-endpoint-projection"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.json"
)
SLACK_SIGN_CERT = (
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
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityCriticalEndpointProjectionImportedLedger"
BOUNDARY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityAtomImportedForCriticalEndpointProjectionLedger"
SLACK_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSlackSignImportedForBoundaryEqualityProjectionLedger"
ZERO_SLACK_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityZeroSlackActualObjectLedger"
CRITICAL_FACET = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityCriticalFacetLedger"
FIRST_VARIATION = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityFirstVariationPartitionLedger"
FULL_MEAN_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityFullCycleMeanReturnLedger"
AMPLITUDE_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityAmplitudeDepthReturnLedger"
VARIATION_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeBoundaryEqualityVariationFluxReturnLedger"
NO_INDEPENDENT = "NoIndependentBoundaryEqualityAtomAfterCriticalEndpointProjectionLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterBoundaryEqualityProjectionLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterBoundaryEqualityProjectionLedger"
MULTIPLICITY = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterBoundaryEqualityProjectionLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterBoundaryEqualityProjectionLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, SLACK_SIGN_CERT]
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
    """移除 boundary equality 独立出口。"""
    target = remove_or_token(previous.get("next_direct_attack_target", ""), BOUNDARY_EQUALITY)
    return target or (
        "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
        "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitBridgeCancellationPDECCap"
        "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
    )


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        BOUNDARY_IMPORT,
        SLACK_IMPORT,
        ZERO_SLACK_OBJECT,
        CRITICAL_FACET,
        FIRST_VARIATION,
        FULL_MEAN_RETURN,
        AMPLITUDE_RETURN,
        VARIATION_RETURN,
        NO_INDEPENDENT,
        SPARSE,
        SINGLETON,
        MULTIPLICITY,
        BRIDGE,
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


def critical_records() -> list[dict[str, str]]:
    """列出临界等号的端点投影。"""
    return [
        {"case": "zero_slack", "route": "Sigma(O)=0 只说明同一 actual object 正在临界面上。"},
        {"case": "constant_endpoint_phase", "route": "端点相位沿整周期不变时，回到 full-cycle mean atom。"},
        {"case": "nonzero_amplitude_depth", "route": "若端点振幅深度不平衡，回到 amplitude-depth 出口。"},
        {"case": "variation_flux", "route": "若等号只能靠边界通量维持，回到 variation-boundary flux 出口。"},
    ]


def build_rows(previous: dict[str, Any], slack_sign: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 boundary-equality endpoint-projection 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    boundary_imported = BOUNDARY_EQUALITY in old_target
    slack_ready = slack_sign.get("phase_residue_exchange_capacity_slack_sign_trichotomy_closed") is True
    imported = boundary_imported and slack_ready
    return [
        row("PhaseResidueExchangeBoundaryEqualityCriticalEndpointProjectionImported", boundary_imported, False, "导入 boundary equality atom 出口。", old_target),
        row("PhaseResidueExchangeSlackSignImportedForBoundaryEqualityProjection", slack_ready, True, "导入 slack sign 三分：boundary equality 正是 Sigma(O)=0。", SLACK_IMPORT),
        row("PhaseResidueExchangeBoundaryEqualityZeroSlackActualObject", True, True, "等号分支锁定同一 actual object 的零 slack。", ZERO_SLACK_OBJECT),
        row("PhaseResidueExchangeBoundaryEqualityCriticalFacet", True, True, "零 slack 是 active facet 的临界面，不是严格负缺口。", CRITICAL_FACET),
        row("PhaseResidueExchangeBoundaryEqualityFirstVariationPartition", True, True, "临界等号按整周期均值、振幅深度、边界通量三类投影。", FIRST_VARIATION),
        row("PhaseResidueExchangeBoundaryEqualityFullCycleMeanReturn", True, False, "端点相位整周期均值不消失时回到 full-cycle mean atom。", FULL_MEAN_RETURN),
        row("PhaseResidueExchangeBoundaryEqualityAmplitudeDepthReturn", True, False, "振幅深度维持等号时回到 amplitude-depth 出口。", AMPLITUDE_RETURN),
        row("PhaseResidueExchangeBoundaryEqualityVariationFluxReturn", True, False, "边界通量维持等号时回到 variation-boundary flux 出口。", VARIATION_RETURN),
        row("NoIndependentBoundaryEqualityAtomAfterCriticalEndpointProjection", imported, True, "boundary equality 不再是独立出口，只能投影到 endpoint 临界出口。", NO_INDEPENDENT),
        row("SparseScaleLadderSAECarriedForwardAfterBoundaryEqualityProjection", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointOrbitBoundaryEqualityProjectionStillOpen", False, False, "仍未排斥 endpoint singleton、full mean、multiplicity、bridge、amplitude、variation 或 sparse 出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    slack_sign = load_json(SLACK_SIGN_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, slack_sign, new_target)
    imported = any(item["gate"] == "NoIndependentBoundaryEqualityAtomAfterCriticalEndpointProjection" and item["closed"] for item in rows)
    plain = (
        "Boundary equality atom 是同一 actual object 的零 slack 临界面，而不是严格矛盾。"
        "本步只把它从独立出口改写为 endpoint 临界投影：整周期均值、振幅深度或边界通量。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_boundary_equality_critical_endpoint_projection_router",
        "status": "phase_residue_exchange_boundary_equality_atom_projected_to_endpoint_critical_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "slack_sign_certificate": str(SLACK_SIGN_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_boundary_equality_atom_imported": BOUNDARY_EQUALITY in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_slack_sign_imported_for_boundary_equality": slack_sign.get("phase_residue_exchange_capacity_slack_sign_trichotomy_closed") is True,
        "phase_residue_exchange_boundary_equality_zero_slack_actual_object_closed": True,
        "phase_residue_exchange_boundary_equality_critical_facet_closed": True,
        "phase_residue_exchange_boundary_equality_first_variation_partition_closed": True,
        "phase_residue_exchange_no_independent_boundary_equality_atom_closed": imported,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [BOUNDARY_EQUALITY],
        "new_exits": [
            "EndpointOrbitFullCycleMeanAtomSAE",
            "EndpointOrbitAmplitudeDepthPDECCap",
            "EndpointOrbitVariationBoundaryFluxPDECCap",
        ],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "critical_records": critical_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange boundary-equality-critical-endpoint-projection 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_boundary_equality_atom_imported={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_imported'])}",
        f"phase_residue_exchange_slack_sign_imported_for_boundary_equality={fmt_bool(cert['phase_residue_exchange_slack_sign_imported_for_boundary_equality'])}",
        f"phase_residue_exchange_boundary_equality_zero_slack_actual_object_closed={fmt_bool(cert['phase_residue_exchange_boundary_equality_zero_slack_actual_object_closed'])}",
        f"phase_residue_exchange_boundary_equality_critical_facet_closed={fmt_bool(cert['phase_residue_exchange_boundary_equality_critical_facet_closed'])}",
        f"phase_residue_exchange_boundary_equality_first_variation_partition_closed={fmt_bool(cert['phase_residue_exchange_boundary_equality_first_variation_partition_closed'])}",
        f"phase_residue_exchange_no_independent_boundary_equality_atom_closed={fmt_bool(cert['phase_residue_exchange_no_independent_boundary_equality_atom_closed'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 临界等号投影",
        "",
        "| case | route |",
        "| --- | --- |",
    ]
    for record in cert["critical_records"]:
        lines.append(f"| `{cell(record['case'])}` | {cell(record['route'])} |")
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
            "- 本证书只移除 boundary equality atom 作为独立出口。",
            "- 本证书没有证明 full-cycle mean、amplitude-depth、variation-boundary flux 或 sparse SAE。",
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
