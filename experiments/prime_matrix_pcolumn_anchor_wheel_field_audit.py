#!/usr/bin/env python3
"""审计第 P 列锚点诱导的全行层叠轮筛。

用法示例：
  python3 experiments/prime_matrix_pcolumn_anchor_wheel_field_audit.py \
    --p-list 101,499,997,2003,5003 \
    --wheels 30,210,2310,30030 \
    --out-prefix docs/pcolumn_anchor_wheel_field_audit_20260506

目标：
  把第 x 行写成 P(x+1)-d，其中 d=P-c。
  第 P 列点 P(x+1) 的同余类决定整行的轮筛骨架。
  审计每行骨架是否只是第一行骨架的圆柱平移，并统计轮骨架洞与最终素数洞。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


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


def prime_factors(value: int) -> list[int]:
    """返回 value 的不同素因子。"""
    factors: list[int] = []
    current = value
    divisor = 2
    while divisor * divisor <= current:
        if current % divisor == 0:
            factors.append(divisor)
            while current % divisor == 0:
                current //= divisor
        divisor += 1 if divisor == 2 else 2
    if current > 1:
        factors.append(current)
    return factors


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def allowed_residues_for_anchor(p: int, y: int, wheel: int) -> set[int]:
    """返回距离 d 的允许 residue：gcd(Py-d,W)=1。"""
    anchor = (p * y) % wheel
    return {
        residue
        for residue in range(wheel)
        if math.gcd((anchor - residue) % wheel, wheel) == 1
    }


def shifted_residues(base: set[int], shift: int, wheel: int) -> set[int]:
    """把 residue 集合平移 shift。"""
    return {(residue + shift) % wheel for residue in base}


def audit_p_wheel(
    p: int, wheel: int, prime_flags: bytearray, include_square_plus: bool
) -> dict:
    """审计固定 P 与 W 的全行锚点轮筛。"""
    base = allowed_residues_for_anchor(p, 2, wheel)
    wheel_primes = prime_factors(wheel)
    y_stop = p + 1 if include_square_plus else p
    row_records = []
    shift_failures = 0
    min_skeleton = None
    min_prime_holes = None
    max_filler_ratio = -1.0
    max_anchor_zero = -1
    min_skeleton_rows = []
    min_prime_rows = []
    max_filler_rows = []
    max_anchor_rows = []

    for y in range(2, y_stop + 1):
        direct = allowed_residues_for_anchor(p, y, wheel)
        shifted = shifted_residues(base, (p * (y - 2)) % wheel, wheel)
        if direct != shifted:
            shift_failures += 1

        skeleton_count = 0
        prime_holes = 0
        for d in range(1, p):
            n = p * y - d
            if d % wheel in direct:
                skeleton_count += 1
            if prime_flags[n]:
                prime_holes += 1

        filler = skeleton_count - prime_holes
        filler_ratio = filler / skeleton_count if skeleton_count else 0.0
        anchor_zero = sum(1 for q in wheel_primes if y % q == 0)
        record = {
            "x": y - 1,
            "y": y,
            "p_column_value": p * y,
            "p_column_cofactor_factors_in_wheel": [
                q for q in wheel_primes if y % q == 0
            ],
            "anchor_zero_prime_count": anchor_zero,
            "skeleton_count": skeleton_count,
            "prime_holes": prime_holes,
            "filler_count": filler,
            "filler_ratio": filler_ratio,
        }
        row_records.append(record)

        if min_skeleton is None or skeleton_count < min_skeleton:
            min_skeleton = skeleton_count
            min_skeleton_rows = [record]
        elif skeleton_count == min_skeleton:
            min_skeleton_rows.append(record)

        if min_prime_holes is None or prime_holes < min_prime_holes:
            min_prime_holes = prime_holes
            min_prime_rows = [record]
        elif prime_holes == min_prime_holes:
            min_prime_rows.append(record)

        if filler_ratio > max_filler_ratio:
            max_filler_ratio = filler_ratio
            max_filler_rows = [record]
        elif filler_ratio == max_filler_ratio:
            max_filler_rows.append(record)

        if anchor_zero > max_anchor_zero:
            max_anchor_zero = anchor_zero
            max_anchor_rows = [record]
        elif anchor_zero == max_anchor_zero:
            max_anchor_rows.append(record)

    return {
        "p": p,
        "wheel": wheel,
        "wheel_prime_factors": wheel_primes,
        "row_count": len(row_records),
        "include_square_plus": include_square_plus,
        "shift_identity_failures": shift_failures,
        "min_skeleton_count": min_skeleton,
        "min_skeleton_rows": min_skeleton_rows[:8],
        "min_prime_holes": min_prime_holes,
        "min_prime_rows": min_prime_rows[:8],
        "max_filler_ratio": max_filler_ratio,
        "max_filler_rows": max_filler_rows[:8],
        "max_anchor_zero_prime_count": max_anchor_zero,
        "max_anchor_rows": max_anchor_rows[:8],
        "sample_rows": row_records[:3] + row_records[-3:],
    }


def audit(p_list: list[int], wheels: list[int], include_square_plus: bool) -> dict:
    """执行审计。"""
    max_p = max(p_list)
    max_y = max_p + 1 if include_square_plus else max_p
    prime_flags = sieve_bool(max_p * max_y)
    rows = [
        audit_p_wheel(p, wheel, prime_flags, include_square_plus)
        for p in p_list
        for wheel in wheels
    ]
    return {
        "parameters": {
            "p_list": p_list,
            "wheels": wheels,
            "include_square_plus": include_square_plus,
            "max_sieve": max_p * max_y,
        },
        "rows": rows,
    }


def fmt(value: float | int) -> str:
    """格式化数值。"""
    if isinstance(value, int):
        return str(value)
    return f"{value:.6f}"


def short_record(record: dict) -> str:
    """压缩行记录。"""
    return (
        f"x={record['x']}, y={record['y']}, "
        f"S={record['skeleton_count']}, primes={record['prime_holes']}, "
        f"fill={record['filler_count']}, ratio={record['filler_ratio']:.6f}, "
        f"anchor={record['p_column_cofactor_factors_in_wheel']}"
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 第P列锚点层叠轮筛审计",
        "",
        "**状态：** `pcolumn_anchor_wheel_field_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `wheels`: `{params['wheels']}`",
        f"- `include_square_plus`: `{params['include_square_plus']}`",
        f"- `max_sieve`: `{params['max_sieve']}`",
        "",
        "## 总表",
        "",
        "| P | W | rows | shift failures | min skeleton | min prime holes | max filler ratio | max anchor primes |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['p']} | {row['wheel']} | {row['row_count']} | "
            f"{row['shift_identity_failures']} | {row['min_skeleton_count']} | "
            f"{row['min_prime_holes']} | {fmt(row['max_filler_ratio'])} | "
            f"{row['max_anchor_zero_prime_count']} |"
        )
    lines.append("")

    for row in result["rows"]:
        lines.extend(
            [
                f"## P={row['p']} W={row['wheel']}",
                "",
                f"- `wheel_prime_factors`: `{row['wheel_prime_factors']}`",
                f"- `shift_identity_failures`: `{row['shift_identity_failures']}`",
                f"- `min_skeleton_count`: `{row['min_skeleton_count']}`",
                f"- `min_prime_holes`: `{row['min_prime_holes']}`",
                f"- `max_filler_ratio`: `{row['max_filler_ratio']:.6f}`",
                f"- `max_anchor_zero_prime_count`: `{row['max_anchor_zero_prime_count']}`",
                "",
                "最小素数洞行：",
                "",
            ]
        )
        for record in row["min_prime_rows"]:
            lines.append(f"- `{short_record(record)}`")
        lines.extend(["", "最高补洞比例行：", ""])
        for record in row["max_filler_rows"]:
            lines.append(f"- `{short_record(record)}`")
        lines.extend(["", "最大第P列锚因子行：", ""])
        for record in row["max_anchor_rows"]:
            lines.append(f"- `{short_record(record)}`")
        lines.append("")

    lines.extend(
        [
            "## 结构解释",
            "",
            "第 `x` 行写成 `P(x+1)-d`，其中 `d=P-c`。所以第 `P` 列锚点 `P(x+1)` 的轮残基决定整行的距离筛：",
            "",
            "```text",
            "P(x+1)-d 避开 W 的全部素因子",
            "<=> d mod W 属于 P(x+1)-U_W。",
            "```",
            "",
            "第一行是 `x=1,y=2`。任意行 `y=x+1` 的允许距离类，等于第一行允许距离类平移 `P(y-2)`。报告中的 `shift_identity_failures=0` 是这个圆柱平移恒等式的机器核验。",
            "",
            "若某个 `q|W` 同时满足 `q|y`，则第 `P` 列锚点在 `mod q` 为零，该 q 在本行覆盖的距离类是 `d≡0 mod q`。这就是第 `P` 列的层叠轮筛如何接入整行斜线覆盖。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="101,499,997,2003,5003")
    parser.add_argument("--wheels", default="30,210,2310,30030")
    parser.add_argument("--include-square-plus", action="store_true", default=True)
    parser.add_argument(
        "--out-prefix",
        default="docs/pcolumn_anchor_wheel_field_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.p_list), parse_ints(args.wheels), args.include_square_plus)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
