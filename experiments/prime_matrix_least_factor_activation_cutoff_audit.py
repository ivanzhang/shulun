#!/usr/bin/env python3
"""最小因子激活截止审计。

用法示例：
  python3 experiments/prime_matrix_least_factor_activation_cutoff_audit.py --p-list 23,101,997 --format table

对 1<=x<=P 的行 n=xP+c，1<=c<P，任何合数 n 的最小素因子
不超过 sqrt(xP+P-1)。因此超过该截止的 q 斜线只可能是 shadow hit，
不能作为独立最小标签。
"""

from __future__ import annotations

import argparse
import json
from math import isqrt, log


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数列表。"""
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (
                ((limit - start) // value) + 1
            )
    return [idx for idx, flag in enumerate(flags) if flag]


def prime_sieve(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (
                ((limit - start) // value) + 1
            )
    return flags


def independent_residual_count(p: int, x: int, primes: list[int]) -> dict:
    """统计只用最小因子截止素数后的残洞。"""
    row_max = x * p + p - 1
    cutoff = isqrt(row_max)
    active = [prime for prime in primes if prime <= cutoff and prime < p]
    covered = bytearray(p)
    covered[0] = 1
    for prime in active:
        residue = (-x * p) % prime
        start = residue if residue != 0 else prime
        if start < p:
            covered[start:p:prime] = b"\x01" * (((p - 1 - start) // prime) + 1)
    residual = []
    for column in range(1, p):
        if not covered[column]:
            residual.append({"column": column, "value": x * p + column})
    return {
        "x": x,
        "row_max": row_max,
        "cutoff": cutoff,
        "active_prime_count": len(active),
        "active_largest": active[-1] if active else None,
        "residual_count": len(residual),
        "residual_sample": residual[:5],
    }


def audit_p(p: int, sample_limit: int) -> dict:
    """审计单个 P。"""
    primes = primes_upto(p - 1)
    prime_flags = prime_sieve(p * p + p)
    rows = []
    mismatch_rows = []
    for x in range(1, p + 1):
        row = independent_residual_count(p, x, primes)
        prime_count = sum(
            1 for column in range(1, p) if prime_flags[x * p + column]
        )
        row["prime_count"] = prime_count
        row["residual_equals_prime_count"] = row["residual_count"] == prime_count
        if row["residual_count"] != prime_count:
            mismatch_rows.append(row)
        rows.append(row)
    min_residual = min(row["residual_count"] for row in rows)
    weakest = [row for row in rows if row["residual_count"] == min_residual][
        :sample_limit
    ]
    min_active = min(row["active_prime_count"] for row in rows)
    max_active = max(row["active_prime_count"] for row in rows)
    return {
        "p": p,
        "row_count": len(rows),
        "basis_prime_count": len(primes),
        "active_prime_count_range": [min_active, max_active],
        "min_residual": min_residual,
        "weakest_rows": weakest,
        "all_residuals_equal_prime_counts": not mismatch_rows,
        "mismatch_rows": mismatch_rows[:sample_limit],
        "scale_p_over_log_p": p / log(p),
        "min_residual_over_scale": min_residual / (p / log(p)),
    }


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def audit(p_values: list[int], sample_limit: int) -> dict:
    """执行审计。"""
    prime_set = set(primes_upto(max(p_values) if p_values else 2))
    rows = []
    skipped = []
    for p in p_values:
        if p not in prime_set or p < 3:
            skipped.append(p)
            continue
        rows.append(audit_p(p, sample_limit))
    return {
        "status": "least_factor_activation_cutoff_exact_identity",
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "p basis active_range min_residual min_over_p_log exact weakest_rows",
        flush=True,
    )
    for row in package["rows"]:
        weakest = ";".join(
            f"x={item['x']}:cutoff={item['cutoff']}:active={item['active_prime_count']}:"
            f"res={item['residual_count']}:sample={item['residual_sample']}"
            for item in row["weakest_rows"]
        )
        print(
            f"{row['p']} {row['basis_prime_count']} {row['active_prime_count_range']} "
            f"{row['min_residual']} {row['min_residual_over_scale']:.6f} "
            f"{row['all_residuals_equal_prime_counts']} {weakest}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="23,101,499,997,1999")
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
