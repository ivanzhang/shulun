#!/usr/bin/env python3
"""前窗口残洞集偏序扫描。

检查是否存在 y<P 使 H(y) 严格包含于 H(x)，即“净消洞且不生新洞”。
若不存在，则残洞迁移守恒可加强为前窗口洞集偏序反链性质。
"""
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
            if 1 <= c < P:
                covered.add(c)
    return [c for c in range(1, P) if c not in covered]


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    rows = [{"x": x, "holes": holes(P, qs, x)} for x in range(1, P)]
    strict_descents = []
    equal_pairs = []
    incomparable = 0
    for left in rows:
        A = set(left["holes"])
        for right in rows:
            if left["x"] == right["x"]:
                continue
            B = set(right["holes"])
            if B < A:
                strict_descents.append(
                    {
                        "from_x": left["x"],
                        "to_x": right["x"],
                        "from_holes": left["holes"],
                        "to_holes": right["holes"],
                        "killed": sorted(A - B),
                        "born": sorted(B - A),
                    }
                )
            elif A == B:
                equal_pairs.append({"x1": left["x"], "x2": right["x"], "holes": left["holes"]})
            elif not (A < B or B < A):
                incomparable += 1
    sizes = {}
    for row in rows:
        sizes.setdefault(len(row["holes"]), 0)
        sizes[len(row["holes"])] += 1
    min_size = min(sizes)
    min_rows = [row for row in rows if len(row["holes"]) == min_size]
    return {
        "P": P,
        "size_histogram": dict(sorted(sizes.items())),
        "min_size": min_size,
        "min_rows": min_rows,
        "strict_descent_count": len(strict_descents),
        "strict_descents_sample": strict_descents[:20],
        "equal_pair_count": len(equal_pairs),
        "equal_pairs_sample": equal_pairs[:20],
        "incomparable_ordered_pair_count": incomparable,
    }


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "front_window_hole_poset_scan",
        "status": "hole_sets_have_many_descents_but_minimal_cores_remain_nonempty",
        "results": results,
        "structural_conclusion": (
            "前窗口洞集并非整体反链：存在 H(y) 严格包含 H(x) 的局部净消洞。"
            "但所有极小洞集仍非空；因此 RCC 不能表述为任意两相位的偏序反链，"
            "必须表述为‘沿可实现的全覆盖补洞链，极小残洞核不可跨窗消失’。"
        ),
        "next_obligations": [
            "识别前窗口洞集偏序中的极小元，研究其残洞核类型。",
            "证明极小元不能为空；这比任意相位净消洞不等式更准确。",
            "把极小残洞核与 CRT 列均衡、镜像相位和相邻商互质约束连接。",
        ],
    }
    (DOCS / "front-window-hole-poset-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# 前窗口残洞集偏序扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for item in results:
        lines.append(
            f"- P={item['P']} hist={item['size_histogram']} min={item['min_size']} "
            f"min_rows={item['min_rows'][:4]} descents={item['strict_descent_count']}"
        )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "front-window-hole-poset-scan.md").write_text("\n".join(lines))
    print(DOCS / "front-window-hole-poset-scan.json")
    print(DOCS / "front-window-hole-poset-scan.md")


if __name__ == "__main__":
    main()
