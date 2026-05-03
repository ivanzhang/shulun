#!/usr/bin/env python3
"""边界残洞迁移审计。

用法示例：
  python3 experiments/prime_matrix_boundary_residual_migration_audit.py

给定前窗口最薄行 x0 的残洞 H(x0)，枚举所有 y<P：
- 若 y 覆盖 H(x0)，检查 y 是否产生新的残洞；
- 若存在 y<P 覆盖 H(x0) 且无新洞，则 BPN 失败；
- 实验中 y<P 可局部补洞，但总会迁移出新洞。

注意：该审计是证据，不是证明。它用于校正 BPN-RM 的精确定义。
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def holes_at_x(p: int, primes: list[int], x: int) -> list[int]:
    """列出相位 x 的未覆盖列。"""
    holes = []
    for col in range(1, p):
        value = x * p + col
        if not any(value % prime == 0 for prime in primes):
            holes.append(col)
    return holes


def covering_factors(p: int, primes: list[int], x: int, col: int) -> list[int]:
    """列出相位 x 覆盖列 col 的根基素数。"""
    value = x * p + col
    return [prime for prime in primes if value % prime == 0]


def best_front_rows(p: int, primes: list[int]) -> tuple[int, list[dict]]:
    """找前窗口中残洞最少的行。"""
    best_size = p
    rows: list[dict] = []
    for x in range(1, p):
        holes = holes_at_x(p, primes, x)
        if len(holes) < best_size:
            best_size = len(holes)
            rows = [{"x": x, "holes": holes}]
        elif len(holes) == best_size and len(rows) < 8:
            rows.append({"x": x, "holes": holes})
    return best_size, rows


def migration_report_for_row(p: int, primes: list[int], row: dict) -> dict:
    """分析某个最薄行的残洞迁移。"""
    old_holes = set(row["holes"])
    patches = []
    full_patch = None
    for y in range(1, p):
        y_holes = set(holes_at_x(p, primes, y))
        if old_holes & y_holes:
            continue
        new_holes = sorted(y_holes - old_holes)
        patch = {
            "y": y,
            "new_holes": new_holes,
            "new_hole_count": len(new_holes),
            "old_hole_witnesses": {
                str(col): covering_factors(p, primes, y, col)
                for col in sorted(old_holes)
            },
        }
        patches.append(patch)
        if not y_holes:
            full_patch = patch
    patches.sort(key=lambda item: (item["new_hole_count"], item["y"]))
    return {
        "x0": row["x"],
        "old_holes": sorted(old_holes),
        "patch_count_y_lt_p": len(patches),
        "min_new_hole_count": None if not patches else patches[0]["new_hole_count"],
        "best_patches": patches[:8],
        "full_patch_y_lt_p": full_patch,
    }


def audit_prime(p: int) -> dict:
    """审计单个素数 P。"""
    primes = primes_upto(p - 1)
    best_size, rows = best_front_rows(p, primes)
    reports = [migration_report_for_row(p, primes, row) for row in rows]
    return {
        "p": p,
        "front_min_holes": best_size,
        "best_row_reports": reports,
        "rm_holds_for_best_rows": all(
            report["full_patch_y_lt_p"] is None for report in reports
        ),
        "min_release_seen": min(
            report["min_new_hole_count"]
            for report in reports
            if report["min_new_hole_count"] is not None
        ),
    }


def run_audit(max_p: int = 199) -> dict:
    """运行审计。"""
    p_values = [prime for prime in primes_upto(max_p) if prime >= 13]
    results = [audit_prime(p) for p in p_values]
    return {
        "certificate_type": "prime_matrix_boundary_residual_migration_audit",
        "status": "local_hole_patching_migrates_residual_holes_in_scanned_best_rows",
        "max_p": max_p,
        "results": results,
        "summary": {
            "checked_prime_count": len(results),
            "failures": [
                item for item in results if not item["rm_holds_for_best_rows"]
            ],
            "global_min_release_seen": min(item["min_release_seen"] for item in results),
        },
        "structural_conclusion": (
            "对扫描内前窗口最薄行，存在许多 y<P 可补掉旧残洞；"
            "但每次都会迁移出至少一个新残洞，未出现 y<P 完整覆盖。"
            "这支持将 BPN-RM 精确定义为残洞集合迁移，而不是高素数单调补洞。"
        ),
        "proof_boundary": (
            "该审计只覆盖最薄行且依赖有限扫描。它不能证明所有 P、所有 x 的 BPN-RM。"
        ),
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# 边界残洞迁移审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        audit["proof_boundary"],
        "",
        "## 总表",
        "",
        "| P | front min holes | min release | RM holds for best rows? | sample best row reports |",
        "| ---: | ---: | ---: | --- | --- |",
    ]
    for item in audit["results"]:
        sample = []
        for report in item["best_row_reports"][:2]:
            sample.append(
                {
                    "x0": report["x0"],
                    "old_holes": report["old_holes"],
                    "patch_count": report["patch_count_y_lt_p"],
                    "min_new_holes": report["min_new_hole_count"],
                    "best_patches": [
                        {
                            "y": patch["y"],
                            "new_holes": patch["new_holes"],
                            "old_hole_witnesses": patch["old_hole_witnesses"],
                        }
                        for patch in report["best_patches"][:3]
                    ],
                }
            )
        lines.append(
            "| {p} | {min_holes} | {release} | {holds} | `{sample}` |".format(
                p=item["p"],
                min_holes=item["front_min_holes"],
                release=item["min_release_seen"],
                holds=item["rm_holds_for_best_rows"],
                sample=sample,
            )
        )
    lines.extend(
        [
            "",
            "## 解释",
            "",
            "若固定最薄行 `x0` 的残洞 `H(x0)`，局部补洞只要求某个新相位 `y` 覆盖 `H(x0)`。实验显示这种 `y<P` 常常存在，说明“高素数不能局部补洞”是错误说法。",
            "",
            "正确说法是：这些 `y<P` 覆盖旧洞时，会把残洞迁移到其它列；若某个 `y<P` 覆盖旧洞且没有新洞，就已经是边界零行，等价于 BPN 失败。",
            "",
            "因此 BPN-RM 必须表述为全局残洞迁移守恒，而不是单调容量不足。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-boundary-residual-migration-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
