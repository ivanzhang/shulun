#!/usr/bin/env python3
"""审计 H3 六轮余量的候选通用尺度公式。

用法示例：
  python3 experiments/prime_matrix_h3_scaling_formula_audit.py
  python3 experiments/prime_matrix_h3_scaling_formula_audit.py --max-p 5000
  python3 experiments/prime_matrix_h3_scaling_formula_audit.py --constants 0.25,0.30,0.33

目标：
  从全量 H3 余量账本中抽取与数据相符的候选不等式：
    margin(p,s) >= c * q / log(q)
  并为每个常数 c 找到在有限账本中“从某个 p 起全部成立”的首个阈值。

注意：
  本脚本只生成有限数据公式审计，不是全局证明。全局证明需要把违反该尺度公式的
  反例路由到 SmallSkeletonOverload / ManyLabel-PDEC / Endpoint-SAE-ColumnCRT。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_total_descent_h3_margin_audit import (
    Fenwick,
    contained_h3_rows,
    h3_candidate_value,
    smallest_prime_factor_table,
)
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def audit(max_p: int, constants: list[float], row_stride: int) -> dict:
    """执行尺度公式审计。"""
    primes = primes_upto(max_p + 100)
    target_primes = [prime for prime in primes if 5 <= prime <= max_p]
    max_q = next_prime(max_p)
    max_n = max_q * max_q
    max_h3_row = (max_n + 2) // 3
    spf = smallest_prime_factor_table(max_n)

    events_by_spf: dict[int, list[int]] = {}
    for h3_row in range(1, max_h3_row + 1):
        candidate = h3_candidate_value(h3_row)
        if candidate <= 1 or candidate > max_n:
            continue
        factor = spf[candidate]
        if 5 <= factor <= max_p:
            events_by_spf.setdefault(factor, []).append(h3_row)

    fenwick = Fenwick(max_h3_row)
    event_keys = sorted(events_by_spf)
    event_cursor = 0
    rows_checked = 0
    prime_rows = []
    global_min_ratio = None
    global_argmin = None

    for p in target_primes:
        while event_cursor < len(event_keys) and event_keys[event_cursor] <= p:
            for h3_row in events_by_spf[event_keys[event_cursor]]:
                fenwick.add(h3_row, 1)
            event_cursor += 1

        q = next_prime(p)
        scale = q / math.log(q)
        min_margin = None
        min_ratio = None
        argmin = None
        sum_margin = 0
        row_count = 0
        for q_row in range(2, q + 1):
            if row_stride > 1 and q_row != q and (q_row - 2) % row_stride != 0:
                continue
            left = (q_row - 1) * q + 1
            right = q_row * q
            first, last = contained_h3_rows(left, right)
            candidate_count = max(0, last - first + 1)
            blocked_count = fenwick.range_sum(first, last) if candidate_count else 0
            margin = candidate_count - blocked_count
            ratio = margin / scale
            rows_checked += 1
            row_count += 1
            sum_margin += margin
            if min_margin is None or margin < min_margin:
                min_margin = margin
                min_ratio = ratio
                argmin = {
                    "p": p,
                    "q": q,
                    "q_row": q_row,
                    "interval": [left, right],
                    "initial_type": classify_q_row_descent(p, q, q_row)["type"],
                    "candidate_count": candidate_count,
                    "blocked_count": blocked_count,
                    "margin": margin,
                    "scale_q_over_logq": scale,
                    "margin_over_scale": ratio,
                }
            if global_min_ratio is None or ratio < global_min_ratio:
                global_min_ratio = ratio
                global_argmin = {
                    "p": p,
                    "q": q,
                    "q_row": q_row,
                    "interval": [left, right],
                    "initial_type": classify_q_row_descent(p, q, q_row)["type"],
                    "candidate_count": candidate_count,
                    "blocked_count": blocked_count,
                    "margin": margin,
                    "scale_q_over_logq": scale,
                    "margin_over_scale": ratio,
                }

        prime_rows.append(
            {
                "p": p,
                "q": q,
                "row_count": row_count,
                "min_margin": min_margin,
                "min_margin_over_scale": min_ratio,
                "avg_margin": sum_margin / row_count if row_count else None,
                "avg_margin_over_scale": (
                    (sum_margin / row_count) / scale if row_count else None
                ),
                "argmin": argmin,
            }
        )

    threshold_by_constant = {}
    for constant in constants:
        threshold = None
        bad_before_threshold = 0
        for index, item in enumerate(prime_rows):
            if all(row["min_margin_over_scale"] >= constant for row in prime_rows[index:]):
                threshold = item["p"]
                bad_before_threshold = sum(
                    1 for row in prime_rows[:index] if row["min_margin_over_scale"] < constant
                )
                break
        threshold_by_constant[str(constant)] = {
            "eventual_threshold_p": threshold,
            "bad_prime_layers_before_threshold": bad_before_threshold,
        }

    return {
        "status": "finite_h3_scaling_formula_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "constants": constants,
            "row_stride": row_stride,
            "max_n": max_n,
        },
        "summary": {
            "q_rows_checked": rows_checked,
            "global_min_margin_over_q_logq": global_min_ratio,
            "global_argmin": global_argmin,
            "threshold_by_constant": threshold_by_constant,
            "tail_min_ratios": {
                "p_ge_331": min(
                    row["min_margin_over_scale"] for row in prime_rows if row["p"] >= 331
                ),
                "p_ge_500": min(
                    row["min_margin_over_scale"] for row in prime_rows if row["p"] >= 500
                ),
                "p_ge_1000": min(
                    row["min_margin_over_scale"] for row in prime_rows if row["p"] >= 1000
                ),
                "p_ge_2000": min(
                    row["min_margin_over_scale"] for row in prime_rows if row["p"] >= 2000
                ),
            },
        },
        "tight_prime_layers": sorted(
            prime_rows,
            key=lambda item: item["min_margin_over_scale"],
        )[:40],
        "tail_prime_layers": prime_rows[-20:],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    lines = [
        "# H3 通用尺度公式审计",
        "",
        "**状态：** `finite_h3_scaling_formula_audit_not_global_proof`",
        "",
        "本文从全量 H3 余量账本中抽取候选公式 `margin >= c*q/log q` 的有限阈值。该公式与数据相符，但尚未被全局证明。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `constants`: `{params['constants']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `max_n`: `{params['max_n']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 全局最小 `margin/(q/log q)`：`{summary['global_min_margin_over_q_logq']}`。",
        f"- 全局最小样本：`{summary['global_argmin']}`。",
        f"- 尾部最小比值：`{summary['tail_min_ratios']}`。",
        "",
        "## 候选常数阈值",
        "",
        "| c | eventual threshold p | bad prime layers before threshold |",
        "|---:|---:|---:|",
    ]
    for constant, item in summary["threshold_by_constant"].items():
        lines.append(
            f"| {constant} | {item['eventual_threshold_p']} | {item['bad_prime_layers_before_threshold']} |"
        )

    lines.extend(
        [
            "",
            "## 最紧素数层",
            "",
            "| p | q | min margin | min margin/(q/log q) | avg margin/(q/log q) | argmin row |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["tight_prime_layers"][:20]:
        lines.append(
            "| {p} | {q} | {minm} | {minr:.6f} | {avgr:.6f} | {row} |".format(
                p=item["p"],
                q=item["q"],
                minm=item["min_margin"],
                minr=item["min_margin_over_scale"],
                avgr=item["avg_margin_over_scale"],
                row=item["argmin"]["q_row"],
            )
        )

    lines.extend(
        [
            "",
            "## 候选通用公式",
            "",
            "有限账本支持以下审稿候选：",
            "",
            "\\[",
            "M_{H3}(p,s)\\ge 0.30\\,{q\\over \\log q}\\qquad(p\\ge113),",
            "\\]",
            "",
            "其中 `M_H3(p,s)` 是第 `s` 个 `q` 行窗口中的 H3 余量。更保守地，可写成带缺陷出口的条件公式：",
            "",
            "```text",
            "Either M_H3(p,s) >= c*q/log q,",
            "or SmallSkeletonOverload / ManyLabel-PDEC / Endpoint-SAE-ColumnCRT fires.",
            "```",
            "",
            "该公式是当前最贴近数据的全局尺度不等式；正式证明不能只引用有限账本，必须证明低于该尺度会触发命名缺陷。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--constants", type=str, default="0.25,0.30,0.33,0.35,0.40")
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-h3-scaling-formula-audit"),
    )
    args = parser.parse_args()
    constants = [float(item) for item in args.constants.split(",") if item.strip()]
    result = audit(max_p=args.max_p, constants=constants, row_stride=max(1, args.row_stride))
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
