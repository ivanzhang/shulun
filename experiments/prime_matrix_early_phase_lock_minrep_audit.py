#!/usr/bin/env python3
"""早期相位锁与首零行最小代表审计。

用法示例：
  python3 experiments/prime_matrix_early_phase_lock_minrep_audit.py --format table

该脚本把“任意相位是否能覆盖”和“实际小代表元相位何时首次覆盖”并列，
用于定位 P=13 起全周期可有零行、但 P 行以内仍无零行的原因。
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_line_activation_cover_audit import audit, parse_p_list


def factorize(value: int | None) -> list[tuple[int, int]] | None:
    """朴素分解。"""
    if value is None:
        return None
    factors: list[tuple[int, int]] = []
    rest = value
    divisor = 2
    while divisor * divisor <= rest:
        if rest % divisor == 0:
            exponent = 0
            while rest % divisor == 0:
                rest //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1 if divisor == 2 else 2
    if rest > 1:
        factors.append((rest, 1))
    return factors


def build_package(p_values: list[int], scan_limit: int, sample_limit: int) -> dict:
    """生成相位锁摘要。"""
    base = audit(p_values, scan_limit, sample_limit)
    rows = []
    for item in base["rows"]:
        first_row = item["first_zero"]["first_zero_row"]
        multiplier = item["first_zero"]["first_zero_multiplier"]
        capacity_row = item["first_cover_capacity_row_with_activated_lines"]
        rows.append(
            {
                "p": item["p"],
                "basis_primes": item["basis_primes"],
                "arbitrary_cover_possible": item[
                    "full_basis_arbitrary_cover_possible"
                ],
                "all_lines_activated_row": item["all_lines_activated_row"],
                "first_arbitrary_capacity_row": capacity_row,
                "early_zero_count": len(item["early_zero_rows"]),
                "min_early_uncovered": item["min_early_uncovered"],
                "first_zero_row": first_row,
                "first_zero_multiplier": multiplier,
                "first_zero_exact_full_period": item["first_zero"][
                    "exact_full_period"
                ],
                "first_zero_row_factorization": factorize(first_row),
                "first_zero_multiplier_factorization": factorize(multiplier),
                "row_over_p": None if first_row is None else first_row / item["p"],
                "row_over_p2": (
                    None if first_row is None else first_row / (item["p"] * item["p"])
                ),
                "phase_lock_gap_from_capacity": (
                    None
                    if first_row is None or capacity_row is None
                    else first_row - capacity_row
                ),
            }
        )
    return {
        "status": "early_phase_lock_minrep_audit_not_a_proof",
        "scan_limit": scan_limit,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "p arbitrary_cover all_activated capacity_row early_zero min_early_holes "
        "first_zero exact row_factor x_factor row_over_p row_over_p2 lock_gap",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['arbitrary_cover_possible']} "
            f"{row['all_lines_activated_row']} {row['first_arbitrary_capacity_row']} "
            f"{row['early_zero_count']} {row['min_early_uncovered']} "
            f"{row['first_zero_row']} {row['first_zero_exact_full_period']} "
            f"{row['first_zero_row_factorization']} "
            f"{row['first_zero_multiplier_factorization']} "
            f"{row['row_over_p']} {row['row_over_p2']} "
            f"{row['phase_lock_gap_from_capacity']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="3,5,7,11,13,17,19,23,29")
    parser.add_argument("--scan-limit", type=int, default=300000)
    parser.add_argument("--sample-limit", type=int, default=4)
    parser.add_argument("--format", choices=("json", "table"), default="table")
    args = parser.parse_args()
    package = build_package(
        parse_p_list(args.p_list), args.scan_limit, args.sample_limit
    )
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    print_table(package)


if __name__ == "__main__":
    main()
