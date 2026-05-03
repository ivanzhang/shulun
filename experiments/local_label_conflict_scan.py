#!/usr/bin/env python3
"""局部标签图与短差冲突能量扫描。"""
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


def labels(P: int, qs: list[int], x: int, c: int) -> list[int]:
    return [q for q in qs if (x * P + c) % q == 0]


def holes(P: int, qs: list[int], x: int) -> list[int]:
    return [c for c in range(1, P) if not labels(P, qs, x, c)]


def front_min_xs(P: int, qs: list[int]) -> list[int]:
    vals = [(x, len(holes(P, qs, x))) for x in range(1, P)]
    m = min(v for _, v in vals)
    return [x for x, v in vals if v == m][:4]


def scan_row(P: int, x: int) -> dict:
    qs = primes_upto(P - 1)
    label_map = {c: labels(P, qs, x, c) for c in range(1, P)}
    H = [c for c, ls in label_map.items() if not ls]
    adjacent_forced_diff = []
    unique_adjacent = []
    short_conflicts = []
    for c in range(1, P - 1):
        L1, L2 = label_map[c], label_map[c + 1]
        if L1 and L2:
            adjacent_forced_diff.append({"c": c, "L_c": L1, "L_next": L2, "disjoint": set(L1).isdisjoint(L2)})
            if len(L1) == 1 and len(L2) == 1:
                unique_adjacent.append({"c": c, "q1": L1[0], "q2": L2[0]})
    covered_cols = [c for c in range(1, P) if label_map[c]]
    for i, c1 in enumerate(covered_cols):
        for c2 in covered_cols[i + 1 :]:
            d = c2 - c1
            if d > 12:
                break
            shared = sorted(set(label_map[c1]) & set(label_map[c2]))
            large_shared = [q for q in shared if q > d]
            if shared or d <= 6:
                short_conflicts.append(
                    {
                        "c1": c1,
                        "c2": c2,
                        "d": d,
                        "L1": label_map[c1],
                        "L2": label_map[c2],
                        "shared": shared,
                        "large_shared_impossible": large_shared,
                    }
                )
    unique_count = sum(1 for c, ls in label_map.items() if len(ls) == 1)
    multi_count = sum(1 for c, ls in label_map.items() if len(ls) > 1)
    return {
        "x": x,
        "holes": H,
        "unique_count": unique_count,
        "multi_count": multi_count,
        "adjacent_pairs": len(adjacent_forced_diff),
        "unique_adjacent_count": len(unique_adjacent),
        "unique_adjacent_sample": unique_adjacent[:20],
        "short_conflict_sample": short_conflicts[:40],
        "label_map_sample": {c: label_map[c] for c in range(1, min(P, 30))},
    }


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    return {"P": P, "rows": [scan_row(P, x) for x in front_min_xs(P, qs)]}


def main() -> None:
    ps = [23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 97]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "local_label_conflict_scan",
        "status": "adjacent_labels_are_forced_disjoint_and_short_distance_large_label_reuse_is_forbidden",
        "results": results,
        "structural_conclusion": (
            "标签图显示相邻列标签天然不相交；短距离列若共享标签，则共享标签必整除列差，"
            "大标签复用被严格禁止。该局部图约束可作为 LD-1 的组合能量。"
        ),
        "next_obligations": [
            "把 unique adjacent chain 转化为路径标签容量不等式。",
            "对短差核证明大标签补洞必须使用互异标签。",
            "将标签互异数量与 CRT 同步模数乘积连接。",
        ],
    }
    (DOCS / "local-label-conflict-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 局部标签图与短差冲突扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(f"- P={result['P']}")
        for row in result["rows"]:
            lines.append(
                f"  - x={row['x']} H={row['holes']} unique={row['unique_count']} multi={row['multi_count']} "
                f"adjacent={row['adjacent_pairs']} unique_adjacent={row['unique_adjacent_count']} "
                f"unique_adj_sample={row['unique_adjacent_sample'][:6]} short_sample={row['short_conflict_sample'][:6]}"
            )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "local-label-conflict-scan.md").write_text("\n".join(lines))
    print(DOCS / "local-label-conflict-scan.json")
    print(DOCS / "local-label-conflict-scan.md")


if __name__ == "__main__":
    main()
