#!/usr/bin/env python3
"""AlphaTail C13 HighDensityEnvelope 的层投影证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_high_density_envelope_certificate.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --eta 0.03 --format table
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope import (
    atom_band_pass,
    band_key,
    band_limit_for_atom,
)
from prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit import unique_physical_atoms
from prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget import (
    split_formal_moving_atoms,
)
from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def high_density_package(
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
    """返回 HighDensityEnvelope 的层投影证书包。"""
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
            layer_density = len(layer_slots) / envelope_slots if envelope_slots else 0.0
            layer_rows.append(
                {
                    "m": point_count,
                    "atom_count": len(layer_atoms),
                    "slot_count": len(layer_slots),
                    "layer_density": layer_density,
                    "q_min": min(atom["q"] for atom in layer_atoms),
                    "q_max": max(atom["q"] for atom in layer_atoms),
                    "h_min": min(layer_slots),
                    "h_max": max(layer_slots),
                    "examples": [
                        {
                            "q": atom["q"],
                            "q_plus_g": atom["q_plus_g"],
                            "h": atom["q_depth"],
                            "d": atom["d"],
                        }
                        for atom in sorted(layer_atoms, key=lambda item: item["q_depth"])[:5]
                    ],
                }
            )
        layer_rows.sort(key=lambda item: (-item["slot_count"], item["m"]))
        best_layer = layer_rows[0] if layer_rows else None
        layer_floor = math.ceil(observed_slots / max(1, len(m_values)))
        layer_floor_density = layer_floor / envelope_slots if envelope_slots else 0.0
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
                "layer_floor": layer_floor,
                "layer_floor_density": layer_floor_density,
                "best_layer": best_layer,
                "layers": layer_rows,
            }
        )

    rows.sort(key=lambda item: (-item["density"], -item["observed_slots"], item["band_key"]))
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
        "high_density_slots": sum(row["observed_slots"] for row in rows),
        "max_density": max((row["density"] for row in rows), default=0.0),
        "max_best_layer_density": max(
            (row["best_layer"]["layer_density"] for row in rows if row["best_layer"]),
            default=0.0,
        ),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出 HighDensityEnvelope 层投影证书。"""
    print(
        "raw formal fixed moving overflow high_groups high_slots max_density "
        "max_best_layer_density eta local_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_fixed_atoms']} "
        f"{package['formal_moving_atoms']} {package['overflow_atoms']} "
        f"{package['high_density_groups']} {package['high_density_slots']} "
        f"{package['max_density']:.6f} {package['max_best_layer_density']:.6f} "
        f"{package['eta']:.6f} {package['local_c']:.6f}",
        flush=True,
    )
    print(
        "shape eps step observed envelope density eta_excess layer_floor best_m "
        "best_slots best_density q_range h_range examples",
        flush=True,
    )
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        best = row["best_layer"] or {}
        examples = ",".join(
            f"{item['q']}+{row['shape_key'][0]}={item['q_plus_g']}@h{item['h']}"
            for item in best.get("examples", [])
        )
        print(
            f"{shape} eps{row['epsilon']} u{row['step']} {row['observed_slots']} "
            f"{row['envelope_slots']} {row['density']:.6f} {row['eta_excess']:.6f} "
            f"{row['layer_floor']} {best.get('m','NA')} {best.get('slot_count',0)} "
            f"{best.get('layer_density',0.0):.6f} "
            f"[{best.get('q_min','NA')},{best.get('q_max','NA')}] "
            f"[{best.get('h_min','NA')},{best.get('h_max','NA')}] "
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

    package = high_density_package(
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
