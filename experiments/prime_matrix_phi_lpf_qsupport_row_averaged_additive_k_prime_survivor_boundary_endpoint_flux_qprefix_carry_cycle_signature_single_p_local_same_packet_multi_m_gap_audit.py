#!/usr/bin/env python3
"""审计 single-P local same-packet multi-m repeated templates 的 m-gap 结构。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_same_packet_multi_m_gap_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-same-packet-multi-m-gap-audit.json

上一层把 repeated templates 分成同 packet 跨 m、跨 packet、同 packet 同 m 多 cycle
三类。本层只处理占主量的同 packet 跨 m 类，把它按 selected m-values 的素数间距
拆成相邻素数对、非相邻素数对、相邻素数链等局部形状。该层关闭有限 m-gap 分类
账本，不证明全局 collision bound。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_occurrence_class_audit as occurrence_class  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "same-packet-multi-m-gap"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_OCCURRENCE_CLASS_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-occurrence-class-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_OCCURRENCE_CLASS_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity-audit.json",
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
        "role": "trace bilinear input; not a same-packet adjacent-m collision theorem",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman input; needs extracted bilinear variables",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced average input; does not bound local m-gap template collisions",
    },
    {
        "key": "Pascadi_2025_nonabelian_amplification_kloosterman",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "composite Type-II input; still requires a nonlocal bilinear family",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2025_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "parameter-sum input; not a fixed-packet m-gap collision bound",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "prime existence input; does not estimate signed same-packet collisions",
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


def selected_m_values(records: list[dict[str, Any]]) -> list[int]:
    """取一个模板 occurrence 记录中的 selected m-values。"""
    return sorted({record["m_value"] for record in records})


def gap_vectors(records: list[dict[str, Any]], prime_index: dict[int, int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """返回整数 m-gap 向量与素数序号 gap 向量。"""
    values = selected_m_values(records)
    integer_gaps = tuple(right - left for left, right in zip(values, values[1:]))
    prime_index_gaps = tuple(
        prime_index[right] - prime_index[left] for left, right in zip(values, values[1:])
    )
    return integer_gaps, prime_index_gaps


def same_packet_gap_class(records: list[dict[str, Any]], prime_index: dict[int, int]) -> str:
    """按 selected m-values 的素数间距分类。"""
    values = selected_m_values(records)
    _, prime_index_gaps = gap_vectors(records, prime_index)
    adjacent = all(gap == 1 for gap in prime_index_gaps)
    if len(values) == 2 and adjacent:
        return "adjacent_prime_pair_collision"
    if len(values) == 2:
        return "nonadjacent_prime_pair_collision"
    if len(values) > 2 and adjacent:
        return "adjacent_prime_chain_collision"
    return "nonadjacent_prime_chain_collision"


def vector_rows(
    template_counter: Counter[tuple[int, ...]],
    edge_counter: Counter[tuple[int, ...]],
    field: str,
) -> list[dict[str, Any]]:
    """输出 gap-vector 表。"""
    total_templates = sum(template_counter.values())
    total_edges = sum(edge_counter.values())
    rows = []
    for key in sorted(edge_counter, key=lambda item: (-edge_counter[item], item)):
        rows.append(
            {
                field: str(list(key)),
                "template_count": template_counter[key],
                "template_ratio": template_counter[key] / total_templates,
                "edge_mass": edge_counter[key],
                "edge_ratio": edge_counter[key] / total_edges,
            }
        )
    return rows


def class_route_rows(counter: Counter[tuple[str, str]], total: int) -> list[dict[str, Any]]:
    """输出 gap class 与 route 的交叉表。"""
    rows = []
    for gap_class, route in sorted(counter, key=lambda key: (-counter[key], key[0], key[1])):
        rows.append(
            {
                "same_packet_gap_class": gap_class,
                "route_class": route,
                "edge_mass": counter[(gap_class, route)],
                "edge_ratio": counter[(gap_class, route)] / total,
            }
        )
    return rows


def top_gap_rows(
    templates: list[str],
    edge_mass: Counter[str],
    records: dict[str, list[dict[str, Any]]],
    cycle_length: dict[str, int],
    p_value: dict[str, int],
    route: dict[str, str],
    a_class: dict[str, str],
    prime_index: dict[int, int],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出最高质量 same-packet multi-m collision 模板。"""
    rows = []
    for template in sorted(
        templates,
        key=lambda key: (-edge_mass[key], -len(records[key]), -cycle_length[key], key),
    )[:limit]:
        template_records = records[template]
        integer_gaps, prime_index_gaps = gap_vectors(template_records, prime_index)
        m_values = selected_m_values(template_records)
        first = template_records[0]
        rows.append(
            {
                "signed_child": template,
                "P": p_value[template],
                "packet_index": first["packet_index"],
                "edge_mass": edge_mass[template],
                "cycle_length": cycle_length[template],
                "occurrence_count": len(template_records),
                "selected_m_values": str(m_values),
                "integer_gap_vector": str(list(integer_gaps)),
                "prime_index_gap_vector": str(list(prime_index_gaps)),
                "same_packet_gap_class": same_packet_gap_class(template_records, prime_index),
                "q_prefix_count": first["q_prefix_count"],
                "m_shell_prime_count": first["m_shell_prime_count"],
                "route_class": route[template],
                "route_superclass": occurrence_class.single_p.route_superclass(route[template]),
                "A_class": a_class[template],
            }
        )
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 same-packet multi-m gap ledger。"""
    previous_payload = json.loads(PREVIOUS_OCCURRENCE_CLASS_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    data = occurrence_class.collect_single_p_templates(max_prime)
    single_edge_mass: Counter[str] = data["single_edge_mass"]
    records: dict[str, list[dict[str, Any]]] = data["template_occurrence_records"]
    cycle_length: dict[str, int] = data["template_cycle_length"]
    p_value: dict[str, int] = data["template_p_value"]
    route: dict[str, str] = data["template_route"]
    a_class: dict[str, str] = data["template_a_class"]
    primes = occurrence_class.flow.primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {prime: index for index, prime in enumerate(primes)}

    templates = [
        template
        for template in single_edge_mass
        if occurrence_class.repeated_class(records[template])
        == "single_packet_multi_m_repeated_template"
    ]

    class_template_count: Counter[str] = Counter()
    class_edge_mass: Counter[str] = Counter()
    class_route_edge_mass: Counter[tuple[str, str]] = Counter()
    integer_gap_template_count: Counter[tuple[int, ...]] = Counter()
    integer_gap_edge_mass: Counter[tuple[int, ...]] = Counter()
    prime_gap_template_count: Counter[tuple[int, ...]] = Counter()
    prime_gap_edge_mass: Counter[tuple[int, ...]] = Counter()
    occurrence_edge_mass: Counter[int] = Counter()
    selected_m_support_edge_mass: Counter[int] = Counter()
    q_prefix_edge_mass: Counter[int] = Counter()
    shell_prime_edge_mass: Counter[int] = Counter()
    span_edge_mass: Counter[int] = Counter()
    p_edge_mass: Counter[int] = Counter()
    bad_same_packet_templates = []

    for template in templates:
        template_records = records[template]
        packet_support = {record["packet_index"] for record in template_records}
        if len(packet_support) != 1:
            bad_same_packet_templates.append(template)
        mass = single_edge_mass[template]
        gap_class = same_packet_gap_class(template_records, prime_index)
        integer_gaps, prime_index_gaps = gap_vectors(template_records, prime_index)
        m_values = selected_m_values(template_records)
        first = template_records[0]
        class_template_count[gap_class] += 1
        class_edge_mass[gap_class] += mass
        class_route_edge_mass[(gap_class, route[template])] += mass
        integer_gap_template_count[integer_gaps] += 1
        integer_gap_edge_mass[integer_gaps] += mass
        prime_gap_template_count[prime_index_gaps] += 1
        prime_gap_edge_mass[prime_index_gaps] += mass
        occurrence_edge_mass[len(template_records)] += mass
        selected_m_support_edge_mass[len(m_values)] += mass
        q_prefix_edge_mass[first["q_prefix_count"]] += mass
        shell_prime_edge_mass[first["m_shell_prime_count"]] += mass
        span_edge_mass[m_values[-1] - m_values[0]] += mass
        p_edge_mass[p_value[template]] += mass

    total_edge_mass = sum(single_edge_mass[template] for template in templates)
    ledger_closed = (
        previous_payload["single_P_local_template_occurrence_class_ledger_closed"]
        and len(templates) == previous["single_packet_multi_m_repeated_template_count"]
        and total_edge_mass == previous["single_packet_multi_m_repeated_edge_mass"]
        and not bad_same_packet_templates
        and sum(class_template_count.values()) == len(templates)
        and sum(class_edge_mass.values()) == total_edge_mass
        and sum(integer_gap_edge_mass.values()) == total_edge_mass
        and sum(prime_gap_edge_mass.values()) == total_edge_mass
        and sum(occurrence_edge_mass.values()) == total_edge_mass
        and sum(selected_m_support_edge_mass.values()) == total_edge_mass
        and all(
            cycle_length[template] * len(records[template]) == single_edge_mass[template]
            for template in templates
        )
    )

    max_prime_index_gap = max(
        (max(key) for key in prime_gap_edge_mass if key),
        default=0,
    )
    max_integer_gap = max((max(key) for key in integer_gap_edge_mass if key), default=0)
    max_occurrence_count = max(occurrence_edge_mass) if occurrence_edge_mass else 0
    max_selected_m_support = max(selected_m_support_edge_mass) if selected_m_support_edge_mass else 0

    return {
        "max_prime": max_prime,
        "previous_single_P_local_template_occurrence_class_ledger_closed": previous_payload[
            "single_P_local_template_occurrence_class_ledger_closed"
        ],
        "single_P_local_same_packet_multi_m_gap_ledger_closed": ledger_closed,
        "same_packet_multi_m_template_count": len(templates),
        "same_packet_multi_m_edge_mass": total_edge_mass,
        "adjacent_prime_pair_collision_template_count": class_template_count[
            "adjacent_prime_pair_collision"
        ],
        "adjacent_prime_pair_collision_edge_mass": class_edge_mass[
            "adjacent_prime_pair_collision"
        ],
        "nonadjacent_prime_pair_collision_template_count": class_template_count[
            "nonadjacent_prime_pair_collision"
        ],
        "nonadjacent_prime_pair_collision_edge_mass": class_edge_mass[
            "nonadjacent_prime_pair_collision"
        ],
        "adjacent_prime_chain_collision_template_count": class_template_count[
            "adjacent_prime_chain_collision"
        ],
        "adjacent_prime_chain_collision_edge_mass": class_edge_mass[
            "adjacent_prime_chain_collision"
        ],
        "nonadjacent_prime_chain_collision_template_count": class_template_count[
            "nonadjacent_prime_chain_collision"
        ],
        "nonadjacent_prime_chain_collision_edge_mass": class_edge_mass[
            "nonadjacent_prime_chain_collision"
        ],
        "bad_same_packet_template_count": len(bad_same_packet_templates),
        "same_packet_multi_m_occurrence_count_max": max_occurrence_count,
        "same_packet_multi_m_selected_m_support_count_max": max_selected_m_support,
        "same_packet_multi_m_prime_index_gap_max": max_prime_index_gap,
        "same_packet_multi_m_integer_gap_max": max_integer_gap,
        "observed_same_packet_multi_m_prime_index_gap_le_3": max_prime_index_gap <= 3,
        "observed_same_packet_multi_m_selected_support_le_4": max_selected_m_support <= 4,
        "observed_same_packet_multi_m_occurrence_count_le_4": max_occurrence_count <= 4,
        "observed_adjacent_prime_pair_dominant": class_edge_mass[
            "adjacent_prime_pair_collision"
        ]
        > 0.9 * total_edge_mass,
        "same_packet_gap_class_template_rows": template_count_table(
            class_template_count, "same_packet_gap_class"
        ),
        "same_packet_gap_class_edge_rows": table_from_counter(
            class_edge_mass, total_edge_mass, "same_packet_gap_class"
        ),
        "same_packet_gap_class_route_edge_rows": class_route_rows(
            class_route_edge_mass, total_edge_mass
        ),
        "integer_gap_vector_rows": vector_rows(
            integer_gap_template_count, integer_gap_edge_mass, "integer_gap_vector"
        ),
        "prime_index_gap_vector_rows": vector_rows(
            prime_gap_template_count, prime_gap_edge_mass, "prime_index_gap_vector"
        ),
        "occurrence_count_edge_rows": table_from_counter(
            occurrence_edge_mass, total_edge_mass, "occurrence_count"
        ),
        "selected_m_support_edge_rows": table_from_counter(
            selected_m_support_edge_mass, total_edge_mass, "selected_m_support_count"
        ),
        "q_prefix_count_edge_rows": table_from_counter(
            q_prefix_edge_mass, total_edge_mass, "q_prefix_count"
        )[:20],
        "m_shell_prime_count_edge_rows": table_from_counter(
            shell_prime_edge_mass, total_edge_mass, "m_shell_prime_count"
        ),
        "m_span_edge_rows": table_from_counter(span_edge_mass, total_edge_mass, "m_span")[:20],
        "top_p_edge_rows": table_from_counter(p_edge_mass, total_edge_mass, "P")[:20],
        "top_same_packet_multi_m_rows": top_gap_rows(
            templates,
            single_edge_mass,
            records,
            cycle_length,
            p_value,
            route,
            a_class,
            prime_index,
        ),
        "adjacent_prime_pair_collision_bound_proved": False,
        "nonadjacent_prime_pair_collision_bound_proved": False,
        "adjacent_prime_chain_collision_bound_proved": False,
        "same_packet_multi_m_collision_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_same_packet_multi_m_gap_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_same_packet_multi_m_gap_ledger_closed_uniform_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "same-packet multi-m collisions carry most repeated occurrence mass",
        "current_object": {
            "input": "the 78 single-P repeated templates whose occurrences stay in one packet but use multiple m-values",
            "operation": "classify selected m-values by integer gaps and prime-index gaps",
            "dominant_shape": "adjacent prime-pair collisions carry almost all same-packet multi-m mass",
            "remaining": "prove local adjacent-prime-pair collision bounds or route excess to PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RepeatedTemplateOccurrenceClassImported",
                finite_audit[
                    "previous_single_P_local_template_occurrence_class_ledger_closed"
                ],
                finite_audit[
                    "previous_single_P_local_template_occurrence_class_ledger_closed"
                ],
                "The previous repeated-template occurrence class ledger is imported.",
                "none for import",
            ),
            gate(
                "SamePacketMultiMGapLedger",
                finite_audit["single_P_local_same_packet_multi_m_gap_ledger_closed"],
                finite_audit["single_P_local_same_packet_multi_m_gap_ledger_closed"],
                "The same-packet multi-m collision class is split by selected m prime gaps.",
                "none for the finite gap ledger",
            ),
            gate(
                "AdjacentPrimePairCollisionBound",
                False,
                False,
                "Promote adjacent prime-pair dominance to a global local collision bound.",
                "finite audit shows 71 templates / 662 edge mass but gives no theorem",
            ),
            gate(
                "NonAdjacentPrimePairCollisionBound",
                False,
                False,
                "Control the six nonadjacent same-packet prime-pair collisions.",
                "finite audit shows 6 templates / 50 edge mass but no global exclusion",
            ),
            gate(
                "AdjacentPrimeChainCollisionBound",
                False,
                False,
                "Control the only observed adjacent prime chain collision.",
                "finite audit shows 1 template / 8 edge mass but no global suppression",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "need nonlocal summation variables and do not directly bound same-packet m-gap collisions",
            "prime_gap_inputs": "ordinary prime-gap information does not control signed template equality across adjacent m-values",
            "short_interval_prime_inputs": "do not estimate local signed same-packet collision classes",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND AdjacentPrimePairCollisionBound",
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
        "single_P_local_same_packet_multi_m_gap_ledger_closed": finite_audit[
            "single_P_local_same_packet_multi_m_gap_ledger_closed"
        ],
        "adjacent_prime_pair_collision_bound_proved": False,
        "nonadjacent_prime_pair_collision_bound_proved": False,
        "adjacent_prime_chain_collision_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local same-packet multi-m gap 审计",
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
        "## 2. same-packet multi-m gap 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_same_packet_multi_m_gap_ledger_closed={str(audit['single_P_local_same_packet_multi_m_gap_ledger_closed']).lower()}",
        f"same_packet_multi_m_template_count={audit['same_packet_multi_m_template_count']}",
        f"same_packet_multi_m_edge_mass={audit['same_packet_multi_m_edge_mass']}",
        f"adjacent_prime_pair_collision_template_count={audit['adjacent_prime_pair_collision_template_count']}",
        f"adjacent_prime_pair_collision_edge_mass={audit['adjacent_prime_pair_collision_edge_mass']}",
        f"nonadjacent_prime_pair_collision_template_count={audit['nonadjacent_prime_pair_collision_template_count']}",
        f"nonadjacent_prime_pair_collision_edge_mass={audit['nonadjacent_prime_pair_collision_edge_mass']}",
        f"adjacent_prime_chain_collision_template_count={audit['adjacent_prime_chain_collision_template_count']}",
        f"adjacent_prime_chain_collision_edge_mass={audit['adjacent_prime_chain_collision_edge_mass']}",
        f"bad_same_packet_template_count={audit['bad_same_packet_template_count']}",
        f"same_packet_multi_m_occurrence_count_max={audit['same_packet_multi_m_occurrence_count_max']}",
        f"same_packet_multi_m_selected_m_support_count_max={audit['same_packet_multi_m_selected_m_support_count_max']}",
        f"same_packet_multi_m_prime_index_gap_max={audit['same_packet_multi_m_prime_index_gap_max']}",
        f"same_packet_multi_m_integer_gap_max={audit['same_packet_multi_m_integer_gap_max']}",
        f"observed_same_packet_multi_m_prime_index_gap_le_3={str(audit['observed_same_packet_multi_m_prime_index_gap_le_3']).lower()}",
        f"observed_same_packet_multi_m_selected_support_le_4={str(audit['observed_same_packet_multi_m_selected_support_le_4']).lower()}",
        f"observed_same_packet_multi_m_occurrence_count_le_4={str(audit['observed_same_packet_multi_m_occurrence_count_le_4']).lower()}",
        f"observed_adjacent_prime_pair_dominant={str(audit['observed_adjacent_prime_pair_dominant']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "same-packet gap class template count：",
        "",
        *markdown_table(
            audit["same_packet_gap_class_template_rows"],
            ["same_packet_gap_class", "template_count", "template_ratio"],
        ),
        "",
        "same-packet gap class edge mass：",
        "",
        *markdown_table(
            audit["same_packet_gap_class_edge_rows"],
            ["same_packet_gap_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "same-packet gap class route edge mass：",
        "",
        *markdown_table(
            audit["same_packet_gap_class_route_edge_rows"],
            ["same_packet_gap_class", "route_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "integer m-gap vector rows：",
        "",
        *markdown_table(
            audit["integer_gap_vector_rows"],
            ["integer_gap_vector", "template_count", "template_ratio", "edge_mass", "edge_ratio"],
        ),
        "",
        "prime-index gap vector rows：",
        "",
        *markdown_table(
            audit["prime_index_gap_vector_rows"],
            [
                "prime_index_gap_vector",
                "template_count",
                "template_ratio",
                "edge_mass",
                "edge_ratio",
            ],
        ),
        "",
        "occurrence count edge mass：",
        "",
        *markdown_table(
            audit["occurrence_count_edge_rows"],
            ["occurrence_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "selected m-support edge mass：",
        "",
        *markdown_table(
            audit["selected_m_support_edge_rows"],
            ["selected_m_support_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "m-shell prime count edge mass：",
        "",
        *markdown_table(
            audit["m_shell_prime_count_edge_rows"],
            ["m_shell_prime_count", "edge_mass", "edge_ratio"],
        ),
        "",
        "m-span edge mass：",
        "",
        *markdown_table(audit["m_span_edge_rows"], ["m_span", "edge_mass", "edge_ratio"]),
        "",
        "最高 same-packet multi-m templates：",
        "",
        *markdown_table(
            audit["top_same_packet_multi_m_rows"],
            [
                "signed_child",
                "P",
                "packet_index",
                "edge_mass",
                "cycle_length",
                "occurrence_count",
                "selected_m_values",
                "integer_gap_vector",
                "prime_index_gap_vector",
                "same_packet_gap_class",
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
        "结论：same-packet multi-m repeated templates 已被拆成相邻素数对、非相邻素数对",
        "与相邻素数链三个局部 m-gap 类。该账本仍是有限结构结果，尚未给出全局",
        "collision bound，也尚未完成 PDEC/SAE 回流。",
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
        f"single_P_local_same_packet_multi_m_gap_ledger_closed={str(payload['single_P_local_same_packet_multi_m_gap_ledger_closed']).lower()}",
        f"adjacent_prime_pair_collision_bound_proved={str(payload['adjacent_prime_pair_collision_bound_proved']).lower()}",
        f"nonadjacent_prime_pair_collision_bound_proved={str(payload['nonadjacent_prime_pair_collision_bound_proved']).lower()}",
        f"adjacent_prime_chain_collision_bound_proved={str(payload['adjacent_prime_chain_collision_bound_proved']).lower()}",
        f"same_packet_multi_m_collision_bound_proved={str(payload['same_packet_multi_m_collision_bound_proved']).lower()}",
        f"multi_packet_duplicate_transport_bound_proved={str(payload['multi_packet_duplicate_transport_bound_proved']).lower()}",
        f"single_packet_single_m_multi_cycle_suppression_proved={str(payload['single_packet_single_m_multi_cycle_suppression_proved']).lower()}",
        f"local_occurrence_multiplicity_uniform_bound_proved={str(payload['local_occurrence_multiplicity_uniform_bound_proved']).lower()}",
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
        "single_P_local_same_packet_multi_m_gap_ledger_closed="
        f"{payload['single_P_local_same_packet_multi_m_gap_ledger_closed']}"
    )
    print(f"same_packet_multi_m_template_count={audit['same_packet_multi_m_template_count']}")
    print(
        "adjacent_prime_pair_collision_edge_mass="
        f"{audit['adjacent_prime_pair_collision_edge_mass']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
