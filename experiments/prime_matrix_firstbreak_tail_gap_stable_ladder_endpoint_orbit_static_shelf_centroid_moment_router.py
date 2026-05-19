#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit static-shelf centroid-moment 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_moment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitStaticShelfAreaMomentImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterStaticShelfCentroidLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStaticShelfCentroidLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterStaticShelfCentroidLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterStaticShelfCentroidLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterStaticShelfCentroidLedger"
AREA_IMPORT = "StableLadderEndpointOrbitStaticShelfAreaMomentModelLedger"
COLLAR_SPLIT = "StableLadderEndpointOrbitStaticShelfBoundaryCollarSplitLedger"
COLLAR_RETURN = "StableLadderEndpointOrbitStaticShelfCollarChargeReturnLedger"
CORE_MASS = "StableLadderEndpointOrbitStaticShelfInteriorCoreMassLedger"
CENTROID = "StableLadderEndpointOrbitStaticShelfInteriorCentroidMomentPacketLedger"
NO_ANON = "NoAnonymousStaticShelfAreaMomentExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterStaticShelfCentroidLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {AREA_IMPORT} "
    f"AND {COLLAR_SPLIT} AND {COLLAR_RETURN} AND {CORE_MASS} "
    f"AND {CENTROID} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 area-moment 硬点替换成 interior-centroid 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 static-shelf centroid-moment 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitStaticShelfAreaMomentImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、static shelf area moment、bridge cancellation、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterStaticShelfCentroid",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStaticShelfCentroid",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterStaticShelfCentroid",
            True,
            False,
            "bridge-cancellation PDEC/cap 继续前传；边界 collar 抵消若足够则回流该出口。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterStaticShelfCentroid",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传；内部同号继续堆高若足够则回流该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterStaticShelfCentroid",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传；边界或内部高振荡若足够则回流该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfAreaMomentModel",
            True,
            True,
            "导入未被端点收费解释的静态 shelf 面积矩。",
            AREA_IMPORT,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfBoundaryCollarSplit",
            True,
            True,
            "把 shelf 区间按参数 eta 拆成左右边界 collar 与 interior core。",
            COLLAR_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfCollarChargeReturn",
            True,
            True,
            "若面积矩主要由 collar 支付，则回流 bridge cancellation、amplitude-depth 或 boundary flux。",
            COLLAR_RETURN,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfInteriorCoreMass",
            True,
            True,
            "若 collar 不能支付，至少固定比例的 weighted increment moment 位于 interior core。",
            CORE_MASS,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfInteriorCentroidMomentPacket",
            True,
            False,
            "内部 core 质量给出远离端点的有向加权质心异常；本步登记为新的 PDEC/cap。",
            CENTROID,
        ),
        row(
            "NoAnonymousStaticShelfAreaMomentExit",
            True,
            True,
            "static shelf area moment 不再匿名保留；它是 interior centroid moment 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterStaticShelfCentroid",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitStaticShelfCentroidStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、interior centroid moment、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、interior centroid moment、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 static-shelf centroid-moment 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "static shelf area moment 给出未被端点收费解释的矩形面积矩。"
        "把 shelf 区间按 eta 拆成左右 boundary collars 与 interior core。"
        "若 weighted increment moment 主要落在 collars，则回流 bridge/amplitude/boundary；"
        "否则至少固定比例的 moment 位于远离端点的 interior core，并形成有向加权质心异常。"
        "因此新剩余压成 static shelf interior centroid moment PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_moment_router",
        "status": "endpoint_orbit_static_shelf_area_moment_reduced_to_interior_centroid_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_static_shelf_area_moment_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_static_shelf_area_moment_model_closed": True,
        "endpoint_orbit_static_shelf_boundary_collar_split_closed": True,
        "endpoint_orbit_static_shelf_collar_charge_return_closed": True,
        "endpoint_orbit_static_shelf_interior_core_mass_closed": True,
        "endpoint_orbit_static_shelf_interior_centroid_moment_packet_registered": True,
        "anonymous_static_shelf_area_moment_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_static_shelf_interior_centroid_moment_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "static_shelf_centroid_formulas": {
            "collar_split": "I = C_left(eta L) union K_eta union C_right(eta L)",
            "weighted_moment": "M(I)=sum w(t)*sigma*d_t",
            "collar_return": "if |M(C_left)+M(C_right)| >= tau*M(I), return to named endpoint exits",
            "interior_mass": "otherwise |M(K_eta)| >= (1-tau)*M(I)",
            "centroid": "c_K=sum_{t in K_eta} t*w(t)*sigma*d_t / sum_{t in K_eta} w(t)*sigma*d_t",
            "new_exit": "StaticShelfInteriorCentroidMomentPDECCap",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder endpoint orbit static-shelf centroid-moment 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_static_shelf_area_moment_imported={fmt_bool(cert['endpoint_orbit_static_shelf_area_moment_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_bridge_cancellation_carried_forward={fmt_bool(cert['endpoint_orbit_bridge_cancellation_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_static_shelf_area_moment_model_closed={fmt_bool(cert['endpoint_orbit_static_shelf_area_moment_model_closed'])}",
        f"endpoint_orbit_static_shelf_boundary_collar_split_closed={fmt_bool(cert['endpoint_orbit_static_shelf_boundary_collar_split_closed'])}",
        f"endpoint_orbit_static_shelf_collar_charge_return_closed={fmt_bool(cert['endpoint_orbit_static_shelf_collar_charge_return_closed'])}",
        f"endpoint_orbit_static_shelf_interior_core_mass_closed={fmt_bool(cert['endpoint_orbit_static_shelf_interior_core_mass_closed'])}",
        f"endpoint_orbit_static_shelf_interior_centroid_moment_packet_registered={fmt_bool(cert['endpoint_orbit_static_shelf_interior_centroid_moment_packet_registered'])}",
        f"anonymous_static_shelf_area_moment_removed={fmt_bool(cert['anonymous_static_shelf_area_moment_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_static_shelf_interior_centroid_moment_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_static_shelf_interior_centroid_moment_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. collar/core 拆分",
        "",
        "导入上一层 static shelf area moment。给定 `0<eta<1/4`，把 shelf 区间拆成左右边界 collar 和 interior core：",
        "",
        "```text",
        "I = C_left(eta L) union K_eta union C_right(eta L).",
        "```",
        "",
        "若面积矩主要落在两个 collar，则它仍是端点收费，回流到 bridge-cancellation、amplitude-depth 或 variation-boundary flux。",
        "",
        "## 2. 内部质心包",
        "",
        "若 collar 不能支付面积矩，则 weighted increment moment 必有固定比例落在 `K_eta`。定义内部有向质心：",
        "",
        "```text",
        "c_K = sum_{t in K_eta} t*w(t)*sigma*d_t / sum_{t in K_eta} w(t)*sigma*d_t.",
        "```",
        "",
        "这个质心远离端点，不能再被边界收费解释；它就是新的内部相位/容量异常接口。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 static shelf area moment，而是 interior centroid moment，或已命名的 bridge/amplitude/boundary 出口，外加 singleton、full-cycle mean 与 sparse SAE。",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
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
            "- 本证书没有证明 endpoint singleton atom/SAE。",
            "- 本证书没有证明 EndpointOrbitFullCycleMeanAtomSAE。",
            "- 本证书没有证明 EndpointOrbitStaticShelfInteriorCentroidMomentPDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 static shelf area moment 压成内部质心矩包或已命名三出口。",
            f"- `{NEW_TARGET}` 仍未闭合。",
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
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
