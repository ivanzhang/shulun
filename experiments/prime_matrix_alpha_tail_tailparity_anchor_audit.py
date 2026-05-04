#!/usr/bin/env python3
"""AlphaTail TailParity 首个高素因子锚点审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailparity_anchor_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
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


def psi_value(left: set[int], right: set[int], shift: int, prime: int) -> int:
    """计算局部 psi。"""
    if shift % prime == 0:
        return 1
    return -1 if (prime in left or prime in right) else 1


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, low_cutoff: int) -> dict:
    """审计单个 p:B:r 的 TailParity 锚点贡献。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift)
    domain_stop = min(2 * block, 2 * block - shift)
    max_value = max(domain_stop, domain_stop + shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    low_primes = [prime for prime in primes if prime <= low_cutoff]
    tail_primes = [prime for prime in primes if prime > low_cutoff]
    anchor_contrib: dict[int, int] = defaultdict(int)
    total_tail = 0
    pair_count = 0
    for value in range(domain_start, domain_stop + 1):
        left = squarefree_support(value, primes)
        if left is None:
            continue
        right = squarefree_support(value + shift, primes)
        if right is None:
            continue
        pair_count += 1
        low_value = 1
        for prime in low_primes:
            low_value *= psi_value(left, right, shift, prime)
        prefix = 1
        pair_tail = 0
        for prime in tail_primes:
            local = psi_value(left, right, shift, prime)
            increment = (local - 1) * prefix
            if increment:
                contribution = low_value * increment
                anchor_contrib[prime] += contribution
                pair_tail += contribution
            prefix *= local
        total_tail += low_value * (prefix - 1)
        if pair_tail != low_value * (prefix - 1):
            raise AssertionError("telescoping mismatch")
    top_abs = sorted(anchor_contrib.items(), key=lambda item: (-abs(item[1]), item[0]))[:12]
    top_pos = sorted(anchor_contrib.items(), key=lambda item: (-item[1], item[0]))[:12]
    top_neg = sorted(anchor_contrib.items(), key=lambda item: (item[1], item[0]))[:12]
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "R": low_cutoff,
        "pair_count": pair_count,
        "tail_prime_count": len(tail_primes),
        "total_tail": total_tail,
        "top_abs": top_abs,
        "top_pos": top_pos,
        "top_neg": top_neg,
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
        print("p block shift R pairs tail total_top_abs_q total_top_abs_value", flush=True)
        for audit in audits:
            top_q, top_value = audit["top_abs"][0] if audit["top_abs"] else (0, 0)
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['R']} "
                f"{audit['pair_count']} {audit['total_tail']} {top_q} {top_value}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
