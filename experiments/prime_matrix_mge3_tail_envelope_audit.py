#!/usr/bin/env python3
"""M_{>=3} 第二锚粗尾包络审计。

用法示例：
  python3 experiments/prime_matrix_mge3_tail_envelope_audit.py
  python3 experiments/prime_matrix_mge3_tail_envelope_audit.py --max-p 2000 --alpha 0.43
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

DEFAULT_JSON = MONOGRAPH / "prime-matrix-mge3-tail-envelope-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-mge3-tail-envelope-audit.md"


def beta_bucket(value: int, p: int, alpha: float) -> str:
    """按 value≈p^beta 分桶。"""
    beta = math.log(value) / math.log(p)
    edges = [alpha, 0.50, 0.60, 2.0 / 3.0, 0.80, 0.90, 1.01]
    labels = ["[α,0.50)", "[0.50,0.60)", "[0.60,2/3)", "[2/3,0.80)", "[0.80,0.90)", "[0.90,1.01)"]
    for label, lo, hi in zip(labels, edges, edges[1:]):
        if lo <= beta < hi:
            return label
    return "outside"


def length_bucket(capacity: int) -> str:
    """按尾区间整数容量分桶。"""
    if capacity <= 1:
        return "1"
    if capacity == 2:
        return "2"
    if capacity <= 5:
        return "3-5"
    if capacity <= 10:
        return "6-10"
    return ">10"


def mertens_products(primes: list[int], limit: int) -> list[float]:
    """构造 V(y)=prod_{ell<y}(1-1/ell) 的前缀表。"""
    values = [1.0] * (limit + 1)
    product = 1.0
    prime_index = 0
    for value in range(limit + 1):
        while prime_index < len(primes) and primes[prime_index] < value:
            ell = primes[prime_index]
            product *= 1.0 - 1.0 / ell
            prime_index += 1
        values[value] = product
    return values


def rough_tail_count(left: int, right: int, lower_prime: int, prime_flags: bytearray, spf: list[int]) -> tuple[int, int]:
    """统计 P^-(d)>=lower_prime 的尾因子数和其中素数数。"""
    rough_count = 0
    prime_count = 0
    for value in range(left, right + 1):
        if spf[value] < lower_prime:
            continue
        rough_count += 1
        if prime_flags[value]:
            prime_count += 1
    return rough_count, prime_count


def new_bucket_row() -> dict[str, Any]:
    """创建包络分桶行。"""
    return {
        "pair_interval_count": 0,
        "integer_capacity": 0,
        "rough_tail_count": 0,
        "prime_tail_count": 0,
        "mertens_envelope": 0.0,
    }


def add_row(row: dict[str, Any], capacity: int, rough_tail: int, prime_tail: int, envelope: float) -> None:
    """累加包络账本。"""
    row["pair_interval_count"] += 1
    row["integer_capacity"] += capacity
    row["rough_tail_count"] += rough_tail
    row["prime_tail_count"] += prime_tail
    row["mertens_envelope"] += envelope


def finalize_table(table: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """渲染包络分桶表。"""
    rows = []
    for name, row in sorted(table.items()):
        envelope = row["mertens_envelope"]
        rough_tail = row["rough_tail_count"]
        rows.append(
            {
                "bucket": name,
                "pair_interval_count": row["pair_interval_count"],
                "integer_capacity": row["integer_capacity"],
                "rough_tail_count": rough_tail,
                "prime_tail_count": row["prime_tail_count"],
                "mertens_envelope": envelope,
                "needed_constant": None if envelope == 0 else rough_tail / envelope,
                "actual_density": None if row["integer_capacity"] == 0 else rough_tail / row["integer_capacity"],
                "prime_tail_share": None if rough_tail == 0 else row["prime_tail_count"] / rough_tail,
            }
        )
    return rows


def audit_tail_envelope(
    hard_windows: list[dict[str, Any]],
    primes: list[int],
    prime_flags: bytearray,
    spf: list[int],
    alpha: float,
) -> dict[str, Any]:
    """审计第二锚粗尾的 Mertens/Brun 包络。"""
    max_prime = max(primes)
    mertens = mertens_products(primes, max_prime)
    by_second_beta: dict[str, dict[str, Any]] = {}
    by_tail_length: dict[str, dict[str, Any]] = {}
    by_window: dict[tuple[int, int, int], dict[str, Any]] = {}
    total_capacity = 0
    total_rough_tail = 0
    total_prime_tail = 0
    total_envelope = 0.0
    pair_rows = []

    for window in hard_windows:
        window_key = (window["p"], window["left"], window["right"])
        by_window[window_key] = {
            "p": window["p"],
            "q": window["q"],
            "q_row": window["q_row"],
            "left": window["left"],
            "right": window["right"],
            "mge3_count": window["mge3_count"],
            "pair_interval_count": 0,
            "integer_capacity": 0,
            "rough_tail_count": 0,
            "prime_tail_count": 0,
            "mertens_envelope": 0.0,
        }

    for window in hard_windows:
        p = window["p"]
        z = window["z"]
        left = window["left"]
        right = window["right"]
        window_key = (p, left, right)
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
                rough_tail, prime_tail = rough_tail_count(tail_left, tail_right, second_anchor, prime_flags, spf)
                envelope = capacity * mertens[second_anchor]
                second_bucket = beta_bucket(second_anchor, p, alpha)
                tail_bucket = length_bucket(capacity)
                add_row(
                    by_second_beta.setdefault(second_bucket, new_bucket_row()),
                    capacity,
                    rough_tail,
                    prime_tail,
                    envelope,
                )
                add_row(
                    by_tail_length.setdefault(tail_bucket, new_bucket_row()),
                    capacity,
                    rough_tail,
                    prime_tail,
                    envelope,
                )
                window_row = by_window[window_key]
                add_row(window_row, capacity, rough_tail, prime_tail, envelope)
                total_capacity += capacity
                total_rough_tail += rough_tail
                total_prime_tail += prime_tail
                total_envelope += envelope
                pair_rows.append(
                    {
                        "p": p,
                        "first_anchor": first_anchor,
                        "second_anchor": second_anchor,
                        "tail_left": tail_left,
                        "tail_right": tail_right,
                        "capacity": capacity,
                        "rough_tail": rough_tail,
                        "prime_tail": prime_tail,
                        "mertens_envelope": envelope,
                        "needed_constant": None if envelope == 0 else rough_tail / envelope,
                    }
                )

    for row in by_window.values():
        envelope = row["mertens_envelope"]
        rough_tail = row["rough_tail_count"]
        row["needed_constant"] = None if envelope == 0 else rough_tail / envelope
        row["actual_density"] = None if row["integer_capacity"] == 0 else rough_tail / row["integer_capacity"]
        row["prime_tail_share"] = None if rough_tail == 0 else row["prime_tail_count"] / rough_tail

    top_pair_spikes = sorted(
        [row for row in pair_rows if row["mertens_envelope"] > 0],
        key=lambda row: (row["needed_constant"], row["rough_tail"]),
        reverse=True,
    )[:12]
    top_window_spikes = sorted(
        [row for row in by_window.values() if row["mertens_envelope"] > 0],
        key=lambda row: (row["needed_constant"], row["rough_tail_count"]),
        reverse=True,
    )[:12]
    return {
        "integer_capacity_total": total_capacity,
        "rough_tail_total": total_rough_tail,
        "prime_tail_total": total_prime_tail,
        "mertens_envelope_total": total_envelope,
        "global_needed_constant": None if total_envelope == 0 else total_rough_tail / total_envelope,
        "global_actual_density": None if total_capacity == 0 else total_rough_tail / total_capacity,
        "global_prime_tail_share": None if total_rough_tail == 0 else total_prime_tail / total_rough_tail,
        "by_second_beta": finalize_table(by_second_beta),
        "by_tail_length": finalize_table(by_tail_length),
        "top_pair_spikes": top_pair_spikes,
        "top_window_spikes": top_window_spikes,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成第二锚粗尾包络审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    envelope = audit_tail_envelope(hard_windows, primes, prime_flags, spf, alpha)
    return {
        "certificate_type": "prime_matrix_mge3_tail_envelope_audit",
        "status": "second_anchor_tail_reduced_to_mertens_envelope_or_spike",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "tail_envelope": envelope,
        "review_conclusion": (
            "第二锚粗尾项可用 Mertens/Brun 粗尾密度形成可计算包络。"
            "样本显示全局只需常数级放大即可覆盖实际 M_{>=3}，"
            "但单个极短尾区间会出现高尖峰；证明应采用聚合包络，并把尖峰列为 CRTDefect/Tail-anchor 出口。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    envelope = audit["tail_envelope"]

    def fmt(value: float | None) -> str:
        """格式化可空浮点数。"""
        return "NA" if value is None else f"{value:.6f}"

    lines = [
        "# M_{>=3} 第二锚粗尾包络审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告把第二锚粗尾计数与 Mertens/Brun 粗尾密度包络比较。对第二锚 `b`，理论密度基准为",
        "",
        "\\[",
        "V(b)=\\prod_{\\ell<b}\\left(1-{1\\over \\ell}\\right).",
        "\\]",
        "",
        "对应包络为 `tail_capacity * V(b)`。若实际粗尾显著超过该包络，则标记为局部密度尖峰出口。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 全局包络",
        "",
        f"- 整数容量：`{envelope['integer_capacity_total']}`。",
        f"- 实际 b-rough 尾数：`{envelope['rough_tail_total']}`。",
        f"- 尾因子为素数数：`{envelope['prime_tail_total']}`。",
        f"- Mertens 包络：`{envelope['mertens_envelope_total']:.6f}`。",
        f"- 所需全局放大常数：`{envelope['global_needed_constant']:.6f}`。",
        f"- 实际密度：`{envelope['global_actual_density']:.6f}`。",
        f"- 尾素数占比：`{envelope['global_prime_tail_share']:.6f}`。",
        "",
        "## 3. 第二锚层包络",
        "",
        "| 第二锚层 | pair区间数 | 容量 | 实际粗尾 | Mertens包络 | 所需常数 | 实际密度 | 尾素数占比 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in envelope["by_second_beta"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['integer_capacity']} | "
            f"{row['rough_tail_count']} | {row['mertens_envelope']:.6f} | "
            f"{fmt(row['needed_constant'])} | {fmt(row['actual_density'])} | {fmt(row['prime_tail_share'])} |"
        )
    lines += [
        "",
        "## 4. 尾区间长度包络",
        "",
        "| 容量层 | pair区间数 | 容量 | 实际粗尾 | Mertens包络 | 所需常数 | 实际密度 | 尾素数占比 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in envelope["by_tail_length"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['integer_capacity']} | "
            f"{row['rough_tail_count']} | {row['mertens_envelope']:.6f} | "
            f"{fmt(row['needed_constant'])} | {fmt(row['actual_density'])} | {fmt(row['prime_tail_share'])} |"
        )
    lines += [
        "",
        "## 5. 最高窗口尖峰",
        "",
        "| p | q行 | J | M>=3 | 容量 | 实际粗尾 | Mertens包络 | 所需常数 | 实际密度 |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in envelope["top_window_spikes"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | `[{row['left']},{row['right']}]` | "
            f"{row['mge3_count']} | {row['integer_capacity']} | {row['rough_tail_count']} | "
            f"{row['mertens_envelope']:.6f} | {row['needed_constant']:.6f} | {row['actual_density']:.6f} |"
        )
    lines += [
        "",
        "## 6. 新最小硬点",
        "",
        "第二锚粗尾上界可写成聚合 Mertens 包络与尖峰出口二分：",
        "",
        "```text",
        "Aggregated second-anchor Mertens envelope",
        "or localized tail-density spike => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "这比裸第二锚容量更强：裸容量效率为 `rough_tail/capacity`，包络效率改为 `rough_tail/sum capacity*V(b)`，把证明义务集中到粗尾筛密度是否正常。",
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
