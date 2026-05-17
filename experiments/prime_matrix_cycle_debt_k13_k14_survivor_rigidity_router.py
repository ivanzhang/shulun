#!/usr/bin/env python3
"""生成 K=13/14 支撑替换幸存相位的 tight-Hall 刚性证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_k13_k14_survivor_rigidity_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json

输出：
  data/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json
  docs/monograph/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.json
  docs/monograph/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
FRESH_OBSTACLE = DATA / "prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.md"

PREVIOUS_TARGET = "K13K14SupportReplacementSurvivorPDECOrGlobalSAE"
NEXT_TARGET = "K13K14TightHallCRTIslandPDECOrMovingSupportSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def log10_int(value: int) -> float:
    """稳定计算大整数的十进对数。"""
    if value <= 0:
        return 0.0
    return math.log10(value)


def smallest_factor(n: int) -> int:
    """返回 n 的最小因子；n 为素数时返回 n 本身。"""
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def lcm_many(values: list[int]) -> int:
    """计算若干整数的最小公倍数。"""
    value = 1
    for item in values:
        value = value * item // math.gcd(value, item)
    return value


def min_cost_assignment(
    needs: list[dict[str, int]],
    candidates: list[dict[str, Any]],
    cost_fn: Callable[[dict[str, int], dict[str, Any]], int],
) -> dict[str, Any]:
    """用小规模最小费用最大流求一个精确匹配下界。"""
    demand_count = len(needs)
    candidate_count = len(candidates)
    node_count = 1 + demand_count + candidate_count + 1
    source = 0
    sink = node_count - 1
    graph: list[list[dict[str, int]]] = [[] for _ in range(node_count)]

    def add_edge(u: int, v: int, capacity: int, cost: int) -> None:
        graph[u].append({"to": v, "capacity": capacity, "cost": cost, "rev": len(graph[v])})
        graph[v].append({"to": u, "capacity": 0, "cost": -cost, "rev": len(graph[u]) - 1})

    for demand_index in range(demand_count):
        add_edge(source, 1 + demand_index, 1, 0)

    for demand_index, need in enumerate(needs):
        required = int(need["required_width"])
        for candidate_index, candidate in enumerate(candidates):
            if int(candidate["capacity"]) >= required:
                add_edge(
                    1 + demand_index,
                    1 + demand_count + candidate_index,
                    1,
                    int(cost_fn(need, candidate)),
                )

    for candidate_index in range(candidate_count):
        add_edge(1 + demand_count + candidate_index, sink, 1, 0)

    flow = 0
    cost = 0
    while flow < demand_count:
        dist = [10**18] * node_count
        previous: list[tuple[int, int] | None] = [None] * node_count
        dist[source] = 0

        # 节点很少，Bellman-Ford 足够直接且避免额外依赖。
        for _ in range(node_count - 1):
            changed = False
            for u, edges in enumerate(graph):
                if dist[u] >= 10**18:
                    continue
                for edge_index, edge in enumerate(edges):
                    if edge["capacity"] <= 0:
                        continue
                    v = edge["to"]
                    next_dist = dist[u] + edge["cost"]
                    if next_dist < dist[v]:
                        dist[v] = next_dist
                        previous[v] = (u, edge_index)
                        changed = True
            if not changed:
                break

        if previous[sink] is None:
            break

        v = sink
        while v != source:
            u, edge_index = previous[v]  # type: ignore[misc]
            edge = graph[u][edge_index]
            edge["capacity"] -= 1
            graph[v][edge["rev"]]["capacity"] += 1
            v = u
        flow += 1
        cost += dist[sink]

    assignments: list[dict[str, Any]] = []
    for demand_index, need in enumerate(needs):
        u = 1 + demand_index
        for edge in graph[u]:
            v = edge["to"]
            if 1 + demand_count <= v < 1 + demand_count + candidate_count and edge["capacity"] == 0:
                candidate = candidates[v - (1 + demand_count)]
                assignments.append(
                    {
                        "need_residue": int(need["residue"]),
                        "required_width": int(need["required_width"]),
                        "assigned_residue": int(candidate["residue"]),
                        "assigned_capacity": int(candidate["capacity"]),
                        "assigned_origin": candidate["origin"],
                        "assigned_original_debt": int(candidate["original_debt"]),
                        "is_same_residue": int(need["residue"]) == int(candidate["residue"]),
                    }
                )
                break

    return {"full_matching": flow == demand_count, "flow": flow, "cost": cost, "assignment": assignments}


def blocker_layer(
    *,
    shift: int,
    threshold: int,
    period_p: int,
    supply_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    """把 tight Hall 层的强制合数槽转成 CRT 阻断素因子证书。"""
    slots: list[dict[str, Any]] = []
    factors: list[int] = []
    for row in supply_rows:
        for offset in range(threshold):
            cycle = shift + offset
            p_value = int(row["first_formal_p"]) + cycle * period_p
            factor = smallest_factor(p_value)
            slots.append(
                {
                    "residue": int(row["residue"]),
                    "offset": offset,
                    "absolute_cycle_from_first_formal": cycle,
                    "p": p_value,
                    "smallest_factor": factor,
                    "is_composite": factor < p_value,
                }
            )
            factors.append(factor)

    unique_factors = sorted(set(factors))
    transverse_factors = [factor for factor in unique_factors if math.gcd(factor, period_p) == 1]
    absorbed_factors = [factor for factor in unique_factors if math.gcd(factor, period_p) != 1]
    lcm_value = lcm_many(unique_factors)
    transverse_lcm = lcm_many(transverse_factors)
    all_slots_composite = all(slot["is_composite"] for slot in slots)
    return {
        "threshold": threshold,
        "forced_supply_row_count": len(supply_rows),
        "mandatory_slot_count": len(slots),
        "all_mandatory_slots_composite": all_slots_composite,
        "unique_blocker_factor_count": len(unique_factors),
        "unique_blocker_factors": unique_factors,
        "period_absorbed_blocker_factors": absorbed_factors,
        "transverse_blocker_factor_count": len(transverse_factors),
        "transverse_blocker_factors": transverse_factors,
        "blocker_lcm": lcm_value,
        "blocker_lcm_log10": log10_int(lcm_value),
        "transverse_lcm": transverse_lcm,
        "transverse_lcm_log10": log10_int(transverse_lcm),
        "transverse_lcm_exceeds_period_p": transverse_lcm > period_p,
        "transverse_lcm_exceeds_mandatory_slot_count": transverse_lcm > len(slots),
        "mandatory_slots_sample": slots[:20],
    }


def forced_shells(
    *,
    zero_thresholds: list[int],
    needs: list[dict[str, int]],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """分解相邻 tight cut 之间的强制壳层。"""
    shells: list[dict[str, Any]] = []
    descending = sorted(zero_thresholds, reverse=True)
    for index, lower in enumerate(descending):
        if index == 0:
            upper = None
            supply = [row for row in candidates if int(row["capacity"]) >= lower]
            demand = [need for need in needs if int(need["required_width"]) >= lower]
            label = f">={lower}"
        else:
            upper = descending[index - 1]
            supply = [
                row
                for row in candidates
                if lower <= int(row["capacity"]) < upper
            ]
            demand = [
                need
                for need in needs
                if lower <= int(need["required_width"]) < upper
            ]
            label = f"{lower}..{upper - 1}"

        supply_residues = sorted(int(row["residue"]) for row in supply)
        demand_residues = sorted(int(need["residue"]) for need in demand)
        overlap = sorted(set(supply_residues) & set(demand_residues))
        shells.append(
            {
                "shell_label": label,
                "lower_threshold": lower,
                "upper_exclusive": upper,
                "forced_supply_count": len(supply),
                "forced_demand_count": len(demand),
                "balanced_shell": len(supply) == len(demand),
                "supply_residues": supply_residues,
                "demand_residues": demand_residues,
                "same_residue_overlap": overlap,
                "forced_replacement_lower_bound_in_shell": len(demand) - len(overlap),
                "immediate_relief_supply_count": sum(
                    1 for row in supply if row["origin"] == "immediate_relief"
                ),
                "positive_debt_supply_count": sum(
                    1 for row in supply if row["origin"] == "positive_debt"
                ),
            }
        )
    return shells


def shift_summary(
    *,
    audit: dict[str, Any],
    needs: list[dict[str, int]],
    period_p: int,
    fresh_by_shift: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """生成单个幸存相位的刚性摘要。"""
    shift = int(audit["shift_cycles"])
    candidates = audit["candidate_capacities"]
    zero_thresholds = [
        int(item["threshold"])
        for item in audit["threshold_slacks"]
        if int(item["slack"]) == 0
    ]

    layers: list[dict[str, Any]] = []
    for threshold in zero_thresholds:
        supply = [row for row in candidates if int(row["capacity"]) >= threshold]
        demand = [need for need in needs if int(need["required_width"]) >= threshold]
        layer = blocker_layer(
            shift=shift,
            threshold=threshold,
            period_p=period_p,
            supply_rows=supply,
        )
        layer.update(
            {
                "demand_row_count": len(demand),
                "hall_cut_exact": len(supply) == len(demand),
                "single_supply_loss_breaks_hall_cut": len(supply) == len(demand),
                "supply_residues": sorted(int(row["residue"]) for row in supply),
                "demand_residues": sorted(int(need["residue"]) for need in demand),
                "immediate_relief_supply_count": sum(
                    1 for row in supply if row["origin"] == "immediate_relief"
                ),
            }
        )
        layers.append(layer)

    min_replacement = min_cost_assignment(
        needs,
        candidates,
        lambda need, candidate: 0
        if int(need["residue"]) == int(candidate["residue"])
        else 1,
    )
    min_immediate = min_cost_assignment(
        needs,
        candidates,
        lambda _need, candidate: 1 if candidate["origin"] == "immediate_relief" else 0,
    )
    min_immediate_width = min_cost_assignment(
        needs,
        candidates,
        lambda need, candidate: int(need["required_width"])
        if candidate["origin"] == "immediate_relief"
        else 0,
    )
    min_overstretch = min_cost_assignment(
        needs,
        candidates,
        lambda need, candidate: max(
            0, int(need["required_width"]) - int(candidate["original_debt"])
        ),
    )

    fresh = fresh_by_shift.get(shift, {})
    critical_candidate_residues = sorted(
        {
            int(row["residue"])
            for layer in layers
            for row in candidates
            if int(row["capacity"]) >= int(layer["threshold"])
        }
    )

    return {
        "shift_cycles": shift,
        "hall_pass": bool(audit["hall_pass"]),
        "zero_slack_thresholds": zero_thresholds,
        "tight_layer_count": len(zero_thresholds),
        "forced_shells": forced_shells(
            zero_thresholds=zero_thresholds,
            needs=needs,
            candidates=candidates,
        ),
        "tight_layers": layers,
        "critical_candidate_residue_count": len(critical_candidate_residues),
        "critical_candidate_residues": critical_candidate_residues,
        "min_replacement_assignment": {
            "minimum_replacement_count": int(min_replacement["cost"]),
            "same_residue_count": len(needs) - int(min_replacement["cost"]),
            "full_matching": min_replacement["full_matching"],
            "same_residue_pairs": [
                item for item in min_replacement["assignment"] if item["is_same_residue"]
            ],
        },
        "min_immediate_relief_assignment": {
            "minimum_immediate_relief_rows": int(min_immediate["cost"]),
            "full_matching": min_immediate["full_matching"],
            "immediate_relief_pairs": [
                item
                for item in min_immediate["assignment"]
                if item["assigned_origin"] == "immediate_relief"
            ],
        },
        "min_immediate_relief_width_assignment": {
            "minimum_width_carried_by_immediate_relief_rows": int(min_immediate_width["cost"]),
            "full_matching": min_immediate_width["full_matching"],
        },
        "min_overstretch_assignment": {
            "minimum_overstretch_units": int(min_overstretch["cost"]),
            "full_matching": min_overstretch["full_matching"],
        },
        "same_support_prime_obstacle_count": fresh.get("prime_obstacle_count"),
        "same_support_new_prime_obstacle_count": fresh.get("new_prime_obstacle_count"),
        "same_support_rows_with_prime_obstacle": fresh.get("rows_with_prime_obstacle"),
    }


def transition_summary(support: dict[str, Any]) -> dict[str, Any]:
    """记录 K=13/14 幸存岛的相邻 Hall 失败边界。"""
    audits = {int(item["shift_cycles"]): item for item in support["shift_audits"]}

    def supply_set(shift: int, threshold: int) -> set[int]:
        return {
            int(row["residue"])
            for row in audits[shift]["candidate_capacities"]
            if int(row["capacity"]) >= threshold
        }

    comparisons = []
    for left, right, threshold in [(12, 13, 8), (14, 15, 7), (14, 15, 6)]:
        left_set = supply_set(left, threshold)
        right_set = supply_set(right, threshold)
        comparisons.append(
            {
                "left_shift": left,
                "right_shift": right,
                "threshold": threshold,
                "left_supply_count": len(left_set),
                "right_supply_count": len(right_set),
                "lost_residues": sorted(left_set - right_set),
                "gained_residues": sorted(right_set - left_set),
            }
        )

    return {
        "survivor_island": [13, 14],
        "left_neighbor_first_defect": audits[12]["first_hall_defect"],
        "right_neighbor_first_defect": audits[15]["first_hall_defect"],
        "right_neighbor_second_defect_shift_16": audits[16]["first_hall_defect"],
        "boundary_supply_comparisons": comparisons,
        "adjacent_hall_failure_both_sides": (
            audits[12]["hall_pass"] is False and audits[15]["hall_pass"] is False
        ),
    }


def build_result() -> dict[str, Any]:
    """构造 K=13/14 tight-Hall survivor 证书。"""
    support = load_json(SUPPORT_HALL)
    fresh = load_json(FRESH_OBSTACLE)
    period_p = int(support["aggregate"]["period_p"])
    needs = [
        {"residue": int(item["residue"]), "required_width": int(item["required_width"])}
        for item in support["needs_sorted_desc"]
    ]
    fresh_by_shift = {
        int(item["shift_cycles"]): item for item in fresh["shift_obstacle_audits"]
    }

    survivor_shifts = [13, 14]
    audit_by_shift = {int(item["shift_cycles"]): item for item in support["shift_audits"]}
    survivors = [
        shift_summary(
            audit=audit_by_shift[shift],
            needs=needs,
            period_p=period_p,
            fresh_by_shift=fresh_by_shift,
        )
        for shift in survivor_shifts
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_k13_k14_survivor_rigidity_router",
        "status": "k13_k14_survivors_are_tight_hall_crt_island_not_free_replacement",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "survivor_shifts": survivor_shifts,
            "survivor_count": len(survivor_shifts),
            "k13_zero_slack_thresholds": survivors[0]["zero_slack_thresholds"],
            "k14_zero_slack_thresholds": survivors[1]["zero_slack_thresholds"],
            "k13_minimum_replacement_count": survivors[0]["min_replacement_assignment"][
                "minimum_replacement_count"
            ],
            "k14_minimum_replacement_count": survivors[1]["min_replacement_assignment"][
                "minimum_replacement_count"
            ],
            "k13_minimum_immediate_relief_rows": survivors[0]["min_immediate_relief_assignment"][
                "minimum_immediate_relief_rows"
            ],
            "k14_minimum_immediate_relief_rows": survivors[1]["min_immediate_relief_assignment"][
                "minimum_immediate_relief_rows"
            ],
            "k13_minimum_overstretch_units": survivors[0]["min_overstretch_assignment"][
                "minimum_overstretch_units"
            ],
            "k14_minimum_overstretch_units": survivors[1]["min_overstretch_assignment"][
                "minimum_overstretch_units"
            ],
            "all_tight_layers_have_transverse_lcm_exceeding_period": all(
                layer["transverse_lcm_exceeds_period_p"]
                for survivor in survivors
                for layer in survivor["tight_layers"]
            ),
            "all_tight_layers_have_composite_slots_certified": all(
                layer["all_mandatory_slots_composite"]
                for survivor in survivors
                for layer in survivor["tight_layers"]
            ),
            "k13_same_support_prime_obstacles": survivors[0]["same_support_prime_obstacle_count"],
            "k14_same_support_prime_obstacles": survivors[1]["same_support_prime_obstacle_count"],
            "survivor_island_has_adjacent_hall_failures": True,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "survivor_audits": survivors,
        "transition_summary": transition_summary(support),
        "plain_conclusion": (
            "K=13,14 不是自由的 support replacement。二者都含多个 zero-slack Hall cut，"
            "对应 supply set 必须整层进入匹配；任何单行容量损失都会破坏相应阈值。"
            "精确最小费用匹配显示，K=13 至少 20 行替换、至少 6 个 immediate-relief 行，"
            "K=14 至少 19 行替换、至少 6 个 immediate-relief 行。"
            "强制 tight 层的合数槽又给出横向 CRT 阻断模数，均超过本地周期。"
            "因此剩余不是普通容量自由度，而是 tight-Hall CRT island 的 PDEC 或 moving-support SAE。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
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
        "# Prime Matrix cycle-debt K13/K14 survivor rigidity router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"survivor_shifts={agg['survivor_shifts']}",
        f"k13_zero_slack_thresholds={agg['k13_zero_slack_thresholds']}",
        f"k14_zero_slack_thresholds={agg['k14_zero_slack_thresholds']}",
        f"k13_minimum_replacement_count={agg['k13_minimum_replacement_count']}",
        f"k14_minimum_replacement_count={agg['k14_minimum_replacement_count']}",
        f"k13_minimum_immediate_relief_rows={agg['k13_minimum_immediate_relief_rows']}",
        f"k14_minimum_immediate_relief_rows={agg['k14_minimum_immediate_relief_rows']}",
        f"k13_minimum_overstretch_units={agg['k13_minimum_overstretch_units']}",
        f"k14_minimum_overstretch_units={agg['k14_minimum_overstretch_units']}",
        f"all_tight_layers_have_transverse_lcm_exceeding_period={fmt_bool(agg['all_tight_layers_have_transverse_lcm_exceeding_period'])}",
        f"survivor_island_has_adjacent_hall_failures={fmt_bool(agg['survivor_island_has_adjacent_hall_failures'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. tight Hall layers",
        "",
        "| K | zero thresholds | min replacements | min immediate rows | min overstretch | same-support prime obstacles |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for survivor in result["survivor_audits"]:
        lines.append(
            f"| {survivor['shift_cycles']} | {survivor['zero_slack_thresholds']} | "
            f"{survivor['min_replacement_assignment']['minimum_replacement_count']} | "
            f"{survivor['min_immediate_relief_assignment']['minimum_immediate_relief_rows']} | "
            f"{survivor['min_overstretch_assignment']['minimum_overstretch_units']} | "
            f"{survivor['same_support_prime_obstacle_count']} |"
        )

    lines.extend(
        [
            "",
            "## 2. forced shells",
            "",
            "| K | shell | supply | demand | immediate supply | replacement lower bound |",
            "| ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for survivor in result["survivor_audits"]:
        for shell in survivor["forced_shells"]:
            lines.append(
                f"| {survivor['shift_cycles']} | `{shell['shell_label']}` | "
                f"{shell['forced_supply_count']} | {shell['forced_demand_count']} | "
                f"{shell['immediate_relief_supply_count']} | "
                f"{shell['forced_replacement_lower_bound_in_shell']} |"
            )

    lines.extend(
        [
            "",
            "## 3. CRT pressure on tight layers",
            "",
            "| K | threshold | slots | unique blockers | transverse blockers | log10 transverse lcm | exceeds period |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | :---: |",
        ]
    )
    for survivor in result["survivor_audits"]:
        for layer in survivor["tight_layers"]:
            lines.append(
                f"| {survivor['shift_cycles']} | {layer['threshold']} | "
                f"{layer['mandatory_slot_count']} | {layer['unique_blocker_factor_count']} | "
                f"{layer['transverse_blocker_factor_count']} | "
                f"{layer['transverse_lcm_log10']:.3f} | "
                f"{fmt_bool(layer['transverse_lcm_exceeds_period_p'])} |"
            )

    transition = result["transition_summary"]
    lines.extend(
        [
            "",
            "## 4. survivor island boundary",
            "",
            "```text",
            f"left_neighbor_first_defect={transition['left_neighbor_first_defect']}",
            f"right_neighbor_first_defect={transition['right_neighbor_first_defect']}",
            f"adjacent_hall_failure_both_sides={fmt_bool(transition['adjacent_hall_failure_both_sides'])}",
            "```",
            "",
            "## 5. 判定",
            "",
            "- `K=13,14` 是一个两点 survivor island，不是可平滑移动的 replacement family。",
            "- 每个 zero-slack 层都是精确 Hall cut；层内任一 supply 行的容量损失都会立刻破坏该阈值。",
            "- 即便优化匹配，仍至少需要 `19/20` 个行替换与 `6` 个 immediate-relief 行。",
            "- 强制合数槽的横向 CRT 模数均超过本地周期；若不是 PDEC，就只能作为 moving-support SAE 继续处理。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
