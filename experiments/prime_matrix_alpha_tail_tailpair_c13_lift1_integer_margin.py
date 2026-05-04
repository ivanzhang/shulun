#!/usr/bin/env python3
"""AlphaTail C13 lift=1 纯整数候选余量审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_integer_margin.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_ap_lift_rigidity_audit import lift_row
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def lift1_margin_row(
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
    """返回单层 lift=1 纯整数候选余量。"""
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
    lift = lift_row(prime_bound, block, shift, point_count, alpha, num_primes)
    slack = target["geometric_upper"] - target["required_m2"]
    possible_lift1 = lift["possible_lift1_count"]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "slack_before_low": slack,
        "possible_lift1": possible_lift1,
        "possible_lift_ge2": lift["possible_lift_ge2_count"],
        "active_lift1": lift["active_lift1_count"],
        "active_lift_ge2": lift["active_lift_ge2_count"],
        "lift1_margin": slack - possible_lift1,
        "lift1_over_slack": ratio(possible_lift1, slack),
        "lift1_pass": possible_lift1 <= slack,
        "active_lift_ge2_zero": lift["active_lift_ge2_count"] == 0,
    }


def lift1_margin_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 lift=1 纯整数候选余量包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "possible_lift1": 0.0,
            "possible_lift_ge2": 0.0,
            "active_lift1": 0.0,
            "active_lift_ge2": 0.0,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "possible_lift1": 0.0,
        "possible_lift_ge2": 0.0,
        "active_lift1": 0.0,
        "active_lift_ge2": 0.0,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = lift1_margin_row(
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
        value["lift1_margin"] = value["slack_before_low"] - value["possible_lift1"]
        value["lift1_over_slack"] = ratio(value["possible_lift1"], value["slack_before_low"])
        value["lift1_pass"] = value["possible_lift1"] <= value["slack_before_low"]
        value["active_lift_ge2_zero"] = value["active_lift_ge2"] == 0
        window_rows.append(value)
    total["lift1_margin"] = total["slack_before_low"] - total["possible_lift1"]
    total["lift1_over_slack"] = ratio(total["possible_lift1"], total["slack_before_low"])
    total["lift1_pass"] = total["possible_lift1"] <= total["slack_before_low"]
    total["active_lift_ge2_zero"] = total["active_lift_ge2"] == 0
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
    """输出 lift=1 纯整数候选余量表。"""
    total = package["total"]
    print(
        "scope slack possible_lift1 margin lift1_slack possible_lift_ge2 "
        "active_lift1 active_lift_ge2 lift1_pass ge2_zero",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['possible_lift1']:.0f} "
        f"{total['lift1_margin']:.6f} {fmt(total['lift1_over_slack'])} "
        f"{total['possible_lift_ge2']:.0f} {total['active_lift1']:.0f} "
        f"{total['active_lift_ge2']:.0f} {total['lift1_pass']} "
        f"{total['active_lift_ge2_zero']}",
        flush=True,
    )
    print("p block shift slack possible_lift1 margin lift1_slack possible_lift_ge2 active_lift1 active_lift_ge2 lift1_pass ge2_zero", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['possible_lift1']:.0f} "
            f"{row['lift1_margin']:.6f} {fmt(row['lift1_over_slack'])} "
            f"{row['possible_lift_ge2']:.0f} {row['active_lift1']:.0f} "
            f"{row['active_lift_ge2']:.0f} {row['lift1_pass']} "
            f"{row['active_lift_ge2_zero']}",
            flush=True,
        )
    print("p block shift m slack possible_lift1 margin lift1_slack possible_lift_ge2 active_lift1 active_lift_ge2 lift1_pass ge2_zero", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['possible_lift1']:.0f} "
            f"{row['lift1_margin']:.6f} {fmt(row['lift1_over_slack'])} "
            f"{row['possible_lift_ge2']:.0f} {row['active_lift1']:.0f} "
            f"{row['active_lift_ge2']:.0f} {row['lift1_pass']} "
            f"{row['active_lift_ge2_zero']}",
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

    package = lift1_margin_package(
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
