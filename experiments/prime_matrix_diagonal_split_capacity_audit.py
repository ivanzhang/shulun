#!/usr/bin/env python3
"""EDA 对角低骨架/高标签容量分割审计。

用法示例：
  python3 experiments/prime_matrix_diagonal_split_capacity_audit.py --selected 101,499,997
  python3 experiments/prime_matrix_diagonal_split_capacity_audit.py --selected 10007 --alphas 0.5,0.66,0.75

对 x=p 的对角行，给定 cutoff y=floor(alpha*p)：
- low_holes: 未被 q<=y 的固定相位覆盖的列数；
- exact_high_capacity: q>y 的固定相位在 [1,p-1] 中实际出现总次数；
- margin = low_holes - exact_high_capacity。
若 margin>0，则该 p 的对角行不可能全覆盖。
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
    """计算对角行未被 q<=cutoff 覆盖的列数。"""
    low_primes = [prime for prime in primes_upto(cutoff) if prime < prime_bound]
    holes = 0
    for column in range(1, prime_bound):
        value = prime_bound * prime_bound + column
        if all(value % prime for prime in low_primes):
            holes += 1
    return holes


def exact_high_capacity(prime_bound: int, cutoff: int) -> tuple[int, dict[int, int]]:
    """计算 q>cutoff 的固定相位实际容量和每素数命中次数分布。"""
    total = 0
    histogram: dict[int, int] = {}
    for prime in primes_upto(prime_bound - 1):
        if prime <= cutoff:
            continue
        residue = (-prime_bound * prime_bound) % prime
        column = residue if residue > 0 else prime
        count = 0
        while column < prime_bound:
            count += 1
            column += prime
        total += count
        histogram[count] = histogram.get(count, 0) + 1
    return total, dict(sorted(histogram.items()))


def audit_prime(prime_bound: int, alphas: list[float]) -> dict:
    """审计一个 p 的多个 alpha 分割。"""
    records = []
    for alpha in alphas:
        cutoff = int(alpha * prime_bound)
        holes = low_hole_count(prime_bound, cutoff)
        capacity, histogram = exact_high_capacity(prime_bound, cutoff)
        records.append(
            {
                "alpha": alpha,
                "cutoff": cutoff,
                "low_holes": holes,
                "exact_high_capacity": capacity,
                "margin": holes - capacity,
                "high_hit_histogram": histogram,
            }
        )
    return {"p": prime_bound, "records": records}


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def parse_float_list(raw: str) -> list[float]:
    """解析逗号分隔小数列表。"""
    return [float(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="23,101,499,997")
    parser.add_argument("--alphas", type=str, default="0.5,0.66,0.75,0.8,0.9")
    args = parser.parse_args()

    alphas = parse_float_list(args.alphas)
    for prime_bound in parse_int_list(args.selected):
        print(audit_prime(prime_bound, alphas), flush=True)


if __name__ == "__main__":
    main()
