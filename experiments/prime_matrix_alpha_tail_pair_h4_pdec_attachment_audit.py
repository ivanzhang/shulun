#!/usr/bin/env python3
"""AlphaTail 热尾素对接入 H4-PDEC 的常数审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_pair_h4_pdec_attachment_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from math import sqrt

from prime_matrix_alpha_tail_pair_crtdefect_audit import audit_row, parse_selected


def attachment_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    top: int,
) -> dict:
    """返回最热尾素对的 H4-PDEC 接入常数。"""
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
    point = pair["top_point"]
    modulus = pair["q1"] * pair["q2"]
    support_count = point["count"]
    kappa = 1.0 - 1.0 / modulus
    l2_norm = sqrt(1.0 - 1.0 / modulus)
    l_pdec = support_count / sqrt(modulus)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "has_pair": True,
        "q1": pair["q1"],
        "q2": pair["q2"],
        "j1": point["j1"],
        "j2": point["j2"],
        "Q": modulus,
        "low_count": row["low_count"],
        "support_count": support_count,
        "model": point["model"],
        "deviation": point["deviation"],
        "kappa": kappa,
        "l2_norm": l2_norm,
        "l_pdec": l_pdec,
        "max_hat": support_count,
        "explicit_hat_over_l_pdec": support_count / l_pdec if l_pdec else None,
    }


def print_table(rows: list[dict]) -> None:
    """输出 H4-PDEC 接入常数表。"""
    print(
        "p block shift m q1 q2 j1 j2 Q low_count support_count model deviation "
        "kappa l2 L_PDEC max_hat hat_over_L",
        flush=True,
    )
    for row in rows:
        if not row["has_pair"]:
            print(
                f"{row['p']} {row['block']} {row['shift']} {row['m']} "
                "NA NA NA NA NA NA 0 0.000000 0.000000 0.000000 0.000000 0.000000 0 0.000000",
                flush=True,
            )
            continue
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['q1']} {row['q2']} {row['j1']} {row['j2']} {row['Q']} "
            f"{row['low_count']} {row['support_count']} {row['model']:.6f} "
            f"{row['deviation']:.6f} {row['kappa']:.12f} {row['l2_norm']:.12f} "
            f"{row['l_pdec']:.12f} {row['max_hat']} {row['explicit_hat_over_l_pdec']:.6f}",
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
                attachment_row(
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
