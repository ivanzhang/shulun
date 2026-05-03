#!/usr/bin/env python3
"""Singleton 走廊重叠与复用结构审计。

用法示例：
  python3 experiments/prime_matrix_singleton_corridor_overlap_audit.py
  python3 experiments/prime_matrix_singleton_corridor_overlap_audit.py --max-p 2000 --alpha 0.43
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_mge3_budget_audit import (
    MONOGRAPH,
    ceil_div,
    collect_hard_windows,
    primes_from_flags,
    sieve,
    smallest_prime_factor,
)
from prime_matrix_singleton_corridor_bound_audit import corridor_interval, count_corridor_objects

DEFAULT_JSON = MONOGRAPH / "prime-matrix-singleton-corridor-overlap-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-singleton-corridor-overlap-audit.md"


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """合并闭区间。"""
    if not intervals:
        return []
    ordered = sorted(intervals)
    merged = [ordered[0]]
    for left, right in ordered[1:]:
        last_left, last_right = merged[-1]
        if left <= last_right + 1:
            merged[-1] = (last_left, max(last_right, right))
        else:
            merged.append((left, right))
    return merged


def interval_width(interval: tuple[int, int]) -> int:
    """闭区间长度。"""
    left, right = interval
    return max(0, right - left + 1)


def max_overlap(intervals: list[tuple[int, int]]) -> int:
    """计算闭区间族最大重叠度。"""
    events: list[tuple[int, int]] = []
    for left, right in intervals:
        events.append((left, 1))
        events.append((right + 1, -1))
    current = 0
    maximum = 0
    for _, delta in sorted(events):
        current += delta
        maximum = max(maximum, current)
    return maximum


def collect_singleton_corridors(
    max_p: int,
    alpha: float,
    tail_fraction: float,
    keep: int,
    primes: list[int],
    prime_flags: bytearray,
    spf: list[int],
) -> list[dict[str, Any]]:
    """收集唯一 singleton-prime 走廊。"""
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    corridors: dict[tuple[int, int, int, int, int], dict[str, Any]] = {}
    for window in hard_windows:
        p = window["p"]
        z = window["z"]
        left = window["left"]
        right = window["right"]
        max_first_anchor = int(round(right ** (1.0 / 3.0))) + 2
        for first_anchor in primes:
            if first_anchor <= z:
                continue
            if first_anchor > max_first_anchor:
                break
            max_second_anchor = int(math.isqrt(right // first_anchor))
            for second_anchor in primes:
                if second_anchor < first_anchor:
                    continue
                if second_anchor > max_second_anchor:
                    break
                pair = first_anchor * second_anchor
                tail_left = max(second_anchor, ceil_div(left, pair))
                tail_right = right // pair
                if tail_left != tail_right:
                    continue
                tail_value = tail_left
                if not prime_flags[tail_value]:
                    continue
                key = (p, window["q_row"], left, right, tail_value)
                if key not in corridors:
                    corridor_left, corridor_right = corridor_interval(left, right, tail_value)
                    width = max(0, corridor_right - corridor_left + 1)
                    counts = count_corridor_objects(corridor_left, corridor_right, z, tail_value, prime_flags, spf)
                    corridors[key] = {
                        "p": p,
                        "q": window["q"],
                        "q_row": window["q_row"],
                        "left": left,
                        "right": right,
                        "z": z,
                        "tail_value": tail_value,
                        "corridor_left": corridor_left,
                        "corridor_right": corridor_right,
                        "width": width,
                        "z_rough_count": counts["z_rough_count"],
                        "semiprime_pair_count": counts["semiprime_pair_count"],
                        "anchors": [],
                    }
                corridors[key]["anchors"].append([first_anchor, second_anchor])
    return list(corridors.values())


def audit_overlap(corridors: list[dict[str, Any]]) -> dict[str, Any]:
    """审计走廊在同一 ASB 窗口内的重叠与复用。"""
    by_window: dict[tuple[int, int, int, int], list[dict[str, Any]]] = {}
    for row in corridors:
        key = (row["p"], row["q_row"], row["left"], row["right"])
        by_window.setdefault(key, []).append(row)

    window_rows = []
    total_width_sum = 0
    total_union_width = 0
    total_overlap_excess = 0
    total_semiprime_pairs = 0
    total_z_rough = 0
    for key, rows in by_window.items():
        intervals = [(row["corridor_left"], row["corridor_right"]) for row in rows]
        merged = merge_intervals(intervals)
        width_sum = sum(row["width"] for row in rows)
        union_width = sum(interval_width(interval) for interval in merged)
        semiprime_pairs = sum(row["semiprime_pair_count"] for row in rows)
        z_rough = sum(row["z_rough_count"] for row in rows)
        overlap_excess = width_sum - union_width
        total_width_sum += width_sum
        total_union_width += union_width
        total_overlap_excess += overlap_excess
        total_semiprime_pairs += semiprime_pairs
        total_z_rough += z_rough
        p, q_row, left, right = key
        window_rows.append(
            {
                "p": p,
                "q_row": q_row,
                "left": left,
                "right": right,
                "corridor_count": len(rows),
                "width_sum": width_sum,
                "union_width": union_width,
                "overlap_excess": overlap_excess,
                "max_overlap": max_overlap(intervals),
                "merged_interval_count": len(merged),
                "semiprime_pair_count": semiprime_pairs,
                "z_rough_count": z_rough,
                "pair_union_ratio": None if union_width == 0 else semiprime_pairs / union_width,
                "zrough_union_ratio": None if union_width == 0 else z_rough / union_width,
            }
        )

    top_overlap = sorted(window_rows, key=lambda row: (row["overlap_excess"], row["corridor_count"]), reverse=True)[:16]
    top_density = sorted(window_rows, key=lambda row: (row["pair_union_ratio"] or 0.0, row["semiprime_pair_count"]), reverse=True)[:16]
    top_corridors_by_anchor_reuse = sorted(
        corridors,
        key=lambda row: (len(row["anchors"]), row["semiprime_pair_count"], row["width"]),
        reverse=True,
    )[:16]

    return {
        "window_count": len(by_window),
        "corridor_count": len(corridors),
        "width_sum": total_width_sum,
        "union_width": total_union_width,
        "overlap_excess": total_overlap_excess,
        "global_max_overlap": max((row["max_overlap"] for row in window_rows), default=0),
        "semiprime_pair_count": total_semiprime_pairs,
        "z_rough_count": total_z_rough,
        "pair_union_ratio": None if total_union_width == 0 else total_semiprime_pairs / total_union_width,
        "zrough_union_ratio": None if total_union_width == 0 else total_z_rough / total_union_width,
        "top_overlap_windows": top_overlap,
        "top_density_windows": top_density,
        "top_corridors_by_anchor_reuse": top_corridors_by_anchor_reuse,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成 singleton 走廊重叠审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    corridors = collect_singleton_corridors(max_p, alpha, tail_fraction, keep, primes, prime_flags, spf)
    overlap = audit_overlap(corridors)
    return {
        "certificate_type": "prime_matrix_singleton_corridor_overlap_audit",
        "status": "singleton_corridors_reduced_to_disjoint_window_unions",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "overlap": overlap,
        "review_conclusion": (
            "Singleton 走廊在同一 ASB 窗口内的重叠可直接审计。"
            "若重叠很小或为零，singleton 侧上界可转为不相交短区间族的 z-rough Selberg 上界；"
            "若出现高重叠或高复用，则该局部窗口自身成为 Tail-anchor/CRTDefect 出口。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    overlap = audit["overlap"]

    def fmt(value: float | None) -> str:
        """格式化可空浮点数。"""
        return "NA" if value is None else f"{value:.6f}"

    lines = [
        "# Singleton 走廊重叠与复用审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告检查 singleton-prime 走廊在同一 ASB 窗口内是否大量重叠。若走廊近似不相交，则可直接转入不相交短区间族筛上界；若重叠高，则本身就是局部复用异常出口。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 全局重叠账本",
        "",
        f"- 含 singleton 走廊窗口数：`{overlap['window_count']}`。",
        f"- 走廊数：`{overlap['corridor_count']}`。",
        f"- 走廊宽度和：`{overlap['width_sum']}`。",
        f"- 同窗口并集宽度：`{overlap['union_width']}`。",
        f"- 重叠冗余：`{overlap['overlap_excess']}`。",
        f"- 最大重叠度：`{overlap['global_max_overlap']}`。",
        f"- semiprime 对数：`{overlap['semiprime_pair_count']}`。",
        f"- z-rough 数：`{overlap['z_rough_count']}`。",
        f"- semiprime/并集宽度：`{fmt(overlap['pair_union_ratio'])}`。",
        f"- z-rough/并集宽度：`{fmt(overlap['zrough_union_ratio'])}`。",
        "",
        "## 3. 重叠最高窗口",
        "",
        "| p | q行 | J | 走廊数 | 宽度和 | 并集宽度 | 冗余 | 最大重叠 | semiprime | z-rough |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in overlap["top_overlap_windows"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | `[{row['left']},{row['right']}]` | "
            f"{row['corridor_count']} | {row['width_sum']} | {row['union_width']} | "
            f"{row['overlap_excess']} | {row['max_overlap']} | "
            f"{row['semiprime_pair_count']} | {row['z_rough_count']} |"
        )
    lines += [
        "",
        "## 4. 密度最高窗口",
        "",
        "| p | q行 | J | 并集宽度 | semiprime | z-rough | semi/并集 | zrough/并集 |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in overlap["top_density_windows"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | `[{row['left']},{row['right']}]` | "
            f"{row['union_width']} | {row['semiprime_pair_count']} | {row['z_rough_count']} | "
            f"{fmt(row['pair_union_ratio'])} | {fmt(row['zrough_union_ratio'])} |"
        )
    lines += [
        "",
        "## 5. 锚复用最高走廊",
        "",
        "| p | q行 | d | C_d | 宽度 | semiprime | z-rough | anchors |",
        "| ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in overlap["top_corridors_by_anchor_reuse"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['tail_value']} | "
            f"`[{row['corridor_left']},{row['corridor_right']}]` | {row['width']} | "
            f"{row['semiprime_pair_count']} | {row['z_rough_count']} | `{row['anchors'][:8]}` |"
        )
    lines += [
        "",
        "## 6. 新最小硬点",
        "",
        "若同窗口走廊族近似不相交，则 singleton 侧可改写为：",
        "",
        "```text",
        "z-rough upper sieve on disjoint singleton-corridor unions",
        "or high overlap/reuse => Tail-anchor/CRTDefect.",
        "```",
        "",
        "这一步把走廊上界从逐单点问题提升为同窗口不相交区间族问题；可用的刚性包括单调商分层、唯一分解、低筛非零同余和锚复用限制。",
        "",
        "## 7. 审稿结论",
        "",
        audit["review_conclusion"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--keep", type=int, default=40)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p, args.alpha, args.tail_fraction, args.keep)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
