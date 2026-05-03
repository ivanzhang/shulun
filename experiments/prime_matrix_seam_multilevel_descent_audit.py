#!/usr/bin/env python3
"""审计缝合零窗继续降阶时是否必然变成完整零行。

用法示例：
  python3 experiments/prime_matrix_seam_multilevel_descent_audit.py
  python3 experiments/prime_matrix_seam_multilevel_descent_audit.py --max-p 200

模型：
  对相邻素数 p<q，假设一条 q 行零窗先降为旧 p-筛下的 seam zero window。
  固定同一数轴区间 I，继续把筛上界从 p 降到更小素数 h。若 I 完整包含某条
  h 对齐行，且剥层复活点不落入该行，则该 h 行被强制成为零行。

注意：
  这是条件模型账本；它检验“seam 必然某层变零行”这一局部机制，
  不等同于全局无条件证明。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_scaled_peeling_halfwidth_audit import contained_rows, interval_for_row
from prime_matrix_zero_row_crt_audit import primes_upto, next_prime


def smallest_prime_factor_table(limit: int) -> list[int]:
    """生成最小素因子表；素数 n 的表值为 n。"""
    spf = list(range(limit + 1))
    if limit >= 0:
        spf[0] = 0
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, int(limit**0.5) + 1):
        if spf[prime] != prime:
            continue
        start = prime * prime
        for n in range(start, limit + 1, prime):
            if spf[n] == n:
                spf[n] = prime
    return spf


def conditional_revived_positions(
    *,
    left: int,
    right: int,
    lower_prime: int,
    upper_prime: int,
    spf: list[int],
    terminal_punctures: set[int],
) -> list[int]:
    """计算从 upper_prime 零窗剥到 lower_prime 后的条件复活点。

    若 I 在 upper_prime-筛下为零，则降到 lower_prime 后的幸存点只能是：
    1. 避开所有 <=lower_prime 素数；
    2. 同时含有某个 (lower_prime, upper_prime] 内的剥离素因子；
    3. 外加来自 q^2 的终端穿孔。
    """
    revived = []
    for n in range(left, right + 1):
        if n in terminal_punctures:
            revived.append(n)
            continue
        # 在避开 <=lower_prime 的条件下，是否含有剥离素因子只由最小素因子决定。
        if lower_prime < spf[n] <= upper_prime:
            revived.append(n)
    return revived


def first_forced_zero_level(
    *,
    p: int,
    q: int,
    q_row: int,
    all_primes: list[int],
    spf: list[int],
    max_levels: int | None,
    stop_at_first_success: bool,
) -> dict:
    """跟踪一条 seam q 行在多层降阶中的首个强制零行。"""
    left, right = interval_for_row(q, q_row)
    p_index = all_primes.index(p)
    lower_indices = list(range(p_index - 1, -1, -1))
    if max_levels is not None:
        lower_indices = lower_indices[:max_levels]

    terminal_punctures = {q * q} if q_row == q else set()
    levels = []
    first_success = None

    for idx in lower_indices:
        lower = all_primes[idx]
        rows = contained_rows(left, right, lower)
        revived = conditional_revived_positions(
            left=left,
            right=right,
            lower_prime=lower,
            upper_prime=p,
            spf=spf,
            terminal_punctures=terminal_punctures,
        )
        revived_set = set(revived)
        zero_rows = []
        blocking_by_row = []
        for row in rows:
            row_left, row_right = interval_for_row(lower, row)
            blockers = [
                n for n in revived if row_left <= n <= row_right
            ]
            if blockers:
                blocking_by_row.append(
                    {
                        "row": row,
                        "interval": [row_left, row_right],
                        "blockers": blockers[:12],
                        "blocker_count": len(blockers),
                    }
                )
            else:
                zero_rows.append(row)

        level = {
            "lower_prime": lower,
            "contained_row_count": len(rows),
            "contained_rows": rows[:20],
            "revived_count": len(revived_set),
            "revived_positions": sorted(revived_set)[:30],
            "forced_zero_rows": zero_rows[:20],
            "forced_zero_row_count": len(zero_rows),
            "blocking_by_row": blocking_by_row[:8],
        }
        levels.append(level)
        if first_success is None and zero_rows:
            first_success = {
                "lower_prime": lower,
                "forced_zero_rows": zero_rows,
                "forced_zero_rows_inside_lower_square": [
                    row for row in zero_rows if row <= lower
                ],
                "level_index_from_p": len(levels),
            }
            if stop_at_first_success:
                break

    return {
        "p": p,
        "q": q,
        "q_row": q_row,
        "interval": [left, right],
        "terminal_punctures": sorted(terminal_punctures),
        "descends_to_forced_zero_row": first_success is not None,
        "first_forced_zero_level": first_success,
        "levels": levels,
    }


def audit(
    max_p: int,
    max_levels: int | None,
    sample_failures: int,
    stop_at_first_success: bool,
    row_stride: int,
) -> dict:
    """执行 seam 多层下降审计。"""
    all_primes = primes_upto(max_p + 100)
    max_q = next_prime(max_p)
    spf = smallest_prime_factor_table(max_q * max_q)
    records = []
    failures = []

    for p in [prime for prime in all_primes if 5 <= prime <= max_p]:
        q = next_prime(p)
        for q_row in range(2, q + 1):
            if row_stride > 1 and (q_row != q) and ((q_row - 2) % row_stride != 0):
                continue
            classification = classify_q_row_descent(p, q, q_row)
            if classification["type"] != "seam_window":
                continue
            record = first_forced_zero_level(
                p=p,
                q=q,
                q_row=q_row,
                all_primes=all_primes,
                spf=spf,
                max_levels=max_levels,
                stop_at_first_success=stop_at_first_success,
            )
            record["seam_classification"] = classification
            records.append(record)
            if not record["descends_to_forced_zero_row"]:
                failures.append(record)

    success_records = [
        record for record in records if record["descends_to_forced_zero_row"]
    ]
    first_levels = [
        record["first_forced_zero_level"]["level_index_from_p"]
        for record in success_records
    ]
    first_primes = [
        record["first_forced_zero_level"]["lower_prime"]
        for record in success_records
    ]
    first_prime_counts = Counter(first_primes)
    first_level_counts = Counter(first_levels)
    inside_square_successes = [
        record
        for record in success_records
        if record["first_forced_zero_level"]["forced_zero_rows_inside_lower_square"]
    ]
    return {
        "status": "finite_seam_multilevel_descent_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "max_levels": max_levels,
            "sample_failures": sample_failures,
            "stop_at_first_success": stop_at_first_success,
            "row_stride": row_stride,
        },
        "summary": {
            "seam_windows_checked": len(records),
            "descend_to_forced_zero_row": len(success_records),
            "blocked_through_checked_levels": len(failures),
            "success_fraction": (
                len(success_records) / len(records) if records else None
            ),
            "max_first_success_level_index": max(first_levels, default=None),
            "min_first_success_lower_prime": min(first_primes, default=None),
            "first_success_lower_prime_counts": dict(
                sorted(first_prime_counts.items())
            ),
            "first_success_level_index_counts": dict(
                sorted(first_level_counts.items())
            ),
            "first_success_inside_lower_square": len(inside_square_successes),
        },
        "failure_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "terminal_punctures": record["terminal_punctures"],
                "seam_classification": record["seam_classification"],
                "last_checked_level": (
                    record["levels"][-1] if record["levels"] else None
                ),
            }
            for record in failures[:sample_failures]
        ],
        "success_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "seam_classification": record["seam_classification"],
                "first_forced_zero_level": record["first_forced_zero_level"],
            }
            for record in success_records[:20]
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    params = result["parameters"]
    prime_counts = summary["first_success_lower_prime_counts"]
    prime_count_items = list(prime_counts.items())
    displayed_prime_counts = dict(prime_count_items[:20])
    if len(prime_count_items) > 20:
        displayed_prime_counts["..."] = "完整分布见 JSON"
    lines = [
        "# Seam 多层下降审计",
        "",
        "**状态：** `finite_seam_multilevel_descent_audit_not_global_proof`",
        "",
        "本文检验问题：一条 `q` 零行若降到旧 `p`-筛时只形成 seam zero window，继续降到更小素数层时，是否必然在某一层变成完整对齐零行。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `max_levels`: `{params['max_levels']}`。",
        f"- `stop_at_first_success`: `{params['stop_at_first_success']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 seam 窗口数：`{summary['seam_windows_checked']}`。",
        f"- 在检查层内变成强制零行的数量：`{summary['descend_to_forced_zero_row']}`。",
        f"- 全部检查层仍被复活点阻断的数量：`{summary['blocked_through_checked_levels']}`。",
        f"- 成功比例：`{summary['success_fraction']}`。",
        f"- 首次成功的最大下降层数：`{summary['max_first_success_level_index']}`。",
        f"- 首次成功层的最小素数：`{summary['min_first_success_lower_prime']}`。",
        f"- 首次成功已落入对应下层 `h×h` 方阵的数量：`{summary['first_success_inside_lower_square']}`。",
        f"- 首次成功素数分布摘录：`{displayed_prime_counts}`。",
        "",
        "## 成功样本",
        "",
        "| p | q | q-row | seam guards | first lower prime | forced rows |",
        "|---:|---:|---:|---|---:|---|",
    ]
    for sample in result["success_samples"][:12]:
        first = sample["first_forced_zero_level"]
        seam = sample["seam_classification"]
        lines.append(
            "| {p} | {q} | {row} | `{guards}` | {lower} | `{forced}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                guards=[seam["left_guard"], seam["right_guard"]],
                lower=first["lower_prime"],
                forced=first["forced_zero_rows"][:8],
            )
        )

    lines.extend(
        [
            "",
            "## 阻断样本",
            "",
            "| p | q | q-row | seam guards | last lower prime | revived count | contained rows |",
            "|---:|---:|---:|---|---:|---:|---:|",
        ]
    )
    for sample in result["failure_samples"][:12]:
        seam = sample["seam_classification"]
        last = sample["last_checked_level"] or {}
        lines.append(
            "| {p} | {q} | {row} | `{guards}` | {lower} | {revived} | {rows} |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                guards=[seam["left_guard"], seam["right_guard"]],
                lower=last.get("lower_prime", "-"),
                revived=last.get("revived_count", "-"),
                rows=last.get("contained_row_count", "-"),
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "几何上，固定长度 `q` 的 seam 区间在降到较小行宽 `h` 时会包含更多完整 `h` 对齐行；因此“有机会变成零行”的几何压力确实增强。",
            "",
            "但筛论上，剥去 `p` 到 `h` 之间的素数后，原先由这些素数覆盖的点会复活。条件复活集为：",
            "",
            "```text",
            "{n in I : n 避开所有 <=h 的素数，且 n 含某个 h<ell<=p 的素因子}",
            "外加最后 q 行的 q^2 端点穿孔。",
            "```",
            "",
            "因此“包含完整下层行”不等于“得到完整下层零行”。完整零行出现当且仅当某条完整下层行避开全部复活点。",
            "",
            "本账本给出的是局部条件机制：若所有 seam 都在有限下降层内出现强制零行，则可形成 `SeamDescent-ZeroRow` 条件引理；若存在阻断样本，则下一硬点必须转为证明这些复活点阻断不能在真实反例中持续，或必进入 `SAE/PDEC/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--max-levels", type=int, default=None)
    parser.add_argument(
        "--full-profile",
        action="store_true",
        help="保留每个 seam 的全部下降层；默认首次成功即停止以便大范围审计。",
    )
    parser.add_argument("--sample-failures", type=int, default=20)
    parser.add_argument(
        "--row-stride",
        type=int,
        default=1,
        help="只检查 q-row=2 mod stride 的 seam 行，并始终保留最后一行。",
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-seam-multilevel-descent-audit"),
    )
    args = parser.parse_args()

    result = audit(
        max_p=args.max_p,
        max_levels=args.max_levels,
        sample_failures=args.sample_failures,
        stop_at_first_success=not args.full_profile,
        row_stride=max(1, args.row_stride),
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
