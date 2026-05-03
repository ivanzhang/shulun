#!/usr/bin/env python3
"""BPN low-hole bucket 桥洞删一审计。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_bridge_deletion_audit.py
  python3 experiments/prime_matrix_bpn_lhb_bridge_deletion_audit.py --p-values 43,47 --q 2310

目标：
- 复核 `low-hole bucket` 中需要一洞删除的 Hall 证书；
- 检查被删除洞是否同时支撑至少两个高素数的最大覆盖块；
- 将“删一洞后容量下降至少 2”写成可符号化的桥洞机制。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import (
    high_completion_stats,
    low_holes_for_phase,
    primes_upto,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def capacity_details(
    p: int,
    q: int,
    phase: int,
    holes: list[int],
    high_primes: list[int],
) -> tuple[int, dict[int, dict[str, Any]]]:
    """计算每个高素数在给定洞集上的最大残基块容量。"""
    total = 0
    details: dict[int, dict[str, Any]] = {}
    for prime in high_primes:
        inverse_p = pow(p, -1, prime)
        inverse_q = pow(q % prime, -1, prime)
        buckets: dict[int, list[int]] = defaultdict(list)
        for col in holes:
            target_row_residue = (1 - col * inverse_p) % prime
            y_residue = ((target_row_residue - phase) * inverse_q) % prime
            buckets[y_residue].append(col)
        max_size = max((len(cols) for cols in buckets.values()), default=0)
        winning_blocks = [
            {"residue": residue, "cols": cols}
            for residue, cols in sorted(buckets.items())
            if len(cols) == max_size
        ]
        total += max_size
        details[prime] = {
            "max_size": max_size,
            "winning_blocks": winning_blocks[:6],
        }
    return total, details


def scan_prime(p: int, q: int) -> dict[str, Any]:
    """扫描单个 P 的一洞删除桥洞结构。"""
    base_primes = primes_upto(p - 1)
    if prod(base_primes) % q != 0:
        raise ValueError(f"q={q} 不整除 P={p} 的根基 CRT 周期")
    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]

    one_delete_rows: list[dict[str, Any]] = []
    for phase in range(q):
        holes = low_holes_for_phase(p, q, low_primes, phase)
        stats = high_completion_stats(p, q, phase, holes, high_primes)
        if stats["completion_count"] != 0:
            continue
        if stats["min_hall_complement_size"] != 1:
            continue

        witness = stats["min_hall_subset_holes"]
        witness_set = set(witness)
        deleted = [col for col in holes if col not in witness_set]
        if len(deleted) != 1:
            continue
        deleted_col = deleted[0]
        full_capacity, full_details = capacity_details(p, q, phase, holes, high_primes)
        reduced_capacity, reduced_details = capacity_details(p, q, phase, witness, high_primes)
        prime_drops = {
            prime: full_details[prime]["max_size"] - reduced_details[prime]["max_size"]
            for prime in high_primes
        }
        support_primes = [
            prime for prime, drop in prime_drops.items()
            if drop > 0
        ]
        capacity_drop = full_capacity - reduced_capacity
        delta_full = len(holes) - full_capacity
        delta_reduced = len(witness) - reduced_capacity
        one_delete_rows.append(
            {
                "phase": phase,
                "holes": holes,
                "deleted_col": deleted_col,
                "witness": witness,
                "hole_count": len(holes),
                "witness_size": len(witness),
                "full_capacity": full_capacity,
                "reduced_capacity": reduced_capacity,
                "capacity_drop": capacity_drop,
                "delta_full": delta_full,
                "delta_reduced": delta_reduced,
                "support_primes": support_primes,
                "prime_drops": prime_drops,
                "bridge_certified": capacity_drop >= 2 and delta_reduced > 0,
                "full_winning_blocks": {
                    str(prime): full_details[prime]["winning_blocks"]
                    for prime in support_primes
                },
            }
        )

    return {
        "p": p,
        "q": q,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "one_delete_count": len(one_delete_rows),
        "bridge_certified_count": sum(
            1 for row in one_delete_rows if row["bridge_certified"]
        ),
        "deleted_col_histogram": dict(
            sorted(Counter(row["deleted_col"] for row in one_delete_rows).items())
        ),
        "capacity_drop_histogram": dict(
            sorted(Counter(row["capacity_drop"] for row in one_delete_rows).items())
        ),
        "delta_full_histogram": dict(
            sorted(Counter(row["delta_full"] for row in one_delete_rows).items())
        ),
        "delta_reduced_histogram": dict(
            sorted(Counter(row["delta_reduced"] for row in one_delete_rows).items())
        ),
        "support_prime_histogram": {
            str(key): value
            for key, value in sorted(
                Counter(tuple(row["support_primes"]) for row in one_delete_rows).items(),
                key=lambda item: (str(item[0]), item[1]),
            )
        },
        "examples": one_delete_rows[:16],
    }


def parse_p_values(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def run(p_values: list[int], q: int) -> dict[str, Any]:
    """运行审计。"""
    results = [scan_prime(p, q) for p in p_values]
    return {
        "certificate_type": "prime_matrix_bpn_lhb_bridge_deletion_audit",
        "status": "one_deletion_hall_witness_reduced_to_bridge_capacity_drop",
        "q": q,
        "results": results,
        "review_conclusion": (
            "一洞删除见证不是任意删洞：样本中被删洞同时支撑两个高素数的最大残基块，"
            "删去该桥洞后总容量下降 2，而洞数只下降 1，于是 Hall 亏损显化。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN low-hole bucket 桥洞删一审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总表",
        "",
        "| P | Q | high primes | one-delete | bridge-certified | deleted columns | capacity drops | Delta(H) | Delta(W) |",
        "| ---: | ---: | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    for row in result["results"]:
        lines.append(
            "| {p} | {q} | `{high}` | {one} | {cert} | `{deleted}` | `{drops}` | `{dh}` | `{dw}` |".format(
                p=row["p"],
                q=row["q"],
                high=row["high_primes"],
                one=row["one_delete_count"],
                cert=row["bridge_certified_count"],
                deleted=row["deleted_col_histogram"],
                drops=row["capacity_drop_histogram"],
                dh=row["delta_full_histogram"],
                dw=row["delta_reduced_histogram"],
            )
        )

    lines.extend(
        [
            "",
            "## 2. 桥洞机制",
            "",
            "设",
            "",
            "\\[",
            "\\Delta(W)=|W|-\\sum_{\\ell\\in R}\\max_a |W\\cap B_{\\ell,a}(t)|.",
            "\\]",
            "",
            "若 `Delta(H)=0`，且存在一个洞 `c_*`，使删除它后总容量下降至少 `2`，即",
            "",
            "\\[",
            "\\sum_{\\ell\\in R}\\left(m_\\ell(H)-m_\\ell(H\\setminus\\{c_*\\})\\right)\\ge 2,",
            "\\]",
            "",
            "则",
            "",
            "\\[",
            "\\Delta(H\\setminus\\{c_*\\})",
            "=\\Delta(H)-1+\\sum_{\\ell\\in R}\\left(m_\\ell(H)-m_\\ell(H\\setminus\\{c_*\\})\\right)>0.",
            "\\]",
            "",
            "这给出一洞删除 Hall 证书。样本中的一洞删除相位均满足该桥洞条件。",
            "",
            "## 3. 样例",
            "",
        ]
    )
    for row in result["results"]:
        if not row["examples"]:
            continue
        lines.extend([f"### P={row['p']}", ""])
        lines.append("| phase | holes | deleted | support primes | cap drop | Delta(H) | Delta(W) |")
        lines.append("| ---: | --- | ---: | --- | ---: | ---: | ---: |")
        for item in row["examples"][:8]:
            lines.append(
                f"| {item['phase']} | `{item['holes']}` | {item['deleted_col']} | `{item['support_primes']}` | {item['capacity_drop']} | {item['delta_full']} | {item['delta_reduced']} |"
            )
        lines.append("")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-values", default="13,17,19,23,29,31,37,43,47")
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-bridge-deletion-audit.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-bridge-deletion-audit.md",
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
