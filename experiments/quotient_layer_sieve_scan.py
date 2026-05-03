#!/usr/bin/env python3
"""固定 t 的商变量 s_q+tP 小筛衰减扫描。

用途示例：
  python3 experiments/quotient_layer_sieve_scan.py --P 2003 --c 219 --bucket 4 --t 0
"""
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


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    t = ((b - a) * pow(m, -1, n)) % n
    return a + m * t, m * n


def bad_s_class(P: int, t: int, d: int, small: list[int]) -> tuple[int, int]:
    a = 0
    mod = 1
    for p in small:
        if d % p == 0:
            ap = (-t * (P % p)) % p
            a, mod = crt_pair(a, mod, ap, p)
    return a % mod, mod


def q_data(P: int, c: int, bucket: int, t: int) -> list[tuple[int, int, int]]:
    primes = primes_upto(P)
    lo, hi = bucket_bounds(P, bucket)
    out = []
    for q in primes:
        if not (lo < q < hi):
            continue
        r = (-c * pow(P % q, -1, q)) % q
        k = r + t * q
        if k >= P:
            continue
        s = (r * P + c) // q
        out.append((q, r, s + t * P))
    return out


def scan(P: int, c: int, bucket: int, t: int, z_count: int) -> dict:
    d0 = isqrt(P)
    small = [p for p in primes_upto(d0) if c % p != 0]
    chosen = small[:z_count]
    data = q_data(P, c, bucket, t)
    values = [v for _, _, v in data]

    single = []
    for p in chosen:
        hits = sum(1 for v in values if v % p == 0)
        expected = len(values) / p
        single.append({"p": p, "hits": hits, "expected": round(expected, 3), "ratio": round(hits / expected, 3) if expected else None})

    multi = []
    d = 1
    for p in chosen:
        d *= p
        if d > max(1, len(values) * 4):
            break
        hits = sum(1 for v in values if v % d == 0)
        expected = len(values) / d
        multi.append({"d": d, "hits": hits, "expected": round(expected, 4), "ratio": round(hits / expected, 3) if expected else None})

    spread = {}
    for p in chosen[:5]:
        counts = Counter(v % p for v in values)
        spread[p] = {"min": min(counts.values()), "max": max(counts.values()), "classes": len(counts)} if counts else {}

    return {
        "P": P,
        "c": c,
        "D": d0,
        "bucket": bucket,
        "t": t,
        "q_count_with_layer": len(values),
        "q_range": bucket_bounds(P, bucket),
        "single_zero_class": single,
        "multi_zero_class": multi,
        "spread_first": spread,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=219)
    parser.add_argument("--bucket", type=int, default=4)
    parser.add_argument("--t", type=int, default=0)
    parser.add_argument("--z-count", type=int, default=7)
    args = parser.parse_args()
    print(scan(args.P, args.c, args.bucket, args.t, args.z_count))


if __name__ == "__main__":
    main()
