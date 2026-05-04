#!/usr/bin/env python3
"""AlphaTail 固定 gap 目标区间尺度下界审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_target_interval_scale_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import (
    brun_row,
    brun_scale_for_interval,
    count_prime_pairs_in_interval,
    interval_for_pattern,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit import exact_gap_coefficients


def interval_scale_rows(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
) -> dict:
    """返回单个窗口族的目标固定 gap 区间尺度审计。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    coefficients = exact_gap_coefficients(shift, point_count)
    tail_set = set(tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes))
    row = brun_row(prime_bound, block, shift, point_count, alpha, num_primes)
    scale_floor = 1.0 / local_c
    intervals = []

    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            for gap in coefficients:
                interval = interval_for_pattern(domain_start, domain_stop, shift, index_a, index_b, gap)
                if interval is None:
                    continue
                lower, upper = interval
                length = upper - lower + 1
                scale = brun_scale_for_interval(lower, upper, gap)
                actual = count_prime_pairs_in_interval(tail_set, lower, upper, gap)
                required_c = actual / scale if scale else None
                intervals.append(
                    {
                        "gap": gap,
                        "j1": index_a,
                        "j2": index_b,
                        "lower": lower,
                        "upper": upper,
                        "length": length,
                        "scale": scale,
                        "actual": actual,
                        "required_c": required_c,
                        "below_scale_floor": scale < scale_floor,
                    }
                )

    intervals.sort(key=lambda item: (item["scale"], item["length"], item["gap"], item["j1"], item["j2"]))
    positive_intervals = [item for item in intervals if item["actual"] > 0]
    low_scale = [item for item in intervals if item["below_scale_floor"]]
    low_scale_positive = [item for item in low_scale if item["actual"] > 0]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "interval_count": len(intervals),
        "positive_interval_count": len(positive_intervals),
        "min_length": min((item["length"] for item in intervals), default=0),
        "min_scale": min((item["scale"] for item in intervals), default=0.0),
        "min_positive_scale": min((item["scale"] for item in positive_intervals), default=0.0),
        "scale_floor": scale_floor,
        "low_scale_count": len(low_scale),
        "low_scale_positive_count": len(low_scale_positive),
        "max_local_required_c": row["max_local_required_c"],
        "top_small_scales": intervals[:8],
        "top_small_positive_scales": sorted(
            positive_intervals,
            key=lambda item: (item["scale"], -item["actual"], item["gap"], item["j1"], item["j2"]),
        )[:8],
    }


def audit_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
) -> dict:
    """返回全部样本的尺度下界审计包。"""
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            rows.append(interval_scale_rows(prime_bound, block, shift, point_count, alpha, num_primes, local_c))
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "row_count": len(rows),
        "total_intervals": sum(row["interval_count"] for row in rows),
        "total_low_scale": sum(row["low_scale_count"] for row in rows),
        "total_low_scale_positive": sum(row["low_scale_positive_count"] for row in rows),
        "global_min_scale": min((row["min_scale"] for row in rows), default=0.0),
        "global_min_positive_scale": min((row["min_positive_scale"] for row in rows), default=0.0),
        "global_max_local_required_c": max((row["max_local_required_c"] for row in rows), default=0.0),
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出尺度审计表。"""
    print(
        f"rows {package['row_count']} intervals {package['total_intervals']} "
        f"local_C {package['local_c']:.6f} scale_floor {1.0 / package['local_c']:.6f} "
        f"low_scale {package['total_low_scale']} low_scale_positive {package['total_low_scale_positive']} "
        f"global_min_scale {package['global_min_scale']:.6f} "
        f"global_min_positive_scale {package['global_min_positive_scale']:.6f} "
        f"global_max_local_C {package['global_max_local_required_c']:.6f}",
        flush=True,
    )
    print(
        "p block shift m intervals positives min_len min_scale min_pos_scale "
        "low_scale low_scale_positive max_local_C",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['interval_count']} {row['positive_interval_count']} {row['min_length']} "
            f"{row['min_scale']:.6f} {row['min_positive_scale']:.6f} "
            f"{row['low_scale_count']} {row['low_scale_positive_count']} "
            f"{row['max_local_required_c']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--local-c", type=float, default=1.3)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = audit_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
    )
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
