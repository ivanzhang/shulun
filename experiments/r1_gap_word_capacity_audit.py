#!/usr/bin/env python3
"""R1 gap-word 容量缺口审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

INTERFACES = [
    {
        "id": "R1a_normal_FS_average",
        "claim": "正常层 gap-word 加权平均的 FS singular factor 为 1+o(1)，即 (4.3.10d)。",
        "evidence": ["docs/final-proof-draft.md:4.3.10d-R1a", "docs/r1a-normal-fs-average-review.md", "docs/final-proof-draft.md:FS8-Disp", "docs/r2a-weighted-fnl-ks-interface-audit.md"],
        "status": "review_passed_modulo_FS8_Disp_and_existing_DBA_acceptance",
        "remaining": "最终接受 FS8-Disp/FNL-KS/DBA 链条；不再是独立 R1a 缺口。",
    },
    {
        "id": "R1b_weighted_bad_layer_absorption",
        "claim": "坏层满足带权吸收 (4.3.10e+)，即 sum_B N_g S_g^FS=o(sum N_g)。",
        "evidence": ["docs/final-proof-draft.md:4.3.10f", "docs/r1b-weighted-bad-layer-absorption-review.md", "docs/dba-A2-A5-parameter-ledger.md", "docs/dba-A1-source-coverage-certificate.md"],
        "status": "reduced_to_existing_DBA_A3_A4_A5_budget_acceptance",
        "remaining": "最终接受 4.3.10f 的逐类支配与既有 DBA-A3/A4/A5 在 singular-factor 加权口径下的适用性。",
    },
    {
        "id": "R1c_capacity_arithmetic",
        "claim": "若 K_sing<=2，则 alpha_8<=2 Theta_rough^8=0.735733...，得到 gamma>=0.132133...。",
        "evidence": ["docs/final-proof-draft.md:4.3.9g"],
        "status": "closed_numeric_arithmetic",
        "remaining": "无；只需保持 Theta_rough 常数来源可复核。",
    },
]


def build_audit() -> dict:
    return {
        "certificate_type": "R1_gap_word_capacity_audit",
        "status": "R1_interfaces_review_passed_modulo_existing_FS8_DBA_parameter_acceptance",
        "target": "4.3.8e gap-word total capacity gap",
        "interfaces": INTERFACES,
        "minimal_remaining": [
            "R1b：4.3.10f 支配证书已生成，剩既有 DBA-A3/A4/A5 加权预算最终接受",
            "R1a：4.3.10d-R1a 复核证书已生成，剩 FS8-Disp/FNL-KS/DBA 链条最终接受",
            "随后由 K_sing<=2 的数值预算推出 alpha_8<1",
        ],
        "conclusion": "R1 的两个接口均已生成复核证书：R1a 归约到 FS8-Disp/FNL-KS/DBA 链条，R1b 归约到 DBA-A3/A4/A5 与 C_poly 预算接受。当前 R1 不再是独立新硬点；剩余并入既有 FS8/DBA/参数账本最终接受。",
    }


def write_markdown(audit: dict) -> None:
    lines = [
        "# R1 Gap-word 容量缺口审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["conclusion"],
        "",
        "## 接口",
    ]
    for item in audit["interfaces"]:
        lines += [
            f"### {item['id']}",
            f"- 命题：{item['claim']}",
            f"- 状态：`{item['status']}`",
            f"- 剩余：{item['remaining']}",
            "- 证据：" + ", ".join(item["evidence"]),
            "",
        ]
    lines += ["## 最小剩余"]
    for item in audit["minimal_remaining"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "r1-gap-word-capacity-audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    audit = build_audit()
    (DOCS / "r1-gap-word-capacity-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit)
    print(DOCS / "r1-gap-word-capacity-audit.json")
    print(DOCS / "r1-gap-word-capacity-audit.md")


if __name__ == "__main__":
    main()
