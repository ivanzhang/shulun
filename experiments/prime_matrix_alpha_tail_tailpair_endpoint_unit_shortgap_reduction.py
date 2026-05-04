#!/usr/bin/env python3
"""AlphaTail 单位截断到固定差值短区间素对常数的归约审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_shortgap_reduction.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_endpoint_unit_truncation_ledger import boundary_kind
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def unit_shortgap_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> dict:
    """把 u=1 全窗口截断项按固定 gap 短区间常数聚合。"""
    records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            for spike in spike_rows(
                prime_bound,
                block,
                shift,
                point_count,
                alpha,
                num_primes,
                local_c,
                endpoint_theta,
            ):
                if spike["route"] != "EndpointSpike" or spike["u"] != 1:
                    continue
                if boundary_kind(spike, domain_start, domain_stop) is None:
                    continue
                if spike["d_lower"] != domain_start or spike["d_upper"] != domain_stop:
                    continue
                records.append(
                    {
                        "window_id": f"{prime_bound}:{block}:{shift}:m{point_count}",
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "m": point_count,
                        "gap": spike["gap"],
                        "j1": spike["j1"],
                        "j2": spike["j2"],
                        "q_lower": spike["q_lower"],
                        "q_upper": spike["q_upper"],
                        "q_length": spike["q_length"],
                        "actual": spike["actual"],
                        "scale": spike["scale"],
                        "required_c": spike["required_c"],
                        "excess": max(0.0, spike["excess"]),
                    }
                )

    grouped: dict[int, dict] = {}
    for record in records:
        gap = record["gap"]
        if gap not in grouped:
            grouped[gap] = {
                "gap": gap,
                "record_count": 0,
                "window_ids": set(),
                "total_actual": 0,
                "total_scale": 0.0,
                "total_excess": 0.0,
                "max_required_c": 0.0,
                "max_record": None,
            }
        row = grouped[gap]
        row["record_count"] += 1
        row["window_ids"].add(record["window_id"])
        row["total_actual"] += record["actual"]
        row["total_scale"] += record["scale"]
        row["total_excess"] += record["excess"]
        if record["required_c"] > row["max_required_c"]:
            row["max_required_c"] = record["required_c"]
            row["max_record"] = record

    gap_rows = []
    for row in grouped.values():
        gap_rows.append(
            {
                "gap": row["gap"],
                "record_count": row["record_count"],
                "support_count": len(row["window_ids"]),
                "total_actual": row["total_actual"],
                "total_scale": row["total_scale"],
                "aggregate_required_c": row["total_actual"] / row["total_scale"] if row["total_scale"] else 0.0,
                "total_excess": row["total_excess"],
                "max_required_c": row["max_required_c"],
                "max_record": row["max_record"],
                "route": "FixedGapShortIntervalConstant",
            }
        )
    gap_rows.sort(key=lambda item: (-item["max_required_c"], -item["total_excess"], item["gap"]))
    return {
        "record_count": len(records),
        "gap_count": len(gap_rows),
        "total_excess": sum(record["excess"] for record in records),
        "max_required_c": max((row["max_required_c"] for row in gap_rows), default=0.0),
        "gap_rows": gap_rows,
    }


def print_table(package: dict) -> None:
    """输出单位截断固定 gap 常数表。"""
    print(
        f"records {package['record_count']} gaps {package['gap_count']} "
        f"excess {package['total_excess']:.6f} max_required_C {package['max_required_c']:.6f}",
        flush=True,
    )
    print("gap records support actual scale aggregate_C max_C max_window max_interval route", flush=True)
    for row in package["gap_rows"]:
        max_record = row["max_record"] or {}
        max_interval = f"[{max_record.get('q_lower')},{max_record.get('q_upper')}]"
        print(
            f"{row['gap']} {row['record_count']} {row['support_count']} "
            f"{row['total_actual']} {row['total_scale']:.6f} "
            f"{row['aggregate_required_c']:.6f} {row['max_required_c']:.6f} "
            f"{max_record.get('window_id')} {max_interval} {row['route']}",
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
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = unit_shortgap_rows(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
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
