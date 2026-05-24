#!/usr/bin/env python3
"""审计 missing-mirror endpoint carriers 的纯端点/混合端点路由。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_endpoint_router_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router-audit.json

上一层已经证明 missing-mirror mass 几乎全是 single-strip endpoint support。
本层继续把 missing signed-child templates 分成纯 endpoint 模板与混合 endpoint
模板，并登记混合模板是否仍局限在 right-tail 内部。这个账本是后续 completion
到 trace/Kloosterman family 前的无损路由检查。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_structure_audit as missing_structure  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit as mirror  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit as carrier  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

STRUCTURE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure-audit.json"
)

DEPENDENCIES = [
    STRUCTURE_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-audit.json",
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
        "role": "needs endpoint-routed missing carriers to be completed as trace-function sums",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "needs explicit bilinear Kloosterman variables after endpoint routing",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "still requires composite Type-II boxes, not just endpoint-routed signed templates",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate only after right-tail routed carriers become unbalanced Kloosterman fractions",
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


def right_tail_group(group: str) -> bool:
    """判断 endpoint group 是否属于 right-tail。"""
    return group.startswith("right_tail")


def route_class(strip_counts: Counter[str], endpoint_counts: Counter[str]) -> str:
    """给 missing template 指定端点路由类。"""
    endpoint_groups = set(endpoint_counts)
    strip_set = set(strip_counts)
    if len(endpoint_groups) == 1:
        endpoint = next(iter(endpoint_groups))
        if len(strip_set) == 1:
            return f"pure_{endpoint}"
        return f"pure_{endpoint}_multi_strip"
    if endpoint_groups and all(right_tail_group(group) for group in endpoint_groups):
        return "mixed_right_tail_endpoint"
    if endpoint_groups and {"upper_wing_single_shell", "lower_wing_single_shell"} & endpoint_groups:
        return "mixed_wing_and_tail_endpoint"
    return "mixed_other_endpoint"


def table_from_counter(counter: Counter[str], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成排序表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], item))
    ]


def top_route_rows(
    route_template_edge_mass: dict[str, Counter[str]],
    template_endpoint_group_counts: dict[str, Counter[str]],
    template_strip_counts: dict[str, Counter[str]],
    template_a_class: dict[str, str],
    template_p_sets: dict[str, set[int]],
    template_base: dict[str, str],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出各 endpoint route 内最高质量模板。"""
    rows = []
    for route, counter in route_template_edge_mass.items():
        for template, mass in counter.most_common(limit):
            rows.append(
                {
                    "route_class": route,
                    "signed_child": template,
                    "raw_base_template": template_base[template],
                    "edge_mass": mass,
                    "A_class": template_a_class[template],
                    "P_support_width": len(template_p_sets[template]),
                    "strip_profile": profile_string(template_strip_counts[template]),
                    "endpoint_group_profile": profile_string(
                        template_endpoint_group_counts[template]
                    ),
                }
            )
    return sorted(rows, key=lambda row: (-row["edge_mass"], row["route_class"]))[:limit]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 missing-mirror endpoint router。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(STRUCTURE_AUDIT.read_text())
    previous = previous_payload["finite_audit"]

    totals: Counter[str] = Counter()
    template_edge_mass: Counter[str] = Counter()
    template_p_sets: dict[str, set[int]] = defaultdict(set)
    template_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_endpoint_group_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_mirror: dict[str, str] = {}
    template_base: dict[str, str] = {}
    template_a_class: dict[str, str] = {}

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
                template_endpoint_group_counts[template][endpoint_group] += length
                template_mirror[template] = mirror.signed_mirror_template(cycle)
                template_base[template] = base
                template_a_class[template] = carrier.a_class(cycle)
                totals["signed_cycle_packet_count"] += 1
                totals["signed_cycle_edge_mass"] += length

    missing_template_edge_mass: Counter[str] = Counter()
    for template, mass in template_edge_mass.items():
        mirror_template = template_mirror[template]
        if mirror_template != template and mirror_template not in template_edge_mass:
            missing_template_edge_mass[template] = mass

    route_edge_mass: Counter[str] = Counter()
    route_template_count: Counter[str] = Counter()
    route_template_edge_mass: dict[str, Counter[str]] = defaultdict(Counter)
    pure_endpoint_edge_mass = 0
    mixed_endpoint_edge_mass = 0
    mixed_right_tail_endpoint_edge_mass = 0
    mixed_wing_tail_endpoint_edge_mass = 0
    single_strip_pure_endpoint_edge_mass = 0
    endpoint_group_widths: list[int] = []
    route_p_widths: dict[str, list[int]] = defaultdict(list)

    for template, mass in missing_template_edge_mass.items():
        endpoint_counts = template_endpoint_group_counts[template]
        strip_counts = template_strip_counts[template]
        route = route_class(strip_counts, endpoint_counts)
        route_edge_mass[route] += mass
        route_template_count[route] += 1
        route_template_edge_mass[route][template] = mass
        route_p_widths[route].append(len(template_p_sets[template]))
        endpoint_width = len(endpoint_counts)
        endpoint_group_widths.append(endpoint_width)
        if endpoint_width == 1:
            pure_endpoint_edge_mass += mass
            if len(strip_counts) == 1:
                single_strip_pure_endpoint_edge_mass += mass
        else:
            mixed_endpoint_edge_mass += mass
            endpoint_groups = set(endpoint_counts)
            if all(right_tail_group(group) for group in endpoint_groups):
                mixed_right_tail_endpoint_edge_mass += mass
            elif {"upper_wing_single_shell", "lower_wing_single_shell"} & endpoint_groups:
                mixed_wing_tail_endpoint_edge_mass += mass

    missing_total = sum(missing_template_edge_mass.values())
    route_rows = [
        {
            "route_class": route,
            "template_count": route_template_count[route],
            "edge_mass": route_edge_mass[route],
            "edge_ratio": route_edge_mass[route] / missing_total,
            "P_support_width_min": min(route_p_widths[route]),
            "P_support_width_median": statistics.median(route_p_widths[route]),
            "P_support_width_max": max(route_p_widths[route]),
        }
        for route in sorted(route_edge_mass, key=lambda item: (-route_edge_mass[item], item))
    ]

    ledger_closed = (
        previous["missing_mirror_structure_ledger_closed"]
        and totals["atom_count_total"] == previous["atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and totals["signed_cycle_packet_count"] == previous["signed_cycle_packet_count"]
        and totals["signed_cycle_edge_mass"] == previous["signed_cycle_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and missing_total == previous["missing_mirror_edge_mass"]
        and len(missing_template_edge_mass) == previous["missing_mirror_pair_count"]
        and pure_endpoint_edge_mass + mixed_endpoint_edge_mass == missing_total
        and sum(route_edge_mass.values()) == missing_total
    )

    return {
        "max_prime": max_prime,
        "previous_missing_mirror_structure_ledger_closed": previous[
            "missing_mirror_structure_ledger_closed"
        ],
        "missing_mirror_endpoint_router_ledger_closed": ledger_closed,
        "atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "signed_cycle_packet_count": totals["signed_cycle_packet_count"],
        "signed_cycle_edge_mass": totals["signed_cycle_edge_mass"],
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "missing_mirror_edge_mass": missing_total,
        "missing_mirror_template_count": len(missing_template_edge_mass),
        "pure_endpoint_template_edge_mass": pure_endpoint_edge_mass,
        "pure_endpoint_template_edge_ratio": pure_endpoint_edge_mass / missing_total,
        "mixed_endpoint_template_edge_mass": mixed_endpoint_edge_mass,
        "mixed_endpoint_template_edge_ratio": mixed_endpoint_edge_mass / missing_total,
        "mixed_right_tail_endpoint_edge_mass": mixed_right_tail_endpoint_edge_mass,
        "mixed_right_tail_endpoint_edge_ratio": mixed_right_tail_endpoint_edge_mass
        / missing_total,
        "mixed_wing_tail_endpoint_edge_mass": mixed_wing_tail_endpoint_edge_mass,
        "mixed_wing_tail_endpoint_edge_ratio": mixed_wing_tail_endpoint_edge_mass
        / missing_total,
        "single_strip_pure_endpoint_edge_mass": single_strip_pure_endpoint_edge_mass,
        "single_strip_pure_endpoint_edge_ratio": single_strip_pure_endpoint_edge_mass
        / missing_total,
        "endpoint_group_width_min": min(endpoint_group_widths),
        "endpoint_group_width_median": statistics.median(endpoint_group_widths),
        "endpoint_group_width_max": max(endpoint_group_widths),
        "endpoint_route_rows": route_rows,
        "endpoint_route_edge_rows": table_from_counter(
            route_edge_mass, missing_total, "route_class"
        ),
        "top_endpoint_route_template_rows": top_route_rows(
            route_template_edge_mass,
            template_endpoint_group_counts,
            template_strip_counts,
            template_a_class,
            template_p_sets,
            template_base,
        ),
        "missing_endpoint_router_ledger_closed_flag": ledger_closed,
        "pure_endpoint_carrier_phase_saving_closed": False,
        "mixed_right_tail_endpoint_router_no_loss_closed": False,
        "missing_mirror_trace_completion_closed": False,
        "unequal_mirror_pair_residual_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_endpoint_router_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "missing_mirror_endpoint_router_ledger_closed_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "missing-mirror endpoint carriers must be routed before any trace/Kloosterman completion can be applied",
        "current_object": {
            "input": "missing-mirror signed-child endpoint support",
            "operation": "pure-endpoint versus mixed-endpoint template routing",
            "dominant_shape": "most mass is pure endpoint; the mixed mass stays in right-tail endpoint mixtures",
            "remaining": "pure endpoint phase saving, right-tail mixed endpoint no-loss routing, and trace/Kloosterman completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "MissingMirrorStructureLedgerImported",
                finite_audit["previous_missing_mirror_structure_ledger_closed"],
                finite_audit["previous_missing_mirror_structure_ledger_closed"],
                "The previous missing-mirror structure ledger is imported.",
                "none for import",
            ),
            gate(
                "MissingMirrorEndpointRouterLedger",
                finite_audit["missing_mirror_endpoint_router_ledger_closed"],
                finite_audit["missing_mirror_endpoint_router_ledger_closed"],
                "Each missing-mirror signed template is routed as pure endpoint or mixed endpoint support.",
                "none for the finite router ledger",
            ),
            gate(
                "PureEndpointCarrierPhaseSaving",
                False,
                False,
                "Prove phase saving on pure endpoint missing-mirror carriers.",
                "requires analytic phase input after route isolation",
            ),
            gate(
                "MixedRightTailEndpointNoLossRouter",
                False,
                False,
                "Split mixed right-tail endpoint templates without losing the signed-child accounting.",
                "requires endpoint-level rather than template-level completion",
            ),
            gate(
                "MissingMirrorTraceCompletion",
                False,
                False,
                "Complete endpoint-routed carriers to admissible trace/Kloosterman families.",
                "requires explicit completion variables",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "candidate only after pure/mixed endpoint routes are completed to trace sums",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "candidate only after endpoint-routed Kloosterman variables are explicit",
            "Pascadi_composite_Type_II": "not matched to endpoint-routed signed-template carriers",
            "Wright_unbalanced_Kloosterman": "candidate for right-tail routes only after unbalanced fraction variables appear",
        },
        "latest_narrowest_mouth": [
            "PureEndpointMissingMirrorCarrierPhaseSaving",
            "AND MixedRightTailEndpointRouterNoLoss",
            "AND MissingMirrorTraceKloostermanCompletion",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "missing_mirror_endpoint_router_ledger_closed": finite_audit[
            "missing_mirror_endpoint_router_ledger_closed"
        ],
        "pure_endpoint_carrier_phase_saving_closed": False,
        "mixed_right_tail_endpoint_router_no_loss_closed": False,
        "missing_mirror_trace_completion_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature missing-mirror endpoint-router 审计",
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
        "## 2. endpoint-router 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"missing_mirror_endpoint_router_ledger_closed={str(audit['missing_mirror_endpoint_router_ledger_closed']).lower()}",
        f"missing_mirror_edge_mass={audit['missing_mirror_edge_mass']}",
        f"missing_mirror_template_count={audit['missing_mirror_template_count']}",
        f"pure_endpoint_template_edge_mass={audit['pure_endpoint_template_edge_mass']}",
        f"pure_endpoint_template_edge_ratio={audit['pure_endpoint_template_edge_ratio']}",
        f"mixed_endpoint_template_edge_mass={audit['mixed_endpoint_template_edge_mass']}",
        f"mixed_endpoint_template_edge_ratio={audit['mixed_endpoint_template_edge_ratio']}",
        f"mixed_right_tail_endpoint_edge_mass={audit['mixed_right_tail_endpoint_edge_mass']}",
        f"mixed_right_tail_endpoint_edge_ratio={audit['mixed_right_tail_endpoint_edge_ratio']}",
        f"mixed_wing_tail_endpoint_edge_mass={audit['mixed_wing_tail_endpoint_edge_mass']}",
        f"mixed_wing_tail_endpoint_edge_ratio={audit['mixed_wing_tail_endpoint_edge_ratio']}",
        f"single_strip_pure_endpoint_edge_mass={audit['single_strip_pure_endpoint_edge_mass']}",
        f"single_strip_pure_endpoint_edge_ratio={audit['single_strip_pure_endpoint_edge_ratio']}",
        f"endpoint_group_width_min/median/max={audit['endpoint_group_width_min']}/{audit['endpoint_group_width_median']}/{audit['endpoint_group_width_max']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "endpoint route edge mass：",
        "",
        *markdown_table(
            audit["endpoint_route_rows"],
            [
                "route_class",
                "template_count",
                "edge_mass",
                "edge_ratio",
                "P_support_width_min",
                "P_support_width_median",
                "P_support_width_max",
            ],
        ),
        "",
        "最高 endpoint-route templates：",
        "",
        *markdown_table(
            audit["top_endpoint_route_template_rows"],
            [
                "route_class",
                "signed_child",
                "raw_base_template",
                "edge_mass",
                "A_class",
                "P_support_width",
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
        "结论：missing-mirror endpoint carriers 已分成纯 endpoint 模板和 right-tail",
        "内部混合 endpoint 模板。该路由账本仍不提供 phase saving，也不完成到",
        "trace/Kloosterman family。",
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
        f"missing_mirror_endpoint_router_ledger_closed={str(payload['missing_mirror_endpoint_router_ledger_closed']).lower()}",
        f"pure_endpoint_carrier_phase_saving_closed={str(payload['pure_endpoint_carrier_phase_saving_closed']).lower()}",
        f"mixed_right_tail_endpoint_router_no_loss_closed={str(payload['mixed_right_tail_endpoint_router_no_loss_closed']).lower()}",
        f"missing_mirror_trace_completion_closed={str(payload['missing_mirror_trace_completion_closed']).lower()}",
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
        "missing_mirror_endpoint_router_ledger_closed="
        f"{payload['missing_mirror_endpoint_router_ledger_closed']}"
    )
    print(f"pure_endpoint_template_edge_ratio={audit['pure_endpoint_template_edge_ratio']}")
    print(f"mixed_endpoint_template_edge_ratio={audit['mixed_endpoint_template_edge_ratio']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
