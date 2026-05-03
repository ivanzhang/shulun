#!/usr/bin/env python3
"""BPN-PDEC 线性对偶证书审计。

用法示例：
  python3 experiments/prime_matrix_bpn_pdec_dual_certificate_audit.py
  python3 experiments/prime_matrix_bpn_pdec_dual_certificate_audit.py --input docs/pdec-dual-cert.json

输入 JSON 格式示例：
{
  "q": 12,
  "kappa": 1.0,
  "f_l2": 100.0,
  "s_size": 12,
  "inequalities": [
    {"name": "mass_cap", "coeffs": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "bound": 12}
  ],
  "equalities": [
    {"name": "phase_0", "coeffs": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "value": 1}
  ],
  "certificates": [
    {
      "name": "h1_dir0",
      "frequency": 1,
      "direction": {"real": 1.0, "imag": 0.0},
      "lambda": [0.0],
      "mu": [1.0],
      "claimed_u_crt": 0.0
    }
  ]
}
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def unit_vector(index: int, length: int) -> list[float]:
    """生成标准基向量。"""
    return [1.0 if pos == index else 0.0 for pos in range(length)]


def target_vector(q: int, frequency: int, direction: complex) -> list[float]:
    """生成 Re{zeta exp(2pi i h t / Q)} 目标向量。"""
    return [
        (direction * cmath.exp(2j * math.pi * frequency * t / q)).real
        for t in range(q)
    ]


def default_certificate() -> dict[str, Any]:
    """生成一个演示用对偶证书。

    该示例用每个相位 g(t)=1 的等式约束精确主控 h=1 的实方向。
    这是格式证明，不代表实际 BPN 无限族约束已闭合。
    """
    q = 12
    frequency = 1
    direction = complex(1.0, 0.0)
    target = target_vector(q, frequency, direction)
    return {
        "q": q,
        "kappa": 1.0,
        "f_l2": 100.0,
        "s_size": float(q),
        "inequalities": [
            {
                "name": "mass_cap",
                "source": "演示总质量上界",
                "coeffs": [1.0] * q,
                "bound": float(q),
            }
        ],
        "equalities": [
            {
                "name": f"phase_{index}",
                "source": "演示相位等式",
                "coeffs": unit_vector(index, q),
                "value": 1.0,
            }
            for index in range(q)
        ],
        "certificates": [
            {
                "name": "demo_h1_real_direction",
                "frequency": frequency,
                "direction": {"real": direction.real, "imag": direction.imag},
                "lambda": [0.0],
                "mu": target,
                "claimed_u_crt": 1e-12,
            }
        ],
        "description": "演示证书：用完整相位等式精确主控一个 Fourier 方向。",
    }


def parse_rows(rows: list[dict[str, Any]], q: int, bound_key: str) -> list[dict[str, Any]]:
    """解析线性约束行。"""
    parsed = []
    for row in rows:
        coeffs = [float(value) for value in row["coeffs"]]
        if len(coeffs) != q:
            raise ValueError(f"{row.get('name', 'row')} 的 coeffs 长度必须等于 q")
        parsed.append(
            {
                "name": row.get("name", ""),
                "source": row.get("source", ""),
                "coeffs": coeffs,
                bound_key: float(row[bound_key]),
            }
        )
    return parsed


def dot(left: list[float], right: list[float]) -> float:
    """计算内积。"""
    return sum(a * b for a, b in zip(left, right))


def audit_single_certificate(
    q: int,
    inequalities: list[dict[str, Any]],
    equalities: list[dict[str, Any]],
    lower: float,
    certificate: dict[str, Any],
    tolerance: float,
) -> dict[str, Any]:
    """审计单个频率方向的对偶证书。"""
    frequency = int(certificate["frequency"])
    if not 1 <= frequency < q:
        raise ValueError("frequency 必须满足 1<=h<Q")

    direction_data = certificate["direction"]
    direction = complex(float(direction_data["real"]), float(direction_data["imag"]))
    direction_abs = abs(direction)
    if direction_abs <= 0:
        raise ValueError("direction 不能为零")
    direction /= direction_abs

    lambdas = [float(value) for value in certificate.get("lambda", [])]
    mus = [float(value) for value in certificate.get("mu", [])]
    if len(lambdas) != len(inequalities):
        raise ValueError("lambda 长度必须等于 inequalities 数量")
    if len(mus) != len(equalities):
        raise ValueError("mu 长度必须等于 equalities 数量")
    if any(value < -tolerance for value in lambdas):
        raise ValueError("不等式对偶权重 lambda 必须非负")

    target = target_vector(q, frequency, direction)
    rhs = []
    min_slack = math.inf
    worst_phase = None
    for phase in range(q):
        value = 0.0
        for weight, row in zip(lambdas, inequalities):
            value += weight * row["coeffs"][phase]
        for weight, row in zip(mus, equalities):
            value += weight * row["coeffs"][phase]
        rhs.append(value)
        slack = value - target[phase]
        if slack < min_slack:
            min_slack = slack
            worst_phase = phase

    pointwise_pass = min_slack >= -tolerance
    dual_bound = sum(
        weight * row["bound"] for weight, row in zip(lambdas, inequalities)
    ) + sum(weight * row["value"] for weight, row in zip(mus, equalities))
    claimed = certificate.get("claimed_u_crt")
    claimed_u = None if claimed is None else float(claimed)
    # Fourier 模的上界必须非负；对偶和可能因浮点舍入出现极小负数。
    effective_u = max(0.0, dual_bound) if claimed_u is None else max(0.0, dual_bound, claimed_u)

    return {
        "name": certificate.get("name", ""),
        "frequency": frequency,
        "direction_real": direction.real,
        "direction_imag": direction.imag,
        "pointwise_pass": pointwise_pass,
        "min_slack": min_slack,
        "worst_phase": worst_phase,
        "dual_bound": dual_bound,
        "claimed_u_crt": claimed_u,
        "effective_u_crt": effective_u,
        "l_pdec": lower,
        "strict_margin": lower - effective_u,
        "certificate_pass": pointwise_pass and effective_u < lower,
    }


def audit_certificate(config: dict[str, Any]) -> dict[str, Any]:
    """审计 PDEC 对偶证书包。"""
    q = int(config["q"])
    if q <= 1:
        raise ValueError("q 必须大于 1")
    s_size = float(config["s_size"])
    kappa = float(config["kappa"])
    f_l2 = float(config["f_l2"])
    if s_size <= 0 or kappa <= 0 or f_l2 <= 0:
        raise ValueError("s_size, kappa, f_l2 必须为正")

    lower = kappa * s_size / (math.sqrt(q - 1) * f_l2)
    inequalities = parse_rows(config.get("inequalities", []), q, "bound")
    equalities = parse_rows(config.get("equalities", []), q, "value")
    certificates = config.get("certificates", [])
    tolerance = float(config.get("tolerance", 1e-9))
    if not certificates:
        raise ValueError("必须至少提供一个 certificate")

    certificate_reports = [
        audit_single_certificate(q, inequalities, equalities, lower, item, tolerance)
        for item in certificates
    ]
    all_pass = all(item["certificate_pass"] for item in certificate_reports)
    worst_margin = min(item["strict_margin"] for item in certificate_reports)
    worst_slack = min(item["min_slack"] for item in certificate_reports)

    return {
        "certificate_type": "prime_matrix_bpn_pdec_dual_certificate_audit",
        "status": "pdec_dual_certificate_checked",
        "q": q,
        "s_size": s_size,
        "kappa": kappa,
        "f_l2": f_l2,
        "l_pdec": lower,
        "num_inequalities": len(inequalities),
        "num_equalities": len(equalities),
        "num_certificates": len(certificate_reports),
        "all_certificates_pass": all_pass,
        "worst_strict_margin": worst_margin,
        "worst_pointwise_slack": worst_slack,
        "certificate_reports": certificate_reports,
        "review_conclusion": (
            "该审计验证 PDEC-Dual-Cert 的线性对偶不等式。若 all_pass=true，"
            "则输入证书覆盖的频率方向满足 U_CRT<L_PDEC；若要闭合无限族，"
            "还必须证明这些约束确实由边界零行结构产生，并覆盖所有 h 与方向。"
        ),
    }


def write_markdown(audit: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# BPN-PDEC 对偶证书审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["review_conclusion"],
        "",
        "## 1. 输入摘要",
        "",
        f"- `Q={audit['q']}`，`|S|={audit['s_size']}`。",
        f"- `L_PDEC={audit['l_pdec']:.12g}`。",
        f"- 不等式 `{audit['num_inequalities']}` 条，等式 `{audit['num_equalities']}` 条。",
        f"- 方向证书 `{audit['num_certificates']}` 个。",
        f"- `all_certificates_pass={audit['all_certificates_pass']}`。",
        f"- 最小严格余量 `{audit['worst_strict_margin']:.12g}`。",
        f"- 最小逐相位 slack `{audit['worst_pointwise_slack']:.12g}`。",
        "",
        "## 2. 方向证书表",
        "",
        "| name | h | pointwise | U_CRT | margin | worst phase | min slack | pass |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in audit["certificate_reports"]:
        lines.append(
            "| {name} | {h} | {pointwise} | {u:.12g} | {margin:.12g} | {phase} | {slack:.12g} | {passed} |".format(
                name=row["name"],
                h=row["frequency"],
                pointwise=row["pointwise_pass"],
                u=row["effective_u_crt"],
                margin=row["strict_margin"],
                phase=row["worst_phase"],
                slack=row["min_slack"],
                passed=row["certificate_pass"],
            )
        )
    lines.extend(
        [
            "",
            "## 3. 审稿含义",
            "",
            "该报告只证明输入线性系统下的对偶上界。正式稿仍必须逐条证明 `inequalities` 与",
            "`equalities` 来自 mirror、column、tail-anchor、core-overlap 与 Rankin routing 等结构约束。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="PDEC 对偶证书 JSON 输入")
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-pdec-dual-certificate-audit.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-pdec-dual-certificate-audit.md",
    )
    args = parser.parse_args()

    config = (
        json.loads(args.input.read_text(encoding="utf-8"))
        if args.input
        else default_certificate()
    )
    audit = audit_certificate(config)
    args.json_output.write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, args.md_output)
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
