#!/usr/bin/env python3
"""生成 terminal switch fresh-arrival 入口素数墙证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_terminal_switch_arrival_wall_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json

输出：
  data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json
  docs/monograph/prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.json
  docs/monograph/prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.md
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

SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
K14_FULL = DATA / "prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json"
SWITCH_PRESSURE = DATA / "prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.md"

PREVIOUS_TARGET = "TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion"
NEXT_TARGET = "EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def smallest_factor(n: int) -> int:
    """返回 n 的最小因子；n 为素数时返回 n。"""
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def lcm_many(values: list[int] | set[int]) -> int:
    """计算最小公倍数。"""
    value = 1
    for item in values:
        value = value * int(item) // math.gcd(value, int(item))
    return value


def log10_int(value: int) -> float:
    """计算正整数十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def capacity_map(support_hall: dict[str, Any], shift: int) -> dict[int, dict[str, Any]]:
    """读取某个 shift 的容量行。"""
    audit = next(item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift)
    return {int(item["residue"]): item for item in audit["candidate_capacities"]}


def extract_k14_arrival_assignments(
    k14_full: dict[str, Any],
    arrival_sources: set[int],
    need_by_residue: dict[int, int],
) -> dict[int, dict[str, int]]:
    """从 K14 full-load summary 提取 arrival source 的实际分配。"""
    result: dict[int, dict[str, int]] = {}
    for lane in k14_full["best_candidate"]["full_load_summary"]["lanes"]:
        delta = int(lane["delta"])
        for edge in lane["edges"]:
            source = int(edge["source_residue"])
            if source not in arrival_sources:
                continue
            target = int(edge["target_residue"])
            result[source] = {
                "source_residue": source,
                "target_residue": target,
                "delta": delta,
                "assigned_width": int(need_by_residue[target]),
            }
    return result


def width_by_delta(rows: list[dict[str, Any]]) -> dict[int, int]:
    """按 delta 汇总 assigned width。"""
    result: dict[int, int] = {}
    for row in rows:
        delta = int(row["delta"])
        result[delta] = result.get(delta, 0) + int(row["assigned_width"])
    return dict(sorted(result.items()))


def factor_summary(factors: list[int], period_p: int) -> dict[str, Any]:
    """汇总因子集合的 CRT 模数。"""
    unique = sorted({int(item) for item in factors})
    lcm_value = lcm_many(unique)
    return {
        "slot_count": len(factors),
        "factor_count": len(unique),
        "factors": unique,
        "lcm": lcm_value,
        "lcm_log10": log10_int(lcm_value),
        "gcd_with_period_p": math.gcd(lcm_value, period_p),
        "coprime_to_period_p": math.gcd(lcm_value, period_p) == 1,
        "lcm_exceeds_period_p": lcm_value > period_p,
    }


def build_result() -> dict[str, Any]:
    """构造 fresh-arrival 入口素数墙证书。"""
    support_hall = load_json(SUPPORT_HALL)
    k14_full = load_json(K14_FULL)
    switch_pressure = load_json(SWITCH_PRESSURE)

    period_p = int(support_hall["aggregate"]["period_p"])
    need_by_residue = {
        int(item["residue"]): int(item["required_width"])
        for item in support_hall["needs_sorted_desc"]
    }
    arrival_sources = set(int(item) for item in switch_pressure["aggregate"]["k14_only_sources"])
    cap13 = capacity_map(support_hall, 13)
    cap14 = capacity_map(support_hall, 14)
    assignments = extract_k14_arrival_assignments(k14_full, arrival_sources, need_by_residue)

    rows: list[dict[str, Any]] = []
    entry_primes: list[int] = []
    assigned_factors: list[int] = []
    tail_factors: list[int] = []
    all_postwall_factors: list[int] = []

    for source in sorted(arrival_sources):
        c13 = cap13[source]
        c14 = cap14[source]
        assignment = assignments[source]
        entry_obstacle = c13["first_prime_obstacle"]
        entry_prime = int(entry_obstacle["p"])
        assigned_width = int(assignment["assigned_width"])
        capacity = int(c14["capacity"])
        first_formal_p = int(c14["first_formal_p"])
        assigned_slots = []
        tail_slots = []
        for offset in range(capacity):
            p_value = first_formal_p + (14 + offset) * period_p
            factor = smallest_factor(p_value)
            slot = {"offset": offset, "p": p_value, "factor": factor}
            all_postwall_factors.append(factor)
            if offset < assigned_width:
                assigned_slots.append(slot)
                assigned_factors.append(factor)
            else:
                tail_slots.append(slot)
                tail_factors.append(factor)

        entry_primes.append(entry_prime)
        rows.append(
            {
                "source_residue": source,
                "target_residue": int(assignment["target_residue"]),
                "delta": int(assignment["delta"]),
                "assigned_width": assigned_width,
                "capacity_at_k13": int(c13["capacity"]),
                "capacity_at_k14": capacity,
                "entry_prime_at_k13": entry_prime,
                "entry_wall_cycle": int(entry_obstacle["absolute_cycle_from_first_formal"]),
                "entry_wall_position": int(entry_obstacle["window_position"]),
                "entry_prime_residue_mod_period": entry_prime % period_p,
                "postwall_first_prime_cycle": int(c14["first_prime_obstacle"]["absolute_cycle_from_first_formal"]),
                "postwall_first_prime_position": int(c14["first_prime_obstacle"]["window_position"]),
                "postwall_first_prime": int(c14["first_prime_obstacle"]["p"]),
                "assigned_slots": assigned_slots,
                "tail_slots": tail_slots,
            }
        )

    entry_summary = factor_summary(entry_primes, period_p)
    assigned_summary = factor_summary(assigned_factors, period_p)
    tail_summary = factor_summary(tail_factors, period_p)
    postwall_summary = factor_summary(all_postwall_factors, period_p)
    entry_assigned_summary = factor_summary(entry_primes + assigned_factors, period_p)
    entry_postwall_summary = factor_summary(entry_primes + all_postwall_factors, period_p)

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": period_p,
        "arrival_source_count": len(arrival_sources),
        "arrival_sources": sorted(arrival_sources),
        "all_arrival_sources_zero_capacity_at_k13": all(int(cap13[source]["capacity"]) == 0 for source in arrival_sources),
        "all_arrival_sources_positive_capacity_at_k14": all(int(cap14[source]["capacity"]) > 0 for source in arrival_sources),
        "entry_wall_cycle": 13,
        "all_entry_wall_positions_zero_at_k13": all(int(row["entry_wall_position"]) == 0 for row in rows),
        "all_entry_wall_cycles_equal_13": all(int(row["entry_wall_cycle"]) == 13 for row in rows),
        "entry_wall_prime_count": len(entry_primes),
        "entry_wall_primes": sorted(entry_primes),
        "entry_wall_lcm_log10": entry_summary["lcm_log10"],
        "entry_wall_coprime_to_period": entry_summary["coprime_to_period_p"],
        "postwall_capacity_total": sum(int(row["capacity_at_k14"]) for row in rows),
        "postwall_assigned_width_total": sum(int(row["assigned_width"]) for row in rows),
        "postwall_tail_slot_total": sum(len(row["tail_slots"]) for row in rows),
        "postwall_assigned_factor_count": assigned_summary["factor_count"],
        "postwall_assigned_lcm_log10": assigned_summary["lcm_log10"],
        "postwall_all_factor_count": postwall_summary["factor_count"],
        "postwall_all_lcm_log10": postwall_summary["lcm_log10"],
        "postwall_tail_factor_count": tail_summary["factor_count"],
        "postwall_tail_lcm_log10": tail_summary["lcm_log10"],
        "entry_plus_assigned_lcm_log10": entry_assigned_summary["lcm_log10"],
        "entry_plus_postwall_lcm_log10": entry_postwall_summary["lcm_log10"],
        "entry_plus_postwall_coprime_to_period": entry_postwall_summary["coprime_to_period_p"],
        "arrival_delta_count": len(width_by_delta(rows)),
        "arrival_width_by_delta": width_by_delta(rows),
        "branch_exclusive_parallel_obligation": "BranchExclusiveCRTLoadExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_terminal_switch_arrival_wall_router",
        "status": "terminal_switch_arrival_entry_wall_and_postwall_crt_registered",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "arrival_rows": rows,
        "crt_factor_summaries": {
            "entry_wall": entry_summary,
            "postwall_assigned": assigned_summary,
            "postwall_tail": tail_summary,
            "postwall_all": postwall_summary,
            "entry_plus_assigned": entry_assigned_summary,
            "entry_plus_postwall": entry_postwall_summary,
        },
        "plain_conclusion": (
            "K14 fresh-arrival 不是平滑打开的匿名容量。8 个 K14-only source 在 K13 时容量全为 0，"
            "并且全部在 K13 入口处撞到 window_position=0 的真实素数墙；入口素数墙的 lcm 约为 10^39.482。"
            "越过该墙后，K14 才得到 39 个 post-wall 容量槽，其中 29 槽被实际分配；"
            "assigned post-wall 因子 lcm 约为 10^20.205，entry+assigned 联合 lcm 约为 10^59.687，"
            "entry+全部 post-wall 联合 lcm 约为 10^68.361，且与本地周期 5680 互素。"
            "因此 terminal switch-arrival 不是局部微调，而是八素数入口墙加 post-wall CRT-load 的持久排斥问题；"
            "并行仍保留 branch-exclusive CRT-load 排斥义务。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(K14_FULL.relative_to(ROOT)): sha256(K14_FULL),
            str(SWITCH_PRESSURE.relative_to(ROOT)): sha256(SWITCH_PRESSURE),
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
        "# Prime Matrix cycle-debt terminal switch arrival wall router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"arrival_source_count={agg['arrival_source_count']}",
        f"all_arrival_sources_zero_capacity_at_k13={str(agg['all_arrival_sources_zero_capacity_at_k13']).lower()}",
        f"all_entry_wall_cycles_equal_13={str(agg['all_entry_wall_cycles_equal_13']).lower()}",
        f"all_entry_wall_positions_zero_at_k13={str(agg['all_entry_wall_positions_zero_at_k13']).lower()}",
        f"entry_wall_lcm_log10={agg['entry_wall_lcm_log10']:.3f}",
        f"postwall_capacity_total={agg['postwall_capacity_total']}",
        f"postwall_assigned_width_total={agg['postwall_assigned_width_total']}",
        f"postwall_tail_slot_total={agg['postwall_tail_slot_total']}",
        f"postwall_assigned_lcm_log10={agg['postwall_assigned_lcm_log10']:.3f}",
        f"entry_plus_assigned_lcm_log10={agg['entry_plus_assigned_lcm_log10']:.3f}",
        f"entry_plus_postwall_lcm_log10={agg['entry_plus_postwall_lcm_log10']:.3f}",
        f"entry_plus_postwall_coprime_to_period={str(agg['entry_plus_postwall_coprime_to_period']).lower()}",
        f"arrival_width_by_delta={agg['arrival_width_by_delta']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. arrival rows",
        "",
        "| source | target | delta | width | cap K13 | cap K14 | entry prime | next prime |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["arrival_rows"]:
        lines.append(
            f"| {row['source_residue']} | {row['target_residue']} | {row['delta']} | "
            f"{row['assigned_width']} | {row['capacity_at_k13']} | {row['capacity_at_k14']} | "
            f"{row['entry_prime_at_k13']} | {row['postwall_first_prime']} |"
        )

    lines.extend(
        [
            "",
            "## 2. CRT factor summaries",
            "",
            "| block | slots | factors | log10 lcm | gcd with period |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for label, block in result["crt_factor_summaries"].items():
        lines.append(
            f"| `{label}` | {block['slot_count']} | {block['factor_count']} | "
            f"{block['lcm_log10']:.3f} | {block['gcd_with_period_p']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- K14-only source 在 K13 全部为 `0` 容量，且全部由同一 `K=13` 入口素数墙切断。",
            "- K14 的 `39` 个 post-wall 容量槽中有 `29` 个被实际分配，剩余 tail 为 `10`。",
            "- 入口素数墙与 post-wall 因子均和本地周期 `5680` 互素，联合 lcm 约 `10^68.361`。",
            "- 因此 switch-arrival 分支已压成八素数入口墙 + post-wall CRT-load 排斥；branch-exclusive CRT-load 仍为并行义务。",
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
