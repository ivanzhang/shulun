#!/usr/bin/env python3
"""AlphaTail C13 lift>=2 候选的模 6 空性审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_mod6_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --format table
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


def mod6_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层 lift>=2 候选的模 6 分类。"""
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
    q_mod6_hist: Counter[int] = Counter()
    t_mod6_hist: Counter[int] = Counter()
    residue_mod6_hist: Counter[int] = Counter()
    ell_mod6_hist: Counter[int] = Counter()
    signature_hist: Counter[tuple[int, int, int, int]] = Counter()
    good_mod6_count = 0
    good_mod6_tail_count = 0
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
                            q_mod6 = q_value % 6
                            candidate_count += 1
                            q_mod6_hist[q_mod6] += 1
                            t_mod6_hist[lift % 6] += 1
                            residue_mod6_hist[residue % 6] += 1
                            ell_mod6_hist[low_prime % 6] += 1
                            signature_hist[(lift % 6, low_prime % 6, residue % 6, q_mod6)] += 1
                            if q_mod6 in (1, 5):
                                good_mod6_count += 1
                                if q_value in tail_set:
                                    good_mod6_tail_count += 1
                            if len(examples) < 8:
                                examples.append(
                                    {
                                        "q": q_value,
                                        "lift": lift,
                                        "ell": low_prime,
                                        "residue": residue,
                                        "t_mod6": lift % 6,
                                        "ell_mod6": low_prime % 6,
                                        "residue_mod6": residue % 6,
                                        "q_mod6": q_mod6,
                                    }
                                )
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "candidate_count": candidate_count,
        "q_mod6_hist": dict(sorted(q_mod6_hist.items())),
        "t_mod6_hist": dict(sorted(t_mod6_hist.items())),
        "residue_mod6_hist": dict(sorted(residue_mod6_hist.items())),
        "ell_mod6_hist": dict(sorted(ell_mod6_hist.items())),
        "signature_hist": [
            {
                "t_mod6": key[0],
                "ell_mod6": key[1],
                "residue_mod6": key[2],
                "q_mod6": key[3],
                "count": count,
            }
            for key, count in signature_hist.most_common(12)
        ],
        "good_mod6_count": good_mod6_count,
        "good_mod6_tail_count": good_mod6_tail_count,
        "bad_mod6_count": candidate_count - good_mod6_count,
        "all_bad_mod6": good_mod6_count == 0,
        "examples": examples,
    }


def mod6_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回 lift>=2 模 6 审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "candidate_count": 0,
            "good_mod6_count": 0,
            "good_mod6_tail_count": 0,
            "bad_mod6_count": 0,
        }
    )
    total = {
        "candidate_count": 0,
        "good_mod6_count": 0,
        "good_mod6_tail_count": 0,
        "bad_mod6_count": 0,
    }
    total_q_mod6: Counter[int] = Counter()
    total_t_mod6: Counter[int] = Counter()
    total_residue_mod6: Counter[int] = Counter()
    total_ell_mod6: Counter[int] = Counter()
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = mod6_row(prime_bound, block, shift, point_count, alpha, num_primes)
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in total:
                total[name] += item[name]
                windows[key][name] += item[name]
            total_q_mod6.update(item["q_mod6_hist"])
            total_t_mod6.update(item["t_mod6_hist"])
            total_residue_mod6.update(item["residue_mod6_hist"])
            total_ell_mod6.update(item["ell_mod6_hist"])
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["all_bad_mod6"] = value["good_mod6_count"] == 0
        window_rows.append(value)
    total["q_mod6_hist"] = dict(sorted(total_q_mod6.items()))
    total["t_mod6_hist"] = dict(sorted(total_t_mod6.items()))
    total["residue_mod6_hist"] = dict(sorted(total_residue_mod6.items()))
    total["ell_mod6_hist"] = dict(sorted(total_ell_mod6.items()))
    total["all_bad_mod6"] = total["good_mod6_count"] == 0
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
    """输出 lift>=2 模 6 表。"""
    total = package["total"]
    print(
        "scope candidates bad_mod6 good_mod6 good_tail all_bad q_mod6 t_mod6 residue_mod6 ell_mod6",
        flush=True,
    )
    print(
        f"highP-total {total['candidate_count']} {total['bad_mod6_count']} "
        f"{total['good_mod6_count']} {total['good_mod6_tail_count']} "
        f"{total['all_bad_mod6']} {total['q_mod6_hist']} {total['t_mod6_hist']} "
        f"{total['residue_mod6_hist']} {total['ell_mod6_hist']}",
        flush=True,
    )
    print("p block shift candidates bad_mod6 good_mod6 good_tail all_bad", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['candidate_count']} {row['bad_mod6_count']} "
            f"{row['good_mod6_count']} {row['good_mod6_tail_count']} "
            f"{row['all_bad_mod6']}",
            flush=True,
        )
    print("p block shift m candidates bad_mod6 good_mod6 q_mod6 t_mod6 residue_mod6 all_bad", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['candidate_count']} {row['bad_mod6_count']} "
            f"{row['good_mod6_count']} {row['q_mod6_hist']} "
            f"{row['t_mod6_hist']} {row['residue_mod6_hist']} "
            f"{row['all_bad_mod6']}",
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

    package = mod6_package(
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
