#!/usr/bin/env python3
"""分解 DPRC 相对筛偏差的 q 尺度来源。

用法示例：
  python3 experiments/prime_matrix_dprc_block_discrepancy_audit.py \
    --records 30137:minus,21149:plus,10037:plus \
    --alpha 0.43 \
    --out-prefix docs/dprc_block_discrepancy_audit_20260506

这里固定 DPRC 的动态底座 Y=P^alpha，逐个剩余高素 q 计算
  d_q = #{k in S_Y: q | P^2±k} - |S_Y|/q，
并按 beta=log(q)/log(P) 分桶，定位正偏差来自哪些尺度。
"""

from __future__ import annotations

import argparse
import json
import math
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
    """按 q=P^beta 尺度分桶。"""
    edges = [0.43, 0.50, 0.60, 0.70, 0.80, 0.90, 1.01]
    labels = [
        "[0.43,0.50)",
        "[0.50,0.60)",
        "[0.60,0.70)",
        "[0.70,0.80)",
        "[0.80,0.90)",
        "[0.90,1.00)",
    ]
    for left, right, label in zip(edges, edges[1:], labels):
        if left <= beta < right:
            return label
    return "outside"


def add_bucket(table: dict[str, dict], key: str, hits: int, expected: float) -> None:
    """累加分桶统计。"""
    row = table.setdefault(
        key,
        {
            "q_count": 0,
            "hits": 0,
            "expected": 0.0,
            "discrepancy": 0.0,
            "positive_part": 0.0,
            "negative_part": 0.0,
        },
    )
    discrepancy = hits - expected
    row["q_count"] += 1
    row["hits"] += hits
    row["expected"] += expected
    row["discrepancy"] += discrepancy
    if discrepancy >= 0:
        row["positive_part"] += discrepancy
    else:
        row["negative_part"] += discrepancy


def audit_one(p: int, side: str, alpha: float, primes: list[int]) -> dict:
    """审计单个 P/side 的 q 分桶偏差。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    rows = []
    bucket_rows: dict[str, dict] = {}
    floor_rows: dict[str, dict] = {}

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if alive[k]:
                hits += 1
        expected = skeleton / q
        discrepancy = hits - expected
        beta = math.log(q) / math.log(p)
        bucket = beta_bucket(beta)
        floor_bucket = f"floor(P/q)={p//q}" if p // q <= 10 else "floor(P/q)>10"
        add_bucket(bucket_rows, bucket, hits, expected)
        add_bucket(floor_rows, floor_bucket, hits, expected)
        rows.append(
            {
                "q": q,
                "beta": beta,
                "floor_p_over_q": p // q,
                "hits": hits,
                "expected": expected,
                "discrepancy": discrepancy,
                "bucket": bucket,
            }
        )

    total_hits = sum(row["hits"] for row in rows)
    expected_total = sum(row["expected"] for row in rows)
    discrepancy_total = total_hits - expected_total
    sqrt_s = math.sqrt(skeleton)
    return {
        "p": p,
        "side": side,
        "alpha": alpha,
        "cutoff": cutoff,
        "skeleton_count": skeleton,
        "total_hits": total_hits,
        "expected_total": expected_total,
        "discrepancy_total": discrepancy_total,
        "discrepancy_over_sqrt": discrepancy_total / sqrt_s if sqrt_s else 0.0,
        "capacity_margin": skeleton - total_hits,
        "bucket_rows": [
            {"bucket": key, **value}
            for key, value in sorted(bucket_rows.items())
        ],
        "floor_rows": [
            {"bucket": key, **value}
            for key, value in sorted(floor_rows.items())
        ],
        "top_positive_q": sorted(rows, key=lambda row: -row["discrepancy"])[:15],
        "top_negative_q": sorted(rows, key=lambda row: row["discrepancy"])[:15],
    }


def parse_records(raw: str) -> list[tuple[int, str]]:
    """解析 P:side 列表。"""
    parsed = []
    for item in raw.split(","):
        if not item.strip():
            continue
        p_raw, side = item.split(":")
        parsed.append((int(p_raw), side.strip()))
    return parsed


def audit(records: list[tuple[int, str]], alpha: float) -> dict:
    """执行多个记录的审计。"""
    max_p = max(p for p, _side in records)
    primes = primes_from_flags(sieve_bool(max_p))
    return {
        "parameters": {"records": records, "alpha": alpha},
        "records": [audit_one(p, side, alpha, primes) for p, side in records],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC q尺度偏差分解审计",
        "",
        "**状态：** `block_discrepancy_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `records`: `{params['records']}`",
        f"- `alpha`: `{params['alpha']}`",
        "",
    ]
    for record in result["records"]:
        lines.extend(
            [
                f"## P={record['p']}, side={record['side']}",
                "",
                f"- `cutoff`: `{record['cutoff']}`",
                f"- `S`: `{record['skeleton_count']}`",
                f"- `T`: `{record['total_hits']}`",
                f"- `expected`: `{record['expected_total']:.6f}`",
                f"- `D/sqrt(S)`: `{record['discrepancy_over_sqrt']:.6f}`",
                f"- `capacity_margin`: `{record['capacity_margin']}`",
                "",
                "### beta buckets",
                "",
                "| bucket | q count | hits | expected | discrepancy | positive | negative |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["bucket_rows"]:
            lines.append(
                f"| {row['bucket']} | {row['q_count']} | {row['hits']} | "
                f"{row['expected']:.6f} | {row['discrepancy']:.6f} | "
                f"{row['positive_part']:.6f} | {row['negative_part']:.6f} |"
            )

        lines.extend(
            [
                "",
                "### floor(P/q) buckets",
                "",
                "| bucket | q count | hits | expected | discrepancy | positive | negative |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["floor_rows"]:
            lines.append(
                f"| {row['bucket']} | {row['q_count']} | {row['hits']} | "
                f"{row['expected']:.6f} | {row['discrepancy']:.6f} | "
                f"{row['positive_part']:.6f} | {row['negative_part']:.6f} |"
            )

        lines.extend(
            [
                "",
                "### top positive q",
                "",
                "| q | beta | floor(P/q) | hits | expected | discrepancy |",
                "|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["top_positive_q"]:
            lines.append(
                f"| {row['q']} | {row['beta']:.6f} | {row['floor_p_over_q']} | "
                f"{row['hits']} | {row['expected']:.6f} | "
                f"{row['discrepancy']:.6f} |"
            )
        lines.extend(
            [
                "",
                "### top negative q",
                "",
                "| q | beta | floor(P/q) | hits | expected | discrepancy |",
                "|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["top_negative_q"]:
            lines.append(
                f"| {row['q']} | {row['beta']:.6f} | {row['floor_p_over_q']} | "
                f"{row['hits']} | {row['expected']:.6f} | "
                f"{row['discrepancy']:.6f} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 结构解释",
            "",
            "这份审计用于定位 `T-HS` 的正偏差来源。若偏差集中在少数 `beta` 或 `floor(P/q)` 桶，下一步应对该桶建立局部容量/相位证书；若偏差在所有桶内分散，则更适合使用大筛型能量界。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--records",
        default="30137:minus,21149:plus,19997:minus,95581:minus,10037:plus",
    )
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_block_discrepancy_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_records(args.records), args.alpha)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
