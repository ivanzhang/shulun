#!/usr/bin/env python3
"""审计 gap-2/gap-4 adjacent-prime-pair carriers 的 exact route-class 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_exact_route_class_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-exact-route-class-audit.json

上一层把 gap2/gap4 主量拆成 route-superclass。这里继续细化到 exact route-class：
gap2 upper/lower wing、gap2 right-tail residual、gap4 right-tail two-sided/left-collar、
gap4 wing residual。该层只关闭有限 exact-route 账本，不证明全局 signed collision bound。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_route_superclass_audit as superclass_audit  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-exact-route-class"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_ROUTE_SUPERCLASS_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-route-superclass-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_ROUTE_SUPERCLASS_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-adjacent-prime-pair-gap-class-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = superclass_audit.EXTERNAL_SOURCES


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


def pair_rows(
    counter: Counter[tuple[str, str]],
    total: int,
    left_field: str,
    right_field: str,
) -> list[dict[str, Any]]:
    """输出二元 edge-mass 表。"""
    return [
        {
            left_field: left,
            right_field: right,
            "edge_mass": counter[(left, right)],
            "edge_ratio": counter[(left, right)] / total,
        }
        for left, right in sorted(counter, key=lambda key: (-counter[key], key[0], key[1]))
    ]


def pair_template_rows(
    counter: Counter[tuple[str, str]],
    total: int,
    left_field: str,
    right_field: str,
) -> list[dict[str, Any]]:
    """输出二元 template-count 表。"""
    return [
        {
            left_field: left,
            right_field: right,
            "template_count": counter[(left, right)],
            "template_ratio": counter[(left, right)] / total,
        }
        for left, right in sorted(counter, key=lambda key: (-counter[key], key[0], key[1]))
    ]


def triple_rows(
    counter: Counter[tuple[str, str, Any]],
    total: int,
    value_field: str,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    """输出 gap class、route class 与第三字段的交叉表。"""
    rows = [
        {
            "adjacent_pair_gap_class": gap,
            "route_class": route,
            value_field: value,
            "edge_mass": counter[(gap, route, value)],
            "edge_ratio": counter[(gap, route, value)] / total,
        }
        for gap, route, value in sorted(
            counter, key=lambda key: (-counter[key], key[0], key[1], str(key[2]))
        )
    ]
    return rows if limit is None else rows[:limit]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 gap2/gap4 exact route-class ledger。"""
    previous_payload = json.loads(PREVIOUS_ROUTE_SUPERCLASS_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    _, selected = superclass_audit.selected_templates(max_prime)

    route_template_count: Counter[tuple[str, str]] = Counter()
    route_edge_mass: Counter[tuple[str, str]] = Counter()
    route_a_edge_mass: Counter[tuple[str, str, str]] = Counter()
    route_cycle_edge_mass: Counter[tuple[str, str, int]] = Counter()
    route_q_edge_mass: Counter[tuple[str, str, int]] = Counter()
    route_shell_edge_mass: Counter[tuple[str, str, int]] = Counter()
    route_p_band_edge_mass: Counter[tuple[str, str, str]] = Counter()
    raw_base_count: defaultdict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    raw_base_edge_mass: Counter[tuple[str, str, str]] = Counter()

    for row in selected:
        gap = row["adjacent_pair_gap_class"]
        route = row["route_class"]
        mass = row["edge_mass"]
        route_template_count[(gap, route)] += 1
        route_edge_mass[(gap, route)] += mass
        route_a_edge_mass[(gap, route, row["A_class"])] += mass
        route_cycle_edge_mass[(gap, route, row["cycle_length"])] += mass
        route_q_edge_mass[(gap, route, row["q_prefix_count"])] += mass
        route_shell_edge_mass[(gap, route, row["m_shell_prime_count"])] += mass
        route_p_band_edge_mass[(gap, route, row["P_band"])] += mass
        raw_base_count[(gap, route)][row["raw_base_template"]] += 1
        raw_base_edge_mass[(gap, route, row["raw_base_template"])] += mass

    total_template_count = len(selected)
    total_edge_mass = sum(row["edge_mass"] for row in selected)

    def mass(gap: str, route: str) -> int:
        return route_edge_mass[(gap, route)]

    def count(gap: str, route: str) -> int:
        return route_template_count[(gap, route)]

    gap2 = "gap2_twin_adjacent_pair_collision"
    gap4 = "gap4_cousin_adjacent_pair_collision"
    upper_wing = "pure_upper_wing_single_shell"
    lower_wing = "pure_lower_wing_single_shell"
    tail_two = "pure_right_tail_two_sided_collar"
    tail_left = "pure_right_tail_left_collar"

    top_two_route_edge_mass = mass(gap4, tail_two) + mass(gap2, upper_wing)
    wing_route_edge_mass = mass(gap2, upper_wing) + mass(gap2, lower_wing)
    right_tail_route_edge_mass = mass(gap4, tail_two) + mass(gap4, tail_left)
    residual_route_edge_mass = total_edge_mass - top_two_route_edge_mass

    duplicate_raw_base_rows = []
    duplicate_raw_base_count = 0
    duplicate_raw_base_edge_mass = 0
    for (gap, route), counter in sorted(raw_base_count.items()):
        for base, template_count in counter.items():
            if template_count <= 1:
                continue
            raw_mass = raw_base_edge_mass[(gap, route, base)]
            duplicate_raw_base_count += 1
            duplicate_raw_base_edge_mass += raw_mass
            duplicate_raw_base_rows.append(
                {
                    "adjacent_pair_gap_class": gap,
                    "route_class": route,
                    "raw_base_template": base,
                    "template_count": template_count,
                    "edge_mass": raw_mass,
                    "edge_ratio": raw_mass / total_edge_mass,
                }
            )

    expected_route_mass = {
        (gap4, tail_two): 258,
        (gap2, upper_wing): 212,
        (gap2, lower_wing): 78,
        (gap4, tail_left): 30,
        (gap4, upper_wing): 22,
        (gap2, tail_two): 6,
        (gap4, lower_wing): 6,
    }
    ledger_closed = (
        previous_payload["single_P_local_gap2_gap4_route_superclass_ledger_closed"]
        and total_template_count == previous["gap2_gap4_template_count"]
        and total_edge_mass == previous["gap2_gap4_edge_mass"]
        and sum(route_edge_mass.values()) == total_edge_mass
        and sum(route_template_count.values()) == total_template_count
        and all(route_edge_mass[key] == value for key, value in expected_route_mass.items())
        and len(route_edge_mass) == len(expected_route_mass)
        and wing_route_edge_mass == previous["gap2_wing_edge_mass"]
        and right_tail_route_edge_mass == previous["gap4_right_tail_edge_mass"]
        and all(row["edge_mass"] == row["cycle_length"] * row["occurrence_count"] for row in selected)
    )

    top_rows = sorted(
        selected,
        key=lambda row: (-row["edge_mass"], row["adjacent_pair_gap_class"], row["route_class"]),
    )[:24]

    return {
        "max_prime": max_prime,
        "previous_gap2_gap4_route_superclass_ledger_closed": previous_payload[
            "single_P_local_gap2_gap4_route_superclass_ledger_closed"
        ],
        "single_P_local_gap2_gap4_exact_route_class_ledger_closed": ledger_closed,
        "gap2_gap4_template_count": total_template_count,
        "gap2_gap4_edge_mass": total_edge_mass,
        "gap4_right_tail_two_sided_template_count": count(gap4, tail_two),
        "gap4_right_tail_two_sided_edge_mass": mass(gap4, tail_two),
        "gap2_upper_wing_template_count": count(gap2, upper_wing),
        "gap2_upper_wing_edge_mass": mass(gap2, upper_wing),
        "gap2_lower_wing_template_count": count(gap2, lower_wing),
        "gap2_lower_wing_edge_mass": mass(gap2, lower_wing),
        "gap4_right_tail_left_collar_template_count": count(gap4, tail_left),
        "gap4_right_tail_left_collar_edge_mass": mass(gap4, tail_left),
        "gap4_upper_wing_template_count": count(gap4, upper_wing),
        "gap4_upper_wing_edge_mass": mass(gap4, upper_wing),
        "gap2_right_tail_two_sided_template_count": count(gap2, tail_two),
        "gap2_right_tail_two_sided_edge_mass": mass(gap2, tail_two),
        "gap4_lower_wing_template_count": count(gap4, lower_wing),
        "gap4_lower_wing_edge_mass": mass(gap4, lower_wing),
        "top_two_route_edge_mass": top_two_route_edge_mass,
        "top_two_route_edge_ratio": top_two_route_edge_mass / total_edge_mass,
        "wing_route_edge_mass": wing_route_edge_mass,
        "right_tail_route_edge_mass": right_tail_route_edge_mass,
        "residual_route_edge_mass": residual_route_edge_mass,
        "residual_route_edge_ratio": residual_route_edge_mass / total_edge_mass,
        "gap2_upper_share_within_gap2": mass(gap2, upper_wing)
        / (mass(gap2, upper_wing) + mass(gap2, lower_wing) + mass(gap2, tail_two)),
        "gap4_two_sided_share_within_gap4": mass(gap4, tail_two)
        / (mass(gap4, tail_two) + mass(gap4, tail_left) + mass(gap4, upper_wing) + mass(gap4, lower_wing)),
        "mixed_positive_negative_edge_mass": sum(
            value
            for (gap, route, a_class), value in route_a_edge_mass.items()
            if a_class == "mixed_positive_negative"
        ),
        "all_positive_edge_mass": sum(
            value
            for (gap, route, a_class), value in route_a_edge_mass.items()
            if a_class == "all_positive"
        ),
        "duplicate_raw_base_count": duplicate_raw_base_count,
        "duplicate_raw_base_edge_mass": duplicate_raw_base_edge_mass,
        "route_class_template_rows": pair_template_rows(
            route_template_count,
            total_template_count,
            "adjacent_pair_gap_class",
            "route_class",
        ),
        "route_class_edge_rows": pair_rows(
            route_edge_mass,
            total_edge_mass,
            "adjacent_pair_gap_class",
            "route_class",
        ),
        "route_class_a_edge_rows": triple_rows(
            route_a_edge_mass,
            total_edge_mass,
            "A_class",
        ),
        "route_class_cycle_edge_rows": triple_rows(
            route_cycle_edge_mass,
            total_edge_mass,
            "cycle_length",
            limit=36,
        ),
        "route_class_q_prefix_edge_rows": triple_rows(
            route_q_edge_mass,
            total_edge_mass,
            "q_prefix_count",
            limit=36,
        ),
        "route_class_m_shell_edge_rows": triple_rows(
            route_shell_edge_mass,
            total_edge_mass,
            "m_shell_prime_count",
            limit=36,
        ),
        "route_class_p_band_edge_rows": triple_rows(
            route_p_band_edge_mass,
            total_edge_mass,
            "P_band",
        ),
        "duplicate_raw_base_rows": sorted(
            duplicate_raw_base_rows,
            key=lambda row: (-row["edge_mass"], row["adjacent_pair_gap_class"], row["route_class"]),
        ),
        "top_gap2_gap4_route_class_template_rows": [
            {
                **row,
                "m_pair": str(row["m_pair"]),
            }
            for row in top_rows
        ],
        "gap2_upper_wing_twin_collision_bound_proved": False,
        "gap2_lower_wing_twin_collision_bound_proved": False,
        "gap2_right_tail_twin_residual_bound_proved": False,
        "gap4_right_tail_two_sided_cousin_collision_bound_proved": False,
        "gap4_right_tail_left_collar_cousin_collision_bound_proved": False,
        "gap4_wing_cousin_residual_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_exact_route_class_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_gap2_gap4_exact_route_class_ledger_closed_collision_bounds_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "route-superclass carriers still hide exact upper/lower wing and collar subclasses",
        "current_object": {
            "input": "the 64 gap2/gap4 adjacent-prime-pair repeated templates",
            "operation": "classify dominant route-superclass carriers by exact route class",
            "dominant_shape": "gap4 two-sided right-tail collar and gap2 upper wing are the two largest exact routes",
            "remaining": "prove signed collision bounds for exact route classes or route them to PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "Gap2Gap4RouteSuperclassLedgerImported",
                finite_audit["previous_gap2_gap4_route_superclass_ledger_closed"],
                finite_audit["previous_gap2_gap4_route_superclass_ledger_closed"],
                "The gap2/gap4 route-superclass ledger is imported.",
                "none for import",
            ),
            gate(
                "Gap2Gap4ExactRouteClassLedger",
                finite_audit["single_P_local_gap2_gap4_exact_route_class_ledger_closed"],
                finite_audit["single_P_local_gap2_gap4_exact_route_class_ledger_closed"],
                "Gap2/gap4 carriers are split by exact route class.",
                "none for the finite exact-route ledger",
            ),
            gate(
                "Gap4RightTailTwoSidedCousinCollisionBound",
                False,
                False,
                "Control the largest exact route: gap4 right-tail two-sided collar.",
                "finite audit shows 258 edge mass but no global theorem",
            ),
            gate(
                "Gap2UpperWingTwinCollisionBound",
                False,
                False,
                "Control the second largest exact route: gap2 upper wing.",
                "finite audit shows 212 edge mass but no global theorem",
            ),
            gate(
                "ResidualExactRouteCollisionBounds",
                False,
                False,
                "Control lower wing, left-collar, and small off-route residuals.",
                "finite audit shows 142 edge mass outside the two largest exact routes",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "do not directly control a fixed upper-wing or two-sided-collar signed template equality",
            "prime_gap_theorems": "do not distinguish Phi-LPF exact route classes",
            "short_interval_prime_inputs": "do not estimate these local carrier collisions",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND Gap2UpperWingTwinCollisionBound",
            "AND Gap2LowerWingTwinCollisionBound",
            "AND Gap2RightTailTwoSidedTwinResidualCollisionBound",
            "AND Gap4RightTailTwoSidedCousinCollisionBound",
            "AND Gap4RightTailLeftCollarCousinCollisionBound",
            "AND Gap4UpperWingCousinResidualCollisionBound",
            "AND Gap4LowerWingCousinResidualCollisionBound",
            "AND Gap6SexyAdjacentPairCollisionBound",
            "AND GapGe8AdjacentPairCollisionBound",
            "AND NonAdjacentPrimePairCollisionBound",
            "AND AdjacentPrimeChainCollisionBound",
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
        "single_P_local_gap2_gap4_exact_route_class_ledger_closed": finite_audit[
            "single_P_local_gap2_gap4_exact_route_class_ledger_closed"
        ],
        "gap2_upper_wing_twin_collision_bound_proved": False,
        "gap2_lower_wing_twin_collision_bound_proved": False,
        "gap2_right_tail_twin_residual_bound_proved": False,
        "gap4_right_tail_two_sided_cousin_collision_bound_proved": False,
        "gap4_right_tail_left_collar_cousin_collision_bound_proved": False,
        "gap4_wing_cousin_residual_bound_proved": False,
        "gap2_twin_adjacent_pair_collision_bound_proved": False,
        "gap4_cousin_adjacent_pair_collision_bound_proved": False,
        "adjacent_prime_pair_collision_bound_proved": False,
        "same_packet_multi_m_collision_bound_proved": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 exact route-class 审计",
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
        "## 2. gap2/gap4 exact route-class 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_gap2_gap4_exact_route_class_ledger_closed={str(audit['single_P_local_gap2_gap4_exact_route_class_ledger_closed']).lower()}",
        f"gap2_gap4_template_count={audit['gap2_gap4_template_count']}",
        f"gap2_gap4_edge_mass={audit['gap2_gap4_edge_mass']}",
        f"gap4_right_tail_two_sided_template_count={audit['gap4_right_tail_two_sided_template_count']}",
        f"gap4_right_tail_two_sided_edge_mass={audit['gap4_right_tail_two_sided_edge_mass']}",
        f"gap2_upper_wing_template_count={audit['gap2_upper_wing_template_count']}",
        f"gap2_upper_wing_edge_mass={audit['gap2_upper_wing_edge_mass']}",
        f"gap2_lower_wing_template_count={audit['gap2_lower_wing_template_count']}",
        f"gap2_lower_wing_edge_mass={audit['gap2_lower_wing_edge_mass']}",
        f"gap4_right_tail_left_collar_template_count={audit['gap4_right_tail_left_collar_template_count']}",
        f"gap4_right_tail_left_collar_edge_mass={audit['gap4_right_tail_left_collar_edge_mass']}",
        f"gap4_upper_wing_template_count={audit['gap4_upper_wing_template_count']}",
        f"gap4_upper_wing_edge_mass={audit['gap4_upper_wing_edge_mass']}",
        f"gap2_right_tail_two_sided_template_count={audit['gap2_right_tail_two_sided_template_count']}",
        f"gap2_right_tail_two_sided_edge_mass={audit['gap2_right_tail_two_sided_edge_mass']}",
        f"gap4_lower_wing_template_count={audit['gap4_lower_wing_template_count']}",
        f"gap4_lower_wing_edge_mass={audit['gap4_lower_wing_edge_mass']}",
        f"top_two_route_edge_mass={audit['top_two_route_edge_mass']}",
        f"top_two_route_edge_ratio={audit['top_two_route_edge_ratio']}",
        f"residual_route_edge_mass={audit['residual_route_edge_mass']}",
        f"residual_route_edge_ratio={audit['residual_route_edge_ratio']}",
        f"gap2_upper_share_within_gap2={audit['gap2_upper_share_within_gap2']}",
        f"gap4_two_sided_share_within_gap4={audit['gap4_two_sided_share_within_gap4']}",
        f"mixed_positive_negative_edge_mass={audit['mixed_positive_negative_edge_mass']}",
        f"all_positive_edge_mass={audit['all_positive_edge_mass']}",
        f"duplicate_raw_base_count={audit['duplicate_raw_base_count']}",
        f"duplicate_raw_base_edge_mass={audit['duplicate_raw_base_edge_mass']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "exact route-class template count：",
        "",
        *markdown_table(
            audit["route_class_template_rows"],
            ["adjacent_pair_gap_class", "route_class", "template_count", "template_ratio"],
        ),
        "",
        "exact route-class edge mass：",
        "",
        *markdown_table(
            audit["route_class_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "exact route-class A-class edge mass：",
        "",
        *markdown_table(
            audit["route_class_a_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "A_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "exact route-class cycle-length edge mass：",
        "",
        *markdown_table(
            audit["route_class_cycle_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "cycle_length", "edge_mass", "edge_ratio"],
        ),
        "",
        "duplicate raw-base rows：",
        "",
        *markdown_table(
            audit["duplicate_raw_base_rows"],
            ["adjacent_pair_gap_class", "route_class", "template_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高 exact-route templates：",
        "",
        *markdown_table(
            audit["top_gap2_gap4_route_class_template_rows"],
            [
                "adjacent_pair_gap_class",
                "route_class",
                "P",
                "packet_index",
                "edge_mass",
                "cycle_length",
                "m_pair",
                "q_prefix_count",
                "m_shell_prime_count",
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
        "结论：gap2/gap4 route-superclass 主量已进一步拆成 exact route-class carrier。",
        "该账本仍是有限结构结果，尚未给出全局 signed collision bound。",
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
        f"single_P_local_gap2_gap4_exact_route_class_ledger_closed={str(payload['single_P_local_gap2_gap4_exact_route_class_ledger_closed']).lower()}",
        f"gap2_upper_wing_twin_collision_bound_proved={str(payload['gap2_upper_wing_twin_collision_bound_proved']).lower()}",
        f"gap2_lower_wing_twin_collision_bound_proved={str(payload['gap2_lower_wing_twin_collision_bound_proved']).lower()}",
        f"gap2_right_tail_twin_residual_bound_proved={str(payload['gap2_right_tail_twin_residual_bound_proved']).lower()}",
        f"gap4_right_tail_two_sided_cousin_collision_bound_proved={str(payload['gap4_right_tail_two_sided_cousin_collision_bound_proved']).lower()}",
        f"gap4_right_tail_left_collar_cousin_collision_bound_proved={str(payload['gap4_right_tail_left_collar_cousin_collision_bound_proved']).lower()}",
        f"gap4_wing_cousin_residual_bound_proved={str(payload['gap4_wing_cousin_residual_bound_proved']).lower()}",
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
        "single_P_local_gap2_gap4_exact_route_class_ledger_closed="
        f"{payload['single_P_local_gap2_gap4_exact_route_class_ledger_closed']}"
    )
    print(f"gap4_right_tail_two_sided_edge_mass={audit['gap4_right_tail_two_sided_edge_mass']}")
    print(f"gap2_upper_wing_edge_mass={audit['gap2_upper_wing_edge_mass']}")
    print(f"top_two_route_edge_ratio={audit['top_two_route_edge_ratio']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
