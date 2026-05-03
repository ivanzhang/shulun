#!/usr/bin/env python3
"""审计零行在 2P 尺度内的复现间隔。

用法示例：
  python3 experiments/prime_matrix_short_recurrence_gap_audit.py

本脚本区分两个命题：
1. 全局短间隔命题：任意两个零行的循环距离都大于 2P；
2. 边界短间隔命题：首零行与末零行跨周期距离大于 2P-1。
第 1 个命题会被 P=23 反例否定；第 2 个命题等价于首零行大于 P。
"""

from __future__ import annotations

import json
from math import prod
from pathlib import Path


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]
P_VALUES = [5, 7, 11, 13, 17, 19, 23]


def primes_less_than(p: int) -> list[int]:
    """返回小于 p 的素数列表。"""
    return [prime for prime in PRIMES if prime < p]


def build_masks(p: int, base_primes: list[int]) -> dict[int, list[int]]:
    """预计算每个小素数模类覆盖的非平凡列掩码。"""
    masks: dict[int, list[int]] = {}
    for prime in base_primes:
        residue_masks = [0] * prime
        inverse = pow(p, -1, prime)
        for col in range(1, p):
            row_residue = (1 - col * inverse) % prime
            residue_masks[row_residue] |= 1 << (col - 1)
        masks[prime] = residue_masks
    return masks


def row_mask(row: int, masks: dict[int, list[int]], full_mask: int) -> int:
    """计算一行被旧小素数覆盖的非平凡列掩码。"""
    mask = 0
    for prime, residue_masks in masks.items():
        mask |= residue_masks[row % prime]
        if mask == full_mask:
            break
    return mask


def zero_rows_for_p(p: int) -> tuple[int, list[int]]:
    """完整扫描 p 的 CRT 行周期零行。"""
    base_primes = primes_less_than(p)
    row_period = prod(base_primes)
    full_mask = (1 << (p - 1)) - 1
    masks = build_masks(p, base_primes)
    zero_rows = [
        row
        for row in range(1, row_period + 1)
        if row_mask(row, masks, full_mask) == full_mask
    ]
    return row_period, zero_rows


def prefix_holes(p: int, row: int, prefix_primes: list[int]) -> list[dict]:
    """列出低素数前缀筛后剩余洞及最终小素因子。"""
    base_primes = primes_less_than(p)
    holes = []
    for col in range(1, p):
        value = (row - 1) * p + col
        if any(value % prime == 0 for prime in prefix_primes):
            continue
        final_factors = [prime for prime in base_primes if value % prime == 0]
        holes.append({"col": col, "final_factors": final_factors})
    return holes


def short_pair_details(p: int, pairs: list[tuple[int, int, int]]) -> list[dict]:
    """提取 P=23 短复现对的相位细节。"""
    if p != 23:
        return []
    details = []
    for left, right, gap in pairs[:20]:
        rows = []
        for row in (left, right):
            rows.append(
                {
                    "row": row,
                    "row_mod_210": row % 210,
                    "residues": {
                        str(prime): row % prime for prime in primes_less_than(p)
                    },
                    "holes_after_2_3_5_7": prefix_holes(p, row, [2, 3, 5, 7]),
                }
            )
        details.append({"left": left, "right": right, "gap": gap, "rows": rows})
    return details


def audit_p(p: int) -> dict:
    """审计单个 p 的短复现结构。"""
    row_period, zero_rows = zero_rows_for_p(p)
    if not zero_rows:
        return {
            "p": p,
            "row_period": row_period,
            "zero_count": 0,
            "status": "no_zero_rows_in_period",
        }
    gaps = [
        (left, right, right - left)
        for left, right in zip(zero_rows, zero_rows[1:])
    ]
    wrap_gap = zero_rows[0] + row_period - zero_rows[-1]
    cyclic_gaps = gaps + [(zero_rows[-1], zero_rows[0] + row_period, wrap_gap)]
    short_pairs = [item for item in cyclic_gaps if item[2] <= 2 * p]
    symmetry_ok = all((row_period - row + 1) in set(zero_rows) for row in zero_rows)
    return {
        "p": p,
        "row_period": row_period,
        "zero_count": len(zero_rows),
        "first_zero": zero_rows[0],
        "last_zero": zero_rows[-1],
        "wrap_gap": wrap_gap,
        "wrap_gap_formula_2_first_minus_1": 2 * zero_rows[0] - 1,
        "min_gap": min(item[2] for item in cyclic_gaps),
        "short_pair_threshold": 2 * p,
        "short_pair_count": len(short_pairs),
        "first_short_pairs": short_pairs[:20],
        "global_no_2p_recurrence": len(short_pairs) == 0,
        "boundary_no_2p_minus_1_recurrence": wrap_gap > 2 * p - 1,
        "first_zero_gt_p": zero_rows[0] > p,
        "symmetry_ok": symmetry_ok,
        "p23_short_pair_details": short_pair_details(p, short_pairs),
    }


def run_audit() -> dict:
    """运行全部审计。"""
    results = [audit_p(p) for p in P_VALUES]
    return {
        "certificate_type": "prime_matrix_short_recurrence_gap_audit",
        "status": "global_2p_gap_false_boundary_gap_equivalent_to_first_zero_delay",
        "results": results,
        "structural_conclusion": (
            "全局 2P 短复现禁止被 P=23 反例否定；可用弱化是边界跨周期短复现禁止，"
            "但该命题在反射对称下等价于首零行大于 P，不能作为独立证明出口。"
        ),
        "next_obligations": [
            "把目标改为首端帽/尾端帽的边界相位非覆盖，而不是全局短间隔非覆盖。",
            "证明低素数骨架在前 P 行必留洞，且高素数补洞 CRT 最小代表超过 P。",
            "将短复现簇作为远离边界的层级证书现象，接入 PDEC/SAE 账本。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写出 Markdown 审计报告。"""
    lines = [
        "# 零行 2P 短复现间隔审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 总表",
        "",
        "| P | row period | zero count | first zero | wrap gap | min gap | short pairs <=2P | global no <=2P? | boundary gap? |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for item in audit["results"]:
        if item["zero_count"] == 0:
            lines.append(
                f"| {item['p']} | {item['row_period']} | 0 | - | - | - | - | true | true |"
            )
            continue
        lines.append(
            "| {p} | {period} | {count} | {first} | {wrap} | {min_gap} | {shorts} | {global_ok} | {boundary_ok} |".format(
                p=item["p"],
                period=item["row_period"],
                count=item["zero_count"],
                first=item["first_zero"],
                wrap=item["wrap_gap"],
                min_gap=item["min_gap"],
                shorts=item["short_pair_count"],
                global_ok=item["global_no_2p_recurrence"],
                boundary_ok=item["boundary_no_2p_minus_1_recurrence"],
            )
        )
    lines.extend(
        [
            "",
            "## P=23 的全局短复现反例",
            "",
            "`P=23` 时 `2P=46`，完整周期内存在 `20` 对循环距离不超过 `46` 的零行。前若干对如下：",
            "",
            "| left row | right row | gap |",
            "| ---: | ---: | ---: |",
        ]
    )
    p23 = next(item for item in audit["results"] if item["p"] == 23)
    for left, right, gap in p23["first_short_pairs"]:
        lines.append(f"| {left} | {right} | {gap} |")
    lines.extend(
        [
            "",
            "因此，强命题“任意零行不可能在平移 `2P` 行内复现”是假的，不能作为闭合行命题的证明出口。",
            "",
            "## P=23 短复现对的相位画像",
            "",
            "短复现发生在周期内部远离边界处。它们不是同一个完整证书的平移，而是低素数相位部分同步、其余高素数标签重新补洞。",
            "",
        ]
    )
    for pair in p23["p23_short_pair_details"][:5]:
        lines.extend(
            [
                f"### gap {pair['gap']}: row {pair['left']} -> row {pair['right']}",
                "",
                "| row | row mod 210 | holes after 2,3,5,7 |",
                "| ---: | ---: | --- |",
            ]
        )
        for row in pair["rows"]:
            holes = ", ".join(
                f"c={hole['col']}:{hole['final_factors']}"
                for hole in row["holes_after_2_3_5_7"]
            )
            lines.append(
                f"| {row['row']} | {row['row_mod_210']} | `{holes}` |"
            )
        lines.append("")
    lines.extend(
        [
            "## 可用的弱化命题",
            "",
            "设零行集合在 CRT 行周期 `N` 中非空，首零行为 `r0`。由反射对称，末零行为 `N-r0+1`，所以跨周期首尾间隔为",
            "",
            "\\[",
            "r_0+N-(N-r_0+1)=2r_0-1.",
            "\\]",
            "",
            "因此",
            "",
            "\\[",
            "r_0>P \\quad\\Longleftrightarrow\\quad \\text{首尾跨周期间隔}>2P-1.",
            "\\]",
            "",
            "这说明“边界 `2P` 短复现禁止”是正确的目标表述，但它与“前 `P` 行无零行”同强，不能单独作为证明。真正应攻的是边界相位非覆盖：在 `r<=P` 的首端帽内，低素数骨架必留洞，且高素数补洞所需 CRT 最小代表必须超过 `P`。",
            "",
            "## 下一步义务",
            "",
        ]
    )
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = Path("docs/monograph/prime-matrix-short-recurrence-gap-audit")
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps(audit["results"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
