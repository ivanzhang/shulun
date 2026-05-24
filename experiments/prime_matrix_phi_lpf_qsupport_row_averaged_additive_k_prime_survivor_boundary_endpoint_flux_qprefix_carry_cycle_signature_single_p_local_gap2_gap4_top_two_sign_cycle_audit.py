#!/usr/bin/env python3
"""审计 gap2/gap4 两个最大 exact-route carrier 的 sign-cycle 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_sign_cycle_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-sign-cycle-audit.json

上一层把 gap2/gap4 拆成 exact route-class。这里只继续下钻两个最大 exact routes：
gap4 right-tail two-sided collar 与 gap2 upper wing。该层关闭有限 sign/cycle 账本，
不证明全局 signed collision bound。
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_exact_route_class_audit as exact_route_audit  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_route_superclass_audit as superclass_audit  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-sign-cycle"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_EXACT_ROUTE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-exact-route-class-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_EXACT_ROUTE_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-route-superclass-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

TOP_TWO_KEYS = {
    ("gap4_cousin_adjacent_pair_collision", "pure_right_tail_two_sided_collar"),
    ("gap2_twin_adjacent_pair_collision", "pure_upper_wing_single_shell"),
}

EXTERNAL_SOURCES = exact_route_audit.EXTERNAL_SOURCES


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sign_word(row: dict[str, Any]) -> str:
    """从 signed child 模板提取正负号字。"""
    signs = re.findall(r"A=(positive|negative)", row["signed_child"])
    return "".join("+" if sign == "positive" else "-" for sign in signs)


def sign_switch_count(word: str) -> int:
    """计算相邻符号切换次数。"""
    return sum(left != right for left, right in zip(word, word[1:]))


def sign_balance(word: str) -> str:
    """记录正负号数量。"""
    return f"plus={word.count('+')},minus={word.count('-')}"


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def edge_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 edge-mass 表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def template_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 template-count 表。"""
    return [
        {field: key, "template_count": counter[key], "template_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def pair_rows(
    counter: Counter[tuple[Any, Any]],
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
        for left, right in sorted(counter, key=lambda key: (-counter[key], str(key[0]), str(key[1])))
    ]


def triple_rows(
    counter: Counter[tuple[Any, Any, Any]],
    total: int,
    fields: tuple[str, str, str],
    limit: int | None = None,
) -> list[dict[str, Any]]:
    """输出三元 edge-mass 表。"""
    rows = [
        {
            fields[0]: first,
            fields[1]: second,
            fields[2]: third,
            "edge_mass": counter[(first, second, third)],
            "edge_ratio": counter[(first, second, third)] / total,
        }
        for first, second, third in sorted(
            counter, key=lambda key: (-counter[key], str(key[0]), str(key[1]), str(key[2]))
        )
    ]
    return rows if limit is None else rows[:limit]


def route_key(row: dict[str, Any]) -> tuple[str, str]:
    """返回 exact route 键。"""
    return (row["adjacent_pair_gap_class"], row["route_class"])


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计两个最大 exact routes 的 sign-cycle ledger。"""
    previous_payload = json.loads(PREVIOUS_EXACT_ROUTE_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    _, selected = superclass_audit.selected_templates(max_prime)
    top_rows = [row for row in selected if route_key(row) in TOP_TWO_KEYS]

    route_edge_mass: Counter[tuple[str, str]] = Counter()
    route_template_count: Counter[tuple[str, str]] = Counter()
    cycle_edge_mass: Counter[int] = Counter()
    cycle_template_count: Counter[int] = Counter()
    switch_edge_mass: Counter[int] = Counter()
    switch_template_count: Counter[int] = Counter()
    sign_word_edge_mass: Counter[str] = Counter()
    sign_word_template_count: Counter[str] = Counter()
    sign_balance_edge_mass: Counter[str] = Counter()
    route_cycle_edge_mass: Counter[tuple[str, str, int]] = Counter()
    route_switch_edge_mass: Counter[tuple[str, str, int]] = Counter()
    route_sign_cycle_edge_mass: Counter[tuple[str, str, str]] = Counter()
    cycle_switch_edge_mass: Counter[tuple[int, int]] = Counter()
    q_prefix_edge_mass: Counter[int] = Counter()
    m_shell_edge_mass: Counter[int] = Counter()

    enriched_rows: list[dict[str, Any]] = []
    for row in top_rows:
        key = route_key(row)
        word = sign_word(row)
        switch_count = sign_switch_count(word)
        balance = sign_balance(word)
        mass = row["edge_mass"]
        cycle = row["cycle_length"]

        route_edge_mass[key] += mass
        route_template_count[key] += 1
        cycle_edge_mass[cycle] += mass
        cycle_template_count[cycle] += 1
        switch_edge_mass[switch_count] += mass
        switch_template_count[switch_count] += 1
        sign_word_edge_mass[word] += mass
        sign_word_template_count[word] += 1
        sign_balance_edge_mass[balance] += mass
        route_cycle_edge_mass[(key[0], key[1], cycle)] += mass
        route_switch_edge_mass[(key[0], key[1], switch_count)] += mass
        route_sign_cycle_edge_mass[(key[0], key[1], f"{word}|cycle={cycle}")] += mass
        cycle_switch_edge_mass[(cycle, switch_count)] += mass
        q_prefix_edge_mass[row["q_prefix_count"]] += mass
        m_shell_edge_mass[row["m_shell_prime_count"]] += mass
        enriched_rows.append(
            {
                **row,
                "m_pair": str(row["m_pair"]),
                "sign_word": word,
                "sign_switch_count": switch_count,
                "sign_balance": balance,
            }
        )

    total_template_count = len(top_rows)
    total_edge_mass = sum(row["edge_mass"] for row in top_rows)
    cycle_456_edge_mass = sum(value for cycle, value in cycle_edge_mass.items() if cycle in {4, 5, 6})
    sign_switch_le3_edge_mass = sum(value for switch, value in switch_edge_mass.items() if switch <= 3)
    cycle_456_and_switch_le3_edge_mass = sum(
        row["edge_mass"]
        for row in enriched_rows
        if row["cycle_length"] in {4, 5, 6} and row["sign_switch_count"] <= 3
    )
    all_pairwise_occurrence = all(row["occurrence_count"] == 2 for row in enriched_rows)
    all_mixed_sign = all(row["A_class"] == "mixed_positive_negative" for row in enriched_rows)

    expected_route_mass = {
        ("gap4_cousin_adjacent_pair_collision", "pure_right_tail_two_sided_collar"): 258,
        ("gap2_twin_adjacent_pair_collision", "pure_upper_wing_single_shell"): 212,
    }
    ledger_closed = (
        previous_payload["single_P_local_gap2_gap4_exact_route_class_ledger_closed"]
        and total_template_count == 48
        and total_edge_mass == previous["top_two_route_edge_mass"]
        and total_edge_mass == 470
        and all(route_edge_mass[key] == value for key, value in expected_route_mass.items())
        and len(route_edge_mass) == len(expected_route_mass)
        and all_pairwise_occurrence
        and all_mixed_sign
        and min(cycle_edge_mass) == 2
        and max(cycle_edge_mass) == 8
        and max(switch_edge_mass) == 6
        and cycle_456_edge_mass == 362
        and sign_switch_le3_edge_mass == 332
        and cycle_456_and_switch_le3_edge_mass == 270
    )

    top_templates = sorted(
        enriched_rows,
        key=lambda row: (
            -row["edge_mass"],
            row["adjacent_pair_gap_class"],
            row["route_class"],
            row["sign_word"],
        ),
    )[:24]

    return {
        "max_prime": max_prime,
        "previous_gap2_gap4_exact_route_class_ledger_closed": previous_payload[
            "single_P_local_gap2_gap4_exact_route_class_ledger_closed"
        ],
        "top_two_exact_route_sign_cycle_ledger_closed": ledger_closed,
        "top_two_exact_route_template_count": total_template_count,
        "top_two_exact_route_edge_mass": total_edge_mass,
        "gap4_right_tail_two_sided_edge_mass": route_edge_mass[
            ("gap4_cousin_adjacent_pair_collision", "pure_right_tail_two_sided_collar")
        ],
        "gap2_upper_wing_edge_mass": route_edge_mass[
            ("gap2_twin_adjacent_pair_collision", "pure_upper_wing_single_shell")
        ],
        "all_top_two_templates_pairwise_occurrence": all_pairwise_occurrence,
        "occurrence_count_two_edge_mass": total_edge_mass if all_pairwise_occurrence else 0,
        "occurrence_count_gt2_edge_mass": sum(
            row["edge_mass"] for row in enriched_rows if row["occurrence_count"] > 2
        ),
        "all_top_two_templates_mixed_positive_negative": all_mixed_sign,
        "mixed_positive_negative_edge_mass": total_edge_mass if all_mixed_sign else 0,
        "all_positive_edge_mass": sum(row["edge_mass"] for row in enriched_rows if row["A_class"] == "all_positive"),
        "cycle_length_min": min(cycle_edge_mass),
        "cycle_length_max": max(cycle_edge_mass),
        "sign_switch_count_max": max(switch_edge_mass),
        "cycle_4_5_6_edge_mass": cycle_456_edge_mass,
        "cycle_4_5_6_edge_ratio": cycle_456_edge_mass / total_edge_mass,
        "sign_switch_le3_edge_mass": sign_switch_le3_edge_mass,
        "sign_switch_le3_edge_ratio": sign_switch_le3_edge_mass / total_edge_mass,
        "cycle_4_5_6_and_switch_le3_edge_mass": cycle_456_and_switch_le3_edge_mass,
        "cycle_4_5_6_and_switch_le3_edge_ratio": cycle_456_and_switch_le3_edge_mass / total_edge_mass,
        "route_class_edge_rows": [
            {
                "adjacent_pair_gap_class": gap,
                "route_class": route,
                "edge_mass": route_edge_mass[(gap, route)],
                "edge_ratio": route_edge_mass[(gap, route)] / total_edge_mass,
                "template_count": route_template_count[(gap, route)],
            }
            for gap, route in sorted(route_edge_mass, key=lambda key: (-route_edge_mass[key], key[0], key[1]))
        ],
        "cycle_length_edge_rows": edge_rows(cycle_edge_mass, total_edge_mass, "cycle_length"),
        "cycle_length_template_rows": template_rows(cycle_template_count, total_template_count, "cycle_length"),
        "sign_switch_edge_rows": edge_rows(switch_edge_mass, total_edge_mass, "sign_switch_count"),
        "sign_switch_template_rows": template_rows(switch_template_count, total_template_count, "sign_switch_count"),
        "sign_word_edge_rows": edge_rows(sign_word_edge_mass, total_edge_mass, "sign_word")[:30],
        "sign_word_template_rows": template_rows(sign_word_template_count, total_template_count, "sign_word")[:30],
        "sign_balance_edge_rows": edge_rows(sign_balance_edge_mass, total_edge_mass, "sign_balance"),
        "route_cycle_edge_rows": triple_rows(
            route_cycle_edge_mass,
            total_edge_mass,
            ("adjacent_pair_gap_class", "route_class", "cycle_length"),
        ),
        "route_switch_edge_rows": triple_rows(
            route_switch_edge_mass,
            total_edge_mass,
            ("adjacent_pair_gap_class", "route_class", "sign_switch_count"),
        ),
        "route_sign_cycle_edge_rows": triple_rows(
            route_sign_cycle_edge_mass,
            total_edge_mass,
            ("adjacent_pair_gap_class", "route_class", "sign_cycle_signature"),
            limit=30,
        ),
        "cycle_switch_edge_rows": pair_rows(
            cycle_switch_edge_mass,
            total_edge_mass,
            "cycle_length",
            "sign_switch_count",
        ),
        "q_prefix_edge_rows": edge_rows(q_prefix_edge_mass, total_edge_mass, "q_prefix_count")[:30],
        "m_shell_edge_rows": edge_rows(m_shell_edge_mass, total_edge_mass, "m_shell_prime_count")[:30],
        "top_two_route_template_rows": [
            {
                "adjacent_pair_gap_class": row["adjacent_pair_gap_class"],
                "route_class": row["route_class"],
                "P": row["P"],
                "packet_index": row["packet_index"],
                "edge_mass": row["edge_mass"],
                "cycle_length": row["cycle_length"],
                "sign_word": row["sign_word"],
                "sign_switch_count": row["sign_switch_count"],
                "m_pair": row["m_pair"],
                "q_prefix_count": row["q_prefix_count"],
                "m_shell_prime_count": row["m_shell_prime_count"],
            }
            for row in top_templates
        ],
        "gap4_right_tail_two_sided_sign_cycle_bound_proved": False,
        "gap2_upper_wing_sign_cycle_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_sign_cycle_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "top_two_exact_route_sign_cycle_ledger_closed_collision_bounds_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the two largest exact routes carry 470 of 612 gap2/gap4 edge mass",
        "current_object": {
            "input": "the two largest gap2/gap4 exact route classes",
            "operation": "split them by pairwise occurrence, sign word, sign-switch count, and cycle length",
            "dominant_shape": "all top-two templates are pairwise mixed-sign occurrences with cycle length at most 8",
            "remaining": "prove sign-cycle collision bounds or route each packet to PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "Gap2Gap4ExactRouteClassLedgerImported",
                finite_audit["previous_gap2_gap4_exact_route_class_ledger_closed"],
                finite_audit["previous_gap2_gap4_exact_route_class_ledger_closed"],
                "The exact route-class ledger is imported.",
                "none for import",
            ),
            gate(
                "TopTwoExactRouteSignCycleLedger",
                finite_audit["top_two_exact_route_sign_cycle_ledger_closed"],
                finite_audit["top_two_exact_route_sign_cycle_ledger_closed"],
                "The two largest exact routes are split by sign/cycle signatures.",
                "none for the finite top-two sign-cycle ledger",
            ),
            gate(
                "Gap4RightTailTwoSidedSignCycleCollisionBound",
                False,
                False,
                "Control sign-cycle packets inside the largest exact route.",
                "finite audit shows 258 edge mass but no global theorem",
            ),
            gate(
                "Gap2UpperWingSignCycleCollisionBound",
                False,
                False,
                "Control sign-cycle packets inside the second largest exact route.",
                "finite audit shows 212 edge mass but no global theorem",
            ),
            gate(
                "ResidualExactRouteCollisionBounds",
                False,
                False,
                "Control lower wing, left collar, and other exact-route residuals.",
                "carried forward from the exact-route ledger",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "still need completion from local sign-cycle words to a usable bilinear family",
            "prime_gap_theorems": "do not see the signed word or cycle-length carrier",
            "short_interval_prime_inputs": "do not estimate fixed endpoint-packet sign-cycle equality",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND Gap4RightTailTwoSidedCousinSignCycleCollisionBound",
            "AND Gap2UpperWingTwinSignCycleCollisionBound",
            "AND Gap2LowerWingTwinCollisionBound",
            "AND Gap2RightTailTwoSidedTwinResidualCollisionBound",
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
        "top_two_exact_route_sign_cycle_ledger_closed": finite_audit[
            "top_two_exact_route_sign_cycle_ledger_closed"
        ],
        "gap4_right_tail_two_sided_sign_cycle_bound_proved": False,
        "gap2_upper_wing_sign_cycle_bound_proved": False,
        "gap2_lower_wing_twin_collision_bound_proved": False,
        "gap2_right_tail_twin_residual_bound_proved": False,
        "gap4_right_tail_left_collar_cousin_collision_bound_proved": False,
        "gap4_wing_cousin_residual_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two sign-cycle 审计",
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
        "## 2. top-two exact-route sign-cycle 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"top_two_exact_route_sign_cycle_ledger_closed={str(audit['top_two_exact_route_sign_cycle_ledger_closed']).lower()}",
        f"top_two_exact_route_template_count={audit['top_two_exact_route_template_count']}",
        f"top_two_exact_route_edge_mass={audit['top_two_exact_route_edge_mass']}",
        f"gap4_right_tail_two_sided_edge_mass={audit['gap4_right_tail_two_sided_edge_mass']}",
        f"gap2_upper_wing_edge_mass={audit['gap2_upper_wing_edge_mass']}",
        f"all_top_two_templates_pairwise_occurrence={str(audit['all_top_two_templates_pairwise_occurrence']).lower()}",
        f"occurrence_count_two_edge_mass={audit['occurrence_count_two_edge_mass']}",
        f"occurrence_count_gt2_edge_mass={audit['occurrence_count_gt2_edge_mass']}",
        f"all_top_two_templates_mixed_positive_negative={str(audit['all_top_two_templates_mixed_positive_negative']).lower()}",
        f"mixed_positive_negative_edge_mass={audit['mixed_positive_negative_edge_mass']}",
        f"all_positive_edge_mass={audit['all_positive_edge_mass']}",
        f"cycle_length_min={audit['cycle_length_min']}",
        f"cycle_length_max={audit['cycle_length_max']}",
        f"sign_switch_count_max={audit['sign_switch_count_max']}",
        f"cycle_4_5_6_edge_mass={audit['cycle_4_5_6_edge_mass']}",
        f"cycle_4_5_6_edge_ratio={audit['cycle_4_5_6_edge_ratio']}",
        f"sign_switch_le3_edge_mass={audit['sign_switch_le3_edge_mass']}",
        f"sign_switch_le3_edge_ratio={audit['sign_switch_le3_edge_ratio']}",
        f"cycle_4_5_6_and_switch_le3_edge_mass={audit['cycle_4_5_6_and_switch_le3_edge_mass']}",
        f"cycle_4_5_6_and_switch_le3_edge_ratio={audit['cycle_4_5_6_and_switch_le3_edge_ratio']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "route class edge mass：",
        "",
        *markdown_table(
            audit["route_class_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "template_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "cycle-length edge mass：",
        "",
        *markdown_table(audit["cycle_length_edge_rows"], ["cycle_length", "edge_mass", "edge_ratio"]),
        "",
        "sign-switch edge mass：",
        "",
        *markdown_table(audit["sign_switch_edge_rows"], ["sign_switch_count", "edge_mass", "edge_ratio"]),
        "",
        "sign-word edge mass：",
        "",
        *markdown_table(audit["sign_word_edge_rows"], ["sign_word", "edge_mass", "edge_ratio"]),
        "",
        "cycle-switch edge mass：",
        "",
        *markdown_table(
            audit["cycle_switch_edge_rows"],
            ["cycle_length", "sign_switch_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "route-cycle edge mass：",
        "",
        *markdown_table(
            audit["route_cycle_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "cycle_length", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高 top-two sign-cycle templates：",
        "",
        *markdown_table(
            audit["top_two_route_template_rows"],
            [
                "adjacent_pair_gap_class",
                "route_class",
                "P",
                "packet_index",
                "edge_mass",
                "cycle_length",
                "sign_word",
                "sign_switch_count",
                "m_pair",
                "q_prefix_count",
                "m_shell_prime_count",
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
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：两个最大 exact routes 已被压成 pairwise mixed-sign sign-cycle packets。",
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
        f"top_two_exact_route_sign_cycle_ledger_closed={str(payload['top_two_exact_route_sign_cycle_ledger_closed']).lower()}",
        f"gap4_right_tail_two_sided_sign_cycle_bound_proved={str(payload['gap4_right_tail_two_sided_sign_cycle_bound_proved']).lower()}",
        f"gap2_upper_wing_sign_cycle_bound_proved={str(payload['gap2_upper_wing_sign_cycle_bound_proved']).lower()}",
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
        "top_two_exact_route_sign_cycle_ledger_closed="
        f"{payload['top_two_exact_route_sign_cycle_ledger_closed']}"
    )
    print(f"top_two_exact_route_edge_mass={audit['top_two_exact_route_edge_mass']}")
    print(f"cycle_4_5_6_edge_mass={audit['cycle_4_5_6_edge_mass']}")
    print(f"sign_switch_le3_edge_mass={audit['sign_switch_le3_edge_mass']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
