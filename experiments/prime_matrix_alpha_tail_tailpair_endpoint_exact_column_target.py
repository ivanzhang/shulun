#!/usr/bin/env python3
"""AlphaTail 端点精确列目标证书输入审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_exact_column_target.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --target-residue 4 --target-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit import axis_lock_rows
from prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit import collect_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def target_records(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    persistent_count: int,
    persistent_excess: float,
    phase_modulus: int,
    target_residue: int,
    target_modulus: int,
) -> dict:
    """抽取某个精确右端列目标下的全部端点记录。"""
    axis_keys = {
        row["key"]: row
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
        )
        if row["endpoint"] == "right" and row["route"] == "EXACT_AXIS_PHASE_LOCK_COLUMNCRT_INPUT"
    }
    rows = []
    for record in collect_records(selected, m_values, alpha, num_primes, local_c, endpoint_theta):
        if record["key"] not in axis_keys:
            continue
        if record["d_upper"] % target_modulus != target_residue % target_modulus:
            continue
        axis = axis_keys[record["key"]]
        rows.append(
            {
                "key": record["key"],
                "window_id": record["window_id"],
                "p": record["p"],
                "block": record["block"],
                "shift": record["shift"],
                "m": record["m"],
                "best_frequency": axis["best_frequency"],
                "d_lower": record["d_lower"],
                "d_upper": record["d_upper"],
                "d_upper_residue": record["d_upper"] % target_modulus,
                "excess": record["excess"],
                "required_c": record["required_c"],
            }
        )
    key_totals: dict[str, dict] = {}
    for row in rows:
        key_totals.setdefault(
            row["key"],
            {
                "key": row["key"],
                "occurrences": 0,
                "total_excess": 0.0,
                "windows": [],
            },
        )
        key_totals[row["key"]]["occurrences"] += 1
        key_totals[row["key"]]["total_excess"] += row["excess"]
        key_totals[row["key"]]["windows"].append(row["window_id"])
    key_rows = sorted(key_totals.values(), key=lambda item: (-item["total_excess"], item["key"]))
    total_excess = sum(row["excess"] for row in rows)
    return {
        "target": f"{target_residue} mod {target_modulus}",
        "target_residue": target_residue,
        "target_modulus": target_modulus,
        "record_count": len(rows),
        "key_count": len(key_rows),
        "window_count": len({row["window_id"] for row in rows}),
        "p_support_count": len({row["p"] for row in rows}),
        "total_excess": total_excess,
        "key_rows": key_rows,
        "records": rows,
        "route": "EXACT_COLUMNCRT_PDEC_INPUT" if rows else "EMPTY_TARGET",
    }


def print_table(package: dict) -> None:
    """输出精确列目标证书输入。"""
    print(
        f"target {package['target']} route {package['route']} "
        f"records {package['record_count']} keys {package['key_count']} "
        f"windows {package['window_count']} p_support {package['p_support_count']} "
        f"excess {package['total_excess']:.6f}",
        flush=True,
    )
    print("key_rows", flush=True)
    print("key occurrences excess windows", flush=True)
    for row in package["key_rows"]:
        print(
            f"{row['key']} {row['occurrences']} {row['total_excess']:.6f} "
            f"{','.join(row['windows'])}",
            flush=True,
        )
    print("records", flush=True)
    print("key window d_interval d_upper_residue excess required_C", flush=True)
    for row in package["records"]:
        print(
            f"{row['key']} {row['window_id']} [{row['d_lower']},{row['d_upper']}] "
            f"{row['d_upper_residue']} {row['excess']:.6f} {row['required_c']:.6f}",
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
    parser.add_argument("--target-residue", type=int, default=4)
    parser.add_argument("--target-modulus", type=int, default=210)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = target_records(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.persistent_count,
        args.persistent_excess,
        args.phase_modulus,
        args.target_residue,
        args.target_modulus,
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
