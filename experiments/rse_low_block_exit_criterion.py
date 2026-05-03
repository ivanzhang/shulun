#!/usr/bin/env python3
"""低模块预算违例到 OSPC*/CRTDefect 的出口准则。

用法示例：
  python3 experiments/rse_low_block_exit_criterion.py
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_RRD_LOW = MONOGRAPH / "rse-rrd-low-projection-dichotomy.json"
DEFAULT_JSON = MONOGRAPH / "rse-low-block-exit-criterion.json"
DEFAULT_MD = MONOGRAPH / "rse-low-block-exit-criterion.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入文件: {path}")
    return json.loads(path.read_text())


def build_criterion(rrd_low: dict[str, Any], delta_dir: float) -> dict[str, Any]:
    """生成低模块出口的常数准则。"""
    epsilon_low = float(rrd_low["budgets"]["RRD_low"])
    allowed_weighted_crt_defect = epsilon_low / math.sqrt(1.0 + delta_dir)
    return {
        "certificate_type": "rse_low_block_exit_criterion",
        "status": "algebraic_exit_criterion_remaining_crt_weighted_bound",
        "source": str(DEFAULT_RRD_LOW.relative_to(ROOT)),
        "parameters": {
            "epsilon_low": epsilon_low,
            "delta_dir": delta_dir,
            "allowed_weighted_crt_defect": allowed_weighted_crt_defect,
        },
        "criterion": {
            "no_ospc": "for every low block B(q,r), E_dir(B) <= 1+delta_dir",
            "no_crtdefect": "sum_B kappa_B * m_B <= epsilon_low/sqrt(1+delta_dir)",
            "conclusion": "|E_low| <= epsilon_low",
            "contrapositive": "|E_low| > epsilon_low implies OSPC* or weighted CRTDefect",
        },
        "definitions": {
            "m_B": "low-block absolute mass share after same-weight normalization; sum_B m_B <= 1 after block partition",
            "kappa_B": "normalized CRT residue discrepancy of the true rough residual on block B",
            "E_dir_B": "(r-1) sum_a |C_{B,a}|^2 / A_B^2, where A_B is pre-cancellation absolute mass",
            "weighted_CRTDefect": "sum_B kappa_B*m_B",
        },
        "next_obligations": [
            "证明低模字典可分解为有限近正交块，且 Gram 损失并入 RRD-conversion。",
            "证明若某块 E_dir(B)>1+delta_dir，则进入 OSPC* 出口。",
            "证明若加权 CRT 缺陷和超过 allowed_weighted_crt_defect，则进入 CRTDefect/Tail-anchor 出口。",
            "若上述两出口均不发生，则由 Cauchy--Schwarz 得 |E_low|<=epsilon_low。",
        ],
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    params = audit["parameters"]
    lines = [
        "# 低模块预算违例的 OSPC*/CRTDefect 出口准则",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告把上一节的低模二分推进成一个纯代数出口准则：只要无 `OSPC*` 且无加权 `CRTDefect`，就必有 `RRD-low<=0.006`。因此 `RRD-low` 大贡献只能从两个出口之一离开主链。",
        "",
        "## 1. 常数",
        "",
        f"- `epsilon_low={params['epsilon_low']:.6f}`。",
        f"- `delta_dir={params['delta_dir']:.6f}`。",
        f"- 允许的加权 CRT 缺陷：`epsilon_low/sqrt(1+delta_dir)={params['allowed_weighted_crt_defect']:.9f}`。",
        "",
        "本报告默认 `delta_dir=1/4`，因此若无 OSPC，则加权 CRT 缺陷需要控制在约 `0.005367` 以内即可吸收 `RRD-low`。",
        "",
        "## 2. 块级对象",
        "",
        "把低模字典 `D_Z` 分解成有限块 `B=(q,r,s)`，其中 `s` 表示 Buchstab 低层或小模周期类型。令",
        "",
        "\\[",
        "\\Pi_{\\le Z}W=\\sum_B W_B.",
        "\\]",
        "",
        "对每个块，按辅助模 `r` 的非零残基分解",
        "",
        "\\[",
        "C_{B,a}=\\sum_{m\\equiv a\\pmod r} W_B(m),",
        "\\qquad",
        "\\mathcal A_B=\\sum_m |W_B(m)|.",
        "\\]",
        "",
        "定义有向能量",
        "",
        "\\[",
        "E_{\\rm dir}(B)=",
        "{(r-1)\\sum_a |C_{B,a}|^2\\over \\mathcal A_B^2}.",
        "\\]",
        "",
        "再定义真实粗数残差在该块上的 CRT 缺陷强度 `kappa_B`，使得",
        "",
        "\\[",
        "\\left|\\sum_a d_{B,a}C_{B,a}\\right|",
        "\\le",
        "\\kappa_B\\left(\\sum_a |C_{B,a}|^2\\right)^{1/2},",
        "\\]",
        "",
        "其中 `d_{B,a}` 是残基类上的真实粗数残差向量。",
        "",
        "## 3. 出口引理",
        "",
        "若所有低模块都没有 OSPC，即",
        "",
        "\\[",
        "E_{\\rm dir}(B)\\le 1+\\delta_{\\rm dir},",
        "\\]",
        "",
        "则",
        "",
        "\\[",
        "\\left(\\sum_a |C_{B,a}|^2\\right)^{1/2}",
        "\\le",
        "{\\sqrt{1+\\delta_{\\rm dir}}\\over \\sqrt{r-1}}\\mathcal A_B.",
        "\\]",
        "",
        "把 `1/sqrt(r-1)` 吸收到块权 `m_B` 后，得到",
        "",
        "\\[",
        "|\\mathcal E_{\\rm low}|",
        "\\le",
        "\\sqrt{1+\\delta_{\\rm dir}}\\sum_B \\kappa_B m_B.",
        "\\tag{LBE}",
        "\\]",
        "",
        "因此若同时无加权 CRTDefect，即",
        "",
        "\\[",
        "\\sum_B \\kappa_B m_B",
        "\\le",
        "{0.006\\over \\sqrt{1+\\delta_{\\rm dir}}},",
        "\\]",
        "",
        "则 `|E_low|<=0.006`，`RRD-low` 被吸收。",
        "",
        "其逆否命题就是当前需要的出口：",
        "",
        "```text",
        "|E_low| > 0.006",
        "=> 存在低模块 OSPC*",
        "   或 加权 CRTDefect 超过 0.006/sqrt(1+delta_dir)。",
        "```",
        "",
        "## 4. 当前剩余",
        "",
        "本轮已经把 `low-block=>exit` 变成代数准则。真正剩余不再是 Hilbert 投影本身，而是两个定量输入：",
        "",
    ]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines += [
        "",
        "下一步最优攻坚是证明加权 CRT 缺陷和 `sum_B kappa_B m_B <= 0.005367`，或证明一旦它失败就触发已有 `Tail-anchor/CRTDefect` 刚性出口。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rrd-low", type=Path, default=DEFAULT_RRD_LOW)
    parser.add_argument("--delta-dir", type=float, default=0.25)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_criterion(load_json(args.rrd_low), args.delta_dir)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
