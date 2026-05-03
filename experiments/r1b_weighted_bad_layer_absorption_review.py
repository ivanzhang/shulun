#!/usr/bin/env python3
"""R1b 带权坏层吸收复核证书。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CASES = [
    {
        "id": "B1_denominator_reciprocity_ramification_jacobian_rank",
        "bad_layers": "分母、CRT/reciprocity、ramification、Jacobian、四点 rank",
        "dominating_weight": "sum_{q in Q_bad} 1/q",
        "budget": "DBA Rankin/divisor + A2 fixed height + A5 B2/KS margins",
        "status": "covered_by_DBA_A1_A2_A5",
    },
    {
        "id": "B2_step_frequency_resonance",
        "bad_layers": "q|h,q|t,q|mU,q|mT,q|m,q|d,q|mdh",
        "dominating_weight": "1/q + 1/T",
        "budget": "A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4 margin",
        "status": "covered_by_A3_A5",
    },
    {
        "id": "B3_layering_endpoint_low_volume",
        "bad_layers": "短弧层化、dyadic 端点、低体积盒、coarea 切片端点",
        "dominating_weight": "1_low log^(C_L+C_KS) P",
        "budget": "A4 low-volume/layering budget + C_star/KS margins",
        "status": "covered_by_A4_A5",
    },
    {
        "id": "B4_multi_skeleton_bad_prime_repetition",
        "bad_layers": "多 skeleton 坏素重复计数",
        "dominating_weight": "Rankin/divisor budget times C_poly label complexity",
        "budget": "rankin_divisor_budget + C_poly absorption scan",
        "status": "covered_by_rankin_Cpoly",
    },
]


def build_certificate() -> dict:
    return {
        "certificate_type": "R1b_weighted_bad_layer_absorption_review",
        "status": "R1b_reduced_to_existing_DBA_A3_A4_A5_budget_acceptance",
        "target": "4.3.10e+ weighted bad-layer absorption",
        "supporting_lemma": "4.3.10f",
        "cases": CASES,
        "conclusion": "4.3.10f 给出坏层 singular factor 的逐点支配：分别由 Rankin/divisor、步长频率、低体积和 C_poly 标签预算控制。因此 R1b 不引入新坏层类型；剩余义务是接受既有 DBA-A3/A4/A5 加权预算在 singular-factor 口径下适用。",
    }


def write_markdown(cert: dict) -> None:
    lines = [
        "# R1b 带权坏层吸收复核",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["conclusion"],
        "",
        "## 分层支配",
    ]
    for item in cert["cases"]:
        lines += [
            f"### {item['id']}",
            f"- 坏层：{item['bad_layers']}",
            f"- 支配权：`{item['dominating_weight']}`",
            f"- 预算：{item['budget']}",
            f"- 状态：`{item['status']}`",
            "",
        ]
    (DOCS / "r1b-weighted-bad-layer-absorption-review.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cert = build_certificate()
    (DOCS / "r1b-weighted-bad-layer-absorption-review.json").write_text(
        json.dumps(cert, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(cert)
    print(DOCS / "r1b-weighted-bad-layer-absorption-review.json")
    print(DOCS / "r1b-weighted-bad-layer-absorption-review.md")


if __name__ == "__main__":
    main()
