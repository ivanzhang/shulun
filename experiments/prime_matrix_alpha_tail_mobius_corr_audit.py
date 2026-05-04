#!/usr/bin/env python3
"""AlphaTail ShiftSmooth 的 Möbius 相关结构审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_mobius_corr_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
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


def audit_item(prime_bound: int, block: int, shift: int, alpha: float) -> dict:
    """审计单个 p:B:r 的 Möbius 相关结构。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift)
    domain_stop = min(2 * block, 2 * block - shift)
    max_value = max(domain_stop, domain_stop + shift, 0)
    small_primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    even_count = 0
    odd_count = 0
    total_common = 0
    total_exclusive = 0
    locked_common = 0
    unlocked_exclusive = 0
    pair_count = 0
    for value in range(domain_start, domain_stop + 1):
        left = squarefree_support(value, small_primes)
        if left is None:
            continue
        right = squarefree_support(value + shift, small_primes)
        if right is None:
            continue
        common = left & right
        exclusive = left ^ right
        pair_count += 1
        total_common += len(common)
        total_exclusive += len(exclusive)
        locked_common += sum(1 for prime in common if shift % prime == 0)
        unlocked_exclusive += sum(1 for prime in exclusive if shift % prime != 0)
        if len(exclusive) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "squarefree_pairs": pair_count,
        "even_symmetric_difference": even_count,
        "odd_symmetric_difference": odd_count,
        "mobius_correlation": even_count - odd_count,
        "avg_common": total_common / pair_count if pair_count else 0.0,
        "avg_exclusive": total_exclusive / pair_count if pair_count else 0.0,
        "locked_common": locked_common,
        "unlocked_exclusive": unlocked_exclusive,
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
        print("p block shift pairs even odd corr avg_common avg_exclusive locked_common", flush=True)
        for audit in audits:
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} "
                f"{audit['squarefree_pairs']} {audit['even_symmetric_difference']} "
                f"{audit['odd_symmetric_difference']} {audit['mobius_correlation']} "
                f"{audit['avg_common']:.6f} {audit['avg_exclusive']:.6f} "
                f"{audit['locked_common']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
