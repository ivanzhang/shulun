#!/usr/bin/env python3
"""EDA Tail/Core 尾项审计。

用法示例：
  python3 experiments/prime_matrix_eda_tailcore_audit.py --selected 23,101,199 --K 5 --D 60
  python3 experiments/prime_matrix_eda_tailcore_audit.py --max-p 200 --K 5 --D 100 --top 8

脚本枚举早期行 I_{p,x} 中的尾核心关联：
  (n,d): n in I_{p,x}, d|n, d|M_<p, omega(d)<=K, d>D
并输出尾关联质量、最强尾桶和尾锚集中度。它用于定位 Tail/Core 分支的真实压力来源。
"""

from __future__ import annotations

import argparse
from collections import Counter
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


def small_prime_factor_table(p: int) -> list[list[int]]:
    """为 n<=p^2+p 生成 <p 的不同素因子列表。"""
    limit = p * p + p
    factors: list[list[int]] = [[] for _ in range(limit + 1)]
    for prime in primes_upto(p - 1):
        for multiple in range(prime, limit + 1, prime):
            factors[multiple].append(prime)
    return factors


def tail_products(factors: list[int], max_omega: int, min_product: int) -> list[tuple[int, int]]:
    """枚举由 factors 组成、阶数<=max_omega 且乘积>min_product 的 squarefree d。"""
    products: list[tuple[int, int]] = []

    def visit(index: int, chosen: int, product: int) -> None:
        if chosen > 0 and product > min_product:
            products.append((product, chosen))
        if chosen == max_omega:
            return
        for next_index in range(index, len(factors)):
            visit(next_index + 1, chosen + 1, product * factors[next_index])

    visit(0, 0, 1)
    return products


def bonferroni_weight(t: int, order: int) -> int:
    """单点奇数阶 Bonferroni 权重。"""
    return sum(((-1) ** j) * comb(t, j) for j in range(0, min(order, t) + 1))


def dyadic_floor(value: int) -> int:
    """返回 value 所在二进制 dyadic 桶的左端。"""
    if value <= 0:
        return 0
    return 1 << (value.bit_length() - 1)


def audit_row(
    p: int,
    x: int,
    order: int,
    min_product: int,
    factors_table: list[list[int]],
    top: int,
) -> dict:
    """审计单个早期行的尾关联结构。"""
    left = p * x + 1
    right = p * x + p
    exact_survivors = 0
    s_order = 0
    signed_tail = 0
    tail_mass = 0
    even_tail_mass = 0
    odd_tail_mass = 0
    max_point_tail = 0
    max_point_omega = 0
    bucket_counter: Counter[tuple[int, int, int]] = Counter()
    even_bucket_counter: Counter[tuple[int, int, int]] = Counter()
    odd_bucket_counter: Counter[tuple[int, int, int]] = Counter()
    anchor_counter: Counter[int] = Counter()

    for value in range(left, right):
        factors = factors_table[value]
        omega = len(factors)
        max_point_omega = max(max_point_omega, omega)
        if omega == 0:
            exact_survivors += 1
        s_order += bonferroni_weight(omega, order)

        products = tail_products(factors, order, min_product)
        if products:
            max_point_tail = max(max_point_tail, len(products))
        for product, product_omega in products:
            cofactor = value // product
            tail_mass += 1
            if product_omega % 2:
                signed_tail -= 1
                odd_tail_mass += 1
            else:
                signed_tail += 1
                even_tail_mass += 1
            bucket = (product_omega, dyadic_floor(product), dyadic_floor(cofactor))
            bucket_counter[bucket] += 1
            if product_omega % 2:
                odd_bucket_counter[bucket] += 1
            else:
                even_bucket_counter[bucket] += 1
            anchor_counter[cofactor] += 1

    top_buckets = [
        {"omega": key[0], "d_dyadic": key[1], "a_dyadic": key[2], "count": count}
        for key, count in bucket_counter.most_common(top)
    ]
    top_anchors = [
        {"anchor": anchor, "count": count}
        for anchor, count in anchor_counter.most_common(top)
    ]
    top_odd_buckets = [
        {"omega": key[0], "d_dyadic": key[1], "a_dyadic": key[2], "count": count}
        for key, count in odd_bucket_counter.most_common(top)
    ]
    top_even_buckets = [
        {"omega": key[0], "d_dyadic": key[1], "a_dyadic": key[2], "count": count}
        for key, count in even_bucket_counter.most_common(top)
    ]

    return {
        "x": x,
        "exact_U": exact_survivors,
        f"S_{order}": s_order,
        "tail_mass": tail_mass,
        "even_tail_mass": even_tail_mass,
        "odd_tail_mass": odd_tail_mass,
        "signed_tail": signed_tail,
        "max_point_tail": max_point_tail,
        "max_point_omega": max_point_omega,
        "top_buckets": top_buckets,
        "top_negative_odd_buckets": top_odd_buckets,
        "top_positive_even_buckets": top_even_buckets,
        "top_anchors": top_anchors,
    }


def audit_prime(p: int, order: int, min_product: int, top: int) -> dict:
    """审计单个 p 的最薄行和尾压力最大行。"""
    factors_table = small_prime_factor_table(p)
    rows = [
        audit_row(p, x, order, min_product, factors_table, top)
        for x in range(1, p + 1)
    ]
    min_exact = min(row["exact_U"] for row in rows)
    min_s = min(row[f"S_{order}"] for row in rows)
    max_tail = max(row["tail_mass"] for row in rows)
    min_exact_rows = [row for row in rows if row["exact_U"] == min_exact][:top]
    max_tail_rows = [row for row in rows if row["tail_mass"] == max_tail][:top]
    min_s_rows = [row for row in rows if row[f"S_{order}"] == min_s][:top]
    return {
        "p": p,
        "K": order,
        "D": min_product,
        "min_exact_U": min_exact,
        f"min_S_{order}": min_s,
        "max_tail_mass": max_tail,
        "min_exact_rows": min_exact_rows,
        "min_S_rows": min_s_rows,
        "max_tail_rows": max_tail_rows,
    }


def parse_selected(raw: str) -> list[int]:
    """解析逗号分隔素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--selected", type=str, default="")
    parser.add_argument("--K", type=int, default=5)
    parser.add_argument("--D", type=int, default=60)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()

    primes = parse_selected(args.selected) if args.selected else odd_primes_upto(args.max_p)
    for p in primes:
        print(audit_prime(p, args.K, args.D, args.top), flush=True)


if __name__ == "__main__":
    main()
