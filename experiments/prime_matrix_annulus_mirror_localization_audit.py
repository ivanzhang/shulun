#!/usr/bin/env python3
"""审计 q 方阵环带零行与 CRT 镜像落点。

用法示例：
  python3 experiments/prime_matrix_annulus_mirror_localization_audit.py

本脚本针对一个更细的递归反推想法：

  若 q 方阵有零行且旧 p 方阵无零行，零行是否必须落在 p^2 与 q^2 之间？
  若落在该环带，其镜像是否会进入更小素数方阵，从而递归矛盾？

审计区分两个不同“镜像”：
1. CRT 零同余镜像 n -> -n mod M_p。它保持小素数零同余覆盖，但落在 CRT 周期尾部；
2. 终端反射 n -> q^2-n。它落到早期小区间，但把零同余类变为 q^2 mod ell 的非零类，
   因而不是小方阵零行。
"""

from __future__ import annotations

import argparse
import json
from math import prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 `limit` 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def classify_q_row_against_p_grid(p: int, q: int, row: int) -> dict[str, Any]:
    """分类 q 行相对 p 网格是完整 p 行支还是缝合支。"""
    gap = q - p
    start_minus_one = (row - 1) * q
    offset = start_minus_one % p
    contains_full_p_row = offset == 0 or offset >= p - gap
    return {
        "row": row,
        "offset_mod_p": offset,
        "contains_full_p_row": contains_full_p_row,
        "type": "direct_full_p_row" if contains_full_p_row else "seam_window",
    }


def row_nontrivial_interval(q: int, row: int) -> tuple[int, int]:
    """返回 q 方阵第 row 行非平凡列对应的整数闭区间。"""
    return (row - 1) * q + 1, row * q - 1


def annulus_relation(p: int, q: int, row: int) -> str:
    """判断 q 行非平凡部分与 p^2 的关系。"""
    start, end = row_nontrivial_interval(q, row)
    if end <= p * p:
        return "inside_p_square"
    if start > p * p:
        return "wholly_annulus"
    return "crosses_p_square_boundary"


def crt_zero_mirror_row(period: int, row: int) -> int:
    """同一固定宽度下保持零同余覆盖的 CRT 行反射。"""
    return period - row + 1


def terminal_reflection_interval(q: int, row: int) -> tuple[int, int]:
    """返回 n -> q^2-n 后的 m 区间。"""
    start, end = row_nontrivial_interval(q, row)
    return q * q - end, q * q - start


def is_actual_matrix_zero_row(width: int, row: int) -> bool:
    """检查给定行号在实际 `width×width` 方阵中是否为零行。"""
    if not (2 <= row <= width):
        return False
    base_primes = primes_upto(width - 1)
    if not base_primes:
        return False
    full_mask = (1 << (width - 1)) - 1
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        if width % prime == 0:
            residues = [0] * prime
            for col in range(1, width):
                for row_residue in range(prime):
                    if ((row_residue - 1) * width + col) % prime == 0:
                        residues[row_residue] |= 1 << (col - 1)
            masks[prime] = residues
        else:
            inverse = pow(width, -1, prime)
            residues = [0] * prime
            for col in range(1, width):
                row_residue = (1 - col * inverse) % prime
                residues[row_residue] |= 1 << (col - 1)
            masks[prime] = residues
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            return True
    return False


def audit_pair(p: int, q: int) -> dict[str, Any]:
    """审计一个相邻素数对。"""
    base_primes = primes_upto(p)
    period = prod(base_primes)
    lower_primes = primes_upto(p - 1)
    row_records = []
    for row in range(2, q + 1):
        relation = annulus_relation(p, q, row)
        classification = classify_q_row_against_p_grid(p, q, row)
        crt_mirror = crt_zero_mirror_row(period, row)
        lower_representatives = []
        for lower in reversed(lower_primes):
            lower_period = prod(primes_upto(lower))
            representative = ((crt_mirror - 1) % lower_period) + 1
            lower_representatives.append(
                {
                    "lower_base": lower,
                    "period": lower_period,
                    "mirror_representative": representative,
                    "inside_lower_matrix_rows": 2 <= representative <= lower,
                    "actual_lower_width_zero_row": is_actual_matrix_zero_row(
                        lower,
                        representative,
                    ),
                }
            )
        terminal_start, terminal_end = terminal_reflection_interval(q, row)
        row_records.append(
            {
                **classification,
                "nontrivial_interval": row_nontrivial_interval(q, row),
                "annulus_relation": relation,
                "crt_zero_mirror_row_in_Mp": crt_mirror,
                "crt_mirror_tail_distance": period - crt_mirror,
                "terminal_q_square_reflection_interval": [terminal_start, terminal_end],
                "terminal_reflection_is_zero_class": False,
                "terminal_reflection_bad_class": "q^2 mod ell, not 0 mod ell",
                "lower_mirror_hits_matrix_rows": [
                    item for item in lower_representatives if item["inside_lower_matrix_rows"]
                ],
                "lower_mirror_sample": lower_representatives[:5],
            }
        )
    inside_core = [item for item in row_records if item["annulus_relation"] == "inside_p_square"]
    core_seam = [item for item in inside_core if item["type"] == "seam_window"]
    annulus_rows = [
        item
        for item in row_records
        if item["annulus_relation"] in {"crosses_p_square_boundary", "wholly_annulus"}
    ]
    lower_hits = [
        item
        for item in annulus_rows
        if item["lower_mirror_hits_matrix_rows"]
    ]
    actual_lower_zero_hits = [
        {
            "row": item["row"],
            "hits": [
                hit
                for hit in item["lower_mirror_hits_matrix_rows"]
                if hit["actual_lower_width_zero_row"]
            ],
        }
        for item in annulus_rows
    ]
    actual_lower_zero_hits = [
        item for item in actual_lower_zero_hits if item["hits"]
    ]
    return {
        "p": p,
        "q": q,
        "period_Mp": period,
        "core_row_count": len(inside_core),
        "core_seam_not_excluded_by_Row_p": len(core_seam),
        "annulus_or_boundary_row_count": len(annulus_rows),
        "annulus_crt_mirror_row_number_hits_smaller_matrix_rows": len(lower_hits),
        "annulus_crt_mirror_actual_smaller_zero_hits": len(actual_lower_zero_hits),
        "core_seam_rows": core_seam,
        "annulus_rows": annulus_rows,
        "actual_lower_zero_hits": actual_lower_zero_hits,
    }


def build(max_top_p: int) -> dict[str, Any]:
    """构造审计报告。"""
    primes = primes_upto(max_top_p + 20)
    pairs = [
        (p, primes[index + 1])
        for index, p in enumerate(primes[:-1])
        if 5 <= p <= max_top_p
    ]
    rows = [audit_pair(p, q) for p, q in pairs]
    return {
        "status": "annulus_mirror_does_not_force_smaller_matrix_zero_row",
        "parameters": {"max_top_p": max_top_p, "pairs": pairs},
        "summary": {
            "pair_count": len(rows),
            "total_core_seam_rows_not_excluded_by_Row_p": sum(
                row["core_seam_not_excluded_by_Row_p"] for row in rows
            ),
            "total_annulus_rows": sum(row["annulus_or_boundary_row_count"] for row in rows),
            "total_annulus_crt_mirror_row_number_hits_smaller_matrix_rows": sum(
                row["annulus_crt_mirror_row_number_hits_smaller_matrix_rows"] for row in rows
            ),
            "total_annulus_crt_mirror_actual_smaller_zero_hits": sum(
                row["annulus_crt_mirror_actual_smaller_zero_hits"] for row in rows
            ),
        },
        "pairs": rows,
        "review_conclusion": [
            "旧 p 方阵无零行只排除 q 行中包含完整 p 对齐行的 direct 支，不能排除 p^2 内 seam q 零窗。",
            "保持零同余覆盖的 CRT 镜像是 n -> -n mod M_p，在行坐标为 r -> M_p-r+1，落在周期尾部而不是早期小方阵。",
            "落到早期区间的是 n -> q^2-n 的终端反射；它把 0 mod ell 改成 q^2 mod ell，成为非零类覆盖问题，不是小方阵零行。",
            "因此该路线不能直接递归推出更小素数方阵零行；可用对象仍是终端镜像块的非零类缺陷或 seam-window/PDEC/SAE。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]

    def summarize_annulus(item: dict[str, Any] | None) -> dict[str, Any] | None:
        """压缩环带行记录，避免报告塞入完整嵌套结构。"""
        if item is None:
            return None
        return {
            "row": item["row"],
            "type": item["type"],
            "interval": item["nontrivial_interval"],
            "relation": item["annulus_relation"],
            "crt_tail_distance": item["crt_mirror_tail_distance"],
            "terminal_reflection_interval": item["terminal_q_square_reflection_interval"],
            "row_number_hits": len(item["lower_mirror_hits_matrix_rows"]),
            "actual_zero_hits": sum(
                1
                for hit in item["lower_mirror_hits_matrix_rows"]
                if hit["actual_lower_width_zero_row"]
            ),
        }

    lines = [
        "# 环带零行与 CRT 镜像落点审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        "## 总结",
        "",
        f"- 相邻素数对数量：`{summary['pair_count']}`。",
        f"- `p^2` 内未被 `Row(p)` 排除的 q 缝合行数：`{summary['total_core_seam_rows_not_excluded_by_Row_p']}`。",
        f"- 穿过或落入 `(p^2,q^2)` 环带的 q 行数：`{summary['total_annulus_rows']}`。",
        f"- 环带行的 CRT 零镜像行号落入更小方阵早期行次数：`{summary['total_annulus_crt_mirror_row_number_hits_smaller_matrix_rows']}`。",
        f"- 上述落点实际成为更小方阵零行次数：`{summary['total_annulus_crt_mirror_actual_smaller_zero_hits']}`。",
        "",
        "## 关键区分",
        "",
        "1. `Row(p)` 只排除完整 `p` 对齐零行；它不排除 `p^2` 内跨两条 p 行的 q 缝合零窗。",
        "2. 保持小素数零同余覆盖的镜像是 `n -> -n mod M_p`。在固定 q 行宽下，行号变为 `r -> M_p-r+1`，这是 CRT 周期尾部，不是早期小方阵。",
        "3. `n -> q^2-n` 的确把环带映到早期小区间，但覆盖条件变成 `q^2 mod ell` 的非零类；它是终端镜像非零类问题，不是零行问题。",
        "",
        "## 样本表",
        "",
        "| p | q | core seam rows | annulus rows | row-number hits | actual zero hits | first annulus row record |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["pairs"]:
        first_annulus = summarize_annulus(row["annulus_rows"][0] if row["annulus_rows"] else None)
        lines.append(
            "| {p} | {q} | {core} | {annulus} | {hits} | {zero_hits} | `{record}` |".format(
                p=row["p"],
                q=row["q"],
                core=row["core_seam_not_excluded_by_Row_p"],
                annulus=row["annulus_or_boundary_row_count"],
                hits=row["annulus_crt_mirror_row_number_hits_smaller_matrix_rows"],
                zero_hits=row["annulus_crt_mirror_actual_smaller_zero_hits"],
                record=first_annulus,
            )
        )
    lines.extend(
        [
            "",
            "## 可保留方向",
            "",
            "这条想法的有效部分应改写为：",
            "",
            "```text",
            "q 方阵零行",
            "=> direct 完整 p 行支 或 seam 缝合支",
            "=> direct 支由 Row(p) 排除",
            "=> seam/terminal 支转入 q^2-n 非零类终端镜像块",
            "=> PDEC / SAE / 端点 CRT 缺陷。",
            "```",
            "",
            "不能写成“环带零行经镜像成为更小素数方阵零行”。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-top-p", type=int, default=31)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=DOCS / "prime-matrix-annulus-mirror-localization-audit",
    )
    args = parser.parse_args()
    result = build(args.max_top_p)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
