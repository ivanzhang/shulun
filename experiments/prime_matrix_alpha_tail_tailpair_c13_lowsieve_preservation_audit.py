#!/usr/bin/env python3
"""AlphaTail C13 高 P 的低筛保存余量审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ceil_div(numerator: int, denominator: int) -> int:
    """返回向上整除。"""
    return -((-numerator) // denominator)


def divisors(value: int) -> list[int]:
    """返回正整数因子。"""
    result = []
    for candidate in range(1, int(value**0.5) + 1):
        if value % candidate == 0:
            result.append(candidate)
            if candidate * candidate != value:
                result.append(value // candidate)
    return sorted(result)


def count_progression(lo: int, hi: int, modulus: int, residue: int) -> int:
    """计数区间内指定同余类的整数个数。"""
    if hi < lo:
        return 0
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


def integer_deletion_ceiling(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回不使用素对分布的低筛删除整数同余上界。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    if not tail_primes:
        return {"channels": 0, "integer_interval_mass": 0, "integer_deletion_ceiling": 0}
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    channels = 0
    integer_interval_mass = 0
    deletion_ceiling = 0
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
                channels += 1
                integer_interval_mass += q_hi - q_lo + 1
                for low_prime in low_primes:
                    inverse = pow(multiplier, -1, low_prime)
                    for index in range(point_count):
                        residue = (-(index - index_a) * shift * inverse) % low_prime
                        deletion_ceiling += count_progression(q_lo, q_hi, low_prime, residue)
    return {
        "channels": channels,
        "integer_interval_mass": integer_interval_mass,
        "integer_deletion_ceiling": deletion_ceiling,
    }


def lowsieve_row(
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
    """返回单层低筛保存审计行。"""
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
    ceiling = integer_deletion_ceiling(
        prime_bound,
        block,
        shift,
        point_count,
        alpha,
        num_primes,
    )
    actual_deleted = target["geometric_upper"] - target["low_survivor_exact"]
    slack_before_low = target["geometric_upper"] - target["required_m2"]
    return {
        **target,
        **ceiling,
        "actual_deleted": actual_deleted,
        "slack_before_low": slack_before_low,
        "actual_preservation_pass": actual_deleted <= slack_before_low,
        "integer_ceiling_pass": ceiling["integer_deletion_ceiling"] <= slack_before_low,
    }


def lowsieve_preservation_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回高 P 低筛保存审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "geometric_upper": 0.0,
            "low_survivor_exact": 0.0,
            "required_m2": 0.0,
            "actual_deleted": 0.0,
            "integer_deletion_ceiling": 0.0,
            "integer_interval_mass": 0.0,
            "channels": 0,
        }
    )
    total = {
        "geometric_upper": 0.0,
        "low_survivor_exact": 0.0,
        "required_m2": 0.0,
        "actual_deleted": 0.0,
        "integer_deletion_ceiling": 0.0,
        "integer_interval_mass": 0.0,
        "channels": 0,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = lowsieve_row(
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
                total[name] += item[name]
                windows[key][name] += item[name]
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["slack_before_low"] = value["geometric_upper"] - value["required_m2"]
        value["actual_preservation_pass"] = value["actual_deleted"] <= value["slack_before_low"]
        value["integer_ceiling_pass"] = value["integer_deletion_ceiling"] <= value["slack_before_low"]
        window_rows.append(value)
    total["slack_before_low"] = total["geometric_upper"] - total["required_m2"]
    total["actual_preservation_pass"] = total["actual_deleted"] <= total["slack_before_low"]
    total["integer_ceiling_pass"] = total["integer_deletion_ceiling"] <= total["slack_before_low"]
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
    """输出低筛保存余量表。"""
    total = package["total"]
    print(
        "scope geom required slack actual_deleted int_del_ceiling channels int_mass "
        "actual_pass int_pass",
        flush=True,
    )
    print(
        f"highP-total {total['geometric_upper']:.0f} {total['required_m2']:.6f} "
        f"{total['slack_before_low']:.6f} {total['actual_deleted']:.0f} "
        f"{total['integer_deletion_ceiling']:.0f} {total['channels']} "
        f"{total['integer_interval_mass']:.0f} {total['actual_preservation_pass']} "
        f"{total['integer_ceiling_pass']}",
        flush=True,
    )
    print("p block shift geom required slack actual_deleted int_del_ceiling channels int_mass actual_pass int_pass", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['geometric_upper']:.0f} {row['required_m2']:.6f} "
            f"{row['slack_before_low']:.6f} {row['actual_deleted']:.0f} "
            f"{row['integer_deletion_ceiling']:.0f} {row['channels']} "
            f"{row['integer_interval_mass']:.0f} {row['actual_preservation_pass']} "
            f"{row['integer_ceiling_pass']}",
            flush=True,
        )
    print("p block shift m geom required slack actual_deleted int_del_ceiling channels int_mass actual_pass int_pass", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['geometric_upper']:.0f} {row['required_m2']:.6f} "
            f"{row['slack_before_low']:.6f} {row['actual_deleted']:.0f} "
            f"{row['integer_deletion_ceiling']:.0f} {row['channels']} "
            f"{row['integer_interval_mass']:.0f} {row['actual_preservation_pass']} "
            f"{row['integer_ceiling_pass']}",
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

    package = lowsieve_preservation_package(
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
