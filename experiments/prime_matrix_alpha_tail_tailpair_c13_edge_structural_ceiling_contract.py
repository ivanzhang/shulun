#!/usr/bin/env python3
"""AlphaTail C13 边缘门结构上界合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import (
    low_primes_for_item,
    parse_selected,
    tail_primes_for_item,
)
from prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget import edge_budget_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def tail_u1_ceiling(point_count: int) -> int:
    """返回 u=1 尾层门数上界 sum_{j1=1}^{m-1} j1^2。"""
    return sum(index * index for index in range(1, point_count))


def choose3(value: int) -> int:
    """返回三组合数。"""
    if value < 3:
        return 0
    return value * (value - 1) * (value - 2) // 6


def edge_structural_ceiling(point_count: int) -> int:
    """返回结构边缘门上界：u=1尾层加u=2,3头层。"""
    return tail_u1_ceiling(point_count) + 2 * choose3(point_count)


def edge_structural_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
) -> dict:
    """返回单层边缘门结构判据。"""
    low_primes = low_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    tail_primes = tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes)
    low_min = min(low_primes) if low_primes else None
    low_max = max(low_primes) if low_primes else None
    tail_min = min(tail_primes) if tail_primes else None
    block_condition = low_min is not None and block < 2 * low_min
    low_upper_guard = low_max is not None and low_max < block + 1
    tail_after_low = tail_min is not None and low_max is not None and tail_min > low_max
    shift_mod6 = abs(shift) % 6 == 0
    structural_guard = block_condition and low_upper_guard and tail_after_low and shift_mod6
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "low_min": low_min,
        "low_max": low_max,
        "tail_min": tail_min,
        "block_condition": block_condition,
        "low_upper_guard": low_upper_guard,
        "tail_after_low": tail_after_low,
        "shift_mod6": shift_mod6,
        "structural_guard": structural_guard,
        "tail_u1_ceiling": tail_u1_ceiling(point_count),
        "head_u23_ceiling": 2 * choose3(point_count),
        "edge_structural_ceiling": edge_structural_ceiling(point_count),
    }


def by_window(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def edge_structural_ceiling_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回边缘门结构上界合同包。"""
    edge = edge_budget_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    exact_by_window = by_window(edge["windows"])
    layer_rows = []
    windows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        window_ceiling = 0
        window_guard = True
        for point_count in m_values:
            row = edge_structural_row(prime_bound, block, shift, point_count, alpha, num_primes)
            layer_rows.append(row)
            window_ceiling += row["edge_structural_ceiling"]
            window_guard = window_guard and row["structural_guard"]
        exact = exact_by_window[(prime_bound, block, shift)]
        structural_gate_envelope = num_primes * window_ceiling
        slack = exact["slack_before_low"]
        windows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "slack": slack,
                "actual_nonempty_gates": exact["nonempty_edge_gate_count"],
                "actual_gate_envelope": exact["gate_envelope"],
                "structural_gate_ceiling": window_ceiling,
                "structural_gate_envelope": structural_gate_envelope,
                "actual_under_ceiling": exact["nonempty_edge_gate_count"] <= window_ceiling,
                "structural_guard": window_guard,
                "structural_margin": slack - structural_gate_envelope,
                "structural_payment_pass": window_guard and structural_gate_envelope <= slack,
            }
        )
    total_slack = sum(row["slack"] for row in windows)
    total_structural_envelope = sum(row["structural_gate_envelope"] for row in windows)
    total_actual_gates = sum(row["actual_nonempty_gates"] for row in windows)
    total_ceiling = sum(row["structural_gate_ceiling"] for row in windows)
    total = {
        "windows": len(windows),
        "all_structural_guard": all(row["structural_guard"] for row in windows),
        "all_actual_under_ceiling": all(row["actual_under_ceiling"] for row in windows),
        "all_structural_payment_pass": all(row["structural_payment_pass"] for row in windows),
        "total_slack": total_slack,
        "total_actual_gates": total_actual_gates,
        "total_structural_gate_ceiling": total_ceiling,
        "total_structural_gate_envelope": total_structural_envelope,
        "total_structural_margin": total_slack - total_structural_envelope,
        "min_structural_margin": min((row["structural_margin"] for row in windows), default=None),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "edge_structural_ceiling_sample_closed_global_open",
        "total": total,
        "windows": windows,
        "rows": layer_rows,
    }


def print_table(package: dict) -> None:
    """输出边缘门结构上界合同表。"""
    total = package["total"]
    print(
        "scope windows guard actual_under structural_pay slack actual_gates ceiling "
        "struct_env total_margin min_margin",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['all_structural_guard']} "
        f"{total['all_actual_under_ceiling']} {total['all_structural_payment_pass']} "
        f"{total['total_slack']:.6f} {total['total_actual_gates']:.0f} "
        f"{total['total_structural_gate_ceiling']} "
        f"{total['total_structural_gate_envelope']} "
        f"{total['total_structural_margin']:.6f} "
        f"{fmt(total['min_structural_margin'])}",
        flush=True,
    )
    print(
        "p block shift slack actual_gates actual_env ceiling struct_env "
        "margin guard under_ceiling pay",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['slack']:.6f} "
            f"{row['actual_nonempty_gates']:.0f} {row['actual_gate_envelope']:.0f} "
            f"{row['structural_gate_ceiling']} {row['structural_gate_envelope']} "
            f"{row['structural_margin']:.6f} {row['structural_guard']} "
            f"{row['actual_under_ceiling']} {row['structural_payment_pass']}",
            flush=True,
        )
    print(
        "p block shift m L U T B_lt_2L U_lt_B T_gt_U mod6 guard "
        "tail_u1 head_u23 ceiling",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['low_min']} {row['low_max']} {row['tail_min']} "
            f"{row['block_condition']} {row['low_upper_guard']} "
            f"{row['tail_after_low']} {row['shift_mod6']} "
            f"{row['structural_guard']} {row['tail_u1_ceiling']} "
            f"{row['head_u23_ceiling']} {row['edge_structural_ceiling']}",
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

    package = edge_structural_ceiling_package(
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
