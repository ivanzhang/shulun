#!/usr/bin/env python3
"""审计 DPRC-BES 近危险样本的结构来源。

用法示例：
  python3 experiments/prime_matrix_dprc_bes_nearmiss_structure_audit.py \
    --records 30137:minus,83267:plus,19997:minus,21149:plus,80489:minus \
    --alpha 0.43 \
    --out-prefix docs/dprc_bes_nearmiss_structure_audit_20260506

目标：
  对 BES 的高 L1 / 高 L2 / 高有效维数近危险样本，分解三类结构：
  1. PointLoad：单个 k 被多少剩余高素 q 命中；
  2. ShortWindow：某个 q 子窗口是否贡献了大比例正偏差；
  3. LowPhase：低模投影上是否出现明显正偏斜。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


BETA_BUCKETS = [
    (0.43, 0.50, "[0.43,0.50)"),
    (0.50, 0.60, "[0.50,0.60)"),
    (0.60, 0.70, "[0.60,0.70)"),
    (0.70, 0.80, "[0.70,0.80)"),
    (0.80, 0.90, "[0.80,0.90)"),
    (0.90, 1.01, "[0.90,1.00)"),
]
LOW_MODS = [30, 210, 2310]


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


def empty_bucket_rows() -> dict[str, dict]:
    """初始化 beta 桶统计。"""
    return {
        label: {
            "q_count": 0,
            "hits": 0,
            "expected": 0.0,
            "discrepancy": 0.0,
            "positive_q_discrepancy": 0.0,
            "negative_q_discrepancy": 0.0,
            "harmonic": 0.0,
        }
        for _left, _right, label in BETA_BUCKETS
    }


def skeleton_residue_counts(alive: bytearray, mods: list[int]) -> dict[int, list[int]]:
    """统计动态粗骨架在低模下的残基分布。"""
    counts = {mod: [0] * mod for mod in mods}
    for k, flag in enumerate(alive):
        if not flag:
            continue
        for mod in mods:
            counts[mod][k % mod] += 1
    return counts


def point_load_summary(point_hits: dict[int, list[int]], p: int, side: str) -> dict:
    """汇总单点高素标签负载。"""
    histogram = Counter(len(labels) for labels in point_hits.values())
    top_points = []
    for k, labels in sorted(point_hits.items(), key=lambda item: -len(item[1]))[:10]:
        n_value = p * p + k if side == "plus" else p * p - k
        top_points.append(
            {
                "k": k,
                "n": n_value,
                "load": len(labels),
                "q_labels": labels[:20],
                "cofactors": [n_value // q for q in labels[:20]],
            }
        )
    return {
        "max_load": max(histogram) if histogram else 0,
        "load_histogram": dict(sorted(histogram.items())),
        "top_points": top_points,
    }


def short_window_summary(
    q_rows: list[dict], subblocks: int, sqrt_s: float
) -> list[dict]:
    """按 beta 桶切 q 子窗口，定位短窗口正偏差。"""
    summaries = []
    for _left, _right, label in BETA_BUCKETS:
        rows = [row for row in q_rows if row["bucket"] == label]
        if not rows:
            continue
        rows.sort(key=lambda row: row["q"])
        chunk_count = min(subblocks, len(rows))
        chunks = []
        for idx in range(chunk_count):
            start = (len(rows) * idx) // chunk_count
            end = (len(rows) * (idx + 1)) // chunk_count
            chunk = rows[start:end]
            hits = sum(row["hits"] for row in chunk)
            expected = sum(row["expected"] for row in chunk)
            discrepancy = hits - expected
            chunks.append(
                {
                    "index": idx,
                    "q_min": chunk[0]["q"],
                    "q_max": chunk[-1]["q"],
                    "q_count": len(chunk),
                    "hits": hits,
                    "expected": expected,
                    "discrepancy": discrepancy,
                    "discrepancy_over_sqrt": discrepancy / sqrt_s if sqrt_s else 0.0,
                }
            )
        bucket_disc = sum(row["discrepancy"] for row in rows)
        top_chunk = max(chunks, key=lambda row: row["discrepancy"])
        positive_disc = sum(max(0.0, row["discrepancy"]) for row in chunks)
        summaries.append(
            {
                "bucket": label,
                "q_count": len(rows),
                "bucket_discrepancy": bucket_disc,
                "bucket_discrepancy_over_sqrt": bucket_disc / sqrt_s
                if sqrt_s
                else 0.0,
                "max_chunk_positive_over_sqrt": max(
                    0.0, top_chunk["discrepancy_over_sqrt"]
                ),
                "top_chunk_share_of_positive": (
                    max(0.0, top_chunk["discrepancy"]) / positive_disc
                    if positive_disc > 0
                    else 0.0
                ),
                "top_chunks": sorted(
                    chunks, key=lambda row: -row["discrepancy"]
                )[:4],
            }
        )
    return summaries


def low_phase_summary(
    p: int,
    side: str,
    skeleton_counts: dict[int, list[int]],
    lowphase_actual: dict[str, dict[int, list[int]]],
    harmonic_by_label: dict[str, float],
    sqrt_s: float,
) -> list[dict]:
    """汇总低模投影偏斜。"""
    rows = []
    for label, mod_tables in lowphase_actual.items():
        harmonic = harmonic_by_label[label]
        for mod, actual in mod_tables.items():
            discrepancies = [
                actual[residue] - skeleton_counts[mod][residue] * harmonic
                for residue in range(mod)
            ]
            positive = [max(0.0, value) for value in discrepancies]
            abs_values = [abs(value) for value in discrepancies]
            max_pos = max(positive) if positive else 0.0
            max_abs = max(abs_values) if abs_values else 0.0
            top_residues = sorted(
                [
                    {
                        "residue": residue,
                        "n_residue": (
                            (p * p + residue) % mod
                            if side == "plus"
                            else (p * p - residue) % mod
                        ),
                        "n_residue_is_unit": math.gcd(
                            (
                                (p * p + residue) % mod
                                if side == "plus"
                                else (p * p - residue) % mod
                            ),
                            mod,
                        )
                        == 1,
                        "actual": actual[residue],
                        "expected": skeleton_counts[mod][residue] * harmonic,
                        "discrepancy": discrepancies[residue],
                        "discrepancy_over_sqrt": discrepancies[residue] / sqrt_s
                        if sqrt_s
                        else 0.0,
                    }
                    for residue in range(mod)
                ],
                key=lambda row: -row["discrepancy"],
            )[:6]
            rows.append(
                {
                    "label": label,
                    "mod": mod,
                    "harmonic": harmonic,
                    "max_positive_over_sqrt": max_pos / sqrt_s if sqrt_s else 0.0,
                    "max_abs_over_sqrt": max_abs / sqrt_s if sqrt_s else 0.0,
                    "positive_l1_over_sqrt": sum(positive) / sqrt_s
                    if sqrt_s
                    else 0.0,
                    "positive_l2_over_sqrt": math.sqrt(
                        sum(value * value for value in positive)
                    )
                    / sqrt_s
                    if sqrt_s
                    else 0.0,
                    "top_residues": top_residues,
                }
            )
    return sorted(rows, key=lambda row: -row["max_positive_over_sqrt"])


def audit_one(
    p: int,
    side: str,
    alpha: float,
    primes: list[int],
    subblocks: int,
    low_mods: list[int],
) -> dict:
    """审计单个 P/side 近危险样本。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    sqrt_s = math.sqrt(skeleton)
    skeleton_counts = skeleton_residue_counts(alive, low_mods)
    bucket_rows = empty_bucket_rows()
    q_rows = []
    point_hits: dict[int, list[int]] = defaultdict(list)
    all_label = "all"
    lowphase_actual: dict[str, dict[int, list[int]]] = {
        all_label: {mod: [0] * mod for mod in low_mods}
    }
    harmonic_by_label = {all_label: 0.0}
    for _left, _right, label in BETA_BUCKETS:
        lowphase_actual[label] = {mod: [0] * mod for mod in low_mods}
        harmonic_by_label[label] = 0.0

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        beta = math.log(q) / math.log(p)
        label = beta_bucket(beta)
        if label == "outside":
            continue
        hits = []
        for k in range(start, p, q):
            if alive[k]:
                hits.append(k)
                point_hits[k].append(q)
                for mod in low_mods:
                    lowphase_actual[all_label][mod][k % mod] += 1
                    lowphase_actual[label][mod][k % mod] += 1
        expected = skeleton / q
        discrepancy = len(hits) - expected
        harmonic_by_label[all_label] += 1.0 / q
        harmonic_by_label[label] += 1.0 / q
        bucket = bucket_rows[label]
        bucket["q_count"] += 1
        bucket["hits"] += len(hits)
        bucket["expected"] += expected
        bucket["discrepancy"] += discrepancy
        bucket["harmonic"] += 1.0 / q
        if discrepancy >= 0:
            bucket["positive_q_discrepancy"] += discrepancy
        else:
            bucket["negative_q_discrepancy"] += discrepancy
        q_rows.append(
            {
                "q": q,
                "beta": beta,
                "bucket": label,
                "floor_p_over_q": p // q,
                "hits": len(hits),
                "expected": expected,
                "discrepancy": discrepancy,
            }
        )

    bucket_vector = [
        bucket_rows[label]["discrepancy"] / sqrt_s if sqrt_s else 0.0
        for _left, _right, label in BETA_BUCKETS
    ]
    positive_vector = [max(0.0, value) for value in bucket_vector]
    positive_l1 = sum(positive_vector)
    positive_l2 = math.sqrt(sum(value * value for value in positive_vector))
    effective_dimension = (
        (positive_l1 * positive_l1) / (positive_l2 * positive_l2)
        if positive_l2
        else 0.0
    )
    total_hits = sum(row["hits"] for row in q_rows)
    total_expected = sum(row["expected"] for row in q_rows)
    return {
        "p": p,
        "side": side,
        "alpha": alpha,
        "cutoff": cutoff,
        "skeleton_count": skeleton,
        "sqrt_skeleton": sqrt_s,
        "total_hits": total_hits,
        "total_expected": total_expected,
        "total_discrepancy": total_hits - total_expected,
        "total_discrepancy_over_sqrt": (total_hits - total_expected) / sqrt_s
        if sqrt_s
        else 0.0,
        "positive_bucket_l1_over_sqrt": positive_l1,
        "positive_bucket_l2_over_sqrt": positive_l2,
        "positive_bucket_effective_dimension": effective_dimension,
        "bucket_rows": [
            {
                "bucket": label,
                **bucket_rows[label],
                "discrepancy_over_sqrt": bucket_rows[label]["discrepancy"] / sqrt_s
                if sqrt_s
                else 0.0,
            }
            for _left, _right, label in BETA_BUCKETS
        ],
        "point_load": point_load_summary(point_hits, p, side),
        "short_window": short_window_summary(q_rows, subblocks, sqrt_s),
        "low_phase": low_phase_summary(
            p,
            side,
            skeleton_counts,
            lowphase_actual,
            harmonic_by_label,
            sqrt_s,
        ),
        "top_positive_q": sorted(q_rows, key=lambda row: -row["discrepancy"])[:12],
    }


def parse_records(raw: str) -> list[tuple[int, str]]:
    """解析 P:side 列表。"""
    records = []
    for item in raw.split(","):
        if not item.strip():
            continue
        p_raw, side = item.split(":")
        records.append((int(p_raw), side.strip()))
    return records


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def audit(
    records: list[tuple[int, str]], alpha: float, subblocks: int, low_mods: list[int]
) -> dict:
    """执行近危险结构审计。"""
    max_p = max(p for p, _side in records)
    primes = primes_from_flags(sieve_bool(max_p))
    return {
        "parameters": {
            "records": records,
            "alpha": alpha,
            "subblocks": subblocks,
            "low_mods": low_mods,
        },
        "records": [
            audit_one(p, side, alpha, primes, subblocks, low_mods)
            for p, side in records
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC-BES 近危险结构审计",
        "",
        "**状态：** `nearmiss_structure_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `records`: `{params['records']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `subblocks`: `{params['subblocks']}`",
        f"- `low_mods`: `{params['low_mods']}`",
        "",
    ]
    for record in result["records"]:
        lines.extend(
            [
                f"## P={record['p']} {record['side']}",
                "",
                f"- `S`: `{record['skeleton_count']}`",
                f"- `T`: `{record['total_hits']}`",
                f"- `D/sqrt(S)`: `{record['total_discrepancy_over_sqrt']:.6f}`",
                f"- `positive L1`: `{record['positive_bucket_l1_over_sqrt']:.6f}`",
                f"- `positive L2`: `{record['positive_bucket_l2_over_sqrt']:.6f}`",
                f"- `effective dimension`: `{record['positive_bucket_effective_dimension']:.6f}`",
                f"- `max point load`: `{record['point_load']['max_load']}`",
                "",
                "### beta桶",
                "",
                "| bucket | q count | hits | expected | D/sqrt | positive q D |",
                "|---|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["bucket_rows"]:
            lines.append(
                f"| {row['bucket']} | {row['q_count']} | {row['hits']} | "
                f"{row['expected']:.3f} | {row['discrepancy_over_sqrt']:.6f} | "
                f"{row['positive_q_discrepancy']:.3f} |"
            )
        lines.extend(
            [
                "",
                "### PointLoad",
                "",
                f"- `load_histogram`: `{record['point_load']['load_histogram']}`",
                "",
                "| k | n | load | q labels |",
                "|---:|---:|---:|---|",
            ]
        )
        for row in record["point_load"]["top_points"][:5]:
            lines.append(
                f"| {row['k']} | {row['n']} | {row['load']} | "
                f"`{row['q_labels']}` |"
            )
        lines.extend(
            [
                "",
                "### ShortWindow",
                "",
                "| bucket | max chunk D/sqrt | top chunk share | top q interval |",
                "|---|---:|---:|---|",
            ]
        )
        for row in record["short_window"]:
            top = row["top_chunks"][0]
            lines.append(
                f"| {row['bucket']} | {row['max_chunk_positive_over_sqrt']:.6f} | "
                f"{row['top_chunk_share_of_positive']:.6f} | "
                f"`[{top['q_min']},{top['q_max']}]` |"
            )
        lines.extend(
            [
                "",
                "### LowPhase",
                "",
                "| label | mod | max positive/sqrt | positive L1/sqrt | positive L2/sqrt | top residue |",
                "|---|---:|---:|---:|---:|---|",
            ]
        )
        for row in record["low_phase"][:12]:
            top = row["top_residues"][0]
            lines.append(
                f"| {row['label']} | {row['mod']} | "
                f"{row['max_positive_over_sqrt']:.6f} | "
                f"{row['positive_l1_over_sqrt']:.6f} | "
                f"{row['positive_l2_over_sqrt']:.6f} | "
                f"`k={top['residue']}, n={top['n_residue']}, "
                f"unit={top['n_residue_is_unit']} (D={top['discrepancy']:.3f})` |"
            )
        lines.extend(
            [
                "",
                "### Top q",
                "",
                "| q | beta | bucket | hits | expected | D |",
                "|---:|---:|---|---:|---:|---:|",
            ]
        )
        for row in record["top_positive_q"][:8]:
            lines.append(
                f"| {row['q']} | {row['beta']:.6f} | {row['bucket']} | "
                f"{row['hits']} | {row['expected']:.3f} | {row['discrepancy']:.3f} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 结构读法",
            "",
            "`PointLoad` 若很高，说明少数列承载过多高素标签，应进入 `ColumnCRT/tail-anchor`；`ShortWindow` 若由单个 q 子窗贡献大比例正偏差，应进入 `SAE`；`LowPhase` 若低模投影有大峰值，则进入 `PDEC`。三者都不尖锐时，BES 失败只能来自真正多尺度分散同步，下一步应走对偶大筛能量界。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--records",
        default="30137:minus,83267:plus,19997:minus,21149:plus,80489:minus",
    )
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--subblocks", type=int, default=8)
    parser.add_argument("--low-mods", default="30,210,2310")
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_bes_nearmiss_structure_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_records(args.records),
        args.alpha,
        args.subblocks,
        parse_ints(args.low_mods),
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
