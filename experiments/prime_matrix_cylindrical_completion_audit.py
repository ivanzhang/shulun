#!/usr/bin/env python3
"""方阵圆柱斜线“完成/未完成”分解审计。

用法示例：
  python3 experiments/prime_matrix_cylindrical_completion_audit.py --p-list 23,101,499,997,1999 --format table
  python3 experiments/prime_matrix_cylindrical_completion_audit.py --max-p 200 --format json
"""

from __future__ import annotations

import argparse
import json
from array import array
from math import isqrt, log


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数列表。"""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for value in range(2, isqrt(limit) + 1):
        if sieve[value]:
            start = value * value
            sieve[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [idx for idx, flag in enumerate(sieve) if flag]


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def small_factor_table(p: int) -> array:
    """记录 n<p^2 的最小 <p 素因子；0 表示没有 <p 素因子。"""
    limit = p * p - 1
    spf = array("H", [0]) * (limit + 1)
    for prime in primes_upto(p - 1):
        start = prime * prime
        for value in range(start, limit + 1, prime):
            if spf[value] == 0:
                spf[value] = prime
    return spf


def row_completion_split(p: int, x: int, spf: array, sample_limit: int) -> dict:
    """分解第 x 个乘数行的已完成斜线覆盖、未完成斜线补洞与最终素数洞。"""
    completed_covered = 0
    incomplete_hit = 0
    final_holes = []
    incomplete_factors: dict[int, int] = {}

    for column in range(1, p):
        value = x * p + column
        factor = spf[value]
        if factor and factor <= x:
            completed_covered += 1
        elif factor and factor < p:
            incomplete_hit += 1
            incomplete_factors[factor] = incomplete_factors.get(factor, 0) + 1
        else:
            # 在 x<p 且 column<p 时，若没有 <p 因子，则 value 必为素数。
            final_holes.append({"column": column, "value": value})

    completed_holes = (p - 1) - completed_covered
    top_incomplete = sorted(
        incomplete_factors.items(),
        key=lambda item: (-item[1], item[0]),
    )[:sample_limit]
    return {
        "x": x,
        "row": x + 1,
        "completed_primes_max": x,
        "completed_covered": completed_covered,
        "completed_holes": completed_holes,
        "incomplete_hit": incomplete_hit,
        "final_prime_holes": len(final_holes),
        "completion_margin": completed_holes - incomplete_hit,
        "final_hole_sample": final_holes[:sample_limit],
        "top_incomplete_factors": top_incomplete,
    }


def audit_p(p: int, sample_limit: int) -> dict:
    """审计单个 P 的圆柱完成分解。"""
    spf = small_factor_table(p)
    rows = [row_completion_split(p, x, spf, sample_limit) for x in range(1, p)]
    min_final = min(row["final_prime_holes"] for row in rows)
    min_margin = min(row["completion_margin"] for row in rows)
    min_completed_holes = min(row["completed_holes"] for row in rows)
    max_incomplete_hit = max(row["incomplete_hit"] for row in rows)
    best_rows = [
        row
        for row in rows
        if row["final_prime_holes"] == min_final
    ][:sample_limit]
    hard_rows = [
        row
        for row in rows
        if row["completion_margin"] <= 0 or row["final_prime_holes"] == 0
    ][:sample_limit]
    return {
        "p": p,
        "x_range": [1, p - 1],
        "row_count": len(rows),
        "min_final_prime_holes": min_final,
        "min_completion_margin": min_margin,
        "min_completed_holes": min_completed_holes,
        "max_incomplete_hit": max_incomplete_hit,
        "all_rows_positive": min_final > 0,
        "count_capacity_fail_rows": sum(1 for row in rows if row["completion_margin"] <= 0),
        "scale_p_over_log_p": p / log(p),
        "min_final_over_p_log": min_final / (p / log(p)),
        "best_rows": best_rows,
        "hard_rows": hard_rows,
    }


def audit(p_values: list[int], sample_limit: int) -> dict:
    """审计多个 P。"""
    available_primes = set(primes_upto(max(p_values) if p_values else 2))
    rows = []
    skipped = []
    for p in p_values:
        if p not in available_primes or p < 3:
            skipped.append(p)
            continue
        rows.append(audit_p(p, sample_limit))
    return {
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "status": "cylindrical_completion_sample_verified_global_open",
        "all_positive_in_sample": all(row["all_rows_positive"] for row in rows),
        "any_capacity_fail_rows": any(row["count_capacity_fail_rows"] for row in rows),
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "p rows min_final min_margin min_completed_holes max_incomplete_hit "
        "all_positive capacity_fail_rows min_final_over_p_log best_rows",
        flush=True,
    )
    for row in package["rows"]:
        best = ";".join(
            f"x={item['x']}:final={item['final_prime_holes']}:"
            f"low_holes={item['completed_holes']}:incomplete={item['incomplete_hit']}:"
            f"sample={item['final_hole_sample']}"
            for item in row["best_rows"]
        )
        print(
            f"{row['p']} {row['row_count']} {row['min_final_prime_holes']} "
            f"{row['min_completion_margin']} {row['min_completed_holes']} "
            f"{row['max_incomplete_hit']} {row['all_rows_positive']} "
            f"{row['count_capacity_fail_rows']} {row['min_final_over_p_log']:.6f} "
            f"{best}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="23,101,499,997,1999")
    parser.add_argument("--max-p", type=int, default=None)
    parser.add_argument("--sample-limit", type=int, default=5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    if args.max_p is not None:
        p_values = [p for p in primes_upto(args.max_p) if p >= 3]
    else:
        p_values = parse_p_list(args.p_list)
    package = audit(p_values, args.sample_limit)

    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
