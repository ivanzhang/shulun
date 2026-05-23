#!/usr/bin/env python3
"""审计 Phi-LPF 的 LPF tail Type-II 义务。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_lpf_tail_typeii_obligation_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json

本层接在 LPF shell 与相邻互质奇偶陷阱之后。它把 30-wheel residual
写成 q*r*a 的同一行 reciprocal-window 图对象，并检查三个非循环事实：

1. q-m 分解是精确的 balanced 形状，但不是矩形盒，而是稀疏 reciprocal 图；
2. 固定 q 的 m 纤维至多 2 个点，固定 m 的 q 纤维至多 2 个点；
3. 固定 (q,r) 后，a 纤维至多 1 个点，因为 q*r>P。

因此 Ford--Maynard/Heath-Brown 型 Type-II 思路若要使用，必须提供
本文对象专用的 reciprocal-graph dispersion，而不能由相邻互质、普通
rough-number 密度或矩形双线性盒估计直接替代。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from prime_matrix_phi_lpf_fixed_wheel_residual_rough_composite_audit import (
    finite_delta_and_prime_count,
    is_prime_from_spf,
)
from prime_matrix_phi_lpf_primorial_wheel_limit_audit import (
    DATA,
    DOCS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    bool_text,
    cell,
    high_band_lower_k,
    next_prime_after_half,
    next_prime_at_least,
    prime_flags,
    primes_from_spf,
    reciprocal_window_for_q,
    shadow_free_cap,
    spf_table,
    upper_band_first_k,
)


SLUG = "prime-matrix-phi-lpf-lpf-tail-typeii-obligation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-lpf-shell-decrement-audit.json",
    DOCS / "prime-matrix-phi-lpf-adjacent-coprime-parity-trap-audit.json",
    DOCS / "prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.json",
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


def is_wheel30_residual_m(spf: list[int], m: int) -> bool:
    """判断 m 是否属于 30-wheel 后仍存活的合成 cofactor。"""
    return (
        m > 1
        and not is_prime_from_spf(spf, m)
        and m % 2 != 0
        and m % 3 != 0
        and m % 5 != 0
    )


def compact_counter(counter: Counter[int], limit: int = 10) -> dict[str, int]:
    """压缩整数计数器，避免证书过大。"""
    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    result = {str(key): value for key, value in ordered[:limit]}
    remaining = sum(value for _, value in ordered[limit:])
    if remaining:
        result["other"] = remaining
    return result


def density_record(row: dict[str, Any]) -> dict[str, Any]:
    """压缩 reciprocal 图密度读数。"""
    return {
        "P": row["P"],
        "k": row["k"],
        "W_int": row["integer_window_capacity"],
        "q_count": row["high_q_prime_count"],
        "m_span": row["m_span"],
        "rectangle_hull_area": row["rectangle_hull_area"],
        "support_density_num": row["support_density_num"],
        "support_density_den": row["support_density_den"],
        "support_density_float": row["support_density_float"],
    }


def row_typeii_profile(
    P: int,
    k: int,
    spf: list[int],
    primes_2p: list[int],
    direct_prime_count: int | None = None,
) -> dict[str, Any]:
    """构造一行的 LPF-tail Type-II 义务读数。"""
    row_start = k * P
    row_end = (k + 1) * P
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]

    q_window_lengths: Counter[int] = Counter()
    q_to_m: dict[int, list[int]] = {}
    m_to_q: defaultdict[int, list[int]] = defaultdict(list)
    qr_to_a: defaultdict[tuple[int, int], list[int]] = defaultdict(list)
    lpf_shells: Counter[int] = Counter()
    quotient_a_bins: Counter[int] = Counter()
    residual_items: list[dict[str, int]] = []
    all_m_values: list[int] = []
    failures: list[dict[str, Any]] = []
    min_qr_minus_p: int | None = None

    for q in high_q_primes:
        lower, upper = reciprocal_window_for_q(P, k, q)
        values = list(range(lower, upper + 1)) if lower <= upper else []
        q_window_lengths[len(values)] += 1
        q_to_m[q] = values
        all_m_values.extend(values)
        for m in values:
            m_to_q[m].append(q)
            n = q * m
            if not (row_start < n < row_end):
                failures.append({"type": "row_window_failure", "P": P, "k": k, "q": q, "m": m})
            if not is_wheel30_residual_m(spf, m):
                continue
            r = spf[m]
            a = m // r
            qr_to_a[(q, r)].append(a)
            lpf_shells[r] += 1
            quotient_a_bins[a.bit_length()] += 1
            min_qr_minus_p = q * r - P if min_qr_minus_p is None else min(min_qr_minus_p, q * r - P)
            residual_items.append({"q": q, "m": m, "r": r, "a": a, "n": n})
            if not (r >= 7 and a >= r and m == r * a):
                failures.append({"type": "lpf_factorization_failure", "P": P, "k": k, "q": q, "m": m})
            if not (row_start < q * r * a < row_end):
                failures.append({"type": "triple_row_failure", "P": P, "k": k, "q": q, "r": r, "a": a})

    max_q_fiber = max((len(values) for values in q_to_m.values()), default=0)
    max_m_fiber = max((len(values) for values in m_to_q.values()), default=0)
    max_qr_fiber = max((len(values) for values in qr_to_a.values()), default=0)
    multiple_q_fibers = sum(1 for values in q_to_m.values() if len(values) > 2)
    multiple_m_fibers = sum(1 for values in m_to_q.values() if len(values) > 2)
    multiple_qr_fibers = sum(1 for values in qr_to_a.values() if len(values) > 1)

    m_min = min(all_m_values) if all_m_values else None
    m_max = max(all_m_values) if all_m_values else None
    m_span = (m_max - m_min + 1) if m_min is not None and m_max is not None else 0
    hull_area = len(high_q_primes) * m_span
    integer_capacity = len(all_m_values)
    support_density = integer_capacity / hull_area if hull_area else None

    return {
        "P": P,
        "k": k,
        "p_half": next_prime_after_half(P, primes_2p),
        "in_shadow_free_subband": k <= shadow_free_cap(P),
        "in_upper_band": k >= upper_band_first_k(P),
        "in_bhp_remaining_high_band": k >= high_band_lower_k(P),
        "direct_prime_count": direct_prime_count,
        "high_q_prime_count": len(high_q_primes),
        "integer_window_capacity": integer_capacity,
        "residual_count_R30": len(residual_items),
        "prime_count_minus_R30": None if direct_prime_count is None else direct_prime_count - len(residual_items),
        "m_min": m_min,
        "m_max": m_max,
        "m_span": m_span,
        "rectangle_hull_area": hull_area,
        "support_density_num": integer_capacity,
        "support_density_den": hull_area,
        "support_density_float": support_density,
        "q_window_length_histogram": compact_counter(q_window_lengths),
        "lpf_shell_histogram": compact_counter(lpf_shells),
        "quotient_a_bit_length_histogram": compact_counter(quotient_a_bins),
        "max_m_values_per_q": max_q_fiber,
        "max_q_values_per_m": max_m_fiber,
        "max_a_values_per_qr": max_qr_fiber,
        "q_fibers_longer_than_2": multiple_q_fibers,
        "m_fibers_longer_than_2": multiple_m_fibers,
        "qr_fibers_longer_than_1": multiple_qr_fibers,
        "min_qr_minus_P": min_qr_minus_p,
        "all_q_m_windows_have_at_most_two_points": max_q_fiber <= 2 and multiple_q_fibers == 0,
        "all_m_q_reverse_fibers_have_at_most_two_points": max_m_fiber <= 2 and multiple_m_fibers == 0,
        "all_qr_a_fibers_have_at_most_one_point": max_qr_fiber <= 1 and multiple_qr_fibers == 0,
        "all_residual_qr_steps_exceed_row_length": min_qr_minus_p is None or min_qr_minus_p > 0,
        "failure_count": len(failures),
        "failures": failures[:5],
    }


def compact_row(row: dict[str, Any]) -> dict[str, Any]:
    """压缩行读数。"""
    return {
        "P": row["P"],
        "k": row["k"],
        "N": row["direct_prime_count"],
        "W_int": row["integer_window_capacity"],
        "R30": row["residual_count_R30"],
        "N_minus_R30": row["prime_count_minus_R30"],
        "q_count": row["high_q_prime_count"],
        "m_span": row["m_span"],
        "support_density": row["support_density_float"],
        "max_m_per_q": row["max_m_values_per_q"],
        "max_q_per_m": row["max_q_values_per_m"],
        "max_a_per_qr": row["max_a_values_per_qr"],
        "min_qr_minus_P": row["min_qr_minus_P"],
        "lpf_shells": row["lpf_shell_histogram"],
    }


def bool_count(rows: list[dict[str, Any]], key: str) -> int:
    """统计布尔字段为真的行数。"""
    return sum(1 for row in rows if row[key])


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总审计行。"""
    active_rows = [row for row in rows if row["residual_count_R30"] > 0]
    max_residual_row = max(active_rows, key=lambda row: row["residual_count_R30"]) if active_rows else None
    min_prime_candidates = [
        row for row in active_rows if row["prime_count_minus_R30"] is not None
    ] or [row for row in rows if row["prime_count_minus_R30"] is not None]
    min_prime_minus_row = min(
        min_prime_candidates,
        key=lambda row: row["prime_count_minus_R30"],
        default=None,
    )
    sparsest_row = min(
        (row for row in rows if row["support_density_float"] is not None),
        key=lambda row: row["support_density_float"],
        default=None,
    )
    sample_keys = {(29, 28), (101, 100), (257, 256), (971, 936), (1009, 1008)}
    total_prime_count = sum(row["direct_prime_count"] or 0 for row in rows)
    total_r30 = sum(row["residual_count_R30"] for row in rows)
    return {
        "row_count": len(rows),
        "active_residual_row_count": len(active_rows),
        "total_R30": total_r30,
        "total_direct_prime_count": total_prime_count if total_prime_count else None,
        "total_prime_count_minus_R30": (
            total_prime_count - total_r30 if total_prime_count else None
        ),
        "all_q_m_windows_have_at_most_two_points": bool_count(
            rows, "all_q_m_windows_have_at_most_two_points"
        )
        == len(rows),
        "all_m_q_reverse_fibers_have_at_most_two_points": bool_count(
            rows, "all_m_q_reverse_fibers_have_at_most_two_points"
        )
        == len(rows),
        "all_qr_a_fibers_have_at_most_one_point": bool_count(
            rows, "all_qr_a_fibers_have_at_most_one_point"
        )
        == len(rows),
        "all_residual_qr_steps_exceed_row_length": bool_count(
            rows, "all_residual_qr_steps_exceed_row_length"
        )
        == len(rows),
        "max_residual_row": compact_row(max_residual_row) if max_residual_row else None,
        "minimum_prime_minus_R30_row": compact_row(min_prime_minus_row) if min_prime_minus_row else None,
        "sparsest_reciprocal_graph_row": density_record(sparsest_row) if sparsest_row else None,
        "sample_rows": [compact_row(row) for row in rows if (row["P"], row["k"]) in sample_keys],
        "failure_rows": [compact_row(row) for row in rows if row["failure_count"] > 0][:10],
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(max_prime * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    rows: list[dict[str, Any]] = []
    for P in primes:
        if P < 11:
            continue
        p_half = next_prime_after_half(P, primes_2p)
        for k in range(2, P):
            _, direct = finite_delta_and_prime_count(P, k, spf, p_half)
            rows.append(row_typeii_profile(P, k, spf, primes_2p, direct))
    summary = summarize_rows(rows)
    summary["max_prime"] = max_prime
    summary["finite_evidence_not_used_as_global_proof"] = True
    return summary


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的 Type-II 义务读数。"""
    max_seed = max(seeds) + 10000
    spf = spf_table(2 * max_seed)
    flags = prime_flags(2 * max_seed)
    rows: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        primes_2p = primes_from_spf(spf, 2 * P)
        k_values = sorted({2, P // 4, P // 2, max(2, P - P // 21), P - 1})
        for k in k_values:
            rows.append(row_typeii_profile(P, k, spf, primes_2p, None))
    summary = summarize_rows(rows)
    summary["sample_seeds"] = seeds
    summary["sample_count"] = len(rows)
    summary["large_samples_are_evidence_not_global_proof"] = True
    return summary


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "LPFTailTripleRepresentation",
            True,
            True,
            "30-wheel residual 精确写成 q*r*a，其中 r=LPF(m)>=7 且 a 为 r-rough。",
            "R30=sum_{q,r,a} 1_{kP<qra<(k+1)P}",
        ),
        gate(
            "ReciprocalGraphThinFibers",
            True,
            True,
            "同一行中固定 q 至多两个 m，固定 m 至多两个 q，固定 (q,r) 至多一个 a。",
            "graph-thin, not rectangular Type-II box",
        ),
        gate(
            "QuotientFiberCancellationAvailable",
            False,
            False,
            "固定 (q,r) 的 a 纤维只有一个点，不能在该纤维内部产生 Type-II 抵消。",
            "cancellation must run across the moving q-r graph",
        ),
        gate(
            "FordMaynardSieveAppliesDirectly",
            False,
            False,
            "prime-producing sieve 需要目标序列的 Type-I/II 输入；本层只给出 exact object 与义务。",
            "same-row reciprocal-window Type-II theorem required",
        ),
        gate(
            "PrimeCountDominatesLPFTailShellSumProved",
            False,
            False,
            "有限审计中 N-R30 为正，但未证明所有 P,k 的点态支配。",
            "PrimeCountDominatesLPFTailShellSum",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层不证明 H_P、外部引理版或内部自足版无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def row_table(rows: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown 表。"""
    lines = [
        "| P | k | N | W_int | R30 | N-R30 | q count | m span | support density | max m/q | max q/m | max a/(q,r) | min qr-P |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        density = row["support_density"]
        density_text = "" if density is None else f"{density:.6g}"
        lines.append(
            f"| {row['P']} | {row['k']} | {cell(row['N'])} | {row['W_int']} | "
            f"{row['R30']} | {cell(row['N_minus_R30'])} | {row['q_count']} | "
            f"{row['m_span']} | {density_text} | {row['max_m_per_q']} | "
            f"{row['max_q_per_m']} | {row['max_a_per_qr']} | {cell(row['min_qr_minus_P'])} |"
        )
    return "\n".join(lines)


def gates_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=bool_text(item["closed"]),
                proved=bool_text(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    finite = finite_audit()
    large = large_sample_audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_lpf_tail_typeii_obligation_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "lpf_tail_reduced_to_same_row_reciprocal_graph_typeii_obligation",
        "definitions": {
            "R30_triple": (
                "q prime in (P/2,P), m=r*a in I_q(P,k), r=LPF(m)>=7, "
                "a>=r and a is r-rough"
            ),
            "thin_q_fiber": "for fixed q, I_q(P,k) has at most two integer m values",
            "thin_reverse_fiber": "for fixed m>q>P/2, the admissible q interval has length <2",
            "one_point_quotient_fiber": "for fixed q,r, the a interval has length P/(q*r)<1",
            "typeii_obligation": "prove signed dispersion on this reciprocal graph, not on a full rectangle",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "external_frontier_note": (
            "Runbo Li type x^0.52 pointwise short-interval input is still above the x^1/2 row scale; "
            "Ford--Maynard prime-producing sieve technology becomes relevant only after Type-I/II "
            "estimates are proved for the exact same-row reciprocal graph."
        ),
        "next_direct_attack_target": (
            "SameRowReciprocalWindowTypeIIDispersionForLPFTail "
            "OR PrimeCountDominatesLPFTailShellSum "
            "OR SquarePhaseEndpointLowerBound"
        ),
        "lpf_tail_triple_representation_closed": True,
        "reciprocal_graph_thin_fibers_closed": True,
        "quotient_fiber_cancellation_available": False,
        "external_prime_producing_sieve_applies_directly": False,
        "prime_count_dominates_lpf_tail_shell_sum_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    finite = payload["finite_audit"]
    large = payload["large_sample_audit"]
    lines = [
        "# Prime Matrix Phi-LPF LPF tail Type-II obligation 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "`30-wheel` 后的 LPF tail residual 可精确写成三变量对象：",
        "",
        "```text",
        "R_30(P,k)=# {(q,r,a): P/2<q<P, q prime, m=r*a in I_q(P,k),",
        "                 r=LPF(m)>=7, a>=r, a is r-rough }",
        "```",
        "",
        "但这个对象不是普通矩形 Type-II 盒。它是同一行 reciprocal graph：",
        "",
        "```text",
        "I_q(P,k)=[max(q, floor(kP/q)+1), min(2P-1, floor(((k+1)P-1)/q))]",
        "# I_q(P,k) <= 2,             because P/q < 2",
        "# {q: m in I_q(P,k)} <= 2,   because P/m < 2",
        "# {a: kP<q*r*a<(k+1)P} <= 1, because P/(q*r)<1",
        "```",
        "",
        "所以 `q,m` 分解形状上接近平衡，但支撑是极稀疏图；`q,r,a` 分解中",
        "固定 `(q,r)` 的 quotient 纤维只有一个点，不能在该纤维内部产生抵消。",
        "真正需要的是跨越移动 reciprocal graph 的同对象 signed dispersion。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"active_residual_row_count={finite['active_residual_row_count']}",
        f"total_R30={finite['total_R30']}",
        f"total_direct_prime_count={finite['total_direct_prime_count']}",
        f"total_prime_count_minus_R30={finite['total_prime_count_minus_R30']}",
        f"all_q_m_windows_have_at_most_two_points={bool_text(finite['all_q_m_windows_have_at_most_two_points'])}",
        f"all_m_q_reverse_fibers_have_at_most_two_points={bool_text(finite['all_m_q_reverse_fibers_have_at_most_two_points'])}",
        f"all_qr_a_fibers_have_at_most_one_point={bool_text(finite['all_qr_a_fibers_have_at_most_one_point'])}",
        f"all_residual_qr_steps_exceed_row_length={bool_text(finite['all_residual_qr_steps_exceed_row_length'])}",
        f"finite_evidence_not_used_as_global_proof={bool_text(finite['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "代表样本：",
        "",
        row_table(finite["sample_rows"]),
        "",
        "最大 residual 行：",
        "",
        row_table([finite["max_residual_row"]]),
        "",
        "有限 active residual 最小 `N-R30` 行：",
        "",
        row_table([finite["minimum_prime_minus_R30_row"]]),
        "",
        "最稀疏 reciprocal graph 行：",
        "",
        "```text",
        f"P={finite['sparsest_reciprocal_graph_row']['P']}, k={finite['sparsest_reciprocal_graph_row']['k']}",
        f"W_int={finite['sparsest_reciprocal_graph_row']['W_int']}",
        f"q_count={finite['sparsest_reciprocal_graph_row']['q_count']}",
        f"m_span={finite['sparsest_reciprocal_graph_row']['m_span']}",
        f"rectangle_hull_area={finite['sparsest_reciprocal_graph_row']['rectangle_hull_area']}",
        f"support_density={finite['sparsest_reciprocal_graph_row']['support_density_float']:.8g}",
        "```",
        "",
        "## 3. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"active_residual_row_count={large['active_residual_row_count']}",
        f"total_R30={large['total_R30']}",
        f"all_q_m_windows_have_at_most_two_points={bool_text(large['all_q_m_windows_have_at_most_two_points'])}",
        f"all_m_q_reverse_fibers_have_at_most_two_points={bool_text(large['all_m_q_reverse_fibers_have_at_most_two_points'])}",
        f"all_qr_a_fibers_have_at_most_one_point={bool_text(large['all_qr_a_fibers_have_at_most_one_point'])}",
        f"all_residual_qr_steps_exceed_row_length={bool_text(large['all_residual_qr_steps_exceed_row_length'])}",
        f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        "## 4. 外部定理验收边界",
        "",
        "短区间素数的 `x^0.52` 点态输入在 `x=P^2` 上仍给 `P^1.04`，",
        "未到本文行长 `P=x^1/2`。Ford--Maynard 型 prime-producing sieve",
        "说明破奇偶通常需要 Type-I/Type-II 或双线性信息，但本层显示所需对象不是",
        "普通矩形盒，而是同一行 reciprocal graph。因此必须新增：",
        "",
        "```text",
        "SameRowReciprocalWindowTypeIIDispersionForLPFTail",
        "```",
        "",
        "它要直接支付 `N(P,k)-R_30(P,k)>0` 或更强的 LPF tail shell 支配。",
        "",
        "## 5. 判定表",
        "",
        gates_markdown(payload["gates"]),
        "",
        "## 6. 当前最窄口",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "```text",
        f"lpf_tail_triple_representation_closed={bool_text(payload['lpf_tail_triple_representation_closed'])}",
        f"reciprocal_graph_thin_fibers_closed={bool_text(payload['reciprocal_graph_thin_fibers_closed'])}",
        f"quotient_fiber_cancellation_available={bool_text(payload['quotient_fiber_cancellation_available'])}",
        f"external_prime_producing_sieve_applies_directly={bool_text(payload['external_prime_producing_sieve_applies_directly'])}",
        f"prime_count_dominates_lpf_tail_shell_sum_proved={bool_text(payload['prime_count_dominates_lpf_tail_shell_sum_proved'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
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
    print("reciprocal_graph_thin_fibers_closed=true")
    print("external_prime_producing_sieve_applies_directly=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
