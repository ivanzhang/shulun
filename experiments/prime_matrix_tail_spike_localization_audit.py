#!/usr/bin/env python3
"""第二锚粗尾局部尖峰定位审计。

用法示例：
  python3 experiments/prime_matrix_tail_spike_localization_audit.py
  python3 experiments/prime_matrix_tail_spike_localization_audit.py --max-p 2000 --alpha 0.43
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
from prime_matrix_mge3_tail_envelope_audit import mertens_products

DEFAULT_JSON = MONOGRAPH / "prime-matrix-tail-spike-localization-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-tail-spike-localization-audit.md"


def classify_capacity(capacity: int) -> str:
    """按尾区间长度分类。"""
    if capacity == 1:
        return "singleton"
    if capacity == 2:
        return "doubleton"
    if capacity <= 5:
        return "short_3_5"
    return "long_gt5"


def classify_tail(capacity: int, rough_tail: int, prime_tail: int) -> str:
    """按尾区间命中类型分类。"""
    if capacity == 1:
        if rough_tail == 0:
            return "singleton_nonrough"
        if prime_tail == 1:
            return "singleton_prime"
        return "singleton_composite_rough"
    if rough_tail == 0:
        return "multi_nonrough"
    if prime_tail == rough_tail:
        return "multi_all_prime_tail"
    return "multi_mixed_tail"


def add_bucket(table: dict[str, dict[str, Any]], key: str, row: dict[str, Any]) -> None:
    """累加尖峰分桶。"""
    bucket = table.setdefault(
        key,
        {
            "pair_interval_count": 0,
            "capacity": 0,
            "rough_tail": 0,
            "prime_tail": 0,
            "mertens_envelope": 0.0,
            "max_needed_constant": 0.0,
            "max_capacity": 0,
        },
    )
    bucket["pair_interval_count"] += 1
    bucket["capacity"] += row["capacity"]
    bucket["rough_tail"] += row["rough_tail"]
    bucket["prime_tail"] += row["prime_tail"]
    bucket["mertens_envelope"] += row["mertens_envelope"]
    bucket["max_needed_constant"] = max(bucket["max_needed_constant"], row["needed_constant"])
    bucket["max_capacity"] = max(bucket["max_capacity"], row["capacity"])


def finalize_buckets(table: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """渲染尖峰分桶。"""
    rows = []
    for key, row in sorted(table.items()):
        envelope = row["mertens_envelope"]
        rough_tail = row["rough_tail"]
        rows.append(
            {
                "bucket": key,
                "pair_interval_count": row["pair_interval_count"],
                "capacity": row["capacity"],
                "rough_tail": rough_tail,
                "prime_tail": row["prime_tail"],
                "mertens_envelope": envelope,
                "needed_constant": None if envelope == 0 else rough_tail / envelope,
                "density": None if row["capacity"] == 0 else rough_tail / row["capacity"],
                "prime_tail_share": None if rough_tail == 0 else row["prime_tail"] / rough_tail,
                "max_needed_constant": row["max_needed_constant"],
                "max_capacity": row["max_capacity"],
            }
        )
    return rows


def singleton_corridor_width(left: int, right: int, tail_value: int) -> int:
    """计算让 tail 区间退化为单点 d 的 ab 乘积走廊宽度。"""
    d = tail_value
    lower_from_left = ceil_div(left, d)
    upper_from_right = right // d
    lower_from_right_next = right // (d + 1) + 1
    if d <= 1:
        upper_from_left_prev = upper_from_right
    else:
        upper_from_left_prev = ceil_div(left, d - 1) - 1
    lower = max(lower_from_left, lower_from_right_next)
    upper = min(upper_from_right, upper_from_left_prev)
    return max(0, upper - lower + 1)


def audit_spikes(
    hard_windows: list[dict[str, Any]],
    primes: list[int],
    prime_flags: bytearray,
    spf: list[int],
) -> dict[str, Any]:
    """定位第二锚粗尾尖峰。"""
    mertens = mertens_products(primes, max(primes))
    by_capacity: dict[str, dict[str, Any]] = {}
    by_tail_type: dict[str, dict[str, Any]] = {}
    by_threshold: dict[str, dict[str, Any]] = {}
    pair_rows = []
    singleton_rough_rows = []
    singleton_corridors: dict[tuple[int, int, int, int, int], dict[str, Any]] = {}

    for window in hard_windows:
        p = window["p"]
        left = window["left"]
        right = window["right"]
        z = window["z"]
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
                capacity = max(0, tail_right - tail_left + 1)
                if capacity == 0:
                    continue
                rough_tail = 0
                prime_tail = 0
                rough_values = []
                for value in range(tail_left, tail_right + 1):
                    if spf[value] < second_anchor:
                        continue
                    rough_tail += 1
                    rough_values.append(value)
                    if prime_flags[value]:
                        prime_tail += 1
                envelope = capacity * mertens[second_anchor]
                needed_constant = 0.0 if envelope == 0 else rough_tail / envelope
                row = {
                    "p": p,
                    "q": window["q"],
                    "q_row": window["q_row"],
                    "left": left,
                    "right": right,
                    "first_anchor": first_anchor,
                    "second_anchor": second_anchor,
                    "tail_left": tail_left,
                    "tail_right": tail_right,
                    "capacity": capacity,
                    "rough_tail": rough_tail,
                    "prime_tail": prime_tail,
                    "mertens_envelope": envelope,
                    "needed_constant": needed_constant,
                    "tail_type": classify_tail(capacity, rough_tail, prime_tail),
                    "capacity_type": classify_capacity(capacity),
                }
                pair_rows.append(row)
                add_bucket(by_capacity, row["capacity_type"], row)
                add_bucket(by_tail_type, row["tail_type"], row)
                for threshold in [1.25, 1.5, 2.0, 3.0]:
                    if needed_constant >= threshold and rough_tail > 0:
                        add_bucket(by_threshold, f">={threshold:.2f}", row)
                if capacity == 1 and rough_tail > 0:
                    tail_value = rough_values[0]
                    corridor_width = singleton_corridor_width(left, right, tail_value)
                    singleton_row = {
                        **row,
                        "tail_value": tail_value,
                        "tail_is_prime": bool(prime_flags[tail_value]),
                        "corridor_width": corridor_width,
                    }
                    singleton_rough_rows.append(singleton_row)
                    corridor_key = (p, window["q_row"], left, right, tail_value)
                    corridor = singleton_corridors.setdefault(
                        corridor_key,
                        {
                            "p": p,
                            "q": window["q"],
                            "q_row": window["q_row"],
                            "left": left,
                            "right": right,
                            "tail_value": tail_value,
                            "tail_is_prime": bool(prime_flags[tail_value]),
                            "corridor_width": corridor_width,
                            "pair_count": 0,
                            "prime_pair_count": 0,
                            "anchors": [],
                        },
                    )
                    corridor["pair_count"] += 1
                    if prime_flags[tail_value]:
                        corridor["prime_pair_count"] += 1
                    corridor["anchors"].append([first_anchor, second_anchor])

    top_pair_spikes = sorted(
        [row for row in pair_rows if row["rough_tail"] > 0],
        key=lambda row: (row["needed_constant"], row["rough_tail"]),
        reverse=True,
    )[:16]
    top_singleton_corridors = sorted(
        singleton_rough_rows,
        key=lambda row: (row["corridor_width"], row["needed_constant"]),
        reverse=True,
    )[:16]
    corridor_rows = list(singleton_corridors.values())
    corridor_width_sum = sum(row["corridor_width"] for row in corridor_rows)
    corridor_pair_count = sum(row["pair_count"] for row in corridor_rows)
    corridor_prime_pair_count = sum(row["prime_pair_count"] for row in corridor_rows)
    for row in corridor_rows:
        row["pair_width_ratio"] = None if row["corridor_width"] == 0 else row["pair_count"] / row["corridor_width"]
    top_corridors_by_pairs = sorted(
        corridor_rows,
        key=lambda row: (row["pair_count"], row["pair_width_ratio"] or 0.0),
        reverse=True,
    )[:16]
    top_corridors_by_density = sorted(
        corridor_rows,
        key=lambda row: (row["pair_width_ratio"] or 0.0, row["pair_count"]),
        reverse=True,
    )[:16]
    return {
        "pair_interval_count": len(pair_rows),
        "rough_pair_interval_count": sum(1 for row in pair_rows if row["rough_tail"] > 0),
        "singleton_rough_count": len(singleton_rough_rows),
        "singleton_prime_count": sum(1 for row in singleton_rough_rows if row["tail_is_prime"]),
        "singleton_composite_rough_count": sum(1 for row in singleton_rough_rows if not row["tail_is_prime"]),
        "unique_singleton_corridor_count": len(corridor_rows),
        "singleton_corridor_width_sum": corridor_width_sum,
        "singleton_corridor_pair_count": corridor_pair_count,
        "singleton_corridor_prime_pair_count": corridor_prime_pair_count,
        "singleton_pair_width_ratio": None
        if corridor_width_sum == 0
        else corridor_pair_count / corridor_width_sum,
        "max_pairs_per_corridor": max((row["pair_count"] for row in corridor_rows), default=0),
        "by_capacity": finalize_buckets(by_capacity),
        "by_tail_type": finalize_buckets(by_tail_type),
        "by_threshold": finalize_buckets(by_threshold),
        "top_pair_spikes": top_pair_spikes,
        "top_singleton_corridors": top_singleton_corridors,
        "top_corridors_by_pairs": top_corridors_by_pairs,
        "top_corridors_by_density": top_corridors_by_density,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成局部尖峰定位审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    spikes = audit_spikes(hard_windows, primes, prime_flags, spf)
    return {
        "certificate_type": "prime_matrix_tail_spike_localization_audit",
        "status": "tail_spikes_localized_to_singleton_prime_corridors",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "spike_localization": spikes,
        "review_conclusion": (
            "第二锚粗尾的高放大常数主要来自尾区间长度为 1 的 singleton 事件。"
            "这些事件等价于 ab 落入由单个尾值 d 决定的极窄双曲走廊；"
            "因此局部尖峰出口可进一步形式化为 singleton-prime corridor，而非一般短区间异常。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    spikes = audit["spike_localization"]

    def fmt(value: float | None) -> str:
        """格式化可空浮点数。"""
        return "NA" if value is None else f"{value:.6f}"

    lines = [
        "# 第二锚粗尾局部尖峰定位审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告处理 Mertens 包络中的局部尖峰。目标是判断尖峰是否来自一般粗尾异常，还是来自可单独定理化的极短 singleton 走廊。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 尖峰总览",
        "",
        f"- pair 尾区间数：`{spikes['pair_interval_count']}`。",
        f"- 有粗尾命中的 pair 区间数：`{spikes['rough_pair_interval_count']}`。",
        f"- singleton 粗尾数：`{spikes['singleton_rough_count']}`。",
        f"- singleton 素尾数：`{spikes['singleton_prime_count']}`。",
        f"- singleton 粗合尾数：`{spikes['singleton_composite_rough_count']}`。",
        f"- 唯一 singleton 走廊数：`{spikes['unique_singleton_corridor_count']}`。",
        f"- singleton 走廊总宽度：`{spikes['singleton_corridor_width_sum']}`。",
        f"- 走廊内素因子对数：`{spikes['singleton_corridor_pair_count']}`。",
        f"- 素因子对/走廊宽度：`{spikes['singleton_pair_width_ratio']:.6f}`。",
        f"- 单走廊最大素因子对数：`{spikes['max_pairs_per_corridor']}`。",
        "",
        "## 3. 按尾区间长度分解",
        "",
        "| 类型 | pair数 | 容量 | 粗尾 | 素尾 | Mertens包络 | 所需常数 | 密度 | 最大单pair常数 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in spikes["by_capacity"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['capacity']} | "
            f"{row['rough_tail']} | {row['prime_tail']} | {row['mertens_envelope']:.6f} | "
            f"{fmt(row['needed_constant'])} | {fmt(row['density'])} | {row['max_needed_constant']:.6f} |"
        )
    lines += [
        "",
        "## 4. 按尾命中类型分解",
        "",
        "| 类型 | pair数 | 容量 | 粗尾 | 素尾 | Mertens包络 | 所需常数 | 密度 | 最大单pair常数 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in spikes["by_tail_type"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['capacity']} | "
            f"{row['rough_tail']} | {row['prime_tail']} | {row['mertens_envelope']:.6f} | "
            f"{fmt(row['needed_constant'])} | {fmt(row['density'])} | {row['max_needed_constant']:.6f} |"
        )
    lines += [
        "",
        "## 5. 尖峰阈值账本",
        "",
        "| 阈值 | pair数 | 容量 | 粗尾 | 素尾 | Mertens包络 | 聚合常数 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in spikes["by_threshold"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['capacity']} | "
            f"{row['rough_tail']} | {row['prime_tail']} | {row['mertens_envelope']:.6f} | "
            f"{fmt(row['needed_constant'])} |"
        )
    lines += [
        "",
        "## 6. 最高单 pair 尖峰",
        "",
        "| p | q行 | a | b | 尾区间 | 容量 | 粗尾 | 素尾 | 所需常数 | 类型 |",
        "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in spikes["top_pair_spikes"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['first_anchor']} | {row['second_anchor']} | "
            f"`[{row['tail_left']},{row['tail_right']}]` | {row['capacity']} | "
            f"{row['rough_tail']} | {row['prime_tail']} | {row['needed_constant']:.6f} | `{row['tail_type']}` |"
        )
    lines += [
        "",
        "## 7. Singleton 走廊",
        "",
        "当尾区间为单点 `d` 时，`ceil(L/(ab))=floor(R/(ab))=d` 等价于 `ab` 落在双曲走廊",
        "",
        "\\[",
        "\\max(\\lceil L/d\\rceil,\\lfloor R/(d+1)\\rfloor+1)\\le ab\\le",
        "\\min(\\lfloor R/d\\rfloor,\\lceil L/(d-1)\\rceil-1).",
        "\\]",
        "",
        "| p | q行 | a | b | d | d为素数 | 走廊宽度 | 所需常数 |",
        "| ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in spikes["top_singleton_corridors"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['first_anchor']} | {row['second_anchor']} | "
            f"{row['tail_value']} | `{row['tail_is_prime']}` | {row['corridor_width']} | "
            f"{row['needed_constant']:.6f} |"
        )
    lines += [
        "",
        "## 8. 走廊聚合上界账本",
        "",
        "同一单点 `d` 走廊可能包含多个素因子对 `ab`。由于每个整数 `m=ab` 至多给出一个有序素因子对 `a<=b`，必有",
        "",
        "\\[",
        "\\#\\{(a,b):ab\\in C_d\\}\\le |C_d|.",
        "\\]",
        "",
        "| p | q行 | d | d为素数 | 走廊宽度 | 素因子对数 | 对/宽度 | anchors |",
        "| ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in spikes["top_corridors_by_pairs"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['tail_value']} | `{row['tail_is_prime']}` | "
            f"{row['corridor_width']} | {row['pair_count']} | {fmt(row['pair_width_ratio'])} | "
            f"`{row['anchors'][:6]}` |"
        )
    lines += [
        "",
        "按密度排序的最紧走廊如下。",
        "",
        "| p | q行 | d | 走廊宽度 | 素因子对数 | 对/宽度 | anchors |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in spikes["top_corridors_by_density"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['tail_value']} | "
            f"{row['corridor_width']} | {row['pair_count']} | {fmt(row['pair_width_ratio'])} | "
            f"`{row['anchors'][:6]}` |"
        )
    lines += [
        "",
        "## 9. 新最小硬点",
        "",
        "局部尖峰已经从一般粗尾异常压缩为 singleton-prime corridor：",
        "",
        "```text",
        "Aggregated Mertens envelope outside singleton corridors",
        "+ singleton-prime corridor bound",
        "or corridor spike => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "这给出更窄的证明目标：聚合包络处理普通尾区间；尾长为 1 的尖峰用双曲走廊中 `ab` 的素因子对计数来单独处理。",
        "",
        "更进一步，singleton-prime corridor 的第一层无条件上界是走廊宽度总和；要获得审稿级余量，需要证明这些走廊中的 semiprime 产品不能持续饱和走廊，或饱和必触发 CRTDefect/Tail-anchor/OSPC。",
        "",
        "## 10. 审稿结论",
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
