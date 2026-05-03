#!/usr/bin/env python3
"""D4/R5 审稿级证书一致性审计。"""
from __future__ import annotations

import json
from pathlib import Path

CHECKS = [
    ("H80 layer integer checks", "docs/d4-r5-light-H80-layer-functional-certificate.json", lambda d: d["all_checks_ok"]),
    ("H80 unified candidate table", "docs/d4-r5-H80-unified-candidate-boxes.json", lambda d: d["integer_candidate_checks_ok"] and d["contract_root_ledgers_ok"] and d["total_unresolved_open_interval_count"] == 0),
    ("H80 membership cells", "docs/d4-r5-H80-membership-cell-decomposition.json", lambda d: d["total_rows"] == 17 and d["total_runs"] == 17),
    ("H80 one-sided all17", "docs/d4-r5-H80-one-sided-fixed-membership-all17-batch.json", lambda d: d["all_ok"] and d["total_root_boxes"] == 0 and d["total_unresolved"] == 0),
    ("Decimal worst audit", "docs/d4-r5-decimal-audit-by-functional-worst.json", lambda d: d["all_certified"] and len(d["rows"]) == 6),
    ("Budget interval audit", "docs/d4-r5-budget-interval-audit-by-functional-worst.json", lambda d: d["all_certified"] and len(d["rows"]) == 6),
    ("Outward interval audit", "docs/d4-r5-outward-interval-audit-by-functional-worst.json", lambda d: d["all_certified"] and len(d["rows"]) == 6),
]


def main() -> int:
    rows = []
    for name, path, predicate in CHECKS:
        p = Path(path)
        if not p.exists():
            rows.append({"name": name, "path": path, "exists": False, "ok": False, "summary": "missing"})
            continue
        data = json.loads(p.read_text())
        ok = bool(predicate(data))
        summary = {k: data[k] for k in data.keys() if k in {
            "all_checks_ok", "integer_candidate_checks_ok", "contract_root_ledgers_ok",
            "total_unresolved_open_interval_count", "total_rows", "total_runs", "all_ok",
            "total_root_boxes", "total_unresolved", "all_certified", "precision"
        }}
        rows.append({"name": name, "path": path, "exists": True, "ok": ok, "summary": summary})
    outward = json.loads(Path("docs/d4-r5-outward-interval-audit-by-functional-worst.json").read_text())
    min_row = min(outward["rows"], key=lambda row: float(row["signed_margin"]))
    payload = {
        "certificate_type": "D4-R5-review-grade-consistency-audit",
        "checks": rows,
        "all_ok": all(row["ok"] for row in rows),
        "min_outward_margin": min_row["signed_margin"],
        "min_outward_margin_functional": min_row["functional"],
        "min_outward_margin_certificate": min_row["outward_certificate"],
        "scope": "H80 R5 resource-lock candidate closure only; does not prove the full prime-in-every-row/column theorem.",
        "remaining_for_full_theorem": [
            "extend the same certificate pipeline from H80 resource-lock units to all R5global1--R5global4 candidate cells",
            "connect R5global closure back into all earlier USC/DBA/JND/column theorem dependencies",
            "extract final global threshold and run finite verification below it",
        ],
    }
    Path("docs/d4-r5-review-grade-consistency-audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in payload.items() if k != "checks"}, ensure_ascii=False, indent=2))
    for row in rows:
        print(f"{row['ok']} {row['name']} {row['path']}")
    return 0 if payload["all_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
