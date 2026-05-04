#!/usr/bin/env python3
"""AlphaTail C13 SparseSAE 总 envelope 可求和账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_sparse_summability.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --eta 0.04 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_tailpair_c13_band_sparse_acceptance import sparse_acceptance_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def sparse_summability_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
    modulus_persistent_count: int,
    eta: float,
) -> dict:
    """返回 SparseSAE 总量付款账本。"""
    sparse = sparse_acceptance_package(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        endpoint_band_theta,
        slack_cut,
        modulus_persistent_count,
        eta,
        1_000_000,
    )
    layer_count_bound = max(1, len(m_values))
    accepted_capacity = layer_count_bound * eta * sparse["accepted_envelope_slots"]
    high_capacity = layer_count_bound * sparse["high_density_envelope_slots"]
    total_capacity = accepted_capacity + high_capacity
    by_window: defaultdict[tuple[int, int, int], dict] = defaultdict(
        lambda: {
            "accepted_groups": 0,
            "high_groups": 0,
            "accepted_slots": 0,
            "high_slots": 0,
            "accepted_envelope": 0,
            "high_envelope": 0,
        }
    )
    for row in sparse["rows"]:
        key = (row["band_key"][0], row["band_key"][1], row["band_key"][2])
        target = by_window[key]
        if row["route"] == "SparseSAE":
            target["accepted_groups"] += 1
            target["accepted_slots"] += row["observed_slots"]
            target["accepted_envelope"] += row["envelope_slots"]
        else:
            target["high_groups"] += 1
            target["high_slots"] += row["observed_slots"]
            target["high_envelope"] += row["envelope_slots"]
    window_rows = []
    for (prime_bound, block, shift), row in sorted(by_window.items()):
        accepted_atom_capacity = layer_count_bound * eta * row["accepted_envelope"]
        window_rows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                **row,
                "accepted_atom_capacity": accepted_atom_capacity,
                "accepted_slot_density": (
                    row["accepted_slots"] / row["accepted_envelope"]
                    if row["accepted_envelope"]
                    else 0.0
                ),
            }
        )
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "eta": eta,
        "layer_count_bound": layer_count_bound,
        "raw_atoms": sparse["raw_atoms"],
        "formal_atoms": sparse["formal_atoms"],
        "formal_moving_atoms": sparse["formal_moving_atoms"],
        "band_group_count": sparse["band_group_count"],
        "accepted_groups": sparse["accepted_groups"],
        "high_density_groups": sparse["high_density_groups"],
        "accepted_slots": sparse["accepted_slots"],
        "high_density_slots": sparse["high_density_slots"],
        "accepted_envelope_slots": sparse["accepted_envelope_slots"],
        "high_density_envelope_slots": sparse["high_density_envelope_slots"],
        "accepted_atom_capacity": accepted_capacity,
        "high_density_atom_capacity": high_capacity,
        "total_atom_capacity": total_capacity,
        "accepted_slot_density": (
            sparse["accepted_slots"] / sparse["accepted_envelope_slots"]
            if sparse["accepted_envelope_slots"]
            else 0.0
        ),
        "moving_atoms_over_capacity": (
            sparse["formal_moving_atoms"] / accepted_capacity
            if accepted_capacity
            else None
        ),
        "window_rows": window_rows,
    }


def print_table(package: dict) -> None:
    """输出 SparseSAE 总量付款表。"""
    ratio = (
        "NA"
        if package["moving_atoms_over_capacity"] is None
        else f"{package['moving_atoms_over_capacity']:.6f}"
    )
    print(
        "raw formal moving groups accepted high accepted_slots high_slots accepted_env high_env "
        "accepted_capacity total_capacity slot_density moving_over_capacity eta layers",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_moving_atoms']} "
        f"{package['band_group_count']} {package['accepted_groups']} {package['high_density_groups']} "
        f"{package['accepted_slots']} {package['high_density_slots']} "
        f"{package['accepted_envelope_slots']} {package['high_density_envelope_slots']} "
        f"{package['accepted_atom_capacity']:.6f} {package['total_atom_capacity']:.6f} "
        f"{package['accepted_slot_density']:.6f} {ratio} "
        f"{package['eta']:.6f} {package['layer_count_bound']}",
        flush=True,
    )
    print("p block shift accepted_groups high_groups accepted_slots accepted_env capacity density", flush=True)
    for row in package["window_rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} "
            f"{row['accepted_groups']} {row['high_groups']} "
            f"{row['accepted_slots']} {row['accepted_envelope']} "
            f"{row['accepted_atom_capacity']:.6f} {row['accepted_slot_density']:.6f}",
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
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--modulus-persistent-count", type=int, default=2)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = sparse_summability_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
        args.modulus_persistent_count,
        args.eta,
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
