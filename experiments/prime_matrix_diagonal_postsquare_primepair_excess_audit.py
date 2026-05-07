#!/usr/bin/env python3
"""审计平方后端点的倒数地板素-素曲线覆盖缺口。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_primepair_excess_audit.py --max-p 20000

对 n=p^2+k, 1<=k<p，低筛骨架为 P^-(n)>y 的列。
当 p>=23 时，一尾覆盖点等价于
  p^2+k = ell*m,
  y<ell<p<m,
  ell,m 均为素数，
且 m=floor(p^2/ell)+s, s=1,2,3。
本脚本审计这些三条倒数地板曲线是否接近完美覆盖低筛骨架。
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


def primes_from_table(flags: bytearray, limit: int | None = None) -> list[int]:
    """提取素数列表。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(end) if flags[idx]]


def audit_p(p: int, primes: list[int], prime_flags: bytearray, y_ratio: float) -> dict:
    """审计单个 p 的低骨架与三曲线素-素覆盖。"""
    y = max(2, int(math.floor(y_ratio * p)))
    low_primes = [prime for prime in primes if prime <= y]
    tail_primes = [prime for prime in primes if y < prime < p]
    p_square = p * p

    low_rough = bytearray(b"\x01") * p
    low_rough[0] = 0
    for ell in low_primes:
        residue = (-(p % ell) * (p % ell)) % ell
        start = residue if residue != 0 else ell
        if start >= p:
            continue
        low_rough[start:p:ell] = b"\x00" * (((p - 1 - start) // ell) + 1)

    low_skeleton = sum(low_rough)
    covered_columns: set[int] = set()
    bad_low_columns = []
    offset_counts: dict[int, int] = {}
    offset_covered_counts: dict[int, int] = {}
    candidate_pairs = 0
    samples = []

    for ell in tail_primes:
        base = p_square // ell
        right = (p_square + p - 1) // ell
        for m in range(base + 1, right + 1):
            if m >= len(prime_flags) or not prime_flags[m]:
                continue
            column = ell * m - p_square
            if not (1 <= column < p):
                continue
            offset = m - base
            candidate_pairs += 1
            offset_counts[offset] = offset_counts.get(offset, 0) + 1
            if low_rough[column]:
                covered_columns.add(column)
                offset_covered_counts[offset] = offset_covered_counts.get(offset, 0) + 1
            elif len(bad_low_columns) < 5:
                bad_low_columns.append(
                    {
                        "ell": ell,
                        "m": m,
                        "offset": offset,
                        "column": column,
                        "value": ell * m,
                    }
                )
            if len(samples) < 5:
                samples.append(
                    {
                        "ell": ell,
                        "m": m,
                        "offset": offset,
                        "column": column,
                        "value": ell * m,
                        "low_rough_column": bool(low_rough[column]),
                    }
                )

    covered = len(covered_columns)
    duplicate_pairs = candidate_pairs - covered
    margin = low_skeleton - covered
    cover_ratio = covered / low_skeleton if low_skeleton else 0.0
    margin_ratio = margin / low_skeleton if low_skeleton else 0.0
    log_p = math.log(p)

    return {
        "p": p,
        "y": y,
        "low_prime_count": len(low_primes),
        "tail_prime_count": len(tail_primes),
        "low_skeleton": low_skeleton,
        "prime_pair_candidates": candidate_pairs,
        "covered_columns": covered,
        "duplicate_pairs": duplicate_pairs,
        "margin": margin,
        "cover_ratio": cover_ratio,
        "margin_ratio": margin_ratio,
        "low_scaled": low_skeleton * log_p / p,
        "cover_scaled_log2": covered * log_p * log_p / p,
        "offset_counts": {
            str(key): offset_counts[key] for key in sorted(offset_counts)
        },
        "offset_covered_counts": {
            str(key): offset_covered_counts[key]
            for key in sorted(offset_covered_counts)
        },
        "bad_low_columns": bad_low_columns,
        "samples": samples,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    prime_limit = int(math.ceil(math.e * (max_p + 1))) + 100
    prime_flags = sieve_bool(prime_limit)
    primes = primes_from_table(prime_flags, max_p)
    target_primes = [prime for prime in primes if prime >= 23]
    records = [audit_p(p, primes, prime_flags, y_ratio) for p in target_primes]

    worst_cover = sorted(records, key=lambda item: -item["cover_ratio"])[:20]
    worst_margin = sorted(records, key=lambda item: item["margin"])[:20]
    bad_low = [record for record in records if record["bad_low_columns"]]
    duplicate_records = [record for record in records if record["duplicate_pairs"]]

    threshold_summary = []
    for threshold in [23, 101, 251, 501, 1009, 2003, 5003, 10007, 20011, 50021]:
        subset = [record for record in records if record["p"] >= threshold]
        if not subset:
            continue
        max_cover = max(subset, key=lambda item: item["cover_ratio"])
        min_margin_ratio = min(subset, key=lambda item: item["margin_ratio"])
        min_margin = min(subset, key=lambda item: item["margin"])
        threshold_summary.append(
            {
                "threshold": threshold,
                "max_cover_ratio_record": {
                    "p": max_cover["p"],
                    "cover_ratio": max_cover["cover_ratio"],
                    "low_skeleton": max_cover["low_skeleton"],
                    "covered_columns": max_cover["covered_columns"],
                },
                "min_margin_ratio_record": {
                    "p": min_margin_ratio["p"],
                    "margin_ratio": min_margin_ratio["margin_ratio"],
                    "margin": min_margin_ratio["margin"],
                    "low_skeleton": min_margin_ratio["low_skeleton"],
                },
                "min_margin_record": {
                    "p": min_margin["p"],
                    "margin": min_margin["margin"],
                    "low_skeleton": min_margin["low_skeleton"],
                    "covered_columns": min_margin["covered_columns"],
                },
            }
        )

    global_offsets: dict[str, int] = {}
    for record in records:
        for key, value in record["offset_covered_counts"].items():
            global_offsets[key] = global_offsets.get(key, 0) + value

    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "bad_low_column_record_count": len(bad_low),
            "duplicate_record_count": len(duplicate_records),
            "min_margin": min((record["margin"] for record in records), default=None),
            "max_cover_ratio": max(
                (record["cover_ratio"] for record in records), default=None
            ),
            "min_margin_ratio": min(
                (record["margin_ratio"] for record in records), default=None
            ),
            "global_offset_covered_counts": {
                key: global_offsets[key] for key in sorted(global_offsets, key=int)
            },
            "worst_cover_records": worst_cover,
            "worst_margin_records": worst_margin,
            "threshold_summary": threshold_summary,
        },
        "bad_low_records": bad_low[:20],
        "duplicate_records": duplicate_records[:20],
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点倒数地板素对覆盖缺口审计",
        "",
        "**状态：** `experimental_reciprocal_floor_prime_pair_excess_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查 `p>=23` 奇素数个数：`{summary['prime_count']}`。",
        f"- 非低骨架候选记录数：`{summary['bad_low_column_record_count']}`。",
        f"- 重复覆盖记录数：`{summary['duplicate_record_count']}`。",
        f"- 最小余量：`{summary['min_margin']}`。",
        f"- 最大覆盖比例：`{summary['max_cover_ratio']}`。",
        f"- 最小余量比例：`{summary['min_margin_ratio']}`。",
        f"- 三曲线覆盖 offset 分布：`{summary['global_offset_covered_counts']}`。",
        "",
        "## 阈值账本",
        "",
        "| threshold | max cover record | min margin ratio record | min margin record |",
        "|---:|---|---|---|",
    ]
    for item in summary["threshold_summary"]:
        lines.append(
            f"| {item['threshold']} | {item['max_cover_ratio_record']} | "
            f"{item['min_margin_ratio_record']} | {item['min_margin_record']} |"
        )

    lines.extend(
        [
            "",
            "## 最大覆盖比例样本",
            "",
            "| p | y | low | covered | ratio | margin | offsets | samples |",
            "|---:|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for record in summary["worst_cover_records"]:
        lines.append(
            f"| {record['p']} | {record['y']} | {record['low_skeleton']} | "
            f"{record['covered_columns']} | {record['cover_ratio']:.6f} | "
            f"{record['margin']} | {record['offset_covered_counts']} | "
            f"{record['samples']} |"
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "对 `p>=23`，尾碰撞已消失，且一尾互补因子必为素数。因此 `margin=low_skeleton-covered_columns` 正是平方后窗口中的无尾储备数；正余量直接给出素数。",
            "",
            "该审计把剩余证明目标压成：三条倒数地板素对曲线的覆盖数必须始终小于低筛骨架数。若某族反例让覆盖比例逼近 `1`，则它必须表现为短窗素数异常集中或固定端点相位的 `PDEC/Tail-anchor` 缺陷。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=20000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_primepair_excess_audit_20260505",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.y_ratio)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key
        not in {
            "worst_cover_records",
            "worst_margin_records",
            "threshold_summary",
        }
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
