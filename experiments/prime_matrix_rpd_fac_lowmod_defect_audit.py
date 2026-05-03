#!/usr/bin/env python3
"""RPD 第一锚 FAC 低模端点缺陷审计。

用法示例：
  python3 experiments/prime_matrix_rpd_fac_lowmod_defect_audit.py
  python3 experiments/prime_matrix_rpd_fac_lowmod_defect_audit.py --cutoffs 3,5,7,11,13,17,23
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from prime_matrix_mge3_budget_audit import (
    MONOGRAPH,
    ceil_div,
    collect_hard_windows,
    primes_from_flags,
    sieve,
    smallest_prime_factor,
)

DEFAULT_JSON = MONOGRAPH / "prime-matrix-rpd-fac-lowmod-defect-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-rpd-fac-lowmod-defect-audit.md"


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数列表。"""
    values = []
    for item in raw.split(","):
        item = item.strip()
        if item:
            values.append(int(item))
    if not values:
        raise ValueError("cutoffs 不能为空")
    return sorted(set(values))


def density_before(primes: list[int], cutoff: int) -> float:
    """计算 V(<cutoff)=prod_{l<cutoff}(1-1/l)。"""
    value = 1.0
    for prime in primes:
        if prime >= cutoff:
            break
        value *= 1.0 - 1.0 / prime
    return value


def is_coprime_to_small_primes(n: int, primes: list[int], cutoff: int) -> bool:
    """判断 n 是否避开所有小于 cutoff 的素因子。"""
    for prime in primes:
        if prime >= cutoff:
            break
        if n % prime == 0:
            return False
    return True


def interval_for_anchor(left: int, right: int, anchor: int) -> tuple[int, int, int]:
    """返回第一锚互补因子区间。"""
    co_left = max(anchor, ceil_div(left, anchor))
    co_right = right // anchor
    capacity = max(0, co_right - co_left + 1)
    return co_left, co_right, capacity


def count_cutoff_interval(
    co_left: int,
    co_right: int,
    cutoff: int,
    primes: list[int],
) -> int:
    """统计互补区间中避开小于 cutoff 素数的整数。"""
    return sum(1 for c in range(co_left, co_right + 1) if is_coprime_to_small_primes(c, primes, cutoff))


def audit_window(
    window: dict[str, Any],
    primes: list[int],
    spf: list[int],
    cutoffs: list[int],
) -> dict[str, Any]:
    """审计一个压力窗口的低模端点缺陷。"""
    p = window["p"]
    z = window["z"]
    left = window["left"]
    right = window["right"]
    anchors = []
    totals = {
        cutoff: {
            "cutoff": cutoff,
            "count": 0,
            "model": 0.0,
            "defect": 0.0,
            "ratio": None,
            "capture_ratio": None,
        }
        for cutoff in cutoffs
    }

    final_count = 0
    final_model = 0.0
    final_capacity = 0

    for anchor in primes:
        if anchor <= z:
            continue
        if anchor > p:
            break
        co_left, co_right, capacity = interval_for_anchor(left, right, anchor)
        if capacity == 0:
            continue

        actual = sum(1 for c in range(co_left, co_right + 1) if spf[c] >= anchor)
        model = capacity * density_before(primes, anchor)
        final_count += actual
        final_model += model
        final_capacity += capacity

        anchor_row = {
            "anchor": anchor,
            "co_left": co_left,
            "co_right": co_right,
            "capacity": capacity,
            "actual_rough": actual,
            "model": model,
            "defect": actual - model,
            "required_constant": None if model <= 0.0 else actual / model,
            "cutoff_counts": {},
        }

        for cutoff in cutoffs:
            local_cutoff = min(anchor, cutoff)
            count = count_cutoff_interval(co_left, co_right, local_cutoff, primes)
            local_model = capacity * density_before(primes, local_cutoff)
            totals[cutoff]["count"] += count
            totals[cutoff]["model"] += local_model
            anchor_row["cutoff_counts"][str(cutoff)] = {
                "effective_cutoff": local_cutoff,
                "count": count,
                "model": local_model,
                "defect": count - local_model,
            }

        anchors.append(anchor_row)

    final_defect = final_count - final_model
    for cutoff in cutoffs:
        row = totals[cutoff]
        row["defect"] = row["count"] - row["model"]
        row["ratio"] = None if row["model"] <= 0.0 else row["count"] / row["model"]
        if final_defect > 0.0:
            row["capture_ratio"] = row["defect"] / final_defect

    capture_80 = None
    capture_90 = None
    if final_defect > 0.0:
        for cutoff in cutoffs:
            ratio = totals[cutoff]["capture_ratio"]
            if capture_80 is None and ratio is not None and ratio >= 0.80:
                capture_80 = cutoff
            if capture_90 is None and ratio is not None and ratio >= 0.90:
                capture_90 = cutoff

    return {
        "p": p,
        "q": window["q"],
        "q_row": window["q_row"],
        "left": left,
        "right": right,
        "rough_count": window["rough_count"],
        "prime_count": window["prime_count"],
        "composite_count": window["composite_count"],
        "fac_capacity": final_capacity,
        "fac_actual_rough": final_count,
        "fac_model": final_model,
        "fac_defect": final_defect,
        "fac_required_constant": None if final_model <= 0.0 else final_count / final_model,
        "identity_gap": final_count - window["composite_count"],
        "capture_80_cutoff": capture_80,
        "capture_90_cutoff": capture_90,
        "cutoff_totals": [totals[cutoff] for cutoff in cutoffs],
        "top_anchor_defects": sorted(anchors, key=lambda row: row["defect"], reverse=True)[:10],
    }


def summarize_windows(rows: list[dict[str, Any]], cutoffs: list[int]) -> dict[str, Any]:
    """汇总低模缺陷捕获情况。"""
    positive = [row for row in rows if row["fac_defect"] > 0.0]
    cutoff_stats = []
    for cutoff in cutoffs:
        ratios = []
        for row in positive:
            for total in row["cutoff_totals"]:
                if total["cutoff"] == cutoff and total["capture_ratio"] is not None:
                    ratios.append(total["capture_ratio"])
        cutoff_stats.append(
            {
                "cutoff": cutoff,
                "positive_window_count": len(ratios),
                "min_capture_ratio": None if not ratios else min(ratios),
                "avg_capture_ratio": None if not ratios else sum(ratios) / len(ratios),
                "max_capture_ratio": None if not ratios else max(ratios),
            }
        )

    return {
        "window_count": len(rows),
        "positive_defect_count": len(positive),
        "capture_80_distribution": count_distribution(row["capture_80_cutoff"] for row in positive),
        "capture_90_distribution": count_distribution(row["capture_90_cutoff"] for row in positive),
        "cutoff_stats": cutoff_stats,
        "worst_required_windows": sorted(rows, key=lambda row: row["fac_required_constant"] or 0.0, reverse=True)[:12],
    }


def count_distribution(values: Any) -> dict[str, int]:
    """统计离散值分布。"""
    counts: dict[str, int] = {}
    for value in values:
        key = "None" if value is None else str(value)
        counts[key] = counts.get(key, 0) + 1
    return counts


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int, cutoffs: list[int]) -> dict[str, Any]:
    """生成低模端点缺陷审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    rows = [audit_window(window, primes, spf, cutoffs) for window in hard_windows]
    return {
        "certificate_type": "prime_matrix_rpd_fac_lowmod_defect_audit",
        "status": "fac_spikes_are_measured_as_weighted_low_mod_endpoint_defects",
        "parameters": {
            "max_p": max_p,
            "alpha": alpha,
            "tail_fraction": tail_fraction,
            "keep": keep,
            "cutoffs": cutoffs,
        },
        "summary": summarize_windows(rows, cutoffs),
        "windows": rows,
        "review_conclusion": (
            "FAC 尖峰可由截断低模端点缺陷账本直接观测。"
            "若低模捕获比例高，下一步应证明该缺陷触发 CRTDefect/Tail-anchor/OSPC；"
            "若捕获比例低，则需要更细锚层 Selberg 常数。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "NA"
    return f"{value:.6f}"


def write_md(report: dict[str, Any], path: Path) -> None:
    """写出 Markdown 报告。"""
    params = report["parameters"]
    summary = report["summary"]
    worst = summary["worst_required_windows"]
    lines = [
        "# RPD 第一锚 FAC 低模端点缺陷审计",
        "",
        "**状态：** `fac_spikes_are_measured_as_weighted_low_mod_endpoint_defects`",
        "",
        "本文审计 FAC 尖峰是否已经在低模截断层显现。对每个 cutoff `T` 计算",
        "",
        "\\[",
        "D_T(J)=\\sum_{z<a\\le p}\\left(",
        "\\#\\{c\\in I_a(J):(c,\\prod_{\\ell<\\min(a,T)}\\ell)=1\\}",
        "-|I_a(J)|V(<\\min(a,T))\\right).",
        "\\]",
        "",
        "`D_T` 是加权低模端点缺陷；当 `T` 增至锚端点时，它变成 FAC 模型缺陷。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        f"- cutoffs：`{', '.join(str(x) for x in params['cutoffs'])}`。",
        "",
        "## 2. 汇总",
        "",
        f"- 窗口数：`{summary['window_count']}`。",
        f"- FAC 正缺陷窗口数：`{summary['positive_defect_count']}`。",
        f"- 80% 捕获 cutoff 分布：`{summary['capture_80_distribution']}`。",
        f"- 90% 捕获 cutoff 分布：`{summary['capture_90_distribution']}`。",
        "",
        "### 2.1 cutoff 捕获率",
        "",
        "捕获率是 `D_T/D_final`，不是概率；由于端点误差可在不同模层间抵消，局部值可小于 `0` 或大于 `1`。",
        "",
        "| cutoff | 正缺陷窗口数 | 最小捕获率 | 平均捕获率 | 最大捕获率 |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary["cutoff_stats"]:
        lines.append(
            "| "
            f"{row['cutoff']} | "
            f"{row['positive_window_count']} | "
            f"{fmt_float(row['min_capture_ratio'])} | "
            f"{fmt_float(row['avg_capture_ratio'])} | "
            f"{fmt_float(row['max_capture_ratio'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 最大 FAC 常数窗口",
            "",
            "| p | q行 | J | FAC | 模型量 | 缺陷 | 所需常数 | 80% cutoff | 90% cutoff |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in worst:
        lines.append(
            "| "
            f"{row['p']} | "
            f"{row['q_row']} | "
            f"`[{row['left']},{row['right']}]` | "
            f"{row['fac_actual_rough']} | "
            f"{fmt_float(row['fac_model'])} | "
            f"{fmt_float(row['fac_defect'])} | "
            f"{fmt_float(row['fac_required_constant'])} | "
            f"{row['capture_80_cutoff']} | "
            f"{row['capture_90_cutoff']} |"
        )

    if worst:
        top = worst[0]
        lines.extend(
            [
                "",
                "## 4. 最尖峰窗口低模剖面",
                "",
                f"最尖峰窗口为 `p={top['p']}`、`q_row={top['q_row']}`、`J=[{top['left']},{top['right']}]`。",
                "",
                "| cutoff | count | model | defect | ratio | capture |",
                "| ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for total in top["cutoff_totals"]:
            lines.append(
                "| "
                f"{total['cutoff']} | "
                f"{total['count']} | "
                f"{fmt_float(total['model'])} | "
                f"{fmt_float(total['defect'])} | "
                f"{fmt_float(total['ratio'])} | "
                f"{fmt_float(total['capture_ratio'])} |"
            )

        lines.extend(
            [
                "",
                "### 4.1 最尖峰窗口锚层贡献",
                "",
                "| anchor | I_a | cap | actual | model | defect | reqC |",
                "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for anchor in top["top_anchor_defects"][:8]:
            lines.append(
                "| "
                f"{anchor['anchor']} | "
                f"`[{anchor['co_left']},{anchor['co_right']}]` | "
                f"{anchor['capacity']} | "
                f"{anchor['actual_rough']} | "
                f"{fmt_float(anchor['model'])} | "
                f"{fmt_float(anchor['defect'])} | "
                f"{fmt_float(anchor['required_constant'])} |"
            )

    lines.extend(
        [
            "",
            "## 5. 审稿结论",
            "",
            "1. FAC 尖峰可被 `D_T` 账本直接定位；这正是加权低模端点缺陷的可计算形式。",
            "2. 若最尖峰窗口在小 cutoff 已捕获大部分 FAC 缺陷，则下一证明义务应转为 `low-mod defect => CRTDefect/Tail-anchor/OSPC`。",
            "3. 若某些窗口捕获率不足，则需改用更细锚层 Selberg 常数，而不是回到半素数与多因子分预算。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--keep", type=int, default=40)
    parser.add_argument("--cutoffs", default="3,5,7,11,13,17,23,31,47,67,101,151,251,503,1009,2003")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    report = build_audit(args.max_p, args.alpha, args.tail_fraction, args.keep, parse_ints(args.cutoffs))
    args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(report, args.md_out)
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")


if __name__ == "__main__":
    main()
