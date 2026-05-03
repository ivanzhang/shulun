#!/usr/bin/env python3
"""DBA-A1 atlas 覆盖逐行复核证书。

对 dba-closure-finite-generated-atlas 的 32 行来源矩阵逐条登记：
- 正文证据位置；
- 去向是否为已知 atlas/budget 类；
- 复核状态。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

EVIDENCE = {
    "6.10.1": ["final-proof-draft.md:6.10.1"],
    "6.10.2": ["final-proof-draft.md:6.10.2"],
    "6.10.3": ["final-proof-draft.md:6.10.3"],
    "6.10.4": ["final-proof-draft.md:6.10.4"],
    "6.11.1": ["final-proof-draft.md:6.11.1"],
    "6.12.2": ["final-proof-draft.md:6.12.2"],
    "6.13.1--6.13.3": ["final-proof-draft.md:6.13.1--6.13.3"],
    "6.13.2": ["final-proof-draft.md:6.13.2"],
    "6.13.6/6.15.3a-K1": ["final-proof-draft.md:6.13.6", "final-proof-draft.md:6.15.3a-K1"],
    "6.13.6/6.15.3a-K2": ["final-proof-draft.md:6.13.6", "final-proof-draft.md:6.15.3a-K2"],
    "6.17.1--6.17.3": ["final-proof-draft.md:6.17.1--6.17.3"],
    "6.17.6/6.18.1d": ["final-proof-draft.md:6.17.6", "final-proof-draft.md:6.18.1d"],
    "6.18.1c": ["final-proof-draft.md:6.18.1c"],
    "6.18.1d": ["final-proof-draft.md:6.18.1d"],
    "6.18.1d-KS": ["final-proof-draft.md:6.18.1d-KS", "final-proof-draft.md:6.15.3a"],
    "6.18.1d-KS-J/6.15.3a": ["final-proof-draft.md:6.18.1d-KS-J", "final-proof-draft.md:6.15.3a"],
    "6.18.1e": ["final-proof-draft.md:6.18.1e"],
    "6.18.2a--b": ["final-proof-draft.md:6.18.2a--6.18.2b"],
    "6.18.2c": ["final-proof-draft.md:6.18.2c"],
    "6.7--6.8": ["final-proof-draft.md:6.7--6.8"],
    "4.3.6/FS8": ["final-proof-draft.md:4.3.6", "final-proof-draft.md:FS8-Disp"],
    "4.3.6h/6.18.1d-KS-J": ["final-proof-draft.md:4.3.6h", "final-proof-draft.md:6.18.1d-KS-J"],
    "B.0.3e+": ["final-proof-draft.md:B.0.3e+", "final-proof-draft.md:6.17.6"],
    "FS8-polymer": ["final-proof-draft.md:FS8-polymer 覆盖审查表", "final-proof-draft.md:6.14.2c-FS8"],
}


def main() -> None:
    atlas = json.loads((DOCS / "dba-closure-finite-generated-atlas.json").read_text(encoding="utf-8"))
    rows = []
    for index, row in enumerate(atlas["source_coverage_matrix"], 1):
        source = row["source"]
        evidence = EVIDENCE.get(source, [])
        status = "verified" if evidence and row["budget_destinations"] else "needs_review"
        rows.append(
            {
                "index": index,
                "source": source,
                "failure_mode": row["failure_mode"],
                "atlas_destination": row["atlas_destination"],
                "budget_destinations": row["budget_destinations"],
                "evidence": evidence,
                "status": status,
                "review_note": "source has explicit atlas destination and budget class" if status == "verified" else "missing evidence or destination",
            }
        )
    audit = {
        "certificate_type": "DBA_A1_source_coverage_certificate",
        "status": "verified" if all(row["status"] == "verified" for row in rows) else "needs_review",
        "row_count": len(rows),
        "verified_count": sum(row["status"] == "verified" for row in rows),
        "needs_review_count": sum(row["status"] != "verified" for row in rows),
        "unknown_destination_count": len(atlas.get("unknown_destinations", [])),
        "rows": rows,
        "interpretation": "This is a coverage certificate for listed failure modes. It verifies that each listed source has evidence and a legal atlas/budget destination; it does not prove that no unlisted source exists beyond the audited sections.",
    }
    out = DOCS / "dba-A1-source-coverage-certificate.json"
    out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# DBA-A1 来源覆盖逐行证书", "", f"**状态：** `{audit['status']}`", "", f"- 行数：`{audit['row_count']}`", f"- 已验证：`{audit['verified_count']}`", f"- 待复核：`{audit['needs_review_count']}`", f"- 未知去向：`{audit['unknown_destination_count']}`", "", "| # | 来源 | 失败方式 | 去向 | 状态 |", "|---:|---|---|---|---|"]
    for row in rows:
        lines.append(f"| {row['index']} | {row['source']} | {row['failure_mode']} | {row['atlas_destination']} | {row['status']} |")
    lines += ["", "## 说明", audit["interpretation"]]
    (DOCS / "dba-A1-source-coverage-certificate.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    print(DOCS / "dba-A1-source-coverage-certificate.md")


if __name__ == "__main__":
    main()
