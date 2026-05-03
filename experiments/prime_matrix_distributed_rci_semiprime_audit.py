#!/usr/bin/env python3
"""审计 Distributed-RCI 的平衡双尾半素数化。

用法示例：
  python3 experiments/prime_matrix_distributed_rci_semiprime_audit.py --max-p 1000

在 y=floor(p/e) 下，终端 RCI 的负项来自至少两个尾素因子的低筛骨架点。
当 y^3>q^2 时，三尾不可能；当剩余余因子也无法 y-rough 时，负项精确等于
区间内的平衡双尾半素数 ell1*ell2。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path


def sieve_bool(n: int) -> bytearray:
    """返回素数布尔表。"""
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0
    for d in range(2, int(n**0.5) + 1):
        if is_prime[d]:
            start = d * d
            is_prime[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return is_prime


def primes_from_table(is_prime: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def next_prime(p: int, primes: list[int]) -> int:
    """返回大于 p 的下一素数。"""
    for prime in primes:
        if prime > p:
            return prime
    raise ValueError("素数表范围不足")


def build_tail_data(
    q: int,
    y: int,
    low_primes: list[int],
    tail_primes: list[int],
) -> tuple[bytearray, bytearray, dict[int, list[int]]]:
    """构造低筛骨架、尾因子数和尾标签。"""
    q_square = q * q
    low_rough = bytearray(b"\x01") * (q_square + 1)
    low_rough[0] = 0
    low_rough[1] = 0
    low_rough[q_square] = 0
    for ell in low_primes:
        low_rough[0 : q_square + 1 : ell] = b"\x00" * ((q_square // ell) + 1)

    tail_omega = bytearray(q_square + 1)
    tail_labels: dict[int, list[int]] = {}
    for ell in tail_primes:
        for pos in range(ell, q_square + 1, ell):
            if not low_rough[pos]:
                continue
            tail_omega[pos] += 1
            tail_labels.setdefault(pos, []).append(ell)
    return low_rough, tail_omega, tail_labels


def audit(max_p: int, y_ratio: float) -> dict:
    """执行半素数化审计。"""
    is_prime = sieve_bool(max_p * max_p + max_p * 20 + 10000)
    primes = primes_from_table(is_prime)
    target_primes = [prime for prime in primes if 3 <= prime <= max_p]

    records = []
    residual_gt1_records = []
    omega_ge3_records = []
    nonprime_no_tail_records = []

    for p in target_primes:
        q = next_prime(p, primes)
        y = max(2, int(math.floor(y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]
        low_rough, tail_omega, tail_labels = build_tail_data(
            q=q,
            y=y,
            low_primes=low_primes,
            tail_primes=tail_primes,
        )

        min_margin = None
        min_row = None
        max_semiprime_ratio = 0.0
        max_semiprime_ratio_row = None
        local_residual_gt1 = 0
        local_omega_ge3 = 0
        local_nonprime_no_tail = 0

        for row in range(1, q + 1):
            left = (row - 1) * q + 1
            right = row * q
            no_tail = 0
            no_tail_prime = 0
            balanced_semiprime = 0
            multi_excess = 0
            residual_gt1 = 0
            omega_ge3 = 0
            tail_label_counter: Counter[int] = Counter()

            for n in range(left, right + 1):
                if not low_rough[n]:
                    continue
                omega = tail_omega[n]
                if omega == 0:
                    no_tail += 1
                    if is_prime[n]:
                        no_tail_prime += 1
                    else:
                        local_nonprime_no_tail += 1
                elif omega >= 2:
                    labels = tail_labels[n]
                    multi_excess += omega - 1
                    for ell in labels:
                        tail_label_counter[ell] += 1
                    if omega >= 3:
                        omega_ge3 += 1
                        local_omega_ge3 += 1
                    product = 1
                    for ell in labels:
                        product *= ell
                    residual = n // product
                    if omega == 2 and residual == 1:
                        balanced_semiprime += 1
                    elif residual > 1:
                        residual_gt1 += 1
                        local_residual_gt1 += 1

            margin = no_tail - multi_excess
            row_record = {
                "p": p,
                "q": q,
                "y": y,
                "row": row,
                "row_interval": [left, right],
                "no_tail": no_tail,
                "no_tail_prime": no_tail_prime,
                "balanced_semiprime": balanced_semiprime,
                "multi_excess": multi_excess,
                "residual_gt1": residual_gt1,
                "omega_ge3": omega_ge3,
                "rci_margin": margin,
                "max_tail_label_load": max(tail_label_counter.values(), default=0),
            }
            if no_tail:
                ratio = balanced_semiprime / no_tail
                if ratio > max_semiprime_ratio:
                    max_semiprime_ratio = ratio
                    max_semiprime_ratio_row = row_record
            if min_margin is None or margin < min_margin:
                min_margin = margin
                min_row = row_record

        record = {
            "p": p,
            "q": q,
            "y": y,
            "y3_gt_q2": y**3 > q * q,
            "min_margin": min_margin,
            "min_row": min_row,
            "max_semiprime_ratio": max_semiprime_ratio,
            "max_semiprime_ratio_row": max_semiprime_ratio_row,
            "local_residual_gt1": local_residual_gt1,
            "local_omega_ge3": local_omega_ge3,
            "local_nonprime_no_tail": local_nonprime_no_tail,
        }
        records.append(record)
        if local_residual_gt1:
            residual_gt1_records.append(record)
        if local_omega_ge3:
            omega_ge3_records.append(record)
        if local_nonprime_no_tail:
            nonprime_no_tail_records.append(record)

    return {
        "parameters": {
            "max_p": max_p,
            "y_ratio": y_ratio,
        },
        "summary": {
            "prime_count": len(records),
            "global_min_margin": min(record["min_margin"] for record in records),
            "last_residual_gt1_p": (
                residual_gt1_records[-1]["p"] if residual_gt1_records else None
            ),
            "last_omega_ge3_p": (
                omega_ge3_records[-1]["p"] if omega_ge3_records else None
            ),
            "last_nonprime_no_tail_p": (
                nonprime_no_tail_records[-1]["p"]
                if nonprime_no_tail_records
                else None
            ),
            "last_y3_le_q2_p": max(
                (record["p"] for record in records if not record["y3_gt_q2"]),
                default=None,
            ),
            "global_max_semiprime_ratio": max(
                record["max_semiprime_ratio"] for record in records
            ),
            "worst_margin_records": sorted(
                records, key=lambda item: item["min_margin"]
            )[:20],
            "worst_ratio_records": sorted(
                records, key=lambda item: item["max_semiprime_ratio"], reverse=True
            )[:20],
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# Distributed-RCI 平衡双尾半素数审计",
        "",
        "**状态：** `experimental_distributed_rci_semiprime_reduction_support`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查相邻素数记录数：`{summary['prime_count']}`。",
        f"- 全局最小 RCI margin：`{summary['global_min_margin']}`。",
        f"- 最后出现双尾残因子 `>1` 的 p：`{summary['last_residual_gt1_p']}`。",
        f"- 最后出现三尾或更多尾因子的 p：`{summary['last_omega_ge3_p']}`。",
        f"- 最后出现无尾但非素数的 p：`{summary['last_nonprime_no_tail_p']}`。",
        f"- 最后未满足 `y^3>q^2` 的 p：`{summary['last_y3_le_q2_p']}`。",
        f"- 最大 `balanced_semiprime/no_tail` 比值：`{summary['global_max_semiprime_ratio']}`。",
        "",
        "## 最小 margin 样本",
        "",
        "| p | q | row | margin | no-tail | primes | semiprime | multi-excess | residual>1 | omega>=3 |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for record in summary["worst_margin_records"]:
        row = record["min_row"]
        lines.append(
            "| {p} | {q} | {row} | {margin} | {no_tail} | {primes} | {semi} | {multi} | {res} | {omega3} |".format(
                p=record["p"],
                q=record["q"],
                row=row["row"],
                margin=row["rci_margin"],
                no_tail=row["no_tail"],
                primes=row["no_tail_prime"],
                semi=row["balanced_semiprime"],
                multi=row["multi_excess"],
                res=row["residual_gt1"],
                omega3=row["omega_ge3"],
            )
        )
    lines.extend(
        [
            "",
            "## 最大半素数比例样本",
            "",
            "| p | q | row | ratio | no-tail | semiprime | margin | tail-load |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for record in summary["worst_ratio_records"]:
        row = record["max_semiprime_ratio_row"]
        lines.append(
            "| {p} | {q} | {row} | {ratio:.6f} | {no_tail} | {semi} | {margin} | {load} |".format(
                p=record["p"],
                q=record["q"],
                row=row["row"],
                ratio=record["max_semiprime_ratio"],
                no_tail=row["no_tail"],
                semi=row["balanced_semiprime"],
                margin=row["rci_margin"],
                load=row["max_tail_label_load"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "当 `y^3>q^2` 且双尾残因子不能为 `y`-rough 时，`RCI` 的负项精确化为平衡双尾半素数计数。无尾项在 `n<q^2` 中则是素数。于是 Distributed-RCI 的核心变成每个终端块内：素数数严格大于平衡双尾半素数数。",
            "",
            "本审计用于识别该半素数化从哪个范围开始完全准确，并记录最紧样本中的比例和尾标签负载。它仍是实验证据，不是无条件证明。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-distributed-rci-semiprime-audit",
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
        if key not in {"worst_margin_records", "worst_ratio_records"}
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
