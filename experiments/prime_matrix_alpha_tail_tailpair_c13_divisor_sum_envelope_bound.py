#!/usr/bin/env python3
"""AlphaTail C13 几何 envelope 的除数和闭式上界。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_divisor_sum_envelope_bound.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
import math

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_group_u_distribution import group_u_distribution_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def divisors(value: int) -> list[int]:
    """返回正整数的所有正因子。"""
    result = []
    for candidate in range(1, int(value**0.5) + 1):
        if value % candidate == 0:
            result.append(candidate)
            if candidate * candidate != value:
                result.append(value // candidate)
    return sorted(result)


def sigma_minus_one(value: int) -> float:
    """返回 sigma_{-1}(value)=sum_{d|value}1/d。"""
    return sum(1.0 / divisor for divisor in divisors(value))


def window_divisor_bounds(
    prime_bound: int,
    block: int,
    shift: int,
    m_values: list[int],
    endpoint_band_theta: float,
    eta: float,
) -> dict:
    """返回单个窗口的除数和 envelope 上界。"""
    shift_abs = abs(shift)
    max_domain_length = max(
        domain_bounds(block, shift, point_count)[1] - domain_bounds(block, shift, point_count)[0] + 1
        for point_count in m_values
    )
    exact_even_floor_bound = 0
    tau_sigma_bound = 0.0
    terms = []
    for point_count in m_values:
        for delta in range(1, point_count):
            multiplicity = point_count - delta
            value = delta * shift_abs
            all_divisors = divisors(value)
            even_divisors = [u_value for u_value in all_divisors if (value // u_value) % 2 == 0]
            exact_term = multiplicity * sum(
                1 + int(endpoint_band_theta * max_domain_length) // u_value
                for u_value in even_divisors
            )
            crude_term = multiplicity * (
                len(all_divisors) + endpoint_band_theta * max_domain_length * sigma_minus_one(value)
            )
            exact_even_floor_bound += exact_term
            tau_sigma_bound += crude_term
            terms.append(
                {
                    "m": point_count,
                    "delta": delta,
                    "value": value,
                    "multiplicity": multiplicity,
                    "divisor_count": len(all_divisors),
                    "even_divisor_count": len(even_divisors),
                    "exact_term": exact_term,
                    "tau_sigma_term": crude_term,
                }
            )
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "shift_abs": shift_abs,
        "max_domain_length": max_domain_length,
        "exact_even_floor_bound": exact_even_floor_bound,
        "tau_sigma_bound": tau_sigma_bound,
        "capacity_exact_even": len(m_values) * eta * exact_even_floor_bound,
        "capacity_tau_sigma": len(m_values) * eta * tau_sigma_bound,
        "terms": terms,
    }


def divisor_sum_package(
    selected: str,
    m_values: list[int],
    endpoint_band_theta: float,
    eta: float,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
) -> dict:
    """返回除数和上界包，并附带几何去重 envelope 作比较。"""
    windows = [
        window_divisor_bounds(prime_bound, block, shift, m_values, endpoint_band_theta, eta)
        for prime_bound, block, shift in parse_selected(selected)
    ]
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
    geometric_row = next(row for row in distribution["rows"] if row["mode"] == "geometric")
    geometric_by_window = {
        (row["p"], row["block"], row["shift"]): row
        for row in geometric_row["window_rows"]
    }
    for window in windows:
        geo = geometric_by_window.get((window["p"], window["block"], window["shift"]), {})
        window["geometric_dedup_env"] = geo.get("deterministic_env", 0)
        window["exact_over_dedup"] = (
            window["exact_even_floor_bound"] / window["geometric_dedup_env"]
            if window["geometric_dedup_env"]
            else None
        )
        window["tau_sigma_over_dedup"] = (
            window["tau_sigma_bound"] / window["geometric_dedup_env"]
            if window["geometric_dedup_env"]
            else None
        )
    total_exact = sum(window["exact_even_floor_bound"] for window in windows)
    total_tau_sigma = sum(window["tau_sigma_bound"] for window in windows)
    total_dedup = sum(window["geometric_dedup_env"] for window in windows)
    return {
        "selected": selected,
        "m_values": m_values,
        "endpoint_band_theta": endpoint_band_theta,
        "eta": eta,
        "geometric_dedup_env": total_dedup,
        "exact_even_floor_bound": total_exact,
        "tau_sigma_bound": total_tau_sigma,
        "capacity_dedup": len(m_values) * eta * total_dedup,
        "capacity_exact_even": len(m_values) * eta * total_exact,
        "capacity_tau_sigma": len(m_values) * eta * total_tau_sigma,
        "exact_over_dedup": total_exact / total_dedup if total_dedup else None,
        "tau_sigma_over_dedup": total_tau_sigma / total_dedup if total_dedup else None,
        "windows": windows,
    }


def print_table(package: dict) -> None:
    """输出除数和上界表。"""
    print(
        "dedup_env exact_even_bound tau_sigma_bound capacity_dedup "
        "capacity_exact capacity_tau_sigma exact_over_dedup tau_over_dedup eta",
        flush=True,
    )
    print(
        f"{package['geometric_dedup_env']} {package['exact_even_floor_bound']} "
        f"{package['tau_sigma_bound']:.6f} {package['capacity_dedup']:.6f} "
        f"{package['capacity_exact_even']:.6f} {package['capacity_tau_sigma']:.6f} "
        f"{(package['exact_over_dedup'] or 0.0):.6f} "
        f"{(package['tau_sigma_over_dedup'] or 0.0):.6f} {package['eta']:.6f}",
        flush=True,
    )
    print(
        "p block shift Lmax dedup_env exact_even tau_sigma cap_exact cap_tau exact_over tau_over",
        flush=True,
    )
    for window in package["windows"]:
        print(
            f"{window['p']} {window['block']} {window['shift']} {window['max_domain_length']} "
            f"{window['geometric_dedup_env']} {window['exact_even_floor_bound']} "
            f"{window['tau_sigma_bound']:.6f} {window['capacity_exact_even']:.6f} "
            f"{window['capacity_tau_sigma']:.6f} "
            f"{(window['exact_over_dedup'] or 0.0):.6f} "
            f"{(window['tau_sigma_over_dedup'] or 0.0):.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = divisor_sum_package(
        args.selected,
        parse_m_values(args.m_values),
        args.endpoint_band_theta,
        args.eta,
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
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
