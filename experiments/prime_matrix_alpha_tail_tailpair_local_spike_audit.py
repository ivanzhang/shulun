#!/usr/bin/env python3
"""AlphaTail 尾素对局部尖峰 SAE/Endpoint 路由审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_local_spike_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import brun_row, interval_for_pattern
from prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit import exact_gap_coefficients


def spike_rows(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> list[dict]:
    """返回局部常数超标的责任区间。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_length = max(1, domain_stop - domain_start + 1)
    row = brun_row(prime_bound, block, shift, point_count, alpha, num_primes)
    coefficients = exact_gap_coefficients(shift, point_count)
    spikes: list[dict] = []
    for item in row["top_requirements"]:
        if item["required_c"] <= local_c:
            continue
        gap = item["gap"]
        index_a = item["j1"]
        index_b = item["j2"]
        interval = interval_for_pattern(domain_start, domain_stop, shift, index_a, index_b, gap)
        if interval is None:
            continue
        base = -(index_a - index_b) * shift
        multiplier = base // gap
        q_lower, q_upper = interval
        d_lower = q_lower * multiplier - index_a * shift
        d_upper = q_upper * multiplier - index_a * shift
        endpoint_distance = min(d_lower - domain_start, domain_stop - d_upper)
        endpoint_ratio = endpoint_distance / domain_length
        route = "EndpointSpike" if endpoint_ratio <= endpoint_theta else "InteriorSpike"
        spikes.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "m": point_count,
                "gap": gap,
                "j1": index_a,
                "j2": index_b,
                "u": multiplier,
                "q_lower": q_lower,
                "q_upper": q_upper,
                "q_length": q_upper - q_lower + 1,
                "d_lower": d_lower,
                "d_upper": d_upper,
                "actual": item["actual"],
                "scale": item["scale"],
                "required_c": item["required_c"],
                "local_c": local_c,
                "excess": item["actual"] - local_c * item["scale"],
                "endpoint_distance": endpoint_distance,
                "endpoint_ratio": endpoint_ratio,
                "route": route,
                "coefficient": coefficients.get(gap, 0),
            }
        )
    return spikes


def print_table(rows: list[dict]) -> None:
    """输出局部尖峰责任区间表。"""
    print(
        "p block shift m gap j1 j2 u q_interval d_interval actual scale req_C "
        "excess endpoint_ratio route",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['gap']} {row['j1']} {row['j2']} {row['u']} "
            f"[{row['q_lower']},{row['q_upper']}] [{row['d_lower']},{row['d_upper']}] "
            f"{row['actual']} {row['scale']:.6f} {row['required_c']:.6f} "
            f"{row['excess']:.6f} {row['endpoint_ratio']:.6f} {row['route']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--local-c", type=float, default=1.5)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows: list[dict] = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.extend(
                spike_rows(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    args.alpha,
                    args.num_primes,
                    args.local_c,
                    args.endpoint_theta,
                )
            )
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
