#!/usr/bin/env python3
"""审计 q-prefix successor carry word 的有限字母表与 run 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_letter_run_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-audit.json

上一层已经证明相邻 prime-q 转移满足

    D' = D + m*(q'-q) - P*c,       c = k' - k.

本层只把转移词继续原子化为有限字母

    raw letter    L=(q'-q, c),
    signed letter L^+=(q'-q, c, sign(A'-A)),

并记录每个 fixed-m atom 的连续相同字母 run。该层关闭的是有限
letter/run 账本；它仍不提供 reciprocal phase cancellation。
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Sequence, TypeVar


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit as qprefix_atom  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_dynamics_audit as carry_dynamics  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_phase_normal_form_audit as phase_normal  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-letter-run"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-audit.json",
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
        "role": "finite carry letters still need completion to trace functions before trace bilinear estimates apply",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "the letter word is not yet an inverse-fraction Kloosterman family modulo q",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "run words are one-dimensional prime-q strings, not balanced composite Type-II boxes",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman input remains candidate only after the letter word is converted to an admissible reciprocal family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short interval prime existence does not estimate finite carry-letter reciprocal phases",
    },
]

T = TypeVar("T")


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sign_label(value: int) -> str:
    """返回稳定符号标签。"""
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def runs(seq: Sequence[T]) -> list[tuple[T, int]]:
    """把序列压缩为连续相同字母的 run。"""
    if not seq:
        return []
    out: list[tuple[T, int]] = []
    current = seq[0]
    length = 1
    for item in seq[1:]:
        if item == current:
            length += 1
        else:
            out.append((current, length))
            current = item
            length = 1
    out.append((current, length))
    return out


def raw_letter_string(letter: tuple[int, int]) -> str:
    """序列化 raw carry letter。"""
    q_gap, carry = letter
    return f"g={q_gap},c={carry}"


def signed_letter_string(letter: tuple[int, int, str]) -> str:
    """序列化 signed carry letter。"""
    q_gap, carry, sign = letter
    return f"g={q_gap},c={carry},A={sign}"


def numeric_rows(counts: Counter[int], key_name: str, count_name: str = "count") -> list[dict[str, Any]]:
    """把整数计数器转成数值排序表格。"""
    return [{key_name: key, count_name: counts[key]} for key in sorted(counts)]


def top_raw_rows(counts: Counter[tuple[int, int]], limit: int = 20) -> list[dict[str, Any]]:
    """输出最高频 raw letters。"""
    return [
        {"raw_letter": raw_letter_string(letter), "count": count}
        for letter, count in counts.most_common(limit)
    ]


def top_signed_rows(
    counts: Counter[tuple[int, int, str]], limit: int = 20
) -> list[dict[str, Any]]:
    """输出最高频 signed letters。"""
    return [
        {"signed_letter": signed_letter_string(letter), "count": count}
        for letter, count in counts.most_common(limit)
    ]


def counter_rows(counts: Counter[str], key_name: str) -> list[dict[str, Any]]:
    """把字符串计数器转成稳定表格。"""
    return [{key_name: key, "count": counts[key]} for key in sorted(counts)]


def sum_run_lengths(rows: Iterable[tuple[int, int]]) -> int:
    """恢复 run 覆盖的 transition 总数。"""
    return sum(length * count for length, count in rows)


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计有限 carry letter alphabet 与 run 分解。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-audit.json"
        ).read_text()
    )
    previous = previous_payload["finite_audit"]

    raw_letter_counts: Counter[tuple[int, int]] = Counter()
    signed_letter_counts: Counter[tuple[int, int, str]] = Counter()
    q_gap_counts: Counter[int] = Counter()
    carry_counts: Counter[int] = Counter()
    a_sign_counts: Counter[str] = Counter()
    raw_run_length_counts: Counter[int] = Counter()
    signed_run_length_counts: Counter[int] = Counter()
    raw_letter_count_by_atom: Counter[int] = Counter()
    signed_letter_count_by_atom: Counter[int] = Counter()
    raw_run_count_by_atom: Counter[int] = Counter()
    signed_run_count_by_atom: Counter[int] = Counter()
    strip_atom_counts: Counter[str] = Counter()
    strip_transition_counts: Counter[str] = Counter()

    raw_run_lengths: list[int] = []
    signed_run_lengths: list[int] = []
    raw_run_counts: list[int] = []
    signed_run_counts: list[int] = []
    raw_letter_counts_per_atom: list[int] = []
    signed_letter_counts_per_atom: list[int] = []

    totals: Counter[str] = Counter()
    sample_high_complexity_atoms: list[dict[str, Any]] = []
    max_raw_run_sample: dict[str, Any] | None = None
    max_signed_run_sample: dict[str, Any] | None = None

    for packet_index, packet in enumerate(packets):
        endpoint_profile = qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        endpoint_class = endpoint_profile["endpoint_flux_class"]
        q_values = phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))

        for m_value in m_values:
            atom_profile, transitions = carry_dynamics.atom_transition_profile(
                packet_index, packet, endpoint_class, m_value, q_values
            )
            totals["atom_count_total"] += 1
            strip_atom_counts[packet["strip"]] += 1

            if not transitions:
                totals["singleton_q_atom_count"] += 1
                continue

            raw_seq: list[tuple[int, int]] = []
            signed_seq: list[tuple[int, int, str]] = []
            for transition in transitions:
                q_gap = transition["q_gap"]
                carry = transition["carry_delta_k"]
                a_sign = sign_label(transition["A_step"])
                raw_letter = (q_gap, carry)
                signed_letter = (q_gap, carry, a_sign)
                raw_seq.append(raw_letter)
                signed_seq.append(signed_letter)
                raw_letter_counts[raw_letter] += 1
                signed_letter_counts[signed_letter] += 1
                q_gap_counts[q_gap] += 1
                carry_counts[carry] += 1
                a_sign_counts[a_sign] += 1

            raw_runs = runs(raw_seq)
            signed_runs = runs(signed_seq)
            raw_distinct = len(set(raw_seq))
            signed_distinct = len(set(signed_seq))
            raw_run_count = len(raw_runs)
            signed_run_count = len(signed_runs)

            totals["multiq_atom_count"] += 1
            totals["successor_transition_count_total"] += len(transitions)
            totals["raw_constant_letter_atom_count"] += int(raw_distinct == 1)
            totals["raw_variable_letter_atom_count"] += int(raw_distinct > 1)
            totals["signed_constant_letter_atom_count"] += int(signed_distinct == 1)
            totals["signed_variable_letter_atom_count"] += int(signed_distinct > 1)
            totals["raw_all_singleton_runs_atom_count"] += int(all(length == 1 for _, length in raw_runs))
            totals["signed_all_singleton_runs_atom_count"] += int(
                all(length == 1 for _, length in signed_runs)
            )
            strip_transition_counts[packet["strip"]] += len(transitions)

            raw_letter_count_by_atom[raw_distinct] += 1
            signed_letter_count_by_atom[signed_distinct] += 1
            raw_run_count_by_atom[raw_run_count] += 1
            signed_run_count_by_atom[signed_run_count] += 1
            raw_letter_counts_per_atom.append(raw_distinct)
            signed_letter_counts_per_atom.append(signed_distinct)
            raw_run_counts.append(raw_run_count)
            signed_run_counts.append(signed_run_count)

            for letter, length in raw_runs:
                raw_run_length_counts[length] += 1
                raw_run_lengths.append(length)
                if max_raw_run_sample is None or length > max_raw_run_sample["run_length"]:
                    max_raw_run_sample = {
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "m": m_value,
                        "raw_letter": raw_letter_string(letter),
                        "run_length": length,
                        "transition_count": len(transitions),
                    }

            for letter, length in signed_runs:
                signed_run_length_counts[length] += 1
                signed_run_lengths.append(length)
                if max_signed_run_sample is None or length > max_signed_run_sample["run_length"]:
                    max_signed_run_sample = {
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "m": m_value,
                        "signed_letter": signed_letter_string(letter),
                        "run_length": length,
                        "transition_count": len(transitions),
                    }

            if len(sample_high_complexity_atoms) < 16 and (
                raw_distinct >= 12 or signed_distinct >= 18 or raw_run_count >= 30
            ):
                sample_high_complexity_atoms.append(
                    {
                        "P": packet["P"],
                        "strip": packet["strip"],
                        "endpoint_flux_class": endpoint_class,
                        "m": m_value,
                        "q_start": atom_profile["q_start"],
                        "q_end": atom_profile["q_end"],
                        "transition_count": len(transitions),
                        "raw_distinct_letter_count": raw_distinct,
                        "signed_distinct_letter_count": signed_distinct,
                        "raw_run_count": raw_run_count,
                        "signed_run_count": signed_run_count,
                        "raw_letter_sample": [raw_letter_string(item) for item in raw_seq[:8]],
                        "signed_letter_sample": [signed_letter_string(item) for item in signed_seq[:8]],
                    }
                )

    adjacent_pair_count = (
        totals["successor_transition_count_total"] - totals["multiq_atom_count"]
    )
    raw_equal_adjacent_pair_count = sum(
        (length - 1) * count for length, count in raw_run_length_counts.items()
    )
    signed_equal_adjacent_pair_count = sum(
        (length - 1) * count for length, count in signed_run_length_counts.items()
    )
    raw_switch_count = adjacent_pair_count - raw_equal_adjacent_pair_count
    signed_switch_count = adjacent_pair_count - signed_equal_adjacent_pair_count

    raw_run_length_sum = sum_run_lengths(raw_run_length_counts.items())
    signed_run_length_sum = sum_run_lengths(signed_run_length_counts.items())
    expected_transition_count = previous["successor_transition_count_total"]
    letter_run_decomposition_closed = (
        totals["atom_count_total"] == previous["carry_dynamics_atom_count_total"]
        and totals["multiq_atom_count"] == previous["multiq_atom_count"]
        and totals["singleton_q_atom_count"] == previous["singleton_q_atom_count"]
        and totals["successor_transition_count_total"] == expected_transition_count
        and raw_run_length_sum == expected_transition_count
        and signed_run_length_sum == expected_transition_count
        and previous["successor_carry_identity_verified"]
    )

    distinct_q_gap_count = len(q_gap_counts)
    distinct_carry_count = len(carry_counts)
    distinct_a_sign_count = len(a_sign_counts)
    raw_capacity = distinct_q_gap_count * distinct_carry_count
    signed_capacity = raw_capacity * distinct_a_sign_count

    return {
        "max_prime": max_prime,
        "previous_successor_carry_identity_verified": previous[
            "successor_carry_identity_verified"
        ],
        "carry_letter_atom_count_total": totals["atom_count_total"],
        "multiq_atom_count": totals["multiq_atom_count"],
        "singleton_q_atom_count": totals["singleton_q_atom_count"],
        "successor_transition_count_total": totals["successor_transition_count_total"],
        "expected_successor_transition_count_total": expected_transition_count,
        "raw_letter_run_length_sum": raw_run_length_sum,
        "signed_letter_run_length_sum": signed_run_length_sum,
        "letter_run_decomposition_closed": letter_run_decomposition_closed,
        "distinct_q_gap_count": distinct_q_gap_count,
        "distinct_carry_delta_k_count": distinct_carry_count,
        "distinct_A_step_sign_count": distinct_a_sign_count,
        "raw_carry_letter_alphabet_count": len(raw_letter_counts),
        "raw_carry_letter_capacity": raw_capacity,
        "raw_carry_letter_density": len(raw_letter_counts) / raw_capacity,
        "signed_carry_letter_alphabet_count": len(signed_letter_counts),
        "signed_carry_letter_capacity": signed_capacity,
        "signed_carry_letter_density": len(signed_letter_counts) / signed_capacity,
        "raw_constant_letter_atom_count": totals["raw_constant_letter_atom_count"],
        "raw_variable_letter_atom_count": totals["raw_variable_letter_atom_count"],
        "signed_constant_letter_atom_count": totals["signed_constant_letter_atom_count"],
        "signed_variable_letter_atom_count": totals["signed_variable_letter_atom_count"],
        "raw_all_singleton_runs_atom_count": totals["raw_all_singleton_runs_atom_count"],
        "signed_all_singleton_runs_atom_count": totals["signed_all_singleton_runs_atom_count"],
        "raw_run_count_total": sum(raw_run_length_counts.values()),
        "signed_run_count_total": sum(signed_run_length_counts.values()),
        "raw_run_length_min": min(raw_run_lengths),
        "raw_run_length_median": statistics.median(raw_run_lengths),
        "raw_run_length_max": max(raw_run_lengths),
        "signed_run_length_min": min(signed_run_lengths),
        "signed_run_length_median": statistics.median(signed_run_lengths),
        "signed_run_length_max": max(signed_run_lengths),
        "raw_run_count_per_atom_median": statistics.median(raw_run_counts),
        "raw_run_count_per_atom_max": max(raw_run_counts),
        "signed_run_count_per_atom_median": statistics.median(signed_run_counts),
        "signed_run_count_per_atom_max": max(signed_run_counts),
        "raw_distinct_letter_per_atom_median": statistics.median(raw_letter_counts_per_atom),
        "raw_distinct_letter_per_atom_max": max(raw_letter_counts_per_atom),
        "signed_distinct_letter_per_atom_median": statistics.median(
            signed_letter_counts_per_atom
        ),
        "signed_distinct_letter_per_atom_max": max(signed_letter_counts_per_atom),
        "adjacent_pair_count_inside_atoms": adjacent_pair_count,
        "raw_equal_adjacent_pair_count": raw_equal_adjacent_pair_count,
        "raw_switch_count": raw_switch_count,
        "raw_switch_ratio": raw_switch_count / adjacent_pair_count,
        "signed_equal_adjacent_pair_count": signed_equal_adjacent_pair_count,
        "signed_switch_count": signed_switch_count,
        "signed_switch_ratio": signed_switch_count / adjacent_pair_count,
        "q_gap_rows": numeric_rows(q_gap_counts, "q_gap"),
        "carry_delta_k_rows": numeric_rows(carry_counts, "carry_delta_k"),
        "A_step_sign_rows": counter_rows(a_sign_counts, "A_step_sign"),
        "top_raw_carry_letter_rows": top_raw_rows(raw_letter_counts),
        "top_signed_carry_letter_rows": top_signed_rows(signed_letter_counts),
        "raw_run_length_rows": numeric_rows(raw_run_length_counts, "run_length", "run_count"),
        "signed_run_length_rows": numeric_rows(
            signed_run_length_counts, "run_length", "run_count"
        ),
        "raw_distinct_letter_count_by_atom_rows": numeric_rows(
            raw_letter_count_by_atom, "distinct_raw_letters", "atom_count"
        ),
        "signed_distinct_letter_count_by_atom_rows": numeric_rows(
            signed_letter_count_by_atom, "distinct_signed_letters", "atom_count"
        ),
        "raw_run_count_by_atom_rows": numeric_rows(raw_run_count_by_atom, "raw_run_count", "atom_count"),
        "signed_run_count_by_atom_rows": numeric_rows(
            signed_run_count_by_atom, "signed_run_count", "atom_count"
        ),
        "strip_rows": [
            {
                "strip": strip,
                "atom_count": strip_atom_counts[strip],
                "transition_count": strip_transition_counts[strip],
            }
            for strip in sorted(strip_atom_counts)
        ],
        "max_raw_run_sample": max_raw_run_sample,
        "max_signed_run_sample": max_signed_run_sample,
        "sample_high_complexity_atoms": sample_high_complexity_atoms,
        "finite_carry_letter_alphabet_closed": letter_run_decomposition_closed,
        "long_constant_letter_block_route_available": False,
        "finite_letter_exponential_sum_saving_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_letter_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_letter_run_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_carry_words_have_finite_letter_run_decomposition_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after successor carry dynamics, the next acyclic step is to expose the finite transition alphabet and run fragmentation",
        "current_object": {
            "input": "15439 fixed-m carry atoms and 162076 adjacent prime-q transitions",
            "raw_letter": "L=(q_next-q, k_next-k)",
            "signed_letter": "L_plus=(q_next-q, k_next-k, sign(A_next-A))",
            "dominant_shape": "finite alphabet with highly fragmented one-step runs",
            "remaining": "exponential-sum saving for finite carry-letter words or conversion to an external trace/Kloosterman family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SuccessorCarryDynamicsImported",
                True,
                True,
                "The previous exact carry identity is imported.",
                "none for import",
            ),
            gate(
                "FiniteCarryLetterAlphabet",
                finite_audit["finite_carry_letter_alphabet_closed"],
                finite_audit["finite_carry_letter_alphabet_closed"],
                "All transitions are encoded by raw and signed finite carry letters.",
                "none for current finite alphabet ledger",
            ),
            gate(
                "CarryRunLengthLedger",
                finite_audit["letter_run_decomposition_closed"],
                finite_audit["letter_run_decomposition_closed"],
                "The run lengths reconstruct all adjacent prime-q transitions without loss.",
                "none for current run ledger",
            ),
            gate(
                "LongConstantLetterBlockReduction",
                False,
                False,
                "The observed maximum raw/signed run length is only 3.",
                "there is no long constant-letter block to exploit as a constant rotation",
            ),
            gate(
                "FiniteCarryLetterWordExponentialSumSaving",
                False,
                False,
                "Prove cancellation for the finite-letter carry words along prime q.",
                "new exponential-sum input or trace/Kloosterman completion required",
            ),
            gate(
                "NoLossQPrefixLetterAtomAggregation",
                False,
                False,
                "Aggregate any letter-word saving across all fixed-m atoms without losing the boundary gain.",
                "requires analytic aggregation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "finite letters are not yet trace functions over a completed family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "the word does not yet expose an inverse variable with a usable modulus family",
            "Pascadi_composite_Type_II": "run decomposition remains one-dimensional and short-shell weighted",
            "Wright_unbalanced_Kloosterman": "candidate only after a completed unbalanced reciprocal family is constructed",
            "Li_short_interval_x_052": "existence of primes in intervals does not control carry-letter phase cancellation",
        },
        "latest_narrowest_mouth": [
            "FiniteCarryLetterWordExponentialSumSaving",
            "AND PrimeGapCarrySwitchingLawOrTraceKloostermanCompletion",
            "AND NoLossAggregationAcross15439QPrefixCarryLetterAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "finite_carry_letter_alphabet_closed": finite_audit[
            "finite_carry_letter_alphabet_closed"
        ],
        "long_constant_letter_block_route_available": False,
        "finite_letter_exponential_sum_saving_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "no_loss_qprefix_letter_atom_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry letter/run 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"raw_letter={current['raw_letter']}",
        f"signed_letter={current['signed_letter']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. 有限字母与 run 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"carry_letter_atom_count_total={audit['carry_letter_atom_count_total']}",
        f"multiq_atom_count={audit['multiq_atom_count']}",
        f"singleton_q_atom_count={audit['singleton_q_atom_count']}",
        f"successor_transition_count_total={audit['successor_transition_count_total']}",
        f"raw_letter_run_length_sum={audit['raw_letter_run_length_sum']}",
        f"signed_letter_run_length_sum={audit['signed_letter_run_length_sum']}",
        f"letter_run_decomposition_closed={str(audit['letter_run_decomposition_closed']).lower()}",
        f"distinct_q_gap_count={audit['distinct_q_gap_count']}",
        f"distinct_carry_delta_k_count={audit['distinct_carry_delta_k_count']}",
        f"distinct_A_step_sign_count={audit['distinct_A_step_sign_count']}",
        f"raw_carry_letter_alphabet_count/capacity={audit['raw_carry_letter_alphabet_count']}/{audit['raw_carry_letter_capacity']}",
        f"signed_carry_letter_alphabet_count/capacity={audit['signed_carry_letter_alphabet_count']}/{audit['signed_carry_letter_capacity']}",
        f"raw_constant/variable_letter_atom_count={audit['raw_constant_letter_atom_count']}/{audit['raw_variable_letter_atom_count']}",
        f"signed_constant/variable_letter_atom_count={audit['signed_constant_letter_atom_count']}/{audit['signed_variable_letter_atom_count']}",
        f"raw_run_count_total={audit['raw_run_count_total']}",
        f"signed_run_count_total={audit['signed_run_count_total']}",
        f"raw_run_length_min/median/max={audit['raw_run_length_min']}/{audit['raw_run_length_median']}/{audit['raw_run_length_max']}",
        f"signed_run_length_min/median/max={audit['signed_run_length_min']}/{audit['signed_run_length_median']}/{audit['signed_run_length_max']}",
        f"raw_switch_count/ratio={audit['raw_switch_count']}/{audit['raw_switch_ratio']}",
        f"signed_switch_count/ratio={audit['signed_switch_count']}/{audit['signed_switch_ratio']}",
        f"finite_letter_exponential_sum_saving_closed={str(audit['finite_letter_exponential_sum_saving_closed']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "最高频 raw carry letters：",
        "",
        *markdown_table(audit["top_raw_carry_letter_rows"], ["raw_letter", "count"]),
        "",
        "最高频 signed carry letters：",
        "",
        *markdown_table(audit["top_signed_carry_letter_rows"], ["signed_letter", "count"]),
        "",
        "raw run length 分布：",
        "",
        *markdown_table(audit["raw_run_length_rows"], ["run_length", "run_count"]),
        "",
        "signed run length 分布：",
        "",
        *markdown_table(audit["signed_run_length_rows"], ["run_length", "run_count"]),
        "",
        "每 atom 的 raw distinct letter 数：",
        "",
        *markdown_table(
            audit["raw_distinct_letter_count_by_atom_rows"],
            ["distinct_raw_letters", "atom_count"],
        ),
        "",
        "每 atom 的 signed distinct letter 数：",
        "",
        *markdown_table(
            audit["signed_distinct_letter_count_by_atom_rows"],
            ["distinct_signed_letters", "atom_count"],
        ),
        "",
        "strip 分桶：",
        "",
        *markdown_table(audit["strip_rows"], ["strip", "atom_count", "transition_count"]),
        "",
        "max run 样本：",
        "",
        "```text",
        f"max_raw_run_sample={audit['max_raw_run_sample']}",
        f"max_signed_run_sample={audit['max_signed_run_sample']}",
        "```",
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
        "结论：successor carry word 已经进一步压成有限 raw/signed carry letter",
        "和 run-length ledger；但是 run 的中位长度为 1、最大长度仅为 3，",
        "主质量仍是频繁切换的有限字母词，而不是可直接求和的长常步长旋转。",
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
        f"finite_carry_letter_alphabet_closed={str(payload['finite_carry_letter_alphabet_closed']).lower()}",
        f"long_constant_letter_block_route_available={str(payload['long_constant_letter_block_route_available']).lower()}",
        f"finite_letter_exponential_sum_saving_closed={str(payload['finite_letter_exponential_sum_saving_closed']).lower()}",
        f"completion_to_external_trace_or_kloosterman_closed={str(payload['completion_to_external_trace_or_kloosterman_closed']).lower()}",
        f"no_loss_qprefix_letter_atom_aggregation_closed={str(payload['no_loss_qprefix_letter_atom_aggregation_closed']).lower()}",
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
    print(f"letter_run_decomposition_closed={payload['finite_carry_letter_alphabet_closed']}")
    print(
        "finite_letter_exponential_sum_saving_closed="
        f"{payload['finite_letter_exponential_sum_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
