#!/usr/bin/env python3
"""计算提升轮中单位类短区间的确定性容量包络。

用法示例：
  python3 experiments/prime_matrix_promoted_wheel_unit_interval_envelope.py \
    --wheels 30030,510510 --lengths 100,200,500,1000,2000,5000 \
    --out-prefix docs/promoted_wheel_unit_interval_envelope_20260506

若 P^2±k=q*m 落在 W 轮骨架中，则 m 必须是 W 的单位类。
所以任意 q 线容量 <= B_W(L)，其中 L 是互补因子区间长度，
B_W(L) 是模 W 任意连续长度 L 中最多单位类个数。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def units_indicator(modulus: int) -> list[int]:
    """返回模 modulus 的单位类指示数组。"""
    return [1 if math.gcd(value, modulus) == 1 else 0 for value in range(modulus)]


def omega_distinct(modulus: int) -> int:
    """返回不同素因子个数。"""
    count = 0
    n = modulus
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            count += 1
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
    if n > 1:
        count += 1
    return count


def max_units_in_cyclic_interval(indicator: list[int], length: int) -> dict:
    """计算循环模 W 上长度 length 的最大单位类数。"""
    modulus = len(indicator)
    if length <= 0:
        return {"length": length, "max_units": 0, "arg_start": 0}
    full, rem = divmod(length, modulus)
    base = full * sum(indicator)
    if rem == 0:
        return {"length": length, "max_units": base, "arg_start": 0}
    doubled = indicator + indicator[: rem]
    window = sum(doubled[:rem])
    best = window
    best_start = 0
    for start in range(1, modulus):
        window += doubled[start + rem - 1] - doubled[start - 1]
        if window > best:
            best = window
            best_start = start
    return {"length": length, "max_units": base + best, "arg_start": best_start}


def audit(wheels: list[int], lengths: list[int]) -> dict:
    """审计多个轮与长度。"""
    result = {"parameters": {"wheels": wheels, "lengths": lengths}, "wheels": {}}
    for wheel in wheels:
        indicator = units_indicator(wheel)
        phi = sum(indicator)
        omega = omega_distinct(wheel)
        rows = []
        for length in lengths:
            row = max_units_in_cyclic_interval(indicator, length)
            density_expected = length * phi / wheel
            mobius_bound = density_expected + (2 ** omega)
            row.update(
                {
                    "density_expected": density_expected,
                    "excess": row["max_units"] - density_expected,
                    "mobius_bound": mobius_bound,
                    "bound_slack": mobius_bound - row["max_units"],
                    "ratio": row["max_units"] / length if length else 0.0,
                }
            )
            rows.append(row)
        result["wheels"][str(wheel)] = {
            "phi": phi,
            "omega": omega,
            "density": phi / wheel,
            "rows": rows,
        }
    return result


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 提升轮单位类短区间容量包络",
        "",
        "**状态：** `deterministic_unit_interval_envelope`",
        "",
        "## 参数",
        "",
        f"- `wheels`: `{params['wheels']}`",
        f"- `lengths`: `{params['lengths']}`",
        "",
        "## 包络表",
        "",
        "| W | omega | phi/W | L | B_W(L) | B_W(L)/L | density expected | excess | mobius bound | slack | arg start |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for wheel_key, wheel in result["wheels"].items():
        for row in wheel["rows"]:
            lines.append(
                f"| {wheel_key} | {wheel['omega']} | {wheel['density']:.6f} | {row['length']} | "
                f"{row['max_units']} | {row['ratio']:.6f} | "
                f"{row['density_expected']:.6f} | {row['excess']:.6f} | "
                f"{row['mobius_bound']:.6f} | {row['bound_slack']:.6f} | "
                f"{row['arg_start']} |"
            )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "`B_W(L)` 是确定性上界：任何剩余高素 `q` 斜线在提升轮 `W` 骨架上的容量，不超过互补因子区间长度 `L_q` 对应的 `B_W(L_q)`。此外由莫比乌斯反演，`B_W(L)<=L*phi(W)/W+2^omega(W)`。这把 q 线容量从经验密度估计改成了可复核的有限 CRT 包络。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--wheels", default="30030,510510")
    parser.add_argument("--lengths", default="100,200,500,1000,2000,5000")
    parser.add_argument(
        "--out-prefix",
        default="docs/promoted_wheel_unit_interval_envelope_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.wheels), parse_ints(args.lengths))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
