#!/usr/bin/env python3
"""行列双缺陷场扫描。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for value in range(2, int(n**0.5) + 1):
        if sieve[value]:
            sieve[value * value : n + 1 : value] = [False] * (((n - value * value) // value) + 1)
    return [value for value, keep in enumerate(sieve) if keep]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def root_holes(P: int, qs: list[int], x: int) -> set[int]:
    return {c for c in range(1, P) if all((x * P + c) % q for q in qs)}


def prime_positions(P: int) -> set[tuple[int, int]]:
    out = set()
    for r in range(1, P + 1):
        for c in range(1, P + 1):
            n = (r - 1) * P + c
            if is_prime(n):
                out.add((r, c))
    return out


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    primes = prime_positions(P)
    row_prime_counts = {r: sum((r, c) in primes for c in range(1, P + 1)) for r in range(1, P + 1)}
    col_prime_counts = {c: sum((r, c) in primes for r in range(1, P + 1)) for c in range(1, P + 1)}
    row_holes = {x + 1: sorted(root_holes(P, qs, x)) for x in range(0, P)}
    row_hole_counts = {r: len(h) for r, h in row_holes.items()}
    col_hole_counts = {c: sum(c in hs for hs in row_holes.values()) for c in range(1, P)}
    zero_prime_rows = [r for r, count in row_prime_counts.items() if count == 0]
    zero_prime_cols = [c for c, count in col_prime_counts.items() if count == 0 and c != P]
    min_row_prime = min(row_prime_counts.values())
    min_col_prime_exclP = min(col_prime_counts[c] for c in range(1, P))
    return {
        "P": P,
        "row_prime_counts": row_prime_counts,
        "col_prime_counts": col_prime_counts,
        "row_hole_counts": row_hole_counts,
        "col_hole_counts_exclP": col_hole_counts,
        "zero_prime_rows": zero_prime_rows,
        "zero_prime_cols_exclP": zero_prime_cols,
        "min_row_prime": min_row_prime,
        "min_col_prime_exclP": min_col_prime_exclP,
        "min_row_hole": min(row_hole_counts.values()),
        "min_col_hole_exclP": min(col_hole_counts.values()),
        "row_holes_sample": {r: h for r, h in row_holes.items() if len(h) == min(row_hole_counts.values())},
    }


def main() -> None:
    ps = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "row_column_dual_field_scan",
        "status": "row_and_column_defects_are_dual_marginals_of_the_same_prime_position_field",
        "results": results,
        "structural_conclusion": (
            "行命题与列命题可视为同一个 P×P 素数位置场的两个边际缺陷。"
            "行残洞场 H_P(x) 给出类素数候选；列计数是这些候选在列方向的投影。"
            "统一证明应控制二维缺陷流，而不只是一维行转移。"
        ),
        "next_obligations": [
            "定义二维缺陷矩阵 Z_{r,c}=1_{(r,c) 为类素数/素数候选}。",
            "把行反例和列反例写成 Z 的零边际。",
            "将 Barrier 的列支撑接入二维边际守恒。",
        ],
    }
    (DOCS / "row-column-dual-field-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 行列双缺陷场扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for r in results:
        lines.append(
            f"- P={r['P']} min_row_prime={r['min_row_prime']} min_col_prime_exclP={r['min_col_prime_exclP']} "
            f"zero_rows={r['zero_prime_rows']} zero_cols={r['zero_prime_cols_exclP']} "
            f"min_row_hole={r['min_row_hole']} min_col_hole={r['min_col_hole_exclP']} sample={r['row_holes_sample']}"
        )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "row-column-dual-field-scan.md").write_text("\n".join(lines))
    print(DOCS / "row-column-dual-field-scan.json")
    print(DOCS / "row-column-dual-field-scan.md")


if __name__ == "__main__":
    main()
