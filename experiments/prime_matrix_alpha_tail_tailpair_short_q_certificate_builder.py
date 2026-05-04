#!/usr/bin/env python3
"""AlphaTail large-u 短 q 例外有限证书生成器。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_short_q_certificate_builder.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def certificate_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> list[dict]:
    """生成 large-u 短 q 有限证书行。"""
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            tail_cutoff = int(alpha * prime_bound)
            tail_set = set(tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes))
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None:
                    continue
                if record["u"] <= endpoint_theta * domain_length:
                    continue
                candidates = []
                pair_count = 0
                for candidate in range(record["q_lower"], record["q_upper"] + 1):
                    left_tail = candidate in tail_set
                    right_tail = candidate + record["gap"] in tail_set
                    is_pair = left_tail and right_tail
                    pair_count += 1 if is_pair else 0
                    candidates.append(
                        {
                            "q": candidate,
                            "q_plus_gap": candidate + record["gap"],
                            "left_tail": left_tail,
                            "right_tail": right_tail,
                            "pair": is_pair,
                        }
                    )
                rows.append(
                    {
                        **record,
                        "domain_length": domain_length,
                        "u_ratio": record["u"] / domain_length,
                        "tail_cutoff": tail_cutoff,
                        "tail_cutoff_void": record["q_upper"] <= tail_cutoff,
                        "candidate_count": len(candidates),
                        "candidate_pair_count": pair_count,
                        "count_matches": pair_count == record["actual"],
                        "certificate_pass": pair_count < record["threshold"],
                        "candidates": candidates,
                    }
                )
    rows.sort(key=lambda item: (-item["candidate_pair_count"], item["gap"], -item["u_ratio"], item["p"]))
    return rows


def package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> dict:
    """返回有限证书包。"""
    rows = certificate_rows(selected, m_values, alpha, num_primes, local_c, endpoint_theta)
    failures = [row for row in rows if not row["certificate_pass"] or not row["count_matches"]]
    positive = [row for row in rows if row["candidate_pair_count"] > 0]
    tail_cutoff_void = [row for row in rows if row["tail_cutoff_void"]]
    return {
        "selected": selected,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "row_count": len(rows),
        "positive_rows": len(positive),
        "failure_rows": len(failures),
        "tail_cutoff_void_rows": len(tail_cutoff_void),
        "max_candidate_count": max((row["candidate_count"] for row in rows), default=0),
        "max_pair_count": max((row["candidate_pair_count"] for row in rows), default=0),
        "max_q_upper": max((row["q_upper"] for row in rows), default=0),
        "min_tail_cutoff": min((row["tail_cutoff"] for row in rows), default=0),
        "all_certified": not failures,
        "rows": rows,
    }


def print_table(pkg: dict) -> None:
    """输出有限证书表。"""
    print(
        f"rows {pkg['row_count']} positive_rows {pkg['positive_rows']} "
        f"failure_rows {pkg['failure_rows']} all_certified {pkg['all_certified']} "
        f"tail_cutoff_void {pkg['tail_cutoff_void_rows']} "
        f"max_candidate_count {pkg['max_candidate_count']} max_pair_count {pkg['max_pair_count']} "
        f"max_q_upper {pkg['max_q_upper']} min_tail_cutoff {pkg['min_tail_cutoff']}",
        flush=True,
    )
    print(
        "p block shift m gap u q_interval cutoff cutoff_void candidates pairs threshold slack pass sample_candidates",
        flush=True,
    )
    for row in pkg["rows"]:
        sample = ",".join(
            f"{item['q']}:{'P' if item['pair'] else '-'}" for item in row["candidates"][:10]
        )
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['gap']} {row['u']} "
            f"[{row['q_lower']},{row['q_upper']}] {row['tail_cutoff']} {row['tail_cutoff_void']} "
            f"{row['candidate_count']} "
            f"{row['candidate_pair_count']} {row['threshold']} {row['integer_slack']} "
            f"{row['certificate_pass']} {sample}",
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
