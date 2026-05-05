#!/usr/bin/env python3
"""AlphaTail C13 中间层奇偶空性合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_midlayer_parity_void_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import low_primes_for_item, parse_selected
from prime_matrix_alpha_tail_tailpair_c13_lift1_midlayer_void_audit import midlayer_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def midlayer_parity_void_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回中间层奇偶空性合同包。"""
    mid = midlayer_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    rows = []
    for row in mid["rows"]:
        low_primes = low_primes_for_item(
            row["p"],
            row["block"],
            row["shift"],
            row["m"],
            alpha,
            num_primes,
        )
        low_min = min(low_primes) if low_primes else None
        half_only = set(row["all_h_ratios"]) <= {"1/2"}
        shift_even = row["shift"] % 2 == 0
        low_odd = low_min is not None and low_min > 2
        parity_void = half_only and shift_even and low_odd
        rows.append(
            {
                "p": row["p"],
                "block": row["block"],
                "shift": row["shift"],
                "m": row["m"],
                "low_min": low_min,
                "mid_gates": row["mid_h_gate_count"],
                "mid_integer_ceiling": row["mid_integer_ceiling"],
                "mid_exact": row["mid_lowprime_exact"],
                "h_ratios": row["all_h_ratios"],
                "half_only": half_only,
                "shift_even": shift_even,
                "low_odd": low_odd,
                "parity_void": parity_void,
                "mid_void": row["mid_void"],
            }
        )
    total = {
        "layers": len(rows),
        "mid_gates": sum(row["mid_gates"] for row in rows),
        "mid_integer_ceiling": sum(row["mid_integer_ceiling"] for row in rows),
        "mid_exact": sum(row["mid_exact"] for row in rows),
        "all_half_only": all(row["half_only"] for row in rows),
        "all_shift_even": all(row["shift_even"] for row in rows),
        "all_low_odd": all(row["low_odd"] for row in rows),
        "all_parity_void": all(row["parity_void"] for row in rows),
        "all_mid_void": all(row["mid_void"] for row in rows),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "midlayer_parity_void_sample_closed_global_open",
        "total": total,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出中间层奇偶空性合同表。"""
    total = package["total"]
    print(
        "scope layers gates int_ceiling exact half_only shift_even low_odd parity_void mid_void",
        flush=True,
    )
    print(
        f"highP-total {total['layers']} {total['mid_gates']} "
        f"{total['mid_integer_ceiling']} {total['mid_exact']} "
        f"{total['all_half_only']} {total['all_shift_even']} "
        f"{total['all_low_odd']} {total['all_parity_void']} "
        f"{total['all_mid_void']}",
        flush=True,
    )
    print(
        "p block shift m low_min gates int_ceiling exact h_ratios half_only "
        "shift_even low_odd parity_void mid_void",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['low_min']} {row['mid_gates']} {row['mid_integer_ceiling']} "
            f"{row['mid_exact']} {row['h_ratios']} {row['half_only']} "
            f"{row['shift_even']} {row['low_odd']} {row['parity_void']} "
            f"{row['mid_void']}",
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

    package = midlayer_parity_void_package(
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
