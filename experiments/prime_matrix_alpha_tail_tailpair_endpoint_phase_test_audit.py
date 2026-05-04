#!/usr/bin/env python3
"""AlphaTail 端点持久键的显式相位测试函数审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import sqrt

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import (
    endpoint_spike_records,
    parse_m_values,
)


def collect_records(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> list[dict]:
    """收集全部端点尖峰原子记录。"""
    records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            records.extend(
                endpoint_spike_records(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    alpha,
                    num_primes,
                    local_c,
                    endpoint_theta,
                )
            )
    return records


def indicator_test_stats(phase_count: int, phase_space: int, mass: float) -> dict:
    """计算观测相位指示函数的零均值测试统计。"""
    if phase_count <= 0 or phase_space <= phase_count:
        return {
            "kappa": 0.0,
            "norm_l2": 0.0,
            "weighted_l_pdec": 0.0,
        }
    density = phase_count / phase_space
    kappa = 1.0 - density
    norm_l2 = sqrt(phase_count * (1.0 - density) ** 2 + (phase_space - phase_count) * density**2)
    weighted_l_pdec = kappa * mass / (sqrt(phase_space - 1.0) * norm_l2) if norm_l2 else 0.0
    return {
        "kappa": kappa,
        "norm_l2": norm_l2,
        "weighted_l_pdec": weighted_l_pdec,
    }


def phase_test_rows(
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
    """为持久端点键构造有限相位测试函数。"""
    if phase_modulus <= 1:
        raise ValueError("phase-modulus 必须大于 1")
    records = collect_records(selected, m_values, alpha, num_primes, local_c, endpoint_theta)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[record["key"]].append(record)

    rows = []
    phase_space = phase_modulus * phase_modulus
    for key, key_records in grouped.items():
        support_windows = {record["window_id"] for record in key_records}
        total_excess = sum(record["excess"] for record in key_records)
        if len(support_windows) < persistent_count and total_excess < persistent_excess:
            continue
        phases = [
            (record["d_lower"] % phase_modulus, record["d_upper"] % phase_modulus)
            for record in key_records
        ]
        phase_set = set(phases)
        phase_loads: dict[tuple[int, int], int] = defaultdict(int)
        for phase in phases:
            phase_loads[phase] += 1
        stats = indicator_test_stats(len(phase_set), phase_space, total_excess)
        rows.append(
            {
                "key": key,
                "support_count": len(support_windows),
                "occurrences": len(key_records),
                "total_excess": total_excess,
                "phase_modulus": phase_modulus,
                "phase_space": phase_space,
                "phase_count": len(phase_set),
                "phase_density": len(phase_set) / phase_space,
                "max_phase_load": max(phase_loads.values(), default=0),
                "kappa": stats["kappa"],
                "norm_l2": stats["norm_l2"],
                "weighted_l_pdec": stats["weighted_l_pdec"],
                "sample_phases": sorted(phase_set)[:8],
                "status": "EXPLICIT_F_K_READY_U_CRT_OPEN",
            }
        )
    rows.sort(key=lambda item: (-item["weighted_l_pdec"], -item["total_excess"], item["key"]))
    return rows


def print_table(rows: list[dict]) -> None:
    """输出相位测试函数表。"""
    print(
        "key support occurrences excess Q phase_count phase_density kappa "
        "norm_l2 weighted_L_PDEC max_phase_load status",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['key']} {row['support_count']} {row['occurrences']} "
            f"{row['total_excess']:.6f} {row['phase_modulus']} {row['phase_count']} "
            f"{row['phase_density']:.8f} {row['kappa']:.8f} {row['norm_l2']:.6f} "
            f"{row['weighted_l_pdec']:.8f} {row['max_phase_load']} {row['status']}",
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

    rows = phase_test_rows(
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
