#!/usr/bin/env python3
"""BPN-PDEC Fourier 上界证书审计。

用法示例：
  python3 experiments/prime_matrix_bpn_pdec_certificate_audit.py
  python3 experiments/prime_matrix_bpn_pdec_certificate_audit.py --input docs/pdec-cert.json

输入 JSON 可选格式：
{
  "q": 12,
  "kappa": 1.0,
  "f_l2": 100.0,
  "counts": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  "claimed_u_crt": 0.01
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


def default_certificate() -> dict[str, Any]:
    """生成一个格式演示用的显式 PDEC 证书。"""
    q = 12
    counts = [1] * q
    return {
        "q": q,
        "kappa": 1.0,
        "f_l2": 100.0,
        "counts": counts,
        "claimed_u_crt": 0.01,
        "description": "演示证书：均匀坏窗计数向量给出近零非零 Fourier 系数。",
    }


def dft_nonzero(counts: list[float]) -> list[dict[str, float]]:
    """计算非零 Fourier 系数的模。"""
    q = len(counts)
    rows: list[dict[str, float]] = []
    for h in range(1, q):
        value = sum(
            count * cmath.exp(2j * math.pi * h * t / q)
            for t, count in enumerate(counts)
        )
        rows.append(
            {
                "h": h,
                "real": value.real,
                "imag": value.imag,
                "abs": abs(value),
            }
        )
    return rows


def audit_certificate(config: dict[str, Any]) -> dict[str, Any]:
    """审计显式 PDEC 证书。"""
    q = int(config["q"])
    counts = [float(value) for value in config["counts"]]
    if len(counts) != q:
        raise ValueError("counts 长度必须等于 q")
    if any(value < 0 for value in counts):
        raise ValueError("counts 必须非负")

    kappa = float(config["kappa"])
    f_l2 = float(config["f_l2"])
    if kappa <= 0 or f_l2 <= 0:
        raise ValueError("kappa 与 f_l2 必须为正")

    s_size = sum(counts)
    lower = kappa * s_size / (math.sqrt(q - 1) * f_l2)
    rows = dft_nonzero(counts)
    max_row = max(rows, key=lambda row: row["abs"]) if rows else {
        "h": None,
        "real": 0.0,
        "imag": 0.0,
        "abs": 0.0,
    }
    exact_u = float(max_row["abs"])
    claimed_u = config.get("claimed_u_crt")
    claimed_u_float = None if claimed_u is None else float(claimed_u)
    effective_u = exact_u if claimed_u_float is None else max(exact_u, claimed_u_float)

    return {
        "certificate_type": "prime_matrix_bpn_pdec_certificate_audit",
        "status": "explicit_pdec_certificate_checked",
        "q": q,
        "s_size": s_size,
        "kappa": kappa,
        "f_l2": f_l2,
        "l_pdec": lower,
        "exact_max_nonzero_fourier": exact_u,
        "max_frequency_row": max_row,
        "claimed_u_crt": claimed_u_float,
        "effective_u_crt": effective_u,
        "pdec_certificate_pass": effective_u < lower,
        "top_frequencies": sorted(rows, key=lambda row: row["abs"], reverse=True)[:10],
        "review_conclusion": (
            "该审计只验证显式 count vector 的 PDEC 上界。若 pass=false，说明该计数向量"
            "不能排除 persistent 分支；若 pass=true，则该具体坏窗相位计数与 PDEC 下界矛盾。"
            "无限族仍需对偶证书或结构约束生成器。"
        ),
    }


def write_markdown(audit: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# BPN-PDEC Fourier 证书审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["review_conclusion"],
        "",
        "## 1. 输入与阈值",
        "",
        f"- `Q={audit['q']}`，`|S|={audit['s_size']}`。",
        f"- `kappa={audit['kappa']}`，`||F||_2={audit['f_l2']}`。",
        f"- `L_PDEC={audit['l_pdec']:.12g}`。",
        f"- `exact max nonzero Fourier={audit['exact_max_nonzero_fourier']:.12g}`。",
        f"- `effective U_CRT={audit['effective_u_crt']:.12g}`。",
        f"- `pdec_certificate_pass={audit['pdec_certificate_pass']}`。",
        "",
        "## 2. 最大频率",
        "",
        "| h | real | imag | abs |",
        "| ---: | ---: | ---: | ---: |",
    ]
    row = audit["max_frequency_row"]
    lines.append(
        f"| {row['h']} | {row['real']:.12g} | {row['imag']:.12g} | {row['abs']:.12g} |"
    )
    lines.extend(
        [
            "",
            "## 3. 前十个频率",
            "",
            "| h | abs |",
            "| ---: | ---: |",
        ]
    )
    for freq in audit["top_frequencies"]:
        lines.append(f"| {freq['h']} | {freq['abs']:.12g} |")
    lines.extend(
        [
            "",
            "## 4. 审稿含义",
            "",
            "该报告是 `PDEC-Explicit-Cert` 的机器可核验层。正式证明若要覆盖无限族，仍需",
            "`prime-matrix-bpn-pdec-dual-certificate-framework.md` 中的对偶证书或解析主控证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="PDEC 证书 JSON 输入")
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-pdec-certificate-audit.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-pdec-certificate-audit.md",
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
