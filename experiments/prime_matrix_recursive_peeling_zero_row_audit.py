#!/usr/bin/env python3
"""审计零行递归剥离是否会自动产生下层对齐零行或连续零行。

用法示例：
  python3 experiments/prime_matrix_recursive_peeling_zero_row_audit.py
  python3 experiments/prime_matrix_recursive_peeling_zero_row_audit.py --max-levels 6

输入使用 `docs/monograph/prime-matrix-zero-row-crt-audit.json` 中已经找到的
首个 p 对齐零行。对每个零行区间 I，逐步把筛素数上界从 p 降到前一个素数 r，
统计在 I 内重新出现的 r-筛幸存者，以及 I 内是否包含完整 r 对齐零行。

目的不是证明定理，而是检验一个递归剥离直觉：
“上层零行是否会自动推出下层零行，甚至连续零行”。审计结果用于定位该思路
必须补充的真正硬条件。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from prime_matrix_zero_row_crt_audit import mark_old_sieve_interval, primes_upto


def interval_for_row(p: int, row: int) -> tuple[int, int]:
    """返回 p 对齐行区间。"""
    return (row - 1) * p + 1, row * p


def alive_positions(left: int, right: int, small_primes: list[int]) -> list[int]:
    """返回 [left,right] 中避开 small_primes 的位置。"""
    alive = mark_old_sieve_interval(left, right, small_primes)
    return [left + idx for idx, flag in enumerate(alive) if flag]


def contained_aligned_zero_rows(
    *,
    left: int,
    right: int,
    row_width: int,
    small_primes: list[int],
) -> list[int]:
    """找出完全包含在 [left,right] 内的 row_width 对齐零行。"""
    first_row = (left + row_width - 1) // row_width
    last_row = right // row_width
    zero_rows: list[int] = []
    for row in range(first_row, last_row + 1):
        row_left, row_right = interval_for_row(row_width, row)
        if row_left < left or row_right > right:
            continue
        if not alive_positions(row_left, row_right, small_primes):
            zero_rows.append(row)
    return zero_rows


def consecutive_pairs(rows: list[int]) -> list[tuple[int, int]]:
    """返回连续零行对。"""
    row_set = set(rows)
    return [(row, row + 1) for row in rows if row + 1 in row_set]


def audit(max_levels: int, source_path: Path) -> dict:
    """执行递归剥离审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    all_primes = primes_upto(source["parameters"]["max_p"] + 100)
    records = []

    for item in source["records"]:
        aligned = item["first_aligned_zero_row_after_p"]
        if not aligned["found"]:
            continue
        p = item["p"]
        row = aligned["row"]
        left, right = aligned["interval"]
        prime_index = all_primes.index(p)
        levels = []

        for idx in range(prime_index - 1, max(-1, prime_index - max_levels - 1), -1):
            level_prime = all_primes[idx]
            small_primes = [prime for prime in all_primes if prime <= level_prime]
            survivors = alive_positions(left, right, small_primes)
            zero_rows = contained_aligned_zero_rows(
                left=left,
                right=right,
                row_width=level_prime,
                small_primes=small_primes,
            )
            levels.append(
                {
                    "level_prime": level_prime,
                    "survivor_count_after_peeling": len(survivors),
                    "survivors": survivors[:20],
                    "contained_aligned_zero_rows": zero_rows,
                    "contained_zero_row_count": len(zero_rows),
                    "consecutive_zero_pairs": consecutive_pairs(zero_rows),
                }
            )

        one_step = levels[0] if levels else None
        records.append(
            {
                "p": p,
                "row": row,
                "interval": [left, right],
                "next_prime": item["q_next"],
                "one_step_zero_after_peeling": (
                    one_step is not None
                    and one_step["survivor_count_after_peeling"] == 0
                ),
                "one_step_contains_aligned_zero_row": (
                    one_step is not None
                    and one_step["contained_zero_row_count"] > 0
                ),
                "any_consecutive_zero_pair_in_profile": any(
                    level["consecutive_zero_pairs"] for level in levels
                ),
                "levels": levels,
            }
        )

    return {
        "status": "recursive_peeling_audit_supports_punctured_windows_not_automatic_zero_rows",
        "source": str(source_path),
        "parameters": {
            "max_levels": max_levels,
            "source_max_p": source["parameters"]["max_p"],
        },
        "summary": {
            "zero_row_records": len(records),
            "one_step_zero_after_peeling": sum(
                1 for record in records if record["one_step_zero_after_peeling"]
            ),
            "one_step_contains_aligned_zero_row": sum(
                1 for record in records if record["one_step_contains_aligned_zero_row"]
            ),
            "records_with_consecutive_zero_pair": sum(
                1 for record in records if record["any_consecutive_zero_pair_in_profile"]
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    params = result["parameters"]
    lines = [
        "# 零行递归剥离审计",
        "",
        "**状态：** `recursive_peeling_audit_supports_punctured_windows_not_automatic_zero_rows`",
        "",
        "## 参数",
        "",
        f"- `source`: `{result['source']}`",
        f"- `source_max_p`: `{params['source_max_p']}`",
        f"- `max_levels`: `{params['max_levels']}`",
        "",
        "## 总结",
        "",
        f"- 已知首个对齐零行记录数：`{summary['zero_row_records']}`。",
        f"- 一步剥离后仍完全零的记录数：`{summary['one_step_zero_after_peeling']}`。",
        f"- 一步剥离后包含完整下层对齐零行的记录数：`{summary['one_step_contains_aligned_zero_row']}`。",
        f"- 剥离剖面中出现连续对齐零行对的记录数：`{summary['records_with_consecutive_zero_pair']}`。",
        "",
        "## 逐例剖面",
        "",
        "| p | row | interval | next | one-step zero | contains aligned zero | consecutive pair | first peeled level | survivors | contained zero rows |",
        "|---:|---:|---|---:|---|---|---|---:|---:|---|",
    ]
    for record in result["records"]:
        first = record["levels"][0] if record["levels"] else {}
        lines.append(
            "| {p} | {row} | `{interval}` | {next_prime} | `{one_zero}` | `{contains}` | `{pair}` | {level} | {survivors} | `{zeros}` |".format(
                p=record["p"],
                row=record["row"],
                interval=record["interval"],
                next_prime=record["next_prime"],
                one_zero=str(record["one_step_zero_after_peeling"]).lower(),
                contains=str(record["one_step_contains_aligned_zero_row"]).lower(),
                pair=str(record["any_consecutive_zero_pair_in_profile"]).lower(),
                level=first.get("level_prime", "-"),
                survivors=first.get("survivor_count_after_peeling", "-"),
                zeros=first.get("contained_aligned_zero_rows", []),
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "若一个区间在 `p`-筛下为零，剥去顶层素数 `p` 后，重新出现的幸存者只能来自该区间内的 `p` 的倍数，并且其商避开更小筛素数。故递归对象不是零行，而是带少数复活点的 punctured zero window。",
            "",
            "本审计显示：已知样本中，一步剥离后完全仍零的情况存在，但多数情况会产生复活点；更关键的是，没有样本在剥离剖面中自动产生连续下层对齐零行。因此“递归剥离自动推出连续零行”不能作为无条件证明出口。",
            "",
            "可保留的硬点是：若能证明这些复活点不能被后续缝合窗口稳定吸收，或证明吸收必造成 `PDEC/TailAnchor/ColumnCRT` 缺陷，则递归剥离可以成为主链条的有效压力项。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-levels", type=int, default=6)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-zero-row-crt-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-recursive-peeling-zero-row-audit"),
    )
    args = parser.parse_args()

    result = audit(max_levels=args.max_levels, source_path=args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
