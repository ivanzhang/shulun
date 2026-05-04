#!/usr/bin/env python3
"""AlphaTail 单侧端点锁相的列残基反解审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_residue_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from math import gcd

from prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit import axis_lock_rows
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def inverse_mod(value: int, modulus: int) -> int:
    """返回 value 在 modulus 下的乘法逆元。"""
    return pow(value % modulus, -1, modulus)


def solve_linear_congruence(coefficient: int, value: int, modulus: int) -> dict:
    """求解 coefficient*x == value mod modulus 的简化列残基类。"""
    divisor = gcd(coefficient, modulus)
    if value % divisor != 0:
        return {
            "solvable": False,
            "residue": None,
            "modulus": None,
            "gcd": divisor,
        }
    reduced_coefficient = coefficient // divisor
    reduced_value = value // divisor
    reduced_modulus = modulus // divisor
    residue = (inverse_mod(reduced_coefficient, reduced_modulus) * reduced_value) % reduced_modulus
    return {
        "solvable": True,
        "residue": residue,
        "modulus": reduced_modulus,
        "gcd": divisor,
    }


def compatible(left: dict, right: dict) -> bool:
    """判断两个列残基类是否有公共投影。"""
    common_modulus = gcd(left["column_modulus"], right["column_modulus"])
    return (left["column_residue"] - right["column_residue"]) % common_modulus == 0


def components(rows: list[dict]) -> list[list[int]]:
    """按残基兼容性生成连通分量。"""
    parent = list(range(len(rows)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    for left in range(len(rows)):
        for right in range(left + 1, len(rows)):
            if compatible(rows[left], rows[right]):
                union(left, right)
    grouped: dict[int, list[int]] = {}
    for index in range(len(rows)):
        grouped.setdefault(find(index), []).append(index)
    return list(grouped.values())


def component_summary(rows: list[dict]) -> list[dict]:
    """返回每个兼容分量的公共低模投影。"""
    result = []
    for indexes in components(rows):
        core_modulus = 0
        for index in indexes:
            core_modulus = rows[index]["column_modulus"] if core_modulus == 0 else gcd(
                core_modulus, rows[index]["column_modulus"]
            )
        core_residue = rows[indexes[0]]["column_residue"] % core_modulus
        result.append(
            {
                "core_modulus": core_modulus,
                "core_residue": core_residue,
                "key_count": len(indexes),
                "total_excess": sum(rows[index]["total_excess"] for index in indexes),
                "keys": [rows[index]["key"] for index in indexes],
            }
        )
    result.sort(key=lambda item: (-item["total_excess"], item["core_modulus"], item["core_residue"]))
    return result


def column_residue_rows(
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
    """把轴向锁相反解为右/左端列残基类并聚合。"""
    rows = []
    for row in axis_lock_rows(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        persistent_count,
        persistent_excess,
        phase_modulus,
    ):
        if row["route"] != "EXACT_AXIS_PHASE_LOCK_COLUMNCRT_INPUT":
            continue
        if len(row["lock_classes"]) != 1:
            continue
        freq_x, freq_y = row["best_frequency"]
        coefficient = freq_y if row["endpoint"] == "right" else freq_x
        lock_value = row["lock_classes"][0]["value"]
        solution = solve_linear_congruence(coefficient, lock_value, phase_modulus)
        rows.append(
            {
                "key": row["key"],
                "endpoint": row["endpoint"],
                "frequency": row["best_frequency"],
                "coefficient": coefficient,
                "lock_value": lock_value,
                "phase_modulus": phase_modulus,
                "solvable": solution["solvable"],
                "column_residue": solution["residue"],
                "column_modulus": solution["modulus"],
                "gcd": solution["gcd"],
                "total_excess": row["total_excess"],
                "route": "COLUMN_RESIDUE_CLASS_READY" if solution["solvable"] else "INCONSISTENT_AXIS_LOCK",
            }
        )
    exact_groups: dict[tuple[str, int, int], dict] = {}
    for row in rows:
        if not row["solvable"]:
            continue
        key = (row["endpoint"], row["column_modulus"], row["column_residue"])
        exact_groups.setdefault(
            key,
            {
                "endpoint": row["endpoint"],
                "column_modulus": row["column_modulus"],
                "column_residue": row["column_residue"],
                "key_count": 0,
                "total_excess": 0.0,
                "keys": [],
            },
        )
        exact_groups[key]["key_count"] += 1
        exact_groups[key]["total_excess"] += row["total_excess"]
        exact_groups[key]["keys"].append(row["key"])
    return {
        "rows": rows,
        "exact_groups": sorted(
            exact_groups.values(),
            key=lambda item: (-item["total_excess"], item["column_modulus"], item["column_residue"]),
        ),
        "components": component_summary([row for row in rows if row["solvable"]]),
    }


def print_table(package: dict) -> None:
    """输出列残基反解表。"""
    print("rows", flush=True)
    print("key endpoint freq lock Q gcd column_residue column_modulus excess route", flush=True)
    for row in package["rows"]:
        freq_x, freq_y = row["frequency"]
        print(
            f"{row['key']} {row['endpoint']} ({freq_x},{freq_y}) {row['lock_value']} "
            f"{row['phase_modulus']} {row['gcd']} {row['column_residue']} "
            f"{row['column_modulus']} {row['total_excess']:.6f} {row['route']}",
            flush=True,
        )
    print("exact_groups", flush=True)
    print("endpoint residue modulus key_count excess keys", flush=True)
    for group in package["exact_groups"]:
        print(
            f"{group['endpoint']} {group['column_residue']} {group['column_modulus']} "
            f"{group['key_count']} {group['total_excess']:.6f} {','.join(group['keys'])}",
            flush=True,
        )
    print("compatible_components", flush=True)
    print("core_residue core_modulus key_count excess keys", flush=True)
    for group in package["components"]:
        print(
            f"{group['core_residue']} {group['core_modulus']} {group['key_count']} "
            f"{group['total_excess']:.6f} {','.join(group['keys'])}",
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

    package = column_residue_rows(
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
