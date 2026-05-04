#!/usr/bin/env python3
"""AlphaTail C13 SparseSAE 的确定性 envelope 上界审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_deterministic_envelope_bound.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --eta 0.04 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope import depth_band_package
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def deterministic_slots_for_group(
    block: int,
    shift: int,
    m_values: list[int],
    u_value: int,
    epsilon: int,
    endpoint_band_theta: float,
) -> int:
    """返回只依赖端点带宽公式的 group 槽数上界。"""
    max_domain_length = 0
    for point_count in m_values:
        domain_start, domain_stop = domain_bounds(block, shift, point_count)
        max_domain_length = max(max_domain_length, max(1, domain_stop - domain_start + 1))
    limit = int(endpoint_band_theta * max_domain_length)
    if limit < epsilon:
        return 0
    return (limit - epsilon) // u_value + 1


def deterministic_envelope_package(
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
    """返回确定性 envelope 上界包。"""
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
    layer_count_bound = max(1, len(m_values))
    rows = []
    by_window: defaultdict[tuple[int, int, int], dict] = defaultdict(
        lambda: {"groups": 0, "observed_envelope": 0, "deterministic_envelope": 0}
    )
    for row in envelope["rows"]:
        prime_bound, block, shift = row["band_key"][:3]
        u_value = row["shape_key"][3]
        epsilon = row["epsilon"]
        deterministic_slots = deterministic_slots_for_group(
            block,
            shift,
            m_values,
            u_value,
            epsilon,
            endpoint_band_theta,
        )
        item = {
            "p": prime_bound,
            "block": block,
            "shift": shift,
            "shape_key": row["shape_key"],
            "epsilon": epsilon,
            "observed_slots": row["observed_slots"],
            "observed_envelope": row["envelope_slots"],
            "deterministic_envelope": deterministic_slots,
            "deterministic_slack": deterministic_slots - row["envelope_slots"],
        }
        rows.append(item)
        key = (prime_bound, block, shift)
        by_window[key]["groups"] += 1
        by_window[key]["observed_envelope"] += row["envelope_slots"]
        by_window[key]["deterministic_envelope"] += deterministic_slots
    rows.sort(key=lambda item: (-item["deterministic_slack"], -item["observed_envelope"], item["p"], item["shape_key"]))
    window_rows = []
    for (prime_bound, block, shift), row in sorted(by_window.items()):
        window_rows.append(
            {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                **row,
                "capacity": layer_count_bound * eta * row["deterministic_envelope"],
            }
        )
    total_deterministic = sum(row["deterministic_envelope"] for row in rows)
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "eta": eta,
        "endpoint_band_theta": endpoint_band_theta,
        "layer_count_bound": layer_count_bound,
        "raw_atoms": envelope["raw_atoms"],
        "formal_atoms": envelope["formal_atoms"],
        "formal_moving_atoms": envelope["formal_moving_atoms"],
        "band_group_count": envelope["band_group_count"],
        "observed_envelope_slots": envelope["envelope_slots"],
        "deterministic_envelope_slots": total_deterministic,
        "deterministic_slack": total_deterministic - envelope["envelope_slots"],
        "deterministic_capacity": layer_count_bound * eta * total_deterministic,
        "moving_over_deterministic_capacity": (
            envelope["formal_moving_atoms"] / (layer_count_bound * eta * total_deterministic)
            if total_deterministic
            else None
        ),
        "window_rows": window_rows,
        "rows": rows[:top],
    }


def print_table(package: dict) -> None:
    """输出确定性 envelope 上界表。"""
    ratio = (
        "NA"
        if package["moving_over_deterministic_capacity"] is None
        else f"{package['moving_over_deterministic_capacity']:.6f}"
    )
    print(
        "raw formal moving groups observed_env deterministic_env slack deterministic_capacity "
        "moving_over_capacity eta layers band_theta",
        flush=True,
    )
    print(
        f"{package['raw_atoms']} {package['formal_atoms']} {package['formal_moving_atoms']} "
        f"{package['band_group_count']} {package['observed_envelope_slots']} "
        f"{package['deterministic_envelope_slots']} {package['deterministic_slack']} "
        f"{package['deterministic_capacity']:.6f} {ratio} "
        f"{package['eta']:.6f} {package['layer_count_bound']} {package['endpoint_band_theta']:.6f}",
        flush=True,
    )
    print("windows p block shift groups observed_env deterministic_env capacity", flush=True)
    for row in package["window_rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['groups']} "
            f"{row['observed_envelope']} {row['deterministic_envelope']} {row['capacity']:.6f}",
            flush=True,
        )
    print("top_groups shape eps p observed_env deterministic_env slack", flush=True)
    for row in package["rows"]:
        shape = (
            f"g{row['shape_key'][0]}:j{row['shape_key'][1]}-"
            f"{row['shape_key'][2]}:u{row['shape_key'][3]}:{row['shape_key'][4]}"
        )
        print(
            f"{shape} eps{row['epsilon']} {row['p']} "
            f"{row['observed_envelope']} {row['deterministic_envelope']} {row['deterministic_slack']}",
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
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = deterministic_envelope_package(
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
