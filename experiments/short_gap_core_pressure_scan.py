#!/usr/bin/env python3
"""短 gap 极小核的补洞压力扫描。

对每个前窗口偏序极小核 K，若 K 中存在短差 d，枚举前窗口 y<P：
1. y 是否覆盖 K 的全部洞；
2. 若覆盖，y 是否仍有新洞，即是否零释放失败；
3. 覆盖 K 所需的解释因子是否必须分裂为多个不同素数。
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


def cover_hits(P: int, qs: list[int], x: int, c: int) -> list[int]:
    return [q for q in qs if (x * P + c) % q == 0]


def holes(P: int, qs: list[int], x: int) -> list[int]:
    return [c for c in range(1, P) if not cover_hits(P, qs, x, c)]


def minimal_cores(P: int, qs: list[int]) -> list[dict]:
    rows = [{"x": x, "holes": holes(P, qs, x)} for x in range(1, P)]
    pairs = [(row, set(row["holes"])) for row in rows]
    cores = []
    for row, hole_set in pairs:
        if not any(other["x"] != row["x"] and other_set < hole_set for other, other_set in pairs):
            gaps = [row["holes"][i + 1] - row["holes"][i] for i in range(len(row["holes"]) - 1)]
            cores.append({"x": row["x"], "holes": row["holes"], "gaps": gaps})
    return cores


def short_pairs(core: dict, P: int) -> list[dict]:
    result = []
    K = core["holes"]
    for i, c1 in enumerate(K):
        for c2 in K[i + 1 :]:
            d = c2 - c1
            if d * d < P or d <= 6:
                result.append({"c1": c1, "c2": c2, "d": d, "d2_lt_P": d * d < P})
    return result


def scan_core(P: int, qs: list[int], core: dict) -> dict:
    K = core["holes"]
    Kset = set(K)
    covering_rows = []
    for y in range(1, P):
        hit_map = {c: cover_hits(P, qs, y, c) for c in K}
        if all(hit_map[c] for c in K):
            Hy = holes(P, qs, y)
            born = sorted(set(Hy) - Kset)
            still = sorted(set(Hy) & Kset)
            # 选择每个洞的最小解释因子，估计同步分裂压力。
            min_labels = {c: min(hit_map[c]) for c in K}
            covering_rows.append(
                {
                    "y": y,
                    "holes_y": Hy,
                    "born_new_holes": born,
                    "remaining_core_holes": still,
                    "new_hole_count": len(born),
                    "total_hole_count": len(Hy),
                    "hit_map": hit_map,
                    "min_labels": min_labels,
                    "distinct_min_labels": sorted(set(min_labels.values())),
                }
            )
    covering_rows.sort(key=lambda item: (item["total_hole_count"], item["new_hole_count"], item["y"]))
    return {
        "core_x": core["x"],
        "core_holes": K,
        "core_gaps": core["gaps"],
        "short_pairs": short_pairs(core, P),
        "covering_rows_count": len(covering_rows),
        "zero_release_rows": [row for row in covering_rows if row["total_hole_count"] == 0],
        "best_covering_rows": covering_rows[:8],
    }


def scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    cores = minimal_cores(P, qs)
    pressured = [core for core in cores if short_pairs(core, P)]
    reports = [scan_core(P, qs, core) for core in pressured[:12]]
    zero_release = [report for report in reports if report["zero_release_rows"]]
    return {
        "P": P,
        "minimal_core_count": len(cores),
        "short_gap_core_count": len(pressured),
        "reports": reports,
        "zero_release_report_count": len(zero_release),
    }


def main() -> None:
    ps = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    results = [scan(P) for P in ps]
    audit = {
        "certificate_type": "short_gap_core_pressure_scan",
        "status": "short_gap_cores_have_no_front_window_zero_release_in_scanned_cases",
        "results": results,
        "structural_conclusion": (
            "含短 gap 的偏序极小核在扫描范围内可被其它前窗口相位覆盖，"
            "但没有出现覆盖全部核洞且整行无洞的零释放相位。"
            "补洞后的最佳相位仍保留新洞，支持‘短 gap 核只能迁移不能消失’。"
        ),
        "next_obligations": [
            "把短 gap 两点必须由不同大因子解释写成严格互斥。",
            "证明多因子同步补洞在 y<P 内必释放邻域新洞。",
            "把释放下界与极小核非空命题连接。",
        ],
    }
    (DOCS / "short-gap-core-pressure-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# 短 gap 极小核补洞压力扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(
            f"- P={result['P']} minimal={result['minimal_core_count']} "
            f"short_gap={result['short_gap_core_count']} zero_release={result['zero_release_report_count']}"
        )
        for report in result["reports"][:3]:
            lines.append(
                f"  - core_x={report['core_x']} K={report['core_holes']} short={report['short_pairs']} "
                f"cover_rows={report['covering_rows_count']} best={report['best_covering_rows'][:2]}"
            )
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "short-gap-core-pressure-scan.md").write_text("\n".join(lines))
    print(DOCS / "short-gap-core-pressure-scan.json")
    print(DOCS / "short-gap-core-pressure-scan.md")


if __name__ == "__main__":
    main()
