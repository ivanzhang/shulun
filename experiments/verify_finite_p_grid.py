#!/usr/bin/env python3
"""有限小 P 验证：检查 P×P 方阵每行、非 P 列是否含素数。"""
from __future__ import annotations

import argparse
from math import isqrt


def sieve(n: int) -> list[bool]:
    """返回 0..n 的素性表。"""
    if n < 2:
        return [False] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : n + 1 : p] = [False] * (((n - start) // p) + 1)
    return is_prime


def primes_up_to(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    table = sieve(n)
    return [i for i, ok in enumerate(table) if ok]


def verify_p(P: int, prime_table: list[bool]) -> tuple[list[int], list[int]]:
    """返回失败行和失败列；列编号为 1..P，自动跳过第 P 列。"""
    bad_rows: list[int] = []
    bad_cols: list[int] = []

    for r in range(1, P + 1):
        start = (r - 1) * P + 1
        end = r * P
        if not any(prime_table[n] for n in range(start, end + 1)):
            bad_rows.append(r)

    for c in range(1, P):
        if not any(prime_table[c + k * P] for k in range(P)):
            bad_cols.append(c)

    return bad_rows, bad_cols


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=200, help="验证所有不超过该值的奇素数 P")
    parser.add_argument("--quiet", action="store_true", help="只输出汇总结果")
    args = parser.parse_args()

    ps = [p for p in primes_up_to(args.max_p) if p % 2 == 1]
    if not ps:
        print("没有需要验证的奇素数。")
        return 0

    max_n = ps[-1] * ps[-1]
    prime_table = sieve(max_n)
    failures = []

    for P in ps:
        bad_rows, bad_cols = verify_p(P, prime_table)
        if bad_rows or bad_cols:
            failures.append((P, bad_rows, bad_cols))
            print(f"FAIL P={P}: bad_rows={bad_rows}, bad_cols={bad_cols}")
        elif not args.quiet:
            print(f"PASS P={P}")

    if failures:
        print(f"SUMMARY: failures={len(failures)} / checked={len(ps)}")
        return 1

    print(f"SUMMARY: all passed for {len(ps)} odd primes P<= {args.max_p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
