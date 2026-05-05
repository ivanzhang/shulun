#!/usr/bin/env python3
"""AlphaTail C13 低筛 AP 单点化归约合同审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_reduction_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract import (
    low_deletion_allowance_package,
)
from prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_deletion_audit import ap_deletion_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def ratio(numerator: float, denominator: float) -> float | None:
    """返回安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def by_key(rows: list[dict]) -> dict[tuple[int, int, int], dict]:
    """按窗口键索引。"""
    return {(row["p"], row["block"], row["shift"]): row for row in rows}


def ap_singleton_package(
    selected: str,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
) -> dict:
    """返回 AP 单点化归约合同包。"""
    ap = ap_deletion_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    allowance = low_deletion_allowance_package(
        selected,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
    )
    allowance_by_window = by_key(allowance["windows"])
    rows = []
    for row in ap["windows"]:
        allowed = allowance_by_window[(row["p"], row["block"], row["shift"])]
        singleton_identity = (
            row["actual_deleted"]
            == row["unique_ap_deletions"]
            == row["raw_ap_deletions"]
            == row["active_ap_class_count"]
            and row["max_ap_per_class"] <= 1
        )
        rows.append(
            {
                "p": row["p"],
                "block": row["block"],
                "shift": row["shift"],
                "actual_deleted": row["actual_deleted"],
                "active_classes": row["active_ap_class_count"],
                "ap_classes": row["ap_class_count"],
                "raw_ap": row["raw_ap_deletions"],
                "unique_ap": row["unique_ap_deletions"],
                "max_ap_per_class": row["max_ap_per_class"],
                "allowed_deletion": allowed["allowed_deletion"],
                "deletion_margin": allowed["allowed_deletion"] - row["active_ap_class_count"],
                "active_class_density_geom": ratio(
                    row["active_ap_class_count"],
                    row["geometric_upper"],
                ),
                "active_class_density_classes": ratio(
                    row["active_ap_class_count"],
                    row["ap_class_count"],
                ),
                "allowed_density_geom": allowed["allowed_deletion_density"],
                "allowed_density_classes": ratio(
                    allowed["allowed_deletion"],
                    row["ap_class_count"],
                ),
                "singleton_identity": singleton_identity,
                "class_allowance_pass": row["active_ap_class_count"] <= allowed["allowed_deletion"],
            }
        )
    total_ap = ap["total"]
    total_allowance = allowance["total"]
    total_singleton_identity = (
        total_ap["actual_deleted"]
        == total_ap["unique_ap_deletions"]
        == total_ap["raw_ap_deletions"]
        == total_ap["active_ap_class_count"]
        and total_ap["max_ap_per_class"] <= 1
    )
    total = {
        "windows": len(rows),
        "actual_deleted": total_ap["actual_deleted"],
        "active_classes": total_ap["active_ap_class_count"],
        "ap_classes": total_ap["ap_class_count"],
        "raw_ap": total_ap["raw_ap_deletions"],
        "unique_ap": total_ap["unique_ap_deletions"],
        "max_ap_per_class": total_ap["max_ap_per_class"],
        "allowed_deletion": total_allowance["allowed_deletion"],
        "deletion_margin": total_allowance["allowed_deletion"] - total_ap["active_ap_class_count"],
        "active_class_density_geom": ratio(
            total_ap["active_ap_class_count"],
            total_allowance["geometric_upper"],
        ),
        "active_class_density_classes": ratio(
            total_ap["active_ap_class_count"],
            total_ap["ap_class_count"],
        ),
        "singleton_identity": total_singleton_identity,
        "all_singleton_identity": all(row["singleton_identity"] for row in rows),
        "all_class_allowance_pass": all(row["class_allowance_pass"] for row in rows),
        "min_deletion_margin": min((row["deletion_margin"] for row in rows), default=None),
    }
    total["allowed_density_geom"] = total_allowance["allowed_deletion_density"]
    return {
        "selected": selected,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "status": "ap_singleton_reduction_sample_closed_global_open",
        "total": total,
        "windows": rows,
        "ap": ap,
        "allowance": allowance,
    }


def print_table(package: dict) -> None:
    """输出 AP 单点化归约合同表。"""
    total = package["total"]
    print(
        "scope windows actual active classes raw unique max_class allowed margin "
        "active_geom active_classes allowed_geom singleton class_pay",
        flush=True,
    )
    print(
        f"highP-total {total['windows']} {total['actual_deleted']:.0f} "
        f"{total['active_classes']} {total['ap_classes']} "
        f"{total['raw_ap']:.0f} {total['unique_ap']:.0f} "
        f"{total['max_ap_per_class']} {total['allowed_deletion']:.6f} "
        f"{total['deletion_margin']:.6f} "
        f"{fmt(total['active_class_density_geom'])} "
        f"{fmt(total['active_class_density_classes'])} "
        f"{fmt(total['allowed_density_geom'])} "
        f"{total['all_singleton_identity']} {total['all_class_allowance_pass']}",
        flush=True,
    )
    print(
        "p block shift actual active classes raw unique max_class allowed margin "
        "active_geom active_classes allowed_geom allowed_classes singleton class_pay",
        flush=True,
    )
    for row in package["windows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['actual_deleted']:.0f} {row['active_classes']} "
            f"{row['ap_classes']} {row['raw_ap']:.0f} {row['unique_ap']:.0f} "
            f"{row['max_ap_per_class']} {row['allowed_deletion']:.6f} "
            f"{row['deletion_margin']:.6f} "
            f"{fmt(row['active_class_density_geom'])} "
            f"{fmt(row['active_class_density_classes'])} "
            f"{fmt(row['allowed_density_geom'])} "
            f"{fmt(row['allowed_density_classes'])} "
            f"{row['singleton_identity']} {row['class_allowance_pass']}",
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

    package = ap_singleton_package(
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
