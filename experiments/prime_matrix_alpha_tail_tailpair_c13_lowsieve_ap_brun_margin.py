#!/usr/bin/env python3
"""AlphaTail C13 低筛 AP 删除的 Brun 常数余量审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_brun_margin.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --ap-c 20 --format table
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import singular_factor
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_deletion_audit import ap_deletion_row
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit import ceil_div, count_progression, divisors
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def ap_brun_scale_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    ap_c: float,
) -> dict:
    """返回单层 AP-Brun 余量。"""
    deletion = ap_deletion_row(
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
        return {**deletion, "ap_brun_scale": 0.0}
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    ap_brun_scale = 0.0
    impossible_class_count = 0
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
                log_base = math.log(max(3, q_lo))
                local_scale = singular_factor(gap) / (log_base * log_base)
                for low_prime in low_primes:
                    inverse = pow(multiplier, -1, low_prime)
                    for index in range(point_count):
                        residue = (-(index - index_a) * shift * inverse) % low_prime
                        if (residue + gap) % low_prime == 0:
                            impossible_class_count += 1
                            continue
                        integer_count = count_progression(q_lo, q_hi, low_prime, residue)
                        ap_brun_scale += local_scale * integer_count
    allowable_c = ratio(deletion["slack_before_low"], ap_brun_scale)
    observed_c = ratio(deletion["raw_ap_deletions"], ap_brun_scale)
    brun_capacity = ap_c * ap_brun_scale
    return {
        **deletion,
        "ap_brun_scale": ap_brun_scale,
        "ap_c": ap_c,
        "brun_capacity": brun_capacity,
        "allowable_c": allowable_c,
        "observed_c": observed_c,
        "impossible_class_count": impossible_class_count,
        "ap_brun_pass": brun_capacity <= deletion["slack_before_low"] + 1e-12,
    }


def ap_brun_margin_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    ap_c: float,
) -> dict:
    """返回 AP-Brun 余量包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "raw_ap_deletions": 0.0,
            "ap_brun_scale": 0.0,
            "brun_capacity": 0.0,
            "impossible_class_count": 0,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "raw_ap_deletions": 0.0,
        "ap_brun_scale": 0.0,
        "brun_capacity": 0.0,
        "impossible_class_count": 0,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = ap_brun_scale_row(
                prime_bound,
                block,
                shift,
                point_count,
                m_values,
                eta,
                alpha,
                num_primes,
                endpoint_band_theta,
                ap_c,
            )
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in total:
                total[name] += item[name]
                windows[key][name] += item[name]
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["ap_c"] = ap_c
        value["allowable_c"] = ratio(value["slack_before_low"], value["ap_brun_scale"])
        value["observed_c"] = ratio(value["raw_ap_deletions"], value["ap_brun_scale"])
        value["ap_brun_pass"] = value["brun_capacity"] <= value["slack_before_low"] + 1e-12
        window_rows.append(value)
    total["ap_c"] = ap_c
    total["allowable_c"] = ratio(total["slack_before_low"], total["ap_brun_scale"])
    total["observed_c"] = ratio(total["raw_ap_deletions"], total["ap_brun_scale"])
    total["ap_brun_pass"] = total["brun_capacity"] <= total["slack_before_low"] + 1e-12
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "ap_c": ap_c,
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出 AP-Brun 余量表。"""
    total = package["total"]
    print(
        "scope slack raw_ap ap_scale brun_cap allowable_C observed_C impossible ap_C pass",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['raw_ap_deletions']:.0f} "
        f"{total['ap_brun_scale']:.6f} {total['brun_capacity']:.6f} "
        f"{fmt(total['allowable_c'])} {fmt(total['observed_c'])} "
        f"{total['impossible_class_count']} {total['ap_c']:.6f} {total['ap_brun_pass']}",
        flush=True,
    )
    print("p block shift slack raw_ap ap_scale brun_cap allowable_C observed_C impossible ap_C pass", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['raw_ap_deletions']:.0f} "
            f"{row['ap_brun_scale']:.6f} {row['brun_capacity']:.6f} "
            f"{fmt(row['allowable_c'])} {fmt(row['observed_c'])} "
            f"{row['impossible_class_count']} {row['ap_c']:.6f} {row['ap_brun_pass']}",
            flush=True,
        )
    print("p block shift m slack raw_ap ap_scale brun_cap allowable_C observed_C impossible ap_C pass", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['raw_ap_deletions']:.0f} "
            f"{row['ap_brun_scale']:.6f} {row['brun_capacity']:.6f} "
            f"{fmt(row['allowable_c'])} {fmt(row['observed_c'])} "
            f"{row['impossible_class_count']} {row['ap_c']:.6f} {row['ap_brun_pass']}",
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
    parser.add_argument("--ap-c", type=float, default=20.0)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = ap_brun_margin_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.endpoint_band_theta,
        args.ap_c,
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
