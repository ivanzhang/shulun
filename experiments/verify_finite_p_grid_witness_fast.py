#!/usr/bin/env python3
"""快速见证式有限验证：全局筛素数，再按素数标记每个 P 的行/列。

用法示例：
  python3 experiments/verify_finite_p_grid_witness_fast.py --max-p 10000 --quiet
"""
from __future__ import annotations

import argparse
from array import array
from math import isqrt


def sieve_bytes(n: int) -> bytearray:
    """返回 0..n 的素性 bytearray。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int) -> array:
    """从素性表提取素数数组。"""
    out = array("I")
    out.extend(i for i in range(2, limit + 1) if flags[i])
    return out


def verify_one(P: int, primes: array) -> tuple[list[int], list[int]]:
    """用素数见证标记单个 P 的行列。"""
    max_n = P * P
    row_hit = bytearray(P + 1)
    col_hit = bytearray(P)
    rows_left = P
    cols_left = P - 1
    for prime in primes:
        if prime > max_n:
            break
        row = (prime - 1) // P + 1
        if row <= P and not row_hit[row]:
            row_hit[row] = 1
            rows_left -= 1
        col = prime % P
        if col and not col_hit[col]:
            col_hit[col] = 1
            cols_left -= 1
        if rows_left == 0 and cols_left == 0:
            break
    bad_rows = [r for r in range(1, P + 1) if not row_hit[r]]
    bad_cols = [c for c in range(1, P) if not col_hit[c]]
    return bad_rows, bad_cols


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    small_flags = sieve_bytes(args.max_p)
    ps = [p for p in range(3, args.max_p + 1, 2) if small_flags[p]]
    if not ps:
        print("没有需要验证的奇素数。")
        return 0
    flags = sieve_bytes(ps[-1] * ps[-1])
    primes = primes_from_flags(flags, ps[-1] * ps[-1])

    failures = []
    for idx, P in enumerate(ps, 1):
        bad_rows, bad_cols = verify_one(P, primes)
        if bad_rows or bad_cols:
            failures.append((P, bad_rows, bad_cols))
            print(f"FAIL P={P}: bad_rows={bad_rows[:10]}, bad_cols={bad_cols[:10]}")
        elif not args.quiet:
            print(f"PASS P={P} ({idx}/{len(ps)})")
    if failures:
        print(f"SUMMARY: failures={len(failures)} / checked={len(ps)}")
        return 1
    print(f"SUMMARY: all passed for {len(ps)} odd primes P<= {args.max_p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
