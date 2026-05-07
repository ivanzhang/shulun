#!/usr/bin/env python3
"""审计平方后端点一尾项的互补因子结构。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_tail_cofactor_audit.py --max-p 10000

若 p^2+k=ell*m 且 y<ell<p，则 m 位于一个长度 < 1+p/ell 的极短区间。
在 p 足够大时，低筛 y-rough 的 m 必为素数。
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
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (
                ((limit - start) // value) + 1
            )
    return flags


def smallest_prime_factor_table(limit: int) -> list[int]:
    """返回最小素因子表；素数的值为自身。"""
    spf = list(range(limit + 1))
    if limit >= 0:
        spf[0] = 0
    if limit >= 1:
        spf[1] = 1
    for value in range(2, int(limit**0.5) + 1):
        if spf[value] != value:
            continue
        start = value * value
        for multiple in range(start, limit + 1, value):
            if spf[multiple] == multiple:
                spf[multiple] = value
    return spf


def primes_from_table(flags: bytearray, limit: int | None = None) -> list[int]:
    """提取素数列表。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(end) if flags[idx]]


def is_y_rough(value: int, y: int, spf: list[int]) -> bool:
    """判断 value 是否避开所有 low_primes。"""
    return spf[value] > y


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    cofactor_limit = int(math.ceil(math.e * max_p)) + 100
    prime_flags = sieve_bool(cofactor_limit)
    spf = smallest_prime_factor_table(cofactor_limit)
    primes = primes_from_table(prime_flags, max_p)
    target_primes = [prime for prime in primes if prime >= 3]

    records = []
    total_yrough_cofactors = 0
    composite_yrough_cofactors = 0
    last_composite_yrough_p = None
    max_interval_length = 0
    max_interval_record = None
    global_offset_counts: dict[int, int] = {}
    max_yrough_record = None

    for p in target_primes:
        y = max(2, int(math.floor(y_ratio * p)))
        tail_primes = [prime for prime in primes if y < prime < p]
        p_square = p * p
        local_yrough = 0
        local_composite = 0
        local_prime = 0
        local_max_interval = 0
        cofactor_prime_threshold_holds = (p_square + p - 1) < (y + 1) ** 3
        offset_counts: dict[int, int] = {}
        samples = []

        for ell in tail_primes:
            base = p_square // ell
            left = p_square // ell + 1
            right = (p_square + p - 1) // ell
            if right < left:
                continue
            interval_length = right - left + 1
            if interval_length > local_max_interval:
                local_max_interval = interval_length
            if interval_length > max_interval_length:
                max_interval_length = interval_length
                max_interval_record = {
                    "p": p,
                    "y": y,
                    "ell": ell,
                    "cofactor_interval": [left, right],
                    "interval_length": interval_length,
                }
            for cofactor in range(left, right + 1):
                if not is_y_rough(cofactor, y, spf):
                    continue
                offset = cofactor - base
                offset_counts[offset] = offset_counts.get(offset, 0) + 1
                global_offset_counts[offset] = global_offset_counts.get(offset, 0) + 1
                local_yrough += 1
                total_yrough_cofactors += 1
                item = {
                    "ell": ell,
                    "cofactor": cofactor,
                    "offset": offset,
                    "value": ell * cofactor,
                    "column": ell * cofactor - p_square,
                    "cofactor_is_prime": bool(prime_flags[cofactor]),
                }
                if prime_flags[cofactor]:
                    local_prime += 1
                else:
                    local_composite += 1
                    composite_yrough_cofactors += 1
                    last_composite_yrough_p = p
                if len(samples) < 5:
                    samples.append(item)

        if max_yrough_record is None or local_yrough > max_yrough_record["yrough_cofactors"]:
            max_yrough_record = {
                "p": p,
                "y": y,
                "tail_prime_count": len(tail_primes),
                "yrough_cofactors": local_yrough,
                "offset_counts": offset_counts,
            }

        records.append(
            {
                "p": p,
                "y": y,
                "tail_prime_count": len(tail_primes),
                "yrough_cofactors": local_yrough,
                "prime_yrough_cofactors": local_prime,
                "composite_yrough_cofactors": local_composite,
                "max_interval_length": local_max_interval,
                "cofactor_prime_threshold_holds": cofactor_prime_threshold_holds,
                "offset_counts": offset_counts,
                "samples": samples,
            }
        )

    worst_interval = sorted(records, key=lambda item: -item["max_interval_length"])[:20]
    composite_records = [
        record for record in records if record["composite_yrough_cofactors"] > 0
    ]
    threshold_failures = [
        record for record in records if not record["cofactor_prime_threshold_holds"]
    ]
    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "total_yrough_cofactors": total_yrough_cofactors,
            "composite_yrough_cofactors": composite_yrough_cofactors,
            "last_composite_yrough_p": last_composite_yrough_p,
            "max_interval_length": max_interval_length,
            "max_interval_record": max_interval_record,
            "composite_record_count": len(composite_records),
            "cofactor_prime_threshold_failure_count": len(threshold_failures),
            "last_cofactor_prime_threshold_failure_p": (
                threshold_failures[-1]["p"] if threshold_failures else None
            ),
            "offset_counts": {
                str(key): global_offset_counts[key]
                for key in sorted(global_offset_counts)
            },
            "max_yrough_record": max_yrough_record,
            "worst_interval_records": worst_interval,
        },
        "composite_records": composite_records,
        "cofactor_prime_threshold_failures": threshold_failures,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点一尾互补因子审计",
        "",
        "**状态：** `experimental_postsquare_tail_cofactor_identity_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- y-rough 互补因子总数：`{summary['total_yrough_cofactors']}`。",
        f"- 复合 y-rough 互补因子数：`{summary['composite_yrough_cofactors']}`。",
        f"- 最后出现复合互补因子的 p：`{summary['last_composite_yrough_p']}`。",
        f"- 最大互补因子区间长度：`{summary['max_interval_length']}`。",
        f"- 最大区间样本：`{summary['max_interval_record']}`。",
        f"- 互补因子素性阈值失败次数：`{summary['cofactor_prime_threshold_failure_count']}`。",
        f"- 最后一个阈值失败 p：`{summary['last_cofactor_prime_threshold_failure_p']}`。",
        f"- floor offset 分布：`{summary['offset_counts']}`。",
        f"- 单行最多互补因子记录：`{summary['max_yrough_record']}`。",
        "",
        "## 最大区间样本",
        "",
        "| p | y | tail primes | yrough cofactors | composite | max interval | sample |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in summary["worst_interval_records"]:
        lines.append(
            f"| {record['p']} | {record['y']} | {record['tail_prime_count']} | "
            f"{record['yrough_cofactors']} | {record['composite_yrough_cofactors']} | "
            f"{record['max_interval_length']} | {record['samples']} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            f"一尾项精确等价于 `p^2+k=ell*m`，其中 `y<ell<p`，且 `m` 仍为 `y`-rough。互补因子区间长度至多 `1+p/ell<1+e`，本次样本实际最大为 `{summary['max_interval_length']}`。若 `p^2+p-1<(y+1)^3`，则任何 `y`-rough 互补因子 `m` 必为素数；样本显示复合 `y`-rough 互补因子只出现在极小 `p`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_tail_cofactor_audit_20260505",
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
        if key != "worst_interval_records"
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
