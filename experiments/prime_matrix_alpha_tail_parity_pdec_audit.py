#!/usr/bin/env python3
"""AlphaTail Parity-PDEC 低模/高尾分解审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_parity_pdec_audit.py --selected '997:4096:-36,5003:8192:-36' --cutoffs 5,7,11,17 --format table
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


def psi_for_prime(left: set[int], right: set[int], shift: int, prime: int) -> int:
    """计算局部奇偶函数 psi_{q,r}。"""
    if shift % prime == 0:
        return 1
    return -1 if (prime in left or prime in right) else 1


def low_mean(shift: int, low_primes: list[int]) -> float:
    """计算低模符号函数在完整 residue 系上的局部均值。"""
    mean = 1.0
    for prime in low_primes:
        if shift % prime == 0:
            continue
        mean *= (prime - 4) / prime
    return mean


def audit_item(prime_bound: int, block: int, shift: int, cutoffs: list[int], alpha: float) -> dict:
    """审计单个 p:B:r 的低模/高尾分解。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift)
    domain_stop = min(2 * block, 2 * block - shift)
    max_value = max(domain_stop, domain_stop + shift, 0)
    small_primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    pairs: list[tuple[set[int], set[int]]] = []
    full_correlation = 0
    for value in range(domain_start, domain_stop + 1):
        left = squarefree_support(value, small_primes)
        if left is None:
            continue
        right = squarefree_support(value + shift, small_primes)
        if right is None:
            continue
        pairs.append((left, right))
        full_correlation += 1 if len(left ^ right) % 2 == 0 else -1

    rows = []
    for raw_cutoff in cutoffs:
        low_primes = [prime for prime in small_primes if prime <= raw_cutoff]
        low_sum = 0
        tail_gap = 0
        for left, right in pairs:
            low_value = 1
            for prime in low_primes:
                low_value *= psi_for_prime(left, right, shift, prime)
            full_value = 1 if len(left ^ right) % 2 == 0 else -1
            low_sum += low_value
            tail_gap += full_value - low_value
        mean = low_mean(shift, low_primes)
        modeled_low = mean * len(pairs)
        rows.append(
            {
                "R": raw_cutoff,
                "low_prime_count": len(low_primes),
                "low_sum": low_sum,
                "low_mean": mean,
                "modeled_low": modeled_low,
                "centered_low": low_sum - modeled_low,
                "tail_gap": tail_gap,
                "full_correlation": full_correlation,
            }
        )
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "pair_count": len(pairs),
        "full_correlation": full_correlation,
        "rows": rows,
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


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--cutoffs", type=str, default="5,7,11,17")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    cutoffs = parse_ints(args.cutoffs)
    audits = [
        audit_item(prime_bound, block, shift, cutoffs, args.alpha)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block shift pairs K R low_sum modeled centered tail_gap", flush=True)
        for audit in audits:
            for row in audit["rows"]:
                print(
                    f"{audit['p']} {audit['block']} {audit['shift']} "
                    f"{audit['pair_count']} {audit['full_correlation']} "
                    f"{row['R']} {row['low_sum']} {row['modeled_low']:.6f} "
                    f"{row['centered_low']:.6f} {row['tail_gap']}",
                    flush=True,
                )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
