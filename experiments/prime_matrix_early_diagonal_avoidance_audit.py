#!/usr/bin/env python3
"""早期对角段避开 CRT 零行集合的实验审计。

用法示例：
  python3 experiments/prime_matrix_early_diagonal_avoidance_audit.py
  python3 experiments/prime_matrix_early_diagonal_avoidance_audit.py --max-p 5000

核心事实：若 1<=x<=p 且 1<=k<p，则 n=px+k<=p^2+p-1。
若 n 没有 <=p 的素因子，则 n 不可能是双粗合数，因而 n 必为 >p 的素数。
所以早期对角避让等价于每个短区间 (px,px+p) 内存在素数。
"""

from __future__ import annotations

import argparse
from math import isqrt, log


def prime_sieve(limit: int) -> bytearray:
    """返回素数指示数组。"""
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if is_prime[value]:
            start = value * value
            step = value
            is_prime[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return is_prime


def prefix_counts(is_prime: bytearray) -> list[int]:
    """返回素数计数前缀和。"""
    prefix = [0] * len(is_prime)
    total = 0
    for idx, flag in enumerate(is_prime):
        total += int(flag)
        prefix[idx] = total
    return prefix


def primes_from_sieve(is_prime: bytearray, max_p: int) -> list[int]:
    """从筛表中提取不超过 max_p 的奇素数。"""
    return [value for value in range(3, max_p + 1) if is_prime[value]]


def row_prime_count(prefix: list[int], p: int, x: int) -> int:
    """统计开区间 (px,px+p) 中的素数，即 px+1..px+p-1。"""
    left = p * x
    right = p * x + p - 1
    return prefix[right] - prefix[left]


def audit(max_p: int) -> dict:
    """执行早期对角段审计。"""
    limit = max_p * max_p + max_p
    is_prime = prime_sieve(limit)
    prefix = prefix_counts(is_prime)
    primes = primes_from_sieve(is_prime, max_p)

    zero_rows: list[dict] = []
    selected: list[dict] = []
    global_min: dict | None = None

    for p in primes:
        min_count = p
        min_rows: list[int] = []
        for x in range(1, p + 1):
            count = row_prime_count(prefix, p, x)
            if count < min_count:
                min_count = count
                min_rows = [x]
            elif count == min_count:
                min_rows.append(x)
            if count == 0:
                zero_rows.append({"p": p, "x": x})

        record = {
            "p": p,
            "min_prime_count": min_count,
            "min_rows": min_rows[:8],
            "min_rows_total": len(min_rows),
            "scale_p_over_log_p": p / log(p),
            "ratio_to_p_over_log_p": min_count / (p / log(p)),
        }
        if global_min is None or (min_count, -p) < (global_min["min_prime_count"], -global_min["p"]):
            global_min = record
        if p <= 31 or p in (101, 199, 499, 997, 1999, 4999) or min_count <= 2:
            selected.append(record)

    return {
        "max_p": max_p,
        "prime_count": len(primes),
        "zero_rows": zero_rows[:20],
        "zero_row_count": len(zero_rows),
        "global_min": global_min,
        "selected": selected,
    }


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    args = parser.parse_args()
    result = audit(args.max_p)

    print(f"max_p={result['max_p']}")
    print(f"odd_prime_count={result['prime_count']}")
    print(f"zero_row_count={result['zero_row_count']}")
    print(f"first_zero_rows={result['zero_rows']}")
    print(f"global_min={result['global_min']}")
    print("selected:")
    for record in result["selected"]:
        print(record)


if __name__ == "__main__":
    main()
