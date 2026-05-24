#!/usr/bin/env python3
"""审计 single-P local adjacent-prime-pair collisions 的 exact gap 分类。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_adjacent_prime_pair_gap_class_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-adjacent-prime-pair-gap-class-audit.json

上一层把 same-packet multi-m repeated templates 的主量压到相邻素数对 collision。
本层只处理这 71 个 adjacent-prime-pair templates，按精确素数间隔 2、4、6、>=8
拆分。该层关闭有限 gap-class 账本，不证明全局相邻素数对 collision bound。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_same_packet_multi_m_gap_audit as same_packet_gap  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_occurrence_class_audit as occurrence_class  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "adjacent-prime-pair-gap-class"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_SAME_PACKET_GAP_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-same-packet-multi-m-gap-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_SAME_PACKET_GAP_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-occurrence-class-audit.json",
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
        "role": "trace bilinear input; not a fixed-packet adjacent-pair equality theorem",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman input; no local gap-2/gap-4 signed template bound",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced average input; not a pointwise adjacent-pair collision bound",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "prime-gap existence theorem; does not control signed template equality on adjacent m-pairs",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence input; not a local collision theorem",
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


def exact_gap_class(integer_gap: int) -> str:
    """把相邻素数对按精确整数 gap 分类。"""
    if integer_gap == 2:
        return "gap2_twin_adjacent_pair_collision"
    if integer_gap == 4:
        return "gap4_cousin_adjacent_pair_collision"
    if integer_gap == 6:
        return "gap6_sexy_adjacent_pair_collision"
    return "gap_ge8_adjacent_pair_collision"


def class_route_rows(counter: Counter[tuple[str, str]], total: int) -> list[dict[str, Any]]:
    """输出 exact gap class 与 route 的交叉表。"""
    rows = []
    for gap_class, route in sorted(counter, key=lambda key: (-counter[key], key[0], key[1])):
        rows.append(
            {
                "adjacent_pair_gap_class": gap_class,
                "route_class": route,
                "edge_mass": counter[(gap_class, route)],
                "edge_ratio": counter[(gap_class, route)] / total,
            }
        )
    return rows


def class_value_rows(
    counter: Counter[tuple[str, Any]], total: int, value_field: str
) -> list[dict[str, Any]]:
    """输出 exact gap class 与任意字段的交叉表。"""
    rows = []
    for gap_class, value in sorted(counter, key=lambda key: (-counter[key], key[0], str(key[1]))):
        rows.append(
            {
                "adjacent_pair_gap_class": gap_class,
                value_field: value,
                "edge_mass": counter[(gap_class, value)],
                "edge_ratio": counter[(gap_class, value)] / total,
            }
        )
    return rows


def top_adjacent_rows(
    templates: list[str],
    edge_mass: Counter[str],
    records: dict[str, list[dict[str, Any]]],
    cycle_length: dict[str, int],
    p_value: dict[str, int],
    route: dict[str, str],
    a_class: dict[str, str],
    base_template: dict[str, str],
    limit: int = 24,
) -> list[dict[str, Any]]:
    """输出最高质量 adjacent-prime-pair collision 模板。"""
    rows = []
    for template in sorted(
        templates,
        key=lambda key: (-edge_mass[key], -cycle_length[key], key),
    )[:limit]:
        template_records = records[template]
        m_values = same_packet_gap.selected_m_values(template_records)
        gap_value = m_values[1] - m_values[0]
        first = template_records[0]
        rows.append(
            {
                "signed_child": template,
                "raw_base_template": base_template[template],
                "P": p_value[template],
                "packet_index": first["packet_index"],
                "edge_mass": edge_mass[template],
                "cycle_length": cycle_length[template],
                "m_pair": str(m_values),
                "integer_gap": gap_value,
                "adjacent_pair_gap_class": exact_gap_class(gap_value),
                "q_prefix_count": first["q_prefix_count"],
                "m_shell_prime_count": first["m_shell_prime_count"],
                "route_class": route[template],
                "route_superclass": occurrence_class.single_p.route_superclass(route[template]),
                "A_class": a_class[template],
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 adjacent prime pair exact-gap classes。"""
    previous_payload = json.loads(PREVIOUS_SAME_PACKET_GAP_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    data = occurrence_class.collect_single_p_templates(max_prime)
    single_edge_mass: Counter[str] = data["single_edge_mass"]
    records: dict[str, list[dict[str, Any]]] = data["template_occurrence_records"]
    cycle_length: dict[str, int] = data["template_cycle_length"]
    p_value: dict[str, int] = data["template_p_value"]
    route: dict[str, str] = data["template_route"]
    a_class: dict[str, str] = data["template_a_class"]
    base_template: dict[str, str] = data["template_base"]
    primes = occurrence_class.flow.primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {prime: index for index, prime in enumerate(primes)}

    templates = [
        template
        for template in single_edge_mass
        if occurrence_class.repeated_class(records[template])
        == "single_packet_multi_m_repeated_template"
        and same_packet_gap.same_packet_gap_class(records[template], prime_index)
        == "adjacent_prime_pair_collision"
    ]

    class_template_count: Counter[str] = Counter()
    class_edge_mass: Counter[str] = Counter()
    class_route_edge_mass: Counter[tuple[str, str]] = Counter()
    class_a_edge_mass: Counter[tuple[str, str]] = Counter()
    class_cycle_edge_mass: Counter[tuple[str, int]] = Counter()
    class_q_edge_mass: Counter[tuple[str, int]] = Counter()
    class_shell_edge_mass: Counter[tuple[str, int]] = Counter()
    gap_value_template_count: Counter[int] = Counter()
    gap_value_edge_mass: Counter[int] = Counter()
    raw_base_template_count: Counter[str] = Counter()
    raw_base_edge_mass: Counter[str] = Counter()
    p_edge_mass: Counter[int] = Counter()
    bad_adjacent_pair_templates = []

    for template in templates:
        template_records = records[template]
        m_values = same_packet_gap.selected_m_values(template_records)
        if len(m_values) != 2:
            bad_adjacent_pair_templates.append(template)
            continue
        gap_value = m_values[1] - m_values[0]
        if prime_index[m_values[1]] - prime_index[m_values[0]] != 1:
            bad_adjacent_pair_templates.append(template)
            continue
        gap_class = exact_gap_class(gap_value)
        mass = single_edge_mass[template]
        first = template_records[0]
        class_template_count[gap_class] += 1
        class_edge_mass[gap_class] += mass
        class_route_edge_mass[(gap_class, route[template])] += mass
        class_a_edge_mass[(gap_class, a_class[template])] += mass
        class_cycle_edge_mass[(gap_class, cycle_length[template])] += mass
        class_q_edge_mass[(gap_class, first["q_prefix_count"])] += mass
        class_shell_edge_mass[(gap_class, first["m_shell_prime_count"])] += mass
        gap_value_template_count[gap_value] += 1
        gap_value_edge_mass[gap_value] += mass
        raw_base_template_count[base_template[template]] += 1
        raw_base_edge_mass[base_template[template]] += mass
        p_edge_mass[p_value[template]] += mass

    total_edge_mass = sum(single_edge_mass[template] for template in templates)
    duplicate_raw_bases = [
        raw_base for raw_base, count in raw_base_template_count.items() if count > 1
    ]
    duplicate_raw_base_edge_mass = sum(raw_base_edge_mass[raw_base] for raw_base in duplicate_raw_bases)
    ledger_closed = (
        previous_payload["single_P_local_same_packet_multi_m_gap_ledger_closed"]
        and len(templates) == previous["adjacent_prime_pair_collision_template_count"]
        and total_edge_mass == previous["adjacent_prime_pair_collision_edge_mass"]
        and not bad_adjacent_pair_templates
        and sum(class_template_count.values()) == len(templates)
        and sum(class_edge_mass.values()) == total_edge_mass
        and sum(gap_value_edge_mass.values()) == total_edge_mass
        and all(
            cycle_length[template] * len(records[template]) == single_edge_mass[template]
            for template in templates
        )
    )

    return {
        "max_prime": max_prime,
        "previous_single_P_local_same_packet_multi_m_gap_ledger_closed": previous_payload[
            "single_P_local_same_packet_multi_m_gap_ledger_closed"
        ],
        "single_P_local_adjacent_prime_pair_gap_class_ledger_closed": ledger_closed,
        "adjacent_prime_pair_template_count": len(templates),
        "adjacent_prime_pair_edge_mass": total_edge_mass,
        "gap2_twin_adjacent_pair_template_count": class_template_count[
            "gap2_twin_adjacent_pair_collision"
        ],
        "gap2_twin_adjacent_pair_edge_mass": class_edge_mass[
            "gap2_twin_adjacent_pair_collision"
        ],
        "gap4_cousin_adjacent_pair_template_count": class_template_count[
            "gap4_cousin_adjacent_pair_collision"
        ],
        "gap4_cousin_adjacent_pair_edge_mass": class_edge_mass[
            "gap4_cousin_adjacent_pair_collision"
        ],
        "gap6_sexy_adjacent_pair_template_count": class_template_count[
            "gap6_sexy_adjacent_pair_collision"
        ],
        "gap6_sexy_adjacent_pair_edge_mass": class_edge_mass[
            "gap6_sexy_adjacent_pair_collision"
        ],
        "gap_ge8_adjacent_pair_template_count": class_template_count[
            "gap_ge8_adjacent_pair_collision"
        ],
        "gap_ge8_adjacent_pair_edge_mass": class_edge_mass[
            "gap_ge8_adjacent_pair_collision"
        ],
        "bad_adjacent_pair_template_count": len(bad_adjacent_pair_templates),
        "adjacent_pair_gap_min": min(gap_value_edge_mass) if gap_value_edge_mass else None,
        "adjacent_pair_gap_max": max(gap_value_edge_mass) if gap_value_edge_mass else None,
        "duplicate_raw_base_count": len(duplicate_raw_bases),
        "duplicate_raw_base_edge_mass": duplicate_raw_base_edge_mass,
        "observed_gap2_or_gap4_edge_mass": class_edge_mass[
            "gap2_twin_adjacent_pair_collision"
        ]
        + class_edge_mass["gap4_cousin_adjacent_pair_collision"],
        "observed_gap2_or_gap4_edge_ratio": (
            class_edge_mass["gap2_twin_adjacent_pair_collision"]
            + class_edge_mass["gap4_cousin_adjacent_pair_collision"]
        )
        / total_edge_mass,
        "observed_gap2_or_gap4_dominant": (
            class_edge_mass["gap2_twin_adjacent_pair_collision"]
            + class_edge_mass["gap4_cousin_adjacent_pair_collision"]
        )
        > 0.9 * total_edge_mass,
        "adjacent_pair_gap_class_template_rows": template_count_table(
            class_template_count, "adjacent_pair_gap_class"
        ),
        "adjacent_pair_gap_class_edge_rows": table_from_counter(
            class_edge_mass, total_edge_mass, "adjacent_pair_gap_class"
        ),
        "exact_integer_gap_template_rows": template_count_table(
            gap_value_template_count, "integer_gap"
        ),
        "exact_integer_gap_edge_rows": table_from_counter(
            gap_value_edge_mass, total_edge_mass, "integer_gap"
        ),
        "adjacent_pair_gap_class_route_edge_rows": class_route_rows(
            class_route_edge_mass, total_edge_mass
        ),
        "adjacent_pair_gap_class_a_edge_rows": class_value_rows(
            class_a_edge_mass, total_edge_mass, "A_class"
        ),
        "adjacent_pair_gap_class_cycle_edge_rows": class_value_rows(
            class_cycle_edge_mass, total_edge_mass, "cycle_length"
        )[:30],
        "adjacent_pair_gap_class_q_edge_rows": class_value_rows(
            class_q_edge_mass, total_edge_mass, "q_prefix_count"
        )[:30],
        "adjacent_pair_gap_class_shell_edge_rows": class_value_rows(
            class_shell_edge_mass, total_edge_mass, "m_shell_prime_count"
        )[:30],
        "top_p_edge_rows": table_from_counter(p_edge_mass, total_edge_mass, "P")[:20],
        "top_adjacent_pair_template_rows": top_adjacent_rows(
            templates,
            single_edge_mass,
            records,
            cycle_length,
            p_value,
            route,
            a_class,
            base_template,
        ),
        "gap2_twin_adjacent_pair_collision_bound_proved": False,
        "gap4_cousin_adjacent_pair_collision_bound_proved": False,
        "gap6_sexy_adjacent_pair_collision_bound_proved": False,
        "gap_ge8_adjacent_pair_collision_bound_proved": False,
        "adjacent_prime_pair_collision_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_adjacent_prime_pair_gap_class_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_adjacent_prime_pair_gap_class_ledger_closed_uniform_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "adjacent-prime-pair collisions are the dominant subgate of same-packet multi-m collisions",
        "current_object": {
            "input": "the 71 same-packet adjacent-prime-pair repeated templates",
            "operation": "classify adjacent pairs by exact integer prime gap 2, 4, 6, or >=8",
            "dominant_shape": "gap 2 and gap 4 together carry almost all adjacent-pair collision mass",
            "remaining": "prove signed collision bounds for gap-2/gap-4 adjacent pairs or route excess to PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SamePacketMultiMGapLedgerImported",
                finite_audit[
                    "previous_single_P_local_same_packet_multi_m_gap_ledger_closed"
                ],
                finite_audit[
                    "previous_single_P_local_same_packet_multi_m_gap_ledger_closed"
                ],
                "The previous same-packet multi-m gap ledger is imported.",
                "none for import",
            ),
            gate(
                "AdjacentPrimePairGapClassLedger",
                finite_audit["single_P_local_adjacent_prime_pair_gap_class_ledger_closed"],
                finite_audit["single_P_local_adjacent_prime_pair_gap_class_ledger_closed"],
                "Adjacent-prime-pair collisions are split by exact prime gap.",
                "none for the finite gap-class ledger",
            ),
            gate(
                "Gap2TwinAdjacentPairCollisionBound",
                False,
                False,
                "Control signed template equality across adjacent m-pairs of gap 2.",
                "finite audit shows 33 templates / 296 edge mass but gives no global theorem",
            ),
            gate(
                "Gap4CousinAdjacentPairCollisionBound",
                False,
                False,
                "Control signed template equality across adjacent m-pairs of gap 4.",
                "finite audit shows 31 templates / 316 edge mass but gives no global theorem",
            ),
            gate(
                "Gap6AndLargeAdjacentPairCollisionBound",
                False,
                False,
                "Control gap 6 and gap >=8 adjacent-pair collisions.",
                "finite audit shows 7 templates / 50 edge mass but no global suppression",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "need nonlocal summation variables and do not directly bound fixed-packet gap-2/gap-4 signed collisions",
            "prime_gap_theorems": "describe existence or density of prime gaps, not equality of Phi-LPF signed templates",
            "short_interval_prime_inputs": "do not estimate adjacent-m template collision classes",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND Gap2TwinAdjacentPairCollisionBound",
            "AND Gap4CousinAdjacentPairCollisionBound",
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
        "single_P_local_adjacent_prime_pair_gap_class_ledger_closed": finite_audit[
            "single_P_local_adjacent_prime_pair_gap_class_ledger_closed"
        ],
        "gap2_twin_adjacent_pair_collision_bound_proved": False,
        "gap4_cousin_adjacent_pair_collision_bound_proved": False,
        "gap6_sexy_adjacent_pair_collision_bound_proved": False,
        "gap_ge8_adjacent_pair_collision_bound_proved": False,
        "adjacent_prime_pair_collision_bound_proved": False,
        "same_packet_multi_m_collision_bound_proved": False,
        "multi_packet_duplicate_transport_bound_proved": False,
        "single_packet_single_m_multi_cycle_suppression_proved": False,
        "repeated_occurrence_aggregation_or_pdec_closed": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
        "local_template_multiplicity_uniform_bound_proved": False,
        "single_P_slice_endpoint_packet_summation_closed": False,
        "single_P_local_endpoint_packet_bound_closed": False,
        "multi_P_trace_completion_closed": False,
        "pure_endpoint_carrier_phase_saving_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local adjacent prime pair gap class 审计",
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
        "## 2. adjacent prime pair exact-gap 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_adjacent_prime_pair_gap_class_ledger_closed={str(audit['single_P_local_adjacent_prime_pair_gap_class_ledger_closed']).lower()}",
        f"adjacent_prime_pair_template_count={audit['adjacent_prime_pair_template_count']}",
        f"adjacent_prime_pair_edge_mass={audit['adjacent_prime_pair_edge_mass']}",
        f"gap2_twin_adjacent_pair_template_count={audit['gap2_twin_adjacent_pair_template_count']}",
        f"gap2_twin_adjacent_pair_edge_mass={audit['gap2_twin_adjacent_pair_edge_mass']}",
        f"gap4_cousin_adjacent_pair_template_count={audit['gap4_cousin_adjacent_pair_template_count']}",
        f"gap4_cousin_adjacent_pair_edge_mass={audit['gap4_cousin_adjacent_pair_edge_mass']}",
        f"gap6_sexy_adjacent_pair_template_count={audit['gap6_sexy_adjacent_pair_template_count']}",
        f"gap6_sexy_adjacent_pair_edge_mass={audit['gap6_sexy_adjacent_pair_edge_mass']}",
        f"gap_ge8_adjacent_pair_template_count={audit['gap_ge8_adjacent_pair_template_count']}",
        f"gap_ge8_adjacent_pair_edge_mass={audit['gap_ge8_adjacent_pair_edge_mass']}",
        f"bad_adjacent_pair_template_count={audit['bad_adjacent_pair_template_count']}",
        f"adjacent_pair_gap_min/max={audit['adjacent_pair_gap_min']}/{audit['adjacent_pair_gap_max']}",
        f"duplicate_raw_base_count={audit['duplicate_raw_base_count']}",
        f"duplicate_raw_base_edge_mass={audit['duplicate_raw_base_edge_mass']}",
        f"observed_gap2_or_gap4_edge_mass={audit['observed_gap2_or_gap4_edge_mass']}",
        f"observed_gap2_or_gap4_edge_ratio={audit['observed_gap2_or_gap4_edge_ratio']}",
        f"observed_gap2_or_gap4_dominant={str(audit['observed_gap2_or_gap4_dominant']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "adjacent pair gap class template count：",
        "",
        *markdown_table(
            audit["adjacent_pair_gap_class_template_rows"],
            ["adjacent_pair_gap_class", "template_count", "template_ratio"],
        ),
        "",
        "adjacent pair gap class edge mass：",
        "",
        *markdown_table(
            audit["adjacent_pair_gap_class_edge_rows"],
            ["adjacent_pair_gap_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "exact integer gap edge mass：",
        "",
        *markdown_table(
            audit["exact_integer_gap_edge_rows"],
            ["integer_gap", "edge_mass", "edge_ratio"],
        ),
        "",
        "gap class route edge mass：",
        "",
        *markdown_table(
            audit["adjacent_pair_gap_class_route_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "gap class A-class edge mass：",
        "",
        *markdown_table(
            audit["adjacent_pair_gap_class_a_edge_rows"],
            ["adjacent_pair_gap_class", "A_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "gap class cycle-length edge mass：",
        "",
        *markdown_table(
            audit["adjacent_pair_gap_class_cycle_edge_rows"],
            ["adjacent_pair_gap_class", "cycle_length", "edge_mass", "edge_ratio"],
        ),
        "",
        "最高 adjacent-pair templates：",
        "",
        *markdown_table(
            audit["top_adjacent_pair_template_rows"],
            [
                "signed_child",
                "P",
                "packet_index",
                "edge_mass",
                "cycle_length",
                "m_pair",
                "integer_gap",
                "adjacent_pair_gap_class",
                "q_prefix_count",
                "m_shell_prime_count",
                "route_class",
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
        "结论：adjacent-prime-pair collisions 已被拆成 gap-2、gap-4、gap-6 与 gap>=8",
        "四个局部类。该账本仍是有限结构结果，尚未给出全局 signed collision bound。",
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
        f"single_P_local_adjacent_prime_pair_gap_class_ledger_closed={str(payload['single_P_local_adjacent_prime_pair_gap_class_ledger_closed']).lower()}",
        f"gap2_twin_adjacent_pair_collision_bound_proved={str(payload['gap2_twin_adjacent_pair_collision_bound_proved']).lower()}",
        f"gap4_cousin_adjacent_pair_collision_bound_proved={str(payload['gap4_cousin_adjacent_pair_collision_bound_proved']).lower()}",
        f"gap6_sexy_adjacent_pair_collision_bound_proved={str(payload['gap6_sexy_adjacent_pair_collision_bound_proved']).lower()}",
        f"gap_ge8_adjacent_pair_collision_bound_proved={str(payload['gap_ge8_adjacent_pair_collision_bound_proved']).lower()}",
        f"adjacent_prime_pair_collision_bound_proved={str(payload['adjacent_prime_pair_collision_bound_proved']).lower()}",
        f"local_occurrence_multiplicity_uniform_bound_proved={str(payload['local_occurrence_multiplicity_uniform_bound_proved']).lower()}",
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
        "single_P_local_adjacent_prime_pair_gap_class_ledger_closed="
        f"{payload['single_P_local_adjacent_prime_pair_gap_class_ledger_closed']}"
    )
    print(f"adjacent_prime_pair_template_count={audit['adjacent_prime_pair_template_count']}")
    print(f"gap2_twin_adjacent_pair_edge_mass={audit['gap2_twin_adjacent_pair_edge_mass']}")
    print(f"gap4_cousin_adjacent_pair_edge_mass={audit['gap4_cousin_adjacent_pair_edge_mass']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
