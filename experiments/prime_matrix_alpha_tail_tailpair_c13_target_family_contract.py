#!/usr/bin/env python3
"""AlphaTail C13 目标窗口族合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_master_contract import master_contract_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def is_power_of_two(value: int) -> bool:
    """判断正整数是否为 2 的幂。"""
    return value > 0 and (value & (value - 1)) == 0


def next_power_of_two(value: int) -> int:
    """返回不小于 value 的最小 2 的幂。"""
    if value <= 1:
        return 1
    return 1 << (value - 1).bit_length()


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def window_maps(master: dict) -> tuple[dict, dict]:
    """按窗口键索引结构判据与 PLT 结果。"""
    structural = {
        (row["p"], row["block"], row["shift"]): row
        for row in master["structural"]["windows"]
    }
    plt = {
        (row["p"], row["block"], row["shift"]): row
        for row in master["plt"]["windows"]
    }
    return structural, plt


def layer_rows(master: dict, key: tuple[int, int, int]) -> list[dict]:
    """抽取同一窗口的所有 m 层结构行。"""
    return [
        row
        for row in master["structural"]["rows"]
        if (row["p"], row["block"], row["shift"]) == key
    ]


def target_family_contract_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回目标窗口族合同审计包。"""
    master = master_contract_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    structural_by_window, plt_by_window = window_maps(master)
    rows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        key = (prime_bound, block, shift)
        structural = structural_by_window[key]
        plt = plt_by_window[key]
        layers = layer_rows(master, key)
        low_min_values = [row["low_min"] for row in layers]
        n_span_values = [row["n_span"] for row in layers]
        block_power2 = is_power_of_two(block)
        dyadic_ceiling = block == next_power_of_two(prime_bound + 1)
        dyadic_band = prime_bound < block < 2 * prime_bound
        shift_mod6 = abs(shift) % 6 == 0
        n_span_guard = all(row["n_condition"] for row in layers)
        block_guard = all(row["block_condition"] for row in layers)
        syntax_pass = block_power2 and dyadic_band and dyadic_ceiling and shift_mod6
        rows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "block_power2": block_power2,
                "dyadic_ceiling": dyadic_ceiling,
                "dyadic_band": dyadic_band,
                "shift_mod6": shift_mod6,
                "syntax_pass": syntax_pass,
                "block_over_p": block / prime_bound,
                "shift_over_p": abs(shift) / prime_bound,
                "min_low_min": min(low_min_values) if low_min_values else None,
                "max_n_span": max(n_span_values) if n_span_values else None,
                "block_guard": block_guard,
                "n_span_guard": n_span_guard,
                "min_block_margin": structural["min_block_margin"],
                "min_n_margin": structural["min_n_margin"],
                "structural_pass": structural["criterion_pass"],
                "gate_pass": plt["gate_pass"],
                "formal_pass": plt["formal_pass"],
                "gate_margin": plt["gate_margin_to_required"],
                "formal_margin": plt["formal_margin_to_required"],
            }
        )
    total = master["total"]
    syntax_pass = all(row["syntax_pass"] for row in rows)
    explicit_contract = syntax_pass and (
        total["total_gate_contract"]
        or total["local_formal_contract"]
        or total["row_formal_contract"]
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "explicit_selected_contract_closed_target_generation_open",
        "target_family_rule_closed": False,
        "target_family_gap": "完整高 P 目标窗口族的生成规则尚未在仓库中形式化。",
        "total": {
            "highp_windows": len(rows),
            "syntax_pass": syntax_pass,
            "structural_pass": total["structural_pass"],
            "total_gate_contract": total["total_gate_contract"],
            "local_formal_contract": total["local_formal_contract"],
            "row_formal_contract": total["row_formal_contract"],
            "explicit_selected_contract": explicit_contract,
            "target_family_rule_closed": False,
        },
        "windows": rows,
        "master": master,
    }


def print_table(package: dict) -> None:
    """输出目标窗口族合同表。"""
    total = package["total"]
    print(
        "scope highp_windows syntax structural total_gate local_formal row_formal "
        "explicit_contract target_rule_closed",
        flush=True,
    )
    print(
        f"highP-selected {total['highp_windows']} {total['syntax_pass']} "
        f"{total['structural_pass']} {total['total_gate_contract']} "
        f"{total['local_formal_contract']} {total['row_formal_contract']} "
        f"{total['explicit_selected_contract']} {total['target_family_rule_closed']}",
        flush=True,
    )
    print(
        "p block shift pow2 ceil band mod6 B_over_p R_over_p min_L max_n "
        "block_margin n_margin structural gate formal gate_margin formal_margin",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['block_power2']} "
            f"{row['dyadic_ceiling']} {row['dyadic_band']} {row['shift_mod6']} "
            f"{row['block_over_p']:.6f} {row['shift_over_p']:.6f} "
            f"{row['min_low_min']} {row['max_n_span']} {row['min_block_margin']} "
            f"{row['min_n_margin']} {row['structural_pass']} {row['gate_pass']} "
            f"{row['formal_pass']} {fmt(row['gate_margin'])} {fmt(row['formal_margin'])}",
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

    package = target_family_contract_package(
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
