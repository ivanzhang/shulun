#!/usr/bin/env python3
"""EDA-Dual 低阶 Bonferroni 下界审计。

用法示例：
  python3 experiments/prime_matrix_eda_bonferroni_audit.py --max-p 200
  python3 experiments/prime_matrix_eda_bonferroni_audit.py --selected 23,101,199,499

对固定奇素数 p 和早期行 1<=x<=p，令 t(n) 为 n 的 <p 不同素因子个数。
精确幸存数 U_p(x) 为 t(n)=0 的个数。奇数阶 Bonferroni 下界为
  S_K(x)=sum_{n in row} sum_{j=0}^{min(K,t(n))} (-1)^j C(t(n),j)
其中 K 为奇数。若 min_x S_K(x)>0，则该 K 阶证书可证明 EDA(p)。
"""

from __future__ import annotations

import argparse
from math import comb, isqrt, log


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


def audit_prime(p: int, orders: list[int]) -> dict:
    """审计单个 p 的精确余量和 Bonferroni 下界。"""
    omega = omega_small_table(p)
    weights = {
        order: [bonferroni_weight(t, order) for t in range(max(omega) + 1)]
        for order in orders
    }
    min_exact = p
    min_exact_rows: list[int] = []
    min_by_order = {order: 10**18 for order in orders}
    rows_by_order = {order: [] for order in orders}

    for x in range(1, p + 1):
        left = p * x + 1
        right = p * x + p
        exact = 0
        sums = {order: 0 for order in orders}
        for value in range(left, right):
            t = omega[value]
            if t == 0:
                exact += 1
            for order in orders:
                sums[order] += weights[order][t]

        if exact < min_exact:
            min_exact = exact
            min_exact_rows = [x]
        elif exact == min_exact:
            min_exact_rows.append(x)

        for order, total in sums.items():
            if total < min_by_order[order]:
                min_by_order[order] = total
                rows_by_order[order] = [x]
            elif total == min_by_order[order]:
                rows_by_order[order].append(x)

    return {
        "p": p,
        "min_exact": min_exact,
        "min_exact_rows": min_exact_rows[:8],
        "scale_p_over_log_p": p / log(p),
        "min_by_order": min_by_order,
        "rows_by_order": {order: rows[:8] for order, rows in rows_by_order.items()},
        "proved_by_orders": [order for order in orders if min_by_order[order] > 0],
    }


def parse_selected(raw: str) -> list[int]:
    """解析逗号分隔素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--selected", type=str, default="")
    parser.add_argument("--orders", type=str, default="1,3,5,7,9")
    args = parser.parse_args()

    orders = [int(item) for item in args.orders.split(",") if item.strip()]
    primes = parse_selected(args.selected) if args.selected else odd_primes_upto(args.max_p)

    print(f"orders={orders}", flush=True)
    for p in primes:
        record = audit_prime(p, orders)
        print(record, flush=True)


if __name__ == "__main__":
    main()
