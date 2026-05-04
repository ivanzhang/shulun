#!/usr/bin/env python3
"""AlphaTail C13 small-u 端点相位键账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_phase_ledger.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def endpoint_phase_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
) -> dict:
    """返回 C13 近门槛端点相位键账本。"""
    key_rows: dict[tuple[int, int, int, int, str], dict] = {}
    total_records = 0
    failure_records = 0
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None or record["d_lower"] is None or record["d_upper"] is None:
                    continue
                if record["gap"] % 2 == 1 or record["actual"] <= 0:
                    continue
                if record["integer_slack"] > slack_cut:
                    continue
                if record["u"] > endpoint_theta * domain_length:
                    continue
                left_distance = record["d_lower"] - domain_start
                right_distance = domain_stop - record["d_upper"]
                side = "left" if left_distance <= right_distance else "right"
                key = (record["gap"], record["j1"], record["j2"], record["u"], side)
                total_records += 1
                failure_records += 1 if record["integer_slack"] <= 0 else 0
                if key not in key_rows:
                    key_rows[key] = {
                        "gap": record["gap"],
                        "j1": record["j1"],
                        "j2": record["j2"],
                        "u": record["u"],
                        "side": side,
                        "record_count": 0,
                        "failure_count": 0,
                        "min_slack": record["integer_slack"],
                        "max_required_c": record["required_c"] or 0.0,
                        "total_actual": 0,
                        "total_threshold": 0,
                        "examples": [],
                    }
                row = key_rows[key]
                row["record_count"] += 1
                row["failure_count"] += 1 if record["integer_slack"] <= 0 else 0
                row["min_slack"] = min(row["min_slack"], record["integer_slack"])
                row["max_required_c"] = max(row["max_required_c"], record["required_c"] or 0.0)
                row["total_actual"] += record["actual"]
                row["total_threshold"] += record["threshold"]
                if len(row["examples"]) < 5:
                    row["examples"].append(
                        {
                            "p": prime_bound,
                            "block": block,
                            "shift": shift,
                            "m": point_count,
                            "q_lower": record["q_lower"],
                            "q_upper": record["q_upper"],
                            "actual": record["actual"],
                            "threshold": record["threshold"],
                            "slack": record["integer_slack"],
                        }
                    )
    rows = sorted(
        key_rows.values(),
        key=lambda item: (item["min_slack"], -item["max_required_c"], -item["record_count"]),
    )
    side_counts = defaultdict(int)
    for row in rows:
        side_counts[row["side"]] += row["record_count"]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "record_count": total_records,
        "failure_records": failure_records,
        "key_count": len(rows),
        "side_counts": dict(side_counts),
        "min_slack": min((row["min_slack"] for row in rows), default=None),
        "max_required_c": max((row["max_required_c"] for row in rows), default=0.0),
        "keys": rows,
    }


def print_table(pkg: dict) -> None:
    """输出端点相位键账本。"""
    min_slack = "NA" if pkg["min_slack"] is None else str(pkg["min_slack"])
    print(
        f"records {pkg['record_count']} failures {pkg['failure_records']} keys {pkg['key_count']} "
        f"slack_cut {pkg['slack_cut']} min_slack {min_slack} "
        f"max_required_C {pkg['max_required_c']:.6f} side_counts {pkg['side_counts']}",
        flush=True,
    )
    print("gap j1 j2 u side count failures min_slack max_required_C total_actual total_threshold", flush=True)
    for row in pkg["keys"][:20]:
        print(
            f"{row['gap']} {row['j1']} {row['j2']} {row['u']} {row['side']} "
            f"{row['record_count']} {row['failure_count']} {row['min_slack']} "
            f"{row['max_required_c']:.6f} {row['total_actual']} {row['total_threshold']}",
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

    pkg = endpoint_phase_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.slack_cut,
    )
    if args.format == "json":
        print(json.dumps(pkg, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(pkg)
        return
    print(pkg, flush=True)


if __name__ == "__main__":
    main()
