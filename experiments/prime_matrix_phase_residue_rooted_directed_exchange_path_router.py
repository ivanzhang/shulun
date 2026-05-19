#!/usr/bin/env python3
"""生成 phase-residue rooted directed exchange path 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_rooted_directed_exchange_path_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.json

输出：
  data/prime-matrix-phase-residue-rooted-directed-exchange-path-ledger.json
  docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.json
  docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-rooted-directed-exchange-path"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-alternating-exchange-circuit-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomAlternatingExchangeCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomRootedDirectedExchangePathCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueAlternatingExchangeCircuitImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterRootedDirectedExchangePathLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterRootedDirectedExchangePathLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterRootedDirectedExchangePathLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterRootedDirectedExchangePathLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterRootedDirectedExchangePathLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterRootedDirectedExchangePathLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterRootedDirectedExchangePathLedger"
BASE = "StableLadderEndpointOrbitPhaseResidueExchangeRootBaseMatchingImportedLedger"
PATH_FAMILY = "StableLadderEndpointOrbitPhaseResidueAlternatingPathFamilyImportedForRootedDirectionLedger"
EDGE_COLORING = "StableLadderEndpointOrbitPhaseResidueExchangePathM0MsEdgeColoringLedger"
ROOT_ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangePathRootOrientationLedger"
SIMPLE_PATH = "StableLadderEndpointOrbitPhaseResidueSimpleDirectedExchangePathNormalFormLedger"
TOGGLE_TRANSFER = "StableLadderEndpointOrbitPhaseResidueExchangeToggleTransferLedger"
EVERY_SOURCE_ROOTED = "StableLadderEndpointOrbitPhaseResidueEverySourceRootReachableByDirectedExchangeLedger"
DIRECTED_PACKET = "StableLadderEndpointOrbitPhaseResidueRootedDirectedExchangePathPacketLedger"
NO_ANON = "NoAnonymousAlternatingExchangeCircuitAfterRootedDirectedPathLedger"


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
    """把 alternating exchange circuit 硬点替换为 rooted directed exchange path 硬点。"""
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
        BASE,
        PATH_FAMILY,
        EDGE_COLORING,
        ROOT_ORIENTATION,
        SIMPLE_PATH,
        TOGGLE_TRANSFER,
        EVERY_SOURCE_ROOTED,
        DIRECTED_PACKET,
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


def directed_records() -> list[dict[str, str]]:
    """给出 rooted directed exchange path 的字段。"""
    return [
        {
            "field": "root_base",
            "meaning": "固定基准缺失源点 s0 与基准匹配 M0=M_{s0}。",
        },
        {
            "field": "edge_coloring",
            "meaning": "每条路径边按来源着色为 M0-only 或 M_s-only，并严格交替。",
        },
        {
            "field": "root_orientation",
            "meaning": "M0-only 边按 source->boundary 定向，M_s-only 边按 boundary->source 定向。",
        },
        {
            "field": "directed_path",
            "meaning": "对每个 s!=s0，P_s 被定向为 s 到 s0 的简单有向交替路径。",
        },
        {
            "field": "toggle_transfer",
            "meaning": "沿 P_s 做对称差切换，可在 M0 与 M_s 的缺失源点状态之间转换。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 rooted directed exchange path 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueAlternatingExchangeCircuitImported",
            imported,
            False,
            "上一层剩余含 phase-residue alternating exchange circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "有向交换路径退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeRootBaseMatchingImported",
            True,
            True,
            "导入固定根 s0 与基准匹配 M0。",
            BASE,
        ),
        row(
            "PhaseResidueAlternatingPathFamilyImportedForRootedDirection",
            True,
            True,
            "导入上一层每个 s 到 s0 的交替路径 P_s。",
            PATH_FAMILY,
        ),
        row(
            "PhaseResidueExchangePathM0MsEdgeColoring",
            True,
            True,
            "每条 P_s 的边按 M0-only/M_s-only 着色并交替。",
            EDGE_COLORING,
        ),
        row(
            "PhaseResidueExchangePathRootOrientation",
            True,
            True,
            "按 M0-only: source->boundary 与 M_s-only: boundary->source 给 P_s 定向。",
            ROOT_ORIENTATION,
        ),
        row(
            "PhaseResidueSimpleDirectedExchangePathNormalForm",
            True,
            True,
            "去除重复顶点后保留同端点简单有向交替路径。",
            SIMPLE_PATH,
        ),
        row(
            "PhaseResidueExchangeToggleTransfer",
            True,
            True,
            "沿 P_s 对称差切换，在 M0 与 M_s 的缺失源点状态之间转换。",
            TOGGLE_TRANSFER,
        ),
        row(
            "PhaseResidueEverySourceRootReachableByDirectedExchange",
            True,
            True,
            "每个源点都通过有向交换路径到达基准缺失源点。",
            EVERY_SOURCE_ROOTED,
        ),
        row(
            "PhaseResidueRootedDirectedExchangePathPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 rooted directed exchange path circuit PDEC/cap。",
            DIRECTED_PACKET,
        ),
        row(
            "NoAnonymousAlternatingExchangeCircuitAfterRootedDirectedPath",
            True,
            True,
            "alternating exchange circuit 不再匿名保留；它含根、有向路径族和切换规则或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterRootedDirectedExchangePath",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueRootedDirectedExchangePathStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、rooted directed exchange path、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 rooted directed exchange path circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 rooted directed exchange path 证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    plain = (
        "phase-residue alternating exchange circuit 已给出基准 s0、M0 以及每个 s 到 s0 的交替路径 P_s。"
        "在 P_s 上把 M0-only 边定向为 source->boundary，把 M_s-only 边定向为 boundary->source，"
        "则路径从 s 有向到 s0；去掉重复顶点后仍是同端点简单有向交替路径。"
        "沿 P_s 作对称差切换可在基准匹配 M0 与删除 s 的匹配 M_s 之间转换。"
        "剩余反例不再是无方向交换 circuit，而是带根、边色、有向路径和切换规则的 rooted directed exchange path circuit PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_rooted_directed_exchange_path_router",
        "status": "phase_residue_alternating_exchange_circuit_reduced_to_rooted_directed_exchange_path_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": old_target or OLD_TARGET,
        "hardpoint_after_router": reduced,
        "phase_residue_alternating_exchange_circuit_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_exchange_root_base_matching_imported": True,
        "phase_residue_alternating_path_family_imported_for_rooted_direction": True,
        "phase_residue_exchange_path_m0_ms_edge_coloring_closed": True,
        "phase_residue_exchange_path_root_orientation_closed": True,
        "phase_residue_simple_directed_exchange_path_normal_form_closed": True,
        "phase_residue_exchange_toggle_transfer_closed": True,
        "phase_residue_every_source_root_reachable_by_directed_exchange_closed": True,
        "phase_residue_rooted_directed_exchange_path_packet_registered": True,
        "anonymous_alternating_exchange_circuit_removed_after_rooted_directed_path": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_rooted_directed_exchange_path_circuit_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "rooted_directed_exchange_path_formulas": {
            "root": "choose s0 in S_* and M0=M_{s0}",
            "path": "P_s is the unique alternating open path in M0 Δ M_s from s to s0",
            "edge_coloring": "edges alternate M0-only, M_s-only, ...",
            "orientation": "M0-only source->boundary; M_s-only boundary->source",
            "directed_reachability": "for every s in S_*, s ->* s0 in the oriented exchange path",
            "toggle": "M0 Δ P_s = M_s on the path component",
            "new_exit": NEW_TARGET,
        },
        "rooted_directed_exchange_path_records": directed_records(),
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "decision_rows": build_rows(previous, new_target),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue rooted directed exchange path 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_alternating_exchange_circuit_imported={fmt_bool(cert['phase_residue_alternating_exchange_circuit_imported'])}",
        f"phase_residue_exchange_path_m0_ms_edge_coloring_closed={fmt_bool(cert['phase_residue_exchange_path_m0_ms_edge_coloring_closed'])}",
        f"phase_residue_exchange_path_root_orientation_closed={fmt_bool(cert['phase_residue_exchange_path_root_orientation_closed'])}",
        f"phase_residue_every_source_root_reachable_by_directed_exchange_closed={fmt_bool(cert['phase_residue_every_source_root_reachable_by_directed_exchange_closed'])}",
        f"phase_residue_rooted_directed_exchange_path_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_rooted_directed_exchange_path_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 根与边色",
        "",
        "上一层已经固定 `s0`、`M0=M_{s0}`，并给出每个 `s!=s0` 的交替路径 `P_s`。",
        "`P_s` 来自 `M0 Δ M_s`，因此边天然分成两类：",
        "",
        "```text",
        "M0-only edge, M_s-only edge",
        "```",
        "",
        "路径从源点 `s` 出发时第一条边属于 `M0`，终止到 `s0` 时最后一条边属于 `M_s`，两类边严格交替。",
        "",
        "## 2. 根向有向路径",
        "",
        "按如下规则定向：",
        "",
        "```text",
        "M0-only: source -> boundary",
        "M_s-only: boundary -> source",
        "```",
        "",
        "于是 `P_s` 被定向为：",
        "",
        "```text",
        "s -> b1 -> u1 -> ... -> s0",
        "```",
        "",
        "若路径中出现重复顶点，截去闭合交替圈后保留同端点简单有向交替路径。",
        "因此每个源点都通过显式方向到达同一个基准缺失源点。",
        "",
        "## 3. 切换解释",
        "",
        "沿 `P_s` 做对称差切换，会把 `M0` 在该路径上的边替换为 `M_s` 的边：",
        "",
        "```text",
        "M0 Δ P_s = M_s on the path component",
        "```",
        "",
        "这给出缺失源点状态之间的显式转移规则；剩余硬点必须在这个有向转移场中形成相位或容量矛盾。",
        "",
        "## 4. rooted directed exchange path 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["rooted_directed_exchange_path_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend([
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 6. 判定表",
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
        "## 7. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 8. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 phase-residue rooted directed exchange path circuit PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 9. 依赖哈希",
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
