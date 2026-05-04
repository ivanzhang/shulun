#!/usr/bin/env python3
"""EDA-BK 端点缺陷桥接审计。

用法示例：
  python3 experiments/prime_matrix_eda_endpoint_defect_audit.py --selected 23,101,499
  python3 experiments/prime_matrix_eda_endpoint_defect_audit.py --max-p 200 --orders 3,5,7

脚本计算奇数阶 Bonferroni 下界 S_K，并把它分解为
  S_K = (p-1) G_K + E_K
其中 G_K 是截断 Euler 主项，E_K 是端点锯齿缺陷项。该脚本用于审计
“若 S_K 失败，则必须出现多强的负端点缺陷”。
"""

from __future__ import annotations

import argparse
from math import comb, isqrt


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


def omega_small_table(p: int) -> bytearray:
    """计算 n<=p^2+p 的 <p 不同素因子个数。"""
    limit = p * p + p
    omega = bytearray(limit + 1)
    for prime in primes_upto(p - 1):
        for multiple in range(prime, limit + 1, prime):
            omega[multiple] += 1
    return omega


def bonferroni_weight(t: int, order: int) -> int:
    """单点奇数阶 Bonferroni 权重。"""
    return sum(((-1) ** j) * comb(t, j) for j in range(0, min(order, t) + 1))


def truncated_euler_main(p: int, order: int) -> float:
    """计算 G_K=sum_{omega(d)<=K} (-1)^omega(d)/d。"""
    elementary = [0.0 for _ in range(order + 1)]
    elementary[0] = 1.0
    for prime in primes_upto(p - 1):
        reciprocal = 1.0 / prime
        for level in range(order, 0, -1):
            elementary[level] += elementary[level - 1] * reciprocal
    return sum(((-1) ** level) * elementary[level] for level in range(order + 1))


def audit_prime(p: int, orders: list[int]) -> list[dict]:
    """审计单个 p 在各阶 K 下的最薄行端点缺陷。"""
    omega = omega_small_table(p)
    max_omega = max(omega)
    weights = {
        order: [bonferroni_weight(t, order) for t in range(max_omega + 1)]
        for order in orders
    }
    records: list[dict] = []

    for order in orders:
        min_s = 10**18
        min_rows: list[int] = []
        for x in range(1, p + 1):
            left = p * x + 1
            right = p * x + p
            total = sum(weights[order][omega[value]] for value in range(left, right))
            if total < min_s:
                min_s = total
                min_rows = [x]
            elif total == min_s:
                min_rows.append(x)

        h = p - 1
        main_density = truncated_euler_main(p, order)
        main = h * main_density
        endpoint_defect = min_s - main
        bridge_applicable = main_density > 0
        records.append(
            {
                "p": p,
                "order": order,
                "max_omega_seen": max_omega,
                "main_density_GK": main_density,
                "main_term": main,
                "min_S_K": min_s,
                "min_rows": min_rows[:8],
                "endpoint_defect_at_min": endpoint_defect,
                "defect_per_H": endpoint_defect / h,
                "bridge_applicable": bridge_applicable,
                "required_negative_defect_if_failure": -main if bridge_applicable else None,
            }
        )
    return records


def parse_selected(raw: str) -> list[int]:
    """解析逗号分隔素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--selected", type=str, default="")
    parser.add_argument("--orders", type=str, default="3,5,7")
    args = parser.parse_args()

    orders = [int(item) for item in args.orders.split(",") if item.strip()]
    primes = parse_selected(args.selected) if args.selected else odd_primes_upto(args.max_p)

    print(f"orders={orders}", flush=True)
    for p in primes:
        for record in audit_prime(p, orders):
            print(record, flush=True)


if __name__ == "__main__":
    main()
