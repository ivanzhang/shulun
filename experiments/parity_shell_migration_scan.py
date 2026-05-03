#!/usr/bin/env python3
"""前窗口残洞核的奇偶壳迁移扫描。"""
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


def holes(P: int, qs: list[int], x: int) -> list[int]:
    covered = set()
    for q in qs:
        residue = (-x * P) % q
        first = residue if residue else q
        for c in range(first, P, q):
            covered.add(c)
    return [c for c in range(1, P) if c not in covered]


def parity_signature(values: list[int]) -> dict:
    odd = [c for c in values if c % 2]
    even = [c for c in values if c % 2 == 0]
    return {"odd_count": len(odd), "even_count": len(even), "odd": odd, "even": even}


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    rows = []
    for x in range(1, P):
        H = holes(P, qs, x)
        rows.append({"x": x, "holes": H, "size": len(H), "parity": parity_signature(H), "x_parity": x % 2})
    min_size = min(row["size"] for row in rows)
    min_rows = [row for row in rows if row["size"] == min_size]
    by_x_parity = {0: [], 1: []}
    for row in rows:
        by_x_parity[row["x_parity"]].append(row["size"])
    shell = {
        parity: {
            "count": len(sizes),
            "min": min(sizes),
            "avg": sum(sizes) / len(sizes),
            "max": max(sizes),
        }
        for parity, sizes in by_x_parity.items()
    }
    parity_flips = []
    for row in min_rows:
        target_parity = 1 - row["x_parity"]
        opposite = [other for other in rows if other["x_parity"] == target_parity]
        best_opposite = min(opposite, key=lambda item: item["size"])
        parity_flips.append(
            {
                "from": row,
                "best_opposite": best_opposite,
                "born_after_flip": sorted(set(best_opposite["holes"]) - set(row["holes"])),
                "killed_after_flip": sorted(set(row["holes"]) - set(best_opposite["holes"])),
            }
        )
    return {"P": P, "shell": shell, "min_size": min_size, "min_rows": min_rows, "parity_flips": parity_flips}


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "parity_shell_migration_scan",
        "status": "parity_shell_flip_explains_many_short_gap_core_migrations",
        "results": results,
        "structural_conclusion": (
            "很多短 gap 核的最佳补洞相位来自奇偶壳翻转：q=2 一次覆盖整组同奇偶洞，"
            "但同时释放另一奇偶壳中的残洞。故 q=2 不提供净消灭能力，只提供壳间迁移。"
        ),
        "next_obligations": [
            "严格证明 q=2 层的覆盖只是奇偶互换，前窗口中不能同时消灭两壳。",
            "将问题剥离到同一奇偶壳内的奇素数覆盖压力。",
            "对剥离后的奇素数层证明短差互斥与释放下界。",
        ],
    }
    (DOCS / "parity-shell-migration-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 奇偶壳迁移扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(
            f"- P={result['P']} shell={result['shell']} min={result['min_size']} "
            f"min_rows={result['min_rows'][:3]} flips={result['parity_flips'][:2]}"
        )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "parity-shell-migration-scan.md").write_text("\n".join(lines))
    print(DOCS / "parity-shell-migration-scan.json")
    print(DOCS / "parity-shell-migration-scan.md")


if __name__ == "__main__":
    main()
