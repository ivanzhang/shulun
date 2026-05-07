#!/usr/bin/env python3
"""Prime Matrix 终端行与 P^2 前素数间隙审计。

用法示例：
  python3 experiments/prime_matrix_terminal_row_gap_audit.py --max-p 5000 --format table
"""

from __future__ import annotations

import argparse
import json
from math import isqrt, log


def prime_sieve(limit: int) -> bytearray:
    """返回素数指示数组。"""
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if sieve[value]:
            start = value * value
            sieve[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return sieve


def prefix_counts(is_prime: bytearray) -> list[int]:
    """返回素数计数前缀和。"""
    prefix = [0] * len(is_prime)
    total = 0
    for value, flag in enumerate(is_prime):
        total += int(flag)
        prefix[value] = total
    return prefix


def primes_from_sieve(is_prime: bytearray, max_p: int) -> list[int]:
    """提取不超过 max_p 的奇素数。"""
    return [value for value in range(3, max_p + 1) if is_prime[value]]


def previous_prime(is_prime: bytearray, value: int) -> int | None:
    """返回小于 value 的最大素数。"""
    for candidate in range(value - 1, 1, -1):
        if is_prime[candidate]:
            return candidate
    return None


def audit(max_p: int) -> dict:
    """审计每个素数 P 的终端行。"""
    limit = max_p * max_p
    is_prime = prime_sieve(limit)
    prefix = prefix_counts(is_prime)
    primes = primes_from_sieve(is_prime, max_p)
    rows = []
    failures = []
    for p in primes:
        left = p * (p - 1)
        right = p * p - 1
        count = prefix[right] - prefix[left]
        prev = previous_prime(is_prime, p * p)
        gap_to_square = p * p - prev if prev is not None else None
        row = {
            "p": p,
            "terminal_x": p - 1,
            "interval": [left + 1, right],
            "prime_count": count,
            "previous_prime": prev,
            "gap_to_square": gap_to_square,
            "gap_over_p": gap_to_square / p if gap_to_square is not None else None,
            "count_over_p_log": count / (p / log(p)),
            "terminal_row_holds": count > 0,
        }
        rows.append(row)
        if count == 0:
            failures.append(row)
    worst_gap = max(rows, key=lambda row: row["gap_to_square"] or 0) if rows else None
    min_count = min((row["prime_count"] for row in rows), default=None)
    thin_rows = [row for row in rows if row["prime_count"] == min_count][:10]
    return {
        "max_p": max_p,
        "prime_count": len(primes),
        "status": "terminal_row_sample_verified_global_open",
        "failure_count": len(failures),
        "failures": failures[:10],
        "min_terminal_prime_count": min_count,
        "thin_rows": thin_rows,
        "worst_gap_to_square": worst_gap,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出终端行审计简表。"""
    print(
        "max_p prime_count failures min_count worst_p worst_gap worst_gap_over_p thin_rows",
        flush=True,
    )
    worst = package["worst_gap_to_square"] or {}
    thin = ";".join(
        f"P={row['p']}:count={row['prime_count']}:gap={row['gap_to_square']}"
        for row in package["thin_rows"]
    )
    print(
        f"{package['max_p']} {package['prime_count']} {package['failure_count']} "
        f"{package['min_terminal_prime_count']} {worst.get('p')} "
        f"{worst.get('gap_to_square')} {worst.get('gap_over_p')} {thin}",
        flush=True,
    )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()
    package = audit(args.max_p)
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
