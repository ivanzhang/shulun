#!/usr/bin/env python3
"""AlphaTail C13 lift=1 全局门数总池证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_global_gate_pool.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget import edge_budget_row
from prime_matrix_alpha_tail_tailpair_c13_lift1_midlayer_void_audit import midlayer_row
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def pool_row(
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
    """返回单层 lift=1 全局门数总池证书。"""
    edge = edge_budget_row(
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
    mid = midlayer_row(
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
    slack = edge["slack_before_low"]
    gate_envelope = edge["gate_envelope"] + mid["mid_gate_envelope"]
    formal_exact = edge["unique_edge_units"] + mid["mid_lowprime_exact"]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "slack_before_low": slack,
        "edge_gate_envelope": edge["gate_envelope"],
        "mid_gate_envelope": mid["mid_gate_envelope"],
        "gate_envelope": gate_envelope,
        "unique_edge_units": edge["unique_edge_units"],
        "mid_lowprime_exact": mid["mid_lowprime_exact"],
        "formal_exact": formal_exact,
        "gate_margin": slack - gate_envelope,
        "formal_margin": slack - formal_exact,
        "gate_over_slack": ratio(gate_envelope, slack),
        "formal_over_slack": ratio(formal_exact, slack),
        "gate_pass": gate_envelope <= slack,
        "formal_pass": formal_exact <= slack,
        "mid_void": mid["mid_void"],
    }


def pool_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 lift=1 全局门数总池证书包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "edge_gate_envelope": 0.0,
            "mid_gate_envelope": 0.0,
            "gate_envelope": 0.0,
            "unique_edge_units": 0.0,
            "mid_lowprime_exact": 0.0,
            "formal_exact": 0.0,
            "all_mid_void": True,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "edge_gate_envelope": 0.0,
        "mid_gate_envelope": 0.0,
        "gate_envelope": 0.0,
        "unique_edge_units": 0.0,
        "mid_lowprime_exact": 0.0,
        "formal_exact": 0.0,
        "all_mid_void": True,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = pool_row(
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
                "edge_gate_envelope",
                "mid_gate_envelope",
                "gate_envelope",
                "unique_edge_units",
                "mid_lowprime_exact",
                "formal_exact",
            ):
                total[name] += item[name]
                windows[key][name] += item[name]
            total["all_mid_void"] = total["all_mid_void"] and item["mid_void"]
            windows[key]["all_mid_void"] = windows[key]["all_mid_void"] and item["mid_void"]
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["gate_margin"] = value["slack_before_low"] - value["gate_envelope"]
        value["formal_margin"] = value["slack_before_low"] - value["formal_exact"]
        value["gate_over_slack"] = ratio(value["gate_envelope"], value["slack_before_low"])
        value["formal_over_slack"] = ratio(value["formal_exact"], value["slack_before_low"])
        value["gate_pass"] = value["gate_envelope"] <= value["slack_before_low"]
        value["formal_pass"] = value["formal_exact"] <= value["slack_before_low"]
        window_rows.append(value)
    total["gate_margin"] = total["slack_before_low"] - total["gate_envelope"]
    total["formal_margin"] = total["slack_before_low"] - total["formal_exact"]
    total["gate_over_slack"] = ratio(total["gate_envelope"], total["slack_before_low"])
    total["formal_over_slack"] = ratio(total["formal_exact"], total["slack_before_low"])
    total["gate_pass"] = total["gate_envelope"] <= total["slack_before_low"]
    total["formal_pass"] = total["formal_exact"] <= total["slack_before_low"]
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
    """输出 lift=1 总池证书表。"""
    total = package["total"]
    print(
        "scope slack edge_gate mid_gate gate_env gate_margin gate_slack "
        "formal formal_margin formal_slack mid_void gate_pass formal_pass",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} "
        f"{total['edge_gate_envelope']:.0f} {total['mid_gate_envelope']:.0f} "
        f"{total['gate_envelope']:.0f} {total['gate_margin']:.6f} "
        f"{fmt(total['gate_over_slack'])} {total['formal_exact']:.0f} "
        f"{total['formal_margin']:.6f} {fmt(total['formal_over_slack'])} "
        f"{total['all_mid_void']} {total['gate_pass']} {total['formal_pass']}",
        flush=True,
    )
    print(
        "p block shift slack edge_gate mid_gate gate_env gate_margin gate_slack "
        "formal formal_margin formal_slack mid_void gate_pass formal_pass",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['edge_gate_envelope']:.0f} "
            f"{row['mid_gate_envelope']:.0f} {row['gate_envelope']:.0f} "
            f"{row['gate_margin']:.6f} {fmt(row['gate_over_slack'])} "
            f"{row['formal_exact']:.0f} {row['formal_margin']:.6f} "
            f"{fmt(row['formal_over_slack'])} {row['all_mid_void']} "
            f"{row['gate_pass']} {row['formal_pass']}",
            flush=True,
        )
    print(
        "p block shift m slack edge_gate mid_gate gate_env gate_margin gate_slack "
        "formal formal_margin formal_slack mid_void gate_pass formal_pass",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['edge_gate_envelope']:.0f} "
            f"{row['mid_gate_envelope']:.0f} {row['gate_envelope']:.0f} "
            f"{row['gate_margin']:.6f} {fmt(row['gate_over_slack'])} "
            f"{row['formal_exact']:.0f} {row['formal_margin']:.6f} "
            f"{fmt(row['formal_over_slack'])} {row['mid_void']} "
            f"{row['gate_pass']} {row['formal_pass']}",
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

    package = pool_package(
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
