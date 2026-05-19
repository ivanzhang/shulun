#!/usr/bin/env python3
"""生成 source-atom multiplicity-fiber 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-"
    "signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / (
    "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-"
    "signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-router.json"
)
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalanceImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger"
FIBER_MODEL = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberModelLedger"
FIBER_QUOTA_DEBT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberQuotaDebtAllocationLedger"
OVERFULL_FIBER = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberPigeonholeLedger"
MULTIPLICITY_CAP_PACKET = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPacketLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberNamedReturnSplitLedger"
FIBER_PACKET = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePacketLedger"
NO_ANON = "NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalanceExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger"

MULTIPLICITY_CAP_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
FIBER_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCap"
)
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOr"
    f"{MULTIPLICITY_CAP_TARGET}Or{FIBER_TARGET}"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BRIDGE} "
    f"AND {AMPLITUDE_DEPTH} AND {BOUNDARY} AND {FIBER_MODEL} "
    f"AND {FIBER_QUOTA_DEBT} AND {OVERFULL_FIBER} "
    f"AND {MULTIPLICITY_CAP_PACKET} AND {RETURN_SPLIT} AND {FIBER_PACKET} "
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


def source_hashes() -> dict[str, str]:
    """登记本脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把活动基中的 source-atom 硬点替换为 multiplicity-fiber 硬点。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 multiplicity-fiber 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalanceImported",
            imported,
            False,
            "上一层剩余含 phase-word-slot source-atom imbalance 或 sparse/atom/mean/三出口。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiber",
            True,
            False,
            "multiplicity fiber 退化成真实孤立点时继续由 singleton atom/SAE 承接。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiber",
            True,
            False,
            "fiber 只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiber",
            True,
            False,
            "fiber 内抵消债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiber",
            True,
            False,
            "同号 fiber 跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiber",
            True,
            False,
            "fiber 穿越 slot 或 phase 边界时继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberModel",
            True,
            True,
            "把 overfull source atom 的 C_{s,rho,omega,tau,alpha} 按有限实际 multiplicity fibers mu 分解。",
            FIBER_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberQuotaDebtAllocation",
            True,
            True,
            "把 d_{s,rho,omega,tau,alpha} 同步分配为 d_{s,rho,omega,tau,alpha,mu}。",
            FIBER_QUOTA_DEBT,
        ),
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberPigeonhole",
            True,
            True,
            "若 source atom 超额且不由 multiplicity cap 出口支付，则存在 mu 使 C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}。",
            OVERFULL_FIBER,
        ),
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPacket",
            True,
            False,
            "若同一 source atom 的实际出现重数超过局部 cap，直接登记为 source-atom multiplicity-cap PDEC/cap。",
            MULTIPLICITY_CAP_PACKET,
        ),
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberNamedReturnSplit",
            True,
            True,
            "overfull multiplicity fiber 的孤立、均值、反号债、堆高、边界迁移分别回流已有出口。",
            RETURN_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePacket",
            True,
            False,
            "若已有出口不支付，剩余就是真实 source-atom multiplicity-fiber imbalance PDEC/cap。",
            FIBER_PACKET,
        ),
        row(
            "NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalanceExit",
            True,
            True,
            "source-atom imbalance 不再匿名保留；它是 multiplicity-cap、multiplicity-fiber imbalance 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiber",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、multiplicity-fiber imbalance、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、multiplicity cap、multiplicity-fiber imbalance、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 multiplicity-fiber 证书。"""
    previous = load_json(PREVIOUS_CERT)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "source-atom imbalance 给出 C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha}。"
        "把同一 source atom 内的实际出现按 multiplicity fiber mu 分解；若出现重数本身超过局部 cap，"
        "它直接成为 source-atom multiplicity-cap PDEC/cap。否则把负载和 quota/debt 同步分配到有限 fibers。"
        "若所有 fibers 都不超额，则加总回到 source atom 不超额，矛盾；因此至少一个实际 multiplicity fiber 超额。"
        "已有出口能支付则回流；真正剩余是 source-atom multiplicity-fiber imbalance。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_router",
        "status": "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_reduced_to_multiplicity_fiber_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_model_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_quota_debt_allocation_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_pigeonhole_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_packet_registered": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_named_return_split_closed": True,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_packet_registered": True,
        "anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "source_atom_multiplicity_fiber_formulas": {
            "source_atom_load": "C_{s,rho,omega,tau,alpha}=sum_mu C_{s,rho,omega,tau,alpha,mu}",
            "quota_debt_source_atom": "d_{s,rho,omega,tau,alpha}=sum_mu d_{s,rho,omega,tau,alpha,mu}",
            "multiplicity_cap_branch": "mult(alpha)>M_cap => SourceAtomMultiplicityCapPDECCap",
            "overfull_fiber": "C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha} => exists mu with C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}, unless the multiplicity-cap branch is active",
            "new_exit": "ResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCap",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous),
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_imported={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_imported'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_model_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_model_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_quota_debt_allocation_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_quota_debt_allocation_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_pigeonhole_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_pigeonhole_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_packet_registered={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_packet_registered'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_named_return_split_closed={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_named_return_split_closed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_packet_registered={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_packet_registered'])}",
        f"anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_removed={fmt_bool(cert['anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_removed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. multiplicity-fiber 分解",
        "",
        "把已超额的 source atom `(s,rho,omega,tau,alpha)` 同步分解到有限实际 multiplicity fiber `mu`：",
        "",
        "```text",
        "C_{s,rho,omega,tau,alpha}=sum_mu C_{s,rho,omega,tau,alpha,mu}",
        "d_{s,rho,omega,tau,alpha}=sum_mu d_{s,rho,omega,tau,alpha,mu}",
        "mult(alpha)>M_cap => SourceAtomMultiplicityCapPDECCap",
        "C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha} => exists mu with C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}, unless the multiplicity-cap branch is active.",
        "```",
        "",
        "因此 source-atom 超额不能匿名停留，必须落到重数 cap 异常、一个实际 multiplicity fiber，或回流已有出口。",
        "",
        "## 2. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend([
        "",
        "## 4. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 5. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 source-atom multiplicity-fiber imbalance PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for file_name, digest in cert["source_hashes"].items():
        lines.append(f"| `{file_name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 ledger、JSON 证书和 Markdown 说明。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
        "outputs": [str(OUT_LEDGER.relative_to(ROOT)), str(OUT_JSON.relative_to(ROOT)), str(OUT_MD.relative_to(ROOT))],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
