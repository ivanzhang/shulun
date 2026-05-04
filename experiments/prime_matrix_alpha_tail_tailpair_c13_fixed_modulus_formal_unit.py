#!/usr/bin/env python3
"""AlphaTail C13 固定模见证的 formal unit 去重账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger import witness_atoms
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def physical_key(atom: dict) -> tuple:
    """返回 PDEC 计数中不可重复的物理见证键。

    m 不进入该键；同一 p/block/shift 下同一个 d 与同一尾素对在不同 m 层出现时，
    是嵌套审计层重复，不是两个独立 PDEC 约束。
    """
    return (
        atom["p"],
        atom["block"],
        atom["shift"],
        atom["gap"],
        atom["j1"],
        atom["j2"],
        atom["u"],
        atom["side"],
        atom["q"],
        atom["q_plus_g"],
        atom["d"],
    )


def unique_physical_atoms(atoms: list[dict]) -> list[dict]:
    """按物理键去重，保留首个代表。"""
    seen: set[tuple] = set()
    result = []
    for atom in atoms:
        key = physical_key(atom)
        if key in seen:
            continue
        seen.add(key)
        result.append(atom)
    return result


def fixed_atom_count(atoms: list[dict], threshold: int) -> tuple[int, int]:
    """返回达到固定模阈值的 atom 数与模数数。"""
    modulus_counts = Counter(atom["pair_modulus"] for atom in atoms)
    fixed_moduli = {modulus for modulus, count in modulus_counts.items() if count >= threshold}
    return (
        sum(count for modulus, count in modulus_counts.items() if modulus in fixed_moduli),
        len(fixed_moduli),
    )


def formal_unit_package(
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
    """返回固定模 formal unit 去重审计包。"""
    atoms = witness_atoms(selected, m_values, alpha, num_primes, local_c, endpoint_theta, slack_cut)
    unique_atoms = unique_physical_atoms(atoms)

    duplicate_buckets: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in atoms:
        duplicate_buckets[physical_key(atom)].append(atom)
    duplicate_classes = [
        {
            "multiplicity": len(bucket),
            "m_values": sorted({atom["m"] for atom in bucket}),
            "p": bucket[0]["p"],
            "block": bucket[0]["block"],
            "shift": bucket[0]["shift"],
            "gap": bucket[0]["gap"],
            "j1": bucket[0]["j1"],
            "j2": bucket[0]["j2"],
            "u": bucket[0]["u"],
            "side": bucket[0]["side"],
            "q": bucket[0]["q"],
            "q_plus_g": bucket[0]["q_plus_g"],
            "d": bucket[0]["d"],
        }
        for bucket in duplicate_buckets.values()
        if len(bucket) > 1
    ]
    duplicate_classes.sort(key=lambda item: (-item["multiplicity"], item["p"], item["q"], item["gap"]))

    by_shape_raw: defaultdict[tuple, list[dict]] = defaultdict(list)
    by_shape_formal: defaultdict[tuple, list[dict]] = defaultdict(list)
    for atom in atoms:
        by_shape_raw[atom["shape_key"]].append(atom)
    for atom in unique_atoms:
        by_shape_formal[atom["shape_key"]].append(atom)

    rows = []
    raw_fixed_total = 0
    formal_fixed_total = 0
    raw_fixed_shape_count = 0
    formal_fixed_shape_count = 0
    for shape_key in sorted(set(by_shape_raw) | set(by_shape_formal)):
        raw_atoms = by_shape_raw.get(shape_key, [])
        formal_atoms = by_shape_formal.get(shape_key, [])
        raw_fixed, raw_moduli = fixed_atom_count(raw_atoms, modulus_persistent_count)
        formal_fixed, formal_moduli = fixed_atom_count(formal_atoms, modulus_persistent_count)
        raw_fixed_total += raw_fixed
        formal_fixed_total += formal_fixed
        raw_fixed_shape_count += 1 if raw_fixed else 0
        formal_fixed_shape_count += 1 if formal_fixed else 0
        if raw_fixed or formal_fixed or len(raw_atoms) != len(formal_atoms):
            raw_counts = Counter(atom["pair_modulus"] for atom in raw_atoms)
            formal_counts = Counter(atom["pair_modulus"] for atom in formal_atoms)
            rows.append(
                {
                    "shape_key": shape_key,
                    "raw_atoms": len(raw_atoms),
                    "formal_atoms": len(formal_atoms),
                    "removed_duplicates": len(raw_atoms) - len(formal_atoms),
                    "raw_fixed_atoms": raw_fixed,
                    "formal_fixed_atoms": formal_fixed,
                    "raw_fixed_moduli": raw_moduli,
                    "formal_fixed_moduli": formal_moduli,
                    "raw_max_modulus_multiplicity": max(raw_counts.values(), default=0),
                    "formal_max_modulus_multiplicity": max(formal_counts.values(), default=0),
                }
            )
    rows.sort(
        key=lambda item: (
            -item["raw_fixed_atoms"],
            -item["removed_duplicates"],
            -item["formal_fixed_atoms"],
            item["shape_key"],
        )
    )
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "modulus_persistent_count": modulus_persistent_count,
        "raw_atoms": len(atoms),
        "formal_atoms": len(unique_atoms),
        "removed_duplicates": len(atoms) - len(unique_atoms),
        "duplicate_class_count": len(duplicate_classes),
        "raw_fixed_atoms": raw_fixed_total,
        "formal_fixed_atoms": formal_fixed_total,
        "raw_fixed_shape_count": raw_fixed_shape_count,
        "formal_fixed_shape_count": formal_fixed_shape_count,
        "rows": rows[:top],
        "duplicate_classes": duplicate_classes[:top],
    }


def print_table(package: dict) -> None:
    """输出 formal unit 去重简表。"""
    print(
        "raw_atoms formal_atoms removed_duplicates duplicate_classes "
        "raw_fixed_atoms formal_fixed_atoms raw_fixed_shapes formal_fixed_shapes local_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['removed_duplicates']} "
        f"{package['duplicate_class_count']} {package['raw_fixed_atoms']} "
        f"{package['formal_fixed_atoms']} {package['raw_fixed_shape_count']} "
        f"{package['formal_fixed_shape_count']} {package['local_c']:.6f}",
        flush=True,
    )
    print(
        "shape raw formal removed raw_fixed formal_fixed raw_moduli formal_moduli raw_max formal_max",
        flush=True,
    )
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        print(
            f"{shape} {row['raw_atoms']} {row['formal_atoms']} {row['removed_duplicates']} "
            f"{row['raw_fixed_atoms']} {row['formal_fixed_atoms']} "
            f"{row['raw_fixed_moduli']} {row['formal_fixed_moduli']} "
            f"{row['raw_max_modulus_multiplicity']} {row['formal_max_modulus_multiplicity']}",
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

    package = formal_unit_package(
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
