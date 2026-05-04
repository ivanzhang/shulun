#!/usr/bin/env python3
"""EDA LowMod/PDEC 证书审计。

用法示例：
  python3 experiments/prime_matrix_eda_lowmod_pdec_audit.py --selected 23,101,499 --D 30
  python3 experiments/prime_matrix_eda_lowmod_pdec_audit.py --max-p 200 --D 60 --tail-frac 0.5

脚本计算低模端点函数
  F_{p,D}(x)=sum_{d|M_<p,d<=D} mu(d)({px/d}-{(px+p-1)/d})
并用 EDA-BK 的正主项阈值 Lambda=(p-1)G_K 审计坏行集合。
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


def odd_primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的奇素数。"""
    return [prime for prime in primes_upto(limit) if prime >= 3]


def mobius_squarefree_table(limit: int) -> list[tuple[int, int, int]]:
    """返回 d<=limit 的 squarefree d、mu(d)、omega(d)。"""
    records: list[tuple[int, int, int]] = [(1, 1, 0)]
    for value in range(2, limit + 1):
        remaining = value
        omega = 0
        squarefree = True
        for prime in primes_upto(isqrt(value) + 1):
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
        mu = -1 if omega % 2 else 1
        records.append((value, mu, omega))
    return records


def low_divisors(p: int, limit: int) -> list[tuple[int, int, int]]:
    """筛出 d|M_<p 且 d<=limit 的 squarefree 低模。"""
    small_primes = set(primes_upto(p - 1))
    records = []
    for value, mu, omega in mobius_squarefree_table(limit):
        if value == 1:
            records.append((value, mu, omega))
            continue
        remaining = value
        ok = True
        for prime in primes_upto(isqrt(value) + 1):
            if remaining % prime == 0:
                if prime not in small_primes:
                    ok = False
                    break
                while remaining % prime == 0:
                    remaining //= prime
        if ok and remaining > 1 and remaining not in small_primes:
            ok = False
        if ok:
            records.append((value, mu, omega))
    return records


def positive_main_density(p: int) -> float:
    """计算 K_* 对应的正主项密度 G_{K_*}。"""
    primes = primes_upto(p - 1)
    density = 1.0
    reciprocal_product = 1.0
    for prime in primes:
        density *= 1.0 - 1.0 / prime
        reciprocal_product *= 1.0 / prime
    if len(primes) % 2 == 1:
        return density
    return density - reciprocal_product


def lowmod_value(p: int, x: int, divisors: list[tuple[int, int, int]]) -> float:
    """计算早期行 x 的低模端点函数。"""
    h = p - 1
    total = 0.0
    px = p * x
    for divisor, mu, _omega in divisors:
        left = (px % divisor) / divisor
        right = ((px + h) % divisor) / divisor
        total += mu * (left - right)
    return total


def audit_prime(p: int, limit: int, tail_frac: float) -> dict:
    """审计单个 p 的 LowMod 坏行。"""
    divisors = low_divisors(p, limit)
    h = p - 1
    main_density = positive_main_density(p)
    lambda_p = h * main_density
    threshold = -(1.0 - tail_frac) * lambda_p

    min_value = 10**100
    min_rows: list[int] = []
    bad_rows: list[int] = []

    for x in range(1, p + 1):
        value = lowmod_value(p, x, divisors)
        if value < min_value:
            min_value = value
            min_rows = [x]
        elif value == min_value:
            min_rows.append(x)
        if value <= threshold:
            bad_rows.append(x)

    return {
        "p": p,
        "D": limit,
        "tail_frac": tail_frac,
        "divisor_count": len(divisors),
        "max_omega_d": max(omega for _d, _mu, omega in divisors),
        "main_density": main_density,
        "lambda": lambda_p,
        "lowmod_threshold": threshold,
        "min_lowmod": min_value,
        "min_rows": min_rows[:10],
        "bad_row_count": len(bad_rows),
        "bad_rows": bad_rows[:20],
    }


def parse_selected(raw: str) -> list[int]:
    """解析逗号分隔素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--selected", type=str, default="")
    parser.add_argument("--D", type=int, default=30)
    parser.add_argument("--tail-frac", type=float, default=0.5)
    args = parser.parse_args()

    primes = parse_selected(args.selected) if args.selected else odd_primes_upto(args.max_p)
    for p in primes:
        print(audit_prime(p, args.D, args.tail_frac), flush=True)


if __name__ == "__main__":
    main()
