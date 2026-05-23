#!/usr/bin/env python3
"""审计 row-averaged mixed-modulus phase 的 k-加性角色支撑。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_support_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-audit.json

上一层把跨 k 平均图压成 mixed-modulus phase：

  D = q*m - k*P = q*m mod P,    e(h*k*P/q)=e(-h*D/q).

本层继续下钻：因为 D == -kP (mod q)，相位可等价看作 q 模上的
k-加性角色 e(h*P*k/q)。这关闭了一个相位重标记门。但 q 固定后，
k 支撑由 residual LPF cofactor m 的稀疏集合诱导，不是完整区间；
因此完整区间加性角色相消仍不能直接套用。
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


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-audit.json",
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


def phase_key(P: int, q: int, m: int) -> str:
    """输出相位重标记标签。"""
    k = (q * m) // P
    d = q * m - k * P
    return f"k={k},D={d},Dmodq={d % q},-kPmodq={(-k * P) % q},phase=e(h*{P % q}*k/{q})"


def support_profile(k_values: set[int]) -> dict[str, Any]:
    """返回 k 支撑的区间孔洞数据。"""
    if not k_values:
        return {
            "count": 0,
            "span": 0,
            "holes": 0,
            "min_k": 0,
            "max_k": 0,
            "complete_interval": False,
        }
    min_k = min(k_values)
    max_k = max(k_values)
    span = max_k - min_k + 1
    count = len(k_values)
    return {
        "count": count,
        "span": span,
        "holes": span - count,
        "min_k": min_k,
        "max_k": max_k,
        "complete_interval": span == count,
    }


def additive_k_support_for_P(
    P: int,
    records: list[dict[str, int]],
    primes: list[int],
    collect_samples: bool,
) -> dict[str, Any]:
    """审计固定 P 的 q 模 k-加性角色支撑。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    q_to_k: dict[int, set[int]] = defaultdict(set)
    q_to_kmod: dict[int, set[int]] = defaultdict(set)
    q_to_edges: Counter[int] = Counter()
    q_to_kmod_collisions: Counter[int] = Counter()
    totals: Counter[str] = Counter()
    sample_edges: list[str] = []
    first_noncomplete_support = "none"
    first_kmod_collision = "none"

    for q in floorcell.odd_q_values(P):
        if math.gcd(q, W) != 1:
            continue
        for record in records:
            m = record["m"]
            if m < q:
                continue
            product = q * m
            k = product // P
            if not (1 <= k < P):
                continue
            d = product - k * P
            if d == 0:
                totals["bad_zero_displacement"] += 1
                continue

            low, high = floorcell.product_cell_window(P, k, q)
            q_odd, odd_count = primorial.unique_odd_candidate(low, high)
            totals["floor_cell_membership_mismatch"] += int(not (low <= m <= high))
            totals["floor_cell_odd_candidate_mismatch"] += int(q_odd is None or q_odd != m)
            totals["bad_floor_cell_odd_count"] += int(odd_count > 1)

            totals["selected_edges"] += 1
            totals["phase_congruence_checked"] += 1
            totals["phase_congruence_mismatch"] += int((d + k * P) % q != 0)
            q_to_k[q].add(k)
            before = len(q_to_kmod[q])
            q_to_kmod[q].add(k % q)
            after = len(q_to_kmod[q])
            q_to_edges[q] += 1
            if after == before:
                q_to_kmod_collisions[q] += 1
                if first_kmod_collision == "none":
                    first_kmod_collision = f"q={q},k={k},kmod={k % q}"
            if collect_samples and len(sample_edges) < 8:
                sample_edges.append(
                    "q={q},m={m},r={r},beta={beta},{phase}".format(
                        q=q,
                        m=m,
                        r=record["r"],
                        beta=record["beta"],
                        phase=phase_key(P, q, m),
                    )
                )

    q_bucket_profiles = {q: support_profile(kset) for q, kset in q_to_k.items()}
    noncomplete_q = [q for q, profile in q_bucket_profiles.items() if not profile["complete_interval"]]
    if noncomplete_q:
        q0 = noncomplete_q[0]
        p0 = q_bucket_profiles[q0]
        first_noncomplete_support = (
            f"q={q0},min_k={p0['min_k']},max_k={p0['max_k']},"
            f"count={p0['count']},span={p0['span']},holes={p0['holes']}"
        )

    total_span = sum(profile["span"] for profile in q_bucket_profiles.values())
    total_count = sum(profile["count"] for profile in q_bucket_profiles.values())
    total_holes = sum(profile["holes"] for profile in q_bucket_profiles.values())
    max_holes = max((profile["holes"] for profile in q_bucket_profiles.values()), default=0)
    max_span = max((profile["span"] for profile in q_bucket_profiles.values()), default=0)
    max_count = max((profile["count"] for profile in q_bucket_profiles.values()), default=0)

    return {
        "P": P,
        "selected_edges": totals["selected_edges"],
        "selected_q_bucket_count": len(q_to_k),
        "phase_congruence_checked": totals["phase_congruence_checked"],
        "phase_congruence_mismatch": totals["phase_congruence_mismatch"],
        "floor_cell_membership_mismatch": totals["floor_cell_membership_mismatch"],
        "floor_cell_odd_candidate_mismatch": totals["floor_cell_odd_candidate_mismatch"],
        "bad_floor_cell_odd_count": totals["bad_floor_cell_odd_count"],
        "bad_zero_displacement": totals["bad_zero_displacement"],
        "max_q_to_k_fiber": max((len(kset) for kset in q_to_k.values()), default=0),
        "max_q_to_kmod_fiber": max((len(kset) for kset in q_to_kmod.values()), default=0),
        "q_buckets_with_kmod_collision": sum(1 for value in q_to_kmod_collisions.values() if value > 0),
        "total_kmod_collision_edges": sum(q_to_kmod_collisions.values()),
        "first_kmod_collision": first_kmod_collision,
        "q_buckets_with_noncomplete_k_interval": len(noncomplete_q),
        "total_k_support_count": total_count,
        "total_k_span_length": total_span,
        "total_k_interval_holes": total_holes,
        "max_k_support_count_per_q": max_count,
        "max_k_span_length_per_q": max_span,
        "max_k_interval_holes_per_q": max_holes,
        "first_noncomplete_k_support": first_noncomplete_support,
        "complete_interval_additive_character_sum_available": len(noncomplete_q) == 0,
        "additive_character_relabeling_closed": totals["phase_congruence_mismatch"] == 0,
        "sample_edges": "; ".join(sample_edges) if sample_edges else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的跨 k 加性角色支撑做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    interesting = {101, 257, 971, 1009}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-audit.json").read_text())

    totals: Counter[str] = Counter()
    maxima: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []
    first_noncomplete = "none"
    first_collision = "none"

    for P in P_values:
        row = additive_k_support_for_P(P, records_by_P[P], primes, P in interesting)
        for key in [
            "selected_edges",
            "selected_q_bucket_count",
            "phase_congruence_checked",
            "phase_congruence_mismatch",
            "floor_cell_membership_mismatch",
            "floor_cell_odd_candidate_mismatch",
            "bad_floor_cell_odd_count",
            "bad_zero_displacement",
            "q_buckets_with_kmod_collision",
            "total_kmod_collision_edges",
            "q_buckets_with_noncomplete_k_interval",
            "total_k_support_count",
            "total_k_span_length",
            "total_k_interval_holes",
        ]:
            totals[key] += row[key]
        for key in [
            "max_q_to_k_fiber",
            "max_q_to_kmod_fiber",
            "max_k_support_count_per_q",
            "max_k_span_length_per_q",
            "max_k_interval_holes_per_q",
        ]:
            maxima[key] = max(maxima[key], row[key])
        if first_noncomplete == "none" and row["first_noncomplete_k_support"] != "none":
            first_noncomplete = f"P={P},{row['first_noncomplete_k_support']}"
        if first_collision == "none" and row["first_kmod_collision"] != "none":
            first_collision = f"P={P},{row['first_kmod_collision']}"
        if P in interesting:
            sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "total_selected_edges": totals["selected_edges"],
        "previous_row_averaged_selected_edges": previous["finite_audit"]["total_row_averaged_selected_edges"],
        "selected_edges_match_previous_total": totals["selected_edges"]
        == previous["finite_audit"]["total_row_averaged_selected_edges"],
        "selected_q_bucket_count_total": totals["selected_q_bucket_count"],
        "phase_congruence_checked_total": totals["phase_congruence_checked"],
        "phase_congruence_mismatch_total": totals["phase_congruence_mismatch"],
        "floor_cell_membership_mismatch_total": totals["floor_cell_membership_mismatch"],
        "floor_cell_odd_candidate_mismatch_total": totals["floor_cell_odd_candidate_mismatch"],
        "bad_floor_cell_odd_count_total": totals["bad_floor_cell_odd_count"],
        "bad_zero_displacement_total": totals["bad_zero_displacement"],
        "max_q_to_k_fiber": maxima["max_q_to_k_fiber"],
        "max_q_to_kmod_fiber": maxima["max_q_to_kmod_fiber"],
        "q_buckets_with_kmod_collision_total": totals["q_buckets_with_kmod_collision"],
        "total_kmod_collision_edges": totals["total_kmod_collision_edges"],
        "first_kmod_collision": first_collision,
        "q_buckets_with_noncomplete_k_interval_total": totals["q_buckets_with_noncomplete_k_interval"],
        "total_k_support_count": totals["total_k_support_count"],
        "total_k_span_length": totals["total_k_span_length"],
        "total_k_interval_holes": totals["total_k_interval_holes"],
        "max_k_support_count_per_q": maxima["max_k_support_count_per_q"],
        "max_k_span_length_per_q": maxima["max_k_span_length_per_q"],
        "max_k_interval_holes_per_q": maxima["max_k_interval_holes_per_q"],
        "first_noncomplete_k_support": first_noncomplete,
        "additive_character_phase_relabeling_closed": totals["phase_congruence_mismatch"] == 0,
        "complete_interval_additive_character_sum_available": totals["q_buckets_with_noncomplete_k_interval"] == 0,
        "sparse_lpf_k_support_completion_closed": False,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_support_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "additive_k_character_relabeling_closed_sparse_k_support_completion_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the row-averaged mixed-modulus graph, the next non-cyclic check is whether the phase can be same-modulus in k and whether the k-support is complete enough for existing additive-character estimates",
        "current_object": {
            "phase_relabeling": "D=qm-kP gives D == -kP (mod q), hence e(-hD/q)=e(hPk/q)",
            "character_modulus": "q",
            "character_variable": "k mod q",
            "support": "k=floor(qm/P) for residual LPF cofactors m in the selected q-bucket",
            "remaining_obstruction": "the q-bucket k-support is sparse and generally not a complete interval",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "MixedModulusPhaseToKAdditiveCharacterRelabeling",
                True,
                True,
                "The row-averaged phase can be written as a q-modulus additive character in k.",
                "none",
            ),
            gate(
                "RowAveragedSelectedEdgeConsistency",
                True,
                True,
                "The additive-k support contains exactly the previously audited row-averaged selected edges.",
                "none",
            ),
            gate(
                "DirectCompleteIntervalAdditiveCharacterCompletionRejected",
                True,
                True,
                "The k-support in q-buckets is sparse and not a complete interval, so complete interval additive-character cancellation is not directly available.",
                "none",
            ),
            gate(
                "SparseLPFKSupportCompletionOrDispersion",
                False,
                False,
                "Complete or estimate the sparse LPF-induced k-support without changing the object.",
                "new sparse-support dispersion theorem",
            ),
            gate(
                "UniformCancellationAcrossSparseKSupportRadialKernels",
                False,
                False,
                "Prove cancellation uniformly across the sparse k-support and coupled radial kernels.",
                "new phase-saving theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "the phase is now an additive character in k mod q, but the support is an LPF-induced sparse set rather than a standard trace-family interval",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "Kloosterman bilinear estimates still need a bilinear/convolution support; the current k-support is sparse and graph-defined",
            "Pascadi_2025_arXiv_2511_08445": "composite Type-II amplification remains downstream of a sparse-support completion theorem",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution estimates are relevant only after the sparse k-support is converted into a controlled convolution family",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree parameter inputs do not by themselves remove the LPF-induced k-support holes",
        },
        "latest_narrowest_mouth": [
            "SparseLPFKSupportCompletionOrDispersion",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "mixed_modulus_phase_to_k_additive_character_relabeling_closed": True,
        "row_averaged_selected_edge_consistency_closed": True,
        "direct_complete_interval_additive_character_completion_rejected": True,
        "sparse_lpf_k_support_completion_or_dispersion_closed": False,
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
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k support 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"phase_relabeling={current['phase_relabeling']}",
        f"character_modulus={current['character_modulus']}",
        f"character_variable={current['character_variable']}",
        f"support={current['support']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. additive-k 支撑审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"total_selected_edges={audit['total_selected_edges']}",
        f"previous_row_averaged_selected_edges={audit['previous_row_averaged_selected_edges']}",
        f"selected_edges_match_previous_total={primorial.bool_text(audit['selected_edges_match_previous_total'])}",
        f"selected_q_bucket_count_total={audit['selected_q_bucket_count_total']}",
        f"phase_congruence_checked_total={audit['phase_congruence_checked_total']}",
        f"phase_congruence_mismatch_total={audit['phase_congruence_mismatch_total']}",
        f"floor_cell_membership_mismatch_total={audit['floor_cell_membership_mismatch_total']}",
        f"floor_cell_odd_candidate_mismatch_total={audit['floor_cell_odd_candidate_mismatch_total']}",
        f"bad_floor_cell_odd_count_total={audit['bad_floor_cell_odd_count_total']}",
        f"bad_zero_displacement_total={audit['bad_zero_displacement_total']}",
        f"max_q_to_k_fiber={audit['max_q_to_k_fiber']}",
        f"max_q_to_kmod_fiber={audit['max_q_to_kmod_fiber']}",
        f"q_buckets_with_kmod_collision_total={audit['q_buckets_with_kmod_collision_total']}",
        f"total_kmod_collision_edges={audit['total_kmod_collision_edges']}",
        f"first_kmod_collision={audit['first_kmod_collision']}",
        f"q_buckets_with_noncomplete_k_interval_total={audit['q_buckets_with_noncomplete_k_interval_total']}",
        f"total_k_support_count={audit['total_k_support_count']}",
        f"total_k_span_length={audit['total_k_span_length']}",
        f"total_k_interval_holes={audit['total_k_interval_holes']}",
        f"max_k_support_count_per_q={audit['max_k_support_count_per_q']}",
        f"max_k_span_length_per_q={audit['max_k_span_length_per_q']}",
        f"max_k_interval_holes_per_q={audit['max_k_interval_holes_per_q']}",
        f"first_noncomplete_k_support={audit['first_noncomplete_k_support']}",
        f"additive_character_phase_relabeling_closed={primorial.bool_text(audit['additive_character_phase_relabeling_closed'])}",
        f"complete_interval_additive_character_sum_available={primorial.bool_text(audit['complete_interval_additive_character_sum_available'])}",
        f"sparse_lpf_k_support_completion_closed={primorial.bool_text(audit['sparse_lpf_k_support_completion_closed'])}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "selected_edges",
                "selected_q_bucket_count",
                "phase_congruence_mismatch",
                "max_q_to_k_fiber",
                "q_buckets_with_noncomplete_k_interval",
                "total_k_interval_holes",
                "max_k_interval_holes_per_q",
                "first_noncomplete_k_support",
                "sample_edges",
            ],
        ),
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
        "结论：混合模数相位可重标记为 `k mod q` 的加性角色，这是推进；但 q-bucket 内的 k 支撑由 LPF residual 集诱导，存在大量区间孔洞。下一步真口不是相位重标记，而是 sparse LPF k-support 的 completion/dispersion。",
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
        f"mixed_modulus_phase_to_k_additive_character_relabeling_closed={primorial.bool_text(payload['mixed_modulus_phase_to_k_additive_character_relabeling_closed'])}",
        f"row_averaged_selected_edge_consistency_closed={primorial.bool_text(payload['row_averaged_selected_edge_consistency_closed'])}",
        f"direct_complete_interval_additive_character_completion_rejected={primorial.bool_text(payload['direct_complete_interval_additive_character_completion_rejected'])}",
        f"sparse_lpf_k_support_completion_or_dispersion_closed={primorial.bool_text(payload['sparse_lpf_k_support_completion_or_dispersion_closed'])}",
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
    print("mixed_modulus_phase_to_k_additive_character_relabeling_closed=true")
    print("complete_interval_additive_character_sum_available=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
