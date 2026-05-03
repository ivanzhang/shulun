#!/usr/bin/env python3
"""分桶联合能量 Φ_j=Q_j-τE_j 扫描。

用途示例：
  python3 experiments/joint_bucket_phi_scan.py
  python3 experiments/joint_bucket_phi_scan.py --ps 503 1009 --tau 0.1
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from math import isqrt


def sieve(n: int) -> list[bool]:
    """返回素数布尔表。"""
    a = [True] * (n + 1)
    if n >= 0:
        a[0] = False
    if n >= 1:
        a[1] = False
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            for j in range(p * p, n + 1, p):
                a[j] = False
    return a


def primes_upto(n: int) -> list[int]:
    s = sieve(n)
    return [i for i, v in enumerate(s) if v]


def factor_distinct(n: int, primes: list[int]) -> list[int]:
    """返回 n 的不同素因子。"""
    out: list[int] = []
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
    if x > 1:
        out.append(x)
    return out


def bucket(q: int, d: int) -> int:
    """按 [2^j D, 2^{j+1}D) 分桶。"""
    j = 0
    x = d
    while q >= 2 * x:
        x *= 2
        j += 1
    return j


def column_metrics(P: int, c: int, pt: list[bool], small: list[int], facp: list[int], tau: float) -> dict:
    d = isqrt(P)
    anchors: dict[int, list[int]] = defaultdict(list)
    rough = []
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            rough.append(k)
            if not pt[n]:
                for q in factor_distinct(n, facp):
                    if d < q < P:
                        anchors[q].append(k)

    by_bucket: dict[int, dict[str, float]] = defaultdict(lambda: {"Q": 0, "A": 0, "E": 0, "Phi": 0.0})
    for q, rows in anchors.items():
        b = bucket(q, d)
        n_q = len(rows)
        e_q = n_q * (n_q - 1) // 2
        by_bucket[b]["Q"] += 1
        by_bucket[b]["A"] += n_q
        by_bucket[b]["E"] += e_q
        by_bucket[b]["Phi"] += 1 - tau * e_q

    N = len(rough)
    Q = len(anchors)
    A = sum(len(rows) for rows in anchors.values())
    E = sum(len(rows) * (len(rows) - 1) // 2 for rows in anchors.values())
    Phi = Q - tau * E
    return {
        "c": c,
        "N": N,
        "Q": Q,
        "A": A,
        "E": E,
        "Phi": Phi,
        "phi_ratio": Phi / N if N else 0.0,
        "q_ratio": Q / N if N else 0.0,
        "a_ratio": A / N if N else 0.0,
        "e_ratio": E / N if N else 0.0,
        "buckets": dict(sorted(by_bucket.items())),
    }


def scan(P: int, tau: float, top: int) -> dict:
    pt = sieve(P * P)
    small = primes_upto(isqrt(P))
    facp = primes_upto(P * P)
    rows = [column_metrics(P, c, pt, small, facp, tau) for c in range(1, P)]
    rows.sort(key=lambda r: (-r["phi_ratio"], -r["q_ratio"], -r["a_ratio"]))
    worst_bucket = Counter()
    for r in rows[:top]:
        if r["buckets"]:
            b, data = max(r["buckets"].items(), key=lambda item: item[1]["Phi"])
            worst_bucket[b] += 1
            r["max_bucket"] = {"bucket": b, **data, "Phi_per_N": data["Phi"] / r["N"] if r["N"] else 0.0}
    return {"P": P, "D": isqrt(P), "tau": tau, "top": rows[:top], "top_bucket_hist": dict(worst_bucket)}


def compact(result: dict) -> dict:
    """压缩输出，只保留审查需要的关键指标。"""
    top = []
    for r in result["top"]:
        top.append({
            "c": r["c"],
            "N": r["N"],
            "Q/N": round(r["q_ratio"], 4),
            "A/N": round(r["a_ratio"], 4),
            "E/N": round(r["e_ratio"], 4),
            "Phi/N": round(r["phi_ratio"], 4),
            "max_bucket": r.get("max_bucket"),
        })
    return {"P": result["P"], "D": result["D"], "tau": result["tau"], "top_bucket_hist": result["top_bucket_hist"], "top": top}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ps", nargs="+", type=int, default=[251, 503, 1009, 2003])
    parser.add_argument("--tau", type=float, default=0.1)
    parser.add_argument("--top", type=int, default=8)
    args = parser.parse_args()
    for P in args.ps:
        print(compact(scan(P, args.tau, args.top)))


if __name__ == "__main__":
    main()
