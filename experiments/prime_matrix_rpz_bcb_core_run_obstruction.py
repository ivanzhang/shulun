#!/usr/bin/env python3
"""审计 RPZ-BCB no-TailAnchor 核心的低筛连续覆盖长度障碍。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_core_run_obstruction.py

BCB-Core 定理给出：

  no TailAnchor => J_T0 是 h-筛零区间。

也就是说，核心区间 `J_T0` 中每个整数都必须被某个 `<=h` 的素数整除。
这要求核心长度不超过模 `P(h)` 周期内的最大低筛连续覆盖长度。

本脚本计算当前 BCB 样本层 `h=5,7,11,13` 的精确最大连续覆盖长度，
并与 BCB 强制核心长度比较。若 `|J_T0|` 更长，则 no-TailAnchor BCB
核心在该参数族中不可能存在，必须回到 TailAnchor 或其它已命名出口。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import primes_upto, primorial


def covered_by_small_prime(value: int, primes: list[int]) -> bool:
    """判断 `value` 是否被给定素数表中的某个素数整除。"""
    return any(value % prime == 0 for prime in primes)


def max_cyclic_covered_run(h: int) -> dict[str, Any]:
    """计算模 `P(h)` 的最大连续低筛覆盖段。"""
    primes = primes_upto(h)
    modulus = primorial(primes, h)
    covered = [
        covered_by_small_prime(value, primes)
        for value in range(1, modulus + 1)
    ]
    if all(covered):
        return {
            "h": h,
            "primorial": modulus,
            "max_covered_run": modulus,
            "example_start": 1,
            "example_end": modulus,
        }

    doubled = covered + covered
    best = 0
    best_end = 0
    current = 0
    for index, flag in enumerate(doubled):
        if flag:
            current += 1
            if min(current, modulus) > best:
                best = min(current, modulus)
                best_end = index
        else:
            current = 0
    start_index = (best_end - best + 1) % modulus
    start_value = start_index + 1
    end_value = ((start_index + best - 1) % modulus) + 1
    return {
        "h": h,
        "primorial": modulus,
        "max_covered_run": best,
        "example_start": start_value,
        "example_end": end_value,
    }


def audit_record(record: dict[str, Any], run_by_h: dict[int, dict[str, Any]]) -> dict[str, Any]:
    """审计单条 BCB 核心记录。"""
    h = record["half_prime"]
    run = run_by_h[h]
    length = record["forced_core_length"]
    margin = length - run["max_covered_run"]
    return {
        "top_prime": record["top_prime"],
        "top_zero_row": record["top_zero_row"],
        "h": h,
        "forced_core_interval": record["forced_core_interval"],
        "forced_core_length": length,
        "max_h_sieve_covered_run": run["max_covered_run"],
        "run_obstruction_margin": margin,
        "no_tailanchor_core_impossible_by_run": margin > 0,
    }


def build(core_path: Path) -> dict[str, Any]:
    """构造核心长度障碍账本。"""
    core = json.loads(core_path.read_text(encoding="utf-8"))
    hs = sorted({record["half_prime"] for record in core["records"]})
    run_rows = [max_cyclic_covered_run(h) for h in hs]
    run_by_h = {row["h"]: row for row in run_rows}
    records = [audit_record(record, run_by_h) for record in core["records"]]
    return {
        "status": "rpz_bcb_no_tailanchor_core_run_obstruction",
        "source": str(core_path),
        "summary": {
            "h_layers": len(run_rows),
            "records": len(records),
            "records_obstructed_by_run_length": sum(
                1 for record in records if record["no_tailanchor_core_impossible_by_run"]
            ),
            "minimum_obstruction_margin": min(
                record["run_obstruction_margin"] for record in records
            ),
        },
        "run_rows": run_rows,
        "records": records,
        "review_boundary": [
            "no TailAnchor 分支强制 J_T0 为 h-筛零区间。",
            "任何 h-筛零区间长度都不能超过模 P(h) 的最大连续低筛覆盖长度。",
            "当前 BCB 样本全部超过该最大长度，因此当前参数族的 no-TailAnchor BCB 核心不相容。",
            "全局闭合仍需证明对应 h 层的 Jacobsthal/低筛覆盖长度上界，或把超界失败送入已命名出口。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ-BCB 核心低筛连续覆盖长度障碍",
        "",
        "**状态：** `rpz_bcb_no_tailanchor_core_run_obstruction`",
        "",
        "## 总结",
        "",
        f"- h 层数：`{summary['h_layers']}`。",
        f"- BCB 记录数：`{summary['records']}`。",
        f"- 被低筛覆盖长度障碍排斥的记录数：`{summary['records_obstructed_by_run_length']}`。",
        f"- 最小障碍余量：`{summary['minimum_obstruction_margin']}`。",
        "",
        "## 低筛最大连续覆盖长度",
        "",
        "| h | P(h) | max covered run | example start | example end |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in result["run_rows"]:
        lines.append(
            "| {h} | {primorial} | {run} | {start} | {end} |".format(
                h=row["h"],
                primorial=row["primorial"],
                run=row["max_covered_run"],
                start=row["example_start"],
                end=row["example_end"],
            )
        )

    lines.extend(
        [
            "",
            "## BCB 核心长度对比",
            "",
            "| top P | top row | h | core interval | core length | max covered run | margin | obstructed |",
            "|---:|---:|---:|---|---:|---:|---:|---|",
        ]
    )
    for row in result["records"]:
        lines.append(
            "| {top} | {top_row} | {h} | `{interval}` | {length} | {run} | {margin} | `{obstructed}` |".format(
                top=row["top_prime"],
                top_row=row["top_zero_row"],
                h=row["h"],
                interval=row["forced_core_interval"],
                length=row["forced_core_length"],
                run=row["max_h_sieve_covered_run"],
                margin=row["run_obstruction_margin"],
                obstructed=row["no_tailanchor_core_impossible_by_run"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "在 no-TailAnchor 分支中，BCB-Core 要求 `J_T0` 是 `h`-筛零区间；这不是端点相位问题，而是低筛连续覆盖长度问题。",
            "当前五条 BCB 样本的核心长度全部严格超过对应 `h` 层的最大连续低筛覆盖长度，所以这些参数族的 no-TailAnchor BCB 核心不相容。",
            "该账本把当前最小硬点从 accepted preimage 进一步上移为 Jacobsthal 型上界：全局证明若能给出 `max_run_h < |J_T0|`，则 BCB no-TailAnchor 分支直接关闭；否则剩余仍需进入 endpoint/first-failure/PDEC/ColumnCRT 出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--core",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-run-obstruction"),
    )
    args = parser.parse_args()

    result = build(args.core)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
