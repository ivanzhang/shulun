#!/usr/bin/env python3
"""AlphaTail ShiftSmooth 近线性大素数删除审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_nearlinear_deletion_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
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


def has_large_prime_factor(value: int, large_primes: list[int]) -> bool:
    """判断 value 是否含有给定列表中的大素因子。"""
    for prime in large_primes:
        if prime > value:
            break
        if value % prime == 0:
            return True
    return False


def squarefree_mobius_sign(value: int, small_primes: list[int]) -> int:
    """返回 squarefree y-smooth 数的 Möbius 符号；非平方自由返回 0。"""
    remaining = value
    omega = 0
    for prime in small_primes:
        if prime > remaining:
            break
        if remaining % prime != 0:
            continue
        remaining //= prime
        omega += 1
        if remaining % prime == 0:
            return 0
    if remaining != 1:
        return 0
    return -1 if omega % 2 else 1


def audit_item(prime_bound: int, block: int, shift: int, alpha: float) -> dict:
    """审计单个 p:B:r 的删除集恒等式。"""
    cutoff = int(alpha * prime_bound)
    left_start = block + 1
    left_stop = 2 * block
    domain_start = max(left_start, left_start - shift)
    domain_stop = min(left_stop, left_stop - shift)
    max_value = max(domain_stop, domain_stop + shift, 0)
    primes = primes_upto(max_value)
    small_primes = [prime for prime in primes if prime <= cutoff]
    large_primes = [prime for prime in primes if prime > cutoff]
    domain = list(range(domain_start, domain_stop + 1)) if domain_stop >= domain_start else []
    left_deleted = {
        value for value in domain if has_large_prime_factor(value, large_primes)
    }
    right_deleted = {
        value for value in domain if has_large_prime_factor(value + shift, large_primes)
    }
    union_deleted = left_deleted | right_deleted
    smooth_pair_count = len(domain) - len(union_deleted)
    plus_pair_count = 0
    minus_pair_count = 0
    squarefree_same_sign_count = 0
    for value in domain:
        if value in union_deleted:
            continue
        left_sign = squarefree_mobius_sign(value, small_primes)
        if left_sign == 0:
            continue
        right_sign = squarefree_mobius_sign(value + shift, small_primes)
        if right_sign == 0 or right_sign != left_sign:
            continue
        squarefree_same_sign_count += 1
        if left_sign > 0:
            plus_pair_count += 1
        else:
            minus_pair_count += 1
    near_linear = max_value < cutoff * cutoff
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "near_linear": near_linear,
        "domain_size": len(domain),
        "left_deleted": len(left_deleted),
        "right_deleted": len(right_deleted),
        "delete_overlap": len(left_deleted & right_deleted),
        "delete_union": len(union_deleted),
        "smooth_pair_count": smooth_pair_count,
        "same_sign_squarefree_pairs": squarefree_same_sign_count,
        "plus_pairs": plus_pair_count,
        "minus_pairs": minus_pair_count,
        "large_prime_count": len(large_primes),
        "max_value": max_value,
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
        print(
            "p block shift near domain left_del right_del overlap union smooth_pairs same_sign plus minus large_primes",
            flush=True,
        )
        for audit in audits:
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} {audit['near_linear']} "
                f"{audit['domain_size']} {audit['left_deleted']} {audit['right_deleted']} "
                f"{audit['delete_overlap']} {audit['delete_union']} "
                f"{audit['smooth_pair_count']} {audit['same_sign_squarefree_pairs']} "
                f"{audit['plus_pairs']} {audit['minus_pairs']} {audit['large_prime_count']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
