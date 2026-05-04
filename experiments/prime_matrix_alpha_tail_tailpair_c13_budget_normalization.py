#!/usr/bin/env python3
"""AlphaTail C13 除数外壳与二阶共振预算的归一化比较。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_budget_normalization.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_divisor_sum_envelope_bound import divisor_sum_package
from prime_matrix_alpha_tail_tailpair_c13_group_u_distribution import group_u_distribution_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_resonance_budget_audit import budget_row


def c13_capacity_by_window(
    selected: str,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
) -> dict[tuple[int, int, int], dict]:
    """返回每个窗口的 C13 几何/失败容量。"""
    divisor = divisor_sum_package(
        selected,
        m_values,
        endpoint_band_theta,
        eta,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        slack_cut,
    )
    distribution = group_u_distribution_package(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        endpoint_band_theta,
        slack_cut,
        eta,
    )
    mode_windows: dict[str, dict[tuple[int, int, int], dict]] = {}
    for row in distribution["rows"]:
        mode_windows[row["mode"]] = {
            (window["p"], window["block"], window["shift"]): window
            for window in row["window_rows"]
        }
    result = {}
    for window in divisor["windows"]:
        key = (window["p"], window["block"], window["shift"])
        result[key] = {
            "p": window["p"],
            "block": window["block"],
            "shift": window["shift"],
            "capacity_tau_sigma": window["capacity_tau_sigma"],
            "capacity_exact_even": window["capacity_exact_even"],
            "capacity_geometric_dedup": 2 * eta * window["geometric_dedup_env"],
            "capacity_failure": mode_windows["failure"].get(key, {}).get("capacity", 0.0),
            "capacity_narrow": mode_windows["narrow"].get(key, {}).get("capacity", 0.0),
            "capacity_positive": mode_windows["positive"].get(key, {}).get("capacity", 0.0),
        }
    return result


def resonance_by_window(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
) -> dict[tuple[int, int, int], dict]:
    """按窗口合并 m 层二阶共振预算。"""
    rows: defaultdict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "low_count": 0,
            "m2": 0,
            "b2_model": 0.0,
            "d2": 0.0,
            "equal_multiplier": 0,
            "unit_multiplier": 0,
            "non_equal": 0,
        }
    )
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            item = budget_row(prime_bound, block, shift, point_count, alpha, num_primes)
            key = (prime_bound, block, shift)
            row = rows[key]
            row["low_count"] += item["low_count"]
            row["m2"] += item["m2"]
            row["b2_model"] += item["b2_model"]
            row["d2"] += item["d2"]
            row["equal_multiplier"] += item["equal_multiplier"]
            row["unit_multiplier"] += item["unit_multiplier"]
            row["non_equal"] += item["non_equal"]
    return {
        key: {"p": key[0], "block": key[1], "shift": key[2], **value}
        for key, value in rows.items()
    }


def ratio(numerator: float, denominator: float) -> float | None:
    """安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def budget_normalization_package(
    selected: str,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
) -> dict:
    """返回 C13 容量相对二阶预算的归一化比较。"""
    capacities = c13_capacity_by_window(
        selected,
        m_values,
        eta,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        endpoint_band_theta,
        slack_cut,
    )
    resonances = resonance_by_window(selected, m_values, alpha, num_primes)
    rows = []
    total = {
        "capacity_tau_sigma": 0.0,
        "capacity_exact_even": 0.0,
        "capacity_geometric_dedup": 0.0,
        "capacity_failure": 0.0,
        "capacity_narrow": 0.0,
        "capacity_positive": 0.0,
        "low_count": 0,
        "m2": 0,
        "b2_model": 0.0,
        "d2": 0.0,
        "equal_multiplier": 0,
        "unit_multiplier": 0,
        "non_equal": 0,
    }
    for key in sorted(capacities):
        capacity = capacities[key]
        resonance = resonances.get(key, {})
        row = {**capacity, **resonance}
        for name in list(total):
            total[name] += row.get(name, 0)
        row["tau_over_d2"] = ratio(row["capacity_tau_sigma"], row.get("d2", 0.0))
        row["exact_over_d2"] = ratio(row["capacity_exact_even"], row.get("d2", 0.0))
        row["failure_over_d2"] = ratio(row["capacity_failure"], row.get("d2", 0.0))
        row["tau_over_equal"] = ratio(row["capacity_tau_sigma"], row.get("equal_multiplier", 0.0))
        row["exact_over_equal"] = ratio(row["capacity_exact_even"], row.get("equal_multiplier", 0.0))
        rows.append(row)
    total["tau_over_d2"] = ratio(total["capacity_tau_sigma"], total["d2"])
    total["exact_over_d2"] = ratio(total["capacity_exact_even"], total["d2"])
    total["failure_over_d2"] = ratio(total["capacity_failure"], total["d2"])
    total["tau_over_equal"] = ratio(total["capacity_tau_sigma"], total["equal_multiplier"])
    total["exact_over_equal"] = ratio(total["capacity_exact_even"], total["equal_multiplier"])
    return {
        "selected": selected,
        "m_values": m_values,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "endpoint_band_theta": endpoint_band_theta,
        "slack_cut": slack_cut,
        "total": total,
        "rows": rows,
    }


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def print_table(package: dict) -> None:
    """输出归一化预算表。"""
    total = package["total"]
    print(
        "scope cap_tau cap_exact cap_failure D2 equal M2 tau_D2 exact_D2 "
        "failure_D2 tau_equal exact_equal",
        flush=True,
    )
    print(
        f"total {total['capacity_tau_sigma']:.6f} {total['capacity_exact_even']:.6f} "
        f"{total['capacity_failure']:.6f} {total['d2']:.6f} {total['equal_multiplier']} "
        f"{total['m2']} {fmt(total['tau_over_d2'])} {fmt(total['exact_over_d2'])} "
        f"{fmt(total['failure_over_d2'])} {fmt(total['tau_over_equal'])} "
        f"{fmt(total['exact_over_equal'])}",
        flush=True,
    )
    print("p block shift cap_tau cap_exact cap_failure D2 equal M2 tau_D2 exact_D2 failure_D2", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['capacity_tau_sigma']:.6f} {row['capacity_exact_even']:.6f} "
            f"{row['capacity_failure']:.6f} {row['d2']:.6f} "
            f"{row['equal_multiplier']} {row['m2']} "
            f"{fmt(row['tau_over_d2'])} {fmt(row['exact_over_d2'])} "
            f"{fmt(row['failure_over_d2'])}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = budget_normalization_package(
        args.selected,
        parse_m_values(args.m_values),
        args.eta,
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
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
