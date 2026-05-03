#!/usr/bin/env python3
"""审计 CRT 镜像零行能否递归反推到更小方阵。

用法示例：
  python3 experiments/prime_matrix_recursive_mirror_descent_audit.py
  python3 experiments/prime_matrix_recursive_mirror_descent_audit.py --max-top-p 19

本脚本检验一个自然但需要严格区分层级的想法：

  上层 q 方阵零行
  => 旧 p-筛长度 q 零窗
  => 旧 p-筛 CRT 周期内零行成镜像偶数
  => 是否能继续递归反推出更小 p' 方阵内也有零行？

审计重点：
1. 全 CRT 周期零行与早期方阵零行不是同一对象；
2. 剥去最大根基素数后，零行可能被“复活洞”打断；
3. 行宽从 q 变为 p' 时，相位方程改变，不能直接投影；
4. 镜像偶性是同一周期内的反射事实，不是跨层下降定理。
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


def build_masks(width: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算根基素数在给定行宽下的覆盖列掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        if width % prime == 0:
            # 非平凡列 1..width-1 不会被 width 的同素因子统一覆盖。
            residues = [0] * prime
            for col in range(1, width):
                for row_residue in range(prime):
                    if ((row_residue - 1) * width + col) % prime == 0:
                        residues[row_residue] |= 1 << (col - 1)
            masks[prime] = residues
            continue
        inverse = pow(width, -1, prime)
        residues = [0] * prime
        for col in range(1, width):
            row_residue = (1 - col * inverse) % prime
            residues[row_residue] |= 1 << (col - 1)
        masks[prime] = residues
    return masks


def row_cover_mask(row: int, masks: dict[int, list[int]], full_mask: int) -> int:
    """返回一行的覆盖列掩码。"""
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            break
    return mask


def zero_rows_for_period(base_h: int, width: int) -> dict[str, Any]:
    """扫描 `<=base_h` 根基素数在给定宽度下的完整行周期零行。"""
    base_primes = primes_upto(base_h)
    period = prod(base_primes) if base_primes else 1
    full_mask = (1 << (width - 1)) - 1
    masks = build_masks(width, base_primes)
    zero_rows: list[int] = []
    for row in range(1, period + 1):
        if row_cover_mask(row, masks, full_mask) == full_mask:
            zero_rows.append(row)
    zero_set = set(zero_rows)
    mirror_ok = all(period - row + 1 in zero_set for row in zero_rows)
    early_rows = [row for row in zero_rows if 2 <= row <= width]
    return {
        "base_h": base_h,
        "width": width,
        "period": period,
        "zero_count": len(zero_rows),
        "zero_count_even": len(zero_rows) % 2 == 0,
        "mirror_ok": mirror_ok,
        "first_zero": zero_rows[0] if zero_rows else None,
        "early_width_rows": early_rows,
        "first_zero_rows": zero_rows[:8],
        "last_zero_rows": zero_rows[-8:],
        "_zero_rows": zero_rows,
    }


def actual_matrix_zero_rows(width: int) -> dict[str, Any]:
    """检查实际 `width×width` 方阵的早期行是否为零行。"""
    base_primes = primes_upto(width - 1)
    full_mask = (1 << (width - 1)) - 1
    masks = build_masks(width, base_primes)
    zero_rows = [
        row
        for row in range(2, width + 1)
        if row_cover_mask(row, masks, full_mask) == full_mask
    ]
    return {
        "width": width,
        "base_h": base_primes[-1] if base_primes else None,
        "matrix_zero_rows_2_to_width": zero_rows,
        "has_matrix_zero_row": bool(zero_rows),
    }


def representative(row: int, period: int) -> int:
    """把行号规范到 `1..period`。"""
    return ((row - 1) % period) + 1


def audit_pair(p: int, q: int) -> dict[str, Any]:
    """审计一个相邻素数对的递归镜像下降情况。"""
    base_chain = list(reversed(primes_upto(p)))
    period_data = {
        base_h: zero_rows_for_period(base_h, q)
        for base_h in base_chain
    }
    descent_rows = []
    for index, base_h in enumerate(base_chain):
        current = period_data[base_h]
        lower_h = base_chain[index + 1] if index + 1 < len(base_chain) else None
        survives_lower = None
        added_by_current_layer = None
        if lower_h is not None:
            lower = period_data[lower_h]
            lower_zero_residues = {
                representative(row, lower["period"])
                for row in lower["_zero_rows"]
            }
            survives_lower = sum(
                1
                for row in current["_zero_rows"]
                if representative(row, lower["period"]) in lower_zero_residues
            )
            added_by_current_layer = current["zero_count"] - survives_lower
        descent_rows.append(
            {
                "base_h": base_h,
                "width_fixed_at_q": q,
                "period": current["period"],
                "zero_count": current["zero_count"],
                "zero_count_even": current["zero_count_even"],
                "mirror_ok": current["mirror_ok"],
                "first_zero": current["first_zero"],
                "early_q_square_zero_rows": current["early_width_rows"],
                "survives_after_peeling_to_lower_h": survives_lower,
                "created_by_current_layer": added_by_current_layer,
                "first_zero_rows": current["first_zero_rows"],
            }
        )
    actual_matrices = [
        actual_matrix_zero_rows(width)
        for width in reversed(primes_upto(q))
        if width >= 5
    ]
    return {
        "p": p,
        "q": q,
        "gap": q - p,
        "top_old_period_zero_count": period_data[p]["zero_count"],
        "top_old_period_first_zero": period_data[p]["first_zero"],
        "top_old_period_early_q_rows": period_data[p]["early_width_rows"],
        "descent_rows_fixed_width_q": descent_rows,
        "actual_smaller_matrix_zero_rows": actual_matrices,
    }


def build(max_top_p: int) -> dict[str, Any]:
    """构造递归镜像下降审计。"""
    primes = primes_upto(max_top_p + 20)
    pairs = [
        (p, primes[index + 1])
        for index, p in enumerate(primes[:-1])
        if 5 <= p <= max_top_p
    ]
    pair_results = [audit_pair(p, q) for p, q in pairs]
    return {
        "status": "recursive_mirror_descent_does_not_force_smaller_matrix_zero_row",
        "parameters": {"max_top_p": max_top_p, "pairs": pairs},
        "summary": {
            "pair_count": len(pair_results),
            "pairs_with_top_full_period_zero_rows": [
                {
                    "p": row["p"],
                    "q": row["q"],
                    "zero_count": row["top_old_period_zero_count"],
                    "first_zero": row["top_old_period_first_zero"],
                    "early_q_rows": row["top_old_period_early_q_rows"],
                }
                for row in pair_results
                if row["top_old_period_zero_count"]
            ],
            "pairs_with_actual_smaller_matrix_zero_rows": [
                {
                    "p": row["p"],
                    "q": row["q"],
                    "actual": [
                        item
                        for item in row["actual_smaller_matrix_zero_rows"]
                        if item["has_matrix_zero_row"]
                    ],
                }
                for row in pair_results
                if any(
                    item["has_matrix_zero_row"]
                    for item in row["actual_smaller_matrix_zero_rows"]
                )
            ],
        },
        "pairs": pair_results,
        "review_conclusion": [
            "同一层完整 CRT 周期内的镜像偶性严格成立，但它只约束该层零行集合。",
            "从 `<=p` 筛剥到 `<=p'` 筛会产生复活洞；零行不单调向下传递。",
            "即使较低筛层在固定宽度 q 的完整周期内有零行，也不等于较低宽度 p' 的方阵内有零行。",
            "样本中存在完整周期零行，但所有实际较小方阵早期行均无零行；因此递归镜像偶性不能推出有限小 p 矛盾。",
            "可保留路线仍是早期 q 零窗的 seam-window/PDEC/SAE 排斥。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# CRT 镜像零行递归下降审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        "## 总结",
        "",
        f"- 相邻素数对数量：`{summary['pair_count']}`。",
        f"- 有旧周期零行的顶层样本：`{summary['pairs_with_top_full_period_zero_rows']}`。",
        f"- 实际较小方阵早期零行样本：`{summary['pairs_with_actual_smaller_matrix_zero_rows']}`。",
        "",
        "## 关键判断",
        "",
        "递归镜像反推不能直接闭合，原因有三层：",
        "",
        "1. **全周期不等于方阵窗口。** 旧 `p`-筛完整 CRT 周期可有零行，但首个零行通常远在 `q×q` 方阵窗口之后。",
        "2. **剥层不单调。** 从 `<=p` 筛剥到 `<=p'` 筛会移除标签 `p`，被 `p` 独占覆盖的列会复活成洞。",
        "3. **宽度不守恒。** 固定宽度 `q` 下的低层零行方程与实际 `p'×p'` 方阵的宽度 `p'` 方程不同，不能直接投影。",
        "",
        "## 顶层样本表",
        "",
        "| p | q | top zero count | top first zero | early q rows | actual smaller matrix zeros |",
        "|---:|---:|---:|---:|---|---|",
    ]
    for row in result["pairs"]:
        actual_bad = [
            item
            for item in row["actual_smaller_matrix_zero_rows"]
            if item["has_matrix_zero_row"]
        ]
        lines.append(
            "| {p} | {q} | {count} | {first} | `{early}` | `{actual}` |".format(
                p=row["p"],
                q=row["q"],
                count=row["top_old_period_zero_count"],
                first=row["top_old_period_first_zero"],
                early=row["top_old_period_early_q_rows"],
                actual=actual_bad,
            )
        )
    lines.extend(
        [
            "",
            "## 典型下降链",
            "",
            "下面列出最大样本的固定宽度 `q` 下降链。`created_by_current_layer` 表示该层最大根基素数补上的零行数；",
            "这些行在剥去该素数后不再是零行。",
            "",
            "| base h | width q | period | zero count | first zero | early q rows | survives after peel | created by h |",
            "|---:|---:|---:|---:|---:|---|---:|---:|",
        ]
    )
    if result["pairs"]:
        largest = result["pairs"][-1]
        for item in largest["descent_rows_fixed_width_q"]:
            lines.append(
                "| {h} | {q} | {period} | {count} | {first} | `{early}` | {survives} | {created} |".format(
                    h=item["base_h"],
                    q=item["width_fixed_at_q"],
                    period=item["period"],
                    count=item["zero_count"],
                    first=item["first_zero"],
                    early=item["early_q_square_zero_rows"],
                    survives=item["survives_after_peeling_to_lower_h"],
                    created=item["created_by_current_layer"],
                )
            )
    lines.extend(
        [
            "",
            "## 可保留的证明形式",
            "",
            "可用路线不是“镜像偶性递归推出小方阵零行”，而是：",
            "",
            "```text",
            "q 方阵零行",
            "=> 旧 p-筛极早 q 零窗",
            "=> 完整 p 对齐零行 或 缝合零窗",
            "=> 完整行支由 Row(p) 排斥；缝合支进入 PDEC/SAE/端点缺陷。",
            "```",
            "",
            "所以下一硬点仍是早期缝合零窗的结构排斥。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-top-p", type=int, default=19)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=DOCS / "prime-matrix-recursive-mirror-descent-audit",
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
