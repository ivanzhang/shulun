#!/usr/bin/env python3
"""ACT 短尾扫描：统计 q>=P/log^B P 的锚贡献。"""
from __future__ import annotations

import argparse
from math import isqrt, log


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


def col(P: int, c: int, B: float) -> dict:
    D = isqrt(P)
    threshold = P / (log(P) ** B)
    small = primes_upto(D)
    facp = primes_upto(P * P)
    N = A = tail = 0
    for k in range(P):
        n = k * P + c
        if n >= 2 and all(n % p for p in small):
            N += 1
            for q in factor_distinct(n, facp):
                if D < q < P:
                    A += 1
                    if q >= threshold:
                        tail += 1
    return {"c": c, "N": N, "A": A, "tail": tail, "A/N": A / N if N else 0, "tail/N": tail / N if N else 0}


def scan(P: int, B: float, top: int) -> dict:
    rows = [col(P, c, B) for c in range(1, P)]
    rows.sort(key=lambda r: -r["tail/N"])
    return {"P": P, "B": B, "threshold": round(P / (log(P) ** B), 3), "top_tail": rows[:top]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ps", nargs="+", type=int, default=[503, 1009, 2003])
    parser.add_argument("--B", type=float, default=2.0)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    for P in args.ps:
        print(scan(P, args.B, args.top))


if __name__ == "__main__":
    main()
