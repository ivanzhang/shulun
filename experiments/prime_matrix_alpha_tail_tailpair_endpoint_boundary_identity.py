#!/usr/bin/env python3
"""AlphaTail 右边界钉扎的几何恒等式审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_boundary_identity.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --target-residue 4 --target-modulus 210 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit import axis_lock_rows
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def right_boundary_owner(block: int, shift: int, point_count: int) -> list[int]:
    """返回造成 domain_stop 的点位下标。"""
    stops = [2 * block - index * shift for index in range(point_count)]
    minimum = min(stops)
    return [index for index, value in enumerate(stops) if value == minimum]


def boundary_identity_rows(
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
    """审计精确列目标是否由右边界几何恒等式强制。"""
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
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            owners = right_boundary_owner(block, shift, point_count)
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
                key = f"g{spike['gap']}:j{spike['j1']}-{spike['j2']}:u{spike['u']}:B"
                if key not in axis_keys:
                    continue
                if spike["d_upper"] % target_modulus != target_residue % target_modulus:
                    continue
                divisor = spike["u"]
                forced_by_divisibility = (domain_stop + spike["j1"] * shift) % divisor == 0
                rows.append(
                    {
                        "key": key,
                        "window_id": f"{prime_bound}:{block}:{shift}:m{point_count}",
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "m": point_count,
                        "domain_start": domain_start,
                        "domain_stop": domain_stop,
                        "right_boundary_owners": owners,
                        "gap": spike["gap"],
                        "j1": spike["j1"],
                        "j2": spike["j2"],
                        "u": spike["u"],
                        "q_upper": spike["q_upper"],
                        "d_lower": spike["d_lower"],
                        "d_upper": spike["d_upper"],
                        "right_slack": domain_stop - spike["d_upper"],
                        "target_hit": spike["d_upper"] % target_modulus == target_residue % target_modulus,
                        "forced_by_u1": spike["u"] == 1,
                        "forced_by_divisibility": forced_by_divisibility,
                        "excess": max(0.0, spike["excess"]),
                        "required_c": spike["required_c"],
                    }
                )
    total_excess = sum(row["excess"] for row in rows)
    forced_u1_excess = sum(row["excess"] for row in rows if row["forced_by_u1"])
    forced_div_excess = sum(row["excess"] for row in rows if row["forced_by_divisibility"])
    return {
        "target": f"{target_residue} mod {target_modulus}",
        "record_count": len(rows),
        "key_count": len({row["key"] for row in rows}),
        "window_count": len({row["window_id"] for row in rows}),
        "total_excess": total_excess,
        "forced_u1_count": sum(1 for row in rows if row["forced_by_u1"]),
        "forced_u1_excess": forced_u1_excess,
        "forced_divisibility_count": sum(1 for row in rows if row["forced_by_divisibility"]),
        "forced_divisibility_excess": forced_div_excess,
        "all_right_boundary": all(row["right_slack"] == 0 for row in rows),
        "all_forced_by_u1": len(rows) > 0 and all(row["forced_by_u1"] for row in rows),
        "all_forced_by_divisibility": len(rows) > 0 and all(row["forced_by_divisibility"] for row in rows),
        "rows": rows,
        "route": "UNIT_MULTIPLIER_RIGHT_ENDPOINT_TRUNCATION"
        if rows and all(row["forced_by_u1"] and row["right_slack"] == 0 for row in rows)
        else "BOUNDARY_PINNED_ENDPOINT_DEFECT",
    }


def print_table(package: dict) -> None:
    """输出右边界恒等式审计表。"""
    print(
        f"target {package['target']} route {package['route']} "
        f"records {package['record_count']} keys {package['key_count']} "
        f"windows {package['window_count']} excess {package['total_excess']:.6f} "
        f"all_right_boundary {package['all_right_boundary']} "
        f"all_forced_by_u1 {package['all_forced_by_u1']} "
        f"all_forced_by_divisibility {package['all_forced_by_divisibility']}",
        flush=True,
    )
    print("key window j1 j2 u q_upper d_interval R right_slack forced_u1 forced_div excess", flush=True)
    for row in package["rows"]:
        print(
            f"{row['key']} {row['window_id']} {row['j1']} {row['j2']} {row['u']} "
            f"{row['q_upper']} [{row['d_lower']},{row['d_upper']}] {row['domain_stop']} "
            f"{row['right_slack']} {row['forced_by_u1']} {row['forced_by_divisibility']} "
            f"{row['excess']:.6f}",
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

    package = boundary_identity_rows(
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
