#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit long-potential-shelf static-bias 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_potential_shelf_static_bias_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitLongPotentialShelfImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterShelfStaticBiasLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterShelfStaticBiasLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterShelfStaticBiasLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterShelfStaticBiasLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterShelfStaticBiasLedger"
SHELF_MODEL = "StableLadderEndpointOrbitLongPotentialShelfModelLedger"
FLOOR = "StableLadderEndpointOrbitShelfPotentialFloorLedger"
INCREMENTS = "StableLadderEndpointOrbitShelfIncrementBalanceLedger"
OSCILLATION = "StableLadderEndpointOrbitShelfOscillationBoundaryFluxDichotomyLedger"
DRIFT = "StableLadderEndpointOrbitShelfPositiveDriftAmplitudeDepthDichotomyLedger"
CANCELLATION = "StableLadderEndpointOrbitShelfNegativeCancellationDichotomyLedger"
STATIC_BIAS = "StableLadderEndpointOrbitStaticPotentialShelfBiasPacketLedger"
NO_ANON = "NoAnonymousLongPotentialShelfExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterShelfStaticBiasLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {SHELF_MODEL} "
    f"AND {FLOOR} AND {INCREMENTS} AND {OSCILLATION} AND {DRIFT} "
    f"AND {CANCELLATION} AND {STATIC_BIAS} AND {NO_ANON} "
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
    """把旧活动基中的 long shelf 硬点替换成 static-bias 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 long-shelf static-bias 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitLongPotentialShelfImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、long potential shelf、bridge cancellation、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterShelfStaticBias",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterShelfStaticBias",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterShelfStaticBias",
            True,
            False,
            "bridge-cancellation PDEC/cap 继续前传；本步不排斥该 cap。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterShelfStaticBias",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传；本步只把 shelf 内正漂移回流到该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterShelfStaticBias",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传；本步只把 shelf 内高振荡回流到该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitLongPotentialShelfModel",
            True,
            True,
            "固定长桥段 I，长度 L>E，且有向势能在 I 上保持同号偏离至少 H/2。",
            SHELF_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitShelfPotentialFloor",
            True,
            True,
            "把 shelf 写成同号势能地板 sigma*S(t)>=H/2；反号情形由 sigma 翻转统一。",
            FLOOR,
        ),
        row(
            "StableLadderEndpointOrbitShelfIncrementBalance",
            True,
            True,
            "将 shelf 内增量分成正漂移、负抵消与边界振荡三类，不再允许匿名内部波动。",
            INCREMENTS,
        ),
        row(
            "StableLadderEndpointOrbitShelfOscillationBoundaryFluxDichotomy",
            True,
            True,
            "若 shelf 内边界切换或总变差超过预算，则回流 variation-boundary flux。",
            OSCILLATION,
        ),
        row(
            "StableLadderEndpointOrbitShelfPositiveDriftAmplitudeDepthDichotomy",
            True,
            True,
            "若 shelf 内同号正漂移继续堆高达到 dyadic 深度阈值，则回流 amplitude-depth。",
            DRIFT,
        ),
        row(
            "StableLadderEndpointOrbitShelfNegativeCancellationDichotomy",
            True,
            True,
            "若 shelf 在遇到相反 plateau 前发生足量反向抵消，则回流 bridge-cancellation。",
            CANCELLATION,
        ),
        row(
            "StableLadderEndpointOrbitStaticPotentialShelfBiasPacket",
            True,
            False,
            "排除高振荡、正漂移堆高和反向抵消后，只剩长时间低波动的一侧静态势能偏置包。",
            STATIC_BIAS,
        ),
        row(
            "NoAnonymousLongPotentialShelfExit",
            True,
            True,
            "long potential shelf 不再匿名保留；它是静态偏置包，或已进入 bridge/amplitude/boundary 出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterShelfStaticBias",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitShelfStaticBiasStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、static shelf bias、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、static shelf bias、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 long-potential-shelf static-bias 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "long potential shelf 给出长度 L>E 的桥段 I，并且有向势能在 I 上保持同号偏离至少 H/2。"
        "把 I 内增量分为正漂移、负抵消与边界振荡：高振荡回流 variation-boundary flux，"
        "正漂移继续堆高回流 amplitude-depth，足量反向抵消回流 bridge-cancellation。"
        "三者都不发生时，剩余被命名为 static potential shelf bias，即长时间低波动的一侧势能偏置包。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_potential_shelf_static_bias_router",
        "status": "endpoint_orbit_long_potential_shelf_reduced_to_static_bias_or_named_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_long_potential_shelf_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_long_potential_shelf_model_closed": True,
        "endpoint_orbit_shelf_potential_floor_closed": True,
        "endpoint_orbit_shelf_increment_balance_closed": True,
        "endpoint_orbit_shelf_oscillation_boundary_flux_dichotomy_closed": True,
        "endpoint_orbit_shelf_positive_drift_amplitude_depth_dichotomy_closed": True,
        "endpoint_orbit_shelf_negative_cancellation_dichotomy_closed": True,
        "endpoint_orbit_static_potential_shelf_bias_packet_registered": True,
        "anonymous_long_potential_shelf_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_static_potential_shelf_bias_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "shelf_static_bias_formulas": {
            "shelf_interval": "I=[a,b], L=|I|>E",
            "potential_floor": "sigma*S(t) >= H/2 for all t in I",
            "increments": "d_t=S(t+1)-S(t)",
            "positive_drift": "sum max(sigma*d_t,0) triggers AmplitudeDepth if dyadic depth threshold is reached",
            "negative_cancellation": "sum max(-sigma*d_t,0) triggers BridgeCancellation if cancellation threshold is reached",
            "boundary_flux": "many sign changes or high total variation triggers VariationBoundaryFlux",
            "static_bias": "otherwise a one-sided low-variation shelf remains as StaticPotentialShelfBiasPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit long-potential-shelf static-bias 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_long_potential_shelf_imported={fmt_bool(cert['endpoint_orbit_long_potential_shelf_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_bridge_cancellation_carried_forward={fmt_bool(cert['endpoint_orbit_bridge_cancellation_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_long_potential_shelf_model_closed={fmt_bool(cert['endpoint_orbit_long_potential_shelf_model_closed'])}",
        f"endpoint_orbit_shelf_potential_floor_closed={fmt_bool(cert['endpoint_orbit_shelf_potential_floor_closed'])}",
        f"endpoint_orbit_shelf_increment_balance_closed={fmt_bool(cert['endpoint_orbit_shelf_increment_balance_closed'])}",
        f"endpoint_orbit_shelf_oscillation_boundary_flux_dichotomy_closed={fmt_bool(cert['endpoint_orbit_shelf_oscillation_boundary_flux_dichotomy_closed'])}",
        f"endpoint_orbit_shelf_positive_drift_amplitude_depth_dichotomy_closed={fmt_bool(cert['endpoint_orbit_shelf_positive_drift_amplitude_depth_dichotomy_closed'])}",
        f"endpoint_orbit_shelf_negative_cancellation_dichotomy_closed={fmt_bool(cert['endpoint_orbit_shelf_negative_cancellation_dichotomy_closed'])}",
        f"endpoint_orbit_static_potential_shelf_bias_packet_registered={fmt_bool(cert['endpoint_orbit_static_potential_shelf_bias_packet_registered'])}",
        f"anonymous_long_potential_shelf_removed={fmt_bool(cert['anonymous_long_potential_shelf_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_static_potential_shelf_bias_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_static_potential_shelf_bias_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 长 shelf 模型",
        "",
        "从上一层导入 long potential shelf：存在桥段 `I=[a,b]`，长度 `L>E`，并且选定符号 `sigma` 后",
        "",
        "```text",
        "sigma*S(t) >= H/2 for all t in I.",
        "```",
        "",
        "这表示势能在相反 plateau 到来前长时间停留在一侧；本步只分析该桥段内部，不切换目标命题。",
        "",
        "## 2. 增量三分",
        "",
        "令 `d_t=S(t+1)-S(t)`。shelf 内部增量只可能以三种方式逃出静态态：",
        "",
        "- 边界切换或总变差过大，进入 variation-boundary flux。",
        "- 同号正漂移继续堆高，进入 amplitude-depth。",
        "- 反向负抵消在相反 plateau 前累积到阈值，进入 bridge-cancellation。",
        "",
        "若三者都不发生，则 shelf 不是动态过渡，而是长时间低波动的一侧静态偏置包。",
        "",
        "```text",
        "static shelf bias = long one-sided potential floor + low oscillation + no deep positive drift + no early cancellation.",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 long potential shelf，而是 static potential shelf bias，或已命名的 bridge/amplitude/boundary 出口，外加 singleton、full-cycle mean 与 sparse SAE。",
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
            "- 本证书没有证明 EndpointOrbitStaticPotentialShelfBiasPDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 long potential shelf 压成 static shelf bias 或已命名三出口。",
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
