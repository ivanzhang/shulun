#!/usr/bin/env python3
"""AlphaTail 单侧端点频率的列残基锁相审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_tailpair_endpoint_frequency_route_audit import frequency_route_rows
from prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit import collect_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def axis_lock_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    persistent_count: int,
    persistent_excess: float,
    phase_modulus: int,
) -> list[dict]:
    """检查单侧端点责任频率是否锁定到单一列残基。"""
    route_rows = frequency_route_rows(
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
    axis_routes = {
        row["key"]: row
        for row in route_rows
        if row["route"] == "OneSidedEndpointCRTDefect/ColumnCRT"
    }
    records_by_key: dict[str, list[dict]] = defaultdict(list)
    for record in collect_records(selected, m_values, alpha, num_primes, local_c, endpoint_theta):
        if record["key"] in axis_routes:
            records_by_key[record["key"]].append(record)

    rows = []
    for key, route_row in axis_routes.items():
        freq_x, freq_y = route_row["best_frequency"]
        endpoint = "right" if freq_x == 0 else "left"
        lock_loads: dict[int, float] = defaultdict(float)
        lock_windows: dict[int, set[str]] = defaultdict(set)
        for record in records_by_key[key]:
            if endpoint == "right":
                lock_value = (freq_y * record["d_upper"]) % phase_modulus
            else:
                lock_value = (freq_x * record["d_lower"]) % phase_modulus
            lock_loads[lock_value] += record["excess"]
            lock_windows[lock_value].add(record["window_id"])
        total_excess = sum(lock_loads.values())
        max_lock_excess = max(lock_loads.values(), default=0.0)
        locked = len(lock_loads) == 1
        rows.append(
            {
                "key": key,
                "endpoint": endpoint,
                "best_frequency": route_row["best_frequency"],
                "phase_modulus": phase_modulus,
                "lock_class_count": len(lock_loads),
                "locked": locked,
                "total_excess": total_excess,
                "max_lock_excess": max_lock_excess,
                "max_lock_fraction": max_lock_excess / total_excess if total_excess else 0.0,
                "lock_classes": [
                    {
                        "value": value,
                        "excess": lock_loads[value],
                        "support_count": len(lock_windows[value]),
                    }
                    for value in sorted(lock_loads, key=lambda item: (-lock_loads[item], item))[:5]
                ],
                "route": "EXACT_AXIS_PHASE_LOCK_COLUMNCRT_INPUT"
                if locked
                else "AXIS_PHASE_SPREAD_NEEDS_COLUMN_BOUND",
            }
        )
    rows.sort(key=lambda item: (-item["total_excess"], item["key"]))
    return rows


def print_table(rows: list[dict]) -> None:
    """输出轴向锁相表。"""
    print(
        "key endpoint best_freq Q lock_classes locked total_excess "
        "max_lock_fraction route locks",
        flush=True,
    )
    for row in rows:
        freq_x, freq_y = row["best_frequency"]
        locks = ",".join(
            f"{item['value']}:{item['excess']:.6f}/{item['support_count']}"
            for item in row["lock_classes"]
        )
        print(
            f"{row['key']} {row['endpoint']} ({freq_x},{freq_y}) "
            f"{row['phase_modulus']} {row['lock_class_count']} {row['locked']} "
            f"{row['total_excess']:.6f} {row['max_lock_fraction']:.6f} "
            f"{row['route']} {locks}",
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

    rows = axis_lock_rows(
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
        print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
