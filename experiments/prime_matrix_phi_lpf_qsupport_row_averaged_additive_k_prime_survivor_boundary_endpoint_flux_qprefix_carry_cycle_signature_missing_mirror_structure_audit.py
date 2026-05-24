#!/usr/bin/env python3
"""审计 missing-mirror residual carriers 的结构支撑。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_structure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure-audit.json

上一层把 mirror-imbalance 拆成 missing-mirror 与 unequal-mirror-pair residual。
本层优先下钻占主导的 missing-mirror mass，登记它的 strip、endpoint、A-class、
cycle length、P-support 与 raw-base 支撑形状。

该层只关闭 missing-mirror 的有限结构账本；它不证明 missing-mirror phase saving。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_mirror_imbalance_support_audit as imbalance  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit as mirror  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit as carrier  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

IMBALANCE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support-audit.json"
)

DEPENDENCIES = [
    IMBALANCE_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "sub-Pólya-Vinogradov bilinear trace-function input, but only after missing carriers become trace sums",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "power-saving bilinear Kloosterman sums for arbitrary q, but requires explicit Kloosterman variables",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "composite-modulus Type-II Kloosterman amplification, not matched to missing signed-child templates",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced convolution/Kloosterman-fraction input, candidate only after endpoint carriers are completed",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence at exponent 0.52, still not a signed-carrier phase estimate",
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


def profile_string(counts: Counter[str]) -> str:
    """把分类计数器转为稳定字符串。"""
    return ",".join(f"{key}:{counts[key]}" for key in sorted(counts))


def p_width_bucket(width: int) -> str:
    """把 P-support 宽度分桶。"""
    if width == 1:
        return "single_P"
    if width <= 4:
        return "P_width_2_to_4"
    if width <= 16:
        return "P_width_5_to_16"
    if width <= 64:
        return "P_width_17_to_64"
    return "P_width_ge_65"


def endpoint_group(endpoint_class: str) -> str:
    """把细 endpoint class 合并成几何组。"""
    if endpoint_class.startswith("lower_wing"):
        return "lower_wing_single_shell"
    if endpoint_class.startswith("upper_wing"):
        return "upper_wing_single_shell"
    if "two_sided_left_and_right_collars" in endpoint_class:
        return "right_tail_two_sided_collar"
    if "left_collar_only" in endpoint_class:
        return "right_tail_left_collar"
    if "right_collar_only" in endpoint_class:
        return "right_tail_right_collar"
    if "terminal_full_interval" in endpoint_class:
        return "right_tail_terminal_full_interval"
    return endpoint_class


def rows_from_counter(counter: Counter[str], total: int, key_name: str) -> list[dict[str, Any]]:
    """把边质量 counter 转为排序表。"""
    return [
        {key_name: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], item))
    ]


def top_missing_rows(
    missing_edge_mass: Counter[str],
    template_base: dict[str, str],
    template_mirror: dict[str, str],
    template_a_class: dict[str, str],
    template_length: dict[str, int],
    template_p_sets: dict[str, set[int]],
    template_strip_counts: dict[str, Counter[str]],
    template_endpoint_counts: dict[str, Counter[str]],
    raw_base_child_edge_mass: dict[str, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量 missing-mirror signed-child rows。"""
    rows = []
    order = sorted(missing_edge_mass, key=lambda key: (-missing_edge_mass[key], key))
    for key in order[:limit]:
        base = template_base[key]
        rows.append(
            {
                "signed_child": key,
                "missing_mirror_child": template_mirror[key],
                "raw_base_template": base,
                "missing_edge_mass": missing_edge_mass[key],
                "cycle_length": template_length[key],
                "A_class": template_a_class[key],
                "P_support_width": len(template_p_sets[key]),
                "P_width_bucket": p_width_bucket(len(template_p_sets[key])),
                "strip_profile": profile_string(template_strip_counts[key]),
                "endpoint_profile": profile_string(template_endpoint_counts[key]),
                "raw_base_child_count": len(raw_base_child_edge_mass[base]),
            }
        )
    return rows


def top_raw_base_rows(
    missing_base_edge_mass: Counter[str],
    raw_base_edge_mass: Counter[str],
    raw_base_child_edge_mass: dict[str, Counter[str]],
    missing_base_strip_counts: dict[str, Counter[str]],
    missing_base_endpoint_group_counts: dict[str, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量 missing raw-base rows。"""
    rows = []
    order = sorted(
        missing_base_edge_mass,
        key=lambda key: (-missing_base_edge_mass[key], -raw_base_edge_mass[key], key),
    )
    for key in order[:limit]:
        rows.append(
            {
                "raw_base_template": key,
                "missing_edge_mass": missing_base_edge_mass[key],
                "raw_base_signed_edge_mass": raw_base_edge_mass[key],
                "missing_share_inside_raw_base": missing_base_edge_mass[key]
                / raw_base_edge_mass[key],
                "signed_child_count": len(raw_base_child_edge_mass[key]),
                "strip_profile": profile_string(missing_base_strip_counts[key]),
                "endpoint_group_profile": profile_string(missing_base_endpoint_group_counts[key]),
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 missing-mirror structure。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(IMBALANCE_AUDIT.read_text())
    previous = previous_payload["finite_audit"]

    totals: Counter[str] = Counter()
    template_edge_mass: Counter[str] = Counter()
    template_p_sets: dict[str, set[int]] = defaultdict(set)
    template_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_endpoint_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_mirror: dict[str, str] = {}
    template_base: dict[str, str] = {}
    template_a_class: dict[str, str] = {}
    template_length: dict[str, int] = {}
    raw_base_edge_mass: Counter[str] = Counter()
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

            signed_seq: list[tuple[int, int, str]] = []
            for transition in transitions:
                signed_seq.append(
                    (
                        transition["q_gap"],
                        transition["carry_delta_k"],
                        flow.letter_run.sign_label(transition["A_step"]),
                    )
                )

            totals["switch_atom_count"] += 1
            totals["adjacent_letter_pair_count_inside_atoms"] += len(signed_seq) - 1
            signed_cycles, signed_stack = signature.loop_erased_cycle_packets(signed_seq)
            totals["signed_residual_edge_mass"] += max(0, len(signed_stack) - 1)

            for cycle in signed_cycles:
                template = signature.signed_template(cycle)
                base = signature.raw_template([(item[0], item[1]) for item in cycle])
                length = len(cycle)
                template_edge_mass[template] += length
                template_p_sets[template].add(packet["P"])
                template_strip_counts[template][packet["strip"]] += length
                template_endpoint_counts[template][endpoint_class] += length
                template_mirror[template] = mirror.signed_mirror_template(cycle)
                template_base[template] = base
                template_a_class[template] = carrier.a_class(cycle)
                template_length[template] = length
                raw_base_edge_mass[base] += length
                raw_base_child_edge_mass[base][template] += length
                totals["signed_cycle_packet_count"] += 1
                totals["signed_cycle_edge_mass"] += length

    missing_edge_mass: Counter[str] = Counter()
    missing_strip_edge_mass: Counter[str] = Counter()
    missing_endpoint_edge_mass: Counter[str] = Counter()
    missing_endpoint_group_edge_mass: Counter[str] = Counter()
    missing_a_class_edge_mass: Counter[str] = Counter()
    missing_cycle_length_edge_mass: Counter[str] = Counter()
    missing_p_width_edge_mass: Counter[str] = Counter()
    missing_base_edge_mass: Counter[str] = Counter()
    missing_base_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    missing_base_endpoint_group_counts: dict[str, Counter[str]] = defaultdict(Counter)
    missing_raw_base_share_values: list[float] = []

    for template, mass in template_edge_mass.items():
        mirror_template = template_mirror[template]
        if mirror_template == template or mirror_template in template_edge_mass:
            continue
        base = template_base[template]
        missing_edge_mass[template] = mass
        missing_a_class_edge_mass[template_a_class[template]] += mass
        missing_cycle_length_edge_mass[str(template_length[template])] += mass
        missing_p_width_edge_mass[p_width_bucket(len(template_p_sets[template]))] += mass
        missing_base_edge_mass[base] += mass

        for strip, edge_mass in template_strip_counts[template].items():
            missing_strip_edge_mass[strip] += edge_mass
            missing_base_strip_counts[base][strip] += edge_mass
        for endpoint_class, edge_mass in template_endpoint_counts[template].items():
            group = endpoint_group(endpoint_class)
            missing_endpoint_edge_mass[endpoint_class] += edge_mass
            missing_endpoint_group_edge_mass[group] += edge_mass
            missing_base_endpoint_group_counts[base][group] += edge_mass

    missing_total = sum(missing_edge_mass.values())
    for base, mass in missing_base_edge_mass.items():
        missing_raw_base_share_values.append(mass / raw_base_edge_mass[base])

    single_strip_missing_edge_mass = sum(
        mass for template, mass in missing_edge_mass.items() if len(template_strip_counts[template]) == 1
    )
    single_P_missing_edge_mass = sum(
        mass for template, mass in missing_edge_mass.items() if len(template_p_sets[template]) == 1
    )
    wing_single_shell_edge_mass = (
        missing_endpoint_group_edge_mass["lower_wing_single_shell"]
        + missing_endpoint_group_edge_mass["upper_wing_single_shell"]
    )
    right_tail_edge_mass = sum(
        mass
        for group, mass in missing_endpoint_group_edge_mass.items()
        if group.startswith("right_tail")
    )

    ledger_closed = (
        previous["mirror_imbalance_support_ledger_closed"]
        and totals["atom_count_total"] == previous["atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and totals["signed_cycle_packet_count"] == previous["signed_cycle_packet_count"]
        and totals["signed_cycle_edge_mass"] == previous["signed_cycle_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and missing_total == previous["missing_mirror_edge_mass"]
        and len(missing_edge_mass) == previous["missing_mirror_pair_count"]
        and sum(missing_strip_edge_mass.values()) == missing_total
        and sum(missing_endpoint_edge_mass.values()) == missing_total
        and sum(missing_a_class_edge_mass.values()) == missing_total
        and sum(missing_p_width_edge_mass.values()) == missing_total
    )

    return {
        "max_prime": max_prime,
        "previous_mirror_imbalance_support_ledger_closed": previous[
            "mirror_imbalance_support_ledger_closed"
        ],
        "missing_mirror_structure_ledger_closed": ledger_closed,
        "atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "signed_cycle_packet_count": totals["signed_cycle_packet_count"],
        "signed_cycle_edge_mass": totals["signed_cycle_edge_mass"],
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "signed_cycle_signature_count": len(template_edge_mass),
        "missing_mirror_edge_mass": missing_total,
        "missing_mirror_pair_count": len(missing_edge_mass),
        "missing_raw_base_count": len(missing_base_edge_mass),
        "single_P_missing_edge_mass": single_P_missing_edge_mass,
        "single_P_missing_edge_ratio": single_P_missing_edge_mass / missing_total,
        "single_strip_missing_edge_mass": single_strip_missing_edge_mass,
        "single_strip_missing_edge_ratio": single_strip_missing_edge_mass / missing_total,
        "wing_single_shell_missing_edge_mass": wing_single_shell_edge_mass,
        "wing_single_shell_missing_edge_ratio": wing_single_shell_edge_mass / missing_total,
        "right_tail_missing_edge_mass": right_tail_edge_mass,
        "right_tail_missing_edge_ratio": right_tail_edge_mass / missing_total,
        "missing_raw_base_share_min": min(missing_raw_base_share_values),
        "missing_raw_base_share_median": statistics.median(missing_raw_base_share_values),
        "missing_raw_base_share_max": max(missing_raw_base_share_values),
        "missing_strip_edge_rows": rows_from_counter(
            missing_strip_edge_mass, missing_total, "strip"
        ),
        "missing_endpoint_group_edge_rows": rows_from_counter(
            missing_endpoint_group_edge_mass, missing_total, "endpoint_group"
        ),
        "missing_endpoint_edge_rows": rows_from_counter(
            missing_endpoint_edge_mass, missing_total, "endpoint_class"
        ),
        "missing_A_class_edge_rows": rows_from_counter(
            missing_a_class_edge_mass, missing_total, "A_class"
        ),
        "missing_cycle_length_edge_rows": rows_from_counter(
            missing_cycle_length_edge_mass, missing_total, "cycle_length"
        ),
        "missing_P_width_bucket_edge_rows": rows_from_counter(
            missing_p_width_edge_mass, missing_total, "P_width_bucket"
        ),
        "top_missing_signed_child_rows": top_missing_rows(
            missing_edge_mass,
            template_base,
            template_mirror,
            template_a_class,
            template_length,
            template_p_sets,
            template_strip_counts,
            template_endpoint_counts,
            raw_base_child_edge_mass,
        ),
        "top_missing_raw_base_rows": top_raw_base_rows(
            missing_base_edge_mass,
            raw_base_edge_mass,
            raw_base_child_edge_mass,
            missing_base_strip_counts,
            missing_base_endpoint_group_counts,
        ),
        "missing_mirror_structure_ledger_closed_flag": ledger_closed,
        "missing_mirror_carrier_phase_saving_closed": False,
        "missing_mirror_to_trace_completion_closed": False,
        "missing_mirror_endpoint_aggregation_closed": False,
        "unequal_mirror_pair_residual_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_structure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "missing_mirror_structure_ledger_closed_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "missing-mirror mass is the dominant part of the latest mirror-imbalance obstruction",
        "current_object": {
            "input": "missing-mirror signed-child residual carriers",
            "operation": "strip/endpoint/A-class/length/P-support/raw-base structure audit",
            "dominant_shape": "missing-mirror mass is mostly mixed-sign and one-strip endpoint support, not yet a trace family",
            "remaining": "phase saving for missing-mirror endpoint carriers and completion to an admissible trace/Kloosterman family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "MirrorImbalanceSupportLedgerImported",
                finite_audit["previous_mirror_imbalance_support_ledger_closed"],
                finite_audit["previous_mirror_imbalance_support_ledger_closed"],
                "The previous mirror-imbalance support ledger is imported.",
                "none for import",
            ),
            gate(
                "MissingMirrorStructureLedger",
                finite_audit["missing_mirror_structure_ledger_closed"],
                finite_audit["missing_mirror_structure_ledger_closed"],
                "Every missing-mirror edge is assigned strip, endpoint, sign, length, P-support, and raw-base structure.",
                "none for the finite structure ledger",
            ),
            gate(
                "MissingMirrorCarrierPhaseSaving",
                False,
                False,
                "Prove cancellation or positivity for the missing-mirror carrier family.",
                "requires analytic phase input on the exposed endpoint support",
            ),
            gate(
                "MissingMirrorTraceCompletion",
                False,
                False,
                "Complete the missing-mirror endpoint carriers to admissible trace/Kloosterman sums.",
                "requires an explicit completion map and no-loss aggregation",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "not directly applicable before missing-mirror endpoint carriers become trace-function sums",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "not directly applicable before explicit Kloosterman variables are extracted",
            "Pascadi_composite_Type_II": "not matched because missing-mirror support is not a composite-modulus Type-II box",
            "Wright_unbalanced_Kloosterman": "candidate only after the endpoint support is converted to unbalanced Kloosterman fractions",
            "Li_short_interval_x_052": "does not estimate signed missing-mirror carrier phases",
        },
        "latest_narrowest_mouth": [
            "MissingMirrorEndpointCarrierPhaseSaving",
            "AND MissingMirrorTraceKloostermanCompletion",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "missing_mirror_structure_ledger_closed": finite_audit[
            "missing_mirror_structure_ledger_closed"
        ],
        "missing_mirror_carrier_phase_saving_closed": False,
        "missing_mirror_to_trace_completion_closed": False,
        "unequal_mirror_pair_residual_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature missing-mirror structure 审计",
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
        "## 2. missing-mirror structure 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"missing_mirror_structure_ledger_closed={str(audit['missing_mirror_structure_ledger_closed']).lower()}",
        f"missing_mirror_edge_mass={audit['missing_mirror_edge_mass']}",
        f"missing_mirror_pair_count={audit['missing_mirror_pair_count']}",
        f"missing_raw_base_count={audit['missing_raw_base_count']}",
        f"single_P_missing_edge_mass={audit['single_P_missing_edge_mass']}",
        f"single_P_missing_edge_ratio={audit['single_P_missing_edge_ratio']}",
        f"single_strip_missing_edge_mass={audit['single_strip_missing_edge_mass']}",
        f"single_strip_missing_edge_ratio={audit['single_strip_missing_edge_ratio']}",
        f"wing_single_shell_missing_edge_mass={audit['wing_single_shell_missing_edge_mass']}",
        f"wing_single_shell_missing_edge_ratio={audit['wing_single_shell_missing_edge_ratio']}",
        f"right_tail_missing_edge_mass={audit['right_tail_missing_edge_mass']}",
        f"right_tail_missing_edge_ratio={audit['right_tail_missing_edge_ratio']}",
        f"missing_raw_base_share_min/median/max={audit['missing_raw_base_share_min']}/{audit['missing_raw_base_share_median']}/{audit['missing_raw_base_share_max']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "missing strip edge mass：",
        "",
        *markdown_table(audit["missing_strip_edge_rows"], ["strip", "edge_mass", "edge_ratio"]),
        "",
        "missing endpoint group edge mass：",
        "",
        *markdown_table(
            audit["missing_endpoint_group_edge_rows"],
            ["endpoint_group", "edge_mass", "edge_ratio"],
        ),
        "",
        "missing A-class edge mass：",
        "",
        *markdown_table(audit["missing_A_class_edge_rows"], ["A_class", "edge_mass", "edge_ratio"]),
        "",
        "missing cycle length edge mass：",
        "",
        *markdown_table(
            audit["missing_cycle_length_edge_rows"],
            ["cycle_length", "edge_mass", "edge_ratio"],
        ),
        "",
        "missing P-width bucket edge mass：",
        "",
        *markdown_table(
            audit["missing_P_width_bucket_edge_rows"],
            ["P_width_bucket", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高 missing signed-child carriers：",
        "",
        *markdown_table(
            audit["top_missing_signed_child_rows"],
            [
                "signed_child",
                "missing_mirror_child",
                "raw_base_template",
                "missing_edge_mass",
                "cycle_length",
                "A_class",
                "P_support_width",
                "P_width_bucket",
                "strip_profile",
                "endpoint_profile",
                "raw_base_child_count",
            ],
        ),
        "",
        "最高 missing raw bases：",
        "",
        *markdown_table(
            audit["top_missing_raw_base_rows"],
            [
                "raw_base_template",
                "missing_edge_mass",
                "raw_base_signed_edge_mass",
                "missing_share_inside_raw_base",
                "signed_child_count",
                "strip_profile",
                "endpoint_group_profile",
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
        *[
            f"{key}={value}"
            for key, value in payload["external_theorem_implication"].items()
        ],
        "```",
        "",
        "结论：missing-mirror 主体已经从匿名 residual mass 压成 endpoint/strip/P-support",
        "结构账本。它仍不是 trace/Kloosterman family，也没有给出 phase saving。",
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
        f"missing_mirror_structure_ledger_closed={str(payload['missing_mirror_structure_ledger_closed']).lower()}",
        f"missing_mirror_carrier_phase_saving_closed={str(payload['missing_mirror_carrier_phase_saving_closed']).lower()}",
        f"missing_mirror_to_trace_completion_closed={str(payload['missing_mirror_to_trace_completion_closed']).lower()}",
        f"unequal_mirror_pair_residual_phase_saving_closed={str(payload['unequal_mirror_pair_residual_phase_saving_closed']).lower()}",
        f"thin_P_support_carrier_summation_closed={str(payload['thin_P_support_carrier_summation_closed']).lower()}",
        f"residual_endpoint_path_summation_closed={str(payload['residual_endpoint_path_summation_closed']).lower()}",
        f"completion_to_external_trace_or_kloosterman_closed={str(payload['completion_to_external_trace_or_kloosterman_closed']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
        "",
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
    OUT_MD.write_text(build_markdown(payload))
    audit = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(
        "missing_mirror_structure_ledger_closed="
        f"{payload['missing_mirror_structure_ledger_closed']}"
    )
    print(f"missing_mirror_edge_mass={audit['missing_mirror_edge_mass']}")
    print(f"single_strip_missing_edge_ratio={audit['single_strip_missing_edge_ratio']}")
    print(f"right_tail_missing_edge_ratio={audit['right_tail_missing_edge_ratio']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
