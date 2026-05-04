#!/usr/bin/env python3
"""AlphaTail 短差值尾素对容量证书审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tailpair_resonance_budget_audit import budget_row


def divisors(value: int) -> list[int]:
    """返回正整数 value 的所有正因子。"""
    result = []
    for candidate in range(1, int(value**0.5) + 1):
        if value % candidate == 0:
            result.append(candidate)
            if candidate * candidate != value:
                result.append(value // candidate)
    return sorted(result)


def allowed_gaps(shift: int, point_count: int) -> list[int]:
    """返回等乘数共振允许的正 gap 集。"""
    shift_abs = abs(shift)
    gaps: set[int] = set()
    for point_gap in range(1, point_count):
        base = point_gap * shift_abs
        for divisor in divisors(base):
            gaps.add(base // divisor)
    return sorted(gaps)


def exact_gap_coefficients(shift: int, point_count: int) -> dict[int, int]:
    """返回每个 gap 的精确有向点位系数 C_{g,m}。"""
    coefficients: dict[int, int] = {}
    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            base = -(index_a - index_b) * shift
            if base <= 0:
                continue
            for divisor in divisors(base):
                gap = base // divisor
                coefficients[gap] = coefficients.get(gap, 0) + 1
    return dict(sorted(coefficients.items()))


def shortgap_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回固定窗口的短差值尾素对容量证书。"""
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_set = set(tail_primes)
    coefficients = exact_gap_coefficients(shift, point_count)
    gaps = sorted(coefficients)
    pair_counts = {gap: sum(1 for prime in tail_primes if prime + gap in tail_set) for gap in gaps}
    total_pair_count = sum(pair_counts.values())
    coarse_upper_m2_equal = point_count * point_count * total_pair_count
    exact_upper_m2_equal = sum(coefficients[gap] * pair_counts[gap] for gap in gaps)
    budget = budget_row(prime_bound, block, shift, point_count, alpha, num_primes)
    top_gap_rows = {
        gap: {
            "pairs": pair_counts[gap],
            "coefficient": coefficients[gap],
            "capacity": pair_counts[gap] * coefficients[gap],
        }
        for gap in gaps
    }
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "tail_prime_count": len(tail_primes),
        "gap_count": len(gaps),
        "total_shortgap_pairs": total_pair_count,
        "coarse_upper_m2_equal": coarse_upper_m2_equal,
        "exact_upper_m2_equal": exact_upper_m2_equal,
        "equal_actual": budget["equal_multiplier"],
        "upper_pass": budget["equal_multiplier"] <= exact_upper_m2_equal,
        "compression_factor": coarse_upper_m2_equal / exact_upper_m2_equal if exact_upper_m2_equal else None,
        "actual_over_exact_upper": budget["equal_multiplier"] / exact_upper_m2_equal if exact_upper_m2_equal else None,
        "top_gap_counts": dict(
            sorted(top_gap_rows.items(), key=lambda item: (-item[1]["capacity"], item[0]))[:8]
        ),
    }


def print_table(rows: list[dict]) -> None:
    """输出短差值容量证书表。"""
    print(
        "p block shift m tail_primes gap_count shortgap_pairs exact_upper coarse_upper "
        "equal_actual upper_pass compression actual_over_exact top_gap_counts",
        flush=True,
    )
    for row in rows:
        gaps = ",".join(
            f"{gap}:{data['pairs']}/{data['coefficient']}/{data['capacity']}"
            for gap, data in row["top_gap_counts"].items()
        )
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['tail_prime_count']} "
            f"{row['gap_count']} {row['total_shortgap_pairs']} {row['exact_upper_m2_equal']} "
            f"{row['coarse_upper_m2_equal']} {row['equal_actual']} {row['upper_pass']} "
            f"{row['compression_factor']:.6f} {row['actual_over_exact_upper']:.6f} {gaps}",
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
            rows.append(shortgap_row(prime_bound, block, shift, point_count, args.alpha, args.num_primes))
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
