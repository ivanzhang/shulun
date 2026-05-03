#!/usr/bin/env python3
"""审计 q 阶零行向 p 阶 CRT 周期提升后的奇偶矛盾路线。

用法示例：
  python3 experiments/prime_matrix_crt_lift_parity_audit.py
  python3 experiments/prime_matrix_crt_lift_parity_audit.py --max-p 19

背景：设 q 是 p 的下一素数。本脚本检验如下候选证明链：

  q×q 方阵若有零行
  => 旧 p-筛 CRT 周期内有零行
  => q 阶 CRT 周期由 q 个旧周期组成，所以零行出现 q 次
  => 镜像刚性要求零行总数为偶数，而 q 为奇数，矛盾。

审计结论会区分三点：
1. q 非平凡列中，q 本身不覆盖任何格点，所以 q 零行确实是旧 p-筛长度 q 零窗。
2. 长度 q 零窗通常不是 p 对齐零行，只能给出“完整 p 行或缝合零窗”二分。
3. 旧 p-筛周期内的零行数本身已由镜像成偶数；放大 q 倍仍为偶数，因此没有奇偶矛盾。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
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


def next_prime(value: int) -> int:
    """返回大于 `value` 的最小素数。"""
    candidate = value + 1
    while True:
        if all(candidate % divisor for divisor in range(2, int(candidate**0.5) + 1)):
            return candidate
        candidate += 1


def build_masks(width: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算旧筛在给定行宽下的行相位覆盖列掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        inverse = pow(width, -1, prime)
        residues = [0] * prime
        for col in range(1, width):
            # (row-1)*width+col == 0 mod prime
            row_residue = (1 - col * inverse) % prime
            residues[row_residue] |= 1 << (col - 1)
        masks[prime] = residues
    return masks


def row_cover_mask(row: int, masks: dict[int, list[int]], full_mask: int) -> int:
    """返回一行被旧筛覆盖的列掩码。"""
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            break
    return mask


def classify_q_row_in_p_grid(p: int, q: int, row: int) -> dict[str, Any]:
    """判定 q 行零窗是否包含完整 p 对齐行，或只是缝合窗口。"""
    gap = q - p
    start_minus_one = (row - 1) * q
    offset = start_minus_one % p
    distance_to_p_boundary = 0 if offset == 0 else p - offset
    contains_full_p_row = distance_to_p_boundary <= gap
    p_row = start_minus_one // p + 1
    if offset != 0:
        p_row += 1
    return {
        "q_row": row,
        "offset_mod_p": offset,
        "distance_to_p_boundary": distance_to_p_boundary,
        "contains_full_p_row": contains_full_p_row,
        "forced_p_row_if_full": p_row if contains_full_p_row else None,
        "forced_p_row_inside_original_p_square": bool(contains_full_p_row and p_row <= p),
        "window_type": "full_p_row" if contains_full_p_row else "seam_window",
    }


def scan_pair(p: int, q: int) -> dict[str, Any]:
    """扫描一对相邻素数的旧 p-筛 q 行宽周期。"""
    base_primes = primes_upto(p)
    period = prod(base_primes)
    masks = build_masks(q, base_primes)
    full_mask = (1 << (q - 1)) - 1
    zero_rows: list[int] = []
    survivor_hist = Counter()

    for row in range(1, period + 1):
        cover_mask = row_cover_mask(row, masks, full_mask)
        survivor_count = (q - 1) - cover_mask.bit_count()
        survivor_hist[survivor_count] += 1
        if survivor_count == 0:
            zero_rows.append(row)

    zero_set = set(zero_rows)
    mirror_ok = all(period - row + 1 in zero_set for row in zero_rows)
    q_square_profiles = []
    q_square_zero_rows = []
    classification_counts = Counter()
    for row in range(2, q + 1):
        cover_mask = row_cover_mask(row, masks, full_mask)
        survivor_count = (q - 1) - cover_mask.bit_count()
        classification = classify_q_row_in_p_grid(p, q, row)
        classification_counts[classification["window_type"]] += 1
        profile = {
            **classification,
            "survivor_count_under_old_p_sieve": survivor_count,
            "is_zero_under_old_p_sieve": survivor_count == 0,
        }
        q_square_profiles.append(profile)
        if survivor_count == 0:
            q_square_zero_rows.append(row)

    zero_count = len(zero_rows)
    lifted_period = q * period
    lifted_zero_count = q * zero_count
    return {
        "p": p,
        "q": q,
        "gap": q - p,
        "base_primes": base_primes,
        "old_p_row_period_for_width_q": period,
        "q_lifted_period": lifted_period,
        "zero_count_in_old_period": zero_count,
        "zero_count_in_q_lifted_period": lifted_zero_count,
        "old_period_zero_count_even": zero_count % 2 == 0,
        "lifted_zero_count_even": lifted_zero_count % 2 == 0,
        "mirror_ok_in_old_period": mirror_ok,
        "first_zero_rows_in_old_period": zero_rows[:10],
        "last_zero_rows_in_old_period": zero_rows[-10:],
        "survivor_histogram": dict(sorted(survivor_hist.items())),
        "q_square_zero_rows_under_old_p_sieve": q_square_zero_rows,
        "q_square_classification_counts": dict(sorted(classification_counts.items())),
        "q_square_thinnest_rows": sorted(
            q_square_profiles,
            key=lambda item: item["survivor_count_under_old_p_sieve"],
        )[:8],
    }


def build(max_p: int) -> dict[str, Any]:
    """构造审计结果。"""
    primes = primes_upto(max_p + 20)
    pairs = [
        (p, primes[index + 1])
        for index, p in enumerate(primes[:-1])
        if 5 <= p <= max_p
    ]
    rows = [scan_pair(p, q) for p, q in pairs]
    return {
        "status": "crt_lift_parity_route_rejected_but_window_descent_kept",
        "parameters": {"max_p": max_p, "pairs": pairs},
        "summary": {
            "pair_count": len(rows),
            "all_old_period_mirror_ok": all(row["mirror_ok_in_old_period"] for row in rows),
            "all_old_zero_counts_even": all(row["old_period_zero_count_even"] for row in rows),
            "all_lifted_zero_counts_even": all(row["lifted_zero_count_even"] for row in rows),
            "pairs_with_q_square_zero_rows": [
                {
                    "p": row["p"],
                    "q": row["q"],
                    "q_square_zero_rows": row["q_square_zero_rows_under_old_p_sieve"],
                }
                for row in rows
                if row["q_square_zero_rows_under_old_p_sieve"]
            ],
        },
        "rows": rows,
        "review_conclusion": [
            "q 非平凡列上，新增素数 q 不参与覆盖；所以 q 零行可降为旧 p-筛长度 q 零窗。",
            "长度 q 零窗不等于 p 对齐零行；它必须先通过 full-p-row/seam-window 二分。",
            "旧 p-筛周期的零行集合已经镜像成偶数；乘以奇数 q 后仍为偶数，不产生奇偶矛盾。",
            "可保留的证明增益是：若 q 方阵内出现零行，则它给出第一周期内非常早的旧 p-筛 q 零窗；下一步应攻早期 seam-window 排斥或端点 CRT 缺陷。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# CRT 提升奇偶矛盾路线审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        "## 总结",
        "",
        f"- 相邻素数对数量：`{summary['pair_count']}`。",
        f"- 旧周期镜像全部成立：`{summary['all_old_period_mirror_ok']}`。",
        f"- 旧周期零行数全部为偶数：`{summary['all_old_zero_counts_even']}`。",
        f"- 提升到 `q` 个旧周期后的零行数全部为偶数：`{summary['all_lifted_zero_counts_even']}`。",
        f"- 样本 q 方阵内旧筛零行：`{summary['pairs_with_q_square_zero_rows']}`。",
        "",
        "## 逐条审计",
        "",
        "1. 在既有约定中只看非平凡列 `1..q-1`。因此新增素数 `q` 不整除任何非平凡列格点；",
        "   q 阶零行如果存在，确实等价于旧 `p`-筛覆盖了一个长度 `q-1` 的 q 行窗口。",
        "2. 该窗口不是自动的 p 对齐零行。设 `q=p+g`、`A=(s-1)q`、`a=A mod p`。",
        "   只有当 `a=0` 或 `a>=p-g` 时，q 行窗口才包含完整 p 对齐非平凡行；否则只是跨两个 p 行的缝合零窗。",
        "3. 旧 p-筛在 q 行宽下的基本行周期为 `M_p=prod_{ell<=p} ell`。若人为放大到 q 阶周期",
        "   `q M_p`，零行数只是乘以奇数 `q`。但 `M_p` 周期内零行集合已由镜像成偶数，所以乘以 q 后仍为偶数。",
        "",
        "## 样本表",
        "",
        "| p | q | M_p | zero rows in M_p | q-lifted zero rows | mirror ok | q-square zero rows | direct/seam rows |",
        "|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in result["rows"]:
        lines.append(
            "| {p} | {q} | {period} | {zero} | {lifted} | `{mirror}` | `{qzeros}` | `{classes}` |".format(
                p=row["p"],
                q=row["q"],
                period=row["old_p_row_period_for_width_q"],
                zero=row["zero_count_in_old_period"],
                lifted=row["zero_count_in_q_lifted_period"],
                mirror=row["mirror_ok_in_old_period"],
                qzeros=row["q_square_zero_rows_under_old_p_sieve"],
                classes=row["q_square_classification_counts"],
            )
        )
    lines.extend(
        [
            "",
            "## 可保留的硬攻方向",
            "",
            "这条路线不能直接给出奇偶矛盾；真正可用的压缩是：",
            "",
            "```text",
            "q 方阵边界零行",
            "=> 旧 p-筛第一周期内极早长度 q 零窗",
            "=> 完整 p 对齐零行 或 p 缝合零窗",
            "=> 早期端点 CRT 缺陷 / PDEC / SAE。",
            "```",
            "",
            "因此下一硬点应是早期缝合零窗排斥，而不是零行总数奇偶排斥。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=19)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=DOCS / "prime-matrix-crt-lift-parity-audit",
    )
    args = parser.parse_args()
    result = build(args.max_p)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
