#!/usr/bin/env python3
"""分段有限验证：检查所有奇素数 P<=max-p 的 P×P 方阵行列含素数。

用法示例：
  python3 experiments/verify_finite_p_grid_segmented.py --max-p 10000 --segment-size 2000000 --quiet

说明：
  使用奇数压缩分段筛，避免一次性构造 0..Pmax^2 的 Python bool 表。
  当前实现优先验证并输出失败；可选保存每个 P 的首个失败信息。
"""
from __future__ import annotations

import argparse
from math import isqrt


def simple_sieve(n: int) -> list[int]:
    """返回不超过 n 的素数表。"""
    if n < 2:
        return []
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            flags[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if flags[i]]


def mark_segment(lo: int, hi: int, base_primes: list[int]) -> bytearray:
    """返回 [lo,hi] 的素性 bytearray。"""
    size = hi - lo + 1
    flags = bytearray(b"\x01") * size
    if lo == 0:
        flags[0:2] = b"\x00\x00"
    elif lo == 1:
        flags[0] = 0
    for p in base_primes:
        pp = p * p
        if pp > hi:
            break
        start = max(pp, ((lo + p - 1) // p) * p)
        flags[start - lo : size : p] = b"\x00" * (((hi - start) // p) + 1)
    return flags


def odd_primes_up_to(n: int) -> list[int]:
    """返回不超过 n 的奇素数。"""
    return [p for p in simple_sieve(n) if p % 2 == 1]


def verify(max_p: int, segment_size: int, quiet: bool) -> int:
    """分段验证目标命题。"""
    ps = odd_primes_up_to(max_p)
    if not ps:
        print("没有需要验证的奇素数。")
        return 0
    max_n = ps[-1] * ps[-1]
    base = simple_sieve(isqrt(max_n) + 1)

    row_hit: dict[int, bytearray] = {P: bytearray(P + 1) for P in ps}
    col_hit: dict[int, bytearray] = {P: bytearray(P) for P in ps}

    for lo in range(0, max_n + 1, segment_size):
        hi = min(max_n, lo + segment_size - 1)
        flags = mark_segment(lo, hi, base)
        for offset, is_p in enumerate(flags):
            if not is_p:
                continue
            n = lo + offset
            if n < 2:
                continue
            for P in ps:
                if n > P * P:
                    continue
                row = (n - 1) // P + 1
                if 1 <= row <= P:
                    row_hit[P][row] = 1
                col = n % P
                if col == 0:
                    col = P
                if 1 <= col < P:
                    col_hit[P][col] = 1
        if not quiet:
            print(f"processed {hi}/{max_n}")

    failures = []
    for P in ps:
        bad_rows = [r for r in range(1, P + 1) if not row_hit[P][r]]
        bad_cols = [c for c in range(1, P) if not col_hit[P][c]]
        if bad_rows or bad_cols:
            failures.append((P, bad_rows[:10], bad_cols[:10]))
            print(f"FAIL P={P}: bad_rows={bad_rows[:10]}, bad_cols={bad_cols[:10]}")
    if failures:
        print(f"SUMMARY: failures={len(failures)} / checked={len(ps)}")
        return 1
    print(f"SUMMARY: all passed for {len(ps)} odd primes P<= {max_p}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--segment-size", type=int, default=2_000_000)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    return verify(args.max_p, args.segment_size, args.quiet)


if __name__ == "__main__":
    raise SystemExit(main())
