#!/usr/bin/env python3
"""生成 FO-PDEC 显式 Fourier 阈值账本。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py
  python3 experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py \
    --input docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json

目标：
  对每个解释因子 ell 的行残基计数 g_ell(rho)，直接计算

      max_{h!=0} |sum_rho g_ell(rho) exp(2*pi*i*h*rho/ell)|

  这就是该 ell 投影上的显式 PDEC 下界。后续只需证明同一投影的
  CRT 上界 U_CRT 小于该数值。

注意：这是有限阈值账本，不是全局 U_CRT 上界证明。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


def grouped_equations(equations: list[dict]) -> dict[str, list[dict]]:
    """构造全局、块、偏移行、矩阵行四种分组。"""
    groups: dict[str, list[dict]] = {"global": equations}
    by_block: defaultdict[tuple[int], list[dict]] = defaultdict(list)
    by_offset: defaultdict[tuple[int], list[dict]] = defaultdict(list)
    by_matrix_row: defaultdict[tuple[int, int], list[dict]] = defaultdict(list)
    for equation in equations:
        by_block[(equation["block_index"],)].append(equation)
        by_offset[(equation["offset_row_index"],)].append(equation)
        by_matrix_row[(equation["q"], equation["source_row"])].append(equation)
    for key, rows in by_block.items():
        groups[f"block:{key[0]}"] = rows
    for key, rows in by_offset.items():
        groups[f"offset-row:{key[0]}"] = rows
    for key, rows in by_matrix_row.items():
        groups[f"matrix-row:q{key[0]}:r{key[1]}"] = rows
    return groups


def max_fourier_for_counts(modulus: int, counts: Counter[int]) -> dict:
    """直接计算非零 Fourier 最大模。"""
    best_h = 0
    best_value = 0.0
    for frequency in range(1, modulus):
        total = 0j
        for residue, count in counts.items():
            angle = 2.0 * math.pi * frequency * residue / modulus
            total += count * cmath.exp(1j * angle)
        magnitude = abs(total)
        if magnitude > best_value:
            best_value = magnitude
            best_h = frequency
    total_count = sum(counts.values())
    support_size = len(counts)
    support_bound = (
        total_count * math.sqrt((modulus - support_size) / (modulus * (modulus - 1) * support_size))
        if support_size and support_size < modulus
        else 0.0
    )
    return {
        "best_frequency": best_h,
        "max_fourier": best_value,
        "support_pdec_lower_bound": support_bound,
        "total_count": total_count,
        "support_size": support_size,
        "top_residues": [
            {"residue": residue, "load": load}
            for residue, load in counts.most_common(8)
        ],
    }


def analyze_group(name: str, equations: Iterable[dict]) -> dict:
    """分析一个方程组的所有解释因子投影。"""
    by_factor: defaultdict[int, Counter[int]] = defaultdict(Counter)
    for equation in equations:
        by_factor[equation["explaining_factor"]].update([equation["target_residue"]])
    factor_rows = []
    for factor, counts in sorted(by_factor.items()):
        row = max_fourier_for_counts(factor, counts)
        row["factor"] = factor
        factor_rows.append(row)
    factor_rows.sort(key=lambda row: (row["max_fourier"], row["total_count"]), reverse=True)
    return {
        "group": name,
        "factor_count": len(factor_rows),
        "equation_count": sum(row["total_count"] for row in factor_rows),
        "best_factor": factor_rows[0] if factor_rows else None,
        "factor_rows": factor_rows,
    }


def build_ledger(source: dict) -> dict:
    """生成 Fourier 阈值账本。"""
    groups = grouped_equations(source["equations"])
    group_rows = [analyze_group(name, rows) for name, rows in sorted(groups.items())]
    global_row = next(row for row in group_rows if row["group"] == "global")
    best_rows = [row["best_factor"] for row in group_rows if row["best_factor"]]
    return {
        "status": "finite_fo_pdec_fourier_threshold_ledger_not_global_proof",
        "summary": {
            "group_count": len(group_rows),
            "global_equation_count": global_row["equation_count"],
            "global_best_factor": global_row["best_factor"],
            "max_group_fourier_threshold": max(
                (row["max_fourier"] for row in best_rows),
                default=0.0,
            ),
            "min_group_best_fourier_threshold": min(
                (row["max_fourier"] for row in best_rows),
                default=0.0,
            ),
            "max_support_pdec_lower_bound": max(
                (row["support_pdec_lower_bound"] for row in best_rows),
                default=0.0,
            ),
        },
        "groups": group_rows,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 阈值账本。"""
    summary = result["summary"]
    lines = [
        "# FO-PDEC 显式 Fourier 阈值账本",
        "",
        "**状态：** `finite_fo_pdec_fourier_threshold_ledger_not_global_proof`",
        "",
        "本文档直接计算每个解释因子投影上的非零 Fourier 最大值。该值是同一坏窗方程集合已经产生的显式 `PDEC` 下界；剩余任务是证明同一投影的 `U_CRT` 上界严格小于该阈值。",
        "",
        "## 摘要",
        "",
        f"- 分组数：`{summary['group_count']}`。",
        f"- 全局方程数：`{summary['global_equation_count']}`。",
        f"- 全局最佳因子：`{summary['global_best_factor']}`。",
        f"- 最大分组 Fourier 阈值：`{summary['max_group_fourier_threshold']}`。",
        f"- 最小分组最佳 Fourier 阈值：`{summary['min_group_best_fourier_threshold']}`。",
        f"- 最大支撑型 PDEC 下界：`{summary['max_support_pdec_lower_bound']}`。",
        "",
        "## 分组最佳阈值",
        "",
        "| group | equations | factors | best ell | best h | max Fourier | support lower | support | top residues |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for group in result["groups"]:
        best = group["best_factor"]
        if not best:
            continue
        lines.append(
            "| {group} | {eq} | {fac} | {ell} | {h} | {fourier:.6f} | {lower:.6f} | {support} | {residues} |".format(
                group=group["group"],
                eq=group["equation_count"],
                fac=group["factor_count"],
                ell=best["factor"],
                h=best["best_frequency"],
                fourier=best["max_fourier"],
                lower=best["support_pdec_lower_bound"],
                support=best["support_size"],
                residues=best["top_residues"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "对每个固定因子 `ell`，相位计数向量 `g_ell` 的非零 Fourier 最大模是直接可核验的 `PDEC` 下界。若能从 CRT 结构约束、端点镜像、列容量、尾锚非复用或 SAE 排除中证明同一 `g_ell` 的上界 `U_CRT` 小于该值，则该投影闭合。",
            "",
            "本账本没有证明 `U_CRT`。它把下一硬点精确为：为最佳投影给出同一坏窗集合上的 `U_CRT` 上界，而不是继续改变命题或扩大有限样本。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger",
    )
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_ledger(source)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
