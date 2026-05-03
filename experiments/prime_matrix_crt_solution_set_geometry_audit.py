#!/usr/bin/env python3
"""CRT 零/非零同余解集几何审计。

用法示例：
  python3 experiments/prime_matrix_crt_solution_set_geometry_audit.py

本审计区分两层：
1. CRT 筛层：行 r 的非零同余幸存列 R(r)，只由模 ell<P 决定；
2. 数值层：幸存数 xP+c 是素数还是 P-rough 合数，依赖数值大小。

边界证明只能使用第 1 层的严格 CRT 几何加第 2 层的边界事实
“x<P 时幸存者自动为素数”。中区粗合数密集是数值层现象，
不能直接推出 CRT 筛层的边界零行不存在。
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


def is_prime(value: int) -> bool:
    """朴素素性测试，用于短块画像。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def build_masks(p: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算每个小素数模类覆盖列掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        residue_masks = [0] * prime
        inverse = pow(p, -1, prime)
        for col in range(1, p):
            row_residue = (1 - col * inverse) % prime
            residue_masks[row_residue] |= 1 << (col - 1)
        masks[prime] = residue_masks
    return masks


def row_cover_mask(row: int, masks: dict[int, list[int]], full_mask: int) -> int:
    """计算行覆盖掩码。"""
    mask = 0
    for prime, residue_masks in masks.items():
        mask |= residue_masks[row % prime]
        if mask == full_mask:
            break
    return mask


def survivor_cols(p: int, cover_mask: int) -> list[int]:
    """由覆盖掩码取幸存列。"""
    return [
        col + 1 for col in range(p - 1) if ((cover_mask >> col) & 1) == 0
    ]


def row_profile(p: int, base_primes: list[int], row: int, masks: dict[int, list[int]]) -> dict:
    """行画像：幸存列、素数幸存者、粗合数幸存者。"""
    full_mask = (1 << (p - 1)) - 1
    cover_mask = row_cover_mask(row, masks, full_mask)
    survivors = survivor_cols(p, cover_mask)
    survivor_items = []
    for col in survivors:
        value = (row - 1) * p + col
        survivor_items.append(
            {
                "col": col,
                "value": value,
                "is_prime": is_prime(value),
                "small_factor_check": [
                    prime for prime in base_primes if value % prime == 0
                ],
            }
        )
    return {
        "row": row,
        "survivor_count": len(survivors),
        "survivors": survivor_items,
        "prime_survivor_count": sum(1 for item in survivor_items if item["is_prime"]),
        "rough_composite_survivor_count": sum(
            1 for item in survivor_items if not item["is_prime"]
        ),
    }


def scan_counts(p: int) -> dict:
    """完整扫描 CRT 周期的行幸存数。"""
    base_primes = primes_upto(p - 1)
    row_period = prod(base_primes)
    masks = build_masks(p, base_primes)
    full_mask = (1 << (p - 1)) - 1
    counts = []
    zero_rows = []
    for row in range(1, row_period + 1):
        cover_mask = row_cover_mask(row, masks, full_mask)
        count = (p - 1) - cover_mask.bit_count()
        counts.append(count)
        if count == 0:
            zero_rows.append(row)
    mirror_ok = all(counts[row - 1] == counts[row_period - row] for row in range(1, row_period + 1))
    zero_mirror_ok = all((row_period - row + 1) in set(zero_rows) for row in zero_rows)
    boundary_rows = list(range(2, min(p, row_period) + 1))
    sample_rows = sorted(
        set(
            boundary_rows
            + [max(1, row_period // 2 - p), row_period // 2, min(row_period, row_period // 2 + p)]
            + list(range(max(1, row_period - p + 1), row_period + 1))
            + zero_rows[:3]
            + [row_period - row + 1 for row in zero_rows[:3]]
        )
    )
    return {
        "p": p,
        "row_period": row_period,
        "hist": dict(sorted(Counter(counts).items())),
        "min_count": min(counts),
        "max_count": max(counts),
        "zero_count": len(zero_rows),
        "first_zero_rows": zero_rows[:10],
        "mirror_count_ok": mirror_ok,
        "zero_mirror_ok": zero_mirror_ok,
        "front_counts": counts[:p],
        "boundary_counts_rows_2_to_p": counts[1:p],
        "middle_profiles": [
            row_profile(p, base_primes, row, masks)
            for row in sample_rows
            if abs(row - row_period // 2) <= p
        ],
        "front_profiles": [
            row_profile(p, base_primes, row, masks)
            for row in boundary_rows
        ],
        "zero_profiles": [
            row_profile(p, base_primes, row, masks) for row in zero_rows[:3]
        ],
    }


def run_audit() -> dict:
    """运行审计。"""
    results = [scan_counts(p) for p in (13, 17, 19, 23)]
    return {
        "certificate_type": "prime_matrix_crt_solution_set_geometry_audit",
        "status": "crt_mirror_exact_but_middle_rough_density_not_boundary_proof",
        "results": results,
        "structural_conclusion": (
            "CRT 筛幸存集合有精确镜像：R(N-r+1)=P-R(r)，所以零行镜像严格成立。"
            "但中区素数/粗合数密集是数值层现象，不是 CRT 行幸存数的单调势能；"
            "它不能单独推出边界零行不存在。"
        ),
        "next_obligations": [
            "把镜像作为两端帽约束使用，而不是短周期或单调密度证明。",
            "若要利用中区粗合数密集，必须先构造连接数值层与 CRT 筛层的势函数。",
            "主链继续回到 BPN 势函数或 GridPrimeGap 条件输入。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# CRT 零/非零同余解集几何审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 总表",
        "",
        "| P | N | hist | zero count | first zeros | mirror counts? | boundary counts rows 2..P |",
        "| ---: | ---: | --- | ---: | --- | --- | --- |",
    ]
    for item in audit["results"]:
        lines.append(
            "| {p} | {period} | `{hist}` | {zero_count} | `{zeros}` | {mirror} | `{front}` |".format(
                p=item["p"],
                period=item["row_period"],
                hist=item["hist"],
                zero_count=item["zero_count"],
                zeros=item["first_zero_rows"],
                mirror=item["mirror_count_ok"] and item["zero_mirror_ok"],
                front=item["boundary_counts_rows_2_to_p"],
            )
        )
    lines.extend(
        [
            "",
            "## 精确镜像引理",
            "",
            "令 `N=prod_{ell<P}ell`。若行 `r` 的幸存列集合为",
            "",
            "\\[",
            "R(r)=\\{1\\le c<P:( (r-1)P+c, N)=1\\},",
            "\\]",
            "",
            "则",
            "",
            "\\[",
            "R(N-r+1)=\\{P-c:c\\in R(r)\\}.",
            "\\]",
            "",
            "证明是取负映射：`(r-1)P+c` 变为 `NP-((r-1)P+c)=(N-r)P+(P-c)`。因此行幸存数和零行集合严格镜像。",
            "",
            "## 中区与边界的区别",
            "",
            "前窗口 `r<=P` 中，任何 CRT 幸存者都小于 `P^2`，所以自动为素数。中区幸存者只保证没有 `<P` 小因子，可能是素数，也可能是 `P`-rough 合数。故“中区粗合数密集”属于数值层，不能直接推出 CRT 筛层的边界非覆盖。",
            "",
            "## 样本画像",
            "",
        ]
    )
    for item in audit["results"]:
        lines.append(f"### P={item['p']} 边界窗口最薄行")
        best_front = min(item["front_profiles"], key=lambda row: row["survivor_count"])
        lines.append(
            f"- row={best_front['row']} survivors={best_front['survivor_count']} prime_survivors={best_front['prime_survivor_count']} rough_composites={best_front['rough_composite_survivor_count']} data=`{best_front['survivors']}`"
        )
        if item["middle_profiles"]:
            best_mid = min(item["middle_profiles"], key=lambda row: row["survivor_count"])
            lines.append(
                f"- middle sample row={best_mid['row']} survivors={best_mid['survivor_count']} prime_survivors={best_mid['prime_survivor_count']} rough_composites={best_mid['rough_composite_survivor_count']}"
            )
        lines.append("")
    lines.extend(["## 下一证明义务", ""])
    for obligation in audit["next_obligations"]:
        lines.append(f"- {obligation}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-crt-solution-set-geometry-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps({item["p"]: item["zero_count"] for item in audit["results"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
