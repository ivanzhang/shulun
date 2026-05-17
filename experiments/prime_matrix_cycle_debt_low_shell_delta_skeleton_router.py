#!/usr/bin/env python3
"""生成 K=13 low-shell delta skeleton 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_low_shell_delta_skeleton_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json

输出：
  data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json
  docs/monograph/prime-matrix-cycle-debt-low-shell-delta-skeleton-router.json
  docs/monograph/prime-matrix-cycle-debt-low-shell-delta-skeleton-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SHELL_GRAPH = DATA / "prime-matrix-cycle-debt-shell-phase-graph-ledger.json"
SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
MULTI_DELTA = DATA / "prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-low-shell-delta-skeleton-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-low-shell-delta-skeleton-router.md"

PREVIOUS_TARGET = "MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE"
NEXT_TARGET = "K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


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


def log10_int(value: int) -> float:
    """计算正整数的十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def displacement(source: int, target: int) -> int:
    """计算 residue 相位差。"""
    return (target - source) % 71


def solve_delta_milp(
    *,
    supply: list[int],
    demand: list[int],
    edges: list[tuple[int, int, int]],
    delta_costs: dict[int, int],
) -> dict[str, Any]:
    """求覆盖一个 shell matching 所需的最小 delta 代价。"""
    deltas = sorted({delta for _, _, delta in edges})
    delta_index = {delta: index for index, delta in enumerate(deltas)}
    edge_count = len(edges)
    delta_count = len(deltas)
    variable_count = edge_count + delta_count

    objective = np.concatenate(
        [
            np.zeros(edge_count),
            np.array([delta_costs.get(delta, 1) for delta in deltas], dtype=float),
        ]
    )

    rows = []
    lower_bounds = []
    upper_bounds = []

    # 每个供给 residue 必须使用一次。
    for source in supply:
        row = np.zeros(variable_count)
        for edge_index, (edge_source, _target, _delta) in enumerate(edges):
            if edge_source == source:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)

    # 每个需求 residue 必须被覆盖一次。
    for target in demand:
        row = np.zeros(variable_count)
        for edge_index, (_source, edge_target, _delta) in enumerate(edges):
            if edge_target == target:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)

    # 若使用边，则必须打开对应 delta lane。
    for edge_index, (_source, _target, delta) in enumerate(edges):
        row = np.zeros(variable_count)
        row[edge_index] = 1
        row[edge_count + delta_index[delta]] = -1
        rows.append(row)
        lower_bounds.append(-np.inf)
        upper_bounds.append(0)

    result = milp(
        objective,
        integrality=np.ones(variable_count),
        bounds=Bounds(np.zeros(variable_count), np.ones(variable_count)),
        constraints=LinearConstraint(
            np.vstack(rows),
            np.array(lower_bounds),
            np.array(upper_bounds),
        ),
        options={"time_limit": 60},
    )
    if not result.success:
        raise RuntimeError(f"MILP failed: {result.message}")

    edge_values = np.rint(result.x[:edge_count]).astype(int)
    delta_values = np.rint(result.x[edge_count:]).astype(int)
    matching = [
        {"source_residue": source, "target_residue": target, "delta": delta}
        for value, (source, target, delta) in zip(edge_values, edges)
        if value
    ]
    used_deltas = [delta for value, delta in zip(delta_values, deltas) if value]
    return {
        "objective_value": int(round(float(result.fun))),
        "used_delta_count": len(used_deltas),
        "used_deltas": used_deltas,
        "matching": sorted(matching, key=lambda item: (item["source_residue"], item["target_residue"])),
    }


def edge_load(
    *,
    shift: int,
    edge: dict[str, int],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
    period_p: int,
) -> dict[str, Any]:
    """把一条匹配边展开成实际合数槽和阻断素因子。"""
    source = int(edge["source_residue"])
    target = int(edge["target_residue"])
    width = int(need_by_residue[target]["required_width"])
    first_formal_p = int(cap_by_residue[source]["first_formal_p"])
    slots = []
    factors = []
    for offset in range(width):
        cycle = shift + offset
        p_value = first_formal_p + cycle * period_p
        factor = smallest_factor(p_value)
        factors.append(factor)
        slots.append(
            {
                "offset": offset,
                "absolute_cycle_from_first_formal": cycle,
                "p": p_value,
                "smallest_factor": factor,
                "is_composite": factor < p_value,
            }
        )
    unique_factors = sorted(set(factors))
    lcm_value = lcm_many(unique_factors)
    return {
        "source_residue": source,
        "target_residue": target,
        "delta": displacement(source, target),
        "required_width": width,
        "source_capacity": int(cap_by_residue[source]["capacity"]),
        "source_origin": cap_by_residue[source]["origin"],
        "unique_blocker_factor_count": len(unique_factors),
        "unique_blocker_factors": unique_factors,
        "blocker_lcm": lcm_value,
        "blocker_lcm_log10": log10_int(lcm_value),
        "all_slots_composite": all(slot["is_composite"] for slot in slots),
        "slots": slots,
    }


def summarize_loads(edge_loads: list[dict[str, Any]], period_p: int) -> dict[str, Any]:
    """按 delta lane 汇总若干 edge loads。"""
    factors = sorted({factor for item in edge_loads for factor in item["unique_blocker_factors"]})
    global_lcm = lcm_many(factors)
    lanes: dict[int, list[dict[str, Any]]] = {}
    for item in edge_loads:
        lanes.setdefault(int(item["delta"]), []).append(item)

    lane_summaries = []
    for delta, items in sorted(lanes.items()):
        lane_factors = sorted({factor for item in items for factor in item["unique_blocker_factors"]})
        lane_lcm = lcm_many(lane_factors)
        lane_summaries.append(
            {
                "delta": delta,
                "edge_count": len(items),
                "total_required_width": sum(int(item["required_width"]) for item in items),
                "unique_blocker_factor_count": len(lane_factors),
                "unique_blocker_factors": lane_factors,
                "lane_lcm": lane_lcm,
                "lane_lcm_log10": log10_int(lane_lcm),
                "lane_lcm_exceeds_period_p": lane_lcm > period_p,
                "edges": [
                    {
                        "source_residue": item["source_residue"],
                        "target_residue": item["target_residue"],
                        "required_width": item["required_width"],
                        "source_origin": item["source_origin"],
                    }
                    for item in items
                ],
            }
        )
    return {
        "edge_count": len(edge_loads),
        "total_required_width": sum(int(item["required_width"]) for item in edge_loads),
        "delta_count": len(lane_summaries),
        "deltas": [item["delta"] for item in lane_summaries],
        "unique_blocker_factor_count": len(factors),
        "unique_blocker_factors": factors,
        "global_lcm": global_lcm,
        "global_lcm_log10": log10_int(global_lcm),
        "global_lcm_exceeds_period_p": global_lcm > period_p,
        "all_edges_composite_certified": all(item["all_slots_composite"] for item in edge_loads),
        "lanes": lane_summaries,
    }


def build_result() -> dict[str, Any]:
    """构造 low-shell delta skeleton 证书。"""
    shell_graph = load_json(SHELL_GRAPH)
    support_hall = load_json(SUPPORT_HALL)
    multi_delta = load_json(MULTI_DELTA)
    period_p = int(support_hall["aggregate"]["period_p"])
    shift = 13

    shell_summary = next(
        item for item in shell_graph["shift_summaries"] if int(item["shift_cycles"]) == shift
    )
    low_shell = next(
        item for item in shell_summary["shell_summaries"] if item["shell_label"] == "1..3"
    )
    hall_audit = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift
    )
    cap_by_residue = {int(item["residue"]): item for item in hall_audit["candidate_capacities"]}
    need_by_residue = {
        int(item["residue"]): item for item in support_hall["needs_sorted_desc"]
    }

    supply = [int(item) for item in low_shell["supply_residues"]]
    demand = [int(item) for item in low_shell["demand_residues"]]
    edges = []
    for source in supply:
        for target in demand:
            if int(cap_by_residue[source]["capacity"]) >= int(need_by_residue[target]["required_width"]):
                edges.append((source, target, displacement(source, target)))

    low_min_delta = solve_delta_milp(
        supply=supply,
        demand=demand,
        edges=edges,
        delta_costs={delta: 1 for delta in range(71)},
    )

    k13_core_best = next(
        item for item in multi_delta["shift_summaries"] if int(item["shift_cycles"]) == shift
    )["best_min_delta_matchings"][0]
    core_deltas = set(int(item) for item in k13_core_best["deltas"])
    low_extra_delta = solve_delta_milp(
        supply=supply,
        demand=demand,
        edges=edges,
        delta_costs={delta: 0 if delta in core_deltas else 1 for delta in range(71)},
    )

    low_extra_loads = [
        edge_load(
            shift=shift,
            edge=edge,
            cap_by_residue=cap_by_residue,
            need_by_residue=need_by_residue,
            period_p=period_p,
        )
        for edge in low_extra_delta["matching"]
    ]
    low_extra_summary = summarize_loads(low_extra_loads, period_p)

    core_edges = [
        {
            "source_residue": int(edge["source_residue"]),
            "target_residue": int(edge["target_residue"]),
            "delta": int(edge["delta"]),
        }
        for edge in k13_core_best["assignment_edges"]
    ]
    core_loads = [
        edge_load(
            shift=shift,
            edge=edge,
            cap_by_residue=cap_by_residue,
            need_by_residue=need_by_residue,
            period_p=period_p,
        )
        for edge in core_edges
    ]
    full_k13_summary = summarize_loads(core_loads + low_extra_loads, period_p)

    new_deltas = sorted(set(low_extra_delta["used_deltas"]) - core_deltas)
    result = {
        "certificate_type": "prime_matrix_cycle_debt_low_shell_delta_skeleton_router",
        "status": "k13_low_shell_full_residue_exit_compressed_to_two_extra_lanes",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "shift_cycles": shift,
            "low_shell_label": "1..3",
            "low_shell_supply_count": len(supply),
            "low_shell_demand_count": len(demand),
            "low_shell_edge_count": len(edges),
            "low_shell_possible_delta_count": int(low_shell["possible_delta_count"]),
            "low_shell_minimum_delta_count": low_min_delta["used_delta_count"],
            "low_shell_minimum_delta_witness": low_min_delta["used_deltas"],
            "core_delta_count_before_low_shell": len(core_deltas),
            "low_shell_new_delta_count_over_core": len(new_deltas),
            "low_shell_new_deltas_over_core": new_deltas,
            "full_k13_delta_count_after_low_shell": full_k13_summary["delta_count"],
            "full_k13_total_required_width": full_k13_summary["total_required_width"],
            "full_k13_global_lcm_log10": full_k13_summary["global_lcm_log10"],
            "full_k13_unique_blocker_factor_count": full_k13_summary["unique_blocker_factor_count"],
            "full_k13_lcm_exceeds_period": full_k13_summary["global_lcm_exceeds_period_p"],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "low_shell_min_delta_solution": low_min_delta,
        "low_shell_extra_delta_solution_over_core": low_extra_delta,
        "low_shell_extra_delta_load_summary": low_extra_summary,
        "full_k13_load_summary": full_k13_summary,
        "plain_conclusion": (
            "K=13 的低层 1..3 shell 虽然可出现全部 71 个 residue delta，"
            "但精确 MILP 显示它单独只需 6 个 delta 即可匹配。"
            "在已有 K=13 刚性核心的 7 个 delta 上，低层只需新增 0 与 66 两条 lane。"
            "于是 K=13 survivor 被压成 9-lane、全 101 demand width 的 CRT 载荷，"
            "全局 lcm 约为 10^42.095。低层 full-residue 逃逸解释被关闭，"
            "剩余是全债务九 lane CRT-load PDEC 或 residual slack-tail SAE。"
        ),
        "dependency_hashes": {
            str(SHELL_GRAPH.relative_to(ROOT)): sha256(SHELL_GRAPH),
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(MULTI_DELTA.relative_to(ROOT)): sha256(MULTI_DELTA),
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
        "# Prime Matrix cycle-debt low-shell delta skeleton router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"low_shell_possible_delta_count={agg['low_shell_possible_delta_count']}",
        f"low_shell_minimum_delta_count={agg['low_shell_minimum_delta_count']}",
        f"low_shell_minimum_delta_witness={agg['low_shell_minimum_delta_witness']}",
        f"core_delta_count_before_low_shell={agg['core_delta_count_before_low_shell']}",
        f"low_shell_new_delta_count_over_core={agg['low_shell_new_delta_count_over_core']}",
        f"low_shell_new_deltas_over_core={agg['low_shell_new_deltas_over_core']}",
        f"full_k13_delta_count_after_low_shell={agg['full_k13_delta_count_after_low_shell']}",
        f"full_k13_total_required_width={agg['full_k13_total_required_width']}",
        f"full_k13_global_lcm_log10={agg['full_k13_global_lcm_log10']:.3f}",
        f"full_k13_lcm_exceeds_period={fmt_bool(agg['full_k13_lcm_exceeds_period'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. low-shell delta skeleton",
        "",
        "| solution | objective | delta count | deltas |",
        "| --- | ---: | ---: | --- |",
        f"| low shell alone | {result['low_shell_min_delta_solution']['objective_value']} | "
        f"{result['low_shell_min_delta_solution']['used_delta_count']} | "
        f"`{result['low_shell_min_delta_solution']['used_deltas']}` |",
        f"| extra over core | {result['low_shell_extra_delta_solution_over_core']['objective_value']} | "
        f"{len(agg['low_shell_new_deltas_over_core'])} new | "
        f"`{result['low_shell_extra_delta_solution_over_core']['used_deltas']}` |",
        "",
        "## 2. full K13 lane load",
        "",
        "| delta | edges | width | blocker factors | log10 lane lcm |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for lane in result["full_k13_load_summary"]["lanes"]:
        lines.append(
            f"| {lane['delta']} | {lane['edge_count']} | {lane['total_required_width']} | "
            f"{lane['unique_blocker_factor_count']} | {lane['lane_lcm_log10']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- `1..3` low shell 的 possible delta 虽为全 `0..70`，但最小匹配骨架只需 6 个 delta。",
            "- 相对 K=13 刚性核心，low shell 只新增 delta `0,66`，总 lane 数变为 9。",
            "- 补齐后 K=13 覆盖全部 `101` demand width，全局 CRT lcm 约 `10^42.095`。",
            "- 因此 low-shell full-residue SAE 被压缩为九 lane 全债务 CRT-load PDEC/SAE 接口。",
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
