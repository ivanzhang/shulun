#!/usr/bin/env python3
"""AlphaTail C13 lift>=2 结构空性判据审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_structural_criterion.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
)
from prime_matrix_alpha_tail_tailpair_c13_liftge2_signature_audit import signature_row
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def criterion_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层 lift>=2 结构空性判据。"""
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    if not low_primes:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "criterion_pass": False,
            "reason": "no_low_primes",
        }
    low_min = min(low_primes)
    shift_abs = abs(shift)
    block_condition = block < 2 * low_min
    n_condition = (point_count - 1) * shift_abs < low_min
    mod6_condition = shift_abs % 6 == 0
    signature = signature_row(prime_bound, block, shift, point_count, alpha, num_primes)
    criterion_pass = block_condition and n_condition and mod6_condition
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "low_min": low_min,
        "block_over_low": block / low_min,
        "n_span": (point_count - 1) * shift_abs,
        "n_span_over_low": ((point_count - 1) * shift_abs) / low_min,
        "block_condition": block_condition,
        "n_condition": n_condition,
        "mod6_condition": mod6_condition,
        "criterion_pass": criterion_pass,
        "signature_candidates": signature["candidate_count"],
        "signature_all_bad": signature["all_bad_mod6"],
        "signature_good_mod6": signature["good_mod6_count"],
        "u_hist": signature["u_hist"],
        "t_hist": signature["t_hist"],
        "h_hist": signature["h_hist"],
    }


def criterion_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回结构空性判据包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "criterion_pass": True,
            "signature_all_bad": True,
            "signature_candidates": 0,
            "signature_good_mod6": 0,
            "min_block_margin": None,
            "min_n_margin": None,
        }
    )
    total = {
        "criterion_pass": True,
        "signature_all_bad": True,
        "signature_candidates": 0,
        "signature_good_mod6": 0,
        "min_block_margin": None,
        "min_n_margin": None,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = criterion_row(prime_bound, block, shift, point_count, alpha, num_primes)
            rows.append(item)
            key = (prime_bound, block, shift)
            block_margin = 2 * item["low_min"] - block
            n_margin = item["low_min"] - item["n_span"]
            for bucket in (total, windows[key]):
                bucket["criterion_pass"] = bucket["criterion_pass"] and item["criterion_pass"]
                bucket["signature_all_bad"] = bucket["signature_all_bad"] and item["signature_all_bad"]
                bucket["signature_candidates"] += item["signature_candidates"]
                bucket["signature_good_mod6"] += item["signature_good_mod6"]
                bucket["min_block_margin"] = (
                    block_margin
                    if bucket["min_block_margin"] is None
                    else min(bucket["min_block_margin"], block_margin)
                )
                bucket["min_n_margin"] = (
                    n_margin
                    if bucket["min_n_margin"] is None
                    else min(bucket["min_n_margin"], n_margin)
                )
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        window_rows.append(value)
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "alpha": alpha,
        "num_primes": num_primes,
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出结构空性判据表。"""
    total = package["total"]
    print(
        "scope candidates good criterion all_bad min_block_margin min_n_margin",
        flush=True,
    )
    print(
        f"highP-total {total['signature_candidates']} {total['signature_good_mod6']} "
        f"{total['criterion_pass']} {total['signature_all_bad']} "
        f"{total['min_block_margin']} {total['min_n_margin']}",
        flush=True,
    )
    print("p block shift candidates good criterion all_bad min_block_margin min_n_margin", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['signature_candidates']} {row['signature_good_mod6']} "
            f"{row['criterion_pass']} {row['signature_all_bad']} "
            f"{row['min_block_margin']} {row['min_n_margin']}",
            flush=True,
        )
    print(
        "p block shift m low_min block_over_low n_span n_over_low "
        "block_ok n_ok mod6_ok criterion candidates good all_bad u_hist t_hist h_hist",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['low_min']} {row['block_over_low']:.6f} "
            f"{row['n_span']} {row['n_span_over_low']:.6f} "
            f"{row['block_condition']} {row['n_condition']} {row['mod6_condition']} "
            f"{row['criterion_pass']} {row['signature_candidates']} "
            f"{row['signature_good_mod6']} {row['signature_all_bad']} "
            f"{row['u_hist']} {row['t_hist']} {row['h_hist']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = criterion_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.alpha,
        args.num_primes,
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
