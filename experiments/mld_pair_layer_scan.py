#!/usr/bin/env python3
"""MLD 双层有效锚扫描：统计同一锚多层同时落入粗骨架的层对数。"""
from __future__ import annotations

import argparse
from collections import defaultdict, Counter
from math import isqrt, log


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
    out = []
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
    j = 0
    x = d
    while q >= 2 * x:
        x *= 2
        j += 1
    return j


def scan(P: int, c: int) -> dict:
    d = isqrt(P)
    pt = sieve(P * P)
    small = primes_upto(d)
    facp = primes_upto(P * P)
    anchors = defaultdict(list)
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small) and not pt[n]:
            for q in factor_distinct(n, facp):
                if d < q < P:
                    anchors[q].append(k)

    by_bucket = defaultdict(lambda: {"Q": 0, "A": 0, "E": 0, "pair_gaps": Counter()})
    for q, ks in anchors.items():
        b = bucket(q, d)
        rows = sorted(ks)
        m = len(rows)
        by_bucket[b]["Q"] += 1
        by_bucket[b]["A"] += m
        by_bucket[b]["E"] += m * (m - 1) // 2
        for i, x in enumerate(rows):
            for y in rows[i + 1:]:
                # 同一锚的行差是 q 的倍数；层差约 (y-x)/q。
                by_bucket[b]["pair_gaps"][round((y - x) / q, 3)] += 1

    rows = []
    Nrough = 0
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            Nrough += 1
    for b, data in sorted(by_bucket.items()):
        rows.append({
            "bucket": b,
            "Q": data["Q"],
            "A": data["A"],
            "E": data["E"],
            "E/Q": round(data["E"] / data["Q"], 4) if data["Q"] else 0,
            "Q/N": round(data["Q"] / Nrough, 4) if Nrough else 0,
            "E/N": round(data["E"] / Nrough, 4) if Nrough else 0,
            "top_pair_gaps": data["pair_gaps"].most_common(5),
        })
    return {"P": P, "c": c, "D": d, "Nrough": Nrough, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=219)
    args = parser.parse_args()
    print(scan(args.P, args.c))


if __name__ == "__main__":
    main()
