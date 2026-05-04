#!/usr/bin/env python3
"""AlphaTail 单高素锚点类贡献审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_single_anchor_audit.py --selected '997:4096:-36,5003:8192:-36' --R 31 --format table
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
    """审计单个 p:B:r 的单锚点左右类贡献。"""
    cutoff = int(alpha * prime_bound)
    domain_start = max(block + 1, block + 1 - shift)
    domain_stop = min(2 * block, 2 * block - shift)
    max_value = max(domain_stop, domain_stop + shift, 0)
    primes = [prime for prime in primes_upto(max_value) if prime <= cutoff]
    low_primes = [prime for prime in primes if prime <= low_cutoff]
    tail_primes = [prime for prime in primes if prime > low_cutoff]
    records: dict[int, dict[str, int]] = defaultdict(
        lambda: {"left_sum": 0, "right_sum": 0, "left_count": 0, "right_count": 0}
    )
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
        for prime in tail_primes:
            local = psi_value(left, right, shift, prime)
            if local != 1 and shift % prime != 0:
                entry = records[prime]
                weight = low_value * prefix
                if prime in left:
                    entry["left_sum"] += weight
                    entry["left_count"] += 1
                if prime in right:
                    entry["right_sum"] += weight
                    entry["right_count"] += 1
            prefix *= local

    rows = []
    for prime, entry in records.items():
        raw_sum = entry["left_sum"] + entry["right_sum"]
        anchor = -2 * raw_sum
        rows.append(
            {
                "q": prime,
                "anchor": anchor,
                "raw_sum": raw_sum,
                "left_sum": entry["left_sum"],
                "right_sum": entry["right_sum"],
                "left_count": entry["left_count"],
                "right_count": entry["right_count"],
                "max_class_abs": max(abs(entry["left_sum"]), abs(entry["right_sum"])),
            }
        )
    rows.sort(key=lambda item: (-abs(item["anchor"]), item["q"]))
    return {
        "p": prime_bound,
        "alpha": alpha,
        "y": cutoff,
        "block": block,
        "shift": shift,
        "R": low_cutoff,
        "pair_count": pair_count,
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


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--R", type=int, default=31)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--top", type=int, default=8)
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
        print("p block shift R pairs q anchor left_sum right_sum left_count right_count", flush=True)
        for audit in audits:
            for row in audit["rows"][: args.top]:
                print(
                    f"{audit['p']} {audit['block']} {audit['shift']} {audit['R']} "
                    f"{audit['pair_count']} {row['q']} {row['anchor']} "
                    f"{row['left_sum']} {row['right_sum']} "
                    f"{row['left_count']} {row['right_count']}",
                    flush=True,
                )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
