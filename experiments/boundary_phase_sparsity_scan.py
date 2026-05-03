#!/usr/bin/env python3
"""边界相位稀疏 BPS 扫描。检查端点相位在模 e 上的坏类命中。"""
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


def endpoint_phases(P: int, c: int, bucket: int, t: int) -> list[tuple[int, int, int]]:
    lo, hi = bucket_bounds(P, bucket)
    out = []
    for q in primes_upto(P):
        if not (lo < q < hi):
            continue
        r0 = (-c * pow(P % q, -1, q)) % q
        if r0 + t * q >= P:
            continue
        R = min(q, P - t * q)
        left_s = (c * pow(q, -1, P)) % P
        right_r = R - 1
        right_s = ((P * right_r + c) * pow(q, -1, P)) % P
        out.append((q, left_s, right_s))
    return out


def scan(P: int, c: int, bucket: int, t: int, e_values: list[int]) -> dict:
    data = endpoint_phases(P, c, bucket, t)
    rows = []
    for e in e_values:
        left = Counter(s % e for _, s, _ in data)
        right = Counter(s % e for _, _, s in data)
        rows.append({
            "e": e,
            "count": len(data),
            "left_max": max(left.values(), default=0),
            "right_max": max(right.values(), default=0),
            "expected": round(len(data) / e, 3) if e else None,
            "left_ratio": round(max(left.values(), default=0) / (len(data) / e), 3) if data and e else None,
            "right_ratio": round(max(right.values(), default=0) / (len(data) / e), 3) if data and e else None,
            "left_classes": len(left),
            "right_classes": len(right),
        })
    return {"P": P, "c": c, "D": isqrt(P), "bucket": bucket, "t": t, "q_count": len(data), "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=219)
    parser.add_argument("--bucket", type=int, default=4)
    parser.add_argument("--t", type=int, default=0)
    parser.add_argument("--e", nargs="+", type=int, default=[2, 3, 5, 7, 10, 30, 70])
    args = parser.parse_args()
    print(scan(args.P, args.c, args.bucket, args.t, args.e))


if __name__ == "__main__":
    main()
