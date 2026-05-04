#!/usr/bin/env python3
"""AlphaTail C13 lift=1 offset/h-layer 分解审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_offset_decomposition.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit import (
    ceil_div,
    count_progression,
    divisors,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def count_linear_congruence(lo: int, hi: int, coefficient: int, modulus: int, rhs: int) -> int:
    """计数 coefficient*x == rhs (mod modulus) 在区间内的整数解。"""
    if hi < lo:
        return 0
    if modulus == 1:
        return hi - lo + 1
    coefficient %= modulus
    rhs %= modulus
    divisor = math.gcd(coefficient, modulus)
    if rhs % divisor != 0:
        return 0
    reduced_modulus = modulus // divisor
    if reduced_modulus == 1:
        return hi - lo + 1
    reduced_coefficient = coefficient // divisor
    reduced_rhs = rhs // divisor
    residue = (reduced_rhs * pow(reduced_coefficient, -1, reduced_modulus)) % reduced_modulus
    return count_progression(lo, hi, reduced_modulus, residue)


def h_gate_interval(
    numerator: int,
    multiplier: int,
    h_layer: int,
    q_lo: int,
    q_hi: int,
    low_min: int,
    low_max: int,
) -> tuple[int, int] | None:
    """返回给定 h 层允许的 ell 区间；空时返回 None。"""
    denominator = multiplier + h_layer
    lo = max(low_min, ceil_div(multiplier * q_lo - numerator, denominator))
    hi = min(low_max, (multiplier * q_hi - numerator) // denominator)

    # 约束 a=(numerator+h*ell)/u 满足 0<=a<ell。
    if h_layer == 0:
        if numerator < 0:
            return None
    else:
        lo = max(lo, ceil_div(-numerator, h_layer))
    if h_layer == multiplier:
        if numerator >= 0:
            return None
    else:
        lo = max(lo, numerator // (multiplier - h_layer) + 1)

    if hi < lo:
        return None
    return lo, hi


def lift1_offset_row(
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
    """返回单层 lift=1 offset/h-layer 分解。"""
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
            "lift1_candidates": 0,
            "h_gate_lowprime_exact": 0,
            "edge_lowprime_exact": 0,
            "mid_lowprime_exact": 0,
            "h_gate_integer_ceiling": 0,
            "exact_identity_ok": True,
            "lowprime_gate_identity_ok": True,
        }

    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    low_min = min(low_primes)
    low_max = max(low_primes)
    lift1_candidates = 0
    h_gate_lowprime_exact = 0
    edge_lowprime_exact = 0
    mid_lowprime_exact = 0
    h_gate_integer_ceiling = 0
    all_channels = set()
    lift1_channels = set()
    h_gate_channels = 0
    offset_hist: Counter[int] = Counter()
    edge_hist: Counter[int] = Counter()
    h_hist: Counter[int] = Counter()
    side_hist: Counter[str] = Counter()
    h_kind_hist: Counter[str] = Counter()
    channel_candidate_hist: Counter[tuple[int, int, int, int]] = Counter()
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
                    channel = (index_a, index_b, multiplier, gap, index)
                    all_channels.add(channel)
                    for h_layer in range(multiplier + 1):
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
                        count = count_linear_congruence(lo, hi, h_layer, multiplier, -numerator)
                        if count:
                            h_gate_channels += 1
                            h_gate_integer_ceiling += count
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
                            h_gate_lowprime_exact += 1
                            if h_layer == 0 or h_layer == multiplier:
                                edge_lowprime_exact += 1
                            else:
                                mid_lowprime_exact += 1
                    for low_prime in low_primes:
                        inverse = pow(multiplier, -1, low_prime)
                        residue = (numerator * inverse) % low_prime
                        if (residue + gap) % low_prime == 0:
                            continue
                        q_value = low_prime + residue
                        if q_value < q_lo or q_value > q_hi:
                            continue
                        h_numerator = multiplier * residue - numerator
                        if h_numerator % low_prime != 0:
                            raise AssertionError("h-layer identity failed")
                        h_layer = h_numerator // low_prime
                        recomposed_q = ((multiplier + h_layer) * low_prime + numerator) // multiplier
                        if recomposed_q != q_value:
                            raise AssertionError("q recomposition failed")
                        lift1_candidates += 1
                        lift1_channels.add(channel)
                        offset_hist[residue] += 1
                        edge_hist[min(residue, low_prime - residue)] += 1
                        h_hist[h_layer] += 1
                        side_hist["head" if residue <= low_prime // 2 else "tail"] += 1
                        if h_layer == 0:
                            h_kind = "h0_head_integer"
                        elif h_layer == multiplier:
                            h_kind = "hu_tail_integer"
                        else:
                            h_kind = "hmid_fractional"
                        h_kind_hist[h_kind] += 1
                        channel_candidate_hist[(index_a, index_b, multiplier, index)] += 1
                        if len(examples) < 8:
                            examples.append(
                                {
                                    "ell": low_prime,
                                    "q": q_value,
                                    "residue": residue,
                                    "edge": min(residue, low_prime - residue),
                                    "h": h_layer,
                                    "u": multiplier,
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
        "slack_before_low": slack,
        "lift1_candidates": lift1_candidates,
        "h_gate_lowprime_exact": h_gate_lowprime_exact,
        "edge_lowprime_exact": edge_lowprime_exact,
        "mid_lowprime_exact": mid_lowprime_exact,
        "all_channel_count": len(all_channels),
        "lift1_channel_count": len(lift1_channels),
        "h_gate_channel_count": h_gate_channels,
        "h_gate_integer_ceiling": h_gate_integer_ceiling,
        "lowprime_gate_over_lift1": ratio(h_gate_lowprime_exact, lift1_candidates),
        "h_gate_over_lift1": ratio(h_gate_integer_ceiling, lift1_candidates),
        "lift1_margin": slack - lift1_candidates,
        "h_gate_margin": slack - h_gate_integer_ceiling,
        "lift1_over_slack": ratio(lift1_candidates, slack),
        "h_gate_over_slack": ratio(h_gate_integer_ceiling, slack),
        "exact_identity_ok": lift1_candidates <= h_gate_integer_ceiling,
        "lowprime_gate_identity_ok": h_gate_lowprime_exact == lift1_candidates,
        "edge_mid_identity_ok": edge_lowprime_exact + mid_lowprime_exact == lift1_candidates,
        "top_offsets": dict(offset_hist.most_common(8)),
        "top_edges": dict(edge_hist.most_common(8)),
        "h_hist": dict(sorted(h_hist.items())),
        "side_hist": dict(sorted(side_hist.items())),
        "h_kind_hist": dict(sorted(h_kind_hist.items())),
        "top_channels": [
            {
                "j1": key[0],
                "j2": key[1],
                "u": key[2],
                "j": key[3],
                "count": count,
            }
            for key, count in channel_candidate_hist.most_common(8)
        ],
        "examples": examples,
    }


def lift1_offset_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 lift=1 offset/h-layer 分解包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "lift1_candidates": 0.0,
            "h_gate_lowprime_exact": 0.0,
            "edge_lowprime_exact": 0.0,
            "mid_lowprime_exact": 0.0,
            "all_channel_count": 0.0,
            "lift1_channel_count": 0.0,
            "h_gate_channel_count": 0.0,
            "h_gate_integer_ceiling": 0.0,
            "exact_identity_ok": True,
            "lowprime_gate_identity_ok": True,
            "edge_mid_identity_ok": True,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "lift1_candidates": 0.0,
        "h_gate_lowprime_exact": 0.0,
        "edge_lowprime_exact": 0.0,
        "mid_lowprime_exact": 0.0,
        "all_channel_count": 0.0,
        "lift1_channel_count": 0.0,
        "h_gate_channel_count": 0.0,
        "h_gate_integer_ceiling": 0.0,
        "exact_identity_ok": True,
        "lowprime_gate_identity_ok": True,
        "edge_mid_identity_ok": True,
    }
    total_h_kind: Counter[str] = Counter()
    total_side: Counter[str] = Counter()
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = lift1_offset_row(
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
            for name in (
                "slack_before_low",
                "lift1_candidates",
                "h_gate_lowprime_exact",
                "edge_lowprime_exact",
                "mid_lowprime_exact",
                "all_channel_count",
                "lift1_channel_count",
                "h_gate_channel_count",
                "h_gate_integer_ceiling",
            ):
                total[name] += item[name]
                windows[key][name] += item[name]
            total["exact_identity_ok"] = total["exact_identity_ok"] and item["exact_identity_ok"]
            windows[key]["exact_identity_ok"] = windows[key]["exact_identity_ok"] and item["exact_identity_ok"]
            total["lowprime_gate_identity_ok"] = (
                total["lowprime_gate_identity_ok"] and item["lowprime_gate_identity_ok"]
            )
            windows[key]["lowprime_gate_identity_ok"] = (
                windows[key]["lowprime_gate_identity_ok"] and item["lowprime_gate_identity_ok"]
            )
            total["edge_mid_identity_ok"] = total["edge_mid_identity_ok"] and item["edge_mid_identity_ok"]
            windows[key]["edge_mid_identity_ok"] = (
                windows[key]["edge_mid_identity_ok"] and item["edge_mid_identity_ok"]
            )
            total_h_kind.update(item["h_kind_hist"])
            total_side.update(item["side_hist"])

    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["lift1_margin"] = value["slack_before_low"] - value["lift1_candidates"]
        value["h_gate_margin"] = value["slack_before_low"] - value["h_gate_integer_ceiling"]
        value["lift1_over_slack"] = ratio(value["lift1_candidates"], value["slack_before_low"])
        value["h_gate_over_slack"] = ratio(value["h_gate_integer_ceiling"], value["slack_before_low"])
        value["h_gate_over_lift1"] = ratio(value["h_gate_integer_ceiling"], value["lift1_candidates"])
        value["lowprime_gate_over_lift1"] = ratio(value["h_gate_lowprime_exact"], value["lift1_candidates"])
        window_rows.append(value)
    total["lift1_margin"] = total["slack_before_low"] - total["lift1_candidates"]
    total["h_gate_margin"] = total["slack_before_low"] - total["h_gate_integer_ceiling"]
    total["lift1_over_slack"] = ratio(total["lift1_candidates"], total["slack_before_low"])
    total["h_gate_over_slack"] = ratio(total["h_gate_integer_ceiling"], total["slack_before_low"])
    total["h_gate_over_lift1"] = ratio(total["h_gate_integer_ceiling"], total["lift1_candidates"])
    total["lowprime_gate_over_lift1"] = ratio(total["h_gate_lowprime_exact"], total["lift1_candidates"])
    total["h_kind_hist"] = dict(sorted(total_h_kind.items()))
    total["side_hist"] = dict(sorted(total_side.items()))
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
    """输出 lift=1 offset/h-layer 分解表。"""
    total = package["total"]
    print(
        "scope slack lift1 exact_hgate edge mid h_gate hgate_lift1 "
        "exact_lift1 lift1_slack hgate_slack lift1_margin hgate_margin "
        "channels lift1_channels h_gate_channels h_kind side identity exact_identity",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['lift1_candidates']:.0f} "
        f"{total['h_gate_lowprime_exact']:.0f} {total['edge_lowprime_exact']:.0f} "
        f"{total['mid_lowprime_exact']:.0f} {total['h_gate_integer_ceiling']:.0f} "
        f"{fmt(total['h_gate_over_lift1'])} {fmt(total['lowprime_gate_over_lift1'])} "
        f"{fmt(total['lift1_over_slack'])} {fmt(total['h_gate_over_slack'])} "
        f"{total['lift1_margin']:.6f} {total['h_gate_margin']:.6f} "
        f"{total['all_channel_count']:.0f} {total['lift1_channel_count']:.0f} "
        f"{total['h_gate_channel_count']:.0f} {total['h_kind_hist']} "
        f"{total['side_hist']} {total['exact_identity_ok']} "
        f"{total['lowprime_gate_identity_ok']}",
        flush=True,
    )
    print(
        "p block shift slack lift1 exact_hgate edge mid h_gate hgate_lift1 "
        "exact_lift1 lift1_slack hgate_slack lift1_margin hgate_margin "
        "channels lift1_channels h_gate_channels identity exact_identity",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['lift1_candidates']:.0f} "
            f"{row['h_gate_lowprime_exact']:.0f} {row['edge_lowprime_exact']:.0f} "
            f"{row['mid_lowprime_exact']:.0f} {row['h_gate_integer_ceiling']:.0f} "
            f"{fmt(row['h_gate_over_lift1'])} {fmt(row['lowprime_gate_over_lift1'])} "
            f"{fmt(row['lift1_over_slack'])} {fmt(row['h_gate_over_slack'])} "
            f"{row['lift1_margin']:.6f} {row['h_gate_margin']:.6f} "
            f"{row['all_channel_count']:.0f} {row['lift1_channel_count']:.0f} "
            f"{row['h_gate_channel_count']:.0f} {row['exact_identity_ok']} "
            f"{row['lowprime_gate_identity_ok']}",
            flush=True,
        )
    print(
        "p block shift m slack lift1 exact_hgate edge mid h_gate hgate_lift1 "
        "exact_lift1 lift1_slack hgate_slack h_kind side top_edges top_offsets identity exact_identity",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['lift1_candidates']:.0f} "
            f"{row['h_gate_lowprime_exact']:.0f} {row['edge_lowprime_exact']:.0f} "
            f"{row['mid_lowprime_exact']:.0f} {row['h_gate_integer_ceiling']:.0f} "
            f"{fmt(row['h_gate_over_lift1'])} {fmt(row['lowprime_gate_over_lift1'])} "
            f"{fmt(row['lift1_over_slack'])} {fmt(row['h_gate_over_slack'])} "
            f"{row['h_kind_hist']} {row['side_hist']} {row['top_edges']} "
            f"{row['top_offsets']} {row['exact_identity_ok']} "
            f"{row['lowprime_gate_identity_ok']}",
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

    package = lift1_offset_package(
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
