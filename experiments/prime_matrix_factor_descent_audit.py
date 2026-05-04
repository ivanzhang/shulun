#!/usr/bin/env python3
"""因子降阶审计。

用法示例：
  python3 experiments/prime_matrix_factor_descent_audit.py --pairs 23:58,13:168
  python3 experiments/prime_matrix_factor_descent_audit.py --p 23 --x 58

给定 P-零行乘数 x，脚本检查每个素因子 pi|x 的降阶情况：
- leakage_count: 前 pi-1 列中没有 <pi 素因子覆盖的列数；
- reduced_multiplier: X=P*x/pi；
- reduced_rep: X mod M_pi 的最小正代表；
- early_rep_hit: reduced_rep<=pi。
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


def least_positive_residue(value: int, modulus: int) -> int:
    """返回模 modulus 的最小正代表。"""
    if modulus == 1:
        return 1
    residue = value % modulus
    return residue if residue > 0 else modulus


def is_zero_row(p: int, x: int) -> bool:
    """检查 x 是否为 p-筛零行乘数。"""
    small_primes = primes_upto(p - 1)
    for column in range(1, p):
        value = p * x + column
        if not any(value % prime == 0 for prime in small_primes):
            return False
    return True


def audit_factor_descent(p: int, x: int) -> dict:
    """审计一个 P,x 的所有可降阶素因子。"""
    records = []
    for factor in prime_factors(x):
        if factor >= p:
            continue
        y = x // factor
        reduced_multiplier = p * y
        modulus = primorial_below(factor)
        reduced_rep = least_positive_residue(reduced_multiplier, modulus)
        leakage_columns = []
        leakage_witnesses = []
        for column in range(1, factor):
            value = p * x + column
            if gcd(value, modulus) == 1:
                leakage_columns.append(column)
                witness = None
                for prime in primes_upto(p - 1):
                    if value % prime == 0:
                        witness = prime
                        break
                leakage_witnesses.append((column, witness))
        records.append(
            {
                "factor_pi": factor,
                "reduced_multiplier": reduced_multiplier,
                "M_pi": modulus,
                "reduced_rep": reduced_rep,
                "early_rep_hit": reduced_rep <= factor,
                "leakage_count": len(leakage_columns),
                "leakage_columns": leakage_columns[:20],
                "leakage_witnesses": leakage_witnesses[:20],
                "strong_descent": len(leakage_columns) == 0,
                "contradicts_EDA_pi_if_known": len(leakage_columns) == 0 and reduced_rep <= factor,
            }
        )
    return {
        "p": p,
        "x": x,
        "is_zero_row": is_zero_row(p, x),
        "factor_records": records,
    }


def parse_pairs(raw: str) -> list[tuple[int, int]]:
    """解析 P:x,P:x 格式。"""
    pairs = []
    for item in raw.split(","):
        if not item.strip():
            continue
        left, right = item.split(":")
        pairs.append((int(left), int(right)))
    return pairs


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=0)
    parser.add_argument("--x", type=int, default=0)
    parser.add_argument("--pairs", type=str, default="")
    args = parser.parse_args()

    pairs = parse_pairs(args.pairs) if args.pairs else [(args.p, args.x)]
    for p, x in pairs:
        print(audit_factor_descent(p, x), flush=True)


if __name__ == "__main__":
    main()
