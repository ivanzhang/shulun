#!/usr/bin/env python3
"""AlphaTail 固定 gap 责任区间格点端点几何审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_lattice_endpoint_geometry_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def geometry_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
) -> dict:
    """返回格点端点几何审计包。"""
    all_records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None or record["d_lower"] is None or record["d_upper"] is None:
                    continue
                left_distance = record["d_lower"] - domain_start
                right_distance = domain_stop - record["d_upper"]
                endpoint_distance = min(left_distance, right_distance)
                lattice_bound = record["u"] - 1
                bound_pass = 0 <= left_distance < record["u"] and 0 <= right_distance < record["u"]
                near_gate = (
                    record["gap"] % 2 == 0
                    and record["actual"] > 0
                    and record["integer_slack"] <= slack_cut
                )
                u_endpoint_forced = record["u"] <= endpoint_theta * domain_length
                all_records.append(
                    {
                        **record,
                        "domain_start": domain_start,
                        "domain_stop": domain_stop,
                        "domain_length": domain_length,
                        "left_distance": left_distance,
                        "right_distance": right_distance,
                        "endpoint_distance": endpoint_distance,
                        "lattice_bound": lattice_bound,
                        "bound_pass": bound_pass,
                        "near_gate": near_gate,
                        "u_endpoint_forced": u_endpoint_forced,
                        "u_ratio": record["u"] / domain_length,
                    }
                )

    near_records = [record for record in all_records if record["near_gate"]]
    near_forced = [record for record in near_records if record["u_endpoint_forced"]]
    near_unforced = [record for record in near_records if not record["u_endpoint_forced"]]
    failures = [record for record in all_records if not record["bound_pass"]]
    top_near = sorted(
        near_records,
        key=lambda item: (item["integer_slack"], -item["required_c"], -item["actual"]),
    )[:12]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "record_count": len(all_records),
        "bound_failures": len(failures),
        "near_count": len(near_records),
        "near_u_endpoint_forced": len(near_forced),
        "near_u_unforced": len(near_unforced),
        "max_near_u_ratio": max((record["u_ratio"] for record in near_records), default=0.0),
        "max_near_endpoint_ratio": max((record["endpoint_ratio"] or 0.0 for record in near_records), default=0.0),
        "top_near_records": top_near,
    }


def print_table(package: dict) -> None:
    """输出格点端点几何表。"""
    print(
        f"records {package['record_count']} bound_failures {package['bound_failures']} "
        f"slack_cut {package['slack_cut']} near {package['near_count']} "
        f"near_u_forced {package['near_u_endpoint_forced']} near_u_unforced {package['near_u_unforced']} "
        f"endpoint_theta {package['endpoint_theta']:.6f} max_near_u_ratio {package['max_near_u_ratio']:.6f} "
        f"max_near_endpoint_ratio {package['max_near_endpoint_ratio']:.6f}",
        flush=True,
    )
    print(
        "top_near p block shift m gap u domain_len q_len actual threshold slack "
        "u_ratio endpoint_ratio left_dist right_dist bound_pass",
        flush=True,
    )
    for record in package["top_near_records"]:
        print(
            f"top_near {record['p']} {record['block']} {record['shift']} {record['m']} "
            f"{record['gap']} {record['u']} {record['domain_length']} {record['q_length']} "
            f"{record['actual']} {record['threshold']} {record['integer_slack']} "
            f"{record['u_ratio']:.6f} {(record['endpoint_ratio'] or 0.0):.6f} "
            f"{record['left_distance']} {record['right_distance']} {record['bound_pass']}",
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
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = geometry_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.slack_cut,
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
