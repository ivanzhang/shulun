#!/usr/bin/env python3
"""AlphaTail 尾素对端点相位键持久性账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_endpoint_crtdefect_audit import endpoint_side
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def parse_m_values(text: str) -> list[int]:
    """解析逗号分隔的点位长度列表。"""
    values = []
    for item in text.split(","):
        item = item.strip()
        if not item:
            continue
        values.append(int(item))
    if not values:
        raise ValueError("m-values 不能为空")
    return values


def endpoint_spike_records(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
) -> list[dict]:
    """把端点尖峰展开为带相位键的原子记录。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    records = []
    for spike in spike_rows(prime_bound, block, shift, point_count, alpha, num_primes, local_c, endpoint_theta):
        if spike["route"] != "EndpointSpike":
            continue
        side = endpoint_side(spike, domain_start, domain_stop, endpoint_theta)
        key = f"g{spike['gap']}:j{spike['j1']}-{spike['j2']}:u{spike['u']}:{side}"
        # 窗口标识保留 m，因为同一几何窗口下不同点位长度是不同证书层。
        window_id = f"{prime_bound}:{block}:{shift}:m{point_count}"
        records.append(
            {
                "key": key,
                "window_id": window_id,
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "m": point_count,
                "gap": spike["gap"],
                "j1": spike["j1"],
                "j2": spike["j2"],
                "u": spike["u"],
                "side": side,
                "actual": spike["actual"],
                "scale": spike["scale"],
                "required_c": spike["required_c"],
                "excess": max(0.0, spike["excess"]),
                "d_lower": spike["d_lower"],
                "d_upper": spike["d_upper"],
                "endpoint_ratio": spike["endpoint_ratio"],
            }
        )
    return records


def persistence_ledger(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    persistent_count: int,
    persistent_excess: float,
    top: int,
) -> dict:
    """聚合端点相位键并按持久/SAE 二分。"""
    records = []
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            records.extend(
                endpoint_spike_records(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    alpha,
                    num_primes,
                    local_c,
                    endpoint_theta,
                )
            )

    grouped: dict[str, dict] = {}
    for record in records:
        key = record["key"]
        if key not in grouped:
            grouped[key] = {
                "key": key,
                "occurrences": 0,
                "support_windows": set(),
                "p_values": set(),
                "total_actual": 0,
                "total_scale": 0.0,
                "total_excess": 0.0,
                "max_required_c": 0.0,
                "max_endpoint_ratio": 0.0,
                "records": [],
            }
        row = grouped[key]
        row["occurrences"] += 1
        row["support_windows"].add(record["window_id"])
        row["p_values"].add(record["p"])
        row["total_actual"] += record["actual"]
        row["total_scale"] += record["scale"]
        row["total_excess"] += record["excess"]
        row["max_required_c"] = max(row["max_required_c"], record["required_c"])
        row["max_endpoint_ratio"] = max(row["max_endpoint_ratio"], record["endpoint_ratio"])
        row["records"].append(record)

    key_rows = []
    for row in grouped.values():
        support_count = len(row["support_windows"])
        p_support_count = len(row["p_values"])
        persistent = support_count >= persistent_count or row["total_excess"] >= persistent_excess
        key_rows.append(
            {
                "key": row["key"],
                "occurrences": row["occurrences"],
                "support_count": support_count,
                "p_support_count": p_support_count,
                "total_actual": row["total_actual"],
                "total_scale": row["total_scale"],
                "total_excess": row["total_excess"],
                "max_required_c": row["max_required_c"],
                "max_endpoint_ratio": row["max_endpoint_ratio"],
                "route": "DirectedEndpointCRTDefect/PDEC" if persistent else "SAE",
                "windows": sorted(row["support_windows"])[:top],
            }
        )
    key_rows.sort(key=lambda item: (-item["support_count"], -item["total_excess"], item["key"]))

    persistent_keys = [row for row in key_rows if row["route"] != "SAE"]
    sae_keys = [row for row in key_rows if row["route"] == "SAE"]
    side_counts = defaultdict(int)
    for record in records:
        side_counts[record["side"]] += 1

    return {
        "selected": selected,
        "m_values": m_values,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "persistent_count": persistent_count,
        "persistent_excess": persistent_excess,
        "endpoint_spikes": len(records),
        "key_count": len(key_rows),
        "persistent_key_count": len(persistent_keys),
        "sae_key_count": len(sae_keys),
        "max_key_count": max((row["support_count"] for row in key_rows), default=0),
        "max_key_excess": max((row["total_excess"] for row in key_rows), default=0.0),
        "total_excess": sum(row["total_excess"] for row in key_rows),
        "side_counts": dict(sorted(side_counts.items())),
        "persistent_keys": persistent_keys[:top],
        "sae_keys": sae_keys[:top],
        "all_keys": key_rows,
    }


def print_table(row: dict) -> None:
    """输出持久性总表。"""
    side_text = ",".join(f"{side}:{count}" for side, count in row["side_counts"].items()) or "none"
    print(
        "endpoint_spikes key_count persistent_keys sae_keys max_key_count "
        "max_key_excess total_excess side_counts",
        flush=True,
    )
    print(
        f"{row['endpoint_spikes']} {row['key_count']} {row['persistent_key_count']} "
        f"{row['sae_key_count']} {row['max_key_count']} {row['max_key_excess']:.6f} "
        f"{row['total_excess']:.6f} {side_text}",
        flush=True,
    )
    print("route key support p_support excess max_req_C windows", flush=True)
    for item in row["persistent_keys"] + row["sae_keys"]:
        windows = ",".join(item["windows"]) or "none"
        print(
            f"{item['route']} {item['key']} {item['support_count']} "
            f"{item['p_support_count']} {item['total_excess']:.6f} "
            f"{item['max_required_c']:.6f} {windows}",
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
    parser.add_argument("--persistent-count", type=int, default=2)
    parser.add_argument("--persistent-excess", type=float, default=20.0)
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    row = persistence_ledger(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.persistent_count,
        args.persistent_excess,
        args.top,
    )
    if args.format == "json":
        print(json.dumps(row, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(row)
        return
    print(row, flush=True)


if __name__ == "__main__":
    main()
