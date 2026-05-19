#!/usr/bin/env python3
"""生成 phase-residue unit-defect critical-cut 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_unit_defect_critical_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.json

输出：
  data/prime-matrix-phase-residue-unit-defect-critical-cut-ledger.json
  docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.json
  docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-unit-defect-critical-cut"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-critical-hall-cut-router.json"

CRITICAL_CUT_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomCriticalHallCutPDECCap"
)
UNIT_DEFECT_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomUnitDefectCriticalHallCutPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterUnitDefectCriticalCutLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterUnitDefectCriticalCutLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterUnitDefectCriticalCutLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterUnitDefectCriticalCutLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterUnitDefectCriticalCutLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterUnitDefectCriticalCutLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterUnitDefectCriticalCutLedger"
PROPER_SUBSET = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutProperSubsetHallOKImportedLedger"
SINGLETON_CASE = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutSingletonCaseUnitDefectLedger"
DELETION_BOUND = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutSingleDeletionBoundLedger"
UNIT_MARGIN = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutUnitMarginLedger"
BOUNDARY_SATURATION = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutSingleDeletionBoundarySaturationLedger"
NO_BULK = "NoMultiUnitPhaseResidueCriticalHallCutDefectLedger"
BOUNDARY_REDUNDANCY = "StableLadderEndpointOrbitPhaseResidueCriticalHallCutBoundaryRedundancyLedger"
UNIT_PACKET = "StableLadderEndpointOrbitPhaseResidueUnitDefectCriticalHallCutPacketLedger"
NO_ANON = "NoAnonymousPhaseResidueCriticalHallCutAfterUnitDefectLedger"


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
    """把 critical-Hall-cut 硬点替换为 unit-defect critical-Hall-cut 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and CRITICAL_CUT_TARGET in target:
        return target.replace(CRITICAL_CUT_TARGET, UNIT_DEFECT_TARGET)
    return UNIT_DEFECT_TARGET


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
        PROPER_SUBSET,
        SINGLETON_CASE,
        DELETION_BOUND,
        UNIT_MARGIN,
        BOUNDARY_SATURATION,
        NO_BULK,
        BOUNDARY_REDUNDANCY,
        UNIT_PACKET,
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


def unit_defect_records() -> list[dict[str, str]]:
    """给出 unit-defect critical cut 的刚性字段。"""
    return [
        {
            "field": "proper_subset_hall_ok",
            "meaning": "上一层已给出：每个真子集 T subset S_* 均满足 |T|<=|N(T)|。",
        },
        {
            "field": "unit_margin",
            "meaning": "若 |S_*|=1，则 B_*=empty 且 Delta_*=1；若 |S_*|>=2，单点删除给出 Delta_*<=1，故 Delta_*=1。",
        },
        {
            "field": "single_deletion_saturation",
            "meaning": "对任意 s in S_*，N(S_*\\{s}) subset B_* 且基数相等，所以 N(S_*\\{s})=B_*。",
        },
        {
            "field": "boundary_redundancy",
            "meaning": "任意边界槽 b in B_* 不由单一源点独占；删除任意源点后仍能在剩余源点中看到 b。",
        },
        {
            "field": "no_bulk_defect",
            "meaning": "critical cut 内部不存在 Delta_*>1 的大容量缺口；剩余只能是单位缺口或已有出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 unit-defect critical-cut 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = CRITICAL_CUT_TARGET in old_target
    return [
        row(
            "PhaseResidueCriticalHallCutImported",
            imported,
            False,
            "上一层剩余含 phase-residue critical-Hall-cut PDEC/cap 或 parallel outlets。",
            old_target or CRITICAL_CUT_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "unit defect 退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueCriticalHallCutProperSubsetHallOKImported",
            True,
            True,
            "critical cut 的真子集 Hall 正常性从上一层导入。",
            PROPER_SUBSET,
        ),
        row(
            "PhaseResidueCriticalHallCutSingletonCaseUnitDefect",
            True,
            True,
            "若 |S_*|=1，正缺陷强制 |B_*|=0，故 Delta_*=1。",
            SINGLETON_CASE,
        ),
        row(
            "PhaseResidueCriticalHallCutSingleDeletionBound",
            True,
            True,
            "若 |S_*|>=2，任取 s：|S_*|-1<=|N(S_*\\{s})|<=|B_*|=|S_*|-Delta_*，所以 Delta_*<=1。",
            DELETION_BOUND,
        ),
        row(
            "PhaseResidueCriticalHallCutUnitMargin",
            True,
            True,
            "Delta_*>0 为整数且 Delta_*<=1，因此 Delta_*=1。",
            UNIT_MARGIN,
        ),
        row(
            "PhaseResidueCriticalHallCutSingleDeletionBoundarySaturation",
            True,
            True,
            "由 |N(S_*\\{s})|=|B_*| 且 N(S_*\\{s}) subset B_* 得 N(S_*\\{s})=B_*。",
            BOUNDARY_SATURATION,
        ),
        row(
            "NoMultiUnitPhaseResidueCriticalHallCutDefect",
            True,
            True,
            "critical cut 内部的多单位容量缺陷被排除；不存在 Delta_*>1 的匿名剩余。",
            NO_BULK,
        ),
        row(
            "PhaseResidueCriticalHallCutBoundaryRedundancy",
            True,
            True,
            "每个边界槽在删除任意源点后仍被剩余源点触达，形成强冗余相位边界。",
            BOUNDARY_REDUNDANCY,
        ),
        row(
            "PhaseResidueUnitDefectCriticalHallCutPacket",
            True,
            False,
            "若已有出口不支付，剩余就是单位缺口 critical-Hall-cut PDEC/cap。",
            UNIT_PACKET,
        ),
        row(
            "NoAnonymousPhaseResidueCriticalHallCutAfterUnitDefect",
            True,
            True,
            "critical-Hall-cut 不再可匿名保留；它是单位缺口 cut 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterUnitDefectCriticalCut",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueUnitDefectCriticalHallCutStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、unit-defect critical cut、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 unit-defect critical cut 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 unit-defect critical-cut 证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    old_target = previous.get("next_direct_attack_target", "")
    imported = CRITICAL_CUT_TARGET in old_target
    plain = (
        "phase-residue critical-Hall-cut 已有 S_*、B_*=N(S_*)、Delta_*=|S_*|-|B_*|>0，且每个真子集 Hall 正常。"
        "若 |S_*|=1，则正缺陷只能是 B_*=empty、Delta_*=1。"
        "若 |S_*|>=2，任取 s in S_*，由真子集 Hall 正常得 |S_*|-1<=|N(S_*\\{s})|，"
        "又有 N(S_*\\{s}) subset B_*，所以 |S_*|-1<=|B_*|=|S_*|-Delta_*，从而 Delta_*<=1。"
        "因 Delta_*>0 为整数，必有 Delta_*=1。进一步 N(S_*\\{s})=B_*，"
        "即删除任一源点后可支付边界仍完整存在。剩余从任意 critical cut 压成单位缺口 critical-Hall-cut PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_unit_defect_critical_cut_router",
        "status": "phase_residue_critical_hall_cut_reduced_to_unit_defect_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": old_target or CRITICAL_CUT_TARGET,
        "hardpoint_after_router": reduced,
        "phase_residue_critical_hall_cut_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_critical_hall_cut_proper_subset_hall_ok_imported": True,
        "phase_residue_critical_hall_cut_singleton_case_unit_defect_closed": True,
        "phase_residue_critical_hall_cut_single_deletion_bound_closed": True,
        "phase_residue_critical_hall_cut_unit_margin_closed": True,
        "phase_residue_critical_hall_cut_single_deletion_boundary_saturation_closed": True,
        "multi_unit_phase_residue_critical_hall_cut_defect_excluded": True,
        "phase_residue_critical_hall_cut_boundary_redundancy_closed": True,
        "phase_residue_unit_defect_critical_hall_cut_packet_registered": True,
        "anonymous_phase_residue_critical_hall_cut_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_unit_defect_critical_hall_cut_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "unit_defect_formulas": {
            "critical_cut": "B_*=N_G(S_*), Delta_*=|S_*|-|B_*|>0",
            "proper_subset_hall_ok": "for every proper T subset S_*, |T|<=|N_G(T)|",
            "single_deletion_bound": "|S_*|-1<=|N_G(S_*\\{s})|<=|B_*|=|S_*|-Delta_*",
            "unit_margin": "Delta_*=1",
            "boundary_saturation": "for every s in S_*, N_G(S_*\\{s})=B_*",
            "new_exit": UNIT_DEFECT_TARGET,
        },
        "unit_defect_records": unit_defect_records(),
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "decision_rows": build_rows(previous, new_target),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue unit-defect critical-cut 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_critical_hall_cut_imported={fmt_bool(cert['phase_residue_critical_hall_cut_imported'])}",
        f"phase_residue_critical_hall_cut_proper_subset_hall_ok_imported={fmt_bool(cert['phase_residue_critical_hall_cut_proper_subset_hall_ok_imported'])}",
        f"phase_residue_critical_hall_cut_unit_margin_closed={fmt_bool(cert['phase_residue_critical_hall_cut_unit_margin_closed'])}",
        f"phase_residue_critical_hall_cut_single_deletion_boundary_saturation_closed={fmt_bool(cert['phase_residue_critical_hall_cut_single_deletion_boundary_saturation_closed'])}",
        f"multi_unit_phase_residue_critical_hall_cut_defect_excluded={fmt_bool(cert['multi_unit_phase_residue_critical_hall_cut_defect_excluded'])}",
        f"phase_residue_unit_defect_critical_hall_cut_pdec_cap_proved={fmt_bool(cert['phase_residue_unit_defect_critical_hall_cut_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单位缺口引理",
        "",
        "上一层给出 `B_*=N_G(S_*)`、`Delta_*=|S_*|-|B_*|>0`，并且每个真子集 Hall 正常。",
        "若 `|S_*|=1`，则 `|B_*|=0` 且 `Delta_*=1`。",
        "若 `|S_*|>=2`，任取 `s in S_*`：",
        "",
        "```text",
        "|S_*|-1 <= |N_G(S_*\\{s})| <= |B_*| = |S_*|-Delta_*",
        "```",
        "",
        "所以 `Delta_*<=1`；又 `Delta_*>0` 为整数，故 `Delta_*=1`。",
        "",
        "## 2. 删除饱和与边界冗余",
        "",
        "同一不等式给出 `|N_G(S_*\\{s})|=|B_*|`，且 `N_G(S_*\\{s}) subset B_*`，因此：",
        "",
        "```text",
        "for every s in S_*: N_G(S_*\\{s})=B_*",
        "```",
        "",
        "这说明 critical cut 内不能藏有大容量缺口；边界槽在删除任一源点后仍被剩余源点触达。真正剩余变成单位缺口 critical-Hall-cut，或回流已有命名出口。",
        "",
        "## 3. unit-defect 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["unit_defect_records"]:
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
        "- 本证书没有证明 phase-residue unit-defect critical-Hall-cut PDEC/cap。",
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
