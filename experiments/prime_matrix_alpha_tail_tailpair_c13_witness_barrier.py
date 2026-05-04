#!/usr/bin/env python3
"""AlphaTail C13 端点失败的尾素对见证障碍。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_witness_barrier.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def tail_pair_witnesses(tail_set: set[int], lower: int, upper: int, gap: int) -> list[dict]:
    """列出 q,q+gap 均为尾素的见证对。"""
    witnesses = []
    for prime in sorted(tail_set):
        if lower <= prime <= upper and prime + gap in tail_set:
            witnesses.append({"q": prime, "q_plus_g": prime + gap})
    return witnesses


def endpoint_side(record: dict, domain_start: int, domain_stop: int) -> str:
    """返回更靠近的端点方向。"""
    left_distance = record["d_lower"] - domain_start
    right_distance = domain_stop - record["d_upper"]
    return "left" if left_distance <= right_distance else "right"


def witness_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
    top: int,
) -> dict:
    """返回 C13 端点失败见证障碍审计包。"""
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            tail_set = set(tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes))
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None or record["d_lower"] is None or record["d_upper"] is None:
                    continue
                if record["gap"] % 2 == 1 or record["actual"] <= 0:
                    continue
                if record["integer_slack"] > slack_cut:
                    continue
                if record["u"] > endpoint_theta * domain_length:
                    continue

                witnesses = tail_pair_witnesses(
                    tail_set,
                    record["q_lower"],
                    record["q_upper"],
                    record["gap"],
                )
                side = endpoint_side(record, domain_start, domain_stop)
                threshold = record["threshold"]
                actual = record["actual"]
                failure_mass = max(0, actual - threshold + 1)
                extra_to_failure = max(0, threshold - actual)
                if side == "left":
                    excess_witnesses = witnesses[:failure_mass]
                else:
                    excess_witnesses = list(reversed(witnesses[-failure_mass:])) if failure_mass else []
                rows.append(
                    {
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "m": point_count,
                        "gap": record["gap"],
                        "j1": record["j1"],
                        "j2": record["j2"],
                        "u": record["u"],
                        "side": side,
                        "q_lower": record["q_lower"],
                        "q_upper": record["q_upper"],
                        "q_length": record["q_length"],
                        "actual": actual,
                        "threshold": threshold,
                        "integer_slack": record["integer_slack"],
                        "required_c": record["required_c"] or 0.0,
                        "witness_count": len(witnesses),
                        "count_identity_ok": len(witnesses) == actual,
                        "failure_mass": failure_mass,
                        "extra_to_failure": extra_to_failure,
                        "excess_witnesses": excess_witnesses,
                    }
                )

    failures = [row for row in rows if row["failure_mass"] > 0]
    nonfailures = [row for row in rows if row["failure_mass"] == 0]
    rows.sort(
        key=lambda item: (
            item["failure_mass"] == 0,
            -item["failure_mass"],
            item["extra_to_failure"],
            item["integer_slack"],
            -item["required_c"],
        )
    )
    identity_failures = [row for row in rows if not row["count_identity_ok"]]
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "record_count": len(rows),
        "failure_records": len(failures),
        "failure_mass": sum(row["failure_mass"] for row in failures),
        "identity_failures": len(identity_failures),
        "min_extra_to_failure": min((row["extra_to_failure"] for row in nonfailures), default=None),
        "max_required_c": max((row["required_c"] for row in rows), default=0.0),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出见证障碍简表。"""
    min_extra = "NA" if package["min_extra_to_failure"] is None else str(package["min_extra_to_failure"])
    print(
        "records failures failure_mass identity_failures min_extra_to_failure max_required_C",
        flush=True,
    )
    print(
        f"{package['record_count']} {package['failure_records']} {package['failure_mass']} "
        f"{package['identity_failures']} {min_extra} {package['max_required_c']:.6f}",
        flush=True,
    )
    print(
        "p block shift m gap j1 j2 u side actual threshold slack "
        "extra_to_failure failure_mass witnesses q_range excess_witnesses",
        flush=True,
    )
    for row in package["rows"]:
        excess = ",".join(f"{item['q']}+{row['gap']}={item['q_plus_g']}" for item in row["excess_witnesses"])
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['gap']} "
            f"{row['j1']} {row['j2']} {row['u']} {row['side']} {row['actual']} "
            f"{row['threshold']} {row['integer_slack']} {row['extra_to_failure']} "
            f"{row['failure_mass']} {row['witness_count']} "
            f"[{row['q_lower']},{row['q_upper']}] {excess or 'none'}",
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
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = witness_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.slack_cut,
        args.top,
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
