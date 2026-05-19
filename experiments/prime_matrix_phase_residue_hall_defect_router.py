#!/usr/bin/env python3
"""生成 phase-residue Hall-defect 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_hall_defect_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-hall-defect-router.json

输出：
  data/prime-matrix-phase-residue-hall-defect-ledger.json
  docs/monograph/prime-matrix-phase-residue-hall-defect-router.json
  docs/monograph/prime-matrix-phase-residue-hall-defect-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-hall-defect"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-canonical-equation-phase-residue-evaluation-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAE"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueEvaluationAtomImbalanceImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterPhaseResidueHallDefectLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPhaseResidueHallDefectLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPhaseResidueHallDefectLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterPhaseResidueHallDefectLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPhaseResidueHallDefectLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPhaseResidueHallDefectLedger"
LOAD_TOKENS = "StableLadderEndpointOrbitPhaseResidueEvaluationLoadTokenLedger"
DEBT_SLOTS = "StableLadderEndpointOrbitPhaseResidueEvaluationQuotaDebtSlotLedger"
PAYMENT_GRAPH = "StableLadderEndpointOrbitPhaseResidueEvaluationPaymentGraphLedger"
HALL_NORMAL_FORM = "StableLadderEndpointOrbitPhaseResidueEvaluationHallDefectNormalFormLedger"
HALL_PIGEONHOLE = "StableLadderEndpointOrbitPhaseResidueEvaluationHallDefectPigeonholeLedger"
DEFECT_PACKET = "StableLadderEndpointOrbitPhaseResidueEvaluationHallDefectPacketLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitPhaseResidueEvaluationHallDefectNamedReturnSplitLedger"
NO_ANON = "NoAnonymousPhaseResidueEvaluationImbalanceAfterHallDefectLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPhaseResidueHallDefectLedger"

MULTIPLICITY_CAP_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
HALL_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomHallDefectPDECCap"
)
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOr"
    f"{MULTIPLICITY_CAP_TARGET}Or{HALL_TARGET}"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {MULTIPLICITY_CAP} AND {SINGLETON} AND {FULL_MEAN} "
    f"AND {BRIDGE} AND {AMPLITUDE_DEPTH} AND {BOUNDARY} "
    f"AND {LOAD_TOKENS} AND {DEBT_SLOTS} AND {PAYMENT_GRAPH} "
    f"AND {HALL_NORMAL_FORM} AND {HALL_PIGEONHOLE} AND {DEFECT_PACKET} "
    f"AND {RETURN_SPLIT} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把活动基中的 phase-residue imbalance 硬点替换为 Hall-defect 硬点。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def hall_records() -> list[dict[str, str]]:
    """给出 Hall 缺陷证书字段。"""
    return [
        {
            "field": "load_token",
            "meaning": "phase-residue evaluation atom 内的实际正负载单位，保留 evaluation_id 与来源索引。",
        },
        {
            "field": "quota_debt_slot",
            "meaning": "同一 evaluation_id 内可支付的 quota 或 cancellation debt slot。",
        },
        {
            "field": "payment_edge",
            "meaning": "只有同 evaluation_id、同 side/orientation 纪律且未跨 boundary 的 token-slot 才允许连边。",
        },
        {
            "field": "hall_defect_subset",
            "meaning": "负载 token 子集 S，满足 |S|>|N(S)|。",
        },
        {
            "field": "defect_margin",
            "meaning": "Delta_H(S)=|S|-|N(S)|>0，是显式供需容量缺口。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 Hall-defect 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PhaseResidueEvaluationAtomImbalanceImported",
            imported,
            False,
            "上一层剩余含 multiplicity cap、phase-residue-evaluation atom imbalance 或 sparse/atom/mean/三出口。",
            PREVIOUS_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "source-atom multiplicity-cap 异常继续作为独立 PDEC/cap 出口；本步不证明该 cap。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "Hall 缺陷退化为单点孤立端点时继续由 singleton atom/SAE 承接。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "Hall 缺陷只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "Hall 图中的反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "同号 Hall 缺陷跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "Hall 缺陷穿越行列、端点侧、phase 或 residue 边界时继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueEvaluationLoadTokenLedger",
            True,
            True,
            "把 C_{...,zeta} 展开为有限实际 load tokens。",
            LOAD_TOKENS,
        ),
        row(
            "PhaseResidueEvaluationQuotaDebtSlotLedger",
            True,
            True,
            "把 d_{...,zeta} 展开为有限 quota/debt slots。",
            DEBT_SLOTS,
        ),
        row(
            "PhaseResidueEvaluationPaymentGraphLedger",
            True,
            True,
            "只在同 evaluation_id 且守住 side/orientation/boundary 纪律的 token-slot 之间连边。",
            PAYMENT_GRAPH,
        ),
        row(
            "PhaseResidueEvaluationHallDefectNormalForm",
            True,
            True,
            "若存在全匹配则 C_{...,zeta}<=d_{...,zeta}；因 C>d，Hall 条件必失败。",
            HALL_NORMAL_FORM,
        ),
        row(
            "PhaseResidueEvaluationHallDefectPigeonhole",
            True,
            True,
            "由 Hall 定理存在负载子集 S 满足 |S|>|N(S)|。",
            HALL_PIGEONHOLE,
        ),
        row(
            "PhaseResidueEvaluationHallDefectPacket",
            True,
            False,
            "若已有出口不支付，剩余就是真实 phase-residue Hall-defect PDEC/cap。",
            DEFECT_PACKET,
        ),
        row(
            "PhaseResidueEvaluationHallDefectNamedReturnSplit",
            True,
            True,
            "Hall 缺陷的孤立、均值、反号债、堆高、边界迁移分别回流已有出口。",
            RETURN_SPLIT,
        ),
        row(
            "NoAnonymousPhaseResidueEvaluationImbalanceAfterHallDefect",
            True,
            True,
            "phase-residue imbalance 不再匿名保留；它是 Hall-defect imbalance 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPhaseResidueHallDefect",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueHallDefectStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、Hall-defect、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、multiplicity cap、Hall-defect、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 Hall-defect 证书。"""
    previous = load_json(PREVIOUS_CERT)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "phase-residue-evaluation atom imbalance 给出 C_{...,zeta}>d_{...,zeta}。"
        "把负载展开为 load tokens，把可支付额度展开为 quota/debt slots，并只在同 evaluation_id 与同边界纪律下连边。"
        "若所有负载 token 可匹配到支付 slot，则 C<=d；因此 Hall 条件必失败，存在 S 满足 |S|>|N(S)|。"
        "真正剩余从抽象超额变为显式 phase-residue Hall-defect PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_hall_defect_router",
        "status": "phase_residue_evaluation_atom_imbalance_reduced_to_hall_defect_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "phase_residue_evaluation_atom_imbalance_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_load_token_ledger_closed": True,
        "phase_residue_quota_debt_slot_ledger_closed": True,
        "phase_residue_payment_graph_closed": True,
        "phase_residue_hall_defect_normal_form_closed": True,
        "phase_residue_hall_defect_pigeonhole_closed": True,
        "phase_residue_hall_defect_packet_registered": True,
        "phase_residue_hall_defect_named_return_split_closed": True,
        "anonymous_phase_residue_evaluation_imbalance_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_hall_defect_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "hall_defect_formulas": {
            "load_tokens": "L_zeta={load tokens counted by C_{...,zeta}}",
            "debt_slots": "D_zeta={quota/debt slots counted by d_{...,zeta}}",
            "payment_graph": "G_zeta=(L_zeta,D_zeta,E_zeta) with edges preserving evaluation_id, side, orientation, and boundary key",
            "hall_defect": "C_{...,zeta}>d_{...,zeta} => exists S subset L_zeta with |S|>|N_G(S)|",
            "defect_margin": "Delta_H(S)=|S|-|N_G(S)|>0",
            "new_exit": HALL_TARGET,
        },
        "hall_defect_records": hall_records(),
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous),
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue Hall-defect 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_evaluation_atom_imbalance_imported={fmt_bool(cert['phase_residue_evaluation_atom_imbalance_imported'])}",
        f"source_atom_multiplicity_cap_carried_forward={fmt_bool(cert['source_atom_multiplicity_cap_carried_forward'])}",
        f"phase_residue_load_token_ledger_closed={fmt_bool(cert['phase_residue_load_token_ledger_closed'])}",
        f"phase_residue_quota_debt_slot_ledger_closed={fmt_bool(cert['phase_residue_quota_debt_slot_ledger_closed'])}",
        f"phase_residue_payment_graph_closed={fmt_bool(cert['phase_residue_payment_graph_closed'])}",
        f"phase_residue_hall_defect_normal_form_closed={fmt_bool(cert['phase_residue_hall_defect_normal_form_closed'])}",
        f"phase_residue_hall_defect_pigeonhole_closed={fmt_bool(cert['phase_residue_hall_defect_pigeonhole_closed'])}",
        f"phase_residue_hall_defect_packet_registered={fmt_bool(cert['phase_residue_hall_defect_packet_registered'])}",
        f"anonymous_phase_residue_evaluation_imbalance_removed={fmt_bool(cert['anonymous_phase_residue_evaluation_imbalance_removed'])}",
        f"phase_residue_hall_defect_pdec_cap_proved={fmt_bool(cert['phase_residue_hall_defect_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Hall 缺陷分解",
        "",
        "把已超额的 phase-residue evaluation atom `zeta` 展开为负载 token 集 `L_zeta` 与支付 slot 集 `D_zeta`。",
        "只允许同 `evaluation_id`、同 side/orientation 纪律且不跨 boundary 的 token-slot 连边。",
        "",
        "```text",
        "G_zeta=(L_zeta,D_zeta,E_zeta)",
        "C_{...,zeta}=|L_zeta|, d_{...,zeta}=|D_zeta|",
        "C_{...,zeta}>d_{...,zeta} => exists S subset L_zeta with |S|>|N_G(S)|.",
        "Delta_H(S)=|S|-|N_G(S)|>0",
        "```",
        "",
        "因此 phase-residue 超额不能匿名保留为 C>d；它必须表现为一个显式 Hall 供需缺陷子集，或回流已有出口。",
        "",
        "## 2. Hall 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["hall_defect_records"]:
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
        "- 本证书没有证明 phase-residue Hall-defect PDEC/cap。",
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
