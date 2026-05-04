#!/usr/bin/env python3
"""CRT 首个零行出现规律的有界扫描。

用法示例：
  python3 experiments/prime_matrix_first_zero_pattern_audit.py
  python3 experiments/prime_matrix_first_zero_pattern_audit.py --max-x 1000000 --max-p 47

本脚本扫描乘数 x，使 px+1..px+p-1 全部被 <p 的素数覆盖。
输出的 first_zero_x 是乘数；一编号行号为 first_zero_x+1。
"""

from __future__ import annotations

import argparse
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def odd_primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的奇素数。"""
    return [prime for prime in primes_upto(limit) if prime >= 3]


def survivor_columns(p: int, x: int, small_primes: list[int]) -> list[int]:
    """返回 px+1..px+p-1 中未被 <p 素数覆盖的列。"""
    survivors: list[int] = []
    for col in range(1, p):
        value = p * x + col
        if all(value % prime for prime in small_primes):
            survivors.append(col)
    return survivors


def scan_prime(p: int, max_x: int) -> dict:
    """扫描单个 p 的首个零行与早期对角余量。"""
    small_primes = primes_upto(p - 1)
    first_zero_x: int | None = None
    first_zero_survivors: list[int] | None = None
    min_early_count = p
    min_early_rows: list[int] = []
    min_seen_count = p
    min_seen_rows: list[int] = []

    for x in range(1, max_x + 1):
        survivors = survivor_columns(p, x, small_primes)
        count = len(survivors)
        if x <= p:
            if count < min_early_count:
                min_early_count = count
                min_early_rows = [x]
            elif count == min_early_count:
                min_early_rows.append(x)
        if count < min_seen_count:
            min_seen_count = count
            min_seen_rows = [x]
        elif count == min_seen_count:
            min_seen_rows.append(x)
        if count == 0:
            first_zero_x = x
            first_zero_survivors = survivors
            break

    return {
        "p": p,
        "max_x": max_x,
        "first_zero_x": first_zero_x,
        "first_zero_row": None if first_zero_x is None else first_zero_x + 1,
        "first_zero_ratio_x_over_p": None if first_zero_x is None else first_zero_x / p,
        "first_zero_survivors": first_zero_survivors,
        "min_early_count": min_early_count,
        "min_early_rows": min_early_rows[:8],
        "min_seen_count_before_stop": min_seen_count,
        "min_seen_rows_before_stop": min_seen_rows[:8],
    }


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=47)
    parser.add_argument("--max-x", type=int, default=200_000)
    args = parser.parse_args()

    print(f"max_p={args.max_p} max_x={args.max_x}")
    for p in odd_primes_upto(args.max_p):
        record = scan_prime(p, args.max_x)
        print(record)


if __name__ == "__main__":
    main()
