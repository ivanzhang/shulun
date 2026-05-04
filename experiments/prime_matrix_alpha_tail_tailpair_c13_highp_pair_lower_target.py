#!/usr/bin/env python3
"""AlphaTail C13 高 P 的固定 gap 素对下界目标审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_divisor_sum_envelope_bound import window_divisor_bounds
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_geometric_certificate_audit import geometric_row
from prime_matrix_alpha_tail_tailpair_resonance_budget_audit import budget_row


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def row_target(
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
    """返回单个 m 层需要的等乘数素对下界。"""
    budget = budget_row(prime_bound, block, shift, point_count, alpha, num_primes)
    divisor = window_divisor_bounds(
        prime_bound,
        block,
        shift,
        m_values,
        endpoint_band_theta,
        eta,
    )
    geometry = geometric_row(prime_bound, block, shift, point_count, alpha, num_primes)
    exact_even_for_m = sum(
        term["exact_term"] for term in divisor["terms"] if term["m"] == point_count
    )
    capacity_even = len(m_values) * eta * exact_even_for_m
    required_m2 = budget["b2_model"] + capacity_even
    margin = budget["m2"] - required_m2
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "cap_even": capacity_even,
        "exact_even_bound": exact_even_for_m,
        "m2": budget["m2"],
        "b2_model": budget["b2_model"],
        "d2": budget["d2"],
        "required_m2": required_m2,
        "margin": margin,
        "equal_multiplier": budget["equal_multiplier"],
        "non_equal": budget["non_equal"],
        "geometric_upper": geometry["geometric_upper"],
        "low_survivor_exact": geometry["low_survivor_exact"],
        "equal_identity_ok": geometry["low_survivor_exact"] == budget["equal_multiplier"],
        "non_equal_ratio": ratio(budget["non_equal"], budget["m2"]),
        "required_over_m2": ratio(required_m2, budget["m2"]),
        "required_over_equal": ratio(required_m2, budget["equal_multiplier"]),
        "required_over_geometric": ratio(required_m2, geometry["geometric_upper"]),
        "low_survivor_over_geometric": ratio(
            geometry["low_survivor_exact"],
            geometry["geometric_upper"],
        ),
    }


def highp_pair_lower_target_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回高 P 固定 gap 素对下界目标包。"""
    rows = []
    total = {
        "cap_even": 0.0,
        "m2": 0.0,
        "b2_model": 0.0,
        "d2": 0.0,
        "required_m2": 0.0,
        "equal_multiplier": 0.0,
        "non_equal": 0.0,
        "geometric_upper": 0.0,
        "low_survivor_exact": 0.0,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = row_target(
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
            for key in total:
                total[key] += item[key]
    total["margin"] = total["m2"] - total["required_m2"]
    total["non_equal_ratio"] = ratio(total["non_equal"], total["m2"])
    total["required_over_m2"] = ratio(total["required_m2"], total["m2"])
    total["required_over_equal"] = ratio(total["required_m2"], total["equal_multiplier"])
    total["required_over_geometric"] = ratio(total["required_m2"], total["geometric_upper"])
    total["low_survivor_over_geometric"] = ratio(
        total["low_survivor_exact"],
        total["geometric_upper"],
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "total": total,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出固定 gap 素对下界目标表。"""
    total = package["total"]
    print(
        "scope cap_even B2 required_M2 M2 margin equal non_equal geom_upper "
        "req_M2 req_equal req_geom low_geom non_equal_ratio",
        flush=True,
    )
    print(
        f"highP-total {total['cap_even']:.6f} {total['b2_model']:.6f} "
        f"{total['required_m2']:.6f} {total['m2']:.0f} {total['margin']:.6f} "
        f"{total['equal_multiplier']:.0f} {total['non_equal']:.0f} "
        f"{total['geometric_upper']:.0f} {fmt(total['required_over_m2'])} "
        f"{fmt(total['required_over_equal'])} {fmt(total['required_over_geometric'])} "
        f"{fmt(total['low_survivor_over_geometric'])} {fmt(total['non_equal_ratio'])}",
        flush=True,
    )
    print(
        "p block shift m cap_even B2 required_M2 M2 margin equal non_equal "
        "geom_upper req_M2 req_equal req_geom low_geom identity",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['cap_even']:.6f} {row['b2_model']:.6f} "
            f"{row['required_m2']:.6f} {row['m2']:.0f} {row['margin']:.6f} "
            f"{row['equal_multiplier']:.0f} {row['non_equal']:.0f} "
            f"{row['geometric_upper']:.0f} {fmt(row['required_over_m2'])} "
            f"{fmt(row['required_over_equal'])} {fmt(row['required_over_geometric'])} "
            f"{fmt(row['low_survivor_over_geometric'])} {row['equal_identity_ok']}",
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

    package = highp_pair_lower_target_package(
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
