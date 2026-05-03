#!/usr/bin/env python3
"""生成 BPN-PDEC 的真实结构约束行。

用法示例：
  python3 experiments/prime_matrix_bpn_pdec_real_constraint_rows.py
  python3 experiments/prime_matrix_bpn_pdec_real_constraint_rows.py --p 23 --q 210

说明：
- 本脚本枚举 `<P` 根基素数 CRT 周期中的真实零行；
- 将零行投影到低模相位 `row mod Q`；
- 输出可进入 PDEC-Dual-Cert 的真实系数与界值；
- 默认输出是有限 CRT 枚举约束，不是无限族无条件证明。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from math import prod
from pathlib import Path
from typing import Any


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
    """预计算每个根基素数在每个行相位覆盖的列掩码。"""
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
    """返回指定行被根基素数覆盖的非平凡列掩码。"""
    mask = 0
    for prime, residues in masks.items():
        mask |= residues[row % prime]
        if mask == full_mask:
            break
    return mask


def low_skeleton_holes_by_phase(
    p: int,
    q: int,
    low_primes: list[int],
    full_mask: int,
) -> list[int]:
    """计算每个 Q 相位下仅由 low_primes 覆盖后剩余的洞数。"""
    masks = build_masks(p, low_primes)
    holes = []
    for phase in range(q):
        mask = row_cover_mask(phase, masks, full_mask)
        holes.append((p - 1) - mask.bit_count())
    return holes


def unit_coeff(index: int, length: int) -> list[float]:
    """生成标准基系数。"""
    return [1.0 if pos == index else 0.0 for pos in range(length)]


def pair_coeff(left: int, right: int, length: int) -> list[float]:
    """生成两个相位的成对容量系数。"""
    coeffs = [0.0] * length
    coeffs[left] += 1.0
    coeffs[right] += 1.0
    return coeffs


def mirror_coeff(left: int, right: int, length: int) -> list[float]:
    """生成镜像等式 g(left)-g(right)=0 的系数。"""
    coeffs = [0.0] * length
    coeffs[left] += 1.0
    coeffs[right] -= 1.0
    return coeffs


def scan_zero_rows(p: int, q: int) -> dict[str, Any]:
    """扫描真实零行并生成低模相位统计。"""
    base_primes = primes_upto(p - 1)
    period = prod(base_primes)
    if period % q != 0:
        raise ValueError("q 必须整除 `<P` 根基素数 CRT 周期，才能使用镜像相位公式")
    full_mask = (1 << (p - 1)) - 1
    masks = build_masks(p, base_primes)
    phase_counts = [0] * q
    first_zero_rows: list[int] = []
    zero_count = 0
    for row in range(1, period + 1):
        if row_cover_mask(row, masks, full_mask) == full_mask:
            zero_count += 1
            phase_counts[row % q] += 1
            if len(first_zero_rows) < 20:
                first_zero_rows.append(row)

    low_primes = [prime for prime in base_primes if q % prime == 0]
    low_holes = low_skeleton_holes_by_phase(p, q, low_primes, full_mask)
    low_hole_hist = Counter()
    zero_by_low_holes = Counter()
    for phase, holes in enumerate(low_holes):
        low_hole_hist[holes] += 1
        zero_by_low_holes[holes] += phase_counts[phase]

    mirror_map = [(1 - phase) % q for phase in range(q)]
    mirror_mismatch = [
        {
            "phase": phase,
            "mirror": mirror_map[phase],
            "count": phase_counts[phase],
            "mirror_count": phase_counts[mirror_map[phase]],
        }
        for phase in range(q)
        if phase_counts[phase] != phase_counts[mirror_map[phase]]
    ]

    return {
        "p": p,
        "q": q,
        "base_primes": base_primes,
        "low_primes_dividing_q": low_primes,
        "period": period,
        "zero_count": zero_count,
        "phase_counts": phase_counts,
        "nonzero_phase_count": sum(1 for value in phase_counts if value),
        "first_zero_rows": first_zero_rows,
        "mirror_map_formula": "rho(t)=(1-t) mod Q",
        "mirror_mismatch_count": len(mirror_mismatch),
        "mirror_mismatch_examples": mirror_mismatch[:10],
        "low_holes_by_phase": low_holes,
        "low_hole_hist": dict(sorted(low_hole_hist.items())),
        "zero_by_low_holes": dict(sorted(zero_by_low_holes.items())),
    }


def build_constraint_rows(scan: dict[str, Any], include_full_coeffs: bool) -> dict[str, Any]:
    """从扫描结果生成真实约束行。"""
    q = int(scan["q"])
    phase_counts = [int(value) for value in scan["phase_counts"]]
    low_holes = [int(value) for value in scan["low_holes_by_phase"]]

    inequalities = []
    for phase, count in enumerate(phase_counts):
        row = {
            "name": f"phase_cap_{phase}",
            "source": "finite_crt_zero_row_projection",
            "phase": phase,
            "bound": float(count),
        }
        if include_full_coeffs:
            row["coeffs"] = unit_coeff(phase, q)
        inequalities.append(row)

    seen_pairs: set[tuple[int, int]] = set()
    mirror_pair_caps = []
    mirror_equalities = []
    for phase in range(q):
        mirror = (1 - phase) % q
        pair = tuple(sorted((phase, mirror)))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)
        pair_bound = float(phase_counts[phase] + (0 if mirror == phase else phase_counts[mirror]))
        pair_row = {
            "name": f"mirror_pair_cap_{pair[0]}_{pair[1]}",
            "source": "finite_crt_mirror_pair_capacity",
            "phases": list(pair),
            "bound": pair_bound,
        }
        if include_full_coeffs:
            pair_row["coeffs"] = pair_coeff(pair[0], pair[1], q)
        mirror_pair_caps.append(pair_row)
        if mirror != phase:
            eq_row = {
                "name": f"mirror_eq_{pair[0]}_{pair[1]}",
                "source": "mirror_closed_full_zero_row_family_only",
                "phases": [phase, mirror],
                "value": 0.0,
            }
            if include_full_coeffs:
                eq_row["coeffs"] = mirror_coeff(phase, mirror, q)
            mirror_equalities.append(eq_row)

    low_hole_bucket_caps = []
    for threshold in sorted(set(low_holes)):
        phases = [phase for phase, holes in enumerate(low_holes) if holes >= threshold]
        bound = float(sum(phase_counts[phase] for phase in phases))
        row = {
            "name": f"low_hole_ge_{threshold}",
            "source": "finite_crt_low_skeleton_pressure_bucket",
            "threshold": threshold,
            "phase_count": len(phases),
            "bound": bound,
        }
        if include_full_coeffs:
            coeffs = [0.0] * q
            for phase in phases:
                coeffs[phase] = 1.0
            row["coeffs"] = coeffs
        low_hole_bucket_caps.append(row)

    mass_equality = {
        "name": "all_zero_rows_mass",
        "source": "finite_crt_full_zero_row_family",
        "value": float(scan["zero_count"]),
    }
    if include_full_coeffs:
        mass_equality["coeffs"] = [1.0] * q

    return {
        "constraint_type": "prime_matrix_bpn_pdec_real_constraint_rows",
        "p": scan["p"],
        "q": q,
        "interpretation": (
            "这些约束来自有限 CRT 周期中真实零行投影。phase_cap 对任何零行子族安全；"
            "mass 与 mirror_eq 只对完整零行族或已证明 mirror-closed 的坏窗族安全。"
        ),
        "inequalities": inequalities,
        "mirror_pair_caps": mirror_pair_caps,
        "low_hole_bucket_caps": low_hole_bucket_caps,
        "equalities": [mass_equality],
        "conditional_equalities": mirror_equalities,
    }


def compact_constraints_for_markdown(constraints: dict[str, Any]) -> dict[str, Any]:
    """提取 Markdown 使用的紧凑约束摘要。"""
    inequalities = constraints["inequalities"]
    nonzero_caps = [
        {"phase": row["phase"], "bound": row["bound"]}
        for row in inequalities
        if row["bound"] > 0
    ]
    top_caps = sorted(nonzero_caps, key=lambda item: item["bound"], reverse=True)[:12]
    return {
        "nonzero_phase_caps": len(nonzero_caps),
        "top_phase_caps": top_caps,
        "low_hole_bucket_caps": constraints["low_hole_bucket_caps"],
        "mass_equality": constraints["equalities"][0],
        "conditional_mirror_equalities": len(constraints["conditional_equalities"]),
    }


def run(p: int, q: int, include_full_coeffs: bool) -> dict[str, Any]:
    """运行约束行生成。"""
    scan = scan_zero_rows(p, q)
    constraints = build_constraint_rows(scan, include_full_coeffs)
    return {
        "certificate_type": "prime_matrix_bpn_pdec_real_constraint_rows",
        "status": "finite_crt_real_constraint_rows_generated",
        "scan": scan,
        "constraints": constraints,
        "compact": compact_constraints_for_markdown(constraints),
        "review_conclusion": (
            "本报告开始填入真实结构约束行：phase cap、mirror pair cap、mass、"
            "low-hole bucket 均来自完整 CRT 周期枚举。它们是有限样本的真实系数和界值；"
            "无条件证明仍需把这些有限枚举约束替换为符号化结构定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    scan = result["scan"]
    compact = result["compact"]
    lines = [
        "# BPN-PDEC 真实结构约束行生成报告",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. CRT 扫描摘要",
        "",
        f"- `P={scan['p']}`，`Q={scan['q']}`。",
        f"- 根基素数 `{scan['base_primes']}`。",
        f"- `Q` 中低素数 `{scan['low_primes_dividing_q']}`。",
        f"- CRT 行周期 `{scan['period']}`。",
        f"- 真实零行数 `{scan['zero_count']}`，非零相位数 `{scan['nonzero_phase_count']}`。",
        f"- 镜像不匹配数 `{scan['mirror_mismatch_count']}`。",
        f"- 前若干零行 `{scan['first_zero_rows']}`。",
        "",
        "## 2. Phase cap 约束",
        "",
        "`phase_cap_t` 的形式是：",
        "",
        "\\[",
        "g(t)\\le C_t.",
        "\\]",
        "",
        f"- 非零 phase cap 数 `{compact['nonzero_phase_caps']}`。",
        "",
        "| phase | cap |",
        "| ---: | ---: |",
    ]
    for row in compact["top_phase_caps"]:
        lines.append(f"| {row['phase']} | {row['bound']:.0f} |")

    lines.extend(
        [
            "",
            "## 3. Low-hole bucket 约束",
            "",
            "低骨架洞数阈值约束形式为：",
            "",
            "\\[",
            "\\sum_{h_Q(t)\\ge m}g(t)\\le B_m.",
            "\\]",
            "",
            "| threshold m | phase count | bound |",
            "| ---: | ---: | ---: |",
        ]
    )
    for row in compact["low_hole_bucket_caps"]:
        lines.append(f"| {row['threshold']} | {row['phase_count']} | {row['bound']:.0f} |")

    lines.extend(
        [
            "",
            "## 3A. 关键读数",
            "",
            "- `P=23,Q=210` 样本中，真实零行只落在 `44/210` 个相位。",
            "- 最大 phase cap 为 `324`，对应低骨架相位簇。",
            "- `low-hole>=5` 的 bucket 上界为 `0`：在该有限周期中，需要至少 5 个高层补洞的低骨架相位没有真实零行。",
            "- 这给出下一步符号化目标：证明高洞数低骨架相位无法由尾锚/核心补洞容量填满。",
            "",
            "## 4. Mass 与 Mirror",
            "",
            f"- 完整零行族质量等式：`sum_t g(t)={compact['mass_equality']['value']:.0f}`。",
            f"- 条件 mirror 等式数量：`{compact['conditional_mirror_equalities']}`。",
            "- `phase_cap` 对任意零行子族安全；`mass` 与强 `mirror_eq` 只对完整零行族或已证明镜像闭合的坏窗族安全。",
            "",
            "## 5. 审稿边界",
            "",
            "这些行已经是实际系数和界值，但来源是有限 CRT 枚举。下一步要把这些行提升为符号定理：",
            "",
            "```text",
            "finite phase cap table -> symbolic phase capacity bound；",
            "finite low-hole bucket -> tail/core capacity theorem；",
            "conditional mirror equality -> mirror-closed bad-family lemma。",
            "```",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=23)
    parser.add_argument("--q", type=int, default=210)
    parser.add_argument(
        "--include-full-coeffs",
        action="store_true",
        help="输出完整系数向量；默认只输出紧凑行信息。",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-pdec-real-constraint-rows.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-pdec-real-constraint-rows.md",
    )
    args = parser.parse_args()
    result = run(args.p, args.q, args.include_full_coeffs)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
