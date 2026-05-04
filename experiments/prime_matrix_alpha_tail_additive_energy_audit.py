#!/usr/bin/env python3
"""AlphaTail 高块低素平方自由集合的加法能量审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_additive_energy_audit.py --selected '997:4096:-,5003:8192:-' --format table
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


def low_squarefree_block(cutoff: int, block: int, sign: str) -> list[int]:
    """返回 block<d<=2block 中由低素数生成且 Möbius 符号指定的平方自由数。"""
    allowed = primes_upto(cutoff)
    allowed_set = set(allowed)
    target_parity = 0 if sign == "+" else 1
    records: list[int] = []
    for value in range(block + 1, 2 * block + 1):
        remaining = value
        omega = 0
        ok = True
        for prime in allowed:
            if prime * prime > remaining:
                break
            if remaining % prime != 0:
                continue
            remaining //= prime
            omega += 1
            if remaining % prime == 0:
                ok = False
                break
        if not ok:
            continue
        if remaining > 1:
            if remaining not in allowed_set:
                continue
            omega += 1
        if omega % 2 == target_parity:
            records.append(value)
    return records


def audit_item(prime_bound: int, block: int, sign: str, alpha: float) -> dict:
    """审计单个 p:B:sign 的加法能量。"""
    values = low_squarefree_block(int(alpha * prime_bound), block, sign)
    diff_counts: dict[int, int] = defaultdict(int)
    for left in values:
        for right in values:
            diff_counts[left - right] += 1
    energy = sum(count * count for count in diff_counts.values())
    nonzero_items = [(diff, count) for diff, count in diff_counts.items() if diff != 0]
    top_nonzero = sorted(nonzero_items, key=lambda item: (-item[1], abs(item[0]), item[0]))[:10]
    cardinality = len(values)
    interval_model = cardinality**4 / max(1, 2 * block) + cardinality * cardinality
    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "sign": sign,
        "d_count": cardinality,
        "diff_support": len(diff_counts),
        "energy": energy,
        "interval_model": interval_model,
        "energy_over_model": energy / interval_model if interval_model else 0.0,
        "max_nonzero_diff": top_nonzero[0] if top_nonzero else [0, 0],
        "top_nonzero_diffs": top_nonzero,
    }


def parse_selected(raw: str) -> list[tuple[int, int, str]]:
    """解析 p:B:sign 逗号列表。"""
    items: list[tuple[int, int, str]] = []
    for part in raw.split(","):
        if not part.strip():
            continue
        prime_raw, block_raw, sign = part.split(":", 2)
        if sign not in {"+", "-"}:
            raise ValueError("sign must be + or -")
        items.append((int(prime_raw), int(block_raw), sign))
    return items


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-,5003:8192:-")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, sign, args.alpha)
        for prime_bound, block, sign in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block sign d_count diff_support energy energy_over_model max_diff max_count", flush=True)
        for audit in audits:
            max_diff, max_count = audit["max_nonzero_diff"]
            print(
                f"{audit['p']} {audit['block']} {audit['sign']} "
                f"{audit['d_count']} {audit['diff_support']} {audit['energy']} "
                f"{audit['energy_over_model']:.6f} {max_diff} {max_count}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
