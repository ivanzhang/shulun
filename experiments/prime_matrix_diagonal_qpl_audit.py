#!/usr/bin/env python3
"""EDA 对角二次相位锁审计。

用法示例：
  python3 experiments/prime_matrix_diagonal_qpl_audit.py --selected 23,101,499

脚本只审计 x=p 对角行：
  p^2+1, ..., p^2+p-1
输出未被 <p 素数覆盖的 k、每列最小覆盖素数、以及幸存 k 的二次字符避让摘要。
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


def legendre_symbol(value: int, prime: int) -> int:
    """返回 Legendre 符号，输入 prime 必须为奇素数。"""
    residue = value % prime
    if residue == 0:
        return 0
    result = pow(residue, (prime - 1) // 2, prime)
    return -1 if result == prime - 1 else result


def least_factor_below(value: int, bound: int) -> int | None:
    """返回 value 的最小 <bound 素因子；若无则返回 None。"""
    for prime in primes_upto(bound - 1):
        if value % prime == 0:
            return prime
    return None


def audit_prime(prime_bound: int) -> dict:
    """审计单个 p 的对角行。"""
    survivors: list[int] = []
    least_factor_hist: dict[int, int] = {}
    odd_primes = [prime for prime in primes_upto(prime_bound - 1) if prime > 2]
    qpl_defect_counts: list[dict] = []

    for column in range(1, prime_bound):
        value = prime_bound * prime_bound + column
        least_factor = least_factor_below(value, prime_bound)
        if least_factor is None:
            survivors.append(column)
            opposite_count = 0
            exact_avoid_count = 0
            for q in odd_primes:
                if column % q == 0:
                    exact_avoid_count += 1
                    continue
                if legendre_symbol(column, q) == -legendre_symbol(-1, q):
                    opposite_count += 1
                if column % q != (-prime_bound * prime_bound) % q:
                    exact_avoid_count += 1
            qpl_defect_counts.append(
                {
                    "k": column,
                    "opposite_legendre_count": opposite_count,
                    "exact_avoid_count": exact_avoid_count,
                    "odd_prime_count": len(odd_primes),
                }
            )
        else:
            least_factor_hist[least_factor] = least_factor_hist.get(least_factor, 0) + 1

    return {
        "p": prime_bound,
        "diagonal_U": len(survivors),
        "survivor_k": survivors[:20],
        "least_factor_hist": dict(sorted(least_factor_hist.items())),
        "qpl_survivor_summary": qpl_defect_counts[:20],
    }


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="23,101,499")
    args = parser.parse_args()

    for prime_bound in parse_int_list(args.selected):
        print(audit_prime(prime_bound), flush=True)


if __name__ == "__main__":
    main()
