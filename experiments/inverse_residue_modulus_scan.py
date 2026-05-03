#!/usr/bin/env python3
"""倒数轨道 IRM 单模/多模分布扫描。

用途示例：
  python3 experiments/inverse_residue_modulus_scan.py
  python3 experiments/inverse_residue_modulus_scan.py --P 2003 --c 219
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
    lo = (2 ** bucket) * d
    hi = min((2 ** (bucket + 1)) * d, P)
    return lo, hi


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    """合并互素模数的两个同余。"""
    t = ((b - a) * pow(m, -1, n)) % n
    return a + m * t, m * n


def bad_class(P: int, c: int, d: int, small: list[int]) -> tuple[int, int]:
    """计算 rP+c 被所有 p|d 整除所要求的 r 同余类。"""
    a = 0
    mod = 1
    for p in small:
        if d % p == 0:
            ap = (-c * pow(P % p, -1, p)) % p
            a, mod = crt_pair(a, mod, ap, p)
    return a % mod, mod


def q_primes_in_bucket(P: int, bucket: int, primes: list[int]) -> list[int]:
    lo, hi = bucket_bounds(P, bucket)
    return [q for q in primes if lo < q < hi]


def inverse_rows(P: int, c: int, qs: list[int]) -> dict[int, int]:
    rows = {}
    for q in qs:
        rows[q] = (-c * pow(P % q, -1, q)) % q
    return rows


def scan(P: int, c: int, bucket: int, z_count: int) -> dict:
    d0 = isqrt(P)
    primes = primes_upto(P)
    small = [p for p in primes_upto(d0) if c % p != 0]
    qs = q_primes_in_bucket(P, bucket, primes)
    rows = inverse_rows(P, c, qs)
    chosen = small[:z_count]

    single = []
    for p in chosen:
        ap = (-c * pow(P % p, -1, p)) % p
        hits = sum(1 for r in rows.values() if r % p == ap)
        expected = len(qs) / p if p else 0
        single.append({"p": p, "hits": hits, "expected": round(expected, 3), "ratio": round(hits / expected, 3) if expected else None})

    multi = []
    mod = 1
    d = 1
    for p in chosen:
        d *= p
        if d > max(1, len(qs) * 4):
            break
        a, mod = bad_class(P, c, d, chosen)
        hits = sum(1 for r in rows.values() if r % mod == a)
        expected = len(qs) / mod
        multi.append({"d": d, "hits": hits, "expected": round(expected, 4), "ratio": round(hits / expected, 3) if expected else None})

    residue_spread = {}
    for p in chosen[:5]:
        counts = Counter(r % p for r in rows.values())
        residue_spread[p] = {"min": min(counts.values()), "max": max(counts.values()), "classes": len(counts)} if counts else {}

    return {
        "P": P,
        "c": c,
        "D": d0,
        "bucket": bucket,
        "q_count": len(qs),
        "q_range": bucket_bounds(P, bucket),
        "single_bad_class": single,
        "multi_bad_class": multi,
        "residue_spread_first": residue_spread,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--c", type=int, default=219)
    parser.add_argument("--bucket", type=int, default=4)
    parser.add_argument("--z-count", type=int, default=7)
    args = parser.parse_args()
    print(scan(args.P, args.c, args.bucket, args.z_count))


if __name__ == "__main__":
    main()
