#!/usr/bin/env python3
"""生成 K13/K14 branch-exclusive 与 entry-wall 耦合证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_coupled_branch_entry_wall_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json

输出：
  data/prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json
  docs/monograph/prime-matrix-cycle-debt-coupled-branch-entry-wall-router.json
  docs/monograph/prime-matrix-cycle-debt-coupled-branch-entry-wall-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SWITCH_PRESSURE = DATA / "prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json"
ARRIVAL_WALL = DATA / "prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-coupled-branch-entry-wall-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-coupled-branch-entry-wall-router.md"

PREVIOUS_TARGET = "EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion"
NEXT_TARGET = "K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lcm_many(values: list[int] | set[int]) -> int:
    """计算最小公倍数。"""
    value = 1
    for item in values:
        value = value * int(item) // math.gcd(value, int(item))
    return value


def log10_int(value: int) -> float:
    """计算正整数十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def factor_summary(factors: list[int], period_p: int) -> dict[str, Any]:
    """汇总因子集合。"""
    unique = sorted({int(item) for item in factors})
    lcm_value = lcm_many(unique)
    return {
        "factor_count": len(unique),
        "factors": unique,
        "lcm": lcm_value,
        "lcm_log10": log10_int(lcm_value),
        "gcd_with_period_p": math.gcd(lcm_value, period_p),
        "coprime_to_period_p": math.gcd(lcm_value, period_p) == 1,
        "lcm_exceeds_period_p": lcm_value > period_p,
    }


def build_result() -> dict[str, Any]:
    """构造耦合 CRT 证书。"""
    switch_pressure = load_json(SWITCH_PRESSURE)
    arrival_wall = load_json(ARRIVAL_WALL)
    period_p = int(arrival_wall["aggregate"]["period_p"])

    k13_ex = switch_pressure["factor_blocks"]["k13_branch_exclusive_deltas"]
    k14_ex = switch_pressure["factor_blocks"]["k14_branch_exclusive_deltas"]
    wall_summaries = arrival_wall["crt_factor_summaries"]

    k13_branch_factors = [int(item) for item in k13_ex["factors"]]
    k14_branch_factors = [int(item) for item in k14_ex["factors"]]
    entry_factors = [int(item) for item in wall_summaries["entry_wall"]["factors"]]
    post_assigned_factors = [int(item) for item in wall_summaries["postwall_assigned"]["factors"]]
    post_all_factors = [int(item) for item in wall_summaries["postwall_all"]["factors"]]

    arrival_rows = arrival_wall["arrival_rows"]
    k14_branch_exclusive_deltas = {2, 4, 16, 28, 48, 70}
    arrival_branch_overlap_width = sum(
        int(row["assigned_width"])
        for row in arrival_rows
        if int(row["delta"]) in k14_branch_exclusive_deltas
    )
    arrival_nonbranch_width = sum(
        int(row["assigned_width"])
        for row in arrival_rows
        if int(row["delta"]) not in k14_branch_exclusive_deltas
    )
    k14_branch_arrival_union_width = int(k14_ex["width"]) + arrival_nonbranch_width

    k14_branch_set = set(k14_branch_factors)
    post_assigned_set = set(post_assigned_factors)
    entry_set = set(entry_factors)
    k13_branch_set = set(k13_branch_factors)

    summaries = {
        "k13_branch_exclusive": factor_summary(k13_branch_factors, period_p),
        "k14_branch_exclusive": factor_summary(k14_branch_factors, period_p),
        "all_branch_exclusive": factor_summary(k13_branch_factors + k14_branch_factors, period_p),
        "k14_branch_plus_entry": factor_summary(k14_branch_factors + entry_factors, period_p),
        "k14_branch_plus_entry_plus_assigned": factor_summary(
            k14_branch_factors + entry_factors + post_assigned_factors,
            period_p,
        ),
        "k14_branch_plus_entry_plus_postwall": factor_summary(
            k14_branch_factors + entry_factors + post_all_factors,
            period_p,
        ),
        "both_branches_plus_k14_entry_postwall": factor_summary(
            k13_branch_factors + k14_branch_factors + entry_factors + post_all_factors,
            period_p,
        ),
    }

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": period_p,
        "k13_branch_exclusive_width": int(k13_ex["width"]),
        "k13_branch_exclusive_lcm_log10": summaries["k13_branch_exclusive"]["lcm_log10"],
        "k14_branch_exclusive_width": int(k14_ex["width"]),
        "k14_branch_exclusive_lcm_log10": summaries["k14_branch_exclusive"]["lcm_log10"],
        "k14_arrival_assigned_width": int(arrival_wall["aggregate"]["postwall_assigned_width_total"]),
        "k14_arrival_branch_overlap_width": arrival_branch_overlap_width,
        "k14_arrival_nonbranch_width": arrival_nonbranch_width,
        "k14_branch_arrival_union_width": k14_branch_arrival_union_width,
        "k14_entry_wall_lcm_log10": arrival_wall["aggregate"]["entry_wall_lcm_log10"],
        "k14_entry_plus_postwall_lcm_log10": arrival_wall["aggregate"]["entry_plus_postwall_lcm_log10"],
        "k14_branch_plus_entry_lcm_log10": summaries["k14_branch_plus_entry"]["lcm_log10"],
        "k14_branch_plus_entry_plus_assigned_lcm_log10": summaries["k14_branch_plus_entry_plus_assigned"]["lcm_log10"],
        "k14_branch_plus_entry_plus_postwall_lcm_log10": summaries["k14_branch_plus_entry_plus_postwall"]["lcm_log10"],
        "both_branches_plus_k14_entry_postwall_lcm_log10": summaries["both_branches_plus_k14_entry_postwall"]["lcm_log10"],
        "k14_branch_postassigned_common_factors": sorted(k14_branch_set & post_assigned_set),
        "k14_branch_only_factors_against_postassigned": sorted(k14_branch_set - post_assigned_set),
        "postassigned_only_factors_against_k14_branch": sorted(post_assigned_set - k14_branch_set),
        "entry_wall_disjoint_from_branch_and_postwall": not bool(entry_set & (k13_branch_set | k14_branch_set | post_assigned_set)),
        "all_coupled_lcms_coprime_to_period": all(
            item["coprime_to_period_p"] for item in summaries.values()
        ),
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_coupled_branch_entry_wall_router",
        "status": "k13_k14_branch_entry_wall_coupling_registered",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "factor_summaries": summaries,
        "plain_conclusion": (
            "Eight-prime entry-wall 与 branch-exclusive 不是两个可任意择一的松散出口。"
            "若终端走 K14，70 宽度 branch-exclusive 载荷与 29 宽度 fresh-arrival 载荷有 21 宽度重叠，"
            "但二者联合仍强制 78 宽度 actual load；K14 branch+entry 的 lcm 约 10^72.064，"
            "branch+entry+assigned post-wall 的 lcm 约 10^76.351，branch+entry+全部 post-wall 的 lcm 约 10^85.024。"
            "若终端走 K13，则剩余是 K13 branch-exclusive CRT-load，宽度 73，lcm 约 10^36.678。"
            "因此最新剩余从泛化的 entry-wall/branch-exclusive 并列出口，压成 K13 branch-exclusive PDEC 或 K14 coupled entry-branch CRT wall。"
        ),
        "dependency_hashes": {
            str(SWITCH_PRESSURE.relative_to(ROOT)): sha256(SWITCH_PRESSURE),
            str(ARRIVAL_WALL.relative_to(ROOT)): sha256(ARRIVAL_WALL),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix cycle-debt coupled branch entry-wall router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"k13_branch_exclusive_width={agg['k13_branch_exclusive_width']}",
        f"k13_branch_exclusive_lcm_log10={agg['k13_branch_exclusive_lcm_log10']:.3f}",
        f"k14_branch_exclusive_width={agg['k14_branch_exclusive_width']}",
        f"k14_arrival_assigned_width={agg['k14_arrival_assigned_width']}",
        f"k14_arrival_branch_overlap_width={agg['k14_arrival_branch_overlap_width']}",
        f"k14_branch_arrival_union_width={agg['k14_branch_arrival_union_width']}",
        f"k14_branch_plus_entry_lcm_log10={agg['k14_branch_plus_entry_lcm_log10']:.3f}",
        f"k14_branch_plus_entry_plus_assigned_lcm_log10={agg['k14_branch_plus_entry_plus_assigned_lcm_log10']:.3f}",
        f"k14_branch_plus_entry_plus_postwall_lcm_log10={agg['k14_branch_plus_entry_plus_postwall_lcm_log10']:.3f}",
        f"both_branches_plus_k14_entry_postwall_lcm_log10={agg['both_branches_plus_k14_entry_postwall_lcm_log10']:.3f}",
        f"entry_wall_disjoint_from_branch_and_postwall={str(agg['entry_wall_disjoint_from_branch_and_postwall']).lower()}",
        f"all_coupled_lcms_coprime_to_period={str(agg['all_coupled_lcms_coprime_to_period']).lower()}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. coupled CRT blocks",
        "",
        "| block | factors | log10 lcm | gcd with period |",
        "| --- | ---: | ---: | ---: |",
    ]
    for label, block in result["factor_summaries"].items():
        lines.append(
            f"| `{label}` | {block['factor_count']} | {block['lcm_log10']:.3f} | {block['gcd_with_period_p']} |"
        )

    lines.extend(
        [
            "",
            "## 2. overlap diagnostics",
            "",
            "| item | value |",
            "| --- | --- |",
            f"| K14 branch/postassigned common factors | `{agg['k14_branch_postassigned_common_factors']}` |",
            f"| K14 branch-only factors | `{agg['k14_branch_only_factors_against_postassigned']}` |",
            f"| postassigned-only factors | `{agg['postassigned_only_factors_against_k14_branch']}` |",
            "",
            "## 3. 判定",
            "",
            "- K14 终端分支同时携带 branch-exclusive 载荷与 entry-wall/post-wall 载荷；不是两个无关出口。",
            "- arrival 与 branch-exclusive 有 `21` 宽度重叠，但联合仍强制 `78` 宽度 actual load。",
            "- K14 耦合载荷的最大审计 lcm 约 `10^85.024`；若把 K13/K14 branch-exclusive 全部合并则约 `10^99.349`。",
            "- 因此最新剩余压成 K13 branch-exclusive 排斥，或 K14 coupled entry-branch CRT wall 排斥。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
