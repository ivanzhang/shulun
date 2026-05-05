#!/usr/bin/env python3
"""AlphaTail C13 全最大绝对热门位移生成器合同。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_maxset_generator_contract.py --p-list 997,5003,10007 --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_additive_energy_audit import low_squarefree_block
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


def maxset_row(prime_bound: int, alpha: float, sign: str) -> dict:
    """返回单个 p 的全部最大绝对热门差值。"""
    block = next_power_of_two(prime_bound + 1)
    values = low_squarefree_block(int(alpha * prime_bound), block, sign)
    diff_counts: dict[int, int] = defaultdict(int)
    for left in values:
        for right in values:
            diff = left - right
            if diff == 0:
                continue
            diff_counts[diff] += 1
    max_count = max(diff_counts.values(), default=0)
    max_abs_diffs = sorted({abs(diff) for diff, count in diff_counts.items() if count == max_count})
    selected_tokens = [f"{prime_bound}:{block}:{-diff}" for diff in max_abs_diffs]
    return {
        "p": prime_bound,
        "block": block,
        "sign": sign,
        "d_count": len(values),
        "max_count": max_count,
        "max_abs_diffs": max_abs_diffs,
        "max_abs_count": len(max_abs_diffs),
        "selected_tokens": selected_tokens,
    }


def hotshift_maxset_package(
    p_list: list[int],
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    sign: str,
) -> dict:
    """返回全最大绝对热门位移生成器合同包。"""
    rows = [maxset_row(prime_bound, alpha, sign) for prime_bound in p_list]
    highp_tokens = [
        token
        for row in rows
        if row["p"] > finite_p_cut
        for token in row["selected_tokens"]
    ]
    highp_selected = ",".join(highp_tokens)
    local_chain = c13_local_chain_package(
        highp_selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    small_slack = small_slack_finite_reduction_package(
        highp_selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    total = {
        "windows": len(rows),
        "highp_selected": highp_selected,
        "highp_token_count": len(highp_tokens),
        "all_have_maxset": all(row["max_abs_count"] > 0 for row in rows),
        "all_sample_abs_unique": all(row["max_abs_count"] == 1 for row in rows),
        "max_abs_counts": {row["p"]: row["max_abs_count"] for row in rows},
        "full_postlow_chain": local_chain["total"]["selected_full_postlow_chain_contract"],
        "small_slack_finite_exit": small_slack["total"]["all_finite_exit_pass"],
        "min_source_margin": small_slack["total"]["min_source_margin"],
        "min_template_margin": local_chain["total"]["active_template_margin"],
        "target_rule_closed": False,
    }
    total["maxset_sample_chain_closed"] = (
        total["all_have_maxset"]
        and total["full_postlow_chain"]
        and total["small_slack_finite_exit"]
    )
    return {
        "p_list": p_list,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "sign": sign,
        "status": "hotshift_maxset_sample_closed_global_open",
        "total": total,
        "rows": rows,
        "local_chain": local_chain,
        "small_slack": small_slack,
    }


def print_table(package: dict) -> None:
    """输出全最大热门集合同表。"""
    total = package["total"]
    print(
        "scope windows highp_selected token_count have_maxset abs_unique "
        "full_postlow small_slack sample_chain target_rule_closed counts "
        "min_source_margin min_template_margin",
        flush=True,
    )
    print(
        f"maxset-total {total['windows']} {total['highp_selected']} "
        f"{total['highp_token_count']} {total['all_have_maxset']} "
        f"{total['all_sample_abs_unique']} {total['full_postlow_chain']} "
        f"{total['small_slack_finite_exit']} {total['maxset_sample_chain_closed']} "
        f"{total['target_rule_closed']} {total['max_abs_counts']} "
        f"{fmt(total['min_source_margin'])} {fmt(total['min_template_margin'])}",
        flush=True,
    )
    print("p block sign d_count max_count max_abs_diffs selected_tokens", flush=True)
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['sign']} {row['d_count']} "
            f"{row['max_count']} {row['max_abs_diffs']} {row['selected_tokens']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="997,5003,10007")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--sign", choices=("+", "-"), default="-")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hotshift_maxset_package(
        parse_p_list(args.p_list),
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
