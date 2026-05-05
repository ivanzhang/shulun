#!/usr/bin/env python3
"""AlphaTail C13 小余量窗口有限化归约合同。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_finite_reduction_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_small_slack_source_certificate import (
    small_slack_source_certificate_package,
)
from prime_matrix_alpha_tail_tailpair_c13_source_slot_structural_contract import (
    source_slot_structural_package,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def by_key(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def small_slack_finite_reduction_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回小余量窗口有限化归约合同包。"""
    source_slot = source_slot_structural_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    source_certificate = small_slack_source_certificate_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    cert_by_window = by_key(source_certificate["windows"])
    windows = []
    finite_keys = []
    for row in source_slot["windows"]:
        key = (row["p"], row["block"], row["shift"])
        cert = cert_by_window[key]
        large_slack_exit = row["coarse_slot_pay"]
        small_slack_exit = (not large_slack_exit) and cert["source_certificate_pass"]
        if small_slack_exit:
            finite_keys.append({"p": row["p"], "block": row["block"], "shift": row["shift"]})
        windows.append(
            {
                "p": row["p"],
                "block": row["block"],
                "shift": row["shift"],
                "class_ceiling": row["class_ceiling"],
                "allowed_deletion": row["allowed_deletion"],
                "coarse_margin": row["class_ceiling_margin"],
                "source_budget": cert["source_budget"],
                "active_sources": cert["active_sources"],
                "source_margin": cert["source_margin"],
                "large_slack_exit": large_slack_exit,
                "small_slack_exit": small_slack_exit,
                "finite_exit_pass": large_slack_exit or small_slack_exit,
                "enumeration_matches_ap": cert["enumeration_matches_ap"],
            }
        )
    total = {
        "windows": len(windows),
        "large_slack_windows": sum(row["large_slack_exit"] for row in windows),
        "small_slack_windows": sum(row["small_slack_exit"] for row in windows),
        "finite_exit_windows": sum(row["finite_exit_pass"] for row in windows),
        "all_finite_exit_pass": all(row["finite_exit_pass"] for row in windows),
        "all_enumeration_matches_ap": all(row["enumeration_matches_ap"] for row in windows),
        "min_coarse_margin": min((row["coarse_margin"] for row in windows), default=None),
        "min_source_margin": min((row["source_margin"] for row in windows), default=None),
        "finite_keys": finite_keys,
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "small_slack_finite_reduction_sample_closed_generator_open",
        "total": total,
        "windows": windows,
        "source_slot": source_slot,
        "source_certificate": source_certificate,
    }


def print_table(package: dict) -> None:
    """输出小余量有限化归约表。"""
    total = package["total"]
    print(
        "scope windows large_slack small_slack finite_exit all_pass matches "
        "min_coarse_margin min_source_margin finite_keys",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['large_slack_windows']} "
        f"{total['small_slack_windows']} {total['finite_exit_windows']} "
        f"{total['all_finite_exit_pass']} {total['all_enumeration_matches_ap']} "
        f"{fmt(total['min_coarse_margin'])} {fmt(total['min_source_margin'])} "
        f"{total['finite_keys']}",
        flush=True,
    )
    print(
        "p block shift class_ceiling allowed coarse_margin source_budget "
        "active_sources source_margin large_exit small_exit finite_exit matches",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['class_ceiling']} "
            f"{row['allowed_deletion']:.6f} {row['coarse_margin']:.6f} "
            f"{fmt(row['source_budget'])} {row['active_sources']} "
            f"{fmt(row['source_margin'])} {row['large_slack_exit']} "
            f"{row['small_slack_exit']} {row['finite_exit_pass']} "
            f"{row['enumeration_matches_ap']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = small_slack_finite_reduction_package(
        args.selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.endpoint_band_theta,
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
