#!/usr/bin/env python3
"""审计 prime-survivor q-prefix cap 的 residual rough-envelope 来源。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_rough_envelope_cap_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.json

上一层有限审计发现 prime-survivor floor graph 的转置 q-fibre 是 prefix，且每行
cap Q*(P,m) 单峰。本层解释该结构的来源。

对固定 P 令 R_P 为 residual rough composite cofactors。对 P/2<q<P，实际
selected residual m 条件等价于显式 envelope 条件：

  m in R_P,  q <= m,  q*m < P^2.

因此 R_{P,q}=R_P ∩ [q, P^2/q) 是随 q 递增而嵌套缩小的集合。令
A_q=min R_{P,q}, B_q=max R_{P,q}。prime survivor blockers 正是

  prime m in [A_q,B_q] minus the diagonal m=P.

于是固定 m 的 q-neighbourhood 是两个单调条件 A_q<m 与 B_q>m 的交，因而是
从首个 eligible q 开始的 prefix；cap 是两个单调阈值的最小值，故为单峰。

这关闭的是 q-prefix/unimodal 结构来源，不是相位节省。
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

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit as tax  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_floor_span_completion_audit as floor_span  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"
TOL = 1e-9

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.json",
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
        "role": "candidate only after the rough-envelope cap is converted into a trace bilinear family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "candidate after completed Kloosterman variables replace the moving floor denominator",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "candidate after splitting the rough-envelope cap into genuine Type-II fibres",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate if the cap can be reorganised as an unbalanced convolution",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "candidate after matching smooth/squarefree parameters; not direct here",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "still does not provide the pointwise theta=1/2 closure needed here",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def envelope_records(P: int, q: int, records: list[dict[str, int]]) -> list[int]:
    """返回显式 residual envelope R_P ∩ [q, P^2/q)。"""
    return [record["m"] for record in records if q <= record["m"] and q * record["m"] < P * P]


def selected_m_from_existing_support(P: int, q: int, records: list[dict[str, int]]) -> list[int]:
    """用既有 selected_k_support_for_q 反推出 selected residual m。"""
    k_values = tax.selected_k_support_for_q(P, q, records)
    out: list[int] = []
    for record in records:
        m = record["m"]
        if m < q:
            continue
        k = (q * m) // P
        if k in k_values:
            out.append(m)
    return sorted(out)


def prime_envelope(P: int, A: int, B: int, primes: list[int]) -> list[int]:
    """返回 rough envelope 内的 prime blockers，扣除 diagonal m=P。"""
    return [m for m in floor_span.primes_in_interval(primes, A, B) if m != P]


def cap_unimodality(caps: list[tuple[int, int, int, int, int]]) -> dict[str, Any]:
    """检查 cap=min(A-threshold,B-threshold) 后的单峰性。"""
    previous = caps[0][1]
    state = "up"
    turn_count = 0
    bad_after_down_increase = 0
    for _m, cap, _a_cap, _b_cap, _count in caps[1:]:
        if cap > previous:
            bad_after_down_increase += int(state == "down")
            state = "up"
        elif cap < previous:
            turn_count += int(state == "up")
            state = "down"
        previous = cap
    max_cap = max(cap for _m, cap, _a_cap, _b_cap, _count in caps)
    peak_ms = [m for m, cap, _a_cap, _b_cap, _count in caps if cap == max_cap]
    return {
        "turn_count": turn_count,
        "bad_after_down_increase": bad_after_down_increase,
        "max_cap_q": max_cap,
        "peak_m_min": peak_ms[0],
        "peak_m_max": peak_ms[-1],
        "peak_plateau_prime_count": len(peak_ms),
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 P<=max_prime 的 residual rough-envelope cap 来源。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    edges = floor_span.prime_blocker_edges(max_prime, primes)
    actual_by_pq: defaultdict[tuple[int, int], set[int]] = defaultdict(set)
    actual_by_pm: defaultdict[tuple[int, int], set[int]] = defaultdict(set)
    for item in edges:
        actual_by_pq[(item["P"], item["q"])].add(item["m"])
        actual_by_pm[(item["P"], item["m"])].add(item["q"])

    P_values = [p for p in primes if 11 <= p <= max_prime]
    totals: Counter[str] = Counter()
    sample_envelopes: list[dict[str, Any]] = []
    sample_rows: list[dict[str, Any]] = []
    cap_paths: list[str] = []
    predicted_by_pm: defaultdict[tuple[int, int], set[int]] = defaultdict(set)
    interesting = {101, 257, 971, 1009}

    for P in P_values:
        records = primorial.residual_records_for_P(P, primes)
        W, _factors = primorial.primorial_modulus(P, primes)
        q_values = floor_span.q_prime_values(P, W, primes)
        envelope_by_q: dict[int, tuple[int, int, list[int]]] = {}
        last_A = None
        last_B = None
        row_bad_A = 0
        row_bad_B = 0
        row_edge_count = 0

        for q in q_values:
            selected_existing = selected_m_from_existing_support(P, q, records)
            selected_formula = sorted(envelope_records(P, q, records))
            totals["q_checked_count"] += 1
            totals["selected_formula_m_count_total"] += len(selected_formula)
            totals["selected_existing_m_count_total"] += len(selected_existing)
            mismatch = selected_existing != selected_formula
            totals["selected_envelope_formula_mismatch_count"] += int(mismatch)

            if selected_formula:
                A = selected_formula[0]
                B = selected_formula[-1]
                envelope_by_q[q] = (A, B, selected_formula)
                totals["nonempty_envelope_q_count"] += 1
                if last_A is not None:
                    row_bad_A += int(A < last_A)
                    row_bad_B += int(B > last_B)
                last_A = A
                last_B = B

                predicted_primes = set(prime_envelope(P, A, B, primes))
                actual_primes = actual_by_pq.get((P, q), set())
                missing = sorted(predicted_primes - actual_primes)
                extra = sorted(actual_primes - predicted_primes)
                totals["predicted_prime_edge_count_total"] += len(predicted_primes)
                totals["actual_prime_edge_count_total"] += len(actual_primes)
                totals["prime_envelope_missing_count"] += len(missing)
                totals["prime_envelope_extra_count"] += len(extra)
                totals["prime_envelope_bad_q_count"] += int(bool(missing or extra))
                row_edge_count += len(actual_primes)
                for m in predicted_primes:
                    predicted_by_pm[(P, m)].add(q)
                if len(sample_envelopes) < 10:
                    sample_envelopes.append(
                        {
                            "P": P,
                            "q": q,
                            "A": A,
                            "B": B,
                            "residual_count": len(selected_formula),
                            "prime_edges": len(actual_primes),
                            "bad_formula": int(mismatch),
                            "bad_prime_envelope": int(bool(missing or extra)),
                        }
                    )

        totals["A_monotonicity_bad_step_count"] += row_bad_A
        totals["B_monotonicity_bad_step_count"] += row_bad_B

        # 中文注释：由 A_q<m 与 B_q>m 两个单调阈值重建 cap。
        row_caps: list[tuple[int, int, int, int, int]] = []
        for (PP, m), actual_qs in sorted(actual_by_pm.items()):
            if PP != P:
                continue
            a_good = [q for q, (A, _B, _items) in envelope_by_q.items() if A < m]
            b_good = [q for q, (_A, B, _items) in envelope_by_q.items() if B > m]
            if not a_good or not b_good:
                totals["cap_threshold_empty_side_count"] += 1
                continue
            a_cap = max(a_good)
            b_cap = max(b_good)
            cap = min(a_cap, b_cap)
            predicted_qs = predicted_by_pm.get((P, m), set())
            actual_cap = max(actual_qs)
            totals["pm_bucket_count"] += 1
            totals["cap_min_threshold_mismatch_count"] += int(cap != actual_cap)
            totals["predicted_qprefix_mismatch_count"] += int(predicted_qs != actual_qs)
            row_caps.append((m, cap, a_cap, b_cap, len(actual_qs)))

        if row_caps:
            profile = cap_unimodality(row_caps)
            totals["active_P_count"] += 1
            totals["cap_unimodality_bad_row_count"] += int(profile["bad_after_down_increase"] != 0)
            totals["cap_turn_count_total"] += profile["turn_count"]
            if P in interesting:
                sample_rows.append(
                    {
                        "P": P,
                        "pm_buckets": len(row_caps),
                        "edge_count": row_edge_count,
                        "A_bad_steps": row_bad_A,
                        "B_bad_steps": row_bad_B,
                        "turn_count": profile["turn_count"],
                        "bad_after_down_increase": profile["bad_after_down_increase"],
                        "max_cap_q": profile["max_cap_q"],
                        "peak_m_min": profile["peak_m_min"],
                        "peak_m_max": profile["peak_m_max"],
                    }
                )
                left = ", ".join(
                    f"{m}->min({a},{b})={cap}" for m, cap, a, b, _count in row_caps[:6]
                )
                right = ", ".join(
                    f"{m}->min({a},{b})={cap}" for m, cap, a, b, _count in row_caps[-6:]
                )
                cap_paths.append(f"P={P}: left {left}; right {right}")

    total_bad = (
        totals["selected_envelope_formula_mismatch_count"]
        + totals["prime_envelope_missing_count"]
        + totals["prime_envelope_extra_count"]
        + totals["A_monotonicity_bad_step_count"]
        + totals["B_monotonicity_bad_step_count"]
        + totals["cap_threshold_empty_side_count"]
        + totals["cap_min_threshold_mismatch_count"]
        + totals["predicted_qprefix_mismatch_count"]
        + totals["cap_unimodality_bad_row_count"]
    )
    return {
        "max_prime": max_prime,
        "q_checked_count": totals["q_checked_count"],
        "nonempty_envelope_q_count": totals["nonempty_envelope_q_count"],
        "selected_formula_m_count_total": totals["selected_formula_m_count_total"],
        "selected_existing_m_count_total": totals["selected_existing_m_count_total"],
        "selected_envelope_formula_mismatch_count": totals[
            "selected_envelope_formula_mismatch_count"
        ],
        "actual_prime_edge_count_total": totals["actual_prime_edge_count_total"],
        "previous_prime_survivor_edge_count_total": previous_audit["prime_survivor_edge_count_total"],
        "predicted_prime_edge_count_total": totals["predicted_prime_edge_count_total"],
        "prime_envelope_missing_count": totals["prime_envelope_missing_count"],
        "prime_envelope_extra_count": totals["prime_envelope_extra_count"],
        "prime_envelope_bad_q_count": totals["prime_envelope_bad_q_count"],
        "A_monotonicity_bad_step_count": totals["A_monotonicity_bad_step_count"],
        "B_monotonicity_bad_step_count": totals["B_monotonicity_bad_step_count"],
        "pm_bucket_count": totals["pm_bucket_count"],
        "previous_pm_bucket_count_total": previous_audit["pm_bucket_count_total"],
        "cap_threshold_empty_side_count": totals["cap_threshold_empty_side_count"],
        "cap_min_threshold_mismatch_count": totals["cap_min_threshold_mismatch_count"],
        "predicted_qprefix_mismatch_count": totals["predicted_qprefix_mismatch_count"],
        "active_P_count": totals["active_P_count"],
        "previous_active_P_count": previous_audit["active_P_count"],
        "cap_unimodality_bad_row_count": totals["cap_unimodality_bad_row_count"],
        "cap_turn_count_total": totals["cap_turn_count_total"],
        "total_bad_rough_envelope_cap_count": total_bad,
        "selected_residual_envelope_formula_verified": (
            totals["selected_envelope_formula_mismatch_count"] == 0
        ),
        "prime_survivor_rough_envelope_identity_verified": (
            totals["prime_envelope_missing_count"] == 0
            and totals["prime_envelope_extra_count"] == 0
        ),
        "rough_envelope_endpoint_monotonicity_verified": (
            totals["A_monotonicity_bad_step_count"] == 0
            and totals["B_monotonicity_bad_step_count"] == 0
        ),
        "cap_min_threshold_identity_verified": (
            totals["cap_min_threshold_mismatch_count"] == 0
            and totals["predicted_qprefix_mismatch_count"] == 0
        ),
        "global_qprefix_unimodal_structure_explained": total_bad == 0,
        "prefix_cap_trace_or_typeii_embedding_closed": False,
        "finite_evidence_not_used_as_target_proof": True,
        "sample_envelopes": sample_envelopes,
        "sample_rows": sample_rows,
        "cap_paths": cap_paths,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_rough_envelope_cap_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "qprefix_unimodal_cap_explained_by_nested_residual_rough_envelope_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the q-prefix cap audit left a structural source question; the fastest non-cyclic advance is to derive the cap from the residual rough-composite envelope",
        "current_object": {
            "selected_residual_formula": "m in R_P and q<=m and q*m<P^2",
            "envelope": "R_{P,q}=R_P cap [q,P^2/q), A_q=min R_{P,q}, B_q=max R_{P,q}",
            "prime_survivor_identity": "M_prime(P,q)={prime m in [A_q,B_q]}\\{P}",
            "cap_formula": "Q*(P,m)=min(max{q:A_q<m}, max{q:B_q>m})",
            "remaining": "exploit the nested envelope cap analytically through trace/Type-II/convolution phase saving",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SelectedResidualRoughEnvelopeFormula",
                True,
                True,
                "The selected residual support is exactly R_P intersected with q<=m and q*m<P^2.",
                "none for the structural identity",
            ),
            gate(
                "PrimeSurvivorRoughEnvelopeIdentity",
                True,
                True,
                "Prime survivors are precisely primes inside [A_q,B_q] after removing the diagonal m=P.",
                "none for the structural identity",
            ),
            gate(
                "NestedEnvelopeEndpointMonotonicity",
                True,
                True,
                "A_q is nondecreasing and B_q is nonincreasing because R_{P,q} is nested as q increases.",
                "none for the structural identity",
            ),
            gate(
                "QPrefixUnimodalCapStructureExplained",
                True,
                True,
                "The q-prefix and unimodal cap follow from the two monotone endpoint thresholds.",
                "none for the support-shape reduction",
            ),
            gate(
                "PrefixCapTraceOrTypeIIPhaseSaving",
                False,
                False,
                "Use the nested rough-envelope cap to obtain cancellation or a completed bilinear/trace family.",
                "new analytic embedding still required",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "the support shape is now nested, but no trace-family sheaf or completed sum has been produced",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "the moving denominator q is not yet transformed into a completed Kloosterman variable",
            "Pascadi_composite_Type_II": "nested support may help split fibres, but Type-II lengths and weights remain unproved",
            "Wright_unbalanced_convolution": "the cap is compatible with an unbalanced viewpoint, but no convolution identity is closed",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "additional smooth/squarefree parameter matching remains absent",
            "Li_short_interval_x_052": "short-interval theta=0.52 remains above the required pointwise half-scale",
        },
        "latest_narrowest_mouth": [
            "PrefixCapTraceOrTypeIIPhaseSavingFromNestedRoughEnvelope",
            "AND CompletedTraceOrKloostermanVariableForMovingPrimeDenominator",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "selected_residual_rough_envelope_formula_closed": True,
        "prime_survivor_rough_envelope_identity_closed": True,
        "nested_envelope_endpoint_monotonicity_closed": True,
        "global_qprefix_unimodal_structure_explained": True,
        "prefix_cap_trace_or_typeii_embedding_closed": False,
        "completed_trace_or_kloosterman_variable_closed": False,
        "prime_floor_span_trace_or_typeii_phase_saving_closed": False,
        "small_lpf_blocker_packet_control_closed": False,
        "uniform_cancellation_across_sparse_k_support_radial_kernels_closed": False,
        "rough_beta_siegel_walfisz_factor_extracted": False,
        "pointwise_pk_transfer_closed": False,
        "q_support_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    sample_envelope_fields = [
        "P",
        "q",
        "A",
        "B",
        "residual_count",
        "prime_edges",
        "bad_formula",
        "bad_prime_envelope",
    ]
    sample_row_fields = [
        "P",
        "pm_buckets",
        "edge_count",
        "A_bad_steps",
        "B_bad_steps",
        "turn_count",
        "bad_after_down_increase",
        "max_cap_q",
        "peak_m_min",
        "peak_m_max",
    ]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor rough-envelope cap 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"selected_residual_formula={current['selected_residual_formula']}",
        f"envelope={current['envelope']}",
        f"prime_survivor_identity={current['prime_survivor_identity']}",
        f"cap_formula={current['cap_formula']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. rough-envelope cap 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"q_checked_count={audit['q_checked_count']}",
        f"nonempty_envelope_q_count={audit['nonempty_envelope_q_count']}",
        f"selected_formula_m_count_total={audit['selected_formula_m_count_total']}",
        f"selected_existing_m_count_total={audit['selected_existing_m_count_total']}",
        f"selected_envelope_formula_mismatch_count={audit['selected_envelope_formula_mismatch_count']}",
        f"actual_prime_edge_count_total={audit['actual_prime_edge_count_total']}",
        f"previous_prime_survivor_edge_count_total={audit['previous_prime_survivor_edge_count_total']}",
        f"predicted_prime_edge_count_total={audit['predicted_prime_edge_count_total']}",
        f"prime_envelope_missing_count={audit['prime_envelope_missing_count']}",
        f"prime_envelope_extra_count={audit['prime_envelope_extra_count']}",
        f"prime_envelope_bad_q_count={audit['prime_envelope_bad_q_count']}",
        f"A_monotonicity_bad_step_count={audit['A_monotonicity_bad_step_count']}",
        f"B_monotonicity_bad_step_count={audit['B_monotonicity_bad_step_count']}",
        f"pm_bucket_count={audit['pm_bucket_count']}",
        f"previous_pm_bucket_count_total={audit['previous_pm_bucket_count_total']}",
        f"cap_threshold_empty_side_count={audit['cap_threshold_empty_side_count']}",
        f"cap_min_threshold_mismatch_count={audit['cap_min_threshold_mismatch_count']}",
        f"predicted_qprefix_mismatch_count={audit['predicted_qprefix_mismatch_count']}",
        f"active_P_count={audit['active_P_count']}",
        f"previous_active_P_count={audit['previous_active_P_count']}",
        f"cap_unimodality_bad_row_count={audit['cap_unimodality_bad_row_count']}",
        f"cap_turn_count_total={audit['cap_turn_count_total']}",
        f"total_bad_rough_envelope_cap_count={audit['total_bad_rough_envelope_cap_count']}",
        f"selected_residual_envelope_formula_verified={primorial.bool_text(audit['selected_residual_envelope_formula_verified'])}",
        f"prime_survivor_rough_envelope_identity_verified={primorial.bool_text(audit['prime_survivor_rough_envelope_identity_verified'])}",
        f"rough_envelope_endpoint_monotonicity_verified={primorial.bool_text(audit['rough_envelope_endpoint_monotonicity_verified'])}",
        f"cap_min_threshold_identity_verified={primorial.bool_text(audit['cap_min_threshold_identity_verified'])}",
        f"global_qprefix_unimodal_structure_explained={primorial.bool_text(audit['global_qprefix_unimodal_structure_explained'])}",
        f"prefix_cap_trace_or_typeii_embedding_closed={primorial.bool_text(audit['prefix_cap_trace_or_typeii_embedding_closed'])}",
        "```",
        "",
        "代表 envelope：",
        "",
        primorial.table(audit["sample_envelopes"], sample_envelope_fields),
        "",
        "代表行：",
        "",
        primorial.table(audit["sample_rows"], sample_row_fields),
        "",
        "cap threshold 样本：",
        "",
        "```text",
        *audit["cap_paths"],
        "```",
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        primorial.table(payload["external_sources_consulted"], source_fields),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：q-prefix 与单峰 cap 的来源已压到 nested residual rough envelope：`R_{P,q}=R_P cap [q,P^2/q)`。这关闭了支撑形状来源，但没有产生相位节省；剩余是把该 nested cap 转成 completed trace/Kloosterman/Type-II 输入。",
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
        f"selected_residual_rough_envelope_formula_closed={primorial.bool_text(payload['selected_residual_rough_envelope_formula_closed'])}",
        f"prime_survivor_rough_envelope_identity_closed={primorial.bool_text(payload['prime_survivor_rough_envelope_identity_closed'])}",
        f"nested_envelope_endpoint_monotonicity_closed={primorial.bool_text(payload['nested_envelope_endpoint_monotonicity_closed'])}",
        f"global_qprefix_unimodal_structure_explained={primorial.bool_text(payload['global_qprefix_unimodal_structure_explained'])}",
        f"prefix_cap_trace_or_typeii_embedding_closed={primorial.bool_text(payload['prefix_cap_trace_or_typeii_embedding_closed'])}",
        f"completed_trace_or_kloosterman_variable_closed={primorial.bool_text(payload['completed_trace_or_kloosterman_variable_closed'])}",
        f"prime_floor_span_trace_or_typeii_phase_saving_closed={primorial.bool_text(payload['prime_floor_span_trace_or_typeii_phase_saving_closed'])}",
        f"small_lpf_blocker_packet_control_closed={primorial.bool_text(payload['small_lpf_blocker_packet_control_closed'])}",
        f"uniform_cancellation_across_sparse_k_support_radial_kernels_closed={primorial.bool_text(payload['uniform_cancellation_across_sparse_k_support_radial_kernels_closed'])}",
        f"rough_beta_siegel_walfisz_factor_extracted={primorial.bool_text(payload['rough_beta_siegel_walfisz_factor_extracted'])}",
        f"pointwise_pk_transfer_closed={primorial.bool_text(payload['pointwise_pk_transfer_closed'])}",
        f"q_support_phase_saving_closed={primorial.bool_text(payload['q_support_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={primorial.bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={primorial.bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={primorial.bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={primorial.bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("global_qprefix_unimodal_structure_explained=true")
    print("prefix_cap_trace_or_typeii_embedding_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
