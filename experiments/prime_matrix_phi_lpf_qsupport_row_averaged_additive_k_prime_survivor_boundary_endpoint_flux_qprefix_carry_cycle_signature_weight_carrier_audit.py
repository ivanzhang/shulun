#!/usr/bin/env python3
"""审计 q-prefix carry cycle signature 的组合权重载体。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-audit.json

上一层已经把 loop-erased cycle core 拆成 directed signatures。本层继续只做
结构下钻：把每个 signature 的组合权重按 P-support、strip-support、
endpoint-flux class 与 signed A-shape fragmentation 分桶。

该层关闭的是 weighted phase saving 的载体账本；它不证明 weighted phase
saving，也不把 signature buckets 完成到 trace/Kloosterman family。
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_audit as signature  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-audit.json",
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
        "role": "needs a trace-function realization of the weighted carrier, not only finite signatures",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "needs bilinear Kloosterman variables modulo q; the carrier is still signature/P/strip incidence",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "needs composite Type-II boxes; the carrier remains a path-template incidence ledger",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "needs admissible unbalanced convolution fractions; the carrier is not yet such a family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "prime existence in short intervals does not control signature carrier phases",
    },
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


def a_class(cycle: list[tuple[int, int, str]]) -> str:
    """返回 signed cycle 的 A-step 符号类。"""
    labels = {item[2] for item in cycle}
    if labels == {"positive"}:
        return "all_positive"
    if labels == {"negative"}:
        return "all_negative"
    if labels == {"zero"}:
        return "all_zero"
    if "zero" in labels:
        return "mixed_with_zero"
    return "mixed_positive_negative"


def profile_string(counts: Counter[str]) -> str:
    """把小型分类计数器转为稳定字符串。"""
    return ",".join(f"{key}:{counts[key]}" for key in sorted(counts))


def mass_profile_string(counts: Counter[str]) -> str:
    """把边质量分类计数器转为稳定字符串。"""
    return ",".join(f"{key}:{counts[key]}" for key in sorted(counts))


def top_carrier_rows(
    template_edge_mass: Counter[str],
    template_counts: Counter[str],
    template_p_sets: dict[str, set[int]],
    template_strip_counts: dict[str, Counter[str]],
    template_endpoint_counts: dict[str, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高边质量的 signature carrier 行。"""
    rows = []
    order = sorted(
        template_edge_mass,
        key=lambda key: (-template_edge_mass[key], -template_counts[key], key),
    )
    for key in order[:limit]:
        rows.append(
            {
                "template": key,
                "cycle_count": template_counts[key],
                "edge_mass": template_edge_mass[key],
                "distinct_P_count": len(template_p_sets[key]),
                "strip_profile": profile_string(template_strip_counts[key]),
                "endpoint_profile": profile_string(template_endpoint_counts[key]),
            }
        )
    return rows


def top_fragment_rows(
    base_edge_mass: Counter[str],
    base_counts: Counter[str],
    child_edge_mass: dict[str, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出 raw-base 到 signed-child 的最高质量 fragmentation 行。"""
    rows = []
    order = sorted(base_edge_mass, key=lambda key: (-base_edge_mass[key], -base_counts[key], key))
    for key in order[:limit]:
        children = child_edge_mass[key]
        top_child, top_child_mass = children.most_common(1)[0]
        rows.append(
            {
                "raw_base_template": key,
                "signed_child_count": len(children),
                "signed_cycle_count": base_counts[key],
                "signed_edge_mass": base_edge_mass[key],
                "max_child_edge_share": top_child_mass / base_edge_mass[key],
                "top_signed_child": top_child,
            }
        )
    return rows


def support_summary(
    edge_mass: Counter[str],
    p_sets: dict[str, set[int]],
    strip_counts: dict[str, Counter[str]],
) -> dict[str, Any]:
    """汇总 signature 的 P/strip 支撑宽度。"""
    multi_p_edge_mass = sum(edge_mass[key] for key, values in p_sets.items() if len(values) > 1)
    multi_strip_edge_mass = sum(
        edge_mass[key] for key, values in strip_counts.items() if len(values) > 1
    )
    p_widths = [len(values) for values in p_sets.values()]
    strip_widths = [len(values) for values in strip_counts.values()]
    total = sum(edge_mass.values())
    return {
        "signature_count": len(edge_mass),
        "multi_P_signature_count": sum(1 for values in p_sets.values() if len(values) > 1),
        "multi_P_edge_mass": multi_p_edge_mass,
        "multi_P_edge_ratio": multi_p_edge_mass / total,
        "multi_strip_signature_count": sum(
            1 for values in strip_counts.values() if len(values) > 1
        ),
        "multi_strip_edge_mass": multi_strip_edge_mass,
        "multi_strip_edge_ratio": multi_strip_edge_mass / total,
        "P_support_width_min": min(p_widths),
        "P_support_width_median": statistics.median(p_widths),
        "P_support_width_max": max(p_widths),
        "strip_support_width_min": min(strip_widths),
        "strip_support_width_median": statistics.median(strip_widths),
        "strip_support_width_max": max(strip_widths),
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 cycle signature 的组合权重载体。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-audit.json"
        ).read_text()
    )
    previous = previous_payload["finite_audit"]

    totals: Counter[str] = Counter()
    raw_counts: Counter[str] = Counter()
    raw_edge_mass: Counter[str] = Counter()
    raw_p_sets: dict[str, set[int]] = defaultdict(set)
    raw_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    raw_endpoint_counts: dict[str, Counter[str]] = defaultdict(Counter)
    signed_counts: Counter[str] = Counter()
    signed_edge_mass: Counter[str] = Counter()
    signed_p_sets: dict[str, set[int]] = defaultdict(set)
    signed_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    signed_endpoint_counts: dict[str, Counter[str]] = defaultdict(Counter)
    signed_a_class_counts: Counter[str] = Counter()
    signed_a_class_edge_mass: Counter[str] = Counter()
    raw_base_signed_counts: Counter[str] = Counter()
    raw_base_signed_edge_mass: Counter[str] = Counter()
    raw_base_child_edge_mass: dict[str, Counter[str]] = defaultdict(Counter)

    for packet_index, packet in enumerate(packets):
        endpoint_profile = flow.qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        q_values = flow.phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(flow.qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))
        endpoint_class = endpoint_profile["endpoint_flux_class"]

        for m_value in m_values:
            _, transitions = flow.carry_dynamics.atom_transition_profile(
                packet_index, packet, endpoint_class, m_value, q_values
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
            raw_cycles, raw_stack = signature.loop_erased_cycle_packets(raw_seq)
            signed_cycles, signed_stack = signature.loop_erased_cycle_packets(signed_seq)
            totals["raw_residual_edge_mass"] += max(0, len(raw_stack) - 1)
            totals["signed_residual_edge_mass"] += max(0, len(signed_stack) - 1)

            for cycle in raw_cycles:
                template = signature.raw_template(cycle)
                length = len(cycle)
                raw_counts[template] += 1
                raw_edge_mass[template] += length
                raw_p_sets[template].add(packet["P"])
                raw_strip_counts[template][packet["strip"]] += 1
                raw_endpoint_counts[template][endpoint_class] += 1
                totals["raw_cycle_packet_count"] += 1
                totals["raw_cycle_edge_mass"] += length

            for cycle in signed_cycles:
                template = signature.signed_template(cycle)
                base = signature.raw_template([(item[0], item[1]) for item in cycle])
                length = len(cycle)
                cls = a_class(cycle)
                signed_counts[template] += 1
                signed_edge_mass[template] += length
                signed_p_sets[template].add(packet["P"])
                signed_strip_counts[template][packet["strip"]] += 1
                signed_endpoint_counts[template][endpoint_class] += 1
                signed_a_class_counts[cls] += 1
                signed_a_class_edge_mass[cls] += length
                raw_base_signed_counts[base] += 1
                raw_base_signed_edge_mass[base] += length
                raw_base_child_edge_mass[base][template] += length
                totals["signed_cycle_packet_count"] += 1
                totals["signed_cycle_edge_mass"] += length

    raw_support = support_summary(raw_edge_mass, raw_p_sets, raw_strip_counts)
    signed_support = support_summary(signed_edge_mass, signed_p_sets, signed_strip_counts)
    fragmented_base_edge_mass = sum(
        raw_base_signed_edge_mass[key]
        for key, children in raw_base_child_edge_mass.items()
        if len(children) > 1
    )
    child_share_rows = [
        max(children.values()) / raw_base_signed_edge_mass[key]
        for key, children in raw_base_child_edge_mass.items()
    ]

    weight_carrier_ledger_closed = (
        totals["atom_count_total"] == previous["cycle_signature_atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and totals["raw_cycle_packet_count"] == previous["raw_cycle_packet_count"]
        and totals["raw_cycle_edge_mass"] == previous["raw_cycle_edge_mass"]
        and totals["raw_residual_edge_mass"] == previous["raw_residual_edge_mass"]
        and len(raw_counts) == previous["raw_cycle_signature_count"]
        and totals["signed_cycle_packet_count"] == previous["signed_cycle_packet_count"]
        and totals["signed_cycle_edge_mass"] == previous["signed_cycle_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and len(signed_counts) == previous["signed_cycle_signature_count"]
    )

    return {
        "max_prime": max_prime,
        "previous_cycle_signature_decomposition_closed": previous[
            "cycle_signature_decomposition_closed"
        ],
        "cycle_signature_weight_carrier_ledger_closed": weight_carrier_ledger_closed,
        "cycle_signature_atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "raw_cycle_packet_count": totals["raw_cycle_packet_count"],
        "raw_cycle_edge_mass": totals["raw_cycle_edge_mass"],
        "raw_residual_edge_mass": totals["raw_residual_edge_mass"],
        "raw_cycle_signature_count": len(raw_counts),
        "raw_carrier_support": raw_support,
        "signed_cycle_packet_count": totals["signed_cycle_packet_count"],
        "signed_cycle_edge_mass": totals["signed_cycle_edge_mass"],
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "signed_cycle_signature_count": len(signed_counts),
        "signed_carrier_support": signed_support,
        "signed_A_class_cycle_rows": [
            {
                "A_class": key,
                "cycle_count": signed_a_class_counts[key],
                "edge_mass": signed_a_class_edge_mass[key],
                "edge_ratio": signed_a_class_edge_mass[key]
                / totals["signed_cycle_edge_mass"],
            }
            for key in sorted(signed_a_class_edge_mass)
        ],
        "raw_base_signed_refinement_count": len(raw_base_signed_edge_mass),
        "raw_base_with_multiple_signed_children_count": sum(
            1 for children in raw_base_child_edge_mass.values() if len(children) > 1
        ),
        "raw_base_fragmented_signed_edge_mass": fragmented_base_edge_mass,
        "raw_base_fragmented_signed_edge_ratio": fragmented_base_edge_mass
        / totals["signed_cycle_edge_mass"],
        "raw_base_max_child_edge_share_min": min(child_share_rows),
        "raw_base_max_child_edge_share_median": statistics.median(child_share_rows),
        "raw_base_max_child_edge_share_max": max(child_share_rows),
        "top_raw_carrier_rows": top_carrier_rows(
            raw_edge_mass, raw_counts, raw_p_sets, raw_strip_counts, raw_endpoint_counts
        ),
        "top_signed_carrier_rows": top_carrier_rows(
            signed_edge_mass,
            signed_counts,
            signed_p_sets,
            signed_strip_counts,
            signed_endpoint_counts,
        ),
        "top_raw_base_signed_fragment_rows": top_fragment_rows(
            raw_base_signed_edge_mass, raw_base_signed_counts, raw_base_child_edge_mass
        ),
        "cycle_signature_weight_carrier_closed": weight_carrier_ledger_closed,
        "cycle_signature_weighted_phase_saving_closed": False,
        "signed_refinement_weight_reconciliation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_flow_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_cycle_signature_weight_carrier_ledger_closed_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the previous finite signature ledger leaves weighted phase saving as the direct hard point",
        "current_object": {
            "input": "raw/signed cycle signatures from the loop-erased carry-switch core",
            "operation": "support and fragmentation audit for the combinatorial weights carried by signatures",
            "dominant_shape": "high-mass signed carriers are thin in P/strip support, while raw bases fragment across signed children",
            "remaining": "weighted phase saving must reconcile signed refinements, thin carriers, residual endpoints, and trace/Kloosterman completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "FiniteCycleSignatureLedgerImported",
                finite_audit["previous_cycle_signature_decomposition_closed"],
                finite_audit["previous_cycle_signature_decomposition_closed"],
                "The previous finite cycle-signature ledger is imported.",
                "none for import",
            ),
            gate(
                "CycleSignatureWeightCarrierLedger",
                finite_audit["cycle_signature_weight_carrier_closed"],
                finite_audit["cycle_signature_weight_carrier_closed"],
                "Every raw/signed signature is assigned P-support, strip-support, endpoint class, and signed fragmentation data.",
                "none for current deterministic carrier ledger",
            ),
            gate(
                "CycleSignatureWeightedPhaseSaving",
                False,
                False,
                "Prove cancellation for the weighted carriers exposed here.",
                "requires analytic phase input after signed refinement and thin-support handling",
            ),
            gate(
                "SignedRefinementWeightReconciliation",
                False,
                False,
                "Reconcile raw-base cycle weights after signed A-step refinement.",
                "requires cancellation or exact transfer across signed children of the same raw base",
            ),
            gate(
                "TraceKloostermanCompletion",
                False,
                False,
                "Convert the weighted carriers to an admissible trace/Kloosterman family.",
                "requires a new completion map, not supplied by this ledger",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "candidate only after weighted carriers are realized as trace-function sums",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "candidate only after inverse-variable Kloosterman variables appear",
            "Pascadi_composite_Type_II": "not matched because carriers are not composite Type-II boxes",
            "Wright_unbalanced_Kloosterman": "not matched because carriers are not unbalanced convolution fractions",
            "Li_short_interval_x_052": "does not estimate the exposed signature carrier phases",
        },
        "latest_narrowest_mouth": [
            "SignedCycleSignatureCarrierWeightedPhaseSaving",
            "AND RawBaseToSignedChildWeightReconciliation",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND TraceKloostermanCompletionOfCycleSignatureAndResidualPackets",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "cycle_signature_weight_carrier_closed": finite_audit[
            "cycle_signature_weight_carrier_closed"
        ],
        "cycle_signature_weighted_phase_saving_closed": False,
        "signed_refinement_weight_reconciliation_closed": False,
        "thin_P_support_carrier_summation_closed": False,
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


def support_block(title: str, data: dict[str, Any]) -> list[str]:
    """生成支撑宽度摘要块。"""
    return [
        title,
        "",
        "```text",
        f"signature_count={data['signature_count']}",
        f"multi_P_signature_count={data['multi_P_signature_count']}",
        f"multi_P_edge_mass={data['multi_P_edge_mass']}",
        f"multi_P_edge_ratio={data['multi_P_edge_ratio']}",
        f"multi_strip_signature_count={data['multi_strip_signature_count']}",
        f"multi_strip_edge_mass={data['multi_strip_edge_mass']}",
        f"multi_strip_edge_ratio={data['multi_strip_edge_ratio']}",
        f"P_support_width_min/median/max={data['P_support_width_min']}/{data['P_support_width_median']}/{data['P_support_width_max']}",
        f"strip_support_width_min/median/max={data['strip_support_width_min']}/{data['strip_support_width_median']}/{data['strip_support_width_max']}",
        "```",
        "",
    ]


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature weight-carrier 审计",
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
        "## 2. weight-carrier 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"cycle_signature_atom_count_total={audit['cycle_signature_atom_count_total']}",
        f"switch_atom_count={audit['switch_atom_count']}",
        f"non_switch_atom_count={audit['non_switch_atom_count']}",
        f"adjacent_letter_pair_count_inside_atoms={audit['adjacent_letter_pair_count_inside_atoms']}",
        f"cycle_signature_weight_carrier_ledger_closed={str(audit['cycle_signature_weight_carrier_ledger_closed']).lower()}",
        f"raw_cycle_packet_count={audit['raw_cycle_packet_count']}",
        f"raw_cycle_edge_mass={audit['raw_cycle_edge_mass']}",
        f"raw_cycle_signature_count={audit['raw_cycle_signature_count']}",
        f"signed_cycle_packet_count={audit['signed_cycle_packet_count']}",
        f"signed_cycle_edge_mass={audit['signed_cycle_edge_mass']}",
        f"signed_cycle_signature_count={audit['signed_cycle_signature_count']}",
        f"raw_base_signed_refinement_count={audit['raw_base_signed_refinement_count']}",
        f"raw_base_with_multiple_signed_children_count={audit['raw_base_with_multiple_signed_children_count']}",
        f"raw_base_fragmented_signed_edge_ratio={audit['raw_base_fragmented_signed_edge_ratio']}",
        f"raw_base_max_child_edge_share_min/median/max={audit['raw_base_max_child_edge_share_min']}/{audit['raw_base_max_child_edge_share_median']}/{audit['raw_base_max_child_edge_share_max']}",
        f"cycle_signature_weighted_phase_saving_closed={str(audit['cycle_signature_weighted_phase_saving_closed']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        *support_block("raw carrier support：", audit["raw_carrier_support"]),
        *support_block("signed carrier support：", audit["signed_carrier_support"]),
        "signed A-class edge mass：",
        "",
        *markdown_table(
            audit["signed_A_class_cycle_rows"],
            ["A_class", "cycle_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高质量 raw carriers：",
        "",
        *markdown_table(
            audit["top_raw_carrier_rows"],
            [
                "template",
                "cycle_count",
                "edge_mass",
                "distinct_P_count",
                "strip_profile",
                "endpoint_profile",
            ],
        ),
        "",
        "最高质量 signed carriers：",
        "",
        *markdown_table(
            audit["top_signed_carrier_rows"],
            [
                "template",
                "cycle_count",
                "edge_mass",
                "distinct_P_count",
                "strip_profile",
                "endpoint_profile",
            ],
        ),
        "",
        "raw-base 到 signed-child fragmentation：",
        "",
        *markdown_table(
            audit["top_raw_base_signed_fragment_rows"],
            [
                "raw_base_template",
                "signed_child_count",
                "signed_cycle_count",
                "signed_edge_mass",
                "max_child_edge_share",
                "top_signed_child",
            ],
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
        "结论：weighted phase saving 的组合载体已经被定位到 signed carriers、",
        "raw-base/signed-child fragmentation 与 thin P-support carriers。该层不是",
        "相位相消证明。",
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
        f"cycle_signature_weight_carrier_closed={str(payload['cycle_signature_weight_carrier_closed']).lower()}",
        f"cycle_signature_weighted_phase_saving_closed={str(payload['cycle_signature_weighted_phase_saving_closed']).lower()}",
        f"signed_refinement_weight_reconciliation_closed={str(payload['signed_refinement_weight_reconciliation_closed']).lower()}",
        f"thin_P_support_carrier_summation_closed={str(payload['thin_P_support_carrier_summation_closed']).lower()}",
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
        "cycle_signature_weight_carrier_closed="
        f"{payload['cycle_signature_weight_carrier_closed']}"
    )
    print(
        "cycle_signature_weighted_phase_saving_closed="
        f"{payload['cycle_signature_weighted_phase_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
