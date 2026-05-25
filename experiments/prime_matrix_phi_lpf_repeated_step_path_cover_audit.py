#!/usr/bin/env python3
"""审计 repeated-step directed graph 的 source-sink path cover。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_path_cover_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-source-sink-path-cover-audit.json

上一层把 repeated-step touching carrier 闭合为一个 5 节点 DAG。本层枚举
source-to-sink 图路径，并明确记录这些路径只是 signature graph 的 stitching：
每条 source-sink 图路径都混合了 P=607 与 P=739，不是单一 witness orbit。
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

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-source-sink-path-cover"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

PREVIOUS_DIRECTED_GRAPH_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_DIRECTED_GRAPH_AUDIT,
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


def load_previous_payload() -> dict[str, Any]:
    """读入上一层 directed-incidence graph 证书。"""
    return json.loads(PREVIOUS_DIRECTED_GRAPH_AUDIT.read_text())


def edge_key(row: dict[str, Any]) -> str:
    """生成有向边键。"""
    return f"{row['from_atom']} -> {row['to_atom']}"


def path_signature(nodes: list[str]) -> str:
    """生成路径签名。"""
    return " -> ".join(nodes)


def path_kind(nodes: list[str]) -> str:
    """标记 source-sink 路径类型。"""
    if len(nodes) == 5:
        return "long_neighbor_corridor"
    if len(nodes) == 4:
        return "bridge_shortcut_corridor"
    return "other"


def switch_count(values: list[Any]) -> int:
    """计算相邻值变化次数。"""
    return sum(1 for left, right in zip(values, values[1:]) if left != right)


def enumerate_paths(
    source: str, sink: str, adjacency: dict[str, list[tuple[str, dict[str, Any]]]]
) -> list[dict[str, Any]]:
    """枚举 DAG 中所有 source-to-sink 路径。"""
    paths: list[dict[str, Any]] = []

    def dfs(node: str, nodes: list[str], edges: list[dict[str, Any]]) -> None:
        if node == sink:
            p_values = [edge["P"] for edge in edges]
            edge_keys = [edge_key(edge) for edge in edges]
            paths.append(
                {
                    "path_id": f"path_{len(paths) + 1}",
                    "path_kind": path_kind(nodes),
                    "node_count": len(nodes),
                    "edge_count": len(edges),
                    "path_edge_mass": sum(edge["edge_mass"] for edge in edges),
                    "path_signature": path_signature(nodes),
                    "node_sequence": nodes,
                    "edge_keys": edge_keys,
                    "edge_ids": [edge["edge_id"] for edge in edges],
                    "P_sequence": p_values,
                    "P_support": sorted(set(p_values)),
                    "P_switch_count": switch_count(p_values),
                    "single_witness_path": len(set(p_values)) == 1,
                    "uses_repeated_bridge": any(edge["edge_class"] == "repeated_to_repeated" for edge in edges),
                    "uses_neighbor_corridor": any(edge["from_node_class"] == "neighbor" and edge["to_node_class"] == "repeated" for edge in edges)
                    and any(edge["from_node_class"] == "repeated" and edge["to_node_class"] == "neighbor" for edge in edges),
                }
            )
            return
        for nxt, edge in adjacency.get(node, []):
            if nxt in nodes:
                continue
            dfs(nxt, [*nodes, nxt], [*edges, edge])

    dfs(source, [source], [])
    return paths


def edge_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def build_edge_membership_rows(
    graph_edges: list[dict[str, Any]], path_rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """统计每条图边被多少 source-sink path 使用。"""
    membership: Counter[str] = Counter()
    path_ids: dict[str, list[str]] = defaultdict(list)
    for path in path_rows:
        for key in path["edge_keys"]:
            membership[key] += 1
            path_ids[key].append(path["path_id"])
    rows: list[dict[str, Any]] = []
    for edge in graph_edges:
        key = edge_key(edge)
        rows.append(
            {
                "edge_key": key,
                "edge_id": edge["edge_id"],
                "edge_class": edge["edge_class"],
                "edge_mass": edge["edge_mass"],
                "path_membership_count": membership[key],
                "path_incidence_mass": membership[key] * edge["edge_mass"],
                "path_ids": path_ids[key],
                "shared_by_all_paths": membership[key] == len(path_rows),
            }
        )
    return sorted(rows, key=lambda row: (-row["path_membership_count"], row["edge_key"]))


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """生成 source-sink path cover 有限审计。"""
    previous_payload = load_previous_payload()
    previous = previous_payload["finite_audit"]
    graph_edges = [row for row in previous["directed_edge_rows"] if row["P"] <= max_prime]
    source = previous["source_nodes"][0]
    sink = previous["sink_nodes"][0]

    adjacency: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for edge in graph_edges:
        adjacency[edge["from_atom"]].append((edge["to_atom"], edge))
    for node in adjacency:
        adjacency[node].sort(key=lambda item: item[0])

    path_rows = enumerate_paths(source, sink, adjacency)
    membership_rows = build_edge_membership_rows(graph_edges, path_rows)

    path_kind_mass: Counter[str] = Counter()
    witness_support_mass: Counter[str] = Counter()
    bridge_usage_mass: Counter[str] = Counter()
    for path in path_rows:
        path_kind_mass[path["path_kind"]] += path["path_edge_mass"]
        witness_support_mass[
            "single_P" if path["single_witness_path"] else "mixed_P"
        ] += path["path_edge_mass"]
        bridge_usage_mass[
            "uses_bridge" if path["uses_repeated_bridge"] else "avoids_bridge"
        ] += path["path_edge_mass"]

    shared_edges = [row for row in membership_rows if row["shared_by_all_paths"]]
    edge_cover_complete = all(row["path_membership_count"] >= 1 for row in membership_rows)
    branch_node = "g=2,c=2,A=negative"
    join_node = "g=6,c=7,A=positive"
    diamond_closed = (
        any(row["edge_key"] == f"{branch_node} -> g=4,c=5,A=negative" for row in membership_rows)
        and any(row["edge_key"] == f"g=4,c=5,A=negative -> {join_node}" for row in membership_rows)
        and any(row["edge_key"] == f"{branch_node} -> {join_node}" for row in membership_rows)
    )
    expected_paths = [
        "g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=4,c=5,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative",
        "g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative",
    ]
    ledger_closed = (
        previous_payload["repeated_step_directed_incidence_graph_ledger_closed"]
        and len(path_rows) == 2
        and [row["path_signature"] for row in path_rows] == expected_paths
        and sum(row["edge_count"] for row in path_rows) == 7
        and sum(row["path_edge_mass"] for row in path_rows) == 70
        and edge_cover_complete
        and len(shared_edges) == 2
        and sum(row["edge_mass"] for row in shared_edges) == 20
        and sum(row["path_incidence_mass"] for row in shared_edges) == 40
        and all(not row["single_witness_path"] for row in path_rows)
        and all(row["P_support"] == [607, 739] for row in path_rows)
        and all(row["P_switch_count"] == 1 for row in path_rows)
        and diamond_closed
    )

    total_path_mass = sum(row["path_edge_mass"] for row in path_rows)
    return {
        "max_prime": max_prime,
        "previous_directed_incidence_graph_ledger_closed": previous_payload[
            "repeated_step_directed_incidence_graph_ledger_closed"
        ],
        "target_sign_word": TARGET_SIGN_WORD,
        "repeated_step_source_sink_path_cover_ledger_closed": ledger_closed,
        "source_node": source,
        "sink_node": sink,
        "source_sink_path_count": len(path_rows),
        "source_sink_path_edge_incidence_count": sum(row["edge_count"] for row in path_rows),
        "source_sink_path_edge_incidence_mass": total_path_mass,
        "edge_cover_complete": edge_cover_complete,
        "shared_edge_count": len(shared_edges),
        "shared_edge_mass": sum(row["edge_mass"] for row in shared_edges),
        "shared_edge_path_incidence_mass": sum(row["path_incidence_mass"] for row in shared_edges),
        "single_witness_source_sink_path_count": sum(1 for row in path_rows if row["single_witness_path"]),
        "mixed_witness_source_sink_path_count": sum(1 for row in path_rows if not row["single_witness_path"]),
        "all_source_sink_paths_mixed_P": all(not row["single_witness_path"] for row in path_rows),
        "all_source_sink_paths_have_one_P_switch": all(row["P_switch_count"] == 1 for row in path_rows),
        "branch_node": branch_node,
        "join_node": join_node,
        "diamond_decomposition_closed": diamond_closed,
        "path_kind_rows": edge_rows(path_kind_mass, total_path_mass, "path_kind"),
        "witness_support_rows": edge_rows(witness_support_mass, total_path_mass, "witness_support"),
        "bridge_usage_rows": edge_rows(bridge_usage_mass, total_path_mass, "bridge_usage"),
        "path_rows": path_rows,
        "edge_membership_rows": membership_rows,
        "repeated_step_source_sink_path_cover_family_bound_proved": False,
        "single_witness_orbit_interpretation_valid": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    previous_payload = load_previous_payload()
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_source_sink_path_cover_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "repeated_step_source_sink_path_cover_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the DAG ledger, the next non-circular object is the exact source-sink path cover and its witness-stitching obstruction",
        "current_object": {
            "input": "the 5-edge acyclic repeated-step directed incidence graph",
            "operation": "enumerate source-sink graph paths and classify shared/branch/bridge edges",
            "dominant_shape": "two source-sink graph paths, both mixed-P, with a branch-join diamond between the repeated nodes",
            "remaining": "turn mixed-P graph stitching into a uniform family bound or replace it by a PDEC/SAE certificate",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "DirectedIncidenceGraphImported",
                finite_audit["previous_directed_incidence_graph_ledger_closed"],
                finite_audit["previous_directed_incidence_graph_ledger_closed"],
                "The 5-node repeated-step DAG is imported.",
                "none for import",
            ),
            gate(
                "SourceSinkPathCoverLedger",
                finite_audit["repeated_step_source_sink_path_cover_ledger_closed"],
                finite_audit["repeated_step_source_sink_path_cover_ledger_closed"],
                "All source-sink graph paths and edge memberships are enumerated.",
                "none for the finite path-cover ledger",
            ),
            gate(
                "MixedPWitnessStitchingDetected",
                finite_audit["all_source_sink_paths_mixed_P"],
                finite_audit["all_source_sink_paths_mixed_P"],
                "Every source-sink graph path mixes P=607 and P=739.",
                "uniform proof must not treat graph paths as single-witness orbits",
            ),
            gate(
                "SourceSinkPathCoverUniformFamilyBound",
                False,
                False,
                "Control the mixed-P source-sink path cover uniformly.",
                "finite path cover gives exact stitching data but no global theorem",
            ),
        ],
        "external_sources_consulted": previous_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "mixed-P graph stitching is not yet a completed trace, bilinear, or Kloosterman family",
            "prime_gap_inputs": "the source-sink graph paths are signature paths, not prime-gap existence statements",
            "short_interval_prime_inputs": "theta=0.52 does not produce a half-scale or mixed-P stitching estimate here",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepMixedPSourceSinkPathCoverUniformBound(two mixed-P graph paths)",
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
        "repeated_step_source_sink_path_cover_ledger_closed": finite_audit[
            "repeated_step_source_sink_path_cover_ledger_closed"
        ],
        "repeated_step_source_sink_path_cover_family_bound_proved": False,
        "single_witness_orbit_interpretation_valid": False,
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
        "# Prime Matrix Phi-LPF dominant-sign-word repeated-step source-sink path cover 审计",
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
        "## 2. source-sink path cover 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"repeated_step_source_sink_path_cover_ledger_closed={str(audit_result['repeated_step_source_sink_path_cover_ledger_closed']).lower()}",
        f"source_node={audit_result['source_node']}",
        f"sink_node={audit_result['sink_node']}",
        f"source_sink_path_count={audit_result['source_sink_path_count']}",
        f"source_sink_path_edge_incidence_count={audit_result['source_sink_path_edge_incidence_count']}",
        f"source_sink_path_edge_incidence_mass={audit_result['source_sink_path_edge_incidence_mass']}",
        f"edge_cover_complete={str(audit_result['edge_cover_complete']).lower()}",
        f"shared_edge_count={audit_result['shared_edge_count']}",
        f"shared_edge_mass={audit_result['shared_edge_mass']}",
        f"shared_edge_path_incidence_mass={audit_result['shared_edge_path_incidence_mass']}",
        f"single_witness_source_sink_path_count={audit_result['single_witness_source_sink_path_count']}",
        f"mixed_witness_source_sink_path_count={audit_result['mixed_witness_source_sink_path_count']}",
        f"all_source_sink_paths_mixed_P={str(audit_result['all_source_sink_paths_mixed_P']).lower()}",
        f"all_source_sink_paths_have_one_P_switch={str(audit_result['all_source_sink_paths_have_one_P_switch']).lower()}",
        f"diamond_decomposition_closed={str(audit_result['diamond_decomposition_closed']).lower()}",
        f"single_witness_orbit_interpretation_valid={str(audit_result['single_witness_orbit_interpretation_valid']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "path-kind and witness-support summaries：",
        "",
        *markdown_table(audit_result["path_kind_rows"], ["path_kind", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["witness_support_rows"], ["witness_support", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["bridge_usage_rows"], ["bridge_usage", "mass", "ratio"]),
        "",
        "source-sink path rows：",
        "",
        *markdown_table(
            audit_result["path_rows"],
            [
                "path_id",
                "path_kind",
                "edge_count",
                "path_edge_mass",
                "P_sequence",
                "P_support",
                "P_switch_count",
                "single_witness_path",
                "uses_repeated_bridge",
                "path_signature",
            ],
        ),
        "",
        "edge membership rows：",
        "",
        *markdown_table(
            audit_result["edge_membership_rows"],
            [
                "edge_key",
                "edge_class",
                "edge_mass",
                "path_membership_count",
                "path_incidence_mass",
                "shared_by_all_paths",
                "path_ids",
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
        "结论：source-sink path cover 已经闭合，但两条图路径均为 mixed-P stitching。",
        "因此不能把图路径解释为单一 witness orbit；这正是新的有限硬点边界。",
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
        f"repeated_step_source_sink_path_cover_ledger_closed={str(payload['repeated_step_source_sink_path_cover_ledger_closed']).lower()}",
        f"repeated_step_source_sink_path_cover_family_bound_proved={str(payload['repeated_step_source_sink_path_cover_family_bound_proved']).lower()}",
        f"single_witness_orbit_interpretation_valid={str(payload['single_witness_orbit_interpretation_valid']).lower()}",
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
        "repeated_step_source_sink_path_cover_ledger_closed="
        f"{payload['repeated_step_source_sink_path_cover_ledger_closed']}"
    )
    print(f"source_sink_path_count={audit_result['source_sink_path_count']}")
    print(f"all_source_sink_paths_mixed_P={audit_result['all_source_sink_paths_mixed_P']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
