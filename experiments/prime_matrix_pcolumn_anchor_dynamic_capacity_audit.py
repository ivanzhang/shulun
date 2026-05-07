#!/usr/bin/env python3
"""审计第 P 列锚点场的动态提升轮容量。

用法示例：
  python3 experiments/prime_matrix_pcolumn_anchor_dynamic_capacity_audit.py \
    --p-list 101,499,997,2003,5003 \
    --alpha 0.43 \
    --out-prefix docs/pcolumn_anchor_dynamic_capacity_audit_20260506

目标：
  对每一行写 n=Py-d，其中 y=x+1, 1<=d<P。
  把 q<=Y=P^alpha 提升进底座，检查剩余 Y<q<P 的总命中 T_Y
  是否小于动态粗骨架 S_Y。
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


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def mark_low_skeleton(p: int, y: int, low_primes: list[int]) -> bytearray:
    """标记 Py-d 的动态低素骨架，索引 d。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    anchor = p * y
    for q in low_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def audit_row(
    p: int,
    y: int,
    low_primes: list[int],
    high_primes: list[int],
    harmonic: float,
) -> dict:
    """审计单个锚点行。"""
    alive = mark_low_skeleton(p, y, low_primes)
    skeleton = sum(alive)
    total_hits = 0
    covered = bytearray(p)
    anchor = p * y
    top_q = []
    for q in high_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        hits = 0
        for d in range(start, p, q):
            if not alive[d]:
                continue
            hits += 1
            covered[d] = 1
        if hits:
            total_hits += hits
            top_q.append({"q": q, "hit_count": hits})

    covered_count = sum(1 for d in range(1, p) if covered[d])
    prime_holes = skeleton - covered_count
    margin = skeleton - total_hits
    sqrt_skeleton = math.sqrt(skeleton) if skeleton else 0.0
    expected_hits = harmonic * skeleton
    positive_discrepancy = max(0.0, total_hits - expected_hits)
    model_gap = skeleton * (1.0 - harmonic)
    return {
        "x": y - 1,
        "y": y,
        "skeleton_count": skeleton,
        "total_high_hits": total_hits,
        "capacity_margin": margin,
        "hit_ratio": total_hits / skeleton if skeleton else 0.0,
        "harmonic": harmonic,
        "expected_high_hits": expected_hits,
        "positive_discrepancy": positive_discrepancy,
        "model_gap": model_gap,
        "positive_discrepancy_over_sqrt": (
            positive_discrepancy / sqrt_skeleton if sqrt_skeleton else 0.0
        ),
        "model_gap_over_sqrt": (
            model_gap / sqrt_skeleton if sqrt_skeleton else 0.0
        ),
        "covered_count": covered_count,
        "prime_holes": prime_holes,
        "union_margin": skeleton - covered_count,
        "top_q": sorted(top_q, key=lambda row: -row["hit_count"])[:8],
    }


def audit_p(p: int, alpha: float, primes: list[int], include_square_plus: bool) -> dict:
    """审计固定 P 的所有锚点行。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    harmonic = sum(1.0 / q for q in high_primes)
    y_stop = p + 1 if include_square_plus else p
    rows = [
        audit_row(p, y, low_primes, high_primes, harmonic)
        for y in range(2, y_stop + 1)
    ]
    min_margin = min(row["capacity_margin"] for row in rows)
    max_ratio = max(row["hit_ratio"] for row in rows)
    min_prime_holes = min(row["prime_holes"] for row in rows)
    min_model_over_sqrt = min(row["model_gap_over_sqrt"] for row in rows)
    max_dplus_over_sqrt = max(
        row["positive_discrepancy_over_sqrt"] for row in rows
    )
    capacity_failures = [row for row in rows if row["capacity_margin"] <= 0]
    union_failures = [row for row in rows if row["prime_holes"] <= 0]
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "harmonic": harmonic,
        "row_count": len(rows),
        "low_prime_count": len(low_primes),
        "high_prime_count": len(high_primes),
        "min_capacity_margin": min_margin,
        "max_hit_ratio": max_ratio,
        "min_prime_holes": min_prime_holes,
        "min_model_over_sqrt": min_model_over_sqrt,
        "max_dplus_over_sqrt": max_dplus_over_sqrt,
        "sqrt_c_window": min_model_over_sqrt - max_dplus_over_sqrt,
        "capacity_failure_count": len(capacity_failures),
        "union_failure_count": len(union_failures),
        "tight_margin_rows": sorted(rows, key=lambda row: row["capacity_margin"])[:8],
        "top_ratio_rows": sorted(rows, key=lambda row: -row["hit_ratio"])[:8],
        "top_dplus_rows": sorted(
            rows, key=lambda row: -row["positive_discrepancy_over_sqrt"]
        )[:8],
        "thin_prime_rows": sorted(rows, key=lambda row: row["prime_holes"])[:8],
    }


def audit(p_list: list[int], alpha: float, include_square_plus: bool) -> dict:
    """执行审计。"""
    max_p = max(p_list)
    primes = primes_from_flags(sieve_bool(max_p))
    records = [audit_p(p, alpha, primes, include_square_plus) for p in p_list]
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "include_square_plus": include_square_plus,
        },
        "records": records,
    }


def fmt(value: float | int) -> str:
    """格式化数值。"""
    if isinstance(value, int):
        return str(value)
    return f"{value:.6f}"


def row_text(row: dict) -> str:
    """压缩行记录。"""
    return (
        f"x={row['x']}, y={row['y']}, "
        f"S={row['skeleton_count']}, T={row['total_high_hits']}, "
        f"margin={row['capacity_margin']}, ratio={row['hit_ratio']:.6f}, "
        f"D+/sqrt={row['positive_discrepancy_over_sqrt']:.6f}, "
        f"prime_holes={row['prime_holes']}, top_q={row['top_q'][:3]}"
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 第P列锚点动态容量审计",
        "",
        "**状态：** `pcolumn_anchor_dynamic_capacity_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `include_square_plus`: `{params['include_square_plus']}`",
        "",
        "## 总表",
        "",
        "| P | cutoff | rows | low primes | high primes | H | min margin | max T/S | min model/sqrt | max D+/sqrt | C-window | min prime holes | cap fails | union fails |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {record['row_count']} | "
            f"{record['low_prime_count']} | {record['high_prime_count']} | "
            f"{record['harmonic']:.6f} | "
            f"{record['min_capacity_margin']} | {record['max_hit_ratio']:.6f} | "
            f"{record['min_model_over_sqrt']:.6f} | "
            f"{record['max_dplus_over_sqrt']:.6f} | "
            f"{record['sqrt_c_window']:.6f} | "
            f"{record['min_prime_holes']} | {record['capacity_failure_count']} | "
            f"{record['union_failure_count']} |"
        )

    for record in result["records"]:
        lines.extend(
            [
                "",
                f"## P={record['p']}",
                "",
                f"- `cutoff`: `{record['cutoff']}`",
                f"- `H=sum_{{P^alpha<q<P}}1/q`: `{record['harmonic']:.6f}`",
                f"- `min_capacity_margin`: `{record['min_capacity_margin']}`",
                f"- `max_hit_ratio`: `{record['max_hit_ratio']:.6f}`",
                f"- `min_model_over_sqrt`: `{record['min_model_over_sqrt']:.6f}`",
                f"- `max_dplus_over_sqrt`: `{record['max_dplus_over_sqrt']:.6f}`",
                f"- `sqrt_c_window`: `{record['sqrt_c_window']:.6f}`",
                f"- `min_prime_holes`: `{record['min_prime_holes']}`",
                "",
                "最小容量余量行：",
                "",
            ]
        )
        for row in record["tight_margin_rows"]:
            lines.append(f"- `{row_text(row)}`")
        lines.extend(["", "最大 T/S 行：", ""])
        for row in record["top_ratio_rows"]:
            lines.append(f"- `{row_text(row)}`")
        lines.extend(["", "最大相对正偏差行：", ""])
        for row in record["top_dplus_rows"]:
            lines.append(f"- `{row_text(row)}`")
        lines.extend(["", "最少素数洞行：", ""])
        for row in record["thin_prime_rows"]:
            lines.append(f"- `{row_text(row)}`")

    lines.extend(
        [
            "",
            "## 结构解释",
            "",
            "该审计是 `PColumn Anchor-Wheel Field` 的动态提升轮版本。对每个锚点行 `Py-d`，先提升全部 `q<=P^alpha`，得到动态粗骨架 `S_Y(P,y)`；再统计剩余 `P^alpha<q<P` 的总命中 `T_Y(P,y)`。若 `T_Y<S_Y`，则即使不利用重叠扣除，也不可能全覆盖该行骨架。",
            "",
            "相对筛余量写成 `S-T=S(1-H)-(T-HS)`，其中 `H=sum_{P^alpha<q<P}1/q`。表中的 `min model/sqrt` 是 `S(1-H)/sqrt(S)` 的最小值，`max D+/sqrt` 是 `max(0,T-HS)/sqrt(S)` 的最大值。若存在常数 `C` 落在二者之间，即 `D+<=C sqrt(S)<S(1-H)`，则解析上推出 `T<S`。",
            "",
            "因此若所有行均有正容量余量，说明第 `P` 列锚点场不仅有低模平移刚性，还满足一阶高素容量夹击。剩余证明任务是把 `T_Y<S_Y` 的样本余量升级为解析不等式，或把失败路由到 `PDEC/SAE/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="101,499,997,2003,5003")
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--include-square-plus", action="store_true", default=True)
    parser.add_argument(
        "--out-prefix",
        default="docs/pcolumn_anchor_dynamic_capacity_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.p_list), args.alpha, args.include_square_plus)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
