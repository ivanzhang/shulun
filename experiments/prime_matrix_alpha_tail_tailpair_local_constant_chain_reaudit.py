#!/usr/bin/env python3
"""AlphaTail 局部常数调整后的端点链重审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_local_constant_chain_reaudit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import brun_row
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def chain_reaudit_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    global_c: float,
) -> dict:
    """审计局部常数调整后端点链是否启动。"""
    rows = []
    total_spikes = 0
    total_endpoint = 0
    total_interior = 0
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            brun = brun_row(prime_bound, block, shift, point_count, alpha, num_primes)
            spikes = spike_rows(
                prime_bound,
                block,
                shift,
                point_count,
                alpha,
                num_primes,
                local_c,
                endpoint_theta,
            )
            endpoint_count = sum(1 for spike in spikes if spike["route"] == "EndpointSpike")
            interior_count = len(spikes) - endpoint_count
            total_spikes += len(spikes)
            total_endpoint += endpoint_count
            total_interior += interior_count
            rows.append(
                {
                    "p": prime_bound,
                    "block": block,
                    "shift": shift,
                    "m": point_count,
                    "required_c_bs": brun["required_c_bs"],
                    "max_local_required_c": brun["max_local_required_c"],
                    "global_pass": brun["required_c_bs"] <= global_c,
                    "local_pass": brun["max_local_required_c"] <= local_c,
                    "spike_count": len(spikes),
                    "endpoint_count": endpoint_count,
                    "interior_count": interior_count,
                    "downstream_route": "DownstreamEmpty" if not spikes else "EndpointChainActive",
                }
            )
    return {
        "selected": selected,
        "global_c": global_c,
        "local_c": local_c,
        "row_count": len(rows),
        "total_spikes": total_spikes,
        "total_endpoint": total_endpoint,
        "total_interior": total_interior,
        "all_global_pass": all(row["global_pass"] for row in rows),
        "all_local_pass": all(row["local_pass"] for row in rows),
        "downstream_empty": total_spikes == 0,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出端点链重审计表。"""
    print(
        f"rows {package['row_count']} global_C {package['global_c']:.6f} "
        f"local_C {package['local_c']:.6f} spikes {package['total_spikes']} "
        f"endpoint {package['total_endpoint']} interior {package['total_interior']} "
        f"all_global_pass {package['all_global_pass']} all_local_pass {package['all_local_pass']} "
        f"downstream_empty {package['downstream_empty']}",
        flush=True,
    )
    print("p block shift m req_C_BS max_local_C global_pass local_pass spikes endpoint interior route", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['required_c_bs']:.6f} {row['max_local_required_c']:.6f} "
            f"{row['global_pass']} {row['local_pass']} {row['spike_count']} "
            f"{row['endpoint_count']} {row['interior_count']} {row['downstream_route']}",
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
    parser.add_argument("--global-c", type=float, default=1.5)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = chain_reaudit_rows(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.global_c,
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
