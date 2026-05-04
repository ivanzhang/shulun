#!/usr/bin/env python3
"""AlphaTail C13 低筛保存总池桥接证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_global_pool_bridge.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_lift1_global_gate_pool import pool_row
from prime_matrix_alpha_tail_tailpair_c13_liftge2_void_audit import liftge2_row
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def bridge_row(
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
    """返回单层低筛保存总池桥接证书。"""
    lift1 = pool_row(
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
    liftge2 = liftge2_row(prime_bound, block, shift, point_count, alpha, num_primes)
    gate_consumed = lift1["gate_envelope"] + liftge2["both_tail_count"]
    formal_consumed = lift1["formal_exact"] + liftge2["both_tail_count"]
    slack = lift1["slack_before_low"]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "slack_before_low": slack,
        "gate_lift1": lift1["gate_envelope"],
        "formal_lift1": lift1["formal_exact"],
        "liftge2_both": liftge2["both_tail_count"],
        "liftge2_candidates": liftge2["candidate_count"],
        "liftge2_void_by_q": liftge2["void_by_q_composite"],
        "gate_consumed": gate_consumed,
        "formal_consumed": formal_consumed,
        "gate_margin": slack - gate_consumed,
        "formal_margin": slack - formal_consumed,
        "gate_over_slack": ratio(gate_consumed, slack),
        "formal_over_slack": ratio(formal_consumed, slack),
        "gate_pass": gate_consumed <= slack,
        "formal_pass": formal_consumed <= slack,
        "mid_void": lift1["mid_void"],
    }


def bridge_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回低筛保存总池桥接证书包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "gate_lift1": 0.0,
            "formal_lift1": 0.0,
            "liftge2_both": 0.0,
            "liftge2_candidates": 0.0,
            "gate_consumed": 0.0,
            "formal_consumed": 0.0,
            "all_liftge2_void_by_q": True,
            "all_mid_void": True,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "gate_lift1": 0.0,
        "formal_lift1": 0.0,
        "liftge2_both": 0.0,
        "liftge2_candidates": 0.0,
        "gate_consumed": 0.0,
        "formal_consumed": 0.0,
        "all_liftge2_void_by_q": True,
        "all_mid_void": True,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = bridge_row(
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
            for name in (
                "slack_before_low",
                "gate_lift1",
                "formal_lift1",
                "liftge2_both",
                "liftge2_candidates",
                "gate_consumed",
                "formal_consumed",
            ):
                total[name] += item[name]
                windows[key][name] += item[name]
            total["all_liftge2_void_by_q"] = (
                total["all_liftge2_void_by_q"] and item["liftge2_void_by_q"]
            )
            windows[key]["all_liftge2_void_by_q"] = (
                windows[key]["all_liftge2_void_by_q"] and item["liftge2_void_by_q"]
            )
            total["all_mid_void"] = total["all_mid_void"] and item["mid_void"]
            windows[key]["all_mid_void"] = windows[key]["all_mid_void"] and item["mid_void"]
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["gate_margin"] = value["slack_before_low"] - value["gate_consumed"]
        value["formal_margin"] = value["slack_before_low"] - value["formal_consumed"]
        value["gate_over_slack"] = ratio(value["gate_consumed"], value["slack_before_low"])
        value["formal_over_slack"] = ratio(value["formal_consumed"], value["slack_before_low"])
        value["gate_pass"] = value["gate_consumed"] <= value["slack_before_low"]
        value["formal_pass"] = value["formal_consumed"] <= value["slack_before_low"]
        window_rows.append(value)
    total["gate_margin"] = total["slack_before_low"] - total["gate_consumed"]
    total["formal_margin"] = total["slack_before_low"] - total["formal_consumed"]
    total["gate_over_slack"] = ratio(total["gate_consumed"], total["slack_before_low"])
    total["formal_over_slack"] = ratio(total["formal_consumed"], total["slack_before_low"])
    total["gate_pass"] = total["gate_consumed"] <= total["slack_before_low"]
    total["formal_pass"] = total["formal_consumed"] <= total["slack_before_low"]
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
    """输出低筛保存总池桥接证书表。"""
    total = package["total"]
    print(
        "scope slack gate_lift1 formal_lift1 ge2_both ge2_candidates "
        "gate_consumed formal_consumed gate_margin formal_margin gate_slack "
        "formal_slack mid_void ge2_void gate_pass formal_pass",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['gate_lift1']:.0f} "
        f"{total['formal_lift1']:.0f} {total['liftge2_both']:.0f} "
        f"{total['liftge2_candidates']:.0f} {total['gate_consumed']:.0f} "
        f"{total['formal_consumed']:.0f} {total['gate_margin']:.6f} "
        f"{total['formal_margin']:.6f} {fmt(total['gate_over_slack'])} "
        f"{fmt(total['formal_over_slack'])} {total['all_mid_void']} "
        f"{total['all_liftge2_void_by_q']} {total['gate_pass']} {total['formal_pass']}",
        flush=True,
    )
    print(
        "p block shift slack gate_lift1 formal_lift1 ge2_both ge2_candidates "
        "gate_consumed formal_consumed gate_margin formal_margin gate_slack "
        "formal_slack mid_void ge2_void gate_pass formal_pass",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['gate_lift1']:.0f} "
            f"{row['formal_lift1']:.0f} {row['liftge2_both']:.0f} "
            f"{row['liftge2_candidates']:.0f} {row['gate_consumed']:.0f} "
            f"{row['formal_consumed']:.0f} {row['gate_margin']:.6f} "
            f"{row['formal_margin']:.6f} {fmt(row['gate_over_slack'])} "
            f"{fmt(row['formal_over_slack'])} {row['all_mid_void']} "
            f"{row['all_liftge2_void_by_q']} {row['gate_pass']} {row['formal_pass']}",
            flush=True,
        )
    print(
        "p block shift m slack gate_lift1 formal_lift1 ge2_both ge2_candidates "
        "gate_consumed formal_consumed gate_margin formal_margin gate_slack "
        "formal_slack mid_void ge2_void gate_pass formal_pass",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['gate_lift1']:.0f} "
            f"{row['formal_lift1']:.0f} {row['liftge2_both']:.0f} "
            f"{row['liftge2_candidates']:.0f} {row['gate_consumed']:.0f} "
            f"{row['formal_consumed']:.0f} {row['gate_margin']:.6f} "
            f"{row['formal_margin']:.6f} {fmt(row['gate_over_slack'])} "
            f"{fmt(row['formal_over_slack'])} {row['mid_void']} "
            f"{row['liftge2_void_by_q']} {row['gate_pass']} {row['formal_pass']}",
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

    package = bridge_package(
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
