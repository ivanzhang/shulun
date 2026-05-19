#!/usr/bin/env python3
"""生成 phase-residue near-perfect matching circuit 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_near_perfect_matching_circuit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.json

输出：
  data/prime-matrix-phase-residue-near-perfect-matching-circuit-ledger.json
  docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.json
  docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-near-perfect-matching-circuit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-unit-defect-critical-cut-router.json"

UNIT_DEFECT_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomUnitDefectCriticalHallCutPDECCap"
)
MATCHING_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomNearPerfectMatchingCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueUnitDefectCriticalHallCutImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterNearPerfectMatchingCircuitLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterNearPerfectMatchingCircuitLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterNearPerfectMatchingCircuitLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterNearPerfectMatchingCircuitLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterNearPerfectMatchingCircuitLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterNearPerfectMatchingCircuitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterNearPerfectMatchingCircuitLedger"
UNIT_MARGIN = "StableLadderEndpointOrbitPhaseResidueUnitDefectMarginImportedLedger"
PROPER_SUBSET = "StableLadderEndpointOrbitPhaseResidueCriticalCutProperSubsetHallImportedForMatchingLedger"
DELETION_SATURATION = "StableLadderEndpointOrbitPhaseResidueCriticalCutDeletionBoundarySaturationImportedForMatchingLedger"
DELETION_HALL = "StableLadderEndpointOrbitPhaseResidueEverySingleDeletionHallOKLedger"
DELETION_MATCHING = "StableLadderEndpointOrbitPhaseResidueEverySingleDeletionPerfectMatchingLedger"
MAX_MATCHING = "StableLadderEndpointOrbitPhaseResidueCriticalCutMaximumMatchingSizeLedger"
ALL_SOURCE_OMITTABLE = "StableLadderEndpointOrbitPhaseResidueEverySourceCanBeUnmatchedLedger"
BOUNDARY_DOUBLE_COVER = "StableLadderEndpointOrbitPhaseResidueBoundaryDoubleCoverLedger"
MATCHING_CIRCUIT = "StableLadderEndpointOrbitPhaseResidueNearPerfectMatchingCircuitPacketLedger"
NO_ANON = "NoAnonymousUnitDefectCriticalHallCutAfterMatchingCircuitLedger"


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


def next_target(previous: dict[str, Any]) -> str:
    """把 unit-defect critical cut 硬点替换为 near-perfect matching circuit 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and UNIT_DEFECT_TARGET in target:
        return target.replace(UNIT_DEFECT_TARGET, MATCHING_TARGET)
    return MATCHING_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        UNIT_MARGIN,
        PROPER_SUBSET,
        DELETION_SATURATION,
        DELETION_HALL,
        DELETION_MATCHING,
        MAX_MATCHING,
        ALL_SOURCE_OMITTABLE,
        BOUNDARY_DOUBLE_COVER,
        MATCHING_CIRCUIT,
        NO_ANON,
        SPARSE,
        new_target,
    ]
    return " AND ".join(ledgers)


def replace_latest_basis(previous: dict[str, Any], reduced: str) -> str:
    """更新长活动基。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    old = previous.get("next_direct_attack_target", "")
    if basis and old and old in basis:
        return basis.replace(old, reduced)
    return reduced


def matching_records() -> list[dict[str, str]]:
    """给出 near-perfect matching circuit 的字段。"""
    return [
        {
            "field": "unit_defect",
            "meaning": "上一层已给出 |S_*|=|B_*|+1。",
        },
        {
            "field": "single_deletion_hall",
            "meaning": "对任意 s in S_*，任意 U subset S_*\\{s} 仍是真子集，故 |U|<=|N(U)|。",
        },
        {
            "field": "perfect_matching_after_deletion",
            "meaning": "由 Hall 定理，G[S_*\\{s},B_*] 存在完美匹配。",
        },
        {
            "field": "all_source_omittable",
            "meaning": "每个源点 s 都可作为唯一未匹配源点；未支付源点不再匿名。",
        },
        {
            "field": "boundary_double_cover",
            "meaning": "删除任一源点仍能匹配全部 B_*，所以每个边界槽至少由两个源点支撑。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 near-perfect matching circuit 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = UNIT_DEFECT_TARGET in old_target
    return [
        row(
            "PhaseResidueUnitDefectCriticalHallCutImported",
            imported,
            False,
            "上一层剩余含 phase-residue unit-defect critical-Hall-cut PDEC/cap 或 parallel outlets。",
            old_target or UNIT_DEFECT_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "匹配 circuit 退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueUnitDefectMarginImported",
            True,
            True,
            "导入 |S_*|=|B_*|+1 的单位缺口。",
            UNIT_MARGIN,
        ),
        row(
            "PhaseResidueCriticalCutProperSubsetHallImportedForMatching",
            True,
            True,
            "导入所有真子集 Hall 正常性。",
            PROPER_SUBSET,
        ),
        row(
            "PhaseResidueCriticalCutDeletionBoundarySaturationImportedForMatching",
            True,
            True,
            "导入 N(S_*\\{s})=B_* 的删除边界饱和。",
            DELETION_SATURATION,
        ),
        row(
            "PhaseResidueEverySingleDeletionHallOK",
            True,
            True,
            "对任意 s，S_*\\{s} 的每个子集仍满足 Hall。",
            DELETION_HALL,
        ),
        row(
            "PhaseResidueEverySingleDeletionPerfectMatching",
            True,
            True,
            "由 Hall 定理，S_*\\{s} 可完美匹配到 B_*。",
            DELETION_MATCHING,
        ),
        row(
            "PhaseResidueCriticalCutMaximumMatchingSize",
            True,
            True,
            "最大匹配大小为 |B_*|=|S_*|-1，整体只缺一个源点。",
            MAX_MATCHING,
        ),
        row(
            "PhaseResidueEverySourceCanBeUnmatched",
            True,
            True,
            "每个源点都可在某个完美删除匹配中作为唯一未匹配点。",
            ALL_SOURCE_OMITTABLE,
        ),
        row(
            "PhaseResidueBoundaryDoubleCover",
            True,
            True,
            "每个边界槽至少有两个源点邻接，否则删除唯一邻接源点会丢失该槽。",
            BOUNDARY_DOUBLE_COVER,
        ),
        row(
            "PhaseResidueNearPerfectMatchingCircuitPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 near-perfect matching circuit PDEC/cap。",
            MATCHING_CIRCUIT,
        ),
        row(
            "NoAnonymousUnitDefectCriticalHallCutAfterMatchingCircuit",
            True,
            True,
            "unit-defect cut 不再匿名保留；它是近完美匹配 circuit 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterNearPerfectMatchingCircuit",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueNearPerfectMatchingCircuitStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、near-perfect matching circuit、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 near-perfect matching circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 near-perfect matching circuit 证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    old_target = previous.get("next_direct_attack_target", "")
    imported = UNIT_DEFECT_TARGET in old_target
    plain = (
        "phase-residue unit-defect critical cut 已有 |S_*|=|B_*|+1，且所有真子集 Hall 正常。"
        "任取 s in S_*，对任意 U subset S_*\\{s}，U 都是真子集，所以 |U|<=|N(U)|；"
        "又上一层给出 N(S_*\\{s})=B_*，故 |S_*\\{s}|=|B_*|。"
        "由 Hall 定理，G[S_*\\{s},B_*] 存在完美匹配。"
        "因此删除任意源点后全部边界可支付，整体最大匹配只差一个源点；剩余从单位缺口 cut 压成 near-perfect matching circuit PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_near_perfect_matching_circuit_router",
        "status": "phase_residue_unit_defect_critical_cut_reduced_to_near_perfect_matching_circuit_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": old_target or UNIT_DEFECT_TARGET,
        "hardpoint_after_router": reduced,
        "phase_residue_unit_defect_critical_hall_cut_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_unit_defect_margin_imported": True,
        "phase_residue_critical_cut_proper_subset_hall_imported_for_matching": True,
        "phase_residue_critical_cut_deletion_boundary_saturation_imported_for_matching": True,
        "phase_residue_every_single_deletion_hall_ok_closed": True,
        "phase_residue_every_single_deletion_perfect_matching_closed": True,
        "phase_residue_critical_cut_maximum_matching_size_closed": True,
        "phase_residue_every_source_can_be_unmatched_closed": True,
        "phase_residue_boundary_double_cover_closed": True,
        "phase_residue_near_perfect_matching_circuit_packet_registered": True,
        "anonymous_unit_defect_critical_hall_cut_removed_after_matching_circuit": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_near_perfect_matching_circuit_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "matching_circuit_formulas": {
            "unit_defect": "|S_*|=|B_*|+1",
            "single_deletion_hall": "for every s in S_* and U subset S_*\\{s}, |U|<=|N_G(U)|",
            "single_deletion_boundary": "N_G(S_*\\{s})=B_*",
            "perfect_matching": "for every s in S_*, there exists a perfect matching M_s:S_*\\{s}->B_*",
            "maximum_matching_size": "nu(G[S_*,B_*])=|B_*|=|S_*|-1",
            "new_exit": MATCHING_TARGET,
        },
        "matching_circuit_records": matching_records(),
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "decision_rows": build_rows(previous, new_target),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue near-perfect matching circuit 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_unit_defect_critical_hall_cut_imported={fmt_bool(cert['phase_residue_unit_defect_critical_hall_cut_imported'])}",
        f"phase_residue_every_single_deletion_hall_ok_closed={fmt_bool(cert['phase_residue_every_single_deletion_hall_ok_closed'])}",
        f"phase_residue_every_single_deletion_perfect_matching_closed={fmt_bool(cert['phase_residue_every_single_deletion_perfect_matching_closed'])}",
        f"phase_residue_critical_cut_maximum_matching_size_closed={fmt_bool(cert['phase_residue_critical_cut_maximum_matching_size_closed'])}",
        f"phase_residue_boundary_double_cover_closed={fmt_bool(cert['phase_residue_boundary_double_cover_closed'])}",
        f"phase_residue_near_perfect_matching_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_near_perfect_matching_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 删除完美匹配",
        "",
        "上一层给出 `|S_*|=|B_*|+1`、`N_G(S_*\\{s})=B_*`，且所有真子集 Hall 正常。",
        "任取 `s in S_*`。对任意 `U subset S_*\\{s}`，`U` 都是 `S_*` 的真子集，因此：",
        "",
        "```text",
        "|U| <= |N_G(U)|",
        "```",
        "",
        "并且 `|S_*\\{s}|=|B_*|`。由 Hall 定理：",
        "",
        "```text",
        "for every s in S_*: exists perfect matching M_s:S_*\\{s}->B_*",
        "```",
        "",
        "所以整体最大匹配大小为 `|B_*|=|S_*|-1`，每个源点都可成为唯一未匹配源点。",
        "",
        "## 2. 边界二重覆盖",
        "",
        "若某个边界槽 `b in B_*` 只邻接唯一源点 `s`，则删除 `s` 后 `b` 不在 `N_G(S_*\\{s})` 中，矛盾。",
        "因此每个边界槽至少由两个源点支撑；剩余反例不能是单边界孤立支付失败。",
        "",
        "## 3. matching circuit 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["matching_circuit_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend([
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 5. 判定表",
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
        "## 6. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 7. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 phase-residue near-perfect matching circuit PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 8. 依赖哈希",
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
