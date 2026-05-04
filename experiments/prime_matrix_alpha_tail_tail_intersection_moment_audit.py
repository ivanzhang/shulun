#!/usr/bin/env python3
"""AlphaTail 条件尾交集矩审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tail_intersection_moment_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from math import comb

from prime_matrix_alpha_tail_tail_overlap_rankin_audit import (
    audit_point_count,
    domain_bounds,
    local_zero_classes,
    primes_upto,
    z_bound,
)


def elementary_symmetric(values: list[float], max_order: int) -> list[float]:
    """计算 elementary symmetric sums e_0...e_max_order。"""
    sums = [0.0] * (max_order + 1)
    sums[0] = 1.0
    for value in values:
        for order in range(max_order, 0, -1):
            sums[order] += sums[order - 1] * value
    return sums


def actual_binomial_moments(hit_histogram: dict[int, int], max_order: int) -> list[int]:
    """由命中直方图计算 sum_d binom(h_T(d), t)。"""
    moments = [0] * (max_order + 1)
    moments[0] = sum(hit_histogram.values())
    for hit_count, frequency in hit_histogram.items():
        for order in range(1, max_order + 1):
            if hit_count >= order:
                moments[order] += frequency * comb(hit_count, order)
    return moments


def tail_densities(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> list[float]:
    """返回尾素事件的局部模型密度 b_q/q。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    z_value = z_bound(domain_start, domain_stop, shift, point_count)
    cutoff = int(alpha * prime_bound)
    large_primes = [prime for prime in primes_upto(z_value) if prime > cutoff]
    tail_primes = large_primes[num_primes:]
    return [local_zero_classes(point_count, shift, prime) / prime for prime in tail_primes]


def audit_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    max_order: int,
    rho: float,
) -> dict:
    """审计单个 p:B:r:m 的尾交集矩。"""
    overlap_row = audit_point_count(prime_bound, block, shift, point_count, alpha, num_primes, rho)
    densities = tail_densities(prime_bound, block, shift, point_count, alpha, num_primes)
    model_esym = elementary_symmetric(densities, max_order)
    actual_moments = actual_binomial_moments(
        {int(key): value for key, value in overlap_row["hit_histogram"].items()},
        max_order,
    )
    model_moments = [overlap_row["low_count"] * model_esym[order] for order in range(max_order + 1)]
    deviations = [actual_moments[order] - model_moments[order] for order in range(max_order + 1)]
    omega = overlap_row["overlap_excess"]
    pair_moment = actual_moments[2] if max_order >= 2 else 0
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "low_count": overlap_row["low_count"],
        "xi_tail": overlap_row["xi_tail"],
        "overlap_excess": omega,
        "pair_dominates_overlap": pair_moment >= omega,
        "actual_moments": actual_moments,
        "model_moments": model_moments,
        "deviations": deviations,
        "tail_prime_count": overlap_row["tail_prime_count"],
        "max_tail_hits": overlap_row["max_tail_hits"],
        "l_bound": overlap_row["l_bound"],
        "product_bound_ok": overlap_row["product_bound_ok"],
    }


def parse_selected(raw: str) -> list[tuple[int, int, int]]:
    """解析 p:B:r 逗号列表。"""
    items: list[tuple[int, int, int]] = []
    for part in raw.split(","):
        if not part.strip():
            continue
        prime_raw, block_raw, shift_raw = part.split(":", 2)
        items.append((int(prime_raw), int(block_raw), int(shift_raw)))
    return items


def print_table(rows: list[dict], max_order: int) -> None:
    """输出交集矩紧凑表格。"""
    headers = ["p", "block", "shift", "m", "omega", "Xi_tail"]
    for order in range(2, max_order + 1):
        headers.extend([f"M{order}", f"B{order}", f"D{order}"])
    headers.extend(["pair_ge_omega", "max_hit", "L_bound"])
    print(" ".join(headers), flush=True)
    for row in rows:
        parts = [
            str(row["p"]),
            str(row["block"]),
            str(row["shift"]),
            str(row["m"]),
            str(row["overlap_excess"]),
            f"{row['xi_tail']:.6f}",
        ]
        for order in range(2, max_order + 1):
            parts.extend(
                [
                    str(row["actual_moments"][order]),
                    f"{row['model_moments'][order]:.6f}",
                    f"{row['deviations'][order]:.6f}",
                ]
            )
        parts.extend(
            [
                str(row["pair_dominates_overlap"]),
                str(row["max_tail_hits"]),
                str(row["l_bound"]),
            ]
        )
        print(" ".join(parts), flush=True)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--rho", type=float, default=1.5)
    parser.add_argument("--max-order", type=int, default=4)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(
                audit_row(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    args.alpha,
                    args.num_primes,
                    args.max_order,
                    args.rho,
                )
            )
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows, args.max_order)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
