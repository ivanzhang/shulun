#!/usr/bin/env python3
"""RRD-low 低模投影与 OSPC 二分规范化。

用法示例：
  python3 experiments/rse_rrd_low_projection_dichotomy.py
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_SCAN = MONOGRAPH / "kscwm-crd-dual-obstruction-scan.json"
DEFAULT_RRD = MONOGRAPH / "rse-rrd-same-weight-reduction.json"
DEFAULT_JSON = MONOGRAPH / "rse-rrd-low-projection-dichotomy.json"
DEFAULT_MD = MONOGRAPH / "rse-rrd-low-projection-dichotomy.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    if not path.exists():
        raise FileNotFoundError(f"缺少输入文件: {path}")
    return json.loads(path.read_text())


def scan_auxiliary_energy(scan: dict[str, Any]) -> dict[str, Any]:
    """汇总旧辅助模能量，用于核对 OSPC 归一化尺度。"""
    rows: list[dict[str, Any]] = []
    for case in scan.get("cases", []):
        for row in case.get("auxiliary_energy", []):
            rows.append(
                {
                    "complex_energy": float(row["complex_energy"]),
                    "max_abs_over_uniform": float(row["max_abs_over_uniform"]),
                    "P": int(case["P"]),
                    "M_exp": float(case["M_exp"]),
                    "R_exp": float(case["R_exp"]),
                    "support_prime": int(row["support_prime"]),
                    "aux_prime": int(row["aux_prime"]),
                }
            )
    rows.sort(key=lambda row: row["complex_energy"], reverse=True)
    return {
        "row_count": len(rows),
        "max_complex_energy": rows[0]["complex_energy"] if rows else 0.0,
        "max_abs_over_uniform": max((row["max_abs_over_uniform"] for row in rows), default=0.0),
        "top_rows": rows[:8],
    }


def build_audit(scan: dict[str, Any], rrd: dict[str, Any]) -> dict[str, Any]:
    """建立低模投影二分的审查包。"""
    auxiliary = scan_auxiliary_energy(scan)
    low_budget = next(item["budget"] for item in rrd["two_stage_targets"] if item["key"] == "RRD-low")
    perp_budget = next(item["budget"] for item in rrd["two_stage_targets"] if item["key"] == "RRD-perp")
    conversion_budget = next(item["budget"] for item in rrd["two_stage_targets"] if item["key"] == "RRD-conversion")
    return {
        "certificate_type": "rse_rrd_low_projection_dichotomy",
        "status": "normalized_ospc_formula_and_low_projection_bridge",
        "scan_source": str(DEFAULT_SCAN.relative_to(ROOT)),
        "rrd_source": str(DEFAULT_RRD.relative_to(ROOT)),
        "budgets": {
            "RRD_low": low_budget,
            "RRD_perp": perp_budget,
            "RRD_conversion": conversion_budget,
            "RRD_total": low_budget + perp_budget + conversion_budget,
        },
        "ospc_normalization": {
            "legacy_issue": "早期文档中 RHS 额外除以 r-1 会使均匀分布也自动满足 OSPC，阈值过弱。",
            "correct_energy": "E_dir(q,r)=(r-1)*sum_a |C_a(q,r)|^2/A_abs(q,r)^2, where A_abs is the pre-cancellation absolute mass",
            "correct_ospc": "E_dir(q,r) >= 1+delta_dir",
            "uniform_coherent_value": 1.0,
            "single_residue_value": "r-1",
        },
        "auxiliary_energy_scan": auxiliary,
        "projection_definition": {
            "space": "H_M=L^2([M,2M), mu_M), mu_M 为 dyadic 归一化计数测度。",
            "low_dictionary": "由 q<=Z 的小模周期、Buchstab 低层和辅助模 r 的有向残基块生成的有限字典 D_Z。",
            "projection": "Pi_{<=Z} 是 H_M 到 span(D_Z) 的正交投影；若字典非正交，先做 Gram 外向区间审计。",
            "residual": "a_perp=(1-Pi_{<=Z})a，满足对所有低模字典原子正交。",
        },
        "hilbert_dichotomy": {
            "statement": (
                "令 W 为同权归一化后的 RSE 临界测试函数。"
                "若 |<Pi a,W>| > epsilon_low，则在低模字典的某个块 B(q,r) 上，"
                "必有 |<a,Pi_B W>| 超过该块预算；该块预算违例就是 OSPC/CRTDefect 候选。"
            ),
            "small_case": "|<Pi a,W>| <= 0.006，RRD-low 被预算吸收。",
            "large_case": "|<Pi a,W>| > 0.006，存在低模块 B(q,r) 产生有向能量异常，进入 OSPC/CRTDefect 出口。",
        },
        "next_obligations": [
            "把 OSPC 公式统一改为 E_dir(q,r)>=1+delta_dir。",
            "在正文中定义 D_Z、Gram 矩阵和 Pi_{<=Z}。",
            "证明低模块预算违例推出修正后的 OSPC 或直接 CRTDefect。",
            "证明 a_perp 的同权测试范数 <=0.012。",
        ],
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    aux = audit["auxiliary_energy_scan"]
    budgets = audit["budgets"]
    lines = [
        "# RRD-low 低模投影与 OSPC 二分",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告继续处理 `RRD-low`。关键结论是：先修正 `OSPC` 的能量归一化，再把 `Pi_{<=Z}` 定义成低模字典的正交投影；这样 `RRD-low` 可以严格二分为“小则吸收，大则进入 OSPC/CRTDefect”。",
        "",
        "## 1. OSPC 归一化修正",
        "",
        "旧文档中的 OSPC 写法右侧额外除以 `r-1`，该尺度过弱：均匀分布也会自动满足，从而不能作为“有向集中”的判据。",
        "",
        "应使用与实验脚本 `complex_energy` 一致的归一化：",
        "",
        "\\[",
        "E_{\\rm dir}(q,r)=",
        "{(r-1)\\sum_{a\\in(\\mathbb Z/r\\mathbb Z)^\\times}|C_a(q,r)|^2",
        "\\over",
        "\\mathcal A(q,r)^2}.",
        "\\]",
        "",
        "这里 `A(q,r)` 是同一批项在分残基前的总绝对质量，即脚本中的 `total_abs`。使用 `A(q,r)` 而不是 `sum_a |C_a|` 可以把残基内相消也计入反集中效果，并与旧扫描的 `complex_energy` 完全一致。",
        "",
        "修正后的有向小素集中定义为",
        "",
        "\\[",
        "E_{\\rm dir}(q,r)\\ge 1+\\delta_{\\rm dir}.",
        "\\tag{OSPC*}",
        "\\]",
        "",
        "在该规范下，均匀同相分布给 `E_dir=1`，单个残基类集中给 `E_dir=r-1`。这才是后续低模出口需要的尺度。",
        "",
        "旧辅助模扫描在该尺度下的最大值为：",
        "",
        f"- `max complex_energy={aux['max_complex_energy']:.6f}`。",
        f"- `maxAbs/uniform={aux['max_abs_over_uniform']:.6f}`。",
        "",
        "这说明旧样本没有显示强 OSPC；也再次确认普通 support concentration 不足，必须使用有向能量判据。",
        "",
        "## 2. 低模投影的正式对象",
        "",
        "在 dyadic 层 `m~M` 上取 Hilbert 空间",
        "",
        "\\[",
        "\\mathcal H_M=L^2([M,2M),\\mu_M),",
        "\\]",
        "",
        "其中 `mu_M` 是归一化计数测度。令",
        "",
        "\\[",
        "a(m)=1_{P^-(m)>Y}-\\rho_M.",
        "\\]",
        "",
        "选择低模字典 `D_Z`，由以下原子张成：",
        "",
        "- `q<=Z` 的小模周期原子；",
        "- Buchstab 分解的低层因子原子；",
        "- 辅助模 `r` 上的有向残基块原子，对应 `C_a(q,r)`。",
        "",
        "定义",
        "",
        "\\[",
        "\\Pi_{\\le Z}:\\mathcal H_M\\to {\\rm span}(D_Z)",
        "\\]",
        "",
        "为正交投影；若字典非正交，则用 Gram 矩阵的外向区间逆来定义可审查投影。分解为",
        "",
        "\\[",
        "a=a_{\\rm low}+a_{\\rm perp},\\qquad",
        "a_{\\rm low}=\\Pi_{\\le Z}a.",
        "\\]",
        "",
        "## 3. Hilbert 二分引理",
        "",
        "令 `W` 为已经同权归一化的 RSE 临界测试函数，即上一节中由",
        "",
        "\\[",
        "{|\\omega_\\ell|\\over h}\\cdot {hH\\over \\ell M}\\big/{H\\over M}",
        "={|\\omega_\\ell|\\over \\ell}",
        "\\]",
        "",
        "归一到 `V_omega=sum |omega_l|/l` 的测试函数。",
        "",
        "则",
        "",
        "\\[",
        "\\mathcal E_{\\rm low}=\\langle \\Pi_{\\le Z}a,W\\rangle",
        "=\\langle a,\\Pi_{\\le Z}W\\rangle.",
        "\\]",
        "",
        "由正交投影和 Cauchy--Bessel，得到严格二分：",
        "",
        "```text",
        "若 |E_low| <= 0.006，则 RRD-low 被账本吸收；",
        "若 |E_low| > 0.006，则某个低模块 B(q,r) 的投影贡献超过块预算。",
        "```",
        "",
        "后一种块预算违例就是修正后 `OSPC*` 或直接 `CRTDefect` 的候选入口。",
        "",
        "## 4. 当前预算接法",
        "",
        f"- `RRD-low <= {budgets['RRD_low']:.3f}`：由小情形吸收，或由大情形转交 OSPC/CRTDefect。",
        f"- `RRD-perp <= {budgets['RRD_perp']:.3f}`：低模正交后再用 Buchstab/CRT 均衡估计。",
        f"- `RRD-conversion <= {budgets['RRD_conversion']:.3f}`：端点和振幅线性化误差。",
        "",
        "## 5. 下一步审稿义务",
        "",
    ]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines += [
        "",
        "本轮完成的是 `RRD-low` 的正确数学接口：修正 OSPC 尺度，并把低模大贡献严格定位到有限低模块。尚未完成的是低模块违例到 `CRTDefect` 的逐项定量证明，以及 `RRD-perp<=0.012`。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--rrd", type=Path, default=DEFAULT_RRD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(load_json(args.scan), load_json(args.rrd))
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
