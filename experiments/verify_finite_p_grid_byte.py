#!/usr/bin/env python3
"""全局 bytearray 有限验证：比原 list 版省内存。

用法示例：
  python3 experiments/verify_finite_p_grid_byte.py --max-p 10000 --quiet
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
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    small = sieve_bytes(args.max_p)
    ps = [p for p in range(3, args.max_p + 1, 2) if small[p]]
    if not ps:
        print("没有需要验证的奇素数。")
        return 0
    flags = sieve_bytes(ps[-1] * ps[-1])
    failures = []
    for P in ps:
        bad_rows = []
        bad_cols = []
        for row in range(1, P + 1):
            start = (row - 1) * P + 1
            if 1 not in flags[start:start + P]:
                bad_rows.append(row)
        for col in range(1, P):
            if not any(flags[col:P * P + 1:P]):
                bad_cols.append(col)
        if bad_rows or bad_cols:
            failures.append((P, bad_rows, bad_cols))
            print(f"FAIL P={P}: bad_rows={bad_rows[:10]}, bad_cols={bad_cols[:10]}")
        elif not args.quiet:
            print(f"PASS P={P}")
    if failures:
        print(f"SUMMARY: failures={len(failures)} / checked={len(ps)}")
        return 1
    print(f"SUMMARY: all passed for {len(ps)} odd primes P<= {args.max_p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
