#!/usr/bin/env python3
"""审计 FO-PDEC FormalUnit-Stitching 的可行性。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_stitching_feasibility_audit.py

目的：
  当前 ell=199 强阈值来自有限库聚合。本脚本把重复事件拆成：
  1. 同 q、同行、同坐标的嵌套块重复；
  2. 不同 q 层中的同一物理整数复用。

  审计目标不是证明全局定理，而是判断这些重复是否已经具备进入单个
  PDEC formal unit 的必要条件。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


Equation = dict[str, object]


def factor_trial(n: int) -> list[int]:
    """用试除法分解审计样本整数。"""
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def best_fourier(rows: Iterable[Equation]) -> dict | None:
    """计算一组方程中的最佳单因子 Fourier 投影。"""
    by_factor: defaultdict[int, Counter[int]] = defaultdict(Counter)
    for row in rows:
        by_factor[int(row["explaining_factor"])][int(row["target_residue"])] += 1
    best: dict | None = None
    for factor, counts in by_factor.items():
        best_value = 0.0
        best_frequency = 0
        for frequency in range(1, factor):
            total = 0j
            for residue, load in counts.items():
                total += load * cmath.exp(2j * math.pi * frequency * residue / factor)
            value = abs(total)
            if value > best_value:
                best_value = value
                best_frequency = frequency
        row = {
            "factor": factor,
            "frequency": best_frequency,
            "fourier": best_value,
            "mass": sum(counts.values()),
            "support": len(counts),
            "residues": [
                {"residue": residue, "load": load}
                for residue, load in counts.most_common()
            ],
        }
        if best is None or (row["fourier"], row["mass"]) > (
            best["fourier"],
            best["mass"],
        ):
            best = row
    return best


def dedupe(rows: Iterable[Equation], key_fields: tuple[str, ...]) -> list[Equation]:
    """按字段去重。"""
    seen: set[tuple] = set()
    result: list[Equation] = []
    for row in rows:
        key = tuple(row[field] for field in key_fields)
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result


def group_best(
    equations: list[Equation],
    group_fields: tuple[str, ...],
    dedupe_fields: tuple[str, ...] | None = None,
) -> dict:
    """按 formal branch 分组后计算最佳投影。"""
    groups: defaultdict[tuple, list[Equation]] = defaultdict(list)
    for row in equations:
        groups[tuple(row[field] for field in group_fields)].append(row)
    rows = []
    for key, values in sorted(groups.items()):
        reduced = dedupe(values, dedupe_fields) if dedupe_fields else list(values)
        rows.append(
            {
                "key": list(key),
                "raw_count": len(values),
                "effective_count": len(reduced),
                "best": best_fourier(reduced),
            }
        )
    best = max(
        (row for row in rows if row["best"]),
        key=lambda row: (row["best"]["fourier"], row["best"]["mass"]),
        default=None,
    )
    return {"unit_count": len(rows), "best_unit": best, "units": rows}


def source(row: Equation) -> dict:
    """压缩方程来源。"""
    return {
        "block_index": row["block_index"],
        "offset_row_index": row["offset_row_index"],
        "p": row["p"],
        "q": row["q"],
        "source_row": row["source_row"],
        "candidate_row": row["candidate_row"],
        "column": row["column"],
        "offset": row["offset"],
        "candidate": row["candidate"],
        "factor": row["explaining_factor"],
        "target_residue": row["target_residue"],
    }


def exact_nested_duplicates(equations: list[Equation]) -> list[dict]:
    """找同 q、同行、同坐标、同解释因子的嵌套重复。"""
    key_fields = (
        "q",
        "source_row",
        "candidate_row",
        "column",
        "offset",
        "candidate",
        "explaining_factor",
        "target_residue",
    )
    buckets: defaultdict[tuple, list[Equation]] = defaultdict(list)
    for row in equations:
        buckets[tuple(row[field] for field in key_fields)].append(row)
    result = []
    for key, rows in sorted(buckets.items()):
        if len(rows) <= 1:
            continue
        block_ids = sorted({int(row["block_index"]) for row in rows})
        result.append(
            {
                "key": list(key),
                "multiplicity": len(rows),
                "block_ids": block_ids,
                "same_formal_coordinate": True,
                "independence_status": "not_independent_without_weighted_hall_dual_row",
                "sources": [source(row) for row in rows],
            }
        )
    return result


def cross_level_reuses(equations: list[Equation]) -> list[dict]:
    """找不同 q 层复用同一物理候选和解释因子的事件。"""
    buckets: defaultdict[tuple, list[Equation]] = defaultdict(list)
    for row in equations:
        buckets[(row["candidate"], row["explaining_factor"])].append(row)
    result = []
    for key, rows in sorted(buckets.items()):
        q_layers = sorted({int(row["q"]) for row in rows})
        if len(q_layers) <= 1:
            continue
        candidate = int(key[0])
        result.append(
            {
                "candidate": candidate,
                "factor": int(key[1]),
                "integer_factorization": factor_trial(candidate),
                "multiplicity": len(rows),
                "q_layers": q_layers,
                "row_residues": [
                    {
                        "q": row["q"],
                        "row": row["source_row"],
                        "target_residue": row["target_residue"],
                    }
                    for row in rows
                ],
                "stitching_status": "not_same_formal_branch_without_persistence_theorem",
                "sources": [source(row) for row in rows],
            }
        )
    return result


def build_audit(source_data: dict, tight_data: dict) -> dict:
    """构造拼接可行性审计。"""
    equations: list[Equation] = source_data["equations"]
    raw_best = best_fourier(equations)
    coordinate_fields = (
        "q",
        "source_row",
        "candidate_row",
        "column",
        "offset",
        "candidate",
        "explaining_factor",
    )
    branch_by_q_row = group_best(
        equations,
        ("q", "source_row"),
        coordinate_fields,
    )
    branch_by_block = group_best(equations, ("block_index",), None)
    tight_blocks = {
        index: {
            "p": row["p"],
            "q": row["q"],
            "row": row["row"],
            "semiprime_values": row["semiprime_values"],
            "semiprime_count": row["semiprime_count"],
            "surplus": row["surplus"],
        }
        for index, row in enumerate(tight_data["tight_long_blocks"], start=1)
    }
    nested = exact_nested_duplicates(equations)
    for duplicate in nested:
        duplicate["block_geometry"] = [
            tight_blocks[block_id] for block_id in duplicate["block_ids"]
        ]
    cross = cross_level_reuses(equations)
    return {
        "status": "finite_fo_pdec_stitching_feasibility_audit_not_global_proof",
        "summary": {
            "raw_best": raw_best,
            "q_row_coordinate_dedup_best": branch_by_q_row["best_unit"],
            "block_local_best": branch_by_block["best_unit"],
            "exact_nested_duplicate_count": len(nested),
            "cross_level_reuse_count": len(cross),
            "formal_unit_conclusion": (
                "当前数据不支持把 global_library_raw 强阈值直接作为单分支 PDEC 下界；"
                "需要额外证明 weighted Hall dual independence 或 cross-q persistence theorem。"
            ),
        },
        "exact_nested_duplicates": nested,
        "cross_level_reuses": cross,
        "branch_by_q_row": branch_by_q_row,
        "branch_by_block": branch_by_block,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    raw = summary["raw_best"]
    qbest = summary["q_row_coordinate_dedup_best"]["best"]
    bbest = summary["block_local_best"]["best"]
    lines = [
        "# FO-PDEC 拼接可行性审计",
        "",
        "**状态：** `finite_fo_pdec_stitching_feasibility_audit_not_global_proof`",
        "",
        "本文档直接审计 `FormalUnit-Stitching` 与 `NestedBlock-Independence`。它区分“有限库聚合信号”和“单个正式反例分支可用的 PDEC 向量”。",
        "",
        "## 总表",
        "",
        "| object | mass | ell | h | Fourier | support |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        f"| global library raw | {raw['mass']} | {raw['factor']} | {raw['frequency']} | {raw['fourier']:.6f} | {raw['support']} |",
        f"| q-row coordinate dedup best | {qbest['mass']} | {qbest['factor']} | {qbest['frequency']} | {qbest['fourier']:.6f} | {qbest['support']} |",
        f"| block-local best | {bbest['mass']} | {bbest['factor']} | {bbest['frequency']} | {bbest['fourier']:.6f} | {bbest['support']} |",
        "",
        "结论：强阈值 `3.959...` 是有限库聚合信号；在单个 `q` 行坐标去重或单个 Hall 块口径下，当前最佳值只有 `1.0`。",
        "",
        "## 嵌套同坐标重复",
        "",
        "| key | multiplicity | blocks | status |",
        "| --- | ---: | --- | --- |",
    ]
    for row in result["exact_nested_duplicates"]:
        lines.append(
            "| `{key}` | {mult} | `{blocks}` | `{status}` |".format(
                key=row["key"],
                mult=row["multiplicity"],
                blocks=row["block_ids"],
                status=row["independence_status"],
            )
        )
    lines.extend(
        [
            "",
            "嵌套同坐标重复的 CRT 方程完全相同。它只有在加权 Hall 对偶中被证明为两条独立约束行时才可重复计数；否则必须按同一正式坐标去重。",
            "",
            "## 跨层同整数复用",
            "",
            "| candidate | factorization | factor | q layers | row residues | status |",
            "| ---: | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in result["cross_level_reuses"]:
        lines.append(
            "| {candidate} | `{factorization}` | {factor} | `{layers}` | `{residues}` | `{status}` |".format(
                candidate=row["candidate"],
                factorization=row["integer_factorization"],
                factor=row["factor"],
                layers=row["q_layers"],
                residues=row["row_residues"],
                status=row["stitching_status"],
            )
        )
    lines.extend(
        [
            "",
            "跨层同整数复用说明同一个合数可在不同方阵宽度中持续被旧小因子解释。但这不是自动的单分支 `PDEC` 向量：必须证明同一个假设反例链会同时强制这些 `q` 层事件，且存在统一相位映射。否则它只是有限库中的相似样本。",
            "",
            "## 硬攻结论",
            "",
            "当前最严谨的结论是一个排除误用的二分：",
            "",
            "```text",
            "A. 证明 weighted Hall dual independence + cross-q persistence theorem，",
            "   然后 global_library_raw 强阈值才可进入 PDEC；",
            "",
            "B. 若不能证明 A，则重复项必须去重或回流 SAE/Endpoint，",
            "   不能用 3.959... 直接闭合全局证明。",
            "```",
            "",
            "因此本轮没有完成全局无条件证明；但它把剩余硬点压缩为两个可审稿的具体定理，而不是继续停留在泛泛的 `U_CRT` 常数优化。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lowmod-input",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json",
    )
    parser.add_argument(
        "--tight-input",
        default="docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-stitching-feasibility-audit",
    )
    args = parser.parse_args()
    source_data = json.loads(Path(args.lowmod_input).read_text(encoding="utf-8"))
    tight_data = json.loads(Path(args.tight_input).read_text(encoding="utf-8"))
    result = build_audit(source_data, tight_data)
    out_prefix = Path(args.out_prefix)
    out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
