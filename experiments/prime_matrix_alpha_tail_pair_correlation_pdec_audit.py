#!/usr/bin/env python3
"""AlphaTail 尾素对相关型 PDEC 下界审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_pair_correlation_pdec_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from math import sqrt

from prime_matrix_alpha_tail_pair_crtdefect_audit import audit_row, parse_selected


def correlation_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    top: int,
) -> dict:
    """返回最热尾素对的相关型 PDEC 下界。"""
    row = audit_row(prime_bound, block, shift, point_count, alpha, num_primes, top)
    if not row["top_pairs"]:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "has_pair": False,
        }
    pair = row["top_pairs"][0]
    modulus = pair["q1"] * pair["q2"]
    residue_count = point_count * point_count
    beta = residue_count / modulus
    l2_phase = sqrt(residue_count * (1.0 - beta))
    e_pair = pair["deviation"]
    l_corr = e_pair * sqrt(modulus) / (sqrt(modulus - 1.0) * l2_phase) if e_pair > 0 else 0.0
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "has_pair": True,
        "q1": pair["q1"],
        "q2": pair["q2"],
        "Q": modulus,
        "low_count": row["low_count"],
        "actual_pair": pair["actual"],
        "model_pair": pair["model"],
        "e_pair": e_pair,
        "residue_count": residue_count,
        "beta": beta,
        "l2_phase": l2_phase,
        "l_corr": l_corr,
        "corr_over_single_count": l_corr / pair["actual"] if pair["actual"] else 0.0,
    }


def print_table(rows: list[dict]) -> None:
    """输出相关型 PDEC 下界表。"""
    print(
        "p block shift m q1 q2 Q low_count actual_pair model_pair E_pair "
        "R_size beta l2_phase L_corr Lcorr_over_actual",
        flush=True,
    )
    for row in rows:
        if not row["has_pair"]:
            print(
                f"{row['p']} {row['block']} {row['shift']} {row['m']} "
                "NA NA NA NA 0 0.000000 0.000000 0 0.000000 0.000000 0.000000 0.000000",
                flush=True,
            )
            continue
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['q1']} {row['q2']} {row['Q']} {row['low_count']} "
            f"{row['actual_pair']} {row['model_pair']:.6f} {row['e_pair']:.6f} "
            f"{row['residue_count']} {row['beta']:.12f} {row['l2_phase']:.12f} "
            f"{row['l_corr']:.12f} {row['corr_over_single_count']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(
                correlation_row(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    args.alpha,
                    args.num_primes,
                    args.top,
                )
            )
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
