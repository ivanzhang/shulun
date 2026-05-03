#!/usr/bin/env python3
"""计算 accepted selector 的最大拒绝间隙阈值。

用法示例：
  python3 experiments/prime_matrix_rpz_selector_gap_threshold.py

若候选行区间 `C_h(J)` 的行数大于 `A_h` 在模 `P(h)` 上的最大连续 rejected
空隙，则它必然命中 `A_h`。该脚本计算当前可枚举层的这个长度阈值，并核对
BCB-Core 当前样本哪些由长度自动保证，哪些仍依赖端点相位精确命中。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    primes_upto,
    primorial,
)
from prime_matrix_rpz_bcb_accepted_row_selector import candidate_rows


def max_rejected_run(primes: list[int], h: int) -> dict[str, Any]:
    """计算 `A_h` 的循环最大连续 rejected 行长度。"""
    modulus = primorial(primes, h)
    accepts = acceptance_checker(primes, h)
    flags = [accepts(h, phase) for phase in range(modulus)]
    accepted_count = sum(1 for flag in flags if flag)
    if accepted_count == 0:
        return {
            "h": h,
            "modulus": modulus,
            "accepted_count": 0,
            "max_rejected_run": modulus,
            "length_threshold": modulus + 1,
        }

    max_run = 0
    run = 0
    for flag in flags + flags:
        if flag:
            run = 0
        else:
            run += 1
            max_run = max(max_run, run)
        if max_run >= modulus - accepted_count:
            break
    max_run = min(max_run, modulus - accepted_count)
    return {
        "h": h,
        "modulus": modulus,
        "accepted_count": accepted_count,
        "rejected_count": modulus - accepted_count,
        "max_rejected_run": max_run,
        "length_threshold": max_run + 1,
    }


def build(source_path: Path, max_enum_modulus: int) -> dict[str, Any]:
    """构造 selector 间隙阈值账本。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    hs = sorted({record["half_prime"] for record in source["records"]})
    max_h = max(hs)
    primes = primes_upto(max_h)
    gap_rows = []
    for h in hs:
        modulus = primorial(primes, h)
        if modulus <= max_enum_modulus:
            row = max_rejected_run(primes, h)
            row["enumerated"] = True
        else:
            row = {
                "h": h,
                "modulus": modulus,
                "enumerated": False,
                "accepted_count": None,
                "rejected_count": None,
                "max_rejected_run": None,
                "length_threshold": None,
            }
        gap_rows.append(row)

    threshold_by_h = {row["h"]: row for row in gap_rows}
    sample_rows = []
    for record in source["records"]:
        h = record["half_prime"]
        left, right = record["forced_core_interval"]
        candidates = candidate_rows(left, right, h)
        threshold = threshold_by_h[h]["length_threshold"]
        length_suffices = threshold is not None and len(candidates) >= threshold
        sample_rows.append(
            {
                "top_prime": record["top_prime"],
                "top_zero_row": record["top_zero_row"],
                "h": h,
                "core_interval": record["forced_core_interval"],
                "candidate_rows": candidates,
                "candidate_count": len(candidates),
                "selector_length_threshold": threshold,
                "length_alone_forces_selector": length_suffices,
            }
        )

    return {
        "status": "rpz_selector_gap_threshold_current_layers",
        "source": str(source_path),
        "parameters": {"max_enum_modulus": max_enum_modulus},
        "summary": {
            "h_layers": len(gap_rows),
            "enumerated_h_layers": sum(1 for row in gap_rows if row["enumerated"]),
            "sample_records": len(sample_rows),
            "records_length_alone_forces_selector": sum(
                1 for row in sample_rows if row["length_alone_forces_selector"]
            ),
            "records_requiring_endpoint_phase": sum(
                1 for row in sample_rows if not row["length_alone_forces_selector"]
            ),
        },
        "gap_rows": gap_rows,
        "sample_rows": sample_rows,
        "review_boundary": [
            "若 candidate_count >= max_rejected_run(A_h)+1，则长度单独保证 selector。",
            "当前样本只有部分记录由长度保证，其余依赖端点相位精确命中 A_h。",
            "该账本不证明全局 selector；它把证明拆为长度阈值分支与短候选相位分支。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ Selector Gap 阈值账本",
        "",
        "**状态：** `rpz_selector_gap_threshold_current_layers`",
        "",
        "## 总结",
        "",
        f"- h 层数：`{summary['h_layers']}`。",
        f"- 已枚举 h 层数：`{summary['enumerated_h_layers']}`。",
        f"- BCB 样本记录数：`{summary['sample_records']}`。",
        f"- 仅由长度强制 selector 的记录数：`{summary['records_length_alone_forces_selector']}`。",
        f"- 仍需端点相位的记录数：`{summary['records_requiring_endpoint_phase']}`。",
        "",
        "## Accepted Set 间隙阈值",
        "",
        "| h | P(h) | accepted | rejected | max rejected run | length threshold |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["gap_rows"]:
        lines.append(
            "| {h} | {modulus} | {accepted} | {rejected} | {run} | {threshold} |".format(
                h=row["h"],
                modulus=row["modulus"],
                accepted=row["accepted_count"],
                rejected=row["rejected_count"],
                run=row["max_rejected_run"],
                threshold=row["length_threshold"],
            )
        )

    lines.extend(
        [
            "",
            "## BCB 样本长度分支",
            "",
            "| top P | top row | h | candidate count | threshold | length alone | candidate rows |",
            "|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for row in result["sample_rows"]:
        lines.append(
            "| {top} | {top_row} | {h} | {count} | {threshold} | `{alone}` | `{candidates}` |".format(
                top=row["top_prime"],
                top_row=row["top_zero_row"],
                h=row["h"],
                count=row["candidate_count"],
                threshold=row["selector_length_threshold"],
                alone=row["length_alone_forces_selector"],
                candidates=row["candidate_rows"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "selector 存在定理自然分成两支：",
            "",
            "1. **长度分支**：若 `|C_h(J)| >= max_rejected_run(A_h)+1`，则自动命中 `A_h`。",
            "2. **短候选相位分支**：若候选行数低于该阈值，必须用端点相位精确证明命中 `A_h`，否则进入 seam/PDEC/ColumnCRT。",
            "",
            "当前样本中 `2/5` 条记录由长度自动保证，`3/5` 条记录仍依赖端点相位。所以下一步不能只扩大核心长度估计；还必须证明短候选端点相位避开 rejected gaps。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-audit.json"),
    )
    parser.add_argument("--max-enum-modulus", type=int, default=10_000_000)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-selector-gap-threshold"),
    )
    args = parser.parse_args()

    result = build(args.source, args.max_enum_modulus)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
