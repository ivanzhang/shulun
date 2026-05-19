#!/usr/bin/env python3
"""生成 phase-residue critical-Hall-cut 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_critical_hall_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.json

输出：
  data/prime-matrix-phase-residue-critical-hall-cut-ledger.json
  docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.json
  docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-critical-hall-cut"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-hall-defect-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAE"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomHallDefectPDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueHallDefectImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCriticalHallCutLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCriticalHallCutLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCriticalHallCutLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCriticalHallCutLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCriticalHallCutLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCriticalHallCutLedger"
DEFECT_FAMILY = "StableLadderEndpointOrbitPhaseResidueHallDefectFiniteFamilyLedger"
MINIMAL_CHOICE = "StableLadderEndpointOrbitPhaseResidueHallDefectMinimalChoiceLedger"
CONNECTED_CORE = "StableLadderEndpointOrbitPhaseResidueHallDefectConnectedCoreLedger"
PROPER_SUBSET_OK = "StableLadderEndpointOrbitPhaseResidueHallDefectProperSubsetHallOKLedger"
CUT_BOUNDARY = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutBoundaryLedger"
CUT_MARGIN = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutMarginLedger"
CUT_PACKET = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutPacketLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutNamedReturnSplitLedger"
NO_ANON = "NoAnonymousPhaseResidueHallDefectAfterCriticalCutLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCriticalHallCutLedger"

MULTIPLICITY_CAP_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
CRITICAL_CUT_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomCriticalHallCutPDECCap"
)
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOr"
    f"{MULTIPLICITY_CAP_TARGET}Or{CRITICAL_CUT_TARGET}"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {MULTIPLICITY_CAP} AND {SINGLETON} AND {FULL_MEAN} "
    f"AND {BRIDGE} AND {AMPLITUDE_DEPTH} AND {BOUNDARY} "
    f"AND {DEFECT_FAMILY} AND {MINIMAL_CHOICE} AND {CONNECTED_CORE} "
    f"AND {PROPER_SUBSET_OK} AND {CUT_BOUNDARY} AND {CUT_MARGIN} "
    f"AND {CUT_PACKET} AND {RETURN_SPLIT} AND {NO_ANON} "
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
    """把活动基中的 Hall-defect 硬点替换为 critical-Hall-cut 硬点。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def critical_cut_records() -> list[dict[str, str]]:
    """给出 critical Hall cut 证书字段。"""
    return [
        {
            "field": "critical_subset",
            "meaning": "在所有 |S|>|N(S)| 的负载子集中按 size、defect、hash 选择的规范 S_*。",
        },
        {
            "field": "connected_core",
            "meaning": "若缺陷分成多个连通分量，至少一个分量仍有正缺陷；S_* 取该分量。",
        },
        {
            "field": "proper_subset_hall_ok",
            "meaning": "S_* 的真子集均不再违反 Hall；否则会更小。",
        },
        {
            "field": "cut_boundary",
            "meaning": "B_*=N(S_*) 是该临界缺陷的全部可支付边界。",
        },
        {
            "field": "critical_margin",
            "meaning": "Delta_*(S_*)=|S_*|-|B_*|>0，是不可再分的容量缺口。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 critical-Hall-cut 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PhaseResidueHallDefectImported",
            imported,
            False,
            "上一层剩余含 multiplicity cap、phase-residue Hall-defect 或 sparse/atom/mean/三出口。",
            PREVIOUS_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterCriticalHallCut",
            True,
            False,
            "source-atom multiplicity-cap 异常继续作为独立 PDEC/cap 出口；本步不证明该 cap。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterCriticalHallCut",
            True,
            False,
            "critical cut 退化为单点孤立端点时继续由 singleton atom/SAE 承接。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterCriticalHallCut",
            True,
            False,
            "critical cut 只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterCriticalHallCut",
            True,
            False,
            "critical cut 中的反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterCriticalHallCut",
            True,
            False,
            "同号 critical cut 跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterCriticalHallCut",
            True,
            False,
            "critical cut 穿越行列、端点侧、phase 或 residue 边界时继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueHallDefectFiniteFamily",
            True,
            True,
            "Hall 缺陷子集族有限且非空。",
            DEFECT_FAMILY,
        ),
        row(
            "PhaseResidueHallDefectMinimalChoice",
            True,
            True,
            "按 |S|、-Delta_H(S)、stable hash 选择规范临界子集 S_*。",
            MINIMAL_CHOICE,
        ),
        row(
            "PhaseResidueHallDefectConnectedCore",
            True,
            True,
            "若 S_* 可分解为互不相连分量，则某分量仍有正缺陷，违背最小性；故可取连通 core。",
            CONNECTED_CORE,
        ),
        row(
            "PhaseResidueHallDefectProperSubsetHallOK",
            True,
            True,
            "S_* 的每个真子集 T 满足 |T|<=|N(T)|。",
            PROPER_SUBSET_OK,
        ),
        row(
            "PhaseResidueCriticalHallCutBoundary",
            True,
            True,
            "B_*=N(S_*) 是全部可支付边界；缺口只能位于 S_* 与 B_* 的 cut 上。",
            CUT_BOUNDARY,
        ),
        row(
            "PhaseResidueCriticalHallCutMargin",
            True,
            True,
            "Delta_*=|S_*|-|B_*|>0 是不可再分的显式容量缺口。",
            CUT_MARGIN,
        ),
        row(
            "PhaseResidueCriticalHallCutPacket",
            True,
            False,
            "若已有出口不支付，剩余就是真实 phase-residue critical-Hall-cut PDEC/cap。",
            CUT_PACKET,
        ),
        row(
            "PhaseResidueCriticalHallCutNamedReturnSplit",
            True,
            True,
            "critical cut 的孤立、均值、反号债、堆高、边界迁移分别回流已有出口。",
            RETURN_SPLIT,
        ),
        row(
            "NoAnonymousPhaseResidueHallDefectAfterCriticalCut",
            True,
            True,
            "phase-residue Hall defect 不再匿名保留；它是 critical cut 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterCriticalHallCut",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueCriticalHallCutStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、critical cut、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、multiplicity cap、critical cut、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 critical-Hall-cut 证书。"""
    previous = load_json(PREVIOUS_CERT)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "phase-residue Hall defect 给出一个有限非空缺陷族 {S: |S|>|N(S)|}。"
        "在该族中按大小、缺陷量和稳定哈希选择规范 S_*；若它可分解，则某个连通分量仍缺陷，故可取连通 core。"
        "S_* 的真子集均满足 Hall，剩余缺口被压成 cut boundary B_*=N(S_*) 上的不可再分容量缺口。"
        "真正剩余从任意 Hall defect 变为 phase-residue critical-Hall-cut PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_critical_hall_cut_router",
        "status": "phase_residue_hall_defect_reduced_to_critical_hall_cut_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "phase_residue_hall_defect_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_hall_defect_finite_family_closed": True,
        "phase_residue_hall_defect_minimal_choice_closed": True,
        "phase_residue_hall_defect_connected_core_closed": True,
        "phase_residue_hall_defect_proper_subset_hall_ok_closed": True,
        "phase_residue_critical_hall_cut_boundary_closed": True,
        "phase_residue_critical_hall_cut_margin_closed": True,
        "phase_residue_critical_hall_cut_packet_registered": True,
        "phase_residue_critical_hall_cut_named_return_split_closed": True,
        "anonymous_phase_residue_hall_defect_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_critical_hall_cut_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "critical_cut_formulas": {
            "defect_family": "F={S subset L_zeta: |S|>|N_G(S)|}",
            "canonical_choice": "S_*=argmin_{S in F} (|S|,-Delta_H(S),stable_hash(S))",
            "connected_core": "S_* may be chosen connected in G[S_* union N(S_*)]",
            "proper_subset_hall_ok": "for every proper T subset S_*, |T|<=|N_G(T)|",
            "critical_margin": "Delta_*=|S_*|-|N_G(S_*)|>0",
            "new_exit": CRITICAL_CUT_TARGET,
        },
        "critical_cut_records": critical_cut_records(),
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous),
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue critical-Hall-cut 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_hall_defect_imported={fmt_bool(cert['phase_residue_hall_defect_imported'])}",
        f"source_atom_multiplicity_cap_carried_forward={fmt_bool(cert['source_atom_multiplicity_cap_carried_forward'])}",
        f"phase_residue_hall_defect_finite_family_closed={fmt_bool(cert['phase_residue_hall_defect_finite_family_closed'])}",
        f"phase_residue_hall_defect_minimal_choice_closed={fmt_bool(cert['phase_residue_hall_defect_minimal_choice_closed'])}",
        f"phase_residue_hall_defect_connected_core_closed={fmt_bool(cert['phase_residue_hall_defect_connected_core_closed'])}",
        f"phase_residue_hall_defect_proper_subset_hall_ok_closed={fmt_bool(cert['phase_residue_hall_defect_proper_subset_hall_ok_closed'])}",
        f"phase_residue_critical_hall_cut_boundary_closed={fmt_bool(cert['phase_residue_critical_hall_cut_boundary_closed'])}",
        f"phase_residue_critical_hall_cut_margin_closed={fmt_bool(cert['phase_residue_critical_hall_cut_margin_closed'])}",
        f"phase_residue_critical_hall_cut_packet_registered={fmt_bool(cert['phase_residue_critical_hall_cut_packet_registered'])}",
        f"phase_residue_critical_hall_cut_pdec_cap_proved={fmt_bool(cert['phase_residue_critical_hall_cut_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 临界 Hall 割分解",
        "",
        "从有限非空缺陷族 `F={S subset L_zeta: |S|>|N_G(S)|}` 中选择规范临界子集 `S_*`。",
        "选择规则先最小化 `|S|`，再最大化缺陷量，最后用 stable hash 破平局。",
        "",
        "```text",
        "S_*=argmin_{S in F} (|S|,-Delta_H(S),stable_hash(S))",
        "B_*=N_G(S_*)",
        "Delta_*=|S_*|-|B_*|>0",
        "for every proper T subset S_*: |T|<=|N_G(T)|",
        "```",
        "",
        "因此任意 Hall 缺陷不能匿名保留；它必须落到一个连通、真子集 Hall 正常、边界明确的 critical cut，或回流已有出口。",
        "",
        "## 2. critical cut 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["critical_cut_records"]:
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
        "- 本证书没有证明 phase-residue critical-Hall-cut PDEC/cap。",
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
