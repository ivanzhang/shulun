#!/usr/bin/env python3
"""生成平方后端点低范围有限证书。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_lowband_finite_certificate.py --max-p 2003

该证书把 `P<2003` 的平方后端点从解析常数债务中剥离：
1. 直接检查 `(P^2,P^2+P)` 内有素数；
2. 对 `P>=23` 同时记录 `G(P)-B(P)>0`；
3. 记录低范围面积、低骨架与素对常数的最坏样本。
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


def low_rough_columns(p: int, y: int, primes: list[int]) -> bytearray:
    """计算平方后端点的低筛骨架列。"""
    low_rough = bytearray(b"\x01") * p
    low_rough[0] = 0
    p_square = p * p
    for ell in primes:
        if ell > y:
            break
        residue = (-p_square) % ell
        start = residue if residue != 0 else ell
        if start >= p:
            continue
        low_rough[start:p:ell] = b"\x00" * (((p - 1 - start) // ell) + 1)
    return low_rough


def audit_p(p: int, primes: list[int], prime_flags: bytearray, y_ratio: float) -> dict:
    """审计单个 p。"""
    y = max(2, int(math.floor(y_ratio * p)))
    p_square = p * p
    endpoint_prime_columns = [
        column for column in range(1, p) if prime_flags[p_square + column]
    ]

    area = 0
    for a in range(y + 1, p):
        area += (p_square + p - 1) // a - p_square // a

    low_rough = low_rough_columns(p, y, primes)
    low_skeleton = sum(low_rough)
    covered_columns: set[int] = set()
    offset_counts: dict[int, int] = {}

    for ell in primes:
        if ell <= y:
            continue
        if ell >= p:
            break
        base = p_square // ell
        right = (p_square + p - 1) // ell
        for m in range(base + 1, right + 1):
            if m >= len(prime_flags) or not prime_flags[m]:
                continue
            column = ell * m - p_square
            if 1 <= column < p and low_rough[column]:
                covered_columns.add(column)
                offset = m - base
                offset_counts[offset] = offset_counts.get(offset, 0) + 1

    covered = len(covered_columns)
    margin = low_skeleton - covered
    log_p = math.log(p)
    return {
        "p": p,
        "y": y,
        "endpoint_prime_columns": endpoint_prime_columns[:10],
        "endpoint_prime_count": len(endpoint_prime_columns),
        "endpoint_prime_exists": bool(endpoint_prime_columns),
        "area": area,
        "area_ratio": area / p,
        "low_skeleton": low_skeleton,
        "covered_columns": covered,
        "margin": margin,
        "g_scaled": low_skeleton * log_p / p,
        "b_scaled_log2": covered * log_p * log_p / p,
        "offset_counts": {
            str(key): offset_counts[key] for key in sorted(offset_counts)
        },
        "certified_by_dimension_gap": p >= 23 and margin > 0,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行低范围证书审计。"""
    prime_flags = sieve_bool(max_p * max_p + max_p)
    primes = primes_from_table(prime_flags, max_p)
    target_primes = [prime for prime in primes if prime >= 3]
    records = [audit_p(p, primes, prime_flags, y_ratio) for p in target_primes]
    endpoint_failures = [record for record in records if not record["endpoint_prime_exists"]]
    dimension_records = [record for record in records if record["p"] >= 23]
    dimension_failures = [
        record for record in dimension_records if not record["certified_by_dimension_gap"]
    ]

    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "endpoint_failure_count": len(endpoint_failures),
            "dimension_record_count": len(dimension_records),
            "dimension_failure_count": len(dimension_failures),
            "min_dimension_margin": min(
                (record["margin"] for record in dimension_records), default=None
            ),
            "max_area_ratio_record": max(
                records, key=lambda item: item["area_ratio"], default=None
            ),
            "min_g_scaled_record": min(
                dimension_records, key=lambda item: item["g_scaled"], default=None
            ),
            "max_b_scaled_record": max(
                dimension_records, key=lambda item: item["b_scaled_log2"], default=None
            ),
            "worst_margin_records": sorted(
                dimension_records, key=lambda item: item["margin"]
            )[:20],
        },
        "endpoint_failures": endpoint_failures,
        "dimension_failures": dimension_failures,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点低范围有限证书",
        "",
        "**状态：** `finite_postsquare_lowband_certificate`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- 直接端点素数失败数：`{summary['endpoint_failure_count']}`。",
        f"- `p>=23` 维数差记录数：`{summary['dimension_record_count']}`。",
        f"- 维数差失败数：`{summary['dimension_failure_count']}`。",
        f"- 最小维数差 margin：`{summary['min_dimension_margin']}`。",
        f"- 最大面积比例记录：`{summary['max_area_ratio_record']}`。",
        f"- 最小 `G log(P)/P` 记录：`{summary['min_g_scaled_record']}`。",
        f"- 最大 `B log(P)^2/P` 记录：`{summary['max_b_scaled_record']}`。",
        "",
        "## 最小 margin 样本",
        "",
        "| p | y | low | B | margin | Glog/P | Blog2/P | primes |",
        "|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in summary["worst_margin_records"]:
        lines.append(
            f"| {record['p']} | {record['y']} | {record['low_skeleton']} | "
            f"{record['covered_columns']} | {record['margin']} | "
            f"{record['g_scaled']:.6f} | {record['b_scaled_log2']:.6f} | "
            f"{record['endpoint_prime_columns']} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "`P<2003` 是平方后端点常数账本的有限低段。该证书直接检查端点素数存在；对 `P>=23`，同时核验 `G(P)-B(P)>0`，因此低段不再占用 `LDG/RFP` 的解析常数预算。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2003)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_lowband_finite_certificate_20260505",
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
        if key != "worst_margin_records"
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
