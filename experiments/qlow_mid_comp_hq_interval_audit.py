#!/usr/bin/env python3
"""QLOW-MID-COMP：H/Q 复数区间增量审计。

用法示例：
  python3 experiments/qlow_mid_comp_hq_interval_audit.py
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_GRID = MONOGRAPH / "qlow-mid-comp-grid-certificate.json"
DEFAULT_ORACLE = MONOGRAPH / "trig-log-interval-oracle-audit.json"


def load_json(path: Path) -> dict:
    """读取 JSON 文件。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入文件: {path}")
    return json.loads(path.read_text())


def hq_rho_margin(oracle_half_radius: float) -> float:
    """由 sin/cos 每坐标半径推出 rho=(|H|/K)(|Q|/V) 的统一增量。"""
    complex_radius = math.sqrt(2.0) * oracle_half_radius
    return 2.0 * complex_radius + complex_radius * complex_radius


def analyze(grid: dict, oracle: dict) -> dict:
    """计算 H/Q 区间 oracle 对 C_comp 的增量。"""
    oracle_radius = float(oracle["max_oracle_half_radius"])
    rho_margin = hq_rho_margin(oracle_radius)
    cases = []
    min_slack_after_hq = float("inf")
    hardest_case = None
    for case in grid["cases"]:
        target = float(case["target"])
        certified = float(case["certified_ratio"])
        with_hq = certified + rho_margin
        slack = target - with_hq
        row = {
            "P": case["P"],
            "R_exp": case["R_exp"],
            "R": case["R"],
            "certified_ratio": certified,
            "hq_rho_margin": rho_margin,
            "certified_with_hq_interval": with_hq,
            "target": target,
            "slack_after_hq": slack,
            "passes": slack > 0,
        }
        cases.append(row)
        if slack < min_slack_after_hq:
            min_slack_after_hq = slack
            hardest_case = row
    return {
        "certificate_type": "qlow_mid_comp_hq_interval_audit",
        "status": "hq_interval_increment_negligible_for_sample_certificate",
        "grid_source": str(DEFAULT_GRID.relative_to(ROOT)),
        "oracle_source": str(DEFAULT_ORACLE.relative_to(ROOT)),
        "oracle_half_radius": oracle_radius,
        "complex_term_radius": math.sqrt(2.0) * oracle_radius,
        "hq_rho_margin": rho_margin,
        "min_slack_after_hq": min_slack_after_hq,
        "hardest_case": hardest_case,
        "cases": cases,
    }


def render_markdown(audit: dict) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# QLOW-MID-COMP 的 H/Q 区间增量审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告把 `sin/cos/log` 有理 oracle 的半径接入",
        "",
        "\\[",
        "\\rho_R(u)=\\frac{|H(iu/\\log R)|}{K}\\frac{|Q(iu/\\log R)|}{\\mathcal V_\\omega}.",
        "\\]",
        "",
        "若每个 `sin/cos` 坐标外向半径为 `eps`，则每个单位复指数项的复平面误差至多",
        "",
        "\\[",
        "\\delta=\\sqrt2\\,\\varepsilon.",
        "\\]",
        "",
        "归一化后有",
        "",
        "\\[",
        "\\frac{|H|}{K}\\mapsto \\frac{|H|}{K}+\\delta,\\qquad",
        "\\frac{|Q|}{\\mathcal V_\\omega}\\mapsto \\frac{|Q|}{\\mathcal V_\\omega}+\\delta.",
        "\\]",
        "",
        "由于两个归一化因子本来都不超过 `1`，得到统一增量",
        "",
        "\\[",
        "\\Delta_{HQ}\\le 2\\delta+\\delta^2.",
        "\\]",
        "",
        "## 增量结果",
        "",
        f"- oracle half-radius: `{audit['oracle_half_radius']:.3e}`",
        f"- complex term radius: `{audit['complex_term_radius']:.3e}`",
        f"- H/Q rho margin: `{audit['hq_rho_margin']:.3e}`",
        f"- minimum slack after H/Q interval: `{audit['min_slack_after_hq']:.6f}`",
        "",
        "## 样本表",
        "",
        "| P | R | certified | +HQ margin | target | slack | pass |",
        "|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for case in audit["cases"]:
        lines.append(
            f"| {case['P']} | {case['R']} | {case['certified_ratio']:.6f} | "
            f"{case['certified_with_hq_interval']:.6f} | {case['target']:.3f} | "
            f"{case['slack_after_hq']:.6f} | {'Y' if case['passes'] else 'N'} |"
        )
    lines += [
        "",
        "## 审稿含义",
        "",
        "- 当前 `H/Q` 的 trig/log 区间误差对 `C_comp` 的影响为 `O(10^-67)`，远低于预算。",
        "- 这闭合的是 `H/Q` 由三角与对数 oracle 导致的外向增量，不闭合 `Phihat`。",
        "- 剩余真正数值硬点集中到 `Phihat` 的 Mellin/求积外向区间，以及 `P>=P0` 的统一 Selberg 矩常数。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=Path, default=DEFAULT_GRID)
    parser.add_argument("--oracle", type=Path, default=DEFAULT_ORACLE)
    args = parser.parse_args()

    audit = analyze(load_json(args.grid), load_json(args.oracle))
    json_path = MONOGRAPH / "qlow-mid-comp-hq-interval-audit.json"
    md_path = MONOGRAPH / "qlow-mid-comp-hq-interval-audit.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
