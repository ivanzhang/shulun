#!/usr/bin/env python3
"""AlphaTail 尾素对端点尖峰吸收审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_absorption_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def absorption_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> dict:
    """统计端点尖峰和内区尖峰。"""
    spikes = spike_rows(prime_bound, block, shift, point_count, alpha, num_primes, local_c, endpoint_theta)
    endpoint_spikes = [spike for spike in spikes if spike["route"] == "EndpointSpike"]
    interior_spikes = [spike for spike in spikes if spike["route"] != "EndpointSpike"]
    max_endpoint_c = max((spike["required_c"] for spike in endpoint_spikes), default=0.0)
    max_interior_c = max((spike["required_c"] for spike in interior_spikes), default=0.0)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "spike_count": len(spikes),
        "endpoint_count": len(endpoint_spikes),
        "interior_count": len(interior_spikes),
        "interior_clear": not interior_spikes,
        "max_endpoint_c": max_endpoint_c,
        "max_interior_c": max_interior_c,
        "top_interior": interior_spikes[:3],
    }


def print_table(rows: list[dict]) -> None:
    """输出端点吸收表。"""
    print(
        "p block shift m local_c theta spikes endpoint interior interior_clear "
        "max_endpoint_C max_interior_C",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['local_c']:.6f} {row['endpoint_theta']:.6f} {row['spike_count']} "
            f"{row['endpoint_count']} {row['interior_count']} {row['interior_clear']} "
            f"{row['max_endpoint_c']:.6f} {row['max_interior_c']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(
                absorption_row(
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
