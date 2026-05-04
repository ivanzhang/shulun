#!/usr/bin/env python3
"""AlphaTail C13 低筛删除 AP 素对上界审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_deletion_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit import ceil_div, count_progression, divisors
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ap_deletion_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回单层 AP 素对删除审计行。"""
    target = row_target(
        prime_bound,
        block,
        shift,
        point_count,
        m_values,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    if not tail_primes:
        return {**target, "raw_ap_deletions": 0, "unique_ap_deletions": 0}
    tail_set = set(tail_primes)
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    raw_integer_ceiling = 0
    raw_ap_deletions = 0
    unique_ap_deletions: set[tuple[int, int, int, int, int]] = set()
    ap_class_count = 0
    active_ap_class_count = 0
    max_ap_per_class = 0
    top_classes: Counter[tuple[int, int, int, int, int, int, int]] = Counter()
    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            base = -(index_a - index_b) * shift
            if base <= 0:
                continue
            for multiplier in divisors(base):
                gap = base // multiplier
                q_lo = max(tail_min, ceil_div(domain_start + index_a * shift, multiplier))
                q_hi = min(tail_max - gap, (domain_stop + index_a * shift) // multiplier)
                if q_hi < q_lo:
                    continue
                candidate_qs = [
                    prime for prime in tail_primes
                    if q_lo <= prime <= q_hi and prime + gap in tail_set
                ]
                for low_prime in low_primes:
                    inverse = pow(multiplier, -1, low_prime)
                    for index in range(point_count):
                        residue = (-(index - index_a) * shift * inverse) % low_prime
                        raw_integer_ceiling += count_progression(q_lo, q_hi, low_prime, residue)
                        ap_class_count += 1
                        class_count = 0
                        for prime in candidate_qs:
                            if prime % low_prime != residue:
                                continue
                            class_count += 1
                            raw_ap_deletions += 1
                            unique_ap_deletions.add((index_a, index_b, multiplier, gap, prime))
                        if class_count:
                            active_ap_class_count += 1
                            max_ap_per_class = max(max_ap_per_class, class_count)
                            top_classes[
                                (low_prime, index, residue, gap, multiplier, index_a, index_b)
                            ] += class_count
    actual_deleted = target["geometric_upper"] - target["low_survivor_exact"]
    slack_before_low = target["geometric_upper"] - target["required_m2"]
    top_class_rows = [
        {
            "ell": key[0],
            "j": key[1],
            "residue": key[2],
            "gap": key[3],
            "u": key[4],
            "j1": key[5],
            "j2": key[6],
            "count": count,
        }
        for key, count in top_classes.most_common(8)
    ]
    return {
        **target,
        "actual_deleted": actual_deleted,
        "slack_before_low": slack_before_low,
        "raw_integer_ceiling": raw_integer_ceiling,
        "raw_ap_deletions": raw_ap_deletions,
        "unique_ap_deletions": len(unique_ap_deletions),
        "ap_class_count": ap_class_count,
        "active_ap_class_count": active_ap_class_count,
        "max_ap_per_class": max_ap_per_class,
        "ap_pass": raw_ap_deletions <= slack_before_low,
        "ap_identity_ok": len(unique_ap_deletions) == actual_deleted,
        "top_classes": top_class_rows,
    }


def ap_deletion_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 AP 素对删除审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "geometric_upper": 0.0,
            "required_m2": 0.0,
            "actual_deleted": 0.0,
            "raw_integer_ceiling": 0.0,
            "raw_ap_deletions": 0.0,
            "unique_ap_deletions": 0.0,
            "ap_class_count": 0,
            "active_ap_class_count": 0,
            "max_ap_per_class": 0,
        }
    )
    total = {
        "geometric_upper": 0.0,
        "required_m2": 0.0,
        "actual_deleted": 0.0,
        "raw_integer_ceiling": 0.0,
        "raw_ap_deletions": 0.0,
        "unique_ap_deletions": 0.0,
        "ap_class_count": 0,
        "active_ap_class_count": 0,
        "max_ap_per_class": 0,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = ap_deletion_row(
                prime_bound,
                block,
                shift,
                point_count,
                m_values,
                eta,
                alpha,
                num_primes,
                endpoint_band_theta,
            )
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in total:
                if name == "max_ap_per_class":
                    total[name] = max(total[name], item[name])
                    windows[key][name] = max(windows[key][name], item[name])
                    continue
                total[name] += item[name]
                windows[key][name] += item[name]
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["slack_before_low"] = value["geometric_upper"] - value["required_m2"]
        value["ap_pass"] = value["raw_ap_deletions"] <= value["slack_before_low"]
        value["ap_identity_ok"] = value["unique_ap_deletions"] == value["actual_deleted"]
        window_rows.append(value)
    total["slack_before_low"] = total["geometric_upper"] - total["required_m2"]
    total["ap_pass"] = total["raw_ap_deletions"] <= total["slack_before_low"]
    total["ap_identity_ok"] = total["unique_ap_deletions"] == total["actual_deleted"]
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出 AP 删除审计表。"""
    total = package["total"]
    print(
        "scope geom required slack actual_del int_ceiling raw_ap unique_ap "
        "classes active_classes max_class ap_pass identity",
        flush=True,
    )
    print(
        f"highP-total {total['geometric_upper']:.0f} {total['required_m2']:.6f} "
        f"{total['slack_before_low']:.6f} {total['actual_deleted']:.0f} "
        f"{total['raw_integer_ceiling']:.0f} {total['raw_ap_deletions']:.0f} "
        f"{total['unique_ap_deletions']:.0f} {total['ap_class_count']} "
        f"{total['active_ap_class_count']} {total['max_ap_per_class']} "
        f"{total['ap_pass']} {total['ap_identity_ok']}",
        flush=True,
    )
    print("p block shift geom required slack actual_del int_ceiling raw_ap unique_ap classes active_classes max_class ap_pass identity", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['geometric_upper']:.0f} {row['required_m2']:.6f} "
            f"{row['slack_before_low']:.6f} {row['actual_deleted']:.0f} "
            f"{row['raw_integer_ceiling']:.0f} {row['raw_ap_deletions']:.0f} "
            f"{row['unique_ap_deletions']:.0f} {row['ap_class_count']} "
            f"{row['active_ap_class_count']} {row['max_ap_per_class']} "
            f"{row['ap_pass']} {row['ap_identity_ok']}",
            flush=True,
        )
    print("p block shift m geom required slack actual_del int_ceiling raw_ap unique_ap classes active_classes max_class ap_pass identity", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['geometric_upper']:.0f} {row['required_m2']:.6f} "
            f"{row['slack_before_low']:.6f} {row['actual_deleted']:.0f} "
            f"{row['raw_integer_ceiling']:.0f} {row['raw_ap_deletions']:.0f} "
            f"{row['unique_ap_deletions']:.0f} {row['ap_class_count']} "
            f"{row['active_ap_class_count']} {row['max_ap_per_class']} "
            f"{row['ap_pass']} {row['ap_identity_ok']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = ap_deletion_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.endpoint_band_theta,
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
