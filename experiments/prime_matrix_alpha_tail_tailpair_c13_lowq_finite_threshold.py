#!/usr/bin/env python3
"""AlphaTail C13 低 q 高密度分支的有限阈值证书。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_finite_threshold.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --witness-c 1.2 --ceiling-c 1.3 --eta 0.04 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
import math

from prime_matrix_alpha_tail_tailpair_brun_constant_audit import singular_factor
from prime_matrix_alpha_tail_tailpair_c13_band_sparse_acceptance import sparse_acceptance_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def q_threshold(ceiling_c: float, singular: float, density: float) -> float:
    """返回固定 gap 密度天花板低于 density 所需的 q 下界。"""
    if density <= 0:
        return math.inf
    return math.exp(math.sqrt(ceiling_c * singular / density))


def lowq_finite_threshold_package(
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
    """返回低 q 高密度分支的阈值/有限证书包。"""
    sparse = sparse_acceptance_package(
        selected,
        m_values,
        alpha,
        num_primes,
        witness_c,
        endpoint_theta,
        endpoint_band_theta,
        slack_cut,
        modulus_persistent_count,
        eta,
        1_000_000,
    )
    layer_count_bound = max(1, len(m_values))
    layer_density = eta / layer_count_bound
    rows = []
    for row in sparse["rows"]:
        gap = row["shape_key"][0]
        singular = singular_factor(gap)
        qcrit_single = q_threshold(ceiling_c, singular, eta)
        qcrit_group = q_threshold(ceiling_c, singular, layer_density)
        prime_bound = row["band_key"][0]
        tail_floor = alpha * prime_bound
        if tail_floor >= qcrit_group:
            route = "CeilingPigeonhole"
        elif row["route"] == "SparseSAE":
            route = "FiniteExactSparse"
        else:
            route = "UnclosedHighDensity"
        rows.append(
            {
                "p": prime_bound,
                "block": row["band_key"][1],
                "shift": row["band_key"][2],
                "shape_key": row["shape_key"],
                "epsilon": row["epsilon"],
                "observed_slots": row["observed_slots"],
                "envelope_slots": row["envelope_slots"],
                "density": row["density"],
                "eta_slack": row["eta_slack"],
                "singular": singular,
                "tail_floor": tail_floor,
                "qcrit_single": qcrit_single,
                "qcrit_group": qcrit_group,
                "pcrit_group": qcrit_group / alpha if alpha else math.inf,
                "sparse_route": row["route"],
                "closure_route": route,
            }
        )
    rows.sort(
        key=lambda item: (
            item["closure_route"] != "UnclosedHighDensity",
            -item["density"],
            -item["qcrit_group"],
            item["p"],
            item["shape_key"],
        )
    )
    max_qcrit_group = max((row["qcrit_group"] for row in rows), default=0.0)
    max_pcrit_group = max((row["pcrit_group"] for row in rows), default=0.0)
    route_counts: dict[str, int] = {}
    for row in rows:
        route_counts[row["closure_route"]] = route_counts.get(row["closure_route"], 0) + 1
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "witness_c": witness_c,
        "ceiling_c": ceiling_c,
        "eta": eta,
        "layer_density": layer_density,
        "layer_count_bound": layer_count_bound,
        "raw_atoms": sparse["raw_atoms"],
        "formal_atoms": sparse["formal_atoms"],
        "band_group_count": sparse["band_group_count"],
        "accepted_groups": sparse["accepted_groups"],
        "high_density_groups": sparse["high_density_groups"],
        "max_density": sparse["max_density"],
        "min_eta_slack": sparse["min_eta_slack"],
        "max_qcrit_group": max_qcrit_group,
        "max_pcrit_group": max_pcrit_group,
        "route_counts": dict(sorted(route_counts.items())),
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出低 q 有限阈值表。"""
    route_counts = ",".join(f"{key}:{value}" for key, value in package["route_counts"].items()) or "none"
    min_slack = "NA" if package["min_eta_slack"] is None else f"{package['min_eta_slack']:.6f}"
    print(
        "raw formal groups accepted high max_density min_eta_slack max_qcrit_group "
        "max_pcrit_group eta layer_eta witness_C ceiling_C routes",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['band_group_count']} "
        f"{package['accepted_groups']} {package['high_density_groups']} "
        f"{package['max_density']:.6f} {min_slack} "
        f"{package['max_qcrit_group']:.2f} {package['max_pcrit_group']:.2f} "
        f"{package['eta']:.6f} {package['layer_density']:.6f} "
        f"{package['witness_c']:.6f} {package['ceiling_c']:.6f} {route_counts}",
        flush=True,
    )
    print(
        "route sparse_route shape eps p density eta_slack tail_floor qcrit_single qcrit_group pcrit_group",
        flush=True,
    )
    for row in package["rows"]:
        shape = (
            f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-"
            f"{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        )
        print(
            f"{row['closure_route']} {row['sparse_route']} {shape} eps{row['epsilon']} "
            f"{row['p']} {row['density']:.6f} {row['eta_slack']:.6f} "
            f"{row['tail_floor']:.2f} {row['qcrit_single']:.2f} "
            f"{row['qcrit_group']:.2f} {row['pcrit_group']:.2f}",
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

    package = lowq_finite_threshold_package(
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
