#!/usr/bin/env python3
"""扫描列方向粗筛候选与粗合数容量。"""
from __future__ import annotations

from math import isqrt


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


def factor_small(n: int, primes: list[int]) -> int | None:
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return p
    return None


def scan(P: int) -> dict:
    small = primes_upto(isqrt(P))
    prime_table = sieve(P * P)
    worst = None
    rows = []
    for c in range(1, P):
        rough = []
        rough_comp = []
        rough_prime = []
        for k in range(P):
            n = k * P + c
            if n < 2:
                continue
            if all(n % q for q in small):
                rough.append(k)
                if prime_table[n]:
                    rough_prime.append(k)
                else:
                    rough_comp.append(k)
        item = {"c": c, "rough": len(rough), "rough_prime": len(rough_prime), "rough_comp": len(rough_comp)}
        rows.append(item)
        if worst is None or item["rough_prime"] < worst["rough_prime"]:
            worst = item
    return {"P": P, "sqrtP": isqrt(P), "small": small, "worst": worst, "min_rough": min(r["rough"] for r in rows), "min_prime": min(r["rough_prime"] for r in rows), "max_comp": max(r["rough_comp"] for r in rows)}


def main() -> None:
    for P in [23, 29, 31, 53, 101, 251, 503, 1009, 2003]:
        print(scan(P))


if __name__ == "__main__":
    main()
