#!/usr/bin/env python3
"""审计 seam 强制零行能否经 CRT 尾镜像落回小阶方阵。

用法示例：
  python3 experiments/prime_matrix_seam_tail_mirror_descent_audit.py
  python3 experiments/prime_matrix_seam_tail_mirror_descent_audit.py --max-p 500
  python3 experiments/prime_matrix_seam_tail_mirror_descent_audit.py --max-p 2000 --row-stride 25

目标：
  对 seam 多层下降中产生的条件强制 h-零行，计算其在 h-筛 CRT 行周期中的相位
  rho=((R-1) mod N_h)+1 及镜像相位 rho*=N_h-rho+1。若 rho<=h 或 rho*<=h，
  则该条件零行通过周期/镜像落入 h×h 方阵头部，给出更直接的下降矛盾入口。

注意：
  本脚本仍以“上层 seam 区间确为旧 p-筛零窗”为条件；它验证尾镜像路径的相位机制，
  不单独构成全局无条件证明。
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
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def period_rows_by_prime(primes: list[int], max_prime: int) -> dict[int, int]:
    """计算每个素数 h 的 CRT 行周期 N_h=prod_{ell<=h}ell / h。"""
    product = 1
    periods: dict[int, int] = {}
    for prime in primes:
        if prime > max_prime:
            break
        product *= prime
        periods[prime] = product // prime
    return periods


def mirror_profile(row: int, h: int, period_rows: int) -> dict:
    """计算 h-行 row 的周期相位和 CRT 镜像相位。"""
    phase = ((row - 1) % period_rows) + 1
    mirror_phase = period_rows - phase + 1
    return {
        "row": row,
        "h": h,
        "period_rows": period_rows,
        "phase": phase,
        "mirror_phase": mirror_phase,
        "direct_head_hit": phase <= h,
        "mirror_head_hit": mirror_phase <= h,
        "head_or_tail_hit": phase <= h or mirror_phase <= h,
        "tail_distance": mirror_phase,
    }


def first_tail_mirror_hit(
    *,
    p: int,
    q: int,
    q_row: int,
    all_primes: list[int],
    spf: list[int],
    periods: dict[int, int],
    max_levels: int | None,
) -> dict:
    """寻找 seam 条件下降中首个可由周期/尾镜像落回 h×h 的强制零行。"""
    left, right = interval_for_row(q, q_row)
    p_index = all_primes.index(p)
    lower_indices = list(range(p_index - 1, -1, -1))
    if max_levels is not None:
        lower_indices = lower_indices[:max_levels]

    terminal_punctures = {q * q} if q_row == q else set()
    first_forced = None
    first_head_or_tail = None
    inspected_levels = []

    for level_index, idx in enumerate(lower_indices, start=1):
        h = all_primes[idx]
        rows = contained_rows(left, right, h)
        revived = conditional_revived_positions(
            left=left,
            right=right,
            lower_prime=h,
            upper_prime=p,
            spf=spf,
            terminal_punctures=terminal_punctures,
        )
        forced_profiles = []
        for row in rows:
            row_left, row_right = interval_for_row(h, row)
            if any(row_left <= n <= row_right for n in revived):
                continue
            forced_profiles.append(mirror_profile(row, h, periods[h]))

        if forced_profiles and first_forced is None:
            first_forced = {
                "level_index_from_p": level_index,
                "h": h,
                "forced_profiles": forced_profiles[:12],
            }

        hits = [
            profile for profile in forced_profiles if profile["head_or_tail_hit"]
        ]
        inspected_levels.append(
            {
                "level_index_from_p": level_index,
                "h": h,
                "contained_row_count": len(rows),
                "revived_count": len(set(revived)),
                "forced_count": len(forced_profiles),
                "head_or_tail_hit_count": len(hits),
                "sample_hits": hits[:6],
                "sample_forced": forced_profiles[:6],
            }
        )
        if hits and first_head_or_tail is None:
            first_head_or_tail = {
                "level_index_from_p": level_index,
                "h": h,
                "hit_profiles": hits[:12],
            }
            break

    return {
        "p": p,
        "q": q,
        "q_row": q_row,
        "interval": [left, right],
        "terminal_punctures": sorted(terminal_punctures),
        "first_forced": first_forced,
        "first_head_or_tail": first_head_or_tail,
        "has_forced_zero": first_forced is not None,
        "has_head_or_tail_hit": first_head_or_tail is not None,
        "inspected_levels": inspected_levels,
    }


def audit(max_p: int, row_stride: int, max_levels: int | None) -> dict:
    """执行尾镜像下降审计。"""
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
            classification = classify_q_row_descent(p, q, q_row)
            if classification["type"] != "seam_window":
                continue
            record = first_tail_mirror_hit(
                p=p,
                q=q,
                q_row=q_row,
                all_primes=all_primes,
                spf=spf,
                periods=periods,
                max_levels=max_levels,
            )
            record["seam_classification"] = classification
            records.append(record)

    forced = [record for record in records if record["has_forced_zero"]]
    hits = [record for record in records if record["has_head_or_tail_hit"]]
    hit_levels = [
        record["first_head_or_tail"]["level_index_from_p"] for record in hits
    ]
    hit_primes = [record["first_head_or_tail"]["h"] for record in hits]
    hit_modes: Counter[str] = Counter()
    for record in hits:
        for profile in record["first_head_or_tail"]["hit_profiles"]:
            if profile["direct_head_hit"]:
                hit_modes["direct_head_phase"] += 1
            if profile["mirror_head_hit"]:
                hit_modes["tail_mirror_phase"] += 1

    return {
        "status": "finite_seam_tail_mirror_descent_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "row_stride": row_stride,
            "max_levels": max_levels,
        },
        "summary": {
            "seam_windows_checked": len(records),
            "forced_zero_found": len(forced),
            "head_or_tail_hits": len(hits),
            "blocked_without_head_or_tail_hit": len(records) - len(hits),
            "hit_fraction": len(hits) / len(records) if records else None,
            "max_hit_level_index": max(hit_levels, default=None),
            "min_hit_prime": min(hit_primes, default=None),
            "hit_prime_counts": dict(sorted(Counter(hit_primes).items())),
            "hit_mode_counts": dict(sorted(hit_modes.items())),
        },
        "hit_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "seam_classification": record["seam_classification"],
                "first_forced": record["first_forced"],
                "first_head_or_tail": record["first_head_or_tail"],
            }
            for record in hits[:20]
        ],
        "blocked_samples": [
            {
                "p": record["p"],
                "q": record["q"],
                "q_row": record["q_row"],
                "interval": record["interval"],
                "seam_classification": record["seam_classification"],
                "first_forced": record["first_forced"],
                "last_level": record["inspected_levels"][-1]
                if record["inspected_levels"]
                else None,
            }
            for record in records
            if not record["has_head_or_tail_hit"]
        ][:20],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    hit_prime_items = list(summary["hit_prime_counts"].items())
    hit_prime_excerpt = dict(hit_prime_items[:20])
    if len(hit_prime_items) > 20:
        hit_prime_excerpt["..."] = "完整分布见 JSON"

    lines = [
        "# Seam 尾镜像下降审计",
        "",
        "**状态：** `finite_seam_tail_mirror_descent_audit_not_global_proof`",
        "",
        "本文审计用户提出的加强路径：seam 降阶后得到的强制零行即使不直接落入小阶方阵，也可能在该小阶 CRT 周期尾边界；由零行镜像刚性，尾边界零行会映回头部方阵，从而得到小阶方阵零行。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `max_levels`: `{params['max_levels']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 seam 窗口数：`{summary['seam_windows_checked']}`。",
        f"- 出现条件强制零行数：`{summary['forced_zero_found']}`。",
        f"- 周期头部或尾镜像命中数：`{summary['head_or_tail_hits']}`。",
        f"- 未命中数：`{summary['blocked_without_head_or_tail_hit']}`。",
        f"- 命中比例：`{summary['hit_fraction']}`。",
        f"- 最大首次命中下降层数：`{summary['max_hit_level_index']}`。",
        f"- 最小命中素数：`{summary['min_hit_prime']}`。",
        f"- 命中模式计数：`{summary['hit_mode_counts']}`。",
        f"- 命中素数分布摘录：`{hit_prime_excerpt}`。",
        "",
        "## 命中样本",
        "",
        "| p | q | q-row | seam guards | h | hit profiles |",
        "|---:|---:|---:|---|---:|---|",
    ]
    for sample in result["hit_samples"][:12]:
        seam = sample["seam_classification"]
        hit = sample["first_head_or_tail"]
        lines.append(
            "| {p} | {q} | {row} | `{guards}` | {h} | `{profiles}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                guards=[seam["left_guard"], seam["right_guard"]],
                h=hit["h"],
                profiles=hit["hit_profiles"][:4],
            )
        )

    lines.extend(
        [
            "",
            "## 未命中样本",
            "",
            "| p | q | q-row | seam guards | first forced | last level |",
            "|---:|---:|---:|---|---|---|",
        ]
    )
    for sample in result["blocked_samples"][:12]:
        seam = sample["seam_classification"]
        lines.append(
            "| {p} | {q} | {row} | `{guards}` | `{forced}` | `{last}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                guards=[seam["left_guard"], seam["right_guard"]],
                forced=sample["first_forced"],
                last=sample["last_level"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "对 `h`-筛，令 `M_h=prod_{ell<=h}ell`、`N_h=M_h/h`。若第 `R` 条 `h` 对齐行是零行，则其行相位",
            "",
            "```text",
            "rho=((R-1) mod N_h)+1",
            "```",
            "",
            "也是零行相位。非平凡列的取负映射给出镜像相位 `rho*=N_h-rho+1`。若 `rho<=h`，则周期直接落入 `h×h` 方阵；若 `rho*<=h`，则尾边界零行经 CRT 镜像落入 `h×h` 方阵。",
            "",
            "因此用户提出的路径是有效的严格接口：",
            "",
            "```text",
            "seam zero window",
            "=> 多层下降产生条件 h-zero-row",
            "=> 若 h-row phase 或 mirror phase <= h",
            "=> 小阶 h×h 方阵条件零行",
            "=> 与已知 Row(h) 或边界非零证书冲突。",
            "```",
            "",
            "但必须保留两个审稿边界：第一，该 h-zero-row 仍是在上层 seam 零窗假设下的条件结论；第二，若相位与镜像相位都不落入头部方阵，则仍需继续用 `SMD-Global Inequality` 或 `SAE/PDEC/ColumnCRT` 排除。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=500)
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument("--max-levels", type=int, default=None)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-seam-tail-mirror-descent-audit"),
    )
    args = parser.parse_args()
    result = audit(
        max_p=args.max_p,
        row_stride=max(1, args.row_stride),
        max_levels=args.max_levels,
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
