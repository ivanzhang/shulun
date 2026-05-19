#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit bipolar-shelf 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_bipolar_shelf_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseSeparatedBipolarPlateauPairImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterBipolarShelfLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterBipolarShelfLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterBipolarShelfLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterBipolarShelfLedger"
BIPOLAR_MODEL = "StableLadderEndpointOrbitPhaseSeparatedBipolarPairModelLedger"
POTENTIAL_COORD = "StableLadderEndpointOrbitBipolarPrefixPotentialCoordinateLedger"
BRIDGE_DECOMP = "StableLadderEndpointOrbitBipolarBridgeDecompositionLedger"
BRIDGE_SPLIT = "StableLadderEndpointOrbitBridgeCancellationOrShelfDichotomyLedger"
CANCEL_PACKET = "StableLadderEndpointOrbitBridgeCancellationPacketLedger"
SHELF_PACKET = "StableLadderEndpointOrbitLongPotentialShelfPacketLedger"
NO_ANON = "NoAnonymousPhaseSeparatedBipolarPlateauPairExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterBipolarShelfLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {AMPLITUDE_DEPTH} "
    f"AND {BOUNDARY} AND {BIPOLAR_MODEL} AND {POTENTIAL_COORD} "
    f"AND {BRIDGE_DECOMP} AND {BRIDGE_SPLIT} AND {CANCEL_PACKET} "
    f"AND {SHELF_PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 phase-separated bipolar 硬点替换成 shelf 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 bipolar-shelf 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitPhaseSeparatedBipolarPlateauPairImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、phase-separated bipolar pair、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterBipolarShelf",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterBipolarShelf",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterBipolarShelf",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传；本步不排斥该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterBipolarShelf",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传；本步不排斥该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitPhaseSeparatedBipolarPairModel",
            True,
            True,
            "固定相位分离的正 plateau P、负 plateau Q，且二者之间的两个 cyclic gap 均超过 E。",
            BIPOLAR_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitBipolarPrefixPotentialCoordinate",
            True,
            True,
            "定义有向势能 S(t)=sum_{i<=t}sigma*Y_i；P 使 S 上升，Q 使 S 回落。",
            POTENTIAL_COORD,
        ),
        row(
            "StableLadderEndpointOrbitBipolarBridgeDecomposition",
            True,
            True,
            "把 P 末端到 Q 起点、Q 末端到 P 起点的两条桥段作为显式桥段，而非匿名相位间隔。",
            BRIDGE_DECOMP,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationOrShelfDichotomy",
            True,
            True,
            "若桥段在遇到相反 plateau 前抵消至少半个高度，则登记 bridge-cancellation；否则出现长势能 shelf。",
            BRIDGE_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationPacket",
            True,
            False,
            "桥段提前抵消登记为 bridge-cancellation PDEC/cap；本步不排斥该 cap。",
            CANCEL_PACKET,
        ),
        row(
            "StableLadderEndpointOrbitLongPotentialShelfPacket",
            True,
            False,
            "无提前抵消时，高/低势能在长桥段上保持，登记为 long potential shelf PDEC/cap。",
            SHELF_PACKET,
        ),
        row(
            "NoAnonymousPhaseSeparatedBipolarPlateauPairExit",
            True,
            True,
            "phase-separated bipolar pair 不再匿名保留；它是 bridge cancellation 或 long shelf。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterBipolarShelf",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitBipolarShelfStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、long shelf、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、long shelf、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 bipolar-shelf 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "phase-separated bipolar plateau pair 给出正 plateau P 与负 plateau Q，二者之间的 cyclic gaps 均超过 E。"
        "用有向前缀势能 S(t)=sum_{i<=t}sigma*Y_i 观察：P 使 S 上升，Q 使 S 回落。"
        "从 P 末端到 Q 起点的桥段若在遇到 Q 前抵消至少半个高度，则这是 bridge-cancellation；"
        "否则 S 在长桥段上保持高位，形成 long potential shelf。反向桥段同理。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_bipolar_shelf_router",
        "status": "endpoint_orbit_phase_separated_bipolar_pair_reduced_to_bridge_cancellation_or_long_shelf_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_phase_separated_bipolar_plateau_pair_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_phase_separated_bipolar_pair_model_closed": True,
        "endpoint_orbit_bipolar_prefix_potential_coordinate_closed": True,
        "endpoint_orbit_bipolar_bridge_decomposition_closed": True,
        "endpoint_orbit_bridge_cancellation_or_shelf_dichotomy_closed": True,
        "endpoint_orbit_bridge_cancellation_packet_registered": True,
        "endpoint_orbit_long_potential_shelf_packet_registered": True,
        "anonymous_phase_separated_bipolar_plateau_pair_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_long_potential_shelf_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "bipolar_shelf_formulas": {
            "phase_separated_pair": "P positive plateau, Q negative plateau, both cyclic gaps > E",
            "potential": "S(t)=sum_{i<=t}sigma*Y_i",
            "positive_rise": "S rises by at least H on P",
            "negative_return": "S falls by at least H on Q",
            "bridge_cancellation": "if a bridge changes S by at least H/2 before the opposite plateau, BridgeCancellationPDECCap",
            "long_shelf": "otherwise S remains at height at least H/2 across a bridge of length > E",
            "new_exit": "LongPotentialShelfPDECCapOrBridgeCancellationPDECCapOrAmplitudeDepthPDECCapOrVariationBoundaryFluxPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit bipolar-shelf 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_phase_separated_bipolar_plateau_pair_imported={fmt_bool(cert['endpoint_orbit_phase_separated_bipolar_plateau_pair_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_phase_separated_bipolar_pair_model_closed={fmt_bool(cert['endpoint_orbit_phase_separated_bipolar_pair_model_closed'])}",
        f"endpoint_orbit_bipolar_prefix_potential_coordinate_closed={fmt_bool(cert['endpoint_orbit_bipolar_prefix_potential_coordinate_closed'])}",
        f"endpoint_orbit_bipolar_bridge_decomposition_closed={fmt_bool(cert['endpoint_orbit_bipolar_bridge_decomposition_closed'])}",
        f"endpoint_orbit_bridge_cancellation_or_shelf_dichotomy_closed={fmt_bool(cert['endpoint_orbit_bridge_cancellation_or_shelf_dichotomy_closed'])}",
        f"endpoint_orbit_bridge_cancellation_packet_registered={fmt_bool(cert['endpoint_orbit_bridge_cancellation_packet_registered'])}",
        f"endpoint_orbit_long_potential_shelf_packet_registered={fmt_bool(cert['endpoint_orbit_long_potential_shelf_packet_registered'])}",
        f"anonymous_phase_separated_bipolar_plateau_pair_removed={fmt_bool(cert['anonymous_phase_separated_bipolar_plateau_pair_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_long_potential_shelf_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_long_potential_shelf_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 双极桥段模型",
        "",
        "相位分离双极包给出正 plateau `P` 与负 plateau `Q`，并且二者之间两个 cyclic gaps 都超过 `E`。定义有向势能：",
        "",
        "```text",
        "S(t)=sum_{i<=t} sigma*Y_i.",
        "```",
        "",
        "`P` 使 `S` 上升，`Q` 使 `S` 回落。两个 gap 被视为显式 bridge，不再是无标签相位间隔。",
        "",
        "## 2. 抵消或 shelf 二分",
        "",
        "若从 `P` 末端到 `Q` 起点的桥段在遇到 `Q` 前已抵消至少半个高度，则登记为 bridge-cancellation PDEC/cap。否则势能在这条长桥段上保持至少半高度，形成 long potential shelf。反向桥段同理。",
        "",
        "```text",
        "bridge cancellation: |Delta S_bridge| >= H/2;",
        "long shelf: S remains displaced by >= H/2 over a bridge of length > E.",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 phase-separated bipolar pair，而是 bridge cancellation 或 long potential shelf，外加 amplitude-depth、boundary flux、singleton、full-cycle mean 与 sparse SAE。",
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
            "- 本证书没有证明 EndpointOrbitLongPotentialShelfPDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 phase-separated bipolar pair 压成 bridge cancellation 或 long potential shelf。",
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
