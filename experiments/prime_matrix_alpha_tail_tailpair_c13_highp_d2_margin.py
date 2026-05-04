#!/usr/bin/env python3
"""AlphaTail C13 高 P 的 D2 支配 D_even 余量审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_highp_d2_margin.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_budget_normalization import budget_normalization_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def highp_d2_margin_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
) -> dict:
    """返回高 P D2 支配 D_even 的余量表。"""
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
    rows = []
    total = {
        "capacity_exact_even": 0.0,
        "d2": 0.0,
        "m2": 0.0,
        "b2_model": 0.0,
        "equal_multiplier": 0.0,
    }
    for row in base["rows"]:
        if row["p"] <= finite_p_cut:
            continue
        b2_model = row["m2"] - row["d2"]
        cap_over_m2 = row["capacity_exact_even"] / row["m2"] if row["m2"] else None
        b2_over_m2 = b2_model / row["m2"] if row["m2"] else None
        allowed_b2_over_m2 = 1.0 - cap_over_m2 if cap_over_m2 is not None else None
        item = {
            "p": row["p"],
            "block": row["block"],
            "shift": row["shift"],
            "capacity_exact_even": row["capacity_exact_even"],
            "d2": row["d2"],
            "m2": row["m2"],
            "b2_model": b2_model,
            "equal_multiplier": row["equal_multiplier"],
            "margin": row["d2"] - row["capacity_exact_even"],
            "cap_over_d2": row["capacity_exact_even"] / row["d2"] if row["d2"] else None,
            "cap_over_m2": cap_over_m2,
            "b2_over_m2": b2_over_m2,
            "allowed_b2_over_m2": allowed_b2_over_m2,
            "b2_margin": (
                allowed_b2_over_m2 - b2_over_m2
                if allowed_b2_over_m2 is not None and b2_over_m2 is not None
                else None
            ),
        }
        rows.append(item)
        for key in total:
            total[key] += item[key]
    total["margin"] = total["d2"] - total["capacity_exact_even"]
    total["cap_over_d2"] = total["capacity_exact_even"] / total["d2"] if total["d2"] else None
    total["cap_over_m2"] = total["capacity_exact_even"] / total["m2"] if total["m2"] else None
    total["b2_over_m2"] = total["b2_model"] / total["m2"] if total["m2"] else None
    total["allowed_b2_over_m2"] = (
        1.0 - total["cap_over_m2"] if total["cap_over_m2"] is not None else None
    )
    total["b2_margin"] = (
        total["allowed_b2_over_m2"] - total["b2_over_m2"]
        if total["allowed_b2_over_m2"] is not None and total["b2_over_m2"] is not None
        else None
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "total": total,
        "rows": rows,
    }


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def print_table(package: dict) -> None:
    """输出高 P D2 余量表。"""
    total = package["total"]
    print(
        "scope cap_even D2 margin M2 B2 cap_D2 cap_M2 B2_M2 allowed_B2_M2 B2_margin",
        flush=True,
    )
    print(
        f"highP-total {total['capacity_exact_even']:.6f} {total['d2']:.6f} "
        f"{total['margin']:.6f} {total['m2']:.0f} {total['b2_model']:.6f} "
        f"{fmt(total['cap_over_d2'])} {fmt(total['cap_over_m2'])} "
        f"{fmt(total['b2_over_m2'])} {fmt(total['allowed_b2_over_m2'])} "
        f"{fmt(total['b2_margin'])}",
        flush=True,
    )
    print("p block shift cap_even D2 margin M2 B2 cap_D2 cap_M2 B2_M2 allowed_B2_M2 B2_margin", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['capacity_exact_even']:.6f} {row['d2']:.6f} {row['margin']:.6f} "
            f"{row['m2']:.0f} {row['b2_model']:.6f} "
            f"{fmt(row['cap_over_d2'])} {fmt(row['cap_over_m2'])} "
            f"{fmt(row['b2_over_m2'])} {fmt(row['allowed_b2_over_m2'])} "
            f"{fmt(row['b2_margin'])}",
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
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = highp_d2_margin_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
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
