#!/usr/bin/env python3
"""审计 additive-k completion-hole correction 的相位分类分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_class_phase_decomposition_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-audit.json

上一层把真实 sparse 相位和写成

  S_K(h) = S_C(h) - S_H(h).

本层继续下钻 S_H。对每个 hole k，product-cell I_{P,k}(q) 长度小于 2；
因此它要么没有整数/只有偶 singleton，要么有唯一奇候选 m。若 m 是奇合数且
最小素因子 >=7，则它就是 residual LPF cofactor，不可能是 hole。所以奇候选
hole 只能是 prime、LPF=3 或 LPF=5。于是

  S_H = S_empty + S_even + S_prime + S_lpf3 + S_lpf5

是同对象 correction 的精确相位分解；仍未给出这些包的相消。
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


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
TOL = 1e-9

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

CLASS_ORDER = [
    "empty_cell",
    "even_singleton",
    "odd_candidate_prime",
    "odd_candidate_lpf3",
    "odd_candidate_lpf5",
    "residual_candidate_forbidden",
    "other_forbidden",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def hole_class(P: int, q: int, k: int, primes: list[int]) -> str:
    """返回 completion hole 的确定性类别。"""
    low, high = floorcell.product_cell_window(P, k, q)
    if low > high:
        return "empty_cell"
    m_odd, odd_count = primorial.unique_odd_candidate(low, high)
    if odd_count == 0:
        return "even_singleton"
    if odd_count > 1:
        return "other_forbidden"
    assert m_odd is not None
    record = primorial.residual_record(m_odd, primes)
    if record is not None:
        return "residual_candidate_forbidden"
    r = primorial.lpf(m_odd, primes)
    if r == m_odd:
        return "odd_candidate_prime"
    if r == 3:
        return "odd_candidate_lpf3"
    if r == 5:
        return "odd_candidate_lpf5"
    return "other_forbidden"


def bucket_decomposition(P: int, q: int, k_values: set[int], primes: list[int]) -> dict[str, Any]:
    """计算一个 q-bucket 的 S_H 分类相位分解。"""
    min_k = min(k_values)
    max_k = max(k_values)
    a = P % q
    class_counts: Counter[str] = Counter()
    class_sums = {name: 0j for name in CLASS_ORDER}
    hole_values: list[int] = []

    for k in range(min_k, max_k + 1):
        if k in k_values:
            continue
        cls = hole_class(P, q, k, primes)
        class_counts[cls] += 1
        class_sums[cls] += correction.additive_phase(a, q, k)
        hole_values.append(k)

    direct_hole_sum = correction.direct_sum(a, q, hole_values)
    class_total_sum = sum(class_sums.values(), 0j)
    class_identity_error = abs(direct_hole_sum - class_total_sum)
    class_abs = {f"abs_{name}_sum_h1": abs(class_sums[name]) for name in CLASS_ORDER}
    active_abs = {name: abs(class_sums[name]) for name in CLASS_ORDER if class_counts[name] > 0}
    dominant_class = max(active_abs, key=active_abs.get) if active_abs else "none"

    return {
        "q": q,
        "min_k": min_k,
        "max_k": max_k,
        "real_k_count": len(k_values),
        "hole_count": len(hole_values),
        "class_identity_error": class_identity_error,
        "dominant_hole_phase_class_h1": dominant_class,
        "dominant_hole_phase_abs_h1": active_abs.get(dominant_class, 0.0),
        **{f"count_{name}": class_counts[name] for name in CLASS_ORDER},
        **class_abs,
    }


def audit_P(P: int, records: list[dict[str, int]], primes: list[int], collect_samples: bool) -> dict[str, Any]:
    """审计固定 P 的 hole-class phase decomposition。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    totals: Counter[str] = Counter()
    float_totals: Counter[str] = Counter()
    max_identity_error = 0.0
    max_class_abs = defaultdict(float)
    dominant_counts: Counter[str] = Counter()
    sample_buckets: list[dict[str, Any]] = []

    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        k_values = tax.selected_k_support_for_q(P, q, records)
        if not k_values:
            continue
        profile = bucket_decomposition(P, q, k_values, primes)
        totals["q_bucket_count"] += 1
        totals["real_k_count"] += profile["real_k_count"]
        totals["hole_count"] += profile["hole_count"]
        max_identity_error = max(max_identity_error, profile["class_identity_error"])
        dominant_counts[profile["dominant_hole_phase_class_h1"]] += 1
        for name in CLASS_ORDER:
            totals[f"count_{name}"] += int(profile[f"count_{name}"])
            value = float(profile[f"abs_{name}_sum_h1"])
            float_totals[f"sum_abs_{name}_sum_h1"] += value
            max_class_abs[f"max_abs_{name}_sum_h1"] = max(
                max_class_abs[f"max_abs_{name}_sum_h1"], value
            )
        if collect_samples and len(sample_buckets) < 4:
            sample_buckets.append(profile)

    return {
        "P": P,
        "q_bucket_count": totals["q_bucket_count"],
        "real_k_count": totals["real_k_count"],
        "hole_count": totals["hole_count"],
        "max_class_identity_error": max_identity_error,
        "dominant_class_counts_h1": json.dumps(dict(sorted(dominant_counts.items())), sort_keys=True),
        **{f"count_{name}": totals[f"count_{name}"] for name in CLASS_ORDER},
        **{key: float_totals[key] for key in sorted(float_totals)},
        **{key: max_class_abs[key] for key in sorted(max_class_abs)},
        "sample_buckets": sample_buckets,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的分类相位分解做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    previous = json.loads(
        (DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-audit.json").read_text()
    )
    previous_audit = previous["finite_audit"]
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    float_totals: Counter[str] = Counter()
    max_values = defaultdict(float)
    dominant_counts: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []

    for P in P_values:
        row = audit_P(P, records_by_P[P], primes, P in interesting)
        for key in ["q_bucket_count", "real_k_count", "hole_count"]:
            totals[key] += int(row[key])
        for name in CLASS_ORDER:
            totals[f"count_{name}"] += int(row[f"count_{name}"])
            for prefix in ["sum_abs", "max_abs"]:
                key = f"{prefix}_{name}_sum_h1"
                if prefix == "sum_abs":
                    float_totals[key] += float(row.get(key, 0.0))
                else:
                    max_values[key] = max(max_values[key], float(row.get(key, 0.0)))
        max_values["max_class_identity_error"] = max(
            max_values["max_class_identity_error"], float(row["max_class_identity_error"])
        )
        dominant_counts.update(json.loads(row["dominant_class_counts_h1"]))
        if P in interesting:
            sample_rows.append(row)

    no_forbidden = (
        totals["count_residual_candidate_forbidden"] == 0
        and totals["count_other_forbidden"] == 0
    )
    classified_total = sum(totals[f"count_{name}"] for name in CLASS_ORDER)
    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "q_bucket_count_total": totals["q_bucket_count"],
        "previous_q_bucket_count_total": previous_audit["q_bucket_count_total"],
        "real_k_count_total": totals["real_k_count"],
        "previous_real_k_count_total": previous_audit["real_k_count_total"],
        "hole_count_total": totals["hole_count"],
        "previous_hole_count_total": previous_audit["hole_count_total"],
        "classified_hole_count_total": classified_total,
        "counts_match_previous_correction_phase": (
            totals["q_bucket_count"] == previous_audit["q_bucket_count_total"]
            and totals["real_k_count"] == previous_audit["real_k_count_total"]
            and totals["hole_count"] == previous_audit["hole_count_total"]
            and classified_total == previous_audit["hole_count_total"]
        ),
        "hole_class_identity_verified": max_values["max_class_identity_error"] < TOL,
        "max_class_identity_error": max_values["max_class_identity_error"],
        "forbidden_class_count_total": totals["count_residual_candidate_forbidden"]
        + totals["count_other_forbidden"],
        "only_empty_even_prime_lpf3_lpf5_classes_seen": no_forbidden,
        **{f"count_{name}_total": totals[f"count_{name}"] for name in CLASS_ORDER},
        **{key: float_totals[key] for key in sorted(float_totals)},
        **{key: max_values[key] for key in sorted(max_values) if key != "max_class_identity_error"},
        "dominant_hole_phase_class_bucket_counts_h1": dict(sorted(dominant_counts.items())),
        "class_phase_control_closed": False,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_class_phase_decomposition_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "hole_class_phase_decomposition_closed_class_phase_control_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after S_K=S_C-S_H, the next non-cyclic refinement is the deterministic local class decomposition of S_H",
        "current_object": {
            "phase_decomposition": "S_H=S_empty+S_even+S_prime+S_lpf3+S_lpf5",
            "classification_law": "hole cells have length <2; an odd nonresidual candidate is either prime or has LPF 3 or 5",
            "remaining_obstruction": "prove cancellation or absorption for the five class phase packets without changing the selector",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "HoleClassPartition",
                True,
                True,
                "Every completion hole belongs to a deterministic local class.",
                "none",
            ),
            gate(
                "OddHolePrimeOrSmallLPFReduction",
                True,
                True,
                "An odd nonresidual completion-hole candidate is prime or has least prime factor 3 or 5.",
                "none",
            ),
            gate(
                "HoleClassPhaseIdentity",
                True,
                True,
                "The hole correction phase sum decomposes as the sum of the class phase packets.",
                "none",
            ),
            gate(
                "FiveClassPhaseCancellationOrAbsorption",
                False,
                False,
                "Control empty, even, prime, LPF3, and LPF5 hole phase packets.",
                "new class-wise phase theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "trace-function bilinear bounds would need a trace-family model for one of the five hole packets; the class split alone does not provide it",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-modulus Kloosterman bilinear estimates still require a Kloosterman phase, not merely the five local hole classes",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II input is downstream of converting prime/LPF3/LPF5 packets into a Type-II object",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution may be relevant only after a class packet is embedded in a controlled convolution support",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree Kloosterman-parameter estimates do not directly treat empty/even or prime/small-LPF additive hole packets",
        },
        "latest_narrowest_mouth": [
            "FiveClassHolePhaseCancellationOrAbsorption",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "hole_class_partition_closed": True,
        "odd_hole_prime_or_small_lpf_reduction_closed": True,
        "hole_class_phase_identity_closed": True,
        "five_class_phase_control_closed": False,
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
        "count_empty_cell",
        "count_even_singleton",
        "count_odd_candidate_prime",
        "count_odd_candidate_lpf3",
        "count_odd_candidate_lpf5",
        "dominant_class_counts_h1",
        "max_class_identity_error",
    ]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k hole-class phase decomposition 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"phase_decomposition={current['phase_decomposition']}",
        f"classification_law={current['classification_law']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. hole-class phase 有限审计",
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
        f"classified_hole_count_total={audit['classified_hole_count_total']}",
        f"counts_match_previous_correction_phase={primorial.bool_text(audit['counts_match_previous_correction_phase'])}",
        f"hole_class_identity_verified={primorial.bool_text(audit['hole_class_identity_verified'])}",
        f"max_class_identity_error={audit['max_class_identity_error']:.3e}",
        f"forbidden_class_count_total={audit['forbidden_class_count_total']}",
        f"only_empty_even_prime_lpf3_lpf5_classes_seen={primorial.bool_text(audit['only_empty_even_prime_lpf3_lpf5_classes_seen'])}",
        f"count_empty_cell_total={audit['count_empty_cell_total']}",
        f"count_even_singleton_total={audit['count_even_singleton_total']}",
        f"count_odd_candidate_prime_total={audit['count_odd_candidate_prime_total']}",
        f"count_odd_candidate_lpf3_total={audit['count_odd_candidate_lpf3_total']}",
        f"count_odd_candidate_lpf5_total={audit['count_odd_candidate_lpf5_total']}",
        f"sum_abs_empty_cell_sum_h1={audit['sum_abs_empty_cell_sum_h1']:.6f}",
        f"sum_abs_even_singleton_sum_h1={audit['sum_abs_even_singleton_sum_h1']:.6f}",
        f"sum_abs_odd_candidate_prime_sum_h1={audit['sum_abs_odd_candidate_prime_sum_h1']:.6f}",
        f"sum_abs_odd_candidate_lpf3_sum_h1={audit['sum_abs_odd_candidate_lpf3_sum_h1']:.6f}",
        f"sum_abs_odd_candidate_lpf5_sum_h1={audit['sum_abs_odd_candidate_lpf5_sum_h1']:.6f}",
        f"dominant_hole_phase_class_bucket_counts_h1={json.dumps(audit['dominant_hole_phase_class_bucket_counts_h1'], sort_keys=True)}",
        f"class_phase_control_closed={primorial.bool_text(audit['class_phase_control_closed'])}",
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
        "结论：`S_H` 的同对象 correction 已被压成五类局部 packet；这关闭了“hole correction 是黑箱残差”的粗口，但仍未证明五类 packet 的相消或吸收。",
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
        f"hole_class_partition_closed={primorial.bool_text(payload['hole_class_partition_closed'])}",
        f"odd_hole_prime_or_small_lpf_reduction_closed={primorial.bool_text(payload['odd_hole_prime_or_small_lpf_reduction_closed'])}",
        f"hole_class_phase_identity_closed={primorial.bool_text(payload['hole_class_phase_identity_closed'])}",
        f"five_class_phase_control_closed={primorial.bool_text(payload['five_class_phase_control_closed'])}",
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
    print("hole_class_phase_identity_closed=true")
    print("five_class_phase_control_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
