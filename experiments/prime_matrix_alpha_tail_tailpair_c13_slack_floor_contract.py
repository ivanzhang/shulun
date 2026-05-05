#!/usr/bin/env python3
"""AlphaTail C13 结构边缘付款的 SlackFloor 合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_slack_floor_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract import (
    edge_structural_ceiling,
)
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def slack_floor_window(
    prime_bound: int,
    block: int,
    shift: int,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回单窗口 SlackFloor 合同审计。"""
    rows = []
    for point_count in m_values:
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
        resonance_margin = target["m2"] - target["required_m2"]
        geometric_buffer = target["geometric_upper"] - target["m2"]
        slack = target["geometric_upper"] - target["required_m2"]
        rows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "m": point_count,
                "m2": target["m2"],
                "b2_model": target["b2_model"],
                "cap_even": target["cap_even"],
                "required_m2": target["required_m2"],
                "geometric_upper": target["geometric_upper"],
                "resonance_margin": resonance_margin,
                "geometric_buffer": geometric_buffer,
                "slack": slack,
                "edge_ceiling": edge_structural_ceiling(point_count),
            }
        )
    resonance_margin = sum(row["resonance_margin"] for row in rows)
    geometric_buffer = sum(row["geometric_buffer"] for row in rows)
    slack = sum(row["slack"] for row in rows)
    edge_ceiling = sum(row["edge_ceiling"] for row in rows)
    edge_envelope = num_primes * edge_ceiling
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "resonance_margin": resonance_margin,
        "geometric_buffer": geometric_buffer,
        "slack": slack,
        "edge_ceiling": edge_ceiling,
        "edge_envelope": edge_envelope,
        "resonance_floor_margin": resonance_margin - edge_envelope,
        "slack_floor_margin": slack - edge_envelope,
        "geometric_buffer_nonnegative": geometric_buffer >= 0,
        "resonance_floor_pass": resonance_margin >= edge_envelope,
        "slack_floor_pass": slack >= edge_envelope,
        "slack_over_edge_envelope": ratio(slack, edge_envelope),
        "rows": rows,
    }


def slack_floor_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 SlackFloor 合同包。"""
    windows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        windows.append(
            slack_floor_window(
                prime_bound,
                block,
                shift,
                m_values,
                eta,
                alpha,
                num_primes,
                endpoint_band_theta,
            )
        )
    layer_rows = [row for window in windows for row in window["rows"]]
    total_resonance = sum(window["resonance_margin"] for window in windows)
    total_buffer = sum(window["geometric_buffer"] for window in windows)
    total_slack = sum(window["slack"] for window in windows)
    total_edge_envelope = sum(window["edge_envelope"] for window in windows)
    total = {
        "windows": len(windows),
        "total_resonance_margin": total_resonance,
        "total_geometric_buffer": total_buffer,
        "total_slack": total_slack,
        "total_edge_envelope": total_edge_envelope,
        "total_resonance_floor_margin": total_resonance - total_edge_envelope,
        "total_slack_floor_margin": total_slack - total_edge_envelope,
        "min_resonance_floor_margin": min(
            (window["resonance_floor_margin"] for window in windows),
            default=None,
        ),
        "min_slack_floor_margin": min(
            (window["slack_floor_margin"] for window in windows),
            default=None,
        ),
        "all_geometric_buffer_nonnegative": all(
            window["geometric_buffer_nonnegative"] for window in windows
        ),
        "all_resonance_floor_pass": all(window["resonance_floor_pass"] for window in windows),
        "all_slack_floor_pass": all(window["slack_floor_pass"] for window in windows),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "slack_floor_sample_closed_global_open",
        "total": total,
        "windows": windows,
        "rows": layer_rows,
    }


def print_table(package: dict) -> None:
    """输出 SlackFloor 合同表。"""
    total = package["total"]
    print(
        "scope windows resonance buffer slack edge_env res_margin slack_margin "
        "min_res_margin min_slack_margin buffer_nonneg res_pass slack_pass",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['total_resonance_margin']:.6f} "
        f"{total['total_geometric_buffer']:.0f} {total['total_slack']:.6f} "
        f"{total['total_edge_envelope']} {total['total_resonance_floor_margin']:.6f} "
        f"{total['total_slack_floor_margin']:.6f} "
        f"{fmt(total['min_resonance_floor_margin'])} "
        f"{fmt(total['min_slack_floor_margin'])} "
        f"{total['all_geometric_buffer_nonnegative']} "
        f"{total['all_resonance_floor_pass']} {total['all_slack_floor_pass']}",
        flush=True,
    )
    print(
        "p block shift resonance buffer slack edge_ceiling edge_env "
        "res_margin slack_margin slack_edge buffer_nonneg res_pass slack_pass",
        flush=True,
    )
    for window in package["windows"]:
        print(
            f"{window['p']} {window['block']} {window['shift']} "
            f"{window['resonance_margin']:.6f} {window['geometric_buffer']:.0f} "
            f"{window['slack']:.6f} {window['edge_ceiling']} "
            f"{window['edge_envelope']} {window['resonance_floor_margin']:.6f} "
            f"{window['slack_floor_margin']:.6f} "
            f"{fmt(window['slack_over_edge_envelope'])} "
            f"{window['geometric_buffer_nonnegative']} "
            f"{window['resonance_floor_pass']} {window['slack_floor_pass']}",
            flush=True,
        )
    print(
        "p block shift m M2 B2 cap required geom resonance buffer slack edge_ceiling",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['m2']:.0f} {row['b2_model']:.6f} {row['cap_even']:.6f} "
            f"{row['required_m2']:.6f} {row['geometric_upper']:.0f} "
            f"{row['resonance_margin']:.6f} {row['geometric_buffer']:.0f} "
            f"{row['slack']:.6f} {row['edge_ceiling']}",
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

    package = slack_floor_package(
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
