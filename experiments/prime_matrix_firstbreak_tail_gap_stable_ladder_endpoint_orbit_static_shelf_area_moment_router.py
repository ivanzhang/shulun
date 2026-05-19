#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit static-shelf area-moment 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_area_moment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitStaticPotentialShelfBiasImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterStaticShelfAreaLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStaticShelfAreaLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterStaticShelfAreaLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterStaticShelfAreaLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterStaticShelfAreaLedger"
STATIC_MODEL = "StableLadderEndpointOrbitStaticShelfBiasModelLedger"
AREA = "StableLadderEndpointOrbitStaticShelfAreaLowerBoundLedger"
PARTS = "StableLadderEndpointOrbitShelfSummationByPartsLedger"
EDGE = "StableLadderEndpointOrbitShelfEndpointChargeReturnLedger"
MOMENT = "StableLadderEndpointOrbitStaticShelfAreaMomentPacketLedger"
NO_ANON = "NoAnonymousStaticPotentialShelfBiasExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterStaticShelfAreaLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {STATIC_MODEL} "
    f"AND {AREA} AND {PARTS} AND {EDGE} AND {MOMENT} "
    f"AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 static shelf bias 硬点替换成面积矩接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 static-shelf area-moment 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitStaticPotentialShelfBiasImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、static potential shelf bias、bridge cancellation、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterStaticShelfArea",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStaticShelfArea",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterStaticShelfArea",
            True,
            False,
            "bridge-cancellation PDEC/cap 继续前传；端点收费若已抵消则回流该出口。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterStaticShelfArea",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传；若面积来自继续堆高则回流该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterStaticShelfArea",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传；若面积由高边界通量解释则回流该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfBiasModel",
            True,
            True,
            "导入低振荡、无深漂移、无早抵消的一侧静态 shelf 偏置。",
            STATIC_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfAreaLowerBound",
            True,
            True,
            "由 sigma*S(t)>=H/2 和 |I|=L>E 得到矩形面积 A(I)>=HL/2。",
            AREA,
        ),
        row(
            "StableLadderEndpointOrbitShelfSummationByParts",
            True,
            True,
            "用离散分部求和把 shelf 面积写成端点收费与 sawtooth/triangular 权重下的增量矩。",
            PARTS,
        ),
        row(
            "StableLadderEndpointOrbitShelfEndpointChargeReturn",
            True,
            True,
            "若端点收费已解释矩形面积，则它回到 bridge cancellation、amplitude-depth 或 boundary flux。",
            EDGE,
        ),
        row(
            "StableLadderEndpointOrbitStaticShelfAreaMomentPacket",
            True,
            False,
            "端点收费不能解释时，剩余是静态 shelf 面积矩 PDEC/cap。",
            MOMENT,
        ),
        row(
            "NoAnonymousStaticPotentialShelfBiasExit",
            True,
            True,
            "static potential shelf bias 不再匿名保留；它是面积矩包或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterStaticShelfArea",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitStaticShelfAreaMomentStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、static shelf area moment、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、static shelf area moment、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 static-shelf area-moment 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "static potential shelf bias 给出低振荡、无深漂移、无早抵消的长一侧势能地板。"
        "在长度 L>E 的区间 I 上，sigma*S(t)>=H/2 强制矩形面积 A(I)>=HL/2。"
        "离散分部求和把该面积分成端点收费与 sawtooth/triangular 权重下的增量矩。"
        "若端点收费已解释面积，则回流 bridge/amplitude/boundary；否则剩余就是 static shelf area moment PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_area_moment_router",
        "status": "endpoint_orbit_static_shelf_bias_reduced_to_area_moment_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_static_potential_shelf_bias_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_static_shelf_bias_model_closed": True,
        "endpoint_orbit_static_shelf_area_lower_bound_closed": True,
        "endpoint_orbit_shelf_summation_by_parts_closed": True,
        "endpoint_orbit_shelf_endpoint_charge_return_closed": True,
        "endpoint_orbit_static_shelf_area_moment_packet_registered": True,
        "anonymous_static_potential_shelf_bias_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_static_shelf_area_moment_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "static_shelf_area_formulas": {
            "shelf_floor": "sigma*S(t) >= H/2 for t in I",
            "area_lower_bound": "A(I)=sum_{t in I} sigma*S(t) >= H*|I|/2",
            "increments": "d_t=S(t+1)-S(t)",
            "summation_by_parts": "A(I)=endpoint_charge + sum triangular_weight(t)*sigma*d_t",
            "endpoint_return": "large endpoint charge returns to BridgeCancellation/AmplitudeDepth/VariationBoundaryFlux",
            "new_exit": "otherwise StaticShelfAreaMomentPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit static-shelf area-moment 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_static_potential_shelf_bias_imported={fmt_bool(cert['endpoint_orbit_static_potential_shelf_bias_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_bridge_cancellation_carried_forward={fmt_bool(cert['endpoint_orbit_bridge_cancellation_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_static_shelf_bias_model_closed={fmt_bool(cert['endpoint_orbit_static_shelf_bias_model_closed'])}",
        f"endpoint_orbit_static_shelf_area_lower_bound_closed={fmt_bool(cert['endpoint_orbit_static_shelf_area_lower_bound_closed'])}",
        f"endpoint_orbit_shelf_summation_by_parts_closed={fmt_bool(cert['endpoint_orbit_shelf_summation_by_parts_closed'])}",
        f"endpoint_orbit_shelf_endpoint_charge_return_closed={fmt_bool(cert['endpoint_orbit_shelf_endpoint_charge_return_closed'])}",
        f"endpoint_orbit_static_shelf_area_moment_packet_registered={fmt_bool(cert['endpoint_orbit_static_shelf_area_moment_packet_registered'])}",
        f"anonymous_static_potential_shelf_bias_removed={fmt_bool(cert['anonymous_static_potential_shelf_bias_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_static_shelf_area_moment_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_static_shelf_area_moment_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 静态 shelf 面积",
        "",
        "导入上一层的 static potential shelf bias：存在 `I` 和符号 `sigma`，满足",
        "",
        "```text",
        "sigma*S(t) >= H/2 for t in I,  |I|=L>E.",
        "```",
        "",
        "因此矩形面积满足：",
        "",
        "```text",
        "A(I)=sum_{t in I} sigma*S(t) >= H*L/2.",
        "```",
        "",
        "## 2. 分部求和与端点收费",
        "",
        "令 `d_t=S(t+1)-S(t)`。离散分部求和把 `A(I)` 写成端点收费加 triangular 权重下的增量矩。",
        "",
        "若端点收费已经解释面积，则它回流到 bridge-cancellation、amplitude-depth 或 variation-boundary flux。否则静态 shelf 必须留下一个真实的面积矩异常。",
        "",
        "```text",
        "static shelf area moment = large rectangular potential area not paid by named endpoint charges.",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 static potential shelf bias，而是 static shelf area moment，或已命名的 bridge/amplitude/boundary 出口，外加 singleton、full-cycle mean 与 sparse SAE。",
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
            "- 本证书没有证明 EndpointOrbitStaticShelfAreaMomentPDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 static potential shelf bias 压成面积矩包或已命名三出口。",
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
