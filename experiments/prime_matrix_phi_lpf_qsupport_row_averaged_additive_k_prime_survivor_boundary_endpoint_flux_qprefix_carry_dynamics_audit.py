#!/usr/bin/env python3
"""审计 fixed-m q-prefix phase atoms 的 successor carry 动力学。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_dynamics_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-audit.json

上一层把 fixed-m q-prefix atom 的相位正规化为

    q*m = k*P + D,       e(h*k*P/q)=e(h*A(q)/q), A(q)=-D mod q.

本层继续下钻相邻 prime-q successor。若 q' 是同一 atom 中 q 的下一个素数，
g=q'-q，则

    D' = D + m*g - P*c,       c = k' - k = floor((D+m*g)/P).

这把 moving numerator A(q) 的来源压成 prime-gap-driven carry word。该层仍
不提供相位节省；它说明主质量不是固定步长旋转，而是由素数间隙和多重 carry
共同驱动的移动分子锯齿轨道。
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit as qprefix_atom  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_phase_normal_form_audit as phase_normal  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-dynamics"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json",
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
        "role": "carry dynamics must still be completed to a trace family before trace bilinear estimates apply",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "prime-gap carry words do not by themselves create an inverse-fraction Kloosterman variable",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "successor carry words are one-dimensional along q and not direct composite Type-II boxes",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman input remains a candidate only after the carry word is completed into an admissible family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not estimate prime-gap-driven reciprocal carry phases",
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


def sign_label(value: int) -> str:
    """返回整数符号标签。"""
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


def counter_rows(
    counts: Counter[Any],
    key_name: str,
    count_name: str = "count",
) -> list[dict[str, Any]]:
    """把计数器转成稳定表格。"""
    return [{key_name: str(key), count_name: counts[key]} for key in sorted(counts, key=str)]


def numeric_counter_rows(counts: Counter[int], key_name: str) -> list[dict[str, Any]]:
    """把整数键计数器转成数值排序表格。"""
    return [{key_name: key, "count": counts[key]} for key in sorted(counts)]


def edge_sequence(P: int, m_value: int, q_values: list[int]) -> list[dict[str, int]]:
    """构造同一 atom 上的正规形边序列。"""
    return [phase_normal.normal_edge(P, q, m_value) for q in q_values]


def atom_transition_profile(
    packet_index: int,
    packet: dict[str, Any],
    endpoint_class: str,
    m_value: int,
    q_values: list[int],
) -> tuple[dict[str, Any], list[dict[str, int]]]:
    """构造一个 atom 的 successor carry profile 与转移表。"""
    edges = edge_sequence(packet["P"], m_value, q_values)
    transitions: list[dict[str, int]] = []
    q_gaps: list[int] = []
    carries: list[int] = []
    a_steps: list[int] = []
    d_steps: list[int] = []

    for left, right in zip(edges, edges[1:]):
        q_gap = right["q"] - left["q"]
        carry = right["k"] - left["k"]
        predicted_D = left["D"] + m_value * q_gap - packet["P"] * carry
        predicted_carry = (left["D"] + m_value * q_gap) // packet["P"]
        item = {
            "q": left["q"],
            "q_next": right["q"],
            "q_gap": q_gap,
            "k": left["k"],
            "k_next": right["k"],
            "carry_delta_k": carry,
            "predicted_carry": predicted_carry,
            "D": left["D"],
            "D_next": right["D"],
            "predicted_D_next": predicted_D,
            "D_step": right["D"] - left["D"],
            "A": left["A"],
            "A_next": right["A"],
            "A_step": right["A"] - left["A"],
        }
        transitions.append(item)
        q_gaps.append(q_gap)
        carries.append(carry)
        d_steps.append(item["D_step"])
        a_steps.append(item["A_step"])

    if not transitions:
        carry_word_class = "singleton_q_no_transition"
        prime_gap_word_class = "singleton_q_no_transition"
        a_motion_class = "singleton_q_no_transition"
    else:
        carry_word_class = (
            "constant_carry_word" if len(set(carries)) == 1 else "variable_carry_word"
        )
        prime_gap_word_class = (
            "constant_prime_gap_word" if len(set(q_gaps)) == 1 else "variable_prime_gap_word"
        )
        if all(step > 0 for step in a_steps):
            a_motion_class = "A_strict_increasing"
        elif all(step < 0 for step in a_steps):
            a_motion_class = "A_strict_decreasing"
        elif all(step == 0 for step in a_steps):
            a_motion_class = "A_constant"
        else:
            a_motion_class = "A_mixed_sawtooth"

    profile = {
        "packet_index": packet_index,
        "P": packet["P"],
        "strip": packet["strip"],
        "endpoint_flux_class": endpoint_class,
        "m": m_value,
        "q_prefix_count": len(q_values),
        "transition_count": len(transitions),
        "q_start": q_values[0],
        "q_end": q_values[-1],
        "carry_word_class": carry_word_class,
        "prime_gap_word_class": prime_gap_word_class,
        "A_motion_class": a_motion_class,
        "q_gap_sample": q_gaps[:6],
        "carry_sample": carries[:6],
        "A_step_sample": a_steps[:6],
        "D_step_sample": d_steps[:6],
        "edge_sample": edges[:5],
    }
    return profile, transitions


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 q-prefix phase atoms 的 successor carry 动力学。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    totals: Counter[str] = Counter()
    atom_count_by_carry_word: Counter[str] = Counter()
    atom_count_by_prime_gap_word: Counter[str] = Counter()
    atom_count_by_a_motion: Counter[str] = Counter()
    atom_count_by_strip: Counter[str] = Counter()
    transition_count_by_strip: Counter[str] = Counter()
    carry_delta_k_counts: Counter[int] = Counter()
    q_gap_counts: Counter[int] = Counter()
    d_step_sign_counts: Counter[str] = Counter()
    a_step_sign_counts: Counter[str] = Counter()

    q_gaps: list[int] = []
    carries: list[int] = []
    d_steps: list[int] = []
    a_steps: list[int] = []
    sample_atoms: list[dict[str, Any]] = []
    bad_transition_samples: list[dict[str, Any]] = []

    for packet_index, packet in enumerate(packets):
        profile = qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        endpoint_class = profile["endpoint_flux_class"]
        q_values = phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))

        for m_value in m_values:
            atom_profile, transitions = atom_transition_profile(
                packet_index, packet, endpoint_class, m_value, q_values
            )
            totals["atom_count_total"] += 1
            totals["multiq_atom_count"] += int(atom_profile["transition_count"] > 0)
            atom_count_by_carry_word[atom_profile["carry_word_class"]] += 1
            atom_count_by_prime_gap_word[atom_profile["prime_gap_word_class"]] += 1
            atom_count_by_a_motion[atom_profile["A_motion_class"]] += 1
            atom_count_by_strip[packet["strip"]] += 1
            transition_count_by_strip[packet["strip"]] += atom_profile["transition_count"]

            for transition in transitions:
                totals["successor_transition_count_total"] += 1
                q_gap = transition["q_gap"]
                carry = transition["carry_delta_k"]
                d_step = transition["D_step"]
                a_step = transition["A_step"]
                q_gaps.append(q_gap)
                carries.append(carry)
                d_steps.append(d_step)
                a_steps.append(a_step)
                q_gap_counts[q_gap] += 1
                carry_delta_k_counts[carry] += 1
                d_step_sign_counts[sign_label(d_step)] += 1
                a_step_sign_counts[sign_label(a_step)] += 1

                carry_mismatch = carry != transition["predicted_carry"]
                D_mismatch = transition["D_next"] != transition["predicted_D_next"]
                A_recomputed = (-transition["D_next"]) % transition["q_next"]
                A_mismatch = transition["A_next"] != A_recomputed
                totals["carry_formula_mismatch_count"] += int(carry_mismatch)
                totals["D_successor_mismatch_count"] += int(D_mismatch)
                totals["A_successor_mismatch_count"] += int(A_mismatch)
                totals["q_gap_nonpositive_count"] += int(q_gap <= 0)
                totals["carry_nonpositive_count"] += int(carry <= 0)
                totals["A_step_zero_count"] += int(a_step == 0)

                if (
                    (carry_mismatch or D_mismatch or A_mismatch or q_gap <= 0 or carry <= 0)
                    and len(bad_transition_samples) < 8
                ):
                    bad_transition_samples.append(
                        {
                            "P": packet["P"],
                            "strip": packet["strip"],
                            "m": m_value,
                            **transition,
                        }
                    )

            if len(sample_atoms) < 16 and (
                atom_profile["A_motion_class"] == "A_mixed_sawtooth"
                or atom_profile["carry_word_class"] == "variable_carry_word"
            ):
                sample_atoms.append(atom_profile)

    expected_transition_count = (
        previous_audit["phase_normal_form_edge_count_total"]
        - previous_audit["phase_normal_form_atom_count_total"]
    )
    identity_verified = (
        totals["successor_transition_count_total"] == expected_transition_count
        and totals["carry_formula_mismatch_count"] == 0
        and totals["D_successor_mismatch_count"] == 0
        and totals["A_successor_mismatch_count"] == 0
        and totals["q_gap_nonpositive_count"] == 0
        and totals["carry_nonpositive_count"] == 0
    )

    return {
        "max_prime": max_prime,
        "previous_phase_normal_form_atom_count_total": previous_audit[
            "phase_normal_form_atom_count_total"
        ],
        "previous_phase_normal_form_edge_count_total": previous_audit[
            "phase_normal_form_edge_count_total"
        ],
        "carry_dynamics_atom_count_total": totals["atom_count_total"],
        "multiq_atom_count": totals["multiq_atom_count"],
        "singleton_q_atom_count": totals["atom_count_total"] - totals["multiq_atom_count"],
        "expected_successor_transition_count_total": expected_transition_count,
        "successor_transition_count_total": totals["successor_transition_count_total"],
        "carry_formula_mismatch_count": totals["carry_formula_mismatch_count"],
        "D_successor_mismatch_count": totals["D_successor_mismatch_count"],
        "A_successor_mismatch_count": totals["A_successor_mismatch_count"],
        "q_gap_nonpositive_count": totals["q_gap_nonpositive_count"],
        "carry_nonpositive_count": totals["carry_nonpositive_count"],
        "A_step_zero_count": totals["A_step_zero_count"],
        "successor_carry_identity_verified": identity_verified,
        "q_gap_min": min(q_gaps),
        "q_gap_median": statistics.median(q_gaps),
        "q_gap_max": max(q_gaps),
        "q_gap_average": sum(q_gaps) / len(q_gaps),
        "carry_delta_k_min": min(carries),
        "carry_delta_k_median": statistics.median(carries),
        "carry_delta_k_max": max(carries),
        "carry_delta_k_average": sum(carries) / len(carries),
        "D_step_min": min(d_steps),
        "D_step_median": statistics.median(d_steps),
        "D_step_max": max(d_steps),
        "D_step_average": sum(d_steps) / len(d_steps),
        "A_step_min": min(a_steps),
        "A_step_median": statistics.median(a_steps),
        "A_step_max": max(a_steps),
        "A_step_average": sum(a_steps) / len(a_steps),
        "distinct_q_gap_count": len(q_gap_counts),
        "distinct_carry_delta_k_count": len(carry_delta_k_counts),
        "atom_count_by_carry_word_rows": counter_rows(
            atom_count_by_carry_word, "carry_word_class", "atom_count"
        ),
        "atom_count_by_prime_gap_word_rows": counter_rows(
            atom_count_by_prime_gap_word, "prime_gap_word_class", "atom_count"
        ),
        "atom_count_by_A_motion_rows": counter_rows(
            atom_count_by_a_motion, "A_motion_class", "atom_count"
        ),
        "atom_count_by_strip_rows": [
            {
                "strip": strip,
                "atom_count": atom_count_by_strip[strip],
                "transition_count": transition_count_by_strip[strip],
            }
            for strip in sorted(atom_count_by_strip)
        ],
        "q_gap_rows": numeric_counter_rows(q_gap_counts, "q_gap"),
        "carry_delta_k_rows": numeric_counter_rows(carry_delta_k_counts, "carry_delta_k"),
        "D_step_sign_rows": counter_rows(d_step_sign_counts, "D_step_sign"),
        "A_step_sign_rows": counter_rows(a_step_sign_counts, "A_step_sign"),
        "bad_transition_samples": bad_transition_samples,
        "sample_atoms": sample_atoms,
        "successor_carry_dynamics_closed": identity_verified,
        "constant_step_rotation_reduction_available": False,
        "prime_gap_driven_variable_carry_dominates": atom_count_by_carry_word[
            "variable_carry_word"
        ]
        > atom_count_by_carry_word["constant_carry_word"],
        "moving_numerator_phase_saving_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_phase_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_dynamics_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_phase_atoms_have_successor_carry_dynamics_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after phase normal form, the next acyclic step is to expose the prime-gap carry word driving the moving numerator",
        "current_object": {
            "input": "15439 fixed-m phase atoms and 162076 adjacent prime-q transitions",
            "identity": "D_next=D+m*(q_next-q)-P*(k_next-k), carry=floor((D+m*(q_next-q))/P)",
            "dominant_shape": "variable prime-gap carry words and mixed A(q) sawtooth motion",
            "remaining": "phase saving for prime-gap-driven moving numerator or completion to an external trace/Kloosterman family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "QPrefixPhaseNormalFormImported",
                True,
                True,
                "The fixed-m A(q)/q normal form is inherited.",
                "none for import",
            ),
            gate(
                "SuccessorCarryIdentity",
                finite_audit["successor_carry_identity_verified"],
                finite_audit["successor_carry_identity_verified"],
                "Every adjacent prime-q transition obeys the exact carry formula.",
                "none for deterministic successor dynamics",
            ),
            gate(
                "PrimeGapDrivenCarryWordLedger",
                finite_audit["successor_carry_identity_verified"],
                finite_audit["successor_carry_identity_verified"],
                "Each atom has an explicit q-gap word, carry word, and A-step word.",
                "none for finite carry ledger",
            ),
            gate(
                "ConstantStepRotationReduction",
                False,
                False,
                "The dominant mass is not a constant-step fixed-denominator rotation.",
                "variable q-gaps and carry words must be estimated",
            ),
            gate(
                "MovingNumeratorPrimeQPrefixPhaseSaving",
                False,
                False,
                "Prove cancellation for the prime-gap-driven A(q)/q orbit.",
                "new carry-word exponential sum or completed trace/Kloosterman input required",
            ),
            gate(
                "NoLossQPrefixPhaseAtomAggregation",
                False,
                False,
                "Aggregate carry-orbit estimates across all fixed-m atoms without losing the boundary gain.",
                "requires analytic aggregation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "successor dynamics is explicit but not a completed trace family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "carry words do not directly supply inverse Kloosterman variables",
            "Pascadi_composite_Type_II": "successor orbits remain one-dimensional and boundary-weighted",
            "Wright_unbalanced_Kloosterman": "could become relevant only after carry words are completed into an admissible unbalanced family",
            "Li_short_interval_x_052": "prime existence does not estimate carry-driven reciprocal phases",
        },
        "latest_narrowest_mouth": [
            "PrimeGapDrivenCarryWordExponentialSumSaving",
            "AND CompletionOfSuccessorCarryDynamicsToTraceOrKloostermanFamily",
            "AND NoLossAggregationAcross15439QPrefixCarryAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "successor_carry_dynamics_closed": finite_audit["successor_carry_dynamics_closed"],
        "constant_step_rotation_reduction_available": False,
        "moving_numerator_phase_saving_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_phase_atom_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF boundary endpoint-flux q-prefix carry dynamics 审计",
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
        "## 2. successor carry 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"previous_phase_normal_form_atom_count_total={audit['previous_phase_normal_form_atom_count_total']}",
        f"previous_phase_normal_form_edge_count_total={audit['previous_phase_normal_form_edge_count_total']}",
        f"carry_dynamics_atom_count_total={audit['carry_dynamics_atom_count_total']}",
        f"multiq_atom_count={audit['multiq_atom_count']}",
        f"singleton_q_atom_count={audit['singleton_q_atom_count']}",
        f"expected_successor_transition_count_total={audit['expected_successor_transition_count_total']}",
        f"successor_transition_count_total={audit['successor_transition_count_total']}",
        f"carry_formula_mismatch_count={audit['carry_formula_mismatch_count']}",
        f"D_successor_mismatch_count={audit['D_successor_mismatch_count']}",
        f"A_successor_mismatch_count={audit['A_successor_mismatch_count']}",
        f"q_gap_nonpositive_count={audit['q_gap_nonpositive_count']}",
        f"carry_nonpositive_count={audit['carry_nonpositive_count']}",
        f"A_step_zero_count={audit['A_step_zero_count']}",
        f"successor_carry_identity_verified={str(audit['successor_carry_identity_verified']).lower()}",
        f"q_gap_min/median/max={audit['q_gap_min']}/{audit['q_gap_median']}/{audit['q_gap_max']}",
        f"carry_delta_k_min/median/max={audit['carry_delta_k_min']}/{audit['carry_delta_k_median']}/{audit['carry_delta_k_max']}",
        f"D_step_min/median/max={audit['D_step_min']}/{audit['D_step_median']}/{audit['D_step_max']}",
        f"A_step_min/median/max={audit['A_step_min']}/{audit['A_step_median']}/{audit['A_step_max']}",
        f"distinct_q_gap_count={audit['distinct_q_gap_count']}",
        f"distinct_carry_delta_k_count={audit['distinct_carry_delta_k_count']}",
        f"successor_carry_dynamics_closed={str(audit['successor_carry_dynamics_closed']).lower()}",
        f"moving_numerator_phase_saving_closed={str(audit['moving_numerator_phase_saving_closed']).lower()}",
        "```",
        "",
        "atom carry word 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_carry_word_rows"], ["carry_word_class", "atom_count"]
        ),
        "",
        "atom prime-gap word 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_prime_gap_word_rows"],
            ["prime_gap_word_class", "atom_count"],
        ),
        "",
        "atom A-motion 分桶：",
        "",
        *markdown_table(audit["atom_count_by_A_motion_rows"], ["A_motion_class", "atom_count"]),
        "",
        "strip 分桶：",
        "",
        *markdown_table(audit["atom_count_by_strip_rows"], ["strip", "atom_count", "transition_count"]),
        "",
        "D-step sign 分桶：",
        "",
        *markdown_table(audit["D_step_sign_rows"], ["D_step_sign", "count"]),
        "",
        "A-step sign 分桶：",
        "",
        *markdown_table(audit["A_step_sign_rows"], ["A_step_sign", "count"]),
        "",
        "carry delta-k 分桶：",
        "",
        *markdown_table(audit["carry_delta_k_rows"], ["carry_delta_k", "count"]),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(
            payload["closed_gates"],
            ["gate", "closed", "proved", "meaning", "remaining"],
        ),
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
        "结论：moving numerator 的相邻 q 演化已经压成 prime-gap carry word。",
        "该层关闭确定性 successor 动力学；但 dominant atoms 具有 variable carry word",
        "和 mixed sawtooth A-motion，因此仍未得到相位节省或 completed trace/Kloosterman 输入。",
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
        f"successor_carry_dynamics_closed={str(payload['successor_carry_dynamics_closed']).lower()}",
        f"constant_step_rotation_reduction_available={str(payload['constant_step_rotation_reduction_available']).lower()}",
        f"moving_numerator_phase_saving_closed={str(payload['moving_numerator_phase_saving_closed']).lower()}",
        f"completion_to_external_trace_or_kloosterman_closed={str(payload['completion_to_external_trace_or_kloosterman_closed']).lower()}",
        f"no_loss_qprefix_phase_atom_aggregation_closed={str(payload['no_loss_qprefix_phase_atom_aggregation_closed']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    payload = build_payload()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload))
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"successor_carry_dynamics_closed={payload['successor_carry_dynamics_closed']}")
    print(f"moving_numerator_phase_saving_closed={payload['moving_numerator_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
