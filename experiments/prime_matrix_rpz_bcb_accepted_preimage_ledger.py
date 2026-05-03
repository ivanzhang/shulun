#!/usr/bin/env python3
"""枚举 RPZ-BCB 顶层行 residue 的 accepted preimage。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_accepted_preimage_ledger.py

上一账本给出 BCB 候选下层行相位的 floor 身份。全局剩余硬点可以
表述为：

  formal BCB 的 R mod hP(h) 必须落入 accepted preimage。

本脚本对当前出现的平台参数逐个枚举 `R mod hP(h)`，统计哪些 residue
会诱导 accepted selector，哪些 residue 无候选行，哪些 residue 诱导
rejected 候选行并带 first-failure 出口键。

该账本不声称全局闭合；它把下一证明义务压成显式 residue preimage
排斥或出口证书闭合。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from prime_matrix_rpz_bcb_candidate_phase_identity import phase_from_residue
from prime_matrix_rpz_formal_phase_automaton import (
    acceptance_checker,
    phase_delta,
    previous_prime,
    primes_upto,
    primorial,
)


def first_failure_key_from_phase(
    primes: list[int],
    h: int,
    phase: int,
) -> list[int] | None:
    """返回 accepted 自动机的首个失败键；accepted 时返回 None。"""
    current = h
    current_phase = phase % primorial(primes, h)
    while current != 2:
        r = previous_prime(primes, current)
        if r is None:
            return None
        gap = current - r
        delta = phase_delta(current, r, current_phase)
        if delta > gap:
            return [current, r, delta, current_phase % r]
        current_phase = ((current_phase - 1) * current + delta) // r + 1
        current_phase %= primorial(primes, r)
        current = r
    return None


def cyclic_distance_to_bad(index: int, bad_flags: list[bool]) -> int | None:
    """返回 residue 到最近坏 residue 的循环距离。"""
    if not any(bad_flags):
        return None
    if bad_flags[index]:
        return 0
    size = len(bad_flags)
    for distance in range(1, size + 1):
        if bad_flags[(index - distance) % size] or bad_flags[(index + distance) % size]:
            return distance
    return None


def max_true_run(flags: list[bool]) -> int:
    """返回循环布尔序列中 True 的最大连续段长度。"""
    if not flags:
        return 0
    if all(flags):
        return len(flags)
    doubled = flags + flags
    best = 0
    current = 0
    for value in doubled:
        if value:
            current += 1
            best = max(best, min(current, len(flags)))
        else:
            current = 0
    return best


def residue_status(
    primes: list[int],
    top_prime: int,
    h: int,
    shift_min: int,
    shift_max: int,
    tail_threshold: int,
    top_row_residue: int,
) -> dict[str, Any]:
    """计算一个 `R mod hP(h)` 的 selector 状态。"""
    modulus_h = primorial(primes, h)
    representative = top_row_residue if top_row_residue != 0 else h * modulus_h
    phase_min, phase_max = phase_from_residue(
        representative,
        top_prime,
        h,
        shift_min,
        shift_max,
        tail_threshold,
        modulus_h,
    )
    quotient, remainder = divmod(top_prime, h)
    raw_min = (
        (representative - 1) * quotient
        + ((representative - 1) * remainder + shift_min + tail_threshold + h - 1) // h
        + 1
    )
    raw_max = (
        representative * quotient
        + (representative * remainder + shift_max - tail_threshold) // h
    )
    candidate_count = max(0, raw_max - raw_min + 1)
    if candidate_count == 0:
        return {
            "status": "no_candidate",
            "candidate_count": 0,
            "candidate_phases": [],
            "first_failure_keys": [],
        }

    phases = [(raw_min + offset) % modulus_h for offset in range(candidate_count)]
    accepts = acceptance_checker(primes, h)
    accepted_flags = [accepts(h, phase) for phase in phases]
    if any(accepted_flags):
        status = "selector"
    else:
        status = "all_rejected"
    return {
        "status": status,
        "candidate_count": candidate_count,
        "candidate_phases": phases,
        "accepted_flags": accepted_flags,
        "phase_min_formula": phase_min,
        "phase_max_formula": phase_max,
        "first_failure_keys": [
            first_failure_key_from_phase(primes, h, phase)
            for phase, accepted in zip(phases, accepted_flags)
            if not accepted
        ],
    }


def audit_family(primes: list[int], record: dict[str, Any]) -> dict[str, Any]:
    """枚举一条当前 BCB 参数族的全部 `R mod hP(h)`。"""
    top_prime = record["top_prime"]
    h = record["half_prime"]
    shift_min = min(record["zero_shift_plateau"])
    shift_max = max(record["zero_shift_plateau"])
    tail_threshold = record["tail_threshold"]
    modulus_h = primorial(primes, h)
    period = h * modulus_h
    status_counter: Counter[str] = Counter()
    candidate_count_counter: Counter[str] = Counter()
    failure_counter: Counter[tuple[int, int, int, int]] = Counter()
    bad_flags: list[bool] = []
    selector_flags: list[bool] = []

    for residue in range(period):
        status = residue_status(
            primes,
            top_prime,
            h,
            shift_min,
            shift_max,
            tail_threshold,
            residue,
        )
        status_counter[status["status"]] += 1
        candidate_count_counter[str(status["candidate_count"])] += 1
        is_bad = status["status"] != "selector"
        bad_flags.append(is_bad)
        selector_flags.append(status["status"] == "selector")
        for key in status["first_failure_keys"]:
            if key is not None:
                failure_counter[tuple(key)] += 1

    actual_residue = record["top_zero_row"] % period
    actual_status = residue_status(
        primes,
        top_prime,
        h,
        shift_min,
        shift_max,
        tail_threshold,
        actual_residue,
    )
    return {
        "top_prime": top_prime,
        "half_prime": h,
        "tail_threshold": tail_threshold,
        "shift_min": shift_min,
        "shift_max": shift_max,
        "period_hP": period,
        "status_counts": dict(sorted(status_counter.items())),
        "candidate_count_histogram": dict(sorted(candidate_count_counter.items())),
        "max_bad_residue_run": max_true_run(bad_flags),
        "max_selector_residue_run": max_true_run(selector_flags),
        "first_failure_key_counts": [
            {"first_failure_key": list(key), "count": count}
            for key, count in sorted(failure_counter.items())
        ],
        "actual_top_row": record["top_zero_row"],
        "actual_top_row_mod_hP": actual_residue,
        "actual_status": actual_status,
        "actual_distance_to_bad_residue": cyclic_distance_to_bad(actual_residue, bad_flags),
    }


def build(core_path: Path) -> dict[str, Any]:
    """构造 accepted preimage 账本。"""
    core = json.loads(core_path.read_text(encoding="utf-8"))
    max_h = max(record["half_prime"] for record in core["records"])
    primes = primes_upto(max_h)
    family_rows = [audit_family(primes, record) for record in core["records"]]
    return {
        "status": "rpz_bcb_accepted_top_row_residue_preimage",
        "source": str(core_path),
        "summary": {
            "families": len(family_rows),
            "actual_families_with_selector": sum(
                1 for row in family_rows if row["actual_status"]["status"] == "selector"
            ),
            "families_with_bad_residues": sum(
                1
                for row in family_rows
                if row["status_counts"].get("all_rejected", 0)
                or row["status_counts"].get("no_candidate", 0)
            ),
        },
        "family_rows": family_rows,
        "review_boundary": [
            "accepted preimage 是 formal BCB 需要证明的精确 residue 条件。",
            "当前实际 top row residue 全部落入 selector preimage。",
            "每个参数族仍存在 bad residue，因此该账本不是全局闭合证明。",
            "bad residue 分为 no_candidate 和 all_rejected；后者带 first-failure seam/PDEC/ColumnCRT 键。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ-BCB Accepted Top-Row Residue Preimage 账本",
        "",
        "**状态：** `rpz_bcb_accepted_top_row_residue_preimage`",
        "",
        "## 总结",
        "",
        f"- 参数族数：`{summary['families']}`。",
        f"- 实际样本落入 selector preimage 的族数：`{summary['actual_families_with_selector']}`。",
        f"- 仍存在 bad residue 的族数：`{summary['families_with_bad_residues']}`。",
        "",
        "## 逐族 preimage 统计",
        "",
        "| top P | h | shifts | period hP | status counts | candidate histogram | max bad run | max selector run | actual R mod hP | actual status | dist to bad |",
        "|---:|---:|---|---:|---|---|---:|---:|---:|---|---:|",
    ]
    for row in result["family_rows"]:
        lines.append(
            "| {top} | {h} | `{shifts}` | {period} | `{counts}` | `{hist}` | {bad} | {sel} | {actual} | `{status}` | {dist} |".format(
                top=row["top_prime"],
                h=row["half_prime"],
                shifts=[row["shift_min"], row["shift_max"]],
                period=row["period_hP"],
                counts=row["status_counts"],
                hist=row["candidate_count_histogram"],
                bad=row["max_bad_residue_run"],
                sel=row["max_selector_residue_run"],
                actual=row["actual_top_row_mod_hP"],
                status=row["actual_status"]["status"],
                dist=row["actual_distance_to_bad_residue"],
            )
        )

    lines.extend(
        [
            "",
            "## all-rejected 出口键",
            "",
            "| top P | h | first-failure keys |",
            "|---:|---:|---|",
        ]
    )
    for row in result["family_rows"]:
        lines.append(
            "| {top} | {h} | `{keys}` |".format(
                top=row["top_prime"],
                h=row["half_prime"],
                keys=row["first_failure_key_counts"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "当前实际 top row residue 全部落入 selector preimage，但每个参数族仍有 bad residue。",
            "因此全局证明不能由 preimage 枚举替代；下一义务是证明 formal BCB 反例的 `R mod hP(h)` 避开 bad residue。",
            "若落入 all-rejected residue，则该 residue 已携带 first-failure seam/PDEC/ColumnCRT 出口键；若落入 no-candidate residue，则回到 BCB grid/endpoint 出口。",
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
        default=Path("docs/monograph/prime-matrix-rpz-bcb-accepted-preimage-ledger"),
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
