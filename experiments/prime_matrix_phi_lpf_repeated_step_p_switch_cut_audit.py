#!/usr/bin/env python3
"""审计 repeated-step source-sink path cover 中的 P-switch cut。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_p_switch_cut_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-p-switch-cut-audit.json

上一层已经证明两条 source-sink 图路径都是 mixed-P stitching。本层继续
原子化：定位每条路径的唯一 P-switch，把硬点从整条 path cover 收缩到两个
repeated node 上的 739->607 切换 cut。它仍不证明 uniform family bound。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-p-switch-cut"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

PREVIOUS_PATH_COVER_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-source-sink-path-cover-audit.json"
)
DIRECTED_GRAPH_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_PATH_COVER_AUDIT,
    DIRECTED_GRAPH_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def load_json(path: Path) -> dict[str, Any]:
    """读入 JSON 证书。"""
    return json.loads(path.read_text())


def edge_key(row: dict[str, Any]) -> str:
    """生成有向边键。"""
    return f"{row['from_atom']} -> {row['to_atom']}"


def p_direction(left_p: int, right_p: int) -> str:
    """标记 P-switch 的方向。"""
    if left_p > right_p:
        return "high_to_low"
    if left_p < right_p:
        return "low_to_high"
    return "same_P"


def p_transition(left_p: int, right_p: int) -> str:
    """生成 P-transition 标签。"""
    return f"{left_p}_to_{right_p}"


def switch_role(switch_node: str, left_edge: dict[str, Any], right_edge: dict[str, Any]) -> str:
    """给 repeated-node P-switch cut 命名。"""
    if switch_node == "g=2,c=2,A=negative":
        return "negative_repeated_node_entry_to_exit_cut"
    if switch_node == "g=6,c=7,A=positive":
        return "positive_repeated_node_bridge_to_exit_cut"
    return f"{left_edge['edge_class']}_then_{right_edge['edge_class']}"


def counter_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total if total else 0.0}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def build_switch_rows(
    path_rows: list[dict[str, Any]],
    edge_map: dict[str, dict[str, Any]],
    node_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """枚举所有相邻边之间的 P-switch cut。"""
    switch_rows: list[dict[str, Any]] = []
    for path in path_rows:
        p_values = path["P_sequence"]
        edge_keys = path["edge_keys"]
        nodes = path["node_sequence"]
        for index, (left_p, right_p) in enumerate(zip(p_values, p_values[1:])):
            if left_p == right_p:
                continue
            left_edge = edge_map[edge_keys[index]]
            right_edge = edge_map[edge_keys[index + 1]]
            switch_node = nodes[index + 1]
            node_row = node_map[switch_node]
            pair_mass = left_edge["edge_mass"] + right_edge["edge_mass"]
            switch_rows.append(
                {
                    "switch_id": f"{path['path_id']}:switch_after_edge_{index + 1}",
                    "path_id": path["path_id"],
                    "path_kind": path["path_kind"],
                    "switch_index_after_edge": index + 1,
                    "switch_node": switch_node,
                    "switch_node_class": node_row["node_class"],
                    "switch_node_occurrence_keys": node_row.get("occurrence_keys", []),
                    "switch_role": switch_role(switch_node, left_edge, right_edge),
                    "left_P": left_p,
                    "right_P": right_p,
                    "P_delta": right_p - left_p,
                    "P_direction": p_direction(left_p, right_p),
                    "P_transition": p_transition(left_p, right_p),
                    "left_edge_key": edge_keys[index],
                    "right_edge_key": edge_keys[index + 1],
                    "left_edge_id": left_edge["edge_id"],
                    "right_edge_id": right_edge["edge_id"],
                    "left_edge_class": left_edge["edge_class"],
                    "right_edge_class": right_edge["edge_class"],
                    "left_transition_role": left_edge["transition_role"],
                    "right_transition_role": right_edge["transition_role"],
                    "left_m_pair": left_edge["m_pair"],
                    "right_m_pair": right_edge["m_pair"],
                    "left_gap_delta": left_edge["gap_delta"],
                    "right_gap_delta": right_edge["gap_delta"],
                    "left_carry_delta": left_edge["carry_delta"],
                    "right_carry_delta": right_edge["carry_delta"],
                    "left_edge_mass": left_edge["edge_mass"],
                    "right_edge_mass": right_edge["edge_mass"],
                    "switch_pair_edge_mass": pair_mass,
                    "touches_repeated_bridge": (
                        left_edge["edge_class"] == "repeated_to_repeated"
                        or right_edge["edge_class"] == "repeated_to_repeated"
                    ),
                    "path_signature": path["path_signature"],
                    "local_cut_signature": f"{edge_keys[index]} || {edge_keys[index + 1]}",
                }
            )
    return switch_rows


def build_switch_edge_rows(
    switch_rows: list[dict[str, Any]], edge_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """统计哪些图边参与 P-switch cut。"""
    membership: Counter[str] = Counter()
    switch_ids: dict[str, list[str]] = defaultdict(list)
    sides: dict[str, list[str]] = defaultdict(list)
    for row in switch_rows:
        for side, key in (("left", row["left_edge_key"]), ("right", row["right_edge_key"])):
            membership[key] += 1
            switch_ids[key].append(row["switch_id"])
            sides[key].append(side)

    rows: list[dict[str, Any]] = []
    for key, edge in edge_map.items():
        rows.append(
            {
                "edge_key": key,
                "edge_id": edge["edge_id"],
                "P": edge["P"],
                "edge_class": edge["edge_class"],
                "transition_role": edge["transition_role"],
                "edge_mass": edge["edge_mass"],
                "switch_membership_count": membership[key],
                "switch_incidence_mass": membership[key] * edge["edge_mass"],
                "switch_ids": switch_ids[key],
                "switch_sides": sides[key],
                "is_switch_edge": membership[key] > 0,
            }
        )
    return sorted(rows, key=lambda row: (-row["switch_membership_count"], row["edge_key"]))


def build_switch_node_rows(
    switch_rows: list[dict[str, Any]], node_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """统计 P-switch cut 落在哪些节点上。"""
    count: Counter[str] = Counter()
    mass: Counter[str] = Counter()
    roles: dict[str, list[str]] = defaultdict(list)
    for row in switch_rows:
        node = row["switch_node"]
        count[node] += 1
        mass[node] += row["switch_pair_edge_mass"]
        roles[node].append(row["switch_role"])

    rows: list[dict[str, Any]] = []
    for node, node_row in node_map.items():
        rows.append(
            {
                "node": node,
                "node_class": node_row["node_class"],
                "switch_count": count[node],
                "switch_pair_edge_mass": mass[node],
                "roles": roles[node],
                "total_incident_mass": node_row["total_incident_mass"],
                "is_switch_node": count[node] > 0,
            }
        )
    return sorted(rows, key=lambda row: (-row["switch_count"], row["node"]))


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """生成 P-switch cut 有限审计。"""
    path_payload = load_json(PREVIOUS_PATH_COVER_AUDIT)
    graph_payload = load_json(DIRECTED_GRAPH_AUDIT)
    path_audit = path_payload["finite_audit"]
    graph_audit = graph_payload["finite_audit"]

    graph_edges = [row for row in graph_audit["directed_edge_rows"] if row["P"] <= max_prime]
    edge_map = {edge_key(row): row for row in graph_edges}
    node_map = {row["node"]: row for row in graph_audit["node_rows"]}
    repeated_nodes = {row["node"] for row in graph_audit["node_rows"] if row["node_class"] == "repeated"}

    path_rows = path_audit["path_rows"]
    switch_rows = build_switch_rows(path_rows, edge_map, node_map)
    switch_edge_rows = build_switch_edge_rows(switch_rows, edge_map)
    switch_node_rows = build_switch_node_rows(switch_rows, node_map)

    total_pair_mass = sum(row["switch_pair_edge_mass"] for row in switch_rows)
    direction_mass: Counter[str] = Counter()
    transition_mass: Counter[str] = Counter()
    node_class_mass: Counter[str] = Counter()
    role_mass: Counter[str] = Counter()
    for row in switch_rows:
        direction_mass[row["P_direction"]] += row["switch_pair_edge_mass"]
        transition_mass[row["P_transition"]] += row["switch_pair_edge_mass"]
        node_class_mass[row["switch_node_class"]] += row["switch_pair_edge_mass"]
        role_mass[row["switch_role"]] += row["switch_pair_edge_mass"]

    switch_nodes = {row["switch_node"] for row in switch_rows}
    switch_edge_incidence_count = sum(row["switch_membership_count"] for row in switch_edge_rows)
    switch_edge_incidence_mass = sum(row["switch_incidence_mass"] for row in switch_edge_rows)
    non_switch_edges = [row for row in switch_edge_rows if not row["is_switch_edge"]]

    ledger_closed = (
        path_payload["repeated_step_source_sink_path_cover_ledger_closed"]
        and graph_payload["repeated_step_directed_incidence_graph_ledger_closed"]
        and len(switch_rows) == 2
        and all(row["P_transition"] == "739_to_607" for row in switch_rows)
        and all(row["P_direction"] == "high_to_low" for row in switch_rows)
        and switch_nodes == repeated_nodes
        and switch_edge_incidence_count == 4
        and switch_edge_incidence_mass == 40
        and total_pair_mass == 40
        and len(non_switch_edges) == 1
        and non_switch_edges[0]["edge_key"] == "g=4,c=5,A=negative -> g=6,c=7,A=positive"
        and all(row["switch_node_class"] == "repeated" for row in switch_rows)
    )

    return {
        "max_prime": max_prime,
        "target_sign_word": TARGET_SIGN_WORD,
        "previous_source_sink_path_cover_ledger_closed": path_payload[
            "repeated_step_source_sink_path_cover_ledger_closed"
        ],
        "previous_directed_incidence_graph_ledger_closed": graph_payload[
            "repeated_step_directed_incidence_graph_ledger_closed"
        ],
        "repeated_step_p_switch_cut_ledger_closed": ledger_closed,
        "source_sink_path_count": path_audit["source_sink_path_count"],
        "path_switch_cut_count": len(switch_rows),
        "switch_node_count": len(switch_nodes),
        "switch_nodes": sorted(switch_nodes),
        "repeated_nodes": sorted(repeated_nodes),
        "repeated_switch_node_cover_complete": switch_nodes == repeated_nodes,
        "neighbor_switch_node_count": sum(
            1 for row in switch_node_rows if row["node_class"] == "neighbor" and row["is_switch_node"]
        ),
        "all_switches_at_repeated_nodes": all(row["switch_node_class"] == "repeated" for row in switch_rows),
        "all_switches_high_to_low": all(row["P_direction"] == "high_to_low" for row in switch_rows),
        "all_switches_739_to_607": all(row["P_transition"] == "739_to_607" for row in switch_rows),
        "switch_pair_edge_mass_total": total_pair_mass,
        "switch_edge_incidence_count": switch_edge_incidence_count,
        "switch_edge_incidence_mass": switch_edge_incidence_mass,
        "switch_edge_unique_count": sum(1 for row in switch_edge_rows if row["is_switch_edge"]),
        "non_switch_edge_unique_count": len(non_switch_edges),
        "non_switch_edge_rows": non_switch_edges,
        "switch_rows": switch_rows,
        "switch_node_rows": switch_node_rows,
        "switch_edge_rows": switch_edge_rows,
        "p_direction_rows": counter_rows(direction_mass, total_pair_mass, "P_direction"),
        "p_transition_rows": counter_rows(transition_mass, total_pair_mass, "P_transition"),
        "switch_node_class_rows": counter_rows(node_class_mass, total_pair_mass, "switch_node_class"),
        "switch_role_rows": counter_rows(role_mass, total_pair_mass, "switch_role"),
        "p_switch_cut_uniform_family_bound_proved": False,
        "single_p_orbit_repair_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    path_payload = load_json(PREVIOUS_PATH_COVER_AUDIT)
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_p_switch_cut_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "repeated_step_p_switch_cut_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the mixed-P path-cover obstruction can be localized to repeated-node P-switch cuts",
        "current_object": {
            "input": "the two mixed-P source-sink graph paths",
            "operation": "localize every P-switch to its switch node and adjacent edge pair",
            "dominant_shape": "two 739->607 cuts, exactly one at each repeated node",
            "remaining": "prove a uniform bound for repeated-node P-switch cuts or replace them by PDEC/SAE certificates",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SourceSinkPathCoverImported",
                finite_audit["previous_source_sink_path_cover_ledger_closed"],
                finite_audit["previous_source_sink_path_cover_ledger_closed"],
                "The exact two-path mixed-P source-sink cover is imported.",
                "none for import",
            ),
            gate(
                "PSwitchCutLedger",
                finite_audit["repeated_step_p_switch_cut_ledger_closed"],
                finite_audit["repeated_step_p_switch_cut_ledger_closed"],
                "Every mixed-P path switch is localized to a repeated node and adjacent edge pair.",
                "none for the finite P-switch cut ledger",
            ),
            gate(
                "RepeatedNodeSwitchCover",
                finite_audit["repeated_switch_node_cover_complete"],
                finite_audit["repeated_switch_node_cover_complete"],
                "The two switch nodes are exactly the two repeated nodes.",
                "uniform proof must control repeated-node switch cuts, not just graph paths",
            ),
            gate(
                "PSwitchCutUniformFamilyBound",
                False,
                False,
                "Control the 739->607 repeated-node switch cuts uniformly.",
                "finite switch-cut localization gives exact data but no global theorem",
            ),
        ],
        "external_sources_consulted": path_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "the P-switch cut is still a local repeated-node stitching event, not yet a trace family",
            "prime_gap_inputs": "the switch cuts are signed grammar events, not prime-gap existence statements",
            "short_interval_prime_inputs": "theta=0.52 does not control these repeated-node 739->607 cuts",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepRepeatedNodePSwitchCutUniformBound(two 739->607 cuts)",
            "AND RepeatedStepMixedPSourceSinkPathCoverUniformBoundOutsideSwitchCuts",
            "AND RepeatedStepDirectedIncidenceGraphUniformBoundOutsidePathCover",
            "AND RepeatedStepUniformFamilyBoundOutsideDirectedIncidenceGraph",
            "AND DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar outside repeated atoms)",
            "AND OtherLargestAtomTemplateWitnessFamilyBounds",
            "AND OtherCoreRouteCycleSwitchAtomBounds",
            "AND TopTwoNonCoreSignCycleResidualBound",
            "AND Gap2LowerWingTwinCollisionBound",
            "AND Gap2RightTailTwoSidedTwinResidualCollisionBound",
            "AND Gap4RightTailLeftCollarCousinCollisionBound",
            "AND Gap4UpperWingCousinResidualCollisionBound",
            "AND Gap4LowerWingCousinResidualCollisionBound",
            "AND Gap6SexyAdjacentPairCollisionBound",
            "AND GapGe8AdjacentPairCollisionBound",
            "AND NonAdjacentPrimePairCollisionBound",
            "AND AdjacentPrimeChainCollisionBound",
            "AND MultiPacketDuplicateTransportBound",
            "AND SinglePacketSingleMMultiCycleSuppression",
            "AND RepeatedOccurrenceAggregationOrPDEC",
            "AND CycleOccurrenceProductBoundOrPDEC",
            "AND SinglePSliceEndpointPacketSummationOrPDEC",
            "AND MultiPPureEndpointTraceKloostermanCompletion",
            "AND PureEndpointCarrierPhaseSaving",
            "AND MixedRightTailEndpointRouterNoLoss",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "repeated_step_p_switch_cut_ledger_closed": finite_audit[
            "repeated_step_p_switch_cut_ledger_closed"
        ],
        "p_switch_cut_uniform_family_bound_proved": False,
        "single_p_orbit_repair_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    """生成 Markdown 表格。"""
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join(["---"] * len(fields)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit_result = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF dominant-sign-word repeated-step P-switch cut 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"operation={current['operation']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. P-switch cut 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"repeated_step_p_switch_cut_ledger_closed={str(audit_result['repeated_step_p_switch_cut_ledger_closed']).lower()}",
        f"path_switch_cut_count={audit_result['path_switch_cut_count']}",
        f"switch_node_count={audit_result['switch_node_count']}",
        f"switch_nodes={audit_result['switch_nodes']}",
        f"repeated_switch_node_cover_complete={str(audit_result['repeated_switch_node_cover_complete']).lower()}",
        f"neighbor_switch_node_count={audit_result['neighbor_switch_node_count']}",
        f"all_switches_at_repeated_nodes={str(audit_result['all_switches_at_repeated_nodes']).lower()}",
        f"all_switches_high_to_low={str(audit_result['all_switches_high_to_low']).lower()}",
        f"all_switches_739_to_607={str(audit_result['all_switches_739_to_607']).lower()}",
        f"switch_pair_edge_mass_total={audit_result['switch_pair_edge_mass_total']}",
        f"switch_edge_incidence_count={audit_result['switch_edge_incidence_count']}",
        f"switch_edge_incidence_mass={audit_result['switch_edge_incidence_mass']}",
        f"switch_edge_unique_count={audit_result['switch_edge_unique_count']}",
        f"non_switch_edge_unique_count={audit_result['non_switch_edge_unique_count']}",
        f"p_switch_cut_uniform_family_bound_proved={str(audit_result['p_switch_cut_uniform_family_bound_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "summary rows：",
        "",
        *markdown_table(audit_result["p_transition_rows"], ["P_transition", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["p_direction_rows"], ["P_direction", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["switch_node_class_rows"], ["switch_node_class", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["switch_role_rows"], ["switch_role", "mass", "ratio"]),
        "",
        "switch rows：",
        "",
        *markdown_table(
            audit_result["switch_rows"],
            [
                "switch_id",
                "path_id",
                "switch_node",
                "switch_role",
                "P_transition",
                "P_delta",
                "left_edge_class",
                "right_edge_class",
                "switch_pair_edge_mass",
                "touches_repeated_bridge",
            ],
        ),
        "",
        "switch node rows：",
        "",
        *markdown_table(
            audit_result["switch_node_rows"],
            ["node", "node_class", "switch_count", "switch_pair_edge_mass", "roles", "is_switch_node"],
        ),
        "",
        "switch edge rows：",
        "",
        *markdown_table(
            audit_result["switch_edge_rows"],
            [
                "edge_key",
                "P",
                "edge_class",
                "transition_role",
                "switch_membership_count",
                "switch_incidence_mass",
                "is_switch_edge",
            ],
        ),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        *markdown_table(payload["external_sources_consulted"], ["key", "url", "role"]),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：mixed-P path-cover 的 P-switch cut 已经局部化到两个 repeated nodes。",
        "但该局部 cut 仍不是 trace/Kloosterman 可求和族，也不是单一 P-orbit 修复。",
        "",
        "## 5. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"repeated_step_p_switch_cut_ledger_closed={str(payload['repeated_step_p_switch_cut_ledger_closed']).lower()}",
        f"p_switch_cut_uniform_family_bound_proved={str(payload['p_switch_cut_uniform_family_bound_proved']).lower()}",
        f"single_p_orbit_repair_proved={str(payload['single_p_orbit_repair_proved']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
    ]
    return "\n".join(lines)


def main() -> None:
    """生成审计证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload).rstrip() + "\n")
    audit_result = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(
        "repeated_step_p_switch_cut_ledger_closed="
        f"{payload['repeated_step_p_switch_cut_ledger_closed']}"
    )
    print(f"path_switch_cut_count={audit_result['path_switch_cut_count']}")
    print(f"all_switches_739_to_607={audit_result['all_switches_739_to_607']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
