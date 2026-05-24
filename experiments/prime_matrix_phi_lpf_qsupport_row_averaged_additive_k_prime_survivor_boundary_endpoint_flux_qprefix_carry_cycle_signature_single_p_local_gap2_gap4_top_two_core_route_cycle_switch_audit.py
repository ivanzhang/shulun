#!/usr/bin/env python3
"""审计 top-two sign-cycle 核心的 route-cycle-switch 原子分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_route_cycle_switch_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-route-cycle-switch-audit.json

上一层把两个最大 exact routes 拆成 pairwise mixed-sign sign-cycle packets。
本层只取其中 cycle length in {4,5,6} 且 sign-switch count <= 3 的核心
270 质量，并继续拆成 route x cycle x switch 原子。该层关闭有限核心分解
账本，不证明全局 signed collision bound。
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_route_superclass_audit as superclass_audit  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_sign_cycle_audit as top_two_audit  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-core-route-cycle-switch"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_TOP_TWO_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-sign-cycle-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_TOP_TWO_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

CORE_CYCLES = {4, 5, 6}
CORE_SWITCH_MAX = 3
EXTERNAL_SOURCES = top_two_audit.EXTERNAL_SOURCES


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
) -> list[dict[str, Any]]:
    """输出三元 edge-mass 表。"""
    return [
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


def route_label(row: dict[str, Any]) -> str:
    """把 route key 压成可读标签。"""
    if row["adjacent_pair_gap_class"] == "gap2_twin_adjacent_pair_collision":
        return "gap2_upper_wing"
    if row["adjacent_pair_gap_class"] == "gap4_cousin_adjacent_pair_collision":
        return "gap4_right_tail_two_sided"
    return f"{row['adjacent_pair_gap_class']}::{row['route_class']}"


def band_q_prefix(count: int) -> str:
    """q-prefix 粗分桶。"""
    if count <= 10:
        return "q<=10"
    if count <= 20:
        return "q<=20"
    return "q>20"


def band_m_shell(count: int) -> str:
    """m-shell prime count 粗分桶。"""
    if count <= 4:
        return "m<=4"
    if count <= 8:
        return "m<=8"
    return "m>8"


def selected_core_rows(max_prime: int) -> list[dict[str, Any]]:
    """抽取 top-two sign-cycle 的核心模板行。"""
    _, selected = superclass_audit.selected_templates(max_prime)
    rows: list[dict[str, Any]] = []
    for row in selected:
        if top_two_audit.route_key(row) not in top_two_audit.TOP_TWO_KEYS:
            continue
        word = top_two_audit.sign_word(row)
        switch_count = top_two_audit.sign_switch_count(word)
        if row["cycle_length"] not in CORE_CYCLES or switch_count > CORE_SWITCH_MAX:
            continue
        rows.append(
            {
                **row,
                "route_label": route_label(row),
                "m_pair": str(row["m_pair"]),
                "sign_word": word,
                "sign_switch_count": switch_count,
                "sign_balance": top_two_audit.sign_balance(word),
                "q_prefix_band": band_q_prefix(row["q_prefix_count"]),
                "m_shell_band": band_m_shell(row["m_shell_prime_count"]),
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计核心 route-cycle-switch 原子账本。"""
    previous_payload = json.loads(PREVIOUS_TOP_TWO_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    rows = selected_core_rows(max_prime)

    route_edge_mass: Counter[str] = Counter()
    route_template_count: Counter[str] = Counter()
    cycle_edge_mass: Counter[int] = Counter()
    cycle_template_count: Counter[int] = Counter()
    switch_edge_mass: Counter[int] = Counter()
    switch_template_count: Counter[int] = Counter()
    route_cycle_switch_edge_mass: Counter[tuple[str, int, int]] = Counter()
    route_cycle_edge_mass: Counter[tuple[str, int]] = Counter()
    route_switch_edge_mass: Counter[tuple[str, int]] = Counter()
    cycle_switch_edge_mass: Counter[tuple[int, int]] = Counter()
    sign_word_edge_mass: Counter[str] = Counter()
    sign_word_template_count: Counter[str] = Counter()
    q_prefix_band_edge_mass: Counter[str] = Counter()
    m_shell_band_edge_mass: Counter[str] = Counter()

    for row in rows:
        mass = row["edge_mass"]
        route = row["route_label"]
        cycle = row["cycle_length"]
        switch_count = row["sign_switch_count"]
        route_edge_mass[route] += mass
        route_template_count[route] += 1
        cycle_edge_mass[cycle] += mass
        cycle_template_count[cycle] += 1
        switch_edge_mass[switch_count] += mass
        switch_template_count[switch_count] += 1
        route_cycle_switch_edge_mass[(route, cycle, switch_count)] += mass
        route_cycle_edge_mass[(route, cycle)] += mass
        route_switch_edge_mass[(route, switch_count)] += mass
        cycle_switch_edge_mass[(cycle, switch_count)] += mass
        sign_word_edge_mass[row["sign_word"]] += mass
        sign_word_template_count[row["sign_word"]] += 1
        q_prefix_band_edge_mass[row["q_prefix_band"]] += mass
        m_shell_band_edge_mass[row["m_shell_band"]] += mass

    total_template_count = len(rows)
    total_edge_mass = sum(row["edge_mass"] for row in rows)
    noncore_edge_mass = previous["top_two_exact_route_edge_mass"] - total_edge_mass
    largest_atom_edge_mass = max(route_cycle_switch_edge_mass.values())
    largest_atom_ratio_inside_core = largest_atom_edge_mass / total_edge_mass
    atom_count = len(route_cycle_switch_edge_mass)
    all_pairwise_occurrence = all(row["occurrence_count"] == 2 for row in rows)
    all_mixed_sign = all(row["A_class"] == "mixed_positive_negative" for row in rows)
    all_cycles_in_core = set(cycle_edge_mass) == CORE_CYCLES
    all_switches_le3 = max(switch_edge_mass) <= CORE_SWITCH_MAX

    ledger_closed = (
        previous_payload["top_two_exact_route_sign_cycle_ledger_closed"]
        and total_template_count == 29
        and total_edge_mass == previous["cycle_4_5_6_and_switch_le3_edge_mass"]
        and total_edge_mass == 270
        and noncore_edge_mass == 200
        and atom_count == 11
        and largest_atom_edge_mass == 70
        and route_edge_mass["gap2_upper_wing"] == 140
        and route_edge_mass["gap4_right_tail_two_sided"] == 130
        and cycle_edge_mass[5] == 150
        and cycle_edge_mass[4] == 96
        and cycle_edge_mass[6] == 24
        and switch_edge_mass[3] == 146
        and switch_edge_mass[1] == 64
        and switch_edge_mass[2] == 60
        and all_pairwise_occurrence
        and all_mixed_sign
        and all_cycles_in_core
        and all_switches_le3
    )

    top_templates = sorted(
        rows,
        key=lambda row: (
            -row["edge_mass"],
            row["route_label"],
            row["cycle_length"],
            row["sign_switch_count"],
            row["sign_word"],
        ),
    )[:24]

    return {
        "max_prime": max_prime,
        "previous_top_two_exact_route_sign_cycle_ledger_closed": previous_payload[
            "top_two_exact_route_sign_cycle_ledger_closed"
        ],
        "top_two_core_route_cycle_switch_ledger_closed": ledger_closed,
        "core_definition": "cycle_length in {4,5,6} and sign_switch_count <= 3",
        "core_template_count": total_template_count,
        "core_edge_mass": total_edge_mass,
        "core_edge_ratio_inside_top_two": total_edge_mass / previous["top_two_exact_route_edge_mass"],
        "noncore_top_two_edge_mass": noncore_edge_mass,
        "noncore_top_two_edge_ratio": noncore_edge_mass / previous["top_two_exact_route_edge_mass"],
        "route_cycle_switch_atom_count": atom_count,
        "largest_route_cycle_switch_atom_edge_mass": largest_atom_edge_mass,
        "largest_route_cycle_switch_atom_ratio_inside_core": largest_atom_ratio_inside_core,
        "gap2_upper_wing_core_edge_mass": route_edge_mass["gap2_upper_wing"],
        "gap4_right_tail_two_sided_core_edge_mass": route_edge_mass["gap4_right_tail_two_sided"],
        "cycle5_core_edge_mass": cycle_edge_mass[5],
        "cycle4_core_edge_mass": cycle_edge_mass[4],
        "cycle6_core_edge_mass": cycle_edge_mass[6],
        "sign_switch3_core_edge_mass": switch_edge_mass[3],
        "sign_switch1_core_edge_mass": switch_edge_mass[1],
        "sign_switch2_core_edge_mass": switch_edge_mass[2],
        "all_core_templates_pairwise_occurrence": all_pairwise_occurrence,
        "all_core_templates_mixed_positive_negative": all_mixed_sign,
        "all_core_cycles_are_4_5_6": all_cycles_in_core,
        "all_core_switches_le3": all_switches_le3,
        "route_edge_rows": [
            {
                "route_label": route,
                "template_count": route_template_count[route],
                "edge_mass": route_edge_mass[route],
                "edge_ratio": route_edge_mass[route] / total_edge_mass,
            }
            for route in sorted(route_edge_mass, key=lambda key: (-route_edge_mass[key], key))
        ],
        "cycle_edge_rows": edge_rows(cycle_edge_mass, total_edge_mass, "cycle_length"),
        "cycle_template_rows": template_rows(cycle_template_count, total_template_count, "cycle_length"),
        "sign_switch_edge_rows": edge_rows(switch_edge_mass, total_edge_mass, "sign_switch_count"),
        "sign_switch_template_rows": template_rows(
            switch_template_count, total_template_count, "sign_switch_count"
        ),
        "route_cycle_switch_edge_rows": triple_rows(
            route_cycle_switch_edge_mass,
            total_edge_mass,
            ("route_label", "cycle_length", "sign_switch_count"),
        ),
        "route_cycle_edge_rows": pair_rows(
            route_cycle_edge_mass,
            total_edge_mass,
            "route_label",
            "cycle_length",
        ),
        "route_switch_edge_rows": pair_rows(
            route_switch_edge_mass,
            total_edge_mass,
            "route_label",
            "sign_switch_count",
        ),
        "cycle_switch_edge_rows": pair_rows(
            cycle_switch_edge_mass,
            total_edge_mass,
            "cycle_length",
            "sign_switch_count",
        ),
        "sign_word_edge_rows": edge_rows(sign_word_edge_mass, total_edge_mass, "sign_word"),
        "sign_word_template_rows": template_rows(sign_word_template_count, total_template_count, "sign_word"),
        "q_prefix_band_edge_rows": edge_rows(q_prefix_band_edge_mass, total_edge_mass, "q_prefix_band"),
        "m_shell_band_edge_rows": edge_rows(m_shell_band_edge_mass, total_edge_mass, "m_shell_band"),
        "top_core_template_rows": [
            {
                "route_label": row["route_label"],
                "P": row["P"],
                "packet_index": row["packet_index"],
                "edge_mass": row["edge_mass"],
                "cycle_length": row["cycle_length"],
                "sign_switch_count": row["sign_switch_count"],
                "sign_word": row["sign_word"],
                "m_pair": row["m_pair"],
                "q_prefix_count": row["q_prefix_count"],
                "m_shell_prime_count": row["m_shell_prime_count"],
            }
            for row in top_templates
        ],
        "core_route_cycle_switch_collision_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_route_cycle_switch_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "top_two_core_route_cycle_switch_ledger_closed_atom_bounds_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the fastest current route is still the finite Phi-LPF single-P local top-two carrier split",
        "current_object": {
            "input": "cycle 4/5/6 and sign-switch <=3 core inside the top-two exact routes",
            "operation": "split the 270 edge mass by route, cycle length, and sign-switch count",
            "dominant_shape": "the core splits into 11 route-cycle-switch atoms; the largest atom has edge mass 70",
            "remaining": "prove one of the atom collision bounds, aggregate atoms through PDEC/SAE, or complete the endpoint trace family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "TopTwoExactRouteSignCycleLedgerImported",
                finite_audit["previous_top_two_exact_route_sign_cycle_ledger_closed"],
                finite_audit["previous_top_two_exact_route_sign_cycle_ledger_closed"],
                "The top-two exact-route sign-cycle ledger is imported.",
                "none for import",
            ),
            gate(
                "TopTwoCoreRouteCycleSwitchLedger",
                finite_audit["top_two_core_route_cycle_switch_ledger_closed"],
                finite_audit["top_two_core_route_cycle_switch_ledger_closed"],
                "The 270-mass cycle 4/5/6 and switch<=3 core is split into route-cycle-switch atoms.",
                "none for the finite core atom ledger",
            ),
            gate(
                "LargestCoreAtomCollisionBound",
                False,
                False,
                "Control the largest 70-mass route-cycle-switch atom.",
                "finite audit identifies the atom but gives no global theorem",
            ),
            gate(
                "AllCoreAtomCollisionBoundsOrPDEC",
                False,
                False,
                "Control all 11 core atoms or route them through PDEC/SAE.",
                "requires signed equality, aggregation, or endpoint trace completion",
            ),
            gate(
                "NonCoreTopTwoSignCycleResidual",
                False,
                False,
                "Control the remaining 200 edge mass outside the core.",
                "carried forward from the top-two sign-cycle ledger",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "still need completion from route-cycle-switch atoms to a bilinear or trace-family object",
            "prime_gap_theorems": "identify possible prime gaps but do not control signed local atom equality",
            "short_interval_prime_inputs": "remain above theta=1/2 and do not see fixed endpoint sign-cycle atoms",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND Gap4RightTailTwoSidedCousinCoreRouteCycleSwitchAtomBound",
            "AND Gap2UpperWingTwinCoreRouteCycleSwitchAtomBound",
            "AND TopTwoNonCoreSignCycleResidualBound",
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
        "top_two_core_route_cycle_switch_ledger_closed": finite_audit[
            "top_two_core_route_cycle_switch_ledger_closed"
        ],
        "core_route_cycle_switch_collision_bound_proved": False,
        "largest_core_atom_collision_bound_proved": False,
        "top_two_noncore_residual_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core route-cycle-switch 审计",
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
        "## 2. core route-cycle-switch 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"top_two_core_route_cycle_switch_ledger_closed={str(audit['top_two_core_route_cycle_switch_ledger_closed']).lower()}",
        f"core_definition={audit['core_definition']}",
        f"core_template_count={audit['core_template_count']}",
        f"core_edge_mass={audit['core_edge_mass']}",
        f"core_edge_ratio_inside_top_two={audit['core_edge_ratio_inside_top_two']}",
        f"noncore_top_two_edge_mass={audit['noncore_top_two_edge_mass']}",
        f"route_cycle_switch_atom_count={audit['route_cycle_switch_atom_count']}",
        f"largest_route_cycle_switch_atom_edge_mass={audit['largest_route_cycle_switch_atom_edge_mass']}",
        f"largest_route_cycle_switch_atom_ratio_inside_core={audit['largest_route_cycle_switch_atom_ratio_inside_core']}",
        f"gap2_upper_wing_core_edge_mass={audit['gap2_upper_wing_core_edge_mass']}",
        f"gap4_right_tail_two_sided_core_edge_mass={audit['gap4_right_tail_two_sided_core_edge_mass']}",
        f"cycle5_core_edge_mass={audit['cycle5_core_edge_mass']}",
        f"cycle4_core_edge_mass={audit['cycle4_core_edge_mass']}",
        f"cycle6_core_edge_mass={audit['cycle6_core_edge_mass']}",
        f"sign_switch3_core_edge_mass={audit['sign_switch3_core_edge_mass']}",
        f"sign_switch1_core_edge_mass={audit['sign_switch1_core_edge_mass']}",
        f"sign_switch2_core_edge_mass={audit['sign_switch2_core_edge_mass']}",
        f"all_core_templates_pairwise_occurrence={str(audit['all_core_templates_pairwise_occurrence']).lower()}",
        f"all_core_templates_mixed_positive_negative={str(audit['all_core_templates_mixed_positive_negative']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "route edge mass：",
        "",
        *markdown_table(audit["route_edge_rows"], ["route_label", "template_count", "edge_mass", "edge_ratio"]),
        "",
        "route-cycle-switch atom edge mass：",
        "",
        *markdown_table(
            audit["route_cycle_switch_edge_rows"],
            ["route_label", "cycle_length", "sign_switch_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "cycle edge mass：",
        "",
        *markdown_table(audit["cycle_edge_rows"], ["cycle_length", "edge_mass", "edge_ratio"]),
        "",
        "sign-switch edge mass：",
        "",
        *markdown_table(audit["sign_switch_edge_rows"], ["sign_switch_count", "edge_mass", "edge_ratio"]),
        "",
        "cycle-switch edge mass：",
        "",
        *markdown_table(
            audit["cycle_switch_edge_rows"],
            ["cycle_length", "sign_switch_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "q-prefix / m-shell bands：",
        "",
        *markdown_table(audit["q_prefix_band_edge_rows"], ["q_prefix_band", "edge_mass", "edge_ratio"]),
        "",
        *markdown_table(audit["m_shell_band_edge_rows"], ["m_shell_band", "edge_mass", "edge_ratio"]),
        "",
        "最高 core templates：",
        "",
        *markdown_table(
            audit["top_core_template_rows"],
            [
                "route_label",
                "P",
                "packet_index",
                "edge_mass",
                "cycle_length",
                "sign_switch_count",
                "sign_word",
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
        "结论：top-two sign-cycle 的 270 核心已被压成 11 个 route-cycle-switch 原子。",
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
        f"top_two_core_route_cycle_switch_ledger_closed={str(payload['top_two_core_route_cycle_switch_ledger_closed']).lower()}",
        f"core_route_cycle_switch_collision_bound_proved={str(payload['core_route_cycle_switch_collision_bound_proved']).lower()}",
        f"largest_core_atom_collision_bound_proved={str(payload['largest_core_atom_collision_bound_proved']).lower()}",
        f"top_two_noncore_residual_bound_proved={str(payload['top_two_noncore_residual_bound_proved']).lower()}",
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
        "top_two_core_route_cycle_switch_ledger_closed="
        f"{payload['top_two_core_route_cycle_switch_ledger_closed']}"
    )
    print(f"core_edge_mass={audit['core_edge_mass']}")
    print(f"route_cycle_switch_atom_count={audit['route_cycle_switch_atom_count']}")
    print(f"largest_route_cycle_switch_atom_edge_mass={audit['largest_route_cycle_switch_atom_edge_mass']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
