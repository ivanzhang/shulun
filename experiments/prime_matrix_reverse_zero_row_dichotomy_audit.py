#!/usr/bin/env python3
"""审计 q 零行向 p 阶段反推时的几何二分。

用法示例：
  python3 experiments/prime_matrix_reverse_zero_row_dichotomy_audit.py --max-p 2000

该脚本不假设 q 零行真实存在，只统计若 q 行全覆盖，则它在 p 行网格中
会落入“含完整 p 行”还是“只形成跨边界缝合零窗”两类。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def sieve_primes(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if is_prime[value]:
            for multiple in range(value * value, limit + 1, value):
                is_prime[multiple] = False
    return [value for value in range(2, limit + 1) if is_prime[value]]


def classify_q_row(p: int, q: int, row: int) -> dict:
    """分类一个假想 q 零行在 p 网格中的形态。"""
    gap = q - p
    start_minus_one = (row - 1) * q
    offset = start_minus_one % p
    p_row_start = start_minus_one // p + 1
    contains_full_p_row = offset >= p - gap
    full_p_row = p_row_start + 1 if contains_full_p_row else None
    core_row = row * q <= p * p
    return {
        "q_row": row,
        "offset_mod_p": offset,
        "core_row": core_row,
        "contains_full_p_row": contains_full_p_row,
        "full_p_row": full_p_row,
        "full_p_row_inside_p_square": bool(
            contains_full_p_row and full_p_row is not None and full_p_row <= p
        ),
        "suffix_length": p - offset,
        "prefix_length": offset + gap,
    }


def audit(max_p: int) -> dict:
    """执行几何二分审计。"""
    primes = sieve_primes(max_p + 100)
    prime_pairs = [
        (p, primes[index + 1])
        for index, p in enumerate(primes[:-1])
        if p >= 3 and p <= max_p
    ]
    records = []
    totals = {
        "q_row_count": 0,
        "core_q_row_count": 0,
        "direct_full_p_row_count": 0,
        "core_direct_full_p_row_count": 0,
        "seam_only_count": 0,
        "core_seam_only_count": 0,
    }
    for p, q in prime_pairs:
        rows = [classify_q_row(p, q, row) for row in range(2, q)]
        q_count = len(rows)
        core_rows = [row for row in rows if row["core_row"]]
        direct = [row for row in rows if row["contains_full_p_row"]]
        core_direct = [row for row in core_rows if row["contains_full_p_row"]]
        seam_only = [row for row in rows if not row["contains_full_p_row"]]
        core_seam = [row for row in core_rows if not row["contains_full_p_row"]]
        for key, value in [
            ("q_row_count", q_count),
            ("core_q_row_count", len(core_rows)),
            ("direct_full_p_row_count", len(direct)),
            ("core_direct_full_p_row_count", len(core_direct)),
            ("seam_only_count", len(seam_only)),
            ("core_seam_only_count", len(core_seam)),
        ]:
            totals[key] += value
        records.append(
            {
                "p": p,
                "q": q,
                "gap": q - p,
                "q_row_count": q_count,
                "core_q_row_count": len(core_rows),
                "direct_full_p_row_count": len(direct),
                "core_direct_full_p_row_count": len(core_direct),
                "seam_only_count": len(seam_only),
                "core_seam_only_count": len(core_seam),
                "direct_ratio": len(direct) / q_count if q_count else None,
                "core_direct_ratio": len(core_direct) / len(core_rows)
                if core_rows
                else None,
                "sample_seam_rows": core_seam[:5],
            }
        )
    worst_core_seam = sorted(
        records,
        key=lambda row: (
            row["core_seam_only_count"] / row["core_q_row_count"]
            if row["core_q_row_count"]
            else 0
        ),
        reverse=True,
    )[:20]
    return {
        "parameters": {"max_p": max_p},
        "summary": {
            **totals,
            "direct_ratio": totals["direct_full_p_row_count"]
            / totals["q_row_count"],
            "core_direct_ratio": totals["core_direct_full_p_row_count"]
            / totals["core_q_row_count"],
            "seam_only_ratio": totals["seam_only_count"] / totals["q_row_count"],
            "core_seam_only_ratio": totals["core_seam_only_count"]
            / totals["core_q_row_count"],
        },
        "worst_core_seam_records": worst_core_seam,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# q 零行反推 p 阶段的几何二分审计",
        "",
        "**状态：** `geometric_reverse_dichotomy_not_a_proof`",
        "",
        "## 总结",
        "",
        f"- q 行样本数：`{summary['q_row_count']}`。",
        f"- 核心区 q 行样本数：`{summary['core_q_row_count']}`。",
        f"- 直接包含完整 p 行比例：`{summary['direct_ratio']}`。",
        f"- 核心区直接包含完整 p 行比例：`{summary['core_direct_ratio']}`。",
        f"- 仅形成缝合零窗比例：`{summary['seam_only_ratio']}`。",
        f"- 核心区仅形成缝合零窗比例：`{summary['core_seam_only_ratio']}`。",
        "",
        "## 解释",
        "",
        "若 `q=p+g`，q 行起点在 p 网格中的偏移为",
        "",
        "\\[",
        "a_s=(s-1)q\\bmod p=(s-1)g\\bmod p.",
        "\\]",
        "",
        "假想 q 零行若满足 `a_s>=p-g`，则它包含一个完整 p 对齐零行；若 `a_s<p-g`，则它只给出相邻两个 p 行的后缀/前缀缝合零窗。后者不能由 `Row(p)` 直接排除。",
        "",
        "## 核心区缝合比例最高样本",
        "",
        "| p | q | gap | core q rows | core direct | core seam | core direct ratio |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["worst_core_seam_records"]:
        lines.append(
            "| {p} | {q} | {gap} | {core} | {direct} | {seam} | {ratio} |".format(
                p=row["p"],
                q=row["q"],
                gap=row["gap"],
                core=row["core_q_row_count"],
                direct=row["core_direct_full_p_row_count"],
                seam=row["core_seam_only_count"],
                ratio=(
                    "NA"
                    if row["core_direct_ratio"] is None
                    else f"{row['core_direct_ratio']:.6f}"
                ),
            )
        )
    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "反推路线的正确版本是：",
            "",
            "```text",
            "q 零行",
            "=> 旧 p 筛长度 q 零窗",
            "=> 完整 p 对齐零行 或 p 缝合零窗",
            "```",
            "",
            "因此，若 induction hypothesis 只含 `Row(p)`，只能排除第一支；第二支必须由 `SeamSafe/ASB/PDEC-or-SAE` 排除。直接从 q 零行反推出 p 方阵零行并不成立。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-reverse-zero-row-dichotomy-audit",
    )
    args = parser.parse_args()
    result = audit(args.max_p)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
