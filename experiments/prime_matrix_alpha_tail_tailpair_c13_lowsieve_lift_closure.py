#!/usr/bin/env python3
"""AlphaTail C13 低筛保存的 lift 分解闭合证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_lift_closure.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_lift1_integer_margin import lift1_margin_row
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


def closure_row(
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
    """返回单层 lift 分解闭合证书。"""
    lift1 = lift1_margin_row(
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
    consumed = lift1["possible_lift1"] + liftge2["both_tail_count"]
    pass_by_lift = consumed <= lift1["slack_before_low"]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "slack_before_low": lift1["slack_before_low"],
        "possible_lift1": lift1["possible_lift1"],
        "liftge2_candidates": liftge2["candidate_count"],
        "liftge2_both_tail": liftge2["both_tail_count"],
        "liftge2_void_by_q": liftge2["void_by_q_composite"],
        "consumed": consumed,
        "margin": lift1["slack_before_low"] - consumed,
        "consumed_over_slack": ratio(consumed, lift1["slack_before_low"]),
        "pass_by_lift": pass_by_lift,
    }


def closure_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回低筛保存 lift 分解闭合包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "possible_lift1": 0.0,
            "liftge2_candidates": 0.0,
            "liftge2_both_tail": 0.0,
            "consumed": 0.0,
            "all_liftge2_void_by_q": True,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "possible_lift1": 0.0,
        "liftge2_candidates": 0.0,
        "liftge2_both_tail": 0.0,
        "consumed": 0.0,
        "all_liftge2_void_by_q": True,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = closure_row(
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
                "possible_lift1",
                "liftge2_candidates",
                "liftge2_both_tail",
                "consumed",
            ):
                total[name] += item[name]
                windows[key][name] += item[name]
            total["all_liftge2_void_by_q"] = total["all_liftge2_void_by_q"] and item["liftge2_void_by_q"]
            windows[key]["all_liftge2_void_by_q"] = (
                windows[key]["all_liftge2_void_by_q"] and item["liftge2_void_by_q"]
            )
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["margin"] = value["slack_before_low"] - value["consumed"]
        value["consumed_over_slack"] = ratio(value["consumed"], value["slack_before_low"])
        value["pass_by_lift"] = value["consumed"] <= value["slack_before_low"]
        window_rows.append(value)
    total["margin"] = total["slack_before_low"] - total["consumed"]
    total["consumed_over_slack"] = ratio(total["consumed"], total["slack_before_low"])
    total["pass_by_lift"] = total["consumed"] <= total["slack_before_low"]
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
    """输出低筛保存 lift 闭合表。"""
    total = package["total"]
    print(
        "scope slack lift1 ge2_candidates ge2_both consumed margin consumed_slack "
        "ge2_void_by_q pass",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['possible_lift1']:.0f} "
        f"{total['liftge2_candidates']:.0f} {total['liftge2_both_tail']:.0f} "
        f"{total['consumed']:.0f} {total['margin']:.6f} "
        f"{fmt(total['consumed_over_slack'])} {total['all_liftge2_void_by_q']} "
        f"{total['pass_by_lift']}",
        flush=True,
    )
    print("p block shift slack lift1 ge2_candidates ge2_both consumed margin consumed_slack ge2_void_by_q pass", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['possible_lift1']:.0f} "
            f"{row['liftge2_candidates']:.0f} {row['liftge2_both_tail']:.0f} "
            f"{row['consumed']:.0f} {row['margin']:.6f} "
            f"{fmt(row['consumed_over_slack'])} {row['all_liftge2_void_by_q']} "
            f"{row['pass_by_lift']}",
            flush=True,
        )
    print("p block shift m slack lift1 ge2_candidates ge2_both consumed margin consumed_slack ge2_void_by_q pass", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['possible_lift1']:.0f} "
            f"{row['liftge2_candidates']:.0f} {row['liftge2_both_tail']:.0f} "
            f"{row['consumed']:.0f} {row['margin']:.6f} "
            f"{fmt(row['consumed_over_slack'])} {row['liftge2_void_by_q']} "
            f"{row['pass_by_lift']}",
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

    package = closure_package(
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
