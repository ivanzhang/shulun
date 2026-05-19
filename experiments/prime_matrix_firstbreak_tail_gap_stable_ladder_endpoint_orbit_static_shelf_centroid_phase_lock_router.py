#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit static-shelf centroid phase-lock 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_phase_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitStaticShelfInteriorCentroidMomentImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCentroidPhaseLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCentroidPhaseLockLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCentroidPhaseLockLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCentroidPhaseLockLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCentroidPhaseLockLedger"
CENTROID_COORDINATE = "StableLadderEndpointOrbitInteriorCentroidCoordinateModelLedger"
PHASE_WINDOW = "StableLadderEndpointOrbitInteriorCentroidScaleWindowLedger"
DRIFT_RETURN = "StableLadderEndpointOrbitInteriorCentroidDriftReturnLedger"
OPPOSITE_BRIDGE_RETURN = "StableLadderEndpointOrbitInteriorCentroidOppositeSignBridgeReturnLedger"
SAME_SIGN_STACK_RETURN = "StableLadderEndpointOrbitInteriorCentroidSameSignStackReturnLedger"
PHASE_LOCK = "StableLadderEndpointOrbitInteriorCentroidPhaseLockPacketLedger"
NO_ANON = "NoAnonymousStaticShelfInteriorCentroidMomentExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCentroidPhaseLockLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {CENTROID_COORDINATE} "
    f"AND {PHASE_WINDOW} AND {DRIFT_RETURN} AND {OPPOSITE_BRIDGE_RETURN} "
    f"AND {SAME_SIGN_STACK_RETURN} AND {PHASE_LOCK} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 interior-centroid 硬点替换成 phase-lock 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 centroid phase-lock 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitStaticShelfInteriorCentroidMomentImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、interior centroid moment、bridge cancellation、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCentroidPhaseLock",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCentroidPhaseLock",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCentroidPhaseLock",
            True,
            False,
            "bridge-cancellation PDEC/cap 继续前传；内部反号互付若足够则回流该出口。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCentroidPhaseLock",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传；同相同号堆高若足够则回流该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCentroidPhaseLock",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传；质心显著漂移若足够则回流该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitInteriorCentroidCoordinateModel",
            True,
            True,
            "把每个 interior-core 质心写成归一化相位 theta=(c-a)/L，且 theta 位于 [eta,1-eta]。",
            CENTROID_COORDINATE,
        ),
        row(
            "StableLadderEndpointOrbitInteriorCentroidScaleWindow",
            True,
            True,
            "在 stable ladder 上按尺度与相位单元分窗；每个窗口保留 signed mass 与 centroid phase。",
            PHASE_WINDOW,
        ),
        row(
            "StableLadderEndpointOrbitInteriorCentroidDriftReturn",
            True,
            True,
            "若相邻窗口质心相位有持续显著漂移，则跨内部切线的质量运输给出 variation-boundary flux。",
            DRIFT_RETURN,
        ),
        row(
            "StableLadderEndpointOrbitInteriorCentroidOppositeSignBridgeReturn",
            True,
            True,
            "若同一相位单元或相邻单元出现足量反号质量，则它是 bridge-cancellation 负债。",
            OPPOSITE_BRIDGE_RETURN,
        ),
        row(
            "StableLadderEndpointOrbitInteriorCentroidSameSignStackReturn",
            True,
            True,
            "若同相同号质量跨窗口累积超过势能预算，则它是 amplitude-depth 负债。",
            SAME_SIGN_STACK_RETURN,
        ),
        row(
            "StableLadderEndpointOrbitInteriorCentroidPhaseLockPacket",
            True,
            False,
            "若漂移、反号互付、同号堆高都不能支付，剩余必为持久内部相位锁定包；本步只登记新 PDEC/cap。",
            PHASE_LOCK,
        ),
        row(
            "NoAnonymousStaticShelfInteriorCentroidMomentExit",
            True,
            True,
            "interior centroid moment 不再匿名保留；它是 phase-lock 或已有命名三出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterCentroidPhaseLock",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitStaticShelfCentroidPhaseLockStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、interior centroid phase-lock、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、interior centroid phase-lock、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 centroid phase-lock 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "static shelf interior centroid moment 给出远离端点的有向质心异常。"
        "把每个窗口的质心归一化为 theta=(c-a)/L，并在 stable ladder 上按尺度与相位单元分窗。"
        "若 theta 持续漂移，则产生内部质量运输并回流 variation-boundary flux；"
        "若同相或近相反号质量足够，则回流 bridge cancellation；"
        "若同相同号质量持续堆高，则回流 amplitude-depth。"
        "三类支付都不发生时，剩余被压成持久内部质心相位锁定 PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_phase_lock_router",
        "status": "endpoint_orbit_static_shelf_interior_centroid_moment_reduced_to_phase_lock_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_static_shelf_interior_centroid_moment_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_interior_centroid_coordinate_model_closed": True,
        "endpoint_orbit_interior_centroid_scale_window_closed": True,
        "endpoint_orbit_interior_centroid_drift_return_closed": True,
        "endpoint_orbit_interior_centroid_opposite_sign_bridge_return_closed": True,
        "endpoint_orbit_interior_centroid_same_sign_stack_return_closed": True,
        "endpoint_orbit_interior_centroid_phase_lock_packet_registered": True,
        "anonymous_static_shelf_interior_centroid_moment_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_static_shelf_interior_centroid_phase_lock_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "centroid_phase_lock_formulas": {
            "centroid_mass": "m_j=sum_{t in K_j} w_j(t)*sigma_j*d_t",
            "centroid": "c_j=sum_{t in K_j} t*w_j(t)*sigma_j*d_t / m_j",
            "normalized_phase": "theta_j=(c_j-a_j)/L_j in [eta,1-eta]",
            "drift_return": "sum |theta_{j+1}-theta_j|*|m_j| large => VariationBoundaryFluxPDECCap",
            "opposite_bridge_return": "opposite signs in same/adjacent phase cells => BridgeCancellationPDECCap",
            "same_sign_stack_return": "same sign in one phase cell with large cumulative mass => AmplitudeDepthPDECCap",
            "new_exit": "StaticShelfInteriorCentroidPhaseLockPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit static-shelf centroid phase-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_static_shelf_interior_centroid_moment_imported={fmt_bool(cert['endpoint_orbit_static_shelf_interior_centroid_moment_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_bridge_cancellation_carried_forward={fmt_bool(cert['endpoint_orbit_bridge_cancellation_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_interior_centroid_coordinate_model_closed={fmt_bool(cert['endpoint_orbit_interior_centroid_coordinate_model_closed'])}",
        f"endpoint_orbit_interior_centroid_scale_window_closed={fmt_bool(cert['endpoint_orbit_interior_centroid_scale_window_closed'])}",
        f"endpoint_orbit_interior_centroid_drift_return_closed={fmt_bool(cert['endpoint_orbit_interior_centroid_drift_return_closed'])}",
        f"endpoint_orbit_interior_centroid_opposite_sign_bridge_return_closed={fmt_bool(cert['endpoint_orbit_interior_centroid_opposite_sign_bridge_return_closed'])}",
        f"endpoint_orbit_interior_centroid_same_sign_stack_return_closed={fmt_bool(cert['endpoint_orbit_interior_centroid_same_sign_stack_return_closed'])}",
        f"endpoint_orbit_interior_centroid_phase_lock_packet_registered={fmt_bool(cert['endpoint_orbit_interior_centroid_phase_lock_packet_registered'])}",
        f"anonymous_static_shelf_interior_centroid_moment_removed={fmt_bool(cert['anonymous_static_shelf_interior_centroid_moment_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_static_shelf_interior_centroid_phase_lock_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_static_shelf_interior_centroid_phase_lock_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 内部质心坐标",
        "",
        "上一层给出远离两端的 interior-core 质心。对每个 stable ladder 窗口 `j` 记：",
        "",
        "```text",
        "m_j = sum_{t in K_j} w_j(t)*sigma_j*d_t",
        "c_j = sum_{t in K_j} t*w_j(t)*sigma_j*d_t / m_j",
        "theta_j = (c_j-a_j)/L_j in [eta,1-eta].",
        "```",
        "",
        "`theta_j` 是内部相位坐标；它把“质心在 core 内部”变成可比较的无量纲相位。",
        "",
        "## 2. 三个回流出口",
        "",
        "- 若 `theta_j` 在连续窗口中持续显著漂移，则内部质量必须跨过相位切线，形成 variation-boundary flux。",
        "- 若同相或邻近相位单元中出现足量反号质量，则它是 bridge-cancellation 支付。",
        "- 若同相同号质量持续堆高并超过势能预算，则它是 amplitude-depth 支付。",
        "",
        "## 3. 新硬点",
        "",
        "若以上三类支付都不足，则所有 surviving centroid mass 必须落入有限个稳定内部相位单元，且符号和尺度长期锁定。这就是新的 phase-lock 包。",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 interior centroid moment，而是 interior centroid phase-lock，或已命名的 bridge/amplitude/boundary 出口，外加 singleton、full-cycle mean 与 sparse SAE。",
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
            "- 本证书没有证明 EndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 interior centroid moment 压成 phase-lock 包或已命名三出口。",
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
