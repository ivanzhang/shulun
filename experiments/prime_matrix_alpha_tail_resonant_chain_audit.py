#!/usr/bin/env python3
"""AlphaTail 共振差值三点链审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_resonant_chain_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
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


def mobius_sign(support: set[int]) -> int:
    """由平方自由支撑返回 Möbius 符号。"""
    return -1 if len(support) % 2 else 1


def audit_item(prime_bound: int, block: int, shift: int, alpha: float) -> dict:
    """审计单个 p:B:r 的三点链。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift, block + 1 - 2 * shift)
    domain_stop = min(2 * block, 2 * block - shift, 2 * block - 2 * shift)
    max_value = max(domain_stop, domain_stop + shift, domain_stop + 2 * shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    chains = 0
    all_same_sign = 0
    alternating_sign = 0
    sign_sum_01 = 0
    sign_sum_12 = 0
    sign_sum_02 = 0
    for value in range(domain_start, domain_stop + 1):
        first = squarefree_support(value, primes)
        if first is None:
            continue
        second = squarefree_support(value + shift, primes)
        if second is None:
            continue
        third = squarefree_support(value + 2 * shift, primes)
        if third is None:
            continue
        chains += 1
        signs = [mobius_sign(first), mobius_sign(second), mobius_sign(third)]
        sign_sum_01 += signs[0] * signs[1]
        sign_sum_12 += signs[1] * signs[2]
        sign_sum_02 += signs[0] * signs[2]
        if signs[0] == signs[1] == signs[2]:
            all_same_sign += 1
        if signs[0] == signs[2] and signs[0] != signs[1]:
            alternating_sign += 1
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "domain_size": max(0, domain_stop - domain_start + 1),
        "chains": chains,
        "all_same_sign": all_same_sign,
        "alternating_sign": alternating_sign,
        "sign_sum_01": sign_sum_01,
        "sign_sum_12": sign_sum_12,
        "sign_sum_02": sign_sum_02,
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
        print("p block shift domain chains all_same alternating corr01 corr12 corr02", flush=True)
        for audit in audits:
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['domain_size']} "
                f"{audit['chains']} {audit['all_same_sign']} {audit['alternating_sign']} "
                f"{audit['sign_sum_01']} {audit['sign_sum_12']} {audit['sign_sum_02']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
