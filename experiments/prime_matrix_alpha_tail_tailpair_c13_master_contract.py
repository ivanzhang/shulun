#!/usr/bin/env python3
"""AlphaTail C13 高 P 主合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_master_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_highp_plt_closure_bridge import (
    closure_package as plt_closure_package,
)
from prime_matrix_alpha_tail_tailpair_c13_liftge2_structural_criterion import (
    criterion_package,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def master_contract_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 C13 高 P 主合同审计包。"""
    structural = criterion_package(selected, m_values, finite_p_cut, alpha, num_primes)
    plt = plt_closure_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    all_window_formal_pass = all(row["formal_pass"] for row in plt["windows"])
    all_row_formal_pass = all(row["formal_pass"] for row in plt["rows"])
    all_window_structural = all(row["criterion_pass"] for row in structural["rows"])
    total_gate_contract = structural["total"]["criterion_pass"] and plt["total"]["gate_pass"]
    local_formal_contract = all_window_structural and all_window_formal_pass
    row_formal_contract = all_window_structural and all_row_formal_pass
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "total": {
            "structural_pass": structural["total"]["criterion_pass"],
            "structural_candidates": structural["total"]["signature_candidates"],
            "structural_good_mod6": structural["total"]["signature_good_mod6"],
            "min_block_margin": structural["total"]["min_block_margin"],
            "min_n_margin": structural["total"]["min_n_margin"],
            "gate_plt_pass": plt["total"]["gate_pass"],
            "formal_plt_pass": plt["total"]["formal_pass"],
            "total_gate_contract": total_gate_contract,
            "local_formal_contract": local_formal_contract,
            "row_formal_contract": row_formal_contract,
            "gate_margin_to_required": plt["total"]["gate_margin_to_required"],
            "formal_margin_to_required": plt["total"]["formal_margin_to_required"],
            "actual_margin_to_required": plt["total"]["actual_margin_to_required"],
            "gate_low_over_required": plt["total"]["gate_low_over_required"],
            "formal_low_over_required": plt["total"]["formal_low_over_required"],
        },
        "structural": structural,
        "plt": plt,
    }


def print_table(package: dict) -> None:
    """输出 C13 高 P 主合同审计表。"""
    total = package["total"]
    print(
        "scope structural candidates good min_block_margin min_n_margin "
        "gate_plt formal_plt total_gate_contract local_formal_contract "
        "row_formal_contract gate_margin formal_margin gate_req formal_req",
        flush=True,
    )
    print(
        f"highP-total {total['structural_pass']} {total['structural_candidates']} "
        f"{total['structural_good_mod6']} {total['min_block_margin']} "
        f"{total['min_n_margin']} {total['gate_plt_pass']} {total['formal_plt_pass']} "
        f"{total['total_gate_contract']} {total['local_formal_contract']} "
        f"{total['row_formal_contract']} {total['gate_margin_to_required']:.6f} "
        f"{total['formal_margin_to_required']:.6f} {fmt(total['gate_low_over_required'])} "
        f"{fmt(total['formal_low_over_required'])}",
        flush=True,
    )
    print(
        "p block shift geom required gate_low formal_low gate_margin formal_margin "
        "gate_pass formal_pass identity",
        flush=True,
    )
    for row in package["plt"]["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['geometric_upper']:.0f} "
            f"{row['required_m2']:.6f} {row['gate_low_lower']:.0f} "
            f"{row['formal_low_lower']:.0f} {row['gate_margin_to_required']:.6f} "
            f"{row['formal_margin_to_required']:.6f} {row['gate_pass']} "
            f"{row['formal_pass']} {row['all_equal_identity_ok']}",
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

    package = master_contract_package(
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
