#!/usr/bin/env python3
"""扫描列方向粗合数的双大因子匹配结构。"""
from __future__ import annotations

from collections import Counter
from math import isqrt, gcd


def sieve(n: int) -> list[bool]:
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            for j in range(p * p, n + 1, p):
                is_prime[j] = False
    return is_prime


def primes_upto(n: int) -> list[int]:
    table = sieve(n)
    return [i for i, ok in enumerate(table) if ok]


def factor(n: int, primes: list[int]) -> list[int]:
    fs = []
    x = n
    for p in primes:
        if p * p > x:
            break
        while x % p == 0:
            fs.append(p)
            x //= p
    if x > 1:
        fs.append(x)
    return fs


def scan(P: int, c: int) -> dict:
    prime_table = sieve(P * P)
    small = primes_upto(isqrt(P))
    allp = primes_upto(P)
    rough_comp = []
    for k in range(P):
        n = k * P + c
        if n < 2 or prime_table[n]:
            continue
        if all(n % q for q in small):
            fs = factor(n, allp)
            if all(f > isqrt(P) for f in fs):
                rough_comp.append((k, n, fs))
    gaps = []
    shared = 0
    close_pairs = 0
    for i in range(len(rough_comp)):
        k1, _, f1 = rough_comp[i]
        for j in range(i + 1, len(rough_comp)):
            k2, _, f2 = rough_comp[j]
            d = abs(k2 - k1)
            if d < isqrt(P):
                close_pairs += 1
                if set(f1) & set(f2):
                    shared += 1
                gaps.append(d)
    factor_counts = Counter(f for _, _, fs in rough_comp for f in set(fs))
    return {
        "P": P,
        "c": c,
        "rough_comp": len(rough_comp),
        "close_pairs": close_pairs,
        "close_shared_factor_pairs": shared,
        "top_factor_reuse": factor_counts.most_common(5),
        "gap_top": Counter(gaps).most_common(8),
        "sample": rough_comp[:8],
    }


def worst_columns(P: int, limit: int = 3) -> list[int]:
    prime_table = sieve(P * P)
    small = primes_upto(isqrt(P))
    vals = []
    for c in range(1, P):
        rc = 0
        for k in range(P):
            n = k * P + c
            if n >= 2 and not prime_table[n] and all(n % q for q in small):
                rc += 1
        vals.append((rc, c))
    vals.sort(reverse=True)
    return [c for _, c in vals[:limit]]


def main() -> None:
    for P in [101, 251, 503, 1009, 2003]:
        for c in worst_columns(P, 2):
            print(scan(P, c))


if __name__ == "__main__":
    main()
