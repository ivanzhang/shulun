#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit locked-column residue-shadow 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_residue_shadow_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitLockedColumnCapacityDefectImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedColumnResidueShadowLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedColumnResidueShadowLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedColumnResidueShadowLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedColumnResidueShadowLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedColumnResidueShadowLedger"
SHADOW_MODEL = "StableLadderEndpointOrbitLockedColumnResidueShadowModelLedger"
SHADOW_QUOTA = "StableLadderEndpointOrbitLockedColumnResidueShadowQuotaLedger"
OVERFULL_SHADOW = "StableLadderEndpointOrbitLockedColumnOverfullShadowPigeonholeLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitLockedColumnResidueShadowNamedReturnSplitLedger"
SHADOW_PACKET = "StableLadderEndpointOrbitLockedColumnResidueShadowImbalancePacketLedger"
NO_ANON = "NoAnonymousLockedColumnCapacityDefectExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterLockedColumnResidueShadowLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnResidueShadowImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {SHADOW_MODEL} "
    f"AND {SHADOW_QUOTA} AND {OVERFULL_SHADOW} AND {RETURN_SPLIT} "
    f"AND {SHADOW_PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 locked-column capacity 硬点替换成 residue-shadow 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 locked-column residue-shadow 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row("StableLadderEndpointOrbitLockedColumnCapacityDefectImported", imported, False, "上一层剩余含 locked column capacity defect 或 sparse/atom/mean/三出口。", PREVIOUS_TARGET),
        row("StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedColumnResidueShadow", True, False, "单 shadow 退化为孤立点时继续由 singleton atom/SAE 承接。", SINGLETON),
        row("StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedColumnResidueShadow", True, False, "所有 shadow 均匀同幅时继续由 full-cycle mean atom/SAE 承接。", FULL_MEAN),
        row("StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedColumnResidueShadow", True, False, "反号 shadow 互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedColumnResidueShadow", True, False, "同号 shadow 跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedColumnResidueShadow", True, False, "overfull shadow 在边界迁移时继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("StableLadderEndpointOrbitLockedColumnResidueShadowModel", True, True, "把列族 C 按 CRT residue shadow s 分解为 C_s，带 signed load L_s。", SHADOW_MODEL),
        row("StableLadderEndpointOrbitLockedColumnResidueShadowQuota", True, True, "容量 quota 逐 shadow 可加：Q(C)=sum_s Q_s。", SHADOW_QUOTA),
        row("StableLadderEndpointOrbitLockedColumnOverfullShadowPigeonhole", True, True, "若 |L(C)|>Q(C)，则不能所有 shadow 都满足 |L_s|<=Q_s；至少一个 shadow overfull。", OVERFULL_SHADOW),
        row("StableLadderEndpointOrbitLockedColumnResidueShadowNamedReturnSplit", True, True, "overfull shadow 的均值、孤立、反号、堆高、迁移部分分别回流已有出口。", RETURN_SPLIT),
        row("StableLadderEndpointOrbitLockedColumnResidueShadowImbalancePacket", True, False, "若已有出口不支付，剩余就是一个真实 overfull residue-shadow imbalance PDEC/cap。", SHADOW_PACKET),
        row("NoAnonymousLockedColumnCapacityDefectExit", True, True, "locked column capacity defect 不再匿名保留；它是 residue-shadow imbalance 或已有命名出口。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterLockedColumnResidueShadow", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitLockedColumnResidueShadowStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、locked column residue-shadow imbalance、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍需关闭 singleton、full-cycle mean、locked column residue-shadow imbalance、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 locked-column residue-shadow 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "locked column capacity defect 给出固定列族 C 的容量超额。"
        "把 C 按 CRT residue shadow 分解为 C_s，并利用 quota 可加性。"
        "若每个 shadow 都不超额，则总列族也不超额，矛盾；因此至少一个 shadow 必须 overfull。"
        "其均值、孤立点、反号互付、同号堆高或迁移部分回流已有出口；真正剩余是 residue-shadow imbalance。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_residue_shadow_router",
        "status": "endpoint_orbit_locked_column_capacity_defect_reduced_to_residue_shadow_imbalance_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_locked_column_capacity_defect_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_locked_column_residue_shadow_model_closed": True,
        "endpoint_orbit_locked_column_residue_shadow_quota_closed": True,
        "endpoint_orbit_locked_column_overfull_shadow_pigeonhole_closed": True,
        "endpoint_orbit_locked_column_residue_shadow_named_return_split_closed": True,
        "endpoint_orbit_locked_column_residue_shadow_imbalance_packet_registered": True,
        "anonymous_locked_column_capacity_defect_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_locked_column_residue_shadow_imbalance_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "locked_column_residue_shadow_formulas": {
            "shadow_load": "L(C)=sum_s L_s",
            "shadow_quota": "Q(C)=sum_s Q_s",
            "overfull_shadow": "|L(C)|>Q(C) => exists s with |L_s|>Q_s after sign selection",
            "new_exit": "LockedColumnResidueShadowImbalancePDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit locked-column residue-shadow 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_locked_column_capacity_defect_imported={fmt_bool(cert['endpoint_orbit_locked_column_capacity_defect_imported'])}",
        f"endpoint_orbit_locked_column_residue_shadow_model_closed={fmt_bool(cert['endpoint_orbit_locked_column_residue_shadow_model_closed'])}",
        f"endpoint_orbit_locked_column_residue_shadow_quota_closed={fmt_bool(cert['endpoint_orbit_locked_column_residue_shadow_quota_closed'])}",
        f"endpoint_orbit_locked_column_overfull_shadow_pigeonhole_closed={fmt_bool(cert['endpoint_orbit_locked_column_overfull_shadow_pigeonhole_closed'])}",
        f"endpoint_orbit_locked_column_residue_shadow_named_return_split_closed={fmt_bool(cert['endpoint_orbit_locked_column_residue_shadow_named_return_split_closed'])}",
        f"endpoint_orbit_locked_column_residue_shadow_imbalance_packet_registered={fmt_bool(cert['endpoint_orbit_locked_column_residue_shadow_imbalance_packet_registered'])}",
        f"anonymous_locked_column_capacity_defect_removed={fmt_bool(cert['anonymous_locked_column_capacity_defect_removed'])}",
        f"endpoint_orbit_locked_column_residue_shadow_imbalance_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_locked_column_residue_shadow_imbalance_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. residue shadow 分解",
        "",
        "把固定列族 `C` 按 CRT residue shadow 分解为 `C_s`：",
        "",
        "```text",
        "L(C)=sum_s L_s",
        "Q(C)=sum_s Q_s.",
        "```",
        "",
        "若 `|L(C)|>Q(C)`，在固定符号选择后不可能所有 `|L_s|<=Q_s`；否则总和也不会超额。",
        "",
        "## 2. 回流出口",
        "",
        "overfull shadow 若退化为孤立点，回到 singleton；若只是整周期均值，回到 full-cycle mean；若反号互付、同号堆高或边界迁移明显，则分别回到 bridge、amplitude 或 boundary。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 locked column capacity defect，而是 locked column residue-shadow imbalance，或 mean/singleton/sparse/三出口。",
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
            "- 本证书没有证明 EndpointOrbitLockedColumnResidueShadowImbalancePDECCap。",
            "- 本证书没有证明 EndpointOrbitBridgeCancellationPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
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
