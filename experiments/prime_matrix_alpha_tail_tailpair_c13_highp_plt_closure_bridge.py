#!/usr/bin/env python3
"""AlphaTail C13 HighP-PLT 低筛闭合桥。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_highp_plt_closure_bridge.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_global_pool_bridge import bridge_row
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def closure_row(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    m_values: list[int],
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回单层 HighP-PLT 闭合桥。"""
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
    bridge = bridge_row(
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
    gate_low_lower = target["geometric_upper"] - bridge["gate_consumed"]
    formal_low_lower = target["geometric_upper"] - bridge["formal_consumed"]
    required = target["required_m2"]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "geometric_upper": target["geometric_upper"],
        "required_m2": required,
        "actual_low_survivor": target["low_survivor_exact"],
        "gate_consumed": bridge["gate_consumed"],
        "formal_consumed": bridge["formal_consumed"],
        "gate_low_lower": gate_low_lower,
        "formal_low_lower": formal_low_lower,
        "gate_margin_to_required": gate_low_lower - required,
        "formal_margin_to_required": formal_low_lower - required,
        "actual_margin_to_required": target["low_survivor_exact"] - required,
        "gate_pass": gate_low_lower >= required,
        "formal_pass": formal_low_lower >= required,
        "actual_pass": target["low_survivor_exact"] >= required,
        "gate_low_over_required": ratio(gate_low_lower, required),
        "formal_low_over_required": ratio(formal_low_lower, required),
        "actual_low_over_required": ratio(target["low_survivor_exact"], required),
        "equal_identity_ok": target["equal_identity_ok"],
    }


def closure_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 HighP-PLT 低筛闭合桥包。"""
    rows = []
    windows: dict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "geometric_upper": 0.0,
            "required_m2": 0.0,
            "actual_low_survivor": 0.0,
            "gate_consumed": 0.0,
            "formal_consumed": 0.0,
            "gate_low_lower": 0.0,
            "formal_low_lower": 0.0,
            "all_equal_identity_ok": True,
        }
    )
    total = {
        "geometric_upper": 0.0,
        "required_m2": 0.0,
        "actual_low_survivor": 0.0,
        "gate_consumed": 0.0,
        "formal_consumed": 0.0,
        "gate_low_lower": 0.0,
        "formal_low_lower": 0.0,
        "all_equal_identity_ok": True,
    }
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        for point_count in m_values:
            item = closure_row(
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
            rows.append(item)
            key = (prime_bound, block, shift)
            for name in (
                "geometric_upper",
                "required_m2",
                "actual_low_survivor",
                "gate_consumed",
                "formal_consumed",
                "gate_low_lower",
                "formal_low_lower",
            ):
                total[name] += item[name]
                windows[key][name] += item[name]
            total["all_equal_identity_ok"] = total["all_equal_identity_ok"] and item["equal_identity_ok"]
            windows[key]["all_equal_identity_ok"] = (
                windows[key]["all_equal_identity_ok"] and item["equal_identity_ok"]
            )
    window_rows = []
    for key, value in sorted(windows.items()):
        value["p"], value["block"], value["shift"] = key
        value["gate_margin_to_required"] = value["gate_low_lower"] - value["required_m2"]
        value["formal_margin_to_required"] = value["formal_low_lower"] - value["required_m2"]
        value["actual_margin_to_required"] = value["actual_low_survivor"] - value["required_m2"]
        value["gate_pass"] = value["gate_low_lower"] >= value["required_m2"]
        value["formal_pass"] = value["formal_low_lower"] >= value["required_m2"]
        value["actual_pass"] = value["actual_low_survivor"] >= value["required_m2"]
        value["gate_low_over_required"] = ratio(value["gate_low_lower"], value["required_m2"])
        value["formal_low_over_required"] = ratio(value["formal_low_lower"], value["required_m2"])
        value["actual_low_over_required"] = ratio(value["actual_low_survivor"], value["required_m2"])
        window_rows.append(value)
    total["gate_margin_to_required"] = total["gate_low_lower"] - total["required_m2"]
    total["formal_margin_to_required"] = total["formal_low_lower"] - total["required_m2"]
    total["actual_margin_to_required"] = total["actual_low_survivor"] - total["required_m2"]
    total["gate_pass"] = total["gate_low_lower"] >= total["required_m2"]
    total["formal_pass"] = total["formal_low_lower"] >= total["required_m2"]
    total["actual_pass"] = total["actual_low_survivor"] >= total["required_m2"]
    total["gate_low_over_required"] = ratio(total["gate_low_lower"], total["required_m2"])
    total["formal_low_over_required"] = ratio(total["formal_low_lower"], total["required_m2"])
    total["actual_low_over_required"] = ratio(total["actual_low_survivor"], total["required_m2"])
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "total": total,
        "windows": window_rows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出 HighP-PLT 低筛闭合桥表。"""
    total = package["total"]
    print(
        "scope geom required actual_low gate_del formal_del gate_low formal_low "
        "actual_margin gate_margin formal_margin actual_req gate_req formal_req "
        "actual_pass gate_pass formal_pass identity",
        flush=True,
    )
    print(
        f"highP-total {total['geometric_upper']:.0f} {total['required_m2']:.6f} "
        f"{total['actual_low_survivor']:.0f} {total['gate_consumed']:.0f} "
        f"{total['formal_consumed']:.0f} {total['gate_low_lower']:.0f} "
        f"{total['formal_low_lower']:.0f} {total['actual_margin_to_required']:.6f} "
        f"{total['gate_margin_to_required']:.6f} {total['formal_margin_to_required']:.6f} "
        f"{fmt(total['actual_low_over_required'])} {fmt(total['gate_low_over_required'])} "
        f"{fmt(total['formal_low_over_required'])} {total['actual_pass']} "
        f"{total['gate_pass']} {total['formal_pass']} {total['all_equal_identity_ok']}",
        flush=True,
    )
    print(
        "p block shift geom required actual_low gate_del formal_del gate_low formal_low "
        "actual_margin gate_margin formal_margin actual_req gate_req formal_req "
        "actual_pass gate_pass formal_pass identity",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['geometric_upper']:.0f} {row['required_m2']:.6f} "
            f"{row['actual_low_survivor']:.0f} {row['gate_consumed']:.0f} "
            f"{row['formal_consumed']:.0f} {row['gate_low_lower']:.0f} "
            f"{row['formal_low_lower']:.0f} {row['actual_margin_to_required']:.6f} "
            f"{row['gate_margin_to_required']:.6f} {row['formal_margin_to_required']:.6f} "
            f"{fmt(row['actual_low_over_required'])} {fmt(row['gate_low_over_required'])} "
            f"{fmt(row['formal_low_over_required'])} {row['actual_pass']} "
            f"{row['gate_pass']} {row['formal_pass']} {row['all_equal_identity_ok']}",
            flush=True,
        )
    print(
        "p block shift m geom required actual_low gate_del formal_del gate_low formal_low "
        "actual_margin gate_margin formal_margin actual_req gate_req formal_req "
        "actual_pass gate_pass formal_pass identity",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['geometric_upper']:.0f} {row['required_m2']:.6f} "
            f"{row['actual_low_survivor']:.0f} {row['gate_consumed']:.0f} "
            f"{row['formal_consumed']:.0f} {row['gate_low_lower']:.0f} "
            f"{row['formal_low_lower']:.0f} {row['actual_margin_to_required']:.6f} "
            f"{row['gate_margin_to_required']:.6f} {row['formal_margin_to_required']:.6f} "
            f"{fmt(row['actual_low_over_required'])} {fmt(row['gate_low_over_required'])} "
            f"{fmt(row['formal_low_over_required'])} {row['actual_pass']} "
            f"{row['gate_pass']} {row['formal_pass']} {row['equal_identity_ok']}",
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

    package = closure_package(
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
