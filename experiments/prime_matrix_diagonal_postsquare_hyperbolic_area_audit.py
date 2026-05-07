#!/usr/bin/env python3
"""审计平方后端点双曲窄带原始面积 X(P)。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_hyperbolic_area_audit.py --max-p 100000

X(P)=#{(a,b): y<a<P, P<b, P^2<ab<P^2+P}。
这是 RFP-Upper 二维上筛前的母集合体量。
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


def audit_p(p: int, y_ratio: float) -> dict:
    """审计单个 p 的双曲窄带面积。"""
    y = max(2, int(math.floor(y_ratio * p)))
    p_square = p * p
    total = 0
    offset_counts: dict[int, int] = {}
    quotient_counts: dict[int, int] = {}
    max_slice = 0
    samples = []

    for a in range(y + 1, p):
        right = (p_square + p - 1) // a
        base = p_square // a
        length = right - base
        if length <= 0:
            continue
        total += length
        if length > max_slice:
            max_slice = length
        quotient = p // a
        quotient_counts[quotient] = quotient_counts.get(quotient, 0) + length
        for offset in range(1, length + 1):
            offset_counts[offset] = offset_counts.get(offset, 0) + 1
            if len(samples) < 5:
                b = base + offset
                samples.append(
                    {
                        "a": a,
                        "b": b,
                        "offset": offset,
                        "column": a * b - p_square,
                        "quotient_floor_p_over_a": quotient,
                    }
                )

    log_p = math.log(p)
    return {
        "p": p,
        "y": y,
        "area": total,
        "area_ratio": total / p,
        "area_minus_p": total - p,
        "area_scaled_log2": total * log_p * log_p / p,
        "offset_counts": {
            str(key): offset_counts[key] for key in sorted(offset_counts)
        },
        "quotient_counts": {
            str(key): quotient_counts[key] for key in sorted(quotient_counts)
        },
        "max_slice_length": max_slice,
        "samples": samples,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    primes = [prime for prime in primes_from_table(sieve_bool(max_p)) if prime >= 23]
    records = [audit_p(p, y_ratio) for p in primes]
    worst_ratio = sorted(records, key=lambda item: -item["area_ratio"])[:20]
    worst_excess = sorted(records, key=lambda item: -item["area_minus_p"])[:20]
    threshold_summary = []
    for threshold in [23, 101, 251, 501, 1009, 2003, 5003, 10007, 20011, 50021]:
        subset = [record for record in records if record["p"] >= threshold]
        if not subset:
            continue
        max_ratio = max(subset, key=lambda item: item["area_ratio"])
        max_excess = max(subset, key=lambda item: item["area_minus_p"])
        threshold_summary.append(
            {
                "threshold": threshold,
                "max_ratio_record": {
                    "p": max_ratio["p"],
                    "area": max_ratio["area"],
                    "area_ratio": max_ratio["area_ratio"],
                    "area_minus_p": max_ratio["area_minus_p"],
                },
                "max_excess_record": {
                    "p": max_excess["p"],
                    "area": max_excess["area"],
                    "area_ratio": max_excess["area_ratio"],
                    "area_minus_p": max_excess["area_minus_p"],
                },
            }
        )

    global_offsets: dict[str, int] = {}
    global_quotients: dict[str, int] = {}
    for record in records:
        for key, value in record["offset_counts"].items():
            global_offsets[key] = global_offsets.get(key, 0) + value
        for key, value in record["quotient_counts"].items():
            global_quotients[key] = global_quotients.get(key, 0) + value

    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "max_area_ratio": max(
                (record["area_ratio"] for record in records), default=None
            ),
            "max_area_minus_p": max(
                (record["area_minus_p"] for record in records), default=None
            ),
            "max_slice_length": max(
                (record["max_slice_length"] for record in records), default=None
            ),
            "global_offset_counts": {
                key: global_offsets[key] for key in sorted(global_offsets, key=int)
            },
            "global_quotient_counts": {
                key: global_quotients[key]
                for key in sorted(global_quotients, key=int)
            },
            "worst_ratio_records": worst_ratio,
            "worst_excess_records": worst_excess,
            "threshold_summary": threshold_summary,
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点双曲窄带面积审计",
        "",
        "**状态：** `experimental_hyperbolic_area_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查 `p>=23` 奇素数个数：`{summary['prime_count']}`。",
        f"- 最大 `X(P)/P`：`{summary['max_area_ratio']}`。",
        f"- 最大 `X(P)-P`：`{summary['max_area_minus_p']}`。",
        f"- 最大切片长度：`{summary['max_slice_length']}`。",
        f"- 全局 offset 分布：`{summary['global_offset_counts']}`。",
        f"- 全局 `floor(P/a)` 分布：`{summary['global_quotient_counts']}`。",
        "",
        "## 阈值账本",
        "",
        "| threshold | max ratio record | max excess record |",
        "|---:|---|---|",
    ]
    for item in summary["threshold_summary"]:
        lines.append(
            f"| {item['threshold']} | {item['max_ratio_record']} | {item['max_excess_record']} |"
        )

    lines.extend(
        [
            "",
            "## 最大比例样本",
            "",
            "| p | y | X(P) | X/P | X-P | offsets | quotients | samples |",
            "|---:|---:|---:|---:|---:|---|---|---|",
        ]
    )
    for record in summary["worst_ratio_records"]:
        lines.append(
            f"| {record['p']} | {record['y']} | {record['area']} | "
            f"{record['area_ratio']:.6f} | {record['area_minus_p']} | "
            f"{record['offset_counts']} | {record['quotient_counts']} | "
            f"{record['samples']} |"
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "该面积是 RFP 二维上筛的母集合体量。样本若支持 `X(P)<=1.02P`，则 `RFP-Upper` 的主要压力转移到二维 Selberg 主常数与双曲地板模分布误差。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=100000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_hyperbolic_area_audit_20260505",
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
        if key not in {"worst_ratio_records", "worst_excess_records", "threshold_summary"}
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
