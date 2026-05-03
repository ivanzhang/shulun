#!/usr/bin/env python3
"""ASB/RPD 硬窗口中的粗半素数锚层投影。

用法示例：
  python3 experiments/prime_matrix_semiprime_anchor_projection.py
  python3 experiments/prime_matrix_semiprime_anchor_projection.py --max-p 2000 --alpha 0.43
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-semiprime-anchor-projection.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-semiprime-anchor-projection.md"


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


def primes_from_flags(flags: bytearray) -> list[int]:
    """从素数标记表抽取素数。"""
    return [i for i in range(2, len(flags)) if flags[i]]


def factorization(n: int, spf: list[int]) -> list[int]:
    """返回带重数素因子分解。"""
    factors: list[int] = []
    while n > 1:
        p = spf[n]
        factors.append(p)
        n //= p
    return factors


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


def analyze_semiprime_anchors(
    hard_windows: list[dict[str, Any]],
    alpha: float,
    spf: list[int],
) -> dict[str, Any]:
    """分析半素数锚层。"""
    buckets: dict[str, dict[str, Any]] = {}
    anchor_hits: dict[str, int] = {}
    total_semiprimes = 0
    total_anchor_capacity = 0
    for window in hard_windows:
        p = window["p"]
        left = window["left"]
        right = window["right"]
        z = window["z"]
        for n in range(left, right + 1):
            if spf[n] <= z:
                continue
            factors = factorization(n, spf)
            if len(factors) != 2:
                continue
            anchor = min(factors)
            cofactor = max(factors)
            if anchor <= z or anchor > p:
                continue
            total_semiprimes += 1
            capacity = right // anchor - (left - 1) // anchor
            total_anchor_capacity += capacity
            bucket = beta_bucket(anchor, p, alpha)
            entry = buckets.setdefault(
                bucket,
                {
                    "semiprime_count": 0,
                    "anchor_capacity_sum": 0,
                    "distinct_anchors": set(),
                    "cofactor_gt_p": 0,
                    "cofactor_le_p": 0,
                },
            )
            entry["semiprime_count"] += 1
            entry["anchor_capacity_sum"] += capacity
            entry["distinct_anchors"].add(anchor)
            if cofactor > p:
                entry["cofactor_gt_p"] += 1
            else:
                entry["cofactor_le_p"] += 1
            key = f"{p}:{anchor}"
            anchor_hits[key] = anchor_hits.get(key, 0) + 1

    rendered_buckets = []
    for name, entry in sorted(buckets.items()):
        count = entry["semiprime_count"]
        rendered_buckets.append(
            {
                "bucket": name,
                "semiprime_count": count,
                "share": None if total_semiprimes == 0 else count / total_semiprimes,
                "anchor_capacity_sum": entry["anchor_capacity_sum"],
                "capacity_efficiency": None
                if entry["anchor_capacity_sum"] == 0
                else count / entry["anchor_capacity_sum"],
                "distinct_anchors": len(entry["distinct_anchors"]),
                "cofactor_gt_p": entry["cofactor_gt_p"],
                "cofactor_le_p": entry["cofactor_le_p"],
            }
        )
    top_anchor_hits = sorted(anchor_hits.items(), key=lambda item: item[1], reverse=True)[:12]
    return {
        "total_semiprimes": total_semiprimes,
        "total_anchor_capacity": total_anchor_capacity,
        "overall_capacity_efficiency": None
        if total_anchor_capacity == 0
        else total_semiprimes / total_anchor_capacity,
        "buckets": rendered_buckets,
        "top_anchor_hits": [{"p_anchor": key, "hits": hits} for key, hits in top_anchor_hits],
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成半素数锚层投影审计。"""
    max_q_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(max_q_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    projection = analyze_semiprime_anchors(hard_windows, alpha, spf)
    return {
        "certificate_type": "prime_matrix_semiprime_anchor_projection",
        "status": "semiprime_pressure_reduced_to_anchor_layers",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "hard_windows": hard_windows,
        "projection": projection,
        "review_conclusion": (
            "粗半素数压力可按最小素因子锚层分解。若某一锚层贡献过大，"
            "就得到双线性短区间投影或 Tail-anchor/CRTDefect 出口；"
            "若所有锚层正常，则半素数投影应由分层容量账本吸收。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    projection = audit["projection"]
    lines = [
        "# 粗半素数锚层投影审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告继续压缩半素数投影硬点。对粗半素数 `n=ab`，取最小因子 `a` 为锚。窗口内所有半素数都来自锚线 `a|n` 与短区间内的互补因子 `b`。因此半素数过密可以分解为锚层过密。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 总体锚容量",
        "",
        f"- 半素数总数：`{projection['total_semiprimes']}`。",
        f"- 锚线容量总和：`{projection['total_anchor_capacity']}`。",
        f"- 容量效率：`{projection['overall_capacity_efficiency']:.6f}`。",
        "",
        "## 3. 锚层分布",
        "",
        "| beta层 | 半素数数 | 占比 | 锚容量 | 容量效率 | 不同锚数 | cofactor>p | cofactor<=p |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in projection["buckets"]:
        lines.append(
            f"| `{row['bucket']}` | {row['semiprime_count']} | {row['share']:.6f} | "
            f"{row['anchor_capacity_sum']} | {row['capacity_efficiency']:.6f} | "
            f"{row['distinct_anchors']} | {row['cofactor_gt_p']} | {row['cofactor_le_p']} |"
        )
    lines += [
        "",
        "## 4. 最高复用锚",
        "",
        "| p:anchor | hits |",
        "| --- | ---: |",
    ]
    for row in projection["top_anchor_hits"]:
        lines.append(f"| `{row['p_anchor']}` | {row['hits']} |")
    lines += [
        "",
        "## 5. 证明接口",
        "",
        "令 `S_{a}(J)` 为锚 `a` 在窗口 `J` 中产生的粗半素数数。半素数投影可写成",
        "",
        "\\[",
        "\\sum_{a\\in(z,p]} S_a(J).",
        "\\]",
        "",
        "若该和过大，则至少出现一个锚层 `A` 满足",
        "",
        "\\[",
        "\\sum_{a\\in A} S_a(J)",
        "\\gg \\sum_{a\\in A}\\left(\\left\\lfloor{R\\over a}\\right\\rfloor-\\left\\lfloor{L-1\\over a}\\right\\rfloor\\right)",
        "\\]",
        "",
        "或多个锚层同时接近容量上限。前者是 Tail-anchor/CRTDefect 出口，后者是分层双线性短区间上界问题。",
        "",
        "因此下一步最小硬点是：",
        "",
        "```text",
        "Anchor-layer semiprime bound",
        "or anchor-layer over-efficiency => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "## 6. 审稿结论",
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
