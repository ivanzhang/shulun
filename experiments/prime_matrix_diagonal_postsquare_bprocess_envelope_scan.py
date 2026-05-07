#!/usr/bin/env python3
"""扫描 EndpointReciprocal-OSC 的 B-process 低频包络。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_bprocess_envelope_scan.py \
    --max-p 100000 --freq 64 --threshold 1.55 \
    --out-prefix docs/diagonal_postsquare_bprocess_envelope_scan_p100000_20260505

该脚本扫描 B-process 主项
  -Im sum_{r,n} c_{r,n}(1-e(sqrt(rn)))e(2P sqrt(rn)+1/8)/(pi r)
在素数 P 上的归一化低频包络。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import defaultdict
from pathlib import Path

TAU = 2.0 * math.pi


def exp1(value: float) -> complex:
    """计算 e(value)=exp(2*pi*i*value)。"""
    return cmath.exp(1j * TAU * value)


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


def primes_between(min_p: int, max_p: int) -> list[int]:
    """提取指定范围内的素数。"""
    flags = sieve_bool(max_p)
    return [idx for idx in range(max(2, min_p), max_p + 1) if flags[idx]]


def squarefree_kernel(value: int) -> int:
    """返回平方自由核。"""
    rem = value
    kernel = 1
    factor = 2
    while factor * factor <= rem:
        power = 0
        while rem % factor == 0:
            rem //= factor
            power += 1
        if power % 2:
            kernel *= factor
        factor += 1 if factor == 2 else 2
    if rem > 1:
        kernel *= rem
    return kernel


def stationary_terms(freq: int) -> list[dict]:
    """生成可能出现的驻相项。"""
    terms = []
    for r in range(1, freq + 1):
        for n in range(r + 1, math.ceil(math.e * math.e * r)):
            root = math.sqrt(r * n)
            coeff = (r ** 0.25) / (
                math.sqrt(2.0) * (n ** 0.75) * math.pi * r
            )
            weight = 1.0 - exp1(root)
            terms.append(
                {
                    "r": r,
                    "n": n,
                    "root": root,
                    "sqrt_ratio": math.sqrt(r / n),
                    "coeff": coeff,
                    "weight": weight,
                    "squarefree": squarefree_kernel(r * n),
                }
            )
    return terms


def bprocess_partial(p: int, terms: list[dict], kappa: float) -> tuple[float, dict[int, float]]:
    """计算单个 P 的 B-process 低频主项与平方自由分组贡献。"""
    y = max(2, int(math.floor(p / math.e)))
    lower_a = y + 1
    total = 0.0
    by_kernel: dict[int, float] = defaultdict(float)
    for term in terms:
        x = p * term["sqrt_ratio"]
        if x < lower_a or x > p - 1:
            continue
        value = term["coeff"] * term["weight"] * exp1(2.0 * p * term["root"] + kappa)
        contribution = -value.imag
        total += contribution
        by_kernel[term["squarefree"]] += contribution
    return total, by_kernel


def audit(
    max_p: int,
    min_p: int,
    freq: int,
    threshold: float,
    top: int,
    core_kernels: set[int],
) -> dict:
    """扫描素数 P 的低频包络。"""
    terms = stationary_terms(freq)
    primes = primes_between(min_p, max_p)
    records = []
    failure_count = 0
    max_record = None
    min_record = None

    for p in primes:
        partial, by_kernel = bprocess_partial(p, terms, 0.125)
        top_positive = sorted(
            (
                {"squarefree": kernel, "contribution": value}
                for kernel, value in by_kernel.items()
            ),
            key=lambda item: -item["contribution"],
        )[:8]
        core_contribution = sum(
            value for kernel, value in by_kernel.items() if kernel in core_kernels
        )
        tail_contribution = partial - core_contribution
        tail_group_abs = sum(
            abs(value) for kernel, value in by_kernel.items() if kernel not in core_kernels
        )
        record = {
            "p": p,
            "partial_over_sqrt_p": partial,
            "margin_to_threshold": threshold - partial,
            "core_contribution": core_contribution,
            "tail_contribution": tail_contribution,
            "tail_group_abs": tail_group_abs,
            "top_positive_squarefree": top_positive,
        }
        if partial > threshold:
            failure_count += 1
            records.append(record)
        else:
            records.append(record)
        if max_record is None or partial > max_record["partial_over_sqrt_p"]:
            max_record = record
        if min_record is None or partial < min_record["partial_over_sqrt_p"]:
            min_record = record

    top_records = sorted(records, key=lambda item: -item["partial_over_sqrt_p"])[:top]
    core_thresholds = [0.0, 0.5, 0.8, 1.0, 1.1, 1.15]
    conditional_tail = []
    for cutoff in core_thresholds:
        bucket = [record for record in records if record["core_contribution"] >= cutoff]
        if not bucket:
            conditional_tail.append(
                {
                    "core_cutoff": cutoff,
                    "count": 0,
                    "max_tail": None,
                    "max_partial": None,
                    "record": None,
                }
            )
            continue
        record = max(bucket, key=lambda item: item["tail_contribution"])
        partial_record = max(bucket, key=lambda item: item["partial_over_sqrt_p"])
        conditional_tail.append(
            {
                "core_cutoff": cutoff,
                "count": len(bucket),
                "max_tail": record["tail_contribution"],
                "max_partial": partial_record["partial_over_sqrt_p"],
                "record": record,
            }
        )
    return {
        "parameters": {
            "max_p": max_p,
            "min_p": min_p,
            "freq": freq,
            "threshold": threshold,
            "top": top,
            "term_count": len(terms),
            "core_kernels": sorted(core_kernels),
        },
        "summary": {
            "prime_count": len(primes),
            "failure_count": failure_count,
            "max_record": max_record,
            "min_record": min_record,
            "max_tail_group_abs_record": max(
                records, key=lambda item: item["tail_group_abs"], default=None
            ),
            "max_tail_contribution_record": max(
                records, key=lambda item: item["tail_contribution"], default=None
            ),
            "max_core_record": max(
                records, key=lambda item: item["core_contribution"], default=None
            ),
            "conditional_tail_by_core": conditional_tail,
            "top_records": top_records,
        },
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]

    def compact_groups(groups: list[dict]) -> str:
        """压缩平方自由核贡献。"""
        return "; ".join(
            f"d={item['squarefree']}: {item['contribution']:.3f}"
            for item in groups[:5]
        )

    lines = [
        "# EndpointReciprocal-OSC B-process 包络扫描",
        "",
        "**状态：** `bprocess_envelope_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `min_p`: `{params['min_p']}`",
        f"- `max_p`: `{params['max_p']}`",
        f"- `freq`: `{params['freq']}`",
        f"- `threshold`: `{params['threshold']}`",
        f"- `term_count`: `{params['term_count']}`",
        f"- `core_kernels`: `{params['core_kernels']}`",
        "",
        "## 总结",
        "",
        f"- 素数样本数：`{summary['prime_count']}`。",
        f"- 超阈值样本数：`{summary['failure_count']}`。",
        f"- 最大样本：`p={summary['max_record']['p']}`，"
        f"`partial/sqrt(P)={summary['max_record']['partial_over_sqrt_p']:.6f}`，"
        f"`margin={summary['max_record']['margin_to_threshold']:.6f}`。",
        f"- 最小样本：`p={summary['min_record']['p']}`，"
        f"`partial/sqrt(P)={summary['min_record']['partial_over_sqrt_p']:.6f}`。",
        f"- 最大核心贡献：`p={summary['max_core_record']['p']}`，"
        f"`core={summary['max_core_record']['core_contribution']:.6f}`。",
        f"- 最大分组尾绝对量：`p={summary['max_tail_group_abs_record']['p']}`，"
        f"`tail_group_abs={summary['max_tail_group_abs_record']['tail_group_abs']:.6f}`。",
        f"- 最大尾核有符号正贡献：`p={summary['max_tail_contribution_record']['p']}`，"
        f"`tail={summary['max_tail_contribution_record']['tail_contribution']:.6f}`。",
        "",
        "## 条件尾核表",
        "",
        "| core cutoff | count | max tail | max partial | witness p |",
        "|---:|---:|---:|---:|---:|",
    ]
    for item in summary["conditional_tail_by_core"]:
        witness = item["record"]["p"] if item["record"] else None
        max_tail = item["max_tail"]
        max_partial = item["max_partial"]
        lines.append(
            f"| {item['core_cutoff']:.2f} | {item['count']} | "
            f"{max_tail:.6f} | {max_partial:.6f} | {witness} |"
            if max_tail is not None
            else f"| {item['core_cutoff']:.2f} | 0 |  |  |  |"
        )
    lines.extend(
        [
            "",
            "## 最大样本表",
            "",
            "| p | partial/sqrtP | margin | core | tail | tail group abs | top positive squarefree |",
            "|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for record in summary["top_records"]:
        lines.append(
            f"| {record['p']} | {record['partial_over_sqrt_p']:.6f} | "
            f"{record['margin_to_threshold']:.6f} | "
            f"{record['core_contribution']:.6f} | "
            f"{record['tail_contribution']:.6f} | "
            f"{record['tail_group_abs']:.6f} | "
            f"{compact_groups(record['top_positive_squarefree'])} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "该扫描把 `ERO-Low` 的真实低频项替换为已校准的 B-process 主项。若包络长期低于阈值，下一步应把该有限非平方根三角多项式写成可审稿的 Diophantine/PDEC 二分；若出现超阈值样本，则直接分析其平方自由核贡献，抽取 endpoint PDEC 证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=100000)
    parser.add_argument("--min-p", type=int, default=10007)
    parser.add_argument("--freq", type=int, default=64)
    parser.add_argument("--threshold", type=float, default=1.55)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument(
        "--core-kernels",
        default="2,3,5,6,7,10,14,15,21,30,42",
        help="逗号分隔的核心平方自由核。",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_bprocess_envelope_scan_20260505",
    )
    args = parser.parse_args()
    core_kernels = {
        int(item) for item in args.core_kernels.split(",") if item.strip()
    }
    result = audit(
        args.max_p,
        args.min_p,
        args.freq,
        args.threshold,
        args.top,
        core_kernels,
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
