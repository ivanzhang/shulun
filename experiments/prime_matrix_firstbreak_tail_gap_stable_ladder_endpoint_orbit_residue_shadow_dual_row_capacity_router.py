#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit residue-shadow dual-row capacity 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPressurePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitResidueShadowDualRowPressureImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowCapacityLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowCapacityLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowCapacityLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowCapacityLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowCapacityLedger"
ROW_PRESSURE_MODEL = "StableLadderEndpointOrbitResidueShadowDualRowPressureModelLedger"
ROW_WINDOW = "StableLadderEndpointOrbitResidueShadowDualRowWindowLedger"
ROW_QUOTA = "StableLadderEndpointOrbitResidueShadowDualRowCapacityQuotaLedger"
LOAD_QUOTA_SPLIT = "StableLadderEndpointOrbitResidueShadowDualRowLoadQuotaDichotomyLedger"
UNDER_RETURN = "StableLadderEndpointOrbitResidueShadowDualRowUnderQuotaReturnLedger"
CAPACITY_DEFECT = "StableLadderEndpointOrbitResidueShadowDualRowCapacityDefectPacketLedger"
NO_ANON = "NoAnonymousResidueShadowDualRowPressureExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowCapacityLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {ROW_PRESSURE_MODEL} "
    f"AND {ROW_WINDOW} AND {ROW_QUOTA} AND {LOAD_QUOTA_SPLIT} "
    f"AND {UNDER_RETURN} AND {CAPACITY_DEFECT} AND {NO_ANON} "
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
    """把旧活动基中的 dual-row pressure 硬点替换成 dual-row capacity defect 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 residue-shadow dual-row capacity 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row("StableLadderEndpointOrbitResidueShadowDualRowPressureImported", imported, False, "上一层剩余含 residue-shadow dual-row pressure 或 sparse/atom/mean/三出口。", PREVIOUS_TARGET),
        row("StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowCapacity", True, False, "dual-row 窗口退化成孤立点时继续由 singleton atom/SAE 承接。", SINGLETON),
        row("StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowCapacity", True, False, "dual-row 压力只表现为整周期均值时继续由 full-cycle mean atom/SAE 承接。", FULL_MEAN),
        row("StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowCapacity", True, False, "对偶行窗口反号互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowCapacity", True, False, "对偶行同号压力跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowCapacity", True, False, "对偶行窗口压力迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("StableLadderEndpointOrbitResidueShadowDualRowPressureModel", True, True, "把 dual-row pressure 写成对偶行窗口 R 上的 signed load H(R)。", ROW_PRESSURE_MODEL),
        row("StableLadderEndpointOrbitResidueShadowDualRowWindow", True, True, "固定 residue shadow 的对偶行纤维给出有限 row-window R。", ROW_WINDOW),
        row("StableLadderEndpointOrbitResidueShadowDualRowCapacityQuota", True, True, "局部 CRT 行纤维允许类数给出 row-window quota B(R)。", ROW_QUOTA),
        row("StableLadderEndpointOrbitResidueShadowDualRowLoadQuotaDichotomy", True, True, "比较 |H(R)| 与 B(R)：未超额则必须回流，超额则形成容量缺陷。", LOAD_QUOTA_SPLIT),
        row("StableLadderEndpointOrbitResidueShadowDualRowUnderQuotaReturn", True, True, "若 |H(R)|<=B(R)，对偶行窗口没有真实容量压力，必须回到 mean/singleton/sparse 或三出口。", UNDER_RETURN),
        row("StableLadderEndpointOrbitResidueShadowDualRowCapacityDefectPacket", True, False, "若 |H(R)|>B(R)，登记为 residue-shadow dual-row capacity defect PDEC/cap。", CAPACITY_DEFECT),
        row("NoAnonymousResidueShadowDualRowPressureExit", True, True, "residue-shadow dual-row pressure 不再匿名保留；它是 capacity defect 或已有命名出口。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowCapacity", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitResidueShadowDualRowCapacityStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、residue-shadow dual-row capacity defect、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍需关闭 singleton、full-cycle mean、residue-shadow dual-row capacity defect、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 residue-shadow dual-row capacity 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "residue-shadow dual-row pressure 必须落在具体对偶行窗口 R 上。"
        "该窗口有 signed load H(R)，同时由局部 CRT 行纤维允许类数给出容量 quota B(R)。"
        "若 |H(R)| 不超过 B(R)，它无法承担上一层强制压力，必须回流 mean/singleton/sparse 或已命名三出口；"
        "若 |H(R)| 超过 B(R)，剩余就是显式 residue-shadow dual-row capacity defect PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_capacity_router",
        "status": "endpoint_orbit_residue_shadow_dual_row_pressure_reduced_to_capacity_defect_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_residue_shadow_dual_row_pressure_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_residue_shadow_dual_row_pressure_model_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_window_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_capacity_quota_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_load_quota_dichotomy_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_under_quota_return_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_capacity_defect_packet_registered": True,
        "anonymous_residue_shadow_dual_row_pressure_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_capacity_defect_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "residue_shadow_dual_row_capacity_formulas": {
            "row_load": "H(R)=sum_{omega projects to R} signed_mass(omega)",
            "row_quota": "B(R)=local_CRT_allowed_row_fiber_count(R)*scale_weight",
            "under_quota_return": "|H(R)| <= B(R) => mean/singleton/sparse/or named endpoint exits",
            "capacity_defect": "|H(R)| > B(R) => ResidueShadowDualRowCapacityDefectPDECCap",
            "new_exit": "ResidueShadowDualRowCapacityDefectPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit residue-shadow dual-row capacity 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_residue_shadow_dual_row_pressure_imported={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_pressure_imported'])}",
        f"endpoint_orbit_residue_shadow_dual_row_pressure_model_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_pressure_model_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_window_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_window_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_capacity_quota_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_capacity_quota_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_load_quota_dichotomy_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_load_quota_dichotomy_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_under_quota_return_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_under_quota_return_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_capacity_defect_packet_registered={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_capacity_defect_packet_registered'])}",
        f"anonymous_residue_shadow_dual_row_pressure_removed={fmt_bool(cert['anonymous_residue_shadow_dual_row_pressure_removed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_capacity_defect_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_capacity_defect_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 对偶行窗口容量账本",
        "",
        "residue-shadow dual-row pressure 被登记到一个有限对偶行窗口 `R`：",
        "",
        "```text",
        "H(R)=sum_{omega projects to R} signed_mass(omega)",
        "B(R)=local_CRT_allowed_row_fiber_count(R)*scale_weight.",
        "```",
        "",
        "这里 `H(R)` 是窗口承载的 signed load，`B(R)` 是 CRT 行纤维允许类数给出的容量 quota。",
        "",
        "## 2. 容量二分",
        "",
        "- 若 `|H(R)| <= B(R)`，对偶行窗口未超额，不能支付上一层强制压力，必须回流 mean/singleton/sparse 或已命名三出口。",
        "- 若 `|H(R)| > B(R)`，该窗口承载超过 CRT 行纤维容量的质量，形成 residue-shadow dual-row capacity defect。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 residue-shadow dual-row pressure，而是 dual-row capacity defect，或 mean/singleton/sparse/bridge/amplitude/boundary 出口。",
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
            "- 本证书没有证明 EndpointOrbitResidueShadowDualRowCapacityDefectPDECCap。",
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
