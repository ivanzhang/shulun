#!/usr/bin/env python3
"""M_{>=3} 第二锚预算审计。

用法示例：
  python3 experiments/prime_matrix_mge3_second_anchor_audit.py
  python3 experiments/prime_matrix_mge3_second_anchor_audit.py --max-p 2000 --alpha 0.43
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

DEFAULT_JSON = MONOGRAPH / "prime-matrix-mge3-second-anchor-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-mge3-second-anchor-audit.md"


def beta_bucket(value: int, p: int, alpha: float) -> str:
    """按 value≈p^beta 分桶。"""
    beta = math.log(value) / math.log(p)
    edges = [alpha, 0.50, 0.60, 2.0 / 3.0, 0.80, 0.90, 1.01]
    labels = ["[α,0.50)", "[0.50,0.60)", "[0.60,2/3)", "[2/3,0.80)", "[0.80,0.90)", "[0.90,1.01)"]
    for label, lo, hi in zip(labels, edges, edges[1:]):
        if lo <= beta < hi:
            return label
    return "outside"


def rough_tail_count(
    left: int,
    right: int,
    lower_prime: int,
    prime_flags: bytearray,
    spf: list[int],
) -> tuple[int, int, int]:
    """统计区间中 P^-(d)>=lower_prime 的尾因子数。"""
    rough_count = 0
    prime_count = 0
    composite_count = 0
    for value in range(left, right + 1):
        if spf[value] < lower_prime:
            continue
        rough_count += 1
        if prime_flags[value]:
            prime_count += 1
        else:
            composite_count += 1
    return rough_count, prime_count, composite_count


def add_bucket(
    table: dict[str, dict[str, Any]],
    name: str,
    capacity: int,
    rough_tail: int,
    prime_tail: int,
    composite_tail: int,
) -> None:
    """累加分桶账本。"""
    row = table.setdefault(
        name,
        {
            "pair_interval_count": 0,
            "integer_capacity": 0,
            "rough_tail_count": 0,
            "prime_tail_count": 0,
            "composite_tail_count": 0,
        },
    )
    row["pair_interval_count"] += 1
    row["integer_capacity"] += capacity
    row["rough_tail_count"] += rough_tail
    row["prime_tail_count"] += prime_tail
    row["composite_tail_count"] += composite_tail


def finalize_buckets(table: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """渲染分桶账本。"""
    rows = []
    for name, row in sorted(table.items()):
        capacity = row["integer_capacity"]
        rough_tail = row["rough_tail_count"]
        rows.append(
            {
                "bucket": name,
                "pair_interval_count": row["pair_interval_count"],
                "integer_capacity": capacity,
                "rough_tail_count": rough_tail,
                "prime_tail_count": row["prime_tail_count"],
                "composite_tail_count": row["composite_tail_count"],
                "rough_tail_density": None if capacity == 0 else rough_tail / capacity,
                "prime_tail_share": None if rough_tail == 0 else row["prime_tail_count"] / rough_tail,
            }
        )
    return rows


def audit_second_anchor(
    hard_windows: list[dict[str, Any]],
    primes: list[int],
    prime_flags: bytearray,
    spf: list[int],
    alpha: float,
) -> dict[str, Any]:
    """把 M_{>=3} 分解为第一锚、第二锚和粗尾因子。"""
    first_anchor_buckets: dict[str, dict[str, Any]] = {}
    second_anchor_buckets: dict[str, dict[str, Any]] = {}
    pair_buckets: dict[str, dict[str, Any]] = {}
    per_window: dict[tuple[int, int, int], dict[str, Any]] = {}
    total_capacity = 0
    total_rough_tail = 0
    total_prime_tail = 0
    total_composite_tail = 0
    max_second_beta = 0.0

    for window in hard_windows:
        key = (window["p"], window["left"], window["right"])
        per_window[key] = {
            "p": window["p"],
            "q": window["q"],
            "q_row": window["q_row"],
            "left": window["left"],
            "right": window["right"],
            "rough_count": window["rough_count"],
            "prime_count": window["prime_count"],
            "semiprime_count": window["semiprime_count"],
            "mge3_count": window["mge3_count"],
            "second_anchor_capacity": 0,
            "second_anchor_rough_tail": 0,
            "second_anchor_prime_tail": 0,
            "second_anchor_composite_tail": 0,
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
                rough_tail, prime_tail, composite_tail = rough_tail_count(
                    tail_left, tail_right, second_anchor, prime_flags, spf
                )
                first_bucket = beta_bucket(first_anchor, p, alpha)
                second_bucket = beta_bucket(second_anchor, p, alpha)
                pair_bucket = f"{first_bucket} × {second_bucket}"
                add_bucket(first_anchor_buckets, first_bucket, capacity, rough_tail, prime_tail, composite_tail)
                add_bucket(second_anchor_buckets, second_bucket, capacity, rough_tail, prime_tail, composite_tail)
                add_bucket(pair_buckets, pair_bucket, capacity, rough_tail, prime_tail, composite_tail)
                total_capacity += capacity
                total_rough_tail += rough_tail
                total_prime_tail += prime_tail
                total_composite_tail += composite_tail
                second_beta = math.log(second_anchor) / math.log(p)
                max_second_beta = max(max_second_beta, second_beta)
                summary = per_window[window_key]
                summary["second_anchor_capacity"] += capacity
                summary["second_anchor_rough_tail"] += rough_tail
                summary["second_anchor_prime_tail"] += prime_tail
                summary["second_anchor_composite_tail"] += composite_tail

    classified_mge3_total = sum(window["mge3_count"] for window in hard_windows)
    for summary in per_window.values():
        capacity = summary["second_anchor_capacity"]
        rough_tail = summary["second_anchor_rough_tail"]
        summary["capacity_efficiency"] = None if capacity == 0 else rough_tail / capacity
        summary["prime_tail_share"] = None if rough_tail == 0 else summary["second_anchor_prime_tail"] / rough_tail

    return {
        "classified_mge3_total": classified_mge3_total,
        "second_anchor_identity_total": total_rough_tail,
        "identity_gap": total_rough_tail - classified_mge3_total,
        "integer_capacity_total": total_capacity,
        "capacity_efficiency": None if total_capacity == 0 else total_rough_tail / total_capacity,
        "tail_prime_total": total_prime_tail,
        "tail_composite_total": total_composite_tail,
        "tail_prime_share": None if total_rough_tail == 0 else total_prime_tail / total_rough_tail,
        "max_second_beta": max_second_beta,
        "first_anchor_buckets": finalize_buckets(first_anchor_buckets),
        "second_anchor_buckets": finalize_buckets(second_anchor_buckets),
        "pair_buckets": finalize_buckets(pair_buckets),
        "worst_windows": sorted(
            per_window.values(),
            key=lambda row: (row["capacity_efficiency"], row["second_anchor_rough_tail"]),
            reverse=True,
        )[:12],
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成第二锚预算审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    second_anchor = audit_second_anchor(hard_windows, primes, prime_flags, spf, alpha)
    aggregate = {
        "rough_count": sum(row["rough_count"] for row in hard_windows),
        "prime_count": sum(row["prime_count"] for row in hard_windows),
        "semiprime_count": sum(row["semiprime_count"] for row in hard_windows),
        "mge3_count": sum(row["mge3_count"] for row in hard_windows),
    }
    return {
        "certificate_type": "prime_matrix_mge3_second_anchor_audit",
        "status": "mge3_reduced_to_second_anchor_rough_tail_bound",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "hard_aggregate": aggregate,
        "second_anchor": second_anchor,
        "review_conclusion": (
            "M_{>=3} 可精确写成第一锚、第二锚和第二锚粗尾因子的三层和。"
            "这把低锚复合互补因子上界进一步压成 b-rough 短尾计数；"
            "若该计数超出二阶容量账本，就必须出现第二锚相位或粗尾密度异常。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    aggregate = audit["hard_aggregate"]
    second_anchor = audit["second_anchor"]
    lines = [
        "# M_{>=3} 第二锚预算审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告继续压缩低锚复合互补因子项。设 `n=a b d`，其中 `a=P^-(n)`，`b` 为第二个素因子，则 `P^-(d)>=b`。于是",
        "",
        "\\[",
        "M_{\\ge3}(J)=\\sum_{z<a\\le b}\\#\\{d:\\lceil L/(ab)\\rceil\\le d\\le\\lfloor R/(ab)\\rfloor,\\ P^-(d)\\ge b\\}.",
        "\\]",
        "",
        "该式按带重数素因子排序给出精确分解。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 2. 总体账本",
        "",
        f"- 低筛粗剩余：`{aggregate['rough_count']}`。",
        f"- 粗剩余素数：`{aggregate['prime_count']}`。",
        f"- 粗半素数：`{aggregate['semiprime_count']}`。",
        f"- `M_{{>=3}}`：`{aggregate['mge3_count']}`。",
        f"- 第二锚恒等式计数：`{second_anchor['second_anchor_identity_total']}`。",
        f"- 第二锚恒等式校验差：`{second_anchor['identity_gap']}`。",
        f"- 第二锚整数容量：`{second_anchor['integer_capacity_total']}`。",
        f"- 第二锚容量效率：`{second_anchor['capacity_efficiency']:.6f}`。",
        f"- 尾因子为素数比例：`{second_anchor['tail_prime_share']:.6f}`。",
        f"- 最大第二锚 beta：`{second_anchor['max_second_beta']:.6f}`。",
        "",
        "## 3. 第一锚分层",
        "",
        "| 第一锚层 | pair区间数 | 整数容量 | b-rough尾数 | 容量效率 | 尾素数占比 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in second_anchor["first_anchor_buckets"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['integer_capacity']} | "
            f"{row['rough_tail_count']} | {row['rough_tail_density']:.6f} | {row['prime_tail_share']:.6f} |"
        )
    lines += [
        "",
        "## 4. 第二锚分层",
        "",
        "| 第二锚层 | pair区间数 | 整数容量 | b-rough尾数 | 容量效率 | 尾素数占比 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in second_anchor["second_anchor_buckets"]:
        lines.append(
            f"| `{row['bucket']}` | {row['pair_interval_count']} | {row['integer_capacity']} | "
            f"{row['rough_tail_count']} | {row['rough_tail_density']:.6f} | {row['prime_tail_share']:.6f} |"
        )
    lines += [
        "",
        "## 5. 最高效率窗口",
        "",
        "| p | q行 | J | M>=3 | 二锚容量 | 二锚计数 | 容量效率 | 尾素数占比 |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in second_anchor["worst_windows"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | `[{row['left']},{row['right']}]` | "
            f"{row['mge3_count']} | {row['second_anchor_capacity']} | "
            f"{row['second_anchor_rough_tail']} | {row['capacity_efficiency']:.6f} | "
            f"{row['prime_tail_share']:.6f} |"
        )
    lines += [
        "",
        "## 6. 新最小硬点",
        "",
        "低锚复合互补因子上界进一步等价为第二锚粗尾短区间上界：",
        "",
        "```text",
        "Second-anchor b-rough tail bound",
        "or second-anchor/tail density spike => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "因此 ASB/RPD 当前最小接口可写为：",
        "",
        "```text",
        "prime-cofactor interval bound",
        "+ second-anchor b-rough tail bound",
        "or corresponding density spikes => CRTDefect/Tail-anchor/OSPC.",
        "```",
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
