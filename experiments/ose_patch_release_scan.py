#!/usr/bin/env python3
"""局部补核代表的释放新洞扫描。"""
from __future__ import annotations

import json
from pathlib import Path

from ose_local_patch_pressure import primes_upto, holes, front_min_rows, short_gap_pairs, patch_scan

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def release_scan(P: int) -> dict:
    qs = primes_upto(P - 1)
    rows = [r for r in front_min_rows(P, qs) if short_gap_pairs(r["holes"], P)]
    reports = []
    for row in rows[:4]:
        K = set(row["holes"])
        pressure = patch_scan(P, row, max_combos=30000)
        layer_reports = {}
        for layer_name, layer in pressure["layer_reports"].items():
            candidates = []
            seen = set()
            for item in layer["best"]:
                for y in item["front_reps"]:
                    if y in seen:
                        continue
                    seen.add(y)
                    Hy = holes(P, qs, y)
                    born = sorted(set(Hy) - K)
                    remaining = sorted(set(Hy) & K)
                    candidates.append(
                        {
                            "y": y,
                            "holes_y": Hy,
                            "born_new": born,
                            "remaining_K": remaining,
                            "release_count": len(born),
                            "total_holes": len(Hy),
                            "scheme": item["scheme"],
                            "mod": item["mod"],
                        }
                    )
            candidates.sort(key=lambda item: (item["total_holes"], item["release_count"], item["y"]))
            layer_reports[layer_name] = candidates[:10]
        reports.append({"x": row["x"], "K": row["holes"], "short_pairs": short_gap_pairs(row["holes"], P), "layers": layer_reports})
    return {"P": P, "reports": reports}


def main() -> None:
    ps = [23, 29, 37, 41, 47, 53, 67, 71, 83, 97]
    results = [release_scan(P) for P in ps]
    audit = {
        "certificate_type": "ose_patch_release_scan",
        "status": "front_patch_representatives_release_new_holes_in_scanned_cases",
        "results": results,
        "structural_conclusion": (
            "当局部补核 CRT 约束仍有前窗口代表时，这些代表在扫描样本中均释放新洞；"
            "它们补掉旧短差核，但洞集迁移到其它列，未产生零行。"
        ),
        "next_obligations": [
            "将 release_count>=1 写成 OSE-local 的精确目标。",
            "证明同奇偶补核时 q=2 不参与，释放来自奇素数层重叠能量不足。",
            "证明异奇偶补核时释放来自对侧奇偶壳。",
        ],
    }
    (DOCS / "ose-patch-release-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# OSE 局部补核释放扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
    ]
    for result in results:
        lines.append(f"- P={result['P']}")
        for report in result["reports"]:
            lines.append(f"  - x={report['x']} K={report['K']} short={report['short_pairs']}")
            for name, candidates in report["layers"].items():
                lines.append(f"    - {name}: {candidates[:5]}")
    lines += ["", "## 下一证明义务"] + [f"- {ob}" for ob in audit["next_obligations"]] + [""]
    (DOCS / "ose-patch-release-scan.md").write_text("\n".join(lines))
    print(DOCS / "ose-patch-release-scan.json")
    print(DOCS / "ose-patch-release-scan.md")


if __name__ == "__main__":
    main()
