#!/usr/bin/env python3
"""MME-2：扫描短窗口粗合数匹配的乘法差与互质结构。"""
from __future__ import annotations

from collections import Counter
from math import gcd, isqrt


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


def rough_composites(P: int, c: int):
    prime_table = sieve(P * P)
    small = primes_upto(isqrt(P))
    allp = primes_upto(P * P)
    out = []
    for k in range(P):
        n = k * P + c
        if n < 2 or prime_table[n]:
            continue
        if all(n % q for q in small):
            fs = factor(n, allp)
            if all(f > isqrt(P) for f in fs):
                out.append({"k": k, "n": n, "factors": fs, "rad": sorted(set(fs))})
    return out


def scan_column(P: int, c: int) -> dict:
    comps = rough_composites(P, c)
    D = isqrt(P)
    windows = []
    for start in range(0, P):
        block = [x for x in comps if start <= x["k"] < start + D]
        if len(block) >= 2:
            all_factors = [f for item in block for f in item["rad"]]
            repeated = len(all_factors) - len(set(all_factors))
            pair_gcds = []
            diff_gcds = []
            for i in range(len(block)):
                for j in range(i + 1, len(block)):
                    a, b = block[i], block[j]
                    pair_gcds.append(gcd(a["n"], b["n"]))
                    diff_gcds.append(gcd(a["n"], abs(a["k"] - b["k"]) * P))
            windows.append({
                "start": start,
                "size": len(block),
                "factor_occ": len(all_factors),
                "distinct_factors": len(set(all_factors)),
                "repeated": repeated,
                "max_pair_gcd": max(pair_gcds) if pair_gcds else 1,
                "gaps": [block[i+1]["k"] - block[i]["k"] for i in range(len(block)-1)],
                "ks": [x["k"] for x in block],
                "sample_factors": [x["rad"] for x in block[:6]],
            })
    windows.sort(key=lambda w: (-w["size"], w["repeated"], w["start"]))
    return {
        "P": P,
        "c": c,
        "D": D,
        "rough_comp": len(comps),
        "best_windows": windows[:8],
        "max_window_size": windows[0]["size"] if windows else 0,
    }


def worst_columns(P: int, limit: int = 2) -> list[int]:
    prime_table = sieve(P * P)
    small = primes_upto(isqrt(P))
    vals = []
    for c in range(1, P):
        count = 0
        for k in range(P):
            n = k * P + c
            if n >= 2 and not prime_table[n] and all(n % q for q in small):
                count += 1
        vals.append((count, c))
    vals.sort(reverse=True)
    return [c for _, c in vals[:limit]]


def main() -> None:
    for P in [251, 503, 1009, 2003]:
        for c in worst_columns(P, 2):
            print(scan_column(P, c))


if __name__ == "__main__":
    main()
