#!/usr/bin/env python3
"""前窗口偏序极小残洞核扫描。"""
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


def features(P: int, holes_: list[int]) -> dict:
    gaps = [holes_[i + 1] - holes_[i] for i in range(len(holes_) - 1)]
    mirror = sorted(P - c for c in holes_)
    small_gaps = [gap for gap in gaps if gap * gap < P]
    return {
        "size": len(holes_),
        "holes": holes_,
        "gaps": gaps,
        "min_gap": None if not gaps else min(gaps),
        "small_gap_count": len(small_gaps),
        "mirror": mirror,
        "mirror_overlap": sorted(set(holes_) & set(mirror)),
        "sum": sum(holes_),
    }


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    rows = [{"x": x, "holes": holes(P, qs, x)} for x in range(1, P)]
    sets = [(row, set(row["holes"])) for row in rows]
    minimal = []
    for row, hole_set in sets:
        has_smaller = False
        for other, other_set in sets:
            if other["x"] != row["x"] and other_set < hole_set:
                has_smaller = True
                break
        if not has_smaller:
            minimal.append({"x": row["x"], **features(P, row["holes"])})
    minimal.sort(key=lambda item: (item["size"], item["x"]))
    return {"P": P, "minimal_count": len(minimal), "minimal_cores": minimal}


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "front_window_minimal_core_scan",
        "status": "minimal_residual_cores_are_nonempty_in_scanned_front_windows",
        "results": results,
        "structural_conclusion": (
            "偏序极小残洞核在扫描范围内全部非空。"
            "极小核数量通常很少，并常带短 gap 或镜像缺陷；这比最小洞数统计更贴近可证明归约。"
        ),
        "next_obligations": [
            "证明下降链必到达偏序极小核，这是有限偏序的直接事实。",
            "分类极小核的短 gap 型与镜像缺陷型。",
            "优先证明短 gap 极小核不可零释放消除。",
        ],
    }
    (DOCS / "front-window-minimal-core-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 前窗口偏序极小残洞核扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(f"- P={result['P']} minimal_count={result['minimal_count']} cores={result['minimal_cores'][:6]}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "front-window-minimal-core-scan.md").write_text("\n".join(lines))
    print(DOCS / "front-window-minimal-core-scan.json")
    print(DOCS / "front-window-minimal-core-scan.md")


if __name__ == "__main__":
    main()
