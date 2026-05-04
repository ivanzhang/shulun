#!/usr/bin/env python3
"""DLS13 低模/尾项端点缺陷分层审计。

用法示例：
  python3 experiments/prime_matrix_dls13_lowmod_tail_audit.py --selected 101,499,997 --D 1000
  python3 experiments/prime_matrix_dls13_lowmod_tail_audit.py --selected 5003 --Ds 100,1000,10000

计算 y=floor(2p/3) 下：
  E_total = H_y - (p-1) V_y
  E_low(D)=sum_{d<=D,d|M_y} mu(d)(N_d-(p-1)/d)
  E_tail(D)=E_total-E_low(D)
并对照分割容量失败阈值 T=C_y-(p-1)V_y。
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


def mobius_squarefree_table(limit: int) -> list[tuple[int, int]]:
    """返回 d<=limit 的 squarefree d 与 mu(d)。"""
    records: list[tuple[int, int]] = [(1, 1)]
    primes = primes_upto(limit)
    for value in range(2, limit + 1):
        remaining = value
        omega = 0
        squarefree = True
        for prime in primes:
            if prime * prime > remaining:
                break
            if remaining % prime != 0:
                continue
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            if exponent > 1:
                squarefree = False
                break
            omega += 1
        if not squarefree:
            continue
        if remaining > 1:
            omega += 1
        records.append((value, -1 if omega % 2 else 1))
    return records


def low_divisors(cutoff: int, limit: int) -> list[tuple[int, int]]:
    """筛出 d<=limit 且所有素因子 <=cutoff 的 squarefree d。"""
    allowed = set(primes_upto(cutoff))
    records: list[tuple[int, int]] = []
    for value, mu in mobius_squarefree_table(limit):
        remaining = value
        ok = True
        for prime in primes_upto(isqrt(value) + 1):
            if remaining % prime != 0:
                continue
            if prime not in allowed:
                ok = False
                break
            while remaining % prime == 0:
                remaining //= prime
        if ok and remaining > 1 and remaining not in allowed:
            ok = False
        if ok:
            records.append((value, mu))
    return records


def count_residue_in_interval(prime_bound: int, divisor: int) -> int:
    """计算 1<=k<p 且 k≡-p^2 mod divisor 的个数。"""
    residue = (-prime_bound * prime_bound) % divisor
    column = residue if residue > 0 else divisor
    count = 0
    while column < prime_bound:
        count += 1
        column += divisor
    return count


def low_hole_count(prime_bound: int, cutoff: int) -> int:
    """计算 H_y(p)。"""
    low_primes = primes_upto(cutoff)
    holes = 0
    for column in range(1, prime_bound):
        value = prime_bound * prime_bound + column
        if all(value % prime for prime in low_primes):
            holes += 1
    return holes


def exact_high_capacity(prime_bound: int, cutoff: int) -> int:
    """计算 C_y(p)。"""
    total = 0
    for prime in primes_upto(prime_bound - 1):
        if prime <= cutoff:
            continue
        total += count_residue_in_interval(prime_bound, prime)
    return total


def main_density(cutoff: int) -> float:
    """计算 V_y。"""
    density = 1.0
    for prime in primes_upto(cutoff):
        density *= 1.0 - 1.0 / prime
    return density


def low_endpoint(prime_bound: int, cutoff: int, divisor_limit: int) -> tuple[float, int]:
    """计算 E_low(D) 及使用的低模个数。"""
    total = 0.0
    divisors = low_divisors(cutoff, divisor_limit)
    interval_length = prime_bound - 1
    for divisor, mu in divisors:
        count = count_residue_in_interval(prime_bound, divisor)
        total += mu * (count - interval_length / divisor)
    return total, len(divisors)


def audit_prime(prime_bound: int, divisor_limits: list[int]) -> dict:
    """审计一个 p 的多个 D。"""
    cutoff = (2 * prime_bound) // 3
    holes = low_hole_count(prime_bound, cutoff)
    capacity = exact_high_capacity(prime_bound, cutoff)
    main = (prime_bound - 1) * main_density(cutoff)
    endpoint_total = holes - main
    failure_threshold = capacity - main
    records = []
    for divisor_limit in divisor_limits:
        endpoint_low, divisor_count = low_endpoint(prime_bound, cutoff, divisor_limit)
        endpoint_tail = endpoint_total - endpoint_low
        records.append(
            {
                "D": divisor_limit,
                "divisor_count": divisor_count,
                "E_low": endpoint_low,
                "E_tail": endpoint_tail,
                "E_low_fraction_of_failure": endpoint_low / failure_threshold
                if failure_threshold
                else None,
                "E_tail_fraction_of_failure": endpoint_tail / failure_threshold
                if failure_threshold
                else None,
            }
        )
    return {
        "p": prime_bound,
        "cutoff": cutoff,
        "main": main,
        "low_holes": holes,
        "high_capacity": capacity,
        "E_total": endpoint_total,
        "failure_threshold": failure_threshold,
        "margin": endpoint_total - failure_threshold,
        "records": records,
    }


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="101,499,997")
    parser.add_argument("--D", type=int, default=1000)
    parser.add_argument("--Ds", type=str, default="")
    args = parser.parse_args()

    divisor_limits = parse_int_list(args.Ds) if args.Ds else [args.D]
    for prime_bound in parse_int_list(args.selected):
        print(audit_prime(prime_bound, divisor_limits), flush=True)


if __name__ == "__main__":
    main()
