#!/usr/bin/env python3
"""AlphaTail 二阶尾素对共振预算审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_resonance_budget_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    collect_tail_events,
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import (
    apply_low_sieve,
    domain_bounds,
    local_zero_classes,
)


def second_model_moment(low_count: int, shift: int, point_count: int, tail_primes: list[int]) -> float:
    """计算二阶乘法模型 B2=|L| e2(b_q/q)。"""
    densities = [local_zero_classes(point_count, shift, prime) / prime for prime in tail_primes]
    first_sum = sum(densities)
    square_sum = sum(value * value for value in densities)
    return low_count * (first_sum * first_sum - square_sum) / 2.0


def budget_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单个样本的 M2 共振预算分解。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_size = max(0, domain_stop - domain_start + 1)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    active = apply_low_sieve(domain_start, domain_size, shift, point_count, low_primes)
    low_count = sum(active)
    events = collect_tail_events(domain_start, domain_size, shift, point_count, active, tail_primes)

    total_m2 = 0
    equal_multiplier = 0
    unit_multiplier = 0
    non_equal = 0
    gap_histogram: dict[int, int] = {}
    for offset, point_events in enumerate(events):
        if not active[offset] or len(point_events) < 2:
            continue
        value = domain_start + offset
        for (prime_a, index_a), (prime_b, index_b) in combinations(sorted(point_events), 2):
            if prime_a == prime_b:
                continue
            total_m2 += 1
            left_a = value + index_a * shift
            left_b = value + index_b * shift
            multiplier_a = left_a // prime_a
            multiplier_b = left_b // prime_b
            if multiplier_a == multiplier_b:
                equal_multiplier += 1
                if multiplier_a == 1:
                    unit_multiplier += 1
                gap = abs(prime_b - prime_a)
                gap_histogram[gap] = gap_histogram.get(gap, 0) + 1
            else:
                non_equal += 1
    b2_model = second_model_moment(low_count, shift, point_count, tail_primes)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "low_count": low_count,
        "tail_prime_count": len(tail_primes),
        "m2": total_m2,
        "b2_model": b2_model,
        "d2": total_m2 - b2_model,
        "equal_multiplier": equal_multiplier,
        "unit_multiplier": unit_multiplier,
        "non_equal": non_equal,
        "equal_ratio": equal_multiplier / total_m2 if total_m2 else 0.0,
        "top_equal_gaps": dict(sorted(gap_histogram.items(), key=lambda item: (-item[1], item[0]))[:8]),
    }


def print_table(rows: list[dict]) -> None:
    """输出 M2 共振预算表。"""
    print(
        "p block shift m low_count M2 B2 D2 equal unit non_equal equal_ratio top_equal_gaps",
        flush=True,
    )
    for row in rows:
        gaps = ",".join(f"{gap}:{count}" for gap, count in row["top_equal_gaps"].items())
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['low_count']} "
            f"{row['m2']} {row['b2_model']:.6f} {row['d2']:.6f} "
            f"{row['equal_multiplier']} {row['unit_multiplier']} {row['non_equal']} "
            f"{row['equal_ratio']:.6f} {gaps}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(budget_row(prime_bound, block, shift, point_count, args.alpha, args.num_primes))
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
