#!/usr/bin/env python3
"""AlphaTail C13 Formal 局部付款合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_formal_local_payment_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_lift1_global_gate_pool import pool_package
from prime_matrix_alpha_tail_tailpair_c13_liftge2_void_audit import liftge2_void_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def by_window(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引审计行。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def formal_local_payment_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 Formal 局部付款合同包。"""
    pool = pool_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    liftge2 = liftge2_void_package(selected, m_values, finite_p_cut, alpha, num_primes)
    pool_by_window = by_window(pool["windows"])
    ge2_by_window = by_window(liftge2["windows"])
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        key = (prime_bound, block, shift)
        pool_row = pool_by_window[key]
        ge2_row = ge2_by_window[key]
        formal_consumed = pool_row["formal_exact"] + ge2_row["both_tail_count"]
        slack = pool_row["slack_before_low"]
        row = {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "slack": slack,
            "unique_edge_units": pool_row["unique_edge_units"],
            "mid_lowprime_exact": pool_row["mid_lowprime_exact"],
            "liftge2_both": ge2_row["both_tail_count"],
            "formal_consumed": formal_consumed,
            "edge_margin_if_void": slack - pool_row["unique_edge_units"],
            "formal_margin": slack - formal_consumed,
            "formal_over_slack": ratio(formal_consumed, slack),
            "mid_void": pool_row["mid_lowprime_exact"] == 0 and pool_row["all_mid_void"],
            "liftge2_void": ge2_row["both_tail_count"] == 0 and ge2_row["both_tail_void"],
            "formal_pass": formal_consumed <= slack,
        }
        rows.append(row)
    total_slack = sum(row["slack"] for row in rows)
    total_formal = sum(row["formal_consumed"] for row in rows)
    total = {
        "highp_windows": len(rows),
        "total_slack": total_slack,
        "total_unique_edge_units": sum(row["unique_edge_units"] for row in rows),
        "total_mid_lowprime_exact": sum(row["mid_lowprime_exact"] for row in rows),
        "total_liftge2_both": sum(row["liftge2_both"] for row in rows),
        "total_formal_consumed": total_formal,
        "total_formal_margin": total_slack - total_formal,
        "max_formal_over_slack": max((row["formal_over_slack"] for row in rows), default=None),
        "min_edge_margin_if_void": min((row["edge_margin_if_void"] for row in rows), default=None),
        "min_formal_margin": min((row["formal_margin"] for row in rows), default=None),
        "all_mid_void": all(row["mid_void"] for row in rows),
        "all_liftge2_void": all(row["liftge2_void"] for row in rows),
        "all_formal_pass": all(row["formal_pass"] for row in rows),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "formal_local_payment_sample_closed_global_open",
        "total": total,
        "windows": rows,
    }


def print_table(package: dict) -> None:
    """输出 Formal 局部付款合同表。"""
    total = package["total"]
    print(
        "scope windows slack edge mid ge2 formal margin min_local_margin "
        "min_edge_void_margin max_formal_slack mid_void ge2_void pass",
        flush=True,
    )
    print(
        f"highP-total {total['highp_windows']} {total['total_slack']:.6f} "
        f"{total['total_unique_edge_units']:.0f} {total['total_mid_lowprime_exact']:.0f} "
        f"{total['total_liftge2_both']:.0f} {total['total_formal_consumed']:.0f} "
        f"{total['total_formal_margin']:.6f} {fmt(total['min_formal_margin'])} "
        f"{fmt(total['min_edge_margin_if_void'])} {fmt(total['max_formal_over_slack'])} "
        f"{total['all_mid_void']} {total['all_liftge2_void']} {total['all_formal_pass']}",
        flush=True,
    )
    print(
        "p block shift slack edge mid ge2 formal edge_void_margin formal_margin "
        "formal_slack mid_void ge2_void pass",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['slack']:.6f} "
            f"{row['unique_edge_units']:.0f} {row['mid_lowprime_exact']:.0f} "
            f"{row['liftge2_both']:.0f} {row['formal_consumed']:.0f} "
            f"{row['edge_margin_if_void']:.6f} {row['formal_margin']:.6f} "
            f"{fmt(row['formal_over_slack'])} {row['mid_void']} "
            f"{row['liftge2_void']} {row['formal_pass']}",
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

    package = formal_local_payment_package(
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
