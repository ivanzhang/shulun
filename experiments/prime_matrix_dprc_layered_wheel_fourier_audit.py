#!/usr/bin/env python3
"""审计层叠轮单位偏差的低模 Fourier 证书。

用法示例：
  python3 experiments/prime_matrix_dprc_layered_wheel_fourier_audit.py \
    --records 64853:minus,34159:minus,34981:minus,30137:minus,21149:plus,83267:plus \
    --wheels 30,210,2310 \
    --out-prefix docs/dprc_layered_wheel_fourier_audit_20260506

目标：
  对单位类偏差 E_W(a) 扣除单位类平均项，扫描加性 Fourier 频率 h。
  若存在大 Fourier 系数，即物化 W-unit PDEC 的低模频率证书。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


BETA_BUCKETS = [
    (0.43, 0.50, "[0.43,0.50)"),
    (0.50, 0.60, "[0.50,0.60)"),
    (0.60, 0.70, "[0.60,0.70)"),
    (0.70, 0.80, "[0.70,0.80)"),
    (0.80, 0.90, "[0.80,0.90)"),
    (0.90, 1.01, "[0.90,1.00)"),
]


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def units_mod(wheel: int) -> list[int]:
    """返回 wheel 的单位类。"""
    return [residue for residue in range(wheel) if math.gcd(residue, wheel) == 1]


def row_residue(p: int, q: int, side: str) -> int:
    """返回 q 覆盖平方前/后行时的 k 同余类。"""
    p2 = (p * p) % q
    if side == "plus":
        return (-p2) % q
    if side == "minus":
        return p2
    raise ValueError(f"unknown side: {side}")


def n_residue_mod(p: int, k: int, side: str, wheel: int) -> int:
    """返回真实数值 P^2±k 的 mod wheel 残基。"""
    p2 = (p * p) % wheel
    if side == "plus":
        return (p2 + k) % wheel
    return (p2 - k) % wheel


def mark_low_skeleton(p: int, low_primes: list[int], side: str) -> bytearray:
    """标记动态粗骨架。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    for q in low_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def beta_bucket(beta: float) -> str:
    """返回 beta 桶标签。"""
    for left, right, label in BETA_BUCKETS:
        if left <= beta < right:
            return label
    return "outside"


def build_record_vectors(
    p: int, side: str, alpha: float, primes: list[int], wheels: list[int]
) -> dict:
    """构造单条记录的 BES 与单位偏差向量。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton = sum(alive)
    sqrt_s = math.sqrt(skeleton)
    bucket_disc = {label: 0.0 for _left, _right, label in BETA_BUCKETS}
    actual = {wheel: [0] * wheel for wheel in wheels}
    expected_counts = {wheel: [0] * wheel for wheel in wheels}
    harmonic_high = 0.0

    for k, flag in enumerate(alive):
        if not flag:
            continue
        for wheel in wheels:
            expected_counts[wheel][n_residue_mod(p, k, side, wheel)] += 1

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if not alive[k]:
                continue
            hits += 1
            for wheel in wheels:
                actual[wheel][n_residue_mod(p, k, side, wheel)] += 1
        harmonic_high += 1.0 / q
        label = beta_bucket(math.log(q) / math.log(p))
        if label != "outside":
            bucket_disc[label] += hits - skeleton / q

    bucket_vector = [
        bucket_disc[label] / sqrt_s if sqrt_s else 0.0
        for _left, _right, label in BETA_BUCKETS
    ]
    positive_vector = [max(0.0, value) for value in bucket_vector]
    l1_value = sum(positive_vector)
    l2_value = math.sqrt(sum(value * value for value in positive_vector))
    effective_dimension = (
        (l1_value * l1_value) / (l2_value * l2_value) if l2_value else 0.0
    )

    wheel_data = {}
    for wheel in wheels:
        units = units_mod(wheel)
        discrepancies = []
        for residue in units:
            expected = expected_counts[wheel][residue] * harmonic_high
            discrepancies.append((residue, actual[wheel][residue] - expected))
        mean = sum(value for _residue, value in discrepancies) / len(units)
        centered = {residue: value - mean for residue, value in discrepancies}
        raw_top = max(discrepancies, key=lambda item: item[1])
        centered_top = max(centered.items(), key=lambda item: item[1])
        centered_l2 = math.sqrt(sum(value * value for value in centered.values()))
        wheel_data[str(wheel)] = {
            "units": units,
            "raw_mean": mean,
            "raw_top_residue": raw_top[0],
            "raw_top_discrepancy": raw_top[1],
            "raw_top_over_sqrt": raw_top[1] / sqrt_s if sqrt_s else 0.0,
            "centered_top_residue": centered_top[0],
            "centered_top_value": centered_top[1],
            "centered_top_over_sqrt": centered_top[1] / sqrt_s if sqrt_s else 0.0,
            "centered_l2": centered_l2,
            "centered_l2_over_sqrt": centered_l2 / sqrt_s if sqrt_s else 0.0,
            "centered": centered,
        }

    return {
        "p": p,
        "side": side,
        "cutoff": cutoff,
        "skeleton_count": skeleton,
        "sqrt_skeleton": sqrt_s,
        "positive_bucket_l1_over_sqrt": l1_value,
        "positive_bucket_l2_over_sqrt": l2_value,
        "positive_bucket_effective_dimension": effective_dimension,
        "wheel_data": wheel_data,
    }


def additive_fourier(centered: dict[int, float], wheel: int, top_n: int) -> dict:
    """扫描加性 Fourier 频率。"""
    coefficients = []
    residues = list(centered.keys())
    for h in range(1, wheel):
        real = 0.0
        imag = 0.0
        for residue in residues:
            angle = 2.0 * math.pi * h * residue / wheel
            value = centered[residue]
            real += value * math.cos(angle)
            imag += value * math.sin(angle)
        abs_value = math.hypot(real, imag)
        coefficients.append(
            {
                "h": h,
                "gcd_h_w": math.gcd(h, wheel),
                "period": wheel // math.gcd(h, wheel),
                "real": real,
                "imag": imag,
                "abs": abs_value,
            }
        )
    coefficients.sort(key=lambda row: -row["abs"])
    energy = sum(value * value for value in centered.values())
    parseval_total = wheel * energy
    nonzero_energy = sum(row["abs"] * row["abs"] for row in coefficients)
    return {
        "top_frequencies": coefficients[:top_n],
        "parseval_total": parseval_total,
        "nonzero_frequency_energy": nonzero_energy,
        "parseval_error": nonzero_energy - parseval_total,
    }


def audit_record(
    p: int,
    side: str,
    alpha: float,
    primes: list[int],
    wheels: list[int],
    top_n: int,
) -> dict:
    """审计单条记录的 Fourier 证书。"""
    built = build_record_vectors(p, side, alpha, primes, wheels)
    sqrt_s = built["sqrt_skeleton"]
    wheel_rows = []
    for wheel in wheels:
        data = built["wheel_data"][str(wheel)]
        fourier = additive_fourier(data["centered"], wheel, top_n)
        top_frequency = fourier["top_frequencies"][0]
        wheel_rows.append(
            {
                "wheel": wheel,
                "phi": len(data["units"]),
                "raw_mean": data["raw_mean"],
                "raw_top_residue": data["raw_top_residue"],
                "raw_top_over_sqrt": data["raw_top_over_sqrt"],
                "centered_top_residue": data["centered_top_residue"],
                "centered_top_over_sqrt": data["centered_top_over_sqrt"],
                "centered_l2_over_sqrt": data["centered_l2_over_sqrt"],
                "max_fourier_abs_over_sqrt": top_frequency["abs"] / sqrt_s
                if sqrt_s
                else 0.0,
                "max_fourier_frequency": top_frequency,
                "top_frequencies": [
                    {
                        **row,
                        "abs_over_sqrt": row["abs"] / sqrt_s if sqrt_s else 0.0,
                    }
                    for row in fourier["top_frequencies"]
                ],
                "parseval_relative_error": (
                    fourier["parseval_error"] / fourier["parseval_total"]
                    if fourier["parseval_total"]
                    else 0.0
                ),
            }
        )

    return {
        "p": built["p"],
        "side": built["side"],
        "cutoff": built["cutoff"],
        "skeleton_count": built["skeleton_count"],
        "positive_bucket_l1_over_sqrt": built["positive_bucket_l1_over_sqrt"],
        "positive_bucket_l2_over_sqrt": built["positive_bucket_l2_over_sqrt"],
        "positive_bucket_effective_dimension": built[
            "positive_bucket_effective_dimension"
        ],
        "wheels": wheel_rows,
    }


def parse_records(raw: str) -> list[tuple[int, str]]:
    """解析 P:side 列表。"""
    records = []
    for item in raw.split(","):
        if not item.strip():
            continue
        p_raw, side = item.split(":")
        records.append((int(p_raw), side.strip()))
    return records


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def audit(
    records: list[tuple[int, str]], alpha: float, wheels: list[int], top_n: int
) -> dict:
    """执行多记录 Fourier 审计。"""
    max_p = max(p for p, _side in records)
    primes = primes_from_flags(sieve_bool(max_p))
    return {
        "parameters": {
            "records": records,
            "alpha": alpha,
            "wheels": wheels,
            "top_n": top_n,
        },
        "records": [
            audit_record(p, side, alpha, primes, wheels, top_n)
            for p, side in records
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# DPRC层叠轮 Fourier 审计",
        "",
        "**状态：** `fourier_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `records`: `{params['records']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `wheels`: `{params['wheels']}`",
        f"- `top_n`: `{params['top_n']}`",
        "",
    ]
    for record in result["records"]:
        lines.extend(
            [
                f"## P={record['p']} {record['side']}",
                "",
                f"- `S`: `{record['skeleton_count']}`",
                f"- `BES L1`: `{record['positive_bucket_l1_over_sqrt']:.6f}`",
                f"- `BES L2`: `{record['positive_bucket_l2_over_sqrt']:.6f}`",
                f"- `BES eff dim`: `{record['positive_bucket_effective_dimension']:.6f}`",
                "",
                "| W | raw peak/sqrt | centered peak/sqrt | centered L2/sqrt | max Fourier/sqrt | top h | gcd(h,W) | period | Parseval rel err |",
                "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in record["wheels"]:
            top = row["max_fourier_frequency"]
            lines.append(
                f"| {row['wheel']} | {row['raw_top_over_sqrt']:.6f} | "
                f"{row['centered_top_over_sqrt']:.6f} | "
                f"{row['centered_l2_over_sqrt']:.6f} | "
                f"{row['max_fourier_abs_over_sqrt']:.6f} | "
                f"{top['h']} | {top['gcd_h_w']} | {top['period']} | "
                f"{row['parseval_relative_error']:.3e} |"
            )
        for row in record["wheels"]:
            lines.extend(
                [
                    "",
                    f"### W={row['wheel']} top frequencies",
                    "",
                    "| h | gcd(h,W) | period | abs/sqrt | real | imag |",
                    "|---:|---:|---:|---:|---:|---:|",
                ]
            )
            for freq in row["top_frequencies"]:
                lines.append(
                    f"| {freq['h']} | {freq['gcd_h_w']} | {freq['period']} | "
                    f"{freq['abs_over_sqrt']:.6f} | "
                    f"{freq['real']:.3f} | {freq['imag']:.3f} |"
                )
        lines.append("")
    lines.extend(
        [
            "## 结构解释",
            "",
            "表中的 `max Fourier/sqrt` 是低模加性 Fourier 频率证书强度。若某个单位类峰在扣除平均项后仍大，则对应的非零频率就是 `W-unit PDEC` 的候选方向。`period` 给出该频率看到的低模周期块，可用于后续构造显式坏相位证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--records",
        default=(
            "64853:minus,34159:minus,34981:minus,"
            "30137:minus,21149:plus,83267:plus,95581:minus,78121:minus"
        ),
    )
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--wheels", default="30,210,2310")
    parser.add_argument("--top-n", type=int, default=8)
    parser.add_argument(
        "--out-prefix",
        default="docs/dprc_layered_wheel_fourier_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_records(args.records),
        args.alpha,
        parse_ints(args.wheels),
        args.top_n,
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
