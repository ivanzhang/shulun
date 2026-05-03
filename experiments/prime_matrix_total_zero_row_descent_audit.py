#!/usr/bin/env python3
"""审计任意高阶 q 行零窗是否强制下降为小阶方阵零行。

用法示例：
  python3 experiments/prime_matrix_total_zero_row_descent_audit.py
  python3 experiments/prime_matrix_total_zero_row_descent_audit.py --max-p 500
  python3 experiments/prime_matrix_total_zero_row_descent_audit.py --max-p 2000 --row-stride 25

模型：
  对相邻素数 p<q，假设 q×q 中第 s 行（2<=s<=q）是 q-筛零行。
  相邻壳层单点性说明该 q 行在旧 p-筛下已经是零窗，唯一例外是末行端点 q^2。
  本脚本不再分 aligned/seam 两套逻辑，而是统一降到所有 h<=p 的行宽，寻找：

    完整 h 对齐行 J⊂I；
    J 避开剥层复活点 Rev_{h,p}(I) 与 q^2 穿孔；
    J 的 CRT 行相位或尾镜像相位落入 h×h 方阵头部。

  若找到，则该 q 零行在条件模型下强制产生小阶 h×h 方阵零行。

注意：
  这是条件下降模型账本，不是全局无条件证明。全局证明仍需证明同一相位命中机制对所有
  素数成立，或把非命中持久阻断送入 SAE/PDEC/ColumnCRT。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_scaled_peeling_halfwidth_audit import contained_rows, interval_for_row
from prime_matrix_seam_multilevel_descent_audit import (
    conditional_revived_positions,
    smallest_prime_factor_table,
)
from prime_matrix_seam_tail_mirror_descent_audit import (
    mirror_profile,
    period_rows_by_prime,
)
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def first_total_descent_hit(
    *,
    p: int,
    q: int,
    q_row: int,
    all_primes: list[int],
    spf: list[int],
    periods: dict[int, int],
    max_levels: int | None,
) -> dict:
    """寻找一条假想 q 零行强制下降到小阶方阵零行的首个命中。"""
    left, right = interval_for_row(q, q_row)
    p_index = all_primes.index(p)
    lower_indices = list(range(p_index, -1, -1))
    if max_levels is not None:
        lower_indices = lower_indices[: max_levels + 1]

    terminal_punctures = {q * q} if q_row == q else set()
    inspected_levels = []
    first_forced = None
    first_hit = None

    for level_index, idx in enumerate(lower_indices):
        h = all_primes[idx]
        rows = contained_rows(left, right, h)
        revived = conditional_revived_positions(
            left=left,
            right=right,
            lower_prime=h,
            upper_prime=p,
            spf=spf,
            terminal_punctures=terminal_punctures,
        )
        forced_profiles = []
        for row in rows:
            row_left, row_right = interval_for_row(h, row)
            if any(row_left <= n <= row_right for n in revived):
                continue
            forced_profiles.append(mirror_profile(row, h, periods[h]))

        if forced_profiles and first_forced is None:
            first_forced = {
                "level_index_from_p": level_index,
                "h": h,
                "forced_profiles": forced_profiles[:12],
            }

        hits = [
            profile for profile in forced_profiles if profile["head_or_tail_hit"]
        ]
        inspected_levels.append(
            {
                "level_index_from_p": level_index,
                "h": h,
                "contained_row_count": len(rows),
                "revived_count": len(set(revived)),
                "forced_count": len(forced_profiles),
                "head_or_tail_hit_count": len(hits),
                "sample_hits": hits[:6],
                "sample_forced": forced_profiles[:6],
            }
        )
        if hits:
            first_hit = {
                "level_index_from_p": level_index,
                "h": h,
                "hit_profiles": hits[:12],
            }
            break

    return {
        "p": p,
        "q": q,
        "q_row": q_row,
        "interval": [left, right],
        "terminal_punctures": sorted(terminal_punctures),
        "initial_classification": classify_q_row_descent(p, q, q_row),
        "first_forced": first_forced,
        "first_hit": first_hit,
        "has_forced_zero": first_forced is not None,
        "has_matrix_hit": first_hit is not None,
        "inspected_levels": inspected_levels,
    }


def audit(max_p: int, row_stride: int, max_levels: int | None) -> dict:
    """执行总下降审计。"""
    all_primes = primes_upto(max_p + 100)
    max_q = next_prime(max_p)
    spf = smallest_prime_factor_table(max_q * max_q)
    periods = period_rows_by_prime(all_primes, max_p)
    records = []

    for p in [prime for prime in all_primes if 5 <= prime <= max_p]:
        q = next_prime(p)
        for q_row in range(2, q + 1):
            if row_stride > 1 and (q_row != q) and ((q_row - 2) % row_stride != 0):
                continue
            records.append(
                first_total_descent_hit(
                    p=p,
                    q=q,
                    q_row=q_row,
                    all_primes=all_primes,
                    spf=spf,
                    periods=periods,
                    max_levels=max_levels,
                )
            )

    hits = [record for record in records if record["has_matrix_hit"]]
    forced = [record for record in records if record["has_forced_zero"]]
    hit_levels = [record["first_hit"]["level_index_from_p"] for record in hits]
    hit_primes = [record["first_hit"]["h"] for record in hits]
    initial_types = Counter(
        record["initial_classification"]["type"] for record in records
    )
    hit_modes: Counter[str] = Counter()
    for record in hits:
        for profile in record["first_hit"]["hit_profiles"]:
            if profile["direct_head_hit"]:
                hit_modes["direct_head_phase"] += 1
            if profile["mirror_head_hit"]:
                hit_modes["tail_mirror_phase"] += 1

    return {
        "status": "finite_total_zero_row_descent_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "row_stride": row_stride,
            "max_levels": max_levels,
            "q_rows": "2..q; row 1 omitted because it is not a candidate zero row",
        },
        "summary": {
            "q_rows_checked": len(records),
            "initial_type_counts": dict(sorted(initial_types.items())),
            "forced_zero_found": len(forced),
            "matrix_head_or_tail_hits": len(hits),
            "unclosed_rows": len(records) - len(hits),
            "hit_fraction": len(hits) / len(records) if records else None,
            "max_hit_level_index": max(hit_levels, default=None),
            "min_hit_prime": min(hit_primes, default=None),
            "hit_prime_counts": dict(sorted(Counter(hit_primes).items())),
            "hit_mode_counts": dict(sorted(hit_modes.items())),
            "terminal_puncture_rows": sum(
                1 for record in records if record["terminal_punctures"]
            ),
        },
        "hit_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "initial_classification": record["initial_classification"],
                "terminal_punctures": record["terminal_punctures"],
                "first_forced": record["first_forced"],
                "first_hit": record["first_hit"],
            }
            for record in hits[:24]
        ],
        "unclosed_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "initial_classification": record["initial_classification"],
                "terminal_punctures": record["terminal_punctures"],
                "first_forced": record["first_forced"],
                "last_level": record["inspected_levels"][-1]
                if record["inspected_levels"]
                else None,
            }
            for record in records
            if not record["has_matrix_hit"]
        ][:24],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    hit_prime_items = list(summary["hit_prime_counts"].items())
    hit_prime_excerpt = dict(hit_prime_items[:20])
    if len(hit_prime_items) > 20:
        hit_prime_excerpt["..."] = "完整分布见 JSON"

    lines = [
        "# 任意 q 零行总下降审计",
        "",
        "**状态：** `finite_total_zero_row_descent_audit_not_global_proof`",
        "",
        "本文把 aligned 分支、seam 分支、末行 `q^2` 端点穿孔、CRT 周期性和尾镜像统一到同一条件下降模型中，检验：若高阶 `q×q` 方阵内任意非第一行是零行，是否会强制某个小阶 `h×h` 方阵内也出现零行。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `max_levels`: `{params['max_levels']}`。",
        f"- `q_rows`: `{params['q_rows']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 初始分支计数：`{summary['initial_type_counts']}`。",
        f"- 出现条件强制零行数：`{summary['forced_zero_found']}`。",
        f"- 小阶方阵头部/尾镜像命中数：`{summary['matrix_head_or_tail_hits']}`。",
        f"- 未闭合行数：`{summary['unclosed_rows']}`。",
        f"- 命中比例：`{summary['hit_fraction']}`。",
        f"- 最大首次命中下降层数：`{summary['max_hit_level_index']}`。",
        f"- 最小命中素数：`{summary['min_hit_prime']}`。",
        f"- 末行端点穿孔行数：`{summary['terminal_puncture_rows']}`。",
        f"- 命中模式计数：`{summary['hit_mode_counts']}`。",
        f"- 命中素数分布摘录：`{hit_prime_excerpt}`。",
        "",
        "## 命中样本",
        "",
        "| p | q | q-row | initial | terminal puncture | hit h | hit profiles |",
        "|---:|---:|---:|---|---|---:|---|",
    ]
    for sample in result["hit_samples"][:12]:
        hit = sample["first_hit"]
        lines.append(
            "| {p} | {q} | {row} | `{initial}` | `{puncture}` | {h} | `{profiles}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                initial=sample["initial_classification"]["type"],
                puncture=sample["terminal_punctures"],
                h=hit["h"],
                profiles=hit["hit_profiles"][:4],
            )
        )

    lines.extend(
        [
            "",
            "## 未闭合样本",
            "",
            "| p | q | q-row | initial | terminal puncture | first forced | last level |",
            "|---:|---:|---:|---|---|---|---|",
        ]
    )
    for sample in result["unclosed_samples"][:12]:
        lines.append(
            "| {p} | {q} | {row} | `{initial}` | `{puncture}` | `{forced}` | `{last}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                initial=sample["initial_classification"]["type"],
                puncture=sample["terminal_punctures"],
                forced=sample["first_forced"],
                last=sample["last_level"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "统一模型使用三个严格输入：",
            "",
            "1. 相邻壳层单点性：`q^2` 内旧 `p`-筛唯一合数幸存者是 `q^2`；",
            "2. 剥层复活恒等式：降到 `h<=p` 后复活点为 `P^-(n)∈(h,p]` 的点，另加末行 `q^2`；",
            "3. CRT 头尾镜像：强制 `h` 零行行相位 `rho` 或镜像相位 `N_h-rho+1` 落入 `1..h` 时，得到 `h×h` 方阵内条件零行。",
            "",
            "因此若归纳已知所有小阶 `Row(h)`，任何命中记录都排斥对应高阶 q 零行。",
            "",
            "本账本支持用户的总路线：在测试域内，不管初始是 aligned 还是 seam，也不管是否末行带 `q^2` 穿孔，全部假想高阶零行都被压到某个小阶方阵零行。",
            "",
            "但全局论文仍需证明 `TotalDescent-TM`：上述命中机制对所有素数和所有行相位成立；或者证明非命中相位集合必触发 `SAE/PDEC/ColumnCRT`。有限账本不能替代这个全局不等式。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=500)
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument("--max-levels", type=int, default=None)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-total-zero-row-descent-audit"),
    )
    args = parser.parse_args()
    result = audit(
        max_p=args.max_p,
        row_stride=max(1, args.row_stride),
        max_levels=args.max_levels,
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
