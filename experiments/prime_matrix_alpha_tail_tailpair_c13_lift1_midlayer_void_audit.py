#!/usr/bin/env python3
"""AlphaTail C13 lift=1 中间 h 层空性审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_midlayer_void_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
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
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_c13_lift1_offset_decomposition import (
    count_linear_congruence,
    h_gate_interval,
    ratio,
)
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit import ceil_div, divisors
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def midlayer_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回单层 lift=1 中间 h 层空性审计。"""
    target = row_target(
        prime_bound,
        block,
        shift,
        point_count,
        m_values,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    slack = target["geometric_upper"] - target["required_m2"]
    if not low_primes or not tail_primes:
        return {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "m": point_count,
            "slack_before_low": slack,
            "mid_lowprime_exact": 0,
            "mid_integer_ceiling": 0,
        }

    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    low_min = min(low_primes)
    low_max = max(low_primes)
    mid_h_gate_count = 0
    mid_integer_ceiling = 0
    mid_lowprime_exact = 0
    mid_gate_envelope = 0
    mid_solution_residue_hist: Counter[int] = Counter()
    h_ratio_hist: Counter[str] = Counter()
    interval_width_hist: Counter[int] = Counter()
    miss_by_lowprime_ap = 0
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
                for index in range(point_count):
                    numerator = -(index - index_a) * shift
                    for h_layer in range(1, multiplier):
                        interval = h_gate_interval(
                            numerator,
                            multiplier,
                            h_layer,
                            q_lo,
                            q_hi,
                            low_min,
                            low_max,
                        )
                        if interval is None:
                            continue
                        lo, hi = interval
                        integer_count = count_linear_congruence(
                            lo,
                            hi,
                            h_layer,
                            multiplier,
                            -numerator,
                        )
                        if integer_count == 0:
                            continue
                        mid_h_gate_count += 1
                        mid_integer_ceiling += integer_count
                        mid_gate_envelope += num_primes
                        interval_width_hist[hi - lo + 1] += 1
                        h_ratio_hist[f"{h_layer}/{multiplier}"] += 1
                        exact_count = 0
                        for low_prime in low_primes:
                            if low_prime < lo or low_prime > hi:
                                continue
                            residue_numerator = numerator + h_layer * low_prime
                            if residue_numerator % multiplier != 0:
                                continue
                            residue = residue_numerator // multiplier
                            if residue < 0 or residue >= low_prime:
                                continue
                            if (residue + gap) % low_prime == 0:
                                continue
                            q_value = low_prime + residue
                            if q_value < q_lo or q_value > q_hi:
                                continue
                            exact_count += 1
                            mid_solution_residue_hist[residue] += 1
                            if len(examples) < 8:
                                examples.append(
                                    {
                                        "ell": low_prime,
                                        "q": q_value,
                                        "residue": residue,
                                        "h": h_layer,
                                        "u": multiplier,
                                        "gap": gap,
                                        "j": index,
                                        "j1": index_a,
                                        "j2": index_b,
                                    }
                                )
                        if exact_count == 0:
                            miss_by_lowprime_ap += 1
                        mid_lowprime_exact += exact_count

    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "slack_before_low": slack,
        "mid_h_gate_count": mid_h_gate_count,
        "mid_integer_ceiling": mid_integer_ceiling,
        "mid_gate_envelope": mid_gate_envelope,
        "mid_lowprime_exact": mid_lowprime_exact,
        "miss_by_lowprime_ap": miss_by_lowprime_ap,
        "mid_void": mid_lowprime_exact == 0,
        "mid_integer_over_slack": ratio(mid_integer_ceiling, slack),
        "mid_gate_over_slack": ratio(mid_gate_envelope, slack),
        "top_h_ratios": dict(h_ratio_hist.most_common(8)),
        "top_interval_widths": dict(interval_width_hist.most_common(8)),
        "top_residues": dict(mid_solution_residue_hist.most_common(8)),
        "examples": examples,
    }


def midlayer_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回中间 h 层空性审计包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "mid_h_gate_count": 0.0,
            "mid_integer_ceiling": 0.0,
            "mid_gate_envelope": 0.0,
            "mid_lowprime_exact": 0.0,
            "miss_by_lowprime_ap": 0.0,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "mid_h_gate_count": 0.0,
        "mid_integer_ceiling": 0.0,
        "mid_gate_envelope": 0.0,
        "mid_lowprime_exact": 0.0,
        "miss_by_lowprime_ap": 0.0,
    }
    total_h_ratios: Counter[str] = Counter()
    total_widths: Counter[int] = Counter()
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = midlayer_row(
                prime_bound,
                block,
                shift,
                point_count,
                m_values,
                eta,
                alpha,
                num_primes,
                endpoint_band_theta,
            )
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in total:
                total[name] += item[name]
                windows[key][name] += item[name]
            total_h_ratios.update(item["top_h_ratios"])
            total_widths.update(item["top_interval_widths"])
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["mid_void"] = value["mid_lowprime_exact"] == 0
        value["mid_integer_over_slack"] = ratio(value["mid_integer_ceiling"], value["slack_before_low"])
        value["mid_gate_over_slack"] = ratio(value["mid_gate_envelope"], value["slack_before_low"])
        window_rows.append(value)
    total["mid_void"] = total["mid_lowprime_exact"] == 0
    total["mid_integer_over_slack"] = ratio(total["mid_integer_ceiling"], total["slack_before_low"])
    total["mid_gate_over_slack"] = ratio(total["mid_gate_envelope"], total["slack_before_low"])
    total["top_h_ratios"] = dict(total_h_ratios.most_common(8))
    total["top_interval_widths"] = dict(total_widths.most_common(8))
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出中间 h 层空性表。"""
    total = package["total"]
    print(
        "scope slack mid_exact mid_gates mid_int mid_gate_env int_slack "
        "gate_slack miss_ap mid_void h_ratios widths",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['mid_lowprime_exact']:.0f} "
        f"{total['mid_h_gate_count']:.0f} {total['mid_integer_ceiling']:.0f} "
        f"{total['mid_gate_envelope']:.0f} {fmt(total['mid_integer_over_slack'])} "
        f"{fmt(total['mid_gate_over_slack'])} {total['miss_by_lowprime_ap']:.0f} "
        f"{total['mid_void']} {total['top_h_ratios']} {total['top_interval_widths']}",
        flush=True,
    )
    print("p block shift slack mid_exact mid_gates mid_int mid_gate_env int_slack gate_slack miss_ap mid_void", flush=True)
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['mid_lowprime_exact']:.0f} "
            f"{row['mid_h_gate_count']:.0f} {row['mid_integer_ceiling']:.0f} "
            f"{row['mid_gate_envelope']:.0f} {fmt(row['mid_integer_over_slack'])} "
            f"{fmt(row['mid_gate_over_slack'])} {row['miss_by_lowprime_ap']:.0f} "
            f"{row['mid_void']}",
            flush=True,
        )
    print("p block shift m slack mid_exact mid_gates mid_int mid_gate_env int_slack gate_slack miss_ap mid_void h_ratios widths", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['mid_lowprime_exact']:.0f} "
            f"{row['mid_h_gate_count']:.0f} {row['mid_integer_ceiling']:.0f} "
            f"{row['mid_gate_envelope']:.0f} {fmt(row['mid_integer_over_slack'])} "
            f"{fmt(row['mid_gate_over_slack'])} {row['miss_by_lowprime_ap']} "
            f"{row['mid_void']} {row['top_h_ratios']} {row['top_interval_widths']}",
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

    package = midlayer_package(
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
