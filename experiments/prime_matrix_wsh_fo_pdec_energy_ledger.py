#!/usr/bin/env python3
"""生成 FO-PDEC 低模能量账本。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py
  python3 experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py --theta 0.25

核心不等式：
  对解释方程多重集 E，记 t_ell 为同一解释因子 ell 的方程数，
  s_ell 为出现过的行残基数。定义

      Energy_ell = t_ell - s_ell * t_ell / ell.

  若 t_ell <= theta*ell，则 Energy_ell >= (1-theta)*t_ell。
  若 t_ell > theta*ell，则同一解释因子出现高负载，进入 Tail/PDEC 出口。

注意：该脚本验证能量下界账本，不证明最终 PDEC 阈值比较。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


def grouped_equations(equations: list[dict]) -> dict[str, list[dict]]:
    """构造全局、块、偏移行、矩阵行四种分组。"""
    groups: dict[str, list[dict]] = {"global": equations}
    by_block: defaultdict[tuple[int], list[dict]] = defaultdict(list)
    by_offset: defaultdict[tuple[int], list[dict]] = defaultdict(list)
    by_matrix_row: defaultdict[tuple[int, int], list[dict]] = defaultdict(list)
    for equation in equations:
        by_block[(equation["block_index"],)].append(equation)
        by_offset[(equation["offset_row_index"],)].append(equation)
        by_matrix_row[(equation["q"], equation["source_row"])].append(equation)
    for key, rows in by_block.items():
        groups[f"block:{key[0]}"] = rows
    for key, rows in by_offset.items():
        groups[f"offset-row:{key[0]}"] = rows
    for key, rows in by_matrix_row.items():
        groups[f"matrix-row:q{key[0]}:r{key[1]}"] = rows
    return groups


def energy_for_group(name: str, equations: Iterable[dict], theta: float) -> dict:
    """计算单个方程组的低模正超额能量。"""
    rows = list(equations)
    by_factor: defaultdict[int, Counter[int]] = defaultdict(Counter)
    for equation in rows:
        factor = equation["explaining_factor"]
        residue = equation["target_residue"]
        by_factor[factor].update([residue])

    total_energy = 0.0
    total_lower_bound = 0.0
    high_load_factors = []
    factor_rows = []
    for factor, residue_counter in sorted(by_factor.items()):
        factor_load = sum(residue_counter.values())
        support_size = len(residue_counter)
        energy = factor_load - support_size * factor_load / factor
        load_ratio = factor_load / factor
        lower_bound = max(0.0, 1.0 - theta) * factor_load if load_ratio <= theta else 0.0
        if load_ratio > theta:
            high_load_factors.append(
                {
                    "factor": factor,
                    "load": factor_load,
                    "load_ratio": load_ratio,
                    "support_size": support_size,
                }
            )
        total_energy += energy
        total_lower_bound += lower_bound
        factor_rows.append(
            {
                "factor": factor,
                "load": factor_load,
                "support_size": support_size,
                "load_ratio": load_ratio,
                "energy": energy,
                "theta_lower_bound": lower_bound,
                "top_residues": [
                    {"residue": residue, "load": load}
                    for residue, load in residue_counter.most_common(8)
                ],
            }
        )

    equation_count = len(rows)
    return {
        "group": name,
        "equation_count": equation_count,
        "distinct_factors": len(by_factor),
        "energy": total_energy,
        "energy_per_equation": total_energy / equation_count if equation_count else 0.0,
        "theta_lower_bound": total_lower_bound,
        "theta_lower_bound_per_equation": (
            total_lower_bound / equation_count if equation_count else 0.0
        ),
        "high_load_factor_count": len(high_load_factors),
        "high_load_factors": high_load_factors,
        "factor_rows": factor_rows,
    }


def build_ledger(source: dict, theta: float) -> dict:
    """生成 FO-PDEC 能量账本。"""
    groups = grouped_equations(source["equations"])
    group_rows = [
        energy_for_group(name, equations, theta)
        for name, equations in sorted(groups.items())
    ]
    global_row = next(row for row in group_rows if row["group"] == "global")
    non_global_rows = [row for row in group_rows if row["group"] != "global"]
    return {
        "status": "finite_fo_pdec_energy_ledger_not_global_proof",
        "theta": theta,
        "summary": {
            "group_count": len(group_rows),
            "global_equation_count": global_row["equation_count"],
            "global_energy": global_row["energy"],
            "global_energy_per_equation": global_row["energy_per_equation"],
            "global_theta_lower_bound": global_row["theta_lower_bound"],
            "global_high_load_factor_count": global_row["high_load_factor_count"],
            "min_group_energy_per_equation": min(
                (row["energy_per_equation"] for row in non_global_rows if row["equation_count"]),
                default=0.0,
            ),
            "max_group_high_load_factor_count": max(
                (row["high_load_factor_count"] for row in group_rows),
                default=0,
            ),
        },
        "groups": group_rows,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 能量账本。"""
    summary = result["summary"]
    theta = result["theta"]
    lines = [
        "# FO-PDEC 低模能量账本",
        "",
        "**状态：** `finite_fo_pdec_energy_ledger_not_global_proof`",
        "",
        "本文档直接审计 `FO-PDEC` 的低模正超额能量。它闭合的是组合能量下界和有限账本；最终仍需把该能量与正式 `PDEC` 阈值比较。",
        "",
        "## 能量不等式",
        "",
        "对固定解释因子 `ell`，记 `t_ell` 为方程数、`s_ell` 为出现过的行残基数，定义",
        "",
        "\\[",
        "  E_\\ell=t_\\ell-s_\\ell t_\\ell/\\ell。",
        "\\]",
        "",
        f"若 `t_ell <= theta ell` 且 `theta={theta}`，则",
        "",
        "\\[",
        "  E_\\ell\\ge (1-\\theta)t_\\ell。",
        "\\]",
        "",
        "若该条件失败，则同一解释因子已经高负载，进入 Tail/PDEC 出口。",
        "",
        "## 摘要",
        "",
        f"- 分组数：`{summary['group_count']}`。",
        f"- 全局方程数：`{summary['global_equation_count']}`。",
        f"- 全局能量：`{summary['global_energy']}`。",
        f"- 全局单位方程能量：`{summary['global_energy_per_equation']}`。",
        f"- 全局 theta 下界：`{summary['global_theta_lower_bound']}`。",
        f"- 全局高负载因子数：`{summary['global_high_load_factor_count']}`。",
        f"- 非全局分组最小单位方程能量：`{summary['min_group_energy_per_equation']}`。",
        f"- 最大分组高负载因子数：`{summary['max_group_high_load_factor_count']}`。",
        "",
        "## 分组账本",
        "",
        "| group | equations | factors | energy | energy/eq | theta lower | high-load factors |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for group in result["groups"]:
        lines.append(
            "| {group} | {eq} | {fac} | {energy:.6f} | {ratio:.6f} | {lower:.6f} | {high} |".format(
                group=group["group"],
                eq=group["equation_count"],
                fac=group["distinct_factors"],
                energy=group["energy"],
                ratio=group["energy_per_equation"],
                lower=group["theta_lower_bound"],
                high=group["high_load_factor_count"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "这一步给出真正硬攻 `FO-PDEC` 的可用定量武器：若解释因子没有高负载，则每条缺失方程贡献确定比例的低模正能量；若出现高负载，则已经是 Tail/PDEC 类型集中。剩余缺口不是方程或能量定义，而是正式 `PDEC` 阈值：必须证明上述能量超过同一坏窗集合的 `L_PDEC`，或证明非持久部分被 `SAE/Endpoint` 吸收。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-energy-ledger",
    )
    parser.add_argument("--theta", type=float, default=0.25)
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_ledger(source, args.theta)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
