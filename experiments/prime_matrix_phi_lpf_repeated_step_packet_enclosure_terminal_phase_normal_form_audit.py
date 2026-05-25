#!/usr/bin/env python3
"""审计 repeated-step terminal line atoms 的局部相位正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_normal_form_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-audit.json

上一层把 packet enclosure 拆成 7 个固定 m 的 q-prefix line atoms。本层继续
下钻：对这些 atoms 的每条边计算

    q*m = k*P + D,  0 < D < P,  A(q) = -D mod q,

并核验 endpoint phase 的局部正规形

    e(h*k*P/q) = e(-h*D/q) = e(h*A(q)/q).

该层只关闭 terminal atoms 的确定性相位账本；它同时记录 selected terminal
atoms 全部是 moving Beatty numerator orbit，因而仍不能直接调用 fixed-numerator
Kloosterman/trace 定理。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"

TERMINAL_LINE_ATOM_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-line-atom-audit.json"
)
GLOBAL_PHASE_NORMAL_FORM_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.json"
)

DEPENDENCIES = [
    TERMINAL_LINE_ATOM_AUDIT,
    GLOBAL_PHASE_NORMAL_FORM_AUDIT,
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
        "role": "trace bilinear input still needs a completed family, not seven fixed local terminal orbits",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "Kloosterman estimates require an admissible inverse or completed denominator variable beyond A(q)/q samples",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "terminal q-prefix orbits are one-dimensional and do not form a Type-II rectangle",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "closest unbalanced interface after promoting terminal moving numerators to a family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short interval prime existence does not estimate the terminal reciprocal phases",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "bounded prime gaps do not control the signed terminal phase orbit",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def load_json(path: Path) -> dict[str, Any]:
    """读入 JSON 证书。"""
    return json.loads(path.read_text())


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def normal_edge(P: int, q: int, m: int) -> dict[str, int]:
    """计算 q*m=kP+D 和 A(q)=-D mod q。"""
    product = q * m
    k = product // P
    D = product - k * P
    A = (-D) % q
    return {"q": q, "m": m, "k": k, "D": D, "A": A}


def step_values(values: list[int]) -> list[int]:
    """计算相邻差分。"""
    return [right - left for left, right in zip(values, values[1:])]


def wrap_count(values: list[int]) -> int:
    """统计序列向下跳跃次数。"""
    return sum(1 for left, right in zip(values, values[1:]) if right < left)


def atom_phase_profile(atom: dict[str, Any]) -> dict[str, Any]:
    """构造单个 terminal/extra atom 的相位正规形 profile。"""
    edges = [normal_edge(atom["P"], q, atom["m"]) for q in atom["q_values"]]
    k_values = [edge["k"] for edge in edges]
    d_values = [edge["D"] for edge in edges]
    a_values = [edge["A"] for edge in edges]
    k_steps = step_values(k_values)
    a_steps = step_values(a_values)
    d_steps = step_values(d_values)
    moving_numerator = len(set(a_values)) > 1
    full_distinct_numerator = len(set(a_values)) == len(a_values)
    strict_k = all(step > 0 for step in k_steps) if k_steps else True
    return {
        "packet_side": atom["packet_side"],
        "packet_index": atom["packet_index"],
        "P": atom["P"],
        "m": atom["m"],
        "role": atom["role"],
        "m_rank": atom["m_rank"],
        "m_rank_terminal": atom["m_rank_terminal"],
        "q_start": atom["q_start"],
        "q_end": atom["q_end"],
        "q_prefix_count": atom["q_prefix_count"],
        "edge_count": atom["edge_count"],
        "k_min": min(k_values),
        "k_max": max(k_values),
        "k_distinct_count": len(set(k_values)),
        "k_span": max(k_values) - min(k_values) + 1,
        "k_strictly_increasing": strict_k,
        "k_step_min": min(k_steps) if k_steps else 0,
        "k_step_max": max(k_steps) if k_steps else 0,
        "D_min": min(d_values),
        "D_max": max(d_values),
        "D_wrap_count": wrap_count(d_values),
        "D_step_min": min(d_steps) if d_steps else 0,
        "D_step_max": max(d_steps) if d_steps else 0,
        "A_min": min(a_values),
        "A_max": max(a_values),
        "A_distinct_count": len(set(a_values)),
        "A_full_distinct": full_distinct_numerator,
        "A_wrap_count": wrap_count(a_values),
        "A_step_min": min(a_steps) if a_steps else 0,
        "A_step_max": max(a_steps) if a_steps else 0,
        "numerator_motion_class": (
            "full_distinct_moving_beatty_numerator"
            if full_distinct_numerator
            else "moving_beatty_numerator_with_collision"
            if moving_numerator
            else "constant_normalized_numerator"
        ),
        "fixed_numerator_kloosterman_ready": not moving_numerator,
        "phase_edges": edges,
        "phase_edge_sample": edges[:5],
        "phase_normal_form": "e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q)",
    }


def counter_rows(
    counts: Counter[Any],
    edges: Counter[Any],
    key_name: str,
    count_name: str = "atom_count",
) -> list[dict[str, Any]]:
    """把计数器转成稳定表格。"""
    return [
        {key_name: str(key), count_name: counts[key], "edge_weight_sum": edges[key]}
        for key in sorted(counts, key=str)
    ]


def audit() -> dict[str, Any]:
    """生成 terminal phase normal-form 审计。"""
    terminal_payload = load_json(TERMINAL_LINE_ATOM_AUDIT)
    global_phase_payload = load_json(GLOBAL_PHASE_NORMAL_FORM_AUDIT)
    terminal_audit = terminal_payload["finite_audit"]
    line_atoms = terminal_audit["line_atoms"]
    phase_profiles = [atom_phase_profile(atom) for atom in line_atoms]

    totals: Counter[str] = Counter()
    role_counts: Counter[str] = Counter()
    role_edges: Counter[str] = Counter()
    numerator_counts: Counter[str] = Counter()
    numerator_edges: Counter[str] = Counter()
    packet_counts: Counter[str] = Counter()
    packet_edges: Counter[str] = Counter()
    bad_edges: list[dict[str, Any]] = []

    for profile in phase_profiles:
        role_counts[profile["role"]] += 1
        role_edges[profile["role"]] += profile["edge_count"]
        numerator_counts[profile["numerator_motion_class"]] += 1
        numerator_edges[profile["numerator_motion_class"]] += profile["edge_count"]
        packet_key = f"{profile['packet_side']}:packet{profile['packet_index']}"
        packet_counts[packet_key] += 1
        packet_edges[packet_key] += profile["edge_count"]
        totals["phase_edge_count_total"] += profile["edge_count"]
        totals["fixed_numerator_atom_count"] += int(profile["fixed_numerator_kloosterman_ready"])
        totals["moving_numerator_atom_count"] += int(
            not profile["fixed_numerator_kloosterman_ready"]
        )
        totals["full_distinct_moving_numerator_atom_count"] += int(
            profile["numerator_motion_class"] == "full_distinct_moving_beatty_numerator"
        )
        if profile["role"] == "selected_terminal":
            totals["selected_terminal_phase_edge_count"] += profile["edge_count"]
            totals["selected_terminal_fixed_numerator_atom_count"] += int(
                profile["fixed_numerator_kloosterman_ready"]
            )
            totals["selected_terminal_moving_numerator_atom_count"] += int(
                not profile["fixed_numerator_kloosterman_ready"]
            )
            totals["selected_terminal_full_distinct_numerator_atom_count"] += int(
                profile["numerator_motion_class"] == "full_distinct_moving_beatty_numerator"
            )
        else:
            totals["extra_phase_edge_count"] += profile["edge_count"]

        for edge in profile["phase_edges"]:
            product = edge["q"] * edge["m"]
            division_bad = product != edge["k"] * profile["P"] + edge["D"]
            congruence_bad = (edge["D"] + edge["k"] * profile["P"]) % edge["q"] != 0
            range_bad = not (1 <= edge["D"] < profile["P"])
            zero_bad = edge["A"] == 0
            totals["product_division_mismatch_count"] += int(division_bad)
            totals["phase_congruence_mismatch_count"] += int(congruence_bad)
            totals["D_out_of_range_count"] += int(range_bad)
            totals["A_zero_count"] += int(zero_bad)
            if (division_bad or congruence_bad or range_bad or zero_bad) and len(bad_edges) < 8:
                bad_edges.append(
                    {
                        "P": profile["P"],
                        "q": edge["q"],
                        "m": edge["m"],
                        "k": edge["k"],
                        "D": edge["D"],
                        "A": edge["A"],
                    }
                )

    selected_profiles = [p for p in phase_profiles if p["role"] == "selected_terminal"]
    extra_profiles = [p for p in phase_profiles if p["role"] == "extra_shell"]
    identity_verified = (
        terminal_payload["terminal_line_atom_ledger_closed"]
        and global_phase_payload["phase_normal_form_closed"]
        and len(phase_profiles) == terminal_audit["unique_line_atom_count_total"]
        and totals["phase_edge_count_total"] == terminal_audit["unique_line_atom_edge_mass_total"]
        and totals["selected_terminal_phase_edge_count"]
        == terminal_audit["selected_terminal_line_atom_edge_mass"]
        and totals["extra_phase_edge_count"] == terminal_audit["extra_line_atom_edge_mass"]
        and totals["product_division_mismatch_count"] == 0
        and totals["phase_congruence_mismatch_count"] == 0
        and totals["D_out_of_range_count"] == 0
        and totals["A_zero_count"] == 0
        and all(profile["k_strictly_increasing"] for profile in phase_profiles)
    )

    selected_all_moving = all(
        not profile["fixed_numerator_kloosterman_ready"] for profile in selected_profiles
    )
    selected_all_full_distinct = all(profile["A_full_distinct"] for profile in selected_profiles)

    return {
        "max_prime": terminal_audit["max_prime"],
        "previous_terminal_line_atom_ledger_closed": terminal_payload[
            "terminal_line_atom_ledger_closed"
        ],
        "previous_global_phase_normal_form_closed": global_phase_payload[
            "phase_normal_form_closed"
        ],
        "terminal_phase_normal_form_atom_count_total": len(phase_profiles),
        "terminal_phase_normal_form_edge_count_total": totals["phase_edge_count_total"],
        "selected_terminal_phase_atom_count": len(selected_profiles),
        "selected_terminal_phase_edge_count": totals["selected_terminal_phase_edge_count"],
        "extra_phase_atom_count": len(extra_profiles),
        "extra_phase_edge_count": totals["extra_phase_edge_count"],
        "product_division_mismatch_count": totals["product_division_mismatch_count"],
        "phase_congruence_mismatch_count": totals["phase_congruence_mismatch_count"],
        "D_out_of_range_count": totals["D_out_of_range_count"],
        "A_zero_count": totals["A_zero_count"],
        "bad_edge_samples": bad_edges,
        "all_phase_k_strictly_increasing": all(
            profile["k_strictly_increasing"] for profile in phase_profiles
        ),
        "selected_terminal_all_moving_numerator": selected_all_moving,
        "selected_terminal_all_full_distinct_numerator": selected_all_full_distinct,
        "selected_terminal_fixed_numerator_atom_count": totals[
            "selected_terminal_fixed_numerator_atom_count"
        ],
        "selected_terminal_moving_numerator_atom_count": totals[
            "selected_terminal_moving_numerator_atom_count"
        ],
        "selected_terminal_full_distinct_numerator_atom_count": totals[
            "selected_terminal_full_distinct_numerator_atom_count"
        ],
        "fixed_numerator_atom_count_total": totals["fixed_numerator_atom_count"],
        "moving_numerator_atom_count_total": totals["moving_numerator_atom_count"],
        "full_distinct_moving_numerator_atom_count_total": totals[
            "full_distinct_moving_numerator_atom_count"
        ],
        "atom_count_by_role_rows": counter_rows(role_counts, role_edges, "role"),
        "atom_count_by_packet_rows": counter_rows(packet_counts, packet_edges, "packet"),
        "atom_count_by_numerator_motion_rows": counter_rows(
            numerator_counts,
            numerator_edges,
            "numerator_motion_class",
        ),
        "phase_profiles": phase_profiles,
        "terminal_phase_normal_form_closed": identity_verified,
        "selected_terminal_fixed_numerator_kloosterman_ready": False,
        "selected_terminal_moving_beatty_numerator_phase_saving_proved": False,
        "extra_phase_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_packet_enclosure_terminal_phase_normal_form_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "terminal_phase_normal_form_closed_moving_numerator_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after terminal line-atom support is isolated, the next acyclic step is to compute the exact local reciprocal phase orbit",
        "current_object": {
            "input": "seven terminal/extra fixed-m line atoms from packet2842 and packet1887",
            "identity": "q*m=k*P+D and e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q)",
            "dominant_shape": "all four selected terminal atoms have moving, full-distinct Beatty numerators A(q)",
            "remaining": "phase saving for selected terminal moving-numerator prime-q reciprocal orbits plus absorption of three extra atoms",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "TerminalLineAtomLedgerImported",
                finite_audit["previous_terminal_line_atom_ledger_closed"],
                finite_audit["previous_terminal_line_atom_ledger_closed"],
                "The seven terminal/extra fixed-m line atoms are imported.",
                "none for support import",
            ),
            gate(
                "GlobalPhaseNormalFormImported",
                finite_audit["previous_global_phase_normal_form_closed"],
                finite_audit["previous_global_phase_normal_form_closed"],
                "The global fixed-m q-prefix phase normal form is imported.",
                "none for formula import",
            ),
            gate(
                "TerminalPhaseNormalForm",
                finite_audit["terminal_phase_normal_form_closed"],
                finite_audit["terminal_phase_normal_form_closed"],
                "All 133 local edges satisfy q*m=kP+D and e(hkP/q)=e(-hD/q).",
                "none for deterministic terminal phase normal form",
            ),
            gate(
                "SelectedTerminalMovingNumeratorDiagnosis",
                finite_audit["selected_terminal_all_moving_numerator"],
                finite_audit["selected_terminal_all_moving_numerator"],
                "Every selected terminal atom has moving normalized numerator A(q).",
                "none for finite diagnosis",
            ),
            gate(
                "SelectedTerminalFixedNumeratorKloostermanReady",
                False,
                False,
                "A direct fixed-numerator Kloosterman input is available for the selected terminal atoms.",
                "false: selected terminal atoms have no fixed numerator",
            ),
            gate(
                "SelectedTerminalMovingBeattyNumeratorPhaseSaving",
                False,
                False,
                "Prove cancellation for the selected terminal moving-numerator reciprocal orbits.",
                "requires a new moving-numerator completion or PDEC/SAE cap",
            ),
            gate(
                "ExtraPhaseAbsorption",
                False,
                False,
                "Absorb the three extra phase atoms without losing the selected terminal gain.",
                "requires a summable family or explicit absorption certificate",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "the local normal form exposes reciprocal phases but still not a completed bilinear trace family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "the selected terminal atoms have moving A(q), so no fixed-numerator Kloosterman input is ready",
            "Pascadi_composite_Type_II": "seven q-prefix orbits are not a two-dimensional Type-II box",
            "Wright_unbalanced_Kloosterman": "unbalanced fraction technology is closest only after these local orbits are promoted to a family",
            "Li_short_interval_x_052": "short interval prime existence does not estimate e(h*A(q)/q)",
            "Maynard_small_gaps": "bounded gaps do not control the signed moving-numerator phase",
        },
        "latest_narrowest_mouth": [
            "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving(packet2842:m=757,761; packet1887:m=769,773)",
            "AND ExtraPhaseAtomAbsorption(m=719,751,479)",
            "AND RepeatedStepPacketEnclosureTerminalLineAtomUniformBoundOutsidePhaseNormalForm",
            "AND RepeatedStepAffineSkeletonPacketEnclosureUniformBoundOutsideTerminalLineAtoms",
            "AND RepeatedStepSharedWitnessPairAffineSkeletonUniformBoundOutsidePacketEnclosure",
            "AND RepeatedStepSameAtomOccurrenceSpliceUniformBoundOutsideSharedWitnessPairSkeleton",
            "AND RepeatedStepRepeatedNodePSwitchCutUniformBoundOutsideOccurrenceSplice",
            "AND RepeatedStepMixedPSourceSinkPathCoverUniformBoundOutsideSwitchCuts",
            "AND RepeatedStepDirectedIncidenceGraphUniformBoundOutsidePathCover",
            "AND RepeatedStepUniformFamilyBoundOutsideDirectedIncidenceGraph",
            "AND DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar outside repeated atoms)",
            "AND OtherLargestAtomTemplateWitnessFamilyBounds",
            "AND OtherCoreRouteCycleSwitchAtomBounds",
            "AND TopTwoNonCoreSignCycleResidualBound",
            "AND Gap2LowerWingTwinCollisionBound",
            "AND Gap2RightTailTwoSidedTwinResidualCollisionBound",
            "AND Gap4RightTailLeftCollarCousinResidualCollisionBound",
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
        "terminal_phase_normal_form_closed": finite_audit["terminal_phase_normal_form_closed"],
        "selected_terminal_fixed_numerator_kloosterman_ready": False,
        "selected_terminal_moving_beatty_numerator_phase_saving_proved": False,
        "extra_phase_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
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
    audit_result = payload["finite_audit"]
    current = payload["current_object"]
    profile_rows = [
        {
            "side": profile["packet_side"],
            "packet": profile["packet_index"],
            "role": profile["role"],
            "m": profile["m"],
            "q_count": profile["q_prefix_count"],
            "k_range": f"[{profile['k_min']},{profile['k_max']}]",
            "D_range": f"[{profile['D_min']},{profile['D_max']}]",
            "A_range": f"[{profile['A_min']},{profile['A_max']}]",
            "A_distinct": profile["A_distinct_count"],
            "A_wrap": profile["A_wrap_count"],
            "numerator": profile["numerator_motion_class"],
        }
        for profile in audit_result["phase_profiles"]
    ]
    lines = [
        "# Prime Matrix Phi-LPF repeated-step packet-enclosure terminal phase normal-form 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"identity={current['identity']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. terminal phase normal-form 有限审计",
        "",
        "```text",
        f"previous_terminal_line_atom_ledger_closed={str(audit_result['previous_terminal_line_atom_ledger_closed']).lower()}",
        f"previous_global_phase_normal_form_closed={str(audit_result['previous_global_phase_normal_form_closed']).lower()}",
        f"terminal_phase_normal_form_atom_count_total={audit_result['terminal_phase_normal_form_atom_count_total']}",
        f"terminal_phase_normal_form_edge_count_total={audit_result['terminal_phase_normal_form_edge_count_total']}",
        f"selected_terminal_phase_atom_count={audit_result['selected_terminal_phase_atom_count']}",
        f"selected_terminal_phase_edge_count={audit_result['selected_terminal_phase_edge_count']}",
        f"extra_phase_atom_count={audit_result['extra_phase_atom_count']}",
        f"extra_phase_edge_count={audit_result['extra_phase_edge_count']}",
        f"product_division_mismatch_count={audit_result['product_division_mismatch_count']}",
        f"phase_congruence_mismatch_count={audit_result['phase_congruence_mismatch_count']}",
        f"D_out_of_range_count={audit_result['D_out_of_range_count']}",
        f"A_zero_count={audit_result['A_zero_count']}",
        f"all_phase_k_strictly_increasing={str(audit_result['all_phase_k_strictly_increasing']).lower()}",
        f"selected_terminal_all_moving_numerator={str(audit_result['selected_terminal_all_moving_numerator']).lower()}",
        f"selected_terminal_all_full_distinct_numerator={str(audit_result['selected_terminal_all_full_distinct_numerator']).lower()}",
        f"selected_terminal_fixed_numerator_atom_count={audit_result['selected_terminal_fixed_numerator_atom_count']}",
        f"selected_terminal_moving_numerator_atom_count={audit_result['selected_terminal_moving_numerator_atom_count']}",
        f"terminal_phase_normal_form_closed={str(audit_result['terminal_phase_normal_form_closed']).lower()}",
        f"selected_terminal_moving_beatty_numerator_phase_saving_proved={str(audit_result['selected_terminal_moving_beatty_numerator_phase_saving_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "phase profile rows：",
        "",
        *markdown_table(
            profile_rows,
            [
                "side",
                "packet",
                "role",
                "m",
                "q_count",
                "k_range",
                "D_range",
                "A_range",
                "A_distinct",
                "A_wrap",
                "numerator",
            ],
        ),
        "",
        "role 分桶：",
        "",
        *markdown_table(audit_result["atom_count_by_role_rows"], ["role", "atom_count", "edge_weight_sum"]),
        "",
        "packet 分桶：",
        "",
        *markdown_table(audit_result["atom_count_by_packet_rows"], ["packet", "atom_count", "edge_weight_sum"]),
        "",
        "numerator motion 分桶：",
        "",
        *markdown_table(
            audit_result["atom_count_by_numerator_motion_rows"],
            ["numerator_motion_class", "atom_count", "edge_weight_sum"],
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
        "结论：terminal/extra line atoms 的局部 endpoint phase 已全部正规化为 `A(q)/q`。",
        "四个 selected terminal atoms 都是 moving 且 full-distinct 的 Beatty numerator orbit；",
        "因此本层排除了直接 fixed-numerator Kloosterman 输入，但没有证明 moving-numerator phase saving。",
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
        f"terminal_phase_normal_form_closed={str(payload['terminal_phase_normal_form_closed']).lower()}",
        f"selected_terminal_fixed_numerator_kloosterman_ready={str(payload['selected_terminal_fixed_numerator_kloosterman_ready']).lower()}",
        f"selected_terminal_moving_beatty_numerator_phase_saving_proved={str(payload['selected_terminal_moving_beatty_numerator_phase_saving_proved']).lower()}",
        f"extra_phase_absorption_proved={str(payload['extra_phase_absorption_proved']).lower()}",
        f"summable_family_created={str(payload['summable_family_created']).lower()}",
        f"trace_or_kloosterman_completion_ready={str(payload['trace_or_kloosterman_completion_ready']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
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
    OUT_MD.write_text(build_markdown(payload).rstrip() + "\n")
    audit_result = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"terminal_phase_normal_form_closed={payload['terminal_phase_normal_form_closed']}")
    print(
        "selected_terminal_moving_numerator_atom_count="
        f"{audit_result['selected_terminal_moving_numerator_atom_count']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
