#!/usr/bin/env python3
"""AlphaTail 高块 CoreLoad 的互补因子审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_cofactor_audit.py --selected 997:4096,5003:8192 --format table

这里 `p:B` 表示审计 dyadic 高块 B<d<=2B。
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def factor_low_primes(value: int, primes: list[int]) -> list[int]:
    """返回 value 的低素数平方自由支撑。"""
    factors: list[int] = []
    for prime in primes:
        if prime > value:
            break
        if value % prime == 0:
            factors.append(prime)
            while value % prime == 0:
                value //= prime
        if value == 1:
            break
    return factors


def enumerate_block_divisors(factors: list[int], block: int) -> list[tuple[int, int]]:
    """枚举由 factors 生成且落在 B<d<=2B 的平方自由除数及 Möbius 符号。"""
    records: list[tuple[int, int]] = []

    def visit(index: int, product: int, parity: int) -> None:
        if product > 2 * block:
            return
        if index == len(factors):
            if block < product <= 2 * block:
                records.append((product, -1 if parity % 2 else 1))
            return
        visit(index + 1, product, parity)
        visit(index + 1, product * factors[index], parity + 1)

    visit(0, 1, 0)
    return records


def harmonic_models(cutoff: int, block: int) -> dict[str, float]:
    """计算 dyadic 块中的正/负 Möbius harmonic 模型量。"""
    allowed = primes_upto(cutoff)
    allowed_set = set(allowed)
    plus = 0.0
    minus = 0.0
    for value in range(block + 1, 2 * block + 1):
        remaining = value
        omega = 0
        ok = True
        for prime in allowed:
            if prime * prime > remaining:
                break
            if remaining % prime != 0:
                continue
            remaining //= prime
            omega += 1
            if remaining % prime == 0:
                ok = False
                break
        if not ok:
            continue
        if remaining > 1:
            if remaining not in allowed_set:
                continue
            omega += 1
        if omega % 2:
            minus += 1 / value
        else:
            plus += 1 / value
    return {"plus": plus, "minus": minus}


def audit_pair(prime_bound: int, block: int, alpha: float) -> dict:
    """审计单个 p:B。"""
    cutoff = int(alpha * prime_bound)
    low_primes = primes_upto(cutoff)
    height = prime_bound - 1
    plus_hits = 0
    minus_hits = 0
    plus_col_loads: dict[int, int] = {}
    minus_col_loads: dict[int, int] = {}
    plus_m_loads: dict[int, int] = defaultdict(int)
    minus_m_loads: dict[int, int] = defaultdict(int)

    for column in range(1, height + 1):
        value = prime_bound * prime_bound + column
        factors = factor_low_primes(value, low_primes)
        plus_column = 0
        minus_column = 0
        for divisor, mu in enumerate_block_divisors(factors, block):
            cofactor = value // divisor
            if mu > 0:
                plus_hits += 1
                plus_column += 1
                plus_m_loads[cofactor] += 1
            else:
                minus_hits += 1
                minus_column += 1
                minus_m_loads[cofactor] += 1
        if plus_column:
            plus_col_loads[column] = plus_column
        if minus_column:
            minus_col_loads[column] = minus_column

    models = harmonic_models(cutoff, block)
    plus_model = height * models["plus"]
    minus_model = height * models["minus"]

    def top_items(loads: dict[int, int], limit: int = 8) -> list[tuple[int, int]]:
        return sorted(loads.items(), key=lambda item: (-item[1], item[0]))[:limit]

    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "high_block": block > height,
        "cofactor_band": [
            (prime_bound * prime_bound) / (2 * block),
            (prime_bound * prime_bound + height) / block,
        ],
        "plus_hits": plus_hits,
        "plus_model": plus_model,
        "plus_gap": plus_hits - plus_model,
        "minus_hits": minus_hits,
        "minus_model": minus_model,
        "minus_gap": minus_hits - minus_model,
        "max_plus_column_load": max(plus_col_loads.values(), default=0),
        "max_minus_column_load": max(minus_col_loads.values(), default=0),
        "max_plus_cofactor_load": max(plus_m_loads.values(), default=0),
        "max_minus_cofactor_load": max(minus_m_loads.values(), default=0),
        "plus_column_support": len(plus_col_loads),
        "minus_column_support": len(minus_col_loads),
        "plus_cofactor_support": len(plus_m_loads),
        "minus_cofactor_support": len(minus_m_loads),
        "top_plus_cofactors": top_items(plus_m_loads),
        "top_minus_cofactors": top_items(minus_m_loads),
    }


def parse_selected(raw: str) -> list[tuple[int, int]]:
    """解析 p:B 逗号列表。"""
    pairs: list[tuple[int, int]] = []
    for part in raw.split(","):
        if not part.strip():
            continue
        prime_raw, block_raw = part.split(":", 1)
        pairs.append((int(prime_raw), int(block_raw)))
    return pairs


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096,5003:8192")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_pair(prime_bound, block, args.alpha)
        for prime_bound, block in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print(
            "p block high plus_gap minus_gap max_col_minus max_m_minus "
            "minus_col_support minus_m_support",
            flush=True,
        )
        for audit in audits:
            print(
                f"{audit['p']} {audit['block']} {audit['high_block']} "
                f"{audit['plus_gap']:.6f} {audit['minus_gap']:.6f} "
                f"{audit['max_minus_column_load']} {audit['max_minus_cofactor_load']} "
                f"{audit['minus_column_support']} {audit['minus_cofactor_support']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
