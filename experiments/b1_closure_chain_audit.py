#!/usr/bin/env python3
"""B1 闭合链审计。

把 DBA-closure 的 atlas 证书接回 4E-DISP、UAS、FNL、NL、B.0.4*，
并区分主链闭合义务与 7.2 阈值压缩增强义务。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CHAIN = [
    {
        "id": "C1_DBA_closure",
        "claim": "DBA-closure 吸收分母、导数、ramification、rank、Jacobian、共振与低体积坏层。",
        "evidence": [
            "docs/dba-closure-finite-generated-atlas.md",
            "docs/dba-A1-source-coverage-certificate.md",
            "docs/dba-A2-fixed-degree-table.md",
            "docs/dba-A2-A5-parameter-ledger.md",
            "docs/b1-dba-final-acceptance-review.md",
        ],
        "status": "A1_A5_reviews_passed_modulo_final_editorial_acceptance",
    },
    {
        "id": "C2_4E_DISP",
        "claim": "离散 coarea、局部 rank 与 DBA-closure 推出四点厚化分散 4E-DISP。",
        "evidence": ["final-proof-draft.md:6.10", "final-proof-draft.md:6.13", "final-proof-draft.md:6.14.7"],
        "status": "conditional_on_C1_and_standard_local_rank/coarea_acceptance",
    },
    {
        "id": "C3_UAS",
        "claim": "4E-DISP 通过 LV/AE 能量放大排除短弧集中，给出 sawtooth 路线的 UAS。",
        "evidence": ["final-proof-draft.md:6.9.5", "final-proof-draft.md:6.18.1--6.18.3"],
        "status": "conditional_on_C2_and_LV_AE_chain",
    },
    {
        "id": "C4_FNL_NL",
        "claim": "UAS/DBA 排除大 Fourier 值并推出 FNL，继而得到 NL。",
        "evidence": ["final-proof-draft.md:6.17", "final-proof-draft.md:6.18.4"],
        "status": "conditional_on_C3_and_admissibility_6_17_6",
    },
    {
        "id": "C5_B004_star",
        "claim": "FNL/NL 闭合硬边界 sawtooth 接口 B.0.4*。",
        "evidence": ["final-proof-draft.md:6.18.4", "final-proof-draft.md:6.16.2"],
        "status": "sawtooth_route_conditionally_closed; does_not_close_smooth_prime_weight_route",
    },
    {
        "id": "C6_row_hard_route",
        "claim": "B.0.4* 接入行侧硬路线；R1/R2 终审证书已生成。",
        "evidence": ["docs/c6-row-hard-route-audit.md", "docs/r1-gap-word-capacity-audit.md", "docs/r2a-weighted-fnl-ks-interface-audit.md"],
        "status": "row_hard_route_reduced_to_existing_FS8_DBA_parameter_acceptance",
    },
]

SEPARATE_INTERFACES = [
    {
        "id": "S1_smooth_prime_weight_route",
        "description": "带 dπ(p) 的 B.0.4S-short 需要素数权/AP 双线性输入；UAS/DBA 只闭合硬 sawtooth 边界。",
        "evidence": ["final-proof-draft.md:6.16"],
        "status": "separate_not_closed",
    },
    {
        "id": "S2_chernoff_threshold_enhancements",
        "description": "7.2 chernoff1 / CH-tail / strong CH-FS 是阈值压缩增强链；不是当前 sawtooth 链的必要条件，但低阈值方案需要它们。",
        "evidence": ["final-proof-draft.md:7.2.T1", "final-proof-draft.md:7.2.CH-FS"],
        "status": "separate_enhancement_chain_not_fully_closed",
    },
    {
        "id": "S3_column_LC",
        "description": "列侧点态容量 LC 独立于行侧 B1 sawtooth 链。",
        "evidence": ["final-proof-draft.md:C.2", "docs/global-unconditional-closure-audit.md"],
        "status": "separate_global_blocker",
    },
]


def main() -> None:
    audit = {
        "certificate_type": "B1_closure_chain_audit",
        "status": "B1_row_sawtooth_route_reduced_to_existing_certificate_acceptance; global_theorem_not_closed",
        "chain": CHAIN,
        "separate_interfaces": SEPARATE_INTERFACES,
        "conclusion": "DBA-A1--A5、R1a/R1b 与 R2a 终审证书已支撑行侧 B1 sawtooth 硬路线的局部闭合；剩余是接受既有证书链，而非新的 B1 局部硬点。全局主定理仍受 R5 全局化、列侧 LC、显式阈值与有限验证阻塞。",
    }
    (DOCS / "b1-closure-chain-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# B1 闭合链审计", "", f"**状态：** `{audit['status']}`", "", audit["conclusion"], "", "## 主链"]
    for node in CHAIN:
        lines += [f"### {node['id']}", f"- 命题：{node['claim']}", f"- 状态：`{node['status']}`", "- 证据：" + ", ".join(node["evidence"]), ""]
    lines += ["## 独立接口"]
    for item in SEPARATE_INTERFACES:
        lines += [f"### {item['id']}", f"- 说明：{item['description']}", f"- 状态：`{item['status']}`", "- 证据：" + ", ".join(item["evidence"]), ""]
    (DOCS / "b1-closure-chain-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "b1-closure-chain-audit.json")
    print(DOCS / "b1-closure-chain-audit.md")


if __name__ == "__main__":
    main()
