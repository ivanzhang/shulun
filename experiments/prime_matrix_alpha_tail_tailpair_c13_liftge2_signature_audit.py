#!/usr/bin/env python3
"""AlphaTail C13 lift>=2 候选的 h/t 模 6 签名审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_signature_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --format table
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


def signature_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层 lift>=2 候选的 h/t 模 6 签名。"""
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
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    candidate_count = 0
    good_mod6_count = 0
    h_hist: Counter[int] = Counter()
    t_hist: Counter[int] = Counter()
    u_hist: Counter[int] = Counter()
    q_mod6_hist: Counter[int] = Counter()
    signature_hist: Counter[tuple[int, int, int, int, int]] = Counter()
    h_over_u_hist: Counter[str] = Counter()
    algebra_failures = 0
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
                        numerator = -(index - index_a) * shift
                        residue = (numerator * inverse) % low_prime
                        if (residue + gap) % low_prime == 0:
                            continue
                        first_q = q_lo + ((residue - q_lo) % low_prime)
                        for q_value in range(first_q, q_hi + 1, low_prime):
                            lift = (q_value - residue) // low_prime
                            if lift < 2:
                                continue
                            h_numerator = multiplier * residue - numerator
                            if h_numerator % low_prime != 0:
                                algebra_failures += 1
                                continue
                            h_layer = h_numerator // low_prime
                            recomposed = (
                                (lift * multiplier + h_layer) * low_prime + numerator
                            )
                            if recomposed != multiplier * q_value:
                                algebra_failures += 1
                                continue
                            candidate_count += 1
                            q_mod6 = q_value % 6
                            if q_mod6 in (1, 5):
                                good_mod6_count += 1
                            h_hist[h_layer] += 1
                            t_hist[lift] += 1
                            u_hist[multiplier] += 1
                            q_mod6_hist[q_mod6] += 1
                            h_over_u_hist[f"{h_layer}/{multiplier}"] += 1
                            signature_hist[
                                (
                                    lift % 6,
                                    multiplier % 6,
                                    h_layer % 6,
                                    low_prime % 6,
                                    q_mod6,
                                )
                            ] += 1
                            if len(examples) < 8:
                                examples.append(
                                    {
                                        "q": q_value,
                                        "ell": low_prime,
                                        "t": lift,
                                        "u": multiplier,
                                        "h": h_layer,
                                        "q_mod6": q_mod6,
                                        "ell_mod6": low_prime % 6,
                                        "gap": gap,
                                        "j": index,
                                        "j1": index_a,
                                        "j2": index_b,
                                    }
                                )
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "candidate_count": candidate_count,
        "good_mod6_count": good_mod6_count,
        "bad_mod6_count": candidate_count - good_mod6_count,
        "all_bad_mod6": good_mod6_count == 0,
        "algebra_failures": algebra_failures,
        "h_hist": dict(sorted(h_hist.items())),
        "t_hist": dict(sorted(t_hist.items())),
        "u_hist": dict(u_hist.most_common(8)),
        "q_mod6_hist": dict(sorted(q_mod6_hist.items())),
        "h_over_u_hist": dict(h_over_u_hist.most_common(8)),
        "signature_hist": [
            {
                "t_mod6": key[0],
                "u_mod6": key[1],
                "h_mod6": key[2],
                "ell_mod6": key[3],
                "q_mod6": key[4],
                "count": count,
            }
            for key, count in signature_hist.most_common(12)
        ],
        "examples": examples,
    }


def signature_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回 lift>=2 签名审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "candidate_count": 0,
            "good_mod6_count": 0,
            "bad_mod6_count": 0,
            "algebra_failures": 0,
        }
    )
    total = {
        "candidate_count": 0,
        "good_mod6_count": 0,
        "bad_mod6_count": 0,
        "algebra_failures": 0,
    }
    total_h: Counter[int] = Counter()
    total_t: Counter[int] = Counter()
    total_u: Counter[int] = Counter()
    total_q_mod6: Counter[int] = Counter()
    total_ratio: Counter[str] = Counter()
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = signature_row(prime_bound, block, shift, point_count, alpha, num_primes)
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in total:
                total[name] += item[name]
                windows[key][name] += item[name]
            total_h.update(item["h_hist"])
            total_t.update(item["t_hist"])
            total_u.update(item["u_hist"])
            total_q_mod6.update(item["q_mod6_hist"])
            total_ratio.update(item["h_over_u_hist"])
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["all_bad_mod6"] = value["good_mod6_count"] == 0
        window_rows.append(value)
    total["all_bad_mod6"] = total["good_mod6_count"] == 0
    total["h_hist"] = dict(sorted(total_h.items()))
    total["t_hist"] = dict(sorted(total_t.items()))
    total["u_hist"] = dict(sorted(total_u.items()))
    total["q_mod6_hist"] = dict(sorted(total_q_mod6.items()))
    total["h_over_u_hist"] = dict(total_ratio.most_common(8))
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
    """输出 lift>=2 签名审计表。"""
    total = package["total"]
    print(
        "scope candidates bad good algebra_fail all_bad q_mod6 t_hist u_hist h_hist h_over_u",
        flush=True,
    )
    print(
        f"highP-total {total['candidate_count']} {total['bad_mod6_count']} "
        f"{total['good_mod6_count']} {total['algebra_failures']} {total['all_bad_mod6']} "
        f"{total['q_mod6_hist']} {total['t_hist']} {total['u_hist']} {total['h_hist']} "
        f"{total['h_over_u_hist']}",
        flush=True,
    )
    print("p block shift candidates bad good algebra_fail all_bad", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['candidate_count']} "
            f"{row['bad_mod6_count']} {row['good_mod6_count']} "
            f"{row['algebra_failures']} {row['all_bad_mod6']}",
            flush=True,
        )
    print("p block shift m candidates bad good q_mod6 t_hist u_hist h_hist h_over_u all_bad", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['candidate_count']} {row['bad_mod6_count']} {row['good_mod6_count']} "
            f"{row['q_mod6_hist']} {row['t_hist']} {row['u_hist']} {row['h_hist']} "
            f"{row['h_over_u_hist']} {row['all_bad_mod6']}",
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

    package = signature_package(
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
