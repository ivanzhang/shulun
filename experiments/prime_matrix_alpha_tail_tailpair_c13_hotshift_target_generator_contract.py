#!/usr/bin/env python3
"""AlphaTail C13 热门位移目标生成器合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_target_generator_contract.py --p-list 997,5003,10007 --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_additive_energy_audit import audit_item
from prime_matrix_alpha_tail_tailpair_c13_local_chain_contract import c13_local_chain_package
from prime_matrix_alpha_tail_tailpair_c13_small_slack_finite_reduction_contract import (
    small_slack_finite_reduction_package,
)
from prime_matrix_alpha_tail_tailpair_c13_target_family_contract import next_power_of_two
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def parse_p_list(raw: str) -> list[int]:
    """解析素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def generated_window(prime_bound: int, alpha: float, sign: str) -> dict:
    """按 dyadic block 与加法能量最热门非零位移生成窗口。"""
    block = next_power_of_two(prime_bound + 1)
    audit = audit_item(prime_bound, block, sign, alpha)
    shift, hot_count = audit["max_nonzero_diff"]
    return {
        "p": prime_bound,
        "block": block,
        "sign": sign,
        "shift": shift,
        "hot_count": hot_count,
        "d_count": audit["d_count"],
        "diff_support": audit["diff_support"],
        "energy": audit["energy"],
        "energy_over_model": audit["energy_over_model"],
        "selected_token": f"{prime_bound}:{block}:{shift}",
    }


def hotshift_target_generator_package(
    p_list: list[int],
    expected_selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    sign: str,
) -> dict:
    """返回热门位移目标生成器合同包。"""
    windows = [generated_window(prime_bound, alpha, sign) for prime_bound in p_list]
    selected = ",".join(row["selected_token"] for row in windows)
    highp_selected = ",".join(
        row["selected_token"] for row in windows if row["p"] > finite_p_cut
    )
    expected_highp_selected = ",".join(
        f"{prime_bound}:{block}:{shift}"
        for prime_bound, block, shift in parse_selected(expected_selected)
        if prime_bound > finite_p_cut
    )
    local_chain = c13_local_chain_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    small_slack = small_slack_finite_reduction_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    total = {
        "windows": len(windows),
        "selected": selected,
        "highp_selected": highp_selected,
        "expected_selected": expected_selected,
        "expected_highp_selected": expected_highp_selected,
        "matches_expected_highp": highp_selected == expected_highp_selected,
        "all_have_hot_shift": all(row["hot_count"] > 0 and row["shift"] != 0 for row in windows),
        "highp_full_postlow_chain": local_chain["total"]["selected_full_postlow_chain_contract"],
        "highp_target_rule_closed": local_chain["total"]["target_family_rule_closed"],
        "small_slack_finite_exit": small_slack["total"]["all_finite_exit_pass"],
        "small_slack_finite_keys": small_slack["total"]["finite_keys"],
        "lowp_excluded": small_slack["total"]["lowp_excluded"],
        "min_source_margin": small_slack["total"]["min_source_margin"],
        "min_template_margin": local_chain["total"]["active_template_margin"],
        "min_formal_margin": local_chain["total"]["formal_local_margin"],
    }
    total["sample_generated_chain_closed"] = (
        total["matches_expected_highp"]
        and total["all_have_hot_shift"]
        and total["highp_full_postlow_chain"]
        and total["small_slack_finite_exit"]
    )
    return {
        "p_list": p_list,
        "expected_selected": expected_selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "sign": sign,
        "status": "hotshift_target_generator_sample_closed_global_open",
        "target_family_rule_closed": False,
        "target_family_gap": "热门位移生成器已复现当前样本；尚未证明它覆盖完整行命题目标族。",
        "total": total,
        "windows": windows,
        "local_chain": local_chain,
        "small_slack": small_slack,
    }


def print_table(package: dict) -> None:
    """输出热门位移生成器合同表。"""
    total = package["total"]
    print(
        "scope windows selected matches_expected hot_shift full_postlow small_slack "
        "sample_chain target_rule_closed finite_keys lowp_excluded min_source_margin "
        "min_template_margin min_formal_margin",
        flush=True,
    )
    print(
        f"hotshift-total {total['windows']} {total['highp_selected']} "
        f"{total['matches_expected_highp']} {total['all_have_hot_shift']} "
        f"{total['highp_full_postlow_chain']} {total['small_slack_finite_exit']} "
        f"{total['sample_generated_chain_closed']} "
        f"{total['highp_target_rule_closed']} {total['small_slack_finite_keys']} "
        f"{total['lowp_excluded']} {fmt(total['min_source_margin'])} "
        f"{fmt(total['min_template_margin'])} {fmt(total['min_formal_margin'])}",
        flush=True,
    )
    print(
        "p block sign shift hot_count d_count diff_support energy_over_model selected_token",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['sign']} {row['shift']} "
            f"{row['hot_count']} {row['d_count']} {row['diff_support']} "
            f"{row['energy_over_model']:.6f} {row['selected_token']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="997,5003,10007")
    parser.add_argument(
        "--expected-selected",
        type=str,
        default="997:4096:-36,5003:8192:-36,10007:16384:-900",
    )
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--sign", choices=("+", "-"), default="-")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hotshift_target_generator_package(
        parse_p_list(args.p_list),
        args.expected_selected,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.endpoint_band_theta,
        args.sign,
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
