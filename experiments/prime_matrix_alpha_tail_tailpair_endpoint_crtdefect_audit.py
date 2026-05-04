#!/usr/bin/env python3
"""AlphaTail 尾素对端点尖峰到 CRTDefect 的相位键审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_crtdefect_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def endpoint_side(spike: dict, domain_start: int, domain_stop: int, theta: float) -> str:
    """判断端点尖峰贴左端、右端或双端。"""
    domain_length = max(1, domain_stop - domain_start + 1)
    left = spike["d_lower"] - domain_start <= theta * domain_length
    right = domain_stop - spike["d_upper"] <= theta * domain_length
    if left and right:
        return "B"
    if left:
        return "L"
    if right:
        return "R"
    return "I"


def crtdefect_rows(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> dict:
    """聚合端点尖峰相位键。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    spikes = spike_rows(prime_bound, block, shift, point_count, alpha, num_primes, local_c, endpoint_theta)
    endpoint_spikes = [spike for spike in spikes if spike["route"] == "EndpointSpike"]
    grouped: dict[str, dict] = {}
    side_counts = defaultdict(int)
    for spike in endpoint_spikes:
        side = endpoint_side(spike, domain_start, domain_stop, endpoint_theta)
        side_counts[side] += 1
        key = f"g{spike['gap']}:j{spike['j1']}-{spike['j2']}:u{spike['u']}:{side}"
        if key not in grouped:
            grouped[key] = {
                "key": key,
                "gap": spike["gap"],
                "j1": spike["j1"],
                "j2": spike["j2"],
                "u": spike["u"],
                "side": side,
                "count": 0,
                "actual": 0,
                "scale": 0.0,
                "excess": 0.0,
                "max_required_c": 0.0,
            }
        row = grouped[key]
        row["count"] += 1
        row["actual"] += spike["actual"]
        row["scale"] += spike["scale"]
        row["excess"] += max(0.0, spike["excess"])
        row["max_required_c"] = max(row["max_required_c"], spike["required_c"])
    top_keys = sorted(grouped.values(), key=lambda item: (-item["excess"], -item["actual"], item["key"]))[:8]
    return {
        "p": prime_bound,
        "block": block,
        "shift": shift,
        "m": point_count,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "endpoint_spike_count": len(endpoint_spikes),
        "phase_key_count": len(grouped),
        "total_excess": sum(item["excess"] for item in grouped.values()),
        "side_counts": dict(sorted(side_counts.items())),
        "top_keys": top_keys,
    }


def print_table(rows: list[dict]) -> None:
    """输出端点 CRTDefect 相位键表。"""
    print(
        "p block shift m endpoint_spikes phase_keys total_excess side_counts top_keys",
        flush=True,
    )
    for row in rows:
        side_text = ",".join(f"{side}:{count}" for side, count in row["side_counts"].items()) or "none"
        top_text = ",".join(
            f"{item['key']}:{item['actual']}/{item['scale']:.3f}/{item['excess']:.3f}"
            for item in row["top_keys"][:5]
        ) or "none"
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['endpoint_spike_count']} {row['phase_key_count']} "
            f"{row['total_excess']:.6f} {side_text} {top_text}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--local-c", type=float, default=1.2)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    rows = []
    for prime_bound, block, shift in parse_selected(args.selected):
        for point_count in (4, 5):
            rows.append(
                crtdefect_rows(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    args.alpha,
                    args.num_primes,
                    args.local_c,
                    args.endpoint_theta,
                )
            )
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(rows)
        return
    for row in rows:
        print(row, flush=True)


if __name__ == "__main__":
    main()
