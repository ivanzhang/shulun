#!/usr/bin/env python3
"""扫描 DPRC q尺度分桶偏差包络。

用法示例：
  python3 experiments/prime_matrix_dprc_block_envelope_scan.py \
    --max-p 100000 --alpha 0.43 \
    --out-prefix docs/dprc_block_envelope_scan_alpha043_p100000_20260506

目标：
  将全局相对偏差 D=T-HS 拆成 beta 桶偏差 D_B，
  扫描每个桶的 max D_B/sqrt(S)，为桶级平方根界提供目标常数。
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

SYNC_SUM_THRESHOLDS = [1.5, 2.0, 2.2, 2.4]
ENERGY_L2_THRESHOLDS = [
    ("1.0", 1.0),
    ("1.1", 1.1),
    ("3/sqrt6", 3.0 / math.sqrt(6.0)),
    ("1.2", 1.2),
]
DANGER_INTERSECTIONS = [
    ("l1_ge_12_5_and_l2_gt_6_5", 12.0 / 5.0, 6.0 / 5.0),
    ("l1_ge_12_5_and_l2_gt_3_sqrt6", 12.0 / 5.0, 3.0 / math.sqrt(6.0)),
]


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


def empty_bucket_stats() -> dict[str, dict]:
    """初始化桶统计。"""
    return {
        label: {
            "max_positive_over_sqrt": -10**9,
            "max_abs_over_sqrt": -1.0,
            "max_positive_record": None,
            "max_abs_record": None,
            "sum_positive_over_sqrt_at_global_worst": None,
        }
        for _left, _right, label in BETA_BUCKETS
    }


def audit_record(p: int, side: str, alpha: float, primes: list[int]) -> dict:
    """计算单条记录的总偏差与分桶偏差。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    sqrt_s = math.sqrt(skeleton)
    bucket_disc = {label: 0.0 for _left, _right, label in BETA_BUCKETS}
    bucket_hits = {label: 0 for _left, _right, label in BETA_BUCKETS}
    bucket_expected = {label: 0.0 for _left, _right, label in BETA_BUCKETS}

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if alive[k]:
                hits += 1
        expected = skeleton / q
        label = beta_bucket(math.log(q) / math.log(p))
        if label == "outside":
            continue
        bucket_hits[label] += hits
        bucket_expected[label] += expected
        bucket_disc[label] += hits - expected

    total_disc = sum(bucket_disc.values())
    bucket_vector = [
        bucket_disc[label] / sqrt_s if sqrt_s else 0.0
        for _left, _right, label in BETA_BUCKETS
    ]
    positive_bucket_vector = [max(0.0, value) for value in bucket_vector]
    positive_bucket_sum = sum(positive_bucket_vector)
    negative_bucket_sum = sum(max(0.0, -value) for value in bucket_vector)
    positive_bucket_l2 = math.sqrt(
        sum(value * value for value in positive_bucket_vector)
    )
    positive_bucket_count = sum(1 for value in positive_bucket_vector if value > 0)
    effective_dimension = (
        (positive_bucket_sum * positive_bucket_sum) / (positive_bucket_l2**2)
        if positive_bucket_l2
        else 0.0
    )
    cauchy6_bound = math.sqrt(len(BETA_BUCKETS)) * positive_bucket_l2
    cauchy_count_bound = (
        math.sqrt(positive_bucket_count) * positive_bucket_l2
        if positive_bucket_count
        else 0.0
    )
    return {
        "p": p,
        "side": side,
        "cutoff": cutoff,
        "skeleton_count": skeleton,
        "sqrt_skeleton": sqrt_s,
        "total_discrepancy": total_disc,
        "total_discrepancy_over_sqrt": total_disc / sqrt_s if sqrt_s else 0.0,
        "positive_bucket_sum_over_sqrt": positive_bucket_sum,
        "negative_bucket_sum_over_sqrt": negative_bucket_sum,
        "bucket_l2_over_sqrt": math.sqrt(sum(value * value for value in bucket_vector)),
        "positive_bucket_l2_over_sqrt": positive_bucket_l2,
        "positive_bucket_count": positive_bucket_count,
        "positive_bucket_effective_dimension": effective_dimension,
        "positive_bucket_cauchy6_bound_over_sqrt": cauchy6_bound,
        "positive_bucket_cauchy6_slack_over_sqrt": (
            cauchy6_bound - positive_bucket_sum
        ),
        "positive_bucket_cauchy_count_slack_over_sqrt": (
            cauchy_count_bound - positive_bucket_sum
        ),
        "bucket_rows": {
            label: {
                "hits": bucket_hits[label],
                "expected": bucket_expected[label],
                "discrepancy": bucket_disc[label],
                "discrepancy_over_sqrt": bucket_disc[label] / sqrt_s
                if sqrt_s
                else 0.0,
            }
            for _left, _right, label in BETA_BUCKETS
        },
    }


def update_envelope(envelope: dict, record: dict) -> None:
    """用单条记录更新包络。"""
    for label, row in record["bucket_rows"].items():
        value = row["discrepancy_over_sqrt"]
        abs_value = abs(value)
        if value > envelope[label]["max_positive_over_sqrt"]:
            envelope[label]["max_positive_over_sqrt"] = value
            envelope[label]["max_positive_record"] = {
                "p": record["p"],
                "side": record["side"],
                "cutoff": record["cutoff"],
                "skeleton_count": record["skeleton_count"],
                "bucket_discrepancy": row["discrepancy"],
                "bucket_discrepancy_over_sqrt": value,
                "total_discrepancy_over_sqrt": record[
                    "total_discrepancy_over_sqrt"
                ],
            }
        if abs_value > envelope[label]["max_abs_over_sqrt"]:
            envelope[label]["max_abs_over_sqrt"] = abs_value
            envelope[label]["max_abs_record"] = {
                "p": record["p"],
                "side": record["side"],
                "cutoff": record["cutoff"],
                "skeleton_count": record["skeleton_count"],
                "bucket_discrepancy": row["discrepancy"],
                "bucket_discrepancy_over_sqrt": value,
                "total_discrepancy_over_sqrt": record[
                    "total_discrepancy_over_sqrt"
                ],
            }


def audit(max_p: int, alpha: float, thresholds: list[int]) -> dict:
    """执行全范围扫描。"""
    flags = sieve_bool(max_p)
    primes = primes_from_flags(flags)
    p_values = [p for p in primes if p >= 13]
    threshold_tables = {
        threshold: {
            "threshold": threshold,
            "record_count": 0,
            "envelope": empty_bucket_stats(),
            "max_total_positive_over_sqrt": -10**9,
            "max_total_positive_record": None,
            "max_positive_bucket_sum_over_sqrt": -10**9,
            "max_positive_bucket_sum_record": None,
            "max_positive_bucket_l2_over_sqrt": -10**9,
            "max_positive_bucket_l2_record": None,
            "max_bucket_l2_over_sqrt": -10**9,
            "max_bucket_l2_record": None,
            "max_positive_bucket_effective_dimension": -10**9,
            "max_positive_bucket_effective_dimension_record": None,
            "max_positive_bucket_cauchy6_bound_over_sqrt": -10**9,
            "max_positive_bucket_cauchy6_bound_record": None,
            "min_cauchy6_slack_when_bound_ge_3": 10**9,
            "min_cauchy6_slack_when_bound_ge_3_record": None,
            "sync_by_positive_sum_threshold": {
                str(limit): {
                    "threshold": limit,
                    "record_count": 0,
                    "max_effective_dimension": -10**9,
                    "max_effective_dimension_record": None,
                    "max_positive_l2_over_sqrt": -10**9,
                    "max_positive_l2_record": None,
                    "min_cauchy6_slack_over_sqrt": 10**9,
                    "min_cauchy6_slack_record": None,
                }
                for limit in SYNC_SUM_THRESHOLDS
            },
            "sync_by_l2_threshold": {
                key: {
                    "threshold": limit,
                    "record_count": 0,
                    "max_positive_sum_over_sqrt": -10**9,
                    "max_positive_sum_record": None,
                    "max_effective_dimension": -10**9,
                    "max_effective_dimension_record": None,
                    "min_cauchy6_slack_over_sqrt": 10**9,
                    "min_cauchy6_slack_record": None,
                }
                for key, limit in ENERGY_L2_THRESHOLDS
            },
            "danger_intersections": {
                key: {
                    "l1_threshold": l1_limit,
                    "l2_threshold": l2_limit,
                    "record_count": 0,
                    "max_positive_sum_over_sqrt": 0.0,
                    "max_positive_l2_over_sqrt": 0.0,
                    "max_record": None,
                }
                for key, l1_limit, l2_limit in DANGER_INTERSECTIONS
            },
        }
        for threshold in thresholds
    }

    for p in p_values:
        for side in ("minus", "plus"):
            record = audit_record(p, side, alpha, primes)
            for threshold, table in threshold_tables.items():
                if p < threshold:
                    continue
                table["record_count"] += 1
                update_envelope(table["envelope"], record)
                total_pos = max(0.0, record["total_discrepancy_over_sqrt"])
                if total_pos > table["max_total_positive_over_sqrt"]:
                    table["max_total_positive_over_sqrt"] = total_pos
                    table["max_total_positive_record"] = record
                pos_sum = record["positive_bucket_sum_over_sqrt"]
                if pos_sum > table["max_positive_bucket_sum_over_sqrt"]:
                    table["max_positive_bucket_sum_over_sqrt"] = pos_sum
                    table["max_positive_bucket_sum_record"] = record
                pos_l2 = record["positive_bucket_l2_over_sqrt"]
                if pos_l2 > table["max_positive_bucket_l2_over_sqrt"]:
                    table["max_positive_bucket_l2_over_sqrt"] = pos_l2
                    table["max_positive_bucket_l2_record"] = record
                l2_value = record["bucket_l2_over_sqrt"]
                if l2_value > table["max_bucket_l2_over_sqrt"]:
                    table["max_bucket_l2_over_sqrt"] = l2_value
                    table["max_bucket_l2_record"] = record
                effdim = record["positive_bucket_effective_dimension"]
                if effdim > table["max_positive_bucket_effective_dimension"]:
                    table["max_positive_bucket_effective_dimension"] = effdim
                    table["max_positive_bucket_effective_dimension_record"] = record
                cauchy6_bound = record["positive_bucket_cauchy6_bound_over_sqrt"]
                if cauchy6_bound > table[
                    "max_positive_bucket_cauchy6_bound_over_sqrt"
                ]:
                    table[
                        "max_positive_bucket_cauchy6_bound_over_sqrt"
                    ] = cauchy6_bound
                    table["max_positive_bucket_cauchy6_bound_record"] = record
                cauchy6_slack = record["positive_bucket_cauchy6_slack_over_sqrt"]
                if (
                    cauchy6_bound >= 3.0
                    and cauchy6_slack
                    < table["min_cauchy6_slack_when_bound_ge_3"]
                ):
                    table["min_cauchy6_slack_when_bound_ge_3"] = cauchy6_slack
                    table["min_cauchy6_slack_when_bound_ge_3_record"] = record
                for limit in SYNC_SUM_THRESHOLDS:
                    if pos_sum < limit:
                        continue
                    sync_table = table["sync_by_positive_sum_threshold"][str(limit)]
                    sync_table["record_count"] += 1
                    if effdim > sync_table["max_effective_dimension"]:
                        sync_table["max_effective_dimension"] = effdim
                        sync_table["max_effective_dimension_record"] = record
                    if pos_l2 > sync_table["max_positive_l2_over_sqrt"]:
                        sync_table["max_positive_l2_over_sqrt"] = pos_l2
                        sync_table["max_positive_l2_record"] = record
                    if cauchy6_slack < sync_table["min_cauchy6_slack_over_sqrt"]:
                        sync_table["min_cauchy6_slack_over_sqrt"] = cauchy6_slack
                        sync_table["min_cauchy6_slack_record"] = record
                for key, limit in ENERGY_L2_THRESHOLDS:
                    if pos_l2 < limit:
                        continue
                    energy_table = table["sync_by_l2_threshold"][key]
                    energy_table["record_count"] += 1
                    if pos_sum > energy_table["max_positive_sum_over_sqrt"]:
                        energy_table["max_positive_sum_over_sqrt"] = pos_sum
                        energy_table["max_positive_sum_record"] = record
                    if effdim > energy_table["max_effective_dimension"]:
                        energy_table["max_effective_dimension"] = effdim
                        energy_table["max_effective_dimension_record"] = record
                    if cauchy6_slack < energy_table["min_cauchy6_slack_over_sqrt"]:
                        energy_table["min_cauchy6_slack_over_sqrt"] = cauchy6_slack
                        energy_table["min_cauchy6_slack_record"] = record
                for key, l1_limit, l2_limit in DANGER_INTERSECTIONS:
                    if pos_sum < l1_limit or pos_l2 <= l2_limit:
                        continue
                    danger_table = table["danger_intersections"][key]
                    danger_table["record_count"] += 1
                    if pos_sum > danger_table["max_positive_sum_over_sqrt"]:
                        danger_table["max_positive_sum_over_sqrt"] = pos_sum
                    if pos_l2 > danger_table["max_positive_l2_over_sqrt"]:
                        danger_table["max_positive_l2_over_sqrt"] = pos_l2
                        danger_table["max_record"] = record

    return {
        "parameters": {
            "max_p": max_p,
            "alpha": alpha,
            "thresholds": thresholds,
            "prime_count": len(p_values),
        },
        "threshold_tables": list(threshold_tables.values()),
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC beta桶偏差包络扫描",
        "",
        "**状态：** `block_envelope_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `thresholds`: `{params['thresholds']}`",
        f"- `prime_count`: `{params['prime_count']}`",
        "",
    ]
    for table in result["threshold_tables"]:
        lines.extend(
            [
                f"## P>={table['threshold']}",
                "",
                f"- `record_count`: `{table['record_count']}`",
                f"- `max_total_positive_over_sqrt`: `{table['max_total_positive_over_sqrt']:.6f}`",
                f"- `max_positive_bucket_sum_over_sqrt`: `{table['max_positive_bucket_sum_over_sqrt']:.6f}`",
                f"- `max_positive_bucket_l2_over_sqrt`: `{table['max_positive_bucket_l2_over_sqrt']:.6f}`",
                f"- `sqrt(6)*max_positive_bucket_l2`: `{math.sqrt(6) * table['max_positive_bucket_l2_over_sqrt']:.6f}`",
                f"- `max_bucket_l2_over_sqrt`: `{table['max_bucket_l2_over_sqrt']:.6f}`",
                f"- `max_positive_bucket_effective_dimension`: `{table['max_positive_bucket_effective_dimension']:.6f}`",
                f"- `max_positive_bucket_cauchy6_bound_over_sqrt`: `{table['max_positive_bucket_cauchy6_bound_over_sqrt']:.6f}`",
                f"- `min_cauchy6_slack_when_bound_ge_3`: `{table['min_cauchy6_slack_when_bound_ge_3']:.6f}`",
                "",
                "| beta bucket | max positive/sqrt | positive record | max abs/sqrt | abs record |",
                "|---|---:|---|---:|---|",
            ]
        )
        for _left, _right, label in BETA_BUCKETS:
            env = table["envelope"][label]
            pos = env["max_positive_record"]
            abs_rec = env["max_abs_record"]
            pos_id = (
                f"P={pos['p']} {pos['side']} D={pos['bucket_discrepancy']:.3f}"
                if pos
                else ""
            )
            abs_id = (
                f"P={abs_rec['p']} {abs_rec['side']} D={abs_rec['bucket_discrepancy']:.3f}"
                if abs_rec
                else ""
            )
            lines.append(
                f"| {label} | {env['max_positive_over_sqrt']:.6f} | "
                f"{pos_id} | {env['max_abs_over_sqrt']:.6f} | {abs_id} |"
            )
        lines.append("")
        lines.extend(
            [
                "### 同步性阈值",
                "",
                "| positive sum threshold | records | max effective dimension | max positive L2/sqrt | min sqrt6 slack |",
                "|---:|---:|---:|---:|---:|",
            ]
        )
        for limit in SYNC_SUM_THRESHOLDS:
            row = table["sync_by_positive_sum_threshold"][str(limit)]
            lines.append(
                f"| {limit:.1f} | {row['record_count']} | "
                f"{row['max_effective_dimension']:.6f} | "
                f"{row['max_positive_l2_over_sqrt']:.6f} | "
                f"{row['min_cauchy6_slack_over_sqrt']:.6f} |"
            )
        lines.append("")
        lines.extend(
            [
                "### 能量阈值",
                "",
                "| positive L2 threshold | records | max positive sum | max effective dimension | min sqrt6 slack |",
                "|---:|---:|---:|---:|---:|",
            ]
        )
        for key, limit in ENERGY_L2_THRESHOLDS:
            row = table["sync_by_l2_threshold"][key]
            lines.append(
                f"| {limit:.6f} | {row['record_count']} | "
                f"{row['max_positive_sum_over_sqrt']:.6f} | "
                f"{row['max_effective_dimension']:.6f} | "
                f"{row['min_cauchy6_slack_over_sqrt']:.6f} |"
            )
        lines.append("")
        lines.extend(
            [
                "### 危险交集",
                "",
                "| intersection | L1 threshold | L2 threshold | records | max L1 | max L2 |",
                "|---|---:|---:|---:|---:|---:|",
            ]
        )
        for key, _l1_limit, _l2_limit in DANGER_INTERSECTIONS:
            row = table["danger_intersections"][key]
            max_l1 = row["max_positive_sum_over_sqrt"] if row["record_count"] else 0.0
            max_l2 = row["max_positive_l2_over_sqrt"] if row["record_count"] else 0.0
            lines.append(
                f"| {key} | {row['l1_threshold']:.6f} | "
                f"{row['l2_threshold']:.6f} | {row['record_count']} | "
                f"{max_l1:.6f} | {max_l2:.6f} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 结构解释",
            "",
            "若全局 `D_+<=3sqrt(S)` 要用桶级不等式证明，表中的 `max positive/sqrt` 给出每个 beta 桶需要覆盖的目标常数。若各桶最坏点不同，说明全局最大值不是单一尺度尖峰，而是多尺度中等偏差叠加；这更适合大筛/能量型证明。新增同步性阈值记录正偏差桶向量的有效维数与 Cauchy 松弛量：若 `sqrt(6)*L2` 只略超 3，但所有超界记录都有稳定松弛，就可以把硬点从单桶界推进到“六个尺度不能同时平坦同向”的结构命题。若某一桶长期主导，则应转入该桶的局部 PDEC/SAE 证书。",
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
        default="docs/dprc_block_envelope_scan_alpha043_p100000_20260506",
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
