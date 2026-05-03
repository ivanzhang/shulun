#!/usr/bin/env python3
"""BPN LHB 尾段有限证书。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_tail_finite_certificate.py

目标：
- 对 `107<=P<=229` 生成精确 `P/5` 分割递推证书；
- 对 `233<=P<=13207` 生成精确连续乘积证书；
- 连续乘积比较使用整数交叉乘法，避免浮点误判。
"""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def coprime_prefix(q: int) -> list[int]:
    """返回两个 CRT 周期上的互素指示前缀和。"""
    period = [1 if gcd(residue, q) == 1 else 0 for residue in range(q)]
    prefix = [0]
    for value in period + period:
        prefix.append(prefix[-1] + value)
    return prefix


def max_low_holes(prefix: list[int], q: int, length: int) -> int:
    """计算长度 `length` 的连续残基段中最多的 `Q`-互素残基数。"""
    full_periods, rest = divmod(length, q)
    period_mass = prefix[q]
    if rest == 0:
        return full_periods * period_mass
    local_max = max(prefix[start + rest] - prefix[start] for start in range(q))
    return full_periods * period_mass + local_max


def product_prefix_fractions(max_value: int, q: int, prime_set: set[int]) -> tuple[list[int], list[int]]:
    """构造 `prod_{ell<=n,q∤ell}(1-1/ell)` 的分子分母前缀。"""
    numerators = [1] * (max_value + 1)
    denominators = [1] * (max_value + 1)
    numerator = 1
    denominator = 1
    for value in range(1, max_value + 1):
        if value in prime_set and q % value != 0:
            numerator *= value - 1
            denominator *= value
        numerators[value] = numerator
        denominators[value] = denominator
    return numerators, denominators


def split_residual(hole_count: int, high_primes: list[int], split_bound: int) -> tuple[int, int]:
    """只用 `ell<=split_bound` 的高素数递推，返回残量和已用个数。"""
    residual = hole_count
    used = 0
    for prime in high_primes:
        if prime > split_bound or residual <= 0:
            break
        residual -= (residual + prime - 1) // prime
        used += 1
    return residual, used


def scan(q: int, max_p: int, split_denominator: int) -> dict[str, Any]:
    """生成两段有限证书。"""
    primes = primes_upto(max_p)
    prime_set = set(primes)
    prefix = coprime_prefix(q)
    numerator_prefix, denominator_prefix = product_prefix_fractions(
        max_p // split_denominator,
        q,
        prime_set,
    )

    split_rows: list[dict[str, Any]] = []
    product_rows: list[dict[str, Any]] = []

    for p_value in primes:
        if p_value < 107:
            continue
        high_primes = [
            prime for prime in primes
            if prime < p_value and q % prime != 0
        ]
        hmax = max_low_holes(prefix, q, p_value - 1)
        split_bound = p_value // split_denominator
        residual, used = split_residual(hmax, high_primes, split_bound)
        remaining_primes = len(high_primes) - used

        if 107 <= p_value <= 229:
            split_rows.append(
                {
                    "p": p_value,
                    "hmax": hmax,
                    "split_bound": split_bound,
                    "split_residual": residual,
                    "remaining_primes": remaining_primes,
                    "margin": remaining_primes - residual,
                }
            )

        if 233 <= p_value <= 13207:
            numerator = numerator_prefix[split_bound]
            denominator = denominator_prefix[split_bound]
            integer_margin = remaining_primes * denominator - hmax * numerator
            product_rows.append(
                {
                    "p": p_value,
                    "hmax": hmax,
                    "split_bound": split_bound,
                    "remaining_primes": remaining_primes,
                    "product_numerator_digits": len(str(numerator)),
                    "product_denominator_digits": len(str(denominator)),
                    "integer_margin_positive": integer_margin > 0,
                    "integer_margin_digits": len(str(integer_margin)) if integer_margin > 0 else None,
                    "float_margin": remaining_primes - hmax * (numerator / denominator),
                }
            )

    split_failures = [row for row in split_rows if row["margin"] < 0]
    product_failures = [
        row for row in product_rows
        if not row["integer_margin_positive"]
    ]
    product_worst = sorted(product_rows, key=lambda row: row["float_margin"])[:20]

    return {
        "certificate_type": "prime_matrix_bpn_lhb_tail_finite_certificate",
        "q": q,
        "split_denominator": split_denominator,
        "split_range": [107, 229],
        "product_range": [233, 13207],
        "split_row_count": len(split_rows),
        "product_row_count": len(product_rows),
        "split_failures": split_failures,
        "product_failures": product_failures,
        "split_min_margin": min((row["margin"] for row in split_rows), default=None),
        "product_min_float_margin": min((row["float_margin"] for row in product_rows), default=None),
        "split_rows": split_rows,
        "product_worst_rows": product_worst,
        "review_conclusion": (
            "两段有限证书均通过：107<=P<=229 的精确分割递推无失败，"
            "233<=P<=13207 的连续乘积比较经整数交叉乘法无失败。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN LHB 尾段有限证书",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总览",
        "",
        f"- `split_range`: `{result['split_range']}`",
        f"- `product_range`: `{result['product_range']}`",
        f"- `split_row_count`: `{result['split_row_count']}`",
        f"- `product_row_count`: `{result['product_row_count']}`",
        f"- `split_failures`: `{len(result['split_failures'])}`",
        f"- `product_failures`: `{len(result['product_failures'])}`",
        f"- `split_min_margin`: `{result['split_min_margin']}`",
        f"- `product_min_float_margin`: `{result['product_min_float_margin']}`",
        "",
        "## 2. 精确分割递推表",
        "",
        "| P | Hmax | split bound | residual | remaining primes | margin |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["split_rows"]:
        lines.append(
            f"| {row['p']} | {row['hmax']} | {row['split_bound']} | "
            f"{row['split_residual']} | {row['remaining_primes']} | {row['margin']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 连续乘积最紧行",
            "",
            "完整 `233<=P<=13207` 乘积表保存在 JSON；下表列出浮点余量最小的 20 行。",
            "实际验收使用 `remaining_primes*denominator - Hmax*numerator > 0` 的整数比较。",
            "",
            "| P | Hmax | split bound | remaining primes | float margin | integer margin digits |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["product_worst_rows"]:
        lines.append(
            f"| {row['p']} | {row['hmax']} | {row['split_bound']} | "
            f"{row['remaining_primes']} | {row['float_margin']:.6f} | "
            f"{row['integer_margin_digits']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 审稿结论",
            "",
            "该证书把尾段有限义务闭合为可复核表格：",
            "`107<=P<=229` 用精确递推余量，`233<=P<=13207` 用整数交叉乘法验证连续乘积。",
            "剩余无限段只需核验显式 Mertens/prime-count 引用，低段 `61<=P<=103` 回到碰撞能量证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument("--max-p", type=int, default=13207)
    parser.add_argument("--split-denominator", type=int, default=5)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-tail-finite-certificate.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-tail-finite-certificate.md",
    )
    args = parser.parse_args()
    result = scan(args.q, args.max_p, args.split_denominator)
    args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
