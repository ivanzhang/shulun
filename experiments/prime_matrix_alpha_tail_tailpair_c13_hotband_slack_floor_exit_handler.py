#!/usr/bin/env python3
"""AlphaTail C13 热门带 SlackFloorExit 统一处理合同。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotband_slack_floor_exit_handler.py --p-list 5003,10007 --beta 0.95 --finite-p-cut 1000 --eta 0.04 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from prime_matrix_alpha_tail_additive_energy_audit import low_squarefree_block
from prime_matrix_alpha_tail_tailpair_c13_endpoint_persistence_contract import (
    endpoint_atom_records,
    grouped_contract,
)
from prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier import (
    hotband_exit_package,
    parse_p_list,
)
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values


def fmt(value: float | None) -> str:
    """格式化可空浮点。"""
    return "NA" if value is None else f"{value:.6f}"


def selected_text(rows: list[dict]) -> str:
    """把窗口行转为 selected 字符串。"""
    return ",".join(row["selected"] for row in rows)


def base_window_id(row: dict) -> str:
    """返回不含 m 层的窗口标识。"""
    return f"{row['p']}:{row['block']}:{row['shift']}"


def atom_base_window_id(atom: dict) -> str:
    """返回端点原子所属的基础窗口标识。"""
    return f"{atom['p']}:{atom['block']}:{atom['shift']}"


def additive_energy_rows(exit_rows: list[dict], alpha: float, sign: str, beta: float) -> dict[str, dict]:
    """为 SlackFloorExit 窗口记录 alpha-tail 热门差值能量承载。"""
    grouped: dict[tuple[int, int], list[dict]] = defaultdict(list)
    for row in exit_rows:
        grouped[(row["p"], row["block"])].append(row)

    energy_by_window = {}
    for (prime_bound, block), rows in grouped.items():
        values = low_squarefree_block(int(alpha * prime_bound), block, sign)
        diff_counts: dict[int, int] = defaultdict(int)
        for left in values:
            for right in values:
                diff = left - right
                if diff == 0:
                    continue
                diff_counts[diff] += 1
        max_count = max(diff_counts.values(), default=0)
        energy = sum(count * count for count in diff_counts.values())
        for row in rows:
            shift = row["shift"]
            oriented_count = diff_counts.get(shift, 0)
            mirror_count = diff_counts.get(-shift, 0)
            carrier_count = max(oriented_count, mirror_count)
            carrier_ratio = carrier_count / max_count if max_count else None
            energy_by_window[base_window_id(row)] = {
                "oriented_count": oriented_count,
                "mirror_count": mirror_count,
                "carrier_count": carrier_count,
                "max_count": max_count,
                "carrier_ratio": carrier_ratio,
                "energy": energy,
                "carrier_energy_share": (carrier_count * carrier_count / energy) if energy else None,
                "alpha_tail_carrier": bool(max_count and carrier_count >= beta * max_count),
            }
    return energy_by_window


def failure_route_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
    persistent_count: int,
    persistent_mass: int,
) -> tuple[dict, dict[str, dict]]:
    """把端点真实失败质量按基础窗口聚合，并沿用持久性合同的路由。"""
    endpoint_contract = grouped_contract(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        slack_cut,
        persistent_count,
        persistent_mass,
        1_000_000,
    )
    route_by_key = {row["key"]: row["route"] for row in endpoint_contract["rows"]}
    per_window: dict[str, dict] = defaultdict(
        lambda: {
            "failure_records": 0,
            "failure_mass": 0,
            "failure_keys": set(),
            "routes": set(),
        }
    )
    atoms = endpoint_atom_records(
        selected,
        m_values,
        alpha,
        num_primes,
        local_c,
        endpoint_theta,
        slack_cut,
    )
    for atom in atoms:
        if not atom["failure"]:
            continue
        window_id = atom_base_window_id(atom)
        row = per_window[window_id]
        row["failure_records"] += 1
        row["failure_mass"] += atom["failure_mass"]
        row["failure_keys"].add(atom["key"])
        row["routes"].add(route_by_key.get(atom["key"], "UnclassifiedFailure"))

    normalized = {}
    for window_id, row in per_window.items():
        routes = sorted(row["routes"])
        if not routes:
            handler_route = "EndpointNoFailure"
        elif routes == ["DirectedEndpointCRTDefect/PDEC"]:
            handler_route = "DirectedEndpointCRTDefect/PDEC"
        elif routes == ["SAE"]:
            handler_route = "SAE"
        elif "UnclassifiedFailure" in routes:
            handler_route = "UnclassifiedFailure"
        else:
            handler_route = "MixedPDECAndSAE"
        normalized[window_id] = {
            "failure_records": row["failure_records"],
            "failure_mass": row["failure_mass"],
            "failure_keys": sorted(row["failure_keys"]),
            "routes": routes,
            "handler_route": handler_route,
        }
    return endpoint_contract, normalized


def hotband_slack_floor_exit_handler_package(
    p_list: list[int],
    beta: float,
    m_values: list[int],
    finite_p_cut: int,
    eta: float,
    alpha: float,
    num_primes: int,
    endpoint_band_theta: float,
    sign: str,
    local_c: float,
    endpoint_theta: float,
    slack_cut: int,
    persistent_count: int,
    persistent_mass: int,
) -> dict:
    """返回热门带 SlackFloorExit 的统一处理包。"""
    classifier = hotband_exit_package(
        p_list,
        beta,
        m_values,
        finite_p_cut,
        eta,
        alpha,
        num_primes,
        endpoint_band_theta,
        sign,
    )
    exit_rows = [row for row in classifier["rows"] if row["exit_type"] == "SlackFloorExit"]
    selected = selected_text(exit_rows)
    energy_by_window = additive_energy_rows(exit_rows, alpha, sign, beta)
    if selected:
        endpoint_contract, failure_by_window = failure_route_rows(
            selected,
            m_values,
            alpha,
            num_primes,
            local_c,
            endpoint_theta,
            slack_cut,
            persistent_count,
            persistent_mass,
        )
    else:
        endpoint_contract = {
            "record_count": 0,
            "key_count": 0,
            "failure_record_count": 0,
            "failure_key_count": 0,
            "failure_mass": 0,
            "route_counts": {},
            "min_slack": None,
            "max_required_c": 0.0,
        }
        failure_by_window = {}

    rows = []
    route_counts: dict[str, int] = defaultdict(int)
    for exit_row in exit_rows:
        window_id = base_window_id(exit_row)
        failure = failure_by_window.get(
            window_id,
            {
                "failure_records": 0,
                "failure_mass": 0,
                "failure_keys": [],
                "routes": [],
                "handler_route": "EndpointNoFailure",
            },
        )
        energy = energy_by_window[window_id]
        # 无真实端点失败时，SlackFloorExit 只保留为热门能量观察压力。
        handler_route = failure["handler_route"]
        if handler_route == "EndpointNoFailure":
            handler_route = "AlphaTailHotband/EndpointNoFailure"
        route_counts[handler_route] += 1
        rows.append(
            {
                **exit_row,
                **energy,
                "failure_records": failure["failure_records"],
                "failure_mass": failure["failure_mass"],
                "failure_key_count": len(failure["failure_keys"]),
                "failure_keys": failure["failure_keys"],
                "failure_routes": failure["routes"],
                "handler_route": handler_route,
            }
        )

    total_failure_mass = endpoint_contract["failure_mass"]
    total = {
        "classifier_windows": classifier["total"]["windows"],
        "slack_floor_exit_windows": len(exit_rows),
        "selected_exits": selected,
        "alpha_tail_carrier_windows": sum(row["alpha_tail_carrier"] for row in rows),
        "all_alpha_tail_carrier": all(row["alpha_tail_carrier"] for row in rows),
        "endpoint_records": endpoint_contract["record_count"],
        "endpoint_keys": endpoint_contract["key_count"],
        "failure_records": endpoint_contract["failure_record_count"],
        "failure_keys": endpoint_contract["failure_key_count"],
        "failure_mass": total_failure_mass,
        "endpoint_route_counts": endpoint_contract["route_counts"],
        "handler_route_counts": dict(sorted(route_counts.items())),
        "min_endpoint_slack": endpoint_contract["min_slack"],
        "max_required_c": endpoint_contract["max_required_c"],
        "all_failure_mass_routed": "UnclassifiedFailure" not in route_counts,
        "pdec_or_sae_obligation": total_failure_mass > 0,
    }
    total["handler_contract_pass"] = (
        total["all_alpha_tail_carrier"] and total["all_failure_mass_routed"]
    )
    total["global_closed"] = total["handler_contract_pass"] and not total["pdec_or_sae_obligation"]
    total["status"] = (
        "slack_floor_exits_routed_with_pdec_or_sae_obligation"
        if total["pdec_or_sae_obligation"]
        else "slack_floor_exits_closed_by_endpoint_no_failure"
    )
    return {
        "p_list": p_list,
        "beta": beta,
        "m_values": m_values,
        "finite_p_cut": finite_p_cut,
        "eta": eta,
        "alpha": alpha,
        "num_primes": num_primes,
        "endpoint_band_theta": endpoint_band_theta,
        "sign": sign,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "slack_cut": slack_cut,
        "persistent_count": persistent_count,
        "persistent_mass": persistent_mass,
        "status": total["status"],
        "total": total,
        "rows": rows,
        "classifier": classifier,
        "endpoint_contract": endpoint_contract,
    }


def print_table(package: dict) -> None:
    """输出 SlackFloorExit 处理合同表。"""
    total = package["total"]
    min_slack = "NA" if total["min_endpoint_slack"] is None else str(total["min_endpoint_slack"])
    print(
        "scope beta classifier_windows slack_exits carriers all_carrier endpoint_records "
        "endpoint_keys failure_records failure_keys failure_mass min_slack max_required_C "
        "handler_routes endpoint_routes contract_pass global_closed status",
        flush=True,
    )
    print(
        f"slack-exit-handler {package['beta']:.6f} {total['classifier_windows']} "
        f"{total['slack_floor_exit_windows']} {total['alpha_tail_carrier_windows']} "
        f"{total['all_alpha_tail_carrier']} {total['endpoint_records']} "
        f"{total['endpoint_keys']} {total['failure_records']} {total['failure_keys']} "
        f"{total['failure_mass']} {min_slack} {total['max_required_c']:.6f} "
        f"{total['handler_route_counts']} {total['endpoint_route_counts']} "
        f"{total['handler_contract_pass']} {total['global_closed']} {total['status']}",
        flush=True,
    )
    print(
        "p block shift hot_count hot_ratio carrier_count carrier_ratio energy_share "
        "handler_route failure_records failure_mass failure_key_count res_margin source_margin",
        flush=True,
    )
    for row in package["rows"]:
        print(
            f"{row['p']} {row['block']} {row['shift']} {row['hot_count']} "
            f"{fmt(row['hot_ratio'])} {row['carrier_count']} {fmt(row['carrier_ratio'])} "
            f"{fmt(row['carrier_energy_share'])} {row['handler_route']} "
            f"{row['failure_records']} {row['failure_mass']} {row['failure_key_count']} "
            f"{fmt(row['res_margin'])} {fmt(row['source_margin'])}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", type=str, default="5003,10007")
    parser.add_argument("--beta", type=float, default=0.95)
    parser.add_argument("--m-values", type=str, default="4,5")
    parser.add_argument("--finite-p-cut", type=int, default=1000)
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--num-primes", type=int, default=8)
    parser.add_argument("--endpoint-band-theta", type=float, default=0.1)
    parser.add_argument("--sign", choices=("+", "-"), default="-")
    parser.add_argument("--local-c", type=float, default=1.3)
    parser.add_argument("--endpoint-theta", type=float, default=0.1)
    parser.add_argument("--slack-cut", type=int, default=40)
    parser.add_argument("--persistent-count", type=int, default=2)
    parser.add_argument("--persistent-mass", type=int, default=2)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = hotband_slack_floor_exit_handler_package(
        parse_p_list(args.p_list),
        args.beta,
        parse_m_values(args.m_values),
        args.finite_p_cut,
        args.eta,
        args.alpha,
        args.num_primes,
        args.endpoint_band_theta,
        args.sign,
        args.local_c,
        args.endpoint_theta,
        args.slack_cut,
        args.persistent_count,
        args.persistent_mass,
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
