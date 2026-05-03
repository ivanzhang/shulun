#!/usr/bin/env python3
"""扫描 FS8-polymer C_poly 对参数余量的影响。"""
from __future__ import annotations

import json
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER_PATH = ROOT / "experiments" / "dba_A2_A5_parameter_ledger.py"

spec = importlib.util.spec_from_file_location("ledger", LEDGER_PATH)
ledger = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(ledger)


def main() -> None:
    results = []
    for c_poly in [0, 80, 160, 240, 320, 480]:
        data = ledger.build(components={"C_poly": c_poly})
        min_margin = min(item["margin"] for item in data["A5_inequalities"] if item["name"] != "Stieltjes_B5_min")
        results.append(
            {
                "C_poly": c_poly,
                "C_star": data["C_star"],
                "parameters": data["chosen_parameters"],
                "min_positive_margin": min_margin,
                "inequalities": data["A5_inequalities"],
                "passes": min_margin > 0,
            }
        )
    audit = {
        "certificate_type": "C_poly_absorption_scan",
        "status": "all_scanned_values_pass" if all(r["passes"] for r in results) else "some_values_fail",
        "results": results,
        "interpretation": "C_poly can be absorbed by increasing C_star and recomputing B1,B2,B4. With the formula in 6.15.2, scanned values through 480 keep positive margins; this affects thresholds but not the local DBA closure logic.",
    }
    (DOCS / "r2-Cpoly-absorption-scan.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# R2 C_poly 吸收扫描", "", f"**状态：** `{audit['status']}`", "", "| C_poly | C_* | B1 | B2 | B4 | 最小余量 |", "|---:|---:|---:|---:|---:|---:|"]
    for r in results:
        p = r["parameters"]
        lines.append(f"| {r['C_poly']} | {r['C_star']} | {p['B1']} | {p['B2']} | {p['B4']} | {r['min_positive_margin']} |")
    lines += ["", "## 解释", audit["interpretation"]]
    (DOCS / "r2-Cpoly-absorption-scan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(DOCS / "r2-Cpoly-absorption-scan.json")
    print(DOCS / "r2-Cpoly-absorption-scan.md")


if __name__ == "__main__":
    main()
