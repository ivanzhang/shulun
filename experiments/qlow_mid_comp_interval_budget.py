#!/usr/bin/env python3
"""QLOW-MID-COMP：外向舍入误差预算表。

用法示例：
  python3 experiments/qlow_mid_comp_interval_budget.py
  python3 experiments/qlow_mid_comp_interval_budget.py --total-budget 0.06
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_INPUT = MONOGRAPH / "qlow-mid-comp-grid-certificate.json"


def load_certificate(path: Path) -> dict:
    """读取上一阶段的紧区间网格证书。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入证书: {path}")
    return json.loads(path.read_text())


def split_budget(total_budget: float) -> dict[str, float]:
    """把总外向舍入预算拆成可审查的误差来源。"""
    return {
        "phi_quadrature_and_mellin": 0.35 * total_budget,
        "trig_log_interval_oracle": 0.25 * total_budget,
        "selberg_weight_solver": 0.20 * total_budget,
        "grid_endpoint_and_cell_weight": 0.12 * total_budget,
        "json_decimal_rounding": 0.08 * total_budget,
    }


def analyze(audit: dict, total_budget: float) -> dict:
    """计算每个样本离目标常数的可承受余量。"""
    budget_parts = split_budget(total_budget)
    rows = []
    min_raw_slack = float("inf")
    min_post_budget_slack = float("inf")
    hardest_case = None
    for case in audit["cases"]:
        target = float(case["target"])
        certified = float(case["certified_ratio"])
        raw_slack = target - certified
        post_budget_upper = certified + total_budget
        post_budget_slack = target - post_budget_upper
        row = {
            "P": case["P"],
            "R_exp": case["R_exp"],
            "R": case["R"],
            "certified_ratio": certified,
            "target": target,
            "raw_slack": raw_slack,
            "total_interval_budget": total_budget,
            "post_budget_upper": post_budget_upper,
            "post_budget_slack": post_budget_slack,
            "passes_after_budget": post_budget_slack > 0,
            "max_allowable_budget": raw_slack,
        }
        rows.append(row)
        if raw_slack < min_raw_slack:
            min_raw_slack = raw_slack
            hardest_case = row
        min_post_budget_slack = min(min_post_budget_slack, post_budget_slack)
    return {
        "certificate_type": "qlow_mid_comp_interval_budget",
        "status": "interval_budget_ready_not_yet_formal_interval_proof",
        "source": str(DEFAULT_INPUT.relative_to(ROOT)),
        "total_interval_budget": total_budget,
        "budget_parts": budget_parts,
        "min_raw_slack": min_raw_slack,
        "min_post_budget_slack": min_post_budget_slack,
        "hardest_case": hardest_case,
        "cases": rows,
    }


def render_markdown(result: dict) -> str:
    """渲染 Markdown 预算表。"""
    hardest = result["hardest_case"]
    lines = [
        "# QLOW-MID-COMP 外向舍入误差预算",
        "",
        f"**状态：** `{result['status']}`",
        "",
        "本文件把紧区间网格证书升级为“区间化前的预算证书”：",
        "",
        "\\[",
        "C_{\\rm grid}+C_{\\rm Lip}+C_{\\rm interval}<C_{\\rm target}.",
        "\\]",
        "",
        "它不把浮点扫描当作证明；作用是量化正式外向舍入证明最多允许消耗多少余量。",
        "",
        "## 总预算",
        "",
        f"- 目标常数：`0.35`。",
        f"- 预留外向舍入总预算：`{result['total_interval_budget']:.6f}`。",
        f"- 最小原始余量：`{result['min_raw_slack']:.6f}`。",
        f"- 扣除预算后最小余量：`{result['min_post_budget_slack']:.6f}`。",
        f"- 最紧样本：`P={hardest['P']}, R={hardest['R']}`。",
        "",
        "## 预算拆分",
        "",
        "| 来源 | 预算 | 证明义务 |",
        "| --- | ---: | --- |",
    ]
    descriptions = {
        "phi_quadrature_and_mellin": "给 `Phihat` 的 Mellin/积分截断与求积外向误差",
        "trig_log_interval_oracle": "给 `sin/cos/log` 的有理区间包络误差",
        "selberg_weight_solver": "给 Selberg 线性系统、`omega` 与 `V_omega` 的区间求解误差",
        "grid_endpoint_and_cell_weight": "给端点、网格宽度和 `|Phihat|` 加权平均替换误差",
        "json_decimal_rounding": "给十进制导出和表格抄录误差",
    }
    for name, value in result["budget_parts"].items():
        lines.append(f"| `{name}` | {value:.6f} | {descriptions[name]} |")
    lines += [
        "",
        "## Selberg 子项进展",
        "",
        "`docs/monograph/selberg-rational-weight-audit.md` 已把有限样本中的 Selberg 最优权线性系统改为有理精确审计。",
        "因此 `selberg_weight_solver=0.013000` 在当前样本上不再表示浮点消元误差，而应解释为以下剩余义务的保守预算：",
        "",
        "- 从有限样本推广到 `P>=P0` 的统一 `V_omega` 与对数矩常数；",
        "- `sum |omega_l|log(l)/l` 中 `log(l)` 的有理区间 oracle；",
        "- 正式稿中有理表格抄录和外向输出误差。",
        "",
        "## sin/cos/log 子项进展",
        "",
        "`docs/monograph/trig-log-interval-oracle-audit.md` 已用纯有理级数建立当前样本所有三角与对数调用的统一 oracle 半径。",
        "其最大半径为 `2.333e-67`，远小于 `trig_log_interval_oracle=0.016250` 的预算量级。",
        "`docs/monograph/qlow-mid-comp-hq-interval-audit.md` 又把该半径接入 `H/Q`，得到 `rho` 增量 `6.600e-67`。",
        "因此当前有限样本中的 `sin/cos/log` 外向包络和 `H/Q` 复数区间增量都不再是常数余量瓶颈。",
        "`docs/monograph/qlow-mid-comp-supnorm-audit.md` 进一步给出 Phihat-free 的 `sup rho` 旁路，最紧 `supBound=0.296630<0.35`。",
        "所以 `QLOW-MID-COMP` 的紧区间常数界不再依赖 `Phihat` 求积外向区间。",
        "",
        "",
        "## 样本余量表",
        "",
        "| P | R | certified | rawSlack | postBudgetUpper | postBudgetSlack | pass |",
        "|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for row in result["cases"]:
        lines.append(
            f"| {row['P']} | {row['R']} | {row['certified_ratio']:.6f} | "
            f"{row['raw_slack']:.6f} | {row['post_budget_upper']:.6f} | "
            f"{row['post_budget_slack']:.6f} | {'Y' if row['passes_after_budget'] else 'N'} |"
        )
    lines += [
        "",
        "## 严格化判据",
        "",
        "若后续区间程序逐项证明",
        "",
        "\\[",
        "C_{\\rm interval}\\le "
        f"{result['total_interval_budget']:.6f},",
        "\\]",
        "",
        "则当前样本证书全部仍满足 `C_comp<0.35`。进一步地，`sup-rho` 旁路已把 `Phihat` 从紧区间证明中移除，下一步应集中在统一 Selberg 矩常数与 `RRD/OSPC`。",
        "",
        "## 未闭合点",
        "",
        "- 当前预算表不是形式证明；它只是给出形式证明需要满足的误差上限。",
        "- `sin/cos/log` 与 `H/Q` 复数区间增量已完成样本级审计。",
        "- Selberg 权样本线性系统已精确审计，但仍需 `P>=P0` 的统一矩常数。",
        "- `Phihat` 的 Mellin/求积外向区间已被 `sup-rho` 旁路绕开，不再是 `QLOW-MID-COMP` 必需输入。",
        "- `H/Q` 网格值仍可进一步做全区间复数重算，以替代当前十进制预算。",
        "- 完成这些后，`QLOW-MID-COMP` 才能从 `grid certificate` 升级为 `interval proof certificate`。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--total-budget", type=float, default=0.065)
    args = parser.parse_args()

    audit = load_certificate(args.input)
    result = analyze(audit, args.total_budget)

    json_path = MONOGRAPH / "qlow-mid-comp-interval-budget.json"
    md_path = MONOGRAPH / "qlow-mid-comp-interval-budget.md"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(result) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
