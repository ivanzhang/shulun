#!/usr/bin/env python3
"""生成 canonical-equation phase-residue-evaluation 归约证书。

用法示例：
  python3 experiments/prime_matrix_canonical_equation_phase_residue_evaluation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.json

输出：
  data/prime-matrix-canonical-equation-phase-residue-evaluation-ledger.json
  docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.json
  docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-canonical-equation-phase-residue-evaluation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-crt-coordinate-canonical-equation-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAE"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitCanonicalCongruenceEquationAtomImbalanceImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterPhaseResidueEvaluationAtomLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPhaseResidueEvaluationAtomLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPhaseResidueEvaluationAtomLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterPhaseResidueEvaluationAtomLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPhaseResidueEvaluationAtomLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPhaseResidueEvaluationAtomLedger"
PHASE_MODEL = "StableLadderEndpointOrbitCanonicalCongruenceEquationPhaseResidueEvaluationAtomModelLedger"
ROW_PHASE = "StableLadderEndpointOrbitCanonicalCongruenceEquationRowPhaseLedger"
COLUMN_PHASE = "StableLadderEndpointOrbitCanonicalCongruenceEquationColumnPhaseLedger"
CARRIER_RESIDUE = "StableLadderEndpointOrbitCanonicalCongruenceEquationCarrierResidueEvaluationLedger"
EVALUATION_ID = "StableLadderEndpointOrbitCanonicalCongruenceEquationPhaseResidueEvaluationIDStabilityLedger"
QUOTA_DEBT = "StableLadderEndpointOrbitCanonicalCongruenceEquationPhaseResidueEvaluationQuotaDebtAllocationLedger"
PIGEONHOLE = "StableLadderEndpointOrbitCanonicalCongruenceEquationPhaseResidueEvaluationAtomPigeonholeLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitCanonicalCongruenceEquationPhaseResidueEvaluationAtomNamedReturnSplitLedger"
PHASE_PACKET = "StableLadderEndpointOrbitCanonicalCongruenceEquationPhaseResidueEvaluationAtomImbalancePacketLedger"
NO_ANON = "NoAnonymousCanonicalCongruenceEquationAtomImbalanceAfterPhaseResidueEvaluationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPhaseResidueEvaluationAtomLedger"

MULTIPLICITY_CAP_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
PHASE_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomImbalancePDECCap"
)
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOr"
    f"{MULTIPLICITY_CAP_TARGET}Or{PHASE_TARGET}"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {MULTIPLICITY_CAP} AND {SINGLETON} AND {FULL_MEAN} "
    f"AND {BRIDGE} AND {AMPLITUDE_DEPTH} AND {BOUNDARY} "
    f"AND {PHASE_MODEL} AND {ROW_PHASE} AND {COLUMN_PHASE} "
    f"AND {CARRIER_RESIDUE} AND {EVALUATION_ID} AND {QUOTA_DEBT} "
    f"AND {PIGEONHOLE} AND {RETURN_SPLIT} AND {PHASE_PACKET} "
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
    """把活动基中的 canonical-equation 硬点替换为 phase-residue-evaluation 硬点。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def evaluation_records() -> list[dict[str, str]]:
    """给出相位残基评价原子的字段。"""
    return [
        {
            "field": "row_phase",
            "meaning": "r_row=row mod q；固定行在载体素数 q 的 CRT 相位。",
        },
        {
            "field": "column_phase",
            "meaning": "r_col=column mod q；固定列在载体素数 q 的 CRT 相位。",
        },
        {
            "field": "evaluated_residue",
            "meaning": "v=N_{row,column,side} mod q；必须与 canonical residue a 同步比较。",
        },
        {
            "field": "evaluation_id",
            "meaning": "H(equation_id,q,a,r_row,r_col,v,side,orientation,phase_boundary_key)。",
        },
        {
            "field": "phase_boundary_key",
            "meaning": "若相位跨边界迁移，必须回流 variation-boundary flux 出口。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 phase-residue-evaluation 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "CanonicalCongruenceEquationAtomImbalanceImported",
            imported,
            False,
            "上一层剩余含 multiplicity cap、canonical-equation atom imbalance 或 sparse/atom/mean/三出口。",
            PREVIOUS_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "source-atom multiplicity-cap 异常继续作为独立 PDEC/cap 出口；本步不证明该 cap。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "相位残基评价原子退化为单点孤立端点时继续由 singleton atom/SAE 承接。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "相位残基评价只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "同一相位评价原子内反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "同号相位评价原子跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "相位评价穿越行列、端点侧、phase 或 residue 边界时继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "CanonicalCongruenceEquationPhaseResidueEvaluationAtomModel",
            True,
            True,
            "把 overfull canonical equation atom 的 C_{...,epsilon} 按有限 phase-residue evaluation atoms zeta 分解。",
            PHASE_MODEL,
        ),
        row(
            "CanonicalCongruenceEquationRowPhase",
            True,
            True,
            "固定 r_row=row mod q，不允许跨行相位支付。",
            ROW_PHASE,
        ),
        row(
            "CanonicalCongruenceEquationColumnPhase",
            True,
            True,
            "固定 r_col=column mod q，不允许跨列相位支付。",
            COLUMN_PHASE,
        ),
        row(
            "CanonicalCongruenceEquationCarrierResidueEvaluation",
            True,
            True,
            "同步固定 evaluated residue v=N_{row,column,side} mod q 与目标 residue a。",
            CARRIER_RESIDUE,
        ),
        row(
            "CanonicalCongruenceEquationPhaseResidueEvaluationIDStability",
            True,
            True,
            "evaluation_id 由 equation_id、q、a、row/column phase、v、side、orientation 与 boundary key 稳定决定。",
            EVALUATION_ID,
        ),
        row(
            "CanonicalCongruenceEquationPhaseResidueEvaluationQuotaDebtAllocation",
            True,
            True,
            "把 d_{...,epsilon} 同步分配为 d_{...,epsilon,zeta}，不允许跨 evaluation_id 支付。",
            QUOTA_DEBT,
        ),
        row(
            "CanonicalCongruenceEquationPhaseResidueEvaluationAtomPigeonhole",
            True,
            True,
            "若 canonical equation atom 超额，则存在 zeta 使 C_{...,epsilon,zeta}>d_{...,epsilon,zeta}。",
            PIGEONHOLE,
        ),
        row(
            "CanonicalCongruenceEquationPhaseResidueEvaluationAtomNamedReturnSplit",
            True,
            True,
            "overfull phase-residue atom 的孤立、均值、反号债、堆高、边界迁移分别回流已有出口。",
            RETURN_SPLIT,
        ),
        row(
            "CanonicalCongruenceEquationPhaseResidueEvaluationAtomImbalancePacket",
            True,
            False,
            "若已有出口不支付，剩余就是真实 phase-residue-evaluation atom imbalance PDEC/cap。",
            PHASE_PACKET,
        ),
        row(
            "NoAnonymousCanonicalCongruenceEquationAtomImbalanceAfterPhaseResidueEvaluation",
            True,
            True,
            "canonical equation atom imbalance 不再匿名保留；它是 phase-residue evaluation imbalance 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPhaseResidueEvaluationAtom",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueEvaluationAtomStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、phase-residue imbalance、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、multiplicity cap、phase-residue imbalance、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 phase-residue-evaluation 证书。"""
    previous = load_json(PREVIOUS_CERT)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "canonical-congruence-equation atom imbalance 给出 C_{...,epsilon}>d_{...,epsilon}。"
        "把 epsilon 内部的实际 CRT 相位评价固定为 zeta=(row mod q,column mod q,N(row,column,side) mod q, residue a, side, orientation)。"
        "若所有 zeta 都不超额，则加总回到 epsilon 不超额，矛盾；因此至少一个实际 phase-residue evaluation atom 超额。"
        "multiplicity-cap 异常继续作为独立出口；已有出口能支付则回流；真正剩余是 phase-residue-evaluation atom imbalance。"
    )
    return {
        "certificate_type": "prime_matrix_canonical_equation_phase_residue_evaluation_router",
        "status": "canonical_congruence_equation_atom_reduced_to_phase_residue_evaluation_atom_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "canonical_congruence_equation_atom_imbalance_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "canonical_equation_phase_residue_evaluation_atom_model_closed": True,
        "canonical_equation_row_phase_closed": True,
        "canonical_equation_column_phase_closed": True,
        "canonical_equation_carrier_residue_evaluation_closed": True,
        "canonical_equation_phase_residue_evaluation_id_stability_closed": True,
        "canonical_equation_phase_residue_evaluation_quota_debt_allocation_closed": True,
        "canonical_equation_phase_residue_evaluation_atom_pigeonhole_closed": True,
        "canonical_equation_phase_residue_evaluation_atom_named_return_split_closed": True,
        "canonical_equation_phase_residue_evaluation_atom_imbalance_packet_registered": True,
        "anonymous_canonical_congruence_equation_atom_imbalance_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_evaluation_atom_imbalance_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "phase_residue_evaluation_formulas": {
            "canonical_equation_atom_load": "C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}",
            "quota_debt_equation_atom": "d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}",
            "phase_residue_atom_key": "zeta=(evaluation_id,equation_id,q,a,row mod q,column mod q,N_{row,column,side} mod q,endpoint_side,orientation,phase_boundary_key)",
            "overfull_phase_residue_atom": "C_{...,epsilon}>d_{...,epsilon} => exists zeta with C_{...,epsilon,zeta}>d_{...,epsilon,zeta}",
            "new_exit": PHASE_TARGET,
        },
        "phase_residue_evaluation_records": evaluation_records(),
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous),
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix canonical-equation phase-residue-evaluation 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"canonical_congruence_equation_atom_imbalance_imported={fmt_bool(cert['canonical_congruence_equation_atom_imbalance_imported'])}",
        f"source_atom_multiplicity_cap_carried_forward={fmt_bool(cert['source_atom_multiplicity_cap_carried_forward'])}",
        f"canonical_equation_phase_residue_evaluation_atom_model_closed={fmt_bool(cert['canonical_equation_phase_residue_evaluation_atom_model_closed'])}",
        f"canonical_equation_row_phase_closed={fmt_bool(cert['canonical_equation_row_phase_closed'])}",
        f"canonical_equation_column_phase_closed={fmt_bool(cert['canonical_equation_column_phase_closed'])}",
        f"canonical_equation_carrier_residue_evaluation_closed={fmt_bool(cert['canonical_equation_carrier_residue_evaluation_closed'])}",
        f"canonical_equation_phase_residue_evaluation_id_stability_closed={fmt_bool(cert['canonical_equation_phase_residue_evaluation_id_stability_closed'])}",
        f"canonical_equation_phase_residue_evaluation_quota_debt_allocation_closed={fmt_bool(cert['canonical_equation_phase_residue_evaluation_quota_debt_allocation_closed'])}",
        f"canonical_equation_phase_residue_evaluation_atom_pigeonhole_closed={fmt_bool(cert['canonical_equation_phase_residue_evaluation_atom_pigeonhole_closed'])}",
        f"canonical_equation_phase_residue_evaluation_atom_imbalance_packet_registered={fmt_bool(cert['canonical_equation_phase_residue_evaluation_atom_imbalance_packet_registered'])}",
        f"anonymous_canonical_congruence_equation_atom_imbalance_removed={fmt_bool(cert['anonymous_canonical_congruence_equation_atom_imbalance_removed'])}",
        f"phase_residue_evaluation_atom_imbalance_pdec_cap_proved={fmt_bool(cert['phase_residue_evaluation_atom_imbalance_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 相位残基评价原子分解",
        "",
        "把已超额的 canonical congruence equation atom `epsilon` 同步分解到有限相位残基评价原子 `zeta`。",
        "`zeta` 固定 `row mod q`、`column mod q`、`N_{row,column,side} mod q`、目标残基 `a`、端点侧、方向和 phase/boundary 标签。",
        "",
        "```text",
        "C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}",
        "d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}",
        "C_{...,epsilon}>d_{...,epsilon} => exists zeta with C_{...,epsilon,zeta}>d_{...,epsilon,zeta}.",
        "```",
        "",
        "因此 canonical equation atom 超额不能靠未显式评价的 CRT 相位匿名保留；它必须落到一个实际 phase-residue evaluation atom，或回流已有出口。",
        "",
        "## 2. 评价字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["phase_residue_evaluation_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend([
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend([
        "",
        "## 5. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 6. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 phase-residue-evaluation atom imbalance PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 7. 依赖哈希",
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
        "outputs": [
            str(OUT_LEDGER.relative_to(ROOT)),
            str(OUT_JSON.relative_to(ROOT)),
            str(OUT_MD.relative_to(ROOT)),
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
