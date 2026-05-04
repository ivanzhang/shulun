#!/usr/bin/env python3
"""AlphaTailStrong 的 dyadic 端点块审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_dyadic_audit.py --selected 997,5003 --alpha 0.9 --maxD 20000

计算 alpha p 低骨架下的端点缺陷：
  E_block(B,2B] = sum mu(d)(N_d-(p-1)/d)
其中 d squarefree、d|M_y、B<d<=2B。
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


def mobius_squarefree_table(limit: int) -> list[tuple[int, int]]:
    """返回 d<=limit 的 squarefree d 与 mu(d)。"""
    primes = primes_upto(limit)
    records: list[tuple[int, int]] = [(1, 1)]
    for value in range(2, limit + 1):
        remaining = value
        omega = 0
        squarefree = True
        for prime in primes:
            if prime * prime > remaining:
                break
            if remaining % prime != 0:
                continue
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            if exponent > 1:
                squarefree = False
                break
            omega += 1
        if not squarefree:
            continue
        if remaining > 1:
            omega += 1
        records.append((value, -1 if omega % 2 else 1))
    return records


def low_divisors(cutoff: int, limit: int) -> list[tuple[int, int]]:
    """返回 d<=limit 且所有素因子 <=cutoff 的 squarefree d。"""
    allowed = set(primes_upto(cutoff))
    records: list[tuple[int, int]] = []
    for value, mu in mobius_squarefree_table(limit):
        remaining = value
        ok = True
        for prime in primes_upto(isqrt(value) + 1):
            if remaining % prime != 0:
                continue
            if prime not in allowed:
                ok = False
                break
            while remaining % prime == 0:
                remaining //= prime
        if ok and remaining > 1 and remaining not in allowed:
            ok = False
        if ok:
            records.append((value, mu))
    return records


def residue_count(prime_bound: int, divisor: int) -> int:
    """计算 1<=k<p 且 k≡-p^2 mod d 的个数。"""
    residue = (-prime_bound * prime_bound) % divisor
    column = residue if residue > 0 else divisor
    count = 0
    while column < prime_bound:
        count += 1
        column += divisor
    return count


def block_records(prime_bound: int, alpha: float, max_divisor: int) -> list[dict]:
    """计算 dyadic block 端点贡献。"""
    cutoff = int(alpha * prime_bound)
    divisors = low_divisors(cutoff, max_divisor)
    interval_length = prime_bound - 1
    blocks: dict[int, dict[str, float]] = {}
    for divisor, mu in divisors:
        if divisor == 1:
            block = 1
        else:
            block = 1
            while 2 * block < divisor:
                block *= 2
        entry = blocks.setdefault(block, {"block_start": block, "count": 0, "endpoint": 0.0})
        entry["count"] += 1
        entry["endpoint"] += mu * (residue_count(prime_bound, divisor) - interval_length / divisor)
    return [blocks[key] for key in sorted(blocks)]


def audit_prime(prime_bound: int, alpha: float, max_divisor: int) -> dict:
    """审计单个 p。"""
    records = block_records(prime_bound, alpha, max_divisor)
    return {
        "p": prime_bound,
        "alpha": alpha,
        "maxD": max_divisor,
        "partial_endpoint": sum(record["endpoint"] for record in records),
        "most_negative_blocks": sorted(records, key=lambda item: item["endpoint"])[:10],
        "records": records,
    }


def parse_int_list(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997,5003")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--maxD", type=int, default=20000)
    parser.add_argument(
        "--format",
        choices=("repr", "json", "table"),
        default="repr",
        help="输出格式；table 适合论文审计摘要。",
    )
    args = parser.parse_args()

    audits = [
        audit_prime(prime_bound, args.alpha, args.maxD)
        for prime_bound in parse_int_list(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p alpha maxD partial_endpoint worst_block worst_endpoint", flush=True)
        for audit in audits:
            worst = audit["most_negative_blocks"][0]
            print(
                f"{audit['p']} {audit['alpha']} {audit['maxD']} "
                f"{audit['partial_endpoint']:.6f} "
                f"{int(worst['block_start'])} {worst['endpoint']:.6f}",
                flush=True,
            )
        return

    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
