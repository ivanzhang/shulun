#!/usr/bin/env python3
"""AlphaTail 端点 PDEC 的责任频率路由审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_frequency_route_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_endpoint_fourier_target_audit import fourier_target_rows
from prime_matrix_alpha_tail_tailpair_endpoint_mirror_constraint_audit import mirror_constraint_rows
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def classify_frequency(freq_x: int, freq_y: int) -> str:
    """按二维端点频率的支撑坐标分类。"""
    if freq_x == 0 and freq_y == 0:
        return "ZeroFrequencyInvalid"
    if freq_x == 0:
        return "RightEndpointAxis"
    if freq_y == 0:
        return "LeftEndpointAxis"
    if freq_x == freq_y:
        return "DiagonalEndpoint"
    return "TwoEndpointMixed"


def route_for_row(frequency_class: str, mirror_route: str) -> str:
    """根据镜像状态与频率类别给出出口。"""
    if mirror_route != "MIRROR_CONSTRAINT_ADMISSIBLE":
        return "MirrorImbalanceDefect/PDEC_OR_SAE"
    if frequency_class in {"LeftEndpointAxis", "RightEndpointAxis"}:
        return "OneSidedEndpointCRTDefect/ColumnCRT"
    if frequency_class == "DiagonalEndpoint":
        return "DiagonalEndpointCRTDefect/PDEC"
    if frequency_class == "TwoEndpointMixed":
        return "TwoEndpointCRTDefect/TailRankinPDEC"
    return "InvalidFrequency"


def frequency_route_rows(
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
    """合并 Fourier 目标频率与镜像闭合状态，输出路由表。"""
    fourier_rows = fourier_target_rows(
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
    mirror_rows = {
        row["key"]: row
        for row in mirror_constraint_rows(
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
    }
    rows = []
    for row in fourier_rows:
        freq_x, freq_y = row["best_frequency"]
        frequency_class = classify_frequency(freq_x, freq_y)
        mirror_row = mirror_rows.get(row["key"], {})
        mirror_route = mirror_row.get("route", "MIRROR_STATUS_MISSING")
        route = route_for_row(frequency_class, mirror_route)
        rows.append(
            {
                "key": row["key"],
                "support_count": row["support_count"],
                "total_excess": row["total_excess"],
                "phase_modulus": phase_modulus,
                "best_frequency": row["best_frequency"],
                "frequency_class": frequency_class,
                "mirror_route": mirror_route,
                "missing_mirror_count": mirror_row.get("missing_mirror_count"),
                "l_pdec": row["weighted_l_pdec_orthonormal"],
                "max_orth": row["max_fourier_orthonormal"],
                "route": route,
            }
        )
    rows.sort(key=lambda item: (item["route"], -item["total_excess"], item["key"]))
    return rows


def route_summary(rows: list[dict]) -> dict:
    """汇总路由数量与质量。"""
    summary: dict[str, dict] = {}
    for row in rows:
        route = row["route"]
        if route not in summary:
            summary[route] = {"count": 0, "total_excess": 0.0}
        summary[route]["count"] += 1
        summary[route]["total_excess"] += row["total_excess"]
    return dict(sorted(summary.items()))


def print_table(rows: list[dict]) -> None:
    """输出责任频率路由表。"""
    print("summary", json.dumps(route_summary(rows), ensure_ascii=False, sort_keys=True), flush=True)
    print(
        "key excess Q best_freq freq_class mirror_route missing_mirror "
        "L_PDEC max_orth route",
        flush=True,
    )
    for row in rows:
        freq_x, freq_y = row["best_frequency"]
        print(
            f"{row['key']} {row['total_excess']:.6f} {row['phase_modulus']} "
            f"({freq_x},{freq_y}) {row['frequency_class']} {row['mirror_route']} "
            f"{row['missing_mirror_count']} {row['l_pdec']:.8f} "
            f"{row['max_orth']:.8f} {row['route']}",
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

    rows = frequency_route_rows(
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
        print(json.dumps({"summary": route_summary(rows), "rows": rows}, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
