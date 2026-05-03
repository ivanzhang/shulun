#!/usr/bin/env python3
"""快速审计固定 h=3 的 TotalDescent-TM 余量。

用法示例：
  python3 experiments/prime_matrix_total_descent_h3_margin_audit.py
  python3 experiments/prime_matrix_total_descent_h3_margin_audit.py --max-p 5000

核心：
  当 h=3 时，CRT 行周期 N_3=2，因此每条完整 3 对齐行都自动满足头部/尾镜像命中。
  每条完整 3 行只有一个避开 2、3 的候选数。若该候选数的最小素因子在 [5,p]，
  该 3 行被复活点打断；否则它是 p-rough 候选。在旧 p-筛零窗假设下，这个候选本身
  已经给出直接矛盾；等价地，也可说它会强制出不可能的 3-筛零行。

注意：
  这是固定 h=3 的有限精确账本，不是全局证明。全局证明仍需证明所有 p,q,row 的
  h=3 余量恒正，或把失败相位送入 SAE/PDEC/ColumnCRT。
"""

from __future__ import annotations

import argparse
import json
from bisect import bisect_right
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


class Fenwick:
    """Fenwick 树，用于动态统计被小素因子打断的 3 行数量。"""

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        """在 1-based index 上累加 value。"""
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def prefix(self, index: int) -> int:
        """返回 [1,index] 的和。"""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_sum(self, left: int, right: int) -> int:
        """返回 [left,right] 的和。"""
        if right < left:
            return 0
        return self.prefix(right) - self.prefix(left - 1)


def smallest_prime_factor_table(limit: int) -> list[int]:
    """生成最小素因子表。"""
    spf = list(range(limit + 1))
    if limit >= 0:
        spf[0] = 0
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, int(limit**0.5) + 1):
        if spf[prime] != prime:
            continue
        for n in range(prime * prime, limit + 1, prime):
            if spf[n] == n:
                spf[n] = prime
    return spf


def h3_candidate_value(row: int) -> int:
    """返回第 row 条 3 对齐行中唯一避开 2、3 的候选数。"""
    if row % 2 == 1:
        return 3 * row - 2
    return 3 * row - 1


def contained_h3_rows(left: int, right: int) -> tuple[int, int]:
    """返回完整包含在 [left,right] 内的 3 对齐行号范围。"""
    first = (left + 4) // 3
    last = right // 3
    return first, last


def audit(max_p: int, row_stride: int) -> dict:
    """执行固定 h=3 余量审计。"""
    primes = primes_upto(max_p + 100)
    target_primes = [prime for prime in primes if 5 <= prime <= max_p]
    max_q = next_prime(max_p)
    max_n = max_q * max_q
    max_h3_row = (max_n + 2) // 3
    spf = smallest_prime_factor_table(max_n)

    # events_by_spf[d] 保存最小素因子恰为 d 的 3 行；当 p 增大到 d 时，该行变为被打断。
    events_by_spf: dict[int, list[int]] = {}
    for row in range(1, max_h3_row + 1):
        candidate = h3_candidate_value(row)
        if candidate <= 1 or candidate > max_n:
            continue
        factor = spf[candidate]
        if 5 <= factor <= max_p:
            events_by_spf.setdefault(factor, []).append(row)

    fenwick = Fenwick(max_h3_row)
    event_keys = sorted(events_by_spf)
    event_cursor = 0
    records_checked = 0
    failures = []
    tight_samples = []
    min_margin = None
    max_margin = None
    initial_type_counts: dict[str, int] = {}
    terminal_rows = 0

    for p in target_primes:
        while event_cursor < len(event_keys) and event_keys[event_cursor] <= p:
            for row in events_by_spf[event_keys[event_cursor]]:
                fenwick.add(row, 1)
            event_cursor += 1

        q = next_prime(p)
        for q_row in range(2, q + 1):
            if row_stride > 1 and (q_row != q) and ((q_row - 2) % row_stride != 0):
                continue
            left = (q_row - 1) * q + 1
            right = q_row * q
            first, last = contained_h3_rows(left, right)
            candidate_count = max(0, last - first + 1)
            blocked_count = fenwick.range_sum(first, last) if candidate_count else 0
            margin = candidate_count - blocked_count
            classification = classify_q_row_descent(p, q, q_row)["type"]
            initial_type_counts[classification] = (
                initial_type_counts.get(classification, 0) + 1
            )
            records_checked += 1
            if q_row == q:
                terminal_rows += 1
            min_margin = margin if min_margin is None else min(min_margin, margin)
            max_margin = margin if max_margin is None else max(max_margin, margin)
            sample = {
                "p": p,
                "q": q,
                "q_row": q_row,
                "interval": [left, right],
                "initial_type": classification,
                "h3_row_range": [first, last],
                "candidate_count": candidate_count,
                "blocked_count": blocked_count,
                "margin": margin,
                "terminal_q2_row": q_row == q,
            }
            if margin <= 0:
                failures.append(sample)
            tight_samples.append(sample)

    tight_samples.sort(key=lambda item: (item["margin"], item["candidate_count"]))
    return {
        "status": "finite_h3_total_descent_margin_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "row_stride": row_stride,
            "max_n": max_n,
            "max_h3_row": max_h3_row,
        },
        "summary": {
            "q_rows_checked": records_checked,
            "initial_type_counts": dict(sorted(initial_type_counts.items())),
            "h3_closed": records_checked - len(failures),
            "h3_failures": len(failures),
            "closure_fraction": (
                (records_checked - len(failures)) / records_checked
                if records_checked
                else None
            ),
            "min_margin": min_margin,
            "max_margin": max_margin,
            "terminal_q2_rows": terminal_rows,
            "event_prime_count": len(event_keys),
        },
        "tight_samples": tight_samples[:32],
        "failure_samples": failures[:32],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    lines = [
        "# 固定 h=3 的 TotalDescent-TM 余量审计",
        "",
        "**状态：** `finite_h3_total_descent_margin_audit_not_global_proof`",
        "",
        "本文专攻当前最窄硬点的更强版本：固定使用 `h=3`，不再任选下降层。由于 `N_3=2`，完整 3 对齐行自动满足 CRT 头部/尾镜像命中；更强的是，完整 3 行的唯一六轮候选一旦不是 `[5,p]` 复活点，就直接成为旧 `p`-筛零窗的幸存点矛盾。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `max_n`: `{params['max_n']}`。",
        f"- `max_h3_row`: `{params['max_h3_row']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 初始分支计数：`{summary['initial_type_counts']}`。",
        f"- `h=3` 闭合数：`{summary['h3_closed']}`。",
        f"- `h=3` 失败数：`{summary['h3_failures']}`。",
        f"- 闭合比例：`{summary['closure_fraction']}`。",
        f"- 最小余量：`{summary['min_margin']}`。",
        f"- 最大余量：`{summary['max_margin']}`。",
        f"- 末行 `q^2` 行数：`{summary['terminal_q2_rows']}`。",
        "",
        "## 最紧样本",
        "",
        "| p | q | q-row | initial | h3 rows | candidates | blocked | margin | terminal |",
        "|---:|---:|---:|---|---|---:|---:|---:|---|",
    ]
    for sample in result["tight_samples"][:20]:
        lines.append(
            "| {p} | {q} | {row} | `{initial}` | `{rows}` | {cand} | {blocked} | {margin} | `{terminal}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                initial=sample["initial_type"],
                rows=sample["h3_row_range"],
                cand=sample["candidate_count"],
                blocked=sample["blocked_count"],
                margin=sample["margin"],
                terminal=sample["terminal_q2_row"],
            )
        )

    lines.extend(
        [
            "",
            "## 严格化目标",
            "",
            "固定 `h=3` 时，每条完整 3 对齐行只有一个避开 `2,3` 的候选数。若该候选数的最小素因子在 `[5,p]`，该行被复活点打断；否则该候选是 `p`-rough 点。由于候选数大于 `1` 且避开 `2,3`，在旧 `p`-筛零窗假设下它已经给出直接幸存点矛盾；等价地，它会强制出不可能的 `3`-筛零行。",
            "",
            "因此最窄硬点可写成显式 6-轮不等式：任意相邻 `p<q` 与任意 `2<=s<=q`，令 `I=[(s-1)q+1,sq]`，完整 3 行的数量严格大于其中候选数最小素因子落在 `[5,p]` 的数量。",
            "",
            "有限账本显示该不等式在测试域内余量恒正。若要成为正式证明，需要给出全局覆盖上界；若上界失败，则失败意味着 `I` 中 6-轮候选数被 `[5,p]` 素因子精确覆盖，应触发 `SAE/PDEC/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-total-descent-h3-margin-audit"),
    )
    args = parser.parse_args()
    result = audit(max_p=args.max_p, row_stride=max(1, args.row_stride))
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
