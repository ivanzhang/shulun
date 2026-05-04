#!/usr/bin/env python3
"""AlphaTail 条件尾重叠 Rankin 账本审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tail_overlap_rankin_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --format table
  python3 experiments/prime_matrix_alpha_tail_tail_overlap_rankin_audit.py --selected '10007:16384:-900' --rho 1.5 --format json
"""

from __future__ import annotations

import argparse
import json
from math import prod


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            start = value * value
            sieve[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [value for value in range(2, limit + 1) if sieve[value]]


def domain_bounds(block: int, shift: int, point_count: int) -> tuple[int, int]:
    """返回 m 点都落在 block 内的起点区间。"""
    starts = [block + 1 - index * shift for index in range(point_count)]
    stops = [2 * block - index * shift for index in range(point_count)]
    return max(starts), min(stops)


def z_bound(domain_start: int, domain_stop: int, shift: int, point_count: int) -> int:
    """返回 m 点链的绝对值上界。"""
    values = []
    for endpoint in (domain_start, domain_stop):
        values.extend(abs(endpoint + index * shift) for index in range(point_count))
    return max(values) if values else 0


def local_zero_classes(point_count: int, shift: int, prime: int) -> int:
    """返回 m 点链在 prime 下的 distinct 禁零类数。"""
    return len({(-index * shift) % prime for index in range(point_count)})


def model_factor(primes: list[int], shift: int, point_count: int) -> float:
    """计算给定大素集合的粗筛模型因子。"""
    factor = 1.0
    for prime in primes:
        factor *= 1.0 - local_zero_classes(point_count, shift, prime) / prime
    return factor


def first_index_for_residue(domain_start: int, residue: int, modulus: int) -> int:
    """返回区间起点数组中首个满足 d == residue mod modulus 的下标。"""
    return (residue - domain_start) % modulus


def apply_low_sieve(
    domain_start: int,
    domain_size: int,
    shift: int,
    point_count: int,
    low_primes: list[int],
) -> bytearray:
    """用低大素删除事件生成低幸存指示数组。"""
    active = bytearray(b"\x01") * domain_size
    for prime in low_primes:
        residues = {(-index * shift) % prime for index in range(point_count)}
        for residue in residues:
            first = first_index_for_residue(domain_start, residue, prime)
            for offset in range(first, domain_size, prime):
                active[offset] = 0
    return active


def tail_hit_counts(
    domain_start: int,
    domain_size: int,
    shift: int,
    point_count: int,
    active: bytearray,
    tail_primes: list[int],
) -> tuple[list[int], list[int]]:
    """统计每个低幸存点的尾素事件命中重数和每个点位的命中量。"""
    hits = [0] * domain_size
    point_hit_sums = [0] * point_count
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
                point_hit_sums[index] += 1
                if seen_stamp[offset] == stamp:
                    continue
                seen_stamp[offset] = stamp
                hits[offset] += 1
    return hits, point_hit_sums


def rankin_level_bound(tail_primes: list[int], z_value: int, point_count: int) -> int:
    """返回乘积界允许的最大尾命中重数。"""
    limit = z_value**point_count
    product = 1
    level = 0
    for prime in tail_primes:
        if product * prime > limit:
            break
        product *= prime
        level += 1
    return level


def audit_point_count(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    rho: float,
) -> dict:
    """审计单个 p:B:r:m 的尾重叠 Rankin 账本。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    domain_size = max(0, domain_stop - domain_start + 1)
    z_value = z_bound(domain_start, domain_stop, shift, point_count)
    cutoff = int(alpha * prime_bound)
    large_primes = [prime for prime in primes_upto(z_value) if prime > cutoff]
    low_primes = large_primes[:num_primes]
    tail_primes = large_primes[num_primes:]
    active = apply_low_sieve(domain_start, domain_size, shift, point_count, low_primes)
    hits, point_hit_sums = tail_hit_counts(domain_start, domain_size, shift, point_count, active, tail_primes)
    low_count = sum(active)
    active_hits = [hits[offset] for offset, is_active in enumerate(active) if is_active]
    tail_hit_sum = sum(active_hits)
    tail_deleted = sum(1 for value in active_hits if value > 0)
    full_count = low_count - tail_deleted
    max_tail_hits = max(active_hits, default=0)
    tail_factor = model_factor(tail_primes, shift, point_count)
    tail_model_deleted = low_count * (1.0 - tail_factor)
    xi_tail = full_count - low_count * tail_factor
    overlap_excess = tail_hit_sum - tail_deleted
    first_moment_model = low_count * sum(
        local_zero_classes(point_count, shift, prime) / prime for prime in tail_primes
    )
    first_moment_defect = first_moment_model - tail_hit_sum
    l_bound = rankin_level_bound(tail_primes, z_value, point_count)
    rankin_level = max(1, max_tail_hits)
    rankin_moment = sum(rho**value for value in active_hits)
    rankin_bound = rankin_moment / (rho**rankin_level)
    product_bound_ok = max_tail_hits <= l_bound
    point_hit_max = max(point_hit_sums, default=0)
    point_hit_argmax = point_hit_sums.index(point_hit_max) if point_hit_sums else -1
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "domain_size": domain_size,
        "low_count": low_count,
        "full_count": full_count,
        "tail_prime_count": len(tail_primes),
        "tail_factor": tail_factor,
        "tail_model_deleted": tail_model_deleted,
        "xi_tail": xi_tail,
        "tail_hit_sum": tail_hit_sum,
        "tail_deleted": tail_deleted,
        "overlap_excess": overlap_excess,
        "first_moment_model": first_moment_model,
        "first_moment_defect": first_moment_defect,
        "max_tail_hits": max_tail_hits,
        "l_bound": l_bound,
        "product_bound_ok": product_bound_ok,
        "rankin_level": rankin_level,
        "rankin_moment": rankin_moment,
        "rankin_bound": rankin_bound,
        "point_hit_max": point_hit_max,
        "point_hit_argmax": point_hit_argmax,
        "point_hit_sums": point_hit_sums,
        "identity_ok": abs(xi_tail - (tail_model_deleted - tail_deleted)) < 1e-9,
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


def audit_items(selected: list[tuple[int, int, int]], alpha: float, num_primes: int, rho: float) -> list[dict]:
    """审计所有选中样本。"""
    rows = []
    for prime_bound, block, shift in selected:
        for point_count in (4, 5):
            rows.append(audit_point_count(prime_bound, block, shift, point_count, alpha, num_primes, rho))
    return rows


def print_table(rows: list[dict]) -> None:
    """输出紧凑表格。"""
    print(
        "p block shift m low_count full_count tail_hit_sum tail_deleted "
        "max_tail_hits L_bound overlap_excess Xi_tail first_moment_defect product_bound_ok",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['low_count']} {row['full_count']} {row['tail_hit_sum']} {row['tail_deleted']} "
            f"{row['max_tail_hits']} {row['l_bound']} {row['overlap_excess']} "
            f"{row['xi_tail']:.6f} {row['first_moment_defect']:.6f} {row['product_bound_ok']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--rho", type=float, default=1.5)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = audit_items(parse_selected(args.selected), args.alpha, args.num_primes, args.rho)
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
