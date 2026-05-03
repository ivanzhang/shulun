#!/usr/bin/env python3
"""审计 TotalDescent-TM 的鸽巢余量不等式。

用法示例：
  python3 experiments/prime_matrix_total_descent_pigeonhole_margin_audit.py
  python3 experiments/prime_matrix_total_descent_pigeonhole_margin_audit.py --max-p 500
  python3 experiments/prime_matrix_total_descent_pigeonhole_margin_audit.py --max-p 2000 --row-stride 25

核心证书：
  对假想 q 零行区间 I 和某个 h<=p，令 C_h(I) 为完整包含在 I 内、且 CRT 头部/尾镜像
  命中的 h 对齐行集合；令 B_h(I) 为其中被复活点 Rev_{h,p}(I) 或 q^2 穿孔击中的行集合。
  若 |C_h(I)|>|B_h(I)|，则存在未被复活点打断的候选 h 行，故强制产生小阶 h×h 方阵零行。

注意：
  这是 TotalDescent-TM 的最窄计数充分条件审计；仍需把有限余量升级为全局不等式。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_scaled_peeling_halfwidth_audit import contained_rows, interval_for_row
from prime_matrix_seam_multilevel_descent_audit import (
    conditional_revived_positions,
    smallest_prime_factor_table,
)
from prime_matrix_seam_tail_mirror_descent_audit import (
    mirror_profile,
    period_rows_by_prime,
)
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def pigeonhole_profile_for_h(
    *,
    left: int,
    right: int,
    h: int,
    p: int,
    periods: dict[int, int],
    spf: list[int],
    terminal_punctures: set[int],
) -> dict:
    """计算固定 h 的候选行、阻断行与余量。"""
    candidate_rows = [
        row
        for row in contained_rows(left, right, h)
        if mirror_profile(row, h, periods[h])["head_or_tail_hit"]
    ]
    candidate_set = set(candidate_rows)
    revived = conditional_revived_positions(
        left=left,
        right=right,
        lower_prime=h,
        upper_prime=p,
        spf=spf,
        terminal_punctures=terminal_punctures,
    )
    blocked_rows = {
        (n + h - 1) // h
        for n in revived
        if (n + h - 1) // h in candidate_set
    }
    margin = len(candidate_rows) - len(blocked_rows)
    return {
        "h": h,
        "candidate_count": len(candidate_rows),
        "blocked_candidate_row_count": len(blocked_rows),
        "margin": margin,
        "candidate_rows": candidate_rows[:20],
        "blocked_rows": sorted(blocked_rows)[:20],
        "revived_count": len(set(revived)),
    }


def best_pigeonhole_profile(
    *,
    p: int,
    q: int,
    q_row: int,
    all_primes: list[int],
    periods: dict[int, int],
    spf: list[int],
    max_levels: int | None,
    min_h: int,
) -> dict:
    """为一条 q 行寻找最佳鸽巢余量层。"""
    left, right = interval_for_row(q, q_row)
    p_index = all_primes.index(p)
    lower_indices = [
        idx for idx in range(p_index, -1, -1) if all_primes[idx] >= min_h
    ]
    if max_levels is not None:
        lower_indices = lower_indices[: max_levels + 1]
    terminal_punctures = {q * q} if q_row == q else set()

    profiles = [
        pigeonhole_profile_for_h(
            left=left,
            right=right,
            h=all_primes[idx],
            p=p,
            periods=periods,
            spf=spf,
            terminal_punctures=terminal_punctures,
        )
        for idx in lower_indices
    ]
    best = max(
        profiles,
        key=lambda item: (
            item["margin"],
            item["candidate_count"],
            -item["blocked_candidate_row_count"],
        ),
    )
    return {
        "p": p,
        "q": q,
        "q_row": q_row,
        "interval": [left, right],
        "terminal_punctures": sorted(terminal_punctures),
        "initial_classification": classify_q_row_descent(p, q, q_row),
        "best_profile": best,
        "pigeonhole_closes": best["margin"] > 0,
        "positive_profiles": sum(1 for profile in profiles if profile["margin"] > 0),
        "profile_count": len(profiles),
    }


def audit(max_p: int, row_stride: int, max_levels: int | None, min_h: int) -> dict:
    """执行鸽巢余量审计。"""
    all_primes = primes_upto(max_p + 100)
    max_q = next_prime(max_p)
    spf = smallest_prime_factor_table(max_q * max_q)
    periods = period_rows_by_prime(all_primes, max_p)
    records = []

    for p in [prime for prime in all_primes if 5 <= prime <= max_p]:
        q = next_prime(p)
        for q_row in range(2, q + 1):
            if row_stride > 1 and (q_row != q) and ((q_row - 2) % row_stride != 0):
                continue
            records.append(
                best_pigeonhole_profile(
                    p=p,
                    q=q,
                    q_row=q_row,
                    all_primes=all_primes,
                    periods=periods,
                    spf=spf,
                    max_levels=max_levels,
                    min_h=min_h,
                )
            )

    closed = [record for record in records if record["pigeonhole_closes"]]
    failures = [record for record in records if not record["pigeonhole_closes"]]
    best_margins = [record["best_profile"]["margin"] for record in records]
    best_h = [record["best_profile"]["h"] for record in records]
    initial_types = Counter(
        record["initial_classification"]["type"] for record in records
    )

    return {
        "status": "finite_total_descent_pigeonhole_margin_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "row_stride": row_stride,
            "max_levels": max_levels,
            "min_h": min_h,
        },
        "summary": {
            "q_rows_checked": len(records),
            "initial_type_counts": dict(sorted(initial_types.items())),
            "pigeonhole_closed": len(closed),
            "pigeonhole_failures": len(failures),
            "closure_fraction": len(closed) / len(records) if records else None,
            "min_best_margin": min(best_margins, default=None),
            "max_best_margin": max(best_margins, default=None),
            "best_h_counts": dict(sorted(Counter(best_h).items())),
            "terminal_puncture_rows": sum(
                1 for record in records if record["terminal_punctures"]
            ),
        },
        "tight_samples": sorted(
            [
                {
                    "p": record["p"],
                    "q": record["q"],
                    "q_row": record["q_row"],
                    "interval": record["interval"],
                    "initial_classification": record["initial_classification"],
                    "terminal_punctures": record["terminal_punctures"],
                    "best_profile": record["best_profile"],
                    "positive_profiles": record["positive_profiles"],
                    "profile_count": record["profile_count"],
                }
                for record in records
            ],
            key=lambda item: (
                item["best_profile"]["margin"],
                item["best_profile"]["candidate_count"],
            ),
        )[:24],
        "failure_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "initial_classification": record["initial_classification"],
                "terminal_punctures": record["terminal_punctures"],
                "best_profile": record["best_profile"],
            }
            for record in failures[:24]
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    best_h_items = list(summary["best_h_counts"].items())
    best_h_excerpt = dict(best_h_items[:20])
    if len(best_h_items) > 20:
        best_h_excerpt["..."] = "完整分布见 JSON"

    lines = [
        "# TotalDescent-TM 鸽巢余量审计",
        "",
        "**状态：** `finite_total_descent_pigeonhole_margin_audit_not_global_proof`",
        "",
        "本文把当前最窄硬点改写为一个显式计数不等式：候选头部/尾镜像 `h` 行数必须严格大于被复活点打断的候选行数。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `max_levels`: `{params['max_levels']}`。",
        f"- `min_h`: `{params['min_h']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 初始分支计数：`{summary['initial_type_counts']}`。",
        f"- 鸽巢闭合数：`{summary['pigeonhole_closed']}`。",
        f"- 鸽巢失败数：`{summary['pigeonhole_failures']}`。",
        f"- 闭合比例：`{summary['closure_fraction']}`。",
        f"- 最小最佳余量：`{summary['min_best_margin']}`。",
        f"- 最大最佳余量：`{summary['max_best_margin']}`。",
        f"- 末行端点穿孔行数：`{summary['terminal_puncture_rows']}`。",
        f"- 最优 h 分布摘录：`{best_h_excerpt}`。",
        "",
        "## 最紧样本",
        "",
        "| p | q | q-row | initial | terminal | h | candidates | blocked rows | margin |",
        "|---:|---:|---:|---|---|---:|---:|---:|---:|",
    ]
    for sample in result["tight_samples"][:16]:
        best = sample["best_profile"]
        lines.append(
            "| {p} | {q} | {row} | `{initial}` | `{terminal}` | {h} | {cand} | {blocked} | {margin} |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                initial=sample["initial_classification"]["type"],
                terminal=sample["terminal_punctures"],
                h=best["h"],
                cand=best["candidate_count"],
                blocked=best["blocked_candidate_row_count"],
                margin=best["margin"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿引理",
            "",
            "设 `C_h(I)` 为完整包含在 `I` 中且满足 `rho<=h` 或 `N_h-rho+1<=h` 的 `h` 对齐行集合。设 `B_h(I)` 为其中含有复活点或端点穿孔的行集合。若",
            "",
            "\\[",
            "|C_h(I)|>|B_h(I)|,",
            "\\]",
            "",
            "则存在一条候选 `h` 行没有被任何复活点打断。由于 `I` 在旧 `p`-筛下为零，该行在 `h`-筛下为零；再由头部/尾镜像条件落入 `h×h` 方阵。",
            "",
            "因此 `TotalDescent-TM` 的当前最窄可审查形式是证明：对任意相邻 `p<q` 与任意 `2<=s<=q`，存在 `h<=p` 使上述严格不等式成立；或证明所有失败相位触发 `SAE/PDEC/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=500)
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument("--max-levels", type=int, default=None)
    parser.add_argument(
        "--min-h",
        type=int,
        default=3,
        help="排除小于该值的下降层；默认排除 h=2 的纯奇偶退化。",
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-total-descent-pigeonhole-margin-audit"),
    )
    args = parser.parse_args()
    result = audit(
        max_p=args.max_p,
        row_stride=max(1, args.row_stride),
        max_levels=args.max_levels,
        min_h=args.min_h,
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
