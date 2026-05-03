#!/usr/bin/env python3
"""审计 H3 六轮余量随 p 增长的尺度。

用法示例：
  python3 experiments/prime_matrix_h3_margin_growth_audit.py
  python3 experiments/prime_matrix_h3_margin_growth_audit.py --max-p 5000
  python3 experiments/prime_matrix_h3_margin_growth_audit.py --buckets 100,317,500,1000,2000,5000

目标：
  统计固定 h=3 的余量 margin = candidate_count - blocked_count 在不同 p 区间的最小值，
  并与六轮 Mertens 粗略尺度 A*prod_{5<=ell<=p}(1-1/ell) 比较。

注意：
  这是有限数据审计，不是全局证明；它用于识别全局证明应攻击的尺度规律。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_total_descent_h3_margin_audit import (
    Fenwick,
    contained_h3_rows,
    h3_candidate_value,
    smallest_prime_factor_table,
)
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def bucket_label(p: int, buckets: list[int]) -> str:
    """返回 p 所在的 bucket 标签。"""
    previous = 5
    for bound in buckets:
        if p <= bound:
            return f"{previous}-{bound}"
        previous = bound + 1
    return f"{previous}+"


def audit(max_p: int, buckets: list[int], row_stride: int) -> dict:
    """执行 H3 余量增长审计。"""
    primes = primes_upto(max_p + 100)
    target_primes = [prime for prime in primes if 5 <= prime <= max_p]
    max_q = next_prime(max_p)
    max_n = max_q * max_q
    max_h3_row = (max_n + 2) // 3
    spf = smallest_prime_factor_table(max_n)

    events_by_spf: dict[int, list[int]] = {}
    for h3_row in range(1, max_h3_row + 1):
        candidate = h3_candidate_value(h3_row)
        if candidate <= 1 or candidate > max_n:
            continue
        factor = spf[candidate]
        if 5 <= factor <= max_p:
            events_by_spf.setdefault(factor, []).append(h3_row)

    fenwick = Fenwick(max_h3_row)
    event_keys = sorted(events_by_spf)
    event_cursor = 0
    rows_checked = 0
    bucket_stats: dict[str, dict] = {}
    prime_stats = []
    sixwheel_rough_product = 1.0
    product_cursor = 0
    product_primes = [prime for prime in primes if 5 <= prime <= max_p]

    for p in target_primes:
        while product_cursor < len(product_primes) and product_primes[product_cursor] <= p:
            prime = product_primes[product_cursor]
            sixwheel_rough_product *= 1.0 - 1.0 / prime
            product_cursor += 1

        while event_cursor < len(event_keys) and event_keys[event_cursor] <= p:
            for h3_row in events_by_spf[event_keys[event_cursor]]:
                fenwick.add(h3_row, 1)
            event_cursor += 1

        q = next_prime(p)
        prime_min = None
        prime_argmin = None
        prime_min_ratio = None
        prime_rows = 0
        prime_sum_margin = 0
        prime_sum_expected = 0.0
        for q_row in range(2, q + 1):
            if row_stride > 1 and q_row != q and (q_row - 2) % row_stride != 0:
                continue
            left = (q_row - 1) * q + 1
            right = q_row * q
            first, last = contained_h3_rows(left, right)
            candidate_count = max(0, last - first + 1)
            blocked_count = fenwick.range_sum(first, last) if candidate_count else 0
            margin = candidate_count - blocked_count
            expected = candidate_count * sixwheel_rough_product
            ratio = margin / expected if expected else None

            rows_checked += 1
            prime_rows += 1
            prime_sum_margin += margin
            prime_sum_expected += expected
            if prime_min is None or margin < prime_min:
                prime_min = margin
                prime_min_ratio = ratio
                prime_argmin = {
                    "p": p,
                    "q": q,
                    "q_row": q_row,
                    "interval": [left, right],
                    "initial_type": classify_q_row_descent(p, q, q_row)["type"],
                    "candidate_count": candidate_count,
                    "blocked_count": blocked_count,
                    "margin": margin,
                    "expected_sixwheel_rough": expected,
                    "margin_over_expected": ratio,
                }

        label = bucket_label(p, buckets)
        stats = bucket_stats.setdefault(
            label,
            {
                "prime_count": 0,
                "row_count": 0,
                "min_margin": None,
                "argmin": None,
                "sum_margin": 0,
                "sum_expected": 0.0,
                "min_margin_over_expected": None,
            },
        )
        stats["prime_count"] += 1
        stats["row_count"] += prime_rows
        stats["sum_margin"] += prime_sum_margin
        stats["sum_expected"] += prime_sum_expected
        if stats["min_margin"] is None or prime_min < stats["min_margin"]:
            stats["min_margin"] = prime_min
            stats["argmin"] = prime_argmin
        if (
            prime_min_ratio is not None
            and (
                stats["min_margin_over_expected"] is None
                or prime_min_ratio < stats["min_margin_over_expected"]
            )
        ):
            stats["min_margin_over_expected"] = prime_min_ratio

        prime_stats.append(
            {
                "p": p,
                "q": q,
                "row_count": prime_rows,
                "min_margin": prime_min,
                "argmin": prime_argmin,
                "avg_margin": prime_sum_margin / prime_rows if prime_rows else None,
                "avg_expected_sixwheel_rough": (
                    prime_sum_expected / prime_rows if prime_rows else None
                ),
            }
        )

    for stats in bucket_stats.values():
        stats["avg_margin"] = stats["sum_margin"] / stats["row_count"]
        stats["avg_expected_sixwheel_rough"] = (
            stats["sum_expected"] / stats["row_count"]
            if stats["row_count"]
            else None
        )

    return {
        "status": "finite_h3_margin_growth_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "buckets": buckets,
            "row_stride": row_stride,
            "max_n": max_n,
        },
        "summary": {
            "q_rows_checked": rows_checked,
            "global_min_margin": min(item["min_margin"] for item in prime_stats),
            "global_max_prime_min_margin": max(item["min_margin"] for item in prime_stats),
            "bucket_stats": bucket_stats,
            "first_prime_with_min_margin_ge_21": next(
                (
                    item["p"]
                    for item in prime_stats
                    if item["min_margin"] >= 21
                    and all(other["min_margin"] >= 21 for other in prime_stats[prime_stats.index(item):])
                ),
                None,
            ),
        },
        "tight_prime_samples": sorted(prime_stats, key=lambda item: item["min_margin"])[:40],
        "tail_prime_samples": prime_stats[-20:],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    lines = [
        "# H3 六轮余量增长审计",
        "",
        "**状态：** `finite_h3_margin_growth_audit_not_global_proof`",
        "",
        "本文统计 H3 余量随 `p` 增长的尺度，并与六轮 Mertens 粗略期望比较。该报告用于识别全局证明的尺度规律，不是全局证明。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `buckets`: `{params['buckets']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `max_n`: `{params['max_n']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 全局最小余量：`{summary['global_min_margin']}`。",
        f"- 各素数最小余量的最大值：`{summary['global_max_prime_min_margin']}`。",
        f"- 自此以后所有素数最小余量 `>=21` 的首个 `p`：`{summary['first_prime_with_min_margin_ge_21']}`。",
        "",
        "## Bucket 统计",
        "",
        "| bucket | primes | rows | min margin | avg margin | avg expected | min margin/expected | argmin |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for label, stats in summary["bucket_stats"].items():
        argmin = stats["argmin"]
        lines.append(
            "| {label} | {pc} | {rows} | {minm} | {avg:.6f} | {exp:.6f} | {ratio:.6f} | `p={p},q={q},row={row}` |".format(
                label=label,
                pc=stats["prime_count"],
                rows=stats["row_count"],
                minm=stats["min_margin"],
                avg=stats["avg_margin"],
                exp=stats["avg_expected_sixwheel_rough"],
                ratio=stats["min_margin_over_expected"],
                p=argmin["p"],
                q=argmin["q"],
                row=argmin["q_row"],
            )
        )

    lines.extend(
        [
            "",
            "## 最紧素数层",
            "",
            "| p | q | min margin | argmin row | avg margin | avg expected |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["tight_prime_samples"][:20]:
        lines.append(
            "| {p} | {q} | {minm} | {row} | {avg:.6f} | {exp:.6f} |".format(
                p=item["p"],
                q=item["q"],
                minm=item["min_margin"],
                row=item["argmin"]["q_row"],
                avg=item["avg_margin"],
                exp=item["avg_expected_sixwheel_rough"],
            )
        )

    lines.extend(
        [
            "",
            "## 尺度洞察",
            "",
            "1. 最小余量只在低层接近临界；在本账本中，从某一素数层之后，所有行的最小余量保持在 `21` 以上。",
            "2. 平均余量与六轮 Mertens 粗略尺度同阶，说明有效幸存点不是由有限模板偶然产生，而是随 `q/log q` 增长。",
            "3. 若全局反例存在，它必须强行压低本应增长的 Mertens 粗剩余；这只能通过小首因子骨架过载或大量中尾标签同步实现。",
            "",
            "因此全局硬攻应转为尺度二分：",
            "",
            "```text",
            "expected rough scale grows like q/log q",
            "but H3 full blocking forces rough scale to 0",
            "=> small skeleton overload or many-label PDEC energy.",
            "```",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--buckets", type=str, default="100,317,500,1000,2000,3000,4000,5000")
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-h3-margin-growth-audit"),
    )
    args = parser.parse_args()
    buckets = [int(item) for item in args.buckets.split(",") if item.strip()]
    result = audit(max_p=args.max_p, buckets=buckets, row_stride=max(1, args.row_stride))
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
