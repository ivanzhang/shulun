#!/usr/bin/env python3
"""AlphaTail 平方一阶质量与粗筛盈余桥审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_square_mass_bridge_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
"""

from __future__ import annotations

import argparse
import json
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def square_hit_capacity(z_value: int) -> int:
    """返回 L2(z)：前 L 个素数平方乘积不超过 z 的最大 L。"""
    product = 1
    capacity = 0
    for prime in primes_upto(z_value):
        next_product = product * prime * prime
        if next_product > z_value:
            break
        product = next_product
        capacity += 1
    return capacity


def has_large_prime_factor(value: int, cutoff: int, primes: list[int]) -> bool:
    """判断 value 是否含有大于 cutoff 的素因子。"""
    for prime in primes:
        if prime <= cutoff:
            continue
        if value % prime == 0:
            return True
    return False


def domain_bounds(block: int, shift: int, point_count: int) -> tuple[int, int]:
    """返回 m 点都落在 block 内的起点区间。"""
    starts = [block + 1 - index * shift for index in range(point_count)]
    stops = [2 * block - index * shift for index in range(point_count)]
    return max(starts), min(stops)


def local_zero_classes(point_count: int, shift: int, prime: int) -> int:
    """返回 m 点链在 prime 下的 distinct 禁零类数。"""
    return len({(-index * shift) % prime for index in range(point_count)})


def main_factor(cutoff: int, z_value: int, shift: int, point_count: int) -> float:
    """计算大素删除主因子 V_m。"""
    factor = 1.0
    for prime in primes_upto(z_value):
        if prime <= cutoff:
            continue
        factor *= 1.0 - local_zero_classes(point_count, shift, prime) / prime
    return factor


def square_hit_count(value: int, shift: int, point_count: int, small_primes: list[int]) -> int:
    """统计一个起点命中的小素平方事件数。"""
    hits = 0
    for prime in small_primes:
        square = prime * prime
        for index in range(point_count):
            if (value + index * shift) % square == 0:
                hits += 1
    return hits


def audit_item(prime_bound: int, block: int, shift: int, alpha: float) -> dict:
    """审计单个 p:B:r 的平方质量桥。"""
    cutoff = int(alpha * prime_bound)
    rows = []
    for point_count in (4, 5):
        domain_start, domain_stop = domain_bounds(block, shift, point_count)
        domain_size = max(0, domain_stop - domain_start + 1)
        z_value = max(domain_stop + index * shift for index in range(point_count))
        all_primes = primes_upto(z_value)
        small_primes = [prime for prime in all_primes if prime <= cutoff]
        rough_count = 0
        first_moment = 0
        for value in range(domain_start, domain_stop + 1):
            point_values = [value + index * shift for index in range(point_count)]
            if any(has_large_prime_factor(point_value, cutoff, all_primes) for point_value in point_values):
                continue
            rough_count += 1
            first_moment += square_hit_count(value, shift, point_count, small_primes)
        factor = main_factor(cutoff, z_value, shift, point_count)
        rough_surplus = rough_count - domain_size * factor
        square_density = point_count * sum(1.0 / (prime * prime) for prime in small_primes)
        model = rough_count * square_density
        square_defect = first_moment - model
        h_bound = point_count * square_hit_capacity(z_value)
        model_margin = model / h_bound - rough_surplus if h_bound else -rough_surplus
        actual_margin = first_moment / h_bound - rough_surplus if h_bound else -rough_surplus
        rows.append(
            {
                "m": point_count,
                "rough_count": rough_count,
                "S1": first_moment,
                "model": model,
                "square_defect": square_defect,
                "Hbound": h_bound,
                "rough_surplus": rough_surplus,
                "model_margin": model_margin,
                "actual_margin": actual_margin,
                "closes": actual_margin >= 0,
            }
        )
    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "shift": shift,
        "rows": rows,
    }


def parse_selected(raw: str) -> list[tuple[int, int, int]]:
    """解析 p:B:r 逗号列表。"""
    items: list[tuple[int, int, int]] = []
    for part in raw.split(","):
        if not part.strip():
            continue
        prime_raw, block_raw, shift_raw = part.split(":", 2)
        items.append((int(prime_raw), int(block_raw), int(shift_raw)))
    return items


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block shift m rough S1 model sq_defect Hbound rough_surplus model_margin actual_margin closes", flush=True)
        for audit in audits:
            for row in audit["rows"]:
                print(
                    f"{audit['p']} {audit['block']} {audit['shift']} "
                    f"{row['m']} {row['rough_count']} {row['S1']} "
                    f"{row['model']:.6f} {row['square_defect']:.6f} {row['Hbound']} "
                    f"{row['rough_surplus']:.6f} {row['model_margin']:.6f} "
                    f"{row['actual_margin']:.6f} {row['closes']}",
                    flush=True,
                )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
