#!/usr/bin/env python3
"""R2 FS8-polymer 短块 cumulant 审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

MECHANISMS = [
    {
        "id": "M1_overlap_diagonal",
        "claim": "overlapping short blocks contract to a connected super-block and lose a free start coordinate",
        "evidence": ["final-proof-draft.md:4.3.11", "final-proof-draft.md:4.3.11b"],
        "status": "closed_by_combinatorial_count",
    },
    {
        "id": "M2_LF_large_factor",
        "claim": "non-overlapping blocks cannot share a >sqrt(P) factor inside the row window; LF edges reduce to overlap/diagonal",
        "evidence": ["final-proof-draft.md:4.3.11", "large-factor mutual exclusion lemma in prior sections"],
        "status": "closed_modulo_existing_large_factor_mutex",
    },
    {
        "id": "M3_SK_small_sieve",
        "claim": "small-sieve admissibility is conditioned into the candidate skeleton; incompatible CRT patterns have zero count",
        "evidence": ["final-proof-draft.md:4.3.11", "final-proof-draft.md:B.0.3e+"],
        "status": "closed_as_conditioned_weight_not_connected_noise",
    },
    {
        "id": "M4_FS_floor_sum",
        "claim": "FS connected skeletons reduce to FNL-KS with polymer weights; bad layers go to DBA atlas",
        "evidence": [
            "final-proof-draft.md:4.3.11d--f",
            "final-proof-draft.md:6.18.1d-KS-poly",
            "docs/dba-A1-source-coverage-certificate.md",
            "docs/r2-Cpoly-absorption-scan.md",
            "docs/r2a-weighted-fnl-ks-interface-audit.md",
        ],
        "status": "reduced_to_4_3_11d; C_poly_absorption_scanned",
    },
]

REMAINING = [
    {
        "id": "R2a_4_3_11d_weighted_FNL_KS",
        "description": "Prove FNL-KS uniformly for connected skeleton weights W_Gamma with complexity (C8 s)^(C8 s).",
        "current_reduction": "R2a audit splits the task into weight peeling, phase inheritance, and weighted LV/AE transfer. WLV-piece and 4.3.11g projection reviews have passed modulo existing DBA atlas and C_poly ledger acceptance.",
    },
    {
        "id": "R2b_C_poly_numeric_absorption",
        "description": "Choose C_poly and rerun/verify that C_star, B1, B2, B4, KS margins remain positive.",
        "current_reduction": "Parameter scan docs/r2-Cpoly-absorption-scan.md passes for C_poly=0,80,160,240,320,480; this is now a ledger choice, not a core analytic obstruction.",
        "status": "numeric_absorption_passed_for_scanned_values",
    },
]


def main() -> None:
    audit = {
        "certificate_type": "R2_FS8_polymer_cumulant_audit",
        "status": "reduced_to_weighted_FNL_KS; C_poly_absorption_scanned",
        "target": "4.3.11a short-block cumulant bound",
        "mechanisms": MECHANISMS,
        "minimal_remaining": REMAINING,
        "conclusion": "Overlap/LF/SK mechanisms are closed or reduced to existing conditions. C_poly numeric absorption has passed the scanned ledger values. The real remaining work is R2a: prove 4.3.11d uniformly for connected skeleton polymer weights.",
    }
    (DOCS / "r2-fs8-polymer-cumulant-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# R2 FS8-polymer 短块 Cumulant 审计", "", f"**状态：** `{audit['status']}`", "", audit["conclusion"], "", "## 四类机制"]
    for item in MECHANISMS:
        lines += [f"### {item['id']}", f"- 命题：{item['claim']}", f"- 状态：`{item['status']}`", "- 证据：" + ", ".join(item["evidence"]), ""]
    lines += ["## 最小剩余"]
    for item in REMAINING:
        lines += [f"### {item['id']}", f"- 任务：{item['description']}"]
        if "status" in item:
            lines.append(f"- 状态：`{item['status']}`")
        lines += [f"- 当前归约：{item['current_reduction']}", ""]
    (DOCS / "r2-fs8-polymer-cumulant-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "r2-fs8-polymer-cumulant-audit.json")
    print(DOCS / "r2-fs8-polymer-cumulant-audit.md")


if __name__ == "__main__":
    main()
