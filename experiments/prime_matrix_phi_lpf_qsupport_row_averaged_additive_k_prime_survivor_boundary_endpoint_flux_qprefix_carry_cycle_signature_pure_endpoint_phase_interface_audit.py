#!/usr/bin/env python3
"""审计 pure endpoint missing-mirror carriers 的相位接口。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_pure_endpoint_phase_interface_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface-audit.json

上一层把 missing-mirror endpoint carriers 路由为 pure endpoint 与 mixed endpoint。
本层只处理 pure endpoint 主体，按 endpoint route、P-support 宽度、single-P
局部包与 multi-P trace 候选包拆账。该层关闭的是相位接口账本，不证明相消。
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
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

ENDPOINT_ROUTER_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router-audit.json"
)

DEPENDENCIES = [
    ENDPOINT_ROUTER_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure-audit.json",
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
        "role": "candidate for multi-P pure endpoint trace sums after sheaf/trace realization",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "candidate for multi-P pure endpoint Kloosterman variables after completion",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate for unbalanced right-tail pure endpoint fractions after variable extraction",
    },
    {
        "key": "Dong_Robles_Zeindler_2026_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2601.00292",
        "role": "withdrawn near-miss; not an admissible external input",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "does not estimate pure endpoint signed-carrier phases",
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
        return "single_P_local_packet"
    if width <= 4:
        return "multi_P_width_2_to_4"
    if width <= 16:
        return "multi_P_width_5_to_16"
    if width <= 64:
        return "multi_P_width_17_to_64"
    return "multi_P_width_ge_65"


def phase_interface_class(route: str, p_width: int) -> str:
    """给纯端点模板指定相位接口类。"""
    if p_width == 1:
        return "single_P_local_endpoint_packet"
    if route.startswith("pure_right_tail"):
        return "multi_P_right_tail_endpoint_trace_candidate"
    if route.startswith("pure_upper_wing") or route.startswith("pure_lower_wing"):
        return "multi_P_wing_endpoint_trace_candidate"
    return "multi_P_other_pure_endpoint_trace_candidate"


def table_from_counter(counter: Counter[str], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成排序表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], item))
    ]


def top_rows(
    pure_edge_mass: Counter[str],
    template_base: dict[str, str],
    template_a_class: dict[str, str],
    template_p_sets: dict[str, set[int]],
    template_route: dict[str, str],
    template_strip_counts: dict[str, Counter[str]],
    template_endpoint_group_counts: dict[str, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量 pure endpoint 模板。"""
    rows = []
    order = sorted(pure_edge_mass, key=lambda key: (-pure_edge_mass[key], key))
    for key in order[:limit]:
        width = len(template_p_sets[key])
        route = template_route[key]
        rows.append(
            {
                "signed_child": key,
                "raw_base_template": template_base[key],
                "edge_mass": pure_edge_mass[key],
                "route_class": route,
                "phase_interface_class": phase_interface_class(route, width),
                "A_class": template_a_class[key],
                "P_support_width": width,
                "P_width_bucket": p_width_bucket(width),
                "strip_profile": profile_string(template_strip_counts[key]),
                "endpoint_group_profile": profile_string(template_endpoint_group_counts[key]),
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 pure endpoint phase interface。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(ENDPOINT_ROUTER_AUDIT.read_text())
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

    route_edge_mass: Counter[str] = Counter()
    phase_interface_edge_mass: Counter[str] = Counter()
    p_width_edge_mass: Counter[str] = Counter()
    a_class_edge_mass: Counter[str] = Counter()
    single_p_edge_mass = 0
    multi_p_edge_mass = 0
    multi_p_right_tail_edge_mass = 0
    multi_p_wing_edge_mass = 0
    p_widths: list[int] = []

    for template, mass in pure_edge_mass.items():
        route = template_route[template]
        width = len(template_p_sets[template])
        iface = phase_interface_class(route, width)
        route_edge_mass[route] += mass
        phase_interface_edge_mass[iface] += mass
        p_width_edge_mass[p_width_bucket(width)] += mass
        a_class_edge_mass[template_a_class[template]] += mass
        p_widths.append(width)
        if width == 1:
            single_p_edge_mass += mass
        else:
            multi_p_edge_mass += mass
            if route.startswith("pure_right_tail"):
                multi_p_right_tail_edge_mass += mass
            elif route.startswith("pure_upper_wing") or route.startswith("pure_lower_wing"):
                multi_p_wing_edge_mass += mass

    pure_total = sum(pure_edge_mass.values())
    ledger_closed = (
        previous["missing_mirror_endpoint_router_ledger_closed"]
        and totals["atom_count_total"] == previous["atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and totals["signed_cycle_packet_count"] == previous["signed_cycle_packet_count"]
        and totals["signed_cycle_edge_mass"] == previous["signed_cycle_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and pure_total == previous["pure_endpoint_template_edge_mass"]
        and single_p_edge_mass + multi_p_edge_mass == pure_total
        and sum(route_edge_mass.values()) == pure_total
        and sum(phase_interface_edge_mass.values()) == pure_total
    )

    return {
        "max_prime": max_prime,
        "previous_missing_endpoint_router_ledger_closed": previous[
            "missing_mirror_endpoint_router_ledger_closed"
        ],
        "pure_endpoint_phase_interface_ledger_closed": ledger_closed,
        "atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "signed_cycle_packet_count": totals["signed_cycle_packet_count"],
        "signed_cycle_edge_mass": totals["signed_cycle_edge_mass"],
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "pure_endpoint_edge_mass": pure_total,
        "pure_endpoint_template_count": len(pure_edge_mass),
        "single_P_pure_endpoint_edge_mass": single_p_edge_mass,
        "single_P_pure_endpoint_edge_ratio": single_p_edge_mass / pure_total,
        "multi_P_pure_endpoint_edge_mass": multi_p_edge_mass,
        "multi_P_pure_endpoint_edge_ratio": multi_p_edge_mass / pure_total,
        "multi_P_right_tail_pure_endpoint_edge_mass": multi_p_right_tail_edge_mass,
        "multi_P_right_tail_pure_endpoint_edge_ratio": multi_p_right_tail_edge_mass
        / pure_total,
        "multi_P_wing_pure_endpoint_edge_mass": multi_p_wing_edge_mass,
        "multi_P_wing_pure_endpoint_edge_ratio": multi_p_wing_edge_mass / pure_total,
        "P_support_width_min": min(p_widths),
        "P_support_width_median": statistics.median(p_widths),
        "P_support_width_max": max(p_widths),
        "pure_endpoint_route_edge_rows": table_from_counter(
            route_edge_mass, pure_total, "route_class"
        ),
        "pure_endpoint_phase_interface_edge_rows": table_from_counter(
            phase_interface_edge_mass, pure_total, "phase_interface_class"
        ),
        "pure_endpoint_P_width_edge_rows": table_from_counter(
            p_width_edge_mass, pure_total, "P_width_bucket"
        ),
        "pure_endpoint_A_class_edge_rows": table_from_counter(
            a_class_edge_mass, pure_total, "A_class"
        ),
        "top_pure_endpoint_template_rows": top_rows(
            pure_edge_mass,
            template_base,
            template_a_class,
            template_p_sets,
            template_route,
            template_strip_counts,
            template_endpoint_group_counts,
        ),
        "pure_endpoint_phase_interface_ledger_closed_flag": ledger_closed,
        "single_P_local_endpoint_packet_bound_closed": False,
        "multi_P_trace_completion_closed": False,
        "pure_endpoint_carrier_phase_saving_closed": False,
        "mixed_right_tail_endpoint_router_no_loss_closed": False,
        "missing_mirror_trace_completion_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_pure_endpoint_phase_interface_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "pure_endpoint_phase_interface_ledger_closed_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "pure endpoint carriers are the dominant routed missing-mirror branch and must be split before external trace inputs can be matched",
        "current_object": {
            "input": "pure endpoint missing-mirror signed-child templates",
            "operation": "single-P versus multi-P phase-interface routing",
            "dominant_shape": "pure endpoint mass splits into local single-P packets and multi-P trace candidates",
            "remaining": "local packet estimates, multi-P trace/Kloosterman completion, and phase saving",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "MissingMirrorEndpointRouterImported",
                finite_audit["previous_missing_endpoint_router_ledger_closed"],
                finite_audit["previous_missing_endpoint_router_ledger_closed"],
                "The previous endpoint router ledger is imported.",
                "none for import",
            ),
            gate(
                "PureEndpointPhaseInterfaceLedger",
                finite_audit["pure_endpoint_phase_interface_ledger_closed"],
                finite_audit["pure_endpoint_phase_interface_ledger_closed"],
                "Pure endpoint mass is routed into single-P local packets and multi-P trace candidates.",
                "none for the finite interface ledger",
            ),
            gate(
                "SinglePLocalEndpointPacketBound",
                False,
                False,
                "Control pure endpoint packets with only one supporting P.",
                "requires local signed packet bounds not supplied by the ledger",
            ),
            gate(
                "MultiPTraceKloostermanCompletion",
                False,
                False,
                "Complete multi-P pure endpoint packets to trace/Kloosterman sums.",
                "requires explicit completion variables and sheaf/Kloosterman admissibility",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "candidate only for multi-P pure endpoint trace candidates after sheaf realization",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "candidate only after bilinear Kloosterman variables are extracted",
            "Wright_unbalanced_Kloosterman": "candidate only for right-tail multi-P packets after fraction variables are explicit",
            "Li_short_interval_x_052": "does not control signed pure endpoint carrier phases",
        },
        "latest_narrowest_mouth": [
            "SinglePLocalPureEndpointPacketBound",
            "AND MultiPPureEndpointTraceKloostermanCompletion",
            "AND PureEndpointCarrierPhaseSaving",
            "AND MixedRightTailEndpointRouterNoLoss",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "pure_endpoint_phase_interface_ledger_closed": finite_audit[
            "pure_endpoint_phase_interface_ledger_closed"
        ],
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature pure endpoint phase-interface 审计",
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
        "## 2. pure endpoint phase-interface 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"pure_endpoint_phase_interface_ledger_closed={str(audit['pure_endpoint_phase_interface_ledger_closed']).lower()}",
        f"pure_endpoint_edge_mass={audit['pure_endpoint_edge_mass']}",
        f"pure_endpoint_template_count={audit['pure_endpoint_template_count']}",
        f"single_P_pure_endpoint_edge_mass={audit['single_P_pure_endpoint_edge_mass']}",
        f"single_P_pure_endpoint_edge_ratio={audit['single_P_pure_endpoint_edge_ratio']}",
        f"multi_P_pure_endpoint_edge_mass={audit['multi_P_pure_endpoint_edge_mass']}",
        f"multi_P_pure_endpoint_edge_ratio={audit['multi_P_pure_endpoint_edge_ratio']}",
        f"multi_P_right_tail_pure_endpoint_edge_mass={audit['multi_P_right_tail_pure_endpoint_edge_mass']}",
        f"multi_P_right_tail_pure_endpoint_edge_ratio={audit['multi_P_right_tail_pure_endpoint_edge_ratio']}",
        f"multi_P_wing_pure_endpoint_edge_mass={audit['multi_P_wing_pure_endpoint_edge_mass']}",
        f"multi_P_wing_pure_endpoint_edge_ratio={audit['multi_P_wing_pure_endpoint_edge_ratio']}",
        f"P_support_width_min/median/max={audit['P_support_width_min']}/{audit['P_support_width_median']}/{audit['P_support_width_max']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "phase-interface edge mass：",
        "",
        *markdown_table(
            audit["pure_endpoint_phase_interface_edge_rows"],
            ["phase_interface_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "pure endpoint route edge mass：",
        "",
        *markdown_table(
            audit["pure_endpoint_route_edge_rows"],
            ["route_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "pure endpoint P-width edge mass：",
        "",
        *markdown_table(
            audit["pure_endpoint_P_width_edge_rows"],
            ["P_width_bucket", "edge_mass", "edge_ratio"],
        ),
        "",
        "pure endpoint A-class edge mass：",
        "",
        *markdown_table(
            audit["pure_endpoint_A_class_edge_rows"],
            ["A_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高 pure endpoint templates：",
        "",
        *markdown_table(
            audit["top_pure_endpoint_template_rows"],
            [
                "signed_child",
                "raw_base_template",
                "edge_mass",
                "route_class",
                "phase_interface_class",
                "A_class",
                "P_support_width",
                "P_width_bucket",
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
        "结论：pure endpoint 主体已拆成 single-P local packets 与 multi-P trace",
        "candidates。该接口账本尚未给出本地包估计、trace/Kloosterman completion 或相消。",
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
        f"pure_endpoint_phase_interface_ledger_closed={str(payload['pure_endpoint_phase_interface_ledger_closed']).lower()}",
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
        "pure_endpoint_phase_interface_ledger_closed="
        f"{payload['pure_endpoint_phase_interface_ledger_closed']}"
    )
    print(f"single_P_pure_endpoint_edge_ratio={audit['single_P_pure_endpoint_edge_ratio']}")
    print(f"multi_P_pure_endpoint_edge_ratio={audit['multi_P_pure_endpoint_edge_ratio']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
