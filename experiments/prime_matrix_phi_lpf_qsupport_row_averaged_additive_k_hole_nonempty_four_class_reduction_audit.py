#!/usr/bin/env python3
"""审计 completion-hole correction 中 empty class 的结构性消除。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_nonempty_four_class_reduction_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-audit.json

上一层得到五类分解：

  S_H = S_empty + S_even + S_prime + S_lpf3 + S_lpf5.

本层继续下钻 empty class。固定 P,q 后，载体整数区间

  M_{P,q} = [max(P/2+1,q), 2P-1] ∩ Z

上的映射 m -> floor(qm/P) 单调，且相邻差为 0 或 1，因为 q<P。因此它不会
跳过中间 k。只要 q-bucket 有真实 sparse 支撑 K_{P,q}，则 [minK,maxK] 中
每个 k 都有至少一个整数载体 m；completion hole 不可能是 empty cell。

所以真正的 correction 从五类压成四类：

  S_H = S_even + S_prime + S_lpf3 + S_lpf5.
"""

from __future__ import annotations

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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_class_phase_decomposition_audit as classes  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

FOUR_CLASSES = [
    "even_singleton",
    "odd_candidate_prime",
    "odd_candidate_lpf3",
    "odd_candidate_lpf5",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def carrier_bounds(P: int, q: int) -> tuple[int, int]:
    """返回固定 q-bucket 的整数载体区间。"""
    return max(P // 2 + 1, q), 2 * P - 1


def carrier_k_counts(P: int, q: int) -> Counter[int]:
    """统计载体区间中 floor(qm/P) 的纤维大小。"""
    low, high = carrier_bounds(P, q)
    counts: Counter[int] = Counter()
    for m in range(low, high + 1):
        counts[(q * m) // P] += 1
    return counts


def bucket_nonempty_profile(P: int, q: int, k_values: set[int], primes: list[int]) -> dict[str, Any]:
    """审计固定 q-bucket 的 nonempty/four-class 结构。"""
    min_k = min(k_values)
    max_k = max(k_values)
    carrier_counts = carrier_k_counts(P, q)
    carrier_min = min(carrier_counts)
    carrier_max = max(carrier_counts)
    carrier_gap_count = sum(1 for k in range(carrier_min, carrier_max + 1) if k not in carrier_counts)
    selected_span_missing = sum(1 for k in range(min_k, max_k + 1) if k not in carrier_counts)
    max_carrier_fiber = max(carrier_counts.values()) if carrier_counts else 0

    hole_counts: Counter[str] = Counter()
    first_nonempty_hole = "none"
    empty_hole_count = 0
    forbidden_hole_count = 0
    for k in range(min_k, max_k + 1):
        if k in k_values:
            continue
        cls = classes.hole_class(P, q, k, primes)
        hole_counts[cls] += 1
        empty_hole_count += int(cls == "empty_cell")
        forbidden_hole_count += int(cls in {"residual_candidate_forbidden", "other_forbidden"})
        if first_nonempty_hole == "none":
            low, high = floorcell.product_cell_window(P, k, q)
            first_nonempty_hole = f"q={q},k={k},I=[{low},{high}],class={cls}"

    return {
        "q": q,
        "carrier_min_k": carrier_min,
        "carrier_max_k": carrier_max,
        "min_k": min_k,
        "max_k": max_k,
        "real_k_count": len(k_values),
        "hole_count": sum(hole_counts.values()),
        "carrier_gap_count": carrier_gap_count,
        "selected_span_missing_count": selected_span_missing,
        "empty_hole_count": empty_hole_count,
        "forbidden_hole_count": forbidden_hole_count,
        "max_carrier_fiber_size": max_carrier_fiber,
        "first_nonempty_hole": first_nonempty_hole,
        **{f"count_{name}": hole_counts[name] for name in FOUR_CLASSES},
    }


def audit_P(P: int, records: list[dict[str, int]], primes: list[int], collect_samples: bool) -> dict[str, Any]:
    """审计固定 P 的 empty-class 消除。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    totals: Counter[str] = Counter()
    max_carrier_fiber_size = 0
    sample_buckets: list[dict[str, Any]] = []

    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        k_values = tax.selected_k_support_for_q(P, q, records)
        if not k_values:
            continue
        profile = bucket_nonempty_profile(P, q, k_values, primes)
        totals["q_bucket_count"] += 1
        for key in [
            "real_k_count",
            "hole_count",
            "carrier_gap_count",
            "selected_span_missing_count",
            "empty_hole_count",
            "forbidden_hole_count",
            *[f"count_{name}" for name in FOUR_CLASSES],
        ]:
            totals[key] += int(profile[key])
        max_carrier_fiber_size = max(max_carrier_fiber_size, profile["max_carrier_fiber_size"])
        if collect_samples and len(sample_buckets) < 4:
            sample_buckets.append(profile)

    return {
        "P": P,
        "q_bucket_count": totals["q_bucket_count"],
        "real_k_count": totals["real_k_count"],
        "hole_count": totals["hole_count"],
        "carrier_gap_count": totals["carrier_gap_count"],
        "selected_span_missing_count": totals["selected_span_missing_count"],
        "empty_hole_count": totals["empty_hole_count"],
        "forbidden_hole_count": totals["forbidden_hole_count"],
        "max_carrier_fiber_size": max_carrier_fiber_size,
        **{f"count_{name}": totals[f"count_{name}"] for name in FOUR_CLASSES},
        "sample_buckets": sample_buckets,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 four-class reduction 做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    previous = json.loads(
        (DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-audit.json").read_text()
    )
    previous_audit = previous["finite_audit"]
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    max_carrier_fiber_size = 0
    sample_rows: list[dict[str, Any]] = []

    for P in P_values:
        row = audit_P(P, records_by_P[P], primes, P in interesting)
        for key in [
            "q_bucket_count",
            "real_k_count",
            "hole_count",
            "carrier_gap_count",
            "selected_span_missing_count",
            "empty_hole_count",
            "forbidden_hole_count",
            *[f"count_{name}" for name in FOUR_CLASSES],
        ]:
            totals[key] += int(row[key])
        max_carrier_fiber_size = max(max_carrier_fiber_size, row["max_carrier_fiber_size"])
        if P in interesting:
            sample_rows.append(row)

    four_class_total = sum(totals[f"count_{name}"] for name in FOUR_CLASSES)
    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "q_bucket_count_total": totals["q_bucket_count"],
        "previous_q_bucket_count_total": previous_audit["q_bucket_count_total"],
        "real_k_count_total": totals["real_k_count"],
        "previous_real_k_count_total": previous_audit["real_k_count_total"],
        "hole_count_total": totals["hole_count"],
        "previous_hole_count_total": previous_audit["hole_count_total"],
        "four_class_hole_count_total": four_class_total,
        "carrier_gap_count_total": totals["carrier_gap_count"],
        "selected_span_missing_count_total": totals["selected_span_missing_count"],
        "empty_hole_count_total": totals["empty_hole_count"],
        "previous_empty_hole_count_total": previous_audit["count_empty_cell_total"],
        "forbidden_hole_count_total": totals["forbidden_hole_count"],
        "max_carrier_fiber_size": max_carrier_fiber_size,
        "counts_match_previous_hole_class_audit": (
            totals["q_bucket_count"] == previous_audit["q_bucket_count_total"]
            and totals["real_k_count"] == previous_audit["real_k_count_total"]
            and totals["hole_count"] == previous_audit["hole_count_total"]
            and totals["empty_hole_count"] == previous_audit["count_empty_cell_total"]
            and four_class_total == previous_audit["hole_count_total"]
        ),
        "carrier_floor_map_no_skip_verified": totals["carrier_gap_count"] == 0,
        "selected_span_nonempty_verified": totals["selected_span_missing_count"] == 0,
        "empty_class_eliminated": totals["empty_hole_count"] == 0,
        "four_class_reduction_closed": (
            totals["carrier_gap_count"] == 0
            and totals["selected_span_missing_count"] == 0
            and totals["empty_hole_count"] == 0
            and totals["forbidden_hole_count"] == 0
        ),
        **{f"count_{name}_total": totals[f"count_{name}"] for name in FOUR_CLASSES},
        "four_class_phase_control_closed": False,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_nonempty_four_class_reduction_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "empty_hole_class_eliminated_four_class_phase_control_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the five-class correction is dominated by explicit local packets; the next non-cyclic refinement is to remove the empty class structurally",
        "current_object": {
            "carrier_interval": "M_{P,q}=[max(P/2+1,q),2P-1]∩Z",
            "carrier_floor_map": "m -> floor(qm/P) is monotone and has adjacent increments 0 or 1 because q<P",
            "empty_class_elimination": "every k between min K_{P,q} and max K_{P,q} has a carrier integer m, so completion holes are nonempty",
            "four_class_phase": "S_H=S_even+S_prime+S_lpf3+S_lpf5",
            "remaining_obstruction": "prove cancellation or absorption for the four nonempty class phase packets",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "CarrierFloorMapNoSkip",
                True,
                True,
                "The carrier floor map has no missing intermediate k-values.",
                "none",
            ),
            gate(
                "SelectedSpanNonempty",
                True,
                True,
                "Every k in the selected span [minK,maxK] has a nonempty product cell.",
                "none",
            ),
            gate(
                "EmptyHoleClassEliminated",
                True,
                True,
                "The empty-cell packet is identically zero for the row-averaged q-buckets.",
                "none",
            ),
            gate(
                "FourClassHolePhaseControl",
                False,
                False,
                "Control the even, prime, LPF3, and LPF5 hole phase packets.",
                "new four-class cancellation/absorption theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "trace-function bilinear bounds would need an embedding of one of the four nonempty hole packets into a trace family",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-modulus Kloosterman bilinear estimates still require a Kloosterman-type phase for the four packets",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II input is relevant only after a four-class packet becomes a Type-II/Kloosterman object",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution estimates require controlled convolution support; four-class locality alone is not enough",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree Kloosterman-parameter estimates do not directly control the even/prime/LPF3/LPF5 packets",
        },
        "latest_narrowest_mouth": [
            "FourClassHolePhaseCancellationOrAbsorption",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "carrier_floor_map_no_skip_closed": True,
        "selected_span_nonempty_closed": True,
        "empty_hole_class_eliminated": True,
        "four_class_hole_phase_identity_closed": True,
        "four_class_phase_control_closed": False,
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
        "carrier_gap_count",
        "selected_span_missing_count",
        "empty_hole_count",
        "count_even_singleton",
        "count_odd_candidate_prime",
        "count_odd_candidate_lpf3",
        "count_odd_candidate_lpf5",
        "max_carrier_fiber_size",
    ]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k hole nonempty four-class reduction 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"carrier_interval={current['carrier_interval']}",
        f"carrier_floor_map={current['carrier_floor_map']}",
        f"empty_class_elimination={current['empty_class_elimination']}",
        f"four_class_phase={current['four_class_phase']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. four-class reduction 有限审计",
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
        f"four_class_hole_count_total={audit['four_class_hole_count_total']}",
        f"carrier_gap_count_total={audit['carrier_gap_count_total']}",
        f"selected_span_missing_count_total={audit['selected_span_missing_count_total']}",
        f"empty_hole_count_total={audit['empty_hole_count_total']}",
        f"previous_empty_hole_count_total={audit['previous_empty_hole_count_total']}",
        f"forbidden_hole_count_total={audit['forbidden_hole_count_total']}",
        f"max_carrier_fiber_size={audit['max_carrier_fiber_size']}",
        f"counts_match_previous_hole_class_audit={primorial.bool_text(audit['counts_match_previous_hole_class_audit'])}",
        f"carrier_floor_map_no_skip_verified={primorial.bool_text(audit['carrier_floor_map_no_skip_verified'])}",
        f"selected_span_nonempty_verified={primorial.bool_text(audit['selected_span_nonempty_verified'])}",
        f"empty_class_eliminated={primorial.bool_text(audit['empty_class_eliminated'])}",
        f"four_class_reduction_closed={primorial.bool_text(audit['four_class_reduction_closed'])}",
        f"count_even_singleton_total={audit['count_even_singleton_total']}",
        f"count_odd_candidate_prime_total={audit['count_odd_candidate_prime_total']}",
        f"count_odd_candidate_lpf3_total={audit['count_odd_candidate_lpf3_total']}",
        f"count_odd_candidate_lpf5_total={audit['count_odd_candidate_lpf5_total']}",
        f"four_class_phase_control_closed={primorial.bool_text(audit['four_class_phase_control_closed'])}",
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
        "结论：empty-cell packet 被结构性消除，hole correction 从五类压为四类。剩余不是 carrier 是否存在，而是 even/prime/LPF3/LPF5 四个非空相位包的统一相消或吸收。",
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
        f"carrier_floor_map_no_skip_closed={primorial.bool_text(payload['carrier_floor_map_no_skip_closed'])}",
        f"selected_span_nonempty_closed={primorial.bool_text(payload['selected_span_nonempty_closed'])}",
        f"empty_hole_class_eliminated={primorial.bool_text(payload['empty_hole_class_eliminated'])}",
        f"four_class_hole_phase_identity_closed={primorial.bool_text(payload['four_class_hole_phase_identity_closed'])}",
        f"four_class_phase_control_closed={primorial.bool_text(payload['four_class_phase_control_closed'])}",
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
    print("empty_hole_class_eliminated=true")
    print("four_class_phase_control_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
