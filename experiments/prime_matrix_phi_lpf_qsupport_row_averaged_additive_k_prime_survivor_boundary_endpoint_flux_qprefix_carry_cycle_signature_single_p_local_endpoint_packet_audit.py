#!/usr/bin/env python3
"""审计 pure endpoint 中 single-P local endpoint packets 的局部结构。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_endpoint_packet_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet-audit.json

上一层把 pure endpoint 主体拆成 single-P local packets 与 multi-P trace
candidates。本层只处理 single-P 支路，记录其局部模板、P 切片、endpoint route
与外部定理不可直接进入的位置。该层关闭的是有限结构账本，不证明全局相消。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit as carrier  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PURE_ENDPOINT_INTERFACE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface-audit.json"
)

DEPENDENCIES = [
    PURE_ENDPOINT_INTERFACE_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router-audit.json",
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
        "role": "not directly applicable to single-P local packets without a long completed trace family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "not directly applicable until a bilinear Kloosterman variable pair is extracted",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "not directly applicable to width-one P-support packets",
    },
    {
        "key": "Xu_Zhang_2026_generalized_kloosterman_arbitrary_sets",
        "url": "https://doi.org/10.1016/j.jnt.2025.09.027",
        "role": "published Kloosterman-set input; still needs explicit finite-field set variables and does not bound width-one packets by itself",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "does not estimate signed single-P local endpoint packets",
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
    """把 Counter 转成稳定表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def template_count_table(counter: Counter[Any], field: str) -> list[dict[str, Any]]:
    """输出模板计数分布。"""
    total = sum(counter.values())
    return [
        {field: key, "template_count": counter[key], "template_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def p_bucket(p_value: int) -> str:
    """把局部 P 切片分桶。"""
    if p_value <= 199:
        return "P_le_199"
    if p_value <= 499:
        return "P_200_to_499"
    if p_value <= 799:
        return "P_500_to_799"
    return "P_800_to_1009"


def q_prefix_bucket(count: int) -> str:
    """把 q-prefix 数量分桶。"""
    if count <= 4:
        return "qprefix_1_to_4"
    if count <= 8:
        return "qprefix_5_to_8"
    if count <= 16:
        return "qprefix_9_to_16"
    if count <= 32:
        return "qprefix_17_to_32"
    return "qprefix_ge_33"


def shell_prime_bucket(count: int) -> str:
    """把 endpoint shell prime 数量分桶。"""
    if count <= 2:
        return "m_shell_1_to_2"
    if count <= 4:
        return "m_shell_3_to_4"
    if count <= 8:
        return "m_shell_5_to_8"
    return "m_shell_ge_9"


def route_superclass(route: str) -> str:
    """将 endpoint route 压成 wing/right-tail 大类。"""
    if route.startswith("pure_right_tail"):
        return "right_tail_single_P_local"
    if route.startswith("pure_upper_wing") or route.startswith("pure_lower_wing"):
        return "wing_single_P_local"
    return "other_single_P_local"


def top_p_rows(
    p_edge_mass: Counter[int],
    p_template_count: Counter[int],
    p_route_mass: dict[int, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高负载 P 切片。"""
    rows = []
    for p_value in sorted(p_edge_mass, key=lambda key: (-p_edge_mass[key], key))[:limit]:
        rows.append(
            {
                "P": p_value,
                "edge_mass": p_edge_mass[p_value],
                "template_count": p_template_count[p_value],
                "route_profile": ",".join(
                    f"{route}:{p_route_mass[p_value][route]}"
                    for route in sorted(
                        p_route_mass[p_value],
                        key=lambda route: (-p_route_mass[p_value][route], route),
                    )
                ),
            }
        )
    return rows


def top_template_rows(
    pure_edge_mass: Counter[str],
    template_p_value: dict[str, int],
    template_route: dict[str, str],
    template_a_class: dict[str, str],
    template_base: dict[str, str],
    template_q_prefix_counts: dict[str, Counter[int]],
    template_m_shell_counts: dict[str, Counter[int]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量 single-P 局部模板。"""
    rows = []
    for template in sorted(pure_edge_mass, key=lambda key: (-pure_edge_mass[key], key))[:limit]:
        rows.append(
            {
                "signed_child": template,
                "raw_base_template": template_base[template],
                "P": template_p_value[template],
                "edge_mass": pure_edge_mass[template],
                "route_class": template_route[template],
                "route_superclass": route_superclass(template_route[template]),
                "A_class": template_a_class[template],
                "q_prefix_profile": ",".join(
                    f"{key}:{template_q_prefix_counts[template][key]}"
                    for key in sorted(template_q_prefix_counts[template])
                ),
                "m_shell_prime_profile": ",".join(
                    f"{key}:{template_m_shell_counts[template][key]}"
                    for key in sorted(template_m_shell_counts[template])
                ),
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 single-P local endpoint packets。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(PURE_ENDPOINT_INTERFACE_AUDIT.read_text())
    previous = previous_payload["finite_audit"]

    template_edge_mass: Counter[str] = Counter()
    template_p_sets: dict[str, set[int]] = defaultdict(set)
    template_p_mass: dict[str, Counter[int]] = defaultdict(Counter)
    template_route_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_endpoint_group_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_q_prefix_counts: dict[str, Counter[int]] = defaultdict(Counter)
    template_m_shell_counts: dict[str, Counter[int]] = defaultdict(Counter)
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
                template_p_sets[template].add(packet["P"])
                template_p_mass[template][packet["P"]] += length
                template_strip_counts[template][packet["strip"]] += length
                template_endpoint_group_counts[template][endpoint_group] += length
                template_q_prefix_counts[template][packet["q_prefix_count"]] += length
                template_m_shell_counts[template][packet["m_shell_prime_count"]] += length
                template_route_counts[template][endpoint_group] += length
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
        if not route.startswith("pure_"):
            continue
        pure_edge_mass[template] = mass
        template_route[template] = route

    single_edge_mass: Counter[str] = Counter()
    template_p_value: dict[str, int] = {}
    for template, mass in pure_edge_mass.items():
        if len(template_p_sets[template]) != 1:
            continue
        single_edge_mass[template] = mass
        template_p_value[template] = next(iter(template_p_sets[template]))

    route_edge_mass: Counter[str] = Counter()
    route_template_count: Counter[str] = Counter()
    route_super_edge_mass: Counter[str] = Counter()
    a_class_edge_mass: Counter[str] = Counter()
    p_edge_mass: Counter[int] = Counter()
    p_template_count: Counter[int] = Counter()
    p_bucket_edge_mass: Counter[str] = Counter()
    p_route_mass: dict[int, Counter[str]] = defaultdict(Counter)
    template_mass_distribution: Counter[int] = Counter()
    template_cycle_length_edge_mass: Counter[int] = Counter()
    q_prefix_edge_mass: Counter[str] = Counter()
    m_shell_edge_mass: Counter[str] = Counter()

    for template, mass in single_edge_mass.items():
        route = template_route[template]
        p_value = template_p_value[template]
        route_edge_mass[route] += mass
        route_template_count[route] += 1
        route_super_edge_mass[route_superclass(route)] += mass
        a_class_edge_mass[template_a_class[template]] += mass
        p_edge_mass[p_value] += mass
        p_template_count[p_value] += 1
        p_bucket_edge_mass[p_bucket(p_value)] += mass
        p_route_mass[p_value][route] += mass
        template_mass_distribution[mass] += 1
        template_cycle_length_edge_mass[template_cycle_length[template]] += mass
        for count, count_mass in template_q_prefix_counts[template].items():
            q_prefix_edge_mass[q_prefix_bucket(count)] += count_mass
        for count, count_mass in template_m_shell_counts[template].items():
            m_shell_edge_mass[shell_prime_bucket(count)] += count_mass

    single_total = sum(single_edge_mass.values())
    p_values = sorted(p_edge_mass)
    p_masses = list(p_edge_mass.values())
    template_masses = list(single_edge_mass.values())
    ledger_closed = (
        previous["pure_endpoint_phase_interface_ledger_closed"]
        and single_total == previous["single_P_pure_endpoint_edge_mass"]
        and all(len(template_p_sets[template]) == 1 for template in single_edge_mass)
        and sum(route_edge_mass.values()) == single_total
        and sum(route_super_edge_mass.values()) == single_total
        and sum(a_class_edge_mass.values()) == single_total
        and sum(p_edge_mass.values()) == single_total
        and sum(q_prefix_edge_mass.values()) == single_total
        and sum(m_shell_edge_mass.values()) == single_total
    )

    return {
        "max_prime": max_prime,
        "previous_pure_endpoint_phase_interface_ledger_closed": previous[
            "pure_endpoint_phase_interface_ledger_closed"
        ],
        "single_P_local_endpoint_structure_ledger_closed": ledger_closed,
        "single_P_local_endpoint_edge_mass": single_total,
        "single_P_local_endpoint_template_count": len(single_edge_mass),
        "single_P_support_prime_count": len(p_edge_mass),
        "single_P_support_P_min": min(p_values),
        "single_P_support_P_max": max(p_values),
        "single_P_edge_mass_per_P_min": min(p_masses),
        "single_P_edge_mass_per_P_median": statistics.median(p_masses),
        "single_P_edge_mass_per_P_max": max(p_masses),
        "single_P_templates_per_P_min": min(p_template_count.values()),
        "single_P_templates_per_P_median": statistics.median(p_template_count.values()),
        "single_P_templates_per_P_max": max(p_template_count.values()),
        "single_P_template_edge_mass_min": min(template_masses),
        "single_P_template_edge_mass_median": statistics.median(template_masses),
        "single_P_template_edge_mass_max": max(template_masses),
        "single_P_route_edge_rows": table_from_counter(route_edge_mass, single_total, "route_class"),
        "single_P_route_template_rows": template_count_table(route_template_count, "route_class"),
        "single_P_route_superclass_edge_rows": table_from_counter(
            route_super_edge_mass, single_total, "route_superclass"
        ),
        "single_P_A_class_edge_rows": table_from_counter(a_class_edge_mass, single_total, "A_class"),
        "single_P_P_bucket_edge_rows": table_from_counter(p_bucket_edge_mass, single_total, "P_bucket"),
        "single_P_template_mass_distribution_rows": template_count_table(
            template_mass_distribution, "template_edge_mass"
        ),
        "single_P_cycle_length_edge_rows": table_from_counter(
            template_cycle_length_edge_mass, single_total, "cycle_length"
        ),
        "single_P_q_prefix_bucket_edge_rows": table_from_counter(
            q_prefix_edge_mass, single_total, "q_prefix_bucket"
        ),
        "single_P_m_shell_bucket_edge_rows": table_from_counter(
            m_shell_edge_mass, single_total, "m_shell_bucket"
        ),
        "top_single_P_slice_rows": top_p_rows(p_edge_mass, p_template_count, p_route_mass),
        "top_single_P_template_rows": top_template_rows(
            single_edge_mass,
            template_p_value,
            template_route,
            template_a_class,
            template_base,
            template_q_prefix_counts,
            template_m_shell_counts,
        ),
        "observed_local_template_edge_mass_le_16": max(template_masses) <= 16,
        "observed_width_one_route_superclass_balance_gap": abs(
            route_super_edge_mass["right_tail_single_P_local"]
            - route_super_edge_mass["wing_single_P_local"]
        ),
        "local_template_multiplicity_uniform_bound_proved": False,
        "single_P_slice_endpoint_packet_summation_closed": False,
        "single_P_local_endpoint_packet_bound_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_endpoint_packet_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_endpoint_structure_ledger_closed_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the latest narrowest mouth begins with SinglePLocalPureEndpointPacketBound",
        "current_object": {
            "input": "single-P local packets inside pure endpoint missing-mirror support",
            "operation": "local template, P-slice, route, and endpoint-shell decomposition",
            "dominant_shape": "many small width-one local templates, with edge mass split almost evenly between wing and right-tail superclasses",
            "remaining": "uniform local template multiplicity and P-slice summation or a named PDEC/SAE return route",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PureEndpointPhaseInterfaceImported",
                finite_audit["previous_pure_endpoint_phase_interface_ledger_closed"],
                finite_audit["previous_pure_endpoint_phase_interface_ledger_closed"],
                "The previous pure endpoint phase-interface ledger is imported.",
                "none for import",
            ),
            gate(
                "SinglePLocalEndpointStructureLedger",
                finite_audit["single_P_local_endpoint_structure_ledger_closed"],
                finite_audit["single_P_local_endpoint_structure_ledger_closed"],
                "The single-P local mass is decomposed by route, A-class, P-slice, q-prefix, and shell-prime load.",
                "none for the finite structure ledger",
            ),
            gate(
                "LocalTemplateMultiplicityUniformBound",
                False,
                False,
                "Promote the observed bounded local template masses to a uniform proof.",
                "requires an analytic or structural multiplicity argument, not just the finite ledger",
            ),
            gate(
                "SinglePSliceEndpointPacketSummationOrPDEC",
                False,
                False,
                "Sum the width-one local packets over P-slices without parity loss, or return failures to a named PDEC/SAE route.",
                "requires global P-slice summation or a formal defect route",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "does not enter before width-one local packets are lifted to a genuine trace family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "does not bound single-P local packets without extracted bilinear Kloosterman variables",
            "Wright_unbalanced_Kloosterman": "does not address P-support width one",
            "Xu_Zhang_generalized_Kloosterman_arbitrary_sets": "published external check; still requires explicit finite-field set variables and is not a direct local packet bound",
            "Li_short_interval_x_052": "irrelevant to signed carrier phase saving",
        },
        "latest_narrowest_mouth": [
            "LocalTemplateMultiplicityUniformBound",
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
        "single_P_local_endpoint_structure_ledger_closed": finite_audit[
            "single_P_local_endpoint_structure_ledger_closed"
        ],
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local endpoint packet 审计",
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
        "## 2. single-P local endpoint packet 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_endpoint_structure_ledger_closed={str(audit['single_P_local_endpoint_structure_ledger_closed']).lower()}",
        f"single_P_local_endpoint_edge_mass={audit['single_P_local_endpoint_edge_mass']}",
        f"single_P_local_endpoint_template_count={audit['single_P_local_endpoint_template_count']}",
        f"single_P_support_prime_count={audit['single_P_support_prime_count']}",
        f"single_P_support_P_min/max={audit['single_P_support_P_min']}/{audit['single_P_support_P_max']}",
        f"single_P_edge_mass_per_P_min/median/max={audit['single_P_edge_mass_per_P_min']}/{audit['single_P_edge_mass_per_P_median']}/{audit['single_P_edge_mass_per_P_max']}",
        f"single_P_template_edge_mass_min/median/max={audit['single_P_template_edge_mass_min']}/{audit['single_P_template_edge_mass_median']}/{audit['single_P_template_edge_mass_max']}",
        f"observed_local_template_edge_mass_le_16={str(audit['observed_local_template_edge_mass_le_16']).lower()}",
        f"observed_width_one_route_superclass_balance_gap={audit['observed_width_one_route_superclass_balance_gap']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "route superclass edge mass：",
        "",
        *markdown_table(
            audit["single_P_route_superclass_edge_rows"],
            ["route_superclass", "edge_mass", "edge_ratio"],
        ),
        "",
        "route edge mass：",
        "",
        *markdown_table(audit["single_P_route_edge_rows"], ["route_class", "edge_mass", "edge_ratio"]),
        "",
        "A-class edge mass：",
        "",
        *markdown_table(audit["single_P_A_class_edge_rows"], ["A_class", "edge_mass", "edge_ratio"]),
        "",
        "P bucket edge mass：",
        "",
        *markdown_table(audit["single_P_P_bucket_edge_rows"], ["P_bucket", "edge_mass", "edge_ratio"]),
        "",
        "template edge-mass distribution：",
        "",
        *markdown_table(
            audit["single_P_template_mass_distribution_rows"],
            ["template_edge_mass", "template_count", "template_ratio"],
        ),
        "",
        "cycle length edge mass：",
        "",
        *markdown_table(audit["single_P_cycle_length_edge_rows"], ["cycle_length", "edge_mass", "edge_ratio"]),
        "",
        "q-prefix bucket edge mass：",
        "",
        *markdown_table(
            audit["single_P_q_prefix_bucket_edge_rows"],
            ["q_prefix_bucket", "edge_mass", "edge_ratio"],
        ),
        "",
        "m-shell bucket edge mass：",
        "",
        *markdown_table(
            audit["single_P_m_shell_bucket_edge_rows"],
            ["m_shell_bucket", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高 P-slices：",
        "",
        *markdown_table(audit["top_single_P_slice_rows"], ["P", "edge_mass", "template_count", "route_profile"]),
        "",
        "最高 single-P templates：",
        "",
        *markdown_table(
            audit["top_single_P_template_rows"],
            [
                "signed_child",
                "raw_base_template",
                "P",
                "edge_mass",
                "route_class",
                "route_superclass",
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
        "结论：single-P local endpoint 支路已被压成局部模板重数与 P-slice",
        "求和两个实际门。平均型 trace/Kloosterman theorem 仍不能直接吃掉该支路。",
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
        f"single_P_local_endpoint_structure_ledger_closed={str(payload['single_P_local_endpoint_structure_ledger_closed']).lower()}",
        f"local_template_multiplicity_uniform_bound_proved={str(payload['local_template_multiplicity_uniform_bound_proved']).lower()}",
        f"single_P_slice_endpoint_packet_summation_closed={str(payload['single_P_slice_endpoint_packet_summation_closed']).lower()}",
        f"single_P_local_endpoint_packet_bound_closed={str(payload['single_P_local_endpoint_packet_bound_closed']).lower()}",
        f"multi_P_trace_completion_closed={str(payload['multi_P_trace_completion_closed']).lower()}",
        f"pure_endpoint_carrier_phase_saving_closed={str(payload['pure_endpoint_carrier_phase_saving_closed']).lower()}",
        f"mixed_right_tail_endpoint_router_no_loss_closed={str(payload['mixed_right_tail_endpoint_router_no_loss_closed']).lower()}",
        f"unequal_mirror_pair_residual_phase_saving_closed={str(payload['unequal_mirror_pair_residual_phase_saving_closed']).lower()}",
        f"thin_P_support_carrier_summation_closed={str(payload['thin_P_support_carrier_summation_closed']).lower()}",
        f"residual_endpoint_path_summation_closed={str(payload['residual_endpoint_path_summation_closed']).lower()}",
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
        "single_P_local_endpoint_structure_ledger_closed="
        f"{payload['single_P_local_endpoint_structure_ledger_closed']}"
    )
    print(f"single_P_local_endpoint_edge_mass={audit['single_P_local_endpoint_edge_mass']}")
    print(
        "single_P_template_edge_mass_max="
        f"{audit['single_P_template_edge_mass_max']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
