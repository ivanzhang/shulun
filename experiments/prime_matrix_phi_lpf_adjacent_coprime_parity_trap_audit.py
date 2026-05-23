#!/usr/bin/env python3
"""审计 Phi-LPF residual 的相邻互质与商相邻互质路线。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_adjacent_coprime_parity_trap_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-adjacent-coprime-parity-trap-audit.json

本层检查用户提示中的相邻互质与 quotient-adjacent coprime 思路。结论：
在 30-wheel residual 中，q、m、r=LPF(m)、a=m/r 都为奇数，且 r>=7。
因此 qm±1、m±1、a±1 都是大于 2 的偶数；它们虽与原对象相邻互质，
但被奇偶性直接强迫为合数。商相邻提升 n=q*r*a -> q*r*(a±1)
的步长为 q*r>P，也不留在同一行。
"""

from __future__ import annotations

import hashlib
import json
from math import gcd
from pathlib import Path
from typing import Any

from prime_matrix_phi_lpf_primorial_wheel_limit_audit import (
    DATA,
    DOCS,
    LARGE_SAMPLE_SEEDS,
    MAX_PRIME_AUDIT,
    ROOT,
    bool_text,
    candidate_m_values,
    cell,
    next_prime_at_least,
    prime_flags,
    primes_from_spf,
    spf_table,
)


SLUG = "prime-matrix-phi-lpf-adjacent-coprime-parity-trap"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-lpf-shell-decrement-audit.json",
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


def is_prime_from_spf(spf: list[int], value: int) -> bool:
    """用 SPF 表判断素数。"""
    return value >= 2 and spf[value] == value


def is_wheel30_residual_m(spf: list[int], m: int) -> bool:
    """判断 m 是否属于 30-wheel 后的合成 residual cofactor。"""
    return (
        m > 1
        and not is_prime_from_spf(spf, m)
        and m % 2 != 0
        and m % 3 != 0
        and m % 5 != 0
    )


def residual_candidates_for_row(P: int, k: int, spf: list[int], primes_2p: list[int]) -> list[dict[str, int]]:
    """列出一行的 30-wheel residual 候选。"""
    high_q_primes = [q for q in primes_2p if P // 2 < q < P]
    candidates: list[dict[str, int]] = []
    for q in high_q_primes:
        for m in candidate_m_values(P, k, [q]):
            if not is_wheel30_residual_m(spf, m):
                continue
            r = spf[m]
            a = m // r
            candidates.append({"q": q, "m": m, "r": r, "a": a, "n": q * m})
    return candidates


def analyze_row(P: int, k: int, spf: list[int], primes_2p: list[int]) -> dict[str, Any]:
    """分析单行相邻互质与商相邻互质。"""
    row_start = k * P
    row_end = (k + 1) * P
    candidates = residual_candidates_for_row(P, k, spf, primes_2p)
    same_row_adjacent_slots: set[int] = set()
    same_row_adjacent_composite_slots: set[int] = set()
    failures: list[dict[str, Any]] = []
    endpoint_single_neighbor_count = 0
    two_neighbor_count = 0
    cofactor_adjacent_checked = 0
    quotient_adjacent_checked = 0
    quotient_lift_inside_count = 0

    for item in candidates:
        q = item["q"]
        m = item["m"]
        r = item["r"]
        a = item["a"]
        n = item["n"]

        if not (q % 2 == 1 and m % 2 == 1 and r >= 7 and r % 2 == 1 and a % 2 == 1):
            failures.append({"type": "oddness_or_lpf_failure", **item})

        adjacent_same_row = [value for value in (n - 1, n + 1) if row_start < value < row_end]
        if len(adjacent_same_row) == 1:
            endpoint_single_neighbor_count += 1
        elif len(adjacent_same_row) == 2:
            two_neighbor_count += 1
        for value in adjacent_same_row:
            same_row_adjacent_slots.add(value)
            if gcd(n, value) != 1 or value % 2 != 0 or value <= 2:
                failures.append({"type": "same_row_adjacent_not_even_coprime", "value": value, **item})
            else:
                same_row_adjacent_composite_slots.add(value)

        for value in (m - 1, m + 1):
            cofactor_adjacent_checked += 1
            if gcd(m, value) != 1 or value % 2 != 0 or value <= 2:
                failures.append({"type": "cofactor_adjacent_not_even_coprime", "value": value, **item})

        for value in (a - 1, a + 1):
            quotient_adjacent_checked += 1
            if gcd(a, value) != 1 or value % 2 != 0 or value <= 2:
                failures.append({"type": "quotient_adjacent_not_even_coprime", "value": value, **item})
            lift = q * r * value
            if row_start < lift < row_end:
                quotient_lift_inside_count += 1
                failures.append({"type": "quotient_adjacent_lift_inside_row", "lift": lift, **item})
            if q * r <= P:
                failures.append({"type": "quotient_lift_step_not_larger_than_row", **item})

    residual_count = len(candidates)
    return {
        "P": P,
        "k": k,
        "residual_count_R30": residual_count,
        "same_row_adjacent_slot_count": len(same_row_adjacent_slots),
        "same_row_adjacent_forced_even_composite_slot_count": len(same_row_adjacent_composite_slots),
        "same_row_adjacent_prime_shadow_count": 0,
        "endpoint_single_neighbor_count": endpoint_single_neighbor_count,
        "two_neighbor_count": two_neighbor_count,
        "cofactor_adjacent_checked": cofactor_adjacent_checked,
        "cofactor_adjacent_prime_shadow_count": 0,
        "quotient_adjacent_checked": quotient_adjacent_checked,
        "quotient_adjacent_prime_shadow_count": 0,
        "quotient_lift_inside_row_count": quotient_lift_inside_count,
        "all_adjacent_coprime_but_even_composite": not failures,
        "failure_count": len(failures),
        "failures": failures[:5],
    }


def compact_row(row: dict[str, Any]) -> dict[str, Any]:
    """压缩行读数。"""
    return {
        "P": row["P"],
        "k": row["k"],
        "R30": row["residual_count_R30"],
        "same_row_slots": row["same_row_adjacent_slot_count"],
        "same_row_prime_shadows": row["same_row_adjacent_prime_shadow_count"],
        "cofactor_checked": row["cofactor_adjacent_checked"],
        "quotient_checked": row["quotient_adjacent_checked"],
        "quotient_lift_inside": row["quotient_lift_inside_row_count"],
    }


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总审计行。"""
    active_rows = [row for row in rows if row["residual_count_R30"] > 0]
    max_residual_row = max(active_rows, key=lambda row: row["residual_count_R30"]) if active_rows else None
    max_adjacent_slot_row = (
        max(active_rows, key=lambda row: row["same_row_adjacent_slot_count"]) if active_rows else None
    )
    sample_keys = {(29, 28), (101, 100), (257, 256), (971, 936), (1009, 1008)}
    sample_rows = [compact_row(row) for row in rows if (row["P"], row["k"]) in sample_keys]
    return {
        "row_count": len(rows),
        "active_residual_row_count": len(active_rows),
        "total_R30": sum(row["residual_count_R30"] for row in rows),
        "total_same_row_adjacent_slots": sum(row["same_row_adjacent_slot_count"] for row in rows),
        "total_same_row_adjacent_prime_shadows": sum(row["same_row_adjacent_prime_shadow_count"] for row in rows),
        "total_cofactor_adjacent_prime_shadows": sum(row["cofactor_adjacent_prime_shadow_count"] for row in rows),
        "total_quotient_adjacent_prime_shadows": sum(row["quotient_adjacent_prime_shadow_count"] for row in rows),
        "total_quotient_lift_inside_row": sum(row["quotient_lift_inside_row_count"] for row in rows),
        "all_active_adjacent_coprime_but_even_composite": all(
            row["all_adjacent_coprime_but_even_composite"] for row in active_rows
        ),
        "max_residual_row": compact_row(max_residual_row) if max_residual_row else None,
        "max_adjacent_slot_row": compact_row(max_adjacent_slot_row) if max_adjacent_slot_row else None,
        "sample_rows": sample_rows,
        "failure_rows": [compact_row(row) for row in rows if row["failure_count"] > 0][:10],
    }


def finite_audit(max_prime: int = MAX_PRIME_AUDIT) -> dict[str, Any]:
    """有限审计；只作一致性检查，不作全局证明。"""
    spf = spf_table(2 * max_prime)
    primes = primes_from_spf(spf, max_prime)
    primes_2p = primes_from_spf(spf, 2 * max_prime)
    rows: list[dict[str, Any]] = []
    for P in primes:
        if P < 11:
            continue
        for k in range(2, P):
            rows.append(analyze_row(P, k, spf, primes_2p))
    summary = summarize_rows(rows)
    summary["max_prime"] = max_prime
    summary["finite_evidence_not_used_as_global_proof"] = True
    return summary


def large_sample_audit(seeds: list[int] = LARGE_SAMPLE_SEEDS) -> dict[str, Any]:
    """抽样较大 P 的相邻互质陷阱读数。"""
    max_seed = max(seeds) + 10000
    spf = spf_table(2 * max_seed)
    flags = prime_flags(2 * max_seed)
    rows: list[dict[str, Any]] = []
    for seed in seeds:
        P = next_prime_at_least(seed, flags)
        primes_2p = primes_from_spf(spf, 2 * P)
        k_values = sorted({2, P // 4, P // 2, max(2, P - P // 21), P - 1})
        for k in k_values:
            rows.append(analyze_row(P, k, spf, primes_2p))
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
            "AdjacentCoprimeIdentityClosed",
            True,
            True,
            "对 n=qm、cofactor m 与 quotient a=m/LPF(m)，相邻数与原数互质。",
            "gcd(x,x±1)=1",
        ),
        gate(
            "Post30WheelAdjacentParityTrapClosed",
            True,
            True,
            "30-wheel residual 中 q,m,r,a 全为奇数且 r>=7，所以 n±1、m±1、a±1 全是大于 2 的偶数合数。",
            "adjacent coprime does not imply prime",
        ),
        gate(
            "QuotientAdjacentLiftLeavesRow",
            True,
            True,
            "商相邻提升的步长为 q*LPF(m)>P，不能同时留在同一长度 P 行内。",
            "quotient-adjacent same-row transfer closed false",
        ),
        gate(
            "AdjacentCoprimePrimePaymentProved",
            False,
            False,
            "相邻互质路线在 30-wheel residual 上给出 0 个同排相邻素数影子。",
            "PrimeCountDominatesLPFTailShellSum still required",
        ),
        gate(
            "ExternalPrimeProducingSieveAppliesDirectly",
            False,
            False,
            "Ford--Maynard 型 prime-producing sieve 需要 Type-I/II 输入；本文尚无 reciprocal-window 同对象 Type-II 包。",
            "same-object bilinear/dispersion theorem required",
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
        "| P | k | R30 | same-row adjacent slots | adjacent prime shadows | cofactor checked | quotient checked | quotient lifts inside row |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['P']} | {row['k']} | {row['R30']} | {row['same_row_slots']} | "
            f"{row['same_row_prime_shadows']} | {row['cofactor_checked']} | "
            f"{row['quotient_checked']} | {row['quotient_lift_inside']} |"
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
        "certificate_type": "prime_matrix_phi_lpf_adjacent_coprime_parity_trap_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "adjacent_coprime_and_quotient_adjacent_routes_trapped_by_parity_after_30_wheel",
        "definitions": {
            "residual_object": "30-wheel rough-composite residual candidate n=q*m",
            "lpf_quotient": "m=r*a, r=LPF(m), r>=7",
            "adjacent_coprime": "gcd(x,x±1)=1",
            "parity_trap": "q,m,r,a are odd; n±1,m±1,a±1 are even >2",
            "quotient_lift": "q*r*(a±1)=n±q*r with q*r>P",
        },
        "finite_audit": finite,
        "large_sample_audit": large,
        "gates": build_gates(),
        "external_frontier_note": (
            "Prime-producing sieve frameworks such as Ford--Maynard are relevant only after "
            "Type-I/II or bilinear information is supplied for the exact reciprocal-window object."
        ),
        "next_direct_attack_target": (
            "PrimeCountDominatesLPFTailShellSum OR same-object Type-II signed dispersion "
            "OR square-phase endpoint lower bound"
        ),
        "adjacent_coprime_identity_closed": True,
        "post30_adjacent_parity_trap_closed": True,
        "quotient_adjacent_lift_leaves_row_closed": True,
        "adjacent_coprime_prime_payment_proved": False,
        "external_prime_producing_sieve_applies_directly": False,
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
        "# Prime Matrix Phi-LPF adjacent-coprime parity-trap 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "在 `30-wheel` residual 中，`m` 没有 `2,3,5` 因子且为合数，故 `r=LPF(m)>=7`。",
        "于是 `q,m,r,a=m/r` 全为奇数。虽然相邻数总是互质：",
        "",
        "```text",
        "gcd(qm, qm±1)=1",
        "gcd(m, m±1)=1",
        "gcd(a, a±1)=1",
        "```",
        "",
        "但这些相邻数全部被奇偶性强迫为合数：",
        "",
        "```text",
        "qm±1, m±1, a±1 are even and >2",
        "```",
        "",
        "商相邻提升也不能留在同一行：",
        "",
        "```text",
        "q*r*(a±1)=q*r*a ± q*r",
        "q*r > (P/2)*7 > P",
        "```",
        "",
        "因此相邻互质和商相邻互质是真刚性，但不是素数支付通道。",
        "",
        "## 2. 有限审计",
        "",
        "```text",
        f"max_prime={finite['max_prime']}",
        f"row_count={finite['row_count']}",
        f"active_residual_row_count={finite['active_residual_row_count']}",
        f"total_R30={finite['total_R30']}",
        f"total_same_row_adjacent_slots={finite['total_same_row_adjacent_slots']}",
        f"total_same_row_adjacent_prime_shadows={finite['total_same_row_adjacent_prime_shadows']}",
        f"total_cofactor_adjacent_prime_shadows={finite['total_cofactor_adjacent_prime_shadows']}",
        f"total_quotient_adjacent_prime_shadows={finite['total_quotient_adjacent_prime_shadows']}",
        f"total_quotient_lift_inside_row={finite['total_quotient_lift_inside_row']}",
        f"all_active_adjacent_coprime_but_even_composite={bool_text(finite['all_active_adjacent_coprime_but_even_composite'])}",
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
        "## 3. 大尺度抽样",
        "",
        "```text",
        f"sample_seeds={large['sample_seeds']}",
        f"sample_count={large['sample_count']}",
        f"active_residual_row_count={large['active_residual_row_count']}",
        f"total_R30={large['total_R30']}",
        f"total_same_row_adjacent_prime_shadows={large['total_same_row_adjacent_prime_shadows']}",
        f"total_quotient_lift_inside_row={large['total_quotient_lift_inside_row']}",
        f"all_active_adjacent_coprime_but_even_composite={bool_text(large['all_active_adjacent_coprime_but_even_composite'])}",
        f"large_samples_are_evidence_not_global_proof={bool_text(large['large_samples_are_evidence_not_global_proof'])}",
        "```",
        "",
        "## 4. 外部定理验收边界",
        "",
        "Ford--Maynard 型 prime-producing sieve 框架说明，若要从筛对象真正产出素数，",
        "需要与对象匹配的 Type-I/Type-II 或双线性信息。当前相邻互质只给出",
        "`gcd=1`，而在 30-wheel residual 上还立即落入偶合数陷阱；因此不能替代",
        "`PrimeCountDominatesLPFTailShellSum`。",
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
        f"adjacent_coprime_identity_closed={bool_text(payload['adjacent_coprime_identity_closed'])}",
        f"post30_adjacent_parity_trap_closed={bool_text(payload['post30_adjacent_parity_trap_closed'])}",
        f"quotient_adjacent_lift_leaves_row_closed={bool_text(payload['quotient_adjacent_lift_leaves_row_closed'])}",
        f"adjacent_coprime_prime_payment_proved={bool_text(payload['adjacent_coprime_prime_payment_proved'])}",
        f"external_prime_producing_sieve_applies_directly={bool_text(payload['external_prime_producing_sieve_applies_directly'])}",
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
    print("post30_adjacent_parity_trap_closed=true")
    print("adjacent_coprime_prime_payment_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
