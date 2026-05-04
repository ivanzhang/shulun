#!/usr/bin/env python3
"""AlphaTail C13 候选 group 数与 u 分布上界审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_tailpair_c13_group_u_distribution.py --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' --num-primes 8 --local-c 1.2 --eta 0.04 --slack-cut 40 --format table
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from prime_matrix_alpha_tail_pair_crtdefect_audit import parse_selected
from prime_matrix_alpha_tail_tail_overlap_rankin_audit import domain_bounds
from prime_matrix_alpha_tail_tailpair_brun_constant_audit import interval_for_pattern
from prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit import interval_records
from prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit import parse_m_values
from prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit import exact_gap_coefficients


def endpoint_side_from_bounds(d_lower: int, d_upper: int, domain_start: int, domain_stop: int) -> str:
    """返回责任区间更靠近的端点方向。"""
    left_distance = d_lower - domain_start
    right_distance = domain_stop - d_upper
    return "left" if left_distance <= right_distance else "right"


def endpoint_epsilon(
    side: str,
    d_lower: int,
    d_upper: int,
    domain_start: int,
    domain_stop: int,
    u_value: int,
) -> int:
    """返回端点深度模 u 的残差。"""
    depth = d_lower - domain_start if side == "left" else domain_stop - d_upper
    return depth % u_value


def deterministic_slots(
    block: int,
    shift: int,
    m_values: list[int],
    u_value: int,
    epsilon: int,
    endpoint_band_theta: float,
) -> int:
    """返回确定性端点带 envelope 槽数。"""
    max_domain_length = 0
    for point_count in m_values:
        domain_start, domain_stop = domain_bounds(block, shift, point_count)
        max_domain_length = max(max_domain_length, max(1, domain_stop - domain_start + 1))
    limit = int(endpoint_band_theta * max_domain_length)
    if limit < epsilon:
        return 0
    return (limit - epsilon) // u_value + 1


def geometric_records(
    prime_bound: int,
    block: int,
    shift: int,
    point_count: int,
) -> list[dict]:
    """返回不依赖实际素对计数的几何候选记录。"""
    domain_start, domain_stop = domain_bounds(block, shift, point_count)
    coefficients = exact_gap_coefficients(shift, point_count)
    rows = []
    for index_a in range(point_count):
        for index_b in range(point_count):
            if index_a == index_b:
                continue
            base = -(index_a - index_b) * shift
            if base <= 0:
                continue
            for gap in coefficients:
                interval = interval_for_pattern(domain_start, domain_stop, shift, index_a, index_b, gap)
                if interval is None or base % gap != 0:
                    continue
                lower, upper = interval
                u_value = base // gap
                d_lower = lower * u_value - index_a * shift
                d_upper = upper * u_value - index_a * shift
                rows.append(
                    {
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "m": point_count,
                        "gap": gap,
                        "j1": index_a,
                        "j2": index_b,
                        "u": u_value,
                        "q_lower": lower,
                        "q_upper": upper,
                        "d_lower": d_lower,
                        "d_upper": d_upper,
                        "actual": None,
                        "integer_slack": None,
                        "route": "GeometricCandidate",
                    }
                )
    return rows


def include_record(record: dict, mode: str, slack_cut: int) -> bool:
    """判断记录是否进入指定候选宇宙。"""
    if record["u"] is None or record["d_lower"] is None or record["d_upper"] is None:
        return False
    if record["gap"] % 2 == 1:
        return False
    if mode == "geometric":
        return True
    if mode == "positive":
        return record["actual"] > 0
    if mode == "narrow":
        return record["actual"] > 0 and record["integer_slack"] <= slack_cut
    if mode == "failure":
        return record["route"] == "C13Failure"
    raise ValueError(f"未知 mode: {mode}")


def collect_mode_rows(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
    eta: float,
    mode: str,
) -> dict:
    """收集单个候选宇宙的 group 与 u 分布。"""
    groups: dict[tuple, dict] = {}
    record_count = 0
    by_window: defaultdict[tuple[int, int, int], dict] = defaultdict(
        lambda: {"records": 0, "groups": 0, "deterministic_env": 0}
    )
    for prime_bound, block, shift in parse_selected(selected):
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            records = (
                geometric_records(prime_bound, block, shift, point_count)
                if mode == "geometric"
                else interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c)
            )
            for record in records:
                if not include_record(record, mode, slack_cut):
                    continue
                if record["u"] > endpoint_theta * domain_length:
                    continue
                side = endpoint_side_from_bounds(
                    record["d_lower"],
                    record["d_upper"],
                    domain_start,
                    domain_stop,
                )
                epsilon = endpoint_epsilon(
                    side,
                    record["d_lower"],
                    record["d_upper"],
                    domain_start,
                    domain_stop,
                    record["u"],
                )
                shape_key = (record["gap"], record["j1"], record["j2"], record["u"], side)
                group_key = (prime_bound, block, shift, shape_key, epsilon)
                record_count += 1
                if group_key not in groups:
                    slots = deterministic_slots(
                        block,
                        shift,
                        m_values,
                        record["u"],
                        epsilon,
                        endpoint_band_theta,
                    )
                    groups[group_key] = {
                        "p": prime_bound,
                        "block": block,
                        "shift": shift,
                        "shape_key": shape_key,
                        "epsilon": epsilon,
                        "u": record["u"],
                        "slots": slots,
                    }

    u_counter: Counter[int] = Counter()
    u_slots: Counter[int] = Counter()
    for group in groups.values():
        u_counter[group["u"]] += 1
        u_slots[group["u"]] += group["slots"]
        key = (group["p"], group["block"], group["shift"])
        by_window[key]["groups"] += 1
        by_window[key]["deterministic_env"] += group["slots"]
    # records 需要单独再算入窗口，避免新 group 去重影响记录数
    for prime_bound, block, shift in parse_selected(selected):
        window_records = 0
        for point_count in m_values:
            domain_start, domain_stop = domain_bounds(block, shift, point_count)
            domain_length = max(1, domain_stop - domain_start + 1)
            records = (
                geometric_records(prime_bound, block, shift, point_count)
                if mode == "geometric"
                else interval_records(prime_bound, block, shift, point_count, alpha, num_primes, local_c)
            )
            for record in records:
                if include_record(record, mode, slack_cut) and record["u"] <= endpoint_theta * domain_length:
                    window_records += 1
        by_window[(prime_bound, block, shift)]["records"] = window_records

    deterministic_env = sum(group["slots"] for group in groups.values())
    return {
        "mode": mode,
        "record_count": record_count,
        "group_count": len(groups),
        "deterministic_env": deterministic_env,
        "deterministic_capacity": len(m_values) * eta * deterministic_env,
        "u_summary": [
            {"u": u_value, "groups": u_counter[u_value], "slots": u_slots[u_value]}
            for u_value, _ in u_counter.most_common()
        ],
        "window_rows": [
            {
                "p": key[0],
                "block": key[1],
                "shift": key[2],
                **value,
                "capacity": len(m_values) * eta * value["deterministic_env"],
            }
            for key, value in sorted(by_window.items())
        ],
    }


def group_u_distribution_package(
    selected: str,
    m_values: list[int],
    alpha: float,
    num_primes: int,
    local_c: float,
    endpoint_theta: float,
    endpoint_band_theta: float,
    slack_cut: int,
    eta: float,
) -> dict:
    """返回四个候选宇宙的 group/u 分布包。"""
    modes = ["geometric", "positive", "narrow", "failure"]
    rows = [
        collect_mode_rows(
            selected,
            m_values,
            alpha,
            num_primes,
            local_c,
            endpoint_theta,
            endpoint_band_theta,
            slack_cut,
            eta,
            mode,
        )
        for mode in modes
    ]
    return {
        "selected": selected,
        "m_values": m_values,
        "alpha": alpha,
        "num_primes": num_primes,
        "local_c": local_c,
        "endpoint_theta": endpoint_theta,
        "endpoint_band_theta": endpoint_band_theta,
        "slack_cut": slack_cut,
        "eta": eta,
        "rows": rows,
    }


def print_table(package: dict) -> None:
    """输出 group/u 分布表。"""
    print("mode records groups deterministic_env capacity top_u", flush=True)
    for row in package["rows"]:
        top_u = ",".join(
            f"u{item['u']}:{item['groups']}/{item['slots']}"
            for item in row["u_summary"][:8]
        )
        print(
            f"{row['mode']} {row['record_count']} {row['group_count']} "
            f"{row['deterministic_env']} {row['deterministic_capacity']:.6f} {top_u}",
            flush=True,
        )
    print("windows mode p block shift records groups deterministic_env capacity", flush=True)
    for row in package["rows"]:
        for window in row["window_rows"]:
            print(
                f"{row['mode']} {window['p']} {window['block']} {window['shift']} "
                f"{window['records']} {window['groups']} {window['deterministic_env']} "
                f"{window['capacity']:.6f}",
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
    parser.add_argument("--eta", type=float, default=0.04)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    package = group_u_distribution_package(
        args.selected,
        parse_m_values(args.m_values),
        args.alpha,
        args.num_primes,
        args.local_c,
        args.endpoint_theta,
        args.endpoint_band_theta,
        args.slack_cut,
        args.eta,
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
