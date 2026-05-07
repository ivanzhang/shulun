#!/usr/bin/env python3
"""未完成高素斜线补洞的缺口坐标审计。

用法示例：
  python3 experiments/prime_matrix_incomplete_filler_deficit_audit.py --p-list 997,1999,5003 --format table
"""

from __future__ import annotations

import argparse
import json
from array import array
from math import isqrt

from prime_matrix_cylindrical_completion_audit import (
    primes_upto,
    row_completion_split,
    small_factor_table,
)


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def incomplete_hits_for_row(p: int, x: int, spf: array, sample_limit: int) -> dict:
    """列出第 x 行中由未完成高素斜线补掉的骨架残洞。"""
    h = p - x
    split = row_completion_split(p, x, spf, sample_limit)
    hits = []
    for column in range(1, p):
        value = x * p + column
        factor = spf[value]
        if not (factor and x < factor < p):
            continue
        cofactor = value // factor
        row = {
            "column": column,
            "value": value,
            "q": factor,
            "m": cofactor,
            "h": h,
            "a": p - factor,
            "b": p - cofactor if cofactor < p else None,
            "cofactor_below_p": cofactor < p,
        }
        if row["b"] is not None:
            row["deficit_sum"] = row["a"] + row["b"]
            row["deficit_error"] = h - row["deficit_sum"]
            row["ab"] = row["a"] * row["b"]
            row["column_minus_ab"] = column - row["ab"]
            row["clean_pair_identity"] = row["deficit_sum"] == h and column == row["ab"]
        else:
            row["deficit_sum"] = None
            row["deficit_error"] = None
            row["ab"] = None
            row["column_minus_ab"] = None
            row["clean_pair_identity"] = False
        hits.append(row)
    return {
        "x": x,
        "h": h,
        "completed_holes": split["completed_holes"],
        "final_prime_holes": split["final_prime_holes"],
        # a 与 h-a 给出同一列；当 h 为偶数时，a=h/2 的高素平方也要计入。
        "pair_column_bound": h // 2,
        "pair_bound_margin": split["completed_holes"] - (h // 2),
        "hit_count": len(hits),
        "all_cofactor_below_p": all(hit["cofactor_below_p"] for hit in hits),
        "all_clean_pair_identity": all(hit["clean_pair_identity"] for hit in hits),
        "sample_hits": hits[:sample_limit],
    }


def audit_p(p: int, sample_limit: int) -> dict:
    """审计单个 P 的底部缺口带。"""
    spf = small_factor_table(p)
    sqrt_p = isqrt(p)
    bottom_rows = list(range(max(1, p - sqrt_p + 1), p))
    rows = [incomplete_hits_for_row(p, x, spf, sample_limit) for x in bottom_rows]
    hit_rows = [row for row in rows if row["hit_count"] > 0]
    max_hit = max((row["hit_count"] for row in rows), default=0)
    min_pair_margin = min((row["pair_bound_margin"] for row in rows), default=None)
    weakest_pair_rows = [
        row for row in rows if row["pair_bound_margin"] == min_pair_margin
    ][:sample_limit]
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "bottom_band": [bottom_rows[0] if bottom_rows else None, bottom_rows[-1] if bottom_rows else None],
        "bottom_row_count": len(bottom_rows),
        "hit_row_count": len(hit_rows),
        "max_incomplete_hits": max_hit,
        "min_pair_bound_margin": min_pair_margin,
        "all_pair_bound_positive": min_pair_margin is not None and min_pair_margin > 0,
        "all_hits_cofactor_below_p": all(row["all_cofactor_below_p"] for row in rows),
        "all_hits_clean_pair_identity": all(row["all_clean_pair_identity"] for row in rows),
        "sample_hit_rows": hit_rows[:sample_limit],
        "weakest_pair_rows": weakest_pair_rows,
    }


def audit(p_values: list[int], sample_limit: int) -> dict:
    """审计多个 P。"""
    prime_set = set(primes_upto(max(p_values) if p_values else 2))
    rows = []
    skipped = []
    for p in p_values:
        if p not in prime_set or p < 3:
            skipped.append(p)
            continue
        rows.append(audit_p(p, sample_limit))
    return {
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "status": "incomplete_filler_deficit_sample_verified_global_open",
        "all_clean_pair_identity": all(row["all_hits_clean_pair_identity"] for row in rows),
        "all_pair_bound_positive": all(row["all_pair_bound_positive"] for row in rows),
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "p sqrt_p band row_count hit_rows max_hits min_pair_margin pair_bound_positive "
        "cofactor_below_p clean_pair_identity weakest_pair_rows sample_hit_rows",
        flush=True,
    )
    for row in package["rows"]:
        samples = ";".join(
            f"x={item['x']}:h={item['h']}:hits={item['hit_count']}:sample={item['sample_hits']}"
            for item in row["sample_hit_rows"]
        ) or "none"
        weakest = ";".join(
            f"x={item['x']}:h={item['h']}:R={item['completed_holes']}:"
            f"pair_bound={item['pair_column_bound']}:margin={item['pair_bound_margin']}:"
            f"final={item['final_prime_holes']}"
            for item in row["weakest_pair_rows"]
        ) or "none"
        print(
            f"{row['p']} {row['sqrt_p']} {row['bottom_band']} {row['bottom_row_count']} "
            f"{row['hit_row_count']} {row['max_incomplete_hits']} "
            f"{row['min_pair_bound_margin']} {row['all_pair_bound_positive']} "
            f"{row['all_hits_cofactor_below_p']} {row['all_hits_clean_pair_identity']} "
            f"{weakest} {samples}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="997,1999,5003")
    parser.add_argument("--sample-limit", type=int, default=5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()
    package = audit(parse_p_list(args.p_list), args.sample_limit)
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
