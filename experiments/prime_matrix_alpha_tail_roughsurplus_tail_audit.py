#!/usr/bin/env python3
"""AlphaTail 粗筛条件高大素尾盈余审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_roughsurplus_tail_audit.py --selected '997:4096:-36,5003:8192:-36' --num-primes 8 --format table
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


def domain_bounds(block: int, shift: int, point_count: int) -> tuple[int, int]:
    """返回 m 点都落在 block 内的起点区间。"""
    starts = [block + 1 - index * shift for index in range(point_count)]
    stops = [2 * block - index * shift for index in range(point_count)]
    return max(starts), min(stops)


def local_zero_classes(point_count: int, shift: int, prime: int) -> int:
    """返回 m 点链在 prime 下的 distinct 禁零类数。"""
    return len({(-index * shift) % prime for index in range(point_count)})


def avoids_primes(value: int, shift: int, point_count: int, primes: list[int]) -> bool:
    """判断 m 点是否避开给定大素数的禁零类。"""
    for prime in primes:
        for index in range(point_count):
            if (value + index * shift) % prime == 0:
                return False
    return True


def hit_count(value: int, shift: int, point_count: int, primes: list[int]) -> int:
    """统计 m 点命中的尾大素删除事件数。"""
    hits = 0
    for prime in primes:
        if any((value + index * shift) % prime == 0 for index in range(point_count)):
            hits += 1
    return hits


def model_factor(primes: list[int], shift: int, point_count: int) -> float:
    """计算给定大素集合的粗筛模型因子。"""
    factor = 1.0
    for prime in primes:
        factor *= 1.0 - local_zero_classes(point_count, shift, prime) / prime
    return factor


def audit_item(prime_bound: int, block: int, shift: int, alpha: float, num_primes: int) -> dict:
    """审计单个 p:B:r 的条件尾盈余。"""
    cutoff = int(alpha * prime_bound)
    rows = []
    for point_count in (4, 5):
        domain_start, domain_stop = domain_bounds(block, shift, point_count)
        domain_size = max(0, domain_stop - domain_start + 1)
        z_value = max(domain_stop + index * shift for index in range(point_count))
        large_primes = [prime for prime in primes_upto(z_value) if prime > cutoff]
        low_primes = large_primes[:num_primes]
        tail_primes = large_primes[num_primes:]
        low_count = 0
        full_count = 0
        tail_first_moment = 0
        tail_deleted = 0
        for value in range(domain_start, domain_stop + 1):
            if not avoids_primes(value, shift, point_count, low_primes):
                continue
            low_count += 1
            tail_hits = hit_count(value, shift, point_count, tail_primes)
            tail_first_moment += tail_hits
            if tail_hits:
                tail_deleted += 1
            else:
                full_count += 1
        low_factor = model_factor(low_primes, shift, point_count)
        tail_factor = model_factor(tail_primes, shift, point_count)
        full_factor = low_factor * tail_factor
        low_surplus = low_count - domain_size * low_factor
        full_surplus = full_count - domain_size * full_factor
        conditional_tail_surplus = full_count - low_count * tail_factor
        rows.append(
            {
                "m": point_count,
                "low_count": low_count,
                "full_count": full_count,
                "tail_prime_count": len(tail_primes),
                "tail_factor": tail_factor,
                "full_surplus": full_surplus,
                "low_scaled": tail_factor * low_surplus,
                "conditional_tail_surplus": conditional_tail_surplus,
                "tail_first_moment": tail_first_moment,
                "tail_deleted": tail_deleted,
                "identity_ok": abs(full_surplus - (tail_factor * low_surplus + conditional_tail_surplus)) < 1e-9,
            }
        )
    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "shift": shift,
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
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, shift, args.alpha, args.num_primes)
        for prime_bound, block, shift in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block shift m low full Vtail full_surplus low_scaled Xi_tail T1 tail_deleted identity", flush=True)
        for audit in audits:
            for row in audit["rows"]:
                print(
                    f"{audit['p']} {audit['block']} {audit['shift']} "
                    f"{row['m']} {row['low_count']} {row['full_count']} "
                    f"{row['tail_factor']:.8f} {row['full_surplus']:.6f} "
                    f"{row['low_scaled']:.6f} {row['conditional_tail_surplus']:.6f} "
                    f"{row['tail_first_moment']} {row['tail_deleted']} {row['identity_ok']}",
                    flush=True,
                )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
