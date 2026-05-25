#!/usr/bin/env python3
"""审计 repeated signed step carrier 的有向 incidence graph。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_incidence_graph_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-audit.json

上一层把两个 repeated signed step atoms 拆成四个 occurrence 与五条 touching
transition。本层把这五条 transition 看成有向图，关闭有限 node/edge/degree/DAG
账本；它仍不证明 repeated-step uniform family bound。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

PREVIOUS_REPEATED_STEP_OCCURRENCE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-occurrence-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_REPEATED_STEP_OCCURRENCE_AUDIT,
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
    """读入上一层 repeated-step occurrence 证书。"""
    return json.loads(PREVIOUS_REPEATED_STEP_OCCURRENCE_AUDIT.read_text())


def node_class(atom: str, repeated_atoms: set[str]) -> str:
    """区分 repeated node 与邻接 node。"""
    return "repeated" if atom in repeated_atoms else "neighbor"


def edge_class(from_atom: str, to_atom: str, repeated_atoms: set[str]) -> str:
    """生成有向边类别。"""
    return f"{node_class(from_atom, repeated_atoms)}_to_{node_class(to_atom, repeated_atoms)}"


def transition_role(row: dict[str, Any], from_atom: str, to_atom: str, repeated_atoms: set[str]) -> str:
    """标记 transition 相对于 repeated carrier 的局部角色。"""
    cls = edge_class(from_atom, to_atom, repeated_atoms)
    if cls == "repeated_to_repeated":
        return "repeated_bridge"
    if cls == "repeated_to_neighbor" and row["from_step"] == 1:
        return "initial_exit"
    if cls == "repeated_to_neighbor":
        return "internal_exit"
    if cls == "neighbor_to_repeated" and row["to_step"] == 5:
        return "terminal_entry"
    return "internal_entry"


def edge_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def build_graph_edges(touching_rows: list[dict[str, Any]], repeated_atoms: set[str]) -> list[dict[str, Any]]:
    """把 touching transition rows 变成 directed graph edge rows。"""
    graph_edges: list[dict[str, Any]] = []
    for row in touching_rows:
        from_atom = row["from_signed_step_signature"]
        to_atom = row["to_signed_step_signature"]
        mass = row["touching_transition_mass"]
        graph_edges.append(
            {
                "edge_id": f"P{row['P']}:step{row['from_step']}-{row['to_step']}",
                "P": row["P"],
                "m_pair": row["m_pair"],
                "from_step": row["from_step"],
                "to_step": row["to_step"],
                "from_atom": from_atom,
                "to_atom": to_atom,
                "from_node_class": node_class(from_atom, repeated_atoms),
                "to_node_class": node_class(to_atom, repeated_atoms),
                "edge_class": edge_class(from_atom, to_atom, repeated_atoms),
                "transition_role": transition_role(row, from_atom, to_atom, repeated_atoms),
                "sign_pair": row["sign_pair"],
                "gap_delta": row["gap_delta"],
                "carry_delta": row["carry_delta"],
                "edge_mass": mass,
                "repeated_endpoint_incidence_count": int(from_atom in repeated_atoms)
                + int(to_atom in repeated_atoms),
                "transition_signature": row["transition_signature"],
            }
        )
    return sorted(graph_edges, key=lambda row: (row["P"], row["from_step"], row["to_step"]))


def weak_components(nodes: set[str], edges: list[dict[str, Any]]) -> list[list[str]]:
    """计算无向弱连通分量。"""
    graph: dict[str, set[str]] = {node: set() for node in nodes}
    for row in edges:
        graph[row["from_atom"]].add(row["to_atom"])
        graph[row["to_atom"]].add(row["from_atom"])
    seen: set[str] = set()
    comps: list[list[str]] = []
    for node in sorted(nodes):
        if node in seen:
            continue
        comp: list[str] = []
        queue: deque[str] = deque([node])
        seen.add(node)
        while queue:
            current = queue.popleft()
            comp.append(current)
            for nxt in sorted(graph[current]):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        comps.append(sorted(comp))
    return comps


def dag_summary(nodes: set[str], edges: list[dict[str, Any]]) -> dict[str, Any]:
    """计算 DAG、源汇点和最长有向链。"""
    out_edges: dict[str, list[str]] = {node: [] for node in nodes}
    indegree: Counter[str] = Counter({node: 0 for node in nodes})
    for row in edges:
        out_edges[row["from_atom"]].append(row["to_atom"])
        indegree[row["to_atom"]] += 1

    queue: deque[str] = deque(sorted(node for node in nodes if indegree[node] == 0))
    topo: list[str] = []
    indegree_work = Counter(indegree)
    while queue:
        node = queue.popleft()
        topo.append(node)
        for nxt in sorted(out_edges[node]):
            indegree_work[nxt] -= 1
            if indegree_work[nxt] == 0:
                queue.append(nxt)

    is_dag = len(topo) == len(nodes)
    if not is_dag:
        return {
            "directed_acyclic": False,
            "source_nodes": [],
            "sink_nodes": [],
            "longest_directed_path_length": None,
            "longest_directed_path_nodes": [],
        }

    dist = {node: 0 for node in nodes}
    parent: dict[str, str | None] = {node: None for node in nodes}
    for node in topo:
        for nxt in sorted(out_edges[node]):
            if dist[node] + 1 > dist[nxt]:
                dist[nxt] = dist[node] + 1
                parent[nxt] = node
    end = max(sorted(nodes), key=lambda node: dist[node])
    path = [end]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])  # type: ignore[arg-type]
    path.reverse()
    return {
        "directed_acyclic": True,
        "source_nodes": sorted(node for node in nodes if indegree[node] == 0),
        "sink_nodes": sorted(node for node in nodes if not out_edges[node]),
        "longest_directed_path_length": dist[end],
        "longest_directed_path_nodes": path,
    }


def build_node_rows(
    nodes: set[str], edges: list[dict[str, Any]], repeated_atoms: set[str], repeated_atom_rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """汇总节点入出度、质量和 occurrence 支撑。"""
    in_degree: Counter[str] = Counter()
    out_degree: Counter[str] = Counter()
    in_mass: Counter[str] = Counter()
    out_mass: Counter[str] = Counter()
    occurrence_keys = {
        row["repeated_signed_step_atom"]: row["occurrence_keys"]
        for row in repeated_atom_rows
    }
    for row in edges:
        out_degree[row["from_atom"]] += 1
        in_degree[row["to_atom"]] += 1
        out_mass[row["from_atom"]] += row["edge_mass"]
        in_mass[row["to_atom"]] += row["edge_mass"]
    result: list[dict[str, Any]] = []
    for node in sorted(nodes):
        result.append(
            {
                "node": node,
                "node_class": node_class(node, repeated_atoms),
                "in_degree": in_degree[node],
                "out_degree": out_degree[node],
                "total_degree": in_degree[node] + out_degree[node],
                "in_mass": in_mass[node],
                "out_mass": out_mass[node],
                "total_incident_mass": in_mass[node] + out_mass[node],
                "is_source": in_degree[node] == 0,
                "is_sink": out_degree[node] == 0,
                "occurrence_keys": occurrence_keys.get(node, []),
            }
        )
    return result


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """生成 directed incidence graph 有限审计。"""
    previous_payload = load_previous_payload()
    previous = previous_payload["finite_audit"]
    repeated_atoms = set(previous["repeated_signed_step_atoms"])
    touching_rows = [
        row for row in previous["touching_transition_rows"] if row["P"] <= max_prime
    ]
    graph_edges = build_graph_edges(touching_rows, repeated_atoms)
    nodes = {row["from_atom"] for row in graph_edges} | {row["to_atom"] for row in graph_edges}
    repeated_nodes = sorted(nodes & repeated_atoms)
    neighbor_nodes = sorted(nodes - repeated_atoms)

    edge_class_mass: Counter[str] = Counter()
    transition_role_mass: Counter[str] = Counter()
    sign_pair_mass: Counter[str] = Counter()
    repeated_endpoint_incidence_mass = 0
    repeated_endpoint_incidence_count = 0
    for row in graph_edges:
        edge_class_mass[row["edge_class"]] += row["edge_mass"]
        transition_role_mass[row["transition_role"]] += row["edge_mass"]
        sign_pair_mass[row["sign_pair"]] += row["edge_mass"]
        repeated_endpoint_incidence_count += row["repeated_endpoint_incidence_count"]
        repeated_endpoint_incidence_mass += (
            row["edge_mass"] * row["repeated_endpoint_incidence_count"]
        )

    node_rows = build_node_rows(nodes, graph_edges, repeated_atoms, previous["repeated_atom_rows"])
    comps = weak_components(nodes, graph_edges)
    dag = dag_summary(nodes, graph_edges)

    cross_repeated_edges = [
        row for row in graph_edges if row["edge_class"] == "repeated_to_repeated"
    ]
    expected_edge_classes = {
        "neighbor_to_repeated": 20,
        "repeated_to_neighbor": 20,
        "repeated_to_repeated": 10,
    }
    expected_longest_path = [
        "g=6,c=6,A=positive",
        "g=2,c=2,A=negative",
        "g=4,c=5,A=negative",
        "g=6,c=7,A=positive",
        "g=8,c=10,A=negative",
    ]
    ledger_closed = (
        previous_payload["dominant_sign_word_repeated_step_occurrence_ledger_closed"]
        and len(repeated_nodes) == 2
        and len(neighbor_nodes) == 3
        and len(nodes) == 5
        and len(graph_edges) == 5
        and sum(row["edge_mass"] for row in graph_edges) == 50
        and dict(edge_class_mass) == expected_edge_classes
        and len(cross_repeated_edges) == 1
        and cross_repeated_edges[0]["transition_signature"]
        == "g=2,c=2,A=negative -> g=6,c=7,A=positive"
        and repeated_endpoint_incidence_count == 6
        and repeated_endpoint_incidence_mass == 60
        and len(comps) == 1
        and dag["directed_acyclic"] is True
        and dag["source_nodes"] == ["g=6,c=6,A=positive"]
        and dag["sink_nodes"] == ["g=8,c=10,A=negative"]
        and dag["longest_directed_path_length"] == 4
        and dag["longest_directed_path_nodes"] == expected_longest_path
    )

    return {
        "max_prime": max_prime,
        "previous_repeated_step_occurrence_ledger_closed": previous_payload[
            "dominant_sign_word_repeated_step_occurrence_ledger_closed"
        ],
        "target_sign_word": TARGET_SIGN_WORD,
        "repeated_step_directed_incidence_graph_ledger_closed": ledger_closed,
        "node_count": len(nodes),
        "repeated_node_count": len(repeated_nodes),
        "neighbor_node_count": len(neighbor_nodes),
        "directed_edge_count": len(graph_edges),
        "directed_edge_mass": sum(row["edge_mass"] for row in graph_edges),
        "repeated_endpoint_incidence_count": repeated_endpoint_incidence_count,
        "repeated_endpoint_incidence_mass": repeated_endpoint_incidence_mass,
        "weak_component_count": len(comps),
        "weak_components": comps,
        "directed_acyclic": dag["directed_acyclic"],
        "source_nodes": dag["source_nodes"],
        "sink_nodes": dag["sink_nodes"],
        "longest_directed_path_length": dag["longest_directed_path_length"],
        "longest_directed_path_nodes": dag["longest_directed_path_nodes"],
        "cross_repeated_bridge_edge_count": len(cross_repeated_edges),
        "cross_repeated_bridge_edge_mass": sum(row["edge_mass"] for row in cross_repeated_edges),
        "edge_class_rows": edge_rows(
            edge_class_mass, sum(row["edge_mass"] for row in graph_edges), "edge_class"
        ),
        "transition_role_rows": edge_rows(
            transition_role_mass, sum(row["edge_mass"] for row in graph_edges), "transition_role"
        ),
        "sign_pair_rows": edge_rows(sign_pair_mass, sum(row["edge_mass"] for row in graph_edges), "sign_pair"),
        "node_rows": node_rows,
        "directed_edge_rows": graph_edges,
        "repeated_step_directed_incidence_graph_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    previous_payload = load_previous_payload()
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_directed_incidence_graph_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "repeated_step_directed_incidence_graph_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the repeated-step carrier is the smallest current non-circular finite obstruction after occurrence localization",
        "current_object": {
            "input": "five touching transitions around two repeated signed step atoms",
            "operation": "view touching transitions as a directed incidence graph",
            "dominant_shape": "one acyclic weak component with two repeated nodes, three neighbor nodes, and one repeated-to-repeated bridge",
            "remaining": "upgrade the finite acyclic carrier to a uniform directed-incidence family bound or PDEC/SAE certificate",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RepeatedStepOccurrenceImported",
                finite_audit["previous_repeated_step_occurrence_ledger_closed"],
                finite_audit["previous_repeated_step_occurrence_ledger_closed"],
                "The repeated-step occurrence/touching-transition ledger is imported.",
                "none for import",
            ),
            gate(
                "DirectedIncidenceGraphLedger",
                finite_audit["repeated_step_directed_incidence_graph_ledger_closed"],
                finite_audit["repeated_step_directed_incidence_graph_ledger_closed"],
                "The five touching transitions form an exact directed node/edge graph.",
                "none for the finite graph ledger",
            ),
            gate(
                "AcyclicCarrierLedger",
                finite_audit["directed_acyclic"],
                finite_audit["directed_acyclic"],
                "The finite carrier is a DAG with one source and one sink.",
                "none for the finite acyclicity ledger",
            ),
            gate(
                "DirectedIncidenceUniformFamilyBound",
                False,
                False,
                "Control this acyclic carrier uniformly in the full Phi-LPF family.",
                "finite graph audit gives exact structure but no global theorem",
            ),
        ],
        "external_sources_consulted": previous_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "the acyclic finite graph is not yet a complete trace, bilinear, or Kloosterman summation family",
            "prime_gap_inputs": "the directed source/sink structure is local grammar data, not a prime-gap existence result",
            "short_interval_prime_inputs": "theta=0.52 remains an external scale bound and does not imply this directed-incidence family estimate",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepDirectedIncidenceGraphUniformBound(acyclic two-repeated-node carrier)",
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
        "repeated_step_directed_incidence_graph_ledger_closed": finite_audit[
            "repeated_step_directed_incidence_graph_ledger_closed"
        ],
        "repeated_step_directed_incidence_graph_family_bound_proved": False,
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
        "# Prime Matrix Phi-LPF dominant-sign-word repeated-step directed-incidence graph 审计",
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
        "## 2. directed incidence graph 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"repeated_step_directed_incidence_graph_ledger_closed={str(audit_result['repeated_step_directed_incidence_graph_ledger_closed']).lower()}",
        f"node_count={audit_result['node_count']}",
        f"repeated_node_count={audit_result['repeated_node_count']}",
        f"neighbor_node_count={audit_result['neighbor_node_count']}",
        f"directed_edge_count={audit_result['directed_edge_count']}",
        f"directed_edge_mass={audit_result['directed_edge_mass']}",
        f"repeated_endpoint_incidence_count={audit_result['repeated_endpoint_incidence_count']}",
        f"repeated_endpoint_incidence_mass={audit_result['repeated_endpoint_incidence_mass']}",
        f"weak_component_count={audit_result['weak_component_count']}",
        f"directed_acyclic={str(audit_result['directed_acyclic']).lower()}",
        f"source_nodes={audit_result['source_nodes']}",
        f"sink_nodes={audit_result['sink_nodes']}",
        f"longest_directed_path_length={audit_result['longest_directed_path_length']}",
        f"longest_directed_path_nodes={audit_result['longest_directed_path_nodes']}",
        f"cross_repeated_bridge_edge_count={audit_result['cross_repeated_bridge_edge_count']}",
        f"cross_repeated_bridge_edge_mass={audit_result['cross_repeated_bridge_edge_mass']}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "edge-class and role summaries：",
        "",
        *markdown_table(audit_result["edge_class_rows"], ["edge_class", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["transition_role_rows"], ["transition_role", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["sign_pair_rows"], ["sign_pair", "mass", "ratio"]),
        "",
        "node rows：",
        "",
        *markdown_table(
            audit_result["node_rows"],
            [
                "node",
                "node_class",
                "in_degree",
                "out_degree",
                "total_degree",
                "in_mass",
                "out_mass",
                "is_source",
                "is_sink",
                "occurrence_keys",
            ],
        ),
        "",
        "directed edge rows：",
        "",
        *markdown_table(
            audit_result["directed_edge_rows"],
            [
                "edge_id",
                "m_pair",
                "from_atom",
                "to_atom",
                "edge_class",
                "transition_role",
                "sign_pair",
                "edge_mass",
                "repeated_endpoint_incidence_count",
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
        "结论：repeated-step touching carrier 已经闭合为一个有限有向无环图。",
        "该账本仍不是全局 uniform family bound。",
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
        f"repeated_step_directed_incidence_graph_ledger_closed={str(payload['repeated_step_directed_incidence_graph_ledger_closed']).lower()}",
        f"repeated_step_directed_incidence_graph_family_bound_proved={str(payload['repeated_step_directed_incidence_graph_family_bound_proved']).lower()}",
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
        "repeated_step_directed_incidence_graph_ledger_closed="
        f"{payload['repeated_step_directed_incidence_graph_ledger_closed']}"
    )
    print(f"node_count={audit_result['node_count']}")
    print(f"directed_edge_count={audit_result['directed_edge_count']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
