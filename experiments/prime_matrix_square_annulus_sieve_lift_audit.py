#!/usr/bin/env python3
"""相邻素数平方壳层筛升级审计。

用法示例：
  python3 experiments/prime_matrix_square_annulus_sieve_lift_audit.py
  python3 experiments/prime_matrix_square_annulus_sieve_lift_audit.py --max-p 10000
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_mge3_budget_audit import MONOGRAPH, primes_from_flags, sieve, smallest_prime_factor

DEFAULT_JSON = MONOGRAPH / "prime-matrix-square-annulus-sieve-lift-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-square-annulus-sieve-lift-audit.md"


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行闭区间。"""
    return (row - 1) * width + 1, row * width


def audit_pair(p: int, q: int, prime_flags: bytearray, spf: list[int]) -> dict[str, Any]:
    """审计相邻素数 p<q 的平方壳层。"""
    left = p * p + 1
    right = q * q
    old_rough = []
    rough_composites = []
    q_multiple_rows = []
    redundant_q_multiples = []
    nonredundant_q_multiples = []

    for n in range(left, right + 1):
        if n % q == 0:
            row = {
                "n": n,
                "cofactor": n // q,
                "old_sieved": spf[n] <= p,
                "smallest_prime_factor": spf[n],
            }
            q_multiple_rows.append(row)
            if row["old_sieved"]:
                redundant_q_multiples.append(row)
            else:
                nonredundant_q_multiples.append(row)

        if spf[n] > p:
            old_rough.append(n)
            if not prime_flags[n]:
                rough_composites.append(n)

    annulus_rows = []
    partial_empty_rows = 0
    full_empty_rows = 0
    q2_only_rows = 0
    for row in range(1, q + 1):
        row_left, row_right = row_interval(q, row)
        seg_left = max(left, row_left)
        seg_right = min(right, row_right)
        if seg_left > seg_right:
            continue
        rough_in_segment = [n for n in range(seg_left, seg_right + 1) if spf[n] > p and n != q * q]
        prime_in_segment = [n for n in rough_in_segment if prime_flags[n]]
        full = seg_left == row_left and seg_right == row_right
        if not rough_in_segment:
            if full:
                full_empty_rows += 1
            else:
                partial_empty_rows += 1
        if [n for n in range(seg_left, seg_right + 1) if spf[n] > p] == [q * q]:
            q2_only_rows += 1
        annulus_rows.append(
            {
                "row": row,
                "segment_left": seg_left,
                "segment_right": seg_right,
                "full_q_row": full,
                "old_rough_excluding_q2": len(rough_in_segment),
                "prime_excluding_q2": len(prime_in_segment),
                "first_prime": None if not prime_in_segment else prime_in_segment[0],
            }
        )

    return {
        "p": p,
        "q": q,
        "gap": q - p,
        "annulus_left": left,
        "annulus_right": right,
        "annulus_length": right - left + 1,
        "old_rough_count": len(old_rough),
        "old_rough_composites": rough_composites,
        "old_rough_composite_exception_ok": rough_composites == [q * q],
        "q_multiples_in_annulus": q_multiple_rows,
        "q_multiple_count": len(q_multiple_rows),
        "redundant_q_multiple_count": len(redundant_q_multiples),
        "nonredundant_q_multiples": nonredundant_q_multiples,
        "nonredundant_q_multiples_are_q2_only": [row["n"] for row in nonredundant_q_multiples] == [q * q],
        "partial_empty_annulus_rows_excluding_q2": partial_empty_rows,
        "full_empty_annulus_rows_excluding_q2": full_empty_rows,
        "q2_only_annulus_rows": q2_only_rows,
        "annulus_rows": annulus_rows,
    }


def build_audit(max_p: int) -> dict[str, Any]:
    """生成平方壳层审计。"""
    flags = sieve((max_p + 500) ** 2)
    spf = smallest_prime_factor((max_p + 500) ** 2)
    primes = [p for p in primes_from_flags(sieve(max_p + 500)) if p >= 3]
    pairs = []
    for p, q in zip(primes, primes[1:]):
        if p > max_p:
            break
        pairs.append(audit_pair(p, q, flags, spf))

    failures = [
        row
        for row in pairs
        if not row["old_rough_composite_exception_ok"] or not row["nonredundant_q_multiples_are_q2_only"]
    ]
    full_empty = [row for row in pairs if row["full_empty_annulus_rows_excluding_q2"] > 0]
    partial_empty = [row for row in pairs if row["partial_empty_annulus_rows_excluding_q2"] > 0]
    full_rows = []
    partial_rows = []
    for pair in pairs:
        for row in pair["annulus_rows"]:
            tagged = {
                "p": pair["p"],
                "q": pair["q"],
                "row": row["row"],
                "segment_left": row["segment_left"],
                "segment_right": row["segment_right"],
                "old_rough_excluding_q2": row["old_rough_excluding_q2"],
                "prime_excluding_q2": row["prime_excluding_q2"],
                "first_prime": row["first_prime"],
            }
            if row["full_q_row"]:
                full_rows.append(tagged)
            else:
                partial_rows.append(tagged)
    return {
        "certificate_type": "prime_matrix_square_annulus_sieve_lift_audit",
        "status": "square_annulus_old_sieve_survivors_are_prime_except_q2",
        "parameters": {"max_p": max_p},
        "pair_count": len(pairs),
        "identity_failure_count": len(failures),
        "full_empty_pair_count": len(full_empty),
        "partial_empty_pair_count": len(partial_empty),
        "max_full_empty_rows": max((row["full_empty_annulus_rows_excluding_q2"] for row in pairs), default=0),
        "max_partial_empty_rows": max((row["partial_empty_annulus_rows_excluding_q2"] for row in pairs), default=0),
        "full_annulus_row_count": len(full_rows),
        "partial_annulus_row_count": len(partial_rows),
        "min_full_row_old_rough_excluding_q2": None
        if not full_rows
        else min(row["old_rough_excluding_q2"] for row in full_rows),
        "min_partial_row_old_rough_excluding_q2": None
        if not partial_rows
        else min(row["old_rough_excluding_q2"] for row in partial_rows),
        "sparsest_full_annulus_rows": sorted(full_rows, key=lambda row: row["old_rough_excluding_q2"])[:12],
        "sparsest_partial_annulus_rows": sorted(partial_rows, key=lambda row: row["old_rough_excluding_q2"])[:12],
        "worst_full_empty_pairs": sorted(full_empty, key=lambda row: row["full_empty_annulus_rows_excluding_q2"], reverse=True)[:12],
        "worst_partial_empty_pairs": sorted(
            partial_empty, key=lambda row: row["partial_empty_annulus_rows_excluding_q2"], reverse=True
        )[:12],
        "sample_pairs": pairs[:20],
        "review_conclusion": (
            "在 (p^2,q^2] 中，旧 p-筛幸存的合数唯一为 q^2；"
            "q 的新增筛线除 q^2 外均为旧筛冗余。"
            "Annulus 命题因此可改写为每个相关 q 行壳层段存在旧筛幸存者且不等于 q^2。"
        ),
    }


def fmt_row(row: dict[str, Any]) -> str:
    """格式化行片段。"""
    return f"`[{row['segment_left']},{row['segment_right']}]`"


def write_md(report: dict[str, Any], path: Path) -> None:
    """写出 Markdown 报告。"""
    params = report["parameters"]
    lines = [
        "# 相邻素数平方壳层筛升级审计",
        "",
        "**状态：** `square_annulus_old_sieve_survivors_are_prime_except_q2`",
        "",
        "本文审计从 `p=p_k` 升级到 `q=p_{k+1}` 时，平方壳层 `(p^2,q^2]` 中旧筛和新筛的关系。",
        "",
        "## 1. 参数与总账本",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- 相邻素数对数：`{report['pair_count']}`。",
        f"- 壳层幸存合数例外失败数：`{report['identity_failure_count']}`。",
        f"- 含完整壳层 q 行空段的素数对数：`{report['full_empty_pair_count']}`。",
        f"- 含边界部分壳层 q 行空段的素数对数：`{report['partial_empty_pair_count']}`。",
        f"- 最大完整空行数：`{report['max_full_empty_rows']}`。",
        f"- 最大部分空行数：`{report['max_partial_empty_rows']}`。",
        f"- 完整壳层 q 行数：`{report['full_annulus_row_count']}`。",
        f"- 完整壳层 q 行最小旧筛幸存者数：`{report['min_full_row_old_rough_excluding_q2']}`。",
        f"- 边界部分壳层 q 行最小旧筛幸存者数：`{report['min_partial_row_old_rough_excluding_q2']}`。",
        "",
        "## 2. 严格核查结论",
        "",
        "对每个相邻素数 `p<q` 和 `n∈(p^2,q^2]`，若 `n` 没有不超过 `p` 的素因子，则：",
        "",
        "```text",
        "n 是素数，或 n=q^2。",
        "```",
        "",
        "等价地，`q` 加入后在壳层中真正非冗余筛掉的旧筛幸存者只有 `q^2`。`pq` 虽然也是 `q` 的倍数，但已经被旧素数 `p` 筛掉，因此不是旧筛待定点。",
        "",
        "## 3. 样本相邻素数对",
        "",
        "| p | q | gap | annulus | old rough | rough composite exceptions | q倍数 | q非冗余倍数 | 完整空行 | 部分空行 |",
        "| ---: | ---: | ---: | --- | ---: | --- | ---: | --- | ---: | ---: |",
    ]
    for row in report["sample_pairs"]:
        lines.append(
            "| "
            f"{row['p']} | "
            f"{row['q']} | "
            f"{row['gap']} | "
            f"`[{row['annulus_left']},{row['annulus_right']}]` | "
            f"{row['old_rough_count']} | "
            f"`{row['old_rough_composites']}` | "
            f"{row['q_multiple_count']} | "
            f"`{[x['n'] for x in row['nonredundant_q_multiples']]}` | "
            f"{row['full_empty_annulus_rows_excluding_q2']} | "
            f"{row['partial_empty_annulus_rows_excluding_q2']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 完整壳层 q 行空段压力",
            "",
        ]
    )
    if report["worst_full_empty_pairs"]:
        lines.extend(["| p | q | 完整空行数 | annulus |", "| ---: | ---: | ---: | --- |"])
        for row in report["worst_full_empty_pairs"]:
            lines.append(
                "| "
                f"{row['p']} | {row['q']} | {row['full_empty_annulus_rows_excluding_q2']} | "
                f"`[{row['annulus_left']},{row['annulus_right']}]` |"
            )
    else:
        lines.append("在本次审计范围内，完整壳层 `q` 行没有出现旧筛幸存者空段。")

    if report["sparsest_full_annulus_rows"]:
        lines.extend(
            [
                "",
                "### 4.1 最稀疏完整壳层行",
                "",
                "| p | q | q行 | segment | old rough≠q² | first prime |",
                "| ---: | ---: | ---: | --- | ---: | ---: |",
            ]
        )
        for row in report["sparsest_full_annulus_rows"]:
            lines.append(
                "| "
                f"{row['p']} | "
                f"{row['q']} | "
                f"{row['row']} | "
                f"{fmt_row(row)} | "
                f"{row['old_rough_excluding_q2']} | "
                f"{row['first_prime']} |"
            )

    lines.extend(
        [
            "",
            "## 5. 审稿结论",
            "",
            "1. 用户观察中的核心正确点是：平方壳层内旧筛幸存者已经几乎完全确定为素数；唯一合数例外是 `q^2`。",
            "2. 需要修正的是：`pq` 不是新增非冗余筛除点，因为它已经被旧筛中的 `p` 删除。",
            "3. `Annulus(p,q)` 可由此改写为更清晰的非空命题：每个需要由壳层负责的 `q` 行段必须含有旧筛幸存者且不等于 `q^2`；一旦有这样的幸存者，它自动是素数。",
            "4. 这显著简化了壳层证明目标，但不自动证明行段非空；非空性仍需 CRT/端点/粗剩余论证。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    report = build_audit(args.max_p)
    args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(report, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")


if __name__ == "__main__":
    main()
