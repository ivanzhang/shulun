#!/usr/bin/env python3
"""AlphaTail C13 变模见证的端点深度槽预算。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit import unique_physical_atoms
from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def depth_slot_key(atom: dict) -> tuple:
    """返回不含 m 的端点深度槽键。"""
    return (
        atom["p"],
        atom["block"],
        atom["shift"],
        atom["shape_key"],
        atom["endpoint_residue_mod_u"],
        atom["q_depth"],
    )


def split_formal_moving_atoms(atoms: list[dict], modulus_persistent_count: int) -> tuple[list[dict], list[dict]]:
    """按 formal unit 后的固定模阈值拆出 fixed/moving 原子。"""
    by_shape: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in atoms:
        by_shape[atom["shape_key"]].append(atom)
    fixed = []
    moving = []
    for shape_atoms in by_shape.values():
        counts = Counter(atom["pair_modulus"] for atom in shape_atoms)
        fixed_moduli = {modulus for modulus, count in counts.items() if count >= modulus_persistent_count}
        for atom in shape_atoms:
            if atom["pair_modulus"] in fixed_moduli:
                fixed.append(atom)
            else:
                moving.append(atom)
    return fixed, moving


def depth_slot_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
    modulus_persistent_count: int,
    top: int,
) -> dict:
    """返回变模深度槽预算包。"""
    raw_atoms = witness_atoms(selected, m_values, alpha, num_primes, local_c, endpoint_theta, slack_cut)
    formal_atoms = unique_physical_atoms(raw_atoms)
    fixed_atoms, moving_atoms = split_formal_moving_atoms(formal_atoms, modulus_persistent_count)

    slots: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in moving_atoms:
        slots[depth_slot_key(atom)].append(atom)

    slot_rows = []
    capacity = len(m_values)
    for key, slot_atoms in slots.items():
        shape_key = key[3]
        slot_rows.append(
            {
                "slot_key": key,
                "shape_key": shape_key,
                "load": len(slot_atoms),
                "capacity": capacity,
                "capacity_pass": len(slot_atoms) <= capacity,
                "m_values": sorted({atom["m"] for atom in slot_atoms}),
                "p": key[0],
                "block": key[1],
                "shift": key[2],
                "endpoint_residue": key[4],
                "q_depth": key[5],
                "examples": [
                    {
                        "m": atom["m"],
                        "q": atom["q"],
                        "q_plus_g": atom["q_plus_g"],
                        "d": atom["d"],
                        "endpoint_depth": atom["endpoint_depth"],
                    }
                    for atom in slot_atoms[:5]
                ],
            }
        )
    slot_rows.sort(key=lambda item: (-item["load"], item["slot_key"]))

    by_shape: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in moving_atoms:
        by_shape[atom["shape_key"]].append(atom)
    shape_rows = []
    for shape_key, shape_atoms in by_shape.items():
        shape_slots = {depth_slot_key(atom) for atom in shape_atoms}
        q_depths = [atom["q_depth"] for atom in shape_atoms]
        endpoint_depths = [atom["endpoint_depth"] for atom in shape_atoms]
        shape_rows.append(
            {
                "shape_key": shape_key,
                "moving_atoms": len(shape_atoms),
                "depth_slots": len(shape_slots),
                "slot_capacity": len(shape_slots) * capacity,
                "slot_slack": len(shape_slots) * capacity - len(shape_atoms),
                "min_q_depth": min(q_depths),
                "max_q_depth": max(q_depths),
                "min_endpoint_depth": min(endpoint_depths),
                "max_endpoint_depth": max(endpoint_depths),
            }
        )
    shape_rows.sort(key=lambda item: (-item["moving_atoms"], -item["depth_slots"], item["shape_key"]))

    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "modulus_persistent_count": modulus_persistent_count,
        "raw_atoms": len(raw_atoms),
        "formal_atoms": len(formal_atoms),
        "formal_fixed_atoms": len(fixed_atoms),
        "formal_moving_atoms": len(moving_atoms),
        "depth_slot_count": len(slots),
        "slot_capacity": len(slots) * capacity,
        "slot_slack": len(slots) * capacity - len(moving_atoms),
        "max_slot_load": max((len(slot_atoms) for slot_atoms in slots.values()), default=0),
        "slot_capacity_failures": sum(1 for slot_atoms in slots.values() if len(slot_atoms) > capacity),
        "collision_slot_count": sum(1 for slot_atoms in slots.values() if len(slot_atoms) > 1),
        "shape_count": len(shape_rows),
        "shape_rows": shape_rows[:top],
        "slot_rows": slot_rows[:top],
    }


def print_table(package: dict) -> None:
    """输出变模深度槽预算表。"""
    print(
        "raw formal fixed moving slots slot_capacity slot_slack max_slot_load "
        "capacity_failures collision_slots shapes local_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_fixed_atoms']} "
        f"{package['formal_moving_atoms']} {package['depth_slot_count']} {package['slot_capacity']} "
        f"{package['slot_slack']} {package['max_slot_load']} {package['slot_capacity_failures']} "
        f"{package['collision_slot_count']} {package['shape_count']} {package['local_c']:.6f}",
        flush=True,
    )
    print("shape moving slots capacity slack q_depth endpoint_depth", flush=True)
    for row in package["shape_rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        print(
            f"{shape} {row['moving_atoms']} {row['depth_slots']} {row['slot_capacity']} "
            f"{row['slot_slack']} [{row['min_q_depth']},{row['max_q_depth']}] "
            f"[{row['min_endpoint_depth']},{row['max_endpoint_depth']}]",
            flush=True,
        )
    print("top_slots slot load capacity m_values examples", flush=True)
    for row in package["slot_rows"][:10]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        examples = ",".join(
            f"m{item['m']}:{item['q']}+{row['shape_key'][0]}={item['q_plus_g']}"
            for item in row["examples"]
        )
        print(
            f"slot {shape} h{row['q_depth']} eps{row['endpoint_residue']} "
            f"{row['load']} {row['capacity']} {row['m_values']} {examples}",
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
    parser.add_argument("--modulus-persistent-count", type=int, default=2)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = depth_slot_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
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
