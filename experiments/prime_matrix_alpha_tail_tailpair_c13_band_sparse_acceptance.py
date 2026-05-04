#!/usr/bin/env python3
"""AlphaTail C13 端点带宽 envelope 的稀疏验收账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_band_sparse_acceptance.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_band_sparse_acceptance.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --slack-cut 40 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope import depth_band_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def sparse_acceptance_package(
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
    """返回 envelope 稀疏/高密度二分账本。"""
    envelope = depth_band_package(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        endpoint_band_theta,
        slack_cut,
        modulus_persistent_count,
        1_000_000,
    )
    accepted = []
    high_density = []
    for row in envelope["rows"]:
        density = row["observed_slots"] / row["envelope_slots"] if row["envelope_slots"] else 0.0
        item = {
            **row,
            "density": density,
            "eta_slack": eta * row["envelope_slots"] - row["observed_slots"],
            "route": "SparseSAE" if density <= eta else "HighDensityEnvelope",
        }
        if density <= eta:
            accepted.append(item)
        else:
            high_density.append(item)
    accepted_slots = sum(row["observed_slots"] for row in accepted)
    high_slots = sum(row["observed_slots"] for row in high_density)
    accepted_envelope = sum(row["envelope_slots"] for row in accepted)
    high_envelope = sum(row["envelope_slots"] for row in high_density)
    rows = sorted(
        high_density + accepted,
        key=lambda item: (
            item["route"] == "SparseSAE",
            -item["density"],
            -item["observed_slots"],
            item["band_key"],
        ),
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
        "raw_atoms": envelope["raw_atoms"],
        "formal_atoms": envelope["formal_atoms"],
        "formal_fixed_atoms": envelope["formal_fixed_atoms"],
        "formal_moving_atoms": envelope["formal_moving_atoms"],
        "overflow_atoms": envelope["overflow_atoms"],
        "band_group_count": envelope["band_group_count"],
        "accepted_groups": len(accepted),
        "high_density_groups": len(high_density),
        "accepted_slots": accepted_slots,
        "high_density_slots": high_slots,
        "accepted_envelope_slots": accepted_envelope,
        "high_density_envelope_slots": high_envelope,
        "max_density": max((row["density"] for row in rows), default=0.0),
        "min_eta_slack": min((row["eta_slack"] for row in rows), default=None),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出稀疏验收表。"""
    min_slack = "NA" if package["min_eta_slack"] is None else f"{package['min_eta_slack']:.6f}"
    print(
        "raw formal fixed moving overflow groups accepted high accepted_slots high_slots "
        "max_density min_eta_slack eta local_C",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_fixed_atoms']} "
        f"{package['formal_moving_atoms']} {package['overflow_atoms']} {package['band_group_count']} "
        f"{package['accepted_groups']} {package['high_density_groups']} "
        f"{package['accepted_slots']} {package['high_density_slots']} "
        f"{package['max_density']:.6f} {min_slack} {package['eta']:.6f} "
        f"{package['local_c']:.6f}",
        flush=True,
    )
    print("route shape eps step observed envelope density eta_slack h_range q_depth", flush=True)
    for row in package["rows"]:
        shape = f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        print(
            f"{row['route']} {shape} eps{row['epsilon']} u{row['step']} "
            f"{row['observed_slots']} {row['envelope_slots']} {row['density']:.6f} "
            f"{row['eta_slack']:.6f} [0,{row['max_h_envelope']}] "
            f"[{row['min_q_depth']},{row['max_q_depth']}]",
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

    package = sparse_acceptance_package(
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
