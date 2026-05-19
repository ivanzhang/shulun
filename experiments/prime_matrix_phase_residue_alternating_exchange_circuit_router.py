#!/usr/bin/env python3
"""生成 phase-residue alternating exchange circuit 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_alternating_exchange_circuit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.json

输出：
  data/prime-matrix-phase-residue-alternating-exchange-circuit-ledger.json
  docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.json
  docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-alternating-exchange-circuit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-near-perfect-matching-circuit-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomNearPerfectMatchingCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomAlternatingExchangeCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueNearPerfectMatchingCircuitImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterAlternatingExchangeCircuitLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterAlternatingExchangeCircuitLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterAlternatingExchangeCircuitLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterAlternatingExchangeCircuitLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterAlternatingExchangeCircuitLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterAlternatingExchangeCircuitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterAlternatingExchangeCircuitLedger"
BASE_CHOICE = "StableLadderEndpointOrbitPhaseResidueBaseOmittedSourceAndMatchingChoiceLedger"
DELETION_MATCHINGS = "StableLadderEndpointOrbitPhaseResidueEveryDeletionMatchingImportedForExchangeLedger"
SYMMETRIC_DIFFERENCE = "StableLadderEndpointOrbitPhaseResidueMatchingSymmetricDifferenceGraphLedger"
ALTERNATING_DECOMPOSITION = "StableLadderEndpointOrbitPhaseResidueAlternatingComponentDecompositionLedger"
UNIQUE_DEFECT_PATH = "StableLadderEndpointOrbitPhaseResidueUniqueSourceDefectAlternatingPathLedger"
EVERY_SOURCE_REACHABLE = "StableLadderEndpointOrbitPhaseResidueEverySourceExchangeReachableLedger"
BOUNDARY_DOUBLE_COVER = "StableLadderEndpointOrbitPhaseResidueBoundaryDoubleCoverCarriedForwardAfterExchangeLedger"
EXCHANGE_PACKET = "StableLadderEndpointOrbitPhaseResidueAlternatingExchangeCircuitPacketLedger"
NO_ANON = "NoAnonymousNearPerfectMatchingCircuitAfterAlternatingExchangeLedger"


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
    """把 near-perfect matching circuit 硬点替换为 alternating exchange circuit 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


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
        BASE_CHOICE,
        DELETION_MATCHINGS,
        SYMMETRIC_DIFFERENCE,
        ALTERNATING_DECOMPOSITION,
        UNIQUE_DEFECT_PATH,
        EVERY_SOURCE_REACHABLE,
        BOUNDARY_DOUBLE_COVER,
        EXCHANGE_PACKET,
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


def exchange_records() -> list[dict[str, str]]:
    """给出 alternating exchange circuit 的字段。"""
    return [
        {
            "field": "base_deleted_source",
            "meaning": "任选基准缺失源点 s0，并取完美匹配 M0=M_{s0}:S_*\\{s0}->B_*。",
        },
        {
            "field": "single_deletion_matching_family",
            "meaning": "对每个 s in S_*，已有完美匹配 M_s:S_*\\{s}->B_*。",
        },
        {
            "field": "symmetric_difference",
            "meaning": "H_s=M0 Δ M_s 中每个边界点度数为 0 或 2，源点除 s、s0 外度数为 0 或 2。",
        },
        {
            "field": "unique_defect_path",
            "meaning": "H_s 分解为偶交替圈加一条端点为 s 与 s0 的交替路径 P_s。",
        },
        {
            "field": "exchange_reachability",
            "meaning": "每个源点都能沿交替交换路径把唯一未匹配源点交换到基准缺失源点。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 alternating exchange circuit 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueNearPerfectMatchingCircuitImported",
            imported,
            False,
            "上一层剩余含 phase-residue near-perfect matching circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "交换图退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueBaseOmittedSourceAndMatchingChoice",
            True,
            True,
            "固定基准缺失源点 s0 及其完美删除匹配 M0。",
            BASE_CHOICE,
        ),
        row(
            "PhaseResidueEveryDeletionMatchingImportedForExchange",
            True,
            True,
            "导入上一层对每个 s 的完美匹配 M_s:S_*\\{s}->B_*。",
            DELETION_MATCHINGS,
        ),
        row(
            "PhaseResidueMatchingSymmetricDifferenceGraph",
            True,
            True,
            "对任意 s，H_s=M0 Δ M_s 是二部交替差图。",
            SYMMETRIC_DIFFERENCE,
        ),
        row(
            "PhaseResidueAlternatingComponentDecomposition",
            True,
            True,
            "H_s 分解为交替偶圈加至多一条开路径。",
            ALTERNATING_DECOMPOSITION,
        ),
        row(
            "PhaseResidueUniqueSourceDefectAlternatingPath",
            True,
            True,
            "当 s!=s0，唯一开路径端点正是 s 与 s0。",
            UNIQUE_DEFECT_PATH,
        ),
        row(
            "PhaseResidueEverySourceExchangeReachable",
            True,
            True,
            "每个源点都能经交替交换路径到达基准缺失源点。",
            EVERY_SOURCE_REACHABLE,
        ),
        row(
            "PhaseResidueBoundaryDoubleCoverCarriedForwardAfterExchange",
            True,
            True,
            "上一层边界二重覆盖继续约束交换路径的每个边界槽。",
            BOUNDARY_DOUBLE_COVER,
        ),
        row(
            "PhaseResidueAlternatingExchangeCircuitPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 alternating exchange circuit PDEC/cap。",
            EXCHANGE_PACKET,
        ),
        row(
            "NoAnonymousNearPerfectMatchingCircuitAfterAlternatingExchange",
            True,
            True,
            "near-perfect matching circuit 不再匿名保留；它含显式交替交换路径族或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterAlternatingExchangeCircuit",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueAlternatingExchangeCircuitStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、alternating exchange circuit、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 alternating exchange circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 alternating exchange circuit 证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    plain = (
        "phase-residue near-perfect matching circuit 已给出 |S_*|=|B_*|+1，且对每个 s 都有完美删除匹配 M_s。"
        "固定基准 s0 与 M0=M_{s0}。对任意 s!=s0，取 H_s=M0 Δ M_s。"
        "因为两匹配都覆盖全部 B_*，边界端点在 H_s 中度数为 0 或 2；源点除 s、s0 外度数为 0 或 2，"
        "而 s 与 s0 度数为 1。故 H_s 分解为交替偶圈加一条端点为 s、s0 的交替路径。"
        "剩余反例不再是孤立的近完美匹配缺口，而是每个源点都交换可达基准缺失源点的 alternating exchange circuit PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_alternating_exchange_circuit_router",
        "status": "phase_residue_near_perfect_matching_circuit_reduced_to_alternating_exchange_circuit_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": old_target or OLD_TARGET,
        "hardpoint_after_router": reduced,
        "phase_residue_near_perfect_matching_circuit_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_base_omitted_source_and_matching_choice_closed": True,
        "phase_residue_every_deletion_matching_imported_for_exchange": True,
        "phase_residue_matching_symmetric_difference_graph_closed": True,
        "phase_residue_alternating_component_decomposition_closed": True,
        "phase_residue_unique_source_defect_alternating_path_closed": True,
        "phase_residue_every_source_exchange_reachable_closed": True,
        "phase_residue_boundary_double_cover_carried_forward_after_exchange": True,
        "phase_residue_alternating_exchange_circuit_packet_registered": True,
        "anonymous_near_perfect_matching_circuit_removed_after_exchange": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_alternating_exchange_circuit_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "exchange_circuit_formulas": {
            "base_matching": "choose s0 in S_* and M0=M_{s0}:S_*\\{s0}->B_*",
            "other_matching": "for every s in S_*, M_s:S_*\\{s}->B_*",
            "symmetric_difference": "H_s=M0 Δ M_s",
            "boundary_degree": "deg_{H_s}(b) in {0,2} for b in B_*",
            "source_degree": "deg_{H_s}(u) in {0,2} except deg(s)=deg(s0)=1",
            "unique_path": "H_s contains an alternating path P_s from s to s0 plus alternating cycles",
            "new_exit": NEW_TARGET,
        },
        "exchange_circuit_records": exchange_records(),
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "decision_rows": build_rows(previous, new_target),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue alternating exchange circuit 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_near_perfect_matching_circuit_imported={fmt_bool(cert['phase_residue_near_perfect_matching_circuit_imported'])}",
        f"phase_residue_matching_symmetric_difference_graph_closed={fmt_bool(cert['phase_residue_matching_symmetric_difference_graph_closed'])}",
        f"phase_residue_unique_source_defect_alternating_path_closed={fmt_bool(cert['phase_residue_unique_source_defect_alternating_path_closed'])}",
        f"phase_residue_every_source_exchange_reachable_closed={fmt_bool(cert['phase_residue_every_source_exchange_reachable_closed'])}",
        f"phase_residue_alternating_exchange_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_alternating_exchange_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 基准匹配与对称差",
        "",
        "上一层给出对每个 `s in S_*` 的完美删除匹配 `M_s:S_*\\{s}->B_*`。",
        "任选基准缺失源点 `s0`，令 `M0=M_{s0}`。对任意 `s != s0`，考察：",
        "",
        "```text",
        "H_s = M0 Δ M_s",
        "```",
        "",
        "`M0` 与 `M_s` 都覆盖全部 `B_*`，所以每个边界槽在 `H_s` 中度数为 `0` 或 `2`。",
        "源点侧除 `s` 与 `s0` 外，要么同时被两匹配使用，要么差分抵消，度数为 `0` 或 `2`；",
        "`s` 只在 `M0` 中出现，`s0` 只在 `M_s` 中出现，二者度数为 `1`。",
        "",
        "## 2. 交替交换路径",
        "",
        "二部匹配的对称差只能分解为交替偶圈与交替开路径。",
        "由于开端点只有 `s` 和 `s0`，故 `H_s` 中存在唯一开路径：",
        "",
        "```text",
        "P_s: s -> ... -> s0",
        "```",
        "",
        "这条路径给出把“未匹配源点为 s”的状态交换到“未匹配源点为 s0”的显式交换链。",
        "因此每个源点都不是独立缺口；它必须进入同一个基准缺失源点的交换可达场。",
        "",
        "## 3. exchange circuit 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["exchange_circuit_records"]:
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
        "- 本证书没有证明 phase-residue alternating exchange circuit PDEC/cap。",
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
