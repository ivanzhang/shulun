#!/usr/bin/env python3
"""AlphaTail C13 边缘层 Gate 局部付款合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_edge_gate_payment_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget import edge_budget_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def by_window(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引审计行。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def edge_gate_payment_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回边缘层 Gate 局部付款合同包。"""
    edge = edge_budget_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    edge_by_window = by_window(edge["windows"])
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        row = edge_by_window[(prime_bound, block, shift)]
        gate_envelope = row["gate_envelope"]
        slack = row["slack_before_low"]
        rows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "slack": slack,
                "unique_edge": row["unique_edge_units"],
                "raw_edge": row["raw_edge_candidates"],
                "duplicate_saving": row["duplicate_saving"],
                "nonempty_edge_gates": row["nonempty_edge_gate_count"],
                "gate_envelope": gate_envelope,
                "gate_margin": slack - gate_envelope,
                "unique_margin": slack - row["unique_edge_units"],
                "gate_over_slack": ratio(gate_envelope, slack),
                "unique_over_slack": ratio(row["unique_edge_units"], slack),
                "allowed_num_primes": row["allowed_num_primes"],
                "num_primes_margin": row["num_primes_margin"],
                "edge_gate_pass": gate_envelope <= slack,
                "edge_exact_pass": row["unique_edge_units"] <= slack,
            }
        )
    total_slack = sum(row["slack"] for row in rows)
    total_gate = sum(row["gate_envelope"] for row in rows)
    total_unique = sum(row["unique_edge"] for row in rows)
    total = {
        "highp_windows": len(rows),
        "total_slack": total_slack,
        "total_gate_envelope": total_gate,
        "total_unique_edge": total_unique,
        "total_gate_margin": total_slack - total_gate,
        "total_unique_margin": total_slack - total_unique,
        "min_gate_margin": min((row["gate_margin"] for row in rows), default=None),
        "min_unique_margin": min((row["unique_margin"] for row in rows), default=None),
        "max_gate_over_slack": max((row["gate_over_slack"] for row in rows), default=None),
        "max_unique_over_slack": max((row["unique_over_slack"] for row in rows), default=None),
        "all_edge_gate_pass": all(row["edge_gate_pass"] for row in rows),
        "all_edge_exact_pass": all(row["edge_exact_pass"] for row in rows),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "edge_gate_payment_sample_closed_global_open",
        "total": total,
        "windows": rows,
    }


def print_table(package: dict) -> None:
    """输出边缘层 Gate 局部付款合同表。"""
    total = package["total"]
    print(
        "scope windows slack gate unique gate_margin unique_margin min_gate_margin "
        "max_gate_slack edge_gate_pass edge_exact_pass",
        flush=True,
    )
    print(
        f"highP-total {total['highp_windows']} {total['total_slack']:.6f} "
        f"{total['total_gate_envelope']:.0f} {total['total_unique_edge']:.0f} "
        f"{total['total_gate_margin']:.6f} {total['total_unique_margin']:.6f} "
        f"{fmt(total['min_gate_margin'])} {fmt(total['max_gate_over_slack'])} "
        f"{total['all_edge_gate_pass']} {total['all_edge_exact_pass']}",
        flush=True,
    )
    print(
        "p block shift slack gates gate_env raw unique dup gate_margin unique_margin "
        "gate_slack unique_slack kcrit kmargin gate_pass exact_pass",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['slack']:.6f} "
            f"{row['nonempty_edge_gates']:.0f} {row['gate_envelope']:.0f} "
            f"{row['raw_edge']:.0f} {row['unique_edge']:.0f} "
            f"{row['duplicate_saving']:.0f} {row['gate_margin']:.6f} "
            f"{row['unique_margin']:.6f} {fmt(row['gate_over_slack'])} "
            f"{fmt(row['unique_over_slack'])} {row['allowed_num_primes']} "
            f"{row['num_primes_margin']} {row['edge_gate_pass']} "
            f"{row['edge_exact_pass']}",
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

    package = edge_gate_payment_package(
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
