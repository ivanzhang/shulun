#!/usr/bin/env python3
"""AlphaTail TailCutoffVoid 充分不等式审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_tail_cutoff_void_inequality_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def inequality_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> list[dict]:
    """返回 large-u 行的 TailCutoffVoid 充分不等式审计。"""
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        tail_cutoff = int(alpha * prime_bound)
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None:
                    continue
                if record["u"] <= endpoint_theta * domain_length:
                    continue
                numerator = domain_stop + record["j1"] * shift
                upper_bound = numerator / (endpoint_theta * domain_length)
                actual_ratio = record["q_upper"] / max(1, tail_cutoff)
                sufficient_ratio = upper_bound / max(1, tail_cutoff)
                rows.append(
                    {
                        **record,
                        "domain_start": domain_start,
                        "domain_stop": domain_stop,
                        "domain_length": domain_length,
                        "tail_cutoff": tail_cutoff,
                        "sufficient_upper_bound": upper_bound,
                        "sufficient_ratio": sufficient_ratio,
                        "actual_q_ratio": actual_ratio,
                        "tail_cutoff_void": record["q_upper"] <= tail_cutoff,
                        "sufficient_pass": upper_bound <= tail_cutoff,
                    }
                )
    rows.sort(key=lambda item: (-item["sufficient_ratio"], -item["actual_q_ratio"], item["p"]))
    return rows


def package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> dict:
    """返回 TailCutoffVoid 不等式审计包。"""
    rows = inequality_rows(selected, m_values, alpha, num_primes, local_c, endpoint_theta)
    failures = [row for row in rows if not row["sufficient_pass"]]
    cutoff_failures = [row for row in rows if not row["tail_cutoff_void"]]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "large_u_count": len(rows),
        "sufficient_failures": len(failures),
        "tail_cutoff_failures": len(cutoff_failures),
        "max_sufficient_ratio": max((row["sufficient_ratio"] for row in rows), default=0.0),
        "max_actual_q_ratio": max((row["actual_q_ratio"] for row in rows), default=0.0),
        "max_q_upper": max((row["q_upper"] for row in rows), default=0),
        "min_tail_cutoff": min((row["tail_cutoff"] for row in rows), default=0),
        "rows": rows,
    }


def print_table(pkg: dict) -> None:
    """输出 TailCutoffVoid 不等式表。"""
    print(
        f"large_u {pkg['large_u_count']} sufficient_failures {pkg['sufficient_failures']} "
        f"tail_cutoff_failures {pkg['tail_cutoff_failures']} "
        f"max_sufficient_ratio {pkg['max_sufficient_ratio']:.6f} "
        f"max_actual_q_ratio {pkg['max_actual_q_ratio']:.6f} "
        f"max_q_upper {pkg['max_q_upper']} min_tail_cutoff {pkg['min_tail_cutoff']}",
        flush=True,
    )
    print(
        "p block shift m gap j1 u q_upper cutoff suff_bound suff_ratio actual_ratio pass",
        flush=True,
    )
    for row in pkg["rows"][:16]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['gap']} "
            f"{row['j1']} {row['u']} {row['q_upper']} {row['tail_cutoff']} "
            f"{row['sufficient_upper_bound']:.6f} {row['sufficient_ratio']:.6f} "
            f"{row['actual_q_ratio']:.6f} {row['sufficient_pass']}",
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

    pkg = package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
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
