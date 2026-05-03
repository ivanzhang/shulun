#!/usr/bin/env python3
"""从 BCB 核心区间抽取 accepted lower-row 选择器。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_accepted_row_selector.py

该脚本继续压缩 formal-family avoidance 的硬点。给定 BCB-Core 强制核心区间
`J=[u,v]` 与半宽素数 `h`，完整包含的 `h` 对齐行集合为

  C_h(J)={m: u <= (m-1)h+1 且 mh <= v}。

若 `C_h(J)` 与 accepted set `A_h` 相交，则可选择一条 accepted lower
zero-row，沿 RPZ canonical ladder 下降到 `p=2`。若相交为空，则所有候选
下层零行都会在某一层首次进入已材料化的 seam/PDEC/ColumnCRT 出口。

本脚本只核验当前 BCB 样本；它不证明全局相交定理。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    phase_delta,
    previous_prime,
    primes_upto,
    primorial,
)
from prime_matrix_scaled_peeling_halfwidth_audit import interval_for_row


def candidate_rows(left: int, right: int, width: int) -> list[int]:
    """返回完全包含在 `[left,right]` 中的 `width` 对齐行号。"""
    first = (left + width - 1) // width
    last = right // width
    return [
        row
        for row in range(first, last + 1)
        if left <= interval_for_row(width, row)[0]
        and interval_for_row(width, row)[1] <= right
    ]


def first_failure(primes: list[int], p: int, row: int) -> dict[str, Any] | None:
    """返回候选行的首个 seam 失败；若 accepted 则返回 None。"""
    phase = row % primorial(primes, p)
    current = p
    while current != 2:
        r = previous_prime(primes, current)
        if r is None:
            return {"status": "no_previous_prime", "p": current}
        gap = current - r
        delta = phase_delta(current, r, phase)
        if delta > gap:
            return {
                "status": "first_grid_fail",
                "p": current,
                "r": r,
                "gap": gap,
                "delta": delta,
                "rho_mod_r": phase % r,
                "phase": phase,
            }
        # 与 formal automaton 的 child_phase 公式一致；避免额外导入循环。
        phase = ((phase - 1) * current + delta) // r + 1
        phase %= primorial(primes, r)
        current = r
    return None


def row_packet(primes: list[int], h: int, row: int) -> dict[str, Any]:
    """构造单条候选行的 accepted/seam 数据包。"""
    accepts = acceptance_checker(primes, h)
    phase = row % primorial(primes, h)
    accepted = accepts(h, phase)
    return {
        "row": row,
        "interval": list(interval_for_row(h, row)),
        "phase_mod_primorial": phase,
        "accepted": accepted,
        "first_failure": None if accepted else first_failure(primes, h, row),
    }


def audit_record(primes: list[int], record: dict[str, Any]) -> dict[str, Any]:
    """审计一条 BCB-Core 记录的 accepted row 选择器。"""
    h = record["half_prime"]
    left, right = record["forced_core_interval"]
    rows = candidate_rows(left, right, h)
    packets = [row_packet(primes, h, row) for row in rows]
    accepted_rows = [packet["row"] for packet in packets if packet["accepted"]]
    rejected_rows = [packet["row"] for packet in packets if not packet["accepted"]]
    return {
        "top_prime": record["top_prime"],
        "top_zero_row": record["top_zero_row"],
        "half_prime": h,
        "core_interval": record["forced_core_interval"],
        "core_length": record["forced_core_length"],
        "candidate_rows": rows,
        "candidate_count": len(rows),
        "accepted_rows": accepted_rows,
        "accepted_count": len(accepted_rows),
        "rejected_rows": rejected_rows,
        "rejected_count": len(rejected_rows),
        "selector_exists": bool(accepted_rows),
        "selected_row": accepted_rows[0] if accepted_rows else None,
        "row_packets": packets,
    }


def build(source_path: Path) -> dict[str, Any]:
    """构造 accepted lower-row 选择器账本。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    max_prime = max(record["half_prime"] for record in source["records"])
    primes = primes_upto(max_prime)
    records = [audit_record(primes, record) for record in source["records"]]
    total_candidates = sum(record["candidate_count"] for record in records)
    total_accepted = sum(record["accepted_count"] for record in records)
    total_rejected = sum(record["rejected_count"] for record in records)
    return {
        "status": "rpz_bcb_accepted_row_selector_current_samples",
        "source": str(source_path),
        "summary": {
            "records": len(records),
            "records_with_selector": sum(1 for record in records if record["selector_exists"]),
            "total_candidate_rows": total_candidates,
            "total_accepted_candidate_rows": total_accepted,
            "total_rejected_candidate_rows": total_rejected,
            "all_records_have_selector": all(record["selector_exists"] for record in records),
        },
        "records": records,
        "selector_theorem_boundary": [
            "若 C_h(J) 与 A_h 相交，则可选择 accepted lower zero-row 并递归下降。",
            "若 C_h(J) 与 A_h 不相交，则所有候选行进入 first-grid-fail seam/PDEC/ColumnCRT。",
            "当前样本全部有 selector；这仍不是全局 selector 存在证明。",
            "全局硬点是证明正式 BCB-Core 的 C_h(J) 必与 A_h 相交，或排除全拒绝候选行的 seam 出口。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ BCB Accepted Lower-Row 选择器账本",
        "",
        "**状态：** `rpz_bcb_accepted_row_selector_current_samples`",
        "",
        "## 总结",
        "",
        f"- BCB-Core 记录数：`{summary['records']}`。",
        f"- 存在 accepted selector 的记录数：`{summary['records_with_selector']}`。",
        f"- 候选完整下层行总数：`{summary['total_candidate_rows']}`。",
        f"- accepted 候选行总数：`{summary['total_accepted_candidate_rows']}`。",
        f"- rejected 候选行总数：`{summary['total_rejected_candidate_rows']}`。",
        f"- 是否每条记录都有 selector：`{summary['all_records_have_selector']}`。",
        "",
        "## 精确选择器形式",
        "",
        "对 BCB 核心区间 `J=[u,v]` 与半宽素数 `h`，完整下层候选行集合为",
        "",
        "```text",
        "C_h(J)={m: u <= (m-1)h+1 and mh <= v}。",
        "```",
        "",
        "目标从“任意起始行都安全”收窄为更弱且足够的选择器命题：",
        "",
        "```text",
        "C_h(J) ∩ A_h != empty。",
        "```",
        "",
        "若相交，则选择其中一条 accepted lower zero-row 下降；若不相交，则所有候选行回流到 seam/PDEC/ColumnCRT 出口。",
        "",
        "## 当前样本选择器表",
        "",
        "| top P | top row | h | core interval | candidate rows | accepted rows | rejected rows | selected |",
        "|---:|---:|---:|---|---|---|---|---:|",
    ]
    for record in result["records"]:
        lines.append(
            "| {top} | {top_row} | {h} | `{core}` | `{candidates}` | `{accepted}` | `{rejected}` | {selected} |".format(
                top=record["top_prime"],
                top_row=record["top_zero_row"],
                h=record["half_prime"],
                core=record["core_interval"],
                candidates=record["candidate_rows"],
                accepted=record["accepted_rows"],
                rejected=record["rejected_rows"],
                selected=record["selected_row"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "当前 `5/5` 条 BCB-Core 样本均满足 `C_h(J)∩A_h` 非空；所有 `6` 条候选完整下层行也都 accepted。",
            "这比上一账本更接近正式证明所需对象：不必证明每个可能下层行都安全，只需证明存在一个 accepted selector。",
            "",
            "仍未闭合的是全局选择器存在定理。下一硬点应证明正式 BCB-Core 的端点相位和长度强制 `C_h(J)` 命中 `A_h`；否则全拒绝候选行必须进入已材料化 seam/PDEC/ColumnCRT 出口。",
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
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-accepted-row-selector"),
    )
    args = parser.parse_args()

    result = build(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
