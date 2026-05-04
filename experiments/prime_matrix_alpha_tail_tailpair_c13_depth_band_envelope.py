#!/usr/bin/env python3
"""AlphaTail C13 变模深度槽的端点带宽 envelope 审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit import unique_physical_atoms
from prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget import (
    depth_slot_key,
    split_formal_moving_atoms,
)
from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def band_limit_for_atom(atom: dict, endpoint_band_theta: float) -> int:
    """返回该 m 层的端点带宽上限。"""
    domain_start, domain_stop = domain_bounds(atom["block"], atom["shift"], atom["m"])
    domain_length = max(1, domain_stop - domain_start + 1)
    return int(endpoint_band_theta * domain_length)


def atom_band_pass(atom: dict, endpoint_band_theta: float) -> bool:
    """判断原子端点深度是否落入指定端点带宽。"""
    return atom["endpoint_depth"] <= band_limit_for_atom(atom, endpoint_band_theta)


def band_key(atom: dict) -> tuple:
    """返回不含 h 与 m 的带宽 envelope 键。"""
    return (
        atom["p"],
        atom["block"],
        atom["shift"],
        atom["shape_key"],
        atom["endpoint_residue_mod_u"],
    )


def depth_band_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
    modulus_persistent_count: int,
    top: int,
) -> dict:
    """返回端点带宽 envelope 审计包。"""
    raw_atoms = witness_atoms(selected, m_values, alpha, num_primes, local_c, endpoint_theta, slack_cut)
    formal_atoms = unique_physical_atoms(raw_atoms)
    fixed_atoms, moving_atoms = split_formal_moving_atoms(formal_atoms, modulus_persistent_count)
    band_atoms = [atom for atom in moving_atoms if atom_band_pass(atom, endpoint_band_theta)]
    overflow_atoms = [atom for atom in moving_atoms if not atom_band_pass(atom, endpoint_band_theta)]

    groups: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in band_atoms:
        groups[band_key(atom)].append(atom)

    rows = []
    total_observed_slots = 0
    total_envelope_slots = 0
    for key, atoms in groups.items():
        shape_key = key[3]
        epsilon = key[4]
        step = shape_key[3]
        observed_slots = {depth_slot_key(atom) for atom in atoms}
        max_h = 0
        for atom in atoms:
            limit = band_limit_for_atom(atom, endpoint_band_theta)
            if limit >= epsilon:
                max_h = max(max_h, (limit - epsilon) // step)
        envelope_slots = max_h + 1
        total_observed_slots += len(observed_slots)
        total_envelope_slots += envelope_slots
        q_depths = [atom["q_depth"] for atom in atoms]
        endpoint_depths = [atom["endpoint_depth"] for atom in atoms]
        rows.append(
            {
                "band_key": key,
                "shape_key": shape_key,
                "epsilon": epsilon,
                "step": step,
                "atom_count": len(atoms),
                "observed_slots": len(observed_slots),
                "envelope_slots": envelope_slots,
                "envelope_slack": envelope_slots - len(observed_slots),
                "max_h_envelope": max_h,
                "min_q_depth": min(q_depths),
                "max_q_depth": max(q_depths),
                "min_endpoint_depth": min(endpoint_depths),
                "max_endpoint_depth": max(endpoint_depths),
            }
        )
    rows.sort(key=lambda item: (-item["observed_slots"], -item["atom_count"], item["band_key"]))

    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "endpoint_band_theta": endpoint_band_theta,
        "slack_cut": slack_cut,
        "modulus_persistent_count": modulus_persistent_count,
        "raw_atoms": len(raw_atoms),
        "formal_atoms": len(formal_atoms),
        "formal_fixed_atoms": len(fixed_atoms),
        "formal_moving_atoms": len(moving_atoms),
        "band_atoms": len(band_atoms),
        "overflow_atoms": len(overflow_atoms),
        "band_group_count": len(groups),
        "observed_slots": total_observed_slots,
        "envelope_slots": total_envelope_slots,
        "envelope_slack": total_envelope_slots - total_observed_slots,
        "max_observed_over_envelope": max(
            (row["observed_slots"] / row["envelope_slots"] for row in rows if row["envelope_slots"]),
            default=0.0,
        ),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出端点带宽 envelope 表。"""
    print(
        "raw formal fixed moving band overflow groups observed_slots envelope_slots "
        "envelope_slack max_obs_over_env local_C band_theta",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_fixed_atoms']} "
        f"{package['formal_moving_atoms']} {package['band_atoms']} {package['overflow_atoms']} "
        f"{package['band_group_count']} {package['observed_slots']} {package['envelope_slots']} "
        f"{package['envelope_slack']} {package['max_observed_over_envelope']:.6f} "
        f"{package['local_c']:.6f} {package['endpoint_band_theta']:.6f}",
        flush=True,
    )
    print("band shape eps step atoms observed envelope slack h_range q_depth endpoint_depth", flush=True)
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        print(
            f"band {shape} eps{row['epsilon']} u{row['step']} {row['atom_count']} "
            f"{row['observed_slots']} {row['envelope_slots']} {row['envelope_slack']} "
            f"[0,{row['max_h_envelope']}] [{row['min_q_depth']},{row['max_q_depth']}] "
            f"[{row['min_endpoint_depth']},{row['max_endpoint_depth']}]",
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
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--modulus-persistent-count", type=int, default=2)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = depth_band_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
        args.modulus_persistent_count,
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
