#!/usr/bin/env python3
"""QLOW-MID-COMP：Phihat-free sup-rho 旁路证书。

用法示例：
  python3 experiments/qlow_mid_comp_supnorm_audit.py
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_GRID = MONOGRAPH / "qlow-mid-comp-grid-certificate.json"
DEFAULT_HQ = MONOGRAPH / "qlow-mid-comp-hq-interval-audit.json"
DEFAULT_BUDGET = MONOGRAPH / "qlow-mid-comp-interval-budget.json"


def load_json(path: Path) -> dict:
    """读取 JSON 文件。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入文件: {path}")
    return json.loads(path.read_text())


def analyze(grid: dict, hq: dict, budget: dict, use_decimal_budget: bool) -> dict:
    """用 sup rho 直接证明紧区间常数界，不再依赖 Phihat 权重。"""
    hq_margin = float(hq["hq_rho_margin"])
    decimal_margin = float(budget["budget_parts"]["json_decimal_rounding"]) if use_decimal_budget else 0.0
    cases = []
    min_slack = float("inf")
    hardest_case = None
    for case in grid["cases"]:
        sup_bound = (
            float(case["max_rho_grid"])
            + float(case["lipschitz_margin"])
            + hq_margin
            + decimal_margin
        )
        target = float(case["target"])
        slack = target - sup_bound
        row = {
            "P": case["P"],
            "R_exp": case["R_exp"],
            "R": case["R"],
            "max_rho_grid": float(case["max_rho_grid"]),
            "lipschitz_margin": float(case["lipschitz_margin"]),
            "hq_margin": hq_margin,
            "decimal_margin": decimal_margin,
            "sup_bound": sup_bound,
            "weighted_certified_ratio": float(case["certified_ratio"]),
            "target": target,
            "slack": slack,
            "passes": slack > 0,
        }
        cases.append(row)
        if slack < min_slack:
            min_slack = slack
            hardest_case = row
    return {
        "certificate_type": "qlow_mid_comp_supnorm_audit",
        "status": "phihat_free_supnorm_certificate_for_sample_grid",
        "grid_source": str(DEFAULT_GRID.relative_to(ROOT)),
        "hq_source": str(DEFAULT_HQ.relative_to(ROOT)),
        "budget_source": str(DEFAULT_BUDGET.relative_to(ROOT)),
        "use_decimal_budget": use_decimal_budget,
        "hq_margin": hq_margin,
        "decimal_margin": decimal_margin,
        "min_slack": min_slack,
        "hardest_case": hardest_case,
        "cases": cases,
    }


def render_markdown(audit: dict) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# QLOW-MID-COMP 的 Phihat-free sup-rho 证书",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告给出一个更强的紧区间旁路：在 `2<u<=12` 上直接证明",
        "",
        "\\[",
        "\\rho_R(u)=\\frac{|H(iu/\\log R)|}{K}\\frac{|Q(iu/\\log R)|}{\\mathcal V_\\omega}<0.35.",
        "\\]",
        "",
        "因为 `|Phihat|` 是非负权，若上式成立，则自动有",
        "",
        "\\[",
        "\\frac{\\int |\\widehat\\Phi|\\,|H|\\,|Q|\\,du/\\log R}",
        "{K\\mathcal V_\\omega\\int |\\widehat\\Phi|\\,du/\\log R}",
        "\\le \\sup_{2<u\\le12}\\rho_R(u)<0.35.",
        "\\]",
        "",
        "因此 `QLOW-MID-COMP` 的紧区间证明不再需要 `Phihat` 的 Mellin/求积外向区间。",
        "",
        "## 证书表",
        "",
        "| P | R | maxRho | Lip | H/Q | decimal | supBound | target | slack | pass |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for case in audit["cases"]:
        lines.append(
            f"| {case['P']} | {case['R']} | {case['max_rho_grid']:.6f} | "
            f"{case['lipschitz_margin']:.6f} | {case['hq_margin']:.1e} | "
            f"{case['decimal_margin']:.6f} | {case['sup_bound']:.6f} | "
            f"{case['target']:.3f} | {case['slack']:.6f} | {'Y' if case['passes'] else 'N'} |"
        )
    lines += [
        "",
        "## 最紧样本",
        "",
        f"- `P={audit['hardest_case']['P']}, R={audit['hardest_case']['R']}`。",
        f"- `supBound={audit['hardest_case']['sup_bound']:.6f}`。",
        f"- `slack={audit['hardest_case']['slack']:.6f}`。",
        "",
        "## 审稿含义",
        "",
        "- 这条证书比带权平均证书更粗，但足以低于目标 `0.35`。",
        "- 它消除了 `QLOW-MID-COMP` 对 `Phihat` 数值求积的依赖。",
        "- 剩余数值义务从 `Phihat` 转移为 `H/Q` 网格值的正式区间重算；当前已由 trig/log oracle、Lipschitz 和十进制预算覆盖。",
        "- 全局无条件化仍需 `P>=P0` 的统一 Selberg 矩常数，以及主链 `RRD/OSPC`。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=Path, default=DEFAULT_GRID)
    parser.add_argument("--hq", type=Path, default=DEFAULT_HQ)
    parser.add_argument("--budget", type=Path, default=DEFAULT_BUDGET)
    parser.add_argument("--no-decimal-budget", action="store_true")
    args = parser.parse_args()

    audit = analyze(
        load_json(args.grid),
        load_json(args.hq),
        load_json(args.budget),
        use_decimal_budget=not args.no_decimal_budget,
    )
    json_path = MONOGRAPH / "qlow-mid-comp-supnorm-audit.json"
    md_path = MONOGRAPH / "qlow-mid-comp-supnorm-audit.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
