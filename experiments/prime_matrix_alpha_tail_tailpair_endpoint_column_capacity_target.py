#!/usr/bin/env python3
"""AlphaTail 端点列残基核的容量目标审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_capacity_target.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_endpoint_column_residue_audit import column_residue_rows
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def capacity_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    persistent_count: int,
    persistent_excess: float,
    phase_modulus: int,
) -> dict:
    """计算列核相对均衡模型的超载目标常数。"""
    package = column_residue_rows(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        persistent_count,
        persistent_excess,
        phase_modulus,
    )
    total_axis_excess = sum(row["total_excess"] for row in package["rows"] if row["solvable"])

    def annotate(group: dict, modulus_key: str, residue_key: str) -> dict:
        modulus = group[modulus_key]
        excess = group["total_excess"]
        model_share = total_axis_excess / modulus if modulus else 0.0
        overload = excess / model_share if model_share else None
        return {
            **group,
            "total_axis_excess": total_axis_excess,
            "model_share": model_share,
            "overload_constant_required": overload,
            "density": excess / total_axis_excess if total_axis_excess else 0.0,
            "uniform_density": 1 / modulus if modulus else 0.0,
            "residue_label": f"{group[residue_key]} mod {modulus}",
        }

    exact_targets = [
        annotate(group, "column_modulus", "column_residue")
        for group in package["exact_groups"]
    ]
    component_targets = [
        annotate(group, "core_modulus", "core_residue")
        for group in package["components"]
    ]
    exact_targets.sort(key=lambda item: (-(item["overload_constant_required"] or 0), -item["total_excess"]))
    component_targets.sort(key=lambda item: (-(item["overload_constant_required"] or 0), -item["total_excess"]))
    return {
        "total_axis_excess": total_axis_excess,
        "exact_targets": exact_targets,
        "component_targets": component_targets,
        "max_component_overload": max(
            (item["overload_constant_required"] for item in component_targets if item["overload_constant_required"]),
            default=0.0,
        ),
        "max_exact_overload": max(
            (item["overload_constant_required"] for item in exact_targets if item["overload_constant_required"]),
            default=0.0,
        ),
    }


def print_table(package: dict) -> None:
    """输出列容量目标表。"""
    print(f"total_axis_excess {package['total_axis_excess']:.6f}", flush=True)
    print("component_targets", flush=True)
    print("residue modulus key_count excess density uniform_density required_C keys", flush=True)
    for item in package["component_targets"]:
        print(
            f"{item['core_residue']} {item['core_modulus']} {item['key_count']} "
            f"{item['total_excess']:.6f} {item['density']:.6f} "
            f"{item['uniform_density']:.6f} {item['overload_constant_required']:.6f} "
            f"{','.join(item['keys'])}",
            flush=True,
        )
    print("exact_targets", flush=True)
    print("residue modulus key_count excess density uniform_density required_C keys", flush=True)
    for item in package["exact_targets"]:
        print(
            f"{item['column_residue']} {item['column_modulus']} {item['key_count']} "
            f"{item['total_excess']:.6f} {item['density']:.6f} "
            f"{item['uniform_density']:.6f} {item['overload_constant_required']:.6f} "
            f"{','.join(item['keys'])}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--persistent-count", type=int, default=2)
    parser.add_argument("--persistent-excess", type=float, default=20.0)
    parser.add_argument("--phase-modulus", type=int, default=210)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = capacity_rows(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.persistent_count,
        args.persistent_excess,
        args.phase_modulus,
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
