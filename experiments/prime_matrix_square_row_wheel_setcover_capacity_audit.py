#!/usr/bin/env python3
"""审计平方前后两行在轮骨架上的高素斜线集合覆盖容量。

用法示例：
  python3 experiments/prime_matrix_square_row_wheel_setcover_capacity_audit.py \
    --primes 10007,36739,95093,99991 --wheels 210,2310 \
    --out-prefix docs/square_row_wheel_setcover_capacity_audit_20260506

结构恒等式：
  P^2+k=q*m 命中 W 轮骨架 <=> q,m 都是 W 的单位类。
  P^2-k=q*m 命中 W 轮骨架 <=> q,m 都是 W 的单位类。

因此每条高素 q 斜线的容量，是一个短 m 区间中的单位类计数。
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


def primes_from_table(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def factor_distinct(value: int) -> list[int]:
    """返回 value 的不同素因子。"""
    factors = []
    n = value
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            factors.append(factor)
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def units(modulus: int) -> set[int]:
    """返回模 modulus 的单位剩余类集合。"""
    return {residue for residue in range(modulus) if math.gcd(residue, modulus) == 1}


def wheel_skeleton(p: int, modulus: int, side: str, unit_set: set[int]) -> set[int]:
    """返回 1<=k<P 中 P^2±k 避开 W 的偏移集合。"""
    p2 = (p * p) % modulus
    if side == "plus":
        residues = {(unit - p2) % modulus for unit in unit_set}
    elif side == "minus":
        residues = {(p2 - unit) % modulus for unit in unit_set}
    else:
        raise ValueError(f"unknown side: {side}")
    return {k for k in range(1, p) if k % modulus in residues}


def m_interval_for_q(p: int, q: int, side: str) -> tuple[int, int]:
    """返回 q*m 落入平方前/后行时的 m 区间。"""
    if side == "plus":
        low = p * p + 1
        high = p * p + p - 1
    elif side == "minus":
        low = p * p - p + 1
        high = p * p - 1
    else:
        raise ValueError(f"unknown side: {side}")
    m_min = (low + q - 1) // q
    m_max = high // q
    return m_min, m_max


def k_from_qm(p: int, q: int, m: int, side: str) -> int:
    """由 q*m 还原偏移 k。"""
    if side == "plus":
        return q * m - p * p
    if side == "minus":
        return p * p - q * m
    raise ValueError(f"unknown side: {side}")


def bucket_for_q(p: int, q: int) -> str:
    """按 q/P 的倒数层分桶。"""
    t = p // q
    if t <= 8:
        return f"floor(P/q)={t}"
    if q * 20 >= p:
        return "9<=floor(P/q)<=19"
    if q * 50 >= p:
        return "20<=floor(P/q)<=49"
    if q * 100 >= p:
        return "50<=floor(P/q)<=99"
    return "floor(P/q)>=100"


def audit_one(p: int, modulus: int, side: str, prime_flags: bytearray) -> dict:
    """审计单个 P,W,side。"""
    factors = factor_distinct(modulus)
    unit_set = units(modulus)
    skeleton = wheel_skeleton(p, modulus, side, unit_set)
    covered: dict[int, int] = {}
    hit_labels: dict[int, list[int]] = {}
    q_records = []
    bucket_stats: dict[str, dict] = {}

    for q in primes_from_table(prime_flags[:p]):
        if q in factors or q == p:
            continue
        if math.gcd(q, modulus) != 1:
            continue
        m_min, m_max = m_interval_for_q(p, q, side)
        hits = []
        for m in range(m_min, m_max + 1):
            if m % modulus not in unit_set:
                continue
            k = k_from_qm(p, q, m, side)
            if 1 <= k < p:
                hits.append(k)
                hit_labels.setdefault(k, []).append(q)
                covered[k] = covered.get(k, 0) + 1
        if not hits:
            continue
        bucket = bucket_for_q(p, q)
        stats = bucket_stats.setdefault(
            bucket,
            {
                "q_count": 0,
                "total_hits": 0,
                "unique_hits": set(),
                "max_hits": 0,
                "max_q": None,
            },
        )
        stats["q_count"] += 1
        stats["total_hits"] += len(hits)
        stats["unique_hits"].update(hits)
        if len(hits) > stats["max_hits"]:
            stats["max_hits"] = len(hits)
            stats["max_q"] = q
        q_records.append(
            {
                "q": q,
                "bucket": bucket,
                "m_min": m_min,
                "m_max": m_max,
                "hit_count": len(hits),
                "first_hits": hits[:8],
            }
        )

    uncovered = sorted(skeleton - set(covered))
    total_hits = sum(record["hit_count"] for record in q_records)
    bucket_rows = []
    for bucket, stats in bucket_stats.items():
        unique_count = len(stats["unique_hits"])
        bucket_rows.append(
            {
                "bucket": bucket,
                "q_count": stats["q_count"],
                "total_hits": stats["total_hits"],
                "unique_hits": unique_count,
                "overlap_excess": stats["total_hits"] - unique_count,
                "max_hits": stats["max_hits"],
                "max_q": stats["max_q"],
            }
        )
    bucket_rows.sort(key=lambda item: item["bucket"])

    top_q = sorted(q_records, key=lambda item: -item["hit_count"])[:12]
    top_overlap = sorted(
        (
            {"k": k, "label_count": len(labels), "labels": labels[:12]}
            for k, labels in hit_labels.items()
            if len(labels) >= 2
        ),
        key=lambda item: -item["label_count"],
    )[:12]
    return {
        "p": p,
        "modulus": modulus,
        "side": side,
        "factors": factors,
        "skeleton_count": len(skeleton),
        "covered_count": len(covered),
        "uncovered_count": len(uncovered),
        "uncovered_first": uncovered[:20],
        "total_hits": total_hits,
        "overlap_excess": total_hits - len(covered),
        "max_label_multiplicity": max((len(v) for v in hit_labels.values()), default=0),
        "top_q": top_q,
        "top_overlap": top_overlap,
        "bucket_rows": bucket_rows,
    }


def audit(primes: list[int], wheels: list[int]) -> dict:
    """执行审计。"""
    max_p = max(primes)
    prime_flags = sieve_bool(max_p)
    records = []
    for p in primes:
        for modulus in wheels:
            for side in ("minus", "plus"):
                records.append(audit_one(p, modulus, side, prime_flags))
    return {"parameters": {"primes": primes, "wheels": wheels}, "records": records}


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 平方前后两行轮骨架集合覆盖容量审计",
        "",
        "**状态：** `wheel_setcover_capacity_structural_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `primes`: `{params['primes']}`",
        f"- `wheels`: `{params['wheels']}`",
        "",
        "## 总表",
        "",
        "| P | W | side | skeleton | covered | uncovered | total hits | overlap excess | max mult |",
        "|---:|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['modulus']} | {record['side']} | "
            f"{record['skeleton_count']} | {record['covered_count']} | "
            f"{record['uncovered_count']} | {record['total_hits']} | "
            f"{record['overlap_excess']} | {record['max_label_multiplicity']} |"
        )

    lines.extend(["", "## 分桶明细", ""])
    for record in result["records"]:
        lines.extend(
            [
                f"### P={record['p']}, W={record['modulus']}, side={record['side']}",
                "",
                f"- `uncovered_first`: `{record['uncovered_first']}`",
                "",
                "| q bucket | q count | total hits | unique hits | overlap excess | max hits | max q |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["bucket_rows"]:
            lines.append(
                f"| {row['bucket']} | {row['q_count']} | {row['total_hits']} | "
                f"{row['unique_hits']} | {row['overlap_excess']} | "
                f"{row['max_hits']} | {row['max_q']} |"
            )
        lines.extend(
            [
                "",
                "Top q lines:",
                "",
                "| q | bucket | hit count | m interval | first hits |",
                "|---:|---|---:|---|---|",
            ]
        )
        for row in record["top_q"]:
            lines.append(
                f"| {row['q']} | {row['bucket']} | {row['hit_count']} | "
                f"[{row['m_min']},{row['m_max']}] | {row['first_hits']} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 审稿解释",
            "",
            "每条高素 q 斜线不再被看成随机命中列，而是被写成短互补因子窗口中的单位类计数。若 `uncovered_count>0`，这些未覆盖偏移就是该轮骨架下的端点幸存点。若某个坏窗试图让 `uncovered_count=0`，必须让多个 q 桶在同一轮平移骨架上形成异常集合覆盖；这就是 `Wheel-Rigid Set Cover -> PDEC/SAE/ColumnCRT` 的证书入口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="10007,36739,95093,99991")
    parser.add_argument("--wheels", default="210,2310")
    parser.add_argument(
        "--out-prefix",
        default="docs/square_row_wheel_setcover_capacity_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.primes), parse_ints(args.wheels))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
