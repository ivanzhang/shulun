#!/usr/bin/env python3
"""完整扫描 P=23 的 CRT 行周期零行复现。

用法示例：
  python3 experiments/prime_matrix_p23_zero_recurrence_audit.py

本脚本验证第 59 行全覆盖是否在 CRT 镜像行之前真实复现，并分析复现间隔。
这里行号采用一编号：第 r 行为 [(r-1)P+1, rP]；因此第 59 行对应乘数 x=58。
"""

from __future__ import annotations

import json
from collections import Counter
from math import gcd, prod
from pathlib import Path


P = 23
PRIMES_LT_P = [2, 3, 5, 7, 11, 13, 17, 19]
PRIMES_LE_P = [*PRIMES_LT_P, P]
ROW_PERIOD = prod(PRIMES_LT_P)
FULL_MASK = (1 << (P - 1)) - 1


def factorize(value: int) -> list[int]:
    """朴素分解整数，用于报告小样本。"""
    factors = []
    n = value
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def build_masks() -> dict[int, list[int]]:
    """预计算每个小素数模类覆盖的非平凡列掩码。"""
    masks = {}
    for prime in PRIMES_LT_P:
        residue_masks = [0] * prime
        inverse = pow(P, -1, prime)
        for col in range(1, P):
            row_residue = (1 - col * inverse) % prime
            residue_masks[row_residue] |= 1 << (col - 1)
        masks[prime] = residue_masks
    return masks


def row_mask(row: int, masks: dict[int, list[int]]) -> int:
    """计算一行被旧小素数覆盖的非平凡列掩码。"""
    mask = 0
    for prime in PRIMES_LT_P:
        mask |= masks[prime][row % prime]
        if mask == FULL_MASK:
            break
    return mask


def scan_zero_rows() -> list[int]:
    """扫描完整 CRT 行周期中的零行。"""
    masks = build_masks()
    zero_rows = []
    for row in range(1, ROW_PERIOD + 1):
        if row_mask(row, masks) == FULL_MASK:
            zero_rows.append(row)
    return zero_rows


def row_profile(row: int) -> dict:
    """逐列列出一行的旧筛覆盖因子和未覆盖点。"""
    cells = []
    uncovered = []
    for col in range(1, P + 1):
        value = (row - 1) * P + col
        small_factors = [prime for prime in PRIMES_LE_P if value % prime == 0]
        if col < P and not small_factors:
            uncovered.append(
                {
                    "col": col,
                    "value": value,
                    "factorization": factorize(value),
                }
            )
        cells.append({"col": col, "value": value, "small_factors": small_factors})
    return {
        "row": row,
        "interval": [(row - 1) * P + 1, row * P],
        "is_zero": not uncovered,
        "uncovered": uncovered,
        "cells": cells,
    }


def residue_cover_profile(row: int) -> list[dict]:
    """列出每个小素数在该行覆盖的列。"""
    masks = build_masks()
    profile = []
    for prime in PRIMES_LT_P:
        mask = masks[prime][row % prime]
        cols = [col + 1 for col in range(P - 1) if (mask >> col) & 1]
        profile.append({"prime": prime, "row_residue": row % prime, "cols": cols})
    return profile


def uncovered_after_prefix(row: int, prefix_primes: list[int]) -> list[dict]:
    """列出只用一段小素数后仍未覆盖的列及最终补洞因子。"""
    holes = []
    for col in range(1, P):
        value = (row - 1) * P + col
        if any(value % prime == 0 for prime in prefix_primes):
            continue
        final_factors = [prime for prime in PRIMES_LT_P if value % prime == 0]
        holes.append({"col": col, "value": value, "final_factors": final_factors})
    return holes


def witness_profile(row: int) -> dict:
    """给出一行的最小见证因子和覆盖重数分布。"""
    witnesses = []
    multiplicity_counter: Counter[int] = Counter()
    least_factor_counter: Counter[str] = Counter()
    for col in range(1, P):
        value = (row - 1) * P + col
        factors = [prime for prime in PRIMES_LT_P if value % prime == 0]
        least_factor = factors[0] if factors else None
        multiplicity_counter[len(factors)] += 1
        least_factor_counter[str(least_factor)] += 1
        witnesses.append(
            {"col": col, "least_factor": least_factor, "small_factors": factors}
        )
    return {
        "row": row,
        "residues": {str(prime): row % prime for prime in PRIMES_LT_P},
        "multiplicity_hist": dict(sorted(multiplicity_counter.items())),
        "least_factor_counts": dict(sorted(least_factor_counter.items())),
        "witnesses": witnesses,
    }


def low_skeleton_summary(zero_rows: list[int], first_row: int, mirror_row: int) -> list[dict]:
    """统计第一个零行的低素数骨架在镜像前如何复现。"""
    rows_before_mirror = [row for row in zero_rows if row < mirror_row]
    summaries = []
    modulus = 1
    prefix: list[int] = []
    for prime in PRIMES_LT_P:
        prefix.append(prime)
        modulus *= prime
        matching = [
            row for row in rows_before_mirror if row % modulus == first_row % modulus
        ]
        summaries.append(
            {
                "prefix_primes": prefix[:],
                "modulus": modulus,
                "target_residue": first_row % modulus,
                "count_before_mirror": len(matching),
                "first_rows": matching[:8],
                "first_after_first_row": next(
                    (row for row in matching if row > first_row), None
                ),
            }
        )
    return summaries


def shift_checks(zero_set: set[int], first_row: int, first_recurrence: int) -> list[dict]:
    """检查围绕第一个零行的真实平移候选。"""
    candidates = [
        ("d=r", first_row),
        ("d=2r-1", 2 * first_row - 1),
        ("d=2r", 2 * first_row),
        ("d=first_real_recurrence-r", first_recurrence - first_row),
        ("d=same_2_3_5_7_skeleton-r", 6569 - first_row),
    ]
    checks = []
    for name, shift in candidates:
        row = first_row + shift
        profile = row_profile(row)
        checks.append(
            {
                "name": name,
                "shift": shift,
                "row": row,
                "is_zero": row in zero_set,
                "uncovered_cols": [item["col"] for item in profile["uncovered"]],
            }
        )
    return checks


def audit() -> dict:
    """执行 P=23 零行复现审计。"""
    zero_rows = scan_zero_rows()
    zero_set = set(zero_rows)
    first_row = 59
    mirror_row = ROW_PERIOD - first_row + 1
    recurrences_before_mirror = [
        row for row in zero_rows if first_row < row < mirror_row
    ]
    gaps = [b - a for a, b in zip(zero_rows, zero_rows[1:])]
    common_gaps = Counter(gaps).most_common(20)
    focus_rows = [first_row, 118, recurrences_before_mirror[0], mirror_row]
    return {
        "parameters": {
            "p": P,
            "row_period": ROW_PERIOD,
            "first_zero_row": first_row,
            "mirror_row": mirror_row,
        },
        "summary": {
            "zero_row_count": len(zero_rows),
            "zero_density": len(zero_rows) / ROW_PERIOD,
            "first_zero_row_is_zero": first_row in zero_set,
            "mirror_row_is_zero": mirror_row in zero_set,
            "recurrence_before_mirror_count": len(recurrences_before_mirror),
            "first_recurrence_before_mirror": recurrences_before_mirror[0],
            "first_recurrence_shift": recurrences_before_mirror[0] - first_row,
            "row_118_is_zero": 118 in zero_set,
            "min_gap": min(gaps),
            "max_gap": max(gaps),
            "common_gaps": common_gaps,
            "symmetry_ok": all((ROW_PERIOD - row + 1) in zero_set for row in zero_rows),
        },
        "first_zero_rows": zero_rows[:30],
        "last_zero_rows": zero_rows[-30:],
        "first_recurrences_before_mirror": recurrences_before_mirror[:60],
        "shift_checks": shift_checks(
            zero_set, first_row, recurrences_before_mirror[0]
        ),
        "low_skeleton_summary": low_skeleton_summary(
            zero_rows, first_row, mirror_row
        ),
        "focus_profiles": [row_profile(row) for row in focus_rows],
        "residue_cover_profiles": {
            str(row): residue_cover_profile(row)
            for row in (first_row, 118, 2612, 6569)
        },
        "witness_profiles": {
            str(row): witness_profile(row) for row in (first_row, 2612, 6569)
        },
        "prefix_hole_profiles": {
            str(row): uncovered_after_prefix(row, [2, 3, 5, 7])
            for row in (first_row, 2612, 5539, 5840, 6569)
        },
        "first_recurrence_gcd_with_period": gcd(
            ROW_PERIOD, recurrences_before_mirror[0] - first_row
        ),
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# P=23 全覆盖行复现审计",
        "",
        "**状态：** `complete_crt_period_scan_for_p23`",
        "",
        "## 总结",
        "",
        f"- `P`: `{params['p']}`。",
        f"- CRT 行周期 `N`: `{params['row_period']}`。",
        f"- 首个零行：`{params['first_zero_row']}`。",
        f"- 镜像零行：`{params['mirror_row']}`。",
        f"- 周期内零行总数：`{summary['zero_row_count']}`。",
        f"- 零行密度：`{summary['zero_density']}`。",
        f"- 镜像对称是否全成立：`{summary['symmetry_ok']}`。",
        f"- 第 `118=2*59` 行是否零行：`{summary['row_118_is_zero']}`。",
        f"- 镜像行之前复现次数：`{summary['recurrence_before_mirror_count']}`。",
        f"- 镜像行之前首次复现：`{summary['first_recurrence_before_mirror']}`。",
        f"- 首次复现平移：`{summary['first_recurrence_shift']}`。",
        f"- 首次复现平移与周期 gcd：`{result['first_recurrence_gcd_with_period']}`。",
        f"- 最小零行间隔：`{summary['min_gap']}`。",
        f"- 最大零行间隔：`{summary['max_gap']}`。",
        "",
        "## 真实平移候选检查",
        "",
        "| shift name | shift | target row | zero? | uncovered cols |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for item in result["shift_checks"]:
        lines.append(
            "| {name} | {shift} | {row} | {zero} | `{cols}` |".format(
                name=item["name"],
                shift=item["shift"],
                row=item["row"],
                zero=item["is_zero"],
                cols=item["uncovered_cols"],
            )
        )
    lines.extend(
        [
            "",
            "这说明 `r`、`2r-1`、`2r` 不是零行现象的自动复现周期；第一个真实复现平移是 `2553`，而同一 `2,3,5,7` 低素数骨架的第一个复现平移是 `6510`。",
            "",
        "## 前后零行",
        "",
        f"- 前 30 个零行：`{result['first_zero_rows']}`。",
        f"- 后 30 个零行：`{result['last_zero_rows']}`。",
        "",
        "## 镜像前首次复现",
        "",
        f"`{result['first_recurrences_before_mirror']}`",
        "",
        "## 常见间隔",
        "",
        "| gap | count |",
        "| ---: | ---: |",
    ]
    )
    for gap, count in summary["common_gaps"]:
        lines.append(f"| {gap} | {count} |")
    lines.extend(
        [
            "",
            "## 关键行画像",
            "",
            "| row | interval | zero? | uncovered nontrivial cells |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for profile in result["focus_profiles"]:
        uncovered = ", ".join(
            f"c={item['col']}:n={item['value']}={item['factorization']}"
            for item in profile["uncovered"]
        )
        lines.append(
            "| {row} | `{interval}` | {zero} | {uncovered} |".format(
                row=profile["row"],
                interval=profile["interval"],
                zero=profile["is_zero"],
                uncovered=uncovered or "none",
            )
        )
    lines.extend(
        [
            "",
            "## 小素数相位覆盖剖面",
            "",
            "每一行的全覆盖由各小素数在该行的模相位共同覆盖 22 个非平凡列。下面列出关键行中每个小素数负责覆盖的列。",
            "",
        ]
    )
    for row, profile in result["residue_cover_profiles"].items():
        lines.extend(
            [
                f"### row {row}",
                "",
                "| prime | row mod prime | covered cols |",
                "| ---: | ---: | --- |",
            ]
        )
        for item in profile:
            lines.append(
                f"| {item['prime']} | {item['row_residue']} | `{item['cols']}` |"
            )
        lines.append("")
    lines.extend(
        [
            "## 低素数骨架复现",
            "",
            "以第 `59` 行的相位为目标，逐步固定前缀小素数 `2,3,5,...` 的残基，统计镜像前仍是零行的复现数量。",
            "",
            "| fixed primes | modulus | residue | count before mirror | first rows | first after 59 |",
            "| --- | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in result["low_skeleton_summary"]:
        lines.append(
            "| `{primes}` | {modulus} | {residue} | {count} | `{rows}` | {first_after} |".format(
                primes=item["prefix_primes"],
                modulus=item["modulus"],
                residue=item["target_residue"],
                count=item["count_before_mirror"],
                rows=item["first_rows"],
                first_after=item["first_after_first_row"],
            )
        )
    lines.extend(
        [
            "",
            "关键事实：固定到 `2,3,5,7` 后，仍有 `324` 个镜像前零行，首个是 `6569`；固定到 `2,3,5,7,11,13,17` 后只剩第 `59` 行。这表明低素数给出粗骨架，高素数负责补洞，完整零行不是单一周期，而是层级 CRT 证书集合。",
            "",
            "## `2,3,5,7` 骨架后的补洞标签",
            "",
            "| row | row mod 210 | holes after 2,3,5,7 with final factors |",
            "| ---: | ---: | --- |",
        ]
    )
    for row, holes in result["prefix_hole_profiles"].items():
        rendered = ", ".join(
            f"c={item['col']}:{item['final_factors']}" for item in holes
        )
        lines.append(f"| {row} | {int(row) % 210} | `{rendered}` |")
    lines.extend(
        [
            "",
            "特别是第 `59` 行与第 `6569` 行同属 `mod 210` 的同一低骨架，`2,3,5,7` 后都只剩列 `5,9,15`。第 `59` 行用 `13,17,19` 依次补 `5,9,15`；第 `6569` 行用 `19,13,17` 补同三洞。这是“同骨架、高素数标签置换补洞”的真实复现机制。",
            "",
            "## 覆盖证书重数",
            "",
            "| row | residues | multiplicity hist | least-factor counts |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for row, profile in result["witness_profiles"].items():
        lines.append(
            f"| {row} | `{profile['residues']}` | `{profile['multiplicity_hist']}` | `{profile['least_factor_counts']}` |"
        )
    lines.extend(
        [
            "",
            "剖面显示：第 `59` 行由奇偶层、模 `3` 层、模 `5` 层和少数大一些的小素数精确补齐；第 `118` 行虽然也有奇偶层和模 `3` 层，但剩余偶数列 `2,8,10,16,20,22` 没被 `5,7,11,13,17,19` 补齐；第 `2612` 行则通过另一套截距相位重新补齐所有列。",
            "",
            "## 审稿解释",
            "",
            "第 `59` 行在镜像行之前确实大量复现；第一个真实复现是第 `2612` 行，而不是第 `118` 行。复现背后的本质不是短周期，而是 CRT 相位空间中存在多个不同覆盖证书点。每个零行是一个相位向量 `(r mod ell)_{ell<23}`，它使 22 个非平凡列都落入某些小素数的禁类。平移会重新组合全部截距相位；若新相位向量仍覆盖 22 列，就出现复现，但这不要求与原证书相同，也不要求形成等差周期。",
            "",
            "更精确地说，零行事件可分层写成“低素数粗骨架 + 高素数补洞标签”。低骨架会按小模数频繁复现，但高素数补洞标签只有在相位同时命中剩余洞时才闭合；这解释了为什么第 `59` 行能在镜像前复现很多次，却不按 `59` 或 `2*59` 短步长复现。",
            "",
            "因此可用的证明支撑是：零行复现集合是 CRT 相位空间中的稀疏覆盖证书集，具有反射对称、层级骨架和高素数补洞置换，但间隔不规则。若反例要求某种短平移稳定，就必须额外证明稳定性；一旦有稳定性，就进入 `gcd(N,d)>=r` 的强限制。否则只能把复现当作稀疏相位点，接入 `PDEC/SAE` 的缺陷账本。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    result = audit()
    prefix = Path("docs/monograph/prime-matrix-p23-zero-recurrence-audit")
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
