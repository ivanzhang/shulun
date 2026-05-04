#!/usr/bin/env python3
"""AlphaTail C13 低筛 AP 删除的提升层刚性审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_ap_lift_rigidity_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit import ceil_div, divisors
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def lift_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层 AP 删除事件的提升层统计。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    if not tail_primes:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "active_deletions": 0,
        }
    tail_set = set(tail_primes)
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    active_lifts: Counter[int] = Counter()
    possible_lifts: Counter[int] = Counter()
    active_offsets: Counter[int] = Counter()
    active_gap_offsets: Counter[tuple[int, int]] = Counter()
    active_records = []
    max_possible_lift = 0
    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            base = -(index_a - index_b) * shift
            if base <= 0:
                continue
            for multiplier in divisors(base):
                gap = base // multiplier
                q_lo = max(tail_min, ceil_div(domain_start + index_a * shift, multiplier))
                q_hi = min(tail_max - gap, (domain_stop + index_a * shift) // multiplier)
                if q_hi < q_lo:
                    continue
                candidate_qs = [
                    prime for prime in tail_primes
                    if q_lo <= prime <= q_hi and prime + gap in tail_set
                ]
                for low_prime in low_primes:
                    inverse = pow(multiplier, -1, low_prime)
                    for index in range(point_count):
                        residue = (-(index - index_a) * shift * inverse) % low_prime
                        if (residue + gap) % low_prime == 0:
                            continue
                        first_q = q_lo + ((residue - q_lo) % low_prime)
                        for q_value in range(first_q, q_hi + 1, low_prime):
                            lift = (q_value - residue) // low_prime
                            possible_lifts[lift] += 1
                            max_possible_lift = max(max_possible_lift, lift)
                        for q_value in candidate_qs:
                            if q_value % low_prime != residue:
                                continue
                            lift = (q_value - residue) // low_prime
                            offset = q_value - low_prime
                            active_lifts[lift] += 1
                            active_offsets[offset] += 1
                            active_gap_offsets[(gap, offset)] += 1
                            active_records.append(
                                {
                                    "ell": low_prime,
                                    "q": q_value,
                                    "q_plus_g": q_value + gap,
                                    "lift": lift,
                                    "offset": offset,
                                    "residue": residue,
                                    "gap": gap,
                                    "u": multiplier,
                                    "j": index,
                                    "j1": index_a,
                                    "j2": index_b,
                                }
                            )
    active_lift_values = sorted(active_lifts)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "active_deletions": sum(active_lifts.values()),
        "active_lift_hist": dict(sorted(active_lifts.items())),
        "possible_lift_hist": dict(sorted(possible_lifts.items())[:12]),
        "max_possible_lift": max_possible_lift,
        "active_lift_min": active_lift_values[0] if active_lift_values else None,
        "active_lift_max": active_lift_values[-1] if active_lift_values else None,
        "active_lift1_count": active_lifts.get(1, 0),
        "active_lift_ge2_count": sum(count for lift, count in active_lifts.items() if lift >= 2),
        "active_offset_min": min(active_offsets) if active_offsets else None,
        "active_offset_max": max(active_offsets) if active_offsets else None,
        "top_offsets": dict(active_offsets.most_common(8)),
        "top_gap_offsets": [
            {"gap": key[0], "offset": key[1], "count": count}
            for key, count in active_gap_offsets.most_common(8)
        ],
        "top_records": active_records[:8],
    }


def lift_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回提升层刚性审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "active_deletions": 0,
            "active_lift1_count": 0,
            "active_lift_ge2_count": 0,
            "max_possible_lift": 0,
        }
    )
    total = {
        "active_deletions": 0,
        "active_lift1_count": 0,
        "active_lift_ge2_count": 0,
        "max_possible_lift": 0,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = lift_row(prime_bound, block, shift, point_count, alpha, num_primes)
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in ("active_deletions", "active_lift1_count", "active_lift_ge2_count"):
                windows[key][name] += item[name]
                total[name] += item[name]
            windows[key]["max_possible_lift"] = max(windows[key]["max_possible_lift"], item["max_possible_lift"])
            total["max_possible_lift"] = max(total["max_possible_lift"], item["max_possible_lift"])
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["all_active_lift1"] = value["active_deletions"] == value["active_lift1_count"]
        window_rows.append(value)
    total["all_active_lift1"] = total["active_deletions"] == total["active_lift1_count"]
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "alpha": alpha,
        "num_primes": num_primes,
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出提升层刚性表。"""
    total = package["total"]
    print("scope active lift1 lift_ge2 max_possible_lift all_active_lift1", flush=True)
    print(
        f"highP-total {total['active_deletions']} {total['active_lift1_count']} "
        f"{total['active_lift_ge2_count']} {total['max_possible_lift']} "
        f"{total['all_active_lift1']}",
        flush=True,
    )
    print("p block shift active lift1 lift_ge2 max_possible_lift all_active_lift1", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['active_deletions']} "
            f"{row['active_lift1_count']} {row['active_lift_ge2_count']} "
            f"{row['max_possible_lift']} {row['all_active_lift1']}",
            flush=True,
        )
    print("p block shift m active lift_hist lift_ge2 offset_min offset_max top_offsets", flush=True)
    for row in package["rows"]:
        offsets = ",".join(f"{offset}:{count}" for offset, count in row["top_offsets"].items())
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['active_deletions']} {row['active_lift_hist']} "
            f"{row['active_lift_ge2_count']} {row['active_offset_min']} "
            f"{row['active_offset_max']} {offsets}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = lift_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.alpha,
        args.num_primes,
    )
    if args.format == "json":
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
