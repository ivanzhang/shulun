#!/usr/bin/env python3
"""生成 SN3-A 中心化低模回流证书报告。

用法示例：
  python3 experiments/prime_matrix_sn3a_centered_lowmod_return_certificate.py \
    --input docs/sn3_distributed_band_projection_audit_20260506.json \
    --out-prefix docs/sn3a_centered_lowmod_return_certificate_20260506

目标：
  读取 SN-3 分散正带投影审计结果，把
  centered_pdec_return / centered_columncrt_return 候选升级为
  可引用的低模证书对象。该脚本只做确定性账本整理，不重新筛数。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path


def euler_phi(value: int) -> int:
    """计算欧拉 phi。"""
    result = value
    n = value
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            result -= result // factor
            while n % factor == 0:
                n //= factor
        factor += 1
    if n > 1:
        result -= result // n
    return result


def flatten_candidates(data: dict) -> list[dict]:
    """提取所有候选带。"""
    return [item for record in data["records"] for item in record["candidates"]]


def contrast_denominator(route: dict) -> int:
    """返回有限对比的平均分母。"""
    w_value = int(route["peak_w"])
    if route["peak_kind"] == "q_mod_w":
        return euler_phi(w_value)
    if route["peak_kind"] == "d_mod_w":
        return w_value
    return max(1, w_value)


def certificate_from_candidate(candidate: dict) -> dict:
    """把一个 SN3-A 回流候选转成证书行。"""
    route = candidate["sn3_centered_route"]
    projection = candidate["projection"]
    excess = float(projection["excess"])
    peak_share = float(route["peak_share"])
    peak_mass = peak_share * excess
    signed_residual = excess - peak_mass
    positive_residual = max(0.0, signed_residual)
    denominator = contrast_denominator(route)
    contrast_share_lower = max(0.0, peak_share - 1.0 / denominator)
    contrast_mass_lower = contrast_share_lower * excess
    return {
        "p": candidate["p"],
        "y": candidate["y"],
        "x": candidate["x"],
        "band": candidate["band"],
        "route": route["route"],
        "peak_kind": route["peak_kind"],
        "w": route["peak_w"],
        "residue": route["peak_key"],
        "threshold": route["threshold"],
        "excess": excess,
        "model": float(projection["model"]),
        "excess_over_required": candidate["excess_over_required"],
        "excess_over_sqrt_model": candidate["excess_over_sqrt_model"],
        "peak_share": peak_share,
        "peak_mass": peak_mass,
        "signed_residual_after_peak": signed_residual,
        "positive_residual_after_peak": positive_residual,
        "contrast_denominator": denominator,
        "contrast_share_lower": contrast_share_lower,
        "contrast_mass_lower": contrast_mass_lower,
    }


def build_report(data: dict) -> dict:
    """生成 SN3-A 证书报告。"""
    candidates = flatten_candidates(data)
    certificates = [
        certificate_from_candidate(item)
        for item in candidates
        if item["sn3_centered_route"]["route"]
        in {"centered_pdec_return", "centered_columncrt_return"}
    ]
    route_counts = Counter(item["route"] for item in certificates)
    total_excess = sum(item["excess"] for item in certificates)
    total_peak_mass = sum(item["peak_mass"] for item in certificates)
    total_positive_residual = sum(
        item["positive_residual_after_peak"] for item in certificates
    )
    return {
        "source_parameters": data["parameters"],
        "summary": {
            "certificate_count": len(certificates),
            "route_counts": dict(route_counts),
            "total_excess": total_excess,
            "total_peak_mass": total_peak_mass,
            "total_peak_mass_over_excess": (
                total_peak_mass / total_excess if total_excess > 0 else 0.0
            ),
            "total_positive_residual_after_peak": total_positive_residual,
            "total_positive_residual_over_excess": (
                total_positive_residual / total_excess if total_excess > 0 else 0.0
            ),
            "min_peak_share": min(
                (item["peak_share"] for item in certificates),
                default=0.0,
            ),
            "max_peak_share": max(
                (item["peak_share"] for item in certificates),
                default=0.0,
            ),
            "min_contrast_share_lower": min(
                (item["contrast_share_lower"] for item in certificates),
                default=0.0,
            ),
            "max_contrast_share_lower": max(
                (item["contrast_share_lower"] for item in certificates),
                default=0.0,
            ),
        },
        "certificates": sorted(
            certificates,
            key=lambda item: (-item["peak_share"], -item["excess_over_required"]),
        ),
    }


def write_markdown(report: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = report["summary"]
    params = report["source_parameters"]
    lines = [
        "# SN3-A 中心化低模回流证书",
        "",
        "**状态：** `sn3a_centered_lowmod_return_certificate_not_a_proof`",
        "",
        "## 来源",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `w_list`: `{params['w_list']}`",
        f"- `centered_return_share`: `{params['centered_return_share']}`",
        "",
        "## 总结",
        "",
        f"- `certificate_count`: `{summary['certificate_count']}`",
        f"- `route_counts`: `{summary['route_counts']}`",
        f"- `total_excess`: `{summary['total_excess']:.6f}`",
        f"- `total_peak_mass`: `{summary['total_peak_mass']:.6f}`",
        f"- `total_peak_mass_over_excess`: `{summary['total_peak_mass_over_excess']:.6f}`",
        f"- `total_positive_residual_after_peak`: `{summary['total_positive_residual_after_peak']:.6f}`",
        f"- `total_positive_residual_over_excess`: `{summary['total_positive_residual_over_excess']:.6f}`",
        f"- `min_peak_share`: `{summary['min_peak_share']:.6f}`",
        f"- `max_peak_share`: `{summary['max_peak_share']:.6f}`",
        f"- `min_contrast_share_lower`: `{summary['min_contrast_share_lower']:.6f}`",
        f"- `max_contrast_share_lower`: `{summary['max_contrast_share_lower']:.6f}`",
        "",
        "## 证书表",
        "",
        "| P | y | band | route | W | residue | E | peak/E | residual+ | contrast/E | E/R |",
        "|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in report["certificates"]:
        lines.append(
            f"| {item['p']} | {item['y']} | `{item['band']}` | "
            f"`{item['route']}` | {item['w']} | {item['residue']} | "
            f"{item['excess']:.6f} | {item['peak_share']:.6f} | "
            f"{item['positive_residual_after_peak']:.6f} | "
            f"{item['contrast_share_lower']:.6f} | "
            f"{item['excess_over_required']:.6f} |"
        )

    lines.extend(
        [
            "",
            "## 证书含义",
            "",
            "若某个中心化低模桶 `beta*` 满足 `E_beta* >= theta E_J`，则确定性分裂为：",
            "",
            "```text",
            "E_J = E_beta* + (E_J-E_beta*)",
            "E_J-E_beta* <= (1-theta)E_J。",
            "```",
            "",
            "因此该带不能继续作为无名分散质量处理：`q mod W` 峰进入 `PDEC`，`d mod W` 峰进入 `ColumnCRT`。表中的 `contrast/E` 是扣除平均桶后仍保留的有限低模对比下界；它只用于定位证书强度，不等于最终排斥证明。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/sn3_distributed_band_projection_audit_20260506.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/sn3a_centered_lowmod_return_certificate_20260506",
    )
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = build_report(data)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, prefix.with_suffix(".md"))
    print(json.dumps(report["summary"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
