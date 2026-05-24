#!/usr/bin/env python3
"""审计 fixed-m q-prefix line atoms 的相位正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_phase_normal_form_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.json

上一层已经把 boundary endpoint-flux packets 无损拆成固定 m 的 q-prefix line
atoms。本层继续关闭一个确定性相位门：对每条边 (P,q,m)，令

    q*m = k*P + D,  0 < D < P.

则 endpoint/sawtooth 相位有精确重标记

    e(h*k*P/q) = e(-h*D/q) = e(h*A(q)/q),  A(q) = -D mod q.

该正规形把 q-prefix atom 变成固定 m、移动 prime-q 分母、Beatty 残差分子的
reciprocal orbit。它不提供相位节省；相反，审计量化说明绝大多数 atoms 的
numerator A(q) 随 q 移动，因此还不是现有 Kloosterman/trace 定理可直接处理的
固定分子 completed family。
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


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-phase-normal-form"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json",
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
        "role": "trace bilinear input would need a completed moving-q family, not just the real reciprocal normal form",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman estimates require an inverse-fraction or completed trace variable after normalization",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "one-dimensional q-prefix orbits with moving numerator are not direct composite Type-II rectangles",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman fractions become relevant only after converting A(q)/q to an admissible completed family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not estimate the fixed-m q-prefix reciprocal phase orbit",
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


def q_values_for_packet(packet: dict[str, Any], primes: list[int]) -> list[int]:
    """展开 packet 的 prime-q prefix。"""
    return [q for q in primes if packet["q_start"] <= q <= packet["q_end"]]


def normal_edge(P: int, q: int, m: int) -> dict[str, int]:
    """返回 q*m=kP+D 的正规形数据。"""
    product = q * m
    k = product // P
    D = product - k * P
    A = (-D) % q
    return {"q": q, "m": m, "k": k, "D": D, "A": A}


def atom_phase_profile(
    packet_index: int,
    packet: dict[str, Any],
    endpoint_class: str,
    m_value: int,
    q_values: list[int],
) -> dict[str, Any]:
    """构造一个 fixed-m q-prefix atom 的相位正规形 profile。"""
    edges = [normal_edge(packet["P"], q, m_value) for q in q_values]
    k_values = [edge["k"] for edge in edges]
    d_values = [edge["D"] for edge in edges]
    a_values = [edge["A"] for edge in edges]
    k_steps = [right - left for left, right in zip(k_values, k_values[1:])]

    if len(q_values) == 1:
        k_orbit_class = "singleton_q"
    elif all(step > 0 for step in k_steps):
        k_orbit_class = "strict_beatty_k_multiq"
    elif len(set(k_values)) == 1:
        k_orbit_class = "constant_k_multiq"
    else:
        k_orbit_class = "mixed_beatty_k"

    if len(set(a_values)) == 1:
        numerator_motion_class = "constant_normalized_numerator"
    else:
        numerator_motion_class = "moving_beatty_numerator"

    return {
        "packet_index": packet_index,
        "P": packet["P"],
        "strip": packet["strip"],
        "endpoint_flux_class": endpoint_class,
        "m": m_value,
        "q_start": packet["q_start"],
        "q_end": packet["q_end"],
        "q_prefix_count": len(q_values),
        "edge_count": len(q_values),
        "k_min": min(k_values),
        "k_max": max(k_values),
        "k_distinct_count": len(set(k_values)),
        "k_span": max(k_values) - min(k_values) + 1,
        "D_min": min(d_values),
        "D_max": max(d_values),
        "A_min": min(a_values),
        "A_max": max(a_values),
        "A_distinct_count": len(set(a_values)),
        "k_orbit_class": k_orbit_class,
        "numerator_motion_class": numerator_motion_class,
        "q_sample": q_values[:5],
        "k_sample": k_values[:5],
        "D_sample": d_values[:5],
        "A_sample": a_values[:5],
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


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 fixed-m q-prefix atoms 的相位正规形。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_set = set(primes)
    packets = qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    atom_count_by_strip: Counter[str] = Counter()
    atom_edge_by_strip: Counter[str] = Counter()
    atom_count_by_k_orbit: Counter[str] = Counter()
    atom_edge_by_k_orbit: Counter[str] = Counter()
    atom_count_by_numerator_motion: Counter[str] = Counter()
    atom_edge_by_numerator_motion: Counter[str] = Counter()
    atom_count_by_endpoint_class: Counter[str] = Counter()
    atom_edge_by_endpoint_class: Counter[str] = Counter()

    q_counts: list[int] = []
    k_spans: list[int] = []
    k_distinct_counts: list[int] = []
    k_step_values: list[int] = []
    sample_atoms: list[dict[str, Any]] = []
    bad_edge_samples: list[dict[str, Any]] = []
    totals: Counter[str] = Counter()

    for packet_index, packet in enumerate(packets):
        profile = qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        endpoint_class = profile["endpoint_flux_class"]
        q_values = q_values_for_packet(packet, primes)
        m_values = sorted(qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))

        for m_value in m_values:
            atom = atom_phase_profile(packet_index, packet, endpoint_class, m_value, q_values)
            atom_count_by_strip[packet["strip"]] += 1
            atom_edge_by_strip[packet["strip"]] += atom["edge_count"]
            atom_count_by_k_orbit[atom["k_orbit_class"]] += 1
            atom_edge_by_k_orbit[atom["k_orbit_class"]] += atom["edge_count"]
            atom_count_by_numerator_motion[atom["numerator_motion_class"]] += 1
            atom_edge_by_numerator_motion[atom["numerator_motion_class"]] += atom["edge_count"]
            atom_count_by_endpoint_class[endpoint_class] += 1
            atom_edge_by_endpoint_class[endpoint_class] += atom["edge_count"]
            q_counts.append(atom["q_prefix_count"])
            k_spans.append(atom["k_span"])
            k_distinct_counts.append(atom["k_distinct_count"])

            previous_k: int | None = None
            for q in q_values:
                edge = normal_edge(packet["P"], q, m_value)
                totals["phase_edge_count_total"] += 1
                totals["q_not_prime_count"] += int(q not in prime_set)
                totals["m_not_prime_count"] += int(m_value not in prime_set)
                totals["m_equals_P_count"] += int(m_value == packet["P"])
                totals["k_out_of_strict_row_range_count"] += int(
                    not (1 <= edge["k"] < packet["P"])
                )
                totals["D_out_of_range_count"] += int(not (1 <= edge["D"] < packet["P"]))
                totals["A_zero_count"] += int(edge["A"] == 0)
                totals["phase_congruence_mismatch_count"] += int(
                    (edge["D"] + edge["k"] * packet["P"]) % q != 0
                )
                totals["product_division_mismatch_count"] += int(
                    q * m_value != edge["k"] * packet["P"] + edge["D"]
                )
                if previous_k is not None:
                    step = edge["k"] - previous_k
                    k_step_values.append(step)
                    totals["k_nonincreasing_step_count"] += int(step <= 0)
                previous_k = edge["k"]

                if (
                    (
                        edge["A"] == 0
                        or not (1 <= edge["D"] < packet["P"])
                        or not (1 <= edge["k"] < packet["P"])
                    )
                    and len(bad_edge_samples) < 8
                ):
                    bad_edge_samples.append(
                        {
                            "P": packet["P"],
                            "q": q,
                            "m": m_value,
                            "k": edge["k"],
                            "D": edge["D"],
                            "A": edge["A"],
                            "strip": packet["strip"],
                        }
                    )

            if len(sample_atoms) < 16 and (
                atom["q_prefix_count"] >= 17
                or atom["numerator_motion_class"] == "constant_normalized_numerator"
            ):
                sample_atoms.append(atom)

    atom_count_total = sum(atom_count_by_strip.values())
    identity_verified = (
        atom_count_total == previous_audit["qprefix_line_atom_count_total"]
        and totals["phase_edge_count_total"]
        == previous_audit["qprefix_line_atom_edge_count_total"]
        and totals["product_division_mismatch_count"] == 0
        and totals["phase_congruence_mismatch_count"] == 0
        and totals["q_not_prime_count"] == 0
        and totals["m_not_prime_count"] == 0
        and totals["m_equals_P_count"] == 0
        and totals["k_out_of_strict_row_range_count"] == 0
        and totals["D_out_of_range_count"] == 0
        and totals["A_zero_count"] == 0
        and totals["k_nonincreasing_step_count"] == 0
    )

    return {
        "max_prime": max_prime,
        "previous_qprefix_line_atom_count_total": previous_audit[
            "qprefix_line_atom_count_total"
        ],
        "previous_qprefix_line_atom_edge_count_total": previous_audit[
            "qprefix_line_atom_edge_count_total"
        ],
        "phase_normal_form_atom_count_total": atom_count_total,
        "phase_normal_form_edge_count_total": totals["phase_edge_count_total"],
        "product_division_mismatch_count": totals["product_division_mismatch_count"],
        "phase_congruence_mismatch_count": totals["phase_congruence_mismatch_count"],
        "q_not_prime_count": totals["q_not_prime_count"],
        "m_not_prime_count": totals["m_not_prime_count"],
        "m_equals_P_count": totals["m_equals_P_count"],
        "k_out_of_strict_row_range_count": totals["k_out_of_strict_row_range_count"],
        "D_out_of_range_count": totals["D_out_of_range_count"],
        "A_zero_count": totals["A_zero_count"],
        "k_nonincreasing_step_count": totals["k_nonincreasing_step_count"],
        "phase_normal_form_identity_verified": identity_verified,
        "q_prefix_count_min": min(q_counts),
        "q_prefix_count_median_atom_weighted": statistics.median(q_counts),
        "q_prefix_count_max": max(q_counts),
        "k_span_min": min(k_spans),
        "k_span_median": statistics.median(k_spans),
        "k_span_max": max(k_spans),
        "k_span_average": sum(k_spans) / len(k_spans),
        "k_distinct_count_min": min(k_distinct_counts),
        "k_distinct_count_median": statistics.median(k_distinct_counts),
        "k_distinct_count_max": max(k_distinct_counts),
        "k_step_min": min(k_step_values),
        "k_step_median": statistics.median(k_step_values),
        "k_step_max": max(k_step_values),
        "k_step_average": sum(k_step_values) / len(k_step_values),
        "atom_count_by_strip_rows": counter_rows(
            atom_count_by_strip, atom_edge_by_strip, "strip"
        ),
        "atom_count_by_k_orbit_rows": counter_rows(
            atom_count_by_k_orbit, atom_edge_by_k_orbit, "k_orbit_class"
        ),
        "atom_count_by_numerator_motion_rows": counter_rows(
            atom_count_by_numerator_motion,
            atom_edge_by_numerator_motion,
            "numerator_motion_class",
        ),
        "atom_count_by_endpoint_flux_class_rows": counter_rows(
            atom_count_by_endpoint_class,
            atom_edge_by_endpoint_class,
            "endpoint_flux_class",
        ),
        "bad_edge_samples": bad_edge_samples,
        "sample_atoms": sample_atoms,
        "phase_normal_form_closed": identity_verified,
        "moving_beatty_numerator_dominates": atom_count_by_numerator_motion[
            "moving_beatty_numerator"
        ]
        > atom_count_by_numerator_motion["constant_normalized_numerator"],
        "fixed_numerator_completed_kloosterman_input_available": False,
        "moving_q_denominator_completed_trace_closed": False,
        "qprefix_line_atom_phase_saving_closed": False,
        "no_loss_qprefix_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_phase_normal_form_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_line_atoms_have_phase_normal_form_completed_trace_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after fixed-m q-prefix atomization, the next acyclic step is to normalize the reciprocal phase before attempting any trace/Kloosterman input",
        "current_object": {
            "input": "15439 fixed-m q-prefix line atoms carrying 177515 edges",
            "identity": "q*m=k*P+D with e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q)",
            "dominant_shape": "moving Beatty numerator A(q) on a prime-q prefix",
            "remaining": "phase saving for moving-numerator prime-q reciprocal orbits and no-loss aggregation",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "QPrefixLineAtomLedgerImported",
                True,
                True,
                "The fixed-m q-prefix atom ledger is inherited.",
                "none for support import",
            ),
            gate(
                "ProductDivisionPhaseNormalForm",
                finite_audit["phase_normal_form_closed"],
                finite_audit["phase_normal_form_closed"],
                "Every edge has q*m=k*P+D with 1<=k<P and 1<=D<P.",
                "none for deterministic division normal form",
            ),
            gate(
                "ReciprocalPhaseRelabeling",
                finite_audit["phase_congruence_mismatch_count"] == 0,
                finite_audit["phase_congruence_mismatch_count"] == 0,
                "The endpoint phase is exactly e(-h*D/q)=e(h*A(q)/q).",
                "none for formal phase relabeling",
            ),
            gate(
                "BeattyKOrbitMonotonicity",
                finite_audit["k_nonincreasing_step_count"] == 0,
                finite_audit["k_nonincreasing_step_count"] == 0,
                "On every multi-q atom, k(q)=floor(q*m/P) is strictly increasing along the prime prefix.",
                "none for finite orbit monotonicity",
            ),
            gate(
                "FixedNumeratorCompletedKloostermanInput",
                False,
                False,
                "Most atoms have a moving Beatty numerator A(q), so the normalized family is not a fixed-numerator completed Kloosterman input.",
                "need a moving-numerator completion or a new reciprocal-orbit estimate",
            ),
            gate(
                "QPrefixLineAtomPhaseSaving",
                False,
                False,
                "Prove cancellation on moving-numerator fixed-m prime-q prefix reciprocal orbits.",
                "new completed trace/Kloosterman or Vaughan-Type-II bridge required",
            ),
            gate(
                "NoLossQPrefixAtomAggregation",
                False,
                False,
                "Aggregate atom-level phase estimates across all 15439 atoms without losing the boundary gain.",
                "requires analytic aggregation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "normal form gives explicit reciprocal phases, but not a completed moving-q trace family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "no direct inverse-fraction Kloosterman variable is produced by e(A(q)/q)",
            "Pascadi_composite_Type_II": "q-prefix line atoms remain one-dimensional after fixed-m normalization",
            "Wright_unbalanced_Kloosterman": "closest candidate after converting moving numerator A(q) into an admissible completed family",
            "Li_short_interval_x_052": "prime existence in short intervals does not estimate the normalized reciprocal phase",
        },
        "latest_narrowest_mouth": [
            "MovingBeattyNumeratorPrimeQPrefixReciprocalPhaseSaving",
            "AND CompletionOfA(q)/qToExternalTraceOrKloostermanFamily",
            "AND NoLossAggregationAcross15439QPrefixPhaseAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "phase_normal_form_closed": finite_audit["phase_normal_form_closed"],
        "fixed_numerator_completed_kloosterman_input_available": False,
        "moving_q_denominator_completed_trace_closed": False,
        "qprefix_line_atom_phase_saving_closed": False,
        "no_loss_qprefix_atom_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF boundary endpoint-flux q-prefix phase normal-form 审计",
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
        "## 2. 相位正规形有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"previous_qprefix_line_atom_count_total={audit['previous_qprefix_line_atom_count_total']}",
        f"previous_qprefix_line_atom_edge_count_total={audit['previous_qprefix_line_atom_edge_count_total']}",
        f"phase_normal_form_atom_count_total={audit['phase_normal_form_atom_count_total']}",
        f"phase_normal_form_edge_count_total={audit['phase_normal_form_edge_count_total']}",
        f"product_division_mismatch_count={audit['product_division_mismatch_count']}",
        f"phase_congruence_mismatch_count={audit['phase_congruence_mismatch_count']}",
        f"q_not_prime_count={audit['q_not_prime_count']}",
        f"m_not_prime_count={audit['m_not_prime_count']}",
        f"m_equals_P_count={audit['m_equals_P_count']}",
        f"k_out_of_strict_row_range_count={audit['k_out_of_strict_row_range_count']}",
        f"D_out_of_range_count={audit['D_out_of_range_count']}",
        f"A_zero_count={audit['A_zero_count']}",
        f"k_nonincreasing_step_count={audit['k_nonincreasing_step_count']}",
        f"phase_normal_form_identity_verified={str(audit['phase_normal_form_identity_verified']).lower()}",
        f"q_prefix_count_min/median_atom_weighted/max={audit['q_prefix_count_min']}/{audit['q_prefix_count_median_atom_weighted']}/{audit['q_prefix_count_max']}",
        f"k_span_min/median/max={audit['k_span_min']}/{audit['k_span_median']}/{audit['k_span_max']}",
        f"k_distinct_count_min/median/max={audit['k_distinct_count_min']}/{audit['k_distinct_count_median']}/{audit['k_distinct_count_max']}",
        f"k_step_min/median/max={audit['k_step_min']}/{audit['k_step_median']}/{audit['k_step_max']}",
        f"phase_normal_form_closed={str(audit['phase_normal_form_closed']).lower()}",
        f"qprefix_line_atom_phase_saving_closed={str(audit['qprefix_line_atom_phase_saving_closed']).lower()}",
        "```",
        "",
        "atom strip 分桶：",
        "",
        *markdown_table(audit["atom_count_by_strip_rows"], ["strip", "atom_count", "edge_weight_sum"]),
        "",
        "k-orbit 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_k_orbit_rows"],
            ["k_orbit_class", "atom_count", "edge_weight_sum"],
        ),
        "",
        "normalized numerator motion 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_numerator_motion_rows"],
            ["numerator_motion_class", "atom_count", "edge_weight_sum"],
        ),
        "",
        "endpoint-flux class 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_endpoint_flux_class_rows"],
            ["endpoint_flux_class", "atom_count", "edge_weight_sum"],
        ),
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
        "结论：fixed-m q-prefix atom 的 endpoint phase 已经正规化为移动分子",
        "`A(q)/q` 的 prime-q reciprocal orbit。该层关闭的是确定性相位正规形，",
        "不关闭相位节省、completed trace/Kloosterman 输入或全局无损聚合。",
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
        f"phase_normal_form_closed={str(payload['phase_normal_form_closed']).lower()}",
        f"fixed_numerator_completed_kloosterman_input_available={str(payload['fixed_numerator_completed_kloosterman_input_available']).lower()}",
        f"moving_q_denominator_completed_trace_closed={str(payload['moving_q_denominator_completed_trace_closed']).lower()}",
        f"qprefix_line_atom_phase_saving_closed={str(payload['qprefix_line_atom_phase_saving_closed']).lower()}",
        f"no_loss_qprefix_atom_aggregation_closed={str(payload['no_loss_qprefix_atom_aggregation_closed']).lower()}",
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
    print(f"phase_normal_form_closed={payload['phase_normal_form_closed']}")
    print(f"qprefix_line_atom_phase_saving_closed={payload['qprefix_line_atom_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
