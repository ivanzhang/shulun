#!/usr/bin/env python3
"""AlphaTail 端点持久键的 PDEC 输入包账本。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_pdec_input_ledger.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
"""

from __future__ import annotations

import argparse
import json

from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import (
    parse_m_values,
    persistence_ledger,
)


def pdec_input_package(
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
    """把持久端点键转换为 PDEC 输入行，并保留 SAE 行。"""
    ledger = persistence_ledger(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        persistent_count,
        persistent_excess,
        top,
    )
    persistent_rows = []
    sae_rows = []
    for item in ledger["all_keys"]:
        base_row = {
            "key": item["key"],
            "support_count": item["support_count"],
            "p_support_count": item["p_support_count"],
            "total_excess": item["total_excess"],
            "max_required_c": item["max_required_c"],
            "windows": item["windows"],
        }
        if item["route"] == "SAE":
            sae_rows.append(
                {
                    **base_row,
                    "exit": "FiniteSAE",
                    "acceptance_obligation": "submit finite SAE row or prove summable SAE family",
                }
            )
            continue
        persistent_rows.append(
            {
                **base_row,
                "exit": "DirectedEndpointCRTDefect/PDEC",
                "bad_window_set": item["windows"],
                "phase_map": "endpoint_phase_key:(g,j1,j2,u,side)",
                "lower_mass_source": "sum positive local Brun/Selberg excess over this key",
                "pdec_lower_input": item["total_excess"],
                "missing_upper_bound": "prove U_CRT(key) < L_PDEC(key) using admissible endpoint constraints",
                "certificate_status": "PDEC_INPUT_READY_THRESHOLD_OPEN",
            }
        )
    return {
        "source_ledger": {
            "selected": ledger["selected"],
            "m_values": ledger["m_values"],
            "local_c": ledger["local_c"],
            "endpoint_theta": ledger["endpoint_theta"],
            "persistent_count": ledger["persistent_count"],
            "persistent_excess": ledger["persistent_excess"],
        },
        "summary": {
            "endpoint_spikes": ledger["endpoint_spikes"],
            "key_count": ledger["key_count"],
            "persistent_key_count": len(persistent_rows),
            "sae_key_count": len(sae_rows),
            "persistent_total_excess": sum(row["total_excess"] for row in persistent_rows),
            "sae_total_excess": sum(row["total_excess"] for row in sae_rows),
        },
        "persistent_pdec_inputs": persistent_rows[:top],
        "sae_inputs": sae_rows[:top],
    }


def print_table(package: dict) -> None:
    """输出 PDEC 输入包简表。"""
    summary = package["summary"]
    print(
        "endpoint_spikes key_count persistent_keys sae_keys "
        "persistent_excess sae_excess",
        flush=True,
    )
    print(
        f"{summary['endpoint_spikes']} {summary['key_count']} "
        f"{summary['persistent_key_count']} {summary['sae_key_count']} "
        f"{summary['persistent_total_excess']:.6f} {summary['sae_total_excess']:.6f}",
        flush=True,
    )
    print("exit key support p_support excess status_or_obligation", flush=True)
    for row in package["persistent_pdec_inputs"]:
        print(
            f"{row['exit']} {row['key']} {row['support_count']} "
            f"{row['p_support_count']} {row['total_excess']:.6f} "
            f"{row['certificate_status']}",
            flush=True,
        )
    for row in package["sae_inputs"]:
        print(
            f"{row['exit']} {row['key']} {row['support_count']} "
            f"{row['p_support_count']} {row['total_excess']:.6f} "
            f"{row['acceptance_obligation']}",
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
    parser.add_argument("--top", type=int, default=100)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = pdec_input_package(
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
        print(json.dumps(package, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print_table(package)
        return
    print(package, flush=True)


if __name__ == "__main__":
    main()
