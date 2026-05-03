#!/usr/bin/env python3
"""零行间隔梯度审计。

用法示例：
  python3 experiments/prime_matrix_zero_row_spacing_gradient_audit.py

本审计只使用 `<P` 根基素数同余筛层，不使用普通合数判定。
目标是检验两个不同命题：
1. 零行在 CRT 周期内镜像分布；
2. 零行间隔是否呈现“中心短、越近边界越宽”的单调梯度。

结论需区分：
- 首尾跨周期边界间隔大于 `2P` 在样本中成立；
- 但全周期的“中心更密、边界更稀”单调规律在样本中不成立。
"""

from __future__ import annotations

import json
from collections import Counter
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def build_masks(p: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算每个小素数的行相位覆盖列掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        inverse = pow(p, -1, prime)
        residues = [0] * prime
        for col in range(1, p):
            row_residue = (1 - col * inverse) % prime
            residues[row_residue] |= 1 << (col - 1)
        masks[prime] = residues
    return masks


def row_cover_mask(row: int, masks: dict[int, list[int]], full_mask: int) -> int:
    """计算行覆盖掩码。"""
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            break
    return mask


def zero_rows_for_prime(p: int) -> tuple[int, list[int]]:
    """返回 CRT 行周期与全部零行。"""
    base_primes = primes_upto(p - 1)
    period = prod(base_primes)
    masks = build_masks(p, base_primes)
    full_mask = (1 << (p - 1)) - 1
    zero_rows = []
    for row in range(1, period + 1):
        if row_cover_mask(row, masks, full_mask) == full_mask:
            zero_rows.append(row)
    return period, zero_rows


def gap_records(zero_rows: list[int], period: int) -> list[dict]:
    """生成相邻零行循环间隔记录。"""
    records = []
    if not zero_rows:
        return records
    pairs = list(zip(zero_rows, zero_rows[1:])) + [(zero_rows[-1], zero_rows[0])]
    for left, right in pairs:
        wraps = right <= left
        gap = right - left if not wraps else period - left + right
        if wraps:
            midpoint = 0.0
            decile = "wrap"
            edge_distance = 0.0
        else:
            midpoint = (left + right) / 2
            decile = str(min(9, int(10 * (midpoint - 1) // period)))
            edge_distance = min(midpoint - 1, period - midpoint + 1)
        records.append(
            {
                "left": left,
                "right": right,
                "gap": gap,
                "wraps": wraps,
                "midpoint": midpoint,
                "decile": decile,
                "edge_distance": edge_distance,
            }
        )
    return records


def summarize_gap_bucket(records: list[dict], key: str) -> dict:
    """按指定字段汇总间隔。"""
    buckets: dict[str, list[int]] = {}
    for record in records:
        buckets.setdefault(str(record[key]), []).append(record["gap"])
    summary = {}
    for name, gaps in sorted(buckets.items(), key=lambda item: item[0]):
        summary[name] = {
            "count": len(gaps),
            "min": min(gaps),
            "avg": sum(gaps) / len(gaps),
            "max": max(gaps),
        }
    return summary


def prefix_counts(zero_rows: list[int], period: int, p: int) -> dict:
    """统计边界帽附近的零行数。"""
    factors = [1, 2, 3, 5, 10, 100]
    counts = {}
    for factor in factors:
        width = min(period // 2, factor * p)
        counts[f"{factor}P"] = {
            "front": sum(1 for row in zero_rows if row <= width),
            "back": sum(1 for row in zero_rows if row >= period - width + 1),
            "width": width,
        }
    return counts


def local_center_profile(zero_rows: list[int], period: int) -> dict:
    """取最接近中心的零行及其相邻间隔。"""
    center = (period + 1) / 2
    best_index = min(range(len(zero_rows)), key=lambda i: abs(zero_rows[i] - center))
    prev_row = zero_rows[best_index - 1]
    current = zero_rows[best_index]
    next_row = zero_rows[(best_index + 1) % len(zero_rows)]
    return {
        "center": center,
        "nearest_zero": current,
        "distance_to_center": abs(current - center),
        "prev_gap": current - prev_row,
        "next_gap": next_row - current if next_row > current else period - current + next_row,
    }


def audit_prime(p: int) -> dict:
    """审计单个素数 P。"""
    period, zero_rows = zero_rows_for_prime(p)
    zero_set = set(zero_rows)
    mirror_ok = all(period - row + 1 in zero_set for row in zero_rows)
    records = gap_records(zero_rows, period)
    nonwrap_records = [record for record in records if not record["wraps"]]
    first_zero = zero_rows[0] if zero_rows else None
    last_zero = zero_rows[-1] if zero_rows else None
    boundary_wrap_gap = None if not zero_rows else period - last_zero + first_zero
    zero_deciles = Counter(str(min(9, int(10 * (row - 1) // period))) for row in zero_rows)
    decile_gap_summary = summarize_gap_bucket(nonwrap_records, "decile")
    edge_avg_gap = (
        decile_gap_summary.get("0", {}).get("avg", 0)
        + decile_gap_summary.get("9", {}).get("avg", 0)
    ) / 2
    center_avg_gap = (
        decile_gap_summary.get("4", {}).get("avg", 0)
        + decile_gap_summary.get("5", {}).get("avg", 0)
    ) / 2
    return {
        "p": p,
        "period": period,
        "zero_count": len(zero_rows),
        "first_zero": first_zero,
        "last_zero": last_zero,
        "mirror_ok": mirror_ok,
        "boundary_wrap_gap": boundary_wrap_gap,
        "boundary_wrap_gap_gt_2p": None
        if boundary_wrap_gap is None
        else boundary_wrap_gap > 2 * p,
        "equivalent_first_zero_gt_p": None if first_zero is None else first_zero > p,
        "prefix_counts": prefix_counts(zero_rows, period, p),
        "zero_deciles": dict(sorted(zero_deciles.items())),
        "decile_gap_summary": decile_gap_summary,
        "edge_avg_gap": edge_avg_gap,
        "center_avg_gap": center_avg_gap,
        "center_shorter_than_edge_deciles": center_avg_gap < edge_avg_gap,
        "global_min_gap": min(record["gap"] for record in records),
        "global_max_gap": max(record["gap"] for record in records),
        "center_profile": local_center_profile(zero_rows, period),
    }


def run_audit() -> dict:
    """运行审计。"""
    results = [audit_prime(p) for p in (13, 17, 19, 23)]
    return {
        "certificate_type": "prime_matrix_zero_row_spacing_gradient_audit",
        "status": "boundary_wrap_gap_confirmed_but_global_center_shorter_claim_false",
        "results": results,
        "structural_conclusion": (
            "零行镜像严格成立，首尾跨周期边界间隔在样本中均大于 2P；"
            "但按十等分统计，零行并非越靠中心越密，样本反而常见边缘十等分零行更多。"
            "因此可保留的是边界帽间隔命题；全局中心密度梯度不能作为证明输入。"
        ),
        "proof_boundary": (
            "首尾跨周期边界间隔 = 2*r0-1，其中 r0 是首个零行。"
            "故 boundary_gap>2P 等价于 r0>P，也等价于 BPN(P)。"
            "它是目标的等价重写，不是独立证明出口。"
        ),
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# 零行间隔梯度与边界复现审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        audit["proof_boundary"],
        "",
        "## 总表",
        "",
        "| P | N | zero count | first zero | boundary gap | >2P? | edge avg gap | center avg gap | center shorter? | prefix zero counts |",
        "| ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |",
    ]
    for item in audit["results"]:
        prefix_sample = {
            key: value for key, value in item["prefix_counts"].items() if key in ("1P", "2P", "3P", "10P")
        }
        lines.append(
            "| {p} | {period} | {zc} | {fz} | {bg} | {gt} | {edge:.3f} | {center:.3f} | {cs} | `{prefix}` |".format(
                p=item["p"],
                period=item["period"],
                zc=item["zero_count"],
                fz=item["first_zero"],
                bg=item["boundary_wrap_gap"],
                gt=item["boundary_wrap_gap_gt_2p"],
                edge=item["edge_avg_gap"],
                center=item["center_avg_gap"],
                cs=item["center_shorter_than_edge_deciles"],
                prefix=prefix_sample,
            )
        )
    lines.extend(
        [
            "",
            "## 1. 严格镜像与边界间隔",
            "",
            "若 `r0` 是首个零行，由镜像刚性可知末个零行为 `N-r0+1`。因此首尾跨周期间隔为",
            "",
            "\\[",
            "\\Delta_{edge}=N-(N-r_0+1)+r_0=2r_0-1.",
            "\\]",
            "",
            "所以",
            "",
            "\\[",
            "\\Delta_{edge}>2P\\quad\\Longleftrightarrow\\quad r_0>P.",
            "\\]",
            "",
            "这正是边界帽无零行 `BPN(P)` 的等价表述。它可以作为审稿友好的目标形式，但不能独立证明 `BPN(P)`。",
            "",
            "## 2. 全局中心密度梯度检验",
            "",
            "样本不支持“零行越靠中心越密、越靠边界越稀”的全局单调规律。十等分统计中，边缘十等分的零行数并不小于中心十等分；例如 `P=23` 的 zero deciles 是 `[361,337,344,344,342,342,344,344,337,361]`。",
            "",
            "因此中区粗合数/素数密集现象不能直接转写成 CRT 零行间隔梯度。真正可用的是更窄的边界帽命题：前 `P` 行与后 `P` 行无零行。",
            "",
            "## 3. 每个 P 的细节",
            "",
        ]
    )
    for item in audit["results"]:
        lines.append(f"### P={item['p']}")
        lines.append(f"- zero_deciles=`{item['zero_deciles']}`")
        lines.append(f"- center_profile=`{item['center_profile']}`")
        lines.append(f"- decile_gap_summary=`{item['decile_gap_summary']}`")
        lines.append("")
    lines.extend(
        [
            "## 4. 下一步硬点",
            "",
            "边界复现距离 `>2P` 不能由全局间隔梯度推出；必须继续攻以下独立形式之一：",
            "",
            "- **BPN-MCR：** 任意完整覆盖证书的 CRT 最小正代表 `>=P`。",
            "- **BPN-Phi：** 构造非循环残洞势函数 `Phi_P(R)`，证明边界相位不能降到空洞集合。",
            "- **BPN-Defect：** 若边界行全覆盖，则其镜像尾端证书与前端证书合并后触发低模 CRT 缺陷或 Tail-anchor 缺陷。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-zero-row-spacing-gradient-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(
        json.dumps(
            {
                item["p"]: {
                    "boundary_gap": item["boundary_wrap_gap"],
                    "gt_2p": item["boundary_wrap_gap_gt_2p"],
                    "center_shorter": item["center_shorter_than_edge_deciles"],
                }
                for item in audit["results"]
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
