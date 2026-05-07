#!/usr/bin/env python3
"""扫描 DPRC-BES 的多层轮单位相位平衡。

用法示例：
  python3 experiments/prime_matrix_dprc_layered_wheel_phase_scan.py \
    --max-p 100000 --alpha 0.43 --wheels 30,210,2310 \
    --out-prefix docs/dprc_layered_wheel_phase_scan_p100000_20260506

目标：
  同时扫描 W=30/210/2310 的单位类相位峰，
  检查低模连乘层级偏斜是否与 BES 高 L1 / 高 L2 危险交集同步。
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


def units_mod(wheel: int) -> set[int]:
    """返回 wheel 的单位类。"""
    return {residue for residue in range(wheel) if math.gcd(residue, wheel) == 1}


def row_residue(p: int, q: int, side: str) -> int:
    """返回 q 覆盖平方前/后行时的 k 同余类。"""
    p2 = (p * p) % q
    if side == "plus":
        return (-p2) % q
    if side == "minus":
        return p2
    raise ValueError(f"unknown side: {side}")


def n_residue_mod(p: int, k: int, side: str, wheel: int) -> int:
    """返回真实数值 P^2±k 的 mod wheel 残基。"""
    p2 = (p * p) % wheel
    if side == "plus":
        return (p2 + k) % wheel
    return (p2 - k) % wheel


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


def compact_record(record: dict, wheel: int | None = None) -> dict:
    """保留报告需要的核心字段。"""
    base = {
        "p": record["p"],
        "side": record["side"],
        "skeleton_count": record["skeleton_count"],
        "positive_bucket_l1_over_sqrt": record["positive_bucket_l1_over_sqrt"],
        "positive_bucket_l2_over_sqrt": record["positive_bucket_l2_over_sqrt"],
        "positive_bucket_effective_dimension": record[
            "positive_bucket_effective_dimension"
        ],
        "danger_l1_l2_6_5": record["danger_l1_l2_6_5"],
        "danger_l1_l2_cauchy": record["danger_l1_l2_cauchy"],
    }
    if wheel is not None:
        base["wheel"] = wheel
        base.update(record["wheel_metrics"][str(wheel)])
    return base


def audit_record(
    p: int,
    side: str,
    alpha: float,
    primes: list[int],
    wheels: list[int],
    unit_tables: dict[int, set[int]],
) -> dict:
    """计算单条 P/side 的 BES 与多层轮相位指标。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    sqrt_s = math.sqrt(skeleton)
    bucket_disc = {label: 0.0 for _left, _right, label in BETA_BUCKETS}
    actual = {wheel: [0] * wheel for wheel in wheels}
    expected_counts = {wheel: [0] * wheel for wheel in wheels}
    harmonic_high = 0.0

    for k, flag in enumerate(alive):
        if not flag:
            continue
        for wheel in wheels:
            expected_counts[wheel][n_residue_mod(p, k, side, wheel)] += 1

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if not alive[k]:
                continue
            hits += 1
            for wheel in wheels:
                actual[wheel][n_residue_mod(p, k, side, wheel)] += 1
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

    wheel_metrics = {}
    for wheel in wheels:
        units = unit_tables[wheel]
        unit_rows = []
        for residue in units:
            expected = expected_counts[wheel][residue] * harmonic_high
            discrepancy = actual[wheel][residue] - expected
            unit_rows.append((residue, discrepancy))
        top_residue, top_discrepancy = max(unit_rows, key=lambda item: item[1])
        positive = [max(0.0, value) for _residue, value in unit_rows]
        wheel_metrics[str(wheel)] = {
            "unit_peak_over_sqrt": max(0.0, top_discrepancy) / sqrt_s
            if sqrt_s
            else 0.0,
            "unit_positive_l1_over_sqrt": sum(positive) / sqrt_s
            if sqrt_s
            else 0.0,
            "unit_positive_l2_over_sqrt": math.sqrt(
                sum(value * value for value in positive)
            )
            / sqrt_s
            if sqrt_s
            else 0.0,
            "unit_top_residue": top_residue,
            "unit_top_discrepancy": top_discrepancy,
        }

    return {
        "p": p,
        "side": side,
        "skeleton_count": skeleton,
        "positive_bucket_l1_over_sqrt": l1_value,
        "positive_bucket_l2_over_sqrt": l2_value,
        "positive_bucket_effective_dimension": effective_dimension,
        "danger_l1_l2_6_5": l1_value >= L1_DANGER and l2_value > L2_ENERGY,
        "danger_l1_l2_cauchy": l1_value >= L1_DANGER and l2_value > L2_CAUCHY,
        "wheel_metrics": wheel_metrics,
    }


def summarize_wheel(rows: list[dict], wheel: int) -> dict:
    """汇总单个 wheel 的层级相位指标。"""
    high_l1 = [row for row in rows if row["positive_bucket_l1_over_sqrt"] >= L1_DANGER]
    high_l2 = [row for row in rows if row["positive_bucket_l2_over_sqrt"] > L2_CAUCHY]
    peak_key = lambda row: row["wheel_metrics"][str(wheel)]["unit_peak_over_sqrt"]
    l1_key = lambda row: row["wheel_metrics"][str(wheel)]["unit_positive_l1_over_sqrt"]
    peak_ge_08 = [row for row in rows if peak_key(row) >= 0.8]
    residue_hist: dict[int, int] = {}
    for row in rows:
        residue = row["wheel_metrics"][str(wheel)]["unit_top_residue"]
        residue_hist[residue] = residue_hist.get(residue, 0) + 1
    top_residues = sorted(
        residue_hist.items(), key=lambda item: (-item[1], item[0])
    )[:20]
    return {
        "wheel": wheel,
        "max_unit_peak_over_sqrt": peak_key(max(rows, key=peak_key)),
        "max_unit_peak_record": compact_record(max(rows, key=peak_key), wheel),
        "max_unit_positive_l1_over_sqrt": l1_key(max(rows, key=l1_key)),
        "max_unit_l1_record": compact_record(max(rows, key=l1_key), wheel),
        "high_l1_count": len(high_l1),
        "high_l1_max_unit_peak": max([peak_key(row) for row in high_l1] or [0.0]),
        "high_l2_count": len(high_l2),
        "high_l2_max_l1": max(
            [row["positive_bucket_l1_over_sqrt"] for row in high_l2] or [0.0]
        ),
        "max_l1_when_unit_peak_ge_0_8": max(
            [row["positive_bucket_l1_over_sqrt"] for row in peak_ge_08] or [0.0]
        ),
        "max_l2_when_unit_peak_ge_0_8": max(
            [row["positive_bucket_l2_over_sqrt"] for row in peak_ge_08] or [0.0]
        ),
        "top_by_unit_peak": [
            compact_record(row, wheel)
            for row in sorted(rows, key=peak_key, reverse=True)[:8]
        ],
        "top_by_l1": [
            compact_record(row, wheel)
            for row in sorted(
                rows, key=lambda row: -row["positive_bucket_l1_over_sqrt"]
            )[:8]
        ],
        "top_residue_histogram": dict(top_residues),
    }


def summarize(records: list[dict], threshold: int, wheels: list[int]) -> dict:
    """汇总某个 P 下界以上的层级相位指标。"""
    rows = [record for record in records if record["p"] >= threshold]
    return {
        "threshold": threshold,
        "record_count": len(rows),
        "danger_l1_l2_6_5_count": sum(row["danger_l1_l2_6_5"] for row in rows),
        "danger_l1_l2_cauchy_count": sum(row["danger_l1_l2_cauchy"] for row in rows),
        "wheels": [summarize_wheel(rows, wheel) for wheel in wheels],
    }


def audit(max_p: int, alpha: float, thresholds: list[int], wheels: list[int]) -> dict:
    """执行层级轮相位扫描。"""
    primes = primes_from_flags(sieve_bool(max_p))
    p_values = [p for p in primes if p >= 13]
    unit_tables = {wheel: units_mod(wheel) for wheel in wheels}
    records = []
    for p in p_values:
        for side in ("minus", "plus"):
            records.append(audit_record(p, side, alpha, primes, wheels, unit_tables))
    return {
        "parameters": {
            "max_p": max_p,
            "alpha": alpha,
            "thresholds": thresholds,
            "wheels": wheels,
            "prime_count": len(p_values),
        },
        "summaries": [summarize(records, threshold, wheels) for threshold in thresholds],
    }


def record_id(row: dict) -> str:
    """格式化记录标识。"""
    return f"P={row['p']} {row['side']}"


def write_record_table(lines: list[str], rows: list[dict]) -> None:
    """写记录表。"""
    lines.extend(
        [
            "| record | L1 | L2 | eff dim | unit peak | unit L1 | top residue |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {record_id(row)} | {row['positive_bucket_l1_over_sqrt']:.6f} | "
            f"{row['positive_bucket_l2_over_sqrt']:.6f} | "
            f"{row['positive_bucket_effective_dimension']:.6f} | "
            f"{row['unit_peak_over_sqrt']:.6f} | "
            f"{row['unit_positive_l1_over_sqrt']:.6f} | "
            f"{row['unit_top_residue']} |"
        )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC 层叠轮单位相位扫描",
        "",
        "**状态：** `layered_wheel_phase_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `thresholds`: `{params['thresholds']}`",
        f"- `wheels`: `{params['wheels']}`",
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
                "",
            ]
        )
        for wheel_summary in summary["wheels"]:
            lines.extend(
                [
                    f"### W={wheel_summary['wheel']}",
                    "",
                    f"- `max_unit_peak_over_sqrt`: `{wheel_summary['max_unit_peak_over_sqrt']:.6f}`",
                    f"- `max_unit_positive_l1_over_sqrt`: `{wheel_summary['max_unit_positive_l1_over_sqrt']:.6f}`",
                    f"- `high_l1_count`: `{wheel_summary['high_l1_count']}`",
                    f"- `high_l1_max_unit_peak`: `{wheel_summary['high_l1_max_unit_peak']:.6f}`",
                    f"- `high_l2_count`: `{wheel_summary['high_l2_count']}`",
                    f"- `high_l2_max_l1`: `{wheel_summary['high_l2_max_l1']:.6f}`",
                    f"- `max_l1_when_unit_peak_ge_0_8`: `{wheel_summary['max_l1_when_unit_peak_ge_0_8']:.6f}`",
                    f"- `max_l2_when_unit_peak_ge_0_8`: `{wheel_summary['max_l2_when_unit_peak_ge_0_8']:.6f}`",
                    f"- `top_residue_histogram`: `{wheel_summary['top_residue_histogram']}`",
                    "",
                    "Top by unit peak:",
                    "",
                ]
            )
            write_record_table(lines, wheel_summary["top_by_unit_peak"])
            lines.extend(["", "Top by L1:", ""])
            write_record_table(lines, wheel_summary["top_by_l1"])
            lines.append("")
    lines.extend(
        [
            "## 结构解释",
            "",
            "若某一层 `W` 的单位峰与 BES 高 L1/L2 危险交集同步，则进入该层 `W-unit PDEC`。若 `30/210/2310` 都不同步，则低模连乘层级只给出局部偏斜，真正剩余必须由高模分散能量控制。",
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
    parser.add_argument("--wheels", default="30,210,2310")
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_layered_wheel_phase_scan_p100000_20260506",
    )
    args = parser.parse_args()
    result = audit(
        args.max_p,
        args.alpha,
        parse_ints(args.thresholds),
        parse_ints(args.wheels),
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
