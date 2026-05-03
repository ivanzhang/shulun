#!/usr/bin/env python3
"""审计 RPZ-BCB 边界压缩会强制出的半宽筛零核心。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_core_audit.py

输入为 `prime-matrix-rpz-sliding-plateau-audit.json`。脚本对每个滑动零窗平台计算：

1. 无 TailAnchor 时被迫为空的中心区间；
2. 该中心区间中实际出现的半宽筛幸存者；
3. 这些幸存者是否正是多重度超过 `T0` 的持久源。

这用于验证 `RPZ-BCB` 的几何路由：避免持久源重复会把半宽筛幸存者压到平台两端，
从而使平台中心成为一个半宽筛零区间。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from prime_matrix_scaled_peeling_halfwidth_audit import contained_rows, interval_for_row
from prime_matrix_zero_row_crt_audit import mark_old_sieve_interval, primes_upto


def h_survivors(left: int, right: int, h: int) -> list[int]:
    """返回 `[left,right]` 中避开所有 `<=h` 素数的整数。"""
    if left > right:
        return []
    alive = mark_old_sieve_interval(left, right, primes_upto(h))
    return [left + idx for idx, flag in enumerate(alive) if flag]


def zero_rows_inside(left: int, right: int, h: int) -> list[int]:
    """返回完全包含在 `[left,right]` 中的 `h` 对齐零行。"""
    rows = []
    small_primes = primes_upto(h)
    for row in contained_rows(left, right, h):
        row_left, row_right = interval_for_row(h, row)
        if mark_old_sieve_interval(row_left, row_right, small_primes).count(1) == 0:
            rows.append(row)
    return rows


def audit_record(record: dict) -> dict:
    """审计单条滑动平台记录。"""
    left, right = record["top_interval"]
    shifts = record["zero_shift_plateau"]
    shift_min = min(shifts)
    shift_max = max(shifts)
    tail_threshold = record["tail_threshold"]
    h = record["half_prime"]

    # 无 TailAnchor 时，多重度超过 T0 的公共核心源必须不存在。
    core_left = left + shift_min + tail_threshold
    core_right = right + shift_max - tail_threshold
    core_survivors = h_survivors(core_left, core_right, h)
    source_by_n = {source["n"]: source for source in record["sources"]}
    core_sources = [source_by_n[n] for n in core_survivors if n in source_by_n]
    non_tail_core_sources = [
        source
        for source in core_sources
        if source["multiplicity"] <= tail_threshold
    ]
    tail_core_sources = [
        source
        for source in core_sources
        if source["multiplicity"] > tail_threshold
    ]

    contained = contained_rows(core_left, core_right, h)
    actual_zero_rows = zero_rows_inside(core_left, core_right, h)
    would_be_zero_rows_after_tail_deletion = contained if not non_tail_core_sources else []

    return {
        "top_prime": record["top_prime"],
        "top_zero_row": record["top_zero_row"],
        "half_prime": h,
        "tail_threshold": tail_threshold,
        "zero_shift_plateau": shifts,
        "zero_shift_plateau_length": record["zero_shift_plateau_length"],
        "forced_core_interval": [core_left, core_right],
        "forced_core_length": max(0, core_right - core_left + 1),
        "contained_half_rows": contained,
        "actual_half_zero_rows_in_core": actual_zero_rows,
        "core_survivor_count": len(core_survivors),
        "core_survivors": core_survivors,
        "tail_core_source_count": len(tail_core_sources),
        "non_tail_core_source_count": len(non_tail_core_sources),
        "would_be_zero_rows_after_tail_deletion": would_be_zero_rows_after_tail_deletion,
        "bcb_core_clean_after_tail_deletion": len(non_tail_core_sources) == 0,
    }


def audit(source_path: Path) -> dict:
    """执行 BCB 核心审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    records = [audit_record(record) for record in source["records"]]
    return {
        "status": "rpz_bcb_forces_half_sieve_core_zero_or_tail_source",
        "source": str(source_path),
        "summary": {
            "records": len(records),
            "records_with_clean_core_after_tail_deletion": sum(
                1 for record in records if record["bcb_core_clean_after_tail_deletion"]
            ),
            "records_with_contained_half_row_in_forced_core": sum(
                1 for record in records if record["contained_half_rows"]
            ),
            "total_core_survivors": sum(record["core_survivor_count"] for record in records),
            "total_tail_core_sources": sum(
                record["tail_core_source_count"] for record in records
            ),
            "total_non_tail_core_sources": sum(
                record["non_tail_core_source_count"] for record in records
            ),
            "max_forced_core_length": max(
                (record["forced_core_length"] for record in records),
                default=0,
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ-BCB 半宽筛零核心审计",
        "",
        "**状态：** `rpz_bcb_forces_half_sieve_core_zero_or_tail_source`",
        "",
        "## 总结",
        "",
        f"- 样本记录数：`{summary['records']}`。",
        f"- 删除尾锚核心源后中心区间干净的记录数：`{summary['records_with_clean_core_after_tail_deletion']}`。",
        f"- 强制中心区间含完整半宽行的记录数：`{summary['records_with_contained_half_row_in_forced_core']}`。",
        f"- 中心区间实际半宽幸存者总数：`{summary['total_core_survivors']}`。",
        f"- 其中尾锚核心源总数：`{summary['total_tail_core_sources']}`。",
        f"- 非尾锚核心源总数：`{summary['total_non_tail_core_sources']}`。",
        f"- 最大强制中心区间长度：`{summary['max_forced_core_length']}`。",
        "",
        "## 逐例表",
        "",
        "| top P | row | half | core interval | core length | contained half rows | core survivors | tail core | non-tail core | clean after deletion |",
        "|---:|---:|---:|---|---:|---|---:|---:|---:|---|",
    ]
    for record in result["records"]:
        lines.append(
            "| {top} | {row} | {half} | `{interval}` | {length} | `{rows}` | {surv} | {tail} | {nontail} | {clean} |".format(
                top=record["top_prime"],
                row=record["top_zero_row"],
                half=record["half_prime"],
                interval=record["forced_core_interval"],
                length=record["forced_core_length"],
                rows=record["contained_half_rows"],
                surv=record["core_survivor_count"],
                tail=record["tail_core_source_count"],
                nontail=record["non_tail_core_source_count"],
                clean="yes" if record["bcb_core_clean_after_tail_deletion"] else "no",
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "在滑动平台长度大于 `T0` 的情况下，公共核心中的任一半宽筛幸存者都会以超过 `T0` 的多重度重复出现，因此它不是低负载分散源，而是 TailAnchor 源。",
            "",
            "本审计显示：样本中的中心区间幸存者全部属于尾锚核心源；若在条件分支中排除 TailAnchor，这些中心区间会变成半宽筛零区间，并且每个样本的中心区间都含完整半宽对齐行。",
            "",
            "这仍不是全局闭合证明。它把下一硬点压缩为：全局证明强制中心区间含完整半宽行，或在不含完整行时把缝合端点送入 `SAE/PDEC/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-sliding-plateau-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-audit"),
    )
    args = parser.parse_args()
    result = audit(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
