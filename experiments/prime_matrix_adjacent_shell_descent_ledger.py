#!/usr/bin/env python3
"""生成相邻素数壳层的零行下降账本。

用法示例：
  python3 experiments/prime_matrix_adjacent_shell_descent_ledger.py
  python3 experiments/prime_matrix_adjacent_shell_descent_ledger.py --max-p 2000

目标：
  精确审计相邻素数 p<q 的两个刚性事实：
  1. 在 q^2 内，从 p-筛升级到 q-筛，非第一行中唯一新增筛掉的 p-rough 点是 q^2；
  2. 任意 q 宽零窗降到 p 宽时，要么完整包含 p 对齐行，要么成为两个 p 行的端点缝合零窗。

注意：
  这是结构账本，不是全局无条件证明。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def has_factor_at_most(n: int, p: int, primes: list[int]) -> bool:
    """判断 n 是否有不超过 p 的素因子。"""
    for prime in primes:
        if prime > p:
            break
        if n % prime == 0:
            return True
    return False


def p_rough_q_multiples(p: int, q: int, primes: list[int]) -> list[int]:
    """列出 q^2 内被 q 新筛除、但旧 p-筛未筛除的 q 倍数。"""
    survivors = []
    for multiplier in range(1, q + 1):
        n = q * multiplier
        if not has_factor_at_most(n, p, primes):
            survivors.append(n)
    return survivors


def classify_q_row_descent(p: int, q: int, row: int) -> dict:
    """分类 q 行降到 p 行时是完整行还是缝合窗。"""
    gap = q - p
    start0 = (row - 1) * q
    offset = start0 % p
    lower_row = start0 // p + 1
    if offset == 0 or offset >= p - gap:
        contained_row = start0 // p + 2 if offset else start0 // p + 1
        return {
            "row": row,
            "type": "aligned_p_row_contained",
            "offset_mod_p": offset,
            "contained_p_row": contained_row,
            "left_guard": None,
            "right_guard": None,
        }
    return {
        "row": row,
        "type": "seam_window",
        "offset_mod_p": offset,
        "lower_rows": [lower_row, lower_row + 1],
        "left_guard": offset,
        "right_guard": p - gap - offset,
    }


def audit(max_p: int) -> dict:
    """执行壳层下降审计。"""
    primes = primes_upto(max_p + 200)
    records = []
    singleton_failures = []
    for p in [prime for prime in primes if 3 <= prime <= max_p]:
        q = next_prime(p)
        new_survivors = p_rough_q_multiples(p, q, primes)
        nonfirst_new_survivors = [n for n in new_survivors if n != q]
        if nonfirst_new_survivors != [q * q]:
            singleton_failures.append(
                {
                    "p": p,
                    "q": q,
                    "new_survivors": new_survivors,
                    "nonfirst_new_survivors": nonfirst_new_survivors,
                }
            )

        rows = [classify_q_row_descent(p, q, row) for row in range(2, q + 1)]
        seam_rows = [row for row in rows if row["type"] == "seam_window"]
        aligned_rows = [row for row in rows if row["type"] == "aligned_p_row_contained"]
        min_guard = min(
            (
                min(int(row["left_guard"]), int(row["right_guard"]))
                for row in seam_rows
            ),
            default=None,
        )
        max_guard_imbalance = max(
            (
                abs(int(row["left_guard"]) - int(row["right_guard"]))
                for row in seam_rows
            ),
            default=0,
        )
        records.append(
            {
                "p": p,
                "q": q,
                "gap": q - p,
                "new_q_killed_p_rough_points": new_survivors,
                "nonfirst_new_points": nonfirst_new_survivors,
                "singleton_ok": nonfirst_new_survivors == [q * q],
                "q_rows_checked": q - 1,
                "aligned_containment_rows": len(aligned_rows),
                "seam_rows": len(seam_rows),
                "seam_fraction": len(seam_rows) / (q - 1),
                "min_seam_guard": min_guard,
                "max_guard_imbalance": max_guard_imbalance,
                "sample_rows": rows[: min(12, len(rows))],
            }
        )
    return {
        "status": "finite_adjacent_shell_descent_ledger_not_global_proof",
        "parameters": {"max_p": max_p},
        "summary": {
            "prime_count": len(records),
            "singleton_failures": len(singleton_failures),
            "max_seam_fraction": max(
                (record["seam_fraction"] for record in records),
                default=0,
            ),
            "min_positive_guard": min(
                (
                    record["min_seam_guard"]
                    for record in records
                    if record["min_seam_guard"] is not None
                ),
                default=None,
            ),
            "max_guard_imbalance": max(
                (record["max_guard_imbalance"] for record in records),
                default=0,
            ),
        },
        "singleton_failures": singleton_failures,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 账本。"""
    summary = result["summary"]
    lines = [
        "# 相邻壳层零行下降账本",
        "",
        "**状态：** `finite_adjacent_shell_descent_ledger_not_global_proof`",
        "",
        "本文档审计相邻素数 `p<q` 的壳层刚性：在 `q^2` 内，新增的 `q` 筛只在非第一行新增筛掉 `q^2`；任意 `q` 宽窗口降到 `p` 宽时，只能是完整 `p` 行或端点缝合窗。",
        "",
        "## 摘要",
        "",
        f"- 素数对数量：`{summary['prime_count']}`。",
        f"- 新筛单点失败数：`{summary['singleton_failures']}`。",
        f"- 最大缝合行比例：`{summary['max_seam_fraction']}`。",
        f"- 最小正 guard 长度：`{summary['min_positive_guard']}`。",
        f"- 最大 guard 不平衡：`{summary['max_guard_imbalance']}`。",
        "",
        "## 代表行",
        "",
        "| p | q | gap | new nonfirst points | aligned rows | seam rows | seam fraction | min guard |",
        "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for record in result["records"][:40]:
        lines.append(
            "| {p} | {q} | {gap} | `{points}` | {aligned} | {seam} | {frac:.6f} | {guard} |".format(
                p=record["p"],
                q=record["q"],
                gap=record["gap"],
                points=record["nonfirst_new_points"],
                aligned=record["aligned_containment_rows"],
                seam=record["seam_rows"],
                frac=record["seam_fraction"],
                guard=record["min_seam_guard"],
            )
        )
    lines.extend(
        [
            "",
            "## 严格解释",
            "",
            "若 `n<q^2` 且旧 `p`-筛未筛掉 `n`，则 `n` 要么是素数，要么所有素因子都 `>p`。由于 `p<q` 相邻，合数情形的最小素因子至少为 `q`。因此合数旧筛幸存者在 `q^2` 内只能是 `q^2`。这就是相邻壳层单点性。",
            "",
            "对 `q` 行 `I_s=[(s-1)q+1,sq]`，写 `(s-1)q=mp+a`。若 `a=0` 或 `a>=p-(q-p)`，则 `I_s` 完整包含一条 `p` 对齐行；否则它只覆盖一条 `p` 行的后缀和下一条 `p` 行的前缀，两个外侧 complement 就是 `left_guard=a` 与 `right_guard=p-(q-p)-a`。",
            "",
            "因此，若 `q^2` 内存在非第一行 `q` 零行，则除最后一行的 `q^2` 穿孔外，它首先降为旧 `p`-筛零窗口；随后无损二分为：完整下层零行，或带两个 guard 的 seam zero window。",
            "",
            "## 对证明路线的含义",
            "",
            "这一步支持用户提出的递归路线，但也说明主障碍精确落在 seam guard：",
            "",
            "```text",
            "q-zero-row",
            "=> old-p q-zero-window plus possible q^2 puncture",
            "=> aligned p-zero-row or seam zero-window with two guards",
            "=> if guards cannot persist: descend",
            "=> if guards persist: endpoint/PDEC/ColumnCRT defect",
            "```",
            "",
            "所以真正需要硬攻的下一条定理是 `SeamGuard-Elimination`，而不是再次证明壳层单点性。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-adjacent-shell-descent-ledger",
    )
    args = parser.parse_args()
    result = audit(max_p=args.max_p)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
