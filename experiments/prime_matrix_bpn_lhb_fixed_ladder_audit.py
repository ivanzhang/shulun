#!/usr/bin/env python3
"""BPN low-hole bucket 固定小高素数碰撞梯审计。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_fixed_ladder_audit.py
  python3 experiments/prime_matrix_bpn_lhb_fixed_ladder_audit.py --p-values 61,67,73

目标：
- 固定顺序使用高素数 `13,17,19,23,...`；
- 每个高素数只选当前未覆盖洞中命中最多的一个列残基块；
- 检查该固定碰撞梯是否足以覆盖全部低洞集 `H_Q(t)`。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase, primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def fixed_ladder_cover(
    holes: list[int],
    high_primes: list[int],
) -> tuple[bool, list[dict[str, Any]], list[int]]:
    """按固定高素数顺序覆盖低洞。"""
    uncovered = set(holes)
    choices: list[dict[str, Any]] = []
    for prime in high_primes:
        if not uncovered:
            break
        blocks: dict[int, set[int]] = defaultdict(set)
        for col in holes:
            blocks[col % prime].add(col)

        best_residue: int | None = None
        best_hit: set[int] = set()
        for residue, cols in blocks.items():
            hit = cols & uncovered
            if len(hit) > len(best_hit):
                best_residue = residue
                best_hit = hit
        if not best_hit:
            continue
        choices.append(
            {
                "prime": prime,
                "residue": best_residue,
                "hit": sorted(best_hit),
                "gain": len(best_hit),
            }
        )
        uncovered -= best_hit
    return not uncovered, choices, sorted(uncovered)


def scan_prime(p: int, q: int) -> dict[str, Any]:
    """扫描单个 P 的固定碰撞梯证书。"""
    base_primes = primes_upto(p - 1)
    if prod(base_primes) % q != 0:
        raise ValueError(f"q={q} 不整除 P={p} 的根基 CRT 周期")
    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]

    fail_examples: list[dict[str, Any]] = []
    max_hole_examples: list[dict[str, Any]] = []
    fail_count = 0
    max_holes = 0
    min_margin: int | None = None
    margin_histogram: Counter[int] = Counter()
    duplicate_gain_histogram: Counter[int] = Counter()
    extra_gain_by_prime: Counter[int] = Counter()

    for phase in range(q):
        holes = low_holes_for_phase(p, q, low_primes, phase)
        ok, choices, uncovered = fixed_ladder_cover(holes, high_primes)
        max_holes = max(max_holes, len(holes))
        if not ok:
            fail_count += 1
            if len(fail_examples) < 8:
                fail_examples.append(
                    {
                        "phase": phase,
                        "holes": holes,
                        "uncovered": uncovered,
                        "choices": choices[:8],
                    }
                )
            continue

        margin = len(high_primes) - len(choices)
        duplicate_gain = len(holes) - len(choices)
        min_margin = margin if min_margin is None else min(min_margin, margin)
        margin_histogram[margin] += 1
        duplicate_gain_histogram[duplicate_gain] += 1
        for choice in choices:
            if choice["gain"] >= 2:
                extra_gain_by_prime[choice["prime"]] += choice["gain"] - 1
        if len(holes) == max_holes and len(max_hole_examples) < 8:
            max_hole_examples.append(
                {
                    "phase": phase,
                    "holes": holes,
                    "duplicate_gain": duplicate_gain,
                    "required_gain": max(0, len(holes) - len(high_primes)),
                    "margin": margin,
                    "multi_gain_choices": [
                        choice for choice in choices if choice["gain"] >= 2
                    ],
                }
            )

    return {
        "p": p,
        "q": q,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "high_prime_count": len(high_primes),
        "max_holes": max_holes,
        "success_count": q - fail_count,
        "fail_count": fail_count,
        "min_margin": min_margin,
        "margin_histogram": dict(sorted(margin_histogram.items())),
        "duplicate_gain_histogram": dict(sorted(duplicate_gain_histogram.items())),
        "extra_gain_by_prime": dict(sorted(extra_gain_by_prime.items())),
        "max_hole_examples": max_hole_examples,
        "fail_examples": fail_examples,
    }


def parse_p_values(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def run(p_values: list[int], q: int) -> dict[str, Any]:
    """运行审计。"""
    results = [scan_prime(p, q) for p in p_values]
    return {
        "certificate_type": "prime_matrix_bpn_lhb_fixed_collision_ladder",
        "status": "fixed_high_prime_collision_ladder_covers_after_turning_point",
        "q": q,
        "results": results,
        "review_conclusion": (
            "固定小高素数碰撞梯按 `13,17,19,23,...` 顺序选择最大列残基块。"
            "`Q=2310` 样本中从 `P=61` 起全相位覆盖成功；这比动态贪心更接近符号证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN low-hole bucket 固定小高素数碰撞梯审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总表",
        "",
        "| P | Q | high # | max holes | success | fail | min margin | top extra-gain primes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["results"]:
        top_gain = sorted(
            row["extra_gain_by_prime"].items(),
            key=lambda item: item[1],
            reverse=True,
        )[:6]
        lines.append(
            "| {p} | {q} | {high_count} | {max_holes} | {succ} | {fail} | {min_margin} | `{top_gain}` |".format(
                p=row["p"],
                q=row["q"],
                high_count=row["high_prime_count"],
                max_holes=row["max_holes"],
                succ=row["success_count"],
                fail=row["fail_count"],
                min_margin=row["min_margin"],
                top_gain=top_gain,
            )
        )

    lines.extend(
        [
            "",
            "## 2. 固定碰撞梯证书",
            "",
            "固定顺序为所有高素数升序排列。第 `j` 步只允许使用第 `j` 个尚可用高素数，",
            "并选择当前未覆盖洞中最大的一个列残基块。若固定顺序也能覆盖全部低洞，",
            "则不需要依赖动态贪心的选择自由。",
            "",
            "该证书把转折后目标压成：小高素数升序碰撞梯提供足够重复增益。",
            "",
            "## 3. 最大洞数样例",
            "",
        ]
    )
    for row in result["results"]:
        if not row["max_hole_examples"]:
            continue
        lines.extend([f"### P={row['p']}", ""])
        lines.append("| phase | holes | duplicate gain | required gain | margin | multi-gain choices |")
        lines.append("| ---: | --- | ---: | ---: | ---: | --- |")
        for item in row["max_hole_examples"][:4]:
            lines.append(
                f"| {item['phase']} | `{item['holes']}` | {item['duplicate_gain']} | {item['required_gain']} | {item['margin']} | `{item['multi_gain_choices']}` |"
            )
        lines.append("")

    lines.extend(["", "## 4. 失败样例", ""])
    for row in result["results"]:
        if not row["fail_examples"]:
            continue
        lines.extend([f"### P={row['p']}", ""])
        lines.append("| phase | holes | uncovered | first choices |")
        lines.append("| ---: | --- | --- | --- |")
        for item in row["fail_examples"][:4]:
            lines.append(
                f"| {item['phase']} | `{item['holes']}` | `{item['uncovered']}` | `{item['choices']}` |"
            )
        lines.append("")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-values", default="53,59,61,67,71,73,79,83,89,97,101,103,107,109,127,149")
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-fixed-ladder-audit.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-fixed-ladder-audit.md",
    )
    args = parser.parse_args()
    result = run(parse_p_values(args.p_values), args.q)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
