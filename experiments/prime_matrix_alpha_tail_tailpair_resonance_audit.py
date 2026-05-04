#!/usr/bin/env python3
"""AlphaTail 尾素对共振剥离审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_resonance_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    audit_row,
    collect_tail_events,
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import apply_low_sieve, domain_bounds


def resonance_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    top: int,
) -> dict:
    """返回最热尾素对的共振剥离统计。"""
    pair_row = audit_row(prime_bound, block, shift, point_count, alpha, num_primes, top)
    if not pair_row["top_pairs"]:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "has_pair": False,
        }
    top_pair = pair_row["top_pairs"][0]
    q1 = top_pair["q1"]
    q2 = top_pair["q2"]
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_size = max(0, domain_stop - domain_start + 1)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    active = apply_low_sieve(domain_start, domain_size, shift, point_count, low_primes)
    events = collect_tail_events(domain_start, domain_size, shift, point_count, active, tail_primes)

    total_pair_points = 0
    unit_resonance = 0
    equal_multiplier = 0
    nonunit_points = 0
    point_patterns: dict[str, int] = {}
    for offset, point_events in enumerate(events):
        if not active[offset]:
            continue
        filtered = [(prime, index) for prime, index in point_events if prime in (q1, q2)]
        if len({prime for prime, _ in filtered}) < 2:
            continue
        value = domain_start + offset
        for (prime_a, index_a), (prime_b, index_b) in combinations(sorted(filtered), 2):
            if (prime_a, prime_b) != (q1, q2):
                continue
            total_pair_points += 1
            left_a = value + index_a * shift
            left_b = value + index_b * shift
            multiplier_a = left_a // q1
            multiplier_b = left_b // q2
            key = f"{index_a},{index_b};{multiplier_a},{multiplier_b}"
            point_patterns[key] = point_patterns.get(key, 0) + 1
            if multiplier_a == 1 and multiplier_b == 1:
                unit_resonance += 1
            elif multiplier_a == multiplier_b:
                equal_multiplier += 1
            else:
                nonunit_points += 1
    gap = q2 - q1
    shift_abs = abs(shift)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "has_pair": True,
        "q1": q1,
        "q2": q2,
        "gap": gap,
        "gap_over_abs_shift": gap / shift_abs if shift_abs else None,
        "actual_pair": top_pair["actual"],
        "deviation": top_pair["deviation"],
        "recount_pair_points": total_pair_points,
        "unit_resonance": unit_resonance,
        "equal_multiplier": equal_multiplier,
        "nonunit_points": nonunit_points,
        "point_patterns": dict(sorted(point_patterns.items(), key=lambda item: (-item[1], item[0]))),
    }


def print_table(rows: list[dict]) -> None:
    """输出共振剥离表。"""
    print(
        "p block shift m q1 q2 gap gap_over_abs_shift actual dev recount "
        "unit equal_multiplier nonunit top_patterns",
        flush=True,
    )
    for row in rows:
        if not row["has_pair"]:
            print(
                f"{row['p']} {row['block']} {row['shift']} {row['m']} "
                "NA NA NA NA 0 0.000000 0 0 0 0 NA",
                flush=True,
            )
            continue
        patterns = ",".join(f"{key}:{value}" for key, value in list(row["point_patterns"].items())[:4])
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['q1']} {row['q2']} {row['gap']} {row['gap_over_abs_shift']:.6f} "
            f"{row['actual_pair']} {row['deviation']:.6f} {row['recount_pair_points']} "
            f"{row['unit_resonance']} {row['equal_multiplier']} {row['nonunit_points']} {patterns}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(resonance_row(prime_bound, block, shift, point_count, args.alpha, args.num_primes, args.top))
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
