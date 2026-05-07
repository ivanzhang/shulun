#!/usr/bin/env python3
"""扫描 DPRC-BES 的 W=30 单位相位平衡。

用法示例：
  python3 experiments/prime_matrix_dprc_wheel_unit_phase_balance_scan.py \
    --max-p 100000 --alpha 0.43 --thresholds 2003,10007 \
    --out-prefix docs/dprc_wheel_unit_phase_balance_w30_p100000_20260506

目标：
  对每个 P/side 同时计算 BES 正桶向量与 mod30 单位类中心化偏差，
  检查低模单位类偏斜是否会与高 L1 / 高 L2 危险交集同步。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


BETA_BUCKETS = [
    (0.43, 0.50, "[0.43,0.50)"),
    (0.50, 0.60, "[0.50,0.60)"),
    (0.60, 0.70, "[0.60,0.70)"),
    (0.70, 0.80, "[0.70,0.80)"),
    (0.80, 0.90, "[0.80,0.90)"),
    (0.90, 1.01, "[0.90,1.00)"),
]
UNIT30 = {1, 7, 11, 13, 17, 19, 23, 29}
L1_DANGER = 12.0 / 5.0
L2_ENERGY = 6.0 / 5.0
L2_CAUCHY = 3.0 / math.sqrt(6.0)


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


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def row_residue(p: int, q: int, side: str) -> int:
    """返回 q 覆盖平方前/后行时的 k 同余类。"""
    p2 = (p * p) % q
    if side == "plus":
        return (-p2) % q
    if side == "minus":
        return p2
    raise ValueError(f"unknown side: {side}")


def n_residue_mod30(p: int, k: int, side: str) -> int:
    """返回真实数值 P^2±k 的 mod30 残基。"""
    p2 = (p * p) % 30
    if side == "plus":
        return (p2 + k) % 30
    return (p2 - k) % 30


def mark_low_skeleton(p: int, low_primes: list[int], side: str) -> bytearray:
    """标记动态粗骨架。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    for q in low_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def beta_bucket(beta: float) -> str:
    """返回 beta 桶标签。"""
    for left, right, label in BETA_BUCKETS:
        if left <= beta < right:
            return label
    return "outside"


def skeleton_n30_counts(p: int, side: str, alive: bytearray) -> list[int]:
    """统计动态粗骨架在真实 n mod30 下的分布。"""
    counts = [0] * 30
    for k, flag in enumerate(alive):
        if flag:
            counts[n_residue_mod30(p, k, side)] += 1
    return counts


def audit_record(p: int, side: str, alpha: float, primes: list[int]) -> dict:
    """计算单条 P/side 的 BES 与 W=30 单位相位指标。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    sqrt_s = math.sqrt(skeleton)
    bucket_disc = {label: 0.0 for _left, _right, label in BETA_BUCKETS}
    actual30 = [0] * 30
    expected_counts30 = skeleton_n30_counts(p, side, alive)
    harmonic_high = 0.0
    total_hits = 0

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if not alive[k]:
                continue
            hits += 1
            total_hits += 1
            actual30[n_residue_mod30(p, k, side)] += 1
        harmonic_high += 1.0 / q
        label = beta_bucket(math.log(q) / math.log(p))
        if label != "outside":
            bucket_disc[label] += hits - skeleton / q

    bucket_vector = [
        bucket_disc[label] / sqrt_s if sqrt_s else 0.0
        for _left, _right, label in BETA_BUCKETS
    ]
    positive_vector = [max(0.0, value) for value in bucket_vector]
    l1_value = sum(positive_vector)
    l2_value = math.sqrt(sum(value * value for value in positive_vector))
    effective_dimension = (
        (l1_value * l1_value) / (l2_value * l2_value) if l2_value else 0.0
    )
    phase_rows = []
    for residue in range(30):
        expected = expected_counts30[residue] * harmonic_high
        discrepancy = actual30[residue] - expected
        phase_rows.append(
            {
                "residue": residue,
                "is_unit": residue in UNIT30,
                "skeleton_count": expected_counts30[residue],
                "actual": actual30[residue],
                "expected": expected,
                "discrepancy": discrepancy,
                "discrepancy_over_sqrt": discrepancy / sqrt_s if sqrt_s else 0.0,
            }
        )
    unit_rows = [row for row in phase_rows if row["is_unit"]]
    top_unit = max(unit_rows, key=lambda row: row["discrepancy"])
    positive_unit = [max(0.0, row["discrepancy"]) for row in unit_rows]
    return {
        "p": p,
        "side": side,
        "cutoff": cutoff,
        "skeleton_count": skeleton,
        "total_hits": total_hits,
        "harmonic_high": harmonic_high,
        "positive_bucket_l1_over_sqrt": l1_value,
        "positive_bucket_l2_over_sqrt": l2_value,
        "positive_bucket_effective_dimension": effective_dimension,
        "unit30_max_positive_over_sqrt": max(0.0, top_unit["discrepancy_over_sqrt"]),
        "unit30_positive_l1_over_sqrt": sum(positive_unit) / sqrt_s
        if sqrt_s
        else 0.0,
        "unit30_positive_l2_over_sqrt": math.sqrt(
            sum(value * value for value in positive_unit)
        )
        / sqrt_s
        if sqrt_s
        else 0.0,
        "unit30_top_residue": top_unit["residue"],
        "unit30_top_discrepancy": top_unit["discrepancy"],
        "danger_l1_l2_6_5": l1_value >= L1_DANGER and l2_value > L2_ENERGY,
        "danger_l1_l2_cauchy": l1_value >= L1_DANGER and l2_value > L2_CAUCHY,
        "phase_rows30": phase_rows,
    }


def compact_record(record: dict) -> dict:
    """保留报告需要的核心字段。"""
    keys = [
        "p",
        "side",
        "cutoff",
        "skeleton_count",
        "total_hits",
        "positive_bucket_l1_over_sqrt",
        "positive_bucket_l2_over_sqrt",
        "positive_bucket_effective_dimension",
        "unit30_max_positive_over_sqrt",
        "unit30_positive_l1_over_sqrt",
        "unit30_positive_l2_over_sqrt",
        "unit30_top_residue",
        "unit30_top_discrepancy",
        "danger_l1_l2_6_5",
        "danger_l1_l2_cauchy",
    ]
    return {key: record[key] for key in keys}


def summarize(records: list[dict], threshold: int) -> dict:
    """汇总某个 P 下界以上的 W=30 相位指标。"""
    rows = [record for record in records if record["p"] >= threshold]
    high_l1 = [row for row in rows if row["positive_bucket_l1_over_sqrt"] >= L1_DANGER]
    high_l2 = [row for row in rows if row["positive_bucket_l2_over_sqrt"] > L2_CAUCHY]
    residue_hist = {}
    for row in rows:
        residue = row["unit30_top_residue"]
        residue_hist[residue] = residue_hist.get(residue, 0) + 1
    return {
        "threshold": threshold,
        "record_count": len(rows),
        "danger_l1_l2_6_5_count": sum(row["danger_l1_l2_6_5"] for row in rows),
        "danger_l1_l2_cauchy_count": sum(row["danger_l1_l2_cauchy"] for row in rows),
        "max_unit30_peak_over_sqrt": max(
            row["unit30_max_positive_over_sqrt"] for row in rows
        ),
        "max_unit30_peak_record": compact_record(
            max(rows, key=lambda row: row["unit30_max_positive_over_sqrt"])
        ),
        "max_unit30_positive_l1_over_sqrt": max(
            row["unit30_positive_l1_over_sqrt"] for row in rows
        ),
        "max_unit30_l1_record": compact_record(
            max(rows, key=lambda row: row["unit30_positive_l1_over_sqrt"])
        ),
        "max_l1_when_unit30_peak_ge_0_8": max(
            [row["positive_bucket_l1_over_sqrt"] for row in rows if row["unit30_max_positive_over_sqrt"] >= 0.8]
            or [0.0]
        ),
        "max_l2_when_unit30_peak_ge_0_8": max(
            [row["positive_bucket_l2_over_sqrt"] for row in rows if row["unit30_max_positive_over_sqrt"] >= 0.8]
            or [0.0]
        ),
        "high_l1_count": len(high_l1),
        "high_l1_max_unit30_peak": max(
            [row["unit30_max_positive_over_sqrt"] for row in high_l1] or [0.0]
        ),
        "high_l2_count": len(high_l2),
        "high_l2_max_l1": max(
            [row["positive_bucket_l1_over_sqrt"] for row in high_l2] or [0.0]
        ),
        "top_by_unit30_peak": [
            compact_record(row)
            for row in sorted(
                rows, key=lambda row: -row["unit30_max_positive_over_sqrt"]
            )[:10]
        ],
        "top_by_l1": [
            compact_record(row)
            for row in sorted(
                rows, key=lambda row: -row["positive_bucket_l1_over_sqrt"]
            )[:10]
        ],
        "top_residue_histogram": dict(sorted(residue_hist.items())),
    }


def audit(max_p: int, alpha: float, thresholds: list[int]) -> dict:
    """执行全范围 W=30 单位相位扫描。"""
    primes = primes_from_flags(sieve_bool(max_p))
    p_values = [p for p in primes if p >= 13]
    records = []
    for p in p_values:
        for side in ("minus", "plus"):
            records.append(audit_record(p, side, alpha, primes))
    return {
        "parameters": {
            "max_p": max_p,
            "alpha": alpha,
            "thresholds": thresholds,
            "prime_count": len(p_values),
        },
        "summaries": [summarize(records, threshold) for threshold in thresholds],
    }


def record_id(record: dict) -> str:
    """格式化记录标识。"""
    return f"P={record['p']} {record['side']}"


def write_record_table(lines: list[str], rows: list[dict]) -> None:
    """写记录表。"""
    lines.extend(
        [
            "| record | L1 | L2 | eff dim | unit30 peak | unit30 L1 | top residue |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {record_id(row)} | {row['positive_bucket_l1_over_sqrt']:.6f} | "
            f"{row['positive_bucket_l2_over_sqrt']:.6f} | "
            f"{row['positive_bucket_effective_dimension']:.6f} | "
            f"{row['unit30_max_positive_over_sqrt']:.6f} | "
            f"{row['unit30_positive_l1_over_sqrt']:.6f} | "
            f"{row['unit30_top_residue']} |"
        )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC W=30单位相位平衡扫描",
        "",
        "**状态：** `wheel_unit_phase_balance_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `thresholds`: `{params['thresholds']}`",
        f"- `prime_count`: `{params['prime_count']}`",
        "",
    ]
    for summary in result["summaries"]:
        lines.extend(
            [
                f"## P>={summary['threshold']}",
                "",
                f"- `record_count`: `{summary['record_count']}`",
                f"- `danger_l1_l2_6_5_count`: `{summary['danger_l1_l2_6_5_count']}`",
                f"- `danger_l1_l2_cauchy_count`: `{summary['danger_l1_l2_cauchy_count']}`",
                f"- `max_unit30_peak_over_sqrt`: `{summary['max_unit30_peak_over_sqrt']:.6f}`",
                f"- `max_unit30_positive_l1_over_sqrt`: `{summary['max_unit30_positive_l1_over_sqrt']:.6f}`",
                f"- `high_l1_count`: `{summary['high_l1_count']}`",
                f"- `high_l1_max_unit30_peak`: `{summary['high_l1_max_unit30_peak']:.6f}`",
                f"- `high_l2_count`: `{summary['high_l2_count']}`",
                f"- `high_l2_max_l1`: `{summary['high_l2_max_l1']:.6f}`",
                f"- `max_l1_when_unit30_peak_ge_0_8`: `{summary['max_l1_when_unit30_peak_ge_0_8']:.6f}`",
                f"- `max_l2_when_unit30_peak_ge_0_8`: `{summary['max_l2_when_unit30_peak_ge_0_8']:.6f}`",
                f"- `top_residue_histogram`: `{summary['top_residue_histogram']}`",
                "",
                "### top by unit30 peak",
                "",
            ]
        )
        write_record_table(lines, summary["top_by_unit30_peak"])
        lines.extend(["", "### top by L1", ""])
        write_record_table(lines, summary["top_by_l1"])
        lines.append("")
    lines.extend(
        [
            "## 结构解释",
            "",
            "该扫描只检查 `W=30` 的单位类投影。若高 `unit30 peak` 与 BES 高 L1/L2 危险交集同步，则应进入 `W-unit PDEC`；若不同步，则 `mod30` 峰只是第一层轮相位偏斜，必须继续提升到 `210/2310` 或交给高模大筛能量界。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=100000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--thresholds", default="2003,10007")
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_wheel_unit_phase_balance_w30_p100000_20260506",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.alpha, parse_ints(args.thresholds))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
