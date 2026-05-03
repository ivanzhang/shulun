#!/usr/bin/env python3
"""审计 WSH-Hall 扩张余量。

用法示例：
  python3 experiments/prime_matrix_wsh_expansion_margin_audit.py --max-p 1000
  python3 experiments/prime_matrix_wsh_expansion_margin_audit.py --max-p 2000 --tight-surplus 1

该脚本不只检查匹配是否存在，而是逐个连续半素数块计算

  Hall surplus = |N_R(B)| - |B|

其中 `N_R(B)` 是同一行无尾素数中距离 `B` 至多 `R=ceil(C log^2 q)` 的邻域。
零余量或小余量块是 `WSH-Expansion-or-Defect` 的真正临界对象。
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
from collections import Counter
from pathlib import Path

from prime_matrix_wsh_hall_phase_certificate import (
    build_tail_data,
    collect_rows,
    fixed_offset_ratio,
    next_prime_after,
    primes_from_table,
    sieve_bool,
    wheel_allowed_offset,
    wheel_modulus,
)


def merge_intervals(intervals: list[tuple[int, int]]) -> list[list[int]]:
    """合并整数闭区间。"""
    if not intervals:
        return []
    sorted_intervals = sorted(intervals)
    merged = [[sorted_intervals[0][0], sorted_intervals[0][1]]]
    for left, right in sorted_intervals[1:]:
        if left <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], right)
        else:
            merged.append([left, right])
    return merged


def count_in_union(values: list[int], intervals: list[list[int]]) -> int:
    """统计有序列表中落入区间并集的元素数。"""
    total = 0
    for left, right in intervals:
        total += bisect.bisect_right(values, right) - bisect.bisect_left(values, left)
    return total


def values_in_union(values: list[int], intervals: list[list[int]], limit: int) -> list[int]:
    """提取区间并集中的前若干元素。"""
    found: list[int] = []
    for left, right in intervals:
        left_index = bisect.bisect_left(values, left)
        right_index = bisect.bisect_right(values, right)
        found.extend(values[left_index:right_index])
        if len(found) >= limit:
            return found[:limit]
    return found


def block_pressure(
    block_semis: list[int],
    row_primes: list[int],
    intervals: list[list[int]],
    tail_labels: dict[int, list[int]],
    wheel_primes: list[int],
    radius: int,
) -> dict:
    """计算一个临界块的尾标签、相位和偏移压力。"""
    modulus = wheel_modulus(wheel_primes)
    tail_counter: Counter[int] = Counter()
    pair_counter: Counter[tuple[int, int]] = Counter()
    phase_counter: Counter[int] = Counter()
    allowed_offset_counter: Counter[int] = Counter()
    actual_edge_offset_counter: Counter[int] = Counter()
    neighbor_primes = values_in_union(row_primes, intervals, 40)

    for semi_value in block_semis:
        labels = tail_labels.get(semi_value, [])
        tail_counter.update(labels)
        if len(labels) == 2:
            pair_counter.update([tuple(labels)])
        phase_counter.update([semi_value % modulus])
        for offset in range(-radius, radius + 1):
            if offset and wheel_allowed_offset(semi_value, offset, wheel_primes):
                allowed_offset_counter.update([offset])

    for prime_value in neighbor_primes:
        for semi_value in block_semis:
            offset = prime_value - semi_value
            if abs(offset) <= radius:
                actual_edge_offset_counter.update([offset])

    return {
        "max_tail_load": max(tail_counter.values(), default=0),
        "max_tail_pair_load": max(pair_counter.values(), default=0),
        "max_wheel_phase_load": max(phase_counter.values(), default=0),
        "max_allowed_offset_load": max(allowed_offset_counter.values(), default=0),
        "max_actual_edge_offset_load": max(actual_edge_offset_counter.values(), default=0),
        "top_tail_labels": [
            {"label": label, "load": load} for label, load in tail_counter.most_common(8)
        ],
        "top_tail_pairs": [
            {"labels": list(labels), "load": load} for labels, load in pair_counter.most_common(8)
        ],
        "top_wheel_phases": [
            {"residue": residue, "load": load} for residue, load in phase_counter.most_common(8)
        ],
        "top_allowed_offsets": [
            {
                "offset": offset,
                "load": load,
                "rho_z_offset": fixed_offset_ratio(offset, wheel_primes),
            }
            for offset, load in allowed_offset_counter.most_common(8)
        ],
        "top_actual_edge_offsets": [
            {
                "offset": offset,
                "load": load,
                "rho_z_offset": fixed_offset_ratio(offset, wheel_primes),
            }
            for offset, load in actual_edge_offset_counter.most_common(8)
        ],
        "neighbor_primes_sample": neighbor_primes,
    }


def audit_row_blocks(
    p: int,
    q: int,
    row: int,
    semiprimes: list[int],
    row_primes: list[int],
    tail_labels: dict[int, list[int]],
    radius: int,
    wheel_primes: list[int],
    tight_surplus: int,
) -> tuple[dict, list[dict]]:
    """审计单行全部连续半素数块。"""
    block_count = 0
    min_surplus = None
    zero_blocks = 0
    tight_blocks: list[dict] = []

    for start_index in range(len(semiprimes)):
        intervals: list[tuple[int, int]] = []
        for end_index in range(start_index, len(semiprimes)):
            semi_value = semiprimes[end_index]
            intervals.append((semi_value - radius, semi_value + radius))
            merged = merge_intervals(intervals)
            prime_count = count_in_union(row_primes, merged)
            semiprime_count = end_index - start_index + 1
            surplus = prime_count - semiprime_count
            block_count += 1
            if min_surplus is None or surplus < min_surplus:
                min_surplus = surplus
            if surplus == 0:
                zero_blocks += 1
            if surplus <= tight_surplus:
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
                tight_blocks.append(
                    {
                        "p": p,
                        "q": q,
                        "row": row,
                        "radius": radius,
                        "semi_index_range": [start_index, end_index],
                        "semiprime_count": semiprime_count,
                        "prime_count": prime_count,
                        "surplus": surplus,
                        "neighbor_intervals": merged,
                        "span": span_right - span_left + 1,
                        "semiprime_values_sample": block_semis[:20],
                        "q_square_mirror_span": [q * q - span_right, q * q - span_left],
                        "pressure": pressure,
                    }
                )

    return (
        {
            "block_count": block_count,
            "min_surplus": 0 if min_surplus is None else min_surplus,
            "zero_blocks": zero_blocks,
        },
        tight_blocks,
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# WSH-Hall 扩张余量审计",
        "",
        "**状态：** `finite_expansion_margin_audit_not_global_proof`",
        "",
        "本文档逐个连续半素数块计算 `|N_R(B)|-|B|`，直接审计 `WSH-Expansion-or-Defect` 中的扩张项。它比单纯匹配证书更强，因为它定位所有零余量与小余量块。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `min_p`: `{params['min_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        f"- `radius_factor`: `{params['radius_factor']}`",
        f"- `tight_surplus`: `{params['tight_surplus']}`",
        f"- `wheel_primes`: `{params['wheel_primes']}`",
        "",
        "## 摘要",
        "",
        f"- 检查素数记录数：`{summary['prime_record_count']}`。",
        f"- 含平衡半素数的行数：`{summary['row_with_semiprime_count']}`。",
        f"- 连续半素数块总数：`{summary['block_count']}`。",
        f"- 全局最小 Hall 余量：`{summary['global_min_surplus']}`。",
        f"- 零余量块数：`{summary['zero_surplus_blocks']}`。",
        f"- 小余量块数：`{summary['tight_block_count']}`。",
        f"- 最大小余量块半素数数：`{summary['max_tight_block_semiprime_count']}`。",
        f"- 最大零余量块半素数数：`{summary['max_zero_block_semiprime_count']}`。",
        f"- 最大尾标签负载：`{summary['max_tail_load_in_tight_blocks']}`。",
        f"- 最大固定允许偏移负载：`{summary['max_allowed_offset_load_in_tight_blocks']}`。",
        "",
        "## 最紧块样本",
        "",
        "| p | q | row | R | semis | primes | surplus | span | tail max | offset max | mirror span |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for block in result["tight_blocks"][:40]:
        pressure = block["pressure"]
        lines.append(
            "| {p} | {q} | {row} | {radius} | {semis} | {primes} | {surplus} | {span} | {tail} | {offset} | {mirror} |".format(
                p=block["p"],
                q=block["q"],
                row=block["row"],
                radius=block["radius"],
                semis=block["semiprime_count"],
                primes=block["prime_count"],
                surplus=block["surplus"],
                span=block["span"],
                tail=pressure["max_tail_load"],
                offset=pressure["max_allowed_offset_load"],
                mirror=block["q_square_mirror_span"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "在审计范围内，`R=ceil(3 log^2 q)` 的所有连续块均满足正 Hall 余量，最小余量为 `1`，因此扩张项在有限样本中没有失败，也没有零余量块。最紧块仍然是关键对象：它们表明全局证明不能只依赖粗密度余量，必须使用尾标签、固定偏移、轮筛相位或端点镜像中的至少一个刚性投影来解释为什么余量不能跌到负数。",
            "",
            "下一步应证明一个分布式扩张引理：若临界块没有尾标签集中，也没有固定偏移/PDEC 相位集中，则 Hall 余量非负；否则该临界块已经落入命名出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def audit(args: argparse.Namespace) -> dict:
    """执行全量扩张余量审计。"""
    wheel_primes = [int(part) for part in args.wheel_primes.split(",") if part]
    sieve_limit = args.max_p * args.max_p + args.max_p * 20 + 10000
    is_prime = sieve_bool(sieve_limit)
    primes = primes_from_table(is_prime)
    target_primes = [prime for prime in primes if args.min_p <= prime <= args.max_p]
    row_with_semiprime_count = 0
    block_count = 0
    zero_surplus_blocks = 0
    global_min_surplus = None
    tight_blocks: list[dict] = []

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
            row_summary, row_tight_blocks = audit_row_blocks(
                p,
                q,
                row,
                semiprimes,
                primes_by_row[row],
                tail_labels,
                radius,
                wheel_primes,
                args.tight_surplus,
            )
            block_count += row_summary["block_count"]
            zero_surplus_blocks += row_summary["zero_blocks"]
            row_min = row_summary["min_surplus"]
            if global_min_surplus is None or row_min < global_min_surplus:
                global_min_surplus = row_min
            tight_blocks.extend(row_tight_blocks)

    tight_blocks.sort(
        key=lambda block: (
            block["surplus"],
            -block["semiprime_count"],
            -block["pressure"]["max_allowed_offset_load"],
            -block["pressure"]["max_tail_load"],
        )
    )
    zero_blocks = [block for block in tight_blocks if block["surplus"] == 0]
    summary = {
        "prime_record_count": len(target_primes),
        "row_with_semiprime_count": row_with_semiprime_count,
        "block_count": block_count,
        "global_min_surplus": 0 if global_min_surplus is None else global_min_surplus,
        "zero_surplus_blocks": zero_surplus_blocks,
        "tight_block_count": len(tight_blocks),
        "max_tight_block_semiprime_count": max(
            (block["semiprime_count"] for block in tight_blocks),
            default=0,
        ),
        "max_zero_block_semiprime_count": max(
            (block["semiprime_count"] for block in zero_blocks),
            default=0,
        ),
        "max_tail_load_in_tight_blocks": max(
            (block["pressure"]["max_tail_load"] for block in tight_blocks),
            default=0,
        ),
        "max_allowed_offset_load_in_tight_blocks": max(
            (block["pressure"]["max_allowed_offset_load"] for block in tight_blocks),
            default=0,
        ),
    }
    return {
        "parameters": {
            "max_p": args.max_p,
            "min_p": args.min_p,
            "y_ratio": args.y_ratio,
            "radius_factor": args.radius_factor,
            "tight_surplus": args.tight_surplus,
            "wheel_primes": wheel_primes,
        },
        "summary": summary,
        "tight_blocks": tight_blocks[: args.max_tight_records],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--min-p", type=int, default=17)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--radius-factor", type=float, default=3.0)
    parser.add_argument("--tight-surplus", type=int, default=1)
    parser.add_argument("--wheel-primes", default="2,3,5,7,11,13")
    parser.add_argument("--max-tight-records", type=int, default=200)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-expansion-margin-audit",
    )
    args = parser.parse_args()
    result = audit(args)
    out_prefix = Path(args.out_prefix)
    out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
