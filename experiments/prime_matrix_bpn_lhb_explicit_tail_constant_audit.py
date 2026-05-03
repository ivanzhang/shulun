#!/usr/bin/env python3
"""BPN LHB 尾段显式常数审计。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_explicit_tail_constant_audit.py
  python3 experiments/prime_matrix_bpn_lhb_explicit_tail_constant_audit.py --mertens-eps 0.03

目标：
- 把 `P/5` 连续乘积不等式接到标准显式 Mertens/素数计数常数包；
- 给出解析常数包开始自动闭合的阈值；
- 明确低于该阈值的有限证书范围。
"""

from __future__ import annotations

import argparse
import json
from math import exp, gcd, log
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
EULER_GAMMA = 0.5772156649015329


def coprime_discrepancy(q: int) -> dict[str, Any]:
    """计算 `Q`-互素残基窗口相对平均密度的最大上偏差。"""
    period = [1 if gcd(residue, q) == 1 else 0 for residue in range(q)]
    phi_q = sum(period)
    density = phi_q / q
    prefix = [0]
    for value in period + period:
        prefix.append(prefix[-1] + value)

    best = {"length": 0, "hmax": 0, "excess": 0.0}
    for length in range(q + 1):
        hmax = 0 if length == 0 else max(
            prefix[start + length] - prefix[start] for start in range(q)
        )
        excess = hmax - density * length
        if excess > best["excess"]:
            best = {"length": length, "hmax": hmax, "excess": excess}
    return {
        "q": q,
        "phi_q": phi_q,
        "density": density,
        "safe_additive_constant": int(best["excess"]) + 1,
        "max_excess": best,
    }


def analytic_margin(
    p_value: int,
    density: float,
    additive_constant: float,
    q: int,
    mertens_eps: float,
    pi_upper_constant: float,
) -> float:
    """计算保守解析下界余量。

    使用候选标准输入：
    - `Hmax(P) <= density*(P-1)+additive_constant`；
    - `prod_{13<=ell<=P/5}(1-1/ell) <= (1/density)*exp(-gamma)*(1+eps)/log(P/5)`；
    - `pi(P-1) >= (P-1)/log(P-1)`；
    - `pi(P/5) <= C*(P/5)/log(P/5)`。
    """
    split = p_value / 5
    hmax_bound = density * (p_value - 1) + additive_constant
    product_bound = (1 / density) * exp(-EULER_GAMMA) * (1 + mertens_eps) / log(split)
    lhs = hmax_bound * product_bound
    rhs = (p_value - 1) / log(p_value - 1) - pi_upper_constant * split / log(split)
    return rhs - lhs


def scan(
    q: int,
    max_p: int,
    mertens_eps: float,
    pi_upper_constant: float,
) -> dict[str, Any]:
    """扫描解析常数包余量。"""
    discrepancy = coprime_discrepancy(q)
    density = discrepancy["density"]
    additive_constant = discrepancy["safe_additive_constant"]

    last_bad = None
    min_margin = None
    samples = []
    for p_value in range(233, max_p + 1):
        margin = analytic_margin(
            p_value,
            density,
            additive_constant,
            q,
            mertens_eps,
            pi_upper_constant,
        )
        if min_margin is None or margin < min_margin["margin"]:
            min_margin = {"p": p_value, "margin": margin}
        if margin < 0:
            last_bad = p_value
        if p_value in {233, 1009, 13208, 25077, 100000, max_p}:
            samples.append({"p": p_value, "margin": margin})

    stable_from = None if last_bad is None else last_bad + 1
    return {
        "certificate_type": "prime_matrix_bpn_lhb_explicit_tail_constants",
        "q": q,
        "max_p": max_p,
        "mertens_eps": mertens_eps,
        "pi_upper_constant": pi_upper_constant,
        "discrepancy": discrepancy,
        "last_bad": last_bad,
        "stable_from_in_scan": stable_from,
        "min_margin": min_margin,
        "samples": samples,
        "review_conclusion": (
            "在候选显式常数包下，连续乘积尾段从 stable_from_in_scan 起闭合；"
            "低于该阈值仍应使用有限精确证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    d = result["discrepancy"]
    lines = [
        "# BPN LHB 尾段显式常数审计",
        "",
        result["review_conclusion"],
        "",
        "## 1. 常数包",
        "",
        f"- `Q`: `{result['q']}`",
        f"- `phi(Q)/Q`: `{d['density']}`",
        f"- `Hmax` 安全加性常数: `{d['safe_additive_constant']}`",
        f"- `max_excess`: `{d['max_excess']}`",
        f"- `mertens_eps`: `{result['mertens_eps']}`",
        f"- `pi_upper_constant`: `{result['pi_upper_constant']}`",
        "",
        "## 2. 解析余量",
        "",
        f"- `last_bad`: `{result['last_bad']}`",
        f"- `stable_from_in_scan`: `{result['stable_from_in_scan']}`",
        f"- `min_margin`: `{result['min_margin']}`",
        "",
        "| P | analytic margin |",
        "| ---: | ---: |",
    ]
    for row in result["samples"]:
        lines.append(f"| {row['p']} | {row['margin']:.6f} |")
    lines.extend(
        [
            "",
            "## 3. 审稿结论",
            "",
            "该报告不替代外部显式 Mertens/素数计数定理；它只核算这些标准输入一旦接受后，",
            "需要保留到哪个有限阈值。当前默认常数包下，`P>=stable_from_in_scan` 由解析余量闭合，",
            "`233<=P<stable_from_in_scan` 应使用精确乘积有限证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument("--max-p", type=int, default=300000)
    parser.add_argument("--mertens-eps", type=float, default=0.03)
    parser.add_argument("--pi-upper-constant", type=float, default=1.25506)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-explicit-tail-constant-audit.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-explicit-tail-constant-audit.md",
    )
    args = parser.parse_args()
    result = scan(args.q, args.max_p, args.mertens_eps, args.pi_upper_constant)
    args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
