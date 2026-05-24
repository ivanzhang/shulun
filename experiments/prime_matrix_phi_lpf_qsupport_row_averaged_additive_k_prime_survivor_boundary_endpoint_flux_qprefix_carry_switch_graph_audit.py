#!/usr/bin/env python3
"""审计 q-prefix carry-letter word 的有向 switch graph。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_graph_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-graph-audit.json

上一层把每条相邻 prime-q 转移编码为有限字母

    L=(g,c),      L^+=(g,c,sign(A'-A)).

本层继续把连续两条转移之间的字母切换编码为有向图边

    L_i -> L_{i+1},       L_i^+ -> L_{i+1}^+.

该层关闭的是 finite switch graph 账本；它不证明 deterministic switching law、
trace/Kloosterman completion 或 reciprocal phase cancellation。
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, TypeVar


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit as qprefix_atom  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_dynamics_audit as carry_dynamics  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_letter_run_audit as letter_run  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_phase_normal_form_audit as phase_normal  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-switch-graph"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "the switch graph is not yet a trace-function family over a complete summation box",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "high-branch switch graph data does not by itself create Kloosterman inverse variables",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "switch graph paths remain one-dimensional prime-q words rather than balanced Type-II rectangles",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman input remains candidate only after switch paths are completed into admissible fractions",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "prime existence in short intervals does not estimate carry-letter switch graph phases",
    },
]

T = TypeVar("T")


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


def raw_switch_string(edge: tuple[tuple[int, int], tuple[int, int]]) -> str:
    """序列化 raw switch edge。"""
    left, right = edge
    return f"{letter_run.raw_letter_string(left)} -> {letter_run.raw_letter_string(right)}"


def signed_switch_string(edge: tuple[tuple[int, int, str], tuple[int, int, str]]) -> str:
    """序列化 signed switch edge。"""
    left, right = edge
    return f"{letter_run.signed_letter_string(left)} -> {letter_run.signed_letter_string(right)}"


def numeric_rows(counts: Counter[int], key_name: str, count_name: str = "count") -> list[dict[str, Any]]:
    """把整数计数器转成数值排序表格。"""
    return [{key_name: key, count_name: counts[key]} for key in sorted(counts)]


def string_rows(counts: Counter[str], key_name: str, count_name: str = "count") -> list[dict[str, Any]]:
    """把字符串计数器转成稳定表格。"""
    return [{key_name: key, count_name: counts[key]} for key in sorted(counts)]


def top_raw_switch_rows(
    counts: Counter[tuple[tuple[int, int], tuple[int, int]]], limit: int = 20
) -> list[dict[str, Any]]:
    """输出最高频 raw switch edges。"""
    return [
        {"raw_switch": raw_switch_string(edge), "count": count}
        for edge, count in counts.most_common(limit)
    ]


def top_signed_switch_rows(
    counts: Counter[tuple[tuple[int, int, str], tuple[int, int, str]]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高频 signed switch edges。"""
    return [
        {"signed_switch": signed_switch_string(edge), "count": count}
        for edge, count in counts.most_common(limit)
    ]


def top_delta_rows(counts: Counter[tuple[int, int]], limit: int = 20) -> list[dict[str, Any]]:
    """输出最高频 letter delta。"""
    return [
        {"delta_gap": key[0], "delta_carry": key[1], "count": count}
        for key, count in counts.most_common(limit)
    ]


def degree_rows(nodes: set[T], adjacency: dict[T, set[T]], key_name: str) -> list[dict[str, Any]]:
    """输出节点度数分布。"""
    counts = Counter(len(adjacency.get(node, set())) for node in nodes)
    return numeric_rows(counts, key_name, "node_count")


def weak_component_sizes(nodes: set[T], outgoing: dict[T, set[T]]) -> list[int]:
    """计算弱连通分量大小。"""
    undirected: dict[T, set[T]] = defaultdict(set)
    for node in nodes:
        undirected[node]
    for left, rights in outgoing.items():
        for right in rights:
            undirected[left].add(right)
            undirected[right].add(left)

    seen: set[T] = set()
    sizes: list[int] = []
    for node in nodes:
        if node in seen:
            continue
        stack = [node]
        seen.add(node)
        size = 0
        while stack:
            current = stack.pop()
            size += 1
            for nxt in undirected[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def strongly_connected_component_sizes(nodes: set[T], outgoing: dict[T, set[T]]) -> list[int]:
    """用 Tarjan 算法计算强连通分量大小。"""
    sys.setrecursionlimit(10000)
    index = 0
    stack: list[T] = []
    on_stack: set[T] = set()
    indices: dict[T, int] = {}
    lowlink: dict[T, int] = {}
    sizes: list[int] = []

    def visit(node: T) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for nxt in outgoing.get(node, set()):
            if nxt not in indices:
                visit(nxt)
                lowlink[node] = min(lowlink[node], lowlink[nxt])
            elif nxt in on_stack:
                lowlink[node] = min(lowlink[node], indices[nxt])

        if lowlink[node] == indices[node]:
            size = 0
            while True:
                item = stack.pop()
                on_stack.remove(item)
                size += 1
                if item == node:
                    break
            sizes.append(size)

    for node in nodes:
        if node not in indices:
            visit(node)
    return sorted(sizes, reverse=True)


def graph_summary(
    nodes: set[T],
    edge_counts: Counter[tuple[T, T]],
    outgoing: dict[T, set[T]],
    incoming: dict[T, set[T]],
) -> dict[str, Any]:
    """汇总 switch graph 的有限图结构。"""
    out_degrees = [len(outgoing.get(node, set())) for node in nodes]
    in_degrees = [len(incoming.get(node, set())) for node in nodes]
    weak_sizes = weak_component_sizes(nodes, outgoing)
    scc_sizes = strongly_connected_component_sizes(nodes, outgoing)
    return {
        "node_count": len(nodes),
        "directed_edge_type_count": len(edge_counts),
        "directed_edge_capacity": len(nodes) * len(nodes),
        "directed_edge_density": len(edge_counts) / (len(nodes) * len(nodes)),
        "zero_outdegree_node_count": sum(1 for degree in out_degrees if degree == 0),
        "zero_indegree_node_count": sum(1 for degree in in_degrees if degree == 0),
        "branching_outdegree_gt1_node_count": sum(1 for degree in out_degrees if degree > 1),
        "branching_indegree_gt1_node_count": sum(1 for degree in in_degrees if degree > 1),
        "outdegree_min": min(out_degrees),
        "outdegree_median": statistics.median(out_degrees),
        "outdegree_max": max(out_degrees),
        "indegree_min": min(in_degrees),
        "indegree_median": statistics.median(in_degrees),
        "indegree_max": max(in_degrees),
        "weak_component_count": len(weak_sizes),
        "weak_component_size_rows": numeric_rows(Counter(weak_sizes), "component_size", "component_count"),
        "largest_weak_component_size": weak_sizes[0],
        "strong_component_count": len(scc_sizes),
        "strong_component_size_rows": numeric_rows(Counter(scc_sizes), "component_size", "component_count"),
        "largest_strong_component_size": scc_sizes[0],
        "outdegree_rows": degree_rows(nodes, outgoing, "outdegree"),
        "indegree_rows": degree_rows(nodes, incoming, "indegree"),
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计有限 carry-letter switch graph。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-audit.json"
        ).read_text()
    )
    previous = previous_payload["finite_audit"]

    raw_nodes: set[tuple[int, int]] = set()
    signed_nodes: set[tuple[int, int, str]] = set()
    raw_switch_counts: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
    signed_switch_counts: Counter[
        tuple[tuple[int, int, str], tuple[int, int, str]]
    ] = Counter()
    raw_delta_counts: Counter[tuple[int, int]] = Counter()
    switch_class_counts: Counter[str] = Counter()
    sign_switch_counts: Counter[str] = Counter()
    strip_switch_counts: Counter[str] = Counter()
    raw_outgoing: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    raw_incoming: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    signed_outgoing: dict[tuple[int, int, str], set[tuple[int, int, str]]] = defaultdict(set)
    signed_incoming: dict[tuple[int, int, str], set[tuple[int, int, str]]] = defaultdict(set)

    totals: Counter[str] = Counter()
    per_atom_switch_counts: list[int] = []
    sample_switch_atoms: list[dict[str, Any]] = []

    for packet_index, packet in enumerate(packets):
        endpoint_profile = qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        endpoint_class = endpoint_profile["endpoint_flux_class"]
        q_values = phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))

        for m_value in m_values:
            atom_profile, transitions = carry_dynamics.atom_transition_profile(
                packet_index, packet, endpoint_class, m_value, q_values
            )
            totals["atom_count_total"] += 1
            if not transitions:
                totals["singleton_q_atom_count"] += 1
                continue

            raw_seq: list[tuple[int, int]] = []
            signed_seq: list[tuple[int, int, str]] = []
            for transition in transitions:
                raw_letter = (transition["q_gap"], transition["carry_delta_k"])
                signed_letter = (
                    transition["q_gap"],
                    transition["carry_delta_k"],
                    letter_run.sign_label(transition["A_step"]),
                )
                raw_seq.append(raw_letter)
                signed_seq.append(signed_letter)
                raw_nodes.add(raw_letter)
                signed_nodes.add(signed_letter)

            totals["multiq_atom_count"] += 1
            totals["successor_transition_count_total"] += len(transitions)
            switch_count = max(0, len(transitions) - 1)
            totals["adjacent_letter_pair_count_inside_atoms"] += switch_count
            per_atom_switch_counts.append(switch_count)
            strip_switch_counts[packet["strip"]] += switch_count

            for left, right, left_signed, right_signed in zip(
                raw_seq, raw_seq[1:], signed_seq, signed_seq[1:]
            ):
                raw_switch_counts[(left, right)] += 1
                signed_switch_counts[(left_signed, right_signed)] += 1
                raw_outgoing[left].add(right)
                raw_incoming[right].add(left)
                signed_outgoing[left_signed].add(right_signed)
                signed_incoming[right_signed].add(left_signed)
                delta = (right[0] - left[0], right[1] - left[1])
                raw_delta_counts[delta] += 1
                switch_class_counts["same_raw_letter" if left == right else "changed_raw_letter"] += 1
                switch_class_counts["same_gap" if left[0] == right[0] else "changed_gap"] += 1
                switch_class_counts["same_carry" if left[1] == right[1] else "changed_carry"] += 1
                sign_switch_counts[
                    "same_A_step_sign" if left_signed[2] == right_signed[2] else "changed_A_step_sign"
                ] += 1

            if len(sample_switch_atoms) < 16 and switch_count >= 30:
                sample_switch_atoms.append(
                    {
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "endpoint_flux_class": endpoint_class,
                        "m": m_value,
                        "q_start": atom_profile["q_start"],
                        "q_end": atom_profile["q_end"],
                        "transition_count": len(transitions),
                        "switch_count": switch_count,
                        "raw_switch_sample": [
                            raw_switch_string(edge)
                            for edge in zip(raw_seq, raw_seq[1:])
                        ][:8],
                        "signed_switch_sample": [
                            signed_switch_string(edge)
                            for edge in zip(signed_seq, signed_seq[1:])
                        ][:8],
                    }
                )

    expected_pairs = (
        previous["successor_transition_count_total"] - previous["multiq_atom_count"]
    )
    raw_summary = graph_summary(raw_nodes, raw_switch_counts, raw_outgoing, raw_incoming)
    signed_summary = graph_summary(
        signed_nodes, signed_switch_counts, signed_outgoing, signed_incoming
    )
    switch_graph_decomposition_closed = (
        totals["atom_count_total"] == previous["carry_letter_atom_count_total"]
        and totals["multiq_atom_count"] == previous["multiq_atom_count"]
        and totals["singleton_q_atom_count"] == previous["singleton_q_atom_count"]
        and totals["successor_transition_count_total"]
        == previous["successor_transition_count_total"]
        and totals["adjacent_letter_pair_count_inside_atoms"] == expected_pairs
        and sum(raw_switch_counts.values()) == expected_pairs
        and sum(signed_switch_counts.values()) == expected_pairs
        and raw_summary["node_count"] == previous["raw_carry_letter_alphabet_count"]
        and signed_summary["node_count"] == previous["signed_carry_letter_alphabet_count"]
    )

    return {
        "max_prime": max_prime,
        "previous_letter_run_decomposition_closed": previous[
            "letter_run_decomposition_closed"
        ],
        "carry_switch_atom_count_total": totals["atom_count_total"],
        "multiq_atom_count": totals["multiq_atom_count"],
        "singleton_q_atom_count": totals["singleton_q_atom_count"],
        "successor_transition_count_total": totals["successor_transition_count_total"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "expected_adjacent_letter_pair_count_inside_atoms": expected_pairs,
        "raw_switch_pair_count_total": sum(raw_switch_counts.values()),
        "signed_switch_pair_count_total": sum(signed_switch_counts.values()),
        "switch_graph_decomposition_closed": switch_graph_decomposition_closed,
        "per_atom_switch_count_median": statistics.median(per_atom_switch_counts),
        "per_atom_switch_count_max": max(per_atom_switch_counts),
        "raw_graph": raw_summary,
        "signed_graph": signed_summary,
        "raw_same_letter_pair_count": switch_class_counts["same_raw_letter"],
        "raw_changed_letter_pair_count": switch_class_counts["changed_raw_letter"],
        "same_gap_pair_count": switch_class_counts["same_gap"],
        "changed_gap_pair_count": switch_class_counts["changed_gap"],
        "same_carry_pair_count": switch_class_counts["same_carry"],
        "changed_carry_pair_count": switch_class_counts["changed_carry"],
        "same_A_step_sign_pair_count": sign_switch_counts["same_A_step_sign"],
        "changed_A_step_sign_pair_count": sign_switch_counts["changed_A_step_sign"],
        "raw_changed_letter_ratio": switch_class_counts["changed_raw_letter"] / expected_pairs,
        "changed_gap_ratio": switch_class_counts["changed_gap"] / expected_pairs,
        "changed_carry_ratio": switch_class_counts["changed_carry"] / expected_pairs,
        "changed_A_step_sign_ratio": sign_switch_counts["changed_A_step_sign"] / expected_pairs,
        "strip_switch_rows": [
            {"strip": strip, "switch_count": strip_switch_counts[strip]}
            for strip in sorted(strip_switch_counts)
        ],
        "top_raw_switch_rows": top_raw_switch_rows(raw_switch_counts),
        "top_signed_switch_rows": top_signed_switch_rows(signed_switch_counts),
        "top_raw_delta_rows": top_delta_rows(raw_delta_counts),
        "switch_class_rows": string_rows(switch_class_counts, "switch_class"),
        "sign_switch_rows": string_rows(sign_switch_counts, "sign_switch_class"),
        "sample_switch_atoms": sample_switch_atoms,
        "finite_switch_graph_closed": switch_graph_decomposition_closed,
        "deterministic_switching_law_closed": False,
        "low_branch_switch_graph_available": False,
        "finite_switch_graph_phase_saving_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_switch_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_graph_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_carry_letter_words_have_finite_switch_graph_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after finite letter/run decomposition, the next acyclic step is to expose the directed switch graph behind the high-frequency letter changes",
        "current_object": {
            "input": "117 raw letters, 256 signed letters, and 147799 adjacent letter pairs",
            "raw_switch": "L_i=(g_i,c_i) -> L_{i+1}=(g_{i+1},c_{i+1})",
            "signed_switch": "L_i^+ -> L_{i+1}^+ with A-step signs",
            "dominant_shape": "connected high-branch finite switch graph rather than deterministic low-branch law",
            "remaining": "switch-graph exponential-sum saving or completion to a trace/Kloosterman family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "CarryLetterRunLedgerImported",
                True,
                True,
                "The previous finite carry-letter and run decomposition is imported.",
                "none for import",
            ),
            gate(
                "FiniteCarrySwitchGraphLedger",
                finite_audit["finite_switch_graph_closed"],
                finite_audit["finite_switch_graph_closed"],
                "All adjacent letter pairs are encoded as raw and signed directed switch edges.",
                "none for current finite switch graph ledger",
            ),
            gate(
                "LowBranchOrDeterministicSwitchingLaw",
                False,
                False,
                "The observed graph has large branching: raw max outdegree 54 and signed max outdegree 100.",
                "a new analytic law is required; the graph is not deterministic",
            ),
            gate(
                "FiniteSwitchGraphPhaseSaving",
                False,
                False,
                "Prove cancellation for paths in the finite switch graph along prime q.",
                "new exponential-sum input or trace/Kloosterman completion required",
            ),
            gate(
                "NoLossQPrefixSwitchAtomAggregation",
                False,
                False,
                "Aggregate any switch-graph saving across all fixed-m atoms without losing the boundary gain.",
                "requires analytic aggregation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "switch edges are not yet trace functions over complete boxes",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "branching switch graph does not by itself expose inverse Kloosterman variables",
            "Pascadi_composite_Type_II": "switch paths remain one-dimensional and do not form balanced composite Type-II packets",
            "Wright_unbalanced_Kloosterman": "could apply only after switch paths are converted to admissible unbalanced fractions",
            "Li_short_interval_x_052": "prime existence in intervals does not estimate switch-graph reciprocal phases",
        },
        "latest_narrowest_mouth": [
            "FiniteSwitchGraphPathExponentialSumSaving",
            "AND TraceKloostermanCompletionOfHighBranchCarrySwitchGraph",
            "AND NoLossAggregationAcross15439QPrefixSwitchAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "finite_switch_graph_closed": finite_audit["finite_switch_graph_closed"],
        "deterministic_switching_law_closed": False,
        "low_branch_switch_graph_available": False,
        "finite_switch_graph_phase_saving_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_switch_atom_aggregation_closed": False,
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
    audit = payload["finite_audit"]
    raw = audit["raw_graph"]
    signed = audit["signed_graph"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix carry switch graph 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"raw_switch={current['raw_switch']}",
        f"signed_switch={current['signed_switch']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. switch graph 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"carry_switch_atom_count_total={audit['carry_switch_atom_count_total']}",
        f"multiq_atom_count={audit['multiq_atom_count']}",
        f"singleton_q_atom_count={audit['singleton_q_atom_count']}",
        f"successor_transition_count_total={audit['successor_transition_count_total']}",
        f"adjacent_letter_pair_count_inside_atoms={audit['adjacent_letter_pair_count_inside_atoms']}",
        f"raw_switch_pair_count_total={audit['raw_switch_pair_count_total']}",
        f"signed_switch_pair_count_total={audit['signed_switch_pair_count_total']}",
        f"switch_graph_decomposition_closed={str(audit['switch_graph_decomposition_closed']).lower()}",
        f"per_atom_switch_count_median/max={audit['per_atom_switch_count_median']}/{audit['per_atom_switch_count_max']}",
        f"raw_graph_nodes/edges/density={raw['node_count']}/{raw['directed_edge_type_count']}/{raw['directed_edge_density']}",
        f"signed_graph_nodes/edges/density={signed['node_count']}/{signed['directed_edge_type_count']}/{signed['directed_edge_density']}",
        f"raw_outdegree_min/median/max={raw['outdegree_min']}/{raw['outdegree_median']}/{raw['outdegree_max']}",
        f"signed_outdegree_min/median/max={signed['outdegree_min']}/{signed['outdegree_median']}/{signed['outdegree_max']}",
        f"raw_largest_weak/scc={raw['largest_weak_component_size']}/{raw['largest_strong_component_size']}",
        f"signed_largest_weak/scc={signed['largest_weak_component_size']}/{signed['largest_strong_component_size']}",
        f"raw_changed_letter_pair_count/ratio={audit['raw_changed_letter_pair_count']}/{audit['raw_changed_letter_ratio']}",
        f"changed_gap_pair_count/ratio={audit['changed_gap_pair_count']}/{audit['changed_gap_ratio']}",
        f"changed_carry_pair_count/ratio={audit['changed_carry_pair_count']}/{audit['changed_carry_ratio']}",
        f"changed_A_step_sign_pair_count/ratio={audit['changed_A_step_sign_pair_count']}/{audit['changed_A_step_sign_ratio']}",
        f"deterministic_switching_law_closed={str(audit['deterministic_switching_law_closed']).lower()}",
        f"finite_switch_graph_phase_saving_closed={str(audit['finite_switch_graph_phase_saving_closed']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "最高频 raw switch edges：",
        "",
        *markdown_table(audit["top_raw_switch_rows"], ["raw_switch", "count"]),
        "",
        "最高频 signed switch edges：",
        "",
        *markdown_table(audit["top_signed_switch_rows"], ["signed_switch", "count"]),
        "",
        "最高频 raw delta：",
        "",
        *markdown_table(audit["top_raw_delta_rows"], ["delta_gap", "delta_carry", "count"]),
        "",
        "switch class 分桶：",
        "",
        *markdown_table(audit["switch_class_rows"], ["switch_class", "count"]),
        "",
        "A-step sign switch 分桶：",
        "",
        *markdown_table(audit["sign_switch_rows"], ["sign_switch_class", "count"]),
        "",
        "strip switch 分桶：",
        "",
        *markdown_table(audit["strip_switch_rows"], ["strip", "switch_count"]),
        "",
        "raw outdegree 分布：",
        "",
        *markdown_table(raw["outdegree_rows"], ["outdegree", "node_count"]),
        "",
        "signed outdegree 分布：",
        "",
        *markdown_table(signed["outdegree_rows"], ["outdegree", "node_count"]),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(
            payload["closed_gates"],
            ["gate", "closed", "proved", "meaning", "remaining"],
        ),
        "",
        "## 4. 外部 theorem 影响",
        "",
        *markdown_table(payload["external_sources_consulted"], ["key", "url", "role"]),
        "",
        "```text",
        *[
            f"{key}={value}"
            for key, value in payload["external_theorem_implication"].items()
        ],
        "```",
        "",
        "结论：carry-letter word 的相邻切换已经被压成有限有向图。",
        "但 raw/signed 图具有高分支节点，且大强连通块占据主要字母质量；",
        "因此本层没有给出 deterministic switching law，也没有给出相位节省。",
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
        f"finite_switch_graph_closed={str(payload['finite_switch_graph_closed']).lower()}",
        f"deterministic_switching_law_closed={str(payload['deterministic_switching_law_closed']).lower()}",
        f"low_branch_switch_graph_available={str(payload['low_branch_switch_graph_available']).lower()}",
        f"finite_switch_graph_phase_saving_closed={str(payload['finite_switch_graph_phase_saving_closed']).lower()}",
        f"completion_to_external_trace_or_kloosterman_closed={str(payload['completion_to_external_trace_or_kloosterman_closed']).lower()}",
        f"no_loss_qprefix_switch_atom_aggregation_closed={str(payload['no_loss_qprefix_switch_atom_aggregation_closed']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    payload = build_payload()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload))
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"finite_switch_graph_closed={payload['finite_switch_graph_closed']}")
    print(f"deterministic_switching_law_closed={payload['deterministic_switching_law_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
