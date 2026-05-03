#!/usr/bin/env python3
"""DPR-energy 扫描：倒数投影模 e 的二阶集中。"""
from __future__ import annotations

import argparse
from collections import Counter
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


def bucket_bounds(P: int, bucket: int) -> tuple[int, int]:
    d = isqrt(P)
    return (2 ** bucket) * d, min((2 ** (bucket + 1)) * d, P)


def dpr_values(P: int, A: int, bucket: int) -> list[int]:
    lo, hi = bucket_bounds(P, bucket)
    out = []
    for q in primes_upto(P):
        if lo < q < hi and q % P:
            out.append((A * pow(q, -1, P)) % P)
    return out


def scan(P: int, A: int, bucket: int, e_values: list[int]) -> dict:
    vals = dpr_values(P, A, bucket)
    rows = []
    n = len(vals)
    for e in e_values:
        counts = Counter(v % e for v in vals)
        second = sum(x * x for x in counts.values())
        model = n * n / e + n
        rows.append({
            "e": e,
            "n": n,
            "classes": len(counts),
            "max": max(counts.values(), default=0),
            "second": second,
            "model_n2e_plus_n": round(model, 3),
            "ratio": round(second / model, 3) if model else None,
        })
    return {"P": P, "A": A, "D": isqrt(P), "bucket": bucket, "q_range": bucket_bounds(P, bucket), "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--A", type=int, default=219)
    parser.add_argument("--bucket", type=int, default=4)
    parser.add_argument("--e", nargs="+", type=int, default=[2, 3, 5, 7, 10, 30, 70, 210])
    args = parser.parse_args()
    print(scan(args.P, args.A, args.bucket, args.e))


if __name__ == "__main__":
    main()
