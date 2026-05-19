#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit residue-shadow dual-row phase-cell 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitResidueShadowDualRowCapacityDefectImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellLedger"
CELL_MODEL = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellModelLedger"
CELL_QUOTA = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellQuotaLedger"
OVERFULL_CELL = "StableLadderEndpointOrbitResidueShadowDualRowOverfullPhaseCellPigeonholeLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellNamedReturnSplitLedger"
CELL_PACKET = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellImbalancePacketLedger"
NO_ANON = "NoAnonymousResidueShadowDualRowCapacityDefectExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {CELL_MODEL} "
    f"AND {CELL_QUOTA} AND {OVERFULL_CELL} AND {RETURN_SPLIT} "
    f"AND {CELL_PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 dual-row capacity defect 硬点替换成 phase-cell imbalance 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 residue-shadow dual-row phase-cell 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row("StableLadderEndpointOrbitResidueShadowDualRowCapacityDefectImported", imported, False, "上一层剩余含 residue-shadow dual-row capacity defect 或 sparse/atom/mean/三出口。", PREVIOUS_TARGET),
        row("StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCell", True, False, "phase-cell 退化成孤立点时继续由 singleton atom/SAE 承接。", SINGLETON),
        row("StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCell", True, False, "phase-cell 只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。", FULL_MEAN),
        row("StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCell", True, False, "相邻或镜像 phase-cell 反号互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCell", True, False, "同号 phase-cell 跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCell", True, False, "overfull phase-cell 穿越窗口边界时继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellModel", True, True, "把对偶行窗口 R 按 CRT phase-cell theta 分解为 R_theta，带 signed load H_theta。", CELL_MODEL),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellQuota", True, True, "容量 quota 逐 phase-cell 可加：B(R)=sum_theta B_theta。", CELL_QUOTA),
        row("StableLadderEndpointOrbitResidueShadowDualRowOverfullPhaseCellPigeonhole", True, True, "若 |H(R)|>B(R)，则固定符号后至少一个 phase-cell 满足 |H_theta|>B_theta。", OVERFULL_CELL),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellNamedReturnSplit", True, True, "overfull phase-cell 的孤立、均值、反号、堆高、边界迁移分别回流已有出口。", RETURN_SPLIT),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellImbalancePacket", True, False, "若已有出口不支付，剩余就是真实 overfull phase-cell imbalance PDEC/cap。", CELL_PACKET),
        row("NoAnonymousResidueShadowDualRowCapacityDefectExit", True, True, "dual-row capacity defect 不再匿名保留；它是 phase-cell imbalance 或已有命名出口。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCell", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitResidueShadowDualRowPhaseCellStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、residue-shadow dual-row phase-cell imbalance、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍需关闭 singleton、full-cycle mean、residue-shadow dual-row phase-cell imbalance、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 residue-shadow dual-row phase-cell 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "residue-shadow dual-row capacity defect 给出对偶行窗口 R 的容量超额。"
        "把 R 按 CRT phase-cell 分解为 R_theta，并利用 quota 可加性。"
        "若每个 phase-cell 都不超额，则整个窗口也不超额，矛盾；因此至少一个 phase-cell 必须 overfull。"
        "其孤立点、整周期均值、反号互付、同号堆高或边界迁移部分回流已有出口；真正剩余是 phase-cell imbalance。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_router",
        "status": "endpoint_orbit_residue_shadow_dual_row_capacity_defect_reduced_to_phase_cell_imbalance_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_residue_shadow_dual_row_capacity_defect_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_model_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_quota_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_overfull_phase_cell_pigeonhole_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_named_return_split_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_packet_registered": True,
        "anonymous_residue_shadow_dual_row_capacity_defect_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "residue_shadow_dual_row_phase_cell_formulas": {
            "phase_cell_load": "H(R)=sum_theta H_theta",
            "phase_cell_quota": "B(R)=sum_theta B_theta",
            "overfull_cell": "|H(R)|>B(R) => exists theta with |H_theta|>B_theta after sign selection",
            "new_exit": "ResidueShadowDualRowPhaseCellImbalancePDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit residue-shadow dual-row phase-cell 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_residue_shadow_dual_row_capacity_defect_imported={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_capacity_defect_imported'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_model_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_model_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_quota_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_quota_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_overfull_phase_cell_pigeonhole_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_overfull_phase_cell_pigeonhole_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_named_return_split_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_named_return_split_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_packet_registered={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_packet_registered'])}",
        f"anonymous_residue_shadow_dual_row_capacity_defect_removed={fmt_bool(cert['anonymous_residue_shadow_dual_row_capacity_defect_removed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. phase-cell 分解",
        "",
        "把对偶行窗口 `R` 按 CRT phase-cell 分解为 `R_theta`：",
        "",
        "```text",
        "H(R)=sum_theta H_theta",
        "B(R)=sum_theta B_theta.",
        "```",
        "",
        "若 `|H(R)|>B(R)`，固定符号选择后不可能所有 `|H_theta|<=B_theta`；否则整个窗口也不会超额。",
        "",
        "## 2. 回流出口",
        "",
        "overfull phase-cell 若退化为孤立点，回到 singleton；若只是整周期均值，回到 full-cycle mean；若反号互付、同号堆高或边界迁移明显，则分别回到 bridge、amplitude 或 boundary。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 residue-shadow dual-row capacity defect，而是 residue-shadow dual-row phase-cell imbalance，或 mean/singleton/sparse/三出口。",
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
            "- 本证书没有证明 EndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
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
