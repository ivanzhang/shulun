#!/usr/bin/env python3
"""AlphaTail 多点共振压力预算审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_resonance_budget_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
"""

from __future__ import annotations

import argparse
import json
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def squarefree_support(value: int, small_primes: list[int]) -> set[int] | None:
    """返回 y-smooth squarefree 数的素因子支撑；否则返回 None。"""
    remaining = value
    support: set[int] = set()
    for prime in small_primes:
        if prime > remaining:
            break
        if remaining % prime != 0:
            continue
        remaining //= prime
        support.add(prime)
        if remaining % prime == 0:
            return None
    if remaining != 1:
        return None
    return support


def chain_values(prime_bound: int, block: int, shift: int, alpha: float, point_count: int) -> list[int]:
    """返回 m 点 y-smooth squarefree 链起点。"""
    cutoff = int(alpha * prime_bound)
    starts = [block + 1 - index * shift for index in range(point_count)]
    stops = [2 * block - index * shift for index in range(point_count)]
    domain_start = max(starts)
    domain_stop = min(stops)
    max_value = max(domain_stop + index * shift for index in range(point_count))
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    values: list[int] = []
    for value in range(domain_start, domain_stop + 1):
        if all(squarefree_support(value + index * shift, primes) is not None for index in range(point_count)):
            values.append(value)
    return values


def diff_count(values: list[int], difference: int) -> int:
    """计算有序差值对数量。"""
    value_set = set(values)
    return sum(1 for value in values if value - difference in value_set)


def audit_item(prime_bound: int, block: int, shift: int, alpha: float) -> dict:
    """审计单个 p:B:r 的共振预算恒等式。"""
    t3_values = chain_values(prime_bound, block, shift, alpha, 3)
    t4_values = chain_values(prime_bound, block, shift, alpha, 4)
    t5_values = chain_values(prime_bound, block, shift, alpha, 5)
    t3 = len(t3_values)
    t4 = len(t4_values)
    t5 = len(t5_values)
    resonant_r = diff_count(t3_values, shift) + diff_count(t3_values, -shift)
    resonant_2r = diff_count(t3_values, 2 * shift) + diff_count(t3_values, -2 * shift)
    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "shift": shift,
        "T3": t3,
        "T4": t4,
        "T5": t5,
        "resonant_r": resonant_r,
        "resonant_2r": resonant_2r,
        "resonance_capacity": 2 * t4 + 2 * t5,
        "identity_ok": resonant_r == 2 * t4 and resonant_2r == 2 * t5,
        "T4_over_T3": t4 / t3 if t3 else 0.0,
        "T5_over_T3": t5 / t3 if t3 else 0.0,
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


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block shift T3 T4 T5 res_r res_2r res_cap T4_T3 T5_T3 identity", flush=True)
        for audit in audits:
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} "
                f"{audit['T3']} {audit['T4']} {audit['T5']} "
                f"{audit['resonant_r']} {audit['resonant_2r']} {audit['resonance_capacity']} "
                f"{audit['T4_over_T3']:.6f} {audit['T5_over_T3']:.6f} {audit['identity_ok']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
