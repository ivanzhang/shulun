#!/usr/bin/env python3
"""审计素因子斜线的平方激活与早期零行覆盖。

用法示例：
  python3 experiments/prime_matrix_line_activation_cover_audit.py --p-list 11,13,17,19,23 --format table

核心区分：
1. q^2 之前，q 的命中是 shadow hit；若 q|n<q^2，则 n 还有更小因子。
2. q^2 之后，q 才可能作为最小素因子给出独立覆盖标签。
3. 即使所有 q<P 已激活，完整覆盖仍需实际行相位同时对齐。
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import isqrt, prod


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


def factorize(value: int) -> list[tuple[int, int]]:
    """朴素分解，样本规模足够。"""
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


def row_cover_mask(p: int, row: int, basis: list[int]) -> int:
    """计算一编号 row 的非平凡列覆盖掩码。"""
    mask = 0
    x = row - 1
    for column in range(1, p):
        value = x * p + column
        if any(value % prime == 0 for prime in basis):
            mask |= 1 << (column - 1)
    return mask


def cover_sets_for_primes(p: int, primes: list[int]) -> dict[int, list[int]]:
    """列出每个素数的一切可选列残基覆盖掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in primes:
        options = []
        for residue in range(prime):
            mask = 0
            for column in range(1, p):
                if column % prime == residue:
                    mask |= 1 << (column - 1)
            options.append(mask)
        masks[prime] = options
    return masks


def arbitrary_phase_cover_possible(p: int, primes: list[int]) -> dict:
    """判断给定素数集合的一残基类任意相位是否可覆盖所有列。"""
    full_mask = (1 << (p - 1)) - 1
    if not primes:
        return {
            "possible": full_mask == 0,
            "max_covered": 0,
            "uncovered_columns": list(range(1, p)),
            "witness_residues": {},
        }
    options = cover_sets_for_primes(p, primes)
    states: dict[int, dict[int, int]] = {0: {}}
    for prime in primes:
        next_states: dict[int, dict[int, int]] = {}
        for mask, residues in states.items():
            for residue, option in enumerate(options[prime]):
                new_mask = mask | option
                if new_mask not in next_states:
                    new_residues = dict(residues)
                    new_residues[prime] = residue
                    next_states[new_mask] = new_residues
        states = next_states
        if full_mask in states:
            return {
                "possible": True,
                "max_covered": p - 1,
                "uncovered_columns": [],
                "witness_residues": states[full_mask],
            }
    best_mask = max(states, key=lambda item: item.bit_count())
    uncovered = [
        column
        for column in range(1, p)
        if not (best_mask & (1 << (column - 1)))
    ]
    return {
        "possible": False,
        "max_covered": best_mask.bit_count(),
        "uncovered_columns": uncovered,
        "witness_residues": states[best_mask],
    }


def first_zero_row(p: int, scan_limit: int | None) -> dict:
    """扫描首个完整 CRT 零行；小周期可全周期严格扫描。"""
    basis = primes_upto(p - 1)
    period = prod(basis) if basis else 1
    limit = period if scan_limit is None else min(period, scan_limit)
    full_mask = (1 << (p - 1)) - 1
    first = None
    for row in range(1, limit + 1):
        if row_cover_mask(p, row, basis) == full_mask:
            first = row
            break
    return {
        "period": period,
        "scan_limit": limit,
        "exact_full_period": limit == period,
        "first_zero_row": first,
        "first_zero_multiplier": None if first is None else first - 1,
    }


def zero_row_profile(p: int, row: int | None, sample_limit: int) -> dict | None:
    """分析首零行的最小标签与平方激活情况。"""
    if row is None:
        return None
    basis = primes_upto(p - 1)
    x = row - 1
    columns = []
    min_label_hist: dict[int, int] = {}
    shadow_factor_uses = 0
    independent_min_uses = 0
    for column in range(1, p):
        value = x * p + column
        factors = [prime for prime in basis if value % prime == 0]
        min_label = min(factors) if factors else None
        if min_label is not None:
            min_label_hist[min_label] = min_label_hist.get(min_label, 0) + 1
            if value >= min_label * min_label:
                independent_min_uses += 1
        for prime in factors:
            if value < prime * prime:
                shadow_factor_uses += 1
        columns.append(
            {
                "column": column,
                "value": value,
                "factors_lt_p": factors,
                "factorization": factorize(value),
                "min_label": min_label,
                "min_label_activated": (
                    None if min_label is None else value >= min_label * min_label
                ),
            }
        )
    return {
        "row": row,
        "multiplier": x,
        "interval": [x * p + 1, x * p + p - 1],
        "min_label_hist": min_label_hist,
        "independent_min_uses": independent_min_uses,
        "shadow_factor_uses": shadow_factor_uses,
        "columns_sample": columns[:sample_limit],
    }


def audit_p(p: int, scan_limit: int | None, sample_limit: int) -> dict:
    """审计单个 P。"""
    basis = primes_upto(p - 1)
    full_basis_cover = arbitrary_phase_cover_possible(p, basis)
    activation_rows = {
        prime: (prime * prime + p - 1) // p
        for prime in basis
    }
    early_rows = []
    for row in range(1, p + 1):
        activated = [prime for prime in basis if activation_rows[prime] <= row]
        arbitrary = arbitrary_phase_cover_possible(p, activated)
        actual_mask = row_cover_mask(p, row, basis)
        uncovered = [
            column
            for column in range(1, p)
            if not (actual_mask & (1 << (column - 1)))
        ]
        early_rows.append(
            {
                "row": row,
                "activated_primes": activated,
                "all_primes_activated": len(activated) == len(basis),
                "arbitrary_activated_cover_possible": arbitrary["possible"],
                "arbitrary_activated_max_covered": arbitrary["max_covered"],
                "actual_uncovered_count": len(uncovered),
                "actual_uncovered_sample": uncovered[:sample_limit],
            }
        )
    first_cover_capacity_row = next(
        (
            row["row"]
            for row in early_rows
            if row["arbitrary_activated_cover_possible"]
        ),
        None,
    )
    all_lines_activated_row = max(activation_rows.values()) if activation_rows else None
    first_zero = first_zero_row(p, scan_limit)
    return {
        "p": p,
        "basis_primes": basis,
        "period": first_zero["period"],
        "full_basis_arbitrary_cover_possible": full_basis_cover["possible"],
        "full_basis_max_covered": full_basis_cover["max_covered"],
        "full_basis_uncovered_columns": full_basis_cover["uncovered_columns"],
        "all_lines_activated_row": all_lines_activated_row,
        "first_cover_capacity_row_with_activated_lines": first_cover_capacity_row,
        "early_zero_rows": [
            row for row in early_rows if row["actual_uncovered_count"] == 0
        ],
        "min_early_uncovered": min(row["actual_uncovered_count"] for row in early_rows),
        "early_rows": early_rows,
        "first_zero": first_zero,
        "first_zero_profile": zero_row_profile(
            p, first_zero["first_zero_row"], sample_limit
        ),
    }


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def audit(p_values: list[int], scan_limit: int | None, sample_limit: int) -> dict:
    """执行审计。"""
    prime_set = set(primes_upto(max(p_values) if p_values else 2))
    rows = []
    skipped = []
    for p in p_values:
        if p not in prime_set or p < 3:
            skipped.append(p)
            continue
        rows.append(audit_p(p, scan_limit, sample_limit))
    return {
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "status": "line_activation_cover_audit_not_a_proof",
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出简表。"""
    print(
        "p basis period arbitrary_cover all_activated_row first_capacity_row "
        "early_zero_count min_early_uncovered first_zero exact min_label_hist",
        flush=True,
    )
    for row in package["rows"]:
        profile = row["first_zero_profile"] or {}
        print(
            f"{row['p']} {row['basis_primes']} {row['period']} "
            f"{row['full_basis_arbitrary_cover_possible']} "
            f"{row['all_lines_activated_row']} "
            f"{row['first_cover_capacity_row_with_activated_lines']} "
            f"{len(row['early_zero_rows'])} {row['min_early_uncovered']} "
            f"{row['first_zero']['first_zero_row']} "
            f"{row['first_zero']['exact_full_period']} "
            f"{profile.get('min_label_hist')}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="3,5,7,11,13,17,19,23,29")
    parser.add_argument("--scan-limit", type=int, default=300000)
    parser.add_argument("--sample-limit", type=int, default=8)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()
    package = audit(parse_p_list(args.p_list), args.scan_limit, args.sample_limit)
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
