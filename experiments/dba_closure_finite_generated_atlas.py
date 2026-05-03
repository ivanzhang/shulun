#!/usr/bin/env python3
"""生成 DBA-closure 有限生成坏层 atlas。

用途：把正文 6.14 的坏层覆盖矩阵转成机器可审查 JSON，
并标记每类坏层的覆盖状态、所需高度账本和剩余人工核查点。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

GENERATORS = [
    {
        "id": "denominator_pole",
        "name": "分母/不可逆层",
        "polynomials": ["D(x_i)", "D_t(x_i)", "S(a_i)", "a_i", "a_i+t", "a_i+jh", "u_1", "u_1+h", "u_2", "u_1u_2(u_1+h)"],
        "covers": ["函数无定义", "CRT/模逆元不可逆", "Kloosterman reciprocity 分母退化"],
        "height_status": "standard_fixed_degree_height",
    },
    {
        "id": "derivative_zero",
        "name": "一变量导数层",
        "polynomials": ["N'D-ND'", "N_t'D_t-N_tD_t'"],
        "covers": ["R'(x_i)=0", "coarea 单调段端点", "水平集聚集的导数退化"],
        "height_status": "standard_fixed_degree_height",
    },
    {
        "id": "ramification",
        "name": "ramification/分支合并层",
        "polynomials": ["Disc_x(N(x)-cD(x))", "Res_x(N-cD,N'D-ND')"],
        "covers": ["水平纤维多根", "多前像合并", "短弧层数失控"],
        "height_status": "resultant_height_needed_but_standard",
    },
    {
        "id": "four_point_rank_failure",
        "name": "四点 rank 失效层",
        "polynomials": ["coefficients of E", "gcd/cofactor coefficients of E modulo q", "KS eight-variable four-point coefficients"],
        "covers": ["E mod q 恒等为零", "有效素因子未贡献 rank", "清分母多项式含高维公共因子"],
        "height_status": "coefficient_height_standard; high-dimensional factor test remains atlas item",
    },
    {
        "id": "jacobian_common_branch",
        "name": "Jacobian/临界纤维层",
        "polynomials": ["∂_{x_i}E·Dtot-E·∂_{x_i}Dtot", "Res(E,J_i)", "multivariate elimination resultants"],
        "covers": ["F 与梯度/Jacobian 共维不足", "投影 Jacobian 消失", "coarea 法向导数过小"],
        "height_status": "multivariate_resultant_height_required",
    },
    {
        "id": "step_frequency_resonance",
        "name": "步长/频率共振层",
        "polynomials": ["h", "t", "mU", "mT", "m", "d", "mdh"],
        "covers": ["q|h", "q|t", "q|mU", "q|mT", "差分/Fourier 频率不可检测"],
        "height_status": "integer_factor_height_trivial; needs averaging 1/q+1/T",
    },
    {
        "id": "layering_endpoint_low_volume",
        "name": "层化端点/低体积账本",
        "polynomials": ["dyadic endpoints", "W_h step endpoints", "low-volume box inequalities"],
        "covers": ["权重突变", "短弧层数超过对数幂", "低体积盒端点余量"],
        "height_status": "not_DBA_polynomial_only; handled by C_L/C_KS and low-volume budget",
    },
]

SOURCE_MATRIX = [
    ("6.10.1", "D_i=0 / 四点分母不可逆", "denominator_pole"),
    ("6.10.1", "E mod q 恒等为零", "four_point_rank_failure"),
    ("6.10.2", "对角/半对角", "separate_count_not_DBA"),
    ("6.10.3", "水平纤维厚化根簇过多", "ramification"),
    ("6.10.3", "R' 消失", "derivative_zero"),
    ("6.10.4", "局部 rank 低于 1", "four_point_rank_failure or jacobian_common_branch"),
    ("6.11.1", "F 与梯度同时小", "jacobian_common_branch"),
    ("6.12.2", "投影 Jacobian 消失", "derivative_zero or ramification or jacobian_common_branch"),
    ("6.13.2", "小导数单调段", "derivative_zero or jacobian_common_branch"),
    ("6.13.2", "分母极点/多值分支合并", "denominator_pole or ramification"),
    ("6.18.1d", "W_h 阶梯端点/权重突变", "layering_endpoint_low_volume"),
    ("6.18.1e", "q|h, q|mT, 分母不可逆", "step_frequency_resonance or denominator_pole"),
    ("6.18.2c", "层化四点厚化异常", "four_point_rank_failure or jacobian_common_branch"),
    ("6.7--6.8", "q|t,q|h,q|mU", "step_frequency_resonance"),
    ("4.3.6/FS8", "多逆元 CRT/Kloosterman 分支退化", "denominator_pole or ramification or step_frequency_resonance"),
    ("6.17.1--6.17.3", "sawtooth 端点相位 Fourier 截断尾", "fourier_truncation_tail"),
    ("6.17.6/6.18.1d", "权重 W(a) 变差或 dyadic 端点过多", "layering_endpoint_low_volume"),
    ("B.0.3e+", "CRT 逆元 b(a) 分母或兼容失败", "denominator_pole or ramification"),
    ("6.18.1c", "差分相位 F_h(a) 分母为零或分片无定义", "denominator_pole"),
    ("6.18.1e", "非共振步长检测失败 q|h,q|mT,q|mU", "step_frequency_resonance"),
    ("6.18.2a--b", "短弧层化 L 超对数幂", "denominator_pole or derivative_zero or ramification or layering_endpoint_low_volume"),
    ("6.13.1--6.13.3", "coarea 切片法向导数为零", "derivative_zero or jacobian_common_branch"),
    ("4.3.6h/6.18.1d-KS-J", "Kloosterman reciprocity 模逆元分支退化", "denominator_pole or ramification or step_frequency_resonance"),
    ("6.18.1d-KS", "KS-W 双线性权重变差和端点分片", "layering_endpoint_low_volume"),
    ("6.18.1d-KS-J/6.15.3a", "KS-J 中 z,t,resultant atlas 退化", "denominator_pole or derivative_zero or ramification or jacobian_common_branch"),
    ("6.13.6/6.15.3a-K1", "KS-DC 切片端点余量或低体积盒", "layering_endpoint_low_volume or jacobian_common_branch"),
    ("6.13.6/6.15.3a-K2", "Kloosterman 八变量 rank 失效", "four_point_rank_failure or jacobian_common_branch"),
    ("FS8-polymer", "skeleton 标签、短块来源、gap-word 端点过多", "layering_endpoint_low_volume"),
    ("FS8-polymer", "不同 connected 分量相位分离", "component_split_mobius_cancelled"),
    ("FS8-polymer", "Hall 叶变量匹配失败", "four_point_rank_failure or jacobian_common_branch"),
    ("FS8-polymer", "相位差分落入共振弧", "step_frequency_resonance or jacobian_common_branch or four_point_rank_failure"),
    ("FS8-polymer", "多 skeleton 坏素重复计数", "rankin_divisor_budget"),
]

BUDGET_CLASSES = {
    "denominator_pole": "DBA polynomial atlas; A2 height + A5 Rankin budget",
    "derivative_zero": "DBA polynomial atlas; A2 height + coarea budget C_co",
    "ramification": "DBA resultant atlas; A2 resultant height + C_co/C_L budget",
    "four_point_rank_failure": "rank/resultant atlas; A2 coefficient height + C_rk budget",
    "jacobian_common_branch": "multivariate resultant atlas; A2 multivariate height + C_co budget",
    "step_frequency_resonance": "A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4",
    "layering_endpoint_low_volume": "A4 non-polynomial budget; C_L/C_KS/low-volume boxes",
    "separate_count_not_DBA": "separate diagonal/semidiagonal count; not DBA",
    "fourier_truncation_tail": "Fourier truncation parameter budget B1; not DBA",
    "component_split_mobius_cancelled": "disconnected cumulant component cancels by Mobius inversion; not DBA",
    "rankin_divisor_budget": "bad prime multiplicity counted by Rankin/divisor budget C_rk",
}

A3_A4_BUDGET = [
    {
        "id": "A3_step_frequency_resonance",
        "objects": ["q|h", "q|t", "q|mU", "q|mT", "q|m", "q|d", "q|mdh"],
        "estimate": "average over step/frequency gives O(1/q+1/T)",
        "absorption": "1/q is absorbed by DBA bad-prime Rankin budget C_rk; 1/T is absorbed by B4 with margin 600 in dba-A2-A5-parameter-ledger",
        "status": "budget_classified_numeric_margin_available",
    },
    {
        "id": "A4_layering_endpoint_low_volume",
        "objects": ["W_h step endpoints", "short-arc layer count", "dyadic endpoints", "low-volume boxes", "coarea slicing endpoints"],
        "estimate": "normal layer count <= log^{C_L} P; Kloosterman slicing/rank overhead <= log^{C_KS} P; low-volume boxes enter explicit low-volume budget",
        "absorption": "C_L=80 and C_KS=80 are included in C_star=160; KS margins are positive in dba-A2-A5-parameter-ledger",
        "status": "budget_classified_numeric_margin_available",
    },
]

SEPARATE_TERMS = [
    {
        "id": "fourier_truncation_tail",
        "status": "parameter_budget_B1",
        "reason": "非结构坏层，由 Fourier 截断参数直接压制。",
    },
    {
        "id": "linear_combination_of_endpoints",
        "status": "no_new_bad_layer",
        "reason": "只是已覆盖 sawtooth 端点项的线性组合。",
    },
    {
        "id": "diagonal_semidiagonal",
        "status": "separately_counted",
        "reason": "在四点能量中作为 O(A^2)/半对角项单独计数。",
    },
]


def build() -> dict:
    coverage_rows = []
    unknown_destinations = []
    for source, failure, dest in SOURCE_MATRIX:
        destination_parts = [part.strip() for part in dest.split(" or ")]
        budgets = []
        for part in destination_parts:
            budget = BUDGET_CLASSES.get(part)
            if budget is None:
                unknown_destinations.append({"source": source, "failure_mode": failure, "unknown_destination": part})
            else:
                budgets.append(budget)
        coverage_rows.append(
            {
                "source": source,
                "failure_mode": failure,
                "atlas_destination": dest,
                "budget_destinations": budgets,
            }
        )
    return {
        "certificate_type": "DBA_closure_finite_generated_atlas",
        "status": "atlas_extracted_A3_A4_budget_classified_A1_requires_final_source_audit",
        "source_sections": ["final-proof-draft.md:6.10--6.14", "final-proof-draft.md:6.18", "final-proof-draft.md:4.3.6/FS8"],
        "generators": GENERATORS,
        "source_coverage_matrix": coverage_rows,
        "unknown_destinations": unknown_destinations,
        "coverage_destination_check_passed": not unknown_destinations,
        "budget_classes": BUDGET_CLASSES,
        "A3_A4_budget": A3_A4_BUDGET,
        "separate_non_DBA_terms": SEPARATE_TERMS,
        "remaining_review_obligations": [
            "确认 source_coverage_matrix 的来源行已覆盖 6.10--6.18 与 4.3.6/FS8 中所有失败方式；当前脚本只检查每个已列来源有合法去向。",
            "对 multivariate elimination resultants 给出固定次数/高度标准界引用或附录证明。",
            "A3/A4 已预算归类；最终需核对正文每次引用均指向 A3_A4_budget 中的相应条目。",
        ],
        "closure_if_obligations_met": "DBA-closure follows; combined with discrete coarea and local rank, this closes 4E-DISP and feeds UAS.",
    }


def main() -> None:
    audit = build()
    out = DOCS / "dba-closure-finite-generated-atlas.json"
    out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# DBA-closure 有限生成坏层 Atlas", "", f"**状态：** `{audit['status']}`", "", "## 生成元"]
    for gen in GENERATORS:
        lines.append(f"### {gen['id']}：{gen['name']}")
        lines.append("- 覆盖：" + "；".join(gen["covers"]))
        lines.append("- 高度状态：" + gen["height_status"])
        lines.append("")
    lines.append("## 覆盖矩阵")
    lines.append("| 来源 | 失败方式 | Atlas 去向 | 预算去向 |")
    lines.append("|---|---|---|---|")
    for row in audit["source_coverage_matrix"]:
        lines.append(f"| {row['source']} | {row['failure_mode']} | {row['atlas_destination']} | {'; '.join(row['budget_destinations'])} |")
    lines += ["", "## A3/A4 预算归类"]
    for item in A3_A4_BUDGET:
        lines.append(f"### {item['id']}")
        lines.append("- 对象：" + "；".join(item["objects"]))
        lines.append("- 估计：" + item["estimate"])
        lines.append("- 吸收：" + item["absorption"])
        lines.append("- 状态：" + item["status"])
        lines.append("")
    lines += ["", "## 剩余审查义务"]
    for item in audit["remaining_review_obligations"]:
        lines.append(f"- {item}")
    lines += ["", "## 条件闭合结论", audit["closure_if_obligations_met"]]
    (DOCS / "dba-closure-finite-generated-atlas.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    print(DOCS / "dba-closure-finite-generated-atlas.md")


if __name__ == "__main__":
    main()
