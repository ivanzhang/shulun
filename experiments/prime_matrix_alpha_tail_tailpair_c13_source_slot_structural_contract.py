#!/usr/bin/env python3
"""AlphaTail C13 活跃源槽结构合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_source_slot_structural_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from math import comb

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract import active_ap_classes
from prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract import (
    low_deletion_allowance_package,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def source_key(row: dict) -> tuple[int, int, int, int, int, int]:
    """返回前向源槽键。"""
    return (
        row["m"],
        row["j"],
        row["gap"],
        row["u"],
        row["j1"],
        row["j2"],
    )


def source_slot_ceiling(point_count: int) -> int:
    """返回前向源槽的纯组合上界。"""
    return 2 * comb(point_count, 3)


def row_structural_flags(row: dict, shift: int) -> dict:
    """返回单个活跃类的源槽结构标志。"""
    row_width = abs(shift)
    forward = row["j"] > row["j1"] > row["j2"]
    divisible_gap = ((row["j1"] - row["j2"]) * row_width) % row["u"] == 0
    divisible_residue = ((row["j"] - row["j1"]) * row_width) % row["u"] == 0
    expected_gap = ((row["j1"] - row["j2"]) * row_width) // row["u"] if divisible_gap else None
    expected_residue = ((row["j"] - row["j1"]) * row_width) // row["u"] if divisible_residue else None
    expected_tail_hi = ((row["j"] - row["j2"]) * row_width) // row["u"] if divisible_gap and divisible_residue else None
    return {
        "forward": forward,
        "divisible_gap": divisible_gap,
        "divisible_residue": divisible_residue,
        "gap_identity": expected_gap == row["gap"],
        "residue_identity": forward and expected_residue == row["residue"],
        "tail_low_identity": expected_residue is not None and row["q"] == row["ell"] + expected_residue,
        "tail_high_identity": expected_tail_hi is not None and row["q_plus_gap"] == row["ell"] + expected_tail_hi,
    }


def summarize_rows(rows: list[dict], shift: int, point_count: int, allowed_deletion: float, num_primes: int) -> dict:
    """汇总单层或单窗口源槽结构。"""
    flags = [row_structural_flags(row, shift) for row in rows]
    active_sources = len({source_key(row) for row in rows})
    slot_ceiling = source_slot_ceiling(point_count)
    class_ceiling = num_primes * slot_ceiling
    exact_source_ceiling = num_primes * active_sources
    return {
        "active_classes": len(rows),
        "active_sources": active_sources,
        "slot_ceiling": slot_ceiling,
        "class_ceiling": class_ceiling,
        "exact_source_ceiling": exact_source_ceiling,
        "allowed_deletion": allowed_deletion,
        "class_ceiling_margin": allowed_deletion - class_ceiling,
        "exact_source_margin": allowed_deletion - exact_source_ceiling,
        "source_budget": ratio(allowed_deletion, num_primes),
        "source_budget_margin": None
        if num_primes == 0
        else allowed_deletion / num_primes - active_sources,
        "all_forward": all(flag["forward"] for flag in flags),
        "all_gap_identity": all(flag["gap_identity"] for flag in flags),
        "all_residue_identity": all(flag["residue_identity"] for flag in flags),
        "all_tail_offset_identity": all(
            flag["tail_low_identity"] and flag["tail_high_identity"] for flag in flags
        ),
        "coarse_slot_pay": class_ceiling <= allowed_deletion,
        "exact_source_pay": exact_source_ceiling <= allowed_deletion,
    }


def layer_allowance_by_key(rows: list[dict]) -> dict[tuple[int, int, int, int], dict]:
    """按层键索引允许量。"""
    return {(row["p"], row["block"], row["shift"], row["m"]): row for row in rows}


def window_allowance_by_key(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引允许量。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def source_slot_structural_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回源槽结构合同包。"""
    allowance = low_deletion_allowance_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    layer_allowance = layer_allowance_by_key(allowance["rows"])
    window_allowance = window_allowance_by_key(allowance["windows"])
    layers = []
    windows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        window_rows = []
        window_slot_ceiling = 0
        for point_count in m_values:
            rows = active_ap_classes(prime_bound, block, shift, point_count, alpha, num_primes)
            window_rows.extend(rows)
            window_slot_ceiling += source_slot_ceiling(point_count)
            allowed = layer_allowance[(prime_bound, block, shift, point_count)]
            layers.append(
                {
                    "p": prime_bound,
                    "block": block,
                    "shift": shift,
                    "m": point_count,
                    **summarize_rows(
                        rows,
                        shift,
                        point_count,
                        allowed["allowed_deletion"],
                        num_primes,
                    ),
                }
            )
        allowed_window = window_allowance[(prime_bound, block, shift)]
        window_summary = summarize_rows(
            window_rows,
            shift,
            sum(m_values),
            allowed_window["allowed_deletion"],
            num_primes,
        )
        window_summary["slot_ceiling"] = window_slot_ceiling
        window_summary["class_ceiling"] = num_primes * window_slot_ceiling
        window_summary["class_ceiling_margin"] = (
            allowed_window["allowed_deletion"] - window_summary["class_ceiling"]
        )
        window_summary["coarse_slot_pay"] = (
            window_summary["class_ceiling"] <= allowed_window["allowed_deletion"]
        )
        windows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                **window_summary,
            }
        )
    total_allowed = sum(row["allowed_deletion"] for row in windows)
    total_class_ceiling = sum(row["class_ceiling"] for row in windows)
    total_exact_ceiling = sum(row["exact_source_ceiling"] for row in windows)
    total = {
        "windows": len(windows),
        "active_classes": sum(row["active_classes"] for row in windows),
        "active_sources": sum(row["active_sources"] for row in windows),
        "slot_ceiling": sum(row["slot_ceiling"] for row in windows),
        "class_ceiling": total_class_ceiling,
        "exact_source_ceiling": total_exact_ceiling,
        "allowed_deletion": total_allowed,
        "class_ceiling_margin": total_allowed - total_class_ceiling,
        "exact_source_margin": total_allowed - total_exact_ceiling,
        "all_forward": all(row["all_forward"] for row in windows),
        "all_gap_identity": all(row["all_gap_identity"] for row in windows),
        "all_residue_identity": all(row["all_residue_identity"] for row in windows),
        "all_tail_offset_identity": all(row["all_tail_offset_identity"] for row in windows),
        "all_coarse_slot_pay": all(row["coarse_slot_pay"] for row in windows),
        "all_exact_source_pay": all(row["exact_source_pay"] for row in windows),
        "min_class_ceiling_margin": min((row["class_ceiling_margin"] for row in windows), default=None),
        "min_exact_source_margin": min((row["exact_source_margin"] for row in windows), default=None),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "source_slot_structural_sample_closed_forward_open",
        "total": total,
        "windows": windows,
        "layers": layers,
        "allowance": allowance,
    }


def print_table(package: dict) -> None:
    """输出源槽结构合同表。"""
    total = package["total"]
    print(
        "scope windows active sources slot_ceiling class_ceiling exact_source_ceiling "
        "allowed class_margin exact_margin forward gap_id residue_id tail_offset "
        "coarse_pay exact_pay min_class_margin min_exact_margin",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['active_classes']} "
        f"{total['active_sources']} {total['slot_ceiling']} "
        f"{total['class_ceiling']} {total['exact_source_ceiling']} "
        f"{total['allowed_deletion']:.6f} {total['class_ceiling_margin']:.6f} "
        f"{total['exact_source_margin']:.6f} {total['all_forward']} "
        f"{total['all_gap_identity']} {total['all_residue_identity']} "
        f"{total['all_tail_offset_identity']} {total['all_coarse_slot_pay']} "
        f"{total['all_exact_source_pay']} {fmt(total['min_class_ceiling_margin'])} "
        f"{fmt(total['min_exact_source_margin'])}",
        flush=True,
    )
    print(
        "p block shift active sources slot_ceiling class_ceiling exact_source_ceiling "
        "allowed class_margin exact_margin source_budget source_budget_margin "
        "forward gap_id residue_id tail_offset coarse_pay exact_pay",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['active_classes']} "
            f"{row['active_sources']} {row['slot_ceiling']} {row['class_ceiling']} "
            f"{row['exact_source_ceiling']} {row['allowed_deletion']:.6f} "
            f"{row['class_ceiling_margin']:.6f} {row['exact_source_margin']:.6f} "
            f"{fmt(row['source_budget'])} {fmt(row['source_budget_margin'])} "
            f"{row['all_forward']} {row['all_gap_identity']} "
            f"{row['all_residue_identity']} {row['all_tail_offset_identity']} "
            f"{row['coarse_slot_pay']} {row['exact_source_pay']}",
            flush=True,
        )
    print(
        "p block shift m active sources slot_ceiling class_ceiling exact_source_ceiling "
        "allowed class_margin exact_margin forward gap_id residue_id tail_offset "
        "coarse_pay exact_pay",
        flush=True,
    )
    for row in package["layers"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['active_classes']} {row['active_sources']} "
            f"{row['slot_ceiling']} {row['class_ceiling']} "
            f"{row['exact_source_ceiling']} {row['allowed_deletion']:.6f} "
            f"{row['class_ceiling_margin']:.6f} {row['exact_source_margin']:.6f} "
            f"{row['all_forward']} {row['all_gap_identity']} "
            f"{row['all_residue_identity']} {row['all_tail_offset_identity']} "
            f"{row['coarse_slot_pay']} {row['exact_source_pay']}",
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

    package = source_slot_structural_package(
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
