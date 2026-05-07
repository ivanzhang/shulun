#!/usr/bin/env python3
"""底部缺口对容量的分段审计。

用法示例：
  python3 experiments/prime_matrix_bottom_deficit_pair_bound_segmented_audit.py --p-list 997,5003
  python3 experiments/prime_matrix_bottom_deficit_pair_bound_segmented_audit.py --p-list 10007,20011 --format table

在 h=P-x<sqrt(P) 的底部带中，若低骨架残洞是合数，则必为
(P-a)(P-b)，且 a+b=h、c=ab。本脚本只在底部近平方带做分段素数筛，
再把高素对补洞和真实素数洞合并成 R_{P-h} 的精确计数。
"""

from __future__ import annotations

import argparse
import json
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数列表。"""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for value in range(2, isqrt(limit) + 1):
        if sieve[value]:
            start = value * value
            sieve[start : limit + 1 : value] = b"\x00" * (
                ((limit - start) // value) + 1
            )
    return [idx for idx, flag in enumerate(sieve) if flag]


def prime_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x00") * (limit + 1)
    for prime in primes_upto(limit):
        flags[prime] = 1
    return flags


def segmented_prime_flags(lo: int, hi: int, base_primes: list[int]) -> bytearray:
    """对闭区间 [lo, hi] 做分段素数筛。"""
    length = hi - lo + 1
    flags = bytearray(b"\x01") * length
    for prime in base_primes:
        start = max(prime * prime, ((lo + prime - 1) // prime) * prime)
        if start > hi:
            continue
        flags[start - lo : length : prime] = b"\x00" * (((hi - start) // prime) + 1)
    for value in range(lo, min(hi, 1) + 1):
        flags[value - lo] = 0
    return flags


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def audit_p(p: int, sample_limit: int) -> dict:
    """审计单个 P 的 h<sqrt(P) 底部带。"""
    sqrt_p = isqrt(p)
    max_h = sqrt_p - 1
    if max_h < 1:
        return {
            "p": p,
            "sqrt_p": sqrt_p,
            "h_range": [None, None],
            "row_count": 0,
            "rows": [],
        }

    lo = p * (p - max_h) + 1
    hi = p * p - 1
    base_primes = primes_upto(p)
    small_prime = prime_bool(p)
    segment = segmented_prime_flags(lo, hi, base_primes)

    prime_counts = [0] * (max_h + 1)
    prime_samples: list[list[int]] = [[] for _ in range(max_h + 1)]
    for offset, is_prime in enumerate(segment):
        if not is_prime:
            continue
        value = lo + offset
        column = value % p
        if column == 0:
            continue
        x = value // p
        h = p - x
        if 1 <= h <= max_h:
            prime_counts[h] += 1
            if len(prime_samples[h]) < sample_limit:
                prime_samples[h].append(value)

    rows = []
    square_pair_rows = []
    for h in range(1, max_h + 1):
        pair_samples = []
        pair_count = 0
        square_pair = None
        for a in range(1, h // 2 + 1):
            b = h - a
            if not (small_prime[p - a] and small_prime[p - b]):
                continue
            column = a * b
            pair_count += 1
            sample = {
                "a": a,
                "b": b,
                "column": column,
                "factors": [p - a, p - b],
            }
            if a == b:
                square_pair = sample
            if len(pair_samples) < sample_limit:
                pair_samples.append(sample)
        capacity = h // 2
        rough_count = prime_counts[h] + pair_count
        margin = rough_count - capacity
        row = {
            "h": h,
            "x": p - h,
            "prime_holes": prime_counts[h],
            "pair_holes": pair_count,
            "pair_capacity": capacity,
            "rough_holes": rough_count,
            "bottom_pair_margin": margin,
            "row_prime_positive": prime_counts[h] > 0,
            "sample_primes": prime_samples[h],
            "sample_pairs": pair_samples,
        }
        if square_pair is not None:
            row["square_pair"] = square_pair
            square_pair_rows.append(h)
        rows.append(row)

    min_prime = min(row["prime_holes"] for row in rows)
    min_margin = min(row["bottom_pair_margin"] for row in rows)
    weakest_prime_rows = [
        row for row in rows if row["prime_holes"] == min_prime
    ][:sample_limit]
    weakest_margin_rows = [
        row for row in rows if row["bottom_pair_margin"] == min_margin
    ][:sample_limit]
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "h_range": [1, max_h],
        "row_count": len(rows),
        "all_rows_have_prime": all(row["row_prime_positive"] for row in rows),
        "min_prime_holes": min_prime,
        "min_bottom_pair_margin": min_margin,
        "max_pair_holes": max(row["pair_holes"] for row in rows),
        "square_pair_row_count": len(square_pair_rows),
        "square_pair_rows": square_pair_rows[:sample_limit],
        "weakest_prime_rows": weakest_prime_rows,
        "weakest_margin_rows": weakest_margin_rows,
        "rows": rows,
    }


def audit(p_values: list[int], sample_limit: int) -> dict:
    """审计多个 P。"""
    max_p = max(p_values) if p_values else 2
    prime_set = set(primes_upto(max_p))
    rows = []
    skipped = []
    for p in p_values:
        if p < 3 or p not in prime_set:
            skipped.append(p)
            continue
        rows.append(audit_p(p, sample_limit))
    return {
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "status": "bottom_deficit_pair_bound_segmented_sample_not_a_proof",
        "all_rows_have_prime": all(row["all_rows_have_prime"] for row in rows),
        "all_bottom_pair_margins_positive": all(
            row["min_bottom_pair_margin"] > 0 for row in rows
        ),
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "p sqrt_p h_range rows all_prime min_prime min_margin max_pair "
        "square_pair_rows weakest_prime weakest_margin",
        flush=True,
    )
    for row in package["rows"]:
        weakest_prime = ";".join(
            f"h={item['h']}:prime={item['prime_holes']}:sample={item['sample_primes']}"
            for item in row["weakest_prime_rows"]
        )
        weakest_margin = ";".join(
            f"h={item['h']}:R={item['rough_holes']}:cap={item['pair_capacity']}:"
            f"margin={item['bottom_pair_margin']}:pairs={item['pair_holes']}"
            for item in row["weakest_margin_rows"]
        )
        print(
            f"{row['p']} {row['sqrt_p']} {row['h_range']} {row['row_count']} "
            f"{row['all_rows_have_prime']} {row['min_prime_holes']} "
            f"{row['min_bottom_pair_margin']} {row['max_pair_holes']} "
            f"{row['square_pair_rows']} {weakest_prime} {weakest_margin}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="997,1999,5003")
    parser.add_argument("--sample-limit", type=int, default=5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()
    package = audit(parse_p_list(args.p_list), args.sample_limit)
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
