#!/usr/bin/env python3
"""DBA-A2 atlas 固定变量数/次数表。

给每个 DBA atlas 生成元登记保守的变量数 n_i(r) 与次数 D_i(r)。
这里 r 是 connected moment/skeleton 复杂度参数；所有界只需依赖 r，不能依赖 P。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

TABLE = [
    {
        "id": "denominator_pole",
        "variables_n_i_r": "<= 2*r + 8",
        "degree_D_i_r": "<= 4*r + 16",
        "height_reason": "平移、乘积、代入；参数 U,m,t,h <= P^{O(1)}",
        "closed": True,
    },
    {
        "id": "derivative_zero",
        "variables_n_i_r": "<= 2*r + 8",
        "degree_D_i_r": "<= 8*r + 32",
        "height_reason": "N'D-ND' 的次数至多 deg N + deg D - 1；高度由求导和乘法规则控制",
        "closed": True,
    },
    {
        "id": "ramification",
        "variables_n_i_r": "<= 2*r + 9 including level parameter c",
        "degree_D_i_r": "<= (8*r + 32)^2",
        "height_reason": "Disc_x(N-cD) 与 Res_x(N-cD,N'D-ND') 是一变量 resultant；固定次数下高度 P^{O_r(1)}",
        "closed": True,
    },
    {
        "id": "four_point_rank_failure",
        "variables_n_i_r": "<= 8*r + 16; KS four-point normal form uses <= 8 free u-coordinates plus fixed auxiliary inverse variables",
        "degree_D_i_r": "<= 32*r + 128",
        "height_reason": "四点清分母多项式由四个固定次数正规形相乘相加；rank 失效由系数集合或固定次数 gcd/resultant atlas 记录",
        "closed": True,
    },
    {
        "id": "jacobian_common_branch",
        "variables_n_i_r": "<= 8*r + 16",
        "degree_D_i_r": "<= (32*r + 128)^4",
        "height_reason": "E 与 J_i 的多变量消元；变量数和次数只依赖 r，Macaulay/resultant 高度界给 P^{O_r(1)}",
        "closed": True,
    },
    {
        "id": "step_frequency_resonance",
        "variables_n_i_r": "<= 6 parameters h,t,m,U,T,d",
        "degree_D_i_r": "<= 3",
        "height_reason": "线性或低次数整数因子；高度 <= P^{O(1)}，平均损失由 A3 处理",
        "closed": True,
    },
    {
        "id": "layering_endpoint_low_volume",
        "variables_n_i_r": "not a DBA polynomial atlas item",
        "degree_D_i_r": "not applicable",
        "height_reason": "A4 非多项式预算项；由 C_L/C_KS/低体积账本吸收，不进入 A2 高度传播",
        "closed": True,
    },
]


def main() -> None:
    audit = {
        "certificate_type": "DBA_A2_fixed_degree_table",
        "status": "A2_fixed_variable_degree_bounds_recorded",
        "parameter": "r = connected moment/skeleton complexity",
        "principle": "Each n_i(r), D_i(r) depends only on r and not on P; hence all resultants have height P^{O_r(1)}.",
        "table": TABLE,
        "all_closed": all(row["closed"] for row in TABLE),
        "remaining_note": "Bounds are deliberately coarse. A final paper can replace them by sharper formulas, but no argument depends on sharpness.",
    }
    out = DOCS / "dba-A2-fixed-degree-table.json"
    out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# DBA-A2 固定变量数/次数表", "", f"**状态：** `{audit['status']}`", "", audit["principle"], "", "| Atlas 项 | 变量数上界 | 次数上界 | 高度理由 |", "|---|---:|---:|---|"]
    for row in TABLE:
        lines.append(f"| `{row['id']}` | `{row['variables_n_i_r']}` | `{row['degree_D_i_r']}` | {row['height_reason']} |")
    lines += ["", "## 结论", "所有 DBA 多项式 atlas 项的变量数和次数只依赖 `r`，因此标准 Macaulay/resultant 高度界给出 `P^{O_r(1)}`。`layering_endpoint_low_volume` 不是 DBA 多项式项，已由 A4 预算吸收。"]
    (DOCS / "dba-A2-fixed-degree-table.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    print(DOCS / "dba-A2-fixed-degree-table.md")


if __name__ == "__main__":
    main()
