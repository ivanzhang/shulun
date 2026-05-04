#!/usr/bin/env python3
"""AlphaTail C=1.3 近门槛区间端点门控审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_gate_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cuts '1,2,4,8,12,20,40' --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part.strip()) for part in raw.split(",") if part.strip()]


def endpoint_gate_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cuts: list[int],
) -> dict:
    """返回近门槛区间的端点门控审计包。"""
    records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            records.extend(interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c))

    active_records = [
        record
        for record in records
        if record["gap"] % 2 == 0 and record["actual"] > 0
    ]
    cut_rows = []
    for cut in slack_cuts:
        near = [record for record in active_records if record["integer_slack"] <= cut]
        endpoint = [
            record
            for record in near
            if record["endpoint_ratio"] is not None and record["endpoint_ratio"] <= endpoint_theta
        ]
        interior = [record for record in near if record not in endpoint]
        cut_rows.append(
            {
                "slack_cut": cut,
                "near_count": len(near),
                "endpoint_count": len(endpoint),
                "interior_count": len(interior),
                "max_endpoint_ratio": max((record["endpoint_ratio"] or 0.0 for record in near), default=0.0),
                "min_slack": min((record["integer_slack"] for record in near), default=None),
                "max_required_c": max((record["required_c"] or 0.0 for record in near), default=0.0),
            }
        )

    top_near = sorted(
        active_records,
        key=lambda item: (item["integer_slack"], -(item["required_c"] or 0.0), -item["actual"]),
    )[:12]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "active_record_count": len(active_records),
        "cut_rows": cut_rows,
        "top_near_records": top_near,
    }


def print_table(package: dict) -> None:
    """输出端点门控审计表。"""
    print(
        f"active_even_positive {package['active_record_count']} local_C {package['local_c']:.6f} "
        f"endpoint_theta {package['endpoint_theta']:.6f}",
        flush=True,
    )
    print("slack_cut near endpoint interior max_endpoint_ratio min_slack max_required_C", flush=True)
    for row in package["cut_rows"]:
        min_slack = "NA" if row["min_slack"] is None else str(row["min_slack"])
        print(
            f"{row['slack_cut']} {row['near_count']} {row['endpoint_count']} {row['interior_count']} "
            f"{row['max_endpoint_ratio']:.6f} {min_slack} {row['max_required_c']:.6f}",
            flush=True,
        )
    print("top_near p block shift m gap j1 j2 u q_len actual threshold slack req_C endpoint_ratio", flush=True)
    for record in package["top_near_records"]:
        print(
            f"top_near {record['p']} {record['block']} {record['shift']} {record['m']} "
            f"{record['gap']} {record['j1']} {record['j2']} {record['u']} "
            f"{record['q_length']} {record['actual']} {record['threshold']} {record['integer_slack']} "
            f"{(record['required_c'] or 0.0):.6f} {(record['endpoint_ratio'] or 0.0):.6f}",
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
    parser.add_argument("--slack-cuts", type=str, default="1,2,4,8,12,20,40")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = endpoint_gate_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        parse_int_list(args.slack_cuts),
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
