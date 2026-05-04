#!/usr/bin/env python3
"""AlphaTail 端点持久键的 Fourier 目标频率审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_fourier_target_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import cos, pi, sin, sqrt

from prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit import (
    collect_records,
    indicator_test_stats,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def max_fourier_coefficient(phase_weights: dict[tuple[int, int], float], modulus: int) -> dict:
    """计算二维有限群上非零频率的最大 Fourier 系数。"""
    max_abs = 0.0
    best_frequency = (0, 0)
    for freq_x in range(modulus):
        for freq_y in range(modulus):
            if freq_x == 0 and freq_y == 0:
                continue
            real = 0.0
            imag = 0.0
            for (phase_x, phase_y), weight in phase_weights.items():
                angle = -2.0 * pi * ((freq_x * phase_x + freq_y * phase_y) % modulus) / modulus
                real += weight * cos(angle)
                imag += weight * sin(angle)
            magnitude = sqrt(real * real + imag * imag)
            if magnitude > max_abs:
                max_abs = magnitude
                best_frequency = (freq_x, freq_y)
    return {
        "max_fourier_unnormalized": max_abs,
        "best_frequency": best_frequency,
    }


def fourier_target_rows(
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
    """输出每个持久键的 Fourier 目标频率与归一化检查。"""
    if phase_modulus <= 1:
        raise ValueError("phase-modulus 必须大于 1")
    records = collect_records(selected, m_values, alpha, num_primes, local_c, endpoint_theta)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[record["key"]].append(record)

    rows = []
    phase_space = phase_modulus * phase_modulus
    sqrt_phase_space = sqrt(phase_space)
    for key, key_records in grouped.items():
        support_windows = {record["window_id"] for record in key_records}
        total_excess = sum(record["excess"] for record in key_records)
        if len(support_windows) < persistent_count and total_excess < persistent_excess:
            continue
        phase_weights: dict[tuple[int, int], float] = defaultdict(float)
        for record in key_records:
            phase = (record["d_lower"] % phase_modulus, record["d_upper"] % phase_modulus)
            phase_weights[phase] += record["excess"]
        stats = indicator_test_stats(len(phase_weights), phase_space, total_excess)
        fourier = max_fourier_coefficient(phase_weights, phase_modulus)
        max_unnormalized = fourier["max_fourier_unnormalized"]
        max_orthonormal = max_unnormalized / sqrt_phase_space
        lower = stats["weighted_l_pdec"]
        rows.append(
            {
                "key": key,
                "support_count": len(support_windows),
                "occurrences": len(key_records),
                "total_excess": total_excess,
                "phase_modulus": phase_modulus,
                "phase_count": len(phase_weights),
                "weighted_l_pdec_orthonormal": lower,
                "max_fourier_orthonormal": max_orthonormal,
                "max_fourier_unnormalized": max_unnormalized,
                "best_frequency": fourier["best_frequency"],
                "actual_over_lower": max_orthonormal / lower if lower else None,
                "normalization_pass": max_orthonormal + 1e-12 >= lower,
                "status": "TARGET_FREQUENCY_FOUND_U_CRT_BOUND_OPEN",
            }
        )
    rows.sort(key=lambda item: (-item["max_fourier_orthonormal"], -item["total_excess"], item["key"]))
    return rows


def print_table(rows: list[dict]) -> None:
    """输出 Fourier 目标表。"""
    print(
        "key support occurrences excess Q phase_count L_orth max_orth "
        "max_un best_freq ratio normalization_pass status",
        flush=True,
    )
    for row in rows:
        freq_x, freq_y = row["best_frequency"]
        print(
            f"{row['key']} {row['support_count']} {row['occurrences']} "
            f"{row['total_excess']:.6f} {row['phase_modulus']} {row['phase_count']} "
            f"{row['weighted_l_pdec_orthonormal']:.8f} "
            f"{row['max_fourier_orthonormal']:.8f} "
            f"{row['max_fourier_unnormalized']:.8f} "
            f"({freq_x},{freq_y}) {row['actual_over_lower']:.6f} "
            f"{row['normalization_pass']} {row['status']}",
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

    rows = fourier_target_rows(
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
