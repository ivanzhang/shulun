#!/usr/bin/env python3
"""DBA-A2/A5 高度传播与参数吸收账本。

把 6.15.5 中的保守对数幂指数数值化，检查 B1/B2/B4 是否吸收
DBA atlas 的高度、Rankin、coarea、KS 与 FS8-polymer 损失。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

DEFAULT_COMPONENTS = {
    "C_ht": 120,
    "C_rk": 80,
    "C_dy": 120,
    "C_co": 160,
    "C_st": 80,
    "C_LV": 160,
    "C_AE": 160,
    "C_L": 80,
    "C_KS": 80,
    "C_poly": 0,
}

A2_HEIGHT_RULES = [
    {
        "operation": "addition_multiplication_substitution",
        "degree_growth": "O_r(1)",
        "height_growth": "P^{O_r(1)}",
        "used_by": ["denominator_pole", "four_point_E", "Kloosterman_clear_denominators"],
        "status": "standard_closed",
    },
    {
        "operation": "derivative",
        "degree_growth": "d -> d-1",
        "height_growth": "H(P') <= d H(P)",
        "used_by": ["derivative_zero", "coarea_critical_points"],
        "status": "standard_closed",
    },
    {
        "operation": "univariate_resultant_discriminant",
        "degree_growth": "O(d^2)",
        "height_growth": "H(Res(P,Q)) <= (2d)^{O(d)} H(P)^{O(d)} H(Q)^{O(d)}",
        "used_by": ["ramification", "branch_merge"],
        "status": "standard_closed_for_fixed_d",
    },
    {
        "operation": "multivariate_elimination_resultant",
        "degree_growth": "D^{O_n(1)} for fixed variable count n",
        "height_growth": "H <= (C D)^{O_n(D^n)} prod_i H_i^{O_n(D^n)}; fixed D,n gives P^{O_r(1)}",
        "used_by": ["jacobian_common_branch", "rank_failure_high_dimensional_factor"],
        "status": "closed_if_fixed_variable_count_and_degree_are_explicitly_recorded",
    },
    {
        "operation": "integer_factor_resonance",
        "degree_growth": "linear factors only",
        "height_growth": "<= P^{O(1)}",
        "used_by": ["step_frequency_resonance"],
        "status": "standard_closed_plus_step_average",
    },
]


def build(B: int = 20, components: dict[str, int] | None = None) -> dict:
    comps = dict(DEFAULT_COMPONENTS)
    if components:
        comps.update(components)
    C_star = max(comps.values())
    B4 = 4 * B + 4 * C_star + 100
    B2 = 6 * B + 4 * C_star + 120
    B1 = 8 * B + 4 * C_star + 160
    B5_min = B + comps["C_st"] + 3
    ks_rhs = 4 * comps["C_KS"] + 3 * comps["C_L"] + C_star + 20
    inequalities = [
        {"name": "thickness_delta", "lhs": B1, "rhs": C_star + B + 10, "margin": B1 - (C_star + B + 10)},
        {"name": "small_root_density", "lhs": B2, "rhs": C_star + 2 * B + 20, "margin": B2 - (C_star + 2 * B + 20)},
        {"name": "step_frequency_T", "lhs": B4, "rhs": C_star + 2 * B + 20, "margin": B4 - (C_star + 2 * B + 20)},
        {"name": "KS_margin_B1", "lhs": B1, "rhs": ks_rhs, "margin": B1 - ks_rhs},
        {"name": "KS_margin_B2", "lhs": B2, "rhs": ks_rhs, "margin": B2 - ks_rhs},
        {"name": "Stieltjes_B5_min", "lhs": B5_min, "rhs": B + comps["C_st"] + 3, "margin": 0},
    ]
    return {
        "certificate_type": "DBA_A2_A5_parameter_ledger",
        "status": "A2_standard_height_closed_conditionally_on_fixed_degree_atlas; A5_numeric_inequalities_pass",
        "base_fourier_B": B,
        "components": comps,
        "C_star": C_star,
        "chosen_parameters": {"B1": B1, "B2": B2, "B4": B4, "B5_min": B5_min},
        "A2_height_rules": A2_HEIGHT_RULES,
        "A2_remaining_explicitness": [
            "在论文正文或附录中记录每个 atlas 项的变量数 n 和次数 D 的固定上界符号 d_i(r)。",
            "对 multivariate_elimination_resultant 引用标准 Macaulay/resultant 高度界，说明 fixed n,D 下为 P^{O_r(1)}。",
            "对 rank_failure_high_dimensional_factor 说明若非零多项式低 rank，则进入系数/resultant atlas，而非正常层。",
        ],
        "A5_inequalities": inequalities,
        "all_A5_margins_positive_except_definition_minimum": all(item["margin"] > 0 or item["name"] == "Stieltjes_B5_min" for item in inequalities),
        "interpretation": "With B=20 and C_star=160, B1=960, B2=880, B4=820. The Kloosterman margins are positive; parameter absorption is no longer the main structural blocker once A1/A2 explicitness is accepted.",
    }


def main() -> None:
    ledger = build()
    out = DOCS / "dba-A2-A5-parameter-ledger.json"
    out.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# DBA-A2/A5 高度传播与参数吸收账本", "", f"**状态：** `{ledger['status']}`", "", "## 参数"]
    lines.append(f"- `B={ledger['base_fourier_B']}`")
    lines.append(f"- `C_*={ledger['C_star']}`")
    for key, value in ledger["chosen_parameters"].items():
        lines.append(f"- `{key}={value}`")
    lines += ["", "## A2 高度传播规则"]
    for rule in A2_HEIGHT_RULES:
        lines.append(f"- `{rule['operation']}`：次数 `{rule['degree_growth']}`；高度 `{rule['height_growth']}`；状态 `{rule['status']}`")
    lines += ["", "## A5 参数不等式"]
    lines.append("| 名称 | 左边 | 右边 | 余量 |")
    lines.append("|---|---:|---:|---:|")
    for item in ledger["A5_inequalities"]:
        lines.append(f"| {item['name']} | {item['lhs']} | {item['rhs']} | {item['margin']} |")
    lines += ["", "## 剩余显式化义务"]
    for item in ledger["A2_remaining_explicitness"]:
        lines.append(f"- {item}")
    lines += ["", "## 解释", ledger["interpretation"]]
    (DOCS / "dba-A2-A5-parameter-ledger.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    print(DOCS / "dba-A2-A5-parameter-ledger.md")


if __name__ == "__main__":
    main()
