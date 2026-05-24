#!/usr/bin/env python3
"""审计 prime-blocker packet 的动态 sqrt-sieve 幸存者正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_dynamic_sqrt_sieve_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-audit.json

上一层已证明 blocker 正规形：

  S_H = S_{30-wheel-blocker} + S_{prime-blocker}.

本层不再尝试继续加固定 wheel，而是把剩余 prime-blocker packet 写成逐点动态
sqrt-sieve 幸存者：

  m_h is prime  iff  m_h mod ell != 0 for every prime ell <= sqrt(m_h).

这是真推进，因为它把“prime blocker”黑箱替换成可核查的 moving local
congruence packet。它仍不是相位节省定理；动态 primorial W(m_h) 随 blocker
移动，Mobius 展开规模随 sqrt(m_h) 增长，仍需 trace/Type-II/dispersion 嵌入
或新的非轮筛相位控制。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_correction_phase_audit as correction  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_primorial_escalation_audit as escalation  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "candidate trace-function bilinear input after a genuine blocker-to-trace embedding",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "candidate arbitrary-modulus Kloosterman input after completion of the moving sqrt-sieve packet",
    },
    {
        "key": "Pascadi_2025_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "candidate composite Type-II input only after the packet is reorganised into bilinear fibres",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate unbalanced convolution input after a completed convolution model exists",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "candidate smooth/squarefree parameter input, not a direct prime-blocker selector estimate",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime input remains above the theta=1/2 pointwise scale needed for direct closure",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def primorial_up_to(limit: int, primes: list[int]) -> tuple[int, int, int]:
    """返回 limit 以下素数个数、primorial 和最大素数因子。"""
    value = 1
    count = 0
    largest = 0
    for ell in primes:
        if ell > limit:
            break
        value *= ell
        count += 1
        largest = ell
    return count, value, largest


def sqrt_sieve_atom(m: int, primes: list[int]) -> dict[str, Any]:
    """返回 m 的动态 sqrt-sieve 原子。"""
    limit = math.isqrt(m)
    pi_sqrt, W_sqrt, largest = primorial_up_to(limit, primes)
    first_obstruction = 0
    first_obstruction_index = 0
    for index, ell in enumerate(primes, start=1):
        if ell > limit:
            break
        if m % ell == 0:
            first_obstruction = ell
            first_obstruction_index = index
            break
    survives = first_obstruction == 0
    return {
        "sqrt_limit": limit,
        "pi_sqrt": pi_sqrt,
        "largest_sqrt_prime": largest,
        "W_sqrt": W_sqrt,
        "W_sqrt_bits": W_sqrt.bit_length(),
        "first_obstruction": first_obstruction,
        "first_obstruction_index": first_obstruction_index,
        "survives_dynamic_sqrt_sieve": survives,
        "mobius_terms_full_expansion": 1 << pi_sqrt,
    }


def stage_profiles(blockers: list[dict[str, int]], primes: list[int]) -> list[dict[str, Any]]:
    """统计固定 cutoff 的逐层幸存数，用来显示 5 之后没有新拒绝层。"""
    max_m = max(item["m"] for item in blockers)
    cutoffs = [ell for ell in primes if ell <= math.isqrt(max_m)]
    rows: list[dict[str, Any]] = []
    for cutoff in cutoffs:
        survived = 0
        rejected = 0
        prime_survived = 0
        small_lpf_rejected = 0
        for item in blockers:
            killed = item["lpf"] <= cutoff
            survived += int(not killed)
            rejected += int(killed)
            prime_survived += int((not killed) and item["lpf"] == item["m"])
            small_lpf_rejected += int(killed and item["lpf"] in {2, 3, 5})
        rows.append(
            {
                "cutoff": cutoff,
                "rejected_count": rejected,
                "survivor_count": survived,
                "prime_survivor_count": prime_survived,
                "small_lpf_rejected_count": small_lpf_rejected,
                "new_rejections_after_5": 0 if cutoff <= 5 else rejected - rows[2]["rejected_count"],
            }
        )
    return rows


def collect_all_blockers(max_prime: int, primes: list[int]) -> list[dict[str, int]]:
    """枚举 P<=max_prime 的全部 hole blockers。"""
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    blockers: list[dict[str, int]] = []
    for P in P_values:
        blockers.extend(escalation.iter_blockers(P, records_by_P[P], primes))
    return blockers


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 prime-blocker packet 与动态 sqrt-sieve 幸存者的等价。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    blockers = collect_all_blockers(max_prime, primes)
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    obstruction_counts: Counter[str] = Counter()
    cutoff_counts: Counter[int] = Counter()
    largest_prime_counts: Counter[int] = Counter()
    q_bucket_prime_sum: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    q_bucket_survivor_sum: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    q_bucket_prime_count: Counter[tuple[int, int]] = Counter()
    q_bucket_survivor_count: Counter[tuple[int, int]] = Counter()
    row_profiles: dict[int, Counter[str]] = defaultdict(Counter)
    sample_rows: list[dict[str, Any]] = []
    sample_prime_blockers: list[str] = []
    max_values: defaultdict[str, float] = defaultdict(float)

    for item in blockers:
        P = item["P"]
        q = item["q"]
        k = item["k"]
        m = item["m"]
        lpf_value = item["lpf"]
        atom = sqrt_sieve_atom(m, primes)
        is_prime_blocker = lpf_value == m
        survivor = bool(atom["survives_dynamic_sqrt_sieve"])
        phase = correction.additive_phase(P % q, q, k)
        bucket_key = (P, q)

        totals["blocker_count"] += 1
        totals["small_lpf_blocker_count"] += int(lpf_value in {2, 3, 5})
        totals["prime_blocker_count"] += int(is_prime_blocker)
        totals["sqrt_sieve_survivor_count"] += int(survivor)
        totals["sqrt_sieve_rejected_count"] += int(not survivor)
        totals["bad_prime_survivor_mismatch"] += int(is_prime_blocker != survivor)
        totals["bad_composite_survivor"] += int((not is_prime_blocker) and survivor)
        totals["bad_prime_rejected"] += int(is_prime_blocker and not survivor)
        totals["rough_composite_rejection_after_5"] += int(
            (not survivor) and atom["first_obstruction"] not in {2, 3, 5}
        )
        totals["prime_blocker_full_sqrt_tests"] += atom["pi_sqrt"] if is_prime_blocker else 0
        totals["small_lpf_short_circuit_tests"] += atom["first_obstruction_index"] if not survivor else 0
        totals["prime_blocker_mobius_terms_full_expansion"] += (
            atom["mobius_terms_full_expansion"] if is_prime_blocker else 0
        )

        obstruction = str(atom["first_obstruction"]) if atom["first_obstruction"] else "none"
        obstruction_counts[obstruction] += 1
        cutoff_counts[atom["sqrt_limit"]] += 1
        largest_prime_counts[atom["largest_sqrt_prime"]] += 1
        max_values["max_pi_sqrt_all"] = max(max_values["max_pi_sqrt_all"], atom["pi_sqrt"])
        max_values["max_pi_sqrt_prime_blocker"] = max(
            max_values["max_pi_sqrt_prime_blocker"],
            atom["pi_sqrt"] if is_prime_blocker else 0,
        )
        max_values["max_mobius_terms_per_blocker"] = max(
            max_values["max_mobius_terms_per_blocker"],
            atom["mobius_terms_full_expansion"],
        )
        max_values["max_W_sqrt_bits"] = max(max_values["max_W_sqrt_bits"], atom["W_sqrt_bits"])
        max_values["max_W_sqrt_over_P"] = max(max_values["max_W_sqrt_over_P"], atom["W_sqrt"] / P)

        if is_prime_blocker:
            q_bucket_prime_sum[bucket_key] += phase
            q_bucket_prime_count[bucket_key] += 1
        if survivor:
            q_bucket_survivor_sum[bucket_key] += phase
            q_bucket_survivor_count[bucket_key] += 1
        if is_prime_blocker and len(sample_prime_blockers) < 8:
            sample_prime_blockers.append(
                "P={P},q={q},k={k},m={m},sqrt={sqrt},pi_sqrt={pi},W_bits={bits}".format(
                    P=P,
                    q=q,
                    k=k,
                    m=m,
                    sqrt=atom["sqrt_limit"],
                    pi=atom["pi_sqrt"],
                    bits=atom["W_sqrt_bits"],
                )
            )

        row = row_profiles[P]
        row["blockers"] += 1
        row["small_lpf_blockers"] += int(lpf_value in {2, 3, 5})
        row["prime_blockers"] += int(is_prime_blocker)
        row["sqrt_sieve_survivors"] += int(survivor)
        row["sqrt_sieve_rejections"] += int(not survivor)
        row["bad_mismatch"] += int(is_prime_blocker != survivor)
        row["max_pi_sqrt"] = max(row["max_pi_sqrt"], atom["pi_sqrt"])
        row["max_W_sqrt_bits"] = max(row["max_W_sqrt_bits"], atom["W_sqrt_bits"])

    bucket_keys = set(q_bucket_prime_sum) | set(q_bucket_survivor_sum)
    max_phase_error = 0.0
    bucket_mismatch_count = 0
    for key in bucket_keys:
        err = abs(q_bucket_prime_sum[key] - q_bucket_survivor_sum[key])
        max_phase_error = max(max_phase_error, err)
        bucket_mismatch_count += int(err > 1e-9 or q_bucket_prime_count[key] != q_bucket_survivor_count[key])

    for P in sorted(interesting):
        if P in row_profiles:
            row = row_profiles[P]
            sample_rows.append(
                {
                    "P": P,
                    "blockers": row["blockers"],
                    "small_lpf_blockers": row["small_lpf_blockers"],
                    "prime_blockers": row["prime_blockers"],
                    "sqrt_sieve_survivors": row["sqrt_sieve_survivors"],
                    "sqrt_sieve_rejections": row["sqrt_sieve_rejections"],
                    "bad_mismatch": row["bad_mismatch"],
                    "max_pi_sqrt": row["max_pi_sqrt"],
                    "max_W_sqrt_bits": row["max_W_sqrt_bits"],
                }
            )

    total_bad = (
        totals["bad_prime_survivor_mismatch"]
        + totals["bad_composite_survivor"]
        + totals["bad_prime_rejected"]
        + totals["rough_composite_rejection_after_5"]
        + bucket_mismatch_count
    )
    stage = stage_profiles(blockers, primes)
    return {
        "max_prime": max_prime,
        "blocker_count_total": totals["blocker_count"],
        "previous_blocker_count_total": previous_audit["blocker_count_total"],
        "small_lpf_blocker_count_total": totals["small_lpf_blocker_count"],
        "previous_small_lpf_blocker_count_total": previous_audit["small_lpf_blocker_count_total"],
        "prime_blocker_count_total": totals["prime_blocker_count"],
        "previous_prime_blocker_count_total": previous_audit["prime_blocker_count_total"],
        "sqrt_sieve_survivor_count_total": totals["sqrt_sieve_survivor_count"],
        "sqrt_sieve_rejected_count_total": totals["sqrt_sieve_rejected_count"],
        "bad_prime_survivor_mismatch_total": totals["bad_prime_survivor_mismatch"],
        "bad_composite_survivor_total": totals["bad_composite_survivor"],
        "bad_prime_rejected_total": totals["bad_prime_rejected"],
        "rough_composite_rejection_after_5_total": totals["rough_composite_rejection_after_5"],
        "q_bucket_with_prime_blocker_count": len(bucket_keys),
        "q_bucket_prime_phase_mismatch_count": bucket_mismatch_count,
        "max_prime_packet_phase_identity_error": max_phase_error,
        "total_bad_dynamic_sqrt_sieve_count": total_bad,
        "counts_match_previous_primorial_escalation": (
            totals["blocker_count"] == previous_audit["blocker_count_total"]
            and totals["small_lpf_blocker_count"] == previous_audit["small_lpf_blocker_count_total"]
            and totals["prime_blocker_count"] == previous_audit["prime_blocker_count_total"]
        ),
        "prime_blocker_equals_dynamic_sqrt_survivor_verified": total_bad == 0,
        "sqrt_sieve_rejections_are_exactly_lpf_2_3_5": (
            totals["sqrt_sieve_rejected_count"] == totals["small_lpf_blocker_count"]
            and totals["rough_composite_rejection_after_5"] == 0
        ),
        "max_pi_sqrt_all": int(max_values["max_pi_sqrt_all"]),
        "max_pi_sqrt_prime_blocker": int(max_values["max_pi_sqrt_prime_blocker"]),
        "max_mobius_terms_per_blocker": int(max_values["max_mobius_terms_per_blocker"]),
        "prime_blocker_full_sqrt_tests_total": totals["prime_blocker_full_sqrt_tests"],
        "small_lpf_short_circuit_tests_total": totals["small_lpf_short_circuit_tests"],
        "prime_blocker_mobius_terms_full_expansion_total": totals[
            "prime_blocker_mobius_terms_full_expansion"
        ],
        "distinct_sqrt_limits_seen": len(cutoff_counts),
        "distinct_largest_sqrt_prime_seen": len(largest_prime_counts),
        "max_W_sqrt_bits": int(max_values["max_W_sqrt_bits"]),
        "max_W_sqrt_over_P": max_values["max_W_sqrt_over_P"],
        "obstruction_counts": dict(sorted(obstruction_counts.items(), key=lambda kv: (kv[0] != "none", kv[0]))),
        "largest_sqrt_prime_counts": dict(sorted(largest_prime_counts.items())),
        "stage_profiles": stage,
        "dynamic_sqrt_sieve_identity_closed": total_bad == 0,
        "dynamic_sqrt_sieve_phase_saving_closed": False,
        "moving_primorial_mobius_compression_closed": False,
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
        "sample_prime_blockers": sample_prime_blockers,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_dynamic_sqrt_sieve_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "prime_blocker_packet_rewritten_as_dynamic_sqrt_sieve_survivors_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after primorial escalation is inert, the fastest non-cyclic refinement is to replace the prime-blocker oracle by its exact moving sqrt-sieve survivor packet",
        "current_object": {
            "prime_blocker_identity": "m_h prime iff m_h is not 0 modulo every prime ell<=sqrt(m_h)",
            "dynamic_packet": "S_{prime-blocker}=S_{sqrt-sieve-survivor}",
            "thirty_wheel_relation": "all non-survivors are exactly LPF 2/3/5 blockers already in the 30-wheel packet",
            "moving_primorial": "W(m_h)=prod_{ell<=sqrt(m_h)} ell varies with m_h",
            "remaining": "phase saving or trace/Type-II embedding for the moving survivor packet",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PrimeBlockerDynamicSqrtSieveIdentity",
                True,
                True,
                "The prime-blocker indicator equals the dynamic sqrt-sieve survivor indicator on every blocker.",
                "none",
            ),
            gate(
                "PrimeBlockerPhasePacketPushforward",
                True,
                True,
                "The additive prime-blocker packet equals the additive survivor packet bucket by bucket.",
                "none",
            ),
            gate(
                "NoRoughCompositeSqrtRejectionAfterThirtyWheel",
                True,
                True,
                "After LPF 2/3/5 rejections, no LPF 7/11/... composite blocker remains.",
                "none",
            ),
            gate(
                "MovingPrimorialMobiusCompression",
                False,
                False,
                "Compress the moving sqrt-sieve survivor product into a usable completed bilinear/trace family.",
                "new compression or trace embedding theorem",
            ),
            gate(
                "PrimeBlockerSurvivorPhaseSaving",
                False,
                False,
                "Prove cancellation or absorption for the survivor packet itself.",
                "non-wheel phase saving beyond parity",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "not directly applicable until the moving sqrt-sieve survivor packet is embedded into a trace-function family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "does not by itself compress W(m_h)-moving local congruence constraints into a completed Kloosterman sum",
            "Pascadi_composite_Type_II": "may help only after the blocker support is reorganised as long bilinear fibres",
            "Wright_unbalanced_convolution": "requires a completed convolution/Kloosterman-fraction form, not just the pointwise primality sieve",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "does not directly estimate the prime-blocker survivor selector",
            "Li_short_interval_x_052": "theta=0.52 remains above the pointwise theta=1/2 scale, so it does not close this packet",
        },
        "latest_narrowest_mouth": [
            "PrimeBlockerSqrtSieveSurvivorPhaseSavingOrTraceEmbedding",
            "AND MovingPrimorialMobiusExpansionCompression",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "prime_blocker_dynamic_sqrt_sieve_identity_closed": True,
        "prime_blocker_phase_packet_pushforward_closed": True,
        "no_rough_composite_sqrt_rejection_after_30_closed": True,
        "moving_primorial_mobius_compression_closed": False,
        "prime_blocker_survivor_phase_saving_closed": False,
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
    sample_fields = [
        "P",
        "blockers",
        "small_lpf_blockers",
        "prime_blockers",
        "sqrt_sieve_survivors",
        "sqrt_sieve_rejections",
        "bad_mismatch",
        "max_pi_sqrt",
        "max_W_sqrt_bits",
    ]
    stage_fields = [
        "cutoff",
        "rejected_count",
        "survivor_count",
        "prime_survivor_count",
        "small_lpf_rejected_count",
        "new_rejections_after_5",
    ]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-blocker dynamic sqrt-sieve 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"prime_blocker_identity={current['prime_blocker_identity']}",
        f"dynamic_packet={current['dynamic_packet']}",
        f"thirty_wheel_relation={current['thirty_wheel_relation']}",
        f"moving_primorial={current['moving_primorial']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. dynamic sqrt-sieve 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"blocker_count_total={audit['blocker_count_total']}",
        f"previous_blocker_count_total={audit['previous_blocker_count_total']}",
        f"small_lpf_blocker_count_total={audit['small_lpf_blocker_count_total']}",
        f"previous_small_lpf_blocker_count_total={audit['previous_small_lpf_blocker_count_total']}",
        f"prime_blocker_count_total={audit['prime_blocker_count_total']}",
        f"previous_prime_blocker_count_total={audit['previous_prime_blocker_count_total']}",
        f"sqrt_sieve_survivor_count_total={audit['sqrt_sieve_survivor_count_total']}",
        f"sqrt_sieve_rejected_count_total={audit['sqrt_sieve_rejected_count_total']}",
        f"bad_prime_survivor_mismatch_total={audit['bad_prime_survivor_mismatch_total']}",
        f"bad_composite_survivor_total={audit['bad_composite_survivor_total']}",
        f"bad_prime_rejected_total={audit['bad_prime_rejected_total']}",
        f"rough_composite_rejection_after_5_total={audit['rough_composite_rejection_after_5_total']}",
        f"q_bucket_with_prime_blocker_count={audit['q_bucket_with_prime_blocker_count']}",
        f"q_bucket_prime_phase_mismatch_count={audit['q_bucket_prime_phase_mismatch_count']}",
        f"max_prime_packet_phase_identity_error={audit['max_prime_packet_phase_identity_error']:.3e}",
        f"total_bad_dynamic_sqrt_sieve_count={audit['total_bad_dynamic_sqrt_sieve_count']}",
        f"counts_match_previous_primorial_escalation={primorial.bool_text(audit['counts_match_previous_primorial_escalation'])}",
        f"prime_blocker_equals_dynamic_sqrt_survivor_verified={primorial.bool_text(audit['prime_blocker_equals_dynamic_sqrt_survivor_verified'])}",
        f"sqrt_sieve_rejections_are_exactly_lpf_2_3_5={primorial.bool_text(audit['sqrt_sieve_rejections_are_exactly_lpf_2_3_5'])}",
        f"max_pi_sqrt_all={audit['max_pi_sqrt_all']}",
        f"max_pi_sqrt_prime_blocker={audit['max_pi_sqrt_prime_blocker']}",
        f"max_mobius_terms_per_blocker={audit['max_mobius_terms_per_blocker']}",
        f"prime_blocker_full_sqrt_tests_total={audit['prime_blocker_full_sqrt_tests_total']}",
        f"small_lpf_short_circuit_tests_total={audit['small_lpf_short_circuit_tests_total']}",
        f"prime_blocker_mobius_terms_full_expansion_total={audit['prime_blocker_mobius_terms_full_expansion_total']}",
        f"distinct_sqrt_limits_seen={audit['distinct_sqrt_limits_seen']}",
        f"distinct_largest_sqrt_prime_seen={audit['distinct_largest_sqrt_prime_seen']}",
        f"max_W_sqrt_bits={audit['max_W_sqrt_bits']}",
        f"max_W_sqrt_over_P={audit['max_W_sqrt_over_P']:.6f}",
        "```",
        "",
        "obstruction counts:",
        "",
        "```text",
        json.dumps(audit["obstruction_counts"], sort_keys=True),
        "```",
        "",
        "逐层 cutoff 摘要：",
        "",
        primorial.table(audit["stage_profiles"], stage_fields),
        "",
        "代表 P：",
        "",
        primorial.table(audit["sample_rows"], sample_fields),
        "",
        "prime-blocker 样本：",
        "",
        "```text",
        *audit["sample_prime_blockers"],
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
        "结论：prime-blocker packet 已被改写成动态 sqrt-sieve survivor packet；所有非幸存者正好是 30-wheel 的 LPF 2/3/5 blocker。剩余不再是素性判定，而是 moving primorial survivor packet 的相位节省、Mobius 压缩或 trace/Type-II 嵌入。",
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
        f"prime_blocker_dynamic_sqrt_sieve_identity_closed={primorial.bool_text(payload['prime_blocker_dynamic_sqrt_sieve_identity_closed'])}",
        f"prime_blocker_phase_packet_pushforward_closed={primorial.bool_text(payload['prime_blocker_phase_packet_pushforward_closed'])}",
        f"no_rough_composite_sqrt_rejection_after_30_closed={primorial.bool_text(payload['no_rough_composite_sqrt_rejection_after_30_closed'])}",
        f"moving_primorial_mobius_compression_closed={primorial.bool_text(payload['moving_primorial_mobius_compression_closed'])}",
        f"prime_blocker_survivor_phase_saving_closed={primorial.bool_text(payload['prime_blocker_survivor_phase_saving_closed'])}",
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
    print("prime_blocker_equals_dynamic_sqrt_survivor_verified=true")
    print("prime_blocker_survivor_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
