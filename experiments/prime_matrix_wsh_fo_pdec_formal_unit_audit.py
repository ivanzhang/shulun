#!/usr/bin/env python3
"""审计 FO-PDEC 阈值账本的 formal unit 一致性。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_formal_unit_audit.py

目的：
  PDEC 证书中的相位向量 g(t) 必须来自同一个正式坏窗集合或多重集合。
  本脚本检查当前最佳投影 ell=199 的强阈值是否来自同一 formal unit，
  还是来自跨 q 层、嵌套块或物理候选重复的诊断性拼接。

注意：
  这是审稿级防误用审计，不是全局无条件证明。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Iterable


Equation = dict[str, object]


def best_fourier_projection(rows: Iterable[Equation]) -> dict | None:
    """返回给定方程集合中最强的单因子 Fourier 投影。"""
    by_factor: defaultdict[int, Counter[int]] = defaultdict(Counter)
    for row in rows:
        by_factor[int(row["explaining_factor"])][int(row["target_residue"])] += 1
    best: dict | None = None
    for factor, counts in by_factor.items():
        best_frequency = 0
        best_value = 0.0
        for frequency in range(1, factor):
            total = 0j
            for residue, load in counts.items():
                total += load * cmath.exp(2j * math.pi * frequency * residue / factor)
            magnitude = abs(total)
            if magnitude > best_value:
                best_frequency = frequency
                best_value = magnitude
        mass = sum(counts.values())
        candidate = {
            "factor": factor,
            "best_frequency": best_frequency,
            "max_fourier": best_value,
            "mass": mass,
            "support_size": len(counts),
            "mass_defect": mass - best_value,
            "top_residues": [
                {"residue": residue, "load": load}
                for residue, load in counts.most_common()
            ],
        }
        if best is None or (
            candidate["max_fourier"],
            candidate["mass"],
            candidate["factor"],
        ) > (best["max_fourier"], best["mass"], best["factor"]):
            best = candidate
    return best


def unique_rows(
    rows: Iterable[Equation],
    dedupe_key: Callable[[Equation], tuple] | None,
) -> list[Equation]:
    """按给定键去重；键为空时保持原多重集合。"""
    if dedupe_key is None:
        return list(rows)
    seen: set[tuple] = set()
    result: list[Equation] = []
    for row in rows:
        key = dedupe_key(row)
        if key in seen:
            continue
        seen.add(key)
        result.append(row)
    return result


def group_mode(
    equations: list[Equation],
    *,
    name: str,
    status: str,
    group_key: Callable[[Equation], tuple],
    dedupe_key: Callable[[Equation], tuple] | None = None,
) -> dict:
    """计算一种 formal-unit 口径下的最强单元投影。"""
    groups: defaultdict[tuple, list[Equation]] = defaultdict(list)
    for equation in equations:
        groups[group_key(equation)].append(equation)

    unit_rows = []
    for key, rows in sorted(groups.items(), key=lambda item: item[0]):
        reduced = unique_rows(rows, dedupe_key)
        best = best_fourier_projection(reduced)
        unit_rows.append(
            {
                "unit_key": list(key),
                "raw_equations": len(rows),
                "effective_equations": len(reduced),
                "best_projection": best,
            }
        )
    valid = [row for row in unit_rows if row["best_projection"]]
    best_unit = max(
        valid,
        key=lambda row: (
            row["best_projection"]["max_fourier"],
            row["best_projection"]["mass"],
            row["effective_equations"],
        ),
        default=None,
    )
    return {
        "mode": name,
        "status": status,
        "unit_count": len(unit_rows),
        "best_unit": best_unit,
        "units": unit_rows,
    }


def duplicate_classes(equations: list[Equation], factor: int) -> list[dict]:
    """分类最佳投影中的重复来源。"""
    rows = [row for row in equations if int(row["explaining_factor"]) == factor]

    def bucket(key_fn: Callable[[Equation], tuple]) -> list[tuple[tuple, list[Equation]]]:
        buckets: defaultdict[tuple, list[Equation]] = defaultdict(list)
        for row in rows:
            buckets[key_fn(row)].append(row)
        return [(key, value) for key, value in buckets.items() if len(value) > 1]

    exact_coordinate = bucket(
        lambda row: (
            row["q"],
            row["source_row"],
            row["candidate_row"],
            row["column"],
            row["offset"],
            row["candidate"],
            row["explaining_factor"],
            row["target_residue"],
        )
    )
    physical = bucket(lambda row: (row["candidate"], row["explaining_factor"]))

    classes = []
    for key, items in exact_coordinate:
        classes.append(
            {
                "type": "nested_same_formal_coordinate",
                "key": list(key),
                "multiplicity": len(items),
                "sources": source_rows(items),
                "proof_obligation": "需要 NestedBlock-Independence；否则只能按一个正式坐标计数。",
            }
        )
    exact_keys = {tuple(item["key"]) for item in classes}
    for key, items in physical:
        q_layers = sorted({int(item["q"]) for item in items})
        residues = sorted({int(item["target_residue"]) for item in items})
        if len(q_layers) > 1:
            classes.append(
                {
                    "type": "cross_level_same_physical_candidate",
                    "key": list(key),
                    "multiplicity": len(items),
                    "q_layers": q_layers,
                    "target_residues": residues,
                    "sources": source_rows(items),
                    "proof_obligation": "需要 CrossLevel-Stitching；否则不能把不同 q 层拼成同一 PDEC 向量。",
                }
            )
        elif not any(tuple(source_key(item)) in exact_keys for item in items):
            classes.append(
                {
                    "type": "same_physical_candidate",
                    "key": list(key),
                    "multiplicity": len(items),
                    "q_layers": q_layers,
                    "target_residues": residues,
                    "sources": source_rows(items),
                    "proof_obligation": "需要证明物理重复对应不同独立约束；否则去重。",
                }
            )
    return classes


def source_key(row: Equation) -> tuple:
    """返回与 exact_coordinate 相同的键。"""
    return (
        row["q"],
        row["source_row"],
        row["candidate_row"],
        row["column"],
        row["offset"],
        row["candidate"],
        row["explaining_factor"],
        row["target_residue"],
    )


def source_rows(rows: Iterable[Equation]) -> list[dict]:
    """压缩输出来源行。"""
    result = []
    for row in rows:
        result.append(
            {
                "block_index": row["block_index"],
                "offset_row_index": row["offset_row_index"],
                "p": row["p"],
                "q": row["q"],
                "source_row": row["source_row"],
                "candidate": row["candidate"],
                "factor": row["explaining_factor"],
                "target_residue": row["target_residue"],
            }
        )
    return result


def build_audit(source: dict) -> dict:
    """生成 formal unit 审计。"""
    equations: list[Equation] = source["equations"]
    modes = [
        group_mode(
            equations,
            name="global_library_raw",
            status="diagnostic_only_requires_persistent_stitching",
            group_key=lambda row: ("global",),
        ),
        group_mode(
            equations,
            name="global_layer_dedup",
            status="diagnostic_only_requires_cross_level_stitching",
            group_key=lambda row: ("global",),
            dedupe_key=lambda row: (
                row["q"],
                row["candidate"],
                row["explaining_factor"],
            ),
        ),
        group_mode(
            equations,
            name="global_physical_dedup",
            status="diagnostic_only_physical_projection",
            group_key=lambda row: ("global",),
            dedupe_key=lambda row: (row["candidate"], row["explaining_factor"]),
        ),
        group_mode(
            equations,
            name="q_row_raw",
            status="single_matrix_row_raw_nested_duplicates_allowed_only_with_block_independence",
            group_key=lambda row: (row["q"], row["source_row"]),
        ),
        group_mode(
            equations,
            name="q_row_coordinate_dedup",
            status="single_matrix_row_coordinate_dedup",
            group_key=lambda row: (row["q"], row["source_row"]),
            dedupe_key=lambda row: (
                row["q"],
                row["source_row"],
                row["candidate_row"],
                row["column"],
                row["offset"],
                row["candidate"],
                row["explaining_factor"],
            ),
        ),
        group_mode(
            equations,
            name="block_local_raw",
            status="single_hall_block",
            group_key=lambda row: (row["block_index"],),
        ),
        group_mode(
            equations,
            name="offset_row_raw",
            status="single_fixed_offset_row",
            group_key=lambda row: (row["offset_row_index"],),
        ),
    ]
    best_global = modes[0]["best_unit"]["best_projection"]
    return {
        "status": "finite_fo_pdec_formal_unit_audit_not_global_proof",
        "summary": {
            "global_raw_best": best_global,
            "accepted_single_unit_best": max(
                (
                    mode["best_unit"]["best_projection"]["max_fourier"]
                    for mode in modes
                    if mode["mode"]
                    in {
                        "q_row_coordinate_dedup",
                        "block_local_raw",
                        "offset_row_raw",
                    }
                    and mode["best_unit"]
                ),
                default=0.0,
            ),
            "hard_obligation": "FormalUnit-Stitching 或 NestedBlock-Independence；否则 global_raw 强阈值只是诊断聚合。",
            "duplicate_classes_for_best_factor": duplicate_classes(
                equations, int(best_global["factor"])
            ),
        },
        "modes": modes,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# FO-PDEC Formal Unit 一致性审计",
        "",
        "**状态：** `finite_fo_pdec_formal_unit_audit_not_global_proof`",
        "",
        "本文档审计当前 `ell=199` 强阈值是否可作为正式 `PDEC` 向量使用。核心规则是：`PDEC` 的 `g(t)` 必须来自同一个坏窗集合或多重集合；跨 `q` 层、嵌套块或物理重复若要合并，必须先给出独立性或持久拼接引理。",
        "",
        "## 口径摘要",
        "",
        "| mode | status | units | best unit | mass | ell | h | Fourier | support |",
        "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for mode in result["modes"]:
        best_unit = mode["best_unit"]
        if best_unit and best_unit["best_projection"]:
            projection = best_unit["best_projection"]
            unit_key = best_unit["unit_key"]
            lines.append(
                "| {mode} | `{status}` | {units} | `{unit}` | {mass} | {ell} | {h} | {fourier:.6f} | {support} |".format(
                    mode=mode["mode"],
                    status=mode["status"],
                    units=mode["unit_count"],
                    unit=unit_key,
                    mass=projection["mass"],
                    ell=projection["factor"],
                    h=projection["best_frequency"],
                    fourier=projection["max_fourier"],
                    support=projection["support_size"],
                )
            )
    lines.extend(
        [
            "",
            "## 最佳因子重复来源",
            "",
            "| type | multiplicity | key | sources | proof obligation |",
            "| --- | ---: | --- | --- | --- |",
        ]
    )
    for row in summary["duplicate_classes_for_best_factor"]:
        lines.append(
            "| `{type}` | {mult} | `{key}` | `{sources}` | {obligation} |".format(
                type=row["type"],
                mult=row["multiplicity"],
                key=row["key"],
                sources=row["sources"],
                obligation=row["proof_obligation"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "当前 `global_library_raw` 的强阈值 `3.959247567099438` 来自有限证书库的聚合：它同时使用了不同 `q` 层的方程，并且包含嵌套块的同一正式坐标重复。因此它不能直接作为单个正式反例分支的 `PDEC` 下界，除非补上以下至少一项：",
            "",
            "1. `FormalUnit-Stitching`：证明这些跨 `q` 层事件属于同一个持久坏窗族，并给出统一相位映射与计数向量；",
            "2. `NestedBlock-Independence`：证明嵌套块重复在 Hall/PDEC 对偶中代表不同独立约束行，且 `U_CRT` 上界也按同一多重集合计算；",
            "3. `SAE/Endpoint absorption`：若无法拼接或独立化，则把重复事件视为孤立端点/非持久样本并回流到 SAE/Endpoint，而不能计入强阈值。",
            "",
            "在上述接口未闭合前，`ell=199` 的强阈值只能作为硬点定位工具，不能升级为全局无条件证明。",
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
        default="docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-audit",
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
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
