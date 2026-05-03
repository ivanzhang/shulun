#!/usr/bin/env python3
"""ALS 桶内锚斜线采样方差扫描。"""
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


def bucket(q: int, d: int) -> int:
    j = 0
    x = d
    while q >= 2 * x:
        x *= 2
        j += 1
    return j


def scan(P: int, c: int) -> dict:
    D = isqrt(P)
    small = primes_upto(D)
    anchors = [q for q in primes_upto(P) if D < q < P]
    rough = [False] * P
    N = 0
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            rough[k] = True
            N += 1
    delta = N / P
    by = defaultdict(lambda: {"cnt": 0, "sumT": 0, "sumX": 0, "sse": 0.0, "rand": 0.0})
    for q in anchors:
        r = (-c * pow(P % q, -1, q)) % q
        ks = list(range(r, P, q))
        T = len(ks)
        X = sum(1 for k in ks if rough[k])
        b = bucket(q, D)
        by[b]["cnt"] += 1
        by[b]["sumT"] += T
        by[b]["sumX"] += X
        by[b]["sse"] += (X - delta * T) ** 2
        by[b]["rand"] += delta * (1 - delta) * T
    rows = []
    for b, v in sorted(by.items()):
        rows.append({
            "bucket": b,
            "cnt": v["cnt"],
            "sumT": v["sumT"],
            "sumX": v["sumX"],
            "sumX/N": round(v["sumX"] / N, 5) if N else 0,
            "main/N": round(delta * v["sumT"] / N, 5) if N else 0,
            "bias/N": round((v["sumX"] - delta * v["sumT"]) / N, 5) if N else 0,
            "sse/rand": round(v["sse"] / v["rand"], 4) if v["rand"] else None,
        })
    return {"P": P, "c": c, "D": D, "N": N, "delta": round(delta, 6), "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=1019)
    args = parser.parse_args()
    print(scan(args.P, args.c))


if __name__ == "__main__":
    main()
