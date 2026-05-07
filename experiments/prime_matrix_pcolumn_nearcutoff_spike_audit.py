#!/usr/bin/env python3
"""审计第 P 列动态容量中的近截止锚峰。

用法示例：
  python3 experiments/prime_matrix_pcolumn_nearcutoff_spike_audit.py \
    --p-list 5003,10007,20011,50021,100003 \
    --alpha 0.43 \
    --y-factor 4 \
    --out-prefix docs/pcolumn_nearcutoff_spike_audit_20260506

目标：
  只扫描 y <= y_factor * P^alpha 的近截止行，分解 q≈P^alpha
  第一批高素造成的 T/S 峰值、相对正偏差和重叠。
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
    """标记 Py-d 避开低素的动态骨架，索引 d。"""
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


def band_key(q: int, cutoff: int) -> str:
    """按 q/Y 的比例给高素分桶。"""
    ratio = q / cutoff
    if ratio <= 1.25:
        return "(1,1.25]Y"
    if ratio <= 1.5:
        return "(1.25,1.5]Y"
    if ratio <= 2:
        return "(1.5,2]Y"
    if ratio <= 3:
        return "(2,3]Y"
    if ratio <= 5:
        return "(3,5]Y"
    if ratio <= 10:
        return "(5,10]Y"
    return ">10Y"


def empty_band() -> dict:
    """创建分桶累计行。"""
    return {
        "q_count": 0,
        "harmonic": 0.0,
        "hits": 0,
        "expected": 0.0,
        "discrepancy": 0.0,
    }


def audit_row(
    p: int,
    y: int,
    cutoff: int,
    low_primes: list[int],
    high_primes: list[int],
    harmonic: float,
) -> dict:
    """审计一个近截止行。"""
    alive = mark_low_skeleton(p, y, low_primes)
    skeleton = sum(alive)
    sqrt_skeleton = math.sqrt(skeleton) if skeleton else 0.0
    anchor = p * y
    total_hits = 0
    covered_multiplicity = bytearray(p)
    top_q = []
    bands: dict[str, dict] = {}

    for q in high_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        hits = 0
        if start < p:
            for d in range(start, p, q):
                if not alive[d]:
                    continue
                hits += 1
                covered_multiplicity[d] += 1
        expected = skeleton / q if skeleton else 0.0
        key = band_key(q, cutoff)
        bucket = bands.setdefault(key, empty_band())
        bucket["q_count"] += 1
        bucket["harmonic"] += 1.0 / q
        bucket["hits"] += hits
        bucket["expected"] += expected
        bucket["discrepancy"] += hits - expected
        if hits:
            top_q.append(
                {
                    "q": q,
                    "hit_count": hits,
                    "expected": expected,
                    "excess": hits - expected,
                    "q_over_cutoff": q / cutoff,
                    "q_minus_y": q - y,
                    "divides_y": y % q == 0,
                    "residue": residue,
                    "start": start,
                }
            )
        total_hits += hits

    covered_count = sum(1 for d in range(1, p) if covered_multiplicity[d])
    max_multiplicity = max(covered_multiplicity) if p else 0
    overlap = total_hits - covered_count
    prime_holes = skeleton - covered_count
    expected_total = harmonic * skeleton
    dplus = max(0.0, total_hits - expected_total)
    model_gap = skeleton * (1.0 - harmonic)

    band_rows = []
    for key, bucket in bands.items():
        positive = max(0.0, bucket["discrepancy"])
        band_rows.append(
            {
                "band": key,
                "q_count": bucket["q_count"],
                "harmonic": bucket["harmonic"],
                "hits": bucket["hits"],
                "expected": bucket["expected"],
                "discrepancy": bucket["discrepancy"],
                "positive_discrepancy": positive,
                "hit_share": total_hits and bucket["hits"] / total_hits,
                "positive_over_sqrt": positive / sqrt_skeleton
                if sqrt_skeleton
                else 0.0,
            }
        )
    band_rows.sort(key=lambda row: -row["positive_discrepancy"])

    return {
        "x": y - 1,
        "y": y,
        "skeleton_count": skeleton,
        "total_high_hits": total_hits,
        "covered_count": covered_count,
        "overlap": overlap,
        "overlap_ratio": overlap / total_hits if total_hits else 0.0,
        "max_multiplicity": int(max_multiplicity),
        "capacity_margin": skeleton - total_hits,
        "hit_ratio": total_hits / skeleton if skeleton else 0.0,
        "union_ratio": covered_count / skeleton if skeleton else 0.0,
        "prime_holes": prime_holes,
        "harmonic": harmonic,
        "expected_high_hits": expected_total,
        "positive_discrepancy": dplus,
        "model_gap": model_gap,
        "positive_discrepancy_over_sqrt": dplus / sqrt_skeleton
        if sqrt_skeleton
        else 0.0,
        "model_gap_over_sqrt": model_gap / sqrt_skeleton
        if sqrt_skeleton
        else 0.0,
        "top_q": sorted(top_q, key=lambda row: -row["hit_count"])[:12],
        "bands_by_positive_discrepancy": band_rows,
    }


def audit_p(p: int, alpha: float, y_factor: float, primes: list[int]) -> dict:
    """审计一个 P 的近截止区域。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    harmonic = sum(1.0 / q for q in high_primes)
    y_limit = min(p + 1, max(2, int(math.ceil(y_factor * cutoff))))
    rows = [
        audit_row(p, y, cutoff, low_primes, high_primes, harmonic)
        for y in range(2, y_limit + 1)
    ]
    best_ratio = max(rows, key=lambda row: row["hit_ratio"])
    best_dplus = max(rows, key=lambda row: row["positive_discrepancy_over_sqrt"])
    best_margin = min(rows, key=lambda row: row["capacity_margin"])
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "harmonic": harmonic,
        "y_factor": y_factor,
        "y_limit": y_limit,
        "row_count": len(rows),
        "low_prime_count": len(low_primes),
        "high_prime_count": len(high_primes),
        "best_ratio_row": best_ratio,
        "best_dplus_row": best_dplus,
        "best_margin_row": best_margin,
        "top_ratio_rows": sorted(rows, key=lambda row: -row["hit_ratio"])[:8],
    }


def audit(p_list: list[int], alpha: float, y_factor: float) -> dict:
    """执行近截止锚峰审计。"""
    primes = primes_from_flags(sieve_bool(max(p_list)))
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "y_factor": y_factor,
        },
        "records": [audit_p(p, alpha, y_factor, primes) for p in p_list],
    }


def row_compact(row: dict) -> str:
    """压缩展示一条行记录。"""
    return (
        f"y={row['y']}, S={row['skeleton_count']}, T={row['total_high_hits']}, "
        f"margin={row['capacity_margin']}, T/S={row['hit_ratio']:.6f}, "
        f"U/S={row['union_ratio']:.6f}, overlap/T={row['overlap_ratio']:.6f}, "
        f"D+/sqrt={row['positive_discrepancy_over_sqrt']:.6f}, "
        f"holes={row['prime_holes']}, top_q={row['top_q'][:4]}"
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 第P列近截止锚峰审计",
        "",
        "**状态：** `nearcutoff_spike_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `y_factor`: `{params['y_factor']}`",
        "",
        "## 总表",
        "",
        "| P | cutoff | y_limit | best y | S | T | margin | T/S | U/S | overlap/T | D+/sqrt | model/sqrt | holes | top q |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in result["records"]:
        row = record["best_ratio_row"]
        top_q = ",".join(str(item["q"]) for item in row["top_q"][:4])
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {record['y_limit']} | "
            f"{row['y']} | {row['skeleton_count']} | {row['total_high_hits']} | "
            f"{row['capacity_margin']} | {row['hit_ratio']:.6f} | "
            f"{row['union_ratio']:.6f} | {row['overlap_ratio']:.6f} | "
            f"{row['positive_discrepancy_over_sqrt']:.6f} | "
            f"{row['model_gap_over_sqrt']:.6f} | {row['prime_holes']} | "
            f"`{top_q}` |"
        )

    for record in result["records"]:
        row = record["best_ratio_row"]
        lines.extend(
            [
                "",
                f"## P={record['p']}",
                "",
                f"- `cutoff`: `{record['cutoff']}`",
                f"- `H`: `{record['harmonic']:.6f}`",
                f"- `y_limit`: `{record['y_limit']}`",
                "",
                "最强 T/S 行：",
                "",
                f"- `{row_compact(row)}`",
                "",
                "正偏差最高分桶：",
                "",
                "| band | q count | harmonic | hits | expected | discrepancy | hit share | D+ / sqrt |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for band in row["bands_by_positive_discrepancy"][:8]:
            lines.append(
                f"| `{band['band']}` | {band['q_count']} | "
                f"{band['harmonic']:.6f} | {band['hits']} | "
                f"{band['expected']:.3f} | {band['discrepancy']:.3f} | "
                f"{band['hit_share']:.6f} | "
                f"{band['positive_over_sqrt']:.6f} |"
            )
        lines.extend(["", "近截止 top rows：", ""])
        for item in record["top_ratio_rows"]:
            lines.append(f"- `{row_compact(item)}`")

    lines.extend(
        [
            "",
            "## 结构解释",
            "",
            "该审计只看 `y<=y_factor*P^alpha` 的近截止区。若最强 `T/S` 行由 `q≈P^alpha` 的第一批高素主导，则它是 `NearCutoff Anchor Spike`。表中的 `U/S` 是实际并集覆盖率，`overlap/T` 是总命中中被重叠消耗的比例。",
            "",
            "若未来出现 `T>=S`，仅靠一阶容量不再够用；但若同一近截止峰仍有大 `overlap/T`，则可转入强制重叠证书。若它同时高命中且低重叠，就不再是普通筛余误差，而应进入 `PDEC/SAE/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="5003,10007,20011,50021,100003")
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--y-factor", type=float, default=4.0)
    parser.add_argument(
        "--out-prefix",
        default="docs/pcolumn_nearcutoff_spike_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.p_list), args.alpha, args.y_factor)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
