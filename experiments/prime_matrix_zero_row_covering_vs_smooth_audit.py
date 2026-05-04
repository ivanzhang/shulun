#!/usr/bin/env python3
"""零行覆盖条件与 p-光滑条件的差异审计。

用法示例：
  python3 experiments/prime_matrix_zero_row_covering_vs_smooth_audit.py

本脚本用于复核：
1. 旧文档中的第 r 行采用区间 [(r-1)p+1, rp]；
2. 用户新记号 px+k 中的 x 等于旧行号 r-1；
3. “至少有一个 <=p 小素因子”不等于“p-光滑”。
"""

from __future__ import annotations

from math import isqrt, prod


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def factorize(value: int) -> list[tuple[int, int]]:
    """朴素整数分解，足够覆盖本文小样本。"""
    factors: list[tuple[int, int]] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def small_factors(value: int, p: int) -> list[int]:
    """列出 value 的 <=p 素因子。"""
    return [prime for prime in primes_upto(p) if value % prime == 0]


def is_zero_multiplier(p: int, x: int) -> bool:
    """判断乘数 x 是否使 px+1 到 px+p 成为 <=p 小素因子覆盖行。"""
    return all(small_factors(p * x + k, p) for k in range(1, p + 1))


def first_zero_multiplier(p: int, limit: int | None = None) -> tuple[int | None, bool]:
    """扫描首个零行乘数；当周期较小时给出严格全周期结论。"""
    modulus = prod(prime for prime in primes_upto(p - 1))
    bound = modulus if limit is None else min(limit, modulus)
    for x in range(1, bound + 1):
        if is_zero_multiplier(p, x):
            return x, limit is None or bound == modulus
    return None, limit is None or bound == modulus


def p23_profiles() -> None:
    """打印 p=23 的 x=58 与 x=59 两个剖面。"""
    p = 23
    for x in (58, 59):
        print(f"\nP={p}, multiplier x={x}, one-indexed row r={x + 1}, interval=[{p*x+1},{p*x+p}]")
        is_zero = True
        for k in range(1, p + 1):
            value = p * x + k
            sf = small_factors(value, p)
            if not sf:
                is_zero = False
            print(f"k={k:2d} n={value:4d} small={sf} factor={factorize(value)}")
        print(f"zero_by_small_factor={is_zero}")


def small_prime_table() -> None:
    """打印小素数首个零行表。"""
    print("\nsmall-prime exact table")
    print("p | modulus M=prod(q<p) | first x | row r=x+1 | exact")
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        x, exact = first_zero_multiplier(p)
        modulus = prod(prime for prime in primes_upto(p - 1))
        row = None if x is None else x + 1
        print(f"{p:2d} | {modulus:10d} | {str(x):>7} | {str(row):>9} | {exact}")


def bounded_large_table() -> None:
    """打印较大 p 的有界搜索表，避免误标为全周期证明。"""
    print("\nbounded search table")
    print("p | search bound | first x found | row r=x+1 | exact")
    for p in (29, 31):
        x, exact = first_zero_multiplier(p, limit=200_000)
        row = None if x is None else x + 1
        print(f"{p:2d} | {200000:12d} | {str(x):>13} | {str(row):>9} | {exact}")


def main() -> None:
    """执行审计。"""
    p23_profiles()
    small_prime_table()
    bounded_large_table()


if __name__ == "__main__":
    main()
