#!/usr/bin/env python3
"""审计 H3 全阻断缺陷的近失败窗口结构。

用法示例：
  python3 experiments/prime_matrix_h3_full_blocking_defect_audit.py
  python3 experiments/prime_matrix_h3_full_blocking_defect_audit.py --max-p 5000 --margin-threshold 3
  python3 experiments/prime_matrix_h3_full_blocking_defect_audit.py --max-p 1000 --out-prefix /tmp/h3-defect

目标：
  在固定 h=3 的六轮余量账本中，抽取 margin 很小的近失败窗口，分析阻断候选的
  first-factor 标签负载、尾部标签比例和低模相位能量，为 H3 Full-Blocking Defect
  定理提供可复核的数据支撑。

注意：
  本脚本输出有限审计报告，不是全局证明。全局证明仍需把 first-factor 高负载或
  分布式低模能量提升为 Tail/PDEC/ColumnCRT/SAE 的正式阈值不等式。
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


def lowmod_energy(
    factor_counts_by_mod: dict[int, dict[int, Counter[int]]],
    moduli: list[int],
) -> dict:
    """计算 first-factor 标签在小模数上的方差能量。"""
    result = {}
    for modulus in moduli:
        energy = 0.0
        label_count = 0
        for residues in factor_counts_by_mod[modulus].values():
            total = sum(residues.values())
            if total == 0:
                continue
            label_count += 1
            expected = total / modulus
            for residue in range(modulus):
                diff = residues.get(residue, 0) - expected
                energy += diff * diff
        result[str(modulus)] = {
            "energy": energy,
            "label_count": label_count,
        }
    return result


def analyze_window(
    *,
    p: int,
    q: int,
    q_row: int,
    first: int,
    last: int,
    spf: list[int],
    small_moduli: list[int],
) -> dict:
    """分析一个近失败 H3 窗口。"""
    candidates = []
    blocked = []
    survivors = []
    factor_counts: Counter[int] = Counter()
    factor_counts_by_mod = {
        modulus: {} for modulus in small_moduli
    }

    for h3_row in range(first, last + 1):
        value = h3_candidate_value(h3_row)
        factor = spf[value]
        item = {
            "h3_row": h3_row,
            "value": value,
            "spf": factor,
        }
        candidates.append(item)
        if 5 <= factor <= p:
            blocked.append(item)
            factor_counts[factor] += 1
            for modulus in small_moduli:
                label_bucket = factor_counts_by_mod[modulus].setdefault(
                    factor,
                    Counter(),
                )
                label_bucket[value % modulus] += 1
        else:
            survivors.append(item)

    blocked_count = len(blocked)
    candidate_count = len(candidates)
    top_factor, top_factor_load = (None, 0)
    if factor_counts:
        top_factor, top_factor_load = factor_counts.most_common(1)[0]

    tail_cutoffs = {
        "gt_q_over_2": sum(count for factor, count in factor_counts.items() if factor > q / 2),
        "gt_q_over_3": sum(count for factor, count in factor_counts.items() if factor > q / 3),
        "gt_sqrt_q": sum(count for factor, count in factor_counts.items() if factor * factor > q),
    }
    energy = lowmod_energy(factor_counts_by_mod, small_moduli)
    max_energy_modulus = None
    max_energy = 0.0
    for modulus, payload in energy.items():
        if payload["energy"] > max_energy:
            max_energy_modulus = modulus
            max_energy = payload["energy"]

    return {
        "p": p,
        "q": q,
        "q_row": q_row,
        "interval": [(q_row - 1) * q + 1, q_row * q],
        "initial_type": classify_q_row_descent(p, q, q_row)["type"],
        "h3_row_range": [first, last],
        "candidate_count": candidate_count,
        "blocked_count": blocked_count,
        "margin": candidate_count - blocked_count,
        "distinct_factor_count": len(factor_counts),
        "top_factor": top_factor,
        "top_factor_load": top_factor_load,
        "top_factor_share": (
            top_factor_load / blocked_count if blocked_count else 0.0
        ),
        "tail_cutoffs": tail_cutoffs,
        "tail_share_gt_q_over_2": (
            tail_cutoffs["gt_q_over_2"] / blocked_count if blocked_count else 0.0
        ),
        "lowmod_energy": energy,
        "max_lowmod_energy": max_energy,
        "max_lowmod_energy_modulus": max_energy_modulus,
        "top_factor_counts": factor_counts.most_common(12),
        "survivor_count": len(survivors),
        "survivor_samples": survivors[:8],
    }


def audit(
    *,
    max_p: int,
    margin_threshold: int,
    row_stride: int,
    small_moduli: list[int],
) -> dict:
    """执行 H3 全阻断缺陷近失败审计。"""
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
    near_windows = []
    margin_counts: Counter[int] = Counter()
    initial_counts: Counter[str] = Counter()
    min_margin = None
    max_margin = None

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
            margin_counts[margin] += 1
            initial_counts[classify_q_row_descent(p, q, q_row)["type"]] += 1
            min_margin = margin if min_margin is None else min(min_margin, margin)
            max_margin = margin if max_margin is None else max(max_margin, margin)

            if margin <= margin_threshold:
                near_windows.append(
                    analyze_window(
                        p=p,
                        q=q,
                        q_row=q_row,
                        first=first,
                        last=last,
                        spf=spf,
                        small_moduli=small_moduli,
                    )
                )

    near_windows.sort(
        key=lambda item: (
            item["margin"],
            -item["top_factor_share"],
            -item["max_lowmod_energy"],
            item["p"],
            item["q_row"],
        )
    )
    top_load = max((item["top_factor_share"] for item in near_windows), default=0.0)
    max_lowmod_energy = max(
        (item["max_lowmod_energy"] for item in near_windows),
        default=0.0,
    )
    aggregate_factor_counts: Counter[int] = Counter()
    for item in near_windows:
        for factor, count in item["top_factor_counts"]:
            aggregate_factor_counts[factor] += count
    return {
        "status": "finite_h3_full_blocking_defect_near_miss_audit_not_global_proof",
        "parameters": {
            "max_p": max_p,
            "margin_threshold": margin_threshold,
            "row_stride": row_stride,
            "small_moduli": small_moduli,
            "max_n": max_n,
        },
        "summary": {
            "q_rows_checked": rows_checked,
            "near_windows": len(near_windows),
            "min_margin": min_margin,
            "max_margin": max_margin,
            "margin_counts_excerpt": dict(sorted(margin_counts.items())[:20]),
            "initial_type_counts": dict(sorted(initial_counts.items())),
            "max_top_factor_share_near": top_load,
            "max_lowmod_energy_near": max_lowmod_energy,
            "near_margin_counts": dict(
                sorted(Counter(item["margin"] for item in near_windows).items())
            ),
            "near_min_p": min((item["p"] for item in near_windows), default=None),
            "near_max_p": max((item["p"] for item in near_windows), default=None),
            "near_max_q": max((item["q"] for item in near_windows), default=None),
            "near_max_candidate_count": max(
                (item["candidate_count"] for item in near_windows),
                default=None,
            ),
            "near_max_blocked_count": max(
                (item["blocked_count"] for item in near_windows),
                default=None,
            ),
            "near_initial_type_counts": dict(
                sorted(Counter(item["initial_type"] for item in near_windows).items())
            ),
            "near_aggregate_factor_counts_top": aggregate_factor_counts.most_common(12),
        },
        "tight_samples": near_windows[:40],
        "highest_load_samples": sorted(
            near_windows,
            key=lambda item: (-item["top_factor_share"], item["margin"]),
        )[:20],
        "highest_lowmod_energy_samples": sorted(
            near_windows,
            key=lambda item: (-item["max_lowmod_energy"], item["margin"]),
        )[:20],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    params = result["parameters"]
    lines = [
        "# H3 Full-Blocking Defect 近失败审计",
        "",
        "**状态：** `finite_h3_full_blocking_defect_near_miss_audit_not_global_proof`",
        "",
        "本文用固定 `h=3` 的全量账本抽取小余量窗口，分析 first-factor 负载与低模相位能量。它服务于 `H3 Full-Blocking Defect`，不是全局证明。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`。",
        f"- `margin_threshold`: `{params['margin_threshold']}`。",
        f"- `row_stride`: `{params['row_stride']}`。",
        f"- `small_moduli`: `{params['small_moduli']}`。",
        f"- `max_n`: `{params['max_n']}`。",
        "",
        "## 摘要",
        "",
        f"- 检查 q 行数：`{summary['q_rows_checked']}`。",
        f"- 近失败窗口数：`{summary['near_windows']}`。",
        f"- 全局最小余量：`{summary['min_margin']}`。",
        f"- 全局最大余量：`{summary['max_margin']}`。",
        f"- 近失败余量分布：`{summary['near_margin_counts']}`。",
        f"- 近失败 p 范围：`{summary['near_min_p']}..{summary['near_max_p']}`。",
        f"- 近失败最大 q：`{summary['near_max_q']}`。",
        f"- 近失败最大候选数：`{summary['near_max_candidate_count']}`。",
        f"- 近失败最大阻断数：`{summary['near_max_blocked_count']}`。",
        f"- 初始分支计数：`{summary['initial_type_counts']}`。",
        f"- 近失败分支计数：`{summary['near_initial_type_counts']}`。",
        f"- 聚合首因子 Top：`{summary['near_aggregate_factor_counts_top']}`。",
        f"- 近失败最大首因子负载占比：`{summary['max_top_factor_share_near']}`。",
        f"- 近失败最大低模能量：`{summary['max_lowmod_energy_near']}`。",
        "",
        "## 最紧窗口",
        "",
        "| p | q | row | initial | cand | blocked | margin | top factor | top load | top share | tail>q/2 | max energy mod | max energy |",
        "|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for sample in result["tight_samples"][:20]:
        lines.append(
            "| {p} | {q} | {row} | `{initial}` | {cand} | {blocked} | {margin} | {factor} | {load} | {share:.4f} | {tail:.4f} | {emod} | {energy:.4f} |".format(
                p=sample["p"],
                q=sample["q"],
                row=sample["q_row"],
                initial=sample["initial_type"],
                cand=sample["candidate_count"],
                blocked=sample["blocked_count"],
                margin=sample["margin"],
                factor=sample["top_factor"],
                load=sample["top_factor_load"],
                share=sample["top_factor_share"],
                tail=sample["tail_share_gt_q_over_2"],
                emod=sample["max_lowmod_energy_modulus"],
                energy=sample["max_lowmod_energy"],
            )
        )

    lines.extend(
        [
            "",
            "## 数据洞察",
            "",
            "1. 近失败窗口不是“单一大因子自由补洞”。最紧窗口通常由少数小首因子承担骨架，再由多个中尾首因子补齐。",
            "2. 聚合首因子 Top 显示小首因子长期承担主负载；若继续压向全阻断，必须提高小首因子的固定相位负担，或引入更多中尾首因子产生低模相位方差。",
            "3. 若要把近失败推向真正全阻断，新增阻断必须继续提高某个 first-factor 负载，或增加低模相位能量。",
            "4. 因此 `H3 Full-Blocking Defect` 的正确形式不是单纯计数，而是二分：高负载进入 `Tail/PDEC`，低负载全覆盖进入 `H3-PDEC` 低模能量。",
            "",
            "## 下一步证明义务",
            "",
            "把上表中的经验量升级为同一口径的定理：",
            "",
            "```text",
            "H3 full blocking",
            "=> first-factor high load",
            "   or distributed low-mod energy >= L_PDEC",
            "   or endpoint SAE/ColumnCRT.",
            "```",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--margin-threshold", type=int, default=20)
    parser.add_argument("--row-stride", type=int, default=1)
    parser.add_argument("--small-moduli", type=str, default="5,7,11,13")
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-h3-full-blocking-defect-audit"),
    )
    args = parser.parse_args()
    small_moduli = [
        int(item)
        for item in args.small_moduli.split(",")
        if item.strip()
    ]
    result = audit(
        max_p=args.max_p,
        margin_threshold=args.margin_threshold,
        row_stride=max(1, args.row_stride),
        small_moduli=small_moduli,
    )
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
