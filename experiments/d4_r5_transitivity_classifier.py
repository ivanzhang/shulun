#!/usr/bin/env python3
"""D4/R5 递归传递 stable/jump 分类器。"""
from __future__ import annotations

import json
from pathlib import Path


def classify_step(prev: dict, cur: dict) -> dict:
    """按 potential/质量变化粗分类 stable 或 jump。"""
    dL = cur["L"] - prev["L"]
    dE2 = cur["E2"] - prev["E2"]
    dD = cur["potential"] - prev["potential"]
    shell_def = dE2 - dL * dL / 20
    # 大幅负 dL 或 potential 大跌视为 jump；否则 stable。
    kind = "jump" if dL < -0.02 or dD < -0.001 else "stable"
    return {
        "from_hi": prev["hi"],
        "to_hi": cur["hi"],
        "kind": kind,
        "dL": dL,
        "dE2": dE2,
        "dD": dD,
        "shell_defect": shell_def,
        "stable_defect_nonnegative": shell_def >= 0 if kind == "stable" else None,
    }


def main() -> int:
    data = json.loads(Path("docs/d4-r5-recursive-peeling-probe.json").read_text())
    rows = []
    totals = {"stable": 0, "jump": 0, "stable_bad": 0}
    for row in data["rows"]:
        steps = []
        for prev, cur in zip(row["stats"], row["stats"][1:]):
            item = classify_step(prev, cur)
            steps.append(item)
            totals[item["kind"]] += 1
            if item["kind"] == "stable" and not item["stable_defect_nonnegative"]:
                totals["stable_bad"] += 1
        rows.append({"x": row["x"], "steps": steps})
    payload = {
        "certificate_type": "D4-R5-recursive-transitivity-classifier",
        "status": "diagnostic classifier for RPL stable/jump split; thresholds are heuristic",
        "rows": rows,
        "totals": totals,
    }
    Path("docs/d4-r5-recursive-transitivity-classification.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(json.dumps({"totals": totals}, ensure_ascii=False, indent=2))
    for row in rows:
        print('x', row['x'])
        for s in row['steps']:
            print(s['from_hi'], '->', s['to_hi'], s['kind'], 'dD', round(s['dD'], 6), 'shell', round(s['shell_defect'], 6))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
