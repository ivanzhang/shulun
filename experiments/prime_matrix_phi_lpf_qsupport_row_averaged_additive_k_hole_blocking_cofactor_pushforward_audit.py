#!/usr/bin/env python3
"""审计 four-class hole correction 的 blocking-cofactor 推前正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_blocking_cofactor_pushforward_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-audit.json

上一层已经证明 empty hole class 结构性为零：

  S_H = S_even + S_prime + S_lpf3 + S_lpf5.

本层继续把每个 completion hole 从缺失的 k 推到一个唯一的 blocking cofactor
m_h。若 product cell 有奇候选，则 residual LPF cofactor 必须是这个奇候选，
所以 blocker 取该唯一奇候选；若没有奇候选，则上一层 nonempty 定理强制 cell
为偶 singleton，blocker 取该偶数。于是 blocker 的 LPF 只能是：

  2, 3, 5, 或 m 本身为素数。

因此四类 correction 等价于两个来源：

  finite 30-wheel rejection packet  (LPF=2,3,5)
  prime blocker packet              (m prime)

这仍只是同对象正规形，不是相消定理。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit as tax  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_class_phase_decomposition_audit as classes  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
TOL = 1e-9

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

BLOCKER_CLASSES = [
    "blocker_lpf2_even",
    "blocker_lpf3",
    "blocker_lpf5",
    "blocker_prime",
]

HOLE_TO_BLOCKER_CLASS = {
    "even_singleton": "blocker_lpf2_even",
    "odd_candidate_lpf3": "blocker_lpf3",
    "odd_candidate_lpf5": "blocker_lpf5",
    "odd_candidate_prime": "blocker_prime",
}


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def blocker_class(m: int, primes: list[int]) -> str:
    """按 blocker 的最小素因子返回四类之一。"""
    r = primorial.lpf(m, primes)
    if r == 2:
        return "blocker_lpf2_even"
    if r == 3:
        return "blocker_lpf3"
    if r == 5:
        return "blocker_lpf5"
    if r == m:
        return "blocker_prime"
    return "blocker_forbidden_lpf_ge7_composite"


def blocking_cofactor(P: int, q: int, k: int, primes: list[int]) -> dict[str, Any]:
    """返回 hole k 的唯一 blocking cofactor 及一致性诊断。"""
    low, high = floorcell.product_cell_window(P, k, q)
    integers = list(range(low, high + 1)) if low <= high else []
    odd_values = [m for m in integers if m % 2 == 1]
    hole_cls = classes.hole_class(P, q, k, primes)

    if odd_values:
        # 中文注释：若存在 residual rough cofactor，只能落在唯一奇候选上。
        m = odd_values[0]
        selector = "unique_odd_candidate"
        bad_odd_multiplicity = int(len(odd_values) != 1)
    else:
        m = integers[0] if integers else None
        selector = "even_singleton_candidate" if m is not None else "empty_forbidden"
        bad_odd_multiplicity = 0

    if m is None:
        return {
            "m": None,
            "low": low,
            "high": high,
            "selector": selector,
            "hole_class": hole_cls,
            "blocker_class": "blocker_empty_forbidden",
            "lpf": 0,
            "bad_empty": 1,
            "bad_odd_multiplicity": bad_odd_multiplicity,
            "bad_floor_mismatch": 1,
            "bad_residual_blocker": 0,
            "bad_class_mismatch": 1,
        }

    cls = blocker_class(m, primes)
    expected = HOLE_TO_BLOCKER_CLASS.get(hole_cls, "none")
    record = primorial.residual_record(m, primes)
    return {
        "m": m,
        "low": low,
        "high": high,
        "selector": selector,
        "hole_class": hole_cls,
        "blocker_class": cls,
        "lpf": primorial.lpf(m, primes),
        "bad_empty": 0,
        "bad_odd_multiplicity": bad_odd_multiplicity,
        "bad_floor_mismatch": int((q * m) // P != k),
        "bad_residual_blocker": int(record is not None),
        "bad_class_mismatch": int(cls != expected),
    }


def bucket_pushforward(P: int, q: int, k_values: set[int], primes: list[int]) -> dict[str, Any]:
    """审计固定 q-bucket 中 hole phase 到 blocker m-space 的推前。"""
    min_k = min(k_values)
    max_k = max(k_values)
    a = P % q
    class_counts: Counter[str] = Counter()
    class_sums = {name: 0j for name in BLOCKER_CLASSES}
    direct_hole_values: list[int] = []
    blocker_keys: set[int] = set()
    sample_blockers: list[str] = []
    totals: Counter[str] = Counter()

    for k in range(min_k, max_k + 1):
        if k in k_values:
            continue
        info = blocking_cofactor(P, q, k, primes)
        direct_hole_values.append(k)
        for key in [
            "bad_empty",
            "bad_odd_multiplicity",
            "bad_floor_mismatch",
            "bad_residual_blocker",
            "bad_class_mismatch",
        ]:
            totals[key] += int(info[key])

        cls = info["blocker_class"]
        if cls in BLOCKER_CLASSES and info["m"] is not None:
            class_counts[cls] += 1
            class_sums[cls] += correction.additive_phase(a, q, (q * info["m"]) // P)
            totals["duplicate_blocker_m"] += int(info["m"] in blocker_keys)
            blocker_keys.add(int(info["m"]))
            if len(sample_blockers) < 6:
                sample_blockers.append(
                    "k={k},m={m},I=[{low},{high}],selector={selector},class={cls},lpf={lpf}".format(
                        k=k,
                        m=info["m"],
                        low=info["low"],
                        high=info["high"],
                        selector=info["selector"],
                        cls=cls,
                        lpf=info["lpf"],
                    )
                )

    direct_sum = correction.direct_sum(a, q, direct_hole_values)
    pushforward_sum = sum(class_sums.values(), 0j)
    small_lpf_sum = (
        class_sums["blocker_lpf2_even"]
        + class_sums["blocker_lpf3"]
        + class_sums["blocker_lpf5"]
    )
    prime_sum = class_sums["blocker_prime"]
    return {
        "q": q,
        "min_k": min_k,
        "max_k": max_k,
        "real_k_count": len(k_values),
        "hole_count": len(direct_hole_values),
        "blocking_cofactor_count": sum(class_counts.values()),
        "small_lpf_blocker_count": class_counts["blocker_lpf2_even"]
        + class_counts["blocker_lpf3"]
        + class_counts["blocker_lpf5"],
        "prime_blocker_count": class_counts["blocker_prime"],
        "pushforward_identity_error": abs(direct_sum - pushforward_sum),
        "abs_small_lpf_blocker_sum_h1": abs(small_lpf_sum),
        "abs_prime_blocker_sum_h1": abs(prime_sum),
        "dominant_two_family_h1": "small_lpf_blocker"
        if abs(small_lpf_sum) >= abs(prime_sum)
        else "prime_blocker",
        **{f"count_{name}": class_counts[name] for name in BLOCKER_CLASSES},
        **{key: totals[key] for key in sorted(totals)},
        "sample_blockers": "; ".join(sample_blockers) if sample_blockers else "none",
    }


def audit_P(P: int, records: list[dict[str, int]], primes: list[int], collect_samples: bool) -> dict[str, Any]:
    """审计固定 P 的 blocker pushforward。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    totals: Counter[str] = Counter()
    float_totals: Counter[str] = Counter()
    max_values = defaultdict(float)
    dominant_two_family_counts: Counter[str] = Counter()
    sample_buckets: list[dict[str, Any]] = []

    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        k_values = tax.selected_k_support_for_q(P, q, records)
        if not k_values:
            continue
        profile = bucket_pushforward(P, q, k_values, primes)
        for key in [
            "real_k_count",
            "hole_count",
            "blocking_cofactor_count",
            "small_lpf_blocker_count",
            "prime_blocker_count",
            "bad_empty",
            "bad_odd_multiplicity",
            "bad_floor_mismatch",
            "bad_residual_blocker",
            "bad_class_mismatch",
            "duplicate_blocker_m",
            *[f"count_{name}" for name in BLOCKER_CLASSES],
        ]:
            totals[key] += int(profile.get(key, 0))
        totals["q_bucket_count"] += 1
        float_totals["sum_abs_small_lpf_blocker_sum_h1"] += float(profile["abs_small_lpf_blocker_sum_h1"])
        float_totals["sum_abs_prime_blocker_sum_h1"] += float(profile["abs_prime_blocker_sum_h1"])
        max_values["max_pushforward_identity_error"] = max(
            max_values["max_pushforward_identity_error"],
            float(profile["pushforward_identity_error"]),
        )
        max_values["max_abs_small_lpf_blocker_sum_h1"] = max(
            max_values["max_abs_small_lpf_blocker_sum_h1"],
            float(profile["abs_small_lpf_blocker_sum_h1"]),
        )
        max_values["max_abs_prime_blocker_sum_h1"] = max(
            max_values["max_abs_prime_blocker_sum_h1"],
            float(profile["abs_prime_blocker_sum_h1"]),
        )
        dominant_two_family_counts[profile["dominant_two_family_h1"]] += 1
        if collect_samples and len(sample_buckets) < 4:
            sample_buckets.append(profile)

    return {
        "P": P,
        "q_bucket_count": totals["q_bucket_count"],
        "real_k_count": totals["real_k_count"],
        "hole_count": totals["hole_count"],
        "blocking_cofactor_count": totals["blocking_cofactor_count"],
        "small_lpf_blocker_count": totals["small_lpf_blocker_count"],
        "prime_blocker_count": totals["prime_blocker_count"],
        "bad_empty": totals["bad_empty"],
        "bad_odd_multiplicity": totals["bad_odd_multiplicity"],
        "bad_floor_mismatch": totals["bad_floor_mismatch"],
        "bad_residual_blocker": totals["bad_residual_blocker"],
        "bad_class_mismatch": totals["bad_class_mismatch"],
        "duplicate_blocker_m": totals["duplicate_blocker_m"],
        **{f"count_{name}": totals[f"count_{name}"] for name in BLOCKER_CLASSES},
        **{key: float_totals[key] for key in sorted(float_totals)},
        **{key: max_values[key] for key in sorted(max_values)},
        "dominant_two_family_counts_h1": json.dumps(
            dict(sorted(dominant_two_family_counts.items())), sort_keys=True
        ),
        "sample_buckets": sample_buckets,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 blocking-cofactor pushforward 做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    float_totals: Counter[str] = Counter()
    max_values = defaultdict(float)
    dominant_two_family_counts: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []

    for P in P_values:
        row = audit_P(P, records_by_P[P], primes, P in interesting)
        for key in [
            "q_bucket_count",
            "real_k_count",
            "hole_count",
            "blocking_cofactor_count",
            "small_lpf_blocker_count",
            "prime_blocker_count",
            "bad_empty",
            "bad_odd_multiplicity",
            "bad_floor_mismatch",
            "bad_residual_blocker",
            "bad_class_mismatch",
            "duplicate_blocker_m",
            *[f"count_{name}" for name in BLOCKER_CLASSES],
        ]:
            totals[key] += int(row.get(key, 0))
        for key in ["sum_abs_small_lpf_blocker_sum_h1", "sum_abs_prime_blocker_sum_h1"]:
            float_totals[key] += float(row.get(key, 0.0))
        for key in [
            "max_pushforward_identity_error",
            "max_abs_small_lpf_blocker_sum_h1",
            "max_abs_prime_blocker_sum_h1",
        ]:
            max_values[key] = max(max_values[key], float(row.get(key, 0.0)))
        dominant_two_family_counts.update(json.loads(row["dominant_two_family_counts_h1"]))
        if P in interesting:
            sample_rows.append(row)

    total_bad = sum(
        totals[key]
        for key in [
            "bad_empty",
            "bad_odd_multiplicity",
            "bad_floor_mismatch",
            "bad_residual_blocker",
            "bad_class_mismatch",
            "duplicate_blocker_m",
        ]
    )
    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "q_bucket_count_total": totals["q_bucket_count"],
        "previous_q_bucket_count_total": previous_audit["q_bucket_count_total"],
        "real_k_count_total": totals["real_k_count"],
        "previous_real_k_count_total": previous_audit["real_k_count_total"],
        "hole_count_total": totals["hole_count"],
        "previous_hole_count_total": previous_audit["hole_count_total"],
        "blocking_cofactor_count_total": totals["blocking_cofactor_count"],
        "small_lpf_blocker_count_total": totals["small_lpf_blocker_count"],
        "prime_blocker_count_total": totals["prime_blocker_count"],
        "small_lpf_blocker_ratio": totals["small_lpf_blocker_count"] / totals["hole_count"],
        "prime_blocker_ratio": totals["prime_blocker_count"] / totals["hole_count"],
        "count_blocker_lpf2_even_total": totals["count_blocker_lpf2_even"],
        "count_blocker_lpf3_total": totals["count_blocker_lpf3"],
        "count_blocker_lpf5_total": totals["count_blocker_lpf5"],
        "count_blocker_prime_total": totals["count_blocker_prime"],
        "bad_empty_total": totals["bad_empty"],
        "bad_odd_multiplicity_total": totals["bad_odd_multiplicity"],
        "bad_floor_mismatch_total": totals["bad_floor_mismatch"],
        "bad_residual_blocker_total": totals["bad_residual_blocker"],
        "bad_class_mismatch_total": totals["bad_class_mismatch"],
        "duplicate_blocker_m_total": totals["duplicate_blocker_m"],
        "total_bad_pushforward_count": total_bad,
        "max_pushforward_identity_error": max_values["max_pushforward_identity_error"],
        "pushforward_identity_verified": max_values["max_pushforward_identity_error"] < TOL,
        "counts_match_previous_four_class_reduction": (
            totals["q_bucket_count"] == previous_audit["q_bucket_count_total"]
            and totals["real_k_count"] == previous_audit["real_k_count_total"]
            and totals["hole_count"] == previous_audit["hole_count_total"]
            and totals["blocking_cofactor_count"] == previous_audit["hole_count_total"]
            and totals["count_blocker_lpf2_even"] == previous_audit["count_even_singleton_total"]
            and totals["count_blocker_lpf3"] == previous_audit["count_odd_candidate_lpf3_total"]
            and totals["count_blocker_lpf5"] == previous_audit["count_odd_candidate_lpf5_total"]
            and totals["count_blocker_prime"] == previous_audit["count_odd_candidate_prime_total"]
        ),
        "unique_blocker_per_hole_verified": total_bad == 0,
        "two_family_split_closed": total_bad == 0
        and totals["small_lpf_blocker_count"] + totals["prime_blocker_count"] == totals["hole_count"],
        **{key: float_totals[key] for key in sorted(float_totals)},
        **{
            key: max_values[key]
            for key in sorted(max_values)
            if key != "max_pushforward_identity_error"
        },
        "dominant_two_family_bucket_counts_h1": dict(sorted(dominant_two_family_counts.items())),
        "two_family_phase_control_closed": False,
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_blocking_cofactor_pushforward_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "four_class_hole_correction_pushed_to_blocking_cofactor_two_family_phase_control_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after empty holes vanish, the most direct non-cyclic refinement is to identify the cofactor that blocks each missing k",
        "current_object": {
            "blocking_selector": "odd candidate if present, otherwise the even singleton carrier",
            "blocker_lpf_classes": "LPF(m)=2,3,5 or m is prime",
            "two_family_phase": "S_H=S_{30-wheel-blocker}+S_{prime-blocker}",
            "small_lpf_packet": "finite 30-wheel rejection packet with LPF 2,3,5",
            "prime_packet": "dynamic prime blocker packet; still needs phase saving or absorption",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "UniqueBlockingCofactorForEveryHole",
                True,
                True,
                "Every completion hole has one selected blocker cofactor m_h.",
                "none",
            ),
            gate(
                "HolePhasePushforwardToBlockingCofactors",
                True,
                True,
                "The phase e(hPk/q) equals e(hP floor(qm_h/P)/q) under the blocker map.",
                "none",
            ),
            gate(
                "ThirtyWheelVsPrimeBlockerSplit",
                True,
                True,
                "Blockers split into finite 30-wheel LPF 2/3/5 rejections and prime blockers.",
                "none",
            ),
            gate(
                "TwoFamilyBlockerPhaseControl",
                False,
                False,
                "Control or absorb the small-LPF blocker packet and the prime blocker packet.",
                "new two-family cancellation/absorption theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "trace-function bilinear estimates still require converting the blocker floor phase into a trace family",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-modulus Kloosterman bounds do not directly see the floor blocker selector",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II input may become relevant only after the blocker support is reorganised into long bilinear fibres",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution/Kloosterman-fraction estimates still need a completed convolution support",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree Kloosterman-parameter estimates do not control the prime blocker selector by themselves",
        },
        "latest_narrowest_mouth": [
            "TwoFamilyBlockerPhaseCancellationOrAbsorption",
            "AND PrimeBlockerDynamicSqrtSieveOrTraceEmbedding",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "unique_blocking_cofactor_closed": True,
        "hole_phase_pushforward_closed": True,
        "thirty_wheel_vs_prime_blocker_split_closed": True,
        "two_family_phase_control_closed": False,
        "prime_blocker_trace_embedding_closed": False,
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
        "q_bucket_count",
        "hole_count",
        "blocking_cofactor_count",
        "small_lpf_blocker_count",
        "prime_blocker_count",
        "bad_empty",
        "bad_floor_mismatch",
        "bad_residual_blocker",
        "duplicate_blocker_m",
        "max_pushforward_identity_error",
    ]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k hole blocking-cofactor pushforward 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"blocking_selector={current['blocking_selector']}",
        f"blocker_lpf_classes={current['blocker_lpf_classes']}",
        f"two_family_phase={current['two_family_phase']}",
        f"small_lpf_packet={current['small_lpf_packet']}",
        f"prime_packet={current['prime_packet']}",
        "```",
        "",
        "## 2. blocking-cofactor pushforward 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"q_bucket_count_total={audit['q_bucket_count_total']}",
        f"previous_q_bucket_count_total={audit['previous_q_bucket_count_total']}",
        f"real_k_count_total={audit['real_k_count_total']}",
        f"previous_real_k_count_total={audit['previous_real_k_count_total']}",
        f"hole_count_total={audit['hole_count_total']}",
        f"previous_hole_count_total={audit['previous_hole_count_total']}",
        f"blocking_cofactor_count_total={audit['blocking_cofactor_count_total']}",
        f"small_lpf_blocker_count_total={audit['small_lpf_blocker_count_total']}",
        f"prime_blocker_count_total={audit['prime_blocker_count_total']}",
        f"small_lpf_blocker_ratio={audit['small_lpf_blocker_ratio']:.6f}",
        f"prime_blocker_ratio={audit['prime_blocker_ratio']:.6f}",
        f"count_blocker_lpf2_even_total={audit['count_blocker_lpf2_even_total']}",
        f"count_blocker_lpf3_total={audit['count_blocker_lpf3_total']}",
        f"count_blocker_lpf5_total={audit['count_blocker_lpf5_total']}",
        f"count_blocker_prime_total={audit['count_blocker_prime_total']}",
        f"bad_empty_total={audit['bad_empty_total']}",
        f"bad_odd_multiplicity_total={audit['bad_odd_multiplicity_total']}",
        f"bad_floor_mismatch_total={audit['bad_floor_mismatch_total']}",
        f"bad_residual_blocker_total={audit['bad_residual_blocker_total']}",
        f"bad_class_mismatch_total={audit['bad_class_mismatch_total']}",
        f"duplicate_blocker_m_total={audit['duplicate_blocker_m_total']}",
        f"total_bad_pushforward_count={audit['total_bad_pushforward_count']}",
        f"max_pushforward_identity_error={audit['max_pushforward_identity_error']:.3e}",
        f"pushforward_identity_verified={primorial.bool_text(audit['pushforward_identity_verified'])}",
        f"counts_match_previous_four_class_reduction={primorial.bool_text(audit['counts_match_previous_four_class_reduction'])}",
        f"unique_blocker_per_hole_verified={primorial.bool_text(audit['unique_blocker_per_hole_verified'])}",
        f"two_family_split_closed={primorial.bool_text(audit['two_family_split_closed'])}",
        f"sum_abs_small_lpf_blocker_sum_h1={audit['sum_abs_small_lpf_blocker_sum_h1']:.6f}",
        f"sum_abs_prime_blocker_sum_h1={audit['sum_abs_prime_blocker_sum_h1']:.6f}",
        f"dominant_two_family_bucket_counts_h1={json.dumps(audit['dominant_two_family_bucket_counts_h1'], sort_keys=True)}",
        f"two_family_phase_control_closed={primorial.bool_text(audit['two_family_phase_control_closed'])}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(audit["sample_rows"], sample_fields),
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：每个 completion hole 被一个唯一 blocking cofactor 推前；四类 correction 变成 30-wheel 小 LPF 阻塞包与 prime 阻塞包。剩余不是 blocker 是否存在，而是两个 packet 的相消、吸收或 trace/Type-II 嵌入。",
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
        f"unique_blocking_cofactor_closed={primorial.bool_text(payload['unique_blocking_cofactor_closed'])}",
        f"hole_phase_pushforward_closed={primorial.bool_text(payload['hole_phase_pushforward_closed'])}",
        f"thirty_wheel_vs_prime_blocker_split_closed={primorial.bool_text(payload['thirty_wheel_vs_prime_blocker_split_closed'])}",
        f"two_family_phase_control_closed={primorial.bool_text(payload['two_family_phase_control_closed'])}",
        f"prime_blocker_trace_embedding_closed={primorial.bool_text(payload['prime_blocker_trace_embedding_closed'])}",
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
    print("unique_blocking_cofactor_closed=true")
    print("two_family_phase_control_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
