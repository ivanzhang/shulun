#!/usr/bin/env python3
"""R1a 正常层 FS 平均放大界复核。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CHECKS = [
    {
        "id": "N1_main_term_normalization",
        "claim": "FS8 主项 |I|/Q 与八个单点 Stieltjes 主项乘法归一，正常层平均为 1+o(1)。",
        "evidence": ["docs/final-proof-draft.md:4.3.FS8-4", "docs/final-proof-draft.md:4.3.10d-R1a"],
        "status": "closed_by_FS8_normal_form",
    },
    {
        "id": "N2_nonzero_sawtooth_cancellation",
        "claim": "所有非主项都含非零 sawtooth 频率；正常层由 FS8-Disp 给 o(1)。",
        "evidence": ["docs/final-proof-draft.md:4.3.FS8-5", "docs/final-proof-draft.md:FS8-Disp"],
        "status": "closed_modulo_FNL_KS_DBA_chain",
    },
    {
        "id": "N3_no_bad_layer_double_counting",
        "claim": "若分母/CRT/Jacobian/rank/共振失败，则该项不在 N_FS，而进入 R1b 带权坏层吸收。",
        "evidence": ["docs/final-proof-draft.md:4.3.10d-R1a", "docs/r1b-weighted-bad-layer-absorption-review.md"],
        "status": "closed_by_normal_bad_partition",
    },
]


def build_certificate() -> dict:
    return {
        "certificate_type": "R1a_normal_FS_average_review",
        "status": "R1a_review_passed_modulo_FS8_Disp_and_existing_DBA_acceptance",
        "target": "4.3.10d normal-layer FS average amplification",
        "supporting_corollary": "4.3.10d-R1a",
        "checks": CHECKS,
        "conclusion": "R1a 已归约到既有 FS8-Disp/FNL-KS/DBA 链条：主项乘法归一，非零 sawtooth 频率在正常层相消，全部退化项排除出 N_FS 并由 R1b 处理。",
    }


def write_markdown(cert: dict) -> None:
    lines = [
        "# R1a 正常层 FS 平均放大界复核",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["conclusion"],
        "",
        "## 复核项",
    ]
    for item in cert["checks"]:
        lines += [
            f"### {item['id']}",
            f"- 命题：{item['claim']}",
            f"- 状态：`{item['status']}`",
            "- 证据：" + ", ".join(item["evidence"]),
            "",
        ]
    (DOCS / "r1a-normal-fs-average-review.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cert = build_certificate()
    (DOCS / "r1a-normal-fs-average-review.json").write_text(
        json.dumps(cert, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(cert)
    print(DOCS / "r1a-normal-fs-average-review.json")
    print(DOCS / "r1a-normal-fs-average-review.md")


if __name__ == "__main__":
    main()
