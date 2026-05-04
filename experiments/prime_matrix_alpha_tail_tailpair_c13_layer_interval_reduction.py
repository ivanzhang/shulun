#!/usr/bin/env python3
"""AlphaTail C13 高密度层到一维固定 gap q-区间的归约证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_layer_interval_reduction.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --eta 0.03 --format table
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict

from prime_matrix_alpha_tail_tailpair_brun_constant_audit import brun_scale_for_interval
from prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope import (
    atom_band_pass,
    band_key,
    band_limit_for_atom,
)
from prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit import unique_physical_atoms
from prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget import split_formal_moving_atoms
from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def q_base_for_atom(atom: dict) -> int:
    """返回 h=0 对应的 q 端点。"""
    if atom["side"] == "left":
        return atom["q"] - atom["q_depth"]
    return atom["q"] + atom["q_depth"]


def q_interval_for_layer(atom: dict, max_h: int) -> tuple[int, int]:
    """返回该层 envelope 对应的一维 q 区间。"""
    base = q_base_for_atom(atom)
    if atom["side"] == "left":
        return base, base + max_h
    return base - max_h, base


def layer_interval_package(
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
    top: int,
) -> dict:
    """返回高密度层的一维 q-区间归约证书。"""
    raw_atoms = witness_atoms(selected, m_values, alpha, num_primes, local_c, endpoint_theta, slack_cut)
    formal_atoms = unique_physical_atoms(raw_atoms)
    fixed_atoms, moving_atoms = split_formal_moving_atoms(formal_atoms, modulus_persistent_count)
    band_atoms = [atom for atom in moving_atoms if atom_band_pass(atom, endpoint_band_theta)]
    overflow_atoms = [atom for atom in moving_atoms if not atom_band_pass(atom, endpoint_band_theta)]

    groups: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in band_atoms:
        groups[band_key(atom)].append(atom)

    rows = []
    for key, atoms in groups.items():
        shape_key = key[3]
        epsilon = key[4]
        step = shape_key[3]
        max_h = 0
        for atom in atoms:
            limit = band_limit_for_atom(atom, endpoint_band_theta)
            if limit >= epsilon:
                max_h = max(max_h, (limit - epsilon) // step)
        envelope_slots = max_h + 1
        observed_slots = len({(atom["q_depth"], atom["endpoint_residue_mod_u"]) for atom in atoms})
        density = observed_slots / envelope_slots if envelope_slots else 0.0
        if density <= eta:
            continue

        by_m: defaultdict[int, list[dict]] = defaultdict(list)
        for atom in atoms:
            by_m[atom["m"]].append(atom)
        layer_rows = []
        for point_count, layer_atoms in by_m.items():
            layer_slots = {atom["q_depth"] for atom in layer_atoms}
            representative = layer_atoms[0]
            q_lower, q_upper = q_interval_for_layer(representative, max_h)
            q_values = sorted({atom["q"] for atom in layer_atoms})
            scale = brun_scale_for_interval(q_lower, q_upper, shape_key[0])
            layer_rows.append(
                {
                    "m": point_count,
                    "q_lower": q_lower,
                    "q_upper": q_upper,
                    "q_length": q_upper - q_lower + 1,
                    "witness_pairs": len(q_values),
                    "layer_density": len(q_values) / envelope_slots if envelope_slots else 0.0,
                    "brun_scale": scale,
                    "required_c": len(q_values) / scale if scale else None,
                    "h_min": min(layer_slots),
                    "h_max": max(layer_slots),
                    "q_min": min(q_values),
                    "q_max": max(q_values),
                    "q_base": q_base_for_atom(representative),
                    "examples": [
                        {
                            "q": atom["q"],
                            "q_plus_g": atom["q_plus_g"],
                            "h": atom["q_depth"],
                            "d": atom["d"],
                        }
                        for atom in sorted(layer_atoms, key=lambda item: item["q_depth"])[:6]
                    ],
                }
            )
        layer_rows.sort(key=lambda item: (-item["witness_pairs"], item["m"]))
        best = layer_rows[0] if layer_rows else None
        rows.append(
            {
                "band_key": key,
                "shape_key": shape_key,
                "epsilon": epsilon,
                "step": step,
                "observed_slots": observed_slots,
                "envelope_slots": envelope_slots,
                "density": density,
                "eta_excess": observed_slots - eta * envelope_slots,
                "best_layer": best,
                "layers": layer_rows,
            }
        )

    rows.sort(
        key=lambda item: (
            -(item["best_layer"]["required_c"] if item["best_layer"] and item["best_layer"]["required_c"] else 0),
            -item["density"],
            -item["observed_slots"],
            item["band_key"],
        )
    )
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
        "eta": eta,
        "raw_atoms": len(raw_atoms),
        "formal_atoms": len(formal_atoms),
        "formal_fixed_atoms": len(fixed_atoms),
        "formal_moving_atoms": len(moving_atoms),
        "overflow_atoms": len(overflow_atoms),
        "high_density_groups": len(rows),
        "max_required_c": max(
            (
                row["best_layer"]["required_c"]
                for row in rows
                if row["best_layer"] and row["best_layer"]["required_c"] is not None
            ),
            default=0.0,
        ),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出一维 q-区间归约表。"""
    print(
        "raw formal fixed moving overflow high_groups max_required_C eta local_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_fixed_atoms']} "
        f"{package['formal_moving_atoms']} {package['overflow_atoms']} "
        f"{package['high_density_groups']} {package['max_required_c']:.6f} "
        f"{package['eta']:.6f} {package['local_c']:.6f}",
        flush=True,
    )
    print(
        "shape eps step best_m q_interval q_len witnesses density scale required_C "
        "h_range q_hits examples",
        flush=True,
    )
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        best = row["best_layer"] or {}
        examples = ",".join(
            f"{item['q']}+{row['shape_key'][0]}={item['q_plus_g']}@h{item['h']}"
            for item in best.get("examples", [])
        )
        required_c = best.get("required_c")
        print(
            f"{shape} eps{row['epsilon']} u{row['step']} {best.get('m','NA')} "
            f"[{best.get('q_lower','NA')},{best.get('q_upper','NA')}] "
            f"{best.get('q_length',0)} {best.get('witness_pairs',0)} "
            f"{best.get('layer_density',0.0):.6f} {best.get('brun_scale',0.0):.6f} "
            f"{(required_c if required_c is not None else 0.0):.6f} "
            f"[{best.get('h_min','NA')},{best.get('h_max','NA')}] "
            f"[{best.get('q_min','NA')},{best.get('q_max','NA')}] "
            f"{examples or 'none'}",
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
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = layer_interval_package(
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
