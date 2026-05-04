#!/usr/bin/env python3
"""AlphaTail 条件尾二阶 CRTDefect 审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_pair_crtdefect_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations

from prime_matrix_alpha_tail_tail_overlap_rankin_audit import (
    apply_low_sieve,
    domain_bounds,
    first_index_for_residue,
    local_zero_classes,
    primes_upto,
    z_bound,
)


def tail_primes_for_item(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> list[int]:
    """返回 cutoff 之后、扣除低大素块后的尾素列表。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    z_value = z_bound(domain_start, domain_stop, shift, point_count)
    cutoff = int(alpha * prime_bound)
    large_primes = [prime for prime in primes_upto(z_value) if prime > cutoff]
    return large_primes[num_primes:]


def low_primes_for_item(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> list[int]:
    """返回 cutoff 之后的低大素块。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    z_value = z_bound(domain_start, domain_stop, shift, point_count)
    cutoff = int(alpha * prime_bound)
    large_primes = [prime for prime in primes_upto(z_value) if prime > cutoff]
    return large_primes[:num_primes]


def collect_tail_events(
    domain_start: int,
    domain_size: int,
    shift: int,
    point_count: int,
    active: bytearray,
    tail_primes: list[int],
) -> list[list[tuple[int, int]]]:
    """收集每个低幸存点命中的尾素与点位。"""
    events: list[list[tuple[int, int]]] = [[] for _ in range(domain_size)]
    seen_stamp = [0] * domain_size
    stamp = 0
    for prime in tail_primes:
        stamp += 1
        for index in range(point_count):
            residue = (-index * shift) % prime
            first = first_index_for_residue(domain_start, residue, prime)
            for offset in range(first, domain_size, prime):
                if not active[offset]:
                    continue
                if seen_stamp[offset] == stamp:
                    continue
                seen_stamp[offset] = stamp
                events[offset].append((prime, index))
    return events


def audit_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    top: int,
) -> dict:
    """审计单个 p:B:r:m 的二阶尾素对偏差。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_size = max(0, domain_stop - domain_start + 1)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    active = apply_low_sieve(domain_start, domain_size, shift, point_count, low_primes)
    low_count = sum(active)
    densities = {
        prime: local_zero_classes(point_count, shift, prime) / prime for prime in tail_primes
    }
    events = collect_tail_events(domain_start, domain_size, shift, point_count, active, tail_primes)
    pair_counts: Counter[tuple[int, int]] = Counter()
    point_pair_counts: Counter[tuple[int, int, int, int]] = Counter()
    for offset, point_events in enumerate(events):
        if not active[offset] or len(point_events) < 2:
            continue
        point_events.sort()
        for (prime_a, index_a), (prime_b, index_b) in combinations(point_events, 2):
            pair_counts[(prime_a, prime_b)] += 1
            point_pair_counts[(prime_a, prime_b, index_a, index_b)] += 1
    pair_rows = []
    positive_deviation_sum = 0.0
    for (prime_a, prime_b), actual in pair_counts.items():
        model = low_count * densities[prime_a] * densities[prime_b]
        deviation = actual - model
        if deviation > 0:
            positive_deviation_sum += deviation
        top_point = None
        for index_a in range(point_count):
            for index_b in range(point_count):
                count = point_pair_counts[(prime_a, prime_b, index_a, index_b)]
                point_model = low_count / (prime_a * prime_b)
                point_deviation = count - point_model
                candidate = {
                    "j1": index_a,
                    "j2": index_b,
                    "count": count,
                    "model": point_model,
                    "deviation": point_deviation,
                }
                if top_point is None or candidate["deviation"] > top_point["deviation"]:
                    top_point = candidate
        pair_rows.append(
            {
                "q1": prime_a,
                "q2": prime_b,
                "actual": actual,
                "model": model,
                "deviation": deviation,
                "top_point": top_point,
            }
        )
    pair_rows.sort(key=lambda item: item["deviation"], reverse=True)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "low_count": low_count,
        "tail_prime_count": len(tail_primes),
        "observed_pair_count": len(pair_counts),
        "positive_deviation_sum": positive_deviation_sum,
        "top_pairs": pair_rows[:top],
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


def print_table(rows: list[dict]) -> None:
    """输出每个样本的最热正偏差尾素对。"""
    print(
        "p block shift m low_count observed_pairs pos_dev_sum "
        "q1 q2 actual model deviation j1 j2 point_count point_model point_deviation",
        flush=True,
    )
    for row in rows:
        top_pair = row["top_pairs"][0] if row["top_pairs"] else None
        if top_pair is None:
            print(
                f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['low_count']} "
                f"{row['observed_pair_count']} {row['positive_deviation_sum']:.6f} "
                "NA NA 0 0.000000 0.000000 NA NA 0 0.000000 0.000000",
                flush=True,
            )
            continue
        top_point = top_pair["top_point"]
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} {row['low_count']} "
            f"{row['observed_pair_count']} {row['positive_deviation_sum']:.6f} "
            f"{top_pair['q1']} {top_pair['q2']} {top_pair['actual']} "
            f"{top_pair['model']:.6f} {top_pair['deviation']:.6f} "
            f"{top_point['j1']} {top_point['j2']} {top_point['count']} "
            f"{top_point['model']:.6f} {top_point['deviation']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(audit_row(prime_bound, block, shift, point_count, args.alpha, args.num_primes, args.top))
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
