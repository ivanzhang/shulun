#!/usr/bin/env python3
"""AlphaTail 的精确坏高标签命中审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_bad_audit.py --selected 499,997 --alpha 0.9

对 alpha>1/2，C_alpha 按高标签 q 命中计数。每个命中 n=p^2+k=q*m：
- 若 n 是低洞，则它计入 H_alpha；
- 若 n 不是低洞，则它是 bad_high_hit。
由于 alpha>1/2，H_alpha>C_alpha 等价于 diagonal_prime_count>bad_high_hit_count。
"""

from __future__ import annotations

import argparse
from math import isqrt


def is_prime(value: int) -> bool:
    """朴素素性测试。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    return [value for value in range(2, limit + 1) if is_prime(value)]


def least_prime_factor(value: int) -> int:
    """返回最小素因子；素数返回自身。"""
    if value % 2 == 0:
        return 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return divisor
        divisor += 2
    return value


def audit_prime(prime_bound: int, alpha: float) -> dict:
    """审计单个 p。"""
    cutoff = int(alpha * prime_bound)
    prime_columns: list[int] = []
    low_semiprime_columns: list[int] = []
    bad_high_hits: list[dict] = []
    high_capacity = 0

    for column in range(1, prime_bound):
        value = prime_bound * prime_bound + column
        least = least_prime_factor(value)
        if least == value:
            prime_columns.append(column)
        elif least > cutoff:
            low_semiprime_columns.append(column)

    low_holes = len(prime_columns) + len(low_semiprime_columns)

    for q in primes_upto(prime_bound - 1):
        if q <= cutoff:
            continue
        residue = (-prime_bound * prime_bound) % q
        column = residue if residue > 0 else q
        while column < prime_bound:
            high_capacity += 1
            value = prime_bound * prime_bound + column
            least = least_prime_factor(value)
            if least <= cutoff:
                bad_high_hits.append(
                    {
                        "k": column,
                        "q": q,
                        "cofactor": value // q,
                        "least_factor": least,
                    }
                )
            column += q

    return {
        "p": prime_bound,
        "alpha": alpha,
        "cutoff": cutoff,
        "prime_count": len(prime_columns),
        "low_semiprime_count": len(low_semiprime_columns),
        "low_holes": low_holes,
        "high_capacity": high_capacity,
        "bad_high_hit_count": len(bad_high_hits),
        "H_minus_C": low_holes - high_capacity,
        "P_minus_Bad": len(prime_columns) - len(bad_high_hits),
        "prime_columns": prime_columns[:20],
        "bad_high_hits": bad_high_hits[:20],
    }


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="499,997,5003")
    parser.add_argument("--alpha", type=float, default=0.9)
    args = parser.parse_args()

    for prime_bound in parse_int_list(args.selected):
        print(audit_prime(prime_bound, args.alpha), flush=True)


if __name__ == "__main__":
    main()
