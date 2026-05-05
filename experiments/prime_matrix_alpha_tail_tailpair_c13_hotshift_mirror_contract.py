#!/usr/bin/env python3
"""AlphaTail C13 热门位移正负镜像等价合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_mirror_contract.py --p-list 5003,10007 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_hotshift_tiebreak_contract import tiebreak_row
from prime_matrix_alpha_tail_tailpair_c13_local_chain_contract import c13_local_chain_package
from prime_matrix_alpha_tail_tailpair_c13_small_slack_finite_reduction_contract import (
    small_slack_finite_reduction_package,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def parse_p_list(raw: str) -> list[int]:
    """解析素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def selected_from_rows(rows: list[dict], sign: int) -> str:
    """按方向生成 selected 字符串。"""
    return ",".join(f"{row['p']}:{row['block']}:{sign * abs(row['oriented_shift'])}" for row in rows)


def hotshift_mirror_package(
    p_list: list[int],
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    sign: str,
) -> dict:
    """返回正负热门位移镜像等价合同包。"""
    rows = [tiebreak_row(prime_bound, alpha, sign) for prime_bound in p_list]
    rows = [row for row in rows if row["p"] > finite_p_cut and row["oriented_shift"] is not None]
    negative_selected = selected_from_rows(rows, -1)
    positive_selected = selected_from_rows(rows, 1)
    negative_chain = c13_local_chain_package(
        negative_selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    positive_chain = c13_local_chain_package(
        positive_selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    negative_finite = small_slack_finite_reduction_package(
        negative_selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    positive_finite = small_slack_finite_reduction_package(
        positive_selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    comparable_keys = [
        "mid_compression_margin",
        "formal_local_margin",
        "edge_structural_margin",
        "resonance_floor_margin",
        "active_template_margin",
        "source_exact_margin",
        "small_slack_source_margin",
    ]
    mirror_equalities = {
        key: negative_chain["total"][key] == positive_chain["total"][key]
        for key in comparable_keys
    }
    finite_equalities = {
        "small_slack_windows": negative_finite["total"]["small_slack_windows"]
        == positive_finite["total"]["small_slack_windows"],
        "min_source_margin": negative_finite["total"]["min_source_margin"]
        == positive_finite["total"]["min_source_margin"],
    }
    total = {
        "windows": len(rows),
        "negative_selected": negative_selected,
        "positive_selected": positive_selected,
        "all_oriented_unique": all(row["oriented_unique"] for row in rows),
        "negative_full_postlow": negative_chain["total"]["selected_full_postlow_chain_contract"],
        "positive_local_chain": positive_chain["total"]["selected_local_chain_contract"],
        "positive_source_forward": positive_chain["total"]["source_forward_struct"],
        "positive_source_exact": positive_chain["total"]["source_exact_pay"],
        "positive_small_slack": positive_finite["total"]["all_finite_exit_pass"],
        "all_numeric_mirror_equal": all(mirror_equalities.values()) and all(finite_equalities.values()),
        "mirror_equalities": mirror_equalities,
        "finite_equalities": finite_equalities,
        "orientation_normalization_closed": (
            all(row["oriented_unique"] for row in rows)
            and negative_chain["total"]["selected_full_postlow_chain_contract"]
            and positive_chain["total"]["selected_local_chain_contract"]
            and positive_chain["total"]["source_exact_pay"]
            and positive_finite["total"]["all_finite_exit_pass"]
            and all(mirror_equalities.values())
            and all(finite_equalities.values())
        ),
    }
    return {
        "p_list": p_list,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "sign": sign,
        "status": "hotshift_mirror_sample_closed_global_open",
        "total": total,
        "rows": rows,
        "negative_chain": negative_chain,
        "positive_chain": positive_chain,
        "negative_finite": negative_finite,
        "positive_finite": positive_finite,
    }


def print_table(package: dict) -> None:
    """输出正负镜像等价合同表。"""
    total = package["total"]
    print(
        "scope windows neg_selected pos_selected unique neg_full pos_local "
        "pos_forward pos_exact pos_small numeric_equal orientation_closed",
        flush=True,
    )
    print(
        f"mirror-total {total['windows']} {total['negative_selected']} "
        f"{total['positive_selected']} {total['all_oriented_unique']} "
        f"{total['negative_full_postlow']} {total['positive_local_chain']} "
        f"{total['positive_source_forward']} {total['positive_source_exact']} "
        f"{total['positive_small_slack']} {total['all_numeric_mirror_equal']} "
        f"{total['orientation_normalization_closed']}",
        flush=True,
    )
    print(
        "margins mid formal edge res active_template source_exact small_slack",
        flush=True,
    )
    neg = package["negative_chain"]["total"]
    print(
        f"negative {neg['mid_compression_margin']} {fmt(neg['formal_local_margin'])} "
        f"{fmt(neg['edge_structural_margin'])} {fmt(neg['resonance_floor_margin'])} "
        f"{fmt(neg['active_template_margin'])} {fmt(neg['source_exact_margin'])} "
        f"{fmt(neg['small_slack_source_margin'])}",
        flush=True,
    )
    pos = package["positive_chain"]["total"]
    print(
        f"positive {pos['mid_compression_margin']} {fmt(pos['formal_local_margin'])} "
        f"{fmt(pos['edge_structural_margin'])} {fmt(pos['resonance_floor_margin'])} "
        f"{fmt(pos['active_template_margin'])} {fmt(pos['source_exact_margin'])} "
        f"{fmt(pos['small_slack_source_margin'])}",
        flush=True,
    )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="5003,10007")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--sign", choices=("+", "-"), default="-")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hotshift_mirror_package(
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
