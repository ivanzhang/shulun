#!/usr/bin/env python3
"""AlphaTail 单位乘数端点截断 SAE/PDEC 账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_truncation_ledger.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def boundary_kind(spike: dict, domain_start: int, domain_stop: int) -> str | None:
    """判断单位乘数尖峰贴住哪一侧精确边界。"""
    left = spike["d_lower"] == domain_start
    right = spike["d_upper"] == domain_stop
    if left and right:
        return "both"
    if left:
        return "left"
    if right:
        return "right"
    return None


def unit_truncation_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    phase_modulus: int,
    persistent_count: int,
    persistent_excess: float,
) -> dict:
    """聚合 u=1 且精确贴边的端点尖峰。"""
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
                side = boundary_kind(spike, domain_start, domain_stop)
                if side is None:
                    continue
                phase_value = (domain_stop if side == "right" else domain_start) % phase_modulus
                key = f"{side}:g{spike['gap']}:j{spike['j1']}-{spike['j2']}:phase{phase_value}"
                records.append(
                    {
                        "key": key,
                        "side": side,
                        "phase_value": phase_value,
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
                        "d_lower": spike["d_lower"],
                        "d_upper": spike["d_upper"],
                        "domain_start": domain_start,
                        "domain_stop": domain_stop,
                        "excess": max(0.0, spike["excess"]),
                        "required_c": spike["required_c"],
                    }
                )
    grouped: dict[str, dict] = {}
    for record in records:
        if record["key"] not in grouped:
            grouped[record["key"]] = {
                "key": record["key"],
                "side": record["side"],
                "phase_value": record["phase_value"],
                "occurrences": 0,
                "support_windows": set(),
                "p_values": set(),
                "total_excess": 0.0,
                "max_required_c": 0.0,
                "sample_records": [],
            }
        row = grouped[record["key"]]
        row["occurrences"] += 1
        row["support_windows"].add(record["window_id"])
        row["p_values"].add(record["p"])
        row["total_excess"] += record["excess"]
        row["max_required_c"] = max(row["max_required_c"], record["required_c"])
        row["sample_records"].append(record)

    key_rows = []
    for row in grouped.values():
        support_count = len(row["support_windows"])
        persistent = support_count >= persistent_count or row["total_excess"] >= persistent_excess
        key_rows.append(
            {
                "key": row["key"],
                "side": row["side"],
                "phase_value": row["phase_value"],
                "occurrences": row["occurrences"],
                "support_count": support_count,
                "p_support_count": len(row["p_values"]),
                "total_excess": row["total_excess"],
                "max_required_c": row["max_required_c"],
                "route": "UnitEndpointTruncation/PDEC" if persistent else "UnitEndpointTruncation/SAE",
                "windows": sorted(row["support_windows"]),
                "sample_records": row["sample_records"][:5],
            }
        )
    key_rows.sort(key=lambda item: (-item["total_excess"], item["key"]))
    route_summary: dict[str, dict] = {}
    for row in key_rows:
        route_summary.setdefault(row["route"], {"count": 0, "total_excess": 0.0})
        route_summary[row["route"]]["count"] += 1
        route_summary[row["route"]]["total_excess"] += row["total_excess"]
    return {
        "record_count": len(records),
        "key_count": len(key_rows),
        "total_excess": sum(record["excess"] for record in records),
        "route_summary": dict(sorted(route_summary.items())),
        "key_rows": key_rows,
    }


def print_table(package: dict) -> None:
    """输出单位乘数端点截断账本。"""
    print(
        f"records {package['record_count']} keys {package['key_count']} "
        f"excess {package['total_excess']:.6f} "
        f"summary {json.dumps(package['route_summary'], ensure_ascii=False, sort_keys=True)}",
        flush=True,
    )
    print("key side phase occurrences support p_support excess max_req_C route windows", flush=True)
    for row in package["key_rows"]:
        print(
            f"{row['key']} {row['side']} {row['phase_value']} {row['occurrences']} "
            f"{row['support_count']} {row['p_support_count']} {row['total_excess']:.6f} "
            f"{row['max_required_c']:.6f} {row['route']} {','.join(row['windows'])}",
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
    parser.add_argument("--phase-modulus", type=int, default=210)
    parser.add_argument("--persistent-count", type=int, default=2)
    parser.add_argument("--persistent-excess", type=float, default=20.0)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = unit_truncation_rows(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.phase_modulus,
        args.persistent_count,
        args.persistent_excess,
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
