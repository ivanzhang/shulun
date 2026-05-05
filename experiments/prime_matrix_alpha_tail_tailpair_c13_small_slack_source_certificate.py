#!/usr/bin/env python3
"""AlphaTail C13 小余量窗口前向源槽有限证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_source_certificate.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract import active_ap_classes
from prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract import (
    low_deletion_allowance_package,
)
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit import ceil_div
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def source_key_from_ap(row: dict) -> tuple[int, int, int, int, int, int]:
    """从 AP 活跃类返回前向源槽键。"""
    return (row["m"], row["j"], row["gap"], row["u"], row["j1"], row["j2"])


def forward_source_trials(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> list[dict]:
    """枚举全部前向源槽与低素试验。"""
    row_width = abs(shift)
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_set = set(tail_primes)
    tail_min = min(tail_primes) if tail_primes else 0
    tail_max = max(tail_primes) if tail_primes else -1
    trials = []
    for low_prime in low_primes:
        for multiplier in (2, 3):
            for index_j2 in range(point_count):
                for index_j1 in range(index_j2 + 1, point_count):
                    for index_j in range(index_j1 + 1, point_count):
                        if ((index_j1 - index_j2) * row_width) % multiplier != 0:
                            continue
                        if ((index_j - index_j1) * row_width) % multiplier != 0:
                            continue
                        gap = ((index_j1 - index_j2) * row_width) // multiplier
                        lower_offset = ((index_j - index_j1) * row_width) // multiplier
                        upper_offset = ((index_j - index_j2) * row_width) // multiplier
                        q_lo = max(tail_min, ceil_div(domain_start + index_j1 * shift, multiplier))
                        q_hi = min(tail_max - gap, (domain_stop + index_j1 * shift) // multiplier)
                        q_value = low_prime + lower_offset
                        q_upper = low_prime + upper_offset
                        active = q_lo <= q_value <= q_hi and q_value in tail_set and q_upper in tail_set
                        trials.append(
                            {
                                "ell": low_prime,
                                "m": point_count,
                                "j": index_j,
                                "gap": gap,
                                "u": multiplier,
                                "j1": index_j1,
                                "j2": index_j2,
                                "lower_offset": lower_offset,
                                "upper_offset": upper_offset,
                                "q": q_value,
                                "q_plus_gap": q_upper,
                                "active": active,
                                "source_key": (
                                    point_count,
                                    index_j,
                                    gap,
                                    multiplier,
                                    index_j1,
                                    index_j2,
                                ),
                            }
                        )
    return trials


def layer_allowance_by_key(rows: list[dict]) -> dict[tuple[int, int, int, int], dict]:
    """按层键索引允许量。"""
    return {(row["p"], row["block"], row["shift"], row["m"]): row for row in rows}


def window_allowance_by_key(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引允许量。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def summarize_layer(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    allowed_deletion: float,
) -> dict:
    """返回单层有限证书摘要。"""
    trials = forward_source_trials(prime_bound, block, shift, point_count, alpha, num_primes)
    active_trials = [trial for trial in trials if trial["active"]]
    ap_rows = active_ap_classes(prime_bound, block, shift, point_count, alpha, num_primes)
    active_source_keys = {trial["source_key"] for trial in active_trials}
    ap_source_keys = {source_key_from_ap(row) for row in ap_rows}
    source_budget = ratio(allowed_deletion, num_primes)
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "forward_trials": len(trials),
        "forward_slots": len({trial["source_key"] for trial in trials}),
        "active_trials": len(active_trials),
        "active_sources": len(active_source_keys),
        "inactive_sources": len({trial["source_key"] for trial in trials}) - len(active_source_keys),
        "ap_active_rows": len(ap_rows),
        "ap_active_sources": len(ap_source_keys),
        "allowed_deletion": allowed_deletion,
        "source_budget": source_budget,
        "source_margin": None if source_budget is None else source_budget - len(active_source_keys),
        "active_trial_density": ratio(len(active_trials), len(trials)),
        "active_source_density": ratio(len(active_source_keys), len({trial["source_key"] for trial in trials})),
        "enumeration_matches_ap": len(active_trials) == len(ap_rows) and active_source_keys == ap_source_keys,
        "source_certificate_pass": source_budget is not None and len(active_source_keys) <= source_budget,
        "active_examples": active_trials[:8],
    }


def small_slack_source_certificate_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回小余量源槽有限证书包。"""
    allowance = low_deletion_allowance_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    layer_allowance = layer_allowance_by_key(allowance["rows"])
    window_allowance = window_allowance_by_key(allowance["windows"])
    layers = []
    windows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        window_layers = []
        for point_count in m_values:
            allowed = layer_allowance[(prime_bound, block, shift, point_count)]
            layer = summarize_layer(
                prime_bound,
                block,
                shift,
                point_count,
                alpha,
                num_primes,
                allowed["allowed_deletion"],
            )
            layers.append(layer)
            window_layers.append(layer)
        allowed_window = window_allowance[(prime_bound, block, shift)]
        source_budget = ratio(allowed_window["allowed_deletion"], num_primes)
        active_sources = sum(row["active_sources"] for row in window_layers)
        forward_slots = sum(row["forward_slots"] for row in window_layers)
        forward_trials = sum(row["forward_trials"] for row in window_layers)
        active_trials = sum(row["active_trials"] for row in window_layers)
        windows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "forward_trials": forward_trials,
                "forward_slots": forward_slots,
                "active_trials": active_trials,
                "active_sources": active_sources,
                "inactive_sources": forward_slots - active_sources,
                "allowed_deletion": allowed_window["allowed_deletion"],
                "source_budget": source_budget,
                "source_margin": None if source_budget is None else source_budget - active_sources,
                "active_trial_density": ratio(active_trials, forward_trials),
                "active_source_density": ratio(active_sources, forward_slots),
                "enumeration_matches_ap": all(row["enumeration_matches_ap"] for row in window_layers),
                "source_certificate_pass": source_budget is not None and active_sources <= source_budget,
                "coarse_slot_pay": num_primes * forward_slots <= allowed_window["allowed_deletion"],
                "small_slack_certificate": num_primes * forward_slots > allowed_window["allowed_deletion"]
                and source_budget is not None
                and active_sources <= source_budget,
            }
        )
    total_source_budget = ratio(sum(row["allowed_deletion"] for row in windows), num_primes)
    total_active_sources = sum(row["active_sources"] for row in windows)
    total = {
        "windows": len(windows),
        "forward_trials": sum(row["forward_trials"] for row in windows),
        "forward_slots": sum(row["forward_slots"] for row in windows),
        "active_trials": sum(row["active_trials"] for row in windows),
        "active_sources": total_active_sources,
        "allowed_deletion": sum(row["allowed_deletion"] for row in windows),
        "source_budget": total_source_budget,
        "source_margin": None if total_source_budget is None else total_source_budget - total_active_sources,
        "all_enumeration_matches_ap": all(row["enumeration_matches_ap"] for row in windows),
        "all_source_certificate_pass": all(row["source_certificate_pass"] for row in windows),
        "small_slack_windows": sum(row["small_slack_certificate"] for row in windows),
        "min_source_margin": min((row["source_margin"] for row in windows), default=None),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "small_slack_source_certificate_sample_closed_global_open",
        "total": total,
        "windows": windows,
        "layers": layers,
        "allowance": allowance,
    }


def print_table(package: dict) -> None:
    """输出小余量源槽有限证书表。"""
    total = package["total"]
    print(
        "scope windows trials slots active_trials active_sources allowed source_budget "
        "source_margin matches cert_pass small_slack min_source_margin",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['forward_trials']} "
        f"{total['forward_slots']} {total['active_trials']} {total['active_sources']} "
        f"{total['allowed_deletion']:.6f} {fmt(total['source_budget'])} "
        f"{fmt(total['source_margin'])} {total['all_enumeration_matches_ap']} "
        f"{total['all_source_certificate_pass']} {total['small_slack_windows']} "
        f"{fmt(total['min_source_margin'])}",
        flush=True,
    )
    print(
        "p block shift trials slots active_trials active_sources inactive_sources "
        "allowed source_budget source_margin trial_dens source_dens matches cert_pass "
        "coarse_pay small_slack",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['forward_trials']} "
            f"{row['forward_slots']} {row['active_trials']} {row['active_sources']} "
            f"{row['inactive_sources']} {row['allowed_deletion']:.6f} "
            f"{fmt(row['source_budget'])} {fmt(row['source_margin'])} "
            f"{fmt(row['active_trial_density'])} {fmt(row['active_source_density'])} "
            f"{row['enumeration_matches_ap']} {row['source_certificate_pass']} "
            f"{row['coarse_slot_pay']} {row['small_slack_certificate']}",
            flush=True,
        )
    print(
        "p block shift m trials slots active_trials active_sources inactive_sources "
        "allowed source_budget source_margin trial_dens source_dens matches cert_pass",
        flush=True,
    )
    for row in package["layers"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['forward_trials']} {row['forward_slots']} "
            f"{row['active_trials']} {row['active_sources']} {row['inactive_sources']} "
            f"{row['allowed_deletion']:.6f} {fmt(row['source_budget'])} "
            f"{fmt(row['source_margin'])} {fmt(row['active_trial_density'])} "
            f"{fmt(row['active_source_density'])} {row['enumeration_matches_ap']} "
            f"{row['source_certificate_pass']}",
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

    package = small_slack_source_certificate_package(
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
