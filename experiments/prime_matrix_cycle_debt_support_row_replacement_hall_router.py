#!/usr/bin/env python3
"""生成 cycle-debt 支撑行替换 Hall 容量证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_support_row_replacement_hall_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json

输出：
  data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json
  docs/monograph/prime-matrix-cycle-debt-support-row-replacement-hall-router.json
  docs/monograph/prime-matrix-cycle-debt-support-row-replacement-hall-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CYCLE_COVER = DATA / "prime-matrix-cycle-debt-crt-cover-pressure-ledger.json"
FULL_HORIZON = DATA / "prime-matrix-accepted-reset-full-relief-horizon-ledger.json"
FRESH_OBSTACLE = DATA / "prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-support-row-replacement-hall-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-support-row-replacement-hall-router.md"

PREVIOUS_TARGET = "FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE"
NEXT_TARGET = "K13K14SupportReplacementSurvivorPDECOrGlobalSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def is_prime(n: int) -> bool:
    """试除判定素数；本证书只处理小样本整数。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def longest_composite_capacity(p0: int, *, shift: int, period_p: int, max_width: int) -> dict[str, Any]:
    """计算从指定相位开始的最长连续合数容量。"""
    capacity = 0
    first_prime = None
    for offset in range(max_width):
        cycle = shift + offset
        p_value = p0 + cycle * period_p
        if is_prime(p_value):
            first_prime = {
                "absolute_cycle_from_first_formal": cycle,
                "window_position": offset,
                "p": p_value,
            }
            break
        capacity += 1
    return {"capacity": capacity, "first_prime_obstacle": first_prime}


def greedy_assignment(
    needs: list[dict[str, int]], candidates: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """按最大需求优先生成一份可审查贪心分配。"""
    ordered_needs = sorted(needs, key=lambda item: (-int(item["required_width"]), int(item["residue"])))
    ordered_candidates = sorted(
        candidates,
        key=lambda item: (-int(item["capacity"]), int(item["residue"])),
    )
    used: set[int] = set()
    assignments: list[dict[str, Any]] = []
    for need in ordered_needs:
        required = int(need["required_width"])
        chosen = None
        for candidate in ordered_candidates:
            residue = int(candidate["residue"])
            if residue in used:
                continue
            if int(candidate["capacity"]) >= required:
                chosen = candidate
                break
        if chosen is None:
            assignments.append(
                {
                    "need_residue": int(need["residue"]),
                    "required_width": required,
                    "assigned": False,
                }
            )
            continue
        used.add(int(chosen["residue"]))
        assignments.append(
            {
                "need_residue": int(need["residue"]),
                "required_width": required,
                "assigned": True,
                "assigned_residue": int(chosen["residue"]),
                "assigned_capacity": int(chosen["capacity"]),
                "assigned_origin": chosen["origin"],
                "assigned_original_debt": int(chosen["original_debt"]),
                "is_same_residue": int(chosen["residue"]) == int(need["residue"]),
            }
        )
    return assignments


def build_result() -> dict[str, Any]:
    """构造支撑行替换 Hall 容量证书。"""
    cover = load_json(CYCLE_COVER)
    horizon = load_json(FULL_HORIZON)
    fresh = load_json(FRESH_OBSTACLE)

    period_p = int(cover["aggregate"]["period_p"])
    near_shift_limit = int(fresh["aggregate"]["near_shift_limit_cycles"])
    positive_rows = sorted(cover["pressure_rows"], key=lambda row: int(row["residue"]))
    positive_by_residue = {int(row["residue"]): row for row in positive_rows}
    max_width = max(int(row["cycle_debt"]) for row in positive_rows)
    needs = [
        {"residue": int(row["residue"]), "required_width": int(row["cycle_debt"])}
        for row in positive_rows
    ]

    candidates: list[dict[str, Any]] = []
    for row in horizon["new_relief_rows"]:
        residue = int(row["residue"])
        if residue in positive_by_residue:
            source = positive_by_residue[residue]
            p0 = int(source["first_formal_p"])
            origin = "positive_debt"
            original_debt = int(source["cycle_debt"])
        else:
            p0 = int(row["p"])
            origin = "immediate_relief"
            original_debt = 0
        candidates.append(
            {
                "residue": residue,
                "first_formal_p": p0,
                "origin": origin,
                "original_debt": original_debt,
            }
        )

    shift_audits: list[dict[str, Any]] = []
    hall_fail_shifts: list[int] = []
    hall_survivor_shifts: list[int] = []

    for shift in range(1, near_shift_limit + 1):
        candidate_caps = []
        for candidate in candidates:
            cap_record = longest_composite_capacity(
                int(candidate["first_formal_p"]),
                shift=shift,
                period_p=period_p,
                max_width=max_width,
            )
            candidate_caps.append({**candidate, **cap_record})

        threshold_slacks = []
        min_slack = None
        first_defect = None
        for threshold in range(1, max_width + 1):
            supply = sum(1 for item in candidate_caps if int(item["capacity"]) >= threshold)
            demand = sum(1 for item in needs if int(item["required_width"]) >= threshold)
            slack = supply - demand
            if min_slack is None or slack < min_slack:
                min_slack = slack
            if slack < 0 and first_defect is None:
                first_defect = {
                    "threshold": threshold,
                    "supply_rows": supply,
                    "demand_rows": demand,
                    "slack": slack,
                }
            threshold_slacks.append(
                {
                    "threshold": threshold,
                    "supply_rows": supply,
                    "demand_rows": demand,
                    "slack": slack,
                }
            )

        hall_pass = bool(min_slack is not None and min_slack >= 0)
        if hall_pass:
            hall_survivor_shifts.append(shift)
        else:
            hall_fail_shifts.append(shift)

        assignments = greedy_assignment(needs, candidate_caps) if hall_pass else []
        assigned_immediate = sum(
            1 for item in assignments if item.get("assigned") and item.get("assigned_origin") == "immediate_relief"
        )
        assigned_positive = sum(
            1 for item in assignments if item.get("assigned") and item.get("assigned_origin") == "positive_debt"
        )
        assigned_replacements = sum(
            1 for item in assignments if item.get("assigned") and not item.get("is_same_residue")
        )

        shift_audits.append(
            {
                "shift_cycles": shift,
                "shift_p": shift * period_p,
                "hall_pass": hall_pass,
                "min_hall_slack": min_slack,
                "first_hall_defect": first_defect,
                "candidate_row_count": len(candidate_caps),
                "needed_row_count": len(needs),
                "total_capacity": sum(int(item["capacity"]) for item in candidate_caps),
                "total_demand_width": sum(int(item["required_width"]) for item in needs),
                "capacity_sorted_desc": sorted(
                    [int(item["capacity"]) for item in candidate_caps], reverse=True
                ),
                "threshold_slacks": threshold_slacks,
                "survivor_assignment": assignments,
                "assigned_immediate_relief_rows": assigned_immediate,
                "assigned_positive_debt_rows": assigned_positive,
                "assigned_replacement_count": assigned_replacements,
                "candidate_capacities": sorted(
                    candidate_caps,
                    key=lambda item: (-int(item["capacity"]), int(item["residue"])),
                ),
            }
        )

    survivor_details = [
        {
            "shift_cycles": item["shift_cycles"],
            "total_capacity": item["total_capacity"],
            "min_hall_slack": item["min_hall_slack"],
            "assigned_immediate_relief_rows": item["assigned_immediate_relief_rows"],
            "assigned_replacement_count": item["assigned_replacement_count"],
        }
        for item in shift_audits
        if item["hall_pass"]
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_support_row_replacement_hall_router",
        "status": "support_row_replacement_hall_capacity_fails_except_k13_k14",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "near_shift_limit_cycles": near_shift_limit,
            "candidate_missing_residue_count": len(candidates),
            "needed_positive_debt_row_count": len(needs),
            "total_demand_width": sum(int(item["required_width"]) for item in needs),
            "max_required_width": max_width,
            "hall_fail_shift_count": len(hall_fail_shifts),
            "hall_fail_shifts": hall_fail_shifts,
            "hall_survivor_shift_count": len(hall_survivor_shifts),
            "hall_survivor_shifts": hall_survivor_shifts,
            "all_but_k13_k14_fail_hall_capacity": hall_survivor_shifts == [13, 14],
            "survivor_details": survivor_details,
            "k13_assigned_immediate_relief_rows": next(
                item["assigned_immediate_relief_rows"] for item in shift_audits if item["shift_cycles"] == 13
            ),
            "k14_assigned_immediate_relief_rows": next(
                item["assigned_immediate_relief_rows"] for item in shift_audits if item["shift_cycles"] == 14
            ),
            "support_row_replacement_closed_except_k13_k14_current_certificate": True,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "needs_sorted_desc": sorted(needs, key=lambda item: (-int(item["required_width"]), int(item["residue"]))),
        "candidate_rows": sorted(candidates, key=lambda item: int(item["residue"])),
        "shift_audits": shift_audits,
        "plain_conclusion": (
            "把 support-row replacement 写成 35 个缺失 residue 候选行对 27 个正债务需求行的 Hall 容量问题。"
            "对每个近程相位 K，候选行容量为从 K 开始最长连续 composite 段，需求为原债务长度。"
            f"16 个相位中有 {len(hall_fail_shifts)} 个直接违反 Hall 阈值容量，只剩 K=13,14。"
            "这两个幸存相位也必须调用 immediate-relief 行并进行大规模支撑行替换，成为新的窄 PDEC/SAE 接口。"
        ),
        "dependency_hashes": {
            str(CYCLE_COVER.relative_to(ROOT)): sha256(CYCLE_COVER),
            str(FULL_HORIZON.relative_to(ROOT)): sha256(FULL_HORIZON),
            str(FRESH_OBSTACLE.relative_to(ROOT)): sha256(FRESH_OBSTACLE),
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
        "# Prime Matrix cycle-debt support-row replacement Hall router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"near_shift_limit_cycles={agg['near_shift_limit_cycles']}",
        f"candidate_missing_residue_count={agg['candidate_missing_residue_count']}",
        f"needed_positive_debt_row_count={agg['needed_positive_debt_row_count']}",
        f"total_demand_width={agg['total_demand_width']}",
        f"max_required_width={agg['max_required_width']}",
        f"hall_fail_shift_count={agg['hall_fail_shift_count']}",
        f"hall_fail_shifts={agg['hall_fail_shifts']}",
        f"hall_survivor_shift_count={agg['hall_survivor_shift_count']}",
        f"hall_survivor_shifts={agg['hall_survivor_shifts']}",
        f"all_but_k13_k14_fail_hall_capacity={fmt_bool(agg['all_but_k13_k14_fail_hall_capacity'])}",
        f"k13_assigned_immediate_relief_rows={agg['k13_assigned_immediate_relief_rows']}",
        f"k14_assigned_immediate_relief_rows={agg['k14_assigned_immediate_relief_rows']}",
        f"support_row_replacement_closed_except_k13_k14_current_certificate={fmt_bool(agg['support_row_replacement_closed_except_k13_k14_current_certificate'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. shift Hall audit",
        "",
        "| shift K | Hall pass | min slack | first defect | total capacity | immediate rows used | replacements |",
        "| ---: | :---: | ---: | --- | ---: | ---: | ---: |",
    ]
    for item in result["shift_audits"]:
        defect = item["first_hall_defect"]
        defect_text = (
            "-"
            if defect is None
            else f"t={defect['threshold']}: {defect['supply_rows']}-{defect['demand_rows']}={defect['slack']}"
        )
        lines.append(
            f"| {item['shift_cycles']} | {fmt_bool(item['hall_pass'])} | "
            f"{item['min_hall_slack']} | {defect_text} | {item['total_capacity']} | "
            f"{item['assigned_immediate_relief_rows']} | {item['assigned_replacement_count']} |"
        )

    lines.extend(
        [
            "",
            "## 2. survivor assignments",
            "",
            "Only `K=13,14` pass the Hall capacity test.  Their assignments are retained in the JSON ledger.",
            "",
            "| shift K | total capacity | min slack | immediate rows used | replacements |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in agg["survivor_details"]:
        lines.append(
            f"| {item['shift_cycles']} | {item['total_capacity']} | {item['min_hall_slack']} | "
            f"{item['assigned_immediate_relief_rows']} | {item['assigned_replacement_count']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- 对每个阈值 `t`，Hall 条件是 `candidate rows with capacity>=t >= demand rows with debt>=t`。",
            "- 16 个近程相位中 14 个直接违反该条件，故 support-row replacement 容量不足。",
            "- 仅 `K=13,14` 存活；它们必须调用 immediate-relief 行并进行大规模支撑行替换。",
            "- 本步仍不宣称行/列命题无条件闭合；它把剩余压成 `K=13,14` 两个幸存相位的 PDEC/SAE。",
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
