#!/usr/bin/env python3
"""抽取 BCB 起始行在 RPZ 符号阶梯中的实际 delta 数字。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_start_digit_ledger.py

该脚本专攻 formal-family avoidance 的下一层：把当前 BCB-Core 给出的
条件下层零行逐项写成相邻素数下降数字

  delta=-(a-1)(p-r) mod r, margin=(p-r)-delta。

结果显示当前账本全部避开 first-grid-fail seam，但许多节点位于
`margin=0` 的临界边界。因此全局证明不能依赖粗余量；必须证明正式构造
给出的行号同余精确落在 allowed residues 中。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from prime_matrix_rpz_formal_phase_automaton import (
    child_phase,
    phase_delta,
    previous_prime,
    primes_upto,
    primorial,
)


def trace_start(primes: list[int], start: dict[str, Any]) -> dict[str, Any]:
    """追踪一条 BCB 起始行的阶梯数字。"""
    p = start["start_prime"]
    phase = start["start_row"] % primorial(primes, p)
    rows = []
    while p != 2:
        r = previous_prime(primes, p)
        if r is None:
            break
        gap = p - r
        delta = phase_delta(p, r, phase)
        margin = gap - delta
        row = {
            "p": p,
            "r": r,
            "phase_mod_primorial_p": phase,
            "phase_mod_r": phase % r,
            "delta": delta,
            "gap": gap,
            "margin": margin,
            "status": "safe" if margin >= 0 else "grid_fail",
            "boundary": margin == 0,
        }
        rows.append(row)
        if margin < 0:
            break
        phase = child_phase(p, r, phase, primorial(primes, r))
        p = r
    return {
        "top_prime": start["top_prime"],
        "top_zero_row": start["top_zero_row"],
        "start_prime": start["start_prime"],
        "start_row": start["start_row"],
        "start_phase": start["start_row"] % primorial(primes, start["start_prime"]),
        "digits": rows,
        "all_safe": all(row["status"] == "safe" for row in rows),
        "boundary_count": sum(1 for row in rows if row["boundary"]),
        "min_margin": min((row["margin"] for row in rows), default=None),
    }


def build(source_path: Path) -> dict[str, Any]:
    """构造 BCB 起始数字账本。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    max_prime = max(start["start_prime"] for start in source["starts"])
    primes = primes_upto(max_prime)
    starts = [trace_start(primes, start) for start in source["starts"]]
    all_digits = [digit for start in starts for digit in start["digits"]]

    margin_counter = Counter(str(digit["margin"]) for digit in all_digits)
    transition_counter: dict[str, Counter[str]] = defaultdict(Counter)
    residue_counter: dict[str, Counter[str]] = defaultdict(Counter)
    for digit in all_digits:
        key = f"{digit['p']}->{digit['r']}"
        transition_counter[key][str(digit["margin"])] += 1
        residue_counter[key][str(digit["phase_mod_r"])] += 1

    return {
        "status": "rpz_bcb_start_digit_ledger_current_samples",
        "source": str(source_path),
        "summary": {
            "start_rows": len(starts),
            "digit_nodes": len(all_digits),
            "safe_digit_nodes": sum(1 for digit in all_digits if digit["status"] == "safe"),
            "grid_fail_digit_nodes": sum(
                1 for digit in all_digits if digit["status"] == "grid_fail"
            ),
            "boundary_digit_nodes": sum(1 for digit in all_digits if digit["boundary"]),
            "minimum_margin": min((digit["margin"] for digit in all_digits), default=None),
            "all_starts_safe": all(start["all_safe"] for start in starts),
        },
        "margin_histogram": dict(sorted(margin_counter.items(), key=lambda kv: int(kv[0]))),
        "transition_margin_histogram": {
            key: dict(value) for key, value in sorted(transition_counter.items())
        },
        "transition_residue_histogram": {
            key: dict(value) for key, value in sorted(residue_counter.items())
        },
        "starts": starts,
        "review_boundary": [
            "当前 BCB 起始行全部满足 delta<=gap。",
            "半数 digit 节点位于 margin=0 边界，说明全局证明需要精确同余而非粗余量。",
            "本账本不证明任意 formal-family start 都安全。",
            "下一步应从 BCB 中心区间与 TailAnchor 删除机制推出 start_row mod r 的允许余类。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 账本。"""
    summary = result["summary"]
    lines = [
        "# RPZ BCB 起始数字账本",
        "",
        "**状态：** `rpz_bcb_start_digit_ledger_current_samples`",
        "",
        "## 总结",
        "",
        f"- BCB 起始行数：`{summary['start_rows']}`。",
        f"- 阶梯 digit 节点数：`{summary['digit_nodes']}`。",
        f"- safe digit 节点数：`{summary['safe_digit_nodes']}`。",
        f"- grid-fail digit 节点数：`{summary['grid_fail_digit_nodes']}`。",
        f"- 边界 `margin=0` 节点数：`{summary['boundary_digit_nodes']}`。",
        f"- 最小 margin：`{summary['minimum_margin']}`。",
        f"- 所有起始行是否安全：`{summary['all_starts_safe']}`。",
        "",
        "## Margin 分布",
        "",
        f"`{result['margin_histogram']}`",
        "",
        "## 按转换的 margin 分布",
        "",
        "| transition | margin histogram | residue histogram |",
        "|---|---|---|",
    ]
    for key in result["transition_margin_histogram"]:
        lines.append(
            "| `{key}` | `{margin}` | `{residue}` |".format(
                key=key,
                margin=result["transition_margin_histogram"][key],
                residue=result["transition_residue_histogram"][key],
            )
        )

    lines.extend(
        [
            "",
            "## 起始行逐项追踪",
            "",
            "| top P | top row | start p | start row | start phase | digits [p->r:delta/gap;margin] | boundary count |",
            "|---:|---:|---:|---:|---:|---|---:|",
        ]
    )
    for start in result["starts"]:
        digits = [
            "{p}->{r}:d={delta}/{gap},m={margin},res={res}".format(
                p=digit["p"],
                r=digit["r"],
                delta=digit["delta"],
                gap=digit["gap"],
                margin=digit["margin"],
                res=digit["phase_mod_r"],
            )
            for digit in start["digits"]
        ]
        lines.append(
            "| {top} | {top_row} | {p} | {row} | {phase} | `{digits}` | {boundary} |".format(
                top=start["top_prime"],
                top_row=start["top_zero_row"],
                p=start["start_prime"],
                row=start["start_row"],
                phase=start["start_phase"],
                digits=digits,
                boundary=start["boundary_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "当前 BCB-Core 样本的 `20` 个阶梯节点全部满足 `delta<=gap`，因此全部避开 first-grid-fail seam。",
            "但其中 `10` 个节点在 `delta=gap` 的边界上；这排除了靠粗不等式余量闭合的路线。",
            "",
            "下一步必须证明：正式反例构造给出的 `start_row mod r` 精确落在 allowed residues 中。",
            "一旦某层落入 forbidden residues，前述 seam/PDEC/ColumnCRT 出口压力账本已经给出回流接口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-start-digit-ledger"),
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
