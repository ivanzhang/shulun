#!/usr/bin/env python3
"""AlphaTail 尾素对局部常数灵敏度审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_local_constant_sensitivity.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-candidates '1.2,1.25,1.254,1.3,1.5' --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import brun_row
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_local_spike_audit import spike_rows


def parse_float_list(text: str) -> list[float]:
    """解析逗号分隔浮点列表。"""
    values = []
    for item in text.split(","):
        item = item.strip()
        if item:
            values.append(float(item))
    if not values:
        raise ValueError("local-candidates 不能为空")
    return values


def sensitivity_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    endpoint_theta: float,
    global_c: float,
    local_candidates: list[float],
) -> dict:
    """计算局部常数候选对尾素对尖峰的吸收情况。"""
    rows = []
    candidate_summary = {
        candidate: {
            "candidate": candidate,
            "row_pass_count": 0,
            "row_count": 0,
            "spike_count": 0,
            "endpoint_count": 0,
            "interior_count": 0,
        }
        for candidate in local_candidates
    }
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            brun = brun_row(prime_bound, block, shift, point_count, alpha, num_primes)
            row = {
                "p": prime_bound,
                "block": block,
                "shift": shift,
                "m": point_count,
                "required_c_bs": brun["required_c_bs"],
                "max_local_required_c": brun["max_local_required_c"],
                "global_pass": brun["required_c_bs"] <= global_c,
                "candidate_results": [],
            }
            for candidate in local_candidates:
                spikes = spike_rows(
                    prime_bound,
                    block,
                    shift,
                    point_count,
                    alpha,
                    num_primes,
                    candidate,
                    endpoint_theta,
                )
                endpoint_count = sum(1 for spike in spikes if spike["route"] == "EndpointSpike")
                interior_count = len(spikes) - endpoint_count
                passed = not spikes
                candidate_summary[candidate]["row_count"] += 1
                candidate_summary[candidate]["row_pass_count"] += 1 if passed else 0
                candidate_summary[candidate]["spike_count"] += len(spikes)
                candidate_summary[candidate]["endpoint_count"] += endpoint_count
                candidate_summary[candidate]["interior_count"] += interior_count
                row["candidate_results"].append(
                    {
                        "candidate": candidate,
                        "passed": passed,
                        "spike_count": len(spikes),
                        "endpoint_count": endpoint_count,
                        "interior_count": interior_count,
                    }
                )
            rows.append(row)
    max_local_required = max((row["max_local_required_c"] for row in rows), default=0.0)
    max_required_c_bs = max((row["required_c_bs"] for row in rows if row["required_c_bs"] is not None), default=0.0)
    return {
        "selected": selected,
        "global_c": global_c,
        "endpoint_theta": endpoint_theta,
        "row_count": len(rows),
        "max_local_required_c": max_local_required,
        "max_required_c_bs": max_required_c_bs,
        "global_pass_all": max_required_c_bs <= global_c,
        "candidate_summary": list(candidate_summary.values()),
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出局部常数灵敏度表。"""
    print(
        f"rows {package['row_count']} global_C {package['global_c']:.6f} "
        f"max_required_C_BS {package['max_required_c_bs']:.6f} "
        f"max_local_required_C {package['max_local_required_c']:.6f} "
        f"global_pass_all {package['global_pass_all']}",
        flush=True,
    )
    print("candidate_summary", flush=True)
    print("candidate row_pass row_count spikes endpoint interior", flush=True)
    for item in package["candidate_summary"]:
        print(
            f"{item['candidate']:.6f} {item['row_pass_count']} {item['row_count']} "
            f"{item['spike_count']} {item['endpoint_count']} {item['interior_count']}",
            flush=True,
        )
    print("rows", flush=True)
    print("p block shift m req_C_BS max_local_C global_pass candidates", flush=True)
    for row in package["rows"]:
        candidates = ",".join(
            f"{item['candidate']:.3f}:{item['spike_count']}/{item['endpoint_count']}/{item['interior_count']}"
            for item in row["candidate_results"]
        )
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['m']} "
            f"{row['required_c_bs']:.6f} {row['max_local_required_c']:.6f} "
            f"{row['global_pass']} {candidates}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-36,5003:8192:-36")
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--global-c", type=float, default=1.5)
    parser.add_argument("--local-candidates", type=str, default="1.2,1.25,1.254,1.3,1.5")
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = sensitivity_rows(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.endpoint_theta,
        args.global_c,
        parse_float_list(args.local_candidates),
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
