#!/usr/bin/env python3
"""EDA ExactEndpoint-MinRep 缺陷综合审计。

用法示例：
  python3 experiments/prime_matrix_eda_exact_defect_audit.py --selected 23,101,499
  python3 experiments/prime_matrix_eda_exact_defect_audit.py --selected 23 --cutoffs 3,5,7,11

脚本输出早期行的精确筛余最小值、对角行余量、低骨架残洞与高标签容量，
并对最小余量行做因子降阶阻塞审计。
"""

from __future__ import annotations

import argparse
from math import ceil, gcd, isqrt


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


def least_positive_residue(value: int, modulus: int) -> int:
    """返回模 modulus 的最小正代表。"""
    if modulus == 1:
        return 1
    residue = value % modulus
    return residue if residue > 0 else modulus


def survivor_columns(prime_bound: int, row_multiplier: int) -> list[int]:
    """返回没有被 <p 素数覆盖的列。"""
    small_primes = primes_upto(prime_bound - 1)
    survivors: list[int] = []
    for column in range(1, prime_bound):
        value = prime_bound * row_multiplier + column
        if all(value % prime for prime in small_primes):
            survivors.append(column)
    return survivors


def low_skeleton_holes(prime_bound: int, row_multiplier: int, cutoff: int) -> list[int]:
    """返回没有被 <=cutoff 低骨架素数覆盖的列。"""
    low_primes = [prime for prime in primes_upto(cutoff) if prime < prime_bound]
    holes: list[int] = []
    for column in range(1, prime_bound):
        value = prime_bound * row_multiplier + column
        if all(value % prime for prime in low_primes):
            holes.append(column)
    return holes


def high_label_capacity(prime_bound: int, cutoff: int) -> int:
    """计算高标签按单相位等差类最多可覆盖的列数总容量。"""
    total = 0
    for prime in primes_upto(prime_bound - 1):
        if prime > cutoff:
            total += ceil((prime_bound - 1) / prime)
    return total


def leakage_records(prime_bound: int, row_multiplier: int) -> list[dict]:
    """对 row_multiplier 的每个素因子审计降阶泄漏与代表逃逸。"""
    records: list[dict] = []
    for factor in prime_factors(row_multiplier):
        if factor >= prime_bound:
            continue
        quotient = row_multiplier // factor
        reduced_multiplier = prime_bound * quotient
        modulus = primorial_below(factor)
        reduced_rep = least_positive_residue(reduced_multiplier, modulus)
        leakage_columns: list[int] = []
        for column in range(1, factor):
            value = prime_bound * row_multiplier + column
            if gcd(value, modulus) == 1:
                leakage_columns.append(column)
        records.append(
            {
                "pi": factor,
                "leakage_count": len(leakage_columns),
                "leakage_columns": leakage_columns[:12],
                "reduced_rep": reduced_rep,
                "range_escape": reduced_rep > factor,
            }
        )
    return records


def audit_prime(prime_bound: int, cutoffs: list[int]) -> dict:
    """审计一个素数 p 的早期对角段。"""
    min_survivor_count = prime_bound
    min_rows: list[int] = []
    diagonal_survivors: list[int] = []

    for row_multiplier in range(1, prime_bound + 1):
        survivors = survivor_columns(prime_bound, row_multiplier)
        survivor_count = len(survivors)
        if row_multiplier == prime_bound:
            diagonal_survivors = survivors
        if survivor_count < min_survivor_count:
            min_survivor_count = survivor_count
            min_rows = [row_multiplier]
        elif survivor_count == min_survivor_count:
            min_rows.append(row_multiplier)

    focus_row = min_rows[0]
    low_skeleton = []
    for cutoff in cutoffs:
        holes = low_skeleton_holes(prime_bound, focus_row, cutoff)
        capacity = high_label_capacity(prime_bound, cutoff)
        low_skeleton.append(
            {
                "cutoff": cutoff,
                "holes": len(holes),
                "high_capacity": capacity,
                "capacity_margin": capacity - len(holes),
            }
        )

    return {
        "p": prime_bound,
        "min_U": min_survivor_count,
        "min_rows": min_rows[:10],
        "diagonal_U": len(diagonal_survivors),
        "focus_row": focus_row,
        "factor_defects": leakage_records(prime_bound, focus_row),
        "low_skeleton": low_skeleton,
    }


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="23,101,499")
    parser.add_argument("--cutoffs", type=str, default="3,5,7,11,17,31")
    args = parser.parse_args()

    cutoffs = parse_int_list(args.cutoffs)
    for prime_bound in parse_int_list(args.selected):
        print(audit_prime(prime_bound, cutoffs), flush=True)


if __name__ == "__main__":
    main()
