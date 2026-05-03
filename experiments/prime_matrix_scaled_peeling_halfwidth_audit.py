#!/usr/bin/env python3
"""审计行号缩放递归剥离与半宽素数连续零行设想。

用法示例：
  python3 experiments/prime_matrix_scaled_peeling_halfwidth_audit.py

本脚本使用已知 p 对齐零行样本，检验两个具体推断：

1. 上层零行 row=n 是否严格推出下层缩放行 `n*p/r` 附近的 r 对齐零行；
2. 当下层素数 h 约为 p/2 时，上层长度 p 的零窗是否在 h 网格中自动给出
   连续两个以上零行。

结论用于区分“可作为严证入口的坐标事实”和“需要额外吸收/缺陷定理的猜想”。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from prime_matrix_zero_row_crt_audit import mark_old_sieve_interval, primes_upto


def interval_for_row(width: int, row: int) -> tuple[int, int]:
    """返回给定行宽的对齐行区间。"""
    return (row - 1) * width + 1, row * width


def alive_count(left: int, right: int, small_primes: list[int]) -> int:
    """返回区间中避开 small_primes 的点数。"""
    return mark_old_sieve_interval(left, right, small_primes).count(1)


def contained_rows(left: int, right: int, width: int) -> list[int]:
    """返回完全包含在 [left,right] 中的 width 对齐行号。"""
    first = (left + width - 1) // width
    last = right // width
    return [
        row
        for row in range(first, last + 1)
        if left <= interval_for_row(width, row)[0]
        and interval_for_row(width, row)[1] <= right
    ]


def zero_rows_inside(
    left: int,
    right: int,
    width: int,
    small_primes: list[int],
) -> list[int]:
    """返回包含区间内的 width 对齐零行。"""
    rows = []
    for row in contained_rows(left, right, width):
        row_left, row_right = interval_for_row(width, row)
        if alive_count(row_left, row_right, small_primes) == 0:
            rows.append(row)
    return rows


def consecutive_runs(rows: list[int]) -> list[list[int]]:
    """把行号列表压缩为连续段。"""
    if not rows:
        return []
    runs = [[rows[0]]]
    for row in rows[1:]:
        if row == runs[-1][-1] + 1:
            runs[-1].append(row)
        else:
            runs.append([row])
    return runs


def factor_with_allowed(n: int, primes: list[int]) -> list[int]:
    """用给定素数表分解 n 的相关小因子。"""
    factors = []
    rest = n
    for prime in primes:
        while rest % prime == 0:
            factors.append(prime)
            rest //= prime
        if rest == 1:
            break
    if rest > 1:
        factors.append(rest)
    return factors


def audit(source_path: Path) -> dict:
    """执行缩放与半宽审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    all_primes = primes_upto(source["parameters"]["max_p"] + 100)
    records = []

    for item in source["records"]:
        aligned = item["first_aligned_zero_row_after_p"]
        if not aligned["found"]:
            continue
        top = item["p"]
        top_row = aligned["row"]
        left, right = aligned["interval"]
        top_index = all_primes.index(top)
        prev_prime = all_primes[top_index - 1]
        half_candidates = [prime for prime in all_primes if prime <= top // 2]
        half_prime = half_candidates[-1]

        prev_primes = [prime for prime in all_primes if prime <= prev_prime]
        half_primes = [prime for prime in all_primes if prime <= half_prime]

        scaled_floor = (top_row * top) // prev_prime
        scaled_ceil = -(-(top_row * top) // prev_prime)
        exact_prev_rows = contained_rows(left, right, prev_prime)
        exact_prev_zero_rows = zero_rows_inside(left, right, prev_prime, prev_primes)

        half_rows = contained_rows(left, right, half_prime)
        half_zero_rows = zero_rows_inside(left, right, half_prime, half_primes)
        half_runs = consecutive_runs(half_zero_rows)
        half_alive = mark_old_sieve_interval(left, right, half_primes)
        half_survivors = [
            left + idx for idx, flag in enumerate(half_alive) if flag
        ]
        peeled_primes = [prime for prime in all_primes if half_prime < prime <= top]
        survivor_factor_profiles = [
            {
                "n": n,
                "factors": factor_with_allowed(n, peeled_primes),
            }
            for n in half_survivors[:20]
        ]

        records.append(
            {
                "top_prime": top,
                "top_zero_row": top_row,
                "top_interval": [left, right],
                "previous_prime": prev_prime,
                "scaled_row_floor_nP_over_prev": scaled_floor,
                "scaled_row_ceil_nP_over_prev": scaled_ceil,
                "exact_contained_prev_rows": exact_prev_rows,
                "exact_contained_prev_zero_rows": exact_prev_zero_rows,
                "half_prime": half_prime,
                "top_length_over_half": top / half_prime,
                "exact_contained_half_rows": half_rows,
                "exact_contained_half_zero_rows": half_zero_rows,
                "half_zero_runs": half_runs,
                "max_half_zero_run_length": max((len(run) for run in half_runs), default=0),
                "half_sieve_survivor_count_in_top_interval": len(half_survivors),
                "half_sieve_survivors": half_survivors[:20],
                "half_survivor_factor_profiles": survivor_factor_profiles,
            }
        )

    return {
        "status": "scaled_peeling_halfwidth_audit_refutes_automatic_consecutive_zero_rows",
        "source": str(source_path),
        "summary": {
            "records": len(records),
            "records_with_prev_scaled_zero": sum(
                1 for record in records if record["exact_contained_prev_zero_rows"]
            ),
            "records_with_two_or_more_half_zero_rows": sum(
                1
                for record in records
                if record["max_half_zero_run_length"] >= 2
            ),
            "max_half_zero_run_length": max(
                (record["max_half_zero_run_length"] for record in records),
                default=0,
            ),
            "min_top_length_over_half": min(
                (record["top_length_over_half"] for record in records),
                default=None,
            ),
            "max_top_length_over_half": max(
                (record["top_length_over_half"] for record in records),
                default=None,
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 摘要。"""
    summary = result["summary"]
    lines = [
        "# 缩放递归剥离与半宽连续零行审计",
        "",
        "**状态：** `scaled_peeling_halfwidth_audit_refutes_automatic_consecutive_zero_rows`",
        "",
        "## 总结",
        "",
        f"- 样本记录数：`{summary['records']}`。",
        f"- 缩放到前一素数后含完整下层零行的记录数：`{summary['records_with_prev_scaled_zero']}`。",
        f"- 半宽素数下出现连续两个以上零行的记录数：`{summary['records_with_two_or_more_half_zero_rows']}`。",
        f"- 最大半宽连续零行段长度：`{summary['max_half_zero_run_length']}`。",
        f"- `top/half_prime` 范围：`{summary['min_top_length_over_half']}` 到 `{summary['max_top_length_over_half']}`。",
        "",
        "## 逐例表",
        "",
        "| top P | row n | prev | scaled floor/ceil | contained prev zero rows | half prime | contained half rows | contained half zero rows | max run | half survivors |",
        "|---:|---:|---:|---|---|---:|---|---|---:|---:|",
    ]
    for record in result["records"]:
        lines.append(
            "| {top} | {row} | {prev} | `{floor}/{ceil}` | `{prev_zero}` | {half} | `{half_rows}` | `{half_zero}` | {run} | {surv} |".format(
                top=record["top_prime"],
                row=record["top_zero_row"],
                prev=record["previous_prime"],
                floor=record["scaled_row_floor_nP_over_prev"],
                ceil=record["scaled_row_ceil_nP_over_prev"],
                prev_zero=record["exact_contained_prev_zero_rows"],
                half=record["half_prime"],
                half_rows=record["exact_contained_half_rows"],
                half_zero=record["exact_contained_half_zero_rows"],
                run=record["max_half_zero_run_length"],
                surv=record["half_sieve_survivor_count_in_top_interval"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "本审计使用的是已知 `P` 对齐零行样本，作为缩放/半宽机制的模型检验；它不是假想 `q×q` 早期零行的存在证书。",
            "",
            "`nP/p` 只是定位同一数轴高度的近似行号。严格结论必须用区间包含判据：上层零窗是否完整包含某条下层对齐行。若不完整包含，只能得到缝合零窗。",
            "",
            "即使选择约 `P/2` 的半宽素数，使上层长度超过两倍下层行宽，也不能自动得到连续两个下层零行。原因是剥到半宽筛时，原上层零窗内会复活所有最小素因子位于 `(half_prime,P]` 的点；这些复活点会打断潜在的连续零行。",
            "",
            "因此该路线的可证版本仍应表述为：若这些复活点全部被继续吸收，则吸收过程必须触发 `ColumnCRT/TailAnchor/ColumnRadius`，而不是直接诉诸连续零行与镜像矛盾。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-zero-row-crt-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit"),
    )
    args = parser.parse_args()
    result = audit(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
