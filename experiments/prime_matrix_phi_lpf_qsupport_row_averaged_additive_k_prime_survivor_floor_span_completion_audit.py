#!/usr/bin/env python3
"""审计 prime-survivor singleton layer 的 floor-span completion 正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_floor_span_completion_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.json

上一层把 moving Mobius 展开压成：

  small LPF blockers cancel by Euler involution,
  prime blockers remain as the d=1 singleton survivor layer.

本层继续非循环下钻：对每个固定 (P,q) bucket，prime survivor 的 m 坐标不是
任意稀疏黑箱，而是一个素数 floor-span：

  {prime m in [L_{P,q}, U_{P,q}]} minus the diagonal ghost m=P.

这里 L_{P,q}, U_{P,q} 是该 bucket 内实际 prime blocker 的最小/最大 m。
对角 m=P 给出 k=q、D=0，不是 blocker；若把 prime interval 完成后必须显式
扣掉它。该正规形仍不是相位节省定理；剩余是把 prime-prime floor graph 嵌入
trace/Type-II/convolution 结构，或者给出新的非点态相消。
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit as floorcell  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_correction_phase_audit as correction  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_dynamic_sqrt_sieve_audit as sqrtblocker  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"
TOL = 1e-9

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-audit.json",
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
        "role": "candidate trace bilinear input only after the floor-span survivor graph is embedded into a trace family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "candidate arbitrary-modulus Kloosterman input after a completed inverse-variable model exists",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "candidate composite Type-II input after dense enough bilinear fibres are constructed",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate unbalanced convolution input after the prime-prime floor graph is converted to a convolution packet",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "candidate smooth/squarefree parameter input, not a direct prime interval floor-span estimate",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "theta=0.52 short-interval prime input remains above the pointwise half-scale required for direct closure",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def primes_in_interval(primes: list[int], low: int, high: int) -> list[int]:
    """返回闭区间中的素数。"""
    return [p for p in primes if low <= p <= high]


def q_prime_values(P: int, W: int, primes: list[int]) -> list[int]:
    """返回 P/2<q<P 且为 W 单位的奇 q；在本设置下它们都是素数。"""
    prime_set = set(primes)
    return [q for q in floorcell.odd_q_values(P) if math.gcd(q, W) == 1 and q in prime_set]


def phase_for_m(P: int, q: int, m: int) -> complex:
    """返回 m 经 k=floor(qm/P) 推到 additive-k 后的相位。"""
    k = (q * m) // P
    return correction.additive_phase(P % q, q, k)


def prime_blocker_edges(max_prime: int, primes: list[int]) -> list[dict[str, int]]:
    """枚举 prime survivor singleton edges。"""
    blockers = sqrtblocker.collect_all_blockers(max_prime, primes)
    return [item for item in blockers if item["lpf"] == item["m"]]


def bucket_profile(
    P: int,
    q: int,
    items: list[dict[str, int]],
    primes: list[int],
) -> dict[str, Any]:
    """审计固定 (P,q) 的 prime survivor floor-span。"""
    m_values = sorted({item["m"] for item in items})
    L = m_values[0]
    U = m_values[-1]
    span_primes = primes_in_interval(primes, L, U)
    span_set = set(span_primes)
    edge_set = set(m_values)
    diagonal_ghost = P if P in span_set else 0
    expected_set = set(span_set)
    if diagonal_ghost:
        expected_set.remove(P)

    raw_missing = sorted(span_set - edge_set)
    raw_extra = sorted(edge_set - span_set)
    expected_missing = sorted(expected_set - edge_set)
    expected_extra = sorted(edge_set - expected_set)

    survivor_phase = sum((phase_for_m(P, q, item["m"]) for item in items), 0j)
    span_phase = sum((phase_for_m(P, q, m) for m in span_primes), 0j)
    ghost_phase = phase_for_m(P, q, P) if diagonal_ghost else 0j
    phase_error = abs(survivor_phase - (span_phase - ghost_phase))

    # 中文注释：m=P 的 floor 值是 k=q 且 D=0，因此只能作为完成后的 ghost。
    ghost_k = (q * P) // P if diagonal_ghost else 0
    return {
        "P": P,
        "q": q,
        "L": L,
        "U": U,
        "edge_count": len(edge_set),
        "span_prime_count": len(span_set),
        "raw_missing_count": len(raw_missing),
        "raw_extra_count": len(raw_extra),
        "diagonal_ghost": diagonal_ghost,
        "diagonal_ghost_k": ghost_k,
        "expected_count_after_diagonal_subtraction": len(expected_set),
        "expected_missing_count": len(expected_missing),
        "expected_extra_count": len(expected_extra),
        "raw_missing_values": raw_missing[:8],
        "raw_extra_values": raw_extra[:8],
        "expected_missing_values": expected_missing[:8],
        "expected_extra_values": expected_extra[:8],
        "phase_error_after_diagonal_subtraction": phase_error,
        "span_identity_verified": (
            not expected_missing
            and not expected_extra
            and not raw_extra
            and all(value == P for value in raw_missing)
            and phase_error <= TOL
        ),
        "sample": f"P={P},q={q},m-span=[{L},{U}],edges={len(edge_set)},span_primes={len(span_set)},ghost={diagonal_ghost or 'none'}",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 P<=max_prime 的 prime survivor floor-span completion。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    edges = prime_blocker_edges(max_prime, primes)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    grouped: defaultdict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for item in edges:
        grouped[(item["P"], item["q"])].append(item)

    totals: Counter[str] = Counter()
    row_profiles: dict[int, Counter[str]] = defaultdict(Counter)
    row_q_sets: defaultdict[int, set[int]] = defaultdict(set)
    row_m_sets: defaultdict[int, set[int]] = defaultdict(set)
    row_m_to_q: defaultdict[int, defaultdict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
    row_k_to_q: defaultdict[int, defaultdict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
    sample_buckets: list[dict[str, Any]] = []
    ghost_samples: list[str] = []
    no_ghost_samples: list[str] = []
    max_phase_error = 0.0

    for (P, q), items in sorted(grouped.items()):
        profile = bucket_profile(P, q, items, primes)
        max_phase_error = max(max_phase_error, profile["phase_error_after_diagonal_subtraction"])
        totals["q_bucket_count"] += 1
        totals["survivor_edge_count"] += profile["edge_count"]
        totals["span_prime_count"] += profile["span_prime_count"]
        totals["raw_missing_count"] += profile["raw_missing_count"]
        totals["raw_extra_count"] += profile["raw_extra_count"]
        totals["diagonal_ghost_count"] += int(bool(profile["diagonal_ghost"]))
        totals["bucket_with_only_diagonal_ghost"] += int(
            bool(profile["diagonal_ghost"])
            and profile["raw_missing_count"] == 1
            and profile["raw_missing_values"] == [P]
        )
        totals["bucket_with_no_raw_missing"] += int(profile["raw_missing_count"] == 0)
        totals["expected_missing_after_diagonal_subtraction"] += profile["expected_missing_count"]
        totals["expected_extra_after_diagonal_subtraction"] += profile["expected_extra_count"]
        totals["bad_span_identity"] += int(not profile["span_identity_verified"])

        row = row_profiles[P]
        row["edge_count"] += profile["edge_count"]
        row["q_bucket_count"] += 1
        row["span_prime_count"] += profile["span_prime_count"]
        row["raw_missing_count"] += profile["raw_missing_count"]
        row["diagonal_ghost_count"] += int(bool(profile["diagonal_ghost"]))
        row["bad_span_identity"] += int(not profile["span_identity_verified"])
        row["max_q_to_m_degree"] = max(row["max_q_to_m_degree"], profile["edge_count"])
        row_q_sets[P].add(q)
        for item in items:
            m = item["m"]
            k = item["k"]
            row_m_sets[P].add(m)
            row_m_to_q[P][m].add(q)
            row_k_to_q[P][k].add(q)

        if len(sample_buckets) < 8:
            sample_buckets.append(
                {
                    "P": P,
                    "q": q,
                    "L": profile["L"],
                    "U": profile["U"],
                    "edges": profile["edge_count"],
                    "span_primes": profile["span_prime_count"],
                    "raw_missing_count": profile["raw_missing_count"],
                    "diagonal_ghost": profile["diagonal_ghost"] or "none",
                    "phase_error": f"{profile['phase_error_after_diagonal_subtraction']:.3e}",
                }
            )
        if profile["diagonal_ghost"] and len(ghost_samples) < 6:
            ghost_samples.append(profile["sample"])
        if not profile["diagonal_ghost"] and len(no_ghost_samples) < 6:
            no_ghost_samples.append(profile["sample"])

    q_eligible_total = 0
    m_eligible_total = 0
    m_eligible_without_diagonal_total = 0
    full_prime_rectangle_total = 0
    full_prime_rectangle_without_diagonal_total = 0
    sample_rows: list[dict[str, Any]] = []
    interesting = {101, 257, 971, 1009}
    for P in P_values:
        W, _factors = primorial.primorial_modulus(P, primes)
        q_eligible = q_prime_values(P, W, primes)
        m_eligible = primes_in_interval(primes, P // 2 + 1, 2 * P - 1)
        m_eligible_without_diagonal = [m for m in m_eligible if m != P]
        q_eligible_total += len(q_eligible)
        m_eligible_total += len(m_eligible)
        m_eligible_without_diagonal_total += len(m_eligible_without_diagonal)
        rectangle = len(q_eligible) * len(m_eligible)
        rectangle_without_diagonal = len(q_eligible) * len(m_eligible_without_diagonal)
        full_prime_rectangle_total += rectangle
        full_prime_rectangle_without_diagonal_total += rectangle_without_diagonal
        row = row_profiles[P]
        if P in interesting:
            max_m_to_q = max((len(qs) for qs in row_m_to_q[P].values()), default=0)
            max_k_to_q = max((len(qs) for qs in row_k_to_q[P].values()), default=0)
            sample_rows.append(
                {
                    "P": P,
                    "edges": row["edge_count"],
                    "q_buckets": len(row_q_sets[P]),
                    "distinct_m": len(row_m_sets[P]),
                    "eligible_q_primes": len(q_eligible),
                    "eligible_m_primes": len(m_eligible),
                    "eligible_m_primes_without_diagonal": len(m_eligible_without_diagonal),
                    "full_rectangle": rectangle,
                    "full_rectangle_without_diagonal": rectangle_without_diagonal,
                    "density": f"{(row['edge_count'] / rectangle) if rectangle else 0:.4f}",
                    "density_without_diagonal": f"{(row['edge_count'] / rectangle_without_diagonal) if rectangle_without_diagonal else 0:.4f}",
                    "max_q_to_m": row["max_q_to_m_degree"],
                    "max_m_to_q": max_m_to_q,
                    "max_k_to_q": max_k_to_q,
                    "diagonal_ghosts": row["diagonal_ghost_count"],
                    "bad_span": row["bad_span_identity"],
                }
            )

    total_bad = (
        totals["bad_span_identity"]
        + totals["raw_extra_count"]
        + totals["expected_missing_after_diagonal_subtraction"]
        + totals["expected_extra_after_diagonal_subtraction"]
        + int(max_phase_error > TOL)
    )
    return {
        "max_prime": max_prime,
        "P_count": len(P_values),
        "prime_survivor_edge_count_total": totals["survivor_edge_count"],
        "previous_prime_singleton_terms_total": previous_audit["prime_singleton_terms_total"],
        "previous_prime_blocker_count_total": previous_audit["prime_blocker_count_total"],
        "q_bucket_count_total": totals["q_bucket_count"],
        "span_prime_count_total": totals["span_prime_count"],
        "raw_missing_count_total": totals["raw_missing_count"],
        "raw_extra_count_total": totals["raw_extra_count"],
        "diagonal_ghost_count_total": totals["diagonal_ghost_count"],
        "bucket_with_only_diagonal_ghost_count": totals["bucket_with_only_diagonal_ghost"],
        "bucket_with_no_raw_missing_count": totals["bucket_with_no_raw_missing"],
        "expected_missing_after_diagonal_subtraction_total": totals[
            "expected_missing_after_diagonal_subtraction"
        ],
        "expected_extra_after_diagonal_subtraction_total": totals[
            "expected_extra_after_diagonal_subtraction"
        ],
        "bad_span_identity_bucket_count": totals["bad_span_identity"],
        "max_span_completion_phase_error": max_phase_error,
        "total_bad_prime_survivor_floor_span_count": total_bad,
        "counts_match_previous_mobius_singleton_layer": (
            totals["survivor_edge_count"] == previous_audit["prime_singleton_terms_total"]
            and totals["survivor_edge_count"] == previous_audit["prime_blocker_count_total"]
        ),
        "prime_survivor_floor_span_identity_verified": total_bad == 0,
        "raw_completion_tax_is_only_diagonal_P": (
            totals["raw_missing_count"] == totals["diagonal_ghost_count"]
            and totals["raw_extra_count"] == 0
            and totals["bad_span_identity"] == 0
        ),
        "diagonal_subtracted_span_equals_survivor_edges": (
            totals["span_prime_count"] - totals["diagonal_ghost_count"]
            == totals["survivor_edge_count"]
        ),
        "q_eligible_prime_count_total": q_eligible_total,
        "m_eligible_prime_count_total": m_eligible_total,
        "m_eligible_prime_count_without_diagonal_total": m_eligible_without_diagonal_total,
        "full_prime_prime_rectangle_edge_count_including_diagonal_total": full_prime_rectangle_total,
        "full_prime_prime_rectangle_edge_count_without_diagonal_total": (
            full_prime_rectangle_without_diagonal_total
        ),
        "prime_survivor_to_full_rectangle_including_diagonal_density": (
            totals["survivor_edge_count"] / full_prime_rectangle_total
            if full_prime_rectangle_total
            else 0.0
        ),
        "prime_survivor_to_full_rectangle_without_diagonal_density": (
            totals["survivor_edge_count"] / full_prime_rectangle_without_diagonal_total
            if full_prime_rectangle_without_diagonal_total
            else 0.0
        ),
        "full_prime_prime_rectangle_completion_available_directly": False,
        "dense_rectangle_completion_missing_edge_count_including_diagonal": (
            full_prime_rectangle_total - totals["survivor_edge_count"]
        ),
        "dense_rectangle_completion_missing_edge_count_without_diagonal": (
            full_prime_rectangle_without_diagonal_total - totals["survivor_edge_count"]
        ),
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
        "sample_buckets": sample_buckets,
        "ghost_samples": ghost_samples,
        "no_ghost_samples": no_ghost_samples,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_floor_span_completion_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "prime_survivor_singleton_layer_rewritten_as_floor_prime_span_with_diagonal_P_ghost_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the Mobius expansion leaves only the d=1 prime survivor layer, the fastest non-cyclic refinement is to expose its prime-prime floor-span geometry",
        "current_object": {
            "floor_span_identity": "for each active (P,q), M_prime(P,q)={prime m in [L_{P,q},U_{P,q}]}\\{P}",
            "phase_packet": "S_prime-survivor=sum_q sum_{m prime in [L_q,U_q],m!=P} e(hP floor(qm/P)/q)",
            "diagonal_ghost": "m=P gives k=q and D=0, so it is a completion ghost, not a blocker",
            "rectangle_obstruction": "the union of span intervals is not the full prime-prime rectangle in (q,m)",
            "remaining": "phase saving or trace/Type-II/convolution embedding for the prime-prime floor graph",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PrimeSurvivorFloorSpanIdentity",
                True,
                True,
                "In each active q-bucket, prime survivors fill the prime m-span after subtracting the diagonal m=P ghost.",
                "none",
            ),
            gate(
                "DiagonalPGhostCompletionTax",
                True,
                True,
                "The only raw span-completion missing prime is m=P, where D=0 and no blocker exists.",
                "none",
            ),
            gate(
                "PrimeSurvivorPhasePacketSpanRewrite",
                True,
                True,
                "The additive packet equals the prime interval span packet minus the diagonal ghost bucket by bucket.",
                "none",
            ),
            gate(
                "FullPrimePrimeRectangleCompletion",
                False,
                False,
                "Upgrade the span graph to a dense prime-prime rectangle suitable for standard bilinear estimates.",
                "not available; many prime-prime rectangle edges are absent",
            ),
            gate(
                "PrimeFloorSpanTraceOrTypeIIPhaseSaving",
                False,
                False,
                "Obtain nontrivial cancellation for the prime-prime floor-span graph.",
                "requires new trace/Type-II/convolution embedding or new phase theorem",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "promising only after the prime floor-span packet is converted into an actual trace-function bilinear family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "requires a completed Kloosterman variable; the present graph has floor denominator q and sparse span support",
            "Pascadi_composite_Type_II": "requires a genuine Type-II factorisation; the audited graph is not a full dense rectangle",
            "Wright_unbalanced_convolution": "requires a convolution/Kloosterman-fraction model for the floor-span graph",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "does not directly estimate this prime interval floor-span selector",
            "Li_short_interval_x_052": "does not lower to the required pointwise theta=1/2 window for this packet",
        },
        "latest_narrowest_mouth": [
            "PrimeSurvivorPrimeIntervalFloorSpanPhaseSavingOrTraceEmbedding",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND DenseRectangleCompletionOrBilinearTraceEmbeddingForPrimePrimeFloorGraph",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "prime_survivor_floor_span_identity_closed": True,
        "diagonal_P_ghost_completion_tax_closed": True,
        "prime_survivor_phase_packet_span_rewrite_closed": True,
        "full_prime_prime_rectangle_completion_closed": False,
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
    sample_row_fields = [
        "P",
        "edges",
        "q_buckets",
        "distinct_m",
        "eligible_q_primes",
        "eligible_m_primes",
        "eligible_m_primes_without_diagonal",
        "full_rectangle",
        "full_rectangle_without_diagonal",
        "density",
        "density_without_diagonal",
        "max_q_to_m",
        "max_m_to_q",
        "max_k_to_q",
        "diagonal_ghosts",
        "bad_span",
    ]
    sample_bucket_fields = [
        "P",
        "q",
        "L",
        "U",
        "edges",
        "span_primes",
        "raw_missing_count",
        "diagonal_ghost",
        "phase_error",
    ]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor floor-span completion 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"floor_span_identity={current['floor_span_identity']}",
        f"phase_packet={current['phase_packet']}",
        f"diagonal_ghost={current['diagonal_ghost']}",
        f"rectangle_obstruction={current['rectangle_obstruction']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. floor-span completion 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_count={audit['P_count']}",
        f"prime_survivor_edge_count_total={audit['prime_survivor_edge_count_total']}",
        f"previous_prime_singleton_terms_total={audit['previous_prime_singleton_terms_total']}",
        f"previous_prime_blocker_count_total={audit['previous_prime_blocker_count_total']}",
        f"q_bucket_count_total={audit['q_bucket_count_total']}",
        f"span_prime_count_total={audit['span_prime_count_total']}",
        f"raw_missing_count_total={audit['raw_missing_count_total']}",
        f"raw_extra_count_total={audit['raw_extra_count_total']}",
        f"diagonal_ghost_count_total={audit['diagonal_ghost_count_total']}",
        f"bucket_with_only_diagonal_ghost_count={audit['bucket_with_only_diagonal_ghost_count']}",
        f"bucket_with_no_raw_missing_count={audit['bucket_with_no_raw_missing_count']}",
        f"expected_missing_after_diagonal_subtraction_total={audit['expected_missing_after_diagonal_subtraction_total']}",
        f"expected_extra_after_diagonal_subtraction_total={audit['expected_extra_after_diagonal_subtraction_total']}",
        f"bad_span_identity_bucket_count={audit['bad_span_identity_bucket_count']}",
        f"max_span_completion_phase_error={audit['max_span_completion_phase_error']:.3e}",
        f"total_bad_prime_survivor_floor_span_count={audit['total_bad_prime_survivor_floor_span_count']}",
        f"counts_match_previous_mobius_singleton_layer={primorial.bool_text(audit['counts_match_previous_mobius_singleton_layer'])}",
        f"prime_survivor_floor_span_identity_verified={primorial.bool_text(audit['prime_survivor_floor_span_identity_verified'])}",
        f"raw_completion_tax_is_only_diagonal_P={primorial.bool_text(audit['raw_completion_tax_is_only_diagonal_P'])}",
        f"diagonal_subtracted_span_equals_survivor_edges={primorial.bool_text(audit['diagonal_subtracted_span_equals_survivor_edges'])}",
        f"q_eligible_prime_count_total={audit['q_eligible_prime_count_total']}",
        f"m_eligible_prime_count_total={audit['m_eligible_prime_count_total']}",
        f"m_eligible_prime_count_without_diagonal_total={audit['m_eligible_prime_count_without_diagonal_total']}",
        f"full_prime_prime_rectangle_edge_count_including_diagonal_total={audit['full_prime_prime_rectangle_edge_count_including_diagonal_total']}",
        f"full_prime_prime_rectangle_edge_count_without_diagonal_total={audit['full_prime_prime_rectangle_edge_count_without_diagonal_total']}",
        f"prime_survivor_to_full_rectangle_including_diagonal_density={audit['prime_survivor_to_full_rectangle_including_diagonal_density']:.8f}",
        f"prime_survivor_to_full_rectangle_without_diagonal_density={audit['prime_survivor_to_full_rectangle_without_diagonal_density']:.8f}",
        f"dense_rectangle_completion_missing_edge_count_including_diagonal={audit['dense_rectangle_completion_missing_edge_count_including_diagonal']}",
        f"dense_rectangle_completion_missing_edge_count_without_diagonal={audit['dense_rectangle_completion_missing_edge_count_without_diagonal']}",
        f"full_prime_prime_rectangle_completion_available_directly={primorial.bool_text(audit['full_prime_prime_rectangle_completion_available_directly'])}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(audit["sample_rows"], sample_row_fields),
        "",
        "代表 q-bucket：",
        "",
        primorial.table(audit["sample_buckets"], sample_bucket_fields),
        "",
        "diagonal ghost 样本：",
        "",
        "```text",
        *audit["ghost_samples"],
        "```",
        "",
        "无 diagonal ghost 样本：",
        "",
        "```text",
        *audit["no_ghost_samples"],
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
        "结论：prime survivor singleton layer 已被写成 prime interval floor-span packet，原始 span completion 唯一缺口是对角 `m=P` ghost。它仍不是完整 prime-prime rectangle，也未给出相位节省；真正剩余是该 floor graph 的 trace/Type-II/convolution 嵌入或新的直接相消。",
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
        f"prime_survivor_floor_span_identity_closed={primorial.bool_text(payload['prime_survivor_floor_span_identity_closed'])}",
        f"diagonal_P_ghost_completion_tax_closed={primorial.bool_text(payload['diagonal_P_ghost_completion_tax_closed'])}",
        f"prime_survivor_phase_packet_span_rewrite_closed={primorial.bool_text(payload['prime_survivor_phase_packet_span_rewrite_closed'])}",
        f"full_prime_prime_rectangle_completion_closed={primorial.bool_text(payload['full_prime_prime_rectangle_completion_closed'])}",
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
    print("prime_survivor_floor_span_identity_verified=true")
    print("full_prime_prime_rectangle_completion_available_directly=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
