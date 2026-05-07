#!/usr/bin/env python3
"""生成 SN3-E 高频列相位 Bohr-cap 证书。

用法示例：
  python3 experiments/prime_matrix_sn3e_highfreq_bohrcap_certificate.py \
    --sn3 docs/sn3_distributed_band_projection_audit_20260506.json \
    --sn3c docs/sn3c_multiband_sync_audit_20260506.json \
    --sn3d docs/sn3d_kls_multishell_frequency_audit_20260506.json \
    --alpha-list 0.0,0.25,0.5 \
    --out-prefix docs/sn3e_highfreq_bohrcap_certificate_20260506

目标：
  对 SN3-D 的高频列相位证书，计算对应 Bohr-cap 中的正/负 Jordan 质量。
  这是确定性频率局部化账本，不是最终排斥证明。
"""

from __future__ import annotations

import argparse
import cmath
import importlib.util
import json
import math
from pathlib import Path


def load_module(name: str, filename: str):
    """从 experiments 目录加载模块。"""
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sn2 = load_module("sn2_band_audit", "prime_matrix_sn2_band_structure_audit.py")
sn3d = load_module("sn3d_frequency_audit", "prime_matrix_sn3d_kls_multishell_frequency_audit.py")


def parse_floats(raw: str) -> list[float]:
    """解析逗号分隔浮点数。"""
    return [float(item) for item in raw.split(",") if item.strip()]


def rebuild_residual(sn3_data: dict, sn3c_row: dict) -> dict:
    """复用 SN3-D 逻辑重构 residual。"""
    params = sn3_data["parameters"]
    p = int(sn3c_row["p"])
    y = int(sn3c_row["y"])
    alpha = float(params["alpha"])
    tail_factor = float(params["tail_factor"])
    flags = sn2.sieve_bool(max(params["p_list"]))
    prefix = sn2.prime_prefix(flags)
    primes = sn2.primes_from_flags(flags)
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_limit = (p * y * 8 - 1) // tail_q_min
    rough = sn2.rough_flags(m_limit, low_primes)
    bands = sorted({band["band"] for band in sn3c_row["bands"]})
    return sn3d.residual_by_d(
        p,
        y,
        bands,
        cutoff,
        tail_factor,
        rough,
        prefix,
        primes,
    )


def bohr_certificate(residual: list[float], h: int, alpha: float) -> dict:
    """计算一个频率和阈值的 Bohr-cap Jordan 账本。"""
    p = len(residual)
    fourier = 0j
    positive_total = 0.0
    negative_total = 0.0
    for d in range(1, p):
        value = residual[d]
        if value >= 0:
            positive_total += value
        else:
            negative_total += -value
        fourier += value * cmath.exp(-2j * math.pi * h * d / p)

    if abs(fourier) == 0:
        phase = 1 + 0j
    else:
        phase = fourier.conjugate() / abs(fourier)

    positive_cap = 0.0
    negative_anticap = 0.0
    positive_cap_count = 0
    negative_anticap_count = 0
    cap_count = 0
    anticap_count = 0
    for d in range(1, p):
        angle_value = (phase * cmath.exp(-2j * math.pi * h * d / p)).real
        if angle_value >= alpha:
            cap_count += 1
            if residual[d] > 0:
                positive_cap += residual[d]
                positive_cap_count += 1
        if angle_value <= -alpha:
            anticap_count += 1
            if residual[d] < 0:
                negative_anticap += -residual[d]
                negative_anticap_count += 1

    variation = positive_total + negative_total
    lower_bound = 0.0
    if alpha < 1:
        lower_bound = max(0.0, (abs(fourier) - alpha * variation) / (1.0 - alpha))
    captured = positive_cap + negative_anticap
    return {
        "alpha": alpha,
        "h": h,
        "fourier_abs": abs(fourier),
        "positive_total": positive_total,
        "negative_total": negative_total,
        "variation": variation,
        "cap_count": cap_count,
        "anticap_count": anticap_count,
        "positive_cap": positive_cap,
        "negative_anticap": negative_anticap,
        "positive_cap_count": positive_cap_count,
        "negative_anticap_count": negative_anticap_count,
        "captured_jordan_mass": captured,
        "captured_over_variation": captured / variation if variation > 0 else 0.0,
        "positive_cap_over_positive": (
            positive_cap / positive_total if positive_total > 0 else 0.0
        ),
        "negative_anticap_over_negative": (
            negative_anticap / negative_total if negative_total > 0 else 0.0
        ),
        "jordan_lower_bound": lower_bound,
        "lower_bound_over_variation": lower_bound / variation if variation > 0 else 0.0,
    }


def build_report(sn3_data: dict, sn3c_data: dict, sn3d_data: dict, alpha_list: list[float]) -> dict:
    """构造 Bohr-cap 证书报告。"""
    sn3c_by_key = {(int(row["p"]), int(row["y"])): row for row in sn3c_data["rows"]}
    records = []
    for row in sn3d_data["records"]:
        key = (int(row["p"]), int(row["y"]))
        residual_info = rebuild_residual(sn3_data, sn3c_by_key[key])
        residual = residual_info["residual"]
        h = int(row["top_frequencies"][0]["h"])
        certs = [bohr_certificate(residual, h, alpha) for alpha in alpha_list]
        records.append(
            {
                "p": row["p"],
                "y": row["y"],
                "bands": row["bands"],
                "top_h": h,
                "excess": row["excess"],
                "top_frequency_abs_over_excess": row["top_frequency_abs_over_excess"],
                "flatness": row["flatness"],
                "certificates": certs,
            }
        )

    return {
        "parameters": {"alpha_list": alpha_list},
        "summary": {
            "record_count": len(records),
            "max_positive_cap_over_positive": max(
                (
                    cert["positive_cap_over_positive"]
                    for row in records
                    for cert in row["certificates"]
                ),
                default=0.0,
            ),
            "max_captured_over_variation": max(
                (
                    cert["captured_over_variation"]
                    for row in records
                    for cert in row["certificates"]
                ),
                default=0.0,
            ),
            "max_lower_bound_over_variation": max(
                (
                    cert["lower_bound_over_variation"]
                    for row in records
                    for cert in row["certificates"]
                ),
                default=0.0,
            ),
        },
        "records": records,
    }


def write_markdown(report: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = report["summary"]
    lines = [
        "# SN3-E 高频 Bohr-cap 证书",
        "",
        "**状态：** `sn3e_highfreq_bohrcap_certificate_not_a_proof`",
        "",
        "## 摘要",
        "",
        f"- `record_count`: `{summary['record_count']}`",
        f"- `max_positive_cap_over_positive`: `{summary['max_positive_cap_over_positive']:.6f}`",
        f"- `max_captured_over_variation`: `{summary['max_captured_over_variation']:.6f}`",
        f"- `max_lower_bound_over_variation`: `{summary['max_lower_bound_over_variation']:.6f}`",
        "",
        "## 证书表",
        "",
        "| P | y | h | alpha | pos cap/pos | neg anti/neg | captured/var | lower/var | cap count | anti count |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["records"]:
        for cert in row["certificates"]:
            lines.append(
                f"| {row['p']} | {row['y']} | {cert['h']} | {cert['alpha']:.2f} | "
                f"{cert['positive_cap_over_positive']:.6f} | "
                f"{cert['negative_anticap_over_negative']:.6f} | "
                f"{cert['captured_over_variation']:.6f} | "
                f"{cert['lower_bound_over_variation']:.6f} | "
                f"{cert['cap_count']} | {cert['anticap_count']} |"
            )

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "对 signed 残余 `r=r_+-r_-`，若频率 `h` 的 Fourier 系数为 `L`、总变差为 `V`，则任意 `alpha<1` 给出 Jordan-Bohr 下界：",
            "",
            "```text",
            "r_+(Bohr_+) + r_-(Bohr_-) >= max(0,(L-alpha V)/(1-alpha))。",
            "```",
            "",
            "正帽质量进入高频 Column/PDEC，负反帽质量是模型过量/端点型缺陷。若两者都被排斥，则非零频率不能保持大值，残余进入 L2-flat clean KLS。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--sn3", default="docs/sn3_distributed_band_projection_audit_20260506.json")
    parser.add_argument("--sn3c", default="docs/sn3c_multiband_sync_audit_20260506.json")
    parser.add_argument("--sn3d", default="docs/sn3d_kls_multishell_frequency_audit_20260506.json")
    parser.add_argument("--alpha-list", default="0.0,0.25,0.5")
    parser.add_argument(
        "--out-prefix",
        default="docs/sn3e_highfreq_bohrcap_certificate_20260506",
    )
    args = parser.parse_args()
    sn3_data = json.loads(Path(args.sn3).read_text(encoding="utf-8"))
    sn3c_data = json.loads(Path(args.sn3c).read_text(encoding="utf-8"))
    sn3d_data = json.loads(Path(args.sn3d).read_text(encoding="utf-8"))
    report = build_report(sn3_data, sn3c_data, sn3d_data, parse_floats(args.alpha_list))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, prefix.with_suffix(".md"))
    print(json.dumps(report["summary"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
