#!/usr/bin/env python3
"""AlphaTail C13 lift=1 边缘层去重预算审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
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


def interval_size(lo: int, hi: int) -> int:
    """返回闭区间整数长度。"""
    if hi < lo:
        return 0
    return hi - lo + 1


def edge_budget_row(
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
    """返回单层 lift=1 边缘层去重预算。"""
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
            "raw_edge_candidates": 0,
            "unique_edge_units": 0,
            "raw_mid_candidates": 0,
            "gate_envelope": 0,
            "gate_envelope_over_slack": ratio(0, slack),
            "gate_envelope_margin": slack,
        }

    tail_min = min(tail_primes)
    tail_max = max(tail_primes)
    low_min = min(low_primes)
    low_max = max(low_primes)
    raw_edge_candidates = 0
    raw_mid_candidates = 0
    edge_integer_span = 0
    edge_gate_count = 0
    nonempty_edge_gate_count = 0
    unique_edge_units: set[tuple[int, int, int, int, int]] = set()
    unit_multiplicity: Counter[tuple[int, int, int, int, int]] = Counter()
    side_hist: Counter[str] = Counter()
    unique_side_hist: defaultdict[str, set[tuple[int, int, int, int, int]]] = defaultdict(set)
    offset_hist: Counter[int] = Counter()
    edge_hist: Counter[int] = Counter()
    low_prime_hist: Counter[int] = Counter()
    channel_hist: Counter[tuple[int, int, int, int]] = Counter()
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
                    edge_specs = []
                    if numerator >= 0 and numerator % multiplier == 0:
                        offset = numerator // multiplier
                        lo = max(low_min, q_lo - offset, offset + 1)
                        hi = min(low_max, q_hi - offset)
                        edge_specs.append(("head", offset, lo, hi))
                    if numerator < 0 and (-numerator) % multiplier == 0:
                        offset = (-numerator) // multiplier
                        lo = max(low_min, ceil_div(q_lo + offset, 2), offset + 1)
                        hi = min(low_max, (q_hi + offset) // 2)
                        edge_specs.append(("tail", offset, lo, hi))
                    for side, offset, lo, hi in edge_specs:
                        edge_gate_count += 1
                        span = interval_size(lo, hi)
                        edge_integer_span += span
                        if span:
                            nonempty_edge_gate_count += 1
                        for low_prime in low_primes:
                            if low_prime < lo or low_prime > hi:
                                continue
                            if side == "head":
                                residue = offset
                                q_value = low_prime + offset
                            else:
                                residue = low_prime - offset
                                q_value = 2 * low_prime - offset
                            if residue < 0 or residue >= low_prime:
                                continue
                            if (residue + gap) % low_prime == 0:
                                continue
                            if q_value < q_lo or q_value > q_hi:
                                continue
                            unit = (index_a, index_b, multiplier, gap, q_value)
                            raw_edge_candidates += 1
                            unique_edge_units.add(unit)
                            unit_multiplicity[unit] += 1
                            side_hist[side] += 1
                            unique_side_hist[side].add(unit)
                            offset_hist[offset] += 1
                            edge_hist[min(offset, low_prime - offset)] += 1
                            low_prime_hist[low_prime] += 1
                            channel_hist[(index_a, index_b, multiplier, index)] += 1
                            if len(examples) < 8:
                                examples.append(
                                    {
                                        "side": side,
                                        "ell": low_prime,
                                        "q": q_value,
                                        "offset": offset,
                                        "edge": min(offset, low_prime - offset),
                                        "gap": gap,
                                        "u": multiplier,
                                        "j": index,
                                        "j1": index_a,
                                        "j2": index_b,
                                    }
                                )

    duplicate_saving = raw_edge_candidates - len(unique_edge_units)
    gate_envelope = num_primes * nonempty_edge_gate_count
    max_unit_multiplicity = max(unit_multiplicity.values()) if unit_multiplicity else 0
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "slack_before_low": slack,
        "raw_edge_candidates": raw_edge_candidates,
        "unique_edge_units": len(unique_edge_units),
        "raw_mid_candidates": raw_mid_candidates,
        "duplicate_saving": duplicate_saving,
        "edge_integer_span": edge_integer_span,
        "edge_gate_count": edge_gate_count,
        "nonempty_edge_gate_count": nonempty_edge_gate_count,
        "gate_envelope": gate_envelope,
        "raw_edge_over_slack": ratio(raw_edge_candidates, slack),
        "unique_edge_over_slack": ratio(len(unique_edge_units), slack),
        "gate_envelope_over_slack": ratio(gate_envelope, slack),
        "unique_edge_margin": slack - len(unique_edge_units),
        "gate_envelope_margin": slack - gate_envelope,
        "duplicate_saving_ratio": ratio(duplicate_saving, raw_edge_candidates),
        "max_unit_multiplicity": max_unit_multiplicity,
        "low_prime_support": len(low_prime_hist),
        "side_hist": dict(sorted(side_hist.items())),
        "unique_side_hist": {
            side: len(units)
            for side, units in sorted(unique_side_hist.items())
        },
        "top_offsets": dict(offset_hist.most_common(8)),
        "top_edges": dict(edge_hist.most_common(8)),
        "top_low_primes": dict(low_prime_hist.most_common(8)),
        "top_channels": [
            {
                "j1": key[0],
                "j2": key[1],
                "u": key[2],
                "j": key[3],
                "count": count,
            }
            for key, count in channel_hist.most_common(8)
        ],
        "examples": examples,
    }


def edge_budget_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 lift=1 边缘层预算包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "slack_before_low": 0.0,
            "raw_edge_candidates": 0.0,
            "unique_edge_units": 0.0,
            "duplicate_saving": 0.0,
            "edge_integer_span": 0.0,
            "edge_gate_count": 0.0,
            "nonempty_edge_gate_count": 0.0,
            "gate_envelope": 0.0,
            "max_unit_multiplicity": 0,
        }
    )
    total = {
        "slack_before_low": 0.0,
        "raw_edge_candidates": 0.0,
        "unique_edge_units": 0.0,
        "duplicate_saving": 0.0,
        "edge_integer_span": 0.0,
        "edge_gate_count": 0.0,
        "nonempty_edge_gate_count": 0.0,
        "gate_envelope": 0.0,
        "max_unit_multiplicity": 0,
    }
    total_side: Counter[str] = Counter()
    total_unique_side: Counter[str] = Counter()
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = edge_budget_row(
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
                "raw_edge_candidates",
                "unique_edge_units",
                "duplicate_saving",
                "edge_integer_span",
                "edge_gate_count",
                "nonempty_edge_gate_count",
                "gate_envelope",
            ):
                total[name] += item[name]
                windows[key][name] += item[name]
            total["max_unit_multiplicity"] = max(total["max_unit_multiplicity"], item["max_unit_multiplicity"])
            windows[key]["max_unit_multiplicity"] = max(
                windows[key]["max_unit_multiplicity"],
                item["max_unit_multiplicity"],
            )
            total_side.update(item["side_hist"])
            total_unique_side.update(item["unique_side_hist"])

    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["raw_edge_over_slack"] = ratio(value["raw_edge_candidates"], value["slack_before_low"])
        value["unique_edge_over_slack"] = ratio(value["unique_edge_units"], value["slack_before_low"])
        value["gate_envelope_over_slack"] = ratio(value["gate_envelope"], value["slack_before_low"])
        value["unique_edge_margin"] = value["slack_before_low"] - value["unique_edge_units"]
        value["gate_envelope_margin"] = value["slack_before_low"] - value["gate_envelope"]
        value["duplicate_saving_ratio"] = ratio(value["duplicate_saving"], value["raw_edge_candidates"])
        window_rows.append(value)
    total["raw_edge_over_slack"] = ratio(total["raw_edge_candidates"], total["slack_before_low"])
    total["unique_edge_over_slack"] = ratio(total["unique_edge_units"], total["slack_before_low"])
    total["gate_envelope_over_slack"] = ratio(total["gate_envelope"], total["slack_before_low"])
    total["unique_edge_margin"] = total["slack_before_low"] - total["unique_edge_units"]
    total["gate_envelope_margin"] = total["slack_before_low"] - total["gate_envelope"]
    total["duplicate_saving_ratio"] = ratio(total["duplicate_saving"], total["raw_edge_candidates"])
    total["side_hist"] = dict(sorted(total_side.items()))
    total["unique_side_hist"] = dict(sorted(total_unique_side.items()))
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
    """输出 lift=1 边缘层预算表。"""
    total = package["total"]
    print(
        "scope slack raw_edge unique_edge dup_save raw_slack unique_slack "
        "gate_env gate_slack unique_margin gate_margin dup_ratio span gates "
        "nonempty max_mult side unique_side",
        flush=True,
    )
    print(
        f"highP-total {total['slack_before_low']:.6f} {total['raw_edge_candidates']:.0f} "
        f"{total['unique_edge_units']:.0f} {total['duplicate_saving']:.0f} "
        f"{fmt(total['raw_edge_over_slack'])} {fmt(total['unique_edge_over_slack'])} "
        f"{total['gate_envelope']:.0f} {fmt(total['gate_envelope_over_slack'])} "
        f"{total['unique_edge_margin']:.6f} {total['gate_envelope_margin']:.6f} "
        f"{fmt(total['duplicate_saving_ratio'])} "
        f"{total['edge_integer_span']:.0f} {total['edge_gate_count']:.0f} "
        f"{total['nonempty_edge_gate_count']:.0f} {total['max_unit_multiplicity']} "
        f"{total['side_hist']} {total['unique_side_hist']}",
        flush=True,
    )
    print(
        "p block shift slack raw_edge unique_edge dup_save raw_slack unique_slack "
        "gate_env gate_slack unique_margin gate_margin dup_ratio span gates nonempty max_mult",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['slack_before_low']:.6f} {row['raw_edge_candidates']:.0f} "
            f"{row['unique_edge_units']:.0f} {row['duplicate_saving']:.0f} "
            f"{fmt(row['raw_edge_over_slack'])} {fmt(row['unique_edge_over_slack'])} "
            f"{row['gate_envelope']:.0f} {fmt(row['gate_envelope_over_slack'])} "
            f"{row['unique_edge_margin']:.6f} {row['gate_envelope_margin']:.6f} "
            f"{fmt(row['duplicate_saving_ratio'])} "
            f"{row['edge_integer_span']:.0f} {row['edge_gate_count']:.0f} "
            f"{row['nonempty_edge_gate_count']:.0f} {row['max_unit_multiplicity']}",
            flush=True,
        )
    print(
        "p block shift m slack raw_edge unique_edge dup_save raw_slack unique_slack "
        "gate_env gate_slack side unique_side top_edges top_offsets top_low_primes max_mult",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['slack_before_low']:.6f} {row['raw_edge_candidates']:.0f} "
            f"{row['unique_edge_units']:.0f} {row['duplicate_saving']:.0f} "
            f"{fmt(row['raw_edge_over_slack'])} {fmt(row['unique_edge_over_slack'])} "
            f"{row['gate_envelope']:.0f} {fmt(row['gate_envelope_over_slack'])} "
            f"{row['side_hist']} {row['unique_side_hist']} {row['top_edges']} "
            f"{row['top_offsets']} {row['top_low_primes']} {row['max_unit_multiplicity']}",
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

    package = edge_budget_package(
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
