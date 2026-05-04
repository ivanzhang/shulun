#!/usr/bin/env python3
"""AlphaTail 端点列核的嵌套精确类压力审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_nested_pressure.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --core-residue 4 --core-modulus 35 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_endpoint_column_capacity_target import capacity_rows
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def is_subclass(child_residue: int, child_modulus: int, core_residue: int, core_modulus: int) -> bool:
    """判断 child 残基类是否包含在 core 残基类中。"""
    return child_modulus % core_modulus == 0 and child_residue % core_modulus == core_residue % core_modulus


def is_nested(left: dict, right: dict) -> bool:
    """判断两个精确类是否存在包含关系。"""
    return is_subclass(
        left["column_residue"],
        left["column_modulus"],
        right["column_residue"],
        right["column_modulus"],
    ) or is_subclass(
        right["column_residue"],
        right["column_modulus"],
        left["column_residue"],
        left["column_modulus"],
    )


def nested_pressure_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    persistent_count: int,
    persistent_excess: float,
    phase_modulus: int,
    core_residue: int,
    core_modulus: int,
) -> dict:
    """抽取某列核下的嵌套精确类压力。"""
    package = capacity_rows(
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
    exact_children = [
        item
        for item in package["exact_targets"]
        if is_subclass(item["column_residue"], item["column_modulus"], core_residue, core_modulus)
    ]
    exact_children.sort(key=lambda item: (-(item["overload_constant_required"] or 0), -item["total_excess"]))
    nested_pairs = []
    for left_index, left in enumerate(exact_children):
        for right in exact_children[left_index + 1 :]:
            if is_nested(left, right):
                nested_pairs.append(
                    {
                        "left": left["residue_label"],
                        "right": right["residue_label"],
                    }
                )
    return {
        "core": f"{core_residue} mod {core_modulus}",
        "total_axis_excess": package["total_axis_excess"],
        "core_rows": [
            item
            for item in package["component_targets"]
            if item["core_residue"] == core_residue and item["core_modulus"] == core_modulus
        ],
        "exact_children": exact_children,
        "strongest_child": exact_children[0] if exact_children else None,
        "weakest_child_required_c": min(
            (item["overload_constant_required"] for item in exact_children if item["overload_constant_required"]),
            default=0.0,
        ),
        "nested_pair_count": len(nested_pairs),
        "nested_pairs": nested_pairs,
        "audit_boundary": "children_are_event_classes_not_disjoint_column_partition",
    }


def print_table(package: dict) -> None:
    """输出嵌套压力账本。"""
    print(f"core {package['core']}", flush=True)
    print(f"total_axis_excess {package['total_axis_excess']:.6f}", flush=True)
    print(f"audit_boundary {package['audit_boundary']}", flush=True)
    print("core_rows", flush=True)
    print("residue modulus key_count excess required_C keys", flush=True)
    for item in package["core_rows"]:
        print(
            f"{item['core_residue']} {item['core_modulus']} {item['key_count']} "
            f"{item['total_excess']:.6f} {item['overload_constant_required']:.6f} "
            f"{','.join(item['keys'])}",
            flush=True,
        )
    print("exact_children", flush=True)
    print("residue modulus key_count excess required_C keys", flush=True)
    for item in package["exact_children"]:
        print(
            f"{item['column_residue']} {item['column_modulus']} {item['key_count']} "
            f"{item['total_excess']:.6f} {item['overload_constant_required']:.6f} "
            f"{','.join(item['keys'])}",
            flush=True,
        )
    strongest = package["strongest_child"]
    if strongest:
        print(
            "strongest_child "
            f"{strongest['column_residue']} {strongest['column_modulus']} "
            f"{strongest['overload_constant_required']:.6f}",
            flush=True,
        )
    print(f"nested_pair_count {package['nested_pair_count']}", flush=True)


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
    parser.add_argument("--core-residue", type=int, default=4)
    parser.add_argument("--core-modulus", type=int, default=35)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = nested_pressure_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.persistent_count,
        args.persistent_excess,
        args.phase_modulus,
        args.core_residue,
        args.core_modulus,
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
