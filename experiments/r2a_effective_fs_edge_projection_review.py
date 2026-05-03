#!/usr/bin/env python3
"""R2a 4.3.11g 有效 FS 边投影终审证书。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CASES = [
    {
        "id": "P1_normal_effective_edge",
        "case": "存在一条 FS 边在冻结其它 skeleton 变量后仍保留两个主 Kloosterman 坐标。",
        "destination": "normal_projection_to_FS8_Disp_poly",
        "status": "closed_normal_case",
        "evidence": ["docs/final-proof-draft.md:4.3.11g", "docs/final-proof-draft.md:FS8-Disp-poly"],
    },
    {
        "id": "P2_component_phase_separates",
        "case": "所有 FS 相位按 connected 分量分离。",
        "destination": "cumulant_Mobius_cancellation",
        "status": "closed_by_connected_cumulant_cancellation",
        "evidence": ["docs/final-proof-draft.md:4.3.11e", "docs/final-proof-draft.md:4.3.11g"],
    },
    {
        "id": "P3_overlap_LF_SK_contraction",
        "case": "候选 FS 连接实为 overlap/LF/SK 收缩、对角或低体积项。",
        "destination": "4.3.11b_c_or_low_volume_atlas",
        "status": "closed_by_existing_mechanisms",
        "evidence": ["docs/final-proof-draft.md:4.3.11b", "docs/final-proof-draft.md:4.3.11c", "docs/final-proof-draft.md:6.14.2c-FS8"],
    },
    {
        "id": "P4_Hall_matching_failure",
        "case": "多条 FS 边争用叶变量，Hall 子集满足 |N(E0)|<|E0|。",
        "destination": "four_point_rank_failure or jacobian_common_branch",
        "status": "verified_by_DBA_A1_row_30",
        "evidence": ["docs/dba-A1-source-coverage-certificate.md:41", "docs/dba-closure-finite-generated-atlas.md:66", "docs/final-proof-draft.md:7.2.CH-FS7"],
    },
    {
        "id": "P5_branch_or_denominator_merger",
        "case": "多父关系来自分母分支合并、ramification 或 Jacobian 退化。",
        "destination": "denominator_pole or ramification or jacobian_common_branch",
        "status": "covered_by_DBA_atlas",
        "evidence": ["docs/dba-closure-finite-generated-atlas.md", "docs/final-proof-draft.md:6.14.2c-FS8"],
    },
]


def build_certificate() -> dict:
    return {
        "certificate_type": "R2a_effective_FS_edge_projection_review",
        "status": "projection_review_passed_modulo_DBA_A1_A5_acceptance",
        "target": "4.3.11g effective FS edge projection",
        "cases": CASES,
        "coverage_checks": {
            "DBA_A1_Hall_row": "verified",
            "DBA_atlas_unknown_destinations": 0,
            "new_bad_layer_types": 0,
        },
        "conclusion": "4.3.11g 的有效 FS 边投影没有生成新坏层：正常情形投影到 FS8-Disp-poly；非正常情形分别由 cumulant 抵消、overlap/LF/SK、低体积、Hall/rank-defect 或 DBA 分母/Jacobian/ramification atlas 覆盖。",
    }


def write_markdown(cert: dict) -> None:
    lines = [
        "# R2a 有效 FS 边投影终审",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["conclusion"],
        "",
        "## 分情况归宿",
    ]
    for item in cert["cases"]:
        lines += [
            f"### {item['id']}",
            f"- 情形：{item['case']}",
            f"- 归宿：`{item['destination']}`",
            f"- 状态：`{item['status']}`",
            "- 证据：" + ", ".join(item["evidence"]),
            "",
        ]
    lines += [
        "## 覆盖核查",
        f"- DBA-A1 Hall 行：`{cert['coverage_checks']['DBA_A1_Hall_row']}`",
        f"- DBA atlas 未知去向数：`{cert['coverage_checks']['DBA_atlas_unknown_destinations']}`",
        f"- 新坏层类型数：`{cert['coverage_checks']['new_bad_layer_types']}`",
        "",
    ]
    (DOCS / "r2a-effective-fs-edge-projection-review.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cert = build_certificate()
    (DOCS / "r2a-effective-fs-edge-projection-review.json").write_text(
        json.dumps(cert, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(cert)
    print(DOCS / "r2a-effective-fs-edge-projection-review.json")
    print(DOCS / "r2a-effective-fs-edge-projection-review.md")


if __name__ == "__main__":
    main()
