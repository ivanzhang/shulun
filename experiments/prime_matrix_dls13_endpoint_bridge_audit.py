#!/usr/bin/env python3
"""DLS13 端点缺陷桥审计。

用法示例：
  python3 experiments/prime_matrix_dls13_endpoint_bridge_audit.py --selected 101,499,997

对 y=floor(2p/3)，计算：
  main=(p-1) prod_{q<=y}(1-1/q)
  endpoint=|H_y|-main
  cap=C_y
若 |H_y|<=cap，则必有 endpoint<=cap-main。
实际样本显示 endpoint 虽为负，但远未达到失败所需阈值。
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


def low_hole_count(prime_bound: int, cutoff: int) -> int:
    """计算对角行低骨架洞数。"""
    low_primes = primes_upto(cutoff)
    holes = 0
    for column in range(1, prime_bound):
        value = prime_bound * prime_bound + column
        if all(value % prime for prime in low_primes):
            holes += 1
    return holes


def exact_high_capacity(prime_bound: int, cutoff: int) -> int:
    """计算 q>cutoff 的固定相位实际容量。"""
    total = 0
    for prime in primes_upto(prime_bound - 1):
        if prime <= cutoff:
            continue
        residue = (-prime_bound * prime_bound) % prime
        column = residue if residue > 0 else prime
        while column < prime_bound:
            total += 1
            column += prime
    return total


def main_density(cutoff: int) -> float:
    """计算低骨架 Euler 主密度。"""
    density = 1.0
    for prime in primes_upto(cutoff):
        density *= 1.0 - 1.0 / prime
    return density


def audit_prime(prime_bound: int) -> dict:
    """审计单个 p 的端点缺陷桥。"""
    cutoff = (2 * prime_bound) // 3
    holes = low_hole_count(prime_bound, cutoff)
    capacity = exact_high_capacity(prime_bound, cutoff)
    main = (prime_bound - 1) * main_density(cutoff)
    endpoint = holes - main
    failure_threshold = capacity - main
    return {
        "p": prime_bound,
        "cutoff": cutoff,
        "main": main,
        "low_holes": holes,
        "high_capacity": capacity,
        "endpoint": endpoint,
        "failure_threshold": failure_threshold,
        "endpoint_margin_to_failure": endpoint - failure_threshold,
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
