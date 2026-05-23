#!/usr/bin/env python3
"""审计 sparse additive-k 支撑补全到完整区间时的精确代价。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-audit.json

上一层已经把 row-averaged phase 重标记为 q 模上的 k-加性角色：

  D = q*m - k*P,    D == -kP (mod q),    e(-hD/q)=e(hPk/q).

本层继续下钻：若为了调用完整区间加性角色相消，把每个 q-bucket 的真实
稀疏支撑 K_{P,q} 补成 [min K_{P,q}, max K_{P,q}]，则补入的 k 不是同对象。
每个补入 k 的 product-cell 长度小于 2，因此至多有一个奇候选 m；若该 m 是
residual LPF cofactor，它本应已经在真实支撑中。于是 completion correction
精确落在“无奇候选”或“奇候选但非 residual LPF cofactor”的洞上。
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


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-audit.json",
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


def classify_nonresidual_odd(m: int, primes: list[int]) -> str:
    """分类补全洞中的唯一奇候选为何不是 residual LPF cofactor。"""
    r = primorial.lpf(m, primes)
    if r == m:
        return "odd_candidate_prime"
    if r < 7:
        return f"odd_candidate_small_lpf_{r}"
    beta = m // r
    if beta < r:
        return "odd_candidate_beta_less_than_lpf"
    if primorial.lpf(beta, primes) < r:
        return "odd_candidate_beta_lpf_below_lpf"
    return "odd_candidate_other_nonresidual"


def selected_k_support_for_q(P: int, q: int, records: list[dict[str, int]]) -> set[int]:
    """返回固定 P,q 下真实 row-averaged additive-k 支撑。"""
    k_values: set[int] = set()
    for record in records:
        m = record["m"]
        if m < q:
            continue
        k = (q * m) // P
        if not (1 <= k < P):
            continue
        d = q * m - k * P
        if d == 0:
            continue
        low, high = floorcell.product_cell_window(P, k, q)
        m_odd, odd_count = primorial.unique_odd_candidate(low, high)
        if odd_count == 1 and m_odd == m:
            k_values.add(k)
    return k_values


def completion_hole_profile(P: int, q: int, k_values: set[int], primes: list[int]) -> dict[str, Any]:
    """分类固定 q-bucket 中补完整区间所加入的假 k。"""
    min_k = min(k_values)
    max_k = max(k_values)
    span = max_k - min_k + 1
    counters: Counter[str] = Counter()
    first_hole = "none"
    first_residual_candidate_hole = "none"
    hole_samples: list[str] = []

    for k in range(min_k, max_k + 1):
        if k in k_values:
            continue
        counters["completion_holes"] += 1
        low, high = floorcell.product_cell_window(P, k, q)
        m_odd, odd_count = primorial.unique_odd_candidate(low, high)
        counters["bad_odd_count_over_one"] += int(odd_count > 1)
        if m_odd is None:
            counters["holes_without_odd_candidate"] += 1
            label = f"k={k},I=[{low},{high}],class=no_odd_candidate"
        else:
            record = primorial.residual_record(m_odd, primes)
            if record is None:
                kind = classify_nonresidual_odd(m_odd, primes)
                counters[kind] += 1
                counters["holes_with_nonresidual_odd_candidate"] += 1
                label = f"k={k},I=[{low},{high}],m={m_odd},class={kind}"
            else:
                counters["holes_with_residual_candidate"] += 1
                if first_residual_candidate_hole == "none":
                    first_residual_candidate_hole = (
                        f"P={P},q={q},k={k},m={m_odd},r={record['r']},beta={record['beta']}"
                    )
                label = (
                    f"k={k},I=[{low},{high}],m={m_odd},"
                    f"class=residual_candidate_should_have_been_selected"
                )
        if first_hole == "none":
            first_hole = f"P={P},q={q},{label}"
        if len(hole_samples) < 6:
            hole_samples.append(label)

    return {
        "q": q,
        "real_k_count": len(k_values),
        "completion_span": span,
        "completion_holes": counters["completion_holes"],
        "completion_tax_ratio": counters["completion_holes"] / len(k_values),
        "holes_without_odd_candidate": counters["holes_without_odd_candidate"],
        "holes_with_nonresidual_odd_candidate": counters["holes_with_nonresidual_odd_candidate"],
        "holes_with_residual_candidate": counters["holes_with_residual_candidate"],
        "bad_odd_count_over_one": counters["bad_odd_count_over_one"],
        "odd_candidate_prime": counters["odd_candidate_prime"],
        "odd_candidate_small_lpf_3": counters["odd_candidate_small_lpf_3"],
        "odd_candidate_small_lpf_5": counters["odd_candidate_small_lpf_5"],
        "odd_candidate_other_nonresidual": counters["odd_candidate_other_nonresidual"],
        "first_completion_hole": first_hole,
        "first_residual_candidate_hole": first_residual_candidate_hole,
        "hole_samples": "; ".join(hole_samples) if hole_samples else "none",
    }


def audit_P(P: int, records: list[dict[str, int]], primes: list[int], collect_samples: bool) -> dict[str, Any]:
    """审计固定 P 下所有非空 q-bucket 的 completion tax。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    totals: Counter[str] = Counter()
    maxima: dict[str, float] = {
        "max_completion_holes_per_q": 0.0,
        "max_completion_tax_ratio_per_q": 0.0,
    }
    sample_buckets: list[dict[str, Any]] = []
    first_hole = "none"
    first_residual_candidate_hole = "none"

    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        k_values = selected_k_support_for_q(P, q, records)
        if not k_values:
            continue
        profile = completion_hole_profile(P, q, k_values, primes)
        totals["selected_q_bucket_count"] += 1
        for key in [
            "real_k_count",
            "completion_span",
            "completion_holes",
            "holes_without_odd_candidate",
            "holes_with_nonresidual_odd_candidate",
            "holes_with_residual_candidate",
            "bad_odd_count_over_one",
            "odd_candidate_prime",
            "odd_candidate_small_lpf_3",
            "odd_candidate_small_lpf_5",
            "odd_candidate_other_nonresidual",
        ]:
            totals[key] += int(profile[key])
        maxima["max_completion_holes_per_q"] = max(
            maxima["max_completion_holes_per_q"], float(profile["completion_holes"])
        )
        maxima["max_completion_tax_ratio_per_q"] = max(
            maxima["max_completion_tax_ratio_per_q"], float(profile["completion_tax_ratio"])
        )
        if first_hole == "none" and profile["first_completion_hole"] != "none":
            first_hole = profile["first_completion_hole"]
        if (
            first_residual_candidate_hole == "none"
            and profile["first_residual_candidate_hole"] != "none"
        ):
            first_residual_candidate_hole = profile["first_residual_candidate_hole"]
        if collect_samples and len(sample_buckets) < 4:
            sample_buckets.append(profile)

    return {
        "P": P,
        "selected_q_bucket_count": totals["selected_q_bucket_count"],
        "real_k_count": totals["real_k_count"],
        "completion_span": totals["completion_span"],
        "completion_holes": totals["completion_holes"],
        "completion_tax_ratio": totals["completion_holes"] / totals["real_k_count"]
        if totals["real_k_count"]
        else 0.0,
        "holes_without_odd_candidate": totals["holes_without_odd_candidate"],
        "holes_with_nonresidual_odd_candidate": totals["holes_with_nonresidual_odd_candidate"],
        "holes_with_residual_candidate": totals["holes_with_residual_candidate"],
        "bad_odd_count_over_one": totals["bad_odd_count_over_one"],
        "odd_candidate_prime": totals["odd_candidate_prime"],
        "odd_candidate_small_lpf_3": totals["odd_candidate_small_lpf_3"],
        "odd_candidate_small_lpf_5": totals["odd_candidate_small_lpf_5"],
        "odd_candidate_other_nonresidual": totals["odd_candidate_other_nonresidual"],
        "max_completion_holes_per_q": int(maxima["max_completion_holes_per_q"]),
        "max_completion_tax_ratio_per_q": maxima["max_completion_tax_ratio_per_q"],
        "first_completion_hole": first_hole,
        "first_residual_candidate_hole": first_residual_candidate_hole,
        "sample_buckets": sample_buckets,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 completion tax 做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-audit.json").read_text())
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    max_completion_holes_per_q = 0
    max_completion_tax_ratio_per_q = 0.0
    sample_rows: list[dict[str, Any]] = []
    first_hole = "none"
    first_residual_candidate_hole = "none"

    for P in P_values:
        row = audit_P(P, records_by_P[P], primes, P in interesting)
        for key in [
            "selected_q_bucket_count",
            "real_k_count",
            "completion_span",
            "completion_holes",
            "holes_without_odd_candidate",
            "holes_with_nonresidual_odd_candidate",
            "holes_with_residual_candidate",
            "bad_odd_count_over_one",
            "odd_candidate_prime",
            "odd_candidate_small_lpf_3",
            "odd_candidate_small_lpf_5",
            "odd_candidate_other_nonresidual",
        ]:
            totals[key] += int(row[key])
        max_completion_holes_per_q = max(max_completion_holes_per_q, row["max_completion_holes_per_q"])
        max_completion_tax_ratio_per_q = max(
            max_completion_tax_ratio_per_q, row["max_completion_tax_ratio_per_q"]
        )
        if first_hole == "none" and row["first_completion_hole"] != "none":
            first_hole = row["first_completion_hole"]
        if first_residual_candidate_hole == "none" and row["first_residual_candidate_hole"] != "none":
            first_residual_candidate_hole = row["first_residual_candidate_hole"]
        if P in interesting:
            sample_rows.append(row)

    previous_audit = previous["finite_audit"]
    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "selected_q_bucket_count_total": totals["selected_q_bucket_count"],
        "previous_selected_q_bucket_count_total": previous_audit["selected_q_bucket_count_total"],
        "real_k_count_total": totals["real_k_count"],
        "previous_total_k_support_count": previous_audit["total_k_support_count"],
        "completion_span_total": totals["completion_span"],
        "previous_total_k_span_length": previous_audit["total_k_span_length"],
        "completion_holes_total": totals["completion_holes"],
        "previous_total_k_interval_holes": previous_audit["total_k_interval_holes"],
        "completion_holes_match_previous_total": totals["completion_holes"]
        == previous_audit["total_k_interval_holes"],
        "real_k_count_matches_previous_total": totals["real_k_count"]
        == previous_audit["total_k_support_count"],
        "completion_span_matches_previous_total": totals["completion_span"]
        == previous_audit["total_k_span_length"],
        "completion_tax_ratio_total": totals["completion_holes"] / totals["real_k_count"],
        "holes_without_odd_candidate_total": totals["holes_without_odd_candidate"],
        "holes_with_nonresidual_odd_candidate_total": totals["holes_with_nonresidual_odd_candidate"],
        "holes_with_residual_candidate_total": totals["holes_with_residual_candidate"],
        "bad_odd_count_over_one_total": totals["bad_odd_count_over_one"],
        "odd_candidate_prime_total": totals["odd_candidate_prime"],
        "odd_candidate_small_lpf_3_total": totals["odd_candidate_small_lpf_3"],
        "odd_candidate_small_lpf_5_total": totals["odd_candidate_small_lpf_5"],
        "odd_candidate_other_nonresidual_total": totals["odd_candidate_other_nonresidual"],
        "max_completion_holes_per_q": max_completion_holes_per_q,
        "max_completion_tax_ratio_per_q": max_completion_tax_ratio_per_q,
        "first_completion_hole": first_hole,
        "first_residual_candidate_hole": first_residual_candidate_hole,
        "residual_candidate_holes_absent": totals["holes_with_residual_candidate"] == 0,
        "complete_interval_replacement_object_preserving": False,
        "completion_correction_control_closed": False,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "complete_interval_replacement_rejected_completion_correction_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the additive-k relabeling reduced the next non-cyclic hard point to sparse support; the fastest honest progress is to quantify the exact cost of replacing that support by complete intervals",
        "current_object": {
            "true_support": "K_{P,q}={floor(qm/P): m is a selected residual LPF cofactor in the q-bucket}",
            "tempting_completion": "[min K_{P,q}, max K_{P,q}]",
            "completion_decomposition": "complete interval = true sparse support disjoint union completion holes",
            "hole_classification": "each hole has no odd product-cell candidate, or its unique odd candidate is not a residual LPF cofactor",
            "remaining_obstruction": "control the completion correction without changing the Phi-LPF selector",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SparseKCompletionTaxLedger",
                True,
                True,
                "Completing each q-bucket to its full k interval adds an explicit disjoint correction set.",
                "none",
            ),
            gate(
                "ResidualCandidateHoleExclusion",
                True,
                True,
                "A completion hole cannot contain a selected residual LPF cofactor; otherwise it would already be in K_{P,q}.",
                "none",
            ),
            gate(
                "DirectCompleteIntervalObjectPreservation",
                False,
                False,
                "The completed interval is not the same object because the correction is much larger than the true support.",
                "requires loss-controlled correction theorem",
            ),
            gate(
                "CompletionCorrectionCancellationOrAbsorption",
                False,
                False,
                "Bound the fake completion correction, including no-odd, prime-candidate, and small-LPF candidate holes.",
                "new correction cancellation/absorption theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "trace-function bilinear bounds are relevant only after the sparse support plus correction is embedded in a genuine trace-family bilinear form",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-modulus Kloosterman bilinear savings do not by themselves bound the non-Kloosterman completion-hole correction",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II Kloosterman amplification needs a true bilinear Kloosterman object, not a completed interval plus fake nonresidual holes",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution/Kloosterman-fraction inputs require controlled convolution support and small-modulus equidistribution; the completion holes are not yet such a support",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree Kloosterman-parameter estimates do not remove the prime and small-LPF hole correction",
        },
        "latest_narrowest_mouth": [
            "CompletionCorrectionCancellationOrAbsorptionForSparseLPFKSupport",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "sparse_k_completion_tax_ledger_closed": True,
        "residual_candidate_hole_exclusion_closed": True,
        "direct_complete_interval_object_preservation_closed": False,
        "completion_correction_control_closed": False,
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
        "selected_q_bucket_count",
        "real_k_count",
        "completion_span",
        "completion_holes",
        "completion_tax_ratio",
        "holes_without_odd_candidate",
        "holes_with_nonresidual_odd_candidate",
        "odd_candidate_prime",
        "odd_candidate_small_lpf_3",
        "odd_candidate_small_lpf_5",
        "max_completion_holes_per_q",
        "first_completion_hole",
    ]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k completion tax 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"true_support={current['true_support']}",
        f"tempting_completion={current['tempting_completion']}",
        f"completion_decomposition={current['completion_decomposition']}",
        f"hole_classification={current['hole_classification']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. completion tax 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"selected_q_bucket_count_total={audit['selected_q_bucket_count_total']}",
        f"previous_selected_q_bucket_count_total={audit['previous_selected_q_bucket_count_total']}",
        f"real_k_count_total={audit['real_k_count_total']}",
        f"previous_total_k_support_count={audit['previous_total_k_support_count']}",
        f"completion_span_total={audit['completion_span_total']}",
        f"previous_total_k_span_length={audit['previous_total_k_span_length']}",
        f"completion_holes_total={audit['completion_holes_total']}",
        f"previous_total_k_interval_holes={audit['previous_total_k_interval_holes']}",
        f"completion_holes_match_previous_total={primorial.bool_text(audit['completion_holes_match_previous_total'])}",
        f"real_k_count_matches_previous_total={primorial.bool_text(audit['real_k_count_matches_previous_total'])}",
        f"completion_span_matches_previous_total={primorial.bool_text(audit['completion_span_matches_previous_total'])}",
        f"completion_tax_ratio_total={audit['completion_tax_ratio_total']:.6f}",
        f"holes_without_odd_candidate_total={audit['holes_without_odd_candidate_total']}",
        f"holes_with_nonresidual_odd_candidate_total={audit['holes_with_nonresidual_odd_candidate_total']}",
        f"holes_with_residual_candidate_total={audit['holes_with_residual_candidate_total']}",
        f"bad_odd_count_over_one_total={audit['bad_odd_count_over_one_total']}",
        f"odd_candidate_prime_total={audit['odd_candidate_prime_total']}",
        f"odd_candidate_small_lpf_3_total={audit['odd_candidate_small_lpf_3_total']}",
        f"odd_candidate_small_lpf_5_total={audit['odd_candidate_small_lpf_5_total']}",
        f"odd_candidate_other_nonresidual_total={audit['odd_candidate_other_nonresidual_total']}",
        f"max_completion_holes_per_q={audit['max_completion_holes_per_q']}",
        f"max_completion_tax_ratio_per_q={audit['max_completion_tax_ratio_per_q']:.6f}",
        f"first_completion_hole={audit['first_completion_hole']}",
        f"first_residual_candidate_hole={audit['first_residual_candidate_hole']}",
        f"residual_candidate_holes_absent={primorial.bool_text(audit['residual_candidate_holes_absent'])}",
        f"complete_interval_replacement_object_preserving={primorial.bool_text(audit['complete_interval_replacement_object_preserving'])}",
        f"completion_correction_control_closed={primorial.bool_text(audit['completion_correction_control_closed'])}",
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
        "结论：完整区间 completion 的相消若直接使用，会把真实 sparse LPF 支撑替换成一个大得多的对象。补入 correction 全部来自无奇候选或非 residual LPF 奇候选；这正是下一步必须控制的非循环硬点。",
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
        f"sparse_k_completion_tax_ledger_closed={primorial.bool_text(payload['sparse_k_completion_tax_ledger_closed'])}",
        f"residual_candidate_hole_exclusion_closed={primorial.bool_text(payload['residual_candidate_hole_exclusion_closed'])}",
        f"direct_complete_interval_object_preservation_closed={primorial.bool_text(payload['direct_complete_interval_object_preservation_closed'])}",
        f"completion_correction_control_closed={primorial.bool_text(payload['completion_correction_control_closed'])}",
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
    print("sparse_k_completion_tax_ledger_closed=true")
    print("complete_interval_replacement_object_preserving=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
