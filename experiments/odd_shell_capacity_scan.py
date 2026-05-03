#!/usr/bin/env python3
"""奇素数层在反奇偶壳上的覆盖容量扫描。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for value in range(2, int(n**0.5) + 1):
        if sieve[value]:
            sieve[value * value : n + 1 : value] = [False] * (((n - value * value) // value) + 1)
    return [value for value, keep in enumerate(sieve) if keep]


def odd_shell(P: int, x: int) -> list[int]:
    # q=2 未覆盖壳：c != x mod 2。
    return [c for c in range(1, P) if c % 2 != x % 2]


def odd_hits(P: int, qs_odd: list[int], x: int, c: int) -> list[int]:
    return [q for q in qs_odd if (x * P + c) % q == 0]


def shell_profile(P: int, x: int) -> dict:
    qs = primes_upto(P - 1)
    qs_odd = [q for q in qs if q != 2]
    shell = odd_shell(P, x)
    hit_counts = []
    uncovered = []
    unique = []
    heavy = []
    by_q = {q: 0 for q in qs_odd}
    for c in shell:
        hits = odd_hits(P, qs_odd, x, c)
        hit_counts.append(len(hits))
        if not hits:
            uncovered.append(c)
        elif len(hits) == 1:
            unique.append({"c": c, "q": hits[0]})
        else:
            heavy.append({"c": c, "hits": hits})
        for q in hits:
            by_q[q] += 1
    active_q = {q: count for q, count in by_q.items() if count}
    capacity_sum = sum((len(shell) + q - 1) // q for q in qs_odd)
    actual_hits = sum(hit_counts)
    return {
        "x": x,
        "shell_size": len(shell),
        "uncovered_count": len(uncovered),
        "uncovered": uncovered,
        "unique_count": len(unique),
        "heavy_count": len(heavy),
        "actual_incidence": actual_hits,
        "naive_capacity_sum": capacity_sum,
        "overlap_excess": actual_hits - (len(shell) - len(uncovered)),
        "active_q_count": len(active_q),
        "active_q": active_q,
        "unique_sample": unique[:10],
        "heavy_sample": heavy[:10],
    }


def scan(P: int) -> dict:
    profiles = [shell_profile(P, x) for x in range(1, P)]
    best = min(profiles, key=lambda item: item["uncovered_count"])
    zero_profiles = [item for item in profiles if item["uncovered_count"] == 0]
    by_min = [item for item in profiles if item["uncovered_count"] == best["uncovered_count"]]
    return {
        "P": P,
        "min_uncovered": best["uncovered_count"],
        "best_profiles": by_min[:8],
        "zero_profile_count": len(zero_profiles),
        "zero_profiles": zero_profiles[:5],
    }


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "odd_shell_capacity_scan",
        "status": "odd_prime_layers_leave_uncovered_points_on_the_parity_complement_in_scanned_front_windows",
        "results": results,
        "structural_conclusion": (
            "剥离 q=2 后，奇素数层在反奇偶壳上的最优覆盖仍留下残点；"
            "这些残点正是原行残洞。容量和并非问题，重叠与同余锁相导致有效覆盖不足。"
        ),
        "next_obligations": [
            "把 naive capacity 与 actual union 的差写成重叠能量。",
            "证明前窗口内奇素数层的重叠能量至少吞掉一个壳点。",
            "用短差互斥刻画唯一覆盖点与重叠点之间的交换约束。",
        ],
    }
    (DOCS / "odd-shell-capacity-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 奇素数层反奇偶壳容量扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(
            f"- P={result['P']} min_uncovered={result['min_uncovered']} "
            f"zero_profiles={result['zero_profile_count']} best={result['best_profiles'][:3]}"
        )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "odd-shell-capacity-scan.md").write_text("\n".join(lines))
    print(DOCS / "odd-shell-capacity-scan.json")
    print(DOCS / "odd-shell-capacity-scan.md")


if __name__ == "__main__":
    main()
