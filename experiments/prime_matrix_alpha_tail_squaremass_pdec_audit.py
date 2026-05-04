#!/usr/bin/env python3
"""AlphaTail SquareMass-PDEC 低平方模审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_squaremass_pdec_audit.py --selected '997:4096:-36,5003:8192:-36' --A 31 --format table
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


def square_hit_count(value: int, shift: int, point_count: int, primes: list[int]) -> int:
    """统计一个起点命中的指定素数平方事件数。"""
    hits = 0
    for prime in primes:
        square = prime * prime
        for index in range(point_count):
            if (value + index * shift) % square == 0:
                hits += 1
    return hits


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, square_cutoff: int) -> dict:
    """审计单个 p:B:r 的低平方质量。"""
    cutoff = int(alpha * prime_bound)
    low_square_primes = primes_upto(square_cutoff)
    rows = []
    for point_count in (4, 5):
        domain_start, domain_stop = domain_bounds(block, shift, point_count)
        z_value = max(domain_stop + index * shift for index in range(point_count))
        all_primes = primes_upto(z_value)
        small_primes = [prime for prime in all_primes if prime <= cutoff]
        high_square_primes = [prime for prime in small_primes if prime > square_cutoff]
        rough_count = 0
        low_sum = 0
        high_sum = 0
        for value in range(domain_start, domain_stop + 1):
            point_values = [value + index * shift for index in range(point_count)]
            if any(has_large_prime_factor(point_value, cutoff, all_primes) for point_value in point_values):
                continue
            rough_count += 1
            low_sum += square_hit_count(value, shift, point_count, low_square_primes)
            high_sum += square_hit_count(value, shift, point_count, high_square_primes)
        low_model = rough_count * point_count * sum(1.0 / (prime * prime) for prime in low_square_primes)
        high_model = rough_count * point_count * sum(1.0 / (prime * prime) for prime in high_square_primes)
        rows.append(
            {
                "m": point_count,
                "A": square_cutoff,
                "rough_count": rough_count,
                "low_sum": low_sum,
                "low_model": low_model,
                "low_centered": low_sum - low_model,
                "high_sum": high_sum,
                "high_model": high_model,
                "high_centered": high_sum - high_model,
                "total_defect": (low_sum + high_sum) - (low_model + high_model),
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
    parser.add_argument("--A", type=int, default=31)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha, args.A)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block shift m A rough low_sum low_model centered high_centered total_defect", flush=True)
        for audit in audits:
            for row in audit["rows"]:
                print(
                    f"{audit['p']} {audit['block']} {audit['shift']} "
                    f"{row['m']} {row['A']} {row['rough_count']} "
                    f"{row['low_sum']} {row['low_model']:.6f} {row['low_centered']:.6f} "
                    f"{row['high_centered']:.6f} {row['total_defect']:.6f}",
                    flush=True,
                )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
