#!/usr/bin/env python3
"""生成 RPZ 短候选端点禁区块公式账本。

用法示例：
  python3 experiments/prime_matrix_rpz_short_phase_block_formula.py

上一账本枚举 `u mod hP(h)` 后发现：当前短候选样本均有 selector，
但完整相位族仍有 all-rejected 端点相位。本脚本把这些端点相位从
枚举集合压成显式块公式。

若核心区间长度为 `ell<2h`，则每个端点 `u` 至多包含一个完整 `h` 行。
对下层行号 `m`，其完整行区间为

  [(m-1)h+1, mh]。

长度 `ell` 的核心起点 `u` 包含该行当且仅当

  mh-ell+1 <= u <= (m-1)h+1。

所以每个 rejected 行相位 `m mod P(h)` 产生一个端点禁区块，块长为
`ell-h+1`。这把短候选硬点化为：证明正式 BCB 端点不落入这些禁区块，
或把对应 rejected 行相位送入 seam/PDEC/ColumnCRT。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_rpz_bcb_accepted_row_selector import candidate_rows
from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    primes_upto,
    primorial,
)


def cyclic_distance_to_set(index: int, flags: list[bool]) -> int | None:
    """返回 `index` 到最近 True 位置的循环距离；若集合空则返回 None。"""
    if not any(flags):
        return None
    if flags[index]:
        return 0
    size = len(flags)
    for distance in range(1, size + 1):
        if flags[(index - distance) % size] or flags[(index + distance) % size]:
            return distance
    return None


def accepted_run_data(phase: int, accepted_flags: list[bool]) -> dict[str, int | bool]:
    """返回包含 `phase` 的循环 accepted 连通块信息。"""
    size = len(accepted_flags)
    accepted = accepted_flags[phase]
    if not accepted:
        return {
            "accepted": False,
            "accepted_run_length": 0,
            "accepted_run_left_steps": 0,
            "accepted_run_right_steps": 0,
            "row_phase_margin_to_rejected": 0,
        }
    if all(accepted_flags):
        return {
            "accepted": True,
            "accepted_run_length": size,
            "accepted_run_left_steps": size,
            "accepted_run_right_steps": size,
            "row_phase_margin_to_rejected": size,
        }

    left_steps = 0
    while accepted_flags[(phase - left_steps - 1) % size]:
        left_steps += 1
    right_steps = 0
    while accepted_flags[(phase + right_steps + 1) % size]:
        right_steps += 1
    return {
        "accepted": True,
        "accepted_run_length": left_steps + right_steps + 1,
        "accepted_run_left_steps": left_steps,
        "accepted_run_right_steps": right_steps,
        "row_phase_margin_to_rejected": min(left_steps, right_steps) + 1,
    }


def endpoint_block_for_row(row: int, h: int, length: int) -> tuple[int, int]:
    """返回端点 `u` 能完整包含下层行 `row` 的闭区间。"""
    return row * h - length + 1, (row - 1) * h + 1


def endpoint_flags(primes: list[int], h: int, length: int) -> list[bool]:
    """返回 `u mod hP(h)` 是否属于 all-rejected 端点禁区。"""
    modulus = primorial(primes, h)
    period = h * modulus
    accepts = acceptance_checker(primes, h)
    rejected = [False] * period
    for u_mod in range(period):
        left = u_mod + period
        right = left + length - 1
        rows = candidate_rows(left, right, h)
        if rows and all(
            not accepts(h, row % modulus)
            for row in rows
        ):
            rejected[u_mod] = True
    return rejected


def audit_family(primes: list[int], h: int, length: int) -> dict[str, Any]:
    """审计一个 `(h,length)` 短候选族的块公式。"""
    modulus = primorial(primes, h)
    period = h * modulus
    window_width = length - h + 1
    accepts = acceptance_checker(primes, h)
    accepted_flags = [accepts(h, phase) for phase in range(modulus)]
    accepted_count = sum(accepted_flags)
    rejected_count = modulus - accepted_count
    no_candidate_formula = max(0, h - window_width) * modulus
    selector_formula = window_width * accepted_count
    all_rejected_formula = window_width * rejected_count

    flags = endpoint_flags(primes, h, length)
    all_rejected_enumerated = sum(flags)
    selector_enumerated = 0
    no_candidate_enumerated = 0
    for u_mod in range(period):
        left = u_mod + period
        right = left + length - 1
        rows = candidate_rows(left, right, h)
        if not rows:
            no_candidate_enumerated += 1
        elif not flags[u_mod]:
            selector_enumerated += 1

    return {
        "h": h,
        "length": length,
        "primorial": modulus,
        "endpoint_period_hP": period,
        "endpoint_window_width": window_width,
        "accepted_row_phase_count": accepted_count,
        "rejected_row_phase_count": rejected_count,
        "no_candidate_formula": no_candidate_formula,
        "selector_formula": selector_formula,
        "all_rejected_formula": all_rejected_formula,
        "no_candidate_enumerated": no_candidate_enumerated,
        "selector_enumerated": selector_enumerated,
        "all_rejected_enumerated": all_rejected_enumerated,
        "block_formula_matches_enumeration": (
            no_candidate_formula == no_candidate_enumerated
            and selector_formula == selector_enumerated
            and all_rejected_formula == all_rejected_enumerated
        ),
    }


def audit_actual_record(primes: list[int], row: dict[str, Any]) -> dict[str, Any]:
    """审计当前实际短候选样本相对端点禁区块的余量。"""
    h = row["h"]
    length = row["length"]
    modulus = primorial(primes, h)
    u_mod = row["u_mod_hP"]
    candidate = row["candidate_rows"][0] if row["candidate_rows"] else None
    accepts = acceptance_checker(primes, h)
    accepted_flags = [accepts(h, phase) for phase in range(modulus)]
    rejected_endpoint_flags = endpoint_flags(primes, h, length)

    block_data: dict[str, Any] = {}
    if candidate is not None:
        block_left, block_right = endpoint_block_for_row(candidate, h, length)
        block_data = {
            "candidate_row": candidate,
            "candidate_phase_mod_primorial": candidate % modulus,
            "candidate_accepted": accepts(h, candidate % modulus),
            "endpoint_block": [block_left, block_right],
            "endpoint_offset_from_block_left": row["u"] - block_left,
            "endpoint_offset_to_block_right": block_right - row["u"],
            **accepted_run_data(candidate % modulus, accepted_flags),
        }

    return {
        "top_prime": row["top_prime"],
        "top_zero_row": row["top_zero_row"],
        "h": h,
        "length": length,
        "u": row["u"],
        "u_mod_hP": u_mod,
        "endpoint_distance_to_all_rejected": cyclic_distance_to_set(
            u_mod,
            rejected_endpoint_flags,
        ),
        **block_data,
    }


def build(short_path: Path) -> dict[str, Any]:
    """构造短候选端点禁区块公式账本。"""
    short = json.loads(short_path.read_text(encoding="utf-8"))
    max_h = max(row["h"] for row in short["actual_short_rows"])
    primes = primes_upto(max_h)
    family_keys = sorted(
        {(row["h"], row["length"]) for row in short["actual_short_rows"]}
    )
    family_rows = [audit_family(primes, h, length) for h, length in family_keys]
    actual_rows = [audit_actual_record(primes, row) for row in short["actual_short_rows"]]
    return {
        "status": "rpz_short_candidate_endpoint_forbidden_block_formula",
        "source": str(short_path),
        "summary": {
            "families": len(family_rows),
            "actual_short_records": len(actual_rows),
            "families_with_formula_match": sum(
                1 for row in family_rows if row["block_formula_matches_enumeration"]
            ),
            "actual_records_accepted": sum(
                1 for row in actual_rows if row.get("candidate_accepted")
            ),
        },
        "family_rows": family_rows,
        "actual_rows": actual_rows,
        "review_boundary": [
            "当 length<2h 时，每个端点最多包含一个完整 h 行。",
            "all-rejected 端点集合等于 rejected 行相位产生的闭区间块并集。",
            "当前实际短候选端点均落在 accepted 行相位块内。",
            "全局仍需证明正式 BCB 端点相位避开 rejected 行相位块，或闭合对应 seam/PDEC/ColumnCRT 出口。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 短候选端点禁区块公式账本",
        "",
        "**状态：** `rpz_short_candidate_endpoint_forbidden_block_formula`",
        "",
        "## 总结",
        "",
        f"- 短候选族数：`{summary['families']}`。",
        f"- 块公式匹配枚举的族数：`{summary['families_with_formula_match']}`。",
        f"- 实际短候选记录数：`{summary['actual_short_records']}`。",
        f"- 实际候选行 accepted 数：`{summary['actual_records_accepted']}`。",
        "",
        "## 块公式",
        "",
        "若 `length<2h`，每个端点 `u` 最多包含一个完整 `h` 行。行号 `m` 的完整行区间为",
        "",
        "```text",
        "[(m-1)h+1, mh]。",
        "```",
        "",
        "长度为 `length` 的核心起点 `u` 包含该行当且仅当",
        "",
        "```text",
        "mh-length+1 <= u <= (m-1)h+1。",
        "```",
        "",
        "因此每个 rejected 行相位给出一个端点禁区块，块长为 `length-h+1`。",
        "",
        "## 族公式核验",
        "",
        "| h | length | P(h) | period hP(h) | block width | accepted phases | rejected phases | no-candidate | selector | all-rejected | formula match |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["family_rows"]:
        lines.append(
            "| {h} | {length} | {modulus} | {period} | {width} | {accepted} | {rejected} | {none} | {selector} | {all_rejected} | `{match}` |".format(
                h=row["h"],
                length=row["length"],
                modulus=row["primorial"],
                period=row["endpoint_period_hP"],
                width=row["endpoint_window_width"],
                accepted=row["accepted_row_phase_count"],
                rejected=row["rejected_row_phase_count"],
                none=row["no_candidate_formula"],
                selector=row["selector_formula"],
                all_rejected=row["all_rejected_formula"],
                match=row["block_formula_matches_enumeration"],
            )
        )

    lines.extend(
        [
            "",
            "## 实际端点余量",
            "",
            "| top P | top row | h | length | u mod hP | candidate | phase | accepted run | row margin | endpoint block offset | distance to all-rejected |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|",
        ]
    )
    for row in result["actual_rows"]:
        lines.append(
            "| {top} | {top_row} | {h} | {length} | {u_mod} | {candidate} | {phase} | {run} | {margin} | `{left}/{right}` | {dist} |".format(
                top=row["top_prime"],
                top_row=row["top_zero_row"],
                h=row["h"],
                length=row["length"],
                u_mod=row["u_mod_hP"],
                candidate=row.get("candidate_row"),
                phase=row.get("candidate_phase_mod_primorial"),
                run=row.get("accepted_run_length"),
                margin=row.get("row_phase_margin_to_rejected"),
                left=row.get("endpoint_offset_from_block_left"),
                right=row.get("endpoint_offset_to_block_right"),
                dist=row["endpoint_distance_to_all_rejected"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "短候选分支已经从大规模端点枚举压缩为一阶块公式：rejected 行相位乘以端点块宽。",
            "当前实际端点均在 accepted 行相位块内，且到 all-rejected 端点集合的循环距离为正。",
            "但这仍不是全局闭合；下一步必须从正式 BCB 构造推出 candidate row phase 属于 `A_h`，否则仍需调用 seam/PDEC/ColumnCRT 出口证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--short-ledger",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-short-candidate-phase-ledger.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-short-phase-block-formula"),
    )
    args = parser.parse_args()

    result = build(args.short_ledger)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
