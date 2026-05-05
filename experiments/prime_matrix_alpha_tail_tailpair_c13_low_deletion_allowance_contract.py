#!/usr/bin/env python3
"""AlphaTail C13 低筛删除允许量合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract import (
    edge_structural_ceiling,
)
from prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target import row_target
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def layer_allowance_row(
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
    """返回单层低筛删除允许量。"""
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
    edge_envelope = num_primes * edge_structural_ceiling(point_count)
    geometric_upper = target["geometric_upper"]
    low_survivor = target["low_survivor_exact"]
    low_deleted = geometric_upper - low_survivor
    required_with_edge = target["required_m2"] + edge_envelope
    allowed_deletion = geometric_upper - required_with_edge
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "geometric_upper": geometric_upper,
        "low_survivor": low_survivor,
        "low_deleted": low_deleted,
        "required_m2": target["required_m2"],
        "edge_envelope": edge_envelope,
        "required_with_edge": required_with_edge,
        "allowed_deletion": allowed_deletion,
        "deletion_margin": allowed_deletion - low_deleted,
        "low_survival_density": ratio(low_survivor, geometric_upper),
        "low_deletion_density": ratio(low_deleted, geometric_upper),
        "required_edge_density": ratio(required_with_edge, geometric_upper),
        "allowed_deletion_density": ratio(allowed_deletion, geometric_upper),
        "density_margin": ratio(allowed_deletion - low_deleted, geometric_upper),
        "allowance_pass": low_deleted <= allowed_deletion,
        "identity_ok": target["equal_identity_ok"],
    }


def low_deletion_allowance_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回低筛删除允许量合同包。"""
    rows = []
    windows = []
    for prime_bound, block, shift in parse_selected(selected):
        if prime_bound <= finite_p_cut:
            continue
        window_rows = [
            layer_allowance_row(
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
            for point_count in m_values
        ]
        rows.extend(window_rows)
        geometric_upper = sum(row["geometric_upper"] for row in window_rows)
        low_survivor = sum(row["low_survivor"] for row in window_rows)
        low_deleted = sum(row["low_deleted"] for row in window_rows)
        required_with_edge = sum(row["required_with_edge"] for row in window_rows)
        allowed_deletion = sum(row["allowed_deletion"] for row in window_rows)
        windows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "geometric_upper": geometric_upper,
                "low_survivor": low_survivor,
                "low_deleted": low_deleted,
                "required_with_edge": required_with_edge,
                "allowed_deletion": allowed_deletion,
                "deletion_margin": allowed_deletion - low_deleted,
                "low_survival_density": ratio(low_survivor, geometric_upper),
                "low_deletion_density": ratio(low_deleted, geometric_upper),
                "required_edge_density": ratio(required_with_edge, geometric_upper),
                "allowed_deletion_density": ratio(allowed_deletion, geometric_upper),
                "density_margin": ratio(allowed_deletion - low_deleted, geometric_upper),
                "allowance_pass": low_deleted <= allowed_deletion,
                "identity_ok": all(row["identity_ok"] for row in window_rows),
            }
        )
    total_geometric = sum(row["geometric_upper"] for row in windows)
    total_low_survivor = sum(row["low_survivor"] for row in windows)
    total_low_deleted = sum(row["low_deleted"] for row in windows)
    total_required_edge = sum(row["required_with_edge"] for row in windows)
    total_allowed = sum(row["allowed_deletion"] for row in windows)
    total = {
        "windows": len(windows),
        "geometric_upper": total_geometric,
        "low_survivor": total_low_survivor,
        "low_deleted": total_low_deleted,
        "required_with_edge": total_required_edge,
        "allowed_deletion": total_allowed,
        "deletion_margin": total_allowed - total_low_deleted,
        "low_survival_density": ratio(total_low_survivor, total_geometric),
        "low_deletion_density": ratio(total_low_deleted, total_geometric),
        "required_edge_density": ratio(total_required_edge, total_geometric),
        "allowed_deletion_density": ratio(total_allowed, total_geometric),
        "density_margin": ratio(total_allowed - total_low_deleted, total_geometric),
        "min_deletion_margin": min((row["deletion_margin"] for row in windows), default=None),
        "min_density_margin": min((row["density_margin"] for row in windows), default=None),
        "all_allowance_pass": all(row["allowance_pass"] for row in windows),
        "all_identity_ok": all(row["identity_ok"] for row in windows),
    }
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "low_deletion_allowance_sample_closed_global_open",
        "total": total,
        "windows": windows,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出低筛删除允许量合同表。"""
    total = package["total"]
    print(
        "scope windows geom survivor deleted required_edge allowed margin "
        "surv_dens del_dens req_dens allow_dens dens_margin min_margin "
        "min_dens allowance identity",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['geometric_upper']:.0f} "
        f"{total['low_survivor']:.0f} {total['low_deleted']:.0f} "
        f"{total['required_with_edge']:.6f} {total['allowed_deletion']:.6f} "
        f"{total['deletion_margin']:.6f} {fmt(total['low_survival_density'])} "
        f"{fmt(total['low_deletion_density'])} {fmt(total['required_edge_density'])} "
        f"{fmt(total['allowed_deletion_density'])} {fmt(total['density_margin'])} "
        f"{fmt(total['min_deletion_margin'])} {fmt(total['min_density_margin'])} "
        f"{total['all_allowance_pass']} {total['all_identity_ok']}",
        flush=True,
    )
    print(
        "p block shift geom survivor deleted required_edge allowed margin "
        "surv_dens del_dens req_dens allow_dens dens_margin allowance identity",
        flush=True,
    )
    for window in package["windows"]:
        print(
            f"{window['p']} {window['block']} {window['shift']} "
            f"{window['geometric_upper']:.0f} {window['low_survivor']:.0f} "
            f"{window['low_deleted']:.0f} {window['required_with_edge']:.6f} "
            f"{window['allowed_deletion']:.6f} {window['deletion_margin']:.6f} "
            f"{fmt(window['low_survival_density'])} "
            f"{fmt(window['low_deletion_density'])} "
            f"{fmt(window['required_edge_density'])} "
            f"{fmt(window['allowed_deletion_density'])} "
            f"{fmt(window['density_margin'])} "
            f"{window['allowance_pass']} {window['identity_ok']}",
            flush=True,
        )
    print(
        "p block shift m geom survivor deleted required edge required_edge "
        "allowed margin surv_dens del_dens req_dens allow_dens dens_margin pass",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['geometric_upper']:.0f} {row['low_survivor']:.0f} "
            f"{row['low_deleted']:.0f} {row['required_m2']:.6f} "
            f"{row['edge_envelope']} {row['required_with_edge']:.6f} "
            f"{row['allowed_deletion']:.6f} {row['deletion_margin']:.6f} "
            f"{fmt(row['low_survival_density'])} "
            f"{fmt(row['low_deletion_density'])} "
            f"{fmt(row['required_edge_density'])} "
            f"{fmt(row['allowed_deletion_density'])} "
            f"{fmt(row['density_margin'])} {row['allowance_pass']}",
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

    package = low_deletion_allowance_package(
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
