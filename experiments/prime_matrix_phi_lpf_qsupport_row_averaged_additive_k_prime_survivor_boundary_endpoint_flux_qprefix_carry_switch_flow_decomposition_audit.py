#!/usr/bin/env python3
"""审计 q-prefix carry switch path 的 loop-erased cycle/residual 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-audit.json

上一层把 finite carry-letter word 的相邻切换写成 directed switch graph。
本层继续对每个 fixed-m atom 的 switch path 做确定性 loop erasure：

    repeated active letter => peel one directed cycle,
    remaining active stack => endpoint residual path.

该层关闭的是 cycle-flow core 与 endpoint residual 的有限账本；它仍不证明
cycle packet 的相位相消、residual endpoint path 的求和或 completed
trace/Kloosterman family。
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any, TypeVar


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
    "boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-graph-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-audit.json",
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
        "role": "cycle packets still need conversion to trace functions before trace bilinear estimates apply",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "cycle-flow packets are not yet inverse-variable Kloosterman sums modulo q",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "loop-erased cycles remain one-dimensional path packets, not balanced composite Type-II rectangles",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman input remains candidate only after cycle/residual paths become admissible fractions",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short interval prime existence does not estimate loop-erased switch-cycle phases",
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


def raw_letter_string(letter: tuple[int, int]) -> str:
    """序列化 raw letter。"""
    return letter_run.raw_letter_string(letter)


def signed_letter_string(letter: tuple[int, int, str]) -> str:
    """序列化 signed letter。"""
    return letter_run.signed_letter_string(letter)


def numeric_rows(counts: Counter[int], key_name: str, count_name: str = "count") -> list[dict[str, Any]]:
    """把整数计数器转成数值排序表格。"""
    return [{key_name: key, count_name: counts[key]} for key in sorted(counts)]


def endpoint_rows(
    counts: Counter[tuple[T, T]], formatter: Any, limit: int = 20
) -> list[dict[str, Any]]:
    """输出最高频 residual endpoint pair。"""
    return [
        {"start": formatter(start), "end": formatter(end), "count": count}
        for (start, end), count in counts.most_common(limit)
    ]


def loop_erased_cycle_decomposition(seq: list[T]) -> tuple[list[int], int, list[T]]:
    """把一个节点路径确定性分解为 loop cycles 与 residual simple path。

    输入是 letter 节点序列，边数为 len(seq)-1。遇到当前 active stack 中已经
    出现的节点时，剥离从旧位置到当前位置的闭合有向 cycle。
    """
    stack: list[T] = []
    positions: dict[T, int] = {}
    cycle_lengths: list[int] = []

    for node in seq:
        if not stack:
            stack.append(node)
            positions[node] = 0
            continue

        if node in positions:
            start = positions[node]
            cycle_lengths.append(len(stack) - start)
            for old in stack[start + 1 :]:
                positions.pop(old, None)
            stack = stack[: start + 1]
        else:
            stack.append(node)
            positions[node] = len(stack) - 1

    return cycle_lengths, max(0, len(stack) - 1), stack


def cycle_summary(prefix: str, cycle_lengths: list[int], residual_lengths: list[int]) -> dict[str, Any]:
    """汇总 loop-erased cycle/residual 数据。"""
    cycle_edge_mass = sum(cycle_lengths)
    residual_edge_mass = sum(residual_lengths)
    total = cycle_edge_mass + residual_edge_mass
    return {
        f"{prefix}_cycle_packet_count": len(cycle_lengths),
        f"{prefix}_cycle_edge_mass": cycle_edge_mass,
        f"{prefix}_residual_edge_mass": residual_edge_mass,
        f"{prefix}_cycle_plus_residual_edge_mass": total,
        f"{prefix}_cycle_edge_ratio": cycle_edge_mass / total,
        f"{prefix}_residual_edge_ratio": residual_edge_mass / total,
        f"{prefix}_cycle_length_min": min(cycle_lengths),
        f"{prefix}_cycle_length_median": statistics.median(cycle_lengths),
        f"{prefix}_cycle_length_max": max(cycle_lengths),
        f"{prefix}_residual_length_min": min(residual_lengths),
        f"{prefix}_residual_length_median": statistics.median(residual_lengths),
        f"{prefix}_residual_length_max": max(residual_lengths),
        f"{prefix}_zero_residual_atom_count": sum(1 for item in residual_lengths if item == 0),
        f"{prefix}_cycle_length_rows": numeric_rows(
            Counter(cycle_lengths), "cycle_length", "cycle_count"
        ),
        f"{prefix}_residual_length_rows": numeric_rows(
            Counter(residual_lengths), "residual_length", "atom_count"
        ),
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 finite switch path 的 loop-erased flow decomposition。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-graph-audit.json"
        ).read_text()
    )
    previous = previous_payload["finite_audit"]

    raw_cycle_lengths: list[int] = []
    signed_cycle_lengths: list[int] = []
    raw_residual_lengths: list[int] = []
    signed_residual_lengths: list[int] = []
    raw_residual_endpoint_counts: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
    signed_residual_endpoint_counts: Counter[
        tuple[tuple[int, int, str], tuple[int, int, str]]
    ] = Counter()
    strip_edge_counts: Counter[str] = Counter()
    strip_raw_cycle_edge_counts: Counter[str] = Counter()
    strip_raw_residual_edge_counts: Counter[str] = Counter()
    strip_signed_cycle_edge_counts: Counter[str] = Counter()
    strip_signed_residual_edge_counts: Counter[str] = Counter()

    totals: Counter[str] = Counter()
    sample_cycle_atoms: list[dict[str, Any]] = []

    for packet_index, packet in enumerate(packets):
        endpoint_profile = qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        q_values = phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))

        for m_value in m_values:
            _, transitions = carry_dynamics.atom_transition_profile(
                packet_index, packet, endpoint_profile["endpoint_flux_class"], m_value, q_values
            )
            totals["atom_count_total"] += 1
            if len(transitions) < 2:
                totals["non_switch_atom_count"] += 1
                continue

            raw_seq: list[tuple[int, int]] = []
            signed_seq: list[tuple[int, int, str]] = []
            for transition in transitions:
                raw_seq.append((transition["q_gap"], transition["carry_delta_k"]))
                signed_seq.append(
                    (
                        transition["q_gap"],
                        transition["carry_delta_k"],
                        letter_run.sign_label(transition["A_step"]),
                    )
                )

            switch_count = len(raw_seq) - 1
            totals["switch_atom_count"] += 1
            totals["adjacent_letter_pair_count_inside_atoms"] += switch_count
            strip_edge_counts[packet["strip"]] += switch_count

            raw_cycles, raw_residual, raw_stack = loop_erased_cycle_decomposition(raw_seq)
            signed_cycles, signed_residual, signed_stack = loop_erased_cycle_decomposition(
                signed_seq
            )
            raw_cycle_lengths.extend(raw_cycles)
            signed_cycle_lengths.extend(signed_cycles)
            raw_residual_lengths.append(raw_residual)
            signed_residual_lengths.append(signed_residual)
            strip_raw_cycle_edge_counts[packet["strip"]] += sum(raw_cycles)
            strip_raw_residual_edge_counts[packet["strip"]] += raw_residual
            strip_signed_cycle_edge_counts[packet["strip"]] += sum(signed_cycles)
            strip_signed_residual_edge_counts[packet["strip"]] += signed_residual

            if raw_stack:
                raw_residual_endpoint_counts[(raw_stack[0], raw_stack[-1])] += 1
            if signed_stack:
                signed_residual_endpoint_counts[(signed_stack[0], signed_stack[-1])] += 1

            if len(sample_cycle_atoms) < 16 and (sum(raw_cycles) > 0 or sum(signed_cycles) > 0):
                sample_cycle_atoms.append(
                    {
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "endpoint_flux_class": endpoint_profile["endpoint_flux_class"],
                        "m": m_value,
                        "switch_count": switch_count,
                        "raw_cycle_edge_mass": sum(raw_cycles),
                        "raw_residual_length": raw_residual,
                        "signed_cycle_edge_mass": sum(signed_cycles),
                        "signed_residual_length": signed_residual,
                        "raw_cycle_length_sample": raw_cycles[:8],
                        "signed_cycle_length_sample": signed_cycles[:8],
                        "raw_letter_sample": [raw_letter_string(item) for item in raw_seq[:8]],
                    }
                )

    raw_summary = cycle_summary("raw", raw_cycle_lengths, raw_residual_lengths)
    signed_summary = cycle_summary("signed", signed_cycle_lengths, signed_residual_lengths)
    loop_erased_flow_decomposition_closed = (
        totals["atom_count_total"] == previous["carry_switch_atom_count_total"]
        and totals["switch_atom_count"] + totals["non_switch_atom_count"]
        == previous["carry_switch_atom_count_total"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and raw_summary["raw_cycle_plus_residual_edge_mass"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and signed_summary["signed_cycle_plus_residual_edge_mass"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
    )

    return {
        "max_prime": max_prime,
        "previous_switch_graph_decomposition_closed": previous[
            "switch_graph_decomposition_closed"
        ],
        "flow_decomposition_atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "loop_erased_flow_decomposition_closed": loop_erased_flow_decomposition_closed,
        **raw_summary,
        **signed_summary,
        "strip_flow_rows": [
            {
                "strip": strip,
                "switch_edge_count": strip_edge_counts[strip],
                "raw_cycle_edge_mass": strip_raw_cycle_edge_counts[strip],
                "raw_residual_edge_mass": strip_raw_residual_edge_counts[strip],
                "signed_cycle_edge_mass": strip_signed_cycle_edge_counts[strip],
                "signed_residual_edge_mass": strip_signed_residual_edge_counts[strip],
            }
            for strip in sorted(strip_edge_counts)
        ],
        "top_raw_residual_endpoint_rows": endpoint_rows(
            raw_residual_endpoint_counts, raw_letter_string
        ),
        "top_signed_residual_endpoint_rows": endpoint_rows(
            signed_residual_endpoint_counts, signed_letter_string
        ),
        "sample_cycle_atoms": sample_cycle_atoms,
        "loop_erased_cycle_flow_core_closed": loop_erased_flow_decomposition_closed,
        "cycle_packet_phase_saving_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_flow_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_switch_paths_have_loop_erased_cycle_flow_core_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after high-branch switch graph, the next acyclic step is to separate recurrent cycle mass from endpoint residual paths",
        "current_object": {
            "input": "147799 adjacent carry-letter switch edges across 13355 switch atoms",
            "operation": "deterministic loop erasure of each raw and signed switch path",
            "dominant_shape": "majority cycle-flow core plus short endpoint residual paths",
            "remaining": "phase saving on cycle packets, residual endpoint summation, and trace/Kloosterman completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "FiniteCarrySwitchGraphImported",
                True,
                True,
                "The previous finite switch graph ledger is imported.",
                "none for import",
            ),
            gate(
                "LoopErasedCycleFlowDecomposition",
                finite_audit["loop_erased_flow_decomposition_closed"],
                finite_audit["loop_erased_flow_decomposition_closed"],
                "Every switch path is split into peeled cycles and one endpoint residual path.",
                "none for current deterministic ledger",
            ),
            gate(
                "CyclePacketPhaseSaving",
                False,
                False,
                "Prove cancellation for the peeled cycle packets.",
                "requires new exponential-sum or trace/Kloosterman input",
            ),
            gate(
                "ResidualEndpointPathSummation",
                False,
                False,
                "Control the loop-erased endpoint residual paths without losing the boundary gain.",
                "requires residual endpoint summation or analytic compression",
            ),
            gate(
                "NoLossQPrefixFlowAtomAggregation",
                False,
                False,
                "Aggregate cycle and residual estimates across all fixed-m atoms.",
                "requires no-loss aggregation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "cycle packets still need trace-function completion",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "loop cycles are not yet Kloosterman inverse families",
            "Pascadi_composite_Type_II": "cycle/residual paths remain one-dimensional rather than Type-II boxes",
            "Wright_unbalanced_Kloosterman": "candidate only after paths are converted to admissible unbalanced fractions",
            "Li_short_interval_x_052": "prime existence does not estimate cycle/residual reciprocal phases",
        },
        "latest_narrowest_mouth": [
            "CyclePacketPhaseSavingForLoopErasedCarrySwitchCore",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND TraceKloostermanCompletionOfCycleAndResidualPackets",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "loop_erased_cycle_flow_core_closed": finite_audit[
            "loop_erased_cycle_flow_core_closed"
        ],
        "cycle_packet_phase_saving_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_flow_atom_aggregation_closed": False,
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
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix carry switch flow decomposition 审计",
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
        "## 2. loop-erased cycle/residual 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"flow_decomposition_atom_count_total={audit['flow_decomposition_atom_count_total']}",
        f"switch_atom_count={audit['switch_atom_count']}",
        f"non_switch_atom_count={audit['non_switch_atom_count']}",
        f"adjacent_letter_pair_count_inside_atoms={audit['adjacent_letter_pair_count_inside_atoms']}",
        f"loop_erased_flow_decomposition_closed={str(audit['loop_erased_flow_decomposition_closed']).lower()}",
        f"raw_cycle_packet_count={audit['raw_cycle_packet_count']}",
        f"raw_cycle_edge_mass={audit['raw_cycle_edge_mass']}",
        f"raw_residual_edge_mass={audit['raw_residual_edge_mass']}",
        f"raw_cycle_edge_ratio={audit['raw_cycle_edge_ratio']}",
        f"raw_cycle_length_min/median/max={audit['raw_cycle_length_min']}/{audit['raw_cycle_length_median']}/{audit['raw_cycle_length_max']}",
        f"raw_residual_length_min/median/max={audit['raw_residual_length_min']}/{audit['raw_residual_length_median']}/{audit['raw_residual_length_max']}",
        f"signed_cycle_packet_count={audit['signed_cycle_packet_count']}",
        f"signed_cycle_edge_mass={audit['signed_cycle_edge_mass']}",
        f"signed_residual_edge_mass={audit['signed_residual_edge_mass']}",
        f"signed_cycle_edge_ratio={audit['signed_cycle_edge_ratio']}",
        f"signed_cycle_length_min/median/max={audit['signed_cycle_length_min']}/{audit['signed_cycle_length_median']}/{audit['signed_cycle_length_max']}",
        f"signed_residual_length_min/median/max={audit['signed_residual_length_min']}/{audit['signed_residual_length_median']}/{audit['signed_residual_length_max']}",
        f"cycle_packet_phase_saving_closed={str(audit['cycle_packet_phase_saving_closed']).lower()}",
        f"residual_endpoint_path_summation_closed={str(audit['residual_endpoint_path_summation_closed']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "raw cycle length 分布：",
        "",
        *markdown_table(audit["raw_cycle_length_rows"], ["cycle_length", "cycle_count"]),
        "",
        "raw residual length 分布：",
        "",
        *markdown_table(audit["raw_residual_length_rows"], ["residual_length", "atom_count"]),
        "",
        "signed cycle length 分布：",
        "",
        *markdown_table(audit["signed_cycle_length_rows"], ["cycle_length", "cycle_count"]),
        "",
        "signed residual length 分布：",
        "",
        *markdown_table(
            audit["signed_residual_length_rows"], ["residual_length", "atom_count"]
        ),
        "",
        "strip flow 分桶：",
        "",
        *markdown_table(
            audit["strip_flow_rows"],
            [
                "strip",
                "switch_edge_count",
                "raw_cycle_edge_mass",
                "raw_residual_edge_mass",
                "signed_cycle_edge_mass",
                "signed_residual_edge_mass",
            ],
        ),
        "",
        "最高频 raw residual endpoint pairs：",
        "",
        *markdown_table(audit["top_raw_residual_endpoint_rows"], ["start", "end", "count"]),
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
        "结论：high-branch switch paths 已经被确定性分成 loop-erased cycle core",
        "与 endpoint residual path。该层是结构分解，不是相位相消。",
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
        f"loop_erased_cycle_flow_core_closed={str(payload['loop_erased_cycle_flow_core_closed']).lower()}",
        f"cycle_packet_phase_saving_closed={str(payload['cycle_packet_phase_saving_closed']).lower()}",
        f"residual_endpoint_path_summation_closed={str(payload['residual_endpoint_path_summation_closed']).lower()}",
        f"completion_to_external_trace_or_kloosterman_closed={str(payload['completion_to_external_trace_or_kloosterman_closed']).lower()}",
        f"no_loss_qprefix_flow_atom_aggregation_closed={str(payload['no_loss_qprefix_flow_atom_aggregation_closed']).lower()}",
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
    print(
        "loop_erased_cycle_flow_core_closed="
        f"{payload['loop_erased_cycle_flow_core_closed']}"
    )
    print(f"cycle_packet_phase_saving_closed={payload['cycle_packet_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
