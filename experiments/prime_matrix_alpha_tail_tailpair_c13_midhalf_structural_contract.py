#!/usr/bin/env python3
"""AlphaTail C13 中间层结构空性合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_midhalf_structural_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import low_primes_for_item, parse_selected
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def midhalf_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层中间层结构空性判据。"""
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    low_min = min(low_primes) if low_primes else None
    n_span = (point_count - 1) * abs(shift)
    if low_min is None:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "low_min": None,
            "n_span": n_span,
            "two_block_plus_n_over_low": None,
            "compression_margin": None,
            "candidate_cases_forced": False,
            "shift_even": shift % 2 == 0,
            "shift_mod3": shift % 3 == 0,
            "low_gt3": False,
            "structural_mid_void": False,
            "reason": "no_low_primes",
        }
    # 若存在真实中间候选，则 q=((u+h)ell+n)/u 且 q<=2B/u。
    # 因 ell>=L, |n|<=N，所以 (u+h)L-N<=2B。
    # 条件 2B+N<5L 强制 u+h<=4，真实中间候选只剩 (2,1) 或 (3,1)。
    compression_margin = 5 * low_min - (2 * block + n_span)
    candidate_cases_forced = compression_margin > 0
    shift_even = shift % 2 == 0
    shift_mod3 = shift % 3 == 0
    low_gt3 = low_min > 3
    # (2,1) 被 n+ell≡0 mod 2 排除；(3,1) 被 n+ell≡0 mod 3 排除。
    structural_mid_void = candidate_cases_forced and shift_even and shift_mod3 and low_gt3
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "low_min": low_min,
        "n_span": n_span,
        "two_block_plus_n_over_low": (2 * block + n_span) / low_min,
        "compression_margin": compression_margin,
        "candidate_cases_forced": candidate_cases_forced,
        "shift_even": shift_even,
        "shift_mod3": shift_mod3,
        "low_gt3": low_gt3,
        "structural_mid_void": structural_mid_void,
        "surviving_candidate_cases": "(u,h)=(2,1) or (3,1)",
    }


def midhalf_structural_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回中间层结构空性合同包。"""
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            rows.append(midhalf_row(prime_bound, block, shift, point_count, alpha, num_primes))
    total = {
        "layers": len(rows),
        "all_candidate_cases_forced": all(row["candidate_cases_forced"] for row in rows),
        "all_shift_even": all(row["shift_even"] for row in rows),
        "all_shift_mod3": all(row["shift_mod3"] for row in rows),
        "all_low_gt3": all(row["low_gt3"] for row in rows),
        "all_structural_mid_void": all(row["structural_mid_void"] for row in rows),
        "min_compression_margin": min(
            (row["compression_margin"] for row in rows if row["compression_margin"] is not None),
            default=None,
        ),
        "max_two_block_plus_n_over_low": max(
            (
                row["two_block_plus_n_over_low"]
                for row in rows
                if row["two_block_plus_n_over_low"] is not None
            ),
            default=None,
        ),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "alpha": alpha,
        "num_primes": num_primes,
        "status": "midlayer_structural_void_sample_closed_global_open",
        "total": total,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出中间层结构空性合同表。"""
    total = package["total"]
    print(
        "scope layers cases_forced shift_even shift_mod3 low_gt3 structural_mid_void "
        "min_compression_margin max_ratio",
        flush=True,
    )
    print(
        f"highP-total {total['layers']} {total['all_candidate_cases_forced']} "
        f"{total['all_shift_even']} {total['all_shift_mod3']} "
        f"{total['all_low_gt3']} {total['all_structural_mid_void']} "
        f"{total['min_compression_margin']} "
        f"{total['max_two_block_plus_n_over_low']:.6f}",
        flush=True,
    )
    print(
        "p block shift m low_min n_span ratio compression_margin cases_forced "
        "shift_even shift_mod3 low_gt3 structural_mid_void",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['low_min']} {row['n_span']} "
            f"{row['two_block_plus_n_over_low']:.6f} "
            f"{row['compression_margin']} {row['candidate_cases_forced']} "
            f"{row['shift_even']} {row['shift_mod3']} {row['low_gt3']} "
            f"{row['structural_mid_void']}",
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

    package = midhalf_structural_package(
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
