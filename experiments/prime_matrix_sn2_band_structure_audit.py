#!/usr/bin/env python3
"""审计 SN-2 正二进带的短窗/相位/列位移结构。

用法示例：
  python3 experiments/prime_matrix_sn2_band_structure_audit.py \
    --p-list 5003,10007,20011,50021,100003,200003 \
    --alpha 0.43 \
    --y-factor 4 \
    --tail-factor 10 \
    --top-n 8 \
    --out-prefix docs/sn2_band_structure_audit_20260506

目标：
  在 SN-2 BandPositive 判据之后，继续把每个正二进 m/y 带拆成：
    q 短窗、q mod 30 相位、d=Py-qm mod 30 列位移。
  若正带由短窗或相位峰支撑，则进入 SAE/PDEC/ColumnCRT；
  若都不支撑，则登记为 DistributedBandLargeSieve 候选。
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


def ratio_bin(m: int, y: int) -> str:
    """把 m/y 放入二进带。"""
    if y <= 0:
        return "undefined"
    ratio = m / y
    if ratio < 1:
        return "<1y"
    exponent = int(math.floor(math.log(ratio, 2))) if ratio > 0 else 0
    left = 2**exponent
    right = 2 ** (exponent + 1)
    return f"[{left}y,{right}y)"


def mark_low_skeleton(p: int, y: int, low_primes: list[int]) -> bytearray:
    """标记低素粗骨架，索引 d。"""
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
    """预计算 Y-rough 互补因子。"""
    rough = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        rough[0] = 0
    for q in low_primes:
        if q > limit:
            break
        rough[q : limit + 1 : q] = b"\x00" * (((limit - q) // q) + 1)
    return rough


def top_counter(counter: Counter[int], total: int) -> dict:
    """返回最大计数类。"""
    if not counter or total <= 0:
        return {"value": None, "count": 0, "share": 0.0}
    value, count = counter.most_common(1)[0]
    return {"value": value, "count": count, "share": count / total}


def row_capacity(
    p: int,
    y: int,
    low_primes: list[int],
    high_primes: list[int],
) -> dict:
    """计算行容量。"""
    alive = mark_low_skeleton(p, y, low_primes)
    skeleton = sum(alive)
    anchor = p * y
    total_hits = 0
    for q in high_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        for d in range(start, p, q):
            if alive[d]:
                total_hits += 1
    return {
        "y": y,
        "x": y - 1,
        "skeleton_count": skeleton,
        "total_high_hits": total_hits,
        "capacity_margin": skeleton - total_hits,
        "hit_ratio": total_hits / skeleton if skeleton else 0.0,
    }


def add_window_model(
    q_windows: dict[int, dict[str, float]],
    q_min: int,
    q_max: int,
    local_log: float,
    q_window_width: int,
) -> None:
    """按整数长度把模型量分配到 q 短窗。"""
    first = q_min // q_window_width
    last = q_max // q_window_width
    for idx in range(first, last + 1):
        left = max(q_min, idx * q_window_width)
        right = min(q_max, (idx + 1) * q_window_width - 1)
        if left > right:
            continue
        item = q_windows[idx]
        item["model"] += (right - left + 1) / local_log
        item["q_min"] = min(item.get("q_min", left), left)
        item["q_max"] = max(item.get("q_max", right), right)


def band_structure_for_row(
    p: int,
    y: int,
    cutoff: int,
    tail_factor: float,
    low_primes: list[int],
    rough: bytearray,
    prefix: list[int],
    primes: list[int],
    q_window_width: int,
) -> dict:
    """计算单行所有正二进带结构。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    bands = defaultdict(
        lambda: {
            "actual": 0,
            "model": 0.0,
            "interval_len": 0,
            "active_m": 0,
            "q_min": None,
            "q_max": None,
            "q_mod30": Counter(),
            "d_mod30": Counter(),
            "q_windows": defaultdict(
                lambda: {"actual": 0, "model": 0.0, "q_min": 10**30, "q_max": 0}
            ),
        }
    )
    total_actual = 0
    total_model = 0.0
    non_tail_hits = 0

    for m in range(1, m_max + 1):
        if m >= len(rough) or not rough[m]:
            continue
        q_min = max(tail_q_min, ceil_div(anchor - (p - 1), m))
        q_max = min(p - 1, (anchor - 1) // m)
        if q_min > q_max:
            continue
        interval_len = q_max - q_min + 1
        count = prefix[q_max] - (prefix[q_min - 1] if q_min > 0 else 0)
        local_log = math.log(max(q_min, 3))
        local_model = interval_len / local_log
        band = ratio_bin(m, y)
        item = bands[band]
        item["actual"] += count
        item["model"] += local_model
        item["interval_len"] += interval_len
        item["q_min"] = q_min if item["q_min"] is None else min(item["q_min"], q_min)
        item["q_max"] = q_max if item["q_max"] is None else max(item["q_max"], q_max)
        add_window_model(item["q_windows"], q_min, q_max, local_log, q_window_width)
        total_actual += count
        total_model += local_model

        if count:
            item["active_m"] += 1
            lo = bisect.bisect_left(primes, q_min)
            hi = bisect.bisect_right(primes, q_max)
            for q in primes[lo:hi]:
                d = anchor - q * m
                item["q_mod30"][q % 30] += 1
                item["d_mod30"][d % 30] += 1
                qwin = q // q_window_width
                item["q_windows"][qwin]["actual"] += 1

    # 用总高命中重算 non-tail：调用方会覆盖真实值。
    del non_tail_hits
    band_rows = []
    for band, item in bands.items():
        actual = int(item["actual"])
        model = float(item["model"])
        excess = actual - model
        q_window_rows = []
        for idx, win in item["q_windows"].items():
            win_actual = int(win["actual"])
            win_model = float(win["model"])
            q_window_rows.append(
                {
                    "window": idx,
                    "q_min": int(win["q_min"]),
                    "q_max": int(win["q_max"]),
                    "actual": win_actual,
                    "model": win_model,
                    "excess": win_actual - win_model,
                    "actual_share": win_actual / actual if actual else 0.0,
                }
            )
        q_window_rows.sort(key=lambda row: -row["excess"])
        max_qwin_excess = q_window_rows[0]["excess"] if q_window_rows else 0.0
        band_rows.append(
            {
                "band": band,
                "actual": actual,
                "model": model,
                "excess": excess,
                "positive_excess": max(0.0, excess),
                "actual_over_model": actual / model if model else 0.0,
                "interval_len": int(item["interval_len"]),
                "active_m": int(item["active_m"]),
                "q_min": item["q_min"],
                "q_max": item["q_max"],
                "q_mod30_peak": top_counter(item["q_mod30"], actual),
                "d_mod30_peak": top_counter(item["d_mod30"], actual),
                "max_qwindow_excess": max_qwin_excess,
                "max_qwindow_excess_over_band_excess": (
                    max_qwin_excess / excess if excess > 0 else 0.0
                ),
                "top_q_windows": q_window_rows[:5],
            }
        )
    band_rows.sort(key=lambda row: -row["positive_excess"])
    return {
        "tail_q_min": tail_q_min,
        "m_max": m_max,
        "actual_tail_hits": total_actual,
        "model_tail": total_model,
        "positive_bands": [row for row in band_rows if row["excess"] > 0],
        "all_bands": band_rows,
    }


def classify_band(
    band: dict,
    qwindow_excess_share: float,
    phase_share: float,
) -> list[str]:
    """给正带登记出口候选。"""
    labels = []
    if band["max_qwindow_excess_over_band_excess"] >= qwindow_excess_share:
        labels.append("sae_short_q_window_candidate")
    if band["q_mod30_peak"]["share"] >= phase_share:
        labels.append("pdec_qmod30_candidate")
    if band["d_mod30_peak"]["share"] >= phase_share:
        labels.append("columncrt_dmod30_candidate")
    if not labels:
        labels.append("distributed_band_large_sieve_candidate")
    return labels


def audit_p(
    p: int,
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    q_window_scale: float,
    qwindow_excess_share: float,
    phase_share: float,
    primes: list[int],
    prefix: list[int],
) -> dict:
    """审计单个 P。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    y_limit = min(p + 1, max(2, int(math.ceil(y_factor * cutoff))))
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_limit = (p * y_limit - 1) // tail_q_min
    rough = rough_flags(m_limit, low_primes)
    q_window_width = max(1, int(round(q_window_scale * math.sqrt(p))))

    rows = [
        row_capacity(p, y, low_primes, high_primes)
        for y in range(2, y_limit + 1)
    ]
    top_rows = sorted(rows, key=lambda row: -row["hit_ratio"])[:top_n]
    audited_rows = []
    route_counts = Counter()
    max_band_pos_ratio = 0.0
    min_band_margin = None

    for row in top_rows:
        bands = band_structure_for_row(
            p,
            row["y"],
            cutoff,
            tail_factor,
            low_primes,
            rough,
            prefix,
            primes,
            q_window_width,
        )
        non_tail = row["total_high_hits"] - bands["actual_tail_hits"]
        allowable = row["skeleton_count"] - non_tail
        c_allow = allowable / bands["model_tail"] if bands["model_tail"] else 0.0
        required = (c_allow - 1.0) * bands["model_tail"]
        positive_band_sum = sum(
            band["positive_excess"] for band in bands["positive_bands"]
        )
        band_margin = required - positive_band_sum
        band_pos_ratio = positive_band_sum / required if required > 0 else 0.0
        max_band_pos_ratio = max(max_band_pos_ratio, band_pos_ratio)
        min_band_margin = (
            band_margin
            if min_band_margin is None
            else min(min_band_margin, band_margin)
        )

        positive_bands = []
        for band in bands["positive_bands"]:
            labels = classify_band(band, qwindow_excess_share, phase_share)
            for label in labels:
                route_counts[label] += 1
            positive_bands.append({**band, "labels": labels})

        audited_rows.append(
            {
                "p": p,
                **row,
                "q_window_width": q_window_width,
                "c_allow": c_allow,
                "required_tail_excess": required,
                "positive_band_excess_sum": positive_band_sum,
                "positive_band_excess_over_required": band_pos_ratio,
                "band_positive_margin": band_margin,
                "positive_bands": positive_bands[:8],
            }
        )

    return {
        "p": p,
        "cutoff": cutoff,
        "y_limit": y_limit,
        "q_window_width": q_window_width,
        "route_counts": dict(route_counts),
        "max_positive_band_excess_over_required": max_band_pos_ratio,
        "min_band_positive_margin": min_band_margin,
        "top_rows": audited_rows,
    }


def audit(
    p_list: list[int],
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    q_window_scale: float,
    qwindow_excess_share: float,
    phase_share: float,
) -> dict:
    """执行审计。"""
    flags = sieve_bool(max(p_list))
    prefix = prime_prefix(flags)
    primes = primes_from_flags(flags)
    records = [
        audit_p(
            p,
            alpha,
            y_factor,
            tail_factor,
            top_n,
            q_window_scale,
            qwindow_excess_share,
            phase_share,
            primes,
            prefix,
        )
        for p in p_list
    ]
    total_routes = Counter()
    for record in records:
        total_routes.update(record["route_counts"])
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "y_factor": y_factor,
            "tail_factor": tail_factor,
            "top_n": top_n,
            "q_window_scale": q_window_scale,
            "qwindow_excess_share": qwindow_excess_share,
            "phase_share": phase_share,
        },
        "global_route_counts": dict(total_routes),
        "records": records,
    }


def band_text(band: dict) -> str:
    """压缩展示正二进带。"""
    return (
        f"band={band['band']}, E={band['excess']:.3f}, "
        f"A/M={band['actual_over_model']:.6f}, "
        f"qwin_E_share={band['max_qwindow_excess_over_band_excess']:.6f}, "
        f"qmod30={band['q_mod30_peak']['share']:.6f}, "
        f"dmod30={band['d_mod30_peak']['share']:.6f}, "
        f"labels={band['labels']}"
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# SN-2 正二进带结构审计",
        "",
        "**状态：** `sn2_band_structure_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `y_factor`: `{params['y_factor']}`",
        f"- `tail_factor`: `{params['tail_factor']}`",
        f"- `top_n`: `{params['top_n']}`",
        f"- `q_window_scale`: `{params['q_window_scale']}`",
        f"- `qwindow_excess_share`: `{params['qwindow_excess_share']}`",
        f"- `phase_share`: `{params['phase_share']}`",
        "",
        "## 总路由",
        "",
        f"- `global_route_counts`: `{result['global_route_counts']}`",
        "",
        "## 总表",
        "",
        "| P | cutoff | y_limit | qwin width | routes | max band+/R | min band margin |",
        "|---:|---:|---:|---:|---|---:|---:|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {record['y_limit']} | "
            f"{record['q_window_width']} | `{record['route_counts']}` | "
            f"{record['max_positive_band_excess_over_required']:.6f} | "
            f"{record['min_band_positive_margin']:.6f} |"
        )

    for record in result["records"]:
        lines.extend(["", f"## P={record['p']}", ""])
        for row in record["top_rows"][:4]:
            lines.append(
                f"- `y={row['y']}, margin={row['capacity_margin']}, "
                f"T/S={row['hit_ratio']:.6f}, band+/R="
                f"{row['positive_band_excess_over_required']:.6f}, "
                f"band_margin={row['band_positive_margin']:.3f}`"
            )
            for band in row["positive_bands"][:4]:
                lines.append(f"  - `{band_text(band)}`")

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "该审计只做结构定位：若正二进带的最大 q 短窗正超额承担比例过高，则进入 `SAE`；若 `q mod 30` 或 `d mod 30` 峰过高，则进入 `PDEC/ColumnCRT`；否则登记为 `DistributedBandLargeSieve` 候选。",
            "",
            "正式证明目标不是这些阈值本身，而是证明分散候选可由带级大筛吸收；若吸收失败，则失败会被上述短窗或相位出口捕获。",
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
    parser.add_argument("--top-n", type=int, default=8)
    parser.add_argument("--q-window-scale", type=float, default=1.0)
    parser.add_argument("--qwindow-excess-share", type=float, default=0.5)
    parser.add_argument("--phase-share", type=float, default=0.35)
    parser.add_argument(
        "--out-prefix",
        default="docs/sn2_band_structure_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_ints(args.p_list),
        args.alpha,
        args.y_factor,
        args.tail_factor,
        args.top_n,
        args.q_window_scale,
        args.qwindow_excess_share,
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
