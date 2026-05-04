#!/usr/bin/env python3
"""AlphaTail 端点 PDEC 的 Parseval 能量地板审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_energy_floor_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from math import sqrt

from prime_matrix_alpha_tail_tailpair_endpoint_fourier_target_audit import fourier_target_rows
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def energy_floor_rows(
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
    """计算仅由质量和相位支撑推出的非零 Fourier 能量地板。"""
    target_rows = fourier_target_rows(
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
    phase_space = phase_modulus * phase_modulus
    rows = []
    for row in target_rows:
        support_size = row["phase_count"]
        mass = row["total_excess"]
        # 在固定支撑大小和总质量下，sum g(t)^2 的最小值是 M^2/support_size。
        min_l2_square = mass * mass / support_size
        nonzero_energy_floor = min_l2_square - mass * mass / phase_space
        rms_floor = sqrt(nonzero_energy_floor / (phase_space - 1.0))
        lower = row["weighted_l_pdec_orthonormal"]
        rows.append(
            {
                "key": row["key"],
                "mass": mass,
                "phase_modulus": phase_modulus,
                "phase_space": phase_space,
                "support_size": support_size,
                "l_pdec": lower,
                "parseval_rms_floor": rms_floor,
                "floor_over_l": rms_floor / lower if lower else None,
                "actual_max_orth": row["max_fourier_orthonormal"],
                "actual_over_floor": row["max_fourier_orthonormal"] / rms_floor if rms_floor else None,
                "conclusion": "NO_SUPPORT_ONLY_UPPER_CAN_BE_STRICT_BELOW_L",
            }
        )
    rows.sort(key=lambda item: (-item["actual_max_orth"], item["key"]))
    return rows


def print_table(rows: list[dict]) -> None:
    """输出能量地板表。"""
    print(
        "key mass Q support L_PDEC parseval_rms_floor floor_over_L "
        "actual_max actual_over_floor conclusion",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['key']} {row['mass']:.6f} {row['phase_modulus']} "
            f"{row['support_size']} {row['l_pdec']:.8f} "
            f"{row['parseval_rms_floor']:.8f} {row['floor_over_l']:.8f} "
            f"{row['actual_max_orth']:.8f} {row['actual_over_floor']:.6f} "
            f"{row['conclusion']}",
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

    rows = energy_floor_rows(
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
