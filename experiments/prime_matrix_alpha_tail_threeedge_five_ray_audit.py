#!/usr/bin/env python3
"""AlphaTail ThreeEdge 五射线热门差值审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_threeedge_five_ray_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
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


def high_prime_reuse_five_ray(shift: int, difference: int, high_primes: list[int]) -> list[int]:
    """返回可锚住差值 s 的高素数 q，即 q|s(s±r)(s±2r)。"""
    if difference in {0, shift, -shift, 2 * shift, -2 * shift}:
        return []
    value = (
        difference
        * (difference - shift)
        * (difference + shift)
        * (difference - 2 * shift)
        * (difference + 2 * shift)
    )
    return [prime for prime in high_primes if value % prime == 0]


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, low_cutoff: int) -> dict:
    """审计单个 p:B:r 的五射线差值账本。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift, block + 1 - 2 * shift)
    domain_stop = min(2 * block, 2 * block - shift, 2 * block - 2 * shift)
    max_value = max(domain_stop, domain_stop + shift, domain_stop + 2 * shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    high_primes = [prime for prime in primes if prime > low_cutoff and shift % prime != 0]
    values: list[int] = []
    for value in range(domain_start, domain_stop + 1):
        supports = [
            squarefree_support(value, primes),
            squarefree_support(value + shift, primes),
            squarefree_support(value + 2 * shift, primes),
        ]
        if any(support is None for support in supports):
            continue
        values.append(value)

    diff_counts: dict[int, int] = defaultdict(int)
    for left in values:
        for right in values:
            if left != right:
                diff_counts[left - right] += 1

    resonant_counts = {
        "s=0": diff_counts.get(0, 0),
        "s=r": diff_counts.get(shift, 0),
        "s=-r": diff_counts.get(-shift, 0),
        "s=2r": diff_counts.get(2 * shift, 0),
        "s=-2r": diff_counts.get(-2 * shift, 0),
    }
    rows = []
    max_reuse = 0
    for difference, count in diff_counts.items():
        if difference in {0, shift, -shift, 2 * shift, -2 * shift}:
            continue
        anchors = high_prime_reuse_five_ray(shift, difference, high_primes)
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
        "chains": len(values),
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
            "p block shift R chains diff_support s_eq_r s_eq_minus_r s_eq_2r s_eq_minus_2r hot_diffs max_reuse top_s top_pairs top_reuse top_pressure",
            flush=True,
        )
        for audit in audits:
            top = audit["top"][0] if audit["top"] else {"s": 0, "pair_count": 0, "reuse": 0, "pressure": 0}
            resonant = audit["resonant_counts"]
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['R']} "
                f"{audit['chains']} {audit['diff_support']} "
                f"{resonant['s=r']} {resonant['s=-r']} {resonant['s=2r']} {resonant['s=-2r']} "
                f"{audit['active_hot_diffs']} {audit['max_reuse']} "
                f"{top['s']} {top['pair_count']} {top['reuse']} {top['pressure']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
