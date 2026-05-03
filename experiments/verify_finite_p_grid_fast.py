#!/usr/bin/env python3
"""更快的有限验证器：逐个奇素数 P 验证行列含素数。

用法示例：
  python3 experiments/verify_finite_p_grid_fast.py --max-p 10000 --quiet

算法：
  对每个 P 单独筛 [0,P^2] 的 bytearray，避免 Python list 布尔表膨胀；
  再按行、列扫描 bytearray。适合 P<=数万的直接证书检查。
"""
from __future__ import annotations

import argparse
from math import isqrt


def sieve_bytes(n: int) -> bytearray:
    """返回 0..n 的素性 bytearray。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    limit = isqrt(n)
    for p in range(2, limit + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_up_to(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    flags = sieve_bytes(n)
    return [i for i in range(2, n + 1) if flags[i]]


def verify_one(P: int) -> tuple[list[int], list[int]]:
    """验证单个 P，返回失败行与失败列。"""
    flags = sieve_bytes(P * P)
    bad_rows: list[int] = []
    bad_cols: list[int] = []

    for row in range(1, P + 1):
        start = (row - 1) * P + 1
        if 1 not in flags[start : start + P]:
            bad_rows.append(row)

    for col in range(1, P):
        hit = False
        for value in range(col, P * P + 1, P):
            if flags[value]:
                hit = True
                break
        if not hit:
            bad_cols.append(col)
    return bad_rows, bad_cols


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    ps = [p for p in primes_up_to(args.max_p) if p % 2 == 1]
    failures = []
    for index, P in enumerate(ps, start=1):
        bad_rows, bad_cols = verify_one(P)
        if bad_rows or bad_cols:
            failures.append((P, bad_rows, bad_cols))
            print(f"FAIL P={P}: bad_rows={bad_rows[:10]}, bad_cols={bad_cols[:10]}")
        elif not args.quiet:
            print(f"PASS P={P} ({index}/{len(ps)})")
    if failures:
        print(f"SUMMARY: failures={len(failures)} / checked={len(ps)}")
        return 1
    print(f"SUMMARY: all passed for {len(ps)} odd primes P<= {args.max_p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
