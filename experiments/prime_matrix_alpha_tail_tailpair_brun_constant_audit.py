#!/usr/bin/env python3
"""AlphaTail 尾素对 Brun/Selberg 常数包审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_brun_constant_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from math import gcd, log

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_geometric_certificate_audit import geometric_row
from prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit import exact_gap_coefficients


def prime_divisors(value: int) -> list[int]:
    """返回 value 的不同素因子。"""
    remaining = abs(value)
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append(remaining)
    return factors


def singular_factor(gap: int) -> float:
    """返回固定差值局部因子，偶性常数吸收到总常数中。"""
    factor = 1.0
    for prime in prime_divisors(gap):
        if prime > 2:
            factor *= (prime - 1.0) / (prime - 2.0)
    return factor


def ceil_div(numerator: int, denominator: int) -> int:
    """整数上取整。"""
    return -((-numerator) // denominator)


def interval_for_pattern(
    domain_start: int,
    domain_stop: int,
    shift: int,
    index_a: int,
    index_b: int,
    gap: int,
) -> tuple[int, int] | None:
    """返回固定 gap 与点位对对应的 q 区间。"""
    base = -(index_a - index_b) * shift
    if base <= 0 or base % gap != 0:
        return None
    multiplier = base // gap
    lower = ceil_div(domain_start + index_a * shift, multiplier)
    upper = (domain_stop + index_a * shift) // multiplier
    if lower > upper:
        return None
    return lower, upper


def count_prime_pairs_in_interval(tail_set: set[int], lower: int, upper: int, gap: int) -> int:
    """精确计数 q,q+gap 均为尾素且 q 落入区间。"""
    return sum(1 for prime in tail_set if lower <= prime <= upper and prime + gap in tail_set)


def brun_scale_for_interval(lower: int, upper: int, gap: int) -> float:
    """返回 S_g |J|/log^2(J_-) 量级。"""
    length = max(0, upper - lower + 1)
    if length == 0:
        return 0.0
    log_base = log(max(3, lower))
    return singular_factor(gap) * length / (log_base * log_base)


def brun_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单个样本的 Brun/Selberg 常数需求。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_set = set(tail_primes)
    coefficients = exact_gap_coefficients(shift, point_count)
    geom = geometric_row(prime_bound, block, shift, point_count, alpha, num_primes)

    total_actual = 0
    total_scale = 0.0
    local_rows = []
    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            for gap in coefficients:
                interval = interval_for_pattern(domain_start, domain_stop, shift, index_a, index_b, gap)
                if interval is None:
                    continue
                lower, upper = interval
                actual = count_prime_pairs_in_interval(tail_set, lower, upper, gap)
                scale = brun_scale_for_interval(lower, upper, gap)
                total_actual += actual
                total_scale += scale
                if actual:
                    local_rows.append(
                        {
                            "gap": gap,
                            "j1": index_a,
                            "j2": index_b,
                            "lower": lower,
                            "upper": upper,
                            "length": upper - lower + 1,
                            "actual": actual,
                            "scale": scale,
                            "required_c": actual / scale if scale else None,
                            "singular": singular_factor(gap),
                        }
                    )
    local_rows.sort(key=lambda item: (-(item["required_c"] or 0), -item["actual"], item["gap"]))
    max_local_required = local_rows[0]["required_c"] if local_rows else 0.0
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "tail_prime_count": len(tail_primes),
        "geom_count": geom["geometric_upper"],
        "actual_from_intervals": total_actual,
        "intervals_match_geom": total_actual == geom["geometric_upper"],
        "bs_scale": total_scale,
        "required_c_bs": total_actual / total_scale if total_scale else None,
        "max_local_required_c": max_local_required,
        "positive_interval_count": len(local_rows),
        "top_requirements": local_rows[:8],
    }


def print_table(rows: list[dict]) -> None:
    """输出常数需求表。"""
    print(
        "p block shift m tail_primes geom_count interval_count match bs_scale "
        "required_C_BS max_local_C positive_intervals top_requirements",
        flush=True,
    )
    for row in rows:
        top = ",".join(
            f"g{item['gap']}:{item['actual']}/{item['scale']:.3f}/{item['required_c']:.3f}"
            for item in row["top_requirements"][:5]
        )
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['tail_prime_count']} "
            f"{row['geom_count']} {row['actual_from_intervals']} {row['intervals_match_geom']} "
            f"{row['bs_scale']:.6f} {row['required_c_bs']:.6f} "
            f"{row['max_local_required_c']:.6f} {row['positive_interval_count']} {top}",
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
            rows.append(brun_row(prime_bound, block, shift, point_count, args.alpha, args.num_primes))
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
