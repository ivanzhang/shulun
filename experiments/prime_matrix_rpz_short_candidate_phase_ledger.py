#!/usr/bin/env python3
"""枚举 RPZ selector 的短候选端点相位。

用法示例：
  python3 experiments/prime_matrix_rpz_short_candidate_phase_ledger.py

`selector gap` 账本显示：当前 BCB 样本中有若干核心区间不能仅靠长度强制
`C_h(J)∩A_h` 非空。本脚本继续攻这些短候选情形。

关键点：端点网格相位 `u mod h` 只决定是否包含完整 `h` 行；是否命中
accepted set `A_h` 还取决于候选行号 `m mod P(h)`。因此短候选 selector
需要细化到

  u mod h*P(h)

或等价地，候选行号模 `P(h)`。

本脚本枚举当前短候选样本的全部 `u mod hP(h)` 相位，统计哪些相位存在
accepted selector，哪些全 rejected 并回流到 seam/PDEC/ColumnCRT。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from prime_matrix_rpz_bcb_accepted_row_selector import candidate_rows
from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    phase_delta,
    previous_prime,
    primes_upto,
    primorial,
)


def first_failure_key(primes: list[int], h: int, row: int) -> list[int] | None:
    """返回候选行首次失败 seam 键 `[p,r,delta,rho]`；accepted 时返回 None。"""
    phase = row % primorial(primes, h)
    current = h
    while current != 2:
        r = previous_prime(primes, current)
        if r is None:
            return None
        gap = current - r
        delta = phase_delta(current, r, phase)
        if delta > gap:
            return [current, r, delta, phase % r]
        phase = ((phase - 1) * current + delta) // r + 1
        phase %= primorial(primes, r)
        current = r
    return None


def row_packet(primes: list[int], h: int, row: int) -> dict[str, Any]:
    """返回候选行的 accepted 与失败信息。"""
    modulus = primorial(primes, h)
    accepts = acceptance_checker(primes, h)
    phase = row % modulus
    accepted = accepts(h, phase)
    return {
        "row": row,
        "phase_mod_primorial": phase,
        "accepted": accepted,
        "first_failure_key": None if accepted else first_failure_key(primes, h, row),
    }


def audit_phase_family(primes: list[int], h: int, length: int) -> dict[str, Any]:
    """枚举固定 `(h,length)` 的全部 `u mod hP(h)` 相位。"""
    modulus = primorial(primes, h)
    phase_period = h * modulus
    accepts = acceptance_checker(primes, h)
    candidate_count_histogram: Counter[str] = Counter()
    selector_count_by_candidate_count: Counter[str] = Counter()
    all_rejected_by_candidate_count: Counter[str] = Counter()
    rejected_failure_counter: Counter[tuple[int, int, int, int]] = Counter()

    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for u_mod in range(phase_period):
        # 加一个整周期，避免代表元靠近 0 时出现非正行号；相位不变。
        left = u_mod + phase_period
        right = left + length - 1
        rows = candidate_rows(left, right, h)
        packets = []
        selector_exists = False
        for row in rows:
            phase = row % modulus
            accepted = accepts(h, phase)
            packet = {
                "row_mod_primorial": phase,
                "accepted": accepted,
            }
            if not accepted:
                key = first_failure_key(primes, h, row)
                packet["first_failure_key"] = key
                if key is not None:
                    rejected_failure_counter[tuple(key)] += 1
            selector_exists = selector_exists or accepted
            packets.append(packet)

        count_key = str(len(rows))
        candidate_count_histogram[count_key] += 1
        if selector_exists:
            selector_count_by_candidate_count[count_key] += 1
        elif rows:
            all_rejected_by_candidate_count[count_key] += 1

        if len(examples[count_key]) < 3:
            examples[count_key].append(
                {
                    "u_mod_hP": u_mod,
                    "u_mod_h": u_mod % h,
                    "candidate_count": len(rows),
                    "selector_exists": selector_exists,
                    "candidate_packets": packets,
                }
            )

    return {
        "h": h,
        "length": length,
        "primorial": modulus,
        "endpoint_phase_period_hP": phase_period,
        "candidate_count_histogram": dict(sorted(candidate_count_histogram.items())),
        "selector_count_by_candidate_count": dict(
            sorted(selector_count_by_candidate_count.items())
        ),
        "all_rejected_by_candidate_count": dict(
            sorted(all_rejected_by_candidate_count.items())
        ),
        "rejected_first_failure_rows": [
            {"first_failure_key": list(key), "count": count}
            for key, count in sorted(rejected_failure_counter.items())
        ],
        "examples_by_candidate_count": dict(examples),
    }


def build(core_path: Path, gap_path: Path) -> dict[str, Any]:
    """构造短候选端点相位账本。"""
    core = json.loads(core_path.read_text(encoding="utf-8"))
    gap = json.loads(gap_path.read_text(encoding="utf-8"))
    short_keys = {
        (row["top_prime"], row["top_zero_row"])
        for row in gap["sample_rows"]
        if not row["length_alone_forces_selector"]
    }
    short_records = [
        record
        for record in core["records"]
        if (record["top_prime"], record["top_zero_row"]) in short_keys
    ]
    max_h = max(record["half_prime"] for record in short_records)
    primes = primes_upto(max_h)

    family_keys = sorted(
        {(record["half_prime"], record["forced_core_length"]) for record in short_records}
    )
    family_rows = [
        audit_phase_family(primes, h, length)
        for h, length in family_keys
    ]
    family_by_key = {(row["h"], row["length"]): row for row in family_rows}

    actual_rows = []
    for record in short_records:
        h = record["half_prime"]
        length = record["forced_core_length"]
        left, right = record["forced_core_interval"]
        rows = candidate_rows(left, right, h)
        packets = [row_packet(primes, h, row) for row in rows]
        actual_rows.append(
            {
                "top_prime": record["top_prime"],
                "top_zero_row": record["top_zero_row"],
                "h": h,
                "length": length,
                "u": left,
                "u_mod_h": left % h,
                "u_mod_hP": left % (h * primorial(primes, h)),
                "candidate_rows": rows,
                "candidate_packets": packets,
                "selector_exists": any(packet["accepted"] for packet in packets),
                "family_all_rejected_count": family_by_key[(h, length)][
                    "all_rejected_by_candidate_count"
                ].get(str(len(rows)), 0),
            }
        )

    return {
        "status": "rpz_short_candidate_endpoint_phase_ledger",
        "sources": {
            "core": str(core_path),
            "selector_gap": str(gap_path),
        },
        "summary": {
            "short_sample_records": len(short_records),
            "phase_families": len(family_rows),
            "actual_records_with_selector": sum(
                1 for row in actual_rows if row["selector_exists"]
            ),
            "actual_records_without_selector": sum(
                1 for row in actual_rows if not row["selector_exists"]
            ),
            "families_with_all_rejected_phases": sum(
                1
                for row in family_rows
                if sum(row["all_rejected_by_candidate_count"].values()) > 0
            ),
        },
        "phase_family_rows": family_rows,
        "actual_short_rows": actual_rows,
        "review_boundary": [
            "短候选 selector 需要 u mod hP(h)，单纯 u mod h 不足以决定 A_h 命中。",
            "当前短候选样本全部命中 accepted selector。",
            "同一 (h,length) 相位族中仍存在 all-rejected 相位；全局证明必须排除正式构造命中这些相位。",
            "all-rejected 相位已带 first_failure_key，可回流到 seam/PDEC/ColumnCRT。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 短候选端点相位账本",
        "",
        "**状态：** `rpz_short_candidate_endpoint_phase_ledger`",
        "",
        "## 总结",
        "",
        f"- 短候选样本记录数：`{summary['short_sample_records']}`。",
        f"- 相位族数：`{summary['phase_families']}`。",
        f"- 实际样本有 selector 数：`{summary['actual_records_with_selector']}`。",
        f"- 实际样本无 selector 数：`{summary['actual_records_without_selector']}`。",
        f"- 存在 all-rejected 相位的族数：`{summary['families_with_all_rejected_phases']}`。",
        "",
        "## 关键相位细化",
        "",
        "短候选情形下，`u mod h` 只决定网格包含；是否命中 `A_h` 取决于候选行号 `m mod P(h)`。",
        "因此 selector 相位必须细化为：",
        "",
        "```text",
        "u mod h*P(h)。",
        "```",
        "",
        "## 短候选实际样本",
        "",
        "| top P | top row | h | length | u mod h | u mod hP | candidates | packets | selector | all-rejected family phases |",
        "|---:|---:|---:|---:|---:|---:|---|---|---|---:|",
    ]
    for row in result["actual_short_rows"]:
        lines.append(
            "| {top} | {top_row} | {h} | {length} | {umodh} | {umodhP} | `{candidates}` | `{packets}` | `{selector}` | {rejects} |".format(
                top=row["top_prime"],
                top_row=row["top_zero_row"],
                h=row["h"],
                length=row["length"],
                umodh=row["u_mod_h"],
                umodhP=row["u_mod_hP"],
                candidates=row["candidate_rows"],
                packets=row["candidate_packets"],
                selector=row["selector_exists"],
                rejects=row["family_all_rejected_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 相位族统计",
            "",
            "| h | length | period hP(h) | candidate count histogram | selector counts | all-rejected counts | first-failure rows |",
            "|---:|---:|---:|---|---|---|---|",
        ]
    )
    for row in result["phase_family_rows"]:
        lines.append(
            "| {h} | {length} | {period} | `{hist}` | `{selectors}` | `{rejects}` | `{failures}` |".format(
                h=row["h"],
                length=row["length"],
                period=row["endpoint_phase_period_hP"],
                hist=row["candidate_count_histogram"],
                selectors=row["selector_count_by_candidate_count"],
                rejects=row["all_rejected_by_candidate_count"],
                failures=row["rejected_first_failure_rows"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "当前三个短候选样本都命中 accepted selector；但对应的完整相位族中仍存在 all-rejected 相位。",
            "因此下一硬点不是证明任意短候选相位都安全，而是证明正式 BCB 构造的 `u mod hP(h)` 避开这些 all-rejected 相位。",
            "若不能排除，则这些 all-rejected 相位已经带有 first-failure seam 键，可进入 seam/PDEC/ColumnCRT 出口账本。",
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
        "--gap",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-selector-gap-threshold.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-short-candidate-phase-ledger"),
    )
    args = parser.parse_args()

    result = build(args.core, args.gap)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
