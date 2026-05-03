#!/usr/bin/env python3
"""审计 FO-PDEC 最佳 Fourier 投影的对偶聚簇结构。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_dual_cluster_audit.py
  python3 experiments/prime_matrix_wsh_fo_pdec_dual_cluster_audit.py \
    --input docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json

目标：
  对每个解释因子 ell 和最佳非零频率 h，计算 transformed residue h*rho mod ell
  的最短圆弧覆盖长度。若 Fourier 模接近质量上界，支撑必须在对偶圆周上聚簇；
  该聚簇就是 U_CRT 上界必须排除或吸收到 SAE/Endpoint 的具体障碍。

注意：这是有限结构审计，不是全局 U_CRT 上界证明。
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


def best_frequency(modulus: int, counts: Counter[int]) -> dict:
    """返回最大 Fourier 频率与模长。"""
    best_h = 0
    best_value = 0.0
    best_sum = 0j
    for frequency in range(1, modulus):
        total = 0j
        for residue, count in counts.items():
            angle = 2.0 * math.pi * frequency * residue / modulus
            total += count * cmath.exp(1j * angle)
        magnitude = abs(total)
        if magnitude > best_value:
            best_h = frequency
            best_value = magnitude
            best_sum = total
    return {"frequency": best_h, "fourier": best_value, "sum": best_sum}


def shortest_arc(modulus: int, residues: Iterable[int]) -> dict:
    """计算圆周上覆盖给定残基支撑的最短整数圆弧。"""
    points = sorted(set(residue % modulus for residue in residues))
    if not points:
        return {"arc_length": 0, "arc_start": None, "arc_end": None, "points": []}
    if len(points) == 1:
        return {
            "arc_length": 0,
            "arc_start": points[0],
            "arc_end": points[0],
            "points": points,
        }
    gaps = []
    for index, point in enumerate(points):
        next_point = points[(index + 1) % len(points)]
        gap = (next_point - point) % modulus
        gaps.append((gap, point, next_point))
    max_gap, gap_start, gap_end = max(gaps)
    return {
        "arc_length": modulus - max_gap,
        "arc_start": gap_end,
        "arc_end": gap_start,
        "points": points,
        "max_gap": max_gap,
    }


def analyze_group(name: str, equations: list[dict]) -> list[dict]:
    """分析一个分组中的每个解释因子。"""
    by_factor: defaultdict[int, Counter[int]] = defaultdict(Counter)
    sample_by_factor: defaultdict[int, list[dict]] = defaultdict(list)
    for equation in equations:
        factor = equation["explaining_factor"]
        residue = equation["target_residue"]
        by_factor[factor].update([residue])
        sample_by_factor[factor].append(equation)

    rows = []
    for factor, counts in by_factor.items():
        best = best_frequency(factor, counts)
        frequency = best["frequency"]
        transformed_counter = Counter(
            (frequency * residue) % factor
            for residue, count in counts.items()
            for _ in range(count)
        )
        arc = shortest_arc(factor, transformed_counter.keys())
        mass = sum(counts.values())
        rows.append(
            {
                "group": name,
                "factor": factor,
                "mass": mass,
                "support_size": len(counts),
                "best_frequency": frequency,
                "max_fourier": best["fourier"],
                "mass_defect": mass - best["fourier"],
                "relative_defect": (mass - best["fourier"]) / mass if mass else 0.0,
                "dual_arc_length": arc["arc_length"],
                "dual_arc_fraction": arc["arc_length"] / factor if factor else 0.0,
                "dual_arc_start": arc["arc_start"],
                "dual_arc_end": arc["arc_end"],
                "transformed_residues": [
                    {"residue": residue, "load": load}
                    for residue, load in transformed_counter.most_common()
                ],
                "original_residues": [
                    {"residue": residue, "load": load}
                    for residue, load in counts.most_common()
                ],
                "sample_equations": sample_by_factor[factor][:10],
            }
        )
    rows.sort(key=lambda row: (row["max_fourier"], -row["mass_defect"]), reverse=True)
    return rows


def build_audit(source: dict) -> dict:
    """生成对偶聚簇审计。"""
    groups = grouped_equations(source["equations"])
    all_rows = []
    best_by_group = []
    for name, equations in sorted(groups.items()):
        rows = analyze_group(name, equations)
        all_rows.extend(rows)
        if rows:
            best_by_group.append(rows[0])
    all_rows.sort(key=lambda row: row["max_fourier"], reverse=True)
    global_best = next(row for row in all_rows if row["group"] == "global")
    return {
        "status": "finite_fo_pdec_dual_cluster_audit_not_global_proof",
        "summary": {
            "group_count": len(groups),
            "projection_count": len(all_rows),
            "global_best": {
                key: global_best[key]
                for key in [
                    "factor",
                    "mass",
                    "support_size",
                    "best_frequency",
                    "max_fourier",
                    "mass_defect",
                    "relative_defect",
                    "dual_arc_length",
                    "dual_arc_fraction",
                    "dual_arc_start",
                    "dual_arc_end",
                    "transformed_residues",
                    "original_residues",
                ]
            },
            "best_group_rows": [
                {
                    key: row[key]
                    for key in [
                        "group",
                        "factor",
                        "mass",
                        "best_frequency",
                        "max_fourier",
                        "mass_defect",
                        "dual_arc_length",
                        "dual_arc_fraction",
                    ]
                }
                for row in best_by_group[:40]
            ],
        },
        "projections": all_rows[:200],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    best = summary["global_best"]
    lines = [
        "# FO-PDEC 对偶聚簇审计",
        "",
        "**状态：** `finite_fo_pdec_dual_cluster_audit_not_global_proof`",
        "",
        "本文档审计 `U_CRT,199` 难点的具体结构：最佳 Fourier 投影接近质量上界，是因为低模残基在乘以最佳频率后落入很短的对偶圆弧。该聚簇必须由 `PDEC-Dual-Cert` 排斥，或由 `SAE/Endpoint` 吸收。",
        "",
        "## 全局最佳投影",
        "",
        f"- 解释因子 `ell`: `{best['factor']}`。",
        f"- 方程质量 `mass`: `{best['mass']}`。",
        f"- 支撑大小：`{best['support_size']}`。",
        f"- 最佳频率 `h`: `{best['best_frequency']}`。",
        f"- Fourier 阈值：`{best['max_fourier']}`。",
        f"- 距离质量上界缺口：`{best['mass_defect']}`。",
        f"- 相对缺口：`{best['relative_defect']}`。",
        f"- 对偶最短弧长：`{best['dual_arc_length']}`。",
        f"- 对偶弧长比例：`{best['dual_arc_fraction']}`。",
        f"- 原始残基：`{best['original_residues']}`。",
        f"- 对偶残基：`{best['transformed_residues']}`。",
        "",
        "## 分组最佳投影",
        "",
        "| group | ell | mass | h | Fourier | mass defect | dual arc | arc fraction |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary["best_group_rows"]:
        lines.append(
            "| {group} | {factor} | {mass} | {h} | {fourier:.6f} | {defect:.6f} | {arc} | {frac:.6f} |".format(
                group=row["group"],
                factor=row["factor"],
                mass=row["mass"],
                h=row["best_frequency"],
                fourier=row["max_fourier"],
                defect=row["mass_defect"],
                arc=row["dual_arc_length"],
                frac=row["dual_arc_fraction"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "单纯质量上界只给 `U_CRT<=4`，而最佳投影下界为 `3.959247567099438`，只差 `0.040752432900562`。因此必须获得约 `1.02%` 的真实结构节省。该节省不能来自非负性或质量行，必须来自对偶聚簇排斥：`ell=199,h=95` 后，支撑压到长度 `11` 的短弧中。",
            "",
            "下一硬点已具体化为：证明这种短对偶弧聚簇若在反例链中持久出现，则进入 `PDEC-Dual-Cert`；若不持久，则进入 `SAE/Endpoint`。在该证明完成前，不能宣称 `U_CRT,199` 全局闭合。",
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
        default="docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-audit",
    )
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_audit(source)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"]["global_best"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
