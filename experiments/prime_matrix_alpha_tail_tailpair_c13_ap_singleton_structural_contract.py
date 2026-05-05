#!/usr/bin/env python3
"""AlphaTail C13 AP 单点化结构充分条件审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
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


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def active_ap_classes(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> list[dict]:
    """枚举活跃 AP 删除类。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    if not tail_primes:
        return []
    tail_set = set(tail_primes)
    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    rows = []
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
                    prime
                    for prime in tail_primes
                    if q_lo <= prime <= q_hi and prime + gap in tail_set
                ]
                if not candidate_qs:
                    continue
                for low_prime in low_primes:
                    inverse = pow(multiplier, -1, low_prime)
                    for index in range(point_count):
                        residue = (-(index - index_a) * shift * inverse) % low_prime
                        hit_qs = [prime for prime in candidate_qs if prime % low_prime == residue]
                        if not hit_qs:
                            continue
                        for q_value in hit_qs:
                            rows.append(
                                {
                                    "p": prime_bound,
                                    "block": block,
                                    "shift": shift,
                                    "m": point_count,
                                    "ell": low_prime,
                                    "j": index,
                                    "residue": residue,
                                    "gap": gap,
                                    "u": multiplier,
                                    "j1": index_a,
                                    "j2": index_b,
                                    "q": q_value,
                                    "q_plus_gap": q_value + gap,
                                    "q_lift": (q_value - residue) // low_prime,
                                    "q_lt_2ell": q_value < 2 * low_prime,
                                }
                            )
    return rows


def structural_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层 AP 单点化结构充分条件。"""
    rows = active_ap_classes(prime_bound, block, shift, point_count, alpha, num_primes)
    u_hist = Counter(row["u"] for row in rows)
    lift_hist = Counter(row["q_lift"] for row in rows)
    gap_hist = Counter(row["gap"] for row in rows)
    ell_hist = Counter(row["ell"] for row in rows)
    all_u23 = all(row["u"] in (2, 3) for row in rows)
    all_q_one_lift = all(row["q_lift"] == 1 for row in rows)
    all_q_lt_2ell = all(row["q_lt_2ell"] for row in rows)
    singleton_structural = all_q_lt_2ell
    max_q_over_ell = max((row["q"] / row["ell"] for row in rows), default=None)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "active_classes": len(rows),
        "all_u23": all_u23,
        "all_q_one_lift": all_q_one_lift,
        "all_q_lt_2ell": all_q_lt_2ell,
        "singleton_structural": singleton_structural,
        "max_q_over_ell": max_q_over_ell,
        "u_hist": dict(sorted(u_hist.items())),
        "lift_hist": dict(sorted(lift_hist.items())),
        "top_gaps": dict(gap_hist.most_common(8)),
        "top_ell": dict(ell_hist.most_common(8)),
        "examples": rows[:8],
    }


def ap_singleton_structural_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回 AP 单点化结构合同包。"""
    rows = []
    windows: defaultdict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "active_classes": 0,
            "all_u23": True,
            "all_q_one_lift": True,
            "all_q_lt_2ell": True,
            "singleton_structural": True,
            "max_q_over_ell": None,
            "u_hist": Counter(),
            "lift_hist": Counter(),
        }
    )
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            row = structural_row(prime_bound, block, shift, point_count, alpha, num_primes)
            rows.append(row)
            key = (prime_bound, block, shift)
            windows[key]["active_classes"] += row["active_classes"]
            for name in ("all_u23", "all_q_one_lift", "all_q_lt_2ell", "singleton_structural"):
                windows[key][name] = windows[key][name] and row[name]
            if row["max_q_over_ell"] is not None:
                current = windows[key]["max_q_over_ell"]
                windows[key]["max_q_over_ell"] = (
                    row["max_q_over_ell"]
                    if current is None
                    else max(current, row["max_q_over_ell"])
                )
            windows[key]["u_hist"].update(row["u_hist"])
            windows[key]["lift_hist"].update(row["lift_hist"])
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["u_hist"] = dict(sorted(value["u_hist"].items()))
        value["lift_hist"] = dict(sorted(value["lift_hist"].items()))
        window_rows.append(value)
    total_u = Counter()
    total_lift = Counter()
    for row in rows:
        total_u.update(row["u_hist"])
        total_lift.update(row["lift_hist"])
    total = {
        "layers": len(rows),
        "active_classes": sum(row["active_classes"] for row in rows),
        "all_u23": all(row["all_u23"] for row in rows),
        "all_q_one_lift": all(row["all_q_one_lift"] for row in rows),
        "all_q_lt_2ell": all(row["all_q_lt_2ell"] for row in rows),
        "all_singleton_structural": all(row["singleton_structural"] for row in rows),
        "max_q_over_ell": max(
            (row["max_q_over_ell"] for row in rows if row["max_q_over_ell"] is not None),
            default=None,
        ),
        "u_hist": dict(sorted(total_u.items())),
        "lift_hist": dict(sorted(total_lift.items())),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "alpha": alpha,
        "num_primes": num_primes,
        "status": "ap_singleton_structural_sample_closed_global_open",
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出 AP 单点化结构合同表。"""
    total = package["total"]
    print(
        "scope layers active u23 q_lift1 q_lt_2ell singleton max_q_over_ell u_hist lift_hist",
        flush=True,
    )
    print(
        f"highP-total {total['layers']} {total['active_classes']} "
        f"{total['all_u23']} {total['all_q_one_lift']} {total['all_q_lt_2ell']} "
        f"{total['all_singleton_structural']} {fmt(total['max_q_over_ell'])} "
        f"{total['u_hist']} {total['lift_hist']}",
        flush=True,
    )
    print(
        "p block shift active u23 q_lift1 q_lt_2ell singleton max_q_over_ell u_hist lift_hist",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['active_classes']} "
            f"{row['all_u23']} {row['all_q_one_lift']} {row['all_q_lt_2ell']} "
            f"{row['singleton_structural']} {fmt(row['max_q_over_ell'])} "
            f"{row['u_hist']} {row['lift_hist']}",
            flush=True,
        )
    print(
        "p block shift m active u23 q_lift1 q_lt_2ell singleton max_q_over_ell "
        "u_hist lift_hist top_gaps top_ell",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['active_classes']} {row['all_u23']} {row['all_q_one_lift']} "
            f"{row['all_q_lt_2ell']} {row['singleton_structural']} "
            f"{fmt(row['max_q_over_ell'])} {row['u_hist']} {row['lift_hist']} "
            f"{row['top_gaps']} {row['top_ell']}",
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

    package = ap_singleton_structural_package(
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
