#!/usr/bin/env python3
"""AlphaTail 固定 gap C=1.3 整数余量审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --format table
"""

from __future__ import annotations

import argparse
import json
import math

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import (
    brun_scale_for_interval,
    count_prime_pairs_in_interval,
    interval_for_pattern,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit import exact_gap_coefficients


def interval_records(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
) -> list[dict]:
    """返回一个窗口族内所有固定 gap 责任区间的整数余量记录。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_length = max(1, domain_stop - domain_start + 1)
    coefficients = exact_gap_coefficients(shift, point_count)
    tail_set = set(tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes))
    records = []

    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            base = -(index_a - index_b) * shift
            if base <= 0:
                continue
            for gap in coefficients:
                interval = interval_for_pattern(domain_start, domain_stop, shift, index_a, index_b, gap)
                if interval is None:
                    continue
                lower, upper = interval
                length = upper - lower + 1
                scale = brun_scale_for_interval(lower, upper, gap)
                actual = count_prime_pairs_in_interval(tail_set, lower, upper, gap)
                threshold = math.floor(local_c * scale) + 1
                integer_slack = threshold - actual
                multiplier = base // gap if base % gap == 0 else None
                if multiplier:
                    d_lower = lower * multiplier - index_a * shift
                    d_upper = upper * multiplier - index_a * shift
                    endpoint_distance = min(d_lower - domain_start, domain_stop - d_upper)
                    endpoint_ratio = endpoint_distance / domain_length
                else:
                    d_lower = None
                    d_upper = None
                    endpoint_ratio = None
                if gap % 2 == 1:
                    route = "ParityVoid"
                elif integer_slack <= 0:
                    route = "C13Failure"
                elif actual == 0:
                    route = "NoPair"
                else:
                    route = "C13PassPositive"
                records.append(
                    {
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "m": point_count,
                        "gap": gap,
                        "j1": index_a,
                        "j2": index_b,
                        "u": multiplier,
                        "q_lower": lower,
                        "q_upper": upper,
                        "q_length": length,
                        "d_lower": d_lower,
                        "d_upper": d_upper,
                        "scale": scale,
                        "actual": actual,
                        "threshold": threshold,
                        "integer_slack": integer_slack,
                        "required_c": actual / scale if scale else None,
                        "endpoint_ratio": endpoint_ratio,
                        "route": route,
                    }
                )
    return records


def row_summary(records: list[dict]) -> dict:
    """汇总单个窗口族的整数余量。"""
    positive = [record for record in records if record["actual"] > 0]
    failures = [record for record in records if record["integer_slack"] <= 0 and record["gap"] % 2 == 0]
    near = sorted(
        [record for record in positive if record["gap"] % 2 == 0],
        key=lambda item: (item["integer_slack"], -(item["required_c"] or 0), -item["actual"]),
    )
    parity_void = [record for record in records if record["route"] == "ParityVoid"]
    return {
        "p": records[0]["p"] if records else None,
        "block": records[0]["block"] if records else None,
        "shift": records[0]["shift"] if records else None,
        "m": records[0]["m"] if records else None,
        "interval_count": len(records),
        "positive_count": len(positive),
        "parity_void_count": len(parity_void),
        "failure_count": len(failures),
        "min_integer_slack": min((record["integer_slack"] for record in near), default=None),
        "max_required_c": max((record["required_c"] or 0.0 for record in positive), default=0.0),
        "top_near_records": near[:8],
    }


def audit_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
) -> dict:
    """返回全部样本的 C=1.3 整数余量审计包。"""
    summaries = []
    all_records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            records = interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c)
            summaries.append(row_summary(records))
            all_records.extend(records)
    positive_even = [record for record in all_records if record["actual"] > 0 and record["gap"] % 2 == 0]
    failures = [record for record in all_records if record["route"] == "C13Failure"]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "row_count": len(summaries),
        "interval_count": len(all_records),
        "positive_even_count": len(positive_even),
        "failure_count": len(failures),
        "global_min_integer_slack": min((record["integer_slack"] for record in positive_even), default=None),
        "global_max_required_c": max((record["required_c"] or 0.0 for record in positive_even), default=0.0),
        "summaries": summaries,
    }


def print_table(package: dict) -> None:
    """输出整数余量审计表。"""
    min_slack = package["global_min_integer_slack"]
    min_slack_text = "NA" if min_slack is None else str(min_slack)
    print(
        f"rows {package['row_count']} intervals {package['interval_count']} "
        f"local_C {package['local_c']:.6f} positive_even {package['positive_even_count']} "
        f"failures {package['failure_count']} global_min_slack {min_slack_text} "
        f"global_max_required_C {package['global_max_required_c']:.6f}",
        flush=True,
    )
    print(
        "p block shift m intervals positives parity_void failures min_slack max_required_C top_near",
        flush=True,
    )
    for row in package["summaries"]:
        top = ",".join(
            f"g{item['gap']}:a{item['actual']}:t{item['threshold']}:s{item['integer_slack']}:"
            f"c{(item['required_c'] or 0):.3f}:len{item['q_length']}:u{item['u']}"
            for item in row["top_near_records"][:5]
        )
        min_slack_row = "NA" if row["min_integer_slack"] is None else str(row["min_integer_slack"])
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['interval_count']} "
            f"{row['positive_count']} {row['parity_void_count']} {row['failure_count']} "
            f"{min_slack_row} {row['max_required_c']:.6f} {top}",
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
