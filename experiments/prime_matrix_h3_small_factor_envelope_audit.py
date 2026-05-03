#!/usr/bin/env python3
"""审计 H3 近失败窗口的小首因子骨架包络。

用法示例：
  python3 experiments/prime_matrix_h3_small_factor_envelope_audit.py
  python3 experiments/prime_matrix_h3_small_factor_envelope_audit.py --max-p 5000 --margin-threshold 20
  python3 experiments/prime_matrix_h3_small_factor_envelope_audit.py --cutoffs 7,13,31,43

目标：
  对 H3 近失败窗口，计算小首因子 cutoff y 的骨架覆盖 C_y、剩余 R_y，以及
  若要全阻断，剩余至少需要多少个 >y 的中尾 first-factor 标签。该账本服务于
  small-first-factor skeleton overload => Tail/PDEC envelope 的第一分支。

注意：
  本脚本只给有限精确账本和组合恒等式，不是全局证明。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from prime_matrix_adjacent_shell_descent_ledger import classify_q_row_descent
from prime_matrix_total_descent_h3_margin_audit import (
    Fenwick,
    contained_h3_rows,
    h3_candidate_value,
    smallest_prime_factor_table,
)
from prime_matrix_zero_row_crt_audit import next_prime, primes_upto


def next_prime_after(primes: list[int], value: int) -> int:
    """返回大于 value 的第一个素数。"""
    for prime in primes:
        if prime > value:
            return prime
    candidate = value + 1
    while True:
        for factor in range(2, int(candidate**0.5) + 1):
            if candidate % factor == 0:
                break
        else:
            return candidate
        candidate += 1


def factor_counts_for_window(
    *,
    first: int,
    last: int,
    p: int,
    spf: list[int],
) -> tuple[int, Counter[int], int]:
    """返回候选数、阻断 first-factor 计数和实际幸存数。"""
    factor_counts: Counter[int] = Counter()
    candidate_count = 0
    survivor_count = 0
    for h3_row in range(first, last + 1):
        candidate_count += 1
        value = h3_candidate_value(h3_row)
        factor = spf[value]
        if 5 <= factor <= p:
            factor_counts[factor] += 1
        else:
            survivor_count += 1
    return candidate_count, factor_counts, survivor_count


def cutoff_profile(
    *,
    candidate_count: int,
    factor_counts: Counter[int],
    q: int,
    cutoff: int,
    primes: list[int],
) -> dict:
    """计算给定 cutoff 的小骨架覆盖与中尾标签下界。"""
    small_load = sum(count for factor, count in factor_counts.items() if factor <= cutoff)
    residual = candidate_count - small_load
    next_label = next_prime_after(primes, cutoff)
    per_label_cap = q // next_label + 1
    min_tail_labels_for_full_block = (
        (residual + per_label_cap - 1) // per_label_cap
        if per_label_cap
        else residual
    )
    actual_tail_labels = sum(1 for factor in factor_counts if factor > cutoff)
    actual_tail_load = sum(count for factor, count in factor_counts.items() if factor > cutoff)
    return {
        "cutoff": cutoff,
        "small_load": small_load,
        "small_share": small_load / candidate_count if candidate_count else 0.0,
        "residual_after_small": residual,
        "next_tail_label": next_label,
        "per_tail_label_cap": per_label_cap,
        "min_tail_labels_for_full_block": min_tail_labels_for_full_block,
        "actual_tail_label_count": actual_tail_labels,
        "actual_tail_load": actual_tail_load,
    }


def audit(
    *,
    max_p: int,
    margin_threshold: int,
    row_stride: int,
    cutoffs: list[int],
) -> dict:
    """执行小首因子骨架包络审计。"""
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
    near_records = []

    for p in target_primes:
        while event_cursor < len(event_keys) and event_keys[event_cursor] <= p:
            for h3_row in events_by_spf[event_keys[event_cursor]]:
                fenwick.add(h3_row, 1)
            event_cursor += 1

        q = next_prime(p)
        for q_row in range(2, q + 1):
            if row_stride > 1 and q_row != q and (q_row - 2) % row_stride != 0:
                continue
            left = (q_row - 1) * q + 1
            right = q_row * q
            first, last = contained_h3_rows(left, right)
            candidate_count = max(0, last - first + 1)
            blocked_count = fenwick.range_sum(first, last) if candidate_count else 0
            margin = candidate_count - blocked_count
            rows_checked += 1
            if margin > margin_threshold:
                continue

            exact_candidate_count, factor_counts, survivor_count = factor_counts_for_window(
                first=first,
                last=last,
                p=p,
                spf=spf,
            )
            profiles = [
                cutoff_profile(
                    candidate_count=exact_candidate_count,
                    factor_counts=factor_counts,
                    q=q,
                    cutoff=cutoff,
                    primes=primes,
                )
                for cutoff in cutoffs
            ]
            near_records.append(
                {
                    "p": p,
                    "q": q,
                    "q_row": q_row,
                    "interval": [left, right],
                    "initial_type": classify_q_row_descent(p, q, q_row)["type"],
                    "candidate_count": exact_candidate_count,
                    "blocked_count": sum(factor_counts.values()),
                    "survivor_count": survivor_count,
                    "margin": margin,
                    "distinct_factor_count": len(factor_counts),
                    "top_factor_counts": factor_counts.most_common(12),
                    "cutoff_profiles": profiles,
                }
            )

    near_records.sort(
        key=lambda item: (
            item["margin"],
            -item["candidate_count"],
            item["p"],
            item["q_row"],
        )
    )

    cutoff_summary = {}
    for cutoff in cutoffs:
        profiles = [
            profile
            for record in near_records
            for profile in record["cutoff_profiles"]
            if profile["cutoff"] == cutoff
        ]
        if not profiles:
            cutoff_summary[str(cutoff)] = {}
            continue
        cutoff_summary[str(cutoff)] = {
            "max_small_share": max(profile["small_share"] for profile in profiles),
            "min_small_share": min(profile["small_share"] for profile in profiles),
            "max_residual_after_small": max(
                profile["residual_after_small"] for profile in profiles
            ),
            "max_min_tail_labels_for_full_block": max(
                profile["min_tail_labels_for_full_block"] for profile in profiles
            ),
            "avg_min_tail_labels_for_full_block": sum(
                profile["min_tail_labels_for_full_block"] for profile in profiles
            )
            / len(profiles),
        }

    return {
        "status": "finite_h3_small_factor_envelope_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "margin_threshold": margin_threshold,
            "row_stride": row_stride,
            "cutoffs": cutoffs,
            "max_n": max_n,
        },
        "summary": {
            "q_rows_checked": rows_checked,
            "near_windows": len(near_records),
            "near_min_p": min((item["p"] for item in near_records), default=None),
            "near_max_p": max((item["p"] for item in near_records), default=None),
            "near_max_q": max((item["q"] for item in near_records), default=None),
            "near_margin_counts": dict(
                sorted(Counter(item["margin"] for item in near_records).items())
            ),
            "cutoff_summary": cutoff_summary,
        },
        "tight_samples": near_records[:32],
        "max_tail_label_need_samples": sorted(
            near_records,
            key=lambda item: max(
                profile["min_tail_labels_for_full_block"]
                for profile in item["cutoff_profiles"]
            ),
            reverse=True,
        )[:24],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    lines = [
        "# H3 小首因子骨架包络审计",
        "",
        "**状态：** `finite_h3_small_factor_envelope_audit_not_global_proof`",
        "",
        "本文审计 `H3 Full-Blocking Defect` 的第一分支：小首因子骨架若承担过多覆盖，应进入 `Tail/PDEC envelope`；否则剩余必须由足够多的中尾 first-factor 标签承担。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `margin_threshold`: `{params['margin_threshold']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `cutoffs`: `{params['cutoffs']}`。",
        f"- `max_n`: `{params['max_n']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 近失败窗口数：`{summary['near_windows']}`。",
        f"- 近失败 p 范围：`{summary['near_min_p']}..{summary['near_max_p']}`。",
        f"- 近失败最大 q：`{summary['near_max_q']}`。",
        f"- 近失败余量分布：`{summary['near_margin_counts']}`。",
        "",
        "## Cutoff 包络摘要",
        "",
        "| cutoff | max small share | max residual | max forced tail labels | avg forced tail labels |",
        "|---:|---:|---:|---:|---:|",
    ]
    for cutoff in params["cutoffs"]:
        item = summary["cutoff_summary"].get(str(cutoff), {})
        if not item:
            continue
        lines.append(
            "| {cutoff} | {share:.6f} | {resid} | {labels} | {avg:.6f} |".format(
                cutoff=cutoff,
                share=item["max_small_share"],
                resid=item["max_residual_after_small"],
                labels=item["max_min_tail_labels_for_full_block"],
                avg=item["avg_min_tail_labels_for_full_block"],
            )
        )

    lines.extend(
        [
            "",
            "## 最紧样本",
            "",
            "| p | q | row | cand | blocked | margin | top factors | cutoff profiles |",
            "|---:|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for sample in result["tight_samples"][:16]:
        profile_excerpt = [
            {
                "y": profile["cutoff"],
                "C_y": profile["small_load"],
                "R_y": profile["residual_after_small"],
                "K_y": profile["min_tail_labels_for_full_block"],
            }
            for profile in sample["cutoff_profiles"]
        ]
        lines.append(
            "| {p} | {q} | {row} | {cand} | {blocked} | {margin} | `{top}` | `{profiles}` |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                cand=sample["candidate_count"],
                blocked=sample["blocked_count"],
                margin=sample["margin"],
                top=sample["top_factor_counts"][:5],
                profiles=profile_excerpt,
            )
        )

    lines.extend(
        [
            "",
            "## 组合二分",
            "",
            "对任意 cutoff `y`，记 `C_y` 为 `<=y` 的小首因子骨架覆盖数，`R_y=A-C_y`。令 `ell_+(y)` 为大于 `y` 的下一素数。任一 `>y` 标签在长度 `q` 的窗口中最多贡献 `floor(q/ell_+(y))+1` 个点。因此若要全阻断，则至少需要",
            "",
            "\\[",
            "K_y=\\left\\lceil {R_y\\over \\lfloor q/\\ell_+(y)\\rfloor+1}\\right\\rceil",
            "\\]",
            "",
            "个中尾标签，除非小首因子骨架本身已经接近满载。故严格路线是：",
            "",
            "```text",
            "H3 full blocking",
            "=> C_y is Tail/PDEC-overloaded",
            "   or at least K_y middle-tail labels are active",
            "   or endpoint phases absorb the rounding loss.",
            "```",
            "",
            "该二分是确定性组合账本；剩余工作是给 `Tail/PDEC-overloaded` 和 `many-label low-mod energy` 填入同一口径阈值。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--margin-threshold", type=int, default=20)
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument("--cutoffs", type=str, default="7,13,31,43")
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-h3-small-factor-envelope-audit"),
    )
    args = parser.parse_args()
    cutoffs = [int(item) for item in args.cutoffs.split(",") if item.strip()]
    result = audit(
        max_p=args.max_p,
        margin_threshold=args.margin_threshold,
        row_stride=max(1, args.row_stride),
        cutoffs=cutoffs,
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
