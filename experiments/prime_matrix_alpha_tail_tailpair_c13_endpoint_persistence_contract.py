#!/usr/bin/env python3
"""AlphaTail C13 端点失败键的持久性/SAE/PDEC 合同。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_persistence_contract.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def endpoint_atom_records(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
) -> list[dict]:
    """抽取 C13 端点原子；真实失败与近门槛观察项分开登记。"""
    atoms = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None or record["d_lower"] is None or record["d_upper"] is None:
                    continue
                if record["gap"] % 2 == 1 or record["actual"] <= 0:
                    continue
                if record["integer_slack"] > slack_cut:
                    continue
                if record["u"] > endpoint_theta * domain_length:
                    continue

                left_distance = record["d_lower"] - domain_start
                right_distance = domain_stop - record["d_upper"]
                side = "left" if left_distance <= right_distance else "right"
                key = f"g{record['gap']}:j{record['j1']}-{record['j2']}:u{record['u']}:{side}"
                failure = record["integer_slack"] <= 0
                # 若 slack=0，则 actual=threshold，已经跨过 floor(CB)+1 的整数门槛，
                # 贡献一个整数失败质量；slack<0 时按超额逐一累计。
                failure_mass = max(0, 1 - record["integer_slack"])
                atoms.append(
                    {
                        "key": key,
                        "window_id": f"{prime_bound}:{block}:{shift}:m{point_count}",
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "m": point_count,
                        "gap": record["gap"],
                        "j1": record["j1"],
                        "j2": record["j2"],
                        "u": record["u"],
                        "side": side,
                        "q_lower": record["q_lower"],
                        "q_upper": record["q_upper"],
                        "actual": record["actual"],
                        "threshold": record["threshold"],
                        "integer_slack": record["integer_slack"],
                        "required_c": record["required_c"] or 0.0,
                        "failure": failure,
                        "failure_mass": failure_mass,
                    }
                )
    return atoms


def grouped_contract(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
    persistent_count: int,
    persistent_mass: int,
    top: int,
) -> dict:
    """按相位键给出真实失败出口与近门槛观察出口。"""
    atoms = endpoint_atom_records(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        slack_cut,
    )
    grouped: dict[str, dict] = {}
    for atom in atoms:
        key = atom["key"]
        if key not in grouped:
            grouped[key] = {
                "key": key,
                "record_count": 0,
                "support_windows": set(),
                "p_values": set(),
                "failure_records": 0,
                "failure_mass": 0,
                "min_slack": atom["integer_slack"],
                "max_required_c": atom["required_c"],
                "side": atom["side"],
                "examples": [],
            }
        row = grouped[key]
        row["record_count"] += 1
        row["support_windows"].add(atom["window_id"])
        row["p_values"].add(atom["p"])
        row["failure_records"] += 1 if atom["failure"] else 0
        row["failure_mass"] += atom["failure_mass"]
        row["min_slack"] = min(row["min_slack"], atom["integer_slack"])
        row["max_required_c"] = max(row["max_required_c"], atom["required_c"])
        if len(row["examples"]) < 5:
            row["examples"].append(
                {
                    "window": atom["window_id"],
                    "q": [atom["q_lower"], atom["q_upper"]],
                    "actual": atom["actual"],
                    "threshold": atom["threshold"],
                    "slack": atom["integer_slack"],
                }
            )

    rows = []
    for row in grouped.values():
        support_count = len(row["support_windows"])
        p_support_count = len(row["p_values"])
        has_failure = row["failure_mass"] > 0
        persistent = has_failure and (
            support_count >= persistent_count or row["failure_mass"] >= persistent_mass
        )
        if persistent:
            route = "DirectedEndpointCRTDefect/PDEC"
        elif has_failure:
            route = "SAE"
        else:
            route = "NearThresholdWatchOnly"
        rows.append(
            {
                "key": row["key"],
                "record_count": row["record_count"],
                "support_count": support_count,
                "p_support_count": p_support_count,
                "failure_records": row["failure_records"],
                "failure_mass": row["failure_mass"],
                "min_slack": row["min_slack"],
                "max_required_c": row["max_required_c"],
                "side": row["side"],
                "route": route,
                "examples": row["examples"],
            }
        )
    rows.sort(
        key=lambda item: (
            item["route"] == "NearThresholdWatchOnly",
            -item["failure_mass"],
            item["min_slack"],
            -item["max_required_c"],
            -item["record_count"],
            item["key"],
        )
    )

    route_counts = defaultdict(int)
    side_counts = defaultdict(int)
    for row in rows:
        route_counts[row["route"]] += 1
        side_counts[row["side"]] += row["record_count"]

    failure_rows = [row for row in rows if row["failure_mass"] > 0]
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "persistent_count": persistent_count,
        "persistent_mass": persistent_mass,
        "record_count": len(atoms),
        "key_count": len(rows),
        "failure_record_count": sum(row["failure_records"] for row in rows),
        "failure_key_count": len(failure_rows),
        "failure_mass": sum(row["failure_mass"] for row in rows),
        "route_counts": dict(sorted(route_counts.items())),
        "side_counts": dict(sorted(side_counts.items())),
        "min_slack": min((row["min_slack"] for row in rows), default=None),
        "max_required_c": max((row["max_required_c"] for row in rows), default=0.0),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出 C13 端点持久性合同简表。"""
    min_slack = "NA" if package["min_slack"] is None else str(package["min_slack"])
    route_counts = ",".join(
        f"{route}:{count}" for route, count in package["route_counts"].items()
    ) or "none"
    side_counts = ",".join(f"{side}:{count}" for side, count in package["side_counts"].items()) or "none"
    print(
        "records keys failure_records failure_keys failure_mass min_slack "
        "max_required_C route_counts side_counts",
        flush=True,
    )
    print(
        f"{package['record_count']} {package['key_count']} {package['failure_record_count']} "
        f"{package['failure_key_count']} {package['failure_mass']} {min_slack} "
        f"{package['max_required_c']:.6f} {route_counts} {side_counts}",
        flush=True,
    )
    print(
        "route key records support p_support failures failure_mass min_slack max_required_C",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['route']} {row['key']} {row['record_count']} {row['support_count']} "
            f"{row['p_support_count']} {row['failure_records']} {row['failure_mass']} "
            f"{row['min_slack']} {row['max_required_c']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--local-c", type=float, default=1.3)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--persistent-count", type=int, default=2)
    parser.add_argument("--persistent-mass", type=int, default=2)
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = grouped_contract(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.slack_cut,
        args.persistent_count,
        args.persistent_mass,
        args.top,
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
