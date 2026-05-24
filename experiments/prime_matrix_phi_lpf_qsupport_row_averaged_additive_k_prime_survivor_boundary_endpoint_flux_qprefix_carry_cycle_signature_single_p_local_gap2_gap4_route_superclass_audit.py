#!/usr/bin/env python3
"""审计 gap-2/gap-4 adjacent-prime-pair collisions 的 route-superclass 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_route_superclass_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-route-superclass-audit.json

上一层把 adjacent-prime-pair collision 拆成 gap 2、gap 4、gap 6、gap >=8。
本层只处理主量 gap 2 与 gap 4，并按几何 route-superclass 拆成：
gap2-wing、gap2-right-tail、gap4-right-tail、gap4-wing。该层关闭有限
route-superclass 账本，不证明全局 signed collision bound。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_adjacent_prime_pair_gap_class_audit as gap_class  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_same_packet_multi_m_gap_audit as same_packet_gap  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_occurrence_class_audit as occurrence_class  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-route-superclass"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_ADJACENT_GAP_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-adjacent-prime-pair-gap-class-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_ADJACENT_GAP_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-same-packet-multi-m-gap-audit.json",
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
        "role": "trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "useful after Kloosterman completion; does not prove fixed packet route-superclass collision control",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "average inverse-fraction input; not pointwise for one gap2/gap4 carrier",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "prime-gap existence input; not a signed Phi-LPF route-superclass theorem",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence input; does not estimate local adjacent-pair template equality",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def route_superclass(route: str) -> str:
    """返回既有 single-P local route 的几何 superclass。"""
    return occurrence_class.single_p.route_superclass(route)


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


def template_rows(counter: Counter[Any], field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 template-count 表。"""
    total = sum(counter.values())
    return [
        {field: key, "template_count": counter[key], "template_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def pair_rows(
    counter: Counter[tuple[str, str]], total: int, left_field: str, right_field: str
) -> list[dict[str, Any]]:
    """输出二元分类 edge 表。"""
    return [
        {
            left_field: left,
            right_field: right,
            "edge_mass": counter[(left, right)],
            "edge_ratio": counter[(left, right)] / total,
        }
        for left, right in sorted(counter, key=lambda key: (-counter[key], key[0], key[1]))
    ]


def triple_rows(
    counter: Counter[tuple[str, str, Any]],
    total: int,
    value_field: str,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    """输出 gap class、route superclass 与第三字段的交叉表。"""
    rows = [
        {
            "adjacent_pair_gap_class": gap,
            "route_superclass": superclass,
            value_field: value,
            "edge_mass": counter[(gap, superclass, value)],
            "edge_ratio": counter[(gap, superclass, value)] / total,
        }
        for gap, superclass, value in sorted(
            counter, key=lambda key: (-counter[key], key[0], key[1], str(key[2]))
        )
    ]
    return rows if limit is None else rows[:limit]


def p_band(P: int) -> str:
    """粗分 P 尺度，避免把有限样本误读成连续分布定理。"""
    if P < 700:
        return "P<700"
    if P < 900:
        return "700<=P<900"
    return "P>=900"


def selected_templates(max_prime: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """抽取 gap2/gap4 adjacent-prime-pair templates。"""
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

    selected: list[dict[str, Any]] = []
    for template in single_edge_mass:
        if occurrence_class.repeated_class(records[template]) != "single_packet_multi_m_repeated_template":
            continue
        if same_packet_gap.same_packet_gap_class(records[template], prime_index) != "adjacent_prime_pair_collision":
            continue

        m_values = same_packet_gap.selected_m_values(records[template])
        if len(m_values) != 2:
            continue
        gap_value = m_values[1] - m_values[0]
        gap_name = gap_class.exact_gap_class(gap_value)
        if gap_name not in {
            "gap2_twin_adjacent_pair_collision",
            "gap4_cousin_adjacent_pair_collision",
        }:
            continue

        first = records[template][0]
        selected.append(
            {
                "signed_child": template,
                "raw_base_template": base_template[template],
                "P": p_value[template],
                "P_band": p_band(p_value[template]),
                "packet_index": first["packet_index"],
                "edge_mass": single_edge_mass[template],
                "occurrence_count": len(records[template]),
                "cycle_length": cycle_length[template],
                "m_pair": m_values,
                "integer_gap": gap_value,
                "adjacent_pair_gap_class": gap_name,
                "q_prefix_count": first["q_prefix_count"],
                "m_shell_prime_count": first["m_shell_prime_count"],
                "route_class": route[template],
                "route_superclass": route_superclass(route[template]),
                "A_class": a_class[template],
            }
        )

    context = {
        "data": data,
        "previous_adjacent_gap_audit": json.loads(PREVIOUS_ADJACENT_GAP_AUDIT.read_text()),
    }
    return context, selected


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 gap2/gap4 route-superclass ledger。"""
    context, selected = selected_templates(max_prime)
    previous = context["previous_adjacent_gap_audit"]
    previous_audit = previous["finite_audit"]

    class_template_count: Counter[str] = Counter()
    class_edge_mass: Counter[str] = Counter()
    superclass_template_count: Counter[tuple[str, str]] = Counter()
    superclass_edge_mass: Counter[tuple[str, str]] = Counter()
    route_edge_mass: Counter[tuple[str, str]] = Counter()
    a_edge_mass: Counter[tuple[str, str, str]] = Counter()
    cycle_edge_mass: Counter[tuple[str, str, int]] = Counter()
    q_edge_mass: Counter[tuple[str, str, int]] = Counter()
    shell_edge_mass: Counter[tuple[str, str, int]] = Counter()
    p_band_edge_mass: Counter[tuple[str, str, str]] = Counter()
    raw_base_count: defaultdict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    raw_base_edge_mass: Counter[tuple[str, str, str]] = Counter()

    for row in selected:
        gap = row["adjacent_pair_gap_class"]
        superclass = row["route_superclass"]
        mass = row["edge_mass"]
        class_template_count[gap] += 1
        class_edge_mass[gap] += mass
        superclass_template_count[(gap, superclass)] += 1
        superclass_edge_mass[(gap, superclass)] += mass
        route_edge_mass[(gap, row["route_class"])] += mass
        a_edge_mass[(gap, superclass, row["A_class"])] += mass
        cycle_edge_mass[(gap, superclass, row["cycle_length"])] += mass
        q_edge_mass[(gap, superclass, row["q_prefix_count"])] += mass
        shell_edge_mass[(gap, superclass, row["m_shell_prime_count"])] += mass
        p_band_edge_mass[(gap, superclass, row["P_band"])] += mass
        raw_base_count[(gap, superclass)][row["raw_base_template"]] += 1
        raw_base_edge_mass[(gap, superclass, row["raw_base_template"])] += mass

    total_edge_mass = sum(row["edge_mass"] for row in selected)
    total_template_count = len(selected)
    gap2_wing_mass = superclass_edge_mass[
        ("gap2_twin_adjacent_pair_collision", "wing_single_P_local")
    ]
    gap2_tail_mass = superclass_edge_mass[
        ("gap2_twin_adjacent_pair_collision", "right_tail_single_P_local")
    ]
    gap4_tail_mass = superclass_edge_mass[
        ("gap4_cousin_adjacent_pair_collision", "right_tail_single_P_local")
    ]
    gap4_wing_mass = superclass_edge_mass[
        ("gap4_cousin_adjacent_pair_collision", "wing_single_P_local")
    ]
    dominant_aligned_edge_mass = gap2_wing_mass + gap4_tail_mass
    offdominant_edge_mass = gap2_tail_mass + gap4_wing_mass

    duplicate_raw_base_rows = []
    duplicate_raw_base_count = 0
    duplicate_raw_base_edge_mass = 0
    for (gap, superclass), counter in sorted(raw_base_count.items()):
        duplicate_bases = [base for base, count in counter.items() if count > 1]
        for base in duplicate_bases:
            duplicate_raw_base_count += 1
            mass = raw_base_edge_mass[(gap, superclass, base)]
            duplicate_raw_base_edge_mass += mass
            duplicate_raw_base_rows.append(
                {
                    "adjacent_pair_gap_class": gap,
                    "route_superclass": superclass,
                    "raw_base_template": base,
                    "template_count": counter[base],
                    "edge_mass": mass,
                    "edge_ratio": mass / total_edge_mass,
                }
            )

    previous_gap2_gap4_edge_mass = (
        previous_audit["gap2_twin_adjacent_pair_edge_mass"]
        + previous_audit["gap4_cousin_adjacent_pair_edge_mass"]
    )
    ledger_closed = (
        previous["single_P_local_adjacent_prime_pair_gap_class_ledger_closed"]
        and class_edge_mass["gap2_twin_adjacent_pair_collision"]
        == previous_audit["gap2_twin_adjacent_pair_edge_mass"]
        and class_edge_mass["gap4_cousin_adjacent_pair_collision"]
        == previous_audit["gap4_cousin_adjacent_pair_edge_mass"]
        and class_template_count["gap2_twin_adjacent_pair_collision"]
        == previous_audit["gap2_twin_adjacent_pair_template_count"]
        and class_template_count["gap4_cousin_adjacent_pair_collision"]
        == previous_audit["gap4_cousin_adjacent_pair_template_count"]
        and total_edge_mass == previous_gap2_gap4_edge_mass
        and sum(class_template_count.values()) == total_template_count
        and sum(class_edge_mass.values()) == total_edge_mass
        and sum(superclass_edge_mass.values()) == total_edge_mass
        and dominant_aligned_edge_mass + offdominant_edge_mass == total_edge_mass
        and all(row["edge_mass"] == row["cycle_length"] * row["occurrence_count"] for row in selected)
    )

    top_rows = sorted(
        selected,
        key=lambda row: (-row["edge_mass"], row["adjacent_pair_gap_class"], row["route_superclass"]),
    )[:24]

    return {
        "max_prime": max_prime,
        "previous_adjacent_pair_gap_class_ledger_closed": previous[
            "single_P_local_adjacent_prime_pair_gap_class_ledger_closed"
        ],
        "single_P_local_gap2_gap4_route_superclass_ledger_closed": ledger_closed,
        "gap2_gap4_template_count": total_template_count,
        "gap2_gap4_edge_mass": total_edge_mass,
        "gap2_twin_template_count": class_template_count[
            "gap2_twin_adjacent_pair_collision"
        ],
        "gap2_twin_edge_mass": class_edge_mass[
            "gap2_twin_adjacent_pair_collision"
        ],
        "gap4_cousin_template_count": class_template_count[
            "gap4_cousin_adjacent_pair_collision"
        ],
        "gap4_cousin_edge_mass": class_edge_mass[
            "gap4_cousin_adjacent_pair_collision"
        ],
        "gap2_wing_template_count": superclass_template_count[
            ("gap2_twin_adjacent_pair_collision", "wing_single_P_local")
        ],
        "gap2_wing_edge_mass": gap2_wing_mass,
        "gap2_right_tail_template_count": superclass_template_count[
            ("gap2_twin_adjacent_pair_collision", "right_tail_single_P_local")
        ],
        "gap2_right_tail_edge_mass": gap2_tail_mass,
        "gap4_right_tail_template_count": superclass_template_count[
            ("gap4_cousin_adjacent_pair_collision", "right_tail_single_P_local")
        ],
        "gap4_right_tail_edge_mass": gap4_tail_mass,
        "gap4_wing_template_count": superclass_template_count[
            ("gap4_cousin_adjacent_pair_collision", "wing_single_P_local")
        ],
        "gap4_wing_edge_mass": gap4_wing_mass,
        "dominant_aligned_edge_mass": dominant_aligned_edge_mass,
        "dominant_aligned_edge_ratio": dominant_aligned_edge_mass / total_edge_mass,
        "offdominant_residual_edge_mass": offdominant_edge_mass,
        "offdominant_residual_edge_ratio": offdominant_edge_mass / total_edge_mass,
        "gap2_wing_edge_ratio_within_gap2": gap2_wing_mass
        / class_edge_mass["gap2_twin_adjacent_pair_collision"],
        "gap4_right_tail_edge_ratio_within_gap4": gap4_tail_mass
        / class_edge_mass["gap4_cousin_adjacent_pair_collision"],
        "dominant_aligned_mixed_positive_negative_edge_mass": a_edge_mass[
            ("gap2_twin_adjacent_pair_collision", "wing_single_P_local", "mixed_positive_negative")
        ]
        + a_edge_mass[
            (
                "gap4_cousin_adjacent_pair_collision",
                "right_tail_single_P_local",
                "mixed_positive_negative",
            )
        ],
        "all_positive_edge_mass": sum(
            mass
            for (gap, superclass, a_class), mass in a_edge_mass.items()
            if a_class == "all_positive"
        ),
        "duplicate_raw_base_count": duplicate_raw_base_count,
        "duplicate_raw_base_edge_mass": duplicate_raw_base_edge_mass,
        "route_superclass_template_rows": [
            {
                "adjacent_pair_gap_class": gap,
                "route_superclass": superclass,
                "template_count": superclass_template_count[(gap, superclass)],
                "template_ratio": superclass_template_count[(gap, superclass)]
                / total_template_count,
            }
            for gap, superclass in sorted(
                superclass_template_count,
                key=lambda key: (-superclass_template_count[key], key[0], key[1]),
            )
        ],
        "route_superclass_edge_rows": pair_rows(
            superclass_edge_mass,
            total_edge_mass,
            "adjacent_pair_gap_class",
            "route_superclass",
        ),
        "route_class_edge_rows": pair_rows(
            route_edge_mass,
            total_edge_mass,
            "adjacent_pair_gap_class",
            "route_class",
        ),
        "route_superclass_a_edge_rows": triple_rows(
            a_edge_mass, total_edge_mass, "A_class"
        ),
        "route_superclass_cycle_edge_rows": triple_rows(
            cycle_edge_mass, total_edge_mass, "cycle_length", limit=30
        ),
        "route_superclass_q_prefix_edge_rows": triple_rows(
            q_edge_mass, total_edge_mass, "q_prefix_count", limit=30
        ),
        "route_superclass_m_shell_edge_rows": triple_rows(
            shell_edge_mass, total_edge_mass, "m_shell_prime_count", limit=30
        ),
        "route_superclass_p_band_edge_rows": triple_rows(
            p_band_edge_mass, total_edge_mass, "P_band"
        ),
        "duplicate_raw_base_rows": sorted(
            duplicate_raw_base_rows,
            key=lambda row: (-row["edge_mass"], row["adjacent_pair_gap_class"], row["route_superclass"]),
        ),
        "top_gap2_gap4_template_rows": [
            {
                **row,
                "m_pair": str(row["m_pair"]),
            }
            for row in top_rows
        ],
        "gap2_wing_twin_collision_bound_proved": False,
        "gap2_right_tail_twin_residual_bound_proved": False,
        "gap4_right_tail_cousin_collision_bound_proved": False,
        "gap4_wing_cousin_residual_bound_proved": False,
        "gap2_twin_adjacent_pair_collision_bound_proved": False,
        "gap4_cousin_adjacent_pair_collision_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_route_superclass_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "single_p_local_gap2_gap4_route_superclass_ledger_closed_collision_bounds_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "gap2 and gap4 carry 612/662 adjacent-pair edge mass and split cleanly by route-superclass",
        "current_object": {
            "input": "the 64 gap2/gap4 adjacent-prime-pair repeated templates",
            "operation": "classify dominant adjacent-pair collisions by route superclass",
            "dominant_shape": "gap2 is wing-dominant while gap4 is right-tail-dominant",
            "remaining": "prove signed collision bounds for the route-superclass carriers or route them to PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "AdjacentPrimePairExactGapLedgerImported",
                finite_audit["previous_adjacent_pair_gap_class_ledger_closed"],
                finite_audit["previous_adjacent_pair_gap_class_ledger_closed"],
                "The adjacent-prime-pair exact-gap ledger is imported.",
                "none for import",
            ),
            gate(
                "Gap2Gap4RouteSuperclassLedger",
                finite_audit["single_P_local_gap2_gap4_route_superclass_ledger_closed"],
                finite_audit["single_P_local_gap2_gap4_route_superclass_ledger_closed"],
                "Gap2/gap4 adjacent-pair collisions are split by route-superclass.",
                "none for the finite route-superclass ledger",
            ),
            gate(
                "Gap2WingTwinAdjacentPairCollisionBound",
                False,
                False,
                "Control the dominant wing carrier for gap-2 adjacent pairs.",
                "finite audit shows 32 templates / 290 edge mass but no global theorem",
            ),
            gate(
                "Gap4RightTailCousinAdjacentPairCollisionBound",
                False,
                False,
                "Control the dominant right-tail carrier for gap-4 adjacent pairs.",
                "finite audit shows 28 templates / 288 edge mass but no global theorem",
            ),
            gate(
                "Gap2Gap4OffdominantResidualBound",
                False,
                False,
                "Control the residual gap2-tail and gap4-wing carriers.",
                "finite audit shows 34 residual edge mass but no global suppression theorem",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "still need a completed nonlocal trace family; they do not bound one fixed gap2-wing or gap4-tail packet",
            "prime_gap_theorems": "classify or produce prime gaps but do not control route-superclass signed template equality",
            "short_interval_prime_inputs": "do not estimate this finite local collision carrier",
        },
        "latest_narrowest_mouth": [
            "LocalCycleLengthUniformBound",
            "AND Gap2WingTwinAdjacentPairCollisionBound",
            "AND Gap2RightTailTwinResidualCollisionBound",
            "AND Gap4RightTailCousinAdjacentPairCollisionBound",
            "AND Gap4WingCousinResidualCollisionBound",
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
        "single_P_local_gap2_gap4_route_superclass_ledger_closed": finite_audit[
            "single_P_local_gap2_gap4_route_superclass_ledger_closed"
        ],
        "gap2_wing_twin_collision_bound_proved": False,
        "gap2_right_tail_twin_residual_bound_proved": False,
        "gap4_right_tail_cousin_collision_bound_proved": False,
        "gap4_wing_cousin_residual_bound_proved": False,
        "gap2_twin_adjacent_pair_collision_bound_proved": False,
        "gap4_cousin_adjacent_pair_collision_bound_proved": False,
        "adjacent_prime_pair_collision_bound_proved": False,
        "same_packet_multi_m_collision_bound_proved": False,
        "local_occurrence_multiplicity_uniform_bound_proved": False,
        "single_P_slice_endpoint_packet_summation_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 route-superclass 审计",
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
        "## 2. gap2/gap4 route-superclass 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"single_P_local_gap2_gap4_route_superclass_ledger_closed={str(audit['single_P_local_gap2_gap4_route_superclass_ledger_closed']).lower()}",
        f"gap2_gap4_template_count={audit['gap2_gap4_template_count']}",
        f"gap2_gap4_edge_mass={audit['gap2_gap4_edge_mass']}",
        f"gap2_twin_template_count={audit['gap2_twin_template_count']}",
        f"gap2_twin_edge_mass={audit['gap2_twin_edge_mass']}",
        f"gap2_wing_template_count={audit['gap2_wing_template_count']}",
        f"gap2_wing_edge_mass={audit['gap2_wing_edge_mass']}",
        f"gap2_right_tail_template_count={audit['gap2_right_tail_template_count']}",
        f"gap2_right_tail_edge_mass={audit['gap2_right_tail_edge_mass']}",
        f"gap4_cousin_template_count={audit['gap4_cousin_template_count']}",
        f"gap4_cousin_edge_mass={audit['gap4_cousin_edge_mass']}",
        f"gap4_right_tail_template_count={audit['gap4_right_tail_template_count']}",
        f"gap4_right_tail_edge_mass={audit['gap4_right_tail_edge_mass']}",
        f"gap4_wing_template_count={audit['gap4_wing_template_count']}",
        f"gap4_wing_edge_mass={audit['gap4_wing_edge_mass']}",
        f"dominant_aligned_edge_mass={audit['dominant_aligned_edge_mass']}",
        f"dominant_aligned_edge_ratio={audit['dominant_aligned_edge_ratio']}",
        f"offdominant_residual_edge_mass={audit['offdominant_residual_edge_mass']}",
        f"offdominant_residual_edge_ratio={audit['offdominant_residual_edge_ratio']}",
        f"gap2_wing_edge_ratio_within_gap2={audit['gap2_wing_edge_ratio_within_gap2']}",
        f"gap4_right_tail_edge_ratio_within_gap4={audit['gap4_right_tail_edge_ratio_within_gap4']}",
        f"dominant_aligned_mixed_positive_negative_edge_mass={audit['dominant_aligned_mixed_positive_negative_edge_mass']}",
        f"all_positive_edge_mass={audit['all_positive_edge_mass']}",
        f"duplicate_raw_base_count={audit['duplicate_raw_base_count']}",
        f"duplicate_raw_base_edge_mass={audit['duplicate_raw_base_edge_mass']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "route-superclass template count：",
        "",
        *markdown_table(
            audit["route_superclass_template_rows"],
            ["adjacent_pair_gap_class", "route_superclass", "template_count", "template_ratio"],
        ),
        "",
        "route-superclass edge mass：",
        "",
        *markdown_table(
            audit["route_superclass_edge_rows"],
            ["adjacent_pair_gap_class", "route_superclass", "edge_mass", "edge_ratio"],
        ),
        "",
        "route-class edge mass：",
        "",
        *markdown_table(
            audit["route_class_edge_rows"],
            ["adjacent_pair_gap_class", "route_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "route-superclass A-class edge mass：",
        "",
        *markdown_table(
            audit["route_superclass_a_edge_rows"],
            ["adjacent_pair_gap_class", "route_superclass", "A_class", "edge_mass", "edge_ratio"],
        ),
        "",
        "route-superclass cycle-length edge mass：",
        "",
        *markdown_table(
            audit["route_superclass_cycle_edge_rows"],
            ["adjacent_pair_gap_class", "route_superclass", "cycle_length", "edge_mass", "edge_ratio"],
        ),
        "",
        "route-superclass P-band edge mass：",
        "",
        *markdown_table(
            audit["route_superclass_p_band_edge_rows"],
            ["adjacent_pair_gap_class", "route_superclass", "P_band", "edge_mass", "edge_ratio"],
        ),
        "",
        "duplicate raw-base rows：",
        "",
        *markdown_table(
            audit["duplicate_raw_base_rows"],
            [
                "adjacent_pair_gap_class",
                "route_superclass",
                "template_count",
                "edge_mass",
                "edge_ratio",
            ],
        ),
        "",
        "最高 gap2/gap4 templates：",
        "",
        *markdown_table(
            audit["top_gap2_gap4_template_rows"],
            [
                "adjacent_pair_gap_class",
                "route_superclass",
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
        "结论：gap2/gap4 主量已被拆成 gap2-wing、gap2-right-tail、gap4-right-tail、gap4-wing",
        "四个 route-superclass carrier。该账本仍是有限结构结果，尚未给出全局 signed collision bound。",
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
        f"single_P_local_gap2_gap4_route_superclass_ledger_closed={str(payload['single_P_local_gap2_gap4_route_superclass_ledger_closed']).lower()}",
        f"gap2_wing_twin_collision_bound_proved={str(payload['gap2_wing_twin_collision_bound_proved']).lower()}",
        f"gap2_right_tail_twin_residual_bound_proved={str(payload['gap2_right_tail_twin_residual_bound_proved']).lower()}",
        f"gap4_right_tail_cousin_collision_bound_proved={str(payload['gap4_right_tail_cousin_collision_bound_proved']).lower()}",
        f"gap4_wing_cousin_residual_bound_proved={str(payload['gap4_wing_cousin_residual_bound_proved']).lower()}",
        f"gap2_twin_adjacent_pair_collision_bound_proved={str(payload['gap2_twin_adjacent_pair_collision_bound_proved']).lower()}",
        f"gap4_cousin_adjacent_pair_collision_bound_proved={str(payload['gap4_cousin_adjacent_pair_collision_bound_proved']).lower()}",
        f"adjacent_prime_pair_collision_bound_proved={str(payload['adjacent_prime_pair_collision_bound_proved']).lower()}",
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
        "single_P_local_gap2_gap4_route_superclass_ledger_closed="
        f"{payload['single_P_local_gap2_gap4_route_superclass_ledger_closed']}"
    )
    print(f"gap2_wing_edge_mass={audit['gap2_wing_edge_mass']}")
    print(f"gap4_right_tail_edge_mass={audit['gap4_right_tail_edge_mass']}")
    print(f"dominant_aligned_edge_ratio={audit['dominant_aligned_edge_ratio']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
