#!/usr/bin/env python3
"""审计 q-prefix carry loop-erased cycle packet 的有限签名分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-audit.json

上一层已经把 high-branch switch paths 拆成 loop-erased cycle core 与
endpoint residual paths。本层只继续把 cycle core 做非循环下钻：

    directed cycle packet => canonical rotation signature
    signature => length/load/sign shape buckets

该层关闭的是有限 cycle-signature/template 账本；它不证明 weighted
cycle-signature phase saving，也不证明外部 trace/Kloosterman completion。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-audit.json",
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
        "role": "cycle signatures still need conversion to trace-function weights before bilinear trace estimates apply",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "cycle signatures are not yet inverse-variable Kloosterman families modulo q",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "signature buckets remain path templates rather than balanced composite Type-II boxes",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate only after signatures are completed to admissible unbalanced fractions",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short interval prime existence does not estimate weighted cycle-signature phases",
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


def loop_erased_cycle_packets(seq: list[T]) -> tuple[list[list[T]], list[T]]:
    """返回确定性 loop erasure 剥离出的有向 cycle packets 与 residual stack。"""
    stack: list[T] = []
    positions: dict[T, int] = {}
    cycles: list[list[T]] = []

    for node in seq:
        if not stack:
            stack.append(node)
            positions[node] = 0
            continue

        if node in positions:
            start = positions[node]
            cycles.append(stack[start:])
            for old in stack[start + 1 :]:
                positions.pop(old, None)
            stack = stack[: start + 1]
        else:
            stack.append(node)
            positions[node] = len(stack) - 1

    return cycles, stack


def canonical_rotation(tokens: list[str]) -> tuple[str, ...]:
    """把有向 cycle 的起点自由度归一化；方向不反转。"""
    if not tokens:
        return ()
    return min(tuple(tokens[i:] + tokens[:i]) for i in range(len(tokens)))


def raw_template(cycle: list[tuple[int, int]]) -> str:
    """raw cycle 的规范旋转模板。"""
    return " -> ".join(canonical_rotation([flow.raw_letter_string(item) for item in cycle]))


def signed_template(cycle: list[tuple[int, int, str]]) -> str:
    """signed cycle 的规范旋转模板。"""
    return " -> ".join(canonical_rotation([flow.signed_letter_string(item) for item in cycle]))


def raw_shape(cycle: list[tuple[int, int]]) -> tuple[int, int, int, int, int, int, int]:
    """raw cycle 的长度与 gap/carry 载荷形状。"""
    q_gaps = [item[0] for item in cycle]
    carries = [item[1] for item in cycle]
    return (
        len(cycle),
        sum(q_gaps),
        sum(carries),
        min(q_gaps),
        max(q_gaps),
        min(carries),
        max(carries),
    )


def signed_shape(cycle: list[tuple[int, int, str]]) -> tuple[int, int, int, int, int, int, int, int, int, int]:
    """signed cycle 的长度、gap/carry 载荷与 A 符号形状。"""
    base = raw_shape([(item[0], item[1]) for item in cycle])
    signs = Counter(item[2] for item in cycle)
    return (
        *base,
        signs["negative"],
        signs["zero"],
        signs["positive"],
    )


def shape_string(shape: tuple[int, ...], signed: bool) -> str:
    """形状签名转成稳定字符串。"""
    head = (
        f"len={shape[0]},sum_g={shape[1]},sum_c={shape[2]},"
        f"g=[{shape[3]},{shape[4]}],c=[{shape[5]},{shape[6]}]"
    )
    if not signed:
        return head
    return f"{head},A(-,0,+)=({shape[7]},{shape[8]},{shape[9]})"


def edge_delta_net_is_zero_raw(cycle: list[tuple[int, int]]) -> bool:
    """检查沿 cycle 边差分后的 gap/carry 净位移为零。"""
    if not cycle:
        return True
    net_gap = 0
    net_carry = 0
    for index, item in enumerate(cycle):
        nxt = cycle[(index + 1) % len(cycle)]
        net_gap += nxt[0] - item[0]
        net_carry += nxt[1] - item[1]
    return net_gap == 0 and net_carry == 0


def signature_rows(
    template_counts: Counter[str],
    template_edge_mass: Counter[str],
    template_shapes: dict[str, str],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量 cycle templates。"""
    rows = []
    order = sorted(
        template_counts,
        key=lambda key: (-template_edge_mass[key], -template_counts[key], key),
    )
    for key in order[:limit]:
        rows.append(
            {
                "template": key,
                "cycle_count": template_counts[key],
                "edge_mass": template_edge_mass[key],
                "shape": template_shapes[key],
            }
        )
    return rows


def shape_rows(shape_counts: Counter[tuple[int, ...]], shape_edge_mass: Counter[tuple[int, ...]], signed: bool, limit: int = 20) -> list[dict[str, Any]]:
    """输出最高质量 length/load/sign shape buckets。"""
    rows = []
    order = sorted(shape_counts, key=lambda key: (-shape_edge_mass[key], -shape_counts[key], key))
    for key in order[:limit]:
        rows.append(
            {
                "shape": shape_string(key, signed),
                "cycle_count": shape_counts[key],
                "edge_mass": shape_edge_mass[key],
            }
        )
    return rows


def concentration(template_edge_mass: Counter[str], total_edge_mass: int, top: int) -> float:
    """计算 top-N 模板覆盖的边质量比例。"""
    mass = sum(value for _, value in template_edge_mass.most_common(top))
    return mass / total_edge_mass if total_edge_mass else 0.0


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 loop-erased cycle core 的有限签名分桶。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-audit.json"
        ).read_text()
    )
    previous = previous_payload["finite_audit"]

    totals: Counter[str] = Counter()
    raw_cycle_lengths: list[int] = []
    signed_cycle_lengths: list[int] = []
    raw_template_counts: Counter[str] = Counter()
    signed_template_counts: Counter[str] = Counter()
    raw_template_edge_mass: Counter[str] = Counter()
    signed_template_edge_mass: Counter[str] = Counter()
    raw_template_shapes: dict[str, str] = {}
    signed_template_shapes: dict[str, str] = {}
    raw_shape_counts: Counter[tuple[int, ...]] = Counter()
    signed_shape_counts: Counter[tuple[int, ...]] = Counter()
    raw_shape_edge_mass: Counter[tuple[int, ...]] = Counter()
    signed_shape_edge_mass: Counter[tuple[int, ...]] = Counter()
    strip_raw_cycle_edge_mass: Counter[str] = Counter()
    strip_signed_cycle_edge_mass: Counter[str] = Counter()
    sample_signature_atoms: list[dict[str, Any]] = []

    for packet_index, packet in enumerate(packets):
        endpoint_profile = flow.qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        q_values = flow.phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(flow.qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))

        for m_value in m_values:
            _, transitions = flow.carry_dynamics.atom_transition_profile(
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
                        flow.letter_run.sign_label(transition["A_step"]),
                    )
                )

            totals["switch_atom_count"] += 1
            totals["adjacent_letter_pair_count_inside_atoms"] += len(raw_seq) - 1

            raw_cycles, raw_stack = loop_erased_cycle_packets(raw_seq)
            signed_cycles, signed_stack = loop_erased_cycle_packets(signed_seq)
            totals["raw_residual_edge_mass"] += max(0, len(raw_stack) - 1)
            totals["signed_residual_edge_mass"] += max(0, len(signed_stack) - 1)

            for cycle in raw_cycles:
                length = len(cycle)
                template = raw_template(cycle)
                shape = raw_shape(cycle)
                raw_cycle_lengths.append(length)
                raw_template_counts[template] += 1
                raw_template_edge_mass[template] += length
                raw_template_shapes[template] = shape_string(shape, False)
                raw_shape_counts[shape] += 1
                raw_shape_edge_mass[shape] += length
                strip_raw_cycle_edge_mass[packet["strip"]] += length
                totals["raw_cycle_edge_mass"] += length
                if length == 1:
                    totals["raw_self_loop_cycle_count"] += 1
                    totals["raw_self_loop_edge_mass"] += length
                if len({item[0] for item in cycle}) > 1:
                    totals["raw_q_gap_variable_cycle_count"] += 1
                if len({item[1] for item in cycle}) > 1:
                    totals["raw_carry_variable_cycle_count"] += 1
                if not edge_delta_net_is_zero_raw(cycle):
                    totals["raw_edge_delta_net_nonzero_count"] += 1

            for cycle in signed_cycles:
                length = len(cycle)
                template = signed_template(cycle)
                shape = signed_shape(cycle)
                signed_cycle_lengths.append(length)
                signed_template_counts[template] += 1
                signed_template_edge_mass[template] += length
                signed_template_shapes[template] = shape_string(shape, True)
                signed_shape_counts[shape] += 1
                signed_shape_edge_mass[shape] += length
                strip_signed_cycle_edge_mass[packet["strip"]] += length
                totals["signed_cycle_edge_mass"] += length
                if length == 1:
                    totals["signed_self_loop_cycle_count"] += 1
                    totals["signed_self_loop_edge_mass"] += length
                if len({item[0] for item in cycle}) > 1:
                    totals["signed_q_gap_variable_cycle_count"] += 1
                if len({item[1] for item in cycle}) > 1:
                    totals["signed_carry_variable_cycle_count"] += 1
                if len({item[2] for item in cycle}) > 1:
                    totals["signed_A_sign_variable_cycle_count"] += 1
                if not edge_delta_net_is_zero_raw([(item[0], item[1]) for item in cycle]):
                    totals["signed_edge_delta_net_nonzero_count"] += 1

            if len(sample_signature_atoms) < 16 and (raw_cycles or signed_cycles):
                sample_signature_atoms.append(
                    {
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "endpoint_flux_class": endpoint_profile["endpoint_flux_class"],
                        "m": m_value,
                        "raw_cycle_templates": [raw_template(cycle) for cycle in raw_cycles[:3]],
                        "signed_cycle_templates": [
                            signed_template(cycle) for cycle in signed_cycles[:3]
                        ],
                    }
                )

    raw_cycle_edge_mass = totals["raw_cycle_edge_mass"]
    signed_cycle_edge_mass = totals["signed_cycle_edge_mass"]
    raw_template_max_edge_mass = max(raw_template_edge_mass.values())
    signed_template_max_edge_mass = max(signed_template_edge_mass.values())
    raw_shape_max_edge_mass = max(raw_shape_edge_mass.values())
    signed_shape_max_edge_mass = max(signed_shape_edge_mass.values())

    signature_decomposition_closed = (
        totals["atom_count_total"] == previous["flow_decomposition_atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and len(raw_cycle_lengths) == previous["raw_cycle_packet_count"]
        and len(signed_cycle_lengths) == previous["signed_cycle_packet_count"]
        and raw_cycle_edge_mass == previous["raw_cycle_edge_mass"]
        and signed_cycle_edge_mass == previous["signed_cycle_edge_mass"]
        and totals["raw_residual_edge_mass"] == previous["raw_residual_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and totals["raw_edge_delta_net_nonzero_count"] == 0
        and totals["signed_edge_delta_net_nonzero_count"] == 0
    )

    return {
        "max_prime": max_prime,
        "previous_loop_erased_flow_decomposition_closed": previous[
            "loop_erased_flow_decomposition_closed"
        ],
        "cycle_signature_decomposition_closed": signature_decomposition_closed,
        "cycle_signature_atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "raw_cycle_packet_count": len(raw_cycle_lengths),
        "raw_cycle_edge_mass": raw_cycle_edge_mass,
        "raw_residual_edge_mass": totals["raw_residual_edge_mass"],
        "raw_cycle_signature_count": len(raw_template_counts),
        "raw_cycle_shape_count": len(raw_shape_counts),
        "raw_cycle_length_min": min(raw_cycle_lengths),
        "raw_cycle_length_median": statistics.median(raw_cycle_lengths),
        "raw_cycle_length_max": max(raw_cycle_lengths),
        "raw_self_loop_cycle_count": totals["raw_self_loop_cycle_count"],
        "raw_self_loop_edge_mass": totals["raw_self_loop_edge_mass"],
        "raw_q_gap_variable_cycle_count": totals["raw_q_gap_variable_cycle_count"],
        "raw_carry_variable_cycle_count": totals["raw_carry_variable_cycle_count"],
        "raw_template_max_edge_mass": raw_template_max_edge_mass,
        "raw_template_max_edge_ratio": raw_template_max_edge_mass / raw_cycle_edge_mass,
        "raw_template_top20_edge_ratio": concentration(
            raw_template_edge_mass, raw_cycle_edge_mass, 20
        ),
        "raw_template_top100_edge_ratio": concentration(
            raw_template_edge_mass, raw_cycle_edge_mass, 100
        ),
        "raw_shape_max_edge_mass": raw_shape_max_edge_mass,
        "raw_shape_max_edge_ratio": raw_shape_max_edge_mass / raw_cycle_edge_mass,
        "signed_cycle_packet_count": len(signed_cycle_lengths),
        "signed_cycle_edge_mass": signed_cycle_edge_mass,
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "signed_cycle_signature_count": len(signed_template_counts),
        "signed_cycle_shape_count": len(signed_shape_counts),
        "signed_cycle_length_min": min(signed_cycle_lengths),
        "signed_cycle_length_median": statistics.median(signed_cycle_lengths),
        "signed_cycle_length_max": max(signed_cycle_lengths),
        "signed_self_loop_cycle_count": totals["signed_self_loop_cycle_count"],
        "signed_self_loop_edge_mass": totals["signed_self_loop_edge_mass"],
        "signed_q_gap_variable_cycle_count": totals["signed_q_gap_variable_cycle_count"],
        "signed_carry_variable_cycle_count": totals["signed_carry_variable_cycle_count"],
        "signed_A_sign_variable_cycle_count": totals["signed_A_sign_variable_cycle_count"],
        "signed_template_max_edge_mass": signed_template_max_edge_mass,
        "signed_template_max_edge_ratio": signed_template_max_edge_mass / signed_cycle_edge_mass,
        "signed_template_top20_edge_ratio": concentration(
            signed_template_edge_mass, signed_cycle_edge_mass, 20
        ),
        "signed_template_top100_edge_ratio": concentration(
            signed_template_edge_mass, signed_cycle_edge_mass, 100
        ),
        "signed_shape_max_edge_mass": signed_shape_max_edge_mass,
        "signed_shape_max_edge_ratio": signed_shape_max_edge_mass / signed_cycle_edge_mass,
        "strip_cycle_signature_rows": [
            {
                "strip": strip,
                "raw_cycle_edge_mass": strip_raw_cycle_edge_mass[strip],
                "signed_cycle_edge_mass": strip_signed_cycle_edge_mass[strip],
            }
            for strip in sorted(set(strip_raw_cycle_edge_mass) | set(strip_signed_cycle_edge_mass))
        ],
        "top_raw_cycle_signature_rows": signature_rows(
            raw_template_counts, raw_template_edge_mass, raw_template_shapes
        ),
        "top_signed_cycle_signature_rows": signature_rows(
            signed_template_counts, signed_template_edge_mass, signed_template_shapes
        ),
        "top_raw_cycle_shape_rows": shape_rows(raw_shape_counts, raw_shape_edge_mass, False),
        "top_signed_cycle_shape_rows": shape_rows(
            signed_shape_counts, signed_shape_edge_mass, True
        ),
        "sample_signature_atoms": sample_signature_atoms,
        "cycle_signature_ledger_closed": signature_decomposition_closed,
        "cycle_signature_weighted_phase_saving_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_flow_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_cycle_core_has_finite_signature_ledger_weighted_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after loop-erased cycle-flow decomposition, the fastest non-cyclic drilldown is to expose the finite cycle template and load/sign buckets",
        "current_object": {
            "input": "loop-erased raw/signed cycle packets from 13355 switch atoms",
            "operation": "canonical rotation signature plus length/load/sign shape bucketing",
            "dominant_shape": "many short recurrent templates with no single template carrying enough mass for trivial cancellation",
            "remaining": "weighted phase saving by cycle signature, endpoint residual summation, and trace/Kloosterman completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "LoopErasedCycleFlowImported",
                finite_audit["previous_loop_erased_flow_decomposition_closed"],
                finite_audit["previous_loop_erased_flow_decomposition_closed"],
                "The previous cycle/residual decomposition ledger is imported.",
                "none for import",
            ),
            gate(
                "FiniteCycleSignatureLedger",
                finite_audit["cycle_signature_ledger_closed"],
                finite_audit["cycle_signature_ledger_closed"],
                "Every peeled cycle packet is assigned a canonical directed signature and a length/load/sign shape.",
                "none for current deterministic ledger",
            ),
            gate(
                "CycleSignatureWeightedPhaseSaving",
                False,
                False,
                "Prove cancellation after grouping by cycle signature and analytic weight.",
                "requires new exponential-sum or trace/Kloosterman input on the weighted buckets",
            ),
            gate(
                "ResidualEndpointPathSummation",
                False,
                False,
                "Control the endpoint residual paths from the previous flow ledger.",
                "requires residual endpoint summation without boundary loss",
            ),
            gate(
                "NoLossQPrefixFlowAtomAggregation",
                False,
                False,
                "Aggregate signature and residual estimates across all fixed-m atoms.",
                "requires no-loss aggregation discipline over 15439 atoms",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "finite signatures still need trace-function weights",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "signature buckets are not yet inverse-variable Kloosterman sums",
            "Pascadi_composite_Type_II": "signature buckets are path templates rather than composite Type-II boxes",
            "Wright_unbalanced_Kloosterman": "candidate only after signature templates become admissible unbalanced fractions",
            "Li_short_interval_x_052": "short interval existence gives no cycle-signature phase estimate",
        },
        "latest_narrowest_mouth": [
            "CycleSignatureWeightedPhaseSavingForLoopErasedCarrySwitchCore",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND TraceKloostermanCompletionOfCycleSignatureAndResidualPackets",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "cycle_signature_ledger_closed": finite_audit["cycle_signature_ledger_closed"],
        "cycle_signature_weighted_phase_saving_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature 审计",
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
        "## 2. cycle-signature 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"cycle_signature_atom_count_total={audit['cycle_signature_atom_count_total']}",
        f"switch_atom_count={audit['switch_atom_count']}",
        f"non_switch_atom_count={audit['non_switch_atom_count']}",
        f"adjacent_letter_pair_count_inside_atoms={audit['adjacent_letter_pair_count_inside_atoms']}",
        f"cycle_signature_decomposition_closed={str(audit['cycle_signature_decomposition_closed']).lower()}",
        f"raw_cycle_packet_count={audit['raw_cycle_packet_count']}",
        f"raw_cycle_edge_mass={audit['raw_cycle_edge_mass']}",
        f"raw_cycle_signature_count={audit['raw_cycle_signature_count']}",
        f"raw_cycle_shape_count={audit['raw_cycle_shape_count']}",
        f"raw_cycle_length_min/median/max={audit['raw_cycle_length_min']}/{audit['raw_cycle_length_median']}/{audit['raw_cycle_length_max']}",
        f"raw_self_loop_cycle_count={audit['raw_self_loop_cycle_count']}",
        f"raw_template_max_edge_ratio={audit['raw_template_max_edge_ratio']}",
        f"raw_template_top20_edge_ratio={audit['raw_template_top20_edge_ratio']}",
        f"raw_template_top100_edge_ratio={audit['raw_template_top100_edge_ratio']}",
        f"signed_cycle_packet_count={audit['signed_cycle_packet_count']}",
        f"signed_cycle_edge_mass={audit['signed_cycle_edge_mass']}",
        f"signed_cycle_signature_count={audit['signed_cycle_signature_count']}",
        f"signed_cycle_shape_count={audit['signed_cycle_shape_count']}",
        f"signed_cycle_length_min/median/max={audit['signed_cycle_length_min']}/{audit['signed_cycle_length_median']}/{audit['signed_cycle_length_max']}",
        f"signed_self_loop_cycle_count={audit['signed_self_loop_cycle_count']}",
        f"signed_A_sign_variable_cycle_count={audit['signed_A_sign_variable_cycle_count']}",
        f"signed_template_max_edge_ratio={audit['signed_template_max_edge_ratio']}",
        f"signed_template_top20_edge_ratio={audit['signed_template_top20_edge_ratio']}",
        f"signed_template_top100_edge_ratio={audit['signed_template_top100_edge_ratio']}",
        f"cycle_signature_weighted_phase_saving_closed={str(audit['cycle_signature_weighted_phase_saving_closed']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "strip cycle edge mass：",
        "",
        *markdown_table(
            audit["strip_cycle_signature_rows"],
            ["strip", "raw_cycle_edge_mass", "signed_cycle_edge_mass"],
        ),
        "",
        "最高质量 raw cycle templates：",
        "",
        *markdown_table(
            audit["top_raw_cycle_signature_rows"],
            ["template", "cycle_count", "edge_mass", "shape"],
        ),
        "",
        "最高质量 signed cycle templates：",
        "",
        *markdown_table(
            audit["top_signed_cycle_signature_rows"],
            ["template", "cycle_count", "edge_mass", "shape"],
        ),
        "",
        "最高质量 raw length/load shapes：",
        "",
        *markdown_table(audit["top_raw_cycle_shape_rows"], ["shape", "cycle_count", "edge_mass"]),
        "",
        "最高质量 signed length/load/sign shapes：",
        "",
        *markdown_table(
            audit["top_signed_cycle_shape_rows"], ["shape", "cycle_count", "edge_mass"]
        ),
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
        "结论：cycle core 已经进一步拆成 finite directed signatures 与",
        "length/load/sign buckets。该层是结构账本，不是相位相消。",
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
        f"cycle_signature_ledger_closed={str(payload['cycle_signature_ledger_closed']).lower()}",
        f"cycle_signature_weighted_phase_saving_closed={str(payload['cycle_signature_weighted_phase_saving_closed']).lower()}",
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
    print(f"cycle_signature_ledger_closed={payload['cycle_signature_ledger_closed']}")
    print(
        "cycle_signature_weighted_phase_saving_closed="
        f"{payload['cycle_signature_weighted_phase_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
