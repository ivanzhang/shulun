#!/usr/bin/env python3
"""AlphaTail large-u 短 q 例外审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_large_u_short_exception_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def large_u_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> dict:
    """返回 large-u 短 q 例外审计包。"""
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None:
                    continue
                if record["u"] <= endpoint_theta * domain_length:
                    continue
                rows.append(
                    {
                        **record,
                        "domain_length": domain_length,
                        "u_ratio": record["u"] / domain_length,
                        "short_bound": int(1 / endpoint_theta),
                    }
                )
    rows.sort(key=lambda item: (-item["actual"], item["integer_slack"], -item["u_ratio"]))
    positive = [row for row in rows if row["actual"] > 0]
    failures = [row for row in rows if row["route"] == "C13Failure"]
    parity_void = [row for row in rows if row["route"] == "ParityVoid"]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "large_u_count": len(rows),
        "positive_count": len(positive),
        "failure_count": len(failures),
        "parity_void_count": len(parity_void),
        "max_q_length": max((row["q_length"] for row in rows), default=0),
        "max_actual": max((row["actual"] for row in rows), default=0),
        "top_large_u": rows[:12],
    }


def print_table(package: dict) -> None:
    """输出 large-u 例外表。"""
    print(
        f"large_u {package['large_u_count']} positive {package['positive_count']} "
        f"failures {package['failure_count']} parity_void {package['parity_void_count']} "
        f"theta {package['endpoint_theta']:.6f} max_q_length {package['max_q_length']} "
        f"max_actual {package['max_actual']}",
        flush=True,
    )
    print("p block shift m gap u u_ratio q_len actual threshold slack route", flush=True)
    for row in package["top_large_u"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['gap']} {row['u']} "
            f"{row['u_ratio']:.6f} {row['q_length']} {row['actual']} {row['threshold']} "
            f"{row['integer_slack']} {row['route']}",
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
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = large_u_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
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
