#!/usr/bin/env python3
"""ACT 桶级偏差扫描：分锚桶比较 A_j/N 与调和主项。"""
from __future__ import annotations

import argparse
from collections import defaultdict
from math import isqrt


def sieve(n: int) -> list[bool]:
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
    D = isqrt(P)
    pt = sieve(P * P)
    small = primes_upto(D)
    facp = primes_upto(P * P)
    prime_anchors = [q for q in primes_upto(P) if D < q < P]
    harmonic = defaultdict(float)
    for q in prime_anchors:
        harmonic[bucket(q, D)] += 1 / q

    N = 0
    A_by = defaultdict(int)
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            N += 1
            if not pt[n]:
                for q in factor_distinct(n, facp):
                    if D < q < P:
                        A_by[bucket(q, D)] += 1
    rows = []
    for b in sorted(set(harmonic) | set(A_by)):
        ratio = A_by[b] / N if N else 0
        rows.append({
            "bucket": b,
            "A_j": A_by[b],
            "A_j/N": round(ratio, 5),
            "harmonic_j": round(harmonic[b], 5),
            "bias": round(ratio - harmonic[b], 5),
        })
    return {"P": P, "c": c, "D": D, "N": N, "A/N": round(sum(A_by.values()) / N, 5), "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=1019)
    args = parser.parse_args()
    print(scan(args.P, args.c))


if __name__ == "__main__":
    main()
