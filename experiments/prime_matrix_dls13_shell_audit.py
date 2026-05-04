#!/usr/bin/env python3
"""DLS-13 低洞的素数/半素数壳层分解审计。

用法示例：
  python3 experiments/prime_matrix_dls13_shell_audit.py --selected 101,499,997

对 y=floor(2p/3)，精确分解：
  |H_y(p)| = diagonal_prime_count + semiprime_shell_count
其中 semiprime_shell 由 q in (y,p), r in (p,3p/2) 的 qr=p^2+k 给出。
"""

from __future__ import annotations

import argparse
from math import isqrt


def is_prime(value: int) -> bool:
    """朴素素性测试，适合当前审计规模。"""
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


def least_prime_factor(value: int) -> int | None:
    """返回 value 的最小素因子；素数返回自身。"""
    if value < 2:
        return None
    if value % 2 == 0:
        return 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return divisor
        divisor += 2
    return value


def audit_prime(prime_bound: int) -> dict:
    """审计单个 p 的 DLS-13 分解。"""
    cutoff = (2 * prime_bound) // 3
    prime_columns: list[int] = []
    shell_records: list[dict] = []
    low_holes = 0

    for column in range(1, prime_bound):
        value = prime_bound * prime_bound + column
        least = least_prime_factor(value)
        if least is None or least <= cutoff:
            continue
        low_holes += 1
        if least == value:
            prime_columns.append(column)
            continue
        cofactor = value // least
        shell_records.append(
            {
                "k": column,
                "q": least,
                "r": cofactor,
                "a": prime_bound - least,
                "b": cofactor - prime_bound,
                "d": cofactor - prime_bound - (prime_bound - least),
            }
        )

    high_primes = [prime for prime in primes_upto(prime_bound - 1) if prime > cutoff]
    return {
        "p": prime_bound,
        "cutoff": cutoff,
        "low_holes": low_holes,
        "prime_count": len(prime_columns),
        "prime_columns": prime_columns[:20],
        "semiprime_shell_count": len(shell_records),
        "semiprime_shell_records": shell_records[:20],
        "high_prime_count": len(high_primes),
    }


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="101,499,997")
    args = parser.parse_args()

    for prime_bound in parse_int_list(args.selected):
        print(audit_prime(prime_bound), flush=True)


if __name__ == "__main__":
    main()
