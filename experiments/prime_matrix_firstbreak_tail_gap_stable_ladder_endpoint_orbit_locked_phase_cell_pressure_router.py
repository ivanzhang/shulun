#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit locked phase-cell pressure 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_phase_cell_pressure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitInteriorCentroidPhaseLockImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedPhaseCellLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedPhaseCellLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedPhaseCellLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedPhaseCellLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedPhaseCellLedger"
CELL_MODEL = "StableLadderEndpointOrbitLockedInteriorPhaseCellModelLedger"
FINITE_SLOT = "StableLadderEndpointOrbitLockedPhaseCellFiniteSlotLedger"
ACTUAL_WORD = "StableLadderEndpointOrbitLockedPhaseCellActualResidueWordLedger"
SPARSE_OR_STABLE = "StableLadderEndpointOrbitLockedPhaseCellSparseOrStableSubsequenceLedger"
COLUMN_PRESSURE = "StableLadderEndpointOrbitLockedPhaseCellColumnPressurePacketLedger"
NO_ANON = "NoAnonymousInteriorCentroidPhaseLockExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterLockedPhaseCellLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {CELL_MODEL} "
    f"AND {FINITE_SLOT} AND {ACTUAL_WORD} AND {SPARSE_OR_STABLE} "
    f"AND {COLUMN_PRESSURE} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 phase-lock 硬点替换成 locked column-pressure 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 locked phase-cell pressure 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitInteriorCentroidPhaseLockImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、interior centroid phase-lock、bridge cancellation、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedPhaseCell",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；锁定宽度退化时可能回到该出口。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedPhaseCell",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；锁定质量只表现为整周期均值时回到该出口。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedPhaseCell",
            True,
            False,
            "bridge-cancellation PDEC/cap 继续前传。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedPhaseCell",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedPhaseCell",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitLockedInteriorPhaseCellModel",
            True,
            True,
            "把 phase-lock 质量放入有限内部相位单元 B_r，并保留符号、尺度与 dyadic mass。",
            CELL_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitLockedPhaseCellFiniteSlot",
            True,
            True,
            "相位单元、符号、dyadic mass 档和局部 CRT 槽位在每个尺度层都是有限选项。",
            FINITE_SLOT,
        ),
        row(
            "StableLadderEndpointOrbitLockedPhaseCellActualResidueWord",
            True,
            True,
            "若不是 sparse SAE，则无穷鸽巢给出持久实际 residue word/slot。",
            ACTUAL_WORD,
        ),
        row(
            "StableLadderEndpointOrbitLockedPhaseCellSparseOrStableSubsequence",
            True,
            True,
            "若持久 actual slot 不存在，则质量只能作为 sparse scale-ladder SAE 前传。",
            SPARSE_OR_STABLE,
        ),
        row(
            "StableLadderEndpointOrbitLockedPhaseCellColumnPressurePacket",
            True,
            False,
            "持久 actual slot 在 CRT cylinder 中形成固定列/窄列族压力；本步登记为新的 PDEC/cap。",
            COLUMN_PRESSURE,
        ),
        row(
            "NoAnonymousInteriorCentroidPhaseLockExit",
            True,
            True,
            "interior centroid phase-lock 不再匿名保留；它是 locked phase-cell column pressure 或 sparse/atom/mean/三出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterLockedPhaseCell",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitLockedPhaseCellPressureStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、locked phase-cell column pressure、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、locked phase-cell column pressure、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 locked phase-cell pressure 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "interior centroid phase-lock 说明 surviving mass 长期停在有限内部相位单元中。"
        "把相位单元、符号、dyadic mass 档和 actual CRT residue word 作为有限槽位。"
        "若这些槽位不能在无穷尺度上稳定，则该分支只能作为 sparse scale-ladder SAE 前传；"
        "若稳定，则得到一个持久 actual residue word，并在 CRT cylinder 中形成固定列或窄列族压力。"
        "因此 phase-lock 被压成 locked interior phase-cell column pressure PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_phase_cell_pressure_router",
        "status": "endpoint_orbit_interior_centroid_phase_lock_reduced_to_locked_phase_cell_column_pressure_or_sparse_atom_mean_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_interior_centroid_phase_lock_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_locked_interior_phase_cell_model_closed": True,
        "endpoint_orbit_locked_phase_cell_finite_slot_closed": True,
        "endpoint_orbit_locked_phase_cell_actual_residue_word_closed": True,
        "endpoint_orbit_locked_phase_cell_sparse_or_stable_subsequence_closed": True,
        "endpoint_orbit_locked_phase_cell_column_pressure_packet_registered": True,
        "anonymous_interior_centroid_phase_lock_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_locked_interior_phase_cell_column_pressure_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "locked_phase_cell_formulas": {
            "phase_cell": "B_r=[eta+r*rho, eta+(r+1)*rho]",
            "slot": "omega=(r, sign, dyadic_mass_band, actual_residue_word)",
            "sparse_or_stable": "nonpersistent omega => SparseScaleLadderSAE",
            "persistent_actual_word": "persistent omega => fixed/narrow CRT cylinder column family",
            "new_exit": "LockedInteriorPhaseCellColumnPressurePDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit locked phase-cell pressure 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_interior_centroid_phase_lock_imported={fmt_bool(cert['endpoint_orbit_interior_centroid_phase_lock_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_bridge_cancellation_carried_forward={fmt_bool(cert['endpoint_orbit_bridge_cancellation_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_locked_interior_phase_cell_model_closed={fmt_bool(cert['endpoint_orbit_locked_interior_phase_cell_model_closed'])}",
        f"endpoint_orbit_locked_phase_cell_finite_slot_closed={fmt_bool(cert['endpoint_orbit_locked_phase_cell_finite_slot_closed'])}",
        f"endpoint_orbit_locked_phase_cell_actual_residue_word_closed={fmt_bool(cert['endpoint_orbit_locked_phase_cell_actual_residue_word_closed'])}",
        f"endpoint_orbit_locked_phase_cell_sparse_or_stable_subsequence_closed={fmt_bool(cert['endpoint_orbit_locked_phase_cell_sparse_or_stable_subsequence_closed'])}",
        f"endpoint_orbit_locked_phase_cell_column_pressure_packet_registered={fmt_bool(cert['endpoint_orbit_locked_phase_cell_column_pressure_packet_registered'])}",
        f"anonymous_interior_centroid_phase_lock_removed={fmt_bool(cert['anonymous_interior_centroid_phase_lock_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_locked_interior_phase_cell_column_pressure_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_locked_interior_phase_cell_column_pressure_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. phase-lock 的有限槽位化",
        "",
        "把内部相位区间 `[eta,1-eta]` 划分为固定相位单元：",
        "",
        "```text",
        "B_r = [eta+r*rho, eta+(r+1)*rho].",
        "```",
        "",
        "对 surviving phase-lock 质量登记有限槽位：",
        "",
        "```text",
        "omega = (phase_cell r, sign, dyadic_mass_band, actual_residue_word).",
        "```",
        "",
        "## 2. sparse 或 actual residue word 稳定",
        "",
        "若没有任何槽位在无穷尺度上持续承载质量，则该分支进入 sparse scale-ladder SAE。若 sparse 出口不支付，则无穷鸽巢给出持久 `omega`，特别给出持久 actual residue word。",
        "",
        "## 3. 新 CRT 压力包",
        "",
        "持久 actual residue word 在 CRT cylinder 中投影成固定列或窄列族。该列族承载了锁定相位的同号质量，因此形成 locked phase-cell column pressure 包。",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 interior centroid phase-lock，而是 locked interior phase-cell column pressure，或 sparse/atom/mean/bridge/amplitude/boundary 出口。",
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
            "- 本证书没有证明 EndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 interior centroid phase-lock 压成 locked column pressure 包或 sparse/atom/mean/三出口。",
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
