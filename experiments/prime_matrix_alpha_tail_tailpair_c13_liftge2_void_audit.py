#!/usr/bin/env python3
"""AlphaTail C13 lift>=2 候选空性审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_void_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --format table
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


def smallest_prime_factor(value: int) -> int:
    """返回最小素因子；素数返回自身。"""
    if value < 2:
        return value
    if value % 2 == 0:
        return 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return divisor
        divisor += 2
    return value


def liftge2_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层 lift>=2 候选空性分类。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    if not tail_primes:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "candidate_count": 0,
        }
    tail_set = set(tail_primes)
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    candidate_count = 0
    q_tail_count = 0
    qg_tail_count = 0
    both_tail_count = 0
    q_not_tail_count = 0
    q_tail_qg_not_tail_count = 0
    q_spf_hist: Counter[int] = Counter()
    qg_spf_hist: Counter[int] = Counter()
    lift_hist: Counter[int] = Counter()
    examples = []
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
                for low_prime in low_primes:
                    inverse = pow(multiplier, -1, low_prime)
                    for index in range(point_count):
                        residue = (-(index - index_a) * shift * inverse) % low_prime
                        if (residue + gap) % low_prime == 0:
                            continue
                        first_q = q_lo + ((residue - q_lo) % low_prime)
                        for q_value in range(first_q, q_hi + 1, low_prime):
                            lift = (q_value - residue) // low_prime
                            if lift < 2:
                                continue
                            q_plus_gap = q_value + gap
                            q_is_tail = q_value in tail_set
                            qg_is_tail = q_plus_gap in tail_set
                            candidate_count += 1
                            lift_hist[lift] += 1
                            if q_is_tail:
                                q_tail_count += 1
                            if qg_is_tail:
                                qg_tail_count += 1
                            if q_is_tail and qg_is_tail:
                                both_tail_count += 1
                            elif not q_is_tail:
                                q_not_tail_count += 1
                                q_spf_hist[smallest_prime_factor(q_value)] += 1
                            else:
                                q_tail_qg_not_tail_count += 1
                                qg_spf_hist[smallest_prime_factor(q_plus_gap)] += 1
                            if len(examples) < 8:
                                examples.append(
                                    {
                                        "q": q_value,
                                        "q_plus_g": q_plus_gap,
                                        "gap": gap,
                                        "lift": lift,
                                        "ell": low_prime,
                                        "residue": residue,
                                        "q_spf": smallest_prime_factor(q_value),
                                        "qg_spf": smallest_prime_factor(q_plus_gap),
                                    }
                                )
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "candidate_count": candidate_count,
        "q_tail_count": q_tail_count,
        "qg_tail_count": qg_tail_count,
        "both_tail_count": both_tail_count,
        "q_not_tail_count": q_not_tail_count,
        "q_tail_qg_not_tail_count": q_tail_qg_not_tail_count,
        "q_spf_hist": dict(sorted(q_spf_hist.items())),
        "qg_spf_hist": dict(sorted(qg_spf_hist.items())),
        "lift_hist": dict(sorted(lift_hist.items())),
        "void_by_q_composite": candidate_count == q_not_tail_count,
        "both_tail_void": both_tail_count == 0,
        "examples": examples,
    }


def liftge2_void_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回 lift>=2 空性审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "candidate_count": 0,
            "q_tail_count": 0,
            "qg_tail_count": 0,
            "both_tail_count": 0,
            "q_not_tail_count": 0,
            "q_tail_qg_not_tail_count": 0,
        }
    )
    total = {
        "candidate_count": 0,
        "q_tail_count": 0,
        "qg_tail_count": 0,
        "both_tail_count": 0,
        "q_not_tail_count": 0,
        "q_tail_qg_not_tail_count": 0,
    }
    total_q_spf: Counter[int] = Counter()
    total_lift_hist: Counter[int] = Counter()
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = liftge2_row(prime_bound, block, shift, point_count, alpha, num_primes)
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in total:
                total[name] += item[name]
                windows[key][name] += item[name]
            total_q_spf.update(item["q_spf_hist"])
            total_lift_hist.update(item["lift_hist"])
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["void_by_q_composite"] = value["candidate_count"] == value["q_not_tail_count"]
        value["both_tail_void"] = value["both_tail_count"] == 0
        window_rows.append(value)
    total["q_spf_hist"] = dict(sorted(total_q_spf.items()))
    total["lift_hist"] = dict(sorted(total_lift_hist.items()))
    total["void_by_q_composite"] = total["candidate_count"] == total["q_not_tail_count"]
    total["both_tail_void"] = total["both_tail_count"] == 0
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
    """输出 lift>=2 空性表。"""
    total = package["total"]
    print(
        "scope candidates q_tail qg_tail both_tail q_not_tail q_tail_qg_not "
        "void_by_q both_void q_spf lift_hist",
        flush=True,
    )
    print(
        f"highP-total {total['candidate_count']} {total['q_tail_count']} "
        f"{total['qg_tail_count']} {total['both_tail_count']} "
        f"{total['q_not_tail_count']} {total['q_tail_qg_not_tail_count']} "
        f"{total['void_by_q_composite']} {total['both_tail_void']} "
        f"{total['q_spf_hist']} {total['lift_hist']}",
        flush=True,
    )
    print("p block shift candidates q_tail qg_tail both_tail q_not_tail q_tail_qg_not void_by_q both_void", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['candidate_count']} {row['q_tail_count']} {row['qg_tail_count']} "
            f"{row['both_tail_count']} {row['q_not_tail_count']} "
            f"{row['q_tail_qg_not_tail_count']} {row['void_by_q_composite']} "
            f"{row['both_tail_void']}",
            flush=True,
        )
    print("p block shift m candidates q_tail qg_tail both_tail q_spf lift_hist void_by_q both_void", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['candidate_count']} {row['q_tail_count']} {row['qg_tail_count']} "
            f"{row['both_tail_count']} {row['q_spf_hist']} {row['lift_hist']} "
            f"{row['void_by_q_composite']} {row['both_tail_void']}",
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
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = liftge2_void_package(
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
