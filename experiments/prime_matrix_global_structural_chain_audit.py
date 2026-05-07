#!/usr/bin/env python3
"""审计行命题全局结构闭合链的最小反例路由账本。

用法示例：
  python3 experiments/prime_matrix_global_structural_chain_audit.py \
    --p-list 5003,10007,20011,50021,100003,200003 \
    --alpha 0.43 \
    --y-factor 4 \
    --tail-factor 10 \
    --top-n 16 \
    --out-prefix docs/global_structural_chain_audit_20260506

目标：
  不固定全局付款常数，而对每个第 P 列锚点风险行计算本行自归一化允许量

      C_allow(P,y) = (S_Y(P,y)-T_{<=BY}(P,y)) / Model_{>BY}(P,y)

  并把该行路由到：
    capacity_closed / tail_self_normalized_closed /
    cofactor_anchor_candidate / pdec_candidate / columncrt_candidate /
    descent_candidate。
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return flags


def prime_prefix(flags: bytearray) -> list[int]:
    """返回 pi(n) 前缀表。"""
    prefix = [0] * len(flags)
    total = 0
    for idx, flag in enumerate(flags):
        if flag:
            total += 1
        prefix[idx] = total
    return prefix


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def ceil_div(a: int, b: int) -> int:
    """整数上取整。"""
    return -(-a // b)


def mark_low_skeleton(p: int, y: int, low_primes: list[int]) -> bytearray:
    """标记 Py-d 避开低素的动态骨架，索引 d。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    anchor = p * y
    for q in low_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def rough_flags(limit: int, low_primes: list[int]) -> bytearray:
    """预计算 m 是否避开所有低素。"""
    rough = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        rough[0] = 0
    for q in low_primes:
        if q > limit:
            break
        rough[q : limit + 1 : q] = b"\x00" * (((limit - q) // q) + 1)
    return rough


def row_capacity(
    p: int,
    y: int,
    low_primes: list[int],
    high_primes: list[int],
) -> dict:
    """计算单行动态骨架和高素一阶命中。"""
    alive = mark_low_skeleton(p, y, low_primes)
    skeleton = sum(alive)
    anchor = p * y
    total_hits = 0
    covered = bytearray(p)
    for q in high_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        for d in range(start, p, q):
            if not alive[d]:
                continue
            total_hits += 1
            covered[d] = 1
    covered_count = sum(1 for d in range(1, p) if covered[d])
    margin = skeleton - total_hits
    return {
        "y": y,
        "x": y - 1,
        "skeleton_count": skeleton,
        "total_high_hits": total_hits,
        "capacity_margin": margin,
        "capacity_margin_over_sqrt": margin / math.sqrt(skeleton)
        if skeleton
        else 0.0,
        "hit_ratio": total_hits / skeleton if skeleton else 0.0,
        "covered_count": covered_count,
        "prime_holes": skeleton - covered_count,
    }


def ratio_bin(m: int, y: int) -> str:
    """把互补因子 m 按 m/y 的二进尺度分桶。"""
    if y <= 0:
        return "undefined"
    ratio = m / y
    if ratio < 1:
        return "<1y"
    exponent = int(math.floor(math.log(ratio, 2))) if ratio > 0 else 0
    left = 2**exponent
    right = 2 ** (exponent + 1)
    return f"[{left}y,{right}y)"


def top_counter_share(counter: Counter[int], total: int) -> dict:
    """返回计数器最大类及份额。"""
    if not counter or total <= 0:
        return {"value": None, "count": 0, "share": 0.0}
    value, count = counter.most_common(1)[0]
    return {"value": value, "count": count, "share": count / total}


def tail_ledger(
    p: int,
    y: int,
    cutoff: int,
    tail_factor: float,
    rough: bytearray,
    prefix: list[int],
    primes: list[int],
) -> dict:
    """计算远尾互补因子账本与低模相位诊断。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    actual = 0
    model = 0.0
    interval_len_total = 0
    active_m_count = 0
    m_rows = []
    band_totals: dict[str, dict[str, float]] = defaultdict(
        lambda: {"actual": 0, "model": 0.0, "interval_len": 0, "active_m": 0}
    )
    q_mod30: Counter[int] = Counter()
    d_mod30: Counter[int] = Counter()

    for m in range(1, m_max + 1):
        if m >= len(rough) or not rough[m]:
            continue
        q_min = max(tail_q_min, ceil_div(anchor - (p - 1), m))
        q_max = min(p - 1, (anchor - 1) // m)
        if q_min > q_max:
            continue

        interval_len = q_max - q_min + 1
        count = prefix[q_max] - (prefix[q_min - 1] if q_min > 0 else 0)
        local_model = interval_len / math.log(max(q_min, 3))
        local_excess = count - local_model
        band = ratio_bin(m, y)

        interval_len_total += interval_len
        actual += count
        model += local_model
        band_totals[band]["actual"] += count
        band_totals[band]["model"] += local_model
        band_totals[band]["interval_len"] += interval_len
        if count:
            active_m_count += 1
            band_totals[band]["active_m"] += 1
            m_rows.append(
                {
                    "m": m,
                    "m_over_y": m / y if y else 0.0,
                    "q_min": q_min,
                    "q_max": q_max,
                    "interval_len": interval_len,
                    "actual": count,
                    "model": local_model,
                    "excess": local_excess,
                    "actual_over_model": count / local_model
                    if local_model
                    else 0.0,
                    "band": band,
                }
            )

            lo = bisect.bisect_left(primes, q_min)
            hi = bisect.bisect_right(primes, q_max)
            for q in primes[lo:hi]:
                d = anchor - q * m
                q_mod30[q % 30] += 1
                d_mod30[d % 30] += 1

    top_by_hits = sorted(m_rows, key=lambda row: -row["actual"])[:8]
    top_by_excess = sorted(m_rows, key=lambda row: -row["excess"])[:8]
    band_rows = []
    for band, values in band_totals.items():
        band_actual = int(values["actual"])
        band_model = float(values["model"])
        band_rows.append(
            {
                "band": band,
                "actual": band_actual,
                "model": band_model,
                "excess": band_actual - band_model,
                "actual_share": band_actual / actual if actual else 0.0,
                "actual_over_model": band_actual / band_model
                if band_model
                else 0.0,
                "interval_len": int(values["interval_len"]),
                "active_m": int(values["active_m"]),
            }
        )
    band_rows.sort(key=lambda row: -row["actual"])

    max_m_hits = top_by_hits[0]["actual"] if top_by_hits else 0
    max_band_share = band_rows[0]["actual_share"] if band_rows else 0.0
    positive_m_excess_sum = sum(max(0.0, row["excess"]) for row in m_rows)
    positive_band_excess_sum = sum(max(0.0, row["excess"]) for row in band_rows)
    return {
        "tail_q_min": tail_q_min,
        "m_max": m_max,
        "active_m_count": active_m_count,
        "interval_len_total": interval_len_total,
        "actual_tail_hits": actual,
        "model_tail": model,
        "actual_over_model": actual / model if model else 0.0,
        "model_excess": actual - model,
        "positive_m_excess_sum": positive_m_excess_sum,
        "positive_band_excess_sum": positive_band_excess_sum,
        "max_m_share": max_m_hits / actual if actual else 0.0,
        "max_band_share": max_band_share,
        "top_m_by_hits": top_by_hits,
        "top_m_by_excess": top_by_excess,
        "top_bands": band_rows[:8],
        "q_mod30_peak": top_counter_share(q_mod30, actual),
        "d_mod30_peak": top_counter_share(d_mod30, actual),
    }


def route_row(row: dict, params: dict) -> dict:
    """按全局结构链给单行登记路由。"""
    tail = row["tail"]
    non_tail = row["non_tail_hits"]
    allowable = row["allowable_tail_hits"]
    model = tail["model_tail"]
    c_allow = row["c_allow"]
    self_margin = allowable - tail["actual_tail_hits"]
    required_tail_excess = (c_allow - 1.0) * model
    tail_excess = tail["model_excess"]

    if row["capacity_margin"] > 0:
        route = "capacity_closed"
        candidates = ["strict_prime_hole"]
    elif model > 0 and tail["actual_tail_hits"] < c_allow * model:
        route = "tail_self_normalized_closed"
        candidates = ["self_normalized_capacity"]
    else:
        route = "named_exit_candidate"
        candidates = []
        if tail["max_m_share"] >= params["m_anchor_share"]:
            candidates.append("cofactor_anchor_candidate")
        if tail["max_band_share"] >= params["band_anchor_share"]:
            candidates.append("cofactor_band_candidate")
        if tail["d_mod30_peak"]["share"] >= params["phase_share"]:
            candidates.append("pdec_candidate")
        if tail["q_mod30_peak"]["share"] >= params["phase_share"]:
            candidates.append("columncrt_candidate")
        candidates.append("descent_candidate")

    risk_flags = []
    if row["hit_ratio"] >= params["near_hit_ratio"]:
        risk_flags.append("near_capacity_boundary")
    if tail["actual_over_model"] >= 1.0:
        risk_flags.append("tail_positive_excess")
    if tail["max_m_share"] >= params["m_anchor_share"]:
        risk_flags.append("cofactor_anchor_hint")
    if tail["max_band_share"] >= params["band_anchor_share"]:
        risk_flags.append("cofactor_band_hint")

    return {
        "route": route,
        "candidates": candidates,
        "risk_flags": risk_flags,
        "self_normalized_margin": self_margin,
        "self_normalized_margin_over_sqrt": self_margin
        / math.sqrt(row["skeleton_count"])
        if row["skeleton_count"]
        else 0.0,
        "non_tail_hits": non_tail,
        "allowable_tail_hits": allowable,
        "c_allow": c_allow,
        "tail_actual_over_callow_model": tail["actual_tail_hits"] / (c_allow * model)
        if c_allow and model
        else 0.0,
        "required_tail_excess": required_tail_excess,
        "tail_excess": tail_excess,
        "tail_excess_gap": required_tail_excess - tail_excess,
        "positive_m_excess_over_required": (
            tail["positive_m_excess_sum"] / required_tail_excess
            if required_tail_excess > 0
            else 0.0
        ),
        "positive_band_excess_over_required": (
            tail["positive_band_excess_sum"] / required_tail_excess
            if required_tail_excess > 0
            else 0.0
        ),
        "m_positive_absorption_margin": (
            required_tail_excess - tail["positive_m_excess_sum"]
        ),
        "band_positive_absorption_margin": (
            required_tail_excess - tail["positive_band_excess_sum"]
        ),
    }


def row_brief(row: dict) -> dict:
    """提取定位风险行的短信息。"""
    return {
        "p": row["p"],
        "y": row["y"],
        "x": row["x"],
        "skeleton_count": row["skeleton_count"],
        "total_high_hits": row["total_high_hits"],
        "capacity_margin": row["capacity_margin"],
        "hit_ratio": row["hit_ratio"],
        "c_allow": row["c_allow"],
        "tail_actual_over_model": row["tail"]["actual_over_model"],
    }


def concentration_extrema(rows: list[dict]) -> dict:
    """汇总远尾集中峰极值。"""
    keys = {
        "max_m_share": lambda row: row["tail"]["max_m_share"],
        "max_band_share": lambda row: row["tail"]["max_band_share"],
        "max_qmod30_share": lambda row: row["tail"]["q_mod30_peak"]["share"],
        "max_dmod30_share": lambda row: row["tail"]["d_mod30_peak"]["share"],
        "max_tail_actual_over_model": lambda row: row["tail"]["actual_over_model"],
        "max_positive_m_excess_over_required": lambda row: row["route_ledger"][
            "positive_m_excess_over_required"
        ],
        "max_positive_band_excess_over_required": lambda row: row["route_ledger"][
            "positive_band_excess_over_required"
        ],
        "min_band_positive_absorption_margin": lambda row: -row["route_ledger"][
            "band_positive_absorption_margin"
        ],
    }
    output = {}
    for name, getter in keys.items():
        row = max(rows, key=getter)
        value = getter(row)
        if name == "min_band_positive_absorption_margin":
            value = -value
        output[name] = {"value": value, "row": row_brief(row)}
    return output


def audit_p(
    p: int,
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    primes: list[int],
    prefix: list[int],
    route_params: dict,
) -> dict:
    """审计单个 P 的 top 风险行并生成路由账本。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    y_limit = min(p + 1, max(2, int(math.ceil(y_factor * cutoff))))
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_limit = (p * y_limit - 1) // tail_q_min
    rough = rough_flags(m_limit, low_primes)

    all_rows = [
        row_capacity(p, y, low_primes, high_primes)
        for y in range(2, y_limit + 1)
    ]
    top_rows = sorted(all_rows, key=lambda row: -row["hit_ratio"])[:top_n]

    enriched = []
    route_counts: Counter[str] = Counter()
    flag_counts: Counter[str] = Counter()
    for row in top_rows:
        tail = tail_ledger(p, row["y"], cutoff, tail_factor, rough, prefix, primes)
        non_tail = row["total_high_hits"] - tail["actual_tail_hits"]
        allowable = row["skeleton_count"] - non_tail
        c_allow = allowable / tail["model_tail"] if tail["model_tail"] else 0.0
        merged = {
            "p": p,
            **row,
            "tail": tail,
            "non_tail_hits": non_tail,
            "allowable_tail_hits": allowable,
            "c_allow": c_allow,
        }
        route = route_row(merged, route_params)
        merged["route_ledger"] = route
        route_counts[route["route"]] += 1
        for flag in route["risk_flags"]:
            flag_counts[flag] += 1
        enriched.append(merged)

    min_margin_row = min(enriched, key=lambda row: row["capacity_margin"])
    min_callow_row = min(enriched, key=lambda row: row["c_allow"])
    max_tail_ratio_row = max(
        enriched, key=lambda row: row["tail"]["actual_over_model"]
    )
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "y_limit": y_limit,
        "top_n": top_n,
        "tail_factor": tail_factor,
        "route_counts": dict(route_counts),
        "risk_flag_counts": dict(flag_counts),
        "min_capacity_margin": min_margin_row["capacity_margin"],
        "min_capacity_margin_over_sqrt": min_margin_row[
            "capacity_margin_over_sqrt"
        ],
        "min_c_allow": min_callow_row["c_allow"],
        "max_tail_actual_over_model": max_tail_ratio_row["tail"][
            "actual_over_model"
        ],
        "concentration_extrema": concentration_extrema(enriched),
        "worst_rows": sorted(
            enriched,
            key=lambda row: (
                0 if row["route_ledger"]["route"] != "capacity_closed" else 1,
                -row["hit_ratio"],
            ),
        )[:8],
        "top_ratio_rows": enriched,
    }


def audit(
    p_list: list[int],
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    near_hit_ratio: float,
    m_anchor_share: float,
    band_anchor_share: float,
    phase_share: float,
) -> dict:
    """执行全局结构链审计。"""
    flags = sieve_bool(max(p_list))
    prefix = prime_prefix(flags)
    primes = primes_from_flags(flags)
    route_params = {
        "near_hit_ratio": near_hit_ratio,
        "m_anchor_share": m_anchor_share,
        "band_anchor_share": band_anchor_share,
        "phase_share": phase_share,
    }
    records = [
        audit_p(
            p,
            alpha,
            y_factor,
            tail_factor,
            top_n,
            primes,
            prefix,
            route_params,
        )
        for p in p_list
    ]
    total_routes: Counter[str] = Counter()
    total_flags: Counter[str] = Counter()
    all_rows = []
    for record in records:
        total_routes.update(record["route_counts"])
        total_flags.update(record["risk_flag_counts"])
        all_rows.extend(record["top_ratio_rows"])
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "y_factor": y_factor,
            "tail_factor": tail_factor,
            "top_n": top_n,
            **route_params,
        },
        "global_route_counts": dict(total_routes),
        "global_risk_flag_counts": dict(total_flags),
        "global_concentration_extrema": concentration_extrema(all_rows),
        "records": records,
    }


def compact_row(row: dict) -> str:
    """压缩展示单个风险行。"""
    route = row["route_ledger"]
    tail = row["tail"]
    return (
        f"y={row['y']}, S={row['skeleton_count']}, T={row['total_high_hits']}, "
        f"margin={row['capacity_margin']}, T/S={row['hit_ratio']:.6f}, "
        f"tail/model={tail['actual_over_model']:.6f}, "
        f"C_allow={row['c_allow']:.6f}, "
        f"self_margin={route['self_normalized_margin']}, "
        f"E/R={route['tail_excess']:.3f}/{route['required_tail_excess']:.3f}, "
        f"band_pos/R={route['positive_band_excess_over_required']:.3f}, "
        f"route={route['route']}, flags={route['risk_flags']}"
    )


def compact_extreme(name: str, item: dict) -> str:
    """压缩展示集中峰极值。"""
    row = item["row"]
    return (
        f"{name}={item['value']:.6f} "
        f"at P={row['p']},y={row['y']},"
        f"margin={row['capacity_margin']},T/S={row['hit_ratio']:.6f}"
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 行命题全局结构链路由审计",
        "",
        "**状态：** `global_structural_chain_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `y_factor`: `{params['y_factor']}`",
        f"- `tail_factor`: `{params['tail_factor']}`",
        f"- `top_n`: `{params['top_n']}`",
        f"- `near_hit_ratio`: `{params['near_hit_ratio']}`",
        f"- `m_anchor_share`: `{params['m_anchor_share']}`",
        f"- `band_anchor_share`: `{params['band_anchor_share']}`",
        f"- `phase_share`: `{params['phase_share']}`",
        "",
        "## 总路由",
        "",
        f"- `global_route_counts`: `{result['global_route_counts']}`",
        f"- `global_risk_flag_counts`: `{result['global_risk_flag_counts']}`",
    ]
    global_extrema = result["global_concentration_extrema"]
    for name in [
        "max_m_share",
        "max_band_share",
        "max_qmod30_share",
        "max_dmod30_share",
        "max_tail_actual_over_model",
        "max_positive_m_excess_over_required",
        "max_positive_band_excess_over_required",
        "min_band_positive_absorption_margin",
    ]:
        lines.append(f"- `{compact_extreme(name, global_extrema[name])}`")
    lines.extend(
        [
            "",
            "## 总表",
            "",
            "| P | cutoff | y_limit | routes | risk flags | min margin | min margin/sqrt | min C_allow | max tail/model |",
            "|---:|---:|---:|---|---|---:|---:|---:|---:|",
        ]
    )
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {record['y_limit']} | "
            f"`{record['route_counts']}` | `{record['risk_flag_counts']}` | "
            f"{record['min_capacity_margin']} | "
            f"{record['min_capacity_margin_over_sqrt']:.6f} | "
            f"{record['min_c_allow']:.6f} | "
            f"{record['max_tail_actual_over_model']:.6f} |"
        )

    lines.extend(["", "## 集中峰诊断", ""])
    for record in result["records"]:
        extrema = record["concentration_extrema"]
        lines.append(
            f"- `P={record['p']}`: "
            f"max_m_share={extrema['max_m_share']['value']:.6f}, "
            f"max_band_share={extrema['max_band_share']['value']:.6f}, "
            f"max_qmod30_share={extrema['max_qmod30_share']['value']:.6f}, "
            f"max_dmod30_share={extrema['max_dmod30_share']['value']:.6f}"
        )

    for record in result["records"]:
        lines.extend(["", f"## P={record['p']}", "", "最强风险行：", ""])
        for row in record["worst_rows"]:
            lines.append(f"- `{compact_row(row)}`")
            if row["tail"]["top_m_by_excess"]:
                top_m = row["tail"]["top_m_by_excess"][0]
                top_band = row["tail"]["top_bands"][0]
                lines.append(
                    f"  - top_m_excess: `m={top_m['m']}, "
                    f"m/y={top_m['m_over_y']:.3f}, "
                    f"actual={top_m['actual']}, model={top_m['model']:.3f}, "
                    f"excess={top_m['excess']:.3f}`"
                )
                lines.append(
                    f"  - top_band: `{top_band['band']}, "
                    f"share={top_band['actual_share']:.6f}, "
                    f"actual/model={top_band['actual_over_model']:.6f}`"
                )

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "`capacity_closed` 是严格门：`T_Y<S_Y` 直接推出该行存在素数洞。",
            "",
            "若未来样本出现 `T_Y>=S_Y`，脚本不会把它当成无名失败，而会按互补因子集中、二进 `m/y` 带集中、`mod 30` 相位峰、列残基峰和递归下降候选登记命名出口。",
            "",
            "因此该审计服务于非固定常数路线：固定常数只作诊断，正式硬点是 `Self-Normalized Tail Dichotomy + NonHit-Phase Descent + No-Cycle Defect Ledger`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="5003,10007,20011,50021,100003,200003")
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--y-factor", type=float, default=4.0)
    parser.add_argument("--tail-factor", type=float, default=10.0)
    parser.add_argument("--top-n", type=int, default=16)
    parser.add_argument("--near-hit-ratio", type=float, default=0.90)
    parser.add_argument("--m-anchor-share", type=float, default=0.10)
    parser.add_argument("--band-anchor-share", type=float, default=0.60)
    parser.add_argument("--phase-share", type=float, default=0.40)
    parser.add_argument(
        "--out-prefix",
        default="docs/global_structural_chain_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_ints(args.p_list),
        args.alpha,
        args.y_factor,
        args.tail_factor,
        args.top_n,
        args.near_hit_ratio,
        args.m_anchor_share,
        args.band_anchor_share,
        args.phase_share,
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["global_route_counts"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
