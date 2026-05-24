#!/usr/bin/env python3
"""审计 single-P local endpoint templates 的重数因式账本。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_multiplicity_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity-audit.json

上一层把 SinglePLocalPureEndpointPacketBound 压成局部模板重数与 P-slice
求和。本层只处理局部模板重数，把模板 edge mass 拆成
cycle_length * occurrence_count，并记录重复模板的局部支撑形状。该层关闭有限
因式账本，不证明全局均匀界。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_endpoint_router_audit as endpoint_router  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_structure_audit as missing_structure  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit as mirror  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_endpoint_packet_audit as single_p  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit as carrier  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

SINGLE_P_PACKET_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet-audit.json"
)

DEPENDENCIES = [
    SINGLE_P_PACKET_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface-audit.json",
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
        "role": "average trace input; does not prove local occurrence multiplicity for a width-one template",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "requires extracted Kloosterman variables, not just a local signed cycle template",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced average input; not a local template occurrence bound",
    },
    {
        "key": "Xu_Zhang_2026_generalized_kloosterman_arbitrary_sets",
        "url": "https://doi.org/10.1016/j.jnt.2025.09.027",
        "role": "published arbitrary-set bilinear input; still not a local cycle occurrence theorem",
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


def table_from_counter(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 edge-mass 表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def template_count_table(counter: Counter[Any], field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 template-count 表。"""
    total = sum(counter.values())
    return [
        {field: key, "template_count": counter[key], "template_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def factor_rows(counter: Counter[tuple[int, int, int]]) -> list[dict[str, Any]]:
    """输出 cycle_length、occurrence_count、edge_mass 因式行。"""
    total_templates = sum(counter.values())
    rows = []
    for cycle_length, occurrence_count, edge_mass in sorted(
        counter,
        key=lambda key: (-counter[key], key[2], key[0], key[1]),
    ):
        rows.append(
            {
                "cycle_length": cycle_length,
                "occurrence_count": occurrence_count,
                "template_edge_mass": edge_mass,
                "template_count": counter[(cycle_length, occurrence_count, edge_mass)],
                "template_ratio": counter[(cycle_length, occurrence_count, edge_mass)]
                / total_templates,
            }
        )
    return rows


def top_template_rows(
    edge_mass: Counter[str],
    occurrence_count: Counter[str],
    cycle_length: dict[str, int],
    template_p_value: dict[str, int],
    template_route: dict[str, str],
    template_a_class: dict[str, str],
    template_base: dict[str, str],
    packet_support: dict[str, set[int]],
    m_value_support: dict[str, set[int]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量与最高重复模板。"""
    rows = []
    for template in sorted(
        edge_mass,
        key=lambda key: (-edge_mass[key], -occurrence_count[key], -cycle_length[key], key),
    )[:limit]:
        rows.append(
            {
                "signed_child": template,
                "raw_base_template": template_base[template],
                "P": template_p_value[template],
                "edge_mass": edge_mass[template],
                "cycle_length": cycle_length[template],
                "occurrence_count": occurrence_count[template],
                "packet_support_count": len(packet_support[template]),
                "m_value_support_count": len(m_value_support[template]),
                "route_class": template_route[template],
                "route_superclass": single_p.route_superclass(template_route[template]),
                "A_class": template_a_class[template],
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 single-P local template multiplicity。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(SINGLE_P_PACKET_AUDIT.read_text())
    previous = previous_payload["finite_audit"]

    template_edge_mass: Counter[str] = Counter()
    template_occurrence_count: Counter[str] = Counter()
    template_p_sets: dict[str, set[int]] = defaultdict(set)
    template_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_endpoint_group_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_packet_support: dict[str, set[int]] = defaultdict(set)
    template_m_value_support: dict[str, set[int]] = defaultdict(set)
    template_q_prefix_support: dict[str, set[int]] = defaultdict(set)
    template_m_shell_support: dict[str, set[int]] = defaultdict(set)
    template_mirror: dict[str, str] = {}
    template_base: dict[str, str] = {}
    template_a_class: dict[str, str] = {}
    template_cycle_length: dict[str, int] = {}

    for packet_index, packet in enumerate(packets):
        endpoint_profile = flow.qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        q_values = flow.phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(flow.qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))
        endpoint_class = endpoint_profile["endpoint_flux_class"]
        endpoint_group = missing_structure.endpoint_group(endpoint_class)

        for m_value in m_values:
            _, transitions = flow.carry_dynamics.atom_transition_profile(
                packet_index, packet, endpoint_class, m_value, q_values
            )
            if len(transitions) < 2:
                continue

            signed_seq = [
                (
                    transition["q_gap"],
                    transition["carry_delta_k"],
                    flow.letter_run.sign_label(transition["A_step"]),
                )
                for transition in transitions
            ]
            signed_cycles, _ = signature.loop_erased_cycle_packets(signed_seq)

            for cycle in signed_cycles:
                template = signature.signed_template(cycle)
                base = signature.raw_template([(item[0], item[1]) for item in cycle])
                length = len(cycle)
                template_edge_mass[template] += length
                template_occurrence_count[template] += 1
                template_p_sets[template].add(packet["P"])
                template_strip_counts[template][packet["strip"]] += length
                template_endpoint_group_counts[template][endpoint_group] += length
                template_packet_support[template].add(packet_index)
                template_m_value_support[template].add(m_value)
                template_q_prefix_support[template].add(packet["q_prefix_count"])
                template_m_shell_support[template].add(packet["m_shell_prime_count"])
                template_mirror[template] = mirror.signed_mirror_template(cycle)
                template_base[template] = base
                template_a_class[template] = carrier.a_class(cycle)
                template_cycle_length[template] = length

    pure_edge_mass: Counter[str] = Counter()
    template_route: dict[str, str] = {}
    for template, mass in template_edge_mass.items():
        mirror_template = template_mirror[template]
        if mirror_template == template or mirror_template in template_edge_mass:
            continue
        route = endpoint_router.route_class(
            template_strip_counts[template], template_endpoint_group_counts[template]
        )
        if route.startswith("pure_"):
            pure_edge_mass[template] = mass
            template_route[template] = route

    single_edge_mass: Counter[str] = Counter()
    template_p_value: dict[str, int] = {}
    for template, mass in pure_edge_mass.items():
        if len(template_p_sets[template]) == 1:
            single_edge_mass[template] = mass
            template_p_value[template] = next(iter(template_p_sets[template]))

    occurrence_template_count: Counter[int] = Counter()
    occurrence_edge_mass: Counter[int] = Counter()
    cycle_template_count: Counter[int] = Counter()
    cycle_edge_mass: Counter[int] = Counter()
    packet_support_template_count: Counter[int] = Counter()
    packet_support_edge_mass: Counter[int] = Counter()
    m_value_support_template_count: Counter[int] = Counter()
    m_value_support_edge_mass: Counter[int] = Counter()
    factor_counter: Counter[tuple[int, int, int]] = Counter()

    for template, mass in single_edge_mass.items():
        occurrence = template_occurrence_count[template]
        cycle_len = template_cycle_length[template]
        packet_count = len(template_packet_support[template])
        m_value_count = len(template_m_value_support[template])
        occurrence_template_count[occurrence] += 1
        occurrence_edge_mass[occurrence] += mass
        cycle_template_count[cycle_len] += 1
        cycle_edge_mass[cycle_len] += mass
        packet_support_template_count[packet_count] += 1
        packet_support_edge_mass[packet_count] += mass
        m_value_support_template_count[m_value_count] += 1
        m_value_support_edge_mass[m_value_count] += mass
        factor_counter[(cycle_len, occurrence, mass)] += 1

    total_edge_mass = sum(single_edge_mass.values())
    total_templates = len(single_edge_mass)
    template_masses = list(single_edge_mass.values())
    occurrence_values = [template_occurrence_count[template] for template in single_edge_mass]
    cycle_values = [template_cycle_length[template] for template in single_edge_mass]
    repeated_templates = [
        template for template in single_edge_mass if template_occurrence_count[template] > 1
    ]
    single_occurrence_templates = [
        template for template in single_edge_mass if template_occurrence_count[template] == 1
    ]
    high_edge_templates = [template for template in single_edge_mass if single_edge_mass[template] > 12]
    multi_packet_templates = [
        template for template in single_edge_mass if len(template_packet_support[template]) > 1
    ]
    multi_m_value_templates = [
        template for template in single_edge_mass if len(template_m_value_support[template]) > 1
    ]

    ledger_closed = (
        previous["single_P_local_endpoint_structure_ledger_closed"]
        and total_edge_mass == previous["single_P_local_endpoint_edge_mass"]
        and total_templates == previous["single_P_local_endpoint_template_count"]
        and max(template_masses) == previous["single_P_template_edge_mass_max"]
        and sum(occurrence_edge_mass.values()) == total_edge_mass
        and sum(cycle_edge_mass.values()) == total_edge_mass
        and sum(packet_support_edge_mass.values()) == total_edge_mass
        and sum(m_value_support_edge_mass.values()) == total_edge_mass
        and all(
            template_cycle_length[template] * template_occurrence_count[template]
            == single_edge_mass[template]
            for template in single_edge_mass
        )
    )

    return {
        "max_prime": max_prime,
        "previous_single_P_local_endpoint_structure_ledger_closed": previous[
            "single_P_local_endpoint_structure_ledger_closed"
        ],
        "single_P_local_template_multiplicity_factor_ledger_closed": ledger_closed,
        "single_P_local_endpoint_edge_mass": total_edge_mass,
        "single_P_local_endpoint_template_count": total_templates,
        "single_occurrence_template_count": len(single_occurrence_templates),
        "single_occurrence_edge_mass": sum(single_edge_mass[t] for t in single_occurrence_templates),
        "repeated_template_count": len(repeated_templates),
        "repeated_template_edge_mass": sum(single_edge_mass[t] for t in repeated_templates),
        "multi_packet_template_count": len(multi_packet_templates),
        "multi_packet_template_edge_mass": sum(single_edge_mass[t] for t in multi_packet_templates),
        "multi_m_value_template_count": len(multi_m_value_templates),
        "multi_m_value_template_edge_mass": sum(single_edge_mass[t] for t in multi_m_value_templates),
        "high_edge_gt12_template_count": len(high_edge_templates),
        "high_edge_gt12_edge_mass": sum(single_edge_mass[t] for t in high_edge_templates),
        "template_edge_mass_min": min(template_masses),
        "template_edge_mass_median": statistics.median(template_masses),
        "template_edge_mass_max": max(template_masses),
        "cycle_length_min": min(cycle_values),
        "cycle_length_median": statistics.median(cycle_values),
        "cycle_length_max": max(cycle_values),
        "occurrence_count_min": min(occurrence_values),
        "occurrence_count_median": statistics.median(occurrence_values),
        "occurrence_count_max": max(occurrence_values),
        "occurrence_template_rows": template_count_table(
            occurrence_template_count, "occurrence_count"
        ),
        "occurrence_edge_rows": table_from_counter(
            occurrence_edge_mass, total_edge_mass, "occurrence_count"
        ),
        "cycle_length_template_rows": template_count_table(
            cycle_template_count, "cycle_length"
        ),
        "cycle_length_edge_rows": table_from_counter(
            cycle_edge_mass, total_edge_mass, "cycle_length"
        ),
        "packet_support_template_rows": template_count_table(
            packet_support_template_count, "packet_support_count"
        ),
        "packet_support_edge_rows": table_from_counter(
            packet_support_edge_mass, total_edge_mass, "packet_support_count"
        ),
        "m_value_support_template_rows": template_count_table(
            m_value_support_template_count, "m_value_support_count"
        ),
        "m_value_support_edge_rows": table_from_counter(
            m_value_support_edge_mass, total_edge_mass, "m_value_support_count"
        ),
        "cycle_occurrence_factor_rows": factor_rows(factor_counter)[:30],
        "top_template_multiplicity_rows": top_template_rows(
            single_edge_mass,
            template_occurrence_count,
            template_cycle_length,
            template_p_value,
            template_route,
            template_a_class,
            template_base,
            template_packet_support,
            template_m_value_support,
        ),
        "observed_template_edge_mass_le_16": max(template_masses) <= 16,
        "observed_occurrence_count_le_4": max(occurrence_values) <= 4,
        "observed_cycle_length_le_14": max(cycle_values) <= 14,
        "local_cycle_length_uniform_bound_proved": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
        "cycle_occurrence_product_bound_proved": False,
        "local_template_multiplicity_uniform_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_multiplicity_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_template_multiplicity_factor_ledger_closed_uniform_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the latest narrowest mouth starts with LocalTemplateMultiplicityUniformBound",
        "current_object": {
            "input": "single-P local endpoint signed-child templates",
            "operation": "factor local template edge mass into cycle length times occurrence count",
            "dominant_shape": "almost all width-one templates occur once; repeated templates are sparse and low-mass",
            "remaining": "global cycle-length and occurrence-product bounds or a PDEC/SAE return route",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SinglePLocalEndpointStructureImported",
                finite_audit["previous_single_P_local_endpoint_structure_ledger_closed"],
                finite_audit["previous_single_P_local_endpoint_structure_ledger_closed"],
                "The previous single-P local endpoint packet ledger is imported.",
                "none for import",
            ),
            gate(
                "LocalTemplateMultiplicityFactorLedger",
                finite_audit["single_P_local_template_multiplicity_factor_ledger_closed"],
                finite_audit["single_P_local_template_multiplicity_factor_ledger_closed"],
                "Each single-P template edge mass is factored as cycle_length times occurrence_count.",
                "none for the finite factor ledger",
            ),
            gate(
                "LocalCycleLengthUniformBound",
                False,
                False,
                "Promote the observed cycle-length cap to a global structural bound.",
                "finite audit shows cycle_length<=14 but does not prove it globally",
            ),
            gate(
                "LocalOccurrenceMultiplicityUniformBound",
                False,
                False,
                "Promote the observed occurrence cap to a global structural bound.",
                "finite audit shows occurrence_count<=4 but does not prove it globally",
            ),
            gate(
                "CycleOccurrenceProductBoundOrPDEC",
                False,
                False,
                "Control the product cycle_length*occurrence_count, or route excess to PDEC/SAE.",
                "finite audit shows edge_mass<=16 but no global excess-return proof is supplied",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_Kloosterman_average_inputs": "do not prove local cycle occurrence multiplicity without a completed averaging variable",
            "Xu_Zhang_arbitrary_sets": "requires explicit finite-field sets; not a local signed-cycle multiplicity theorem",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND LocalOccurrenceMultiplicityUniformBound",
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
        "single_P_local_template_multiplicity_factor_ledger_closed": finite_audit[
            "single_P_local_template_multiplicity_factor_ledger_closed"
        ],
        "local_cycle_length_uniform_bound_proved": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
        "cycle_occurrence_product_bound_proved": False,
        "local_template_multiplicity_uniform_bound_proved": False,
        "single_P_slice_endpoint_packet_summation_closed": False,
        "single_P_local_endpoint_packet_bound_closed": False,
        "multi_P_trace_completion_closed": False,
        "pure_endpoint_carrier_phase_saving_closed": False,
        "mixed_right_tail_endpoint_router_no_loss_closed": False,
        "unequal_mirror_pair_residual_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local template multiplicity 审计",
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
        "## 2. local template multiplicity 因式审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_template_multiplicity_factor_ledger_closed={str(audit['single_P_local_template_multiplicity_factor_ledger_closed']).lower()}",
        f"single_P_local_endpoint_edge_mass={audit['single_P_local_endpoint_edge_mass']}",
        f"single_P_local_endpoint_template_count={audit['single_P_local_endpoint_template_count']}",
        f"single_occurrence_template_count={audit['single_occurrence_template_count']}",
        f"single_occurrence_edge_mass={audit['single_occurrence_edge_mass']}",
        f"repeated_template_count={audit['repeated_template_count']}",
        f"repeated_template_edge_mass={audit['repeated_template_edge_mass']}",
        f"multi_packet_template_count={audit['multi_packet_template_count']}",
        f"multi_packet_template_edge_mass={audit['multi_packet_template_edge_mass']}",
        f"multi_m_value_template_count={audit['multi_m_value_template_count']}",
        f"multi_m_value_template_edge_mass={audit['multi_m_value_template_edge_mass']}",
        f"high_edge_gt12_template_count={audit['high_edge_gt12_template_count']}",
        f"high_edge_gt12_edge_mass={audit['high_edge_gt12_edge_mass']}",
        f"template_edge_mass_min/median/max={audit['template_edge_mass_min']}/{audit['template_edge_mass_median']}/{audit['template_edge_mass_max']}",
        f"cycle_length_min/median/max={audit['cycle_length_min']}/{audit['cycle_length_median']}/{audit['cycle_length_max']}",
        f"occurrence_count_min/median/max={audit['occurrence_count_min']}/{audit['occurrence_count_median']}/{audit['occurrence_count_max']}",
        f"observed_template_edge_mass_le_16={str(audit['observed_template_edge_mass_le_16']).lower()}",
        f"observed_occurrence_count_le_4={str(audit['observed_occurrence_count_le_4']).lower()}",
        f"observed_cycle_length_le_14={str(audit['observed_cycle_length_le_14']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "occurrence template count：",
        "",
        *markdown_table(
            audit["occurrence_template_rows"],
            ["occurrence_count", "template_count", "template_ratio"],
        ),
        "",
        "occurrence edge mass：",
        "",
        *markdown_table(
            audit["occurrence_edge_rows"],
            ["occurrence_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "cycle length template count：",
        "",
        *markdown_table(
            audit["cycle_length_template_rows"],
            ["cycle_length", "template_count", "template_ratio"],
        ),
        "",
        "packet support edge mass：",
        "",
        *markdown_table(
            audit["packet_support_edge_rows"],
            ["packet_support_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "m-value support edge mass：",
        "",
        *markdown_table(
            audit["m_value_support_edge_rows"],
            ["m_value_support_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "cycle-occurrence factor rows：",
        "",
        *markdown_table(
            audit["cycle_occurrence_factor_rows"],
            ["cycle_length", "occurrence_count", "template_edge_mass", "template_count", "template_ratio"],
        ),
        "",
        "最高 local templates：",
        "",
        *markdown_table(
            audit["top_template_multiplicity_rows"],
            [
                "signed_child",
                "raw_base_template",
                "P",
                "edge_mass",
                "cycle_length",
                "occurrence_count",
                "packet_support_count",
                "m_value_support_count",
                "route_class",
                "A_class",
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
        "结论：local template multiplicity 已被拆成 cycle length、occurrence count",
        "与二者乘积三个门。该账本仍是有限结构结果，尚未给出全局均匀界。",
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
        f"single_P_local_template_multiplicity_factor_ledger_closed={str(payload['single_P_local_template_multiplicity_factor_ledger_closed']).lower()}",
        f"local_cycle_length_uniform_bound_proved={str(payload['local_cycle_length_uniform_bound_proved']).lower()}",
        f"local_occurrence_multiplicity_uniform_bound_proved={str(payload['local_occurrence_multiplicity_uniform_bound_proved']).lower()}",
        f"cycle_occurrence_product_bound_proved={str(payload['cycle_occurrence_product_bound_proved']).lower()}",
        f"local_template_multiplicity_uniform_bound_proved={str(payload['local_template_multiplicity_uniform_bound_proved']).lower()}",
        f"single_P_slice_endpoint_packet_summation_closed={str(payload['single_P_slice_endpoint_packet_summation_closed']).lower()}",
        f"single_P_local_endpoint_packet_bound_closed={str(payload['single_P_local_endpoint_packet_bound_closed']).lower()}",
        f"multi_P_trace_completion_closed={str(payload['multi_P_trace_completion_closed']).lower()}",
        f"pure_endpoint_carrier_phase_saving_closed={str(payload['pure_endpoint_carrier_phase_saving_closed']).lower()}",
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
        "single_P_local_template_multiplicity_factor_ledger_closed="
        f"{payload['single_P_local_template_multiplicity_factor_ledger_closed']}"
    )
    print(f"template_edge_mass_max={audit['template_edge_mass_max']}")
    print(f"occurrence_count_max={audit['occurrence_count_max']}")
    print(f"cycle_length_max={audit['cycle_length_max']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
