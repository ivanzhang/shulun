#!/usr/bin/env python3
"""审计列命题输入对行命题的桥接强度。

用法示例：
  python3 experiments/prime_matrix_column_row_bridge_audit.py --max-q 1000

对每个素数 q，考察 q×q 方阵 [1,q^2]。
列命题只保证每一列至少有一个素数；为了帮助行命题，还需要知道：
固定行 r 附近，每一列最近的素数离 r 有多远。

本脚本输出“列见证半径”

  D_col(r)=max_c min{|r-r'|: 第 c 列第 r' 行为素数}

若 D_col(r) 很小，则列命题在该行附近形成强纵向支撑；
若 D_col(r) 可很大，则列命题本身不能直接推出该行非空。
"""

from __future__ import annotations

import argparse
import bisect
import json
from pathlib import Path


def sieve_bool(n: int) -> bytearray:
    """返回素数布尔表。"""
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0
    for d in range(2, int(n**0.5) + 1):
        if is_prime[d]:
            start = d * d
            is_prime[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return is_prime


def primes_from_table(is_prime: bytearray) -> list[int]:
    """从布尔表提取素数。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def nearest_distance(sorted_rows: list[int], row: int, fallback: int) -> int:
    """计算某列素数行集合到 row 的最近距离。"""
    if not sorted_rows:
        return fallback
    pos = bisect.bisect_left(sorted_rows, row)
    best = fallback
    if pos < len(sorted_rows):
        best = min(best, abs(sorted_rows[pos] - row))
    if pos:
        best = min(best, abs(sorted_rows[pos - 1] - row))
    return best


def audit_prime(q: int, is_prime: bytearray) -> dict:
    """审计单个 q×q 方阵。"""
    row_prime_counts = [0] * q
    prime_rows_by_col: list[list[int]] = [[] for _ in range(q)]

    for n in range(2, q * q + 1):
        if not is_prime[n]:
            continue
        row = (n - 1) // q
        col = (n - 1) % q
        row_prime_counts[row] += 1
        prime_rows_by_col[col].append(row)

    # 第 q 列只含 q 的平凡素数见证，桥接行命题时单独处理；这里聚焦非平凡列 c<q。
    nontrivial_prime_rows_by_col = prime_rows_by_col[: q - 1]
    empty_columns = [
        idx + 1
        for idx, rows in enumerate(nontrivial_prime_rows_by_col)
        if not rows
    ]
    col_radius_rows = []
    max_radius = -1
    min_row_prime_count = min(row_prime_counts)
    min_row_records = []

    for row in range(q):
        distances = [
            nearest_distance(rows, row, q) for rows in nontrivial_prime_rows_by_col
        ]
        radius = max(distances)
        row_record = {
            "row": row + 1,
            "row_interval": [row * q + 1, (row + 1) * q],
            "row_prime_count": row_prime_counts[row],
            "column_witness_radius": radius,
            "nontrivial_columns_with_witness_distance_le_1": sum(
                1 for d in distances if d <= 1
            ),
            "nontrivial_columns_with_witness_distance_le_2": sum(
                1 for d in distances if d <= 2
            ),
            "nontrivial_columns_with_witness_distance_le_5": sum(
                1 for d in distances if d <= 5
            ),
            "max_distance_columns": [
                idx + 1 for idx, dist in enumerate(distances) if dist == radius
            ][:10],
        }
        if radius > max_radius:
            max_radius = radius
            col_radius_rows = [row_record]
        elif radius == max_radius:
            col_radius_rows.append(row_record)
        if row_prime_counts[row] == min_row_prime_count:
            min_row_records.append(row_record)

    low_prime_rows = sorted(
        (
            {
                "row": row + 1,
                "row_interval": [row * q + 1, (row + 1) * q],
                "row_prime_count": row_prime_counts[row],
            }
            for row in range(q)
        ),
        key=lambda item: (item["row_prime_count"], item["row"]),
    )[:10]

    return {
        "q": q,
        "column_theorem_holds_in_data": len(empty_columns) == 0,
        "empty_columns": empty_columns[:10],
        "min_row_prime_count": min_row_prime_count,
        "min_row_records": min_row_records[:10],
        "max_column_witness_radius": max_radius,
        "max_radius_rows": col_radius_rows[:10],
        "low_prime_rows": low_prime_rows,
    }


def audit(max_q: int) -> dict:
    """执行全范围审计。"""
    is_prime = sieve_bool(max_q * max_q + 10)
    primes = [prime for prime in primes_from_table(is_prime) if 3 <= prime <= max_q]
    records = [audit_prime(q, is_prime) for q in primes]

    worst_radius = max(records, key=lambda item: item["max_column_witness_radius"])
    worst_row_count = min(records, key=lambda item: item["min_row_prime_count"])
    column_failures = [
        record for record in records if not record["column_theorem_holds_in_data"]
    ]
    return {
        "parameters": {
            "max_q": max_q,
        },
        "summary": {
            "prime_count": len(records),
            "column_failure_records": len(column_failures),
            "global_min_row_prime_count": min(
                record["min_row_prime_count"] for record in records
            ),
            "worst_min_row_prime_record": worst_row_count,
            "global_max_column_witness_radius": worst_radius[
                "max_column_witness_radius"
            ],
            "worst_column_radius_record": worst_radius,
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    params = result["parameters"]
    summary = result["summary"]
    worst_radius = summary["worst_column_radius_record"]
    worst_min_row = summary["worst_min_row_prime_record"]
    lines = [
        "# 列输入到行命题桥接强度审计",
        "",
        "**状态：** `experimental_column_input_bridge_strength_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_q`: `{params['max_q']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- 数据中列命题失败记录数：`{summary['column_failure_records']}`。",
        f"- 全局最小行素数数：`{summary['global_min_row_prime_count']}`。",
        f"- 最大列见证半径：`{summary['global_max_column_witness_radius']}`。",
        "",
        "## 最薄行记录",
        "",
        f"- `q`: `{worst_min_row['q']}`",
        f"- `min_row_prime_count`: `{worst_min_row['min_row_prime_count']}`",
        f"- `min_row_records`: `{worst_min_row['min_row_records']}`",
        "",
        "## 最大列见证半径记录",
        "",
        f"- `q`: `{worst_radius['q']}`",
        f"- `max_column_witness_radius`: `{worst_radius['max_column_witness_radius']}`",
        f"- `max_radius_rows`: `{worst_radius['max_radius_rows']}`",
        "",
        "## 审稿解释",
        "",
        "列命题若作为已证输入，只能保证每个非平凡列 `c<q` 某处有素数；第 `q` 列只有平凡见证 `q`，本审计已将其从桥接半径中剥离。要推出固定行非空，还需要把这些列素数见证拉回该行附近，或证明拉不回时产生端点/尾锚缺陷。",
        "",
        "本审计量化了这个缺口：`D_col(r)` 是覆盖所有列所需的最小纵向半径。若 `D_col(r)` 无显式小上界，列命题不能直接推出行命题；若能证明坏行导致 `D_col(r)` 异常并触发 CRT 缺陷，则可形成行列闭锁桥接。",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=1000)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-column-row-bridge-audit",
    )
    args = parser.parse_args()
    result = audit(args.max_q)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key not in {"worst_min_row_prime_record", "worst_column_radius_record"}
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
