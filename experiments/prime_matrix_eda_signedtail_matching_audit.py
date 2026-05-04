#!/usr/bin/env python3
"""EDA SignedTail 奇偶核心双向影子匹配审计。

用法示例：
  python3 experiments/prime_matrix_eda_signedtail_matching_audit.py --selected 101,199,499 --K 5 --D 100
  python3 experiments/prime_matrix_eda_signedtail_matching_audit.py --max-p 200 --K 5 --D 60 --top 5

脚本对每个 n 的奇尾核心与偶尾核心建立相差一个素因子的双向影子图，计算最大匹配缺口。
若奇核心都能匹配到偶核心，则该 n 的 signed tail 非负；未匹配奇核心就是需要继续
用孤立奇核心或影子拥塞解释的真实缺口。
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


def subset_products(factors: list[int], max_omega: int, min_product: int) -> list[tuple[int, int, int]]:
    """枚举尾核心，返回 mask、product、omega。"""
    records: list[tuple[int, int, int]] = []
    count = len(factors)

    def visit(index: int, chosen: int, mask: int, product: int) -> None:
        if chosen > 0 and product > min_product:
            records.append((mask, product, chosen))
        if chosen == max_omega:
            return
        for next_index in range(index, count):
            visit(
                next_index + 1,
                chosen + 1,
                mask | (1 << next_index),
                product * factors[next_index],
            )

    visit(0, 0, 0, 1)
    return records


def maximum_matching(left_edges: list[list[int]], right_count: int) -> int:
    """用 DFS 增广计算小图最大匹配。"""
    match_right = [-1] * right_count

    def augment(left: int, seen: list[bool]) -> bool:
        for right in left_edges[left]:
            if seen[right]:
                continue
            seen[right] = True
            if match_right[right] == -1 or augment(match_right[right], seen):
                match_right[right] = left
                return True
        return False

    matched = 0
    for left in range(len(left_edges)):
        if augment(left, [False] * right_count):
            matched += 1
    return matched


def matching_deficit_for_value(factors: list[int], order: int, min_product: int) -> dict:
    """计算单个 n 的尾核心 signed tail 与匹配缺口。"""
    records = subset_products(factors, order, min_product)
    even_masks = [mask for mask, _product, omega in records if omega % 2 == 0]
    odd_records = [(mask, product, omega) for mask, product, omega in records if omega % 2 == 1]
    even_index = {mask: index for index, mask in enumerate(even_masks)}

    left_edges: list[list[int]] = []
    boundary = 0
    boundary_by_omega: Counter[int] = Counter()
    even_degree: Counter[int] = Counter()
    for mask, _product, _omega in odd_records:
        edges: list[int] = []
        bit = 1
        while bit <= mask:
            if mask & bit:
                submask = mask ^ bit
                if submask in even_index:
                    edges.append(even_index[submask])
            bit <<= 1
        for factor_index in range(len(factors)):
            bit = 1 << factor_index
            if mask & bit:
                continue
            supermask = mask | bit
            if supermask in even_index:
                edges.append(even_index[supermask])
        if not edges:
            boundary += 1
            boundary_by_omega[_omega] += 1
        for right in set(edges):
            even_degree[right] += 1
        left_edges.append(edges)

    matched = maximum_matching(left_edges, len(even_masks)) if even_masks else 0
    odd_count = len(odd_records)
    even_count = len(even_masks)
    deficit = odd_count - matched
    signed_tail = even_count - odd_count
    return {
        "even": even_count,
        "odd": odd_count,
        "signed_tail": signed_tail,
        "matched_odd": matched,
        "matching_deficit": deficit,
        "boundary_odd": boundary,
        "boundary_by_omega": dict(boundary_by_omega),
        "shadow_congestion_deficit": max(0, deficit - boundary),
        "max_even_shadow_degree": max(even_degree.values(), default=0),
    }


def bonferroni_weight(t: int, order: int) -> int:
    """单点奇数阶 Bonferroni 权重。"""
    return sum(((-1) ** j) * comb(t, j) for j in range(0, min(order, t) + 1))


def audit_row(p: int, x: int, order: int, min_product: int, factors_table: list[list[int]]) -> dict:
    """审计单行的匹配缺口。"""
    total = {
        "even": 0,
        "odd": 0,
        "signed_tail": 0,
        "matched_odd": 0,
        "matching_deficit": 0,
        "boundary_odd": 0,
        "shadow_congestion_deficit": 0,
        "max_even_shadow_degree": 0,
    }
    boundary_by_omega: Counter[int] = Counter()
    exact_survivors = 0
    s_order = 0
    max_point_deficit = 0
    max_point_boundary = 0
    max_point_congestion = 0

    for value in range(p * x + 1, p * x + p):
        factors = factors_table[value]
        if not factors:
            exact_survivors += 1
        s_order += bonferroni_weight(len(factors), order)
        point = matching_deficit_for_value(factors, order, min_product)
        for key in total:
            if key == "max_even_shadow_degree":
                total[key] = max(total[key], point[key])
            else:
                total[key] += point[key]
        boundary_by_omega.update(point["boundary_by_omega"])
        max_point_deficit = max(max_point_deficit, point["matching_deficit"])
        max_point_boundary = max(max_point_boundary, point["boundary_odd"])
        max_point_congestion = max(max_point_congestion, point["shadow_congestion_deficit"])

    return {
        "x": x,
        "exact_U": exact_survivors,
        f"S_{order}": s_order,
        **total,
        "boundary_by_omega": dict(sorted(boundary_by_omega.items())),
        "max_point_deficit": max_point_deficit,
        "max_point_boundary": max_point_boundary,
        "max_point_congestion": max_point_congestion,
    }


def audit_prime(p: int, order: int, min_product: int, top: int) -> dict:
    """审计单个 p 的最薄行、最差 signed tail 行和最大缺口行。"""
    factors_table = small_prime_factor_table(p)
    rows = [audit_row(p, x, order, min_product, factors_table) for x in range(1, p + 1)]
    min_exact = min(row["exact_U"] for row in rows)
    min_signed = min(row["signed_tail"] for row in rows)
    max_deficit = max(row["matching_deficit"] for row in rows)
    return {
        "p": p,
        "K": order,
        "D": min_product,
        "min_exact_U": min_exact,
        "min_signed_tail": min_signed,
        "max_matching_deficit": max_deficit,
        "min_exact_rows": [row for row in rows if row["exact_U"] == min_exact][:top],
        "min_signed_rows": [row for row in rows if row["signed_tail"] == min_signed][:top],
        "max_deficit_rows": [row for row in rows if row["matching_deficit"] == max_deficit][:top],
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
    parser.add_argument("--D", type=int, default=100)
    parser.add_argument("--top", type=int, default=3)
    args = parser.parse_args()

    primes = parse_selected(args.selected) if args.selected else odd_primes_upto(args.max_p)
    for p in primes:
        print(audit_prime(p, args.K, args.D, args.top), flush=True)


if __name__ == "__main__":
    main()
