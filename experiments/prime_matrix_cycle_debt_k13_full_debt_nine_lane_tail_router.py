#!/usr/bin/env python3
"""生成 K=13 full-debt nine-lane residual tail 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_k13_full_debt_nine_lane_tail_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json

输出：
  data/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json
  docs/monograph/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.json
  docs/monograph/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.md
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

SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"
LOW_SHELL = DATA / "prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.md"

PREVIOUS_TARGET = "K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE"
NEXT_TARGET = "K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE"


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


def slot_factors(
    *,
    first_formal_p: int,
    shift: int,
    period_p: int,
    start_offset: int,
    end_offset: int,
) -> list[int]:
    """计算一段槽位的最小阻断素因子。"""
    return [
        smallest_factor(first_formal_p + (shift + offset) * period_p)
        for offset in range(start_offset, end_offset)
    ]


def tail_edge_record(
    *,
    edge: dict[str, int],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
    shift: int,
    period_p: int,
) -> dict[str, Any]:
    """把一条匹配边展开为已用槽和 residual tail 槽。"""
    source = int(edge["source_residue"])
    target = int(edge["target_residue"])
    capacity = int(cap_by_residue[source]["capacity"])
    width = int(need_by_residue[target]["required_width"])
    first_formal_p = int(cap_by_residue[source]["first_formal_p"])
    used_factors = slot_factors(
        first_formal_p=first_formal_p,
        shift=shift,
        period_p=period_p,
        start_offset=0,
        end_offset=width,
    )
    tail_factors = slot_factors(
        first_formal_p=first_formal_p,
        shift=shift,
        period_p=period_p,
        start_offset=width,
        end_offset=capacity,
    )
    tail_slots = []
    for offset in range(width, capacity):
        p_value = first_formal_p + (shift + offset) * period_p
        factor = smallest_factor(p_value)
        tail_slots.append(
            {
                "offset": offset,
                "absolute_cycle_from_first_formal": shift + offset,
                "p": p_value,
                "smallest_factor": factor,
                "is_composite": factor < p_value,
            }
        )
    return {
        "source_residue": source,
        "target_residue": target,
        "delta": int(edge["delta"]),
        "source_capacity": capacity,
        "required_width": width,
        "slack_tail_slots": capacity - width,
        "source_origin": cap_by_residue[source]["origin"],
        "used_factor_count": len(set(used_factors)),
        "used_factors": sorted(set(used_factors)),
        "tail_factor_count": len(set(tail_factors)),
        "tail_factors": sorted(set(tail_factors)),
        "tail_slots": tail_slots,
    }


def solve_factor_activation(
    *,
    sources: list[dict[str, Any]],
    demands: list[dict[str, Any]],
    allowed_deltas: set[int],
    shift: int,
    period_p: int,
    objective: str,
) -> dict[str, Any]:
    """在九 lane 约束下优化 residual tail 的素因子激活量。"""
    edges = []
    all_tail_factors: list[int] = []
    for source_index, source in enumerate(sources):
        for demand_index, demand in enumerate(demands):
            capacity = int(source["capacity"])
            width = int(demand["required_width"])
            delta = displacement(int(source["residue"]), int(demand["residue"]))
            if capacity < width or delta not in allowed_deltas:
                continue
            tail_factors = sorted(
                set(
                    slot_factors(
                        first_formal_p=int(source["first_formal_p"]),
                        shift=shift,
                        period_p=period_p,
                        start_offset=width,
                        end_offset=capacity,
                    )
                )
            )
            all_tail_factors.extend(tail_factors)
            edges.append(
                {
                    "source_index": source_index,
                    "demand_index": demand_index,
                    "source_residue": int(source["residue"]),
                    "target_residue": int(demand["residue"]),
                    "delta": delta,
                    "slack_tail_slots": capacity - width,
                    "tail_factors": tail_factors,
                }
            )

    factors = sorted(set(all_tail_factors))
    factor_index = {factor: index for index, factor in enumerate(factors)}
    edge_count = len(edges)
    factor_count = len(factors)
    variable_count = edge_count + factor_count

    rows = []
    lower_bounds = []
    upper_bounds = []

    # 每个容量行必须被使用一次；K=13 第 1 层 Hall 贴边保证没有备用行。
    for source_index in range(len(sources)):
        row = np.zeros(variable_count)
        for edge_index, edge in enumerate(edges):
            if int(edge["source_index"]) == source_index:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)

    # 每个需求行必须被覆盖一次。
    for demand_index in range(len(demands)):
        row = np.zeros(variable_count)
        for edge_index, edge in enumerate(edges):
            if int(edge["demand_index"]) == demand_index:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)

    # 若选择某边，其 tail 中出现的素因子必须激活。
    for edge_index, edge in enumerate(edges):
        for factor in edge["tail_factors"]:
            row = np.zeros(variable_count)
            row[edge_index] = 1
            row[edge_count + factor_index[factor]] = -1
            rows.append(row)
            lower_bounds.append(-np.inf)
            upper_bounds.append(0)

    if objective in {"min_count", "max_count"}:
        weights = np.ones(factor_count)
    elif objective in {"min_log", "max_log"}:
        weights = np.array([math.log10(factor) for factor in factors], dtype=float)
    else:
        raise ValueError(f"unknown objective: {objective}")
    if objective.startswith("max"):
        weights = -weights

    objective_vector = np.concatenate([np.zeros(edge_count), weights])
    result = milp(
        objective_vector,
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
    factor_values = np.rint(result.x[edge_count:]).astype(int)
    chosen_edges = [edge for value, edge in zip(edge_values, edges) if value]
    active_factors = [factor for value, factor in zip(factor_values, factors) if value]
    tail_lcm = lcm_many(active_factors)
    return {
        "objective": objective,
        "objective_value": float(result.fun),
        "chosen_edge_count": len(chosen_edges),
        "allowed_edge_count": edge_count,
        "active_tail_factor_count": len(active_factors),
        "active_tail_factors": active_factors,
        "tail_lcm": tail_lcm,
        "tail_lcm_log10": log10_int(tail_lcm),
        "tail_lcm_exceeds_period_p": tail_lcm > period_p,
        "tail_slot_count": sum(int(edge["slack_tail_slots"]) for edge in chosen_edges),
        "lane_slack": lane_slack_summary(chosen_edges),
        "chosen_edges": sorted(
            [
                {
                    "source_residue": int(edge["source_residue"]),
                    "target_residue": int(edge["target_residue"]),
                    "delta": int(edge["delta"]),
                    "slack_tail_slots": int(edge["slack_tail_slots"]),
                    "tail_factors": edge["tail_factors"],
                }
                for edge in chosen_edges
            ],
            key=lambda item: (item["delta"], item["source_residue"], item["target_residue"]),
        ),
    }


def lane_slack_summary(edges: list[dict[str, Any]]) -> list[dict[str, int]]:
    """汇总各 delta lane 的 tail slack。"""
    result = []
    for delta in sorted({int(edge["delta"]) for edge in edges}):
        result.append(
            {
                "delta": delta,
                "tail_slot_count": sum(
                    int(edge["slack_tail_slots"])
                    for edge in edges
                    if int(edge["delta"]) == delta
                ),
            }
        )
    return result


def optimize_lane_slack(
    *,
    sources: list[dict[str, Any]],
    demands: list[dict[str, Any]],
    allowed_deltas: set[int],
    delta: int,
    maximize: bool,
) -> int:
    """在线性匹配约束下优化单条 lane 的 tail slot 数。"""
    edges = []
    for source_index, source in enumerate(sources):
        for demand_index, demand in enumerate(demands):
            capacity = int(source["capacity"])
            width = int(demand["required_width"])
            edge_delta = displacement(int(source["residue"]), int(demand["residue"]))
            if capacity < width or edge_delta not in allowed_deltas:
                continue
            edges.append(
                {
                    "source_index": source_index,
                    "demand_index": demand_index,
                    "delta": edge_delta,
                    "slack_tail_slots": capacity - width,
                }
            )

    edge_count = len(edges)
    rows = []
    lower_bounds = []
    upper_bounds = []
    for source_index in range(len(sources)):
        row = np.zeros(edge_count)
        for edge_index, edge in enumerate(edges):
            if int(edge["source_index"]) == source_index:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)
    for demand_index in range(len(demands)):
        row = np.zeros(edge_count)
        for edge_index, edge in enumerate(edges):
            if int(edge["demand_index"]) == demand_index:
                row[edge_index] = 1
        rows.append(row)
        lower_bounds.append(1)
        upper_bounds.append(1)

    weights = np.array(
        [
            int(edge["slack_tail_slots"]) if int(edge["delta"]) == delta else 0
            for edge in edges
        ],
        dtype=float,
    )
    if maximize:
        weights = -weights
    result = milp(
        weights,
        integrality=np.ones(edge_count),
        bounds=Bounds(np.zeros(edge_count), np.ones(edge_count)),
        constraints=LinearConstraint(
            np.vstack(rows),
            np.array(lower_bounds),
            np.array(upper_bounds),
        ),
        options={"time_limit": 60},
    )
    if not result.success:
        raise RuntimeError(f"MILP failed for lane {delta}: {result.message}")
    value = -result.fun if maximize else result.fun
    return int(round(float(value)))


def reconstruct_current_edges(low_shell: dict[str, Any]) -> list[dict[str, int]]:
    """从上一层 full K13 load summary 还原当前九 lane 见证边。"""
    edges = []
    for lane in low_shell["full_k13_load_summary"]["lanes"]:
        delta = int(lane["delta"])
        for edge in lane["edges"]:
            edges.append(
                {
                    "source_residue": int(edge["source_residue"]),
                    "target_residue": int(edge["target_residue"]),
                    "delta": delta,
                }
            )
    return sorted(edges, key=lambda item: (item["delta"], item["source_residue"], item["target_residue"]))


def build_result() -> dict[str, Any]:
    """构造 K13 residual tail 证书。"""
    support_hall = load_json(SUPPORT_HALL)
    low_shell = load_json(LOW_SHELL)

    period_p = int(support_hall["aggregate"]["period_p"])
    shift = 13
    hall_audit = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift
    )
    cap_by_residue = {int(item["residue"]): item for item in hall_audit["candidate_capacities"]}
    need_by_residue = {
        int(item["residue"]): item for item in support_hall["needs_sorted_desc"]
    }
    sources = sorted(
        [item for item in hall_audit["candidate_capacities"] if int(item["capacity"]) > 0],
        key=lambda item: int(item["residue"]),
    )
    demands = sorted(support_hall["needs_sorted_desc"], key=lambda item: int(item["residue"]))
    allowed_deltas = set(int(item) for item in low_shell["full_k13_load_summary"]["deltas"])

    max_width = max(int(item["required_width"]) for item in demands)
    layer_profile = []
    for threshold in range(1, max_width + 1):
        supply_rows = [int(item["residue"]) for item in sources if int(item["capacity"]) >= threshold]
        demand_rows = [int(item["residue"]) for item in demands if int(item["required_width"]) >= threshold]
        layer_profile.append(
            {
                "threshold": threshold,
                "supply_rows": len(supply_rows),
                "demand_rows": len(demand_rows),
                "slack": len(supply_rows) - len(demand_rows),
                "zero_slack": len(supply_rows) == len(demand_rows),
                "supply_residues": supply_rows,
                "demand_residues": demand_rows,
            }
        )

    current_edges = reconstruct_current_edges(low_shell)
    current_tail_edges = [
        tail_edge_record(
            edge=edge,
            cap_by_residue=cap_by_residue,
            need_by_residue=need_by_residue,
            shift=shift,
            period_p=period_p,
        )
        for edge in current_edges
    ]
    current_tail_factors = sorted(
        {factor for edge in current_tail_edges for factor in edge["tail_factors"]}
    )
    current_used_factors = sorted(
        {factor for edge in current_tail_edges for factor in edge["used_factors"]}
    )
    current_tail_lcm = lcm_many(current_tail_factors)

    factor_optimizations = {
        objective: solve_factor_activation(
            sources=sources,
            demands=demands,
            allowed_deltas=allowed_deltas,
            shift=shift,
            period_p=period_p,
            objective=objective,
        )
        for objective in ["min_count", "min_log", "max_count", "max_log"]
    }

    lane_slack_ranges = []
    for delta in sorted(allowed_deltas):
        lane_slack_ranges.append(
            {
                "delta": delta,
                "min_tail_slots": optimize_lane_slack(
                    sources=sources,
                    demands=demands,
                    allowed_deltas=allowed_deltas,
                    delta=delta,
                    maximize=False,
                ),
                "max_tail_slots": optimize_lane_slack(
                    sources=sources,
                    demands=demands,
                    allowed_deltas=allowed_deltas,
                    delta=delta,
                    maximize=True,
                ),
            }
        )

    total_capacity = sum(int(item["capacity"]) for item in sources)
    total_demand = sum(int(item["required_width"]) for item in demands)
    total_tail_slots = total_capacity - total_demand
    min_tail = factor_optimizations["min_log"]
    result = {
        "certificate_type": "prime_matrix_cycle_debt_k13_full_debt_nine_lane_tail_router",
        "status": "k13_nine_lane_residual_tail_layer_invariant_and_crt_lower_bound",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "shift_cycles": shift,
            "capacity_row_count": len(sources),
            "demand_row_count": len(demands),
            "all_capacity_rows_mandatory": len(sources) == len(demands) == layer_profile[0]["supply_rows"],
            "total_capacity": total_capacity,
            "total_demand_width": total_demand,
            "unavoidable_tail_slot_count": total_tail_slots,
            "layer_slack_sum": sum(int(item["slack"]) for item in layer_profile),
            "zero_slack_layers": [
                int(item["threshold"]) for item in layer_profile if bool(item["zero_slack"])
            ],
            "positive_slack_layers": [
                {
                    "threshold": int(item["threshold"]),
                    "slack": int(item["slack"]),
                }
                for item in layer_profile
                if int(item["slack"]) > 0
            ],
            "allowed_delta_count": len(allowed_deltas),
            "allowed_deltas": sorted(allowed_deltas),
            "allowed_edge_count": factor_optimizations["min_log"]["allowed_edge_count"],
            "min_tail_factor_count": min_tail["active_tail_factor_count"],
            "min_tail_factors": min_tail["active_tail_factors"],
            "min_tail_lcm_log10": min_tail["tail_lcm_log10"],
            "min_tail_lcm_exceeds_period": min_tail["tail_lcm_exceeds_period_p"],
            "max_tail_factor_count": factor_optimizations["max_log"]["active_tail_factor_count"],
            "max_tail_lcm_log10": factor_optimizations["max_log"]["tail_lcm_log10"],
            "current_witness_tail_slot_count": sum(
                int(item["slack_tail_slots"]) for item in current_tail_edges
            ),
            "current_witness_tail_factor_count": len(current_tail_factors),
            "current_witness_tail_lcm_log10": log10_int(current_tail_lcm),
            "current_witness_tail_new_factor_count_over_used": len(
                set(current_tail_factors) - set(current_used_factors)
            ),
            "current_witness_tail_new_factors_over_used": sorted(
                set(current_tail_factors) - set(current_used_factors)
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "layer_slack_profile": layer_profile,
        "factor_optimizations": factor_optimizations,
        "lane_slack_ranges": lane_slack_ranges,
        "current_witness_tail_summary": {
            "tail_slot_count": sum(int(item["slack_tail_slots"]) for item in current_tail_edges),
            "tail_factor_count": len(current_tail_factors),
            "tail_factors": current_tail_factors,
            "tail_lcm": current_tail_lcm,
            "tail_lcm_log10": log10_int(current_tail_lcm),
            "tail_lcm_exceeds_period_p": current_tail_lcm > period_p,
            "used_factor_count": len(current_used_factors),
            "tail_new_factors_over_used": sorted(set(current_tail_factors) - set(current_used_factors)),
            "lane_slack": lane_slack_summary(current_tail_edges),
            "tail_edges": [
                edge for edge in current_tail_edges if int(edge["slack_tail_slots"]) > 0
            ],
        },
        "plain_conclusion": (
            "K=13 九 lane 全债务分支中，27 个正容量行与 27 个需求行在第 1 层 Hall 完全贴边，"
            "所以所有正容量行都必须使用。总容量 119、总需求 101，残余 tail 恰为 18 槽，"
            "且层 slack 向量在阈值 1,4,7,8 为零。这说明 residual slack-tail 不是匹配伪影。"
            "在固定九 lane 的所有可行匹配中，tail 至少激活 8 个互素阻断素因子，"
            "最小 tail lcm 约为 10^11.488，已经超过本地周期 5680。"
            "因此剩余接口压成层不变量 tail-CRT PDEC，或真正移动族 SAE。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(LOW_SHELL.relative_to(ROOT)): sha256(LOW_SHELL),
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
        "# Prime Matrix cycle-debt K13 full-debt nine-lane tail router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"capacity_row_count={agg['capacity_row_count']}",
        f"demand_row_count={agg['demand_row_count']}",
        f"all_capacity_rows_mandatory={fmt_bool(agg['all_capacity_rows_mandatory'])}",
        f"total_capacity={agg['total_capacity']}",
        f"total_demand_width={agg['total_demand_width']}",
        f"unavoidable_tail_slot_count={agg['unavoidable_tail_slot_count']}",
        f"zero_slack_layers={agg['zero_slack_layers']}",
        f"allowed_deltas={agg['allowed_deltas']}",
        f"allowed_edge_count={agg['allowed_edge_count']}",
        f"min_tail_factor_count={agg['min_tail_factor_count']}",
        f"min_tail_factors={agg['min_tail_factors']}",
        f"min_tail_lcm_log10={agg['min_tail_lcm_log10']:.3f}",
        f"min_tail_lcm_exceeds_period={fmt_bool(agg['min_tail_lcm_exceeds_period'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. layer slack invariant",
        "",
        "| threshold | supply rows | demand rows | slack | zero slack |",
        "| ---: | ---: | ---: | ---: | :---: |",
    ]
    for item in result["layer_slack_profile"]:
        lines.append(
            f"| {item['threshold']} | {item['supply_rows']} | {item['demand_rows']} | "
            f"{item['slack']} | {fmt_bool(item['zero_slack'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. tail factor optimization",
            "",
            "| objective | active factors | log10 tail lcm | tail slots | exceeds period |",
            "| --- | ---: | ---: | ---: | :---: |",
        ]
    )
    for objective in ["min_count", "min_log", "max_count", "max_log"]:
        item = result["factor_optimizations"][objective]
        lines.append(
            f"| `{objective}` | {item['active_tail_factor_count']} | "
            f"{item['tail_lcm_log10']:.3f} | {item['tail_slot_count']} | "
            f"{fmt_bool(item['tail_lcm_exceeds_period_p'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. lane tail ranges",
            "",
            "| delta | min tail slots | max tail slots |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in result["lane_slack_ranges"]:
        lines.append(f"| {item['delta']} | {item['min_tail_slots']} | {item['max_tail_slots']} |")

    lines.extend(
        [
            "",
            "## 4. current witness tail rows",
            "",
            "| source | target | delta | capacity | width | tail slots | tail factors |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for edge in result["current_witness_tail_summary"]["tail_edges"]:
        lines.append(
            f"| {edge['source_residue']} | {edge['target_residue']} | {edge['delta']} | "
            f"{edge['source_capacity']} | {edge['required_width']} | "
            f"{edge['slack_tail_slots']} | `{edge['tail_factors']}` |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定",
            "",
            "- 第 1 层 Hall slack 为 `0`，所以没有备用容量行；任何 full-debt 匹配都必须使用全部 27 个正容量行。",
            "- `sum layer_slack = total_capacity-total_demand = 18`，残余 tail 槽数是层账本不变量。",
            "- 零 slack 层 `1,4,7,8` 是移动槽的刚性门；在这些层失去一行容量会立即破坏 Hall 条件，除非产生新的 arrival/PDEC。",
            "- 在九 lane 约束内，即使优化 tail 因子，仍至少需要 8 个互素 blocker，tail lcm 约 `10^11.488`。",
            "- 因此 residual slack-tail 出口被命名为层不变量 tail-CRT PDEC 或真正 moving-family SAE。",
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
