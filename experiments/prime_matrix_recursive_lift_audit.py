#!/usr/bin/env python3
"""相邻素数方阵递推升级审计。

用法示例：
  python3 experiments/prime_matrix_recursive_lift_audit.py
  python3 experiments/prime_matrix_recursive_lift_audit.py --max-p 2000
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-recursive-lift-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-recursive-lift-audit.md"


def sieve(n: int) -> bytearray:
    """返回素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    p = 2
    while p * p <= n:
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return flags


def primes_upto(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def first_prime_in_interval(flags: bytearray, left: int, right: int) -> int | None:
    """查找闭区间内第一个素数。"""
    left = max(left, 2)
    right = min(right, len(flags) - 1)
    for n in range(left, right + 1):
        if flags[n]:
            return n
    return None


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否包含一个完整的 p 行块。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def row_interval(width: int, row: int) -> tuple[int, int]:
    """方阵第 row 行对应的整数区间。"""
    return (row - 1) * width + 1, row * width


def analyze_pair(p: int, q: int, flags: bytearray) -> dict[str, Any]:
    """分析从 p×p 升级到 q×q 时旧核心区的行传递。"""
    old_square = p * p
    q_rows_touching_old = []
    q_rows_fully_old = []
    no_full_p_row = 0
    no_full_p_row_fully_old = 0
    no_prime = 0
    no_prime_fully_old = 0
    seam_residues: set[int] = set()
    last_old_row = (old_square - 1) // q + 1
    for q_row in range(1, last_old_row + 1):
        left, right = row_interval(q, q_row)
        clipped_right = min(right, old_square)
        if left > old_square:
            continue
        full = contains_full_p_row(p, left, clipped_right)
        prime = first_prime_in_interval(flags, left, clipped_right)
        residue = (left - 1) % p
        seam_residues.add(residue)
        if not full:
            no_full_p_row += 1
        if prime is None:
            no_prime += 1
        row = {
            "q_row": q_row,
            "left": left,
            "right": clipped_right,
            "full_q_right": right,
            "length": clipped_right - left + 1,
            "is_fully_inside_old_square": right <= old_square,
            "start_residue_mod_p": residue,
            "contains_full_p_row": full,
            "first_prime": prime,
        }
        q_rows_touching_old.append(row)
        if row["is_fully_inside_old_square"]:
            q_rows_fully_old.append(row)
            if not full:
                no_full_p_row_fully_old += 1
            if prime is None:
                no_prime_fully_old += 1

    gap = q - p
    good_full_by_residue = sum(1 for row in q_rows_touching_old if row["contains_full_p_row"])
    good_full_by_residue_fully_old = sum(1 for row in q_rows_fully_old if row["contains_full_p_row"])
    return {
        "p": p,
        "q": q,
        "gap": gap,
        "old_square": old_square,
        "q_rows_touching_old": len(q_rows_touching_old),
        "q_rows_fully_inside_old": len(q_rows_fully_old),
        "q_rows_without_full_p_row": no_full_p_row,
        "q_rows_fully_old_without_full_p_row": no_full_p_row_fully_old,
        "q_rows_without_prime_in_old_core": no_prime,
        "q_rows_fully_old_without_prime": no_prime_fully_old,
        "distinct_start_residues_mod_p": len(seam_residues),
        "full_p_row_transfer_rows": good_full_by_residue,
        "full_p_row_transfer_rows_fully_old": good_full_by_residue_fully_old,
        "full_p_row_transfer_ratio": good_full_by_residue / len(q_rows_touching_old) if q_rows_touching_old else 0.0,
        "full_p_row_transfer_ratio_fully_old": (
            good_full_by_residue_fully_old / len(q_rows_fully_old) if q_rows_fully_old else 0.0
        ),
        "sample_bad_transfer_rows": [row for row in q_rows_touching_old if not row["contains_full_p_row"]][:8],
        "sample_bad_transfer_rows_fully_old": [row for row in q_rows_fully_old if not row["contains_full_p_row"]][:8],
        "sample_prime_rows": [row for row in q_rows_touching_old if row["first_prime"] is not None][:8],
    }


def build_audit(max_p: int) -> dict[str, Any]:
    """生成相邻素数递推审计。"""
    primes = [p for p in primes_upto(max_p + 200) if p >= 3]
    max_q = primes[-1]
    flags = sieve(max_q * max_q)
    cases = []
    for p, q in zip(primes, primes[1:]):
        if p > max_p:
            break
        cases.append(analyze_pair(p, q, flags))
    worst_transfer = max(cases, key=lambda case: case["q_rows_fully_old_without_full_p_row"], default=None)
    return {
        "certificate_type": "prime_matrix_recursive_lift_audit",
        "status": "recursive_lift_route_analysis_not_a_proof",
        "parameters": {"max_p": max_p},
        "case_count": len(cases),
        "cases": cases,
        "worst_transfer_case": worst_transfer,
        "review_conclusion": (
            "旧核心中的实际素数在升级筛后不会变成合数；但 p 行命题不能直接推出 q 行命题，"
            "因为 q 行边界与 p 行边界发生漂移，多数 q 行不包含完整 p 行。"
            "递推路线需要额外的滑动窗口/缝合行引理。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# 相邻素数方阵递推升级审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告审查一个新的递推思路：若 `p=p_k` 的 `p×p` 方阵行命题成立，是否可在升级到 `q=p_{k+1}` 的 `q×q` 方阵时，直接继承旧核心 `[1,p^2]` 的行素数存在性，只需处理 `(p^2,q^2]` 新区间。",
        "",
        "## 1. 可以保留的正确部分",
        "",
        "- 旧核心 `[1,p^2]` 中已经确定为素数的位置，升级到 `q` 后不会变成合数。",
        "- 新素数 `q` 的整除线在 `q×q` 方阵中是第 `q` 列；低于 `p^2` 的多数 `q` 倍数已带有较小互补因子，真正新增的筛除压力主要从旧平方边界之后开始。",
        "- 因此“递推剥离旧核心、重点处理 annulus `(p^2,q^2]`”是合理的结构视角。",
        "",
        "## 2. 不能直接推出的关键点",
        "",
        "`p` 行命题只保证每个 `p` 对齐行块",
        "",
        "\\[",
        "I_t^{(p)}=[(t-1)p+1,tp]",
        "\\]",
        "",
        "含素数；而升级后需要检查的是 `q` 对齐行块",
        "",
        "\\[",
        "J_s^{(q)}=[(s-1)q+1,sq].",
        "\\]",
        "",
        "即使 `J_s^{(q)}\\subset[1,p^2]`，它通常也不包含完整的 `p` 行。设 `q=p+g`，`A=(s-1)q`。`J_s^{(q)}` 包含完整 `p` 行当且仅当下一个 `p` 倍数距 `A` 不超过 `g`：",
        "",
        "\\[",
        "(-A\\bmod p)\\le g.",
        "\\]",
        "",
        "由于 `g` 通常远小于 `p`，多数 `q` 行只是跨过两个相邻 `p` 行的尾部和头部，不能从“每个 `p` 行有一个素数”直接继承。",
        "",
        "## 3. 样本审计",
        "",
        "| p | q | gap | 完全位于旧核心的q行 | 不含完整p行 | 完整p行传递比例 | 完整旧核心q行无实际素数 |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for case in audit["cases"][:20]:
        lines.append(
            f"| {case['p']} | {case['q']} | {case['gap']} | {case['q_rows_fully_inside_old']} | "
            f"{case['q_rows_fully_old_without_full_p_row']} | {case['full_p_row_transfer_ratio_fully_old']:.3f} | "
            f"{case['q_rows_fully_old_without_prime']} |"
        )
    worst = audit["worst_transfer_case"]
    if worst:
        lines += [
            "",
            "最坏传递样本：",
            "",
            f"- `p={worst['p']}, q={worst['q']}, gap={worst['gap']}`。",
            f"- 完全位于旧核心的 `q` 行数：`{worst['q_rows_fully_inside_old']}`。",
            f"- 不含完整 `p` 行的完整旧核心 `q` 行数：`{worst['q_rows_fully_old_without_full_p_row']}`。",
            f"- 完整 `p` 行传递比例：`{worst['full_p_row_transfer_ratio_fully_old']:.3f}`。",
            "",
            "这些“不含完整 `p` 行”的行就是递推路线的缝合硬点。",
        ]
    lines += [
        "",
        "## 4. 正确的递推命题应如何加强",
        "",
        "递推路线不能只假设 `Row(p)`。需要加强为一个缝合窗口命题：对每个由 `q` 行边界切出的旧核心窗口",
        "",
        "\\[",
        "J_s^{(q)}\\cap[1,p^2]",
        "\\]",
        "",
        "必须含有旧核心素数。等价地，需要证明：每个跨越两个相邻 `p` 行的“尾段+头段”窗口含素数。",
        "",
        "可定义加强命题 `Seam(p,q)`：对所有相关 `s`，",
        "",
        "\\[",
        "J_s^{(q)}\\cap[1,p^2]\\cap\\mathbb P\\ne\\varnothing.",
        "\\]",
        "",
        "若有",
        "",
        "```text",
        "Row(p) + Seam(p,q) + Annulus(p,q) => Row(q),",
        "```",
        "",
        "则递推结构成立。其中 `Annulus(p,q)` 只处理 `(p^2,q^2]` 中的新行段。",
        "",
        "## 5. 对你的斜线覆盖观察的严格化",
        "",
        "- 新素数 `q` 在 `q×q` 方阵中主要表现为第 `q` 列的整除线。",
        "- 对旧核心 `[1,p^2]`，真实素数不会被新增小素数筛消去；但行窗口重分块后，旧素数可能落在新行窗口之外。",
        "- 因此“新斜线不能穿过旧已定素数”不是主要障碍；主要障碍是 `q` 行窗口是否捕获旧素数。",
        "- 一旦 `Seam(p,q)` 成立，新区间 `(p^2,q^2]` 的覆盖压力确实比全局重证更局部，可作为递推剥离路线的核心优势。",
        "",
        "## 6. 审稿结论",
        "",
        audit["review_conclusion"],
        "",
        "下一步若沿此路线推进，应优先证明 `Seam(p,q)`，而不是直接处理整个 `q×q` 方阵。`Seam` 的本质是滑动长度约 `q` 的旧核心素数窗口命题；它比原始行命题强，但比全局重新证明更局部。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
