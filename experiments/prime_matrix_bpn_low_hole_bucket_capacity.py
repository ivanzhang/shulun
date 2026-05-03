#!/usr/bin/env python3
"""BPN low-hole bucket 高层补洞容量扫描。

用法示例：
  python3 experiments/prime_matrix_bpn_low_hole_bucket_capacity.py
  python3 experiments/prime_matrix_bpn_low_hole_bucket_capacity.py --p-values 13,17,19,23,29,31,37,43,47 --q 210

核心思想：
- 固定低模 `Q`，先只用 `Q` 中的小素数形成低骨架洞集 `H_Q(t)`；
- 对每个低相位 `t mod Q`，用剩余高根基素数的 CRT 变量 `y`，其中 `r=t+Qy`；
- 用残基类 set-cover 动态规划精确计算有多少 `y mod M_high` 能补完全部低骨架洞。

这把 `low-hole bucket` 从整周期行枚举改写为低骨架洞集上的高层补洞容量问题。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from math import prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def low_holes_for_phase(p: int, q: int, low_primes: list[int], phase: int) -> list[int]:
    """返回低骨架在相位 phase 下未覆盖的列。"""
    holes = []
    for col in range(1, p):
        value_residue_zero = False
        for prime in low_primes:
            if ((phase - 1) * p + col) % prime == 0:
                value_residue_zero = True
                break
        if not value_residue_zero:
            holes.append(col)
    return holes


def high_completion_stats(
    p: int,
    q: int,
    phase: int,
    holes: list[int],
    high_primes: list[int],
) -> dict[str, int]:
    """用 set-cover DP 精确计算高层 CRT 变量 y 的补洞统计。"""
    if not holes:
        high_period = prod(high_primes) if high_primes else 1
        return {
            "completion_count": high_period,
            "max_single_residue_class_cover": 0,
            "simple_capacity_sum": 0,
            "best_hall_deficit": 0,
            "best_hall_subset_size": 0,
            "best_hall_subset_holes": [],
            "min_hall_complement_size": None,
            "min_hall_deficit": 0,
            "min_hall_subset_holes": [],
        }
    hole_index = {col: index for index, col in enumerate(holes)}
    full_mask = (1 << len(holes)) - 1
    high_period = prod(high_primes) if high_primes else 1

    coverage_tables: dict[int, list[int]] = {}
    for prime in high_primes:
        inverse_p = pow(p, -1, prime)
        inverse_q = pow(q % prime, -1, prime)
        table = [0] * prime
        for col in holes:
            target_row_residue = (1 - col * inverse_p) % prime
            y_residue = ((target_row_residue - phase) * inverse_q) % prime
            table[y_residue] |= 1 << hole_index[col]
        coverage_tables[prime] = table

    max_single_residue_class_cover = max(
        (mask.bit_count() for table in coverage_tables.values() for mask in table),
        default=0,
    )
    simple_capacity_sum = sum(
        max(mask.bit_count() for mask in coverage_tables[prime])
        for prime in high_primes
    )

    # CRT 使每个高素数的 y residue 可独立选择；因此补洞计数等于
    # 每个高素数选一个残基类时，其覆盖掩码并集为 full_mask 的选择数。
    dp: dict[int, int] = {0: 1}
    for prime in high_primes:
        # 同一个覆盖掩码可能由多个残基给出，先合并可显著减少 DP 分支。
        mask_counts = Counter(coverage_tables[prime])
        next_dp: dict[int, int] = {}
        for old_mask, old_count in dp.items():
            for prime_mask, multiplicity in mask_counts.items():
                new_mask = old_mask | prime_mask
                next_dp[new_mask] = next_dp.get(new_mask, 0) + old_count * multiplicity
        dp = next_dp
    count = dp.get(full_mask, 0)
    best_hall_deficit = 0
    best_hall_subset_size = 0
    best_hall_subset_mask = 0
    min_hall_complement_size: int | None = None
    min_hall_deficit = 0
    min_hall_subset_mask = 0
    if count == 0 and len(holes) <= 18:
        for subset in range(1, full_mask + 1):
            subset_size = subset.bit_count()
            capacity = 0
            for prime in high_primes:
                capacity += max(
                    (prime_mask & subset).bit_count()
                    for prime_mask in coverage_tables[prime]
                )
            deficit = subset_size - capacity
            if deficit > best_hall_deficit:
                best_hall_deficit = deficit
                best_hall_subset_size = subset_size
                best_hall_subset_mask = subset
            if deficit > 0:
                complement_size = len(holes) - subset_size
                if (
                    min_hall_complement_size is None
                    or complement_size < min_hall_complement_size
                    or (
                        complement_size == min_hall_complement_size
                        and deficit > min_hall_deficit
                    )
                ):
                    min_hall_complement_size = complement_size
                    min_hall_deficit = deficit
                    min_hall_subset_mask = subset
    best_hall_subset_holes = [
        col for index, col in enumerate(holes)
        if (best_hall_subset_mask >> index) & 1
    ]
    min_hall_subset_holes = [
        col for index, col in enumerate(holes)
        if (min_hall_subset_mask >> index) & 1
    ]
    return {
        "completion_count": count,
        "max_single_residue_class_cover": max_single_residue_class_cover,
        "simple_capacity_sum": simple_capacity_sum,
        "best_hall_deficit": best_hall_deficit,
        "best_hall_subset_size": best_hall_subset_size,
        "best_hall_subset_holes": best_hall_subset_holes,
        "min_hall_complement_size": min_hall_complement_size,
        "min_hall_deficit": min_hall_deficit,
        "min_hall_subset_holes": min_hall_subset_holes,
    }


def scan_prime(p: int, q: int) -> dict[str, Any]:
    """扫描单个 P 的 low-hole bucket 高层补洞容量。"""
    base_primes = primes_upto(p - 1)
    period = prod(base_primes)
    if period % q != 0:
        raise ValueError(f"q={q} 不整除 P={p} 的根基 CRT 周期 {period}")
    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]
    high_period = prod(high_primes) if high_primes else 1

    phase_rows = []
    bucket_bounds: Counter[int] = Counter()
    bucket_phase_counts: Counter[int] = Counter()
    nonzero_phases = 0
    max_completion = 0
    for phase in range(q):
        holes = low_holes_for_phase(p, q, low_primes, phase)
        stats = high_completion_stats(p, q, phase, holes, high_primes)
        count = stats["completion_count"]
        if count:
            nonzero_phases += 1
            max_completion = max(max_completion, count)
        hole_count = len(holes)
        bucket_phase_counts[hole_count] += 1
        bucket_bounds[hole_count] += count
        phase_rows.append(
            {
                "phase": phase,
                "low_hole_count": hole_count,
                "completion_count": count,
                "max_single_residue_class_cover": stats["max_single_residue_class_cover"],
                "simple_capacity_sum": stats["simple_capacity_sum"],
                "best_hall_deficit": stats["best_hall_deficit"],
                "best_hall_subset_size": stats["best_hall_subset_size"],
                "best_hall_subset_holes": stats["best_hall_subset_holes"],
                "min_hall_complement_size": stats["min_hall_complement_size"],
                "min_hall_deficit": stats["min_hall_deficit"],
                "min_hall_subset_holes": stats["min_hall_subset_holes"],
                "holes": holes,
            }
        )

    threshold_rows = []
    for threshold in sorted(set(bucket_phase_counts)):
        phases = [row for row in phase_rows if row["low_hole_count"] >= threshold]
        threshold_rows.append(
            {
                "threshold": threshold,
                "phase_count": len(phases),
                "completion_bound": sum(row["completion_count"] for row in phases),
            }
        )

    positive_rows = [row for row in phase_rows if row["completion_count"] > 0]
    max_low_holes_with_completion = max(
        (row["low_hole_count"] for row in positive_rows),
        default=None,
    )
    max_single_residue_class_cover = max(
        (row["max_single_residue_class_cover"] for row in positive_rows),
        default=0,
    )
    max_simple_capacity_sum_on_completion = max(
        (row["simple_capacity_sum"] for row in positive_rows),
        default=0,
    )
    capacity_deficit_zero_rows = [
        row for row in phase_rows
        if row["low_hole_count"] > row["simple_capacity_sum"]
    ]
    zero_rows = [row for row in phase_rows if row["completion_count"] == 0]
    hall_certified_zero_rows = [
        row for row in zero_rows if row["best_hall_deficit"] > 0
    ]
    whole_hole_hall_rows = [
        row for row in hall_certified_zero_rows
        if row["min_hall_complement_size"] == 0
    ]
    one_deletion_hall_rows = [
        row for row in hall_certified_zero_rows
        if row["min_hall_complement_size"] == 1
    ]
    witness_complement_histogram = Counter(
        row["min_hall_complement_size"]
        for row in hall_certified_zero_rows
    )
    two_plus_deletion_hall_rows = [
        row for row in hall_certified_zero_rows
        if (
            row["min_hall_complement_size"] is not None
            and row["min_hall_complement_size"] >= 2
        )
    ]
    min_low_holes_without_completion = min(
        (row["low_hole_count"] for row in phase_rows if row["completion_count"] == 0),
        default=None,
    )

    return {
        "p": p,
        "q": q,
        "base_primes": base_primes,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "period": period,
        "high_period": high_period,
        "total_completion_count": sum(row["completion_count"] for row in phase_rows),
        "nonzero_phase_count": nonzero_phases,
        "max_completion_per_phase": max_completion,
        "max_low_holes_with_completion": max_low_holes_with_completion,
        "high_prime_count": len(high_primes),
        "max_single_residue_class_cover": max_single_residue_class_cover,
        "max_simple_capacity_sum_on_completion": max_simple_capacity_sum_on_completion,
        "capacity_deficit_phase_count": len(capacity_deficit_zero_rows),
        "capacity_deficit_completion_sum": sum(
            row["completion_count"] for row in capacity_deficit_zero_rows
        ),
        "zero_phase_count": len(zero_rows),
        "hall_certified_zero_phase_count": len(hall_certified_zero_rows),
        "hall_uncertified_zero_phase_count": len(zero_rows) - len(hall_certified_zero_rows),
        "whole_hole_hall_phase_count": len(whole_hole_hall_rows),
        "one_deletion_hall_phase_count": len(one_deletion_hall_rows),
        "two_plus_deletion_hall_phase_count": len(two_plus_deletion_hall_rows),
        "hall_witness_complement_histogram": dict(
            sorted(witness_complement_histogram.items())
        ),
        "max_hall_deficit": max(
            (row["best_hall_deficit"] for row in hall_certified_zero_rows),
            default=0,
        ),
        "hall_witness_examples": [
            {
                "phase": row["phase"],
                "holes": row["holes"],
                "witness_holes": row["min_hall_subset_holes"],
                "deficit": row["min_hall_deficit"],
                "deleted_holes": [
                    col for col in row["holes"]
                    if col not in set(row["min_hall_subset_holes"])
                ],
                "min_complement_size": row["min_hall_complement_size"],
                "max_deficit": row["best_hall_deficit"],
            }
            for row in hall_certified_zero_rows[:8]
        ],
        "min_low_holes_without_completion": min_low_holes_without_completion,
        "threshold_rows": threshold_rows,
        "top_completion_phases": sorted(
            positive_rows,
            key=lambda row: row["completion_count"],
            reverse=True,
        )[:12],
        "zero_completion_high_hole_examples": [
            row for row in phase_rows if row["completion_count"] == 0
        ][:12],
    }


def run(p_values: list[int], q: int) -> dict[str, Any]:
    """运行多 P 扫描。"""
    results = [scan_prime(p, q) for p in p_values]
    return {
        "certificate_type": "prime_matrix_bpn_low_hole_bucket_capacity",
        "status": "low_hole_bucket_reduced_to_high_layer_crt_completion_capacity",
        "q": q,
        "results": results,
        "review_conclusion": (
            "low-hole bucket 已改写为高层 CRT 补洞容量：固定低相位 t 后，"
            "每个高根基素数只能选择一个 y 残基类，问题精确等价于多素数残基类"
            " set-cover。该 DP 比整周期行枚举更接近符号证明；下一步是把"
            " capacity deficit 或 Hall deficit 写成一般定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN low-hole bucket 高层补洞容量扫描",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总表",
        "",
        "| P | Q | high primes | M_high | total completions | nonzero phases | max cap | max holes with completion | min holes without completion |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["results"]:
        lines.append(
            "| {p} | {q} | `{high}` | {mh} | {total} | {nonzero} | {maxcap} | {maxholes} | {minzero} |".format(
                p=row["p"],
                q=row["q"],
                high=row["high_primes"],
                mh=row["high_period"],
                total=row["total_completion_count"],
                nonzero=row["nonzero_phase_count"],
                maxcap=row["max_completion_per_phase"],
                maxholes=row["max_low_holes_with_completion"],
                minzero=row["min_low_holes_without_completion"],
            )
        )

    lines.extend(
        [
            "",
            "## 1A. 残基类容量诊断",
            "",
            "| P | high prime count | max holes with completion | max single residue-class cover | max simple capacity on completion | deficit phases | deficit completion sum |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["results"]:
        lines.append(
            "| {p} | {hpc} | {maxholes} | {single} | {capacity} | {deficits} | {deficit_sum} |".format(
                p=row["p"],
                hpc=row["high_prime_count"],
                maxholes=row["max_low_holes_with_completion"],
                single=row["max_single_residue_class_cover"],
                capacity=row["max_simple_capacity_sum_on_completion"],
                deficits=row["capacity_deficit_phase_count"],
                deficit_sum=row["capacity_deficit_completion_sum"],
            )
        )

    lines.extend(
        [
            "",
            "## 1B. Hall 亏损证书覆盖",
            "",
            "| P | zero phases | Hall-certified | W=H | W=H\\\\{c} | W删2+洞 | uncertified | max Hall deficit |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["results"]:
        lines.append(
            "| {p} | {zero} | {cert} | {whole} | {one_del} | {two_plus} | {uncert} | {deficit} |".format(
                p=row["p"],
                zero=row["zero_phase_count"],
                cert=row["hall_certified_zero_phase_count"],
                whole=row["whole_hole_hall_phase_count"],
                one_del=row["one_deletion_hall_phase_count"],
                two_plus=row["two_plus_deletion_hall_phase_count"],
                uncert=row["hall_uncertified_zero_phase_count"],
                deficit=row["max_hall_deficit"],
            )
        )

    lines.extend(
        [
            "",
            "## 1B+. Hall 见证删洞数分布",
            "",
            "`删洞数 = |H_Q(t)|-|W|`。删洞数为 `0` 表示整洞集见证，`1` 表示一洞删除见证。",
            "",
            "| P | complement-size histogram |",
            "| ---: | --- |",
        ]
    )
    for row in result["results"]:
        lines.append(
            f"| {row['p']} | `{row['hall_witness_complement_histogram']}` |"
        )

    lines.extend(
        [
            "",
            "## 1C. Hall 见证样例",
            "",
        ]
    )
    for row in result["results"]:
        if not row["hall_witness_examples"]:
            continue
        lines.extend([f"### P={row['p']}", ""])
        lines.append("| phase | holes | witness W | deleted | min d | deficit | max deficit |")
        lines.append("| ---: | --- | --- | --- | ---: | ---: | ---: |")
        for item in row["hall_witness_examples"][:5]:
            lines.append(
                f"| {item['phase']} | `{item['holes']}` | `{item['witness_holes']}` | `{item['deleted_holes']}` | {item['min_complement_size']} | {item['deficit']} | {item['max_deficit']} |"
            )
        lines.append("")

    lines.extend(
        [
            "",
            "## 2. Threshold bucket",
            "",
        ]
    )
    for row in result["results"]:
        lines.extend(
            [
                f"### P={row['p']}",
                "",
                "| threshold h | phase count | completion bound |",
                "| ---: | ---: | ---: |",
            ]
        )
        for bucket in row["threshold_rows"]:
            lines.append(
                f"| {bucket['threshold']} | {bucket['phase_count']} | {bucket['completion_bound']} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 3. 形式化目标",
            "",
            "固定低相位 `t mod Q`，设低骨架洞集为 `H_Q(t)`。对每个高根基素数 `ell` 和洞 `c`，",
            "补洞条件是一个关于 `y` 的同余：",
            "",
            "\\[",
            "y\\equiv (1-cP^{-1}-t)Q^{-1}\\pmod \\ell.",
            "\\]",
            "",
            "因此 `completion_count(t)` 是一个有限 CRT 覆盖问题。若能证明当 `|H_Q(t)|` 超过阈值时",
            "这些同余类族不能共同覆盖所有洞，就得到 `low-hole bucket` 的符号上界。",
            "",
            "更精确地说，每个高素数 `ell` 只能选择一个 `y mod ell` 残基类，因此只能覆盖",
            "`H_Q(t)` 中落在同一个 `mod ell` 残基类的洞。补洞非空等价于这些残基类在所有",
            "高素数上的一次选择能覆盖 `H_Q(t)`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_p_values(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-values", default="13,17,19,23,29,31,37,43,47")
    parser.add_argument("--q", type=int, default=210)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-low-hole-bucket-capacity.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-low-hole-bucket-capacity.md",
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
