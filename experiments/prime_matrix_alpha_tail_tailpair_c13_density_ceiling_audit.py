#!/usr/bin/env python3
"""AlphaTail C13 高密度端点带的固定 gap 密度天花板审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_density_ceiling_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --witness-c 1.2 --ceiling-c 1.3 --eta 0.04 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict

from prime_matrix_alpha_tail_tailpair_brun_constant_audit import (
    brun_scale_for_interval,
    singular_factor,
)
from prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope import (
    atom_band_pass,
    band_key,
    band_limit_for_atom,
)
from prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit import unique_physical_atoms
from prime_matrix_alpha_tail_tailpair_c13_layer_interval_reduction import q_interval_for_layer
from prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget import split_formal_moving_atoms
from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def critical_q_floor(local_c: float, singular: float, density_threshold: float) -> float:
    """返回使 C*S/log(q)^2 <= density_threshold 成立的 q 下界。"""
    if density_threshold <= 0:
        return math.inf
    return math.exp(math.sqrt(local_c * singular / density_threshold))


def density_ceiling_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    witness_c: float,
    ceiling_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
    modulus_persistent_count: int,
    eta: float,
    top: int,
) -> dict:
    """返回 C13 高密度层的固定 gap 密度天花板包。"""
    raw_atoms = witness_atoms(selected, m_values, alpha, num_primes, witness_c, endpoint_theta, slack_cut)
    formal_atoms = unique_physical_atoms(raw_atoms)
    fixed_atoms, moving_atoms = split_formal_moving_atoms(formal_atoms, modulus_persistent_count)
    band_atoms = [atom for atom in moving_atoms if atom_band_pass(atom, endpoint_band_theta)]
    overflow_atoms = [atom for atom in moving_atoms if not atom_band_pass(atom, endpoint_band_theta)]

    groups: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in band_atoms:
        groups[band_key(atom)].append(atom)

    rows = []
    layer_eta = eta / max(1, len(m_values))
    for key, atoms in groups.items():
        shape_key = key[3]
        epsilon = key[4]
        gap = shape_key[0]
        step = shape_key[3]
        max_h = 0
        for atom in atoms:
            limit = band_limit_for_atom(atom, endpoint_band_theta)
            if limit >= epsilon:
                max_h = max(max_h, (limit - epsilon) // step)
        envelope_slots = max_h + 1
        if envelope_slots <= 0:
            continue

        by_m: defaultdict[int, list[dict]] = defaultdict(list)
        for atom in atoms:
            by_m[atom["m"]].append(atom)

        for point_count, layer_atoms in by_m.items():
            representative = layer_atoms[0]
            q_lower, q_upper = q_interval_for_layer(representative, max_h)
            q_values = sorted({atom["q"] for atom in layer_atoms})
            observed = len(q_values)
            scale = brun_scale_for_interval(q_lower, q_upper, gap)
            singular = singular_factor(gap)
            ceiling_count = ceiling_c * scale
            ceiling_density = ceiling_count / envelope_slots
            actual_density = observed / envelope_slots
            required_c = observed / scale if scale else None
            critical_c_eta = eta * envelope_slots / scale if scale else math.inf
            critical_c_layer_eta = layer_eta * envelope_slots / scale if scale else math.inf
            rows.append(
                {
                    "band_key": key,
                    "shape_key": shape_key,
                    "epsilon": epsilon,
                    "m": point_count,
                    "gap": gap,
                    "q_lower": q_lower,
                    "q_upper": q_upper,
                    "q_length": q_upper - q_lower + 1,
                    "observed": observed,
                    "actual_density": actual_density,
                    "scale": scale,
                    "singular": singular,
                    "required_c": required_c,
                    "critical_c_eta": critical_c_eta,
                    "critical_c_layer_eta": critical_c_layer_eta,
                    "ceiling_count": ceiling_count,
                    "ceiling_density": ceiling_density,
                    "eta": eta,
                    "layer_eta": layer_eta,
                    "single_layer_sparse_cert": ceiling_density <= eta + 1e-15,
                    "pigeonhole_sparse_cert": ceiling_density <= layer_eta + 1e-15,
                    "critical_q_eta": critical_q_floor(ceiling_c, singular, eta),
                    "critical_q_layer_eta": critical_q_floor(ceiling_c, singular, layer_eta),
                    "q_min_observed": min(q_values) if q_values else None,
                    "q_max_observed": max(q_values) if q_values else None,
                }
            )

    rows.sort(
        key=lambda item: (
            -item["ceiling_density"],
            -item["actual_density"],
            item["q_lower"],
            item["gap"],
            item["m"],
        )
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "witness_c": witness_c,
        "ceiling_c": ceiling_c,
        "endpoint_theta": endpoint_theta,
        "endpoint_band_theta": endpoint_band_theta,
        "slack_cut": slack_cut,
        "modulus_persistent_count": modulus_persistent_count,
        "eta": eta,
        "layer_eta": layer_eta,
        "raw_atoms": len(raw_atoms),
        "formal_atoms": len(formal_atoms),
        "formal_fixed_atoms": len(fixed_atoms),
        "formal_moving_atoms": len(moving_atoms),
        "overflow_atoms": len(overflow_atoms),
        "band_group_count": len(groups),
        "layer_count": len(rows),
        "single_layer_sparse_cert_count": sum(1 for row in rows if row["single_layer_sparse_cert"]),
        "pigeonhole_sparse_cert_count": sum(1 for row in rows if row["pigeonhole_sparse_cert"]),
        "max_ceiling_density": max((row["ceiling_density"] for row in rows), default=0.0),
        "max_actual_density": max((row["actual_density"] for row in rows), default=0.0),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出密度天花板审计表。"""
    print(
        "raw formal moving overflow groups layers single_cert pigeonhole_cert "
        "max_actual_density max_ceiling_density eta layer_eta witness_C ceiling_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_moving_atoms']} "
        f"{package['overflow_atoms']} {package['band_group_count']} {package['layer_count']} "
        f"{package['single_layer_sparse_cert_count']} {package['pigeonhole_sparse_cert_count']} "
        f"{package['max_actual_density']:.6f} {package['max_ceiling_density']:.6f} "
        f"{package['eta']:.6f} {package['layer_eta']:.6f} "
        f"{package['witness_c']:.6f} {package['ceiling_c']:.6f}",
        flush=True,
    )
    print(
        "shape eps m q_interval obs actual_density required_C ceiling_density "
        "critical_C_eta critical_C_layer single_cert pigeonhole_cert qcrit_eta qcrit_layer observed_q",
        flush=True,
    )
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        observed_q = (
            "NA"
            if row["q_min_observed"] is None
            else f"[{row['q_min_observed']},{row['q_max_observed']}]"
        )
        print(
            f"{shape} eps{row['epsilon']} {row['m']} "
            f"[{row['q_lower']},{row['q_upper']}] {row['observed']} "
            f"{row['actual_density']:.6f} "
            f"{(row['required_c'] if row['required_c'] is not None else 0.0):.6f} "
            f"{row['ceiling_density']:.6f} "
            f"{row['critical_c_eta']:.6f} {row['critical_c_layer_eta']:.6f} "
            f"{row['single_layer_sparse_cert']} {row['pigeonhole_sparse_cert']} "
            f"{row['critical_q_eta']:.2f} {row['critical_q_layer_eta']:.2f} {observed_q}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--witness-c", type=float, default=1.2)
    parser.add_argument("--ceiling-c", type=float, default=1.3)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--modulus-persistent-count", type=int, default=2)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = density_ceiling_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.witness_c,
        args.ceiling_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
        args.modulus_persistent_count,
        args.eta,
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
