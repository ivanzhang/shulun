#!/usr/bin/env python3
"""AlphaTail 尾素对 Brun/Selberg 验收账本审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_brun_acceptance_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --global-c 1.5 --local-c 1.5 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import brun_row


def acceptance_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    global_c: float,
    local_c: float,
) -> dict:
    """返回单个窗口的 Brun/Selberg 验收状态。"""
    row = brun_row(prime_bound, block, shift, point_count, alpha, num_primes)
    global_capacity = global_c * row["bs_scale"]
    global_pass = row["geom_count"] <= global_capacity + 1e-12
    local_pass = row["max_local_required_c"] <= local_c + 1e-12
    if global_pass and local_pass:
        verdict = "EnvelopePass"
    elif not local_pass:
        verdict = "SAEEndpointCandidate"
    else:
        verdict = "GlobalConstantGap"
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "geom_count": row["geom_count"],
        "bs_scale": row["bs_scale"],
        "required_c_bs": row["required_c_bs"],
        "max_local_required_c": row["max_local_required_c"],
        "global_c": global_c,
        "local_c": local_c,
        "global_capacity": global_capacity,
        "global_pass": global_pass,
        "local_pass": local_pass,
        "verdict": verdict,
        "top_requirement": row["top_requirements"][0] if row["top_requirements"] else None,
    }


def print_table(rows: list[dict]) -> None:
    """输出验收表。"""
    print(
        "p block shift m geom bs_scale req_C max_local_C global_C local_C "
        "global_pass local_pass verdict top",
        flush=True,
    )
    for row in rows:
        top = row["top_requirement"]
        if top:
            top_text = (
                f"g{top['gap']}[{top['lower']},{top['upper']}]:"
                f"{top['actual']}/{top['scale']:.3f}/{top['required_c']:.3f}"
            )
        else:
            top_text = "NA"
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['geom_count']} {row['bs_scale']:.6f} {row['required_c_bs']:.6f} "
            f"{row['max_local_required_c']:.6f} {row['global_c']:.6f} {row['local_c']:.6f} "
            f"{row['global_pass']} {row['local_pass']} {row['verdict']} {top_text}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--global-c", type=float, default=1.5)
    parser.add_argument("--local-c", type=float, default=1.5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(
                acceptance_row(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    args.alpha,
                    args.num_primes,
                    args.global_c,
                    args.local_c,
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
