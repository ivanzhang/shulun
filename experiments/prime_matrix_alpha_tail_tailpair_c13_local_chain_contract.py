#!/usr/bin/env python3
"""AlphaTail C13 高 P 局部闭合链合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_local_chain_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract import (
    edge_structural_ceiling_package,
)
from prime_matrix_alpha_tail_tailpair_c13_midhalf_structural_contract import (
    midhalf_structural_package,
)
from prime_matrix_alpha_tail_tailpair_c13_target_family_contract import (
    target_family_contract_package,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def c13_local_chain_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 C13 高 P 局部闭合链合同包。"""
    target = target_family_contract_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    mid = midhalf_structural_package(
        selected,
        m_values,
        finite_p_cut,
        alpha,
        num_primes,
    )
    edge = edge_structural_ceiling_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    total = {
        "syntax_pass": target["total"]["syntax_pass"],
        "ratio_structural_pass": target["total"]["ratio_structural_pass"],
        "mid_structural_void": mid["total"]["all_structural_mid_void"],
        "mid_compression_margin": mid["total"]["min_compression_margin"],
        "edge_structural_payment": edge["total"]["all_structural_payment_pass"],
        "formal_local_margin": target["total"]["min_formal_window_margin"],
        "edge_structural_margin": edge["total"]["min_structural_margin"],
        "target_family_rule_closed": target["total"]["target_family_rule_closed"],
    }
    total["selected_local_chain_contract"] = (
        total["syntax_pass"]
        and total["ratio_structural_pass"]
        and total["mid_structural_void"]
        and total["edge_structural_payment"]
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "c13_local_chain_sample_closed_target_family_open",
        "total": total,
        "target": target,
        "mid": mid,
        "edge": edge,
    }


def print_table(package: dict) -> None:
    """输出 C13 高 P 局部闭合链合同表。"""
    total = package["total"]
    print(
        "scope syntax ratio_struct mid_struct edge_struct local_chain "
        "mid_margin formal_margin edge_struct_margin target_rule_closed",
        flush=True,
    )
    print(
        f"highP-selected {total['syntax_pass']} {total['ratio_structural_pass']} "
        f"{total['mid_structural_void']} {total['edge_structural_payment']} "
        f"{total['selected_local_chain_contract']} "
        f"{total['mid_compression_margin']} "
        f"{fmt(total['formal_local_margin'])} {fmt(total['edge_structural_margin'])} "
        f"{total['target_family_rule_closed']}",
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

    package = c13_local_chain_package(
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
