#!/usr/bin/env python3
"""AlphaTail 跨点锚点热门差值审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_hot_difference_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
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


def high_prime_reuse(shift: int, difference: int, high_primes: list[int]) -> list[int]:
    """返回可锚住差值 s 的高素数 q，即 q|s(s-r)(s+r)。"""
    if difference in {0, shift, -shift}:
        return []
    value = difference * (difference - shift) * (difference + shift)
    return [prime for prime in high_primes if value % prime == 0]


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, low_cutoff: int) -> dict:
    """审计单个 p:B:r 的热门差值。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift)
    domain_stop = min(2 * block, 2 * block - shift)
    max_value = max(domain_stop, domain_stop + shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    high_primes = [prime for prime in primes if prime > low_cutoff and shift % prime != 0]
    values: list[int] = []
    for value in range(domain_start, domain_stop + 1):
        left = squarefree_support(value, primes)
        if left is None:
            continue
        right = squarefree_support(value + shift, primes)
        if right is None:
            continue
        values.append(value)

    diff_counts: dict[int, int] = defaultdict(int)
    for left in values:
        for right in values:
            if left != right:
                diff_counts[left - right] += 1

    rows = []
    resonant_counts = {
        "s=0": diff_counts.get(0, 0),
        "s=r": diff_counts.get(shift, 0),
        "s=-r": diff_counts.get(-shift, 0),
    }
    max_reuse = 0
    for difference, count in diff_counts.items():
        if difference in {0, shift, -shift}:
            continue
        anchors = high_prime_reuse(shift, difference, high_primes)
        reuse = len(anchors)
        max_reuse = max(max_reuse, reuse)
        if reuse:
            rows.append(
                {
                    "s": difference,
                    "pair_count": count,
                    "reuse": reuse,
                    "anchors": anchors,
                    "pressure": count * reuse,
                }
            )
    rows.sort(key=lambda item: (-item["pressure"], -item["reuse"], -item["pair_count"], abs(item["s"])))
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "R": low_cutoff,
        "pair_support": len(values),
        "diff_support": len(diff_counts),
        "resonant_counts": resonant_counts,
        "active_hot_diffs": len(rows),
        "max_reuse": max_reuse,
        "top": rows[:12],
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
    parser.add_argument("--R", type=int, default=31)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha, args.R)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print(
            "p block shift R pairs diff_support s_eq_r s_eq_minus_r hot_diffs max_reuse top_s top_pairs top_reuse top_pressure",
            flush=True,
        )
        for audit in audits:
            top = audit["top"][0] if audit["top"] else {"s": 0, "pair_count": 0, "reuse": 0, "pressure": 0}
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['R']} "
                f"{audit['pair_support']} {audit['diff_support']} "
                f"{audit['resonant_counts']['s=r']} {audit['resonant_counts']['s=-r']} "
                f"{audit['active_hot_diffs']} "
                f"{audit['max_reuse']} {top['s']} {top['pair_count']} {top['reuse']} {top['pressure']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
