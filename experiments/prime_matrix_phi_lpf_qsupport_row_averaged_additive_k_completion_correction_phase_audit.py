#!/usr/bin/env python3
"""审计 additive-k 完整区间补全后的 correction 相位恒等式。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_correction_phase_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-audit.json

上一层证明 completion tax：把真实 sparse 支撑 K_{P,q} 补成完整区间
C_{P,q} 会加入非同对象 holes H_{P,q}。本层继续下钻到相位层：

  S_K(h) = sum_{k in K} e(hPk/q)
         = sum_{k in C} e(hPk/q) - sum_{k in H} e(hPk/q).

完整区间项是普通几何和；但 hole correction 不是自动小量。有限审计只验证
恒等式和量级诊断，不把它提升为 Phi-LPF 目标证明。
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit as floorcell  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit as tax  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
TAU = 2.0 * math.pi
TOL = 1e-9

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def additive_phase(a: int, q: int, k: int) -> complex:
    """返回 e(a*k/q)。"""
    return cmath.exp(1j * TAU * ((a * k) % q) / q)


def direct_sum(a: int, q: int, k_values: list[int]) -> complex:
    """直接求 k 支撑上的加性角色和。"""
    return sum((additive_phase(a, q, k) for k in k_values), 0j)


def geometric_sum(a: int, q: int, min_k: int, max_k: int) -> complex:
    """返回完整连续 k 区间上的几何和公式。"""
    length = max_k - min_k + 1
    if length <= 0:
        return 0j
    ratio = cmath.exp(1j * TAU * (a % q) / q)
    first = additive_phase(a, q, min_k)
    return first * (1 - ratio**length) / (1 - ratio)


def hole_label(P: int, q: int, k: int, primes: list[int]) -> str:
    """分类 completion hole 的来源。"""
    low, high = floorcell.product_cell_window(P, k, q)
    m_odd, odd_count = primorial.unique_odd_candidate(low, high)
    if odd_count > 1:
        return "bad_odd_count_over_one"
    if m_odd is None:
        return "no_odd_candidate"
    record = primorial.residual_record(m_odd, primes)
    if record is not None:
        return "residual_candidate"
    return tax.classify_nonresidual_odd(m_odd, primes)


def phase_profile_for_bucket(P: int, q: int, k_values: set[int], primes: list[int]) -> dict[str, Any]:
    """计算一个 q-bucket 的 sparse/complete/correction 相位和。"""
    min_k = min(k_values)
    max_k = max(k_values)
    complete_values = list(range(min_k, max_k + 1))
    hole_values = [k for k in complete_values if k not in k_values]
    a = P % q

    sparse_sum = direct_sum(a, q, sorted(k_values))
    complete_direct = direct_sum(a, q, complete_values)
    complete_formula = geometric_sum(a, q, min_k, max_k)
    hole_sum = direct_sum(a, q, hole_values)
    correction_identity_error = abs(sparse_sum - (complete_direct - hole_sum))
    geometric_formula_error = abs(complete_direct - complete_formula)

    label_counts: Counter[str] = Counter()
    label_abs_sums: dict[str, complex] = {}
    for k in hole_values:
        label = hole_label(P, q, k, primes)
        label_counts[label] += 1
        label_abs_sums[label] = label_abs_sums.get(label, 0j) + additive_phase(a, q, k)

    abs_complete = abs(complete_formula)
    abs_hole = abs(hole_sum)
    abs_sparse = abs(sparse_sum)
    ratio = abs_hole / abs_complete if abs_complete > TOL else 0.0

    return {
        "q": q,
        "min_k": min_k,
        "max_k": max_k,
        "real_k_count": len(k_values),
        "complete_span": len(complete_values),
        "hole_count": len(hole_values),
        "abs_sparse_sum_h1": abs_sparse,
        "abs_complete_geometric_sum_h1": abs_complete,
        "abs_hole_correction_sum_h1": abs_hole,
        "hole_over_complete_abs_ratio_h1": ratio,
        "hole_abs_gt_complete_abs_h1": abs_hole > abs_complete + TOL,
        "sparse_abs_gt_complete_abs_h1": abs_sparse > abs_complete + TOL,
        "complete_near_zero_with_nonzero_hole_h1": abs_complete <= TOL and abs_hole > TOL,
        "geometric_formula_error": geometric_formula_error,
        "correction_identity_error": correction_identity_error,
        "hole_label_counts": dict(sorted(label_counts.items())),
        "hole_label_abs_sums_h1": {
            label: abs(value) for label, value in sorted(label_abs_sums.items())
        },
    }


def audit_P(P: int, records: list[dict[str, int]], primes: list[int], collect_samples: bool) -> dict[str, Any]:
    """审计固定 P 下全部 q-bucket 的 completion correction 相位。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    totals: Counter[str] = Counter()
    sums: Counter[str] = Counter()
    max_values = {
        "max_abs_sparse_sum_h1": 0.0,
        "max_abs_complete_geometric_sum_h1": 0.0,
        "max_abs_hole_correction_sum_h1": 0.0,
        "max_hole_over_complete_abs_ratio_h1": 0.0,
        "max_geometric_formula_error": 0.0,
        "max_correction_identity_error": 0.0,
    }
    sample_buckets: list[dict[str, Any]] = []
    first_hole_dominates = "none"

    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        k_values = tax.selected_k_support_for_q(P, q, records)
        if not k_values:
            continue
        profile = phase_profile_for_bucket(P, q, k_values, primes)
        totals["q_bucket_count"] += 1
        totals["real_k_count"] += profile["real_k_count"]
        totals["complete_span"] += profile["complete_span"]
        totals["hole_count"] += profile["hole_count"]
        totals["hole_abs_gt_complete_abs_h1"] += int(profile["hole_abs_gt_complete_abs_h1"])
        totals["sparse_abs_gt_complete_abs_h1"] += int(profile["sparse_abs_gt_complete_abs_h1"])
        totals["complete_near_zero_with_nonzero_hole_h1"] += int(
            profile["complete_near_zero_with_nonzero_hole_h1"]
        )
        for key, value in profile["hole_label_counts"].items():
            totals[f"hole_label_{key}"] += int(value)
        sums["sum_abs_sparse_sum_h1"] += profile["abs_sparse_sum_h1"]
        sums["sum_abs_complete_geometric_sum_h1"] += profile["abs_complete_geometric_sum_h1"]
        sums["sum_abs_hole_correction_sum_h1"] += profile["abs_hole_correction_sum_h1"]
        for key in max_values:
            source_key = key.removeprefix("max_")
            max_values[key] = max(max_values[key], float(profile[source_key]))
        if first_hole_dominates == "none" and profile["hole_abs_gt_complete_abs_h1"]:
            first_hole_dominates = (
                f"P={P},q={q},holes={profile['hole_count']},"
                f"abs_complete={profile['abs_complete_geometric_sum_h1']:.6f},"
                f"abs_hole={profile['abs_hole_correction_sum_h1']:.6f},"
                f"abs_sparse={profile['abs_sparse_sum_h1']:.6f}"
            )
        if collect_samples and len(sample_buckets) < 4:
            sample = dict(profile)
            sample["hole_label_counts"] = json.dumps(sample["hole_label_counts"], sort_keys=True)
            sample["hole_label_abs_sums_h1"] = json.dumps(
                {k: round(v, 6) for k, v in profile["hole_label_abs_sums_h1"].items()},
                sort_keys=True,
            )
            sample_buckets.append(sample)

    return {
        "P": P,
        "q_bucket_count": totals["q_bucket_count"],
        "real_k_count": totals["real_k_count"],
        "complete_span": totals["complete_span"],
        "hole_count": totals["hole_count"],
        "sum_abs_sparse_sum_h1": sums["sum_abs_sparse_sum_h1"],
        "sum_abs_complete_geometric_sum_h1": sums["sum_abs_complete_geometric_sum_h1"],
        "sum_abs_hole_correction_sum_h1": sums["sum_abs_hole_correction_sum_h1"],
        "hole_abs_gt_complete_abs_bucket_count_h1": totals["hole_abs_gt_complete_abs_h1"],
        "sparse_abs_gt_complete_abs_bucket_count_h1": totals["sparse_abs_gt_complete_abs_h1"],
        "complete_near_zero_with_nonzero_hole_bucket_count_h1": totals[
            "complete_near_zero_with_nonzero_hole_h1"
        ],
        "hole_label_no_odd_candidate": totals["hole_label_no_odd_candidate"],
        "hole_label_odd_candidate_prime": totals["hole_label_odd_candidate_prime"],
        "hole_label_odd_candidate_small_lpf_3": totals["hole_label_odd_candidate_small_lpf_3"],
        "hole_label_odd_candidate_small_lpf_5": totals["hole_label_odd_candidate_small_lpf_5"],
        "hole_label_residual_candidate": totals["hole_label_residual_candidate"],
        "max_abs_sparse_sum_h1": max_values["max_abs_sparse_sum_h1"],
        "max_abs_complete_geometric_sum_h1": max_values["max_abs_complete_geometric_sum_h1"],
        "max_abs_hole_correction_sum_h1": max_values["max_abs_hole_correction_sum_h1"],
        "max_hole_over_complete_abs_ratio_h1": max_values["max_hole_over_complete_abs_ratio_h1"],
        "max_geometric_formula_error": max_values["max_geometric_formula_error"],
        "max_correction_identity_error": max_values["max_correction_identity_error"],
        "first_hole_dominates_complete": first_hole_dominates,
        "sample_buckets": sample_buckets,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 correction 相位恒等式做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    previous = json.loads(
        (DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-audit.json").read_text()
    )
    previous_audit = previous["finite_audit"]
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    float_sums: Counter[str] = Counter()
    max_values = {
        "max_abs_sparse_sum_h1": 0.0,
        "max_abs_complete_geometric_sum_h1": 0.0,
        "max_abs_hole_correction_sum_h1": 0.0,
        "max_hole_over_complete_abs_ratio_h1": 0.0,
        "max_geometric_formula_error": 0.0,
        "max_correction_identity_error": 0.0,
    }
    sample_rows: list[dict[str, Any]] = []
    first_hole_dominates = "none"

    for P in P_values:
        row = audit_P(P, records_by_P[P], primes, P in interesting)
        for key in [
            "q_bucket_count",
            "real_k_count",
            "complete_span",
            "hole_count",
            "hole_abs_gt_complete_abs_bucket_count_h1",
            "sparse_abs_gt_complete_abs_bucket_count_h1",
            "complete_near_zero_with_nonzero_hole_bucket_count_h1",
            "hole_label_no_odd_candidate",
            "hole_label_odd_candidate_prime",
            "hole_label_odd_candidate_small_lpf_3",
            "hole_label_odd_candidate_small_lpf_5",
            "hole_label_residual_candidate",
        ]:
            totals[key] += int(row[key])
        for key in [
            "sum_abs_sparse_sum_h1",
            "sum_abs_complete_geometric_sum_h1",
            "sum_abs_hole_correction_sum_h1",
        ]:
            float_sums[key] += float(row[key])
        for key in max_values:
            max_values[key] = max(max_values[key], float(row[key]))
        if first_hole_dominates == "none" and row["first_hole_dominates_complete"] != "none":
            first_hole_dominates = row["first_hole_dominates_complete"]
        if P in interesting:
            sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "q_bucket_count_total": totals["q_bucket_count"],
        "previous_selected_q_bucket_count_total": previous_audit["selected_q_bucket_count_total"],
        "real_k_count_total": totals["real_k_count"],
        "previous_real_k_count_total": previous_audit["real_k_count_total"],
        "complete_span_total": totals["complete_span"],
        "previous_completion_span_total": previous_audit["completion_span_total"],
        "hole_count_total": totals["hole_count"],
        "previous_completion_holes_total": previous_audit["completion_holes_total"],
        "phase_identity_counts_match_completion_tax": (
            totals["q_bucket_count"] == previous_audit["selected_q_bucket_count_total"]
            and totals["real_k_count"] == previous_audit["real_k_count_total"]
            and totals["complete_span"] == previous_audit["completion_span_total"]
            and totals["hole_count"] == previous_audit["completion_holes_total"]
        ),
        "geometric_formula_verified": max_values["max_geometric_formula_error"] < TOL,
        "correction_phase_identity_verified": max_values["max_correction_identity_error"] < TOL,
        "max_geometric_formula_error": max_values["max_geometric_formula_error"],
        "max_correction_identity_error": max_values["max_correction_identity_error"],
        "sum_abs_sparse_sum_h1": float_sums["sum_abs_sparse_sum_h1"],
        "sum_abs_complete_geometric_sum_h1": float_sums["sum_abs_complete_geometric_sum_h1"],
        "sum_abs_hole_correction_sum_h1": float_sums["sum_abs_hole_correction_sum_h1"],
        "max_abs_sparse_sum_h1": max_values["max_abs_sparse_sum_h1"],
        "max_abs_complete_geometric_sum_h1": max_values["max_abs_complete_geometric_sum_h1"],
        "max_abs_hole_correction_sum_h1": max_values["max_abs_hole_correction_sum_h1"],
        "max_hole_over_complete_abs_ratio_h1": max_values["max_hole_over_complete_abs_ratio_h1"],
        "hole_abs_gt_complete_abs_bucket_count_h1": totals["hole_abs_gt_complete_abs_bucket_count_h1"],
        "sparse_abs_gt_complete_abs_bucket_count_h1": totals["sparse_abs_gt_complete_abs_bucket_count_h1"],
        "complete_near_zero_with_nonzero_hole_bucket_count_h1": totals[
            "complete_near_zero_with_nonzero_hole_bucket_count_h1"
        ],
        "hole_label_no_odd_candidate_total": totals["hole_label_no_odd_candidate"],
        "hole_label_odd_candidate_prime_total": totals["hole_label_odd_candidate_prime"],
        "hole_label_odd_candidate_small_lpf_3_total": totals["hole_label_odd_candidate_small_lpf_3"],
        "hole_label_odd_candidate_small_lpf_5_total": totals["hole_label_odd_candidate_small_lpf_5"],
        "hole_label_residual_candidate_total": totals["hole_label_residual_candidate"],
        "first_hole_dominates_complete": first_hole_dominates,
        "complete_interval_geometric_part_closed": True,
        "hole_correction_phase_control_closed": False,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_correction_phase_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "complete_interval_geometric_phase_closed_hole_correction_phase_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after completion tax, the next non-cyclic refinement is the exact additive-character identity separating the geometric complete interval from the fake hole correction",
        "current_object": {
            "phase_identity": "S_K(h)=S_C(h)-S_H(h), with S_C a finite geometric progression",
            "phase_h_tested": "h=1 for finite magnitude diagnostics; the symbolic identity holds for every integer h",
            "complete_interval_term": "explicit geometric additive-character sum on [min K_{P,q},max K_{P,q}]",
            "hole_correction": "non-object holes from no-odd, prime-candidate, and small-LPF candidate cells",
            "remaining_obstruction": "prove cancellation or absorption for S_H without changing the Phi-LPF selector",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "CompleteIntervalGeometricPhaseFormula",
                True,
                True,
                "The completed k-interval contribution is an explicit geometric additive-character sum.",
                "none",
            ),
            gate(
                "SparseSupportMinusHoleCorrectionIdentity",
                True,
                True,
                "The true sparse sum equals the complete interval sum minus the completion-hole correction.",
                "none",
            ),
            gate(
                "HoleCorrectionPhaseCancellationOrAbsorption",
                False,
                False,
                "Control the correction phase sum from no-odd, prime-candidate, and small-LPF holes.",
                "new correction phase theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "the complete interval part is now elementary; trace-function input would have to control or bypass the non-trace hole correction",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-modulus Kloosterman bilinear estimates do not apply directly to the additive hole correction S_H",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II amplification is downstream of converting S_H into a true Kloosterman/Type-II family",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution estimates become relevant only after the hole correction is embedded in a controlled convolution support",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree parameter estimates do not absorb the prime and small-LPF hole phases automatically",
        },
        "latest_narrowest_mouth": [
            "HoleCorrectionPhaseCancellationOrAbsorptionForNoOddPrimeSmallLPFCells",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "complete_interval_geometric_phase_closed": True,
        "sparse_support_minus_hole_correction_identity_closed": True,
        "hole_correction_phase_control_closed": False,
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
        "real_k_count",
        "complete_span",
        "hole_count",
        "sum_abs_sparse_sum_h1",
        "sum_abs_complete_geometric_sum_h1",
        "sum_abs_hole_correction_sum_h1",
        "hole_abs_gt_complete_abs_bucket_count_h1",
        "max_hole_over_complete_abs_ratio_h1",
        "first_hole_dominates_complete",
    ]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k completion correction phase 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"phase_identity={current['phase_identity']}",
        f"phase_h_tested={current['phase_h_tested']}",
        f"complete_interval_term={current['complete_interval_term']}",
        f"hole_correction={current['hole_correction']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. correction phase 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"q_bucket_count_total={audit['q_bucket_count_total']}",
        f"previous_selected_q_bucket_count_total={audit['previous_selected_q_bucket_count_total']}",
        f"real_k_count_total={audit['real_k_count_total']}",
        f"previous_real_k_count_total={audit['previous_real_k_count_total']}",
        f"complete_span_total={audit['complete_span_total']}",
        f"previous_completion_span_total={audit['previous_completion_span_total']}",
        f"hole_count_total={audit['hole_count_total']}",
        f"previous_completion_holes_total={audit['previous_completion_holes_total']}",
        f"phase_identity_counts_match_completion_tax={primorial.bool_text(audit['phase_identity_counts_match_completion_tax'])}",
        f"geometric_formula_verified={primorial.bool_text(audit['geometric_formula_verified'])}",
        f"correction_phase_identity_verified={primorial.bool_text(audit['correction_phase_identity_verified'])}",
        f"max_geometric_formula_error={audit['max_geometric_formula_error']:.3e}",
        f"max_correction_identity_error={audit['max_correction_identity_error']:.3e}",
        f"sum_abs_sparse_sum_h1={audit['sum_abs_sparse_sum_h1']:.6f}",
        f"sum_abs_complete_geometric_sum_h1={audit['sum_abs_complete_geometric_sum_h1']:.6f}",
        f"sum_abs_hole_correction_sum_h1={audit['sum_abs_hole_correction_sum_h1']:.6f}",
        f"max_abs_sparse_sum_h1={audit['max_abs_sparse_sum_h1']:.6f}",
        f"max_abs_complete_geometric_sum_h1={audit['max_abs_complete_geometric_sum_h1']:.6f}",
        f"max_abs_hole_correction_sum_h1={audit['max_abs_hole_correction_sum_h1']:.6f}",
        f"max_hole_over_complete_abs_ratio_h1={audit['max_hole_over_complete_abs_ratio_h1']:.6f}",
        f"hole_abs_gt_complete_abs_bucket_count_h1={audit['hole_abs_gt_complete_abs_bucket_count_h1']}",
        f"sparse_abs_gt_complete_abs_bucket_count_h1={audit['sparse_abs_gt_complete_abs_bucket_count_h1']}",
        f"complete_near_zero_with_nonzero_hole_bucket_count_h1={audit['complete_near_zero_with_nonzero_hole_bucket_count_h1']}",
        f"hole_label_no_odd_candidate_total={audit['hole_label_no_odd_candidate_total']}",
        f"hole_label_odd_candidate_prime_total={audit['hole_label_odd_candidate_prime_total']}",
        f"hole_label_odd_candidate_small_lpf_3_total={audit['hole_label_odd_candidate_small_lpf_3_total']}",
        f"hole_label_odd_candidate_small_lpf_5_total={audit['hole_label_odd_candidate_small_lpf_5_total']}",
        f"hole_label_residual_candidate_total={audit['hole_label_residual_candidate_total']}",
        f"first_hole_dominates_complete={audit['first_hole_dominates_complete']}",
        f"complete_interval_geometric_part_closed={primorial.bool_text(audit['complete_interval_geometric_part_closed'])}",
        f"hole_correction_phase_control_closed={primorial.bool_text(audit['hole_correction_phase_control_closed'])}",
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
        "结论：完整区间相位项已退化为显式几何和；真实难点完全落到 completion-hole correction 的相位控制。有限账本中很多 q-bucket 的 hole correction 幅度大于完整区间几何项，因此不能把 correction 当作可忽略误差。",
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
        f"complete_interval_geometric_phase_closed={primorial.bool_text(payload['complete_interval_geometric_phase_closed'])}",
        f"sparse_support_minus_hole_correction_identity_closed={primorial.bool_text(payload['sparse_support_minus_hole_correction_identity_closed'])}",
        f"hole_correction_phase_control_closed={primorial.bool_text(payload['hole_correction_phase_control_closed'])}",
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
    print("complete_interval_geometric_phase_closed=true")
    print("hole_correction_phase_control_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
