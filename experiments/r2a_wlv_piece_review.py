#!/usr/bin/env python3
"""R2a WLV-piece 三步复核证书。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CHECKS = [
    {
        "id": "W1_complex_phase_rotation",
        "claim": "signed/complex Stieltjes 测度经极分解和四象限旋转后，只损失固定常数。",
        "evidence": ["docs/final-proof-draft.md:WLV-rot", "docs/final-proof-draft.md:6.18.1d-WLV"],
        "status": "closed_deterministic",
        "review_note": "不使用随机符号或正相关假设。",
    },
    {
        "id": "W2_variation_to_box_piece",
        "claim": "Hardy--Krause 分部后，端点/角点承载大值则入低体积坏层；否则存在二维正常盒片承载大值。",
        "evidence": ["docs/final-proof-draft.md:WLV-piece", "docs/final-proof-draft.md:6.14.2c-FS8"],
        "status": "closed_modulo_existing_low_volume_atlas",
        "review_note": "避免把总变差集中在低维端点误判为二维密度。",
    },
    {
        "id": "W3_LV_weight_absorption",
        "claim": "抽取的正权盒片在 vdC 平移后仍满足 KS-W 型变差界，新增端点由 C_WLV/C_poly 支付。",
        "evidence": ["docs/final-proof-draft.md:KS-W", "docs/final-proof-draft.md:KS-W-poly", "docs/r2-Cpoly-absorption-scan.md"],
        "status": "closed_modulo_parameter_ledger",
        "review_note": "若平移端点超账本，则归入 dyadic 端点/低体积坏层。",
    },
]


def build_certificate() -> dict:
    return {
        "certificate_type": "R2a_WLV_piece_review",
        "status": "WLV_piece_review_passed_modulo_existing_atlas_and_parameter_ledger",
        "target": "6.18.1d-WLV / WLV-piece",
        "checks": CHECKS,
        "conclusion": "WLV-piece 的 signed/complex 旋转、总变差到二维盒片、LV-KS 权重吸收三步均已拆成确定性审稿点；剩余不再是新数学接口，而是确认引用的低体积 atlas 与 C_poly 参数账本被最终接受。",
    }


def write_markdown(cert: dict) -> None:
    lines = [
        "# R2a WLV-piece 三步复核",
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
            f"- 审查说明：{item['review_note']}",
            "- 证据：" + ", ".join(item["evidence"]),
            "",
        ]
    (DOCS / "r2a-wlv-piece-review.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cert = build_certificate()
    (DOCS / "r2a-wlv-piece-review.json").write_text(
        json.dumps(cert, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(cert)
    print(DOCS / "r2a-wlv-piece-review.json")
    print(DOCS / "r2a-wlv-piece-review.md")


if __name__ == "__main__":
    main()
