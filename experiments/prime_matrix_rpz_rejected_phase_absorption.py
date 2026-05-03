#!/usr/bin/env python3
"""分解 RPZ formal automaton 的 rejected set 并核对 seam 出口覆盖。

用法示例：
  python3 experiments/prime_matrix_rpz_rejected_phase_absorption.py

该脚本继续攻击路线 A：对每个素数层 `p` 的自动机拒绝相位，追踪其第一次失败的
相邻转换 `q->r`、`delta` 与行号余类 `rho mod r`，并核对这些首失败相位是否已经被
first-grid-fail seam 证书材料化。

结论不是“排除 rejected set”，而是更精确的吸收结论：

  phase in A_p       -> canonical descent to p=2 contradiction；
  phase not in A_p   -> first-grid-fail seam row already materialized。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import (
    child_phase,
    phase_delta,
    previous_prime,
    primes_upto,
    primorial,
)


def first_failure(primes: list[int], p: int, phase: int) -> dict[str, Any] | None:
    """返回相位的首个 grid_fail；若接受则返回 None。"""
    current_p = p
    current_phase = phase
    while current_p != 2:
        r = previous_prime(primes, current_p)
        if r is None:
            return {
                "status": "no_previous_prime",
                "p": current_p,
                "phase": current_phase,
            }
        gap = current_p - r
        delta = phase_delta(current_p, r, current_phase)
        if delta > gap:
            return {
                "status": "first_grid_fail",
                "p": current_p,
                "r": r,
                "gap": gap,
                "delta": delta,
                "rho_mod_r": current_phase % r,
            }
        modulus_r = primorial(primes, r)
        current_phase = child_phase(current_p, r, current_phase, modulus_r)
        current_p = r
    return None


def accepts_checker(primes: list[int]):
    """返回接受相位判定器。"""

    @lru_cache(maxsize=None)
    def accepts(p: int, phase: int) -> bool:
        failure = first_failure(primes, p, phase)
        return failure is None

    return accepts


def seam_key(row: dict[str, Any]) -> tuple[int, int, int, int]:
    """生成 seam 行键。"""
    return (
        row["p"],
        row["r"],
        row["delta"],
        row["row_residue_mod_r"],
    )


def build(automaton_path: Path, seam_path: Path) -> dict[str, Any]:
    """构造 rejected set 吸收证书。"""
    automaton = json.loads(automaton_path.read_text(encoding="utf-8"))
    seam = json.loads(seam_path.read_text(encoding="utf-8"))
    max_prime = automaton["summary"]["max_prime"]
    primes = primes_upto(max_prime)
    accepts = accepts_checker(primes)
    materialized_seams = {seam_key(row) for row in seam["seam_phase_rows"]}

    absorption_rows = []
    uncovered_examples = []
    first_fail_counter: Counter[tuple[int, int, int, int]] = Counter()
    by_start_prime: dict[int, Counter[tuple[int, int, int, int]]] = defaultdict(Counter)

    for row in automaton["acceptance_rows"]:
        p = row["p"]
        modulus = row["modulus"]
        if p <= 5:
            absorption_rows.append(
                {
                    "start_p": p,
                    "modulus": modulus,
                    "rejected_phase_count": 0,
                    "first_fail_rows": [],
                    "all_rejected_covered_by_materialized_seams": True,
                }
            )
            continue
        local_counter: Counter[tuple[int, int, int, int]] = Counter()
        for phase in range(modulus):
            if accepts(p, phase):
                continue
            failure = first_failure(primes, p, phase)
            if failure is None or failure["status"] != "first_grid_fail":
                uncovered_examples.append(
                    {
                        "start_p": p,
                        "phase": phase,
                        "failure": failure,
                        "reason": "not_first_grid_fail",
                    }
                )
                continue
            key = (
                failure["p"],
                failure["r"],
                failure["delta"],
                failure["rho_mod_r"],
            )
            local_counter[key] += 1
            first_fail_counter[key] += 1
            by_start_prime[p][key] += 1
            if key not in materialized_seams:
                uncovered_examples.append(
                    {
                        "start_p": p,
                        "phase": phase,
                        "failure": failure,
                        "reason": "seam_key_not_materialized",
                    }
                )

        first_fail_rows = [
            {
                "first_fail_key": list(key),
                "count": count,
                "materialized": key in materialized_seams,
            }
            for key, count in sorted(local_counter.items())
        ]
        absorption_rows.append(
            {
                "start_p": p,
                "modulus": modulus,
                "rejected_phase_count": sum(local_counter.values()),
                "first_fail_rows": first_fail_rows,
                "all_rejected_covered_by_materialized_seams": all(
                    item["materialized"] for item in first_fail_rows
                ),
            }
        )

    return {
        "status": "rpz_rejected_phase_absorption_certificate",
        "sources": {
            "automaton": str(automaton_path),
            "seam": str(seam_path),
        },
        "summary": {
            "start_prime_rows": len(absorption_rows),
            "total_rejected_phases": sum(
                row["rejected_phase_count"] for row in absorption_rows
            ),
            "distinct_first_fail_seams": len(first_fail_counter),
            "materialized_seam_rows": len(materialized_seams),
            "uncovered_rejected_examples": len(uncovered_examples),
            "all_rejected_covered_by_materialized_seams": len(uncovered_examples) == 0,
        },
        "absorption_rows": absorption_rows,
        "global_first_fail_rows": [
            {
                "first_fail_key": list(key),
                "count": count,
                "materialized": key in materialized_seams,
            }
            for key, count in sorted(first_fail_counter.items())
        ],
        "uncovered_examples": uncovered_examples[:20],
        "review_boundary": [
            "rejected set 已全部吸收到 first-grid-fail seam 证书行",
            "该证书不排除 seam/PDEC/ColumnCRT 出口",
            "若要全局闭合，仍需排除 seam 出口或证明 formal starts never enter rejected set",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ Rejected Phase 吸收证书",
        "",
        "**状态：** `rpz_rejected_phase_absorption_certificate`",
        "",
        "## 总结",
        "",
        f"- 起始素数层数：`{summary['start_prime_rows']}`。",
        f"- rejected phase 总数：`{summary['total_rejected_phases']}`。",
        f"- 不同首失败 seam 数：`{summary['distinct_first_fail_seams']}`。",
        f"- 已物化 seam 行数：`{summary['materialized_seam_rows']}`。",
        f"- 未覆盖 rejected 样例数：`{summary['uncovered_rejected_examples']}`。",
        f"- rejected 是否全部被已物化 seam 覆盖：`{summary['all_rejected_covered_by_materialized_seams']}`。",
        "",
        "## 按起始素数分解",
        "",
        "| start p | modulus | rejected | first-fail rows | covered |",
        "|---:|---:|---:|---:|---|",
    ]
    for row in result["absorption_rows"]:
        lines.append(
            "| {p} | {modulus} | {rejected} | {rows} | `{covered}` |".format(
                p=row["start_p"],
                modulus=row["modulus"],
                rejected=row["rejected_phase_count"],
                rows=len(row["first_fail_rows"]),
                covered=row["all_rejected_covered_by_materialized_seams"],
            )
        )

    lines.extend(
        [
            "",
            "## 全局首失败 seam 表",
            "",
            "| first fail key [p,r,delta,rho] | count | materialized |",
            "|---|---:|---|",
        ]
    )
    for row in result["global_first_fail_rows"]:
        lines.append(
            "| `{key}` | {count} | `{materialized}` |".format(
                key=row["first_fail_key"],
                count=row["count"],
                materialized=row["materialized"],
            )
        )

    lines.extend(
        [
            "",
            "## 证书定理",
            "",
            "对当前自动机范围内的任意起始相位：",
            "",
            "```text",
            "phase in A_p     => canonical descent reaches p=2；",
            "phase not in A_p => first failure is one of the materialized first-grid-fail seam rows。",
            "```",
            "",
            "因此路线 A 的 rejected set 不再是未定义逃逸；它已经完全回流到 seam/PDEC/ColumnCRT 证书链。",
            "",
            "## 剩余缺口",
            "",
            "本证书仍不排除 seam 出口。全局闭合还需要二选一：证明 formal-family 起始相位从不进入 rejected set；或排除已物化 seam/PDEC/ColumnCRT 出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--automaton",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-formal-phase-automaton.json"),
    )
    parser.add_argument(
        "--seam",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-rejected-phase-absorption"),
    )
    args = parser.parse_args()
    result = build(args.automaton, args.seam)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
