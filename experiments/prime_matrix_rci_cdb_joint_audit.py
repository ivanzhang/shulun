#!/usr/bin/env python3
"""联合审计 RCI/PDEC 与 CDB 列位移桥接。

用法示例：
  python3 experiments/prime_matrix_rci_cdb_joint_audit.py --max-p 1000

本脚本同时统计终端行的：
1. RCI 账本：无尾储备、单尾抵消、多尾碰撞超额；
2. CDB 账本：同列素数见证半径、双尾列的见证位移、尾锚集中度。

目标不是证明定理，而是定位最小硬点：
RCI 若变紧，是否同时表现为列位移异常或尾锚集中。
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
from collections import Counter
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
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def next_prime(p: int, primes: list[int]) -> int:
    """返回大于 p 的下一素数。"""
    for prime in primes:
        if prime > p:
            return prime
    raise ValueError("素数表范围不足")


def nearest_row(sorted_rows: list[int], row: int) -> tuple[int | None, int | None]:
    """返回某列距离 row 最近的素数行与距离。行号为 1-based。"""
    if not sorted_rows:
        return None, None
    pos = bisect.bisect_left(sorted_rows, row)
    best_row = None
    best_distance = None
    for idx in (pos - 1, pos):
        if 0 <= idx < len(sorted_rows):
            candidate = sorted_rows[idx]
            distance = abs(candidate - row)
            if best_distance is None or distance < best_distance:
                best_distance = distance
                best_row = candidate
    return best_row, best_distance


def column_prime_rows(q: int, is_prime: bytearray) -> list[list[int]]:
    """返回 q×q 方阵中每列的素数行列表，行号为 1-based。"""
    rows_by_col: list[list[int]] = [[] for _ in range(q + 1)]
    for n in range(2, q * q + 1):
        if not is_prime[n]:
            continue
        row = (n - 1) // q + 1
        col = (n - 1) % q + 1
        rows_by_col[col].append(row)
    return rows_by_col


def low_rough_and_tail_omega(
    q: int,
    y: int,
    low_primes: list[int],
    tail_primes: list[int],
) -> tuple[bytearray, bytearray, dict[int, list[int]]]:
    """构造低筛骨架、尾素因子个数和每个 n 的尾标签列表。"""
    q_square = q * q
    low_rough = bytearray(b"\x01") * (q_square + 1)
    low_rough[0] = 0
    low_rough[1] = 0
    low_rough[q_square] = 0
    for ell in low_primes:
        low_rough[0 : q_square + 1 : ell] = b"\x00" * ((q_square // ell) + 1)

    tail_omega = bytearray(q_square + 1)
    tail_labels: dict[int, list[int]] = {}
    for ell in tail_primes:
        for pos in range(ell, q_square + 1, ell):
            if not low_rough[pos]:
                continue
            if tail_omega[pos] < 255:
                tail_omega[pos] += 1
            tail_labels.setdefault(pos, []).append(ell)
    return low_rough, tail_omega, tail_labels


def audit(max_p: int, y_ratio: float, keep_rows: int) -> dict:
    """执行联合审计。"""
    is_prime = sieve_bool(max_p * max_p + max_p * 20 + 10000)
    primes = primes_from_table(is_prime)
    target_primes = [prime for prime in primes if 3 <= prime <= max_p]

    records = []
    row_records = []

    for p in target_primes:
        q = next_prime(p, primes)
        y = max(2, int(math.floor(y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]
        rows_by_col = column_prime_rows(q, is_prime)
        low_rough, tail_omega, tail_labels = low_rough_and_tail_omega(
            q=q,
            y=y,
            low_primes=low_primes,
            tail_primes=tail_primes,
        )

        min_margin = None
        min_row_record = None
        max_radius_on_tight_rows = 0
        local_rows = []

        for row in range(1, q + 1):
            left = (row - 1) * q + 1
            right = row * q
            no_tail = 0
            one_tail = 0
            multi_count = 0
            multi_excess = 0
            multi_columns = []
            tail_label_counter: Counter[int] = Counter()
            displacement_residue_counter: Counter[tuple[int, int]] = Counter()
            max_witness_distance = 0
            multi_max_witness_distance = 0
            nontrivial_columns_with_witness_le_2 = 0
            nontrivial_columns_with_witness_le_5 = 0

            for col in range(1, q):
                witness_row, distance = nearest_row(rows_by_col[col], row)
                if distance is None:
                    distance = q
                max_witness_distance = max(max_witness_distance, distance)
                if distance <= 2:
                    nontrivial_columns_with_witness_le_2 += 1
                if distance <= 5:
                    nontrivial_columns_with_witness_le_5 += 1

                n = (row - 1) * q + col
                if n < left or n > right or not low_rough[n]:
                    continue
                omega = tail_omega[n]
                if omega == 0:
                    no_tail += 1
                elif omega == 1:
                    one_tail += 1
                else:
                    labels = tail_labels.get(n, [])
                    multi_count += 1
                    multi_excess += omega - 1
                    multi_columns.append(col)
                    multi_max_witness_distance = max(
                        multi_max_witness_distance, distance
                    )
                    for ell in labels:
                        tail_label_counter[ell] += 1
                        if witness_row is not None:
                            displacement = witness_row - row
                            displacement_residue_counter[(ell, displacement % ell)] += 1

            # 第 q 列单独计入 RCI，但不计入非平凡列位移桥。
            n = row * q
            if 1 < n < q * q and low_rough[n]:
                omega = tail_omega[n]
                if omega == 0:
                    no_tail += 1
                elif omega == 1:
                    one_tail += 1
                else:
                    multi_count += 1
                    multi_excess += omega - 1
                    for ell in tail_labels.get(n, []):
                        tail_label_counter[ell] += 1

            margin = no_tail - multi_excess
            max_tail_label_load = max(tail_label_counter.values(), default=0)
            max_displacement_residue_load = max(
                displacement_residue_counter.values(), default=0
            )
            row_record = {
                "p": p,
                "q": q,
                "y": y,
                "row": row,
                "row_interval": [left, right],
                "rci_margin": margin,
                "no_tail_reserve": no_tail,
                "one_tail_cancelled": one_tail,
                "multi_tail_count": multi_count,
                "multi_tail_excess": multi_excess,
                "max_column_witness_radius": max_witness_distance,
                "multi_columns": multi_columns[:20],
                "multi_max_witness_distance": multi_max_witness_distance,
                "nontrivial_columns_with_witness_le_2": (
                    nontrivial_columns_with_witness_le_2
                ),
                "nontrivial_columns_with_witness_le_5": (
                    nontrivial_columns_with_witness_le_5
                ),
                "max_tail_label_load": max_tail_label_load,
                "max_displacement_residue_load": max_displacement_residue_load,
            }
            local_rows.append(row_record)
            if min_margin is None or margin < min_margin:
                min_margin = margin
                min_row_record = row_record

        tight_rows = sorted(local_rows, key=lambda item: item["rci_margin"])[:keep_rows]
        max_radius_on_tight_rows = max(
            (item["max_column_witness_radius"] for item in tight_rows),
            default=0,
        )
        records.append(
            {
                "p": p,
                "q": q,
                "y": y,
                "min_rci_margin": min_margin,
                "min_row_record": min_row_record,
                "max_column_radius_among_tight_rows": max_radius_on_tight_rows,
                "tight_rows": tight_rows,
            }
        )
        row_records.extend(tight_rows)

    worst_margin = sorted(row_records, key=lambda item: item["rci_margin"])[:20]
    worst_radius = sorted(
        row_records, key=lambda item: item["max_column_witness_radius"], reverse=True
    )[:20]
    worst_tail_load = sorted(
        row_records,
        key=lambda item: (item["max_tail_label_load"], item["multi_tail_excess"]),
        reverse=True,
    )[:20]
    return {
        "parameters": {
            "max_p": max_p,
            "y_ratio": y_ratio,
            "keep_rows": keep_rows,
        },
        "summary": {
            "prime_count": len(records),
            "global_min_rci_margin": min(
                record["min_rci_margin"] for record in records
            ),
            "global_max_column_radius_on_tight_rows": max(
                record["max_column_radius_among_tight_rows"] for record in records
            ),
            "global_max_tail_label_load_on_tight_rows": max(
                row["max_tail_label_load"] for row in row_records
            ),
            "global_max_displacement_residue_load_on_tight_rows": max(
                row["max_displacement_residue_load"] for row in row_records
            ),
            "worst_margin_rows": worst_margin,
            "worst_radius_rows": worst_radius,
            "worst_tail_load_rows": worst_tail_load,
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# RCI/PDEC 与 CDB 联合审计",
        "",
        "**状态：** `experimental_rci_cdb_joint_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        f"- `keep_rows`: `{params['keep_rows']}`",
        "",
        "## 总结",
        "",
        f"- 检查相邻素数记录数：`{summary['prime_count']}`。",
        f"- 紧行全局最小 RCI margin：`{summary['global_min_rci_margin']}`。",
        f"- 紧行最大列见证半径：`{summary['global_max_column_radius_on_tight_rows']}`。",
        f"- 紧行最大尾标签负载：`{summary['global_max_tail_label_load_on_tight_rows']}`。",
        f"- 紧行最大位移余类负载：`{summary['global_max_displacement_residue_load_on_tight_rows']}`。",
        "",
        "## 最小 RCI margin 行",
        "",
        "| p | q | row | margin | no-tail | multi-excess | col-radius | tail-load | disp-load |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in summary["worst_margin_rows"]:
        lines.append(
            "| {p} | {q} | {row} | {margin} | {no_tail} | {multi} | {radius} | {tail} | {disp} |".format(
                p=item["p"],
                q=item["q"],
                row=item["row"],
                margin=item["rci_margin"],
                no_tail=item["no_tail_reserve"],
                multi=item["multi_tail_excess"],
                radius=item["max_column_witness_radius"],
                tail=item["max_tail_label_load"],
                disp=item["max_displacement_residue_load"],
            )
        )

    lines.extend(
        [
            "",
            "## 最大列见证半径紧行",
            "",
            "| p | q | row | margin | col-radius | multi-excess | tail-load | disp-load |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in summary["worst_radius_rows"]:
        lines.append(
            "| {p} | {q} | {row} | {margin} | {radius} | {multi} | {tail} | {disp} |".format(
                p=item["p"],
                q=item["q"],
                row=item["row"],
                margin=item["rci_margin"],
                radius=item["max_column_witness_radius"],
                multi=item["multi_tail_excess"],
                tail=item["max_tail_label_load"],
                disp=item["max_displacement_residue_load"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "该审计把 `RCI` 的横向账本与 `CDB` 的纵向列见证位移放在同一行记录中。若某行 `RCI` margin 很小，同时列见证半径或尾标签负载很大，则说明 `RCI/PDEC` 与 `CDB/PDEC` 的异常出口是同一结构的两个投影。",
            "",
            "样本中 `RCI` margin 仍为正，因此没有反例；但最紧行的尾标签负载和位移余类负载可作为下一步证明 `CDB-1/CDB-2` 的参数依据。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--keep-rows", type=int, default=5)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-rci-cdb-joint-audit",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.y_ratio, args.keep_rows)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key
        not in {"worst_margin_rows", "worst_radius_rows", "worst_tail_load_rows"}
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
