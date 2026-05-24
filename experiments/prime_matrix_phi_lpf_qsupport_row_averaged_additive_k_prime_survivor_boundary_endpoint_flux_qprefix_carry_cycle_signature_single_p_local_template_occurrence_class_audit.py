#!/usr/bin/env python3
"""审计 single-P local repeated templates 的 occurrence 分类。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_occurrence_class_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-occurrence-class-audit.json

上一层把 single-P local template edge mass 拆成 cycle_length * occurrence_count。
本层只继续拆 occurrence_count>1 的 97 个重复模板，把它们分成同 packet 跨 m、
跨 packet、同 packet 同 m 多 cycle 三类。该层关闭有限分类账本，不证明全局重数界。
"""

from __future__ import annotations

import hashlib
import json
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
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "template-occurrence-class"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_TEMPLATE_MULTIPLICITY_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_TEMPLATE_MULTIPLICITY_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet-audit.json",
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
        "role": "bilinear trace input; does not prove local repeated-template collision bounds",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman average; needs extracted bilinear variables",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced convolution input; does not bound width-one occurrence collisions",
    },
    {
        "key": "Pascadi_2025_nonabelian_amplification_kloosterman",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "composite-modulus Type-II input; still needs a bilinear family, not a single local collision",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2025_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "square-free/smooth parameter input; does not control repeated signed local templates",
    },
    {
        "key": "Xu_Zhang_2026_generalized_kloosterman_arbitrary_sets",
        "url": "https://doi.org/10.1016/j.jnt.2025.09.027",
        "role": "arbitrary-set bilinear input; still requires explicit finite-field set variables",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "prime existence input; not an occurrence-collision theorem",
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


def compact_location(records: list[dict[str, Any]], limit: int = 4) -> str:
    """压缩 occurrence 位置，避免 Markdown 表过长。"""
    parts = []
    for record in records[:limit]:
        parts.append(
            "pkt={packet_index},m={m_value},q={q_prefix_count},s={m_shell_prime_count}".format(
                **record
            )
        )
    if len(records) > limit:
        parts.append(f"...+{len(records) - limit}")
    return "; ".join(parts)


def repeated_class(records: list[dict[str, Any]]) -> str:
    """按 occurrence 支撑给重复模板分类。"""
    packet_support = {record["packet_index"] for record in records}
    m_value_support = {record["m_value"] for record in records}
    packet_m_support = {(record["packet_index"], record["m_value"]) for record in records}
    if len(packet_support) > 1:
        return "multi_packet_repeated_template"
    if len(m_value_support) > 1:
        return "single_packet_multi_m_repeated_template"
    if len(packet_m_support) < len(records):
        return "single_packet_single_m_multi_cycle_template"
    return "unclassified_repeated_template"


def support_signature(records: list[dict[str, Any]], cycle_length: int, edge_mass: int) -> tuple[int, ...]:
    """生成重复模板的支撑签名。"""
    return (
        len({record["packet_index"] for record in records}),
        len({record["m_value"] for record in records}),
        len({record["q_prefix_count"] for record in records}),
        len({record["m_shell_prime_count"] for record in records}),
        len({record["strip"] for record in records}),
        len(records),
        cycle_length,
        edge_mass,
    )


def support_signature_rows(counter: Counter[tuple[int, ...]]) -> list[dict[str, Any]]:
    """输出支撑签名表。"""
    total = sum(counter.values())
    rows = []
    for key in sorted(counter, key=lambda item: (-counter[item], item)):
        rows.append(
            {
                "packet_support_count": key[0],
                "m_value_support_count": key[1],
                "q_prefix_support_count": key[2],
                "m_shell_support_count": key[3],
                "strip_support_count": key[4],
                "occurrence_count": key[5],
                "cycle_length": key[6],
                "template_edge_mass": key[7],
                "template_count": counter[key],
                "template_ratio": counter[key] / total,
            }
        )
    return rows


def class_route_rows(counter: Counter[tuple[str, str]], total: int) -> list[dict[str, Any]]:
    """输出 occurrence class 与 route 的交叉表。"""
    rows = []
    for occurrence_class, route in sorted(
        counter,
        key=lambda key: (-counter[key], key[0], key[1]),
    ):
        rows.append(
            {
                "occurrence_class": occurrence_class,
                "route_class": route,
                "edge_mass": counter[(occurrence_class, route)],
                "edge_ratio": counter[(occurrence_class, route)] / total,
            }
        )
    return rows


def top_repeated_rows(
    templates: list[str],
    edge_mass: Counter[str],
    cycle_length: dict[str, int],
    records: dict[str, list[dict[str, Any]]],
    p_value: dict[str, int],
    route: dict[str, str],
    a_class: dict[str, str],
    base_template: dict[str, str],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量的重复模板。"""
    rows = []
    for template in sorted(
        templates,
        key=lambda key: (-edge_mass[key], -len(records[key]), -cycle_length[key], key),
    )[:limit]:
        template_records = records[template]
        rows.append(
            {
                "signed_child": template,
                "raw_base_template": base_template[template],
                "P": p_value[template],
                "edge_mass": edge_mass[template],
                "cycle_length": cycle_length[template],
                "occurrence_count": len(template_records),
                "occurrence_class": repeated_class(template_records),
                "packet_support_count": len({record["packet_index"] for record in template_records}),
                "m_value_support_count": len({record["m_value"] for record in template_records}),
                "q_prefix_support_count": len(
                    {record["q_prefix_count"] for record in template_records}
                ),
                "m_shell_support_count": len(
                    {record["m_shell_prime_count"] for record in template_records}
                ),
                "route_class": route[template],
                "route_superclass": single_p.route_superclass(route[template]),
                "A_class": a_class[template],
                "occurrence_locations": compact_location(template_records),
            }
        )
    return rows


def collect_single_p_templates(max_prime: int) -> dict[str, Any]:
    """重建 single-P local pure endpoint templates 与 occurrence 记录。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)

    template_edge_mass: Counter[str] = Counter()
    template_occurrence_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    template_p_sets: dict[str, set[int]] = defaultdict(set)
    template_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_endpoint_group_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_mirror: dict[str, str] = {}
    template_base: dict[str, str] = {}
    template_a_class: dict[str, str] = {}
    template_cycle_length: dict[str, int] = {}

    for packet_index, packet in enumerate(packets):
        endpoint_profile = flow.qprefix_atom.endpoint_profile_for_packet(
            packet, fibres_by_row, primes
        )
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

            for cycle_index, cycle in enumerate(signed_cycles):
                template = signature.signed_template(cycle)
                length = len(cycle)
                template_edge_mass[template] += length
                template_occurrence_records[template].append(
                    {
                        "packet_index": packet_index,
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "m_value": m_value,
                        "q_prefix_count": packet["q_prefix_count"],
                        "m_shell_prime_count": packet["m_shell_prime_count"],
                        "endpoint_group": endpoint_group,
                        "cycle_index": cycle_index,
                        "cycle_length": length,
                    }
                )
                template_p_sets[template].add(packet["P"])
                template_strip_counts[template][packet["strip"]] += length
                template_endpoint_group_counts[template][endpoint_group] += length
                template_mirror[template] = mirror.signed_mirror_template(cycle)
                template_base[template] = signature.raw_template(
                    [(item[0], item[1]) for item in cycle]
                )
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

    return {
        "single_edge_mass": single_edge_mass,
        "template_occurrence_records": template_occurrence_records,
        "template_cycle_length": template_cycle_length,
        "template_p_value": template_p_value,
        "template_route": template_route,
        "template_a_class": template_a_class,
        "template_base": template_base,
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 repeated template occurrence classes。"""
    previous_payload = json.loads(PREVIOUS_TEMPLATE_MULTIPLICITY_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    data = collect_single_p_templates(max_prime)
    single_edge_mass: Counter[str] = data["single_edge_mass"]
    occurrence_records: dict[str, list[dict[str, Any]]] = data["template_occurrence_records"]
    cycle_length: dict[str, int] = data["template_cycle_length"]
    template_p_value: dict[str, int] = data["template_p_value"]
    template_route: dict[str, str] = data["template_route"]

    repeated_templates = [
        template for template in single_edge_mass if len(occurrence_records[template]) > 1
    ]

    class_template_count: Counter[str] = Counter()
    class_edge_mass: Counter[str] = Counter()
    class_route_edge_mass: Counter[tuple[str, str]] = Counter()
    support_counter: Counter[tuple[int, ...]] = Counter()
    packet_support_edge_mass: Counter[int] = Counter()
    m_value_support_edge_mass: Counter[int] = Counter()
    q_prefix_support_edge_mass: Counter[int] = Counter()
    m_shell_support_edge_mass: Counter[int] = Counter()
    strip_support_edge_mass: Counter[int] = Counter()
    occurrence_support_edge_mass: Counter[int] = Counter()
    repeated_p_edge_mass: Counter[int] = Counter()
    unclassified_templates = []

    for template in repeated_templates:
        records = occurrence_records[template]
        occurrence_class = repeated_class(records)
        if occurrence_class == "unclassified_repeated_template":
            unclassified_templates.append(template)
        mass = single_edge_mass[template]
        class_template_count[occurrence_class] += 1
        class_edge_mass[occurrence_class] += mass
        class_route_edge_mass[(occurrence_class, template_route[template])] += mass
        support_counter[support_signature(records, cycle_length[template], mass)] += 1
        packet_support_edge_mass[len({record["packet_index"] for record in records})] += mass
        m_value_support_edge_mass[len({record["m_value"] for record in records})] += mass
        q_prefix_support_edge_mass[len({record["q_prefix_count"] for record in records})] += mass
        m_shell_support_edge_mass[len({record["m_shell_prime_count"] for record in records})] += mass
        strip_support_edge_mass[len({record["strip"] for record in records})] += mass
        occurrence_support_edge_mass[len(records)] += mass
        repeated_p_edge_mass[template_p_value[template]] += mass

    repeated_edge_mass = sum(single_edge_mass[template] for template in repeated_templates)
    total_edge_mass = sum(single_edge_mass.values())
    max_packet_support = max(packet_support_edge_mass) if packet_support_edge_mass else 0
    max_m_value_support = max(m_value_support_edge_mass) if m_value_support_edge_mass else 0
    max_q_prefix_support = max(q_prefix_support_edge_mass) if q_prefix_support_edge_mass else 0
    max_m_shell_support = max(m_shell_support_edge_mass) if m_shell_support_edge_mass else 0
    max_strip_support = max(strip_support_edge_mass) if strip_support_edge_mass else 0
    max_occurrence = max(occurrence_support_edge_mass) if occurrence_support_edge_mass else 0

    ledger_closed = (
        previous_payload["single_P_local_template_multiplicity_factor_ledger_closed"]
        and total_edge_mass == previous["single_P_local_endpoint_edge_mass"]
        and len(single_edge_mass) == previous["single_P_local_endpoint_template_count"]
        and len(repeated_templates) == previous["repeated_template_count"]
        and repeated_edge_mass == previous["repeated_template_edge_mass"]
        and not unclassified_templates
        and sum(class_template_count.values()) == len(repeated_templates)
        and sum(class_edge_mass.values()) == repeated_edge_mass
        and sum(packet_support_edge_mass.values()) == repeated_edge_mass
        and sum(m_value_support_edge_mass.values()) == repeated_edge_mass
        and sum(q_prefix_support_edge_mass.values()) == repeated_edge_mass
        and sum(m_shell_support_edge_mass.values()) == repeated_edge_mass
        and sum(strip_support_edge_mass.values()) == repeated_edge_mass
        and all(
            cycle_length[template] * len(occurrence_records[template])
            == single_edge_mass[template]
            for template in repeated_templates
        )
    )

    return {
        "max_prime": max_prime,
        "previous_single_P_local_template_multiplicity_factor_ledger_closed": previous_payload[
            "single_P_local_template_multiplicity_factor_ledger_closed"
        ],
        "single_P_local_template_occurrence_class_ledger_closed": ledger_closed,
        "single_P_local_endpoint_edge_mass": total_edge_mass,
        "single_P_local_endpoint_template_count": len(single_edge_mass),
        "repeated_template_count": len(repeated_templates),
        "repeated_template_edge_mass": repeated_edge_mass,
        "repeated_template_edge_ratio": repeated_edge_mass / total_edge_mass,
        "single_packet_multi_m_repeated_template_count": class_template_count[
            "single_packet_multi_m_repeated_template"
        ],
        "single_packet_multi_m_repeated_edge_mass": class_edge_mass[
            "single_packet_multi_m_repeated_template"
        ],
        "multi_packet_repeated_template_count": class_template_count[
            "multi_packet_repeated_template"
        ],
        "multi_packet_repeated_edge_mass": class_edge_mass["multi_packet_repeated_template"],
        "single_packet_single_m_multi_cycle_template_count": class_template_count[
            "single_packet_single_m_multi_cycle_template"
        ],
        "single_packet_single_m_multi_cycle_edge_mass": class_edge_mass[
            "single_packet_single_m_multi_cycle_template"
        ],
        "unclassified_repeated_template_count": len(unclassified_templates),
        "repeated_template_packet_support_count_max": max_packet_support,
        "repeated_template_m_value_support_count_max": max_m_value_support,
        "repeated_template_q_prefix_support_count_max": max_q_prefix_support,
        "repeated_template_m_shell_support_count_max": max_m_shell_support,
        "repeated_template_strip_support_count_max": max_strip_support,
        "repeated_template_occurrence_count_max": max_occurrence,
        "observed_repeated_templates_single_strip": max_strip_support == 1,
        "observed_repeated_packet_support_le_2": max_packet_support <= 2,
        "observed_repeated_m_value_support_le_4": max_m_value_support <= 4,
        "observed_repeated_occurrence_count_le_4": max_occurrence <= 4,
        "occurrence_class_template_rows": template_count_table(
            class_template_count, "occurrence_class"
        ),
        "occurrence_class_edge_rows": table_from_counter(
            class_edge_mass, repeated_edge_mass, "occurrence_class"
        ),
        "occurrence_class_route_edge_rows": class_route_rows(
            class_route_edge_mass, repeated_edge_mass
        ),
        "support_signature_rows": support_signature_rows(support_counter)[:30],
        "packet_support_edge_rows": table_from_counter(
            packet_support_edge_mass, repeated_edge_mass, "packet_support_count"
        ),
        "m_value_support_edge_rows": table_from_counter(
            m_value_support_edge_mass, repeated_edge_mass, "m_value_support_count"
        ),
        "q_prefix_support_edge_rows": table_from_counter(
            q_prefix_support_edge_mass, repeated_edge_mass, "q_prefix_support_count"
        ),
        "m_shell_support_edge_rows": table_from_counter(
            m_shell_support_edge_mass, repeated_edge_mass, "m_shell_support_count"
        ),
        "strip_support_edge_rows": table_from_counter(
            strip_support_edge_mass, repeated_edge_mass, "strip_support_count"
        ),
        "occurrence_count_edge_rows": table_from_counter(
            occurrence_support_edge_mass, repeated_edge_mass, "occurrence_count"
        ),
        "top_repeated_p_rows": table_from_counter(repeated_p_edge_mass, repeated_edge_mass, "P")[
            :20
        ],
        "top_repeated_template_rows": top_repeated_rows(
            repeated_templates,
            single_edge_mass,
            cycle_length,
            occurrence_records,
            template_p_value,
            template_route,
            data["template_a_class"],
            data["template_base"],
        ),
        "single_packet_multi_m_collision_bound_proved": False,
        "multi_packet_duplicate_transport_bound_proved": False,
        "single_packet_single_m_multi_cycle_suppression_proved": False,
        "repeated_occurrence_aggregation_or_pdec_closed": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_occurrence_class_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_template_occurrence_class_ledger_closed_uniform_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the repeated-template part is the narrowest subgate of LocalOccurrenceMultiplicityUniformBound",
        "current_object": {
            "input": "the 97 single-P local endpoint templates with occurrence_count>1",
            "operation": "classify repeated occurrences by packet, m-value and local cycle support",
            "dominant_shape": "all repeated templates stay inside one strip; most are same-packet multi-m collisions",
            "remaining": "prove uniform collision bounds or route repeated excess to PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SinglePLocalTemplateMultiplicityImported",
                finite_audit[
                    "previous_single_P_local_template_multiplicity_factor_ledger_closed"
                ],
                finite_audit[
                    "previous_single_P_local_template_multiplicity_factor_ledger_closed"
                ],
                "The previous cycle_length times occurrence_count factor ledger is imported.",
                "none for import",
            ),
            gate(
                "RepeatedTemplateOccurrenceClassLedger",
                finite_audit["single_P_local_template_occurrence_class_ledger_closed"],
                finite_audit["single_P_local_template_occurrence_class_ledger_closed"],
                "Every repeated template is classified as same-packet multi-m, multi-packet, or same-m multi-cycle.",
                "none for the finite classification ledger",
            ),
            gate(
                "SinglePacketMultiMCollisionBound",
                False,
                False,
                "Promote same-packet multi-m collision sparsity to a structural bound.",
                "finite audit shows 78 templates / 720 edge mass but gives no global theorem",
            ),
            gate(
                "MultiPacketDuplicateTransportBound",
                False,
                False,
                "Control repeated templates transported across packets.",
                "finite audit shows 17 templates / 136 edge mass but no global transport bound",
            ),
            gate(
                "SinglePacketSingleMMultiCycleSuppression",
                False,
                False,
                "Suppress multiple cycles inside one packet and one m-value.",
                "finite audit shows 2 templates / 16 edge mass but no global exclusion",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_average_inputs": "do not directly control width-one local repeated-template collisions",
            "arbitrary_set_inputs": "need explicit finite-field sets and a summation variable not present in a single local collision",
            "short_interval_prime_inputs": "do not estimate signed endpoint occurrence classes",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND SinglePacketMultiMCollisionBound",
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
        "single_P_local_template_occurrence_class_ledger_closed": finite_audit[
            "single_P_local_template_occurrence_class_ledger_closed"
        ],
        "single_packet_multi_m_collision_bound_proved": False,
        "multi_packet_duplicate_transport_bound_proved": False,
        "single_packet_single_m_multi_cycle_suppression_proved": False,
        "repeated_occurrence_aggregation_or_pdec_closed": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local template occurrence class 审计",
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
        "## 2. repeated occurrence 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_template_occurrence_class_ledger_closed={str(audit['single_P_local_template_occurrence_class_ledger_closed']).lower()}",
        f"single_P_local_endpoint_edge_mass={audit['single_P_local_endpoint_edge_mass']}",
        f"single_P_local_endpoint_template_count={audit['single_P_local_endpoint_template_count']}",
        f"repeated_template_count={audit['repeated_template_count']}",
        f"repeated_template_edge_mass={audit['repeated_template_edge_mass']}",
        f"repeated_template_edge_ratio={audit['repeated_template_edge_ratio']}",
        f"single_packet_multi_m_repeated_template_count={audit['single_packet_multi_m_repeated_template_count']}",
        f"single_packet_multi_m_repeated_edge_mass={audit['single_packet_multi_m_repeated_edge_mass']}",
        f"multi_packet_repeated_template_count={audit['multi_packet_repeated_template_count']}",
        f"multi_packet_repeated_edge_mass={audit['multi_packet_repeated_edge_mass']}",
        f"single_packet_single_m_multi_cycle_template_count={audit['single_packet_single_m_multi_cycle_template_count']}",
        f"single_packet_single_m_multi_cycle_edge_mass={audit['single_packet_single_m_multi_cycle_edge_mass']}",
        f"unclassified_repeated_template_count={audit['unclassified_repeated_template_count']}",
        f"repeated_template_packet_support_count_max={audit['repeated_template_packet_support_count_max']}",
        f"repeated_template_m_value_support_count_max={audit['repeated_template_m_value_support_count_max']}",
        f"repeated_template_q_prefix_support_count_max={audit['repeated_template_q_prefix_support_count_max']}",
        f"repeated_template_m_shell_support_count_max={audit['repeated_template_m_shell_support_count_max']}",
        f"repeated_template_strip_support_count_max={audit['repeated_template_strip_support_count_max']}",
        f"repeated_template_occurrence_count_max={audit['repeated_template_occurrence_count_max']}",
        f"observed_repeated_templates_single_strip={str(audit['observed_repeated_templates_single_strip']).lower()}",
        f"observed_repeated_packet_support_le_2={str(audit['observed_repeated_packet_support_le_2']).lower()}",
        f"observed_repeated_m_value_support_le_4={str(audit['observed_repeated_m_value_support_le_4']).lower()}",
        f"observed_repeated_occurrence_count_le_4={str(audit['observed_repeated_occurrence_count_le_4']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "occurrence class template count：",
        "",
        *markdown_table(
            audit["occurrence_class_template_rows"],
            ["occurrence_class", "template_count", "template_ratio"],
        ),
        "",
        "occurrence class edge mass：",
        "",
        *markdown_table(
            audit["occurrence_class_edge_rows"],
            ["occurrence_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "occurrence class route edge mass：",
        "",
        *markdown_table(
            audit["occurrence_class_route_edge_rows"],
            ["occurrence_class", "route_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "support signature rows：",
        "",
        *markdown_table(
            audit["support_signature_rows"],
            [
                "packet_support_count",
                "m_value_support_count",
                "q_prefix_support_count",
                "m_shell_support_count",
                "strip_support_count",
                "occurrence_count",
                "cycle_length",
                "template_edge_mass",
                "template_count",
                "template_ratio",
            ],
        ),
        "",
        "q-prefix support edge mass：",
        "",
        *markdown_table(
            audit["q_prefix_support_edge_rows"],
            ["q_prefix_support_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "m-shell support edge mass：",
        "",
        *markdown_table(
            audit["m_shell_support_edge_rows"],
            ["m_shell_support_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "strip support edge mass：",
        "",
        *markdown_table(
            audit["strip_support_edge_rows"],
            ["strip_support_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "top repeated P rows：",
        "",
        *markdown_table(audit["top_repeated_p_rows"], ["P", "edge_mass", "edge_ratio"]),
        "",
        "最高 repeated templates：",
        "",
        *markdown_table(
            audit["top_repeated_template_rows"],
            [
                "signed_child",
                "P",
                "edge_mass",
                "cycle_length",
                "occurrence_count",
                "occurrence_class",
                "packet_support_count",
                "m_value_support_count",
                "q_prefix_support_count",
                "m_shell_support_count",
                "route_class",
                "occurrence_locations",
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
        "结论：repeated occurrence 已拆成三个可审计局部类。该账本仍是有限结构结果，",
        "尚未给出全局 collision bound，也尚未完成 PDEC/SAE 回流。",
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
        f"single_P_local_template_occurrence_class_ledger_closed={str(payload['single_P_local_template_occurrence_class_ledger_closed']).lower()}",
        f"single_packet_multi_m_collision_bound_proved={str(payload['single_packet_multi_m_collision_bound_proved']).lower()}",
        f"multi_packet_duplicate_transport_bound_proved={str(payload['multi_packet_duplicate_transport_bound_proved']).lower()}",
        f"single_packet_single_m_multi_cycle_suppression_proved={str(payload['single_packet_single_m_multi_cycle_suppression_proved']).lower()}",
        f"repeated_occurrence_aggregation_or_pdec_closed={str(payload['repeated_occurrence_aggregation_or_pdec_closed']).lower()}",
        f"local_occurrence_multiplicity_uniform_bound_proved={str(payload['local_occurrence_multiplicity_uniform_bound_proved']).lower()}",
        f"local_template_multiplicity_uniform_bound_proved={str(payload['local_template_multiplicity_uniform_bound_proved']).lower()}",
        f"single_P_slice_endpoint_packet_summation_closed={str(payload['single_P_slice_endpoint_packet_summation_closed']).lower()}",
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
        "single_P_local_template_occurrence_class_ledger_closed="
        f"{payload['single_P_local_template_occurrence_class_ledger_closed']}"
    )
    print(f"repeated_template_count={audit['repeated_template_count']}")
    print(f"single_packet_multi_m_repeated_edge_mass={audit['single_packet_multi_m_repeated_edge_mass']}")
    print(f"multi_packet_repeated_edge_mass={audit['multi_packet_repeated_edge_mass']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
