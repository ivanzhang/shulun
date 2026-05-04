#!/usr/bin/env python3
"""AlphaTail 端点 PDEC 的镜像闭合约束审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_mirror_constraint_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --phase-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_endpoint_crtdefect_audit import endpoint_side
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def endpoint_records_with_mirror(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    phase_modulus: int,
) -> list[dict]:
    """收集带镜像相位的端点尖峰记录。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    mirror_sum = domain_start + domain_stop
    records = []
    for spike in spike_rows(prime_bound, block, shift, point_count, alpha, num_primes, local_c, endpoint_theta):
        if spike["route"] != "EndpointSpike":
            continue
        side = endpoint_side(spike, domain_start, domain_stop, endpoint_theta)
        key = f"g{spike['gap']}:j{spike['j1']}-{spike['j2']}:u{spike['u']}:{side}"
        phase = (spike["d_lower"] % phase_modulus, spike["d_upper"] % phase_modulus)
        mirror_phase = (
            (mirror_sum - spike["d_upper"]) % phase_modulus,
            (mirror_sum - spike["d_lower"]) % phase_modulus,
        )
        records.append(
            {
                "key": key,
                "window_id": f"{prime_bound}:{block}:{shift}:m{point_count}",
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "m": point_count,
                "phase": phase,
                "mirror_phase": mirror_phase,
                "self_mirror": phase == mirror_phase,
                "excess": max(0.0, spike["excess"]),
                "required_c": spike["required_c"],
            }
        )
    return records


def mirror_constraint_rows(
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
    """检查持久键的端点相位集合是否按同窗口镜像闭合。"""
    if phase_modulus <= 1:
        raise ValueError("phase-modulus 必须大于 1")
    all_records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            all_records.extend(
                endpoint_records_with_mirror(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    alpha,
                    num_primes,
                    local_c,
                    endpoint_theta,
                    phase_modulus,
                )
            )

    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in all_records:
        grouped[record["key"]].append(record)

    rows = []
    for key, records in grouped.items():
        support_windows = {record["window_id"] for record in records}
        total_excess = sum(record["excess"] for record in records)
        if len(support_windows) < persistent_count and total_excess < persistent_excess:
            continue
        window_phases: dict[str, set[tuple[int, int]]] = defaultdict(set)
        for record in records:
            window_phases[record["window_id"]].add(tuple(record["phase"]))

        missing = []
        self_mirror_count = 0
        for record in records:
            if record["self_mirror"]:
                self_mirror_count += 1
            if tuple(record["mirror_phase"]) not in window_phases[record["window_id"]]:
                missing.append(record)
        rows.append(
            {
                "key": key,
                "support_count": len(support_windows),
                "occurrences": len(records),
                "total_excess": total_excess,
                "phase_modulus": phase_modulus,
                "self_mirror_count": self_mirror_count,
                "missing_mirror_count": len(missing),
                "mirror_closed": not missing,
                "missing_excess": sum(record["excess"] for record in missing),
                "sample_missing": [
                    {
                        "window_id": record["window_id"],
                        "phase": record["phase"],
                        "mirror_phase": record["mirror_phase"],
                        "excess": record["excess"],
                    }
                    for record in missing[:5]
                ],
                "route": "MIRROR_CONSTRAINT_ADMISSIBLE"
                if not missing
                else "MIRROR_IMBALANCE_DEFECT/PDEC_OR_SAE",
            }
        )
    rows.sort(key=lambda item: (-item["missing_excess"], -item["total_excess"], item["key"]))
    return rows


def print_table(rows: list[dict]) -> None:
    """输出镜像约束表。"""
    print(
        "key support occurrences excess Q self_mirror missing_mirror "
        "missing_excess mirror_closed route",
        flush=True,
    )
    for row in rows:
        print(
            f"{row['key']} {row['support_count']} {row['occurrences']} "
            f"{row['total_excess']:.6f} {row['phase_modulus']} "
            f"{row['self_mirror_count']} {row['missing_mirror_count']} "
            f"{row['missing_excess']:.6f} {row['mirror_closed']} {row['route']}",
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

    rows = mirror_constraint_rows(
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
