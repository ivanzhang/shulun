#!/usr/bin/env python3
"""AlphaTail 尾素对共振几何截断证书审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_geometric_certificate_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import apply_low_sieve, domain_bounds
from prime_matrix_alpha_tail_tailpair_resonance_budget_audit import budget_row
from prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit import exact_gap_coefficients


def geometric_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单个样本的几何截断容量。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_size = max(0, domain_stop - domain_start + 1)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_set = set(tail_primes)
    active = apply_low_sieve(domain_start, domain_size, shift, point_count, low_primes)
    coefficients = exact_gap_coefficients(shift, point_count)

    geometric_upper = 0
    low_survivor_exact = 0
    top_gap_rows: dict[int, dict[str, int]] = {}
    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            base = -(index_a - index_b) * shift
            if base <= 0:
                continue
            for gap in coefficients:
                if base % gap != 0:
                    continue
                multiplier = base // gap
                gap_geo = 0
                gap_low = 0
                for prime in tail_primes:
                    if prime + gap not in tail_set:
                        continue
                    candidate = prime * multiplier - index_a * shift
                    if candidate < domain_start or candidate > domain_stop:
                        continue
                    gap_geo += 1
                    if active[candidate - domain_start]:
                        gap_low += 1
                geometric_upper += gap_geo
                low_survivor_exact += gap_low
                if gap_geo or gap_low:
                    entry = top_gap_rows.setdefault(gap, {"geometric": 0, "low": 0})
                    entry["geometric"] += gap_geo
                    entry["low"] += gap_low
    budget = budget_row(prime_bound, block, shift, point_count, alpha, num_primes)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "tail_prime_count": len(tail_primes),
        "coefficient_gap_count": len(coefficients),
        "geometric_upper": geometric_upper,
        "low_survivor_exact": low_survivor_exact,
        "equal_actual": budget["equal_multiplier"],
        "exact_matches_actual": low_survivor_exact == budget["equal_multiplier"],
        "geom_over_actual": geometric_upper / budget["equal_multiplier"] if budget["equal_multiplier"] else None,
        "top_gap_rows": dict(sorted(top_gap_rows.items(), key=lambda item: (-item[1]["geometric"], item[0]))[:8]),
    }


def print_table(rows: list[dict]) -> None:
    """输出几何截断表。"""
    print(
        "p block shift m tail_primes gap_count geometric_upper low_survivor_exact "
        "equal_actual match geom_over_actual top_gap_rows",
        flush=True,
    )
    for row in rows:
        gaps = ",".join(
            f"{gap}:{data['geometric']}/{data['low']}" for gap, data in row["top_gap_rows"].items()
        )
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['tail_prime_count']} "
            f"{row['coefficient_gap_count']} {row['geometric_upper']} {row['low_survivor_exact']} "
            f"{row['equal_actual']} {row['exact_matches_actual']} {row['geom_over_actual']:.6f} {gaps}",
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
            rows.append(geometric_row(prime_bound, block, shift, point_count, args.alpha, args.num_primes))
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
