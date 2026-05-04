#!/usr/bin/env python3
"""AlphaTail C13 低 P 有限外壳 + 高 P 除数外壳的混合预算证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hybrid_budget_certificate.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --eta 0.04 --finite-p-cut 1000 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_budget_normalization import budget_normalization_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def hybrid_budget_package(
    selected: str,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
    finite_p_cut: int,
    finite_mode: str,
) -> dict:
    """返回低 P 有限、高 P 闭式的混合预算证书。"""
    base = budget_normalization_package(
        selected,
        m_values,
        eta,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        endpoint_band_theta,
        slack_cut,
    )
    finite_field = {
        "failure": "capacity_failure",
        "geometric": "capacity_geometric_dedup",
        "narrow": "capacity_narrow",
        "positive": "capacity_positive",
    }[finite_mode]
    rows = []
    totals = {
        "hybrid_capacity": 0.0,
        "d2": 0.0,
        "equal_multiplier": 0.0,
        "m2": 0.0,
    }
    for row in base["rows"]:
        use_finite = row["p"] <= finite_p_cut
        capacity = row[finite_field] if use_finite else row["capacity_exact_even"]
        route = f"Finite-{finite_mode}" if use_finite else "Divisor-D_even"
        item = {
            "p": row["p"],
            "block": row["block"],
            "shift": row["shift"],
            "route": route,
            "hybrid_capacity": capacity,
            "d2": row["d2"],
            "equal_multiplier": row["equal_multiplier"],
            "m2": row["m2"],
            "hybrid_over_d2": capacity / row["d2"] if row["d2"] else None,
            "hybrid_over_equal": capacity / row["equal_multiplier"] if row["equal_multiplier"] else None,
            "finite_capacity": row[finite_field],
            "exact_even_capacity": row["capacity_exact_even"],
        }
        rows.append(item)
        totals["hybrid_capacity"] += capacity
        totals["d2"] += row["d2"]
        totals["equal_multiplier"] += row["equal_multiplier"]
        totals["m2"] += row["m2"]
    totals["hybrid_over_d2"] = totals["hybrid_capacity"] / totals["d2"] if totals["d2"] else None
    totals["hybrid_over_equal"] = (
        totals["hybrid_capacity"] / totals["equal_multiplier"]
        if totals["equal_multiplier"]
        else None
    )
    totals["max_window_hybrid_over_d2"] = max(
        (row["hybrid_over_d2"] for row in rows if row["hybrid_over_d2"] is not None),
        default=None,
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "finite_p_cut": finite_p_cut,
        "finite_mode": finite_mode,
        "total": totals,
        "rows": rows,
    }


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def print_table(package: dict) -> None:
    """输出混合预算证书表。"""
    total = package["total"]
    print(
        "finite_cut finite_mode hybrid_capacity D2 equal M2 hybrid_D2 "
        "hybrid_equal max_window_D2",
        flush=True,
    )
    print(
        f"{package['finite_p_cut']} {package['finite_mode']} "
        f"{total['hybrid_capacity']:.6f} {total['d2']:.6f} "
        f"{total['equal_multiplier']:.0f} {total['m2']:.0f} "
        f"{fmt(total['hybrid_over_d2'])} {fmt(total['hybrid_over_equal'])} "
        f"{fmt(total['max_window_hybrid_over_d2'])}",
        flush=True,
    )
    print("p block shift route hybrid_capacity finite_capacity exact_even D2 hybrid_D2 hybrid_equal", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['route']} "
            f"{row['hybrid_capacity']:.6f} {row['finite_capacity']:.6f} "
            f"{row['exact_even_capacity']:.6f} {row['d2']:.6f} "
            f"{fmt(row['hybrid_over_d2'])} {fmt(row['hybrid_over_equal'])}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--finite-mode", choices=("failure", "geometric", "narrow", "positive"), default="geometric")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hybrid_budget_package(
        args.selected,
        parse_m_values(args.m_values),
        args.eta,
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
        args.finite_p_cut,
        args.finite_mode,
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
