#!/usr/bin/env python3
"""审计 SN3-D KLS-Multishell 的高频列相位。

用法示例：
  python3 experiments/prime_matrix_sn3d_kls_multishell_frequency_audit.py \
    --sn3 docs/sn3_distributed_band_projection_audit_20260506.json \
    --sn3c docs/sn3c_multiband_sync_audit_20260506.json \
    --max-frequency 256 \
    --out-prefix docs/sn3d_kls_multishell_frequency_audit_20260506

目标：
  对 SN3-C 留下的 KLS-Multishell 候选，重构列位移
  d=Py-qm 上的中心化残余，并扫描 d mod P 的非零 Fourier 频率。
  若某个高频显著，则登记为 high-frequency Column/PDEC 证书；
  若所有扫描频率平坦，则该候选进入 clean KLS/dispersion 输入。
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
sn3 = load_module("sn3_projection_audit", "prime_matrix_sn3_distributed_band_projection_audit.py")


def residual_by_d(
    p: int,
    y: int,
    bands: list[str],
    cutoff: int,
    tail_factor: float,
    rough: bytearray,
    prefix: list[int],
    primes: list[int],
) -> dict:
    """重构多个带合并后的 d 列中心化残余。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    residual = [0.0] * p
    actual_total = 0
    model_total = 0.0
    interval_len = 0

    for band in bands:
        left_m, right_m = sn3.band_bounds(band, y, m_max)
        for m in range(left_m, right_m + 1):
            if m >= len(rough) or not rough[m]:
                continue
            q_min = max(tail_q_min, sn2.ceil_div(anchor - (p - 1), m))
            q_max = min(p - 1, (anchor - 1) // m)
            if q_min > q_max:
                continue
            local_weight = 1.0 / math.log(max(q_min, 3))
            interval_len += q_max - q_min + 1
            model_total += (q_max - q_min + 1) * local_weight
            for q in range(q_min, q_max + 1):
                d = anchor - q * m
                if 0 < d < p:
                    residual[d] -= local_weight
            lo = sn2.bisect.bisect_left(primes, q_min)
            hi = sn2.bisect.bisect_right(primes, q_max)
            for q in primes[lo:hi]:
                d = anchor - q * m
                if 0 < d < p:
                    residual[d] += 1.0
                    actual_total += 1

    excess = actual_total - model_total
    l2 = math.sqrt(sum(value * value for value in residual))
    mean = excess / (p - 1)
    centered_l2 = math.sqrt(
        sum((residual[d] - mean) * (residual[d] - mean) for d in range(1, p))
    )
    flatness = abs(excess) / (math.sqrt(p - 1) * l2) if l2 > 0 else 0.0
    return {
        "residual": residual,
        "actual": actual_total,
        "model": model_total,
        "excess": excess,
        "interval_len": interval_len,
        "l2": l2,
        "centered_l2": centered_l2,
        "flatness": flatness,
    }


def scan_fourier(residual: list[float], max_frequency: int) -> dict:
    """扫描 d mod P 的前 max_frequency 个非零 Fourier 频率。"""
    p = len(residual)
    rows = []
    for h in range(1, min(max_frequency, p - 1) + 1):
        total = 0j
        for d in range(1, p):
            value = residual[d]
            if value:
                total += value * cmath.exp(-2j * math.pi * h * d / p)
        rows.append({"h": h, "abs": abs(total), "real": total.real, "imag": total.imag})
    rows.sort(key=lambda row: -row["abs"])
    partial_l2 = math.sqrt(sum(row["abs"] * row["abs"] for row in rows))
    return {"top_frequencies": rows[:12], "partial_fourier_l2": partial_l2}


def build_report(sn3_data: dict, sn3c_data: dict, max_frequency: int) -> dict:
    """生成 SN3-D 高频审计。"""
    params = sn3_data["parameters"]
    p_list = params["p_list"]
    alpha = float(params["alpha"])
    tail_factor = float(params["tail_factor"])
    flags = sn2.sieve_bool(max(p_list))
    prefix = sn2.prime_prefix(flags)
    primes = sn2.primes_from_flags(flags)

    records = []
    for row in sn3c_data["rows"]:
        kls_pairs = [pair for pair in row["pairs"] if pair["route"] == "kls_multishell_candidate"]
        if not kls_pairs:
            continue
        p = int(row["p"])
        y = int(row["y"])
        cutoff = int(p**alpha)
        low_primes = [q for q in primes if q <= cutoff]
        tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
        m_limit = (p * y * 8 - 1) // tail_q_min
        rough = sn2.rough_flags(m_limit, low_primes)
        bands = sorted({band["band"] for band in row["bands"]})
        residual = residual_by_d(
            p,
            y,
            bands,
            cutoff,
            tail_factor,
            rough,
            prefix,
            primes,
        )
        fourier = scan_fourier(residual["residual"], max_frequency)
        top_abs = fourier["top_frequencies"][0]["abs"] if fourier["top_frequencies"] else 0.0
        excess = abs(residual["excess"])
        records.append(
            {
                "p": p,
                "y": y,
                "bands": bands,
                "true_excess_over_required": row["total_true_excess_over_required"],
                "q_shells": [band["q_shell"] for band in row["bands"]],
                "kls_pair_count": len(kls_pairs),
                "actual": residual["actual"],
                "model": residual["model"],
                "excess": residual["excess"],
                "l2": residual["l2"],
                "centered_l2": residual["centered_l2"],
                "flatness": residual["flatness"],
                "top_frequency_abs_over_excess": top_abs / excess if excess > 0 else 0.0,
                "partial_fourier_l2_over_excess": (
                    fourier["partial_fourier_l2"] / excess if excess > 0 else 0.0
                ),
                **fourier,
            }
        )

    return {
        "source_parameters": params,
        "parameters": {"max_frequency": max_frequency},
        "summary": {
            "kls_multishell_record_count": len(records),
            "max_top_frequency_abs_over_excess": max(
                (row["top_frequency_abs_over_excess"] for row in records),
                default=0.0,
            ),
            "max_partial_fourier_l2_over_excess": max(
                (row["partial_fourier_l2_over_excess"] for row in records),
                default=0.0,
            ),
            "min_flatness": min((row["flatness"] for row in records), default=0.0),
            "max_flatness": max((row["flatness"] for row in records), default=0.0),
        },
        "records": sorted(records, key=lambda row: -row["true_excess_over_required"]),
    }


def write_markdown(report: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = report["summary"]
    lines = [
        "# SN3-D KLS-Multishell 高频列相位审计",
        "",
        "**状态：** `sn3d_kls_multishell_frequency_audit_not_a_proof`",
        "",
        "## 摘要",
        "",
        f"- `kls_multishell_record_count`: `{summary['kls_multishell_record_count']}`",
        f"- `max_top_frequency_abs_over_excess`: `{summary['max_top_frequency_abs_over_excess']:.6f}`",
        f"- `max_partial_fourier_l2_over_excess`: `{summary['max_partial_fourier_l2_over_excess']:.6f}`",
        f"- `min_flatness`: `{summary['min_flatness']:.6f}`",
        f"- `max_flatness`: `{summary['max_flatness']:.6f}`",
        "",
        "## KLS 候选",
        "",
        "| P | y | bands | E/R | excess | l2 | flatness | top h | top/E | partial/E |",
        "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["records"]:
        top = row["top_frequencies"][0] if row["top_frequencies"] else {"h": 0}
        lines.append(
            f"| {row['p']} | {row['y']} | `{row['bands']}` | "
            f"{row['true_excess_over_required']:.6f} | "
            f"{row['excess']:.6f} | {row['l2']:.6f} | "
            f"{row['flatness']:.6f} | {top['h']} | "
            f"{row['top_frequency_abs_over_excess']:.6f} | "
            f"{row['partial_fourier_l2_over_excess']:.6f} |"
        )
        top_text = ", ".join(
            f"h={item['h']}:abs={item['abs']:.3f}"
            for item in row["top_frequencies"][:6]
        )
        lines.append(f"|  |  | top frequencies |  |  |  |  |  | `{top_text}` |  |")

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "该审计把 KLS-Multishell 候选重构为列位移 `d=Py-qm` 上的中心化残余，并扫描 `d mod P` 的非零 Fourier 频率。若非零频率持续偏大，则进入高频 Column/PDEC 证书；若频率平坦，则该候选满足 clean KLS/dispersion 输入的形态。",
            "",
            "这不是证明；它把 `KLS-Multishell` 的失败形态物化为可检查的高频列相位证书，或把无峰残余送入外部/待证 KLS 估计。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--sn3", default="docs/sn3_distributed_band_projection_audit_20260506.json")
    parser.add_argument("--sn3c", default="docs/sn3c_multiband_sync_audit_20260506.json")
    parser.add_argument("--max-frequency", type=int, default=256)
    parser.add_argument(
        "--out-prefix",
        default="docs/sn3d_kls_multishell_frequency_audit_20260506",
    )
    args = parser.parse_args()
    sn3_data = json.loads(Path(args.sn3).read_text(encoding="utf-8"))
    sn3c_data = json.loads(Path(args.sn3c).read_text(encoding="utf-8"))
    report = build_report(sn3_data, sn3c_data, args.max_frequency)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, prefix.with_suffix(".md"))
    print(json.dumps(report["summary"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
