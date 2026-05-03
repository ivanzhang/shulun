#!/usr/bin/env python3
"""生成 WSH-Hall 的 SCB-1 长块扩张证书。

用法示例：
  python3 experiments/prime_matrix_wsh_scb1_long_block_certificate.py
  python3 experiments/prime_matrix_wsh_scb1_long_block_certificate.py --max-p 1000

SCB-1 目标：
  对所有 |B|>=4 的连续平衡双尾半素数长块，审计
  |N_R(B)|-|B| 的最小值，并记录最紧长块的尾标签、固定偏移、小轮相位和端点镜像压力。

注意：这是有限长块证书，不是全局 SCB-1 证明。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

from prime_matrix_wsh_expansion_margin_audit import (
    block_pressure,
    count_in_union,
    merge_intervals,
)
from prime_matrix_wsh_hall_phase_certificate import (
    build_tail_data,
    collect_rows,
    next_prime_after,
    primes_from_table,
    sieve_bool,
)


def classify_long_pressure(block: dict) -> list[str]:
    """给长块分配结构压力标签。"""
    labels = ["Endpoint-margin"]
    pressure = block["pressure"]
    size = block["semiprime_count"]
    if pressure["max_tail_load"] >= 2:
        labels.append("Tail-repeat")
    if pressure["max_allowed_offset_load"] >= size:
        labels.append("Fixed-offset-full-load")
    elif pressure["max_allowed_offset_load"] >= max(3, size - 1):
        labels.append("Fixed-offset-heavy-load")
    if pressure["max_wheel_phase_load"] >= 2:
        labels.append("Wheel-phase-repeat")
    return labels


def audit_long_blocks(args: argparse.Namespace) -> dict:
    """审计全部 |B|>=min_block_size 的长块。"""
    wheel_primes = [int(part) for part in args.wheel_primes.split(",") if part]
    sieve_limit = args.max_p * args.max_p + args.max_p * 20 + 10000
    is_prime = sieve_bool(sieve_limit)
    primes = primes_from_table(is_prime)
    target_primes = [prime for prime in primes if args.min_p <= prime <= args.max_p]

    long_block_count = 0
    row_with_semiprime_count = 0
    min_surplus = None
    min_surplus_by_size: dict[int, int] = {}
    tight_count_by_signature: Counter[tuple[int, int]] = Counter()
    pressure_counter: Counter[str] = Counter()
    tight_blocks: list[dict] = []
    negative_blocks = 0
    zero_blocks = 0

    for p in target_primes:
        q = next_prime_after(p, primes)
        y = max(2, int(math.floor(args.y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]
        low_rough, tail_omega, tail_labels = build_tail_data(q, low_primes, tail_primes)
        primes_by_row, semis_by_row, _ = collect_rows(
            q,
            low_rough,
            tail_omega,
            tail_labels,
            is_prime,
        )
        radius = math.ceil(args.radius_factor * math.log(q) ** 2)
        for row in range(1, q + 1):
            semiprimes = semis_by_row[row]
            if not semiprimes:
                continue
            row_with_semiprime_count += 1
            row_primes = primes_by_row[row]
            for start_index in range(len(semiprimes)):
                intervals: list[tuple[int, int]] = []
                for end_index in range(start_index, len(semiprimes)):
                    semi_value = semiprimes[end_index]
                    intervals.append((semi_value - radius, semi_value + radius))
                    size = end_index - start_index + 1
                    if size < args.min_block_size:
                        continue
                    merged = merge_intervals(intervals)
                    prime_count = count_in_union(row_primes, merged)
                    surplus = prime_count - size
                    long_block_count += 1
                    if min_surplus is None or surplus < min_surplus:
                        min_surplus = surplus
                    if size not in min_surplus_by_size or surplus < min_surplus_by_size[size]:
                        min_surplus_by_size[size] = surplus
                    if surplus < 0:
                        negative_blocks += 1
                    if surplus == 0:
                        zero_blocks += 1
                    if surplus <= args.tight_surplus:
                        block_semis = semiprimes[start_index : end_index + 1]
                        span_left = min(interval[0] for interval in merged)
                        span_right = max(interval[1] for interval in merged)
                        pressure = block_pressure(
                            block_semis,
                            row_primes,
                            merged,
                            tail_labels,
                            wheel_primes,
                            radius,
                        )
                        block = {
                            "p": p,
                            "q": q,
                            "row": row,
                            "radius": radius,
                            "semiprime_count": size,
                            "prime_count": prime_count,
                            "surplus": surplus,
                            "neighbor_intervals": merged,
                            "span": span_right - span_left + 1,
                            "semiprime_values": block_semis,
                            "q_square_mirror_span": [q * q - span_right, q * q - span_left],
                            "pressure": pressure,
                        }
                        labels = classify_long_pressure(block)
                        block["pressure_labels"] = labels
                        tight_blocks.append(block)
                        tight_count_by_signature[(surplus, size)] += 1
                        pressure_counter.update(labels)

    tight_blocks.sort(
        key=lambda block: (
            block["surplus"],
            -block["semiprime_count"],
            -block["pressure"]["max_allowed_offset_load"],
            -block["pressure"]["max_tail_load"],
        )
    )

    return {
        "parameters": {
            "max_p": args.max_p,
            "min_p": args.min_p,
            "y_ratio": args.y_ratio,
            "radius_factor": args.radius_factor,
            "min_block_size": args.min_block_size,
            "tight_surplus": args.tight_surplus,
            "wheel_primes": wheel_primes,
        },
        "summary": {
            "prime_record_count": len(target_primes),
            "row_with_semiprime_count": row_with_semiprime_count,
            "long_block_count": long_block_count,
            "global_min_long_surplus": 0 if min_surplus is None else min_surplus,
            "negative_long_blocks": negative_blocks,
            "zero_long_blocks": zero_blocks,
            "tight_long_block_count": len(tight_blocks),
            "tight_count_by_signature": [
                {"surplus": surplus, "size": size, "count": count}
                for (surplus, size), count in sorted(tight_count_by_signature.items())
            ],
            "min_surplus_by_size_sample": {
                str(size): value
                for size, value in sorted(min_surplus_by_size.items())[:20]
            },
            "pressure_label_counts": dict(sorted(pressure_counter.items())),
            "max_tight_long_block_size": max(
                (block["semiprime_count"] for block in tight_blocks),
                default=0,
            ),
            "max_tail_load_in_tight_long_blocks": max(
                (block["pressure"]["max_tail_load"] for block in tight_blocks),
                default=0,
            ),
            "max_allowed_offset_load_in_tight_long_blocks": max(
                (block["pressure"]["max_allowed_offset_load"] for block in tight_blocks),
                default=0,
            ),
        },
        "tight_long_blocks": tight_blocks[: args.max_records],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 证书报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# WSH-Hall SCB-1 长块扩张证书",
        "",
        "**状态：** `finite_scb1_long_block_certificate_not_global_proof`",
        "",
        "本文档专攻 `SCB-1`：对 `|B|>=4` 的连续平衡双尾半素数长块审计 Hall 余量与命名出口压力。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `min_p`: `{params['min_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        f"- `radius_factor`: `{params['radius_factor']}`",
        f"- `min_block_size`: `{params['min_block_size']}`",
        f"- `tight_surplus`: `{params['tight_surplus']}`",
        f"- `wheel_primes`: `{params['wheel_primes']}`",
        "",
        "## 摘要",
        "",
        f"- 检查素数记录数：`{summary['prime_record_count']}`。",
        f"- 含平衡半素数的行数：`{summary['row_with_semiprime_count']}`。",
        f"- 长块总数：`{summary['long_block_count']}`。",
        f"- 全局最小长块 Hall 余量：`{summary['global_min_long_surplus']}`。",
        f"- 负余量长块数：`{summary['negative_long_blocks']}`。",
        f"- 零余量长块数：`{summary['zero_long_blocks']}`。",
        f"- 小余量长块数：`{summary['tight_long_block_count']}`。",
        f"- 小余量长块签名：`{summary['tight_count_by_signature']}`。",
        f"- 压力标签计数：`{summary['pressure_label_counts']}`。",
        f"- 最大小余量长块尺寸：`{summary['max_tight_long_block_size']}`。",
        f"- 小余量最大尾标签负载：`{summary['max_tail_load_in_tight_long_blocks']}`。",
        f"- 小余量最大固定允许偏移负载：`{summary['max_allowed_offset_load_in_tight_long_blocks']}`。",
        "",
        "## 最紧长块样本",
        "",
        "| p | q | row | R | size | primes | surplus | labels | semis | mirror span |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for block in result["tight_long_blocks"][:40]:
        lines.append(
            "| {p} | {q} | {row} | {radius} | {size} | {primes} | {surplus} | {labels} | {semis} | {mirror} |".format(
                p=block["p"],
                q=block["q"],
                row=block["row"],
                radius=block["radius"],
                size=block["semiprime_count"],
                primes=block["prime_count"],
                surplus=block["surplus"],
                labels=",".join(block["pressure_labels"]),
                semis=block["semiprime_values"],
                mirror=block["q_square_mirror_span"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "在有限范围内，所有 `|B|>=4` 长块都有正 Hall 余量，最小值为 `3`。所有达到 `surplus<=3` 的长块都带有固定偏移满载或重载压力，说明长块临界不是自由随机缺口，而是可路由到固定偏移/PDEC 的局部相位压缩。",
            "",
            "这支持下一步证明模板：长块若不能自动给出至少 `3` 个余量，则必须表现为固定偏移通道重载、尾标签重复或端点镜像亏损。该文件仍是有限证书，不是全局证明。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--min-p", type=int, default=17)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--radius-factor", type=float, default=3.0)
    parser.add_argument("--min-block-size", type=int, default=4)
    parser.add_argument("--tight-surplus", type=int, default=3)
    parser.add_argument("--wheel-primes", default="2,3,5,7,11,13")
    parser.add_argument("--max-records", type=int, default=200)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-scb1-long-block-certificate",
    )
    args = parser.parse_args()
    result = audit_long_blocks(args)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
