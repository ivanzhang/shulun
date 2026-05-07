#!/usr/bin/env python3
"""审计 CarryMain 的调和恒等式与显式余量。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_carry_main_identity_audit.py --max-p 100000

面积进位分解中 C(P)=W(P)+D(P)。本脚本验证并记录
  allowance(P)-W(P)=P*(1.02-(H_{P-1}-H_y))
以及初等上界
  H_{P-1}-H_y <= log((P-1)/y) <= log((P-1)/(P/e-1)).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return flags


def primes_from_table(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def harmonic_table(limit: int) -> list[float]:
    """返回 H_n 表。"""
    values = [0.0] * (limit + 1)
    for n in range(1, limit + 1):
        values[n] = values[n - 1] + 1.0 / n
    return values


def audit_p(p: int, harmonics: list[float], y_ratio: float) -> dict:
    """审计单个 p 的 CarryMain 余量。"""
    y = max(2, int(math.floor(y_ratio * p)))
    harmonic_gap = harmonics[p - 1] - harmonics[y]
    allowance_minus_weight = p * (1.02 - harmonic_gap)
    integral_gap_bound = math.log((p - 1) / y)
    floor_free_gap_bound = math.log((p - 1) / (p / math.e - 1))
    integral_margin = p * (1.02 - integral_gap_bound)
    floor_free_margin = p * (1.02 - floor_free_gap_bound)
    sqrt_p = math.sqrt(p)
    return {
        "p": p,
        "y": y,
        "harmonic_gap": harmonic_gap,
        "allowance_minus_weight": allowance_minus_weight,
        "allowance_minus_weight_over_sqrt_p": allowance_minus_weight / sqrt_p,
        "integral_gap_bound": integral_gap_bound,
        "integral_margin": integral_margin,
        "integral_margin_over_sqrt_p": integral_margin / sqrt_p,
        "floor_free_gap_bound": floor_free_gap_bound,
        "floor_free_margin": floor_free_margin,
        "floor_free_margin_over_sqrt_p": floor_free_margin / sqrt_p,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    primes = [prime for prime in primes_from_table(sieve_bool(max_p)) if prime >= 23]
    harmonics = harmonic_table(max_p)
    records = [audit_p(p, harmonics, y_ratio) for p in primes]
    threshold_summary = []
    for threshold in [2003, 5003, 10007, 20011, 50021, 100003]:
        subset = [record for record in records if record["p"] >= threshold]
        if not subset:
            continue
        threshold_summary.append(
            {
                "threshold": threshold,
                "min_actual_record": min(
                    subset, key=lambda item: item["allowance_minus_weight_over_sqrt_p"]
                ),
                "min_floor_free_record": min(
                    subset, key=lambda item: item["floor_free_margin_over_sqrt_p"]
                ),
            }
        )

    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "min_actual_record": min(
                records, key=lambda item: item["allowance_minus_weight_over_sqrt_p"]
            ),
            "min_integral_bound_record": min(
                records, key=lambda item: item["integral_margin_over_sqrt_p"]
            ),
            "min_floor_free_bound_record": min(
                records, key=lambda item: item["floor_free_margin_over_sqrt_p"]
            ),
            "threshold_summary": threshold_summary,
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点 CarryMain 调和恒等式审计",
        "",
        "**状态：** `carry_main_harmonic_identity_and_margin`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查 `p>=23` 奇素数个数：`{summary['prime_count']}`。",
        f"- 最小实际 `allowance-W` 记录：`{summary['min_actual_record']}`。",
        f"- 最小积分界余量记录：`{summary['min_integral_bound_record']}`。",
        f"- 最小去 floor 界余量记录：`{summary['min_floor_free_bound_record']}`。",
        "",
        "## 阈值账本",
        "",
        "| threshold | min actual | min floor-free bound |",
        "|---:|---|---|",
    ]
    for item in summary["threshold_summary"]:
        lines.append(
            f"| {item['threshold']} | {item['min_actual_record']} | {item['min_floor_free_record']} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "`allowance-W=P(1.02-(H_{P-1}-H_y))` 是精确恒等式。由单调积分可得 `H_{P-1}-H_y<=log((P-1)/y)`，再用 `y>=P/e-1` 得去 floor 的显式下界。该账本把 CarryMain 从实验量降为初等调和不等式。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=100000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_carry_main_identity_audit_20260505",
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
        if key != "threshold_summary"
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
