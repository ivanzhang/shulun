#!/usr/bin/env python3
"""AlphaTail C13 失败见证的相位/PDEC 输入账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected, tail_primes_for_item
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_c13_witness_barrier import endpoint_side, tail_pair_witnesses
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def excess_witnesses_for_side(witnesses: list[dict], side: str, failure_mass: int) -> list[dict]:
    """按端点方向选取规范超额见证。"""
    if failure_mass <= 0:
        return []
    if side == "left":
        return witnesses[:failure_mass]
    return list(reversed(witnesses[-failure_mass:]))


def witness_atoms(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
) -> list[dict]:
    """展开所有 C13 失败的规范尾素对见证原子。"""
    atoms = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            tail_set = set(tail_primes_for_item(prime_bound, block, shift, point_count, alpha, num_primes))
            for record in interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c):
                if record["u"] is None or record["d_lower"] is None or record["d_upper"] is None:
                    continue
                if record["gap"] % 2 == 1 or record["actual"] <= 0:
                    continue
                if record["integer_slack"] > slack_cut:
                    continue
                if record["u"] > endpoint_theta * domain_length:
                    continue
                failure_mass = max(0, record["actual"] - record["threshold"] + 1)
                if failure_mass <= 0:
                    continue

                witnesses = tail_pair_witnesses(tail_set, record["q_lower"], record["q_upper"], record["gap"])
                side = endpoint_side(record, domain_start, domain_stop)
                selected_witnesses = excess_witnesses_for_side(witnesses, side, failure_mass)
                for witness in selected_witnesses:
                    q_left = witness["q"]
                    q_right = witness["q_plus_g"]
                    d_value = q_left * record["u"] - record["j1"] * shift
                    left_value = d_value + record["j1"] * shift
                    right_value = d_value + record["j2"] * shift
                    left_divisible = left_value % q_left == 0
                    right_divisible = right_value % q_right == 0
                    left_quotient = left_value // q_left if left_divisible else None
                    right_quotient = right_value // q_right if right_divisible else None
                    quotient_lock = (
                        left_divisible
                        and right_divisible
                        and left_quotient == record["u"]
                        and right_quotient == record["u"]
                    )
                    endpoint_depth = (
                        d_value - domain_start if side == "left" else domain_stop - d_value
                    )
                    q_depth = (
                        q_left - record["q_lower"] if side == "left" else record["q_upper"] - q_left
                    )
                    modulus = q_left * q_right
                    atoms.append(
                        {
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
                            "q": q_left,
                            "q_plus_g": q_right,
                            "d": d_value,
                            "endpoint_depth": endpoint_depth,
                            "q_depth": q_depth,
                            "endpoint_residue_mod_u": endpoint_depth % record["u"],
                            "pair_modulus": modulus,
                            "pair_residue": d_value % modulus,
                            "left_quotient": left_quotient,
                            "right_quotient": right_quotient,
                            "quotient_lock": quotient_lock,
                            "shape_key": (
                                record["gap"],
                                record["j1"],
                                record["j2"],
                                record["u"],
                                side,
                            ),
                            "pair_key": (record["gap"], q_left, q_right),
                        }
                    )
    return atoms


def phase_ledger(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
    persistent_count: int,
    top: int,
) -> dict:
    """按形状键聚合 C13 失败见证相位。"""
    atoms = witness_atoms(selected, m_values, alpha, num_primes, local_c, endpoint_theta, slack_cut)
    grouped: dict[tuple[int, int, int, int, str], dict] = {}
    for atom in atoms:
        key = atom["shape_key"]
        if key not in grouped:
            grouped[key] = {
                "shape_key": key,
                "atom_count": 0,
                "support_windows": set(),
                "p_values": set(),
                "pair_keys": set(),
                "quotient_lock_failures": 0,
                "min_endpoint_depth": atom["endpoint_depth"],
                "max_endpoint_depth": atom["endpoint_depth"],
                "min_q_depth": atom["q_depth"],
                "max_q_depth": atom["q_depth"],
                "examples": [],
            }
        row = grouped[key]
        row["atom_count"] += 1
        row["support_windows"].add(atom["window_id"])
        row["p_values"].add(atom["p"])
        row["pair_keys"].add(atom["pair_key"])
        row["quotient_lock_failures"] += 0 if atom["quotient_lock"] else 1
        row["min_endpoint_depth"] = min(row["min_endpoint_depth"], atom["endpoint_depth"])
        row["max_endpoint_depth"] = max(row["max_endpoint_depth"], atom["endpoint_depth"])
        row["min_q_depth"] = min(row["min_q_depth"], atom["q_depth"])
        row["max_q_depth"] = max(row["max_q_depth"], atom["q_depth"])
        if len(row["examples"]) < 5:
            row["examples"].append(
                {
                    "window": atom["window_id"],
                    "q": atom["q"],
                    "q_plus_g": atom["q_plus_g"],
                    "d": atom["d"],
                    "pair_modulus": atom["pair_modulus"],
                    "pair_residue": atom["pair_residue"],
                    "endpoint_depth": atom["endpoint_depth"],
                    "q_depth": atom["q_depth"],
                }
            )

    rows = []
    for row in grouped.values():
        support_count = len(row["support_windows"])
        persistent = support_count >= persistent_count or row["atom_count"] >= persistent_count
        rows.append(
            {
                "shape_key": row["shape_key"],
                "atom_count": row["atom_count"],
                "support_count": support_count,
                "p_support_count": len(row["p_values"]),
                "distinct_pair_count": len(row["pair_keys"]),
                "quotient_lock_failures": row["quotient_lock_failures"],
                "min_endpoint_depth": row["min_endpoint_depth"],
                "max_endpoint_depth": row["max_endpoint_depth"],
                "min_q_depth": row["min_q_depth"],
                "max_q_depth": row["max_q_depth"],
                "route": "PairPhase-PDEC/ColumnCRT" if persistent else "SAEWitness",
                "examples": row["examples"],
            }
        )
    rows.sort(
        key=lambda item: (
            item["route"] == "SAEWitness",
            -item["atom_count"],
            -item["support_count"],
            item["shape_key"],
        )
    )
    route_counts = defaultdict(int)
    for row in rows:
        route_counts[row["route"]] += 1

    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "persistent_count": persistent_count,
        "atom_count": len(atoms),
        "shape_count": len(rows),
        "quotient_lock_failures": sum(1 for atom in atoms if not atom["quotient_lock"]),
        "route_counts": dict(sorted(route_counts.items())),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出 C13 见证相位账本。"""
    route_counts = ",".join(
        f"{route}:{count}" for route, count in package["route_counts"].items()
    ) or "none"
    print(
        "atoms shapes quotient_lock_failures route_counts local_C",
        flush=True,
    )
    print(
        f"{package['atom_count']} {package['shape_count']} {package['quotient_lock_failures']} "
        f"{route_counts} {package['local_c']:.6f}",
        flush=True,
    )
    print(
        "route shape atoms support p_support distinct_pairs endpoint_depth q_depth quotient_fail examples",
        flush=True,
    )
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        examples = ",".join(
            f"{item['q']}+{row['shape_key'][0]}={item['q_plus_g']}@d{item['d']}"
            for item in row["examples"][:3]
        )
        print(
            f"{row['route']} {shape} {row['atom_count']} {row['support_count']} "
            f"{row['p_support_count']} {row['distinct_pair_count']} "
            f"[{row['min_endpoint_depth']},{row['max_endpoint_depth']}] "
            f"[{row['min_q_depth']},{row['max_q_depth']}] "
            f"{row['quotient_lock_failures']} {examples or 'none'}",
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
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = phase_ledger(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.slack_cut,
        args.persistent_count,
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
