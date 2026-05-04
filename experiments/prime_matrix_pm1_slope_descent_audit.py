#!/usr/bin/env python3
"""p±1 斜率递降审计。

用法示例：
  python3 experiments/prime_matrix_pm1_slope_descent_audit.py --pairs 23:58,17:1210

给定 p-零行乘数 x，若 pi|p-1 或 pi|p+1，则
  px+k = x(p-1)+(x+k) = pi*A + (x+k)
  px+k = x(p+1)+(k-x) = pi*B + (k-x)
脚本检查这些长度 p 的 pi-网格长窗中，是否存在完整 pi 子窗全部由 <pi 素数覆盖。
同时区分任意连续 pi 子窗与真正对齐的 pi 行子窗。
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def prime_factors(value: int) -> list[int]:
    """返回 value 的不同素因子。"""
    factors: list[int] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


def primorial_below(limit_prime: int) -> int:
    """返回所有小于 limit_prime 的素数乘积。"""
    product = 1
    for prime in primes_upto(limit_prime - 1):
        product *= prime
    return product


def is_zero_row(p: int, x: int) -> bool:
    """检查 x 是否为 p-筛零行乘数。"""
    small_primes = primes_upto(p - 1)
    return all(any((p * x + column) % q == 0 for q in small_primes) for column in range(1, p))


def subwindow_leakage(values: list[int], pi: int) -> list[dict]:
    """检查任意连续 pi 子窗的 <pi 泄漏情况。"""
    modulus = primorial_below(pi)
    records: list[dict] = []
    if pi < 2:
        return records
    for start in range(0, max(0, len(values) - pi + 1)):
        block = values[start : start + pi]
        leakage = [index + 1 for index, value in enumerate(block) if gcd(value, modulus) == 1]
        records.append(
            {
                "start_offset": start,
                "leakage_count": len(leakage),
                "leakage_positions": leakage[:20],
                "strong_pi_zero_block": len(leakage) == 0,
            }
        )
    return records


def aligned_block_leakage(values: list[int], pi: int) -> list[dict]:
    """检查完全对齐的 pi 行子窗。"""
    modulus = primorial_below(pi)
    value_set = set(values)
    records: list[dict] = []
    if not values:
        return records
    first_y = (min(values) - 1 + pi - 1) // pi
    last_y = max(values) // pi
    for multiplier in range(first_y, last_y + 1):
        block = [pi * multiplier + column for column in range(1, pi + 1)]
        if not all(value in value_set for value in block):
            continue
        leakage = [column for column, value in enumerate(block, start=1) if gcd(value, modulus) == 1]
        records.append(
            {
                "multiplier": multiplier,
                "leakage_count": len(leakage),
                "leakage_columns": leakage[:20],
                "strong_pi_zero_row": len(leakage) == 0,
            }
        )
    return records


def audit_branch(p: int, x: int, pi: int, sign: int) -> dict:
    """审计 pi|p-sign 分支。sign=-1 表示 p-1；sign=+1 表示 p+1。"""
    values = [p * x + column for column in range(1, p)]
    records = subwindow_leakage(values, pi)
    aligned_records = aligned_block_leakage(values, pi)
    best = min((record["leakage_count"] for record in records), default=None)
    aligned_best = min((record["leakage_count"] for record in aligned_records), default=None)
    strong_blocks = [record for record in records if record["strong_pi_zero_block"]]
    aligned_strong_blocks = [record for record in aligned_records if record["strong_pi_zero_row"]]
    return {
        "pi": pi,
        "sign": "p-1" if sign == -1 else "p+1",
        "window_count": len(records),
        "min_leakage_count": best,
        "strong_block_count": len(strong_blocks),
        "first_strong_blocks": strong_blocks[:5],
        "best_blocks": [record for record in records if record["leakage_count"] == best][:5],
        "aligned_window_count": len(aligned_records),
        "aligned_min_leakage_count": aligned_best,
        "aligned_strong_block_count": len(aligned_strong_blocks),
        "aligned_best_blocks": [
            record for record in aligned_records if record["leakage_count"] == aligned_best
        ][:5],
    }


def audit_pair(p: int, x: int) -> dict:
    """审计一个 p:x。"""
    branches = []
    for sign, value in [(-1, p - 1), (+1, p + 1)]:
        for pi in prime_factors(value):
            if pi < p:
                branches.append(audit_branch(p, x, pi, sign))
    return {"p": p, "x": x, "is_zero_row": is_zero_row(p, x), "branches": branches}


def parse_pairs(raw: str) -> list[tuple[int, int]]:
    """解析 p:x,p:x。"""
    pairs: list[tuple[int, int]] = []
    for item in raw.split(","):
        if not item.strip():
            continue
        left, right = item.split(":")
        pairs.append((int(left), int(right)))
    return pairs


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", type=str, default="23:58,17:1210,19:3658")
    args = parser.parse_args()

    for p, x in parse_pairs(args.pairs):
        print(audit_pair(p, x), flush=True)


if __name__ == "__main__":
    main()
