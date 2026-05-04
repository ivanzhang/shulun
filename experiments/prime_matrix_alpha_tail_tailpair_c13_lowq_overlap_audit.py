#!/usr/bin/env python3
"""AlphaTail C13 低 q 高密度剩余层的共享锚重叠审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_overlap_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --witness-c 1.2 --ceiling-c 1.3 --eta 0.04 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_tailpair_brun_constant_audit import brun_scale_for_interval
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


def lowq_overlap_package(
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
    """返回不能由密度天花板排斥的低 q 层重叠包。"""
    raw_atoms = witness_atoms(selected, m_values, alpha, num_primes, witness_c, endpoint_theta, slack_cut)
    formal_atoms = unique_physical_atoms(raw_atoms)
    fixed_atoms, moving_atoms = split_formal_moving_atoms(formal_atoms, modulus_persistent_count)
    band_atoms = [atom for atom in moving_atoms if atom_band_pass(atom, endpoint_band_theta)]

    groups: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in band_atoms:
        groups[band_key(atom)].append(atom)

    lowq_layers = []
    q_counter: Counter[int] = Counter()
    pair_counter: Counter[tuple[int, int, int]] = Counter()
    shape_counter: Counter[tuple] = Counter()
    interval_counter: Counter[tuple[int, int]] = Counter()

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
            scale = brun_scale_for_interval(q_lower, q_upper, gap)
            ceiling_density = ceiling_c * scale / envelope_slots if envelope_slots else 0.0
            if ceiling_density <= eta + 1e-15:
                continue

            q_values = sorted({atom["q"] for atom in layer_atoms})
            pairs = sorted({(atom["q"], atom["q_plus_g"], atom["q_plus_g"] - atom["q"]) for atom in layer_atoms})
            for q_value in q_values:
                q_counter[q_value] += 1
            for pair in pairs:
                pair_counter[pair] += 1
            shape_counter[tuple(shape_key)] += 1
            interval_counter[(q_lower, q_upper)] += 1
            lowq_layers.append(
                {
                    "band_key": key,
                    "shape_key": shape_key,
                    "epsilon": epsilon,
                    "m": point_count,
                    "q_lower": q_lower,
                    "q_upper": q_upper,
                    "observed": len(q_values),
                    "actual_density": len(q_values) / envelope_slots,
                    "ceiling_density": ceiling_density,
                    "required_c": len(q_values) / scale if scale else None,
                    "q_values": q_values,
                    "pairs": pairs,
                }
            )

    lowq_layers.sort(
        key=lambda item: (
            -item["observed"],
            item["q_lower"],
            item["shape_key"],
            item["m"],
        )
    )
    q_rows = [
        {
            "q": q,
            "multiplicity": multiplicity,
            "pairs": [
                {"q_plus_g": q_plus_g, "gap": gap, "multiplicity": pair_counter[(q, q_plus_g, gap)]}
                for qq, q_plus_g, gap in sorted(pair_counter)
                if qq == q
            ],
        }
        for q, multiplicity in q_counter.most_common()
    ]
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "witness_c": witness_c,
        "ceiling_c": ceiling_c,
        "eta": eta,
        "raw_atoms": len(raw_atoms),
        "formal_atoms": len(formal_atoms),
        "formal_fixed_atoms": len(fixed_atoms),
        "formal_moving_atoms": len(moving_atoms),
        "band_group_count": len(groups),
        "lowq_layer_count": len(lowq_layers),
        "total_layer_witnesses": sum(layer["observed"] for layer in lowq_layers),
        "unique_q_count": len(q_counter),
        "unique_pair_count": len(pair_counter),
        "max_q_multiplicity": max(q_counter.values(), default=0),
        "shape_summary": [
            {"shape_key": key, "count": value}
            for key, value in shape_counter.most_common()
        ],
        "interval_summary": [
            {"q_interval": key, "count": value}
            for key, value in interval_counter.most_common()
        ],
        "q_rows": q_rows[:top],
        "layers": lowq_layers[:top],
    }


def print_table(package: dict) -> None:
    """输出低 q 重叠审计表。"""
    print(
        "raw formal moving groups lowq_layers total_witnesses unique_q unique_pairs "
        "max_q_mult eta witness_C ceiling_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_moving_atoms']} "
        f"{package['band_group_count']} {package['lowq_layer_count']} "
        f"{package['total_layer_witnesses']} {package['unique_q_count']} "
        f"{package['unique_pair_count']} {package['max_q_multiplicity']} "
        f"{package['eta']:.6f} {package['witness_c']:.6f} {package['ceiling_c']:.6f}",
        flush=True,
    )
    print("q_support q multiplicity pairs", flush=True)
    for row in package["q_rows"]:
        pairs = ",".join(
            f"{item['q_plus_g']}(g{item['gap']})x{item['multiplicity']}"
            for item in row["pairs"]
        )
        print(f"q {row['q']} {row['multiplicity']} {pairs}", flush=True)
    print("layers shape eps m q_interval obs actual_density required_C ceiling_density q_values", flush=True)
    for layer in package["layers"]:
        shape = (
            f"g{layer['shape_key'][0]}:j{layer['shape_key'][1]}-"
            f"{layer['shape_key'][2]}:u{layer['shape_key'][3]}:{layer['shape_key'][4]}"
        )
        q_values = ",".join(str(q) for q in layer["q_values"])
        print(
            f"{shape} eps{layer['epsilon']} {layer['m']} "
            f"[{layer['q_lower']},{layer['q_upper']}] {layer['observed']} "
            f"{layer['actual_density']:.6f} "
            f"{(layer['required_c'] if layer['required_c'] is not None else 0.0):.6f} "
            f"{layer['ceiling_density']:.6f} {q_values}",
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

    package = lowq_overlap_package(
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
