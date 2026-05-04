#!/usr/bin/env python3
"""AlphaTail C13 低 P 有限几何 group 证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowp_finite_certificate.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_group_u_distribution import (
    deterministic_slots,
    endpoint_epsilon,
    endpoint_side_from_bounds,
    geometric_records,
    include_record,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_resonance_budget_audit import budget_row


def lowp_finite_certificate(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    alpha: float,
    num_primes: int,
    endpoint_theta: float,
    endpoint_band_theta: float,
    eta: float,
    top: int,
) -> dict:
    """返回低 P 几何 group 有限证书。"""
    groups: dict[tuple, dict] = {}
    window_records: dict[tuple[int, int, int], int] = {}
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound > finite_p_cut:
            continue
        window_key = (prime_bound, block, shift)
        window_records[window_key] = 0
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            for record in geometric_records(prime_bound, block, shift, point_count):
                if not include_record(record, "geometric", 0):
                    continue
                if record["u"] > endpoint_theta * domain_length:
                    continue
                side = endpoint_side_from_bounds(
                    record["d_lower"],
                    record["d_upper"],
                    domain_start,
                    domain_stop,
                )
                epsilon = endpoint_epsilon(
                    side,
                    record["d_lower"],
                    record["d_upper"],
                    domain_start,
                    domain_stop,
                    record["u"],
                )
                shape_key = (record["gap"], record["j1"], record["j2"], record["u"], side)
                group_key = (prime_bound, block, shift, shape_key, epsilon)
                window_records[window_key] += 1
                if group_key in groups:
                    groups[group_key]["support_m"].add(point_count)
                    groups[group_key]["record_count"] += 1
                    continue
                slots = deterministic_slots(
                    block,
                    shift,
                    m_values,
                    record["u"],
                    epsilon,
                    endpoint_band_theta,
                )
                groups[group_key] = {
                    "p": prime_bound,
                    "block": block,
                    "shift": shift,
                    "shape_key": shape_key,
                    "epsilon": epsilon,
                    "u": record["u"],
                    "slots": slots,
                    "record_count": 1,
                    "support_m": {point_count},
                    "q_lower": record["q_lower"],
                    "q_upper": record["q_upper"],
                }

    rows = []
    for item in groups.values():
        rows.append({**item, "support_m": sorted(item["support_m"])})
    rows.sort(key=lambda item: (-item["slots"], item["p"], item["shape_key"], item["epsilon"]))

    windows = []
    total_d2 = 0.0
    total_equal = 0
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound > finite_p_cut:
            continue
        key = (prime_bound, block, shift)
        window_groups = [
            row for row in rows if (row["p"], row["block"], row["shift"]) == key
        ]
        d2 = 0.0
        equal_multiplier = 0
        for point_count in m_values:
            budget = budget_row(prime_bound, block, shift, point_count, alpha, num_primes)
            d2 += budget["d2"]
            equal_multiplier += budget["equal_multiplier"]
        slots = sum(row["slots"] for row in window_groups)
        capacity = len(m_values) * eta * slots
        total_d2 += d2
        total_equal += equal_multiplier
        windows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "records": window_records.get(key, 0),
                "groups": len(window_groups),
                "slots": slots,
                "capacity": capacity,
                "d2": d2,
                "equal_multiplier": equal_multiplier,
                "capacity_over_d2": capacity / d2 if d2 else None,
                "capacity_over_equal": capacity / equal_multiplier if equal_multiplier else None,
            }
        )

    total_slots = sum(row["slots"] for row in rows)
    total_capacity = len(m_values) * eta * total_slots
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_theta": endpoint_theta,
        "endpoint_band_theta": endpoint_band_theta,
        "eta": eta,
        "window_count": len(windows),
        "group_count": len(rows),
        "slot_count": total_slots,
        "capacity": total_capacity,
        "d2": total_d2,
        "equal_multiplier": total_equal,
        "capacity_over_d2": total_capacity / total_d2 if total_d2 else None,
        "capacity_over_equal": total_capacity / total_equal if total_equal else None,
        "windows": windows,
        "groups": rows[:top],
    }


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def print_table(package: dict) -> None:
    """输出低 P 有限证书表。"""
    print(
        "finite_cut windows groups slots capacity D2 equal cap_D2 cap_equal eta",
        flush=True,
    )
    print(
        f"{package['finite_p_cut']} {package['window_count']} {package['group_count']} "
        f"{package['slot_count']} {package['capacity']:.6f} {package['d2']:.6f} "
        f"{package['equal_multiplier']} {fmt(package['capacity_over_d2'])} "
        f"{fmt(package['capacity_over_equal'])} {package['eta']:.6f}",
        flush=True,
    )
    print("windows p block shift records groups slots capacity D2 cap_D2 cap_equal", flush=True)
    for window in package["windows"]:
        print(
            f"{window['p']} {window['block']} {window['shift']} "
            f"{window['records']} {window['groups']} {window['slots']} "
            f"{window['capacity']:.6f} {window['d2']:.6f} "
            f"{fmt(window['capacity_over_d2'])} {fmt(window['capacity_over_equal'])}",
            flush=True,
        )
    print("top_groups shape eps p slots records support_m q_interval", flush=True)
    for row in package["groups"]:
        shape = (
            f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-"
            f"{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        )
        support_m = ",".join(str(value) for value in row["support_m"])
        print(
            f"{shape} eps{row['epsilon']} {row['p']} {row['slots']} "
            f"{row['record_count']} {support_m} [{row['q_lower']},{row['q_upper']}]",
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
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = lowp_finite_certificate(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.alpha,
        args.num_primes,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.eta,
        args.top,
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
