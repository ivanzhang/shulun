#!/usr/bin/env python3
"""AlphaTail 尾素对小位移端点清除审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_smallshift_endpoint_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds


def smallshift_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    endpoint_theta: float,
) -> dict:
    """返回小位移端点清除条件。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_length = max(0, domain_stop - domain_start + 1)
    max_multiplier = (point_count - 1) * abs(shift)
    endpoint_budget = endpoint_theta * domain_length
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "domain_start": domain_start,
        "domain_stop": domain_stop,
        "domain_length": domain_length,
        "u_max": max_multiplier,
        "endpoint_theta": endpoint_theta,
        "endpoint_budget": endpoint_budget,
        "smallshift_pass": max_multiplier <= endpoint_budget,
        "margin": endpoint_budget - max_multiplier,
        "ratio": max_multiplier / domain_length if domain_length else None,
    }


def print_table(rows: list[dict]) -> None:
    """输出小位移端点清除表。"""
    print(
        "p block shift m domain_length u_max thetaH ratio margin smallshift_pass",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['domain_length']} {row['u_max']} {row['endpoint_budget']:.6f} "
            f"{row['ratio']:.6f} {row['margin']:.6f} {row['smallshift_pass']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(smallshift_row(prime_bound, block, shift, point_count, args.endpoint_theta))
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
