#!/usr/bin/env python3
"""AlphaTail 多点光滑链审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_multipoint_chain_audit.py --selected '997:4096:-36,5003:8192:-36' --format table
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


def local_zero_classes(point_count: int, shift: int, prime: int) -> int:
    """返回 m 点链在 prime 下的 distinct 禁零类数。"""
    return len({(-index * shift) % prime for index in range(point_count)})


def chain_count(prime_bound: int, block: int, shift: int, alpha: float, point_count: int) -> int:
    """计算 m 点 y-smooth squarefree 链数量。"""
    cutoff = int(alpha * prime_bound)
    starts = [block + 1 - index * shift for index in range(point_count)]
    stops = [2 * block - index * shift for index in range(point_count)]
    domain_start = max(starts)
    domain_stop = min(stops)
    max_value = max(domain_stop + index * shift for index in range(point_count))
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    count = 0
    for value in range(domain_start, domain_stop + 1):
        if all(squarefree_support(value + index * shift, primes) is not None for index in range(point_count)):
            count += 1
    return count


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, local_cutoff: int) -> dict:
    """审计单个 p:B:r 的多点链。"""
    local_primes = primes_upto(local_cutoff)
    counts = {
        f"T{point_count}": chain_count(prime_bound, block, shift, alpha, point_count)
        for point_count in (3, 4, 5)
    }
    local_classes = {}
    for point_count in (3, 4, 5):
        values = [local_zero_classes(point_count, shift, prime) for prime in local_primes]
        local_classes[f"b{point_count}_avg"] = sum(values) / len(values)
        local_classes[f"b{point_count}_max"] = max(values)
    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "shift": shift,
        "local_cutoff": local_cutoff,
        **counts,
        **local_classes,
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
    parser.add_argument("--local-cutoff", type=int, default=97)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha, args.local_cutoff)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block shift T3 T4 T5 b3_avg b4_avg b5_avg b5_max", flush=True)
        for audit in audits:
            print(
                f"{audit['p']} {audit['block']} {audit['shift']} "
                f"{audit['T3']} {audit['T4']} {audit['T5']} "
                f"{audit['b3_avg']:.6f} {audit['b4_avg']:.6f} {audit['b5_avg']:.6f} {audit['b5_max']}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
