#!/usr/bin/env python3
"""D4/R5 G1a 尺度无关状态语义审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

STATE = [
    {
        "symbol": "S_j",
        "definition": "第 j 尺度的候选/危险冻结成员单元，等于旧尺度单元与新壳层非零同余约束的交。",
        "invariance_role": "递归剥离的对象；剥离新壳层应投影到 S_{j-1} 的同型冻结成员单元。",
        "status": "definition_fixed_projection_not_yet_proved",
    },
    {
        "symbol": "L_j",
        "definition": "付款口径活动容量：positive_contract_sum，按层分解后为各层正收缩质量之和。",
        "invariance_role": "stable 支付项 L_{j-1} Delta L_j / 10 使用同一 L；危险阈值采用 L_cap=0.48。",
        "status": "definition_fixed_local_evidence_available",
    },
    {
        "symbol": "E_j^*",
        "definition": "平方根层资源：transition_high_tail_l2_sqrt + transition_low_start_l2_sqrt + short_chain_l2_sqrt + light_l2_sqrt。",
        "invariance_role": "高容量强迫能量的辅助 Lyapunov 口径；避免使用局部可为负的裸 layer_l2。",
        "status": "definition_fixed_needs_derivation_from_layer_Cauchy",
    },
    {
        "symbol": "D_j^*",
        "definition": "容量缺陷 D_j^*=E_j^*-L_j^2/20。",
        "invariance_role": "若 L_j>L_cap，则希望 D_j^*>=eta_*=0.015，从危险类退出。",
        "status": "local_margin_observed_global_proof_missing",
    },
    {
        "symbol": "B_j",
        "definition": "坏度向量：light_over_026、potential_deficit、U_over_0182、V_over_0074、L_highmass 等阈值超额。",
        "invariance_role": "jump/backflow 递推的单调或可回传对象。",
        "status": "definition_fixed_boundary_count_missing",
    },
    {
        "symbol": "C_j",
        "definition": "层分类标签：light/short_chain/transition/highmass 及其阈值边界。",
        "invariance_role": "判定 stable 或 jump；jump 是 C_j 改变或阈值穿越。",
        "status": "definition_fixed_global_jump_count_missing",
    },
]


def build_audit() -> dict:
    return {
        "certificate_type": "D4_R5_G1_state_semantics_audit",
        "status": "G1a_state_definitions_fixed_transitivity_not_yet_proved",
        "state_variables": STATE,
        "normalization_contract": {
            "single_weight_convention": "所有 L_j 与 E_j^* 使用同一 positive_contract_sum / layer l2_sqrt 付款口径，不再混用裸 layer_l2。",
            "stable_step": "C_j=C_{j-1} 且新壳层只增加同型层质量；要求 Delta L_j>=0。",
            "jump_step": "C_j 改变或穿越 tau_sum/count/U/V/L 阈值。",
            "backflow_step": "非 stable 支付且非 jump 吸收时，需构造 pi_j:S_j -> S_{j-1}。",
        },
        "minimal_remaining": [
            "证明 S_j 剥离新壳层后仍投影到同型冻结成员单元",
            "从分层 Cauchy 推导每层 B_i <= A_i e_i 并给出全局 A_eff；需先处理 E_* 未覆盖 heavy/ordinary 正质量的问题",
            "证明 E_j^* 与 stable 支付恒等式兼容或作为辅助排除泛函传递",
        ],
        "conclusion": "G1a 的第一步已经完成：状态变量和归一化口径固定。它尚未证明全局传递性；下一步应证明投影同型性与分层 Cauchy 的尺度无关 A_eff。",
    }


def write_markdown(audit: dict) -> None:
    lines = [
        "# D4/R5 G1a 状态语义审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["conclusion"],
        "",
        "## 状态变量",
    ]
    for item in audit["state_variables"]:
        lines += [
            f"### `{item['symbol']}`",
            f"- 定义：{item['definition']}",
            f"- 递归作用：{item['invariance_role']}",
            f"- 状态：`{item['status']}`",
            "",
        ]
    lines += ["## 归一化契约"]
    for key, value in audit["normalization_contract"].items():
        lines.append(f"- `{key}`：{value}")
    lines += ["", "## 最小剩余"]
    for item in audit["minimal_remaining"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-state-semantics-audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    audit = build_audit()
    (DOCS / "d4-r5-G1-state-semantics-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit)
    print(DOCS / "d4-r5-G1-state-semantics-audit.json")
    print(DOCS / "d4-r5-G1-state-semantics-audit.md")


if __name__ == "__main__":
    main()
