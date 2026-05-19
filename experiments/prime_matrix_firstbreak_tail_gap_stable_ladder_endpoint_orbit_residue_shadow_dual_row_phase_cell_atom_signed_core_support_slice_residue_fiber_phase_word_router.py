#!/usr/bin/env python3
"""生成 support-slice residue-fiber phase-word 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalanceImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger"
PHASE_WORD_MODEL = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordModelLedger"
PHASE_WORD_QUOTA_DEBT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordQuotaDebtAllocationLedger"
OVERFULL_PHASE_WORD = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordPigeonholeLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordNamedReturnSplitLedger"
PHASE_WORD_PACKET = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePacketLedger"
NO_ANON = "NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalanceExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {PHASE_WORD_MODEL} "
    f"AND {PHASE_WORD_QUOTA_DEBT} AND {OVERFULL_PHASE_WORD} AND {RETURN_SPLIT} "
    f"AND {PHASE_WORD_PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 residue-fiber imbalance 硬点替换成 phase-word imbalance 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 residue-fiber phase-word 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalanceImported", imported, False, "上一层剩余含 residue-fiber imbalance 或 sparse/atom/mean/三出口。", PREVIOUS_TARGET),
        row("StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWord", True, False, "phase word 退化成真实孤立点时继续由 singleton atom/SAE 承接。", SINGLETON),
        row("StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWord", True, False, "phase word 只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。", FULL_MEAN),
        row("StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWord", True, False, "phase word 内抵消债或镜像互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWord", True, False, "同号 phase word 跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWord", True, False, "phase word 穿越 residue、atom 或 phase-cell 边界时继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordModel", True, True, "把 overfull residue fiber 的 C_{s,rho} 按有限 CRT phase word omega 分解为 C_{s,rho,omega}。", PHASE_WORD_MODEL),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordQuotaDebtAllocation", True, True, "把 d_{s,rho} 同步分配为 d_{s,rho,omega}，满足 sum_omega d_{s,rho,omega}=d_{s,rho}。", PHASE_WORD_QUOTA_DEBT),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordPigeonhole", True, True, "若 C_{s,rho}>d_{s,rho}，则存在 omega 使 C_{s,rho,omega}>d_{s,rho,omega}。", OVERFULL_PHASE_WORD),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordNamedReturnSplit", True, True, "overfull phase word 的孤立、均值、反号债、堆高、边界迁移分别回流已有出口。", RETURN_SPLIT),
        row("StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePacket", True, False, "若已有出口不支付，剩余就是真实 phase-word imbalance PDEC/cap。", PHASE_WORD_PACKET),
        row("NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalanceExit", True, True, "residue-fiber imbalance 不再匿名保留；它是 phase-word imbalance 或已有命名出口。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWord", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、phase-word imbalance、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍需关闭 singleton、full-cycle mean、phase-word imbalance、bridge cancellation、amplitude-depth、boundary flux 或 sparse SAE。", NEW_TARGET),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 residue-fiber phase-word 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "residue-fiber imbalance 给出 C_{s,rho}>d_{s,rho}。"
        "把 C_{s,rho} 按实际 CRT phase word omega 分解为 C_{s,rho,omega}，并把局部 quota 加抵消债分配为 d_{s,rho,omega}。"
        "若所有 C_{s,rho,omega}<=d_{s,rho,omega}，则加总得到 C_{s,rho}<=d_{s,rho}，矛盾；因此至少一个 phase word 真实超额。"
        "已有出口能支付则回流；真正剩余是 residue-fiber phase-word imbalance。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_router",
        "status": "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_reduced_to_phase_word_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_model_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_quota_debt_allocation_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_pigeonhole_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_named_return_split_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_packet_registered": True,
        "anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_formulas": {
            "residue_fiber_phase_word_load": "C_{s,rho}=sum_omega C_{s,rho,omega}",
            "quota_debt_phase_word": "d_{s,rho}=sum_omega d_{s,rho,omega}",
            "overfull_phase_word": "C_{s,rho}>d_{s,rho} => exists omega with C_{s,rho,omega}>d_{s,rho,omega}",
            "new_exit": "ResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_imported={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_imported'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_model_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_model_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_quota_debt_allocation_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_quota_debt_allocation_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_pigeonhole_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_pigeonhole_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_named_return_split_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_named_return_split_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_packet_registered={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_packet_registered'])}",
        f"anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_removed={fmt_bool(cert['anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_removed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. phase-word 分解",
        "",
        "把已超额的 residue fiber `(s,rho)` 继续同步分解到有限 CRT phase word `omega`：",
        "",
        "```text",
        "C_{s,rho}=sum_omega C_{s,rho,omega}",
        "d_{s,rho}=sum_omega d_{s,rho,omega}",
        "C_{s,rho}>d_{s,rho} => exists omega with C_{s,rho,omega}>d_{s,rho,omega}.",
        "```",
        "",
        "因此 residue-fiber 超额不能匿名停留，必须落在某个实际 phase word。",
        "",
        "## 2. 回流出口",
        "",
        "overfull phase word 若退化为孤立点或整周期均值，回到 singleton 或 full-cycle mean；若由抵消债、跨尺度堆高或边界迁移支付，则回到 bridge、amplitude 或 boundary。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 residue-fiber imbalance，而是具体 phase-word imbalance，或 mean/singleton/sparse/三出口。",
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
            "- 本证书没有证明 EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCap。",
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
