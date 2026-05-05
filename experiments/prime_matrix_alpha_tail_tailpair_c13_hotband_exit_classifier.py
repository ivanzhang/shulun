#!/usr/bin/env python3
"""AlphaTail C13 热门带闭合/出口分类审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier.py --p-list 5003,10007 --beta 0.95 --finite-p-cut 1000 --eta 0.04 --format table
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


def hotband_tokens(prime_bound: int, alpha: float, sign: str, beta: float) -> list[dict]:
    """生成达到 beta*max 的负向热门带窗口。"""
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
    abs_counts: dict[int, int] = {}
    for diff, count in diff_counts.items():
        abs_diff = abs(diff)
        abs_counts[abs_diff] = max(abs_counts.get(abs_diff, 0), count)
    rows = []
    for abs_diff, count in sorted(abs_counts.items(), key=lambda item: (-item[1], item[0])):
        if max_count == 0 or count < beta * max_count:
            continue
        rows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": -abs_diff,
                "hot_count": count,
                "hot_ratio": count / max_count if max_count else None,
                "max_count": max_count,
                "selected": f"{prime_bound}:{block}:{-abs_diff}",
            }
        )
    return rows


def classify_window(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回单窗口 C13 闭合或出口分类。"""
    local = c13_local_chain_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    finite = small_slack_finite_reduction_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    total = local["total"]
    finite_total = finite["total"]
    if total["selected_full_postlow_chain_contract"] and finite_total["all_finite_exit_pass"]:
        exit_type = "C13Closed"
    elif not total["syntax_pass"] or not total["ratio_structural_pass"]:
        exit_type = "TargetSyntaxOrRatioExit"
    elif not total["slack_floor_pass"] or not total["resonance_floor_pass"]:
        exit_type = "SlackFloorExit"
    elif not total["active_template_pay"]:
        exit_type = "ActiveTemplateExit"
    elif not finite_total["all_finite_exit_pass"]:
        exit_type = "FiniteSourceExit"
    else:
        exit_type = "ResidualPDECOrSAEExit"
    return {
        "exit_type": exit_type,
        "syntax": total["syntax_pass"],
        "ratio": total["ratio_structural_pass"],
        "local_chain": total["selected_local_chain_contract"],
        "full_postlow": total["selected_full_postlow_chain_contract"],
        "slack_floor": total["slack_floor_pass"],
        "res_floor": total["resonance_floor_pass"],
        "active_template": total["active_template_pay"],
        "source_exact": total["source_exact_pay"],
        "small_finite": finite_total["all_finite_exit_pass"],
        "formal_margin": total["formal_local_margin"],
        "res_margin": total["resonance_floor_margin"],
        "template_margin": total["active_template_margin"],
        "source_margin": finite_total["min_source_margin"],
    }


def hotband_exit_package(
    p_list: list[int],
    beta: float,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    sign: str,
) -> dict:
    """返回热门带闭合/出口分类包。"""
    token_rows = [
        row
        for prime_bound in p_list
        for row in hotband_tokens(prime_bound, alpha, sign, beta)
        if prime_bound > finite_p_cut
    ]
    rows = []
    for row in token_rows:
        classification = classify_window(
            row["selected"],
            m_values,
            finite_p_cut,
            eta,
            alpha,
            num_primes,
            endpoint_band_theta,
        )
        rows.append({**row, **classification})
    exit_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        exit_counts[row["exit_type"]] += 1
    total = {
        "windows": len(rows),
        "beta": beta,
        "closed_windows": exit_counts.get("C13Closed", 0),
        "exit_windows": len(rows) - exit_counts.get("C13Closed", 0),
        "exit_counts": dict(sorted(exit_counts.items())),
        "all_classified": len(rows) == sum(exit_counts.values()),
        "selected_closed": ",".join(row["selected"] for row in rows if row["exit_type"] == "C13Closed"),
        "selected_exits": ",".join(row["selected"] for row in rows if row["exit_type"] != "C13Closed"),
        "min_closed_source_margin": min(
            (row["source_margin"] for row in rows if row["exit_type"] == "C13Closed"),
            default=None,
        ),
        "min_exit_res_margin": min(
            (row["res_margin"] for row in rows if row["exit_type"] != "C13Closed"),
            default=None,
        ),
    }
    return {
        "p_list": p_list,
        "beta": beta,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "sign": sign,
        "status": "hotband_exit_classifier_sample_classified_global_open",
        "total": total,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出热门带分类表。"""
    total = package["total"]
    print(
        "scope beta windows closed exits classified exit_counts closed_selected exit_selected "
        "min_closed_source_margin min_exit_res_margin",
        flush=True,
    )
    print(
        f"hotband-total {total['beta']:.6f} {total['windows']} "
        f"{total['closed_windows']} {total['exit_windows']} {total['all_classified']} "
        f"{total['exit_counts']} {total['selected_closed']} {total['selected_exits']} "
        f"{fmt(total['min_closed_source_margin'])} {fmt(total['min_exit_res_margin'])}",
        flush=True,
    )
    print(
        "p block shift hot_count hot_ratio exit_type syntax ratio local full "
        "slack res active_template source_exact small_finite formal_margin "
        "res_margin template_margin source_margin",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['hot_count']} "
            f"{fmt(row['hot_ratio'])} {row['exit_type']} {row['syntax']} "
            f"{row['ratio']} {row['local_chain']} {row['full_postlow']} "
            f"{row['slack_floor']} {row['res_floor']} {row['active_template']} "
            f"{row['source_exact']} {row['small_finite']} {fmt(row['formal_margin'])} "
            f"{fmt(row['res_margin'])} {fmt(row['template_margin'])} "
            f"{fmt(row['source_margin'])}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="5003,10007")
    parser.add_argument("--beta", type=float, default=0.95)
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--sign", choices=("+", "-"), default="-")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hotband_exit_package(
        parse_p_list(args.p_list),
        args.beta,
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
