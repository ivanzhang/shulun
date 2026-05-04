#!/usr/bin/env python3
"""EDA 变量阶 Bonferroni 精确性审计。

用法示例：
  python3 experiments/prime_matrix_eda_variable_order_audit.py --selected 23,101,499
  python3 experiments/prime_matrix_eda_variable_order_audit.py --max-p 200

脚本选取 K_p 为不小于 floor(log2(p^2+p-1)) 的奇数，验证 S_K(p,x)=U_p(x)。
"""

from __future__ import annotations

import argparse
from math import comb, isqrt, log2


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


def variable_order(p: int) -> int:
    """返回覆盖早期区段最大 omega 的奇数阶 K_p。"""
    omega_bound = int(log2(p * p + p - 1))
    return omega_bound if omega_bound % 2 else omega_bound + 1


def omega_small_table(p: int) -> bytearray:
    """计算 n<=p^2+p 的 <p 不同素因子个数。"""
    limit = p * p + p
    omega = bytearray(limit + 1)
    for prime in primes_upto(p - 1):
        for multiple in range(prime, limit + 1, prime):
            omega[multiple] += 1
    return omega


def bonferroni_weight(t: int, order: int) -> int:
    """单点 Bonferroni 权重。"""
    return sum(((-1) ** j) * comb(t, j) for j in range(0, min(order, t) + 1))


def audit_prime(p: int) -> dict:
    """审计单个 p 的变量阶精确性。"""
    order = variable_order(p)
    omega = omega_small_table(p)
    max_seen = 0
    min_exact = p
    min_s = p
    mismatch_rows = []
    for x in range(1, p + 1):
        exact = 0
        s_value = 0
        for value in range(p * x + 1, p * x + p):
            t = omega[value]
            max_seen = max(max_seen, t)
            if t == 0:
                exact += 1
            s_value += bonferroni_weight(t, order)
        min_exact = min(min_exact, exact)
        min_s = min(min_s, s_value)
        if exact != s_value:
            mismatch_rows.append((x, exact, s_value))
    return {
        "p": p,
        "K_p": order,
        "max_omega_seen": max_seen,
        "min_exact_U": min_exact,
        "min_S_K": min_s,
        "mismatch_count": len(mismatch_rows),
        "mismatch_rows": mismatch_rows[:10],
    }


def parse_selected(raw: str) -> list[int]:
    """解析逗号分隔素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--selected", type=str, default="")
    args = parser.parse_args()

    primes = parse_selected(args.selected) if args.selected else odd_primes_upto(args.max_p)
    for p in primes:
        print(audit_prime(p), flush=True)


if __name__ == "__main__":
    main()
