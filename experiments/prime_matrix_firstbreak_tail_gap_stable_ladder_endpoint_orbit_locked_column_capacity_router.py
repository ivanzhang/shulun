#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit locked-column capacity 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitLockedPhaseCellColumnPressureImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedColumnCapacityLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedColumnCapacityLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedColumnCapacityLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedColumnCapacityLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedColumnCapacityLedger"
COLUMN_MODEL = "StableLadderEndpointOrbitLockedColumnFamilyModelLedger"
FIBER_QUOTA = "StableLadderEndpointOrbitLockedColumnFiberQuotaLedger"
LOAD_SPLIT = "StableLadderEndpointOrbitLockedColumnLoadQuotaDichotomyLedger"
UNDER_RETURN = "StableLadderEndpointOrbitLockedColumnUnderQuotaReturnLedger"
CAPACITY_DEFECT = "StableLadderEndpointOrbitLockedColumnCapacityDefectPacketLedger"
NO_ANON = "NoAnonymousLockedPhaseCellColumnPressureExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterLockedColumnCapacityLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {COLUMN_MODEL} "
    f"AND {FIBER_QUOTA} AND {LOAD_SPLIT} AND {UNDER_RETURN} "
    f"AND {CAPACITY_DEFECT} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 locked column-pressure 硬点替换成 capacity defect 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 locked-column capacity 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitLockedPhaseCellColumnPressureImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、locked phase-cell column pressure、bridge cancellation、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row("StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedColumnCapacity", True, False, "列族宽度退化到孤立点时回到 singleton atom/SAE。", SINGLETON),
        row("StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedColumnCapacity", True, False, "列压力只表现为整周期均值时回到 full-cycle mean atom/SAE。", FULL_MEAN),
        row("StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedColumnCapacity", True, False, "反号列簇互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedColumnCapacity", True, False, "同号列簇堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedColumnCapacity", True, False, "列族边界迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("StableLadderEndpointOrbitLockedColumnFamilyModel", True, True, "把持久 actual residue word 投影为固定列或窄列族 C，带 signed load L(C)。", COLUMN_MODEL),
        row("StableLadderEndpointOrbitLockedColumnFiberQuota", True, True, "列纤维的可承载容量由局部 CRT 允许类数与尺度窗口给出 quota Q(C)。", FIBER_QUOTA),
        row("StableLadderEndpointOrbitLockedColumnLoadQuotaDichotomy", True, True, "比较 |L(C)| 与 Q(C)：不足则必须回到均值/原子/稀疏或已有三出口；超额则产生容量缺陷。", LOAD_SPLIT),
        row("StableLadderEndpointOrbitLockedColumnUnderQuotaReturn", True, True, "若列压力未超额，它不能支付上一层强制质量，必须回流 full-cycle mean、singleton、sparse 或三出口。", UNDER_RETURN),
        row("StableLadderEndpointOrbitLockedColumnCapacityDefectPacket", True, False, "若列压力超出 quota，则登记为 locked column capacity defect PDEC/cap。", CAPACITY_DEFECT),
        row("NoAnonymousLockedPhaseCellColumnPressureExit", True, True, "locked column pressure 不再匿名保留；它是容量缺陷或已有命名出口。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterLockedColumnCapacity", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitLockedColumnCapacityStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、locked column capacity defect、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍需关闭 singleton、full-cycle mean、locked column capacity defect、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 locked-column capacity 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "locked phase-cell column pressure 给出固定列或窄列族 C 上的 signed load。"
        "列纤维有由局部 CRT 允许类数决定的容量 quota Q(C)。"
        "若 |L(C)| 不超过 quota，则它无法支付上一层锁定质量，必须回流 mean/singleton/sparse 或已命名三出口；"
        "若 |L(C)| 超过 quota，则得到真正的 locked column capacity defect PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_capacity_router",
        "status": "endpoint_orbit_locked_phase_cell_column_pressure_reduced_to_locked_column_capacity_defect_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_locked_phase_cell_column_pressure_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_locked_column_family_model_closed": True,
        "endpoint_orbit_locked_column_fiber_quota_closed": True,
        "endpoint_orbit_locked_column_load_quota_dichotomy_closed": True,
        "endpoint_orbit_locked_column_under_quota_return_closed": True,
        "endpoint_orbit_locked_column_capacity_defect_packet_registered": True,
        "anonymous_locked_phase_cell_column_pressure_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_locked_column_capacity_defect_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "locked_column_capacity_formulas": {
            "load": "L(C)=sum_{omega projects to C} signed_mass(omega)",
            "quota": "Q(C)=local_CRT_allowed_fiber_count(C)*scale_weight",
            "under_quota_return": "|L(C)| <= Q(C) => mean/singleton/sparse/or named endpoint exits",
            "capacity_defect": "|L(C)| > Q(C) => LockedColumnCapacityDefectPDECCap",
            "new_exit": "LockedColumnCapacityDefectPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit locked-column capacity 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_locked_phase_cell_column_pressure_imported={fmt_bool(cert['endpoint_orbit_locked_phase_cell_column_pressure_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_bridge_cancellation_carried_forward={fmt_bool(cert['endpoint_orbit_bridge_cancellation_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_locked_column_family_model_closed={fmt_bool(cert['endpoint_orbit_locked_column_family_model_closed'])}",
        f"endpoint_orbit_locked_column_fiber_quota_closed={fmt_bool(cert['endpoint_orbit_locked_column_fiber_quota_closed'])}",
        f"endpoint_orbit_locked_column_load_quota_dichotomy_closed={fmt_bool(cert['endpoint_orbit_locked_column_load_quota_dichotomy_closed'])}",
        f"endpoint_orbit_locked_column_under_quota_return_closed={fmt_bool(cert['endpoint_orbit_locked_column_under_quota_return_closed'])}",
        f"endpoint_orbit_locked_column_capacity_defect_packet_registered={fmt_bool(cert['endpoint_orbit_locked_column_capacity_defect_packet_registered'])}",
        f"anonymous_locked_phase_cell_column_pressure_removed={fmt_bool(cert['anonymous_locked_phase_cell_column_pressure_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_locked_column_capacity_defect_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_locked_column_capacity_defect_pdec_cap_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定列容量账本",
        "",
        "上一层的持久 actual residue word 投影成固定列或窄列族 `C`。登记 signed load 与容量：",
        "",
        "```text",
        "L(C)=sum_{omega projects to C} signed_mass(omega)",
        "Q(C)=local_CRT_allowed_fiber_count(C)*scale_weight.",
        "```",
        "",
        "## 2. 容量二分",
        "",
        "- 若 `|L(C)| <= Q(C)`，列压力未超额，无法支付上一层强制锁定质量，必须回流 mean/singleton/sparse 或已命名三出口。",
        "- 若 `|L(C)| > Q(C)`，则固定列族承载超过 CRT 允许纤维容量的质量，形成 locked column capacity defect。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 locked phase-cell column pressure，而是 locked column capacity defect，或 mean/singleton/sparse/bridge/amplitude/boundary 出口。",
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
            "- 本证书没有证明 EndpointOrbitLockedColumnCapacityDefectPDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 locked column pressure 压成 capacity defect 包或 mean/singleton/sparse/三出口。",
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
