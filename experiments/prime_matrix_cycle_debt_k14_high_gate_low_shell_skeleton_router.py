#!/usr/bin/env python3
"""生成 K=14 high-gate drift low-shell skeleton 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_k14_high_gate_low_shell_skeleton_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json

输出：
  data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json
  docs/monograph/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.json
  docs/monograph/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.md
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
SHELL_GRAPH = DATA / "prime-matrix-cycle-debt-shell-phase-graph-ledger.json"
K13_GATE_DRIFT = DATA / "prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.md"

PREVIOUS_TARGET = "K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE"
NEXT_TARGET = "K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC"


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


def enumerate_core_alternatives(k14_shell_summary: dict[str, Any]) -> list[list[dict[str, int]]]:
    """枚举 K=14 tight-shell core 的所有匹配。"""
    shell_edge_options: list[list[list[dict[str, int]]]] = []
    for shell in k14_shell_summary["shell_summaries"]:
        supply = [int(item) for item in shell["supply_residues"]]
        demand = [int(item) for item in shell["demand_residues"]]
        if len(supply) != len(demand):
            raise ValueError(f"unbalanced shell: {shell['shell_label']}")
        options = []
        for permutation in itertools.permutations(demand):
            edges = [
                {
                    "source_residue": source,
                    "target_residue": target,
                    "delta": displacement(source, target),
                    "shell_label": shell["shell_label"],
                }
                for source, target in zip(supply, permutation)
            ]
            options.append(edges)
        shell_edge_options.append(options)

    alternatives = []
    for product in itertools.product(*shell_edge_options):
        alternatives.append([edge for option in product for edge in option])
    return alternatives


def solve_low_shell(
    *,
    core_edges: list[dict[str, int]],
    sources: list[dict[str, Any]],
    demands: list[dict[str, Any]],
    objective: str,
) -> dict[str, Any]:
    """在固定 high-gate core 后求低层补齐的 delta skeleton。"""
    used_sources = {int(edge["source_residue"]) for edge in core_edges}
    used_targets = {int(edge["target_residue"]) for edge in core_edges}
    core_deltas = {int(edge["delta"]) for edge in core_edges}
    remaining_sources = [item for item in sources if int(item["residue"]) not in used_sources]
    remaining_demands = [item for item in demands if int(item["residue"]) not in used_targets]

    edges = []
    for source_index, source in enumerate(remaining_sources):
        for demand_index, demand in enumerate(remaining_demands):
            capacity = int(source["capacity"])
            width = int(demand["required_width"])
            if capacity < width:
                continue
            source_residue = int(source["residue"])
            target_residue = int(demand["residue"])
            edges.append(
                {
                    "source_index": source_index,
                    "demand_index": demand_index,
                    "source_residue": source_residue,
                    "target_residue": target_residue,
                    "delta": displacement(source_residue, target_residue),
                }
            )

    deltas = sorted({int(edge["delta"]) for edge in edges})
    delta_index = {delta: index for index, delta in enumerate(deltas)}
    edge_count = len(edges)
    delta_count = len(deltas)
    variable_count = edge_count + delta_count

    rows = []
    lower_bounds = []
    upper_bounds = []

    # K=14 低层存在备用容量行，因此供给行最多使用一次。
    for source_index in range(len(remaining_sources)):
        row = np.zeros(variable_count)
        for edge_index, edge in enumerate(edges):
            if int(edge["source_index"]) == source_index:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(0)
        upper_bounds.append(1)

    # 每个剩余需求行必须被覆盖一次。
    for demand_index in range(len(remaining_demands)):
        row = np.zeros(variable_count)
        for edge_index, edge in enumerate(edges):
            if int(edge["demand_index"]) == demand_index:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)

    # 若使用边，则必须打开相应 delta lane。
    for edge_index, edge in enumerate(edges):
        row = np.zeros(variable_count)
        row[edge_index] = 1
        row[edge_count + delta_index[int(edge["delta"])]] = -1
        rows.append(row)
        lower_bounds.append(-np.inf)
        upper_bounds.append(0)

    if objective == "unit":
        costs = np.ones(delta_count)
    elif objective == "extra_over_core":
        # 先最小化新增 lane 数，再轻微偏向少总 lane、较小 delta，使结果稳定。
        costs = np.array(
            [
                (1000.0 if delta not in core_deltas else 0.0) + 1.0 + delta / 1000.0
                for delta in deltas
            ],
            dtype=float,
        )
    else:
        raise ValueError(f"unknown objective: {objective}")

    result = milp(
        np.concatenate([np.zeros(edge_count), costs]),
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
        raise RuntimeError(f"MILP failed for {objective}: {result.message}")

    edge_values = np.rint(result.x[:edge_count]).astype(int)
    delta_values = np.rint(result.x[edge_count:]).astype(int)
    chosen_edges = [
        {
            "source_residue": int(edge["source_residue"]),
            "target_residue": int(edge["target_residue"]),
            "delta": int(edge["delta"]),
        }
        for value, edge in zip(edge_values, edges)
        if value
    ]
    used_deltas = [delta for value, delta in zip(delta_values, deltas) if value]
    return {
        "objective": objective,
        "remaining_source_count": len(remaining_sources),
        "remaining_demand_count": len(remaining_demands),
        "candidate_edge_count": len(edges),
        "used_delta_count": len(used_deltas),
        "used_deltas": used_deltas,
        "new_delta_count_over_core": len(set(used_deltas) - core_deltas),
        "new_deltas_over_core": sorted(set(used_deltas) - core_deltas),
        "matching": sorted(chosen_edges, key=lambda item: (item["delta"], item["source_residue"], item["target_residue"])),
    }


def edge_load(
    *,
    edge: dict[str, int],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
    shift: int,
    period_p: int,
) -> dict[str, Any]:
    """把一条边展开为实际 composite 槽和 tail 槽。"""
    source = int(edge["source_residue"])
    target = int(edge["target_residue"])
    capacity = int(cap_by_residue[source]["capacity"])
    width = int(need_by_residue[target]["required_width"])
    first_formal_p = int(cap_by_residue[source]["first_formal_p"])
    used_factors = []
    tail_factors = []
    for offset in range(capacity):
        p_value = first_formal_p + (shift + offset) * period_p
        factor = smallest_factor(p_value)
        if offset < width:
            used_factors.append(factor)
        else:
            tail_factors.append(factor)
    return {
        "source_residue": source,
        "target_residue": target,
        "delta": int(edge["delta"]),
        "required_width": width,
        "source_capacity": capacity,
        "source_origin": cap_by_residue[source]["origin"],
        "used_factors": sorted(set(used_factors)),
        "tail_slots": capacity - width,
        "tail_factors": sorted(set(tail_factors)),
    }


def summarize_loads(edge_loads: list[dict[str, Any]], period_p: int) -> dict[str, Any]:
    """汇总 full-debt 载荷。"""
    used_factors = sorted({factor for item in edge_loads for factor in item["used_factors"]})
    tail_factors = sorted({factor for item in edge_loads for factor in item["tail_factors"]})
    global_lcm = lcm_many(used_factors)
    tail_lcm = lcm_many(tail_factors)
    lanes = []
    for delta in sorted({int(item["delta"]) for item in edge_loads}):
        items = [item for item in edge_loads if int(item["delta"]) == delta]
        lane_factors = sorted({factor for item in items for factor in item["used_factors"]})
        lane_lcm = lcm_many(lane_factors)
        lanes.append(
            {
                "delta": delta,
                "edge_count": len(items),
                "total_required_width": sum(int(item["required_width"]) for item in items),
                "tail_slots": sum(int(item["tail_slots"]) for item in items),
                "unique_blocker_factor_count": len(lane_factors),
                "lane_lcm_log10": log10_int(lane_lcm),
                "lane_lcm_exceeds_period_p": lane_lcm > period_p,
                "edges": [
                    {
                        "source_residue": int(item["source_residue"]),
                        "target_residue": int(item["target_residue"]),
                        "required_width": int(item["required_width"]),
                        "source_capacity": int(item["source_capacity"]),
                        "source_origin": item["source_origin"],
                    }
                    for item in items
                ],
            }
        )
    return {
        "edge_count": len(edge_loads),
        "total_required_width": sum(int(item["required_width"]) for item in edge_loads),
        "used_capacity": sum(int(item["source_capacity"]) for item in edge_loads),
        "used_tail_slots": sum(int(item["tail_slots"]) for item in edge_loads),
        "delta_count": len(lanes),
        "deltas": [int(item["delta"]) for item in lanes],
        "unique_blocker_factor_count": len(used_factors),
        "global_lcm": global_lcm,
        "global_lcm_log10": log10_int(global_lcm),
        "global_lcm_exceeds_period_p": global_lcm > period_p,
        "tail_factor_count": len(tail_factors),
        "tail_lcm": tail_lcm,
        "tail_lcm_log10": log10_int(tail_lcm),
        "tail_lcm_exceeds_period_p": tail_lcm > period_p,
        "lanes": lanes,
    }


def build_result() -> dict[str, Any]:
    """构造 K14 high-gate low-shell skeleton 证书。"""
    support_hall = load_json(SUPPORT_HALL)
    shell_graph = load_json(SHELL_GRAPH)
    k13_gate_drift = load_json(K13_GATE_DRIFT)
    period_p = int(support_hall["aggregate"]["period_p"])
    shift = 14

    hall_audit = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift
    )
    shell_summary = next(
        item for item in shell_graph["shift_summaries"] if int(item["shift_cycles"]) == shift
    )
    sources = sorted(
        [item for item in hall_audit["candidate_capacities"] if int(item["capacity"]) > 0],
        key=lambda item: int(item["residue"]),
    )
    demands = sorted(support_hall["needs_sorted_desc"], key=lambda item: int(item["residue"]))
    cap_by_residue = {int(item["residue"]): item for item in hall_audit["candidate_capacities"]}
    need_by_residue = {int(item["residue"]): item for item in support_hall["needs_sorted_desc"]}

    core_alternatives = enumerate_core_alternatives(shell_summary)
    candidate_summaries = []
    for core_edges in core_alternatives:
        low_unit = solve_low_shell(
            core_edges=core_edges,
            sources=sources,
            demands=demands,
            objective="unit",
        )
        low_extra = solve_low_shell(
            core_edges=core_edges,
            sources=sources,
            demands=demands,
            objective="extra_over_core",
        )
        full_edges = [
            {
                "source_residue": int(edge["source_residue"]),
                "target_residue": int(edge["target_residue"]),
                "delta": int(edge["delta"]),
            }
            for edge in core_edges
        ] + low_extra["matching"]
        loads = [
            edge_load(
                edge=edge,
                cap_by_residue=cap_by_residue,
                need_by_residue=need_by_residue,
                shift=shift,
                period_p=period_p,
            )
            for edge in full_edges
        ]
        load_summary = summarize_loads(loads, period_p)
        candidate_summaries.append(
            {
                "core_edges": sorted(core_edges, key=lambda item: (item["shell_label"], item["source_residue"])),
                "core_delta_count": len({int(edge["delta"]) for edge in core_edges}),
                "core_deltas": sorted({int(edge["delta"]) for edge in core_edges}),
                "low_shell_min_delta_solution": low_unit,
                "low_shell_extra_over_core_solution": low_extra,
                "full_load_summary": load_summary,
            }
        )

    best = sorted(
        candidate_summaries,
        key=lambda item: (
            int(item["full_load_summary"]["delta_count"]),
            int(item["low_shell_extra_over_core_solution"]["new_delta_count_over_core"]),
            float(item["full_load_summary"]["global_lcm_log10"]),
        ),
    )[0]
    result = {
        "certificate_type": "prime_matrix_cycle_debt_k14_high_gate_low_shell_skeleton_router",
        "status": "k14_high_gate_drift_compressed_to_full_debt_eight_lane_crt_load",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "shift_cycles": shift,
            "k13_previous_gate_hardpoint": k13_gate_drift["aggregate"]["hardpoint_after_router"],
            "k14_zero_slack_layers": [
                int(item["threshold"]) for item in hall_audit["threshold_slacks"] if int(item["slack"]) == 0
            ],
            "k14_high_gate_core_alternative_count": len(core_alternatives),
            "k14_best_core_deltas": best["core_deltas"],
            "k14_low_shell_minimum_delta_count": best["low_shell_min_delta_solution"]["used_delta_count"],
            "k14_low_shell_new_delta_count_over_core": best["low_shell_extra_over_core_solution"]["new_delta_count_over_core"],
            "k14_low_shell_new_deltas_over_core": best["low_shell_extra_over_core_solution"]["new_deltas_over_core"],
            "k14_full_delta_count_after_low_shell": best["full_load_summary"]["delta_count"],
            "k14_full_deltas_after_low_shell": best["full_load_summary"]["deltas"],
            "k14_full_total_required_width": best["full_load_summary"]["total_required_width"],
            "k14_full_global_lcm_log10": best["full_load_summary"]["global_lcm_log10"],
            "k14_full_unique_blocker_factor_count": best["full_load_summary"]["unique_blocker_factor_count"],
            "k14_full_lcm_exceeds_period": best["full_load_summary"]["global_lcm_exceeds_period_p"],
            "k14_full_used_tail_slots": best["full_load_summary"]["used_tail_slots"],
            "k14_tail_lcm_log10": best["full_load_summary"]["tail_lcm_log10"],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "candidate_summaries": candidate_summaries,
        "best_candidate": best,
        "plain_conclusion": (
            "K=14 high-gate drift 不是新的未登记自由族。K=14 的 tight shell 只有 2 个 high-core 匹配；"
            "选择最优 core 后，剩余低层用整数规划补齐，low shell 单独最少 6 个 delta，"
            "相对 core 只需新增 2,48,58,70 四条 lane。于是 K=14 全 101 宽度被压成 8-lane CRT 载荷，"
            "全局 lcm 约 10^48.508，超过本地周期 5680。K14 moving 分支回到 full-debt CRT-load PDEC。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(SHELL_GRAPH.relative_to(ROOT)): sha256(SHELL_GRAPH),
            str(K13_GATE_DRIFT.relative_to(ROOT)): sha256(K13_GATE_DRIFT),
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
        "# Prime Matrix cycle-debt K14 high-gate low-shell skeleton router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"k14_zero_slack_layers={agg['k14_zero_slack_layers']}",
        f"k14_high_gate_core_alternative_count={agg['k14_high_gate_core_alternative_count']}",
        f"k14_best_core_deltas={agg['k14_best_core_deltas']}",
        f"k14_low_shell_minimum_delta_count={agg['k14_low_shell_minimum_delta_count']}",
        f"k14_low_shell_new_delta_count_over_core={agg['k14_low_shell_new_delta_count_over_core']}",
        f"k14_low_shell_new_deltas_over_core={agg['k14_low_shell_new_deltas_over_core']}",
        f"k14_full_delta_count_after_low_shell={agg['k14_full_delta_count_after_low_shell']}",
        f"k14_full_deltas_after_low_shell={agg['k14_full_deltas_after_low_shell']}",
        f"k14_full_total_required_width={agg['k14_full_total_required_width']}",
        f"k14_full_global_lcm_log10={agg['k14_full_global_lcm_log10']:.3f}",
        f"k14_full_lcm_exceeds_period={fmt_bool(agg['k14_full_lcm_exceeds_period'])}",
        f"k14_full_used_tail_slots={agg['k14_full_used_tail_slots']}",
        f"k14_tail_lcm_log10={agg['k14_tail_lcm_log10']:.3f}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. K14 core alternatives",
        "",
        "| candidate | core deltas | low min deltas | new over core | full deltas | log10 full lcm | tail slots |",
        "| ---: | --- | ---: | --- | --- | ---: | ---: |",
    ]
    for index, item in enumerate(result["candidate_summaries"], start=1):
        low = item["low_shell_extra_over_core_solution"]
        load = item["full_load_summary"]
        lines.append(
            f"| {index} | `{item['core_deltas']}` | "
            f"{item['low_shell_min_delta_solution']['used_delta_count']} | "
            f"`{low['new_deltas_over_core']}` | `{load['deltas']}` | "
            f"{load['global_lcm_log10']:.3f} | {load['used_tail_slots']} |"
        )

    lines.extend(
        [
            "",
            "## 2. best full K14 lane load",
            "",
            "| delta | edges | width | tail slots | blocker factors | log10 lane lcm |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for lane in result["best_candidate"]["full_load_summary"]["lanes"]:
        lines.append(
            f"| {lane['delta']} | {lane['edge_count']} | {lane['total_required_width']} | "
            f"{lane['tail_slots']} | {lane['unique_blocker_factor_count']} | "
            f"{lane['lane_lcm_log10']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- K14 高门漂移只留下两个 high-core 匹配，不是未命名的自由移动族。",
            "- 最优 high-core 的低层补齐只需新增四条 lane：`2,48,58,70`。",
            "- K14 全部 `101` 需求宽度被压成 `8` lane CRT 载荷，全局 lcm 约 `10^48.508`。",
            "- 因此 K14 moving 分支回到 full-debt CRT-load PDEC；剩余还包括固定 K13 gate-profile PDEC。",
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
