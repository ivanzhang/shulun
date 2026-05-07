#!/usr/bin/env python3
"""审计 CarryDiscrepancy 的倒数相位 Fourier 结构。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_carry_reciprocal_frequency_audit.py --max-p 30000 --top 20 --freq 64

因为 h=P-floor(P/a)*a，有
  e(r*h^2/a)=e(r*P^2/a)。
同时 h/a=P/a-floor(P/a)，所以
  e(r*h/a)=e(r*P/a)。
所以 CarryDiscrepancy 的 Fourier 展开只含倒数相位 P^2/a，
权重来自同一端点长度 P 的因子 1-e(r*P/a)。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

TAU = 2.0 * math.pi


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


def discrepancy_record(p: int, y_ratio: float) -> dict:
    """计算真实 D(P)。"""
    y = max(2, int(math.floor(y_ratio * p)))
    carry = 0
    weight = 0.0
    for a in range(y + 1, p):
        q = p // a
        h = p - q * a
        residue = (h * h) % a
        carry += 1 if residue + h > a else 0
        weight += h / a
    discrepancy = carry - weight
    return {"p": p, "y": y, "carry": carry, "weight": weight, "discrepancy": discrepancy}


def frequency_audit_p(p: int, y_ratio: float, freq: int) -> dict:
    """计算单个 p 的低频倒数相位和。"""
    base = discrepancy_record(p, y_ratio)
    y = base["y"]
    sqrt_p = math.sqrt(p)
    weighted_terms = []
    unweighted_terms = []
    partial = 0.0
    harmonic_abs = 0.0

    for r in range(1, freq + 1):
        weighted_sum = 0j
        reciprocal_sum = 0j
        for a in range(y + 1, p):
            phase = cmath.exp(1j * TAU * ((r * (p * p % a)) / a))
            # h/a 与 P/a 只差整数 floor(P/a)，指数相同。
            weight_phase = 1.0 - cmath.exp(1j * TAU * ((r * p) / a))
            weighted_sum += phase * weight_phase
            reciprocal_sum += phase
        contribution = -weighted_sum.imag / (math.pi * r)
        partial += contribution
        harmonic_abs += abs(weighted_sum) / (math.pi * r)
        weighted_terms.append(
            {
                "r": r,
                "abs": abs(weighted_sum),
                "abs_over_sqrt_p": abs(weighted_sum) / sqrt_p,
                "contribution": contribution,
            }
        )
        unweighted_terms.append(
            {
                "r": r,
                "abs": abs(reciprocal_sum),
                "abs_over_sqrt_p": abs(reciprocal_sum) / sqrt_p,
            }
        )

    top_weighted = sorted(weighted_terms, key=lambda item: -item["abs"])[:10]
    top_unweighted = sorted(unweighted_terms, key=lambda item: -item["abs"])[:10]
    base.update(
        {
            "freq": freq,
            "discrepancy_over_sqrt_p": base["discrepancy"] / sqrt_p,
            "fourier_partial": partial,
            "fourier_partial_over_sqrt_p": partial / sqrt_p,
            "harmonic_abs_over_sqrt_p": harmonic_abs / sqrt_p,
            "partial_error": base["discrepancy"] - partial,
            "partial_error_over_sqrt_p": (base["discrepancy"] - partial) / sqrt_p,
            "max_weighted_abs_over_sqrt_p": max(
                item["abs_over_sqrt_p"] for item in weighted_terms
            ),
            "max_unweighted_abs_over_sqrt_p": max(
                item["abs_over_sqrt_p"] for item in unweighted_terms
            ),
            "top_weighted": top_weighted,
            "top_unweighted": top_unweighted,
        }
    )
    return base


def audit(max_p: int, min_p: int, y_ratio: float, freq: int, top: int) -> dict:
    """审计 D(P) 最大的若干样本。"""
    primes = [
        prime for prime in primes_from_table(sieve_bool(max_p)) if prime >= min_p
    ]
    discrepancy_records = [discrepancy_record(p, y_ratio) for p in primes]
    selected = sorted(
        discrepancy_records, key=lambda item: -item["discrepancy"] / math.sqrt(item["p"])
    )[:top]
    records = [frequency_audit_p(item["p"], y_ratio, freq) for item in selected]
    return {
        "parameters": {
            "max_p": max_p,
            "min_p": min_p,
            "y_ratio": y_ratio,
            "freq": freq,
            "top": top,
        },
        "summary": {
            "candidate_count": len(discrepancy_records),
            "max_discrepancy_record": records[0] if records else None,
            "max_weighted_frequency_record": max(
                records, key=lambda item: item["max_weighted_abs_over_sqrt_p"], default=None
            ),
            "max_unweighted_frequency_record": max(
                records,
                key=lambda item: item["max_unweighted_abs_over_sqrt_p"],
                default=None,
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    max_d = summary["max_discrepancy_record"]
    max_weighted = summary["max_weighted_frequency_record"]
    max_unweighted = summary["max_unweighted_frequency_record"]

    def compact_top_terms(terms: list[dict], limit: int = 3) -> str:
        """压缩最高频率项，避免 Markdown 报告被 JSON 淹没。"""
        return "; ".join(
            f"r={term['r']}: {term['abs_over_sqrt_p']:.3f}"
            for term in terms[:limit]
        )

    lines = [
        "# CarryDiscrepancy 倒数相位频率审计",
        "",
        "**状态：** `experimental_reciprocal_frequency_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `min_p`: `{params['min_p']}`",
        f"- `freq`: `{params['freq']}`",
        f"- `top`: `{params['top']}`",
        "",
        "## 总结",
        "",
        f"- 候选素数个数：`{summary['candidate_count']}`。",
        f"- 最大正偏差：`p={max_d['p'] if max_d else None}`，"
        f"`D/sqrt(P)={max_d['discrepancy_over_sqrt_p']:.6f}`。"
        if max_d
        else "- 最大正偏差：无样本。",
        f"- 已展开样本中的最大加权频率：`p={max_weighted['p'] if max_weighted else None}`，"
        f"`max |S_r|/sqrt(P)={max_weighted['max_weighted_abs_over_sqrt_p']:.6f}`。"
        if max_weighted
        else "- 已展开样本中的最大加权频率：无样本。",
        f"- 已展开样本中的最大无权倒数频率：`p={max_unweighted['p'] if max_unweighted else None}`，"
        f"`max |T_r|/sqrt(P)={max_unweighted['max_unweighted_abs_over_sqrt_p']:.6f}`。"
        if max_unweighted
        else "- 已展开样本中的最大无权倒数频率：无样本。",
        "",
        "## 样本表",
        "",
        "| p | D/sqrtP | partial/sqrtP | err/sqrtP | abs budget/sqrtP | max weighted/sqrtP | max reciprocal/sqrtP | top weighted |",
        "|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['discrepancy_over_sqrt_p']:.6f} | "
            f"{record['fourier_partial_over_sqrt_p']:.6f} | {record['partial_error_over_sqrt_p']:.6f} | "
            f"{record['harmonic_abs_over_sqrt_p']:.6f} | "
            f"{record['max_weighted_abs_over_sqrt_p']:.6f} | "
            f"{record['max_unweighted_abs_over_sqrt_p']:.6f} | "
            f"{compact_top_terms(record['top_weighted'])} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "该审计验证 CarryDiscrepancy 的 Fourier 对象是加权倒数相位和 `sum e(rP^2/a)(1-e(rP/a))`。若 `D(P)` 超过阈值，必有低频加权倒数相位和异常偏大，正是 `RSE/HyperbolicDisc/PDEC` 的证书对象。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=30000)
    parser.add_argument("--min-p", type=int, default=10007)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--freq", type=int, default=64)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_carry_reciprocal_frequency_audit_20260505",
    )
    args = parser.parse_args()
    if args.max_p < args.min_p:
        raise SystemExit("--max-p 必须不小于 --min-p，否则尾段样本为空。")
    result = audit(args.max_p, args.min_p, args.y_ratio, args.freq, args.top)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = result["summary"]
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
