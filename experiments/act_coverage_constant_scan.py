#!/usr/bin/env python3
"""ACT 覆盖能力常数扫描：比较 A/N 与 sum_{D<q<P}1/q。"""
from __future__ import annotations

import argparse
from collections import defaultdict
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


def column_A(P: int, c: int, pt: list[bool], small: list[int], facp: list[int]) -> tuple[int, int, int]:
    D = isqrt(P)
    N = 0
    A = 0
    anchored_points = 0
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            N += 1
            local = 0
            if not pt[n]:
                for q in factor_distinct(n, facp):
                    if D < q < P:
                        local += 1
            A += local
            if local:
                anchored_points += 1
    return N, A, anchored_points


def scan(P: int, top: int) -> dict:
    D = isqrt(P)
    pt = sieve(P * P)
    small = primes_upto(D)
    facp = primes_upto(P * P)
    anchor_primes = [q for q in primes_upto(P) if D < q < P]
    harmonic = sum(1 / q for q in anchor_primes)
    rows = []
    for c in range(1, P):
        N, A, anchored = column_A(P, c, pt, small, facp)
        rows.append({
            "c": c,
            "N": N,
            "A": A,
            "anchored": anchored,
            "A/N": round(A / N, 5) if N else 0,
            "anchored/N": round(anchored / N, 5) if N else 0,
            "excess_vs_harmonic": round(A / N - harmonic, 5) if N else 0,
        })
    rows.sort(key=lambda r: -r["A/N"])
    return {"P": P, "D": D, "harmonic": round(harmonic, 6), "log2": round(log(2), 6), "top": rows[:top]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ps", nargs="+", type=int, default=[251, 503, 1009, 2003])
    parser.add_argument("--top", type=int, default=8)
    args = parser.parse_args()
    for P in args.ps:
        print(scan(P, args.top))


if __name__ == "__main__":
    main()
