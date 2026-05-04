#!/usr/bin/env python3
"""AlphaTail C13 见证相位的固定模/变模分流账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_pairphase_modulus_route.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_pairphase_modulus_route.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter

from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def atom_depth_relation_ok(atom: dict) -> bool:
    """核验端点深度是否落在同商数锁定给出的 u-阶梯上。"""
    return atom["endpoint_depth"] == atom["endpoint_residue_mod_u"] + atom["u"] * atom["q_depth"]


def modulus_route_package(
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
    """返回固定模/变模无损分流账本。"""
    atoms = witness_atoms(selected, m_values, alpha, num_primes, local_c, endpoint_theta, slack_cut)
    by_shape: dict[tuple[int, int, int, int, str], list[dict]] = {}
    for atom in atoms:
        by_shape.setdefault(atom["shape_key"], []).append(atom)

    rows = []
    fixed_modulus_total = 0
    moving_modulus_total = 0
    for shape_key, shape_atoms in by_shape.items():
        modulus_counts = Counter(atom["pair_modulus"] for atom in shape_atoms)
        fixed_moduli = {
            modulus for modulus, count in modulus_counts.items() if count >= modulus_persistent_count
        }
        fixed_atoms = [atom for atom in shape_atoms if atom["pair_modulus"] in fixed_moduli]
        moving_atoms = [atom for atom in shape_atoms if atom["pair_modulus"] not in fixed_moduli]
        fixed_modulus_total += len(fixed_atoms)
        moving_modulus_total += len(moving_atoms)
        if fixed_atoms and moving_atoms:
            route = "MixedFixedAndMoving"
        elif fixed_atoms:
            route = "FixedModulus-PDEC"
        else:
            route = "MovingModulusDepth-SAE"

        depth_failures = sum(1 for atom in shape_atoms if not atom_depth_relation_ok(atom))
        repeated_examples = []
        for modulus, count in modulus_counts.most_common(5):
            if count < modulus_persistent_count:
                continue
            example = next(atom for atom in shape_atoms if atom["pair_modulus"] == modulus)
            repeated_examples.append(
                {
                    "modulus": modulus,
                    "count": count,
                    "q": example["q"],
                    "q_plus_g": example["q_plus_g"],
                    "d": example["d"],
                }
            )
        moving_examples = [
            {
                "q": atom["q"],
                "q_plus_g": atom["q_plus_g"],
                "d": atom["d"],
                "depth": atom["endpoint_depth"],
                "q_depth": atom["q_depth"],
            }
            for atom in moving_atoms[:5]
        ]
        rows.append(
            {
                "shape_key": shape_key,
                "route": route,
                "atom_count": len(shape_atoms),
                "fixed_modulus_atoms": len(fixed_atoms),
                "moving_modulus_atoms": len(moving_atoms),
                "distinct_moduli": len(modulus_counts),
                "fixed_moduli": len(fixed_moduli),
                "max_modulus_multiplicity": max(modulus_counts.values(), default=0),
                "depth_relation_failures": depth_failures,
                "min_endpoint_depth": min((atom["endpoint_depth"] for atom in shape_atoms), default=None),
                "max_endpoint_depth": max((atom["endpoint_depth"] for atom in shape_atoms), default=None),
                "min_q_depth": min((atom["q_depth"] for atom in shape_atoms), default=None),
                "max_q_depth": max((atom["q_depth"] for atom in shape_atoms), default=None),
                "repeated_examples": repeated_examples,
                "moving_examples": moving_examples,
            }
        )
    rows.sort(
        key=lambda item: (
            item["route"] == "MovingModulusDepth-SAE",
            item["route"] == "MixedFixedAndMoving",
            -item["atom_count"],
            -item["fixed_modulus_atoms"],
            item["shape_key"],
        )
    )
    route_counts = Counter(row["route"] for row in rows)
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "modulus_persistent_count": modulus_persistent_count,
        "atom_count": len(atoms),
        "shape_count": len(rows),
        "fixed_modulus_atoms": fixed_modulus_total,
        "moving_modulus_atoms": moving_modulus_total,
        "depth_relation_failures": sum(1 for atom in atoms if not atom_depth_relation_ok(atom)),
        "route_counts": dict(sorted(route_counts.items())),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出固定模/变模分流账本。"""
    route_counts = ",".join(
        f"{route}:{count}" for route, count in package["route_counts"].items()
    ) or "none"
    print(
        "atoms shapes fixed_atoms moving_atoms depth_failures route_counts local_C",
        flush=True,
    )
    print(
        f"{package['atom_count']} {package['shape_count']} {package['fixed_modulus_atoms']} "
        f"{package['moving_modulus_atoms']} {package['depth_relation_failures']} "
        f"{route_counts} {package['local_c']:.6f}",
        flush=True,
    )
    print(
        "route shape atoms fixed moving moduli fixed_moduli max_mult depth q_depth repeated moving",
        flush=True,
    )
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        repeated = ",".join(
            f"{item['q']}+{row['shape_key'][0]}={item['q_plus_g']}x{item['count']}"
            for item in row["repeated_examples"][:3]
        )
        moving = ",".join(
            f"{item['q']}+{row['shape_key'][0]}={item['q_plus_g']}@h{item['q_depth']}"
            for item in row["moving_examples"][:3]
        )
        print(
            f"{row['route']} {shape} {row['atom_count']} {row['fixed_modulus_atoms']} "
            f"{row['moving_modulus_atoms']} {row['distinct_moduli']} {row['fixed_moduli']} "
            f"{row['max_modulus_multiplicity']} "
            f"[{row['min_endpoint_depth']},{row['max_endpoint_depth']}] "
            f"[{row['min_q_depth']},{row['max_q_depth']}] "
            f"{repeated or 'none'} {moving or 'none'}",
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
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = modulus_route_package(
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
