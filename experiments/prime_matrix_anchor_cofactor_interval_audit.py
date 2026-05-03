#!/usr/bin/env python3
"""锚层互补素数短区间审计。

用法示例：
  python3 experiments/prime_matrix_anchor_cofactor_interval_audit.py
  python3 experiments/prime_matrix_anchor_cofactor_interval_audit.py --max-p 2000 --alpha 0.43
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-anchor-cofactor-interval-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-anchor-cofactor-interval-audit.md"


def sieve(n: int) -> bytearray:
    """返回不超过 n 的素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    p = 2
    while p * p <= n:
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return flags


def prime_prefix(flags: bytearray) -> list[int]:
    """构造素数计数前缀和。"""
    prefix = [0] * len(flags)
    total = 0
    for i, flag in enumerate(flags):
        if flag:
            total += 1
        prefix[i] = total
    return prefix


def primes_from_flags(flags: bytearray) -> list[int]:
    """从素数标记表抽取素数。"""
    return [i for i in range(2, len(flags)) if flags[i]]


def smallest_prime_factor(n: int) -> list[int]:
    """构造最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
        p += 1
    return spf


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行对应的闭区间。"""
    return (row - 1) * width + 1, row * width


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否含完整旧 p 行。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def sampled_windows(p: int, q: int, tail_fraction: float) -> list[tuple[int, int, int, int]]:
    """列出后排 ASB 采样窗口。"""
    g = q - p
    last_full_q_row = (p * p) // q
    tail_start = max(1, int((1.0 - tail_fraction) * last_full_q_row))
    windows = []
    for s in range(tail_start, last_full_q_row + 1):
        left, right = row_interval(q, s)
        if contains_full_p_row(p, left, right):
            continue
        r = (left - 1) % p
        if r <= g:
            continue
        windows.append((s, left, right, r))
    return windows


def beta_bucket(anchor: int, p: int, alpha: float) -> str:
    """按 anchor≈p^beta 分桶。"""
    beta = math.log(anchor) / math.log(p)
    edges = [alpha, 0.50, 0.60, 0.70, 0.80, 0.90, 1.01]
    for lo, hi in zip(edges, edges[1:]):
        if lo <= beta < hi:
            return f"[{lo:.2f},{hi:.2f})"
    return "outside"


def ceil_div(a: int, b: int) -> int:
    """整数上取整除法。"""
    return -(-a // b)


def count_primes(prefix: list[int], left: int, right: int) -> int:
    """闭区间素数计数。"""
    if right < left:
        return 0
    right = min(right, len(prefix) - 1)
    left = max(left, 2)
    if right < left:
        return 0
    return prefix[right] - (prefix[left - 1] if left > 0 else 0)


def window_prime_ratio(left: int, right: int, z: int, prime_flags: bytearray, spf: list[int]) -> tuple[int, int, float | None]:
    """计算低筛粗剩余和素数比例。"""
    rough = 0
    primes = 0
    for n in range(left, right + 1):
        if spf[n] <= z:
            continue
        rough += 1
        if prime_flags[n]:
            primes += 1
    return rough, primes, None if rough == 0 else primes / rough


def collect_hard_windows(
    max_p: int,
    alpha: float,
    tail_fraction: float,
    keep: int,
    prime_flags: bytearray,
    spf: list[int],
) -> list[dict[str, Any]]:
    """收集 RPD 压力最大的窗口。"""
    small_flags = sieve(max_p + 200)
    base_primes = [p for p in primes_from_flags(small_flags) if p >= 3]
    rows = []
    for p, q in zip(base_primes, base_primes[1:]):
        if p > max_p:
            break
        z = max(2, int(p**alpha))
        for q_row, left, right, r in sampled_windows(p, q, tail_fraction):
            rough, prime_count, ratio = window_prime_ratio(left, right, z, prime_flags, spf)
            if rough:
                rows.append(
                    {
                        "p": p,
                        "q": q,
                        "z": z,
                        "q_row": q_row,
                        "left": left,
                        "right": right,
                        "r": r,
                        "rough_count": rough,
                        "prime_count": prime_count,
                        "prime_ratio": ratio,
                    }
                )
    rows.sort(key=lambda row: (row["prime_ratio"], -row["rough_count"]))
    return rows[:keep]


def analyze_cofactor_intervals(
    hard_windows: list[dict[str, Any]],
    alpha: float,
    primes: list[int],
    prefix: list[int],
) -> dict[str, Any]:
    """分析互补素数短区间。"""
    buckets: dict[str, dict[str, Any]] = {}
    intervals = []
    window_summaries: dict[tuple[int, int, int], dict[str, Any]] = {}
    for window in hard_windows:
        key = (window["p"], window["left"], window["right"])
        window_summaries[key] = {
            "p": window["p"],
            "q": window["q"],
            "q_row": window["q_row"],
            "left": window["left"],
            "right": window["right"],
            "rough_count": window["rough_count"],
            "rough_prime_count": window["prime_count"],
            "rough_prime_ratio": window["prime_ratio"],
            "interval_count": 0,
            "integer_capacity": 0,
            "prime_cofactor_count": 0,
        }
    for window in hard_windows:
        p = window["p"]
        left = window["left"]
        right = window["right"]
        z = window["z"]
        window_key = (p, left, right)
        for anchor in primes:
            if anchor <= z:
                continue
            if anchor > p:
                break
            co_left = max(anchor, ceil_div(left, anchor))
            co_right = right // anchor
            capacity = max(0, co_right - co_left + 1)
            if capacity == 0:
                continue
            prime_count = count_primes(prefix, co_left, co_right)
            bucket = beta_bucket(anchor, p, alpha)
            window_summary = window_summaries[window_key]
            window_summary["interval_count"] += 1
            window_summary["integer_capacity"] += capacity
            window_summary["prime_cofactor_count"] += prime_count
            entry = buckets.setdefault(
                bucket,
                {
                    "interval_count": 0,
                    "integer_capacity": 0,
                    "prime_cofactor_count": 0,
                    "nonzero_prime_intervals": 0,
                    "max_prime_count": 0,
                    "max_density": 0.0,
                    "cofactor_left_min": None,
                    "cofactor_right_max": None,
                },
            )
            entry["interval_count"] += 1
            entry["integer_capacity"] += capacity
            entry["prime_cofactor_count"] += prime_count
            if prime_count > 0:
                entry["nonzero_prime_intervals"] += 1
            entry["max_prime_count"] = max(entry["max_prime_count"], prime_count)
            density = prime_count / capacity
            entry["max_density"] = max(entry["max_density"], density)
            entry["cofactor_left_min"] = (
                co_left
                if entry["cofactor_left_min"] is None
                else min(entry["cofactor_left_min"], co_left)
            )
            entry["cofactor_right_max"] = (
                co_right
                if entry["cofactor_right_max"] is None
                else max(entry["cofactor_right_max"], co_right)
            )
            intervals.append(
                {
                    "p": p,
                    "anchor": anchor,
                    "bucket": bucket,
                    "co_left": co_left,
                    "co_right": co_right,
                    "capacity": capacity,
                    "prime_count": prime_count,
                    "density": density,
                }
            )
    rendered = []
    total_capacity = 0
    total_prime_count = 0
    total_intervals = 0
    for name, entry in sorted(buckets.items()):
        total_capacity += entry["integer_capacity"]
        total_prime_count += entry["prime_cofactor_count"]
        total_intervals += entry["interval_count"]
        rendered.append(
            {
                "bucket": name,
                "interval_count": entry["interval_count"],
                "integer_capacity": entry["integer_capacity"],
                "prime_cofactor_count": entry["prime_cofactor_count"],
                "prime_density": None
                if entry["integer_capacity"] == 0
                else entry["prime_cofactor_count"] / entry["integer_capacity"],
                "nonzero_prime_intervals": entry["nonzero_prime_intervals"],
                "max_prime_count": entry["max_prime_count"],
                "max_density": entry["max_density"],
                "cofactor_left_min": entry["cofactor_left_min"],
                "cofactor_right_max": entry["cofactor_right_max"],
            }
        )
    top_intervals = sorted(intervals, key=lambda row: (row["density"], row["prime_count"]), reverse=True)[:12]
    per_window = []
    for entry in window_summaries.values():
        composite_count = entry["rough_count"] - entry["rough_prime_count"]
        entry["cofactor_density"] = (
            None
            if entry["integer_capacity"] == 0
            else entry["prime_cofactor_count"] / entry["integer_capacity"]
        )
        entry["semiprime_to_rough"] = (
            None if entry["rough_count"] == 0 else entry["prime_cofactor_count"] / entry["rough_count"]
        )
        entry["semiprime_to_composite"] = (
            None if composite_count <= 0 else entry["prime_cofactor_count"] / composite_count
        )
        entry["other_composite_count"] = composite_count - entry["prime_cofactor_count"]
        per_window.append(entry)
    worst_prime_ratio_windows = sorted(
        per_window, key=lambda row: (row["rough_prime_ratio"], -row["rough_count"])
    )[:12]
    highest_semiprime_pressure_windows = sorted(
        per_window,
        key=lambda row: (
            -1.0 if row["semiprime_to_composite"] is None else row["semiprime_to_composite"],
            row["rough_prime_ratio"],
        ),
        reverse=True,
    )[:12]
    return {
        "total_intervals": total_intervals,
        "total_integer_capacity": total_capacity,
        "total_prime_cofactor_count": total_prime_count,
        "overall_prime_density": None if total_capacity == 0 else total_prime_count / total_capacity,
        "buckets": rendered,
        "top_density_intervals": top_intervals,
        "per_window": per_window,
        "worst_prime_ratio_windows": worst_prime_ratio_windows,
        "highest_semiprime_pressure_windows": highest_semiprime_pressure_windows,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成互补素数短区间审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    prefix = prime_prefix(prime_flags)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    cofactor = analyze_cofactor_intervals(hard_windows, alpha, primes, prefix)
    return {
        "certificate_type": "prime_matrix_anchor_cofactor_interval_audit",
        "status": "anchor_layer_reduced_to_average_prime_cofactor_intervals",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "cofactor_projection": cofactor,
        "review_conclusion": (
            "锚层半素数计数精确等于互补素数短区间计数的分层和。"
            "高锚层效率高主要来自互补区间很短；证明应转为平均互补素数短区间上界，"
            "或证明某些互补区间素数密度异常触发 CRTDefect/Tail-anchor/OSPC。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    projection = audit["cofactor_projection"]
    lines = [
        "# 锚层互补素数短区间审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告继续攻坚锚层半素数接口。对锚 `a`，半素数贡献不是任意容量，而是互补因子 `b` 落在短区间",
        "",
        "\\[",
        "\\max(a,\\lceil L/a\\rceil)\\le b\\le \\lfloor R/a\\rfloor",
        "\\]",
        "",
        "中的素数数。因此",
        "",
        "\\[",
        "S_a(J)=\\pi(\\lfloor R/a\\rfloor)-\\pi(\\max(a,\\lceil L/a\\rceil)-1).",
        "\\]",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 总体互补区间",
        "",
        f"- 互补区间数：`{projection['total_intervals']}`。",
        f"- 整数容量总和：`{projection['total_integer_capacity']}`。",
        f"- 素互补因子总数：`{projection['total_prime_cofactor_count']}`。",
        f"- 总素密度：`{projection['overall_prime_density']:.6f}`。",
        "",
        "## 3. 分层互补素数密度",
        "",
        "| beta层 | 区间数 | 整数容量 | 素互补数 | 素密度 | 非零区间 | 单区间最大素数数 | 单区间最大密度 | cofactor范围 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in projection["buckets"]:
        lines.append(
            f"| `{row['bucket']}` | {row['interval_count']} | {row['integer_capacity']} | "
            f"{row['prime_cofactor_count']} | {row['prime_density']:.6f} | "
            f"{row['nonzero_prime_intervals']} | {row['max_prime_count']} | "
            f"{row['max_density']:.6f} | `[{row['cofactor_left_min']},{row['cofactor_right_max']}]` |"
        )
    lines += [
        "",
        "## 4. 最高密度互补区间",
        "",
        "| p | anchor | beta层 | cofactor区间 | 容量 | 素数数 | 密度 |",
        "| ---: | ---: | --- | --- | ---: | ---: | ---: |",
    ]
    for row in projection["top_density_intervals"]:
        lines.append(
            f"| {row['p']} | {row['anchor']} | `{row['bucket']}` | "
            f"`[{row['co_left']},{row['co_right']}]` | {row['capacity']} | "
            f"{row['prime_count']} | {row['density']:.6f} |"
        )
    lines += [
        "",
        "## 5. 逐窗口压力账本",
        "",
        "下表只列最坏粗剩余素数比例窗口。`semirough` 是互补素数短区间给出的粗半素数数；`other` 是剩余多因子粗合数数。",
        "",
        "| p | q行 | J | rough | prime | prime/rough | semirough | semi/composite | other | cofactor容量 |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in projection["worst_prime_ratio_windows"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | `[{row['left']},{row['right']}]` | "
            f"{row['rough_count']} | {row['rough_prime_count']} | {row['rough_prime_ratio']:.6f} | "
            f"{row['prime_cofactor_count']} | {row['semiprime_to_composite']:.6f} | "
            f"{row['other_composite_count']} | {row['integer_capacity']} |"
        )
    lines += [
        "",
        "半素数压力最高窗口如下。它们显示主要压力来自粗半素数；剩余 `other` 多因子部分较小，但仍需单独账本吸收。",
        "",
        "| p | q行 | rough | prime | semirough | semi/composite | other |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in projection["highest_semiprime_pressure_windows"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | {row['rough_count']} | "
            f"{row['rough_prime_count']} | {row['prime_cofactor_count']} | "
            f"{row['semiprime_to_composite']:.6f} | {row['other_composite_count']} |"
        )
    lines += [
        "",
        "## 6. 新最小硬点",
        "",
        "锚层半素数上界等价于平均互补素数短区间上界：",
        "",
        "\\[",
        "\\sum_{a\\in A} S_a(J)",
        "\\le \\text{可吸收预算}(A,J).",
        "\\]",
        "",
        "若该式失败，则必有某个锚层或某族互补区间出现素数密度异常偏高。这正是可送入 `CRTDefect/Tail-anchor/OSPC` 的出口。",
        "",
        "因此下一步最小接口更新为：",
        "",
        "```text",
        "Average prime-cofactor interval bound",
        "or prime-cofactor density spike => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "更精确地，单个 ASB 窗口 `J` 的待证接口应写成",
        "",
        "\\[",
        "\\sum_{z<a\\le p} S_a(J)+M_{\\ge 3}(J)\\le (1-\\eta)|R_z(J)|,",
        "\\]",
        "",
        "其中 `M_{\\ge 3}(J)` 是至少三个粗因子的剩余粗合数预算。若该式失败，则必须出现互补素数短区间平均密度异常，或多因子粗合数能量异常。",
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
