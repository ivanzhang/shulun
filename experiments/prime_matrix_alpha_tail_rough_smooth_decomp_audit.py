#!/usr/bin/env python3
"""AlphaTail 多点 C=1 缺陷的粗筛/平方自由分解审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_rough_smooth_decomp_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
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


def squarefree_support(value: int, small_primes: list[int]) -> set[int] | None:
    """返回 y-smooth squarefree 数的素因子支撑；否则返回 None。"""
    remaining = value
    support: set[int] = set()
    for prime in small_primes:
        if prime > remaining:
            break
        if remaining % prime != 0:
            continue
        remaining //= prime
        support.add(prime)
        if remaining % prime == 0:
            return None
    if remaining != 1:
        return None
    return support


def has_large_prime_factor(value: int, cutoff: int, primes: list[int]) -> bool:
    """判断 value 是否含有大于 cutoff 的素因子。"""
    for prime in primes:
        if prime <= cutoff:
            continue
        if value % prime == 0:
            return True
    return False


def local_zero_classes(point_count: int, shift: int, prime: int) -> int:
    """返回 m 点链在 prime 下的 distinct 禁零类数。"""
    return len({(-index * shift) % prime for index in range(point_count)})


def domain_bounds(block: int, shift: int, point_count: int) -> tuple[int, int]:
    """返回 m 点都落在 block 内的起点区间。"""
    starts = [block + 1 - index * shift for index in range(point_count)]
    stops = [2 * block - index * shift for index in range(point_count)]
    return max(starts), min(stops)


def main_factor(cutoff: int, z_value: int, shift: int, point_count: int) -> float:
    """计算大素删除主因子 V_m。"""
    factor = 1.0
    for prime in primes_upto(z_value):
        if prime <= cutoff:
            continue
        forbidden = local_zero_classes(point_count, shift, prime)
        factor *= 1.0 - forbidden / prime
    return factor


def audit_item(prime_bound: int, block: int, shift: int, alpha: float) -> dict:
    """审计单个 p:B:r 的粗筛/平方自由分解。"""
    cutoff = int(alpha * prime_bound)
    rows = []
    for point_count in (4, 5):
        domain_start, domain_stop = domain_bounds(block, shift, point_count)
        domain_size = max(0, domain_stop - domain_start + 1)
        z_value = max(domain_stop + index * shift for index in range(point_count))
        all_primes = primes_upto(z_value)
        small_primes = [prime for prime in all_primes if prime <= cutoff]
        rough_count = 0
        smooth_squarefree_count = 0
        for value in range(domain_start, domain_stop + 1):
            point_values = [value + index * shift for index in range(point_count)]
            if any(has_large_prime_factor(point_value, cutoff, all_primes) for point_value in point_values):
                continue
            rough_count += 1
            if all(squarefree_support(point_value, small_primes) is not None for point_value in point_values):
                smooth_squarefree_count += 1
        factor = main_factor(cutoff, z_value, shift, point_count)
        main_budget = domain_size * factor
        rough_surplus = rough_count - main_budget
        square_deletion = rough_count - smooth_squarefree_count
        defect = smooth_squarefree_count - main_budget
        rows.append(
            {
                "m": point_count,
                "domain_size": domain_size,
                "rough_count": rough_count,
                "smooth_squarefree_count": smooth_squarefree_count,
                "main_budget": main_budget,
                "rough_surplus": rough_surplus,
                "square_deletion": square_deletion,
                "defect": defect,
                "identity_ok": abs(defect - (rough_surplus - square_deletion)) < 1e-9,
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
        print("p block shift m rough sqfree HV rough_surplus sq_deletion E identity", flush=True)
        for audit in audits:
            for row in audit["rows"]:
                print(
                    f"{audit['p']} {audit['block']} {audit['shift']} "
                    f"{row['m']} {row['rough_count']} {row['smooth_squarefree_count']} "
                    f"{row['main_budget']:.6f} {row['rough_surplus']:.6f} "
                    f"{row['square_deletion']} {row['defect']:.6f} {row['identity_ok']}",
                    flush=True,
                )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
