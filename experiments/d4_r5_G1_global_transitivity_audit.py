#!/usr/bin/env python3
"""D4/R5 G1 全局传递性审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

GATES = [
    {
        "id": "G1a_state_semantics",
        "claim": "L,D,B,C 在尺度递推、壳层加入和重分类后保持同一语义。",
        "evidence": ["docs/d4-r5-G1-state-semantics-audit.md", "docs/d4-r5-G1-partition-refinement-audit.md", "docs/d4-r5-G1-ordinary-energy-audit.md", "docs/d4-r5-G1-unified-exceptional-energy-audit.md", "docs/d4-r5-G1-unified-theoremization-audit.md", "docs/d4-r5-G1-O2-effective-support-audit.md", "docs/d4-r5-G1-Neff-mechanism-audit.md", "docs/d4-r5-G1-caseA-neighborhood-audit.md", "docs/d4-r5-G1-direct-neff-audit.md", "docs/d4-r5-G1-tau-bucket-ledger-audit.md", "docs/d4-r5-G1-joint-bucket-cauchy-audit.md", "docs/d4-r5-G1-bucket-danger-domain-audit.md", "docs/d4-r5-G1-six-bucket-simplex-audit.md", "docs/d4-r5-G1-bucket-density-ladder-audit.md", "docs/d4-r5-G1-worst-vector-qp-audit.md", "docs/d4-r5-G1-strict-qp-certificate.md", "docs/d4-r5-G1-strict-qp-near-vectors.md", "docs/d4-r5-G1-Aeff-audit.md", "docs/d4-r5-recursive-transitivity-analysis.md", "docs/d4-r5-rpl-correction.md", "docs/global-rigidity-growth-crt-route.md"],
        "status": "definitions_fixed_projection_and_Aeff_missing",
        "remaining": "证明剥离投影同型性；统一 exceptional 路线已压缩为 O1 ordinary<=8E、O2 直接 Neff(nonordinary)<=64、O3 能量语义、O4 支付兼容四个引理；O2 当前应证明联合 tau 桶二阶能量账本 Q/S^2>=1/64；固定 top-r/tail44 与逐桶独立常数账本均已被密邻域/桶审计排除。新的可证接口是桶内 Cauchy：Q/S^2>=sum_i m_i^2/n_i，再证明六桶质量-支撑危险域为空；二块粗并已审计为不足。当前最优子接口是“相邻 3/2 密度链 + 低三桶质量帽 low<=3/5”的联合引理；近危险支撑向量已由严格 Fraction QP 证书覆盖。",
    },
    {
        "id": "G1b_stable_capacity_payment",
        "claim": "stable 步的负 D 下降由 L_old*dL/10 支付，并可望远镜求和。",
        "evidence": ["docs/d4-r5-capacity-payment-audit.json", "docs/d4-r5-global-rpl-theorem.md"],
        "status": "local_verified_global_algebra_available",
        "remaining": "把局部三行样板推广到任意尺度危险链；证明 dL>=0 和壳层分类 stable 的判据全局有效。",
    },
    {
        "id": "G1c_jump_absorption",
        "claim": "jump 步要么坏度下降，要么落入有限外向证书窗口。",
        "evidence": ["docs/d4-r5-jump-absorption-audit.json", "docs/d4-r5-transitivity-proof-obligations.md"],
        "status": "local_verified_one_jump_global_boundary_count_missing",
        "remaining": "证明所有阈值穿越集合可数且误差可求和，或被有限危险窗口证书覆盖。",
    },
    {
        "id": "G1d_backflow_projection",
        "claim": "若无 stable 支付且无 jump 吸收，坏结构可投影回旧尺度，损失 eps_j 可求和。",
        "evidence": ["docs/d4-r5-rpl-local-closure.md", "docs/d4-r5-global-rpl-theorem.md"],
        "status": "not_proved_backflow_not_triggered_only_locally",
        "remaining": "构造投影算子 pi_j 并证明 sum eps_j 小于基尺度证书余量。",
    },
    {
        "id": "G1e_base_certificate_coverage",
        "claim": "所有回传终点由外向区间证书覆盖。",
        "evidence": ["docs/d4-r5-current-candidate-closure-status.md", "docs/d4-r5-global-rpl-gates.json"],
        "status": "local_H80_certificates_available_global_template_coverage_missing",
        "remaining": "证明终端窗口族枚举覆盖所有可能回传相位单元。",
    },
]


def build_audit() -> dict:
    return {
        "certificate_type": "D4_R5_G1_global_transitivity_audit",
        "status": "G1_reduced_to_state_semantics_backflow_and_jump_globalization",
        "gates": GATES,
        "minimal_remaining": [
            "G1a：状态定义已固定；统一 exceptional A_eff 已压缩为 O1--O4；O2 正式路线是直接 Neff<=64，剩余为联合桶 Cauchy 后的六桶质量-支撑危险域排除，优先证明相邻 3/2 密度链 + low<=3/5，及 low>3/5 时的补偿增强",
            "G1d：backflow 投影与 eps_j 可求和",
            "G1c/G1e：jump 边界计数与终端窗口族覆盖",
        ],
        "conclusion": "G1 的局部数值样板和 stable 支付恒等式已经很强；O2 不能再依赖固定 top-r/tail44 或逐桶独立常数；当前最优接口是联合桶 Cauchy 账本，需证明六桶质量-支撑危险域为空，不能粗并为两块；最小硬点已定位为证明结构二选一：low<=3/5 或密度链/高桶质量进一步增强。真正全局缺口仍是递归状态语义不变、backflow 投影可传递、jump/终端窗口族全局覆盖。",
    }


def write_markdown(audit: dict) -> None:
    lines = [
        "# D4/R5 G1 全局传递性审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["conclusion"],
        "",
        "## 递归门",
    ]
    for item in audit["gates"]:
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
    (DOCS / "d4-r5-G1-global-transitivity-audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    audit = build_audit()
    (DOCS / "d4-r5-G1-global-transitivity-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit)
    print(DOCS / "d4-r5-G1-global-transitivity-audit.json")
    print(DOCS / "d4-r5-G1-global-transitivity-audit.md")


if __name__ == "__main__":
    main()
