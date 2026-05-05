#!/usr/bin/env python3
"""AlphaTail C13 高 P 局部闭合链合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_local_chain_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_active_class_template_bound_contract import (
    active_class_template_bound_package,
)
from prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract import (
    edge_structural_ceiling_package,
)
from prime_matrix_alpha_tail_tailpair_c13_midhalf_structural_contract import (
    midhalf_structural_package,
)
from prime_matrix_alpha_tail_tailpair_c13_small_slack_source_certificate import (
    small_slack_source_certificate_package,
)
from prime_matrix_alpha_tail_tailpair_c13_slack_floor_contract import slack_floor_package
from prime_matrix_alpha_tail_tailpair_c13_source_slot_structural_contract import (
    source_slot_structural_package,
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
    slack = slack_floor_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    active_template = active_class_template_bound_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    source_slot = source_slot_structural_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    small_slack_source = small_slack_source_certificate_package(
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
        "slack_floor_pass": slack["total"]["all_slack_floor_pass"],
        "resonance_floor_pass": slack["total"]["all_resonance_floor_pass"],
        "resonance_floor_margin": slack["total"]["min_resonance_floor_margin"],
        "active_template_pay": active_template["total"]["all_template_pay"],
        "active_template_margin": active_template["total"]["min_template_margin"],
        "source_forward_struct": source_slot["total"]["all_forward"],
        "source_exact_pay": source_slot["total"]["all_exact_source_pay"],
        "source_exact_margin": source_slot["total"]["min_exact_source_margin"],
        "small_slack_source_cert": small_slack_source["total"]["all_source_certificate_pass"],
        "small_slack_windows": small_slack_source["total"]["small_slack_windows"],
        "small_slack_source_margin": small_slack_source["total"]["min_source_margin"],
        "target_family_rule_closed": target["total"]["target_family_rule_closed"],
    }
    total["selected_local_chain_contract"] = (
        total["syntax_pass"]
        and total["ratio_structural_pass"]
        and total["mid_structural_void"]
        and total["edge_structural_payment"]
        and total["slack_floor_pass"]
    )
    total["selected_full_postlow_chain_contract"] = (
        total["selected_local_chain_contract"]
        and total["active_template_pay"]
        and total["source_forward_struct"]
        and total["source_exact_pay"]
        and total["small_slack_source_cert"]
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
        "slack": slack,
        "active_template": active_template,
        "source_slot": source_slot,
        "small_slack_source": small_slack_source,
    }


def print_table(package: dict) -> None:
    """输出 C13 高 P 局部闭合链合同表。"""
    total = package["total"]
    print(
        "scope syntax ratio_struct mid_struct edge_struct local_chain "
        "mid_margin formal_margin edge_struct_margin slack_floor "
        "res_floor res_margin active_template source_forward source_exact "
        "small_slack_cert full_postlow_chain target_rule_closed",
        flush=True,
    )
    print(
        f"highP-selected {total['syntax_pass']} {total['ratio_structural_pass']} "
        f"{total['mid_structural_void']} {total['edge_structural_payment']} "
        f"{total['selected_local_chain_contract']} "
        f"{total['mid_compression_margin']} "
        f"{fmt(total['formal_local_margin'])} {fmt(total['edge_structural_margin'])} "
        f"{total['slack_floor_pass']} {total['resonance_floor_pass']} "
        f"{fmt(total['resonance_floor_margin'])} "
        f"{total['active_template_pay']} {total['source_forward_struct']} "
        f"{total['source_exact_pay']} {total['small_slack_source_cert']} "
        f"{total['selected_full_postlow_chain_contract']} "
        f"{total['target_family_rule_closed']}",
        flush=True,
    )
    print(
        "postlow_margins active_template source_exact small_slack_windows small_slack_source",
        flush=True,
    )
    print(
        f"postlow_margins {fmt(total['active_template_margin'])} "
        f"{fmt(total['source_exact_margin'])} "
        f"{total['small_slack_windows']} {fmt(total['small_slack_source_margin'])}",
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
