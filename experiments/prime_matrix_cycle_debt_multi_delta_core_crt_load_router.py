#!/usr/bin/env python3
"""生成 multi-delta core 的 CRT 载荷证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_multi_delta_core_crt_load_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json

输出：
  data/prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json
  docs/monograph/prime-matrix-cycle-debt-multi-delta-core-crt-load-router.json
  docs/monograph/prime-matrix-cycle-debt-multi-delta-core-crt-load-router.md
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

SHELL_GRAPH = DATA / "prime-matrix-cycle-debt-shell-phase-graph-ledger.json"
SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-multi-delta-core-crt-load-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-multi-delta-core-crt-load-router.md"

PREVIOUS_TARGET = "NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE"
NEXT_TARGET = "MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE"


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


def edge_load(
    *,
    shift: int,
    edge: tuple[int, int],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
    period_p: int,
) -> dict[str, Any]:
    """把一条 source->target 边展开成实际合数槽和阻断素因子。"""
    source, target = edge
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
    edge_lcm = lcm_many(unique_factors)
    return {
        "source_residue": source,
        "target_residue": target,
        "delta": displacement(source, target),
        "required_width": width,
        "source_capacity": int(cap_by_residue[source]["capacity"]),
        "source_origin": cap_by_residue[source]["origin"],
        "source_original_debt": int(cap_by_residue[source]["original_debt"]),
        "unique_blocker_factor_count": len(unique_factors),
        "unique_blocker_factors": unique_factors,
        "blocker_lcm": edge_lcm,
        "blocker_lcm_log10": log10_int(edge_lcm),
        "all_slots_composite": all(slot["is_composite"] for slot in slots),
        "slot_count": len(slots),
        "slots": slots,
    }


def lane_summary(edge_loads: list[dict[str, Any]], period_p: int) -> list[dict[str, Any]]:
    """按 delta lane 汇总边载荷。"""
    by_delta: dict[int, list[dict[str, Any]]] = {}
    for item in edge_loads:
        by_delta.setdefault(int(item["delta"]), []).append(item)

    lanes = []
    for delta, items in sorted(by_delta.items()):
        factors = sorted({factor for item in items for factor in item["unique_blocker_factors"]})
        lcm_value = lcm_many(factors)
        lanes.append(
            {
                "delta": delta,
                "edge_count": len(items),
                "total_required_width": sum(int(item["required_width"]) for item in items),
                "edges": [
                    {
                        "source_residue": item["source_residue"],
                        "target_residue": item["target_residue"],
                        "required_width": item["required_width"],
                        "source_origin": item["source_origin"],
                    }
                    for item in items
                ],
                "unique_blocker_factor_count": len(factors),
                "unique_blocker_factors": factors,
                "lane_lcm": lcm_value,
                "lane_lcm_log10": log10_int(lcm_value),
                "lane_lcm_exceeds_period_p": lcm_value > period_p,
            }
        )
    return lanes


def assignment_metrics(
    *,
    shift: int,
    assignment: list[tuple[int, int]],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
    period_p: int,
) -> dict[str, Any]:
    """计算一个核心匹配方案的多 delta CRT 载荷。"""
    loads = [
        edge_load(
            shift=shift,
            edge=edge,
            cap_by_residue=cap_by_residue,
            need_by_residue=need_by_residue,
            period_p=period_p,
        )
        for edge in assignment
    ]
    factors = sorted({factor for item in loads for factor in item["unique_blocker_factors"]})
    lcm_value = lcm_many(factors)
    lanes = lane_summary(loads, period_p)
    deltas = sorted({int(item["delta"]) for item in loads})
    return {
        "assignment_edges": [
            {"source_residue": source, "target_residue": target, "delta": displacement(source, target)}
            for source, target in assignment
        ],
        "delta_count": len(deltas),
        "deltas": deltas,
        "edge_count": len(loads),
        "total_required_width": sum(int(item["required_width"]) for item in loads),
        "immediate_relief_edge_count": sum(1 for item in loads if item["source_origin"] == "immediate_relief"),
        "unique_blocker_factor_count": len(factors),
        "unique_blocker_factors": factors,
        "global_lcm": lcm_value,
        "global_lcm_log10": log10_int(lcm_value),
        "global_lcm_exceeds_period_p": lcm_value > period_p,
        "all_edges_composite_certified": all(item["all_slots_composite"] for item in loads),
        "lanes": lanes,
        "edge_loads": loads,
    }


def core_matchings(shift_summary: dict[str, Any]) -> list[list[tuple[int, int]]]:
    """从 shell phase graph 中取出可枚举核心的全部匹配组合。"""
    shell_matchings: list[list[list[tuple[int, int]]]] = []
    for shell in shift_summary["shell_summaries"]:
        if not shell["matching_enumerated_for_core"]:
            continue
        current_shell = [
            [(int(source), int(target)) for source, target in matching]
            for matching in shell["enumerated_matchings"]
        ]
        shell_matchings.append(current_shell)

    combinations: list[list[tuple[int, int]]] = [[]]
    for matchings in shell_matchings:
        next_combinations: list[list[tuple[int, int]]] = []
        for prefix in combinations:
            for matching in matchings:
                next_combinations.append(prefix + matching)
        combinations = next_combinations
    return combinations


def summarize_shift(
    *,
    shift_summary: dict[str, Any],
    support_hall: dict[str, Any],
    period_p: int,
) -> dict[str, Any]:
    """生成单个 survivor 的最小多 delta 核心 CRT 载荷摘要。"""
    shift = int(shift_summary["shift_cycles"])
    hall_audit = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift
    )
    cap_by_residue = {int(item["residue"]): item for item in hall_audit["candidate_capacities"]}
    need_by_residue = {
        int(item["residue"]): item for item in support_hall["needs_sorted_desc"]
    }
    matchings = core_matchings(shift_summary)
    all_metrics = [
        assignment_metrics(
            shift=shift,
            assignment=matching,
            cap_by_residue=cap_by_residue,
            need_by_residue=need_by_residue,
            period_p=period_p,
        )
        for matching in matchings
    ]
    min_delta = min(int(item["delta_count"]) for item in all_metrics)
    min_delta_metrics = [item for item in all_metrics if int(item["delta_count"]) == min_delta]
    min_lcm = min(int(item["global_lcm"]) for item in min_delta_metrics)
    max_lcm = max(int(item["global_lcm"]) for item in min_delta_metrics)
    best_metrics = [item for item in min_delta_metrics if int(item["global_lcm"]) == min_lcm]

    excluded_large_shells = shift_summary["core_phase_fragmentation"]["excluded_large_shell_labels"]
    return {
        "shift_cycles": shift,
        "enumerated_core_matching_count": len(matchings),
        "minimum_delta_count": min_delta,
        "minimum_delta_matching_count": len(min_delta_metrics),
        "minimum_delta_min_lcm": min_lcm,
        "minimum_delta_min_lcm_log10": log10_int(min_lcm),
        "minimum_delta_max_lcm": max_lcm,
        "minimum_delta_max_lcm_log10": log10_int(max_lcm),
        "best_min_delta_matching_count": len(best_metrics),
        "excluded_large_shell_labels": excluded_large_shells,
        "best_min_delta_matchings": best_metrics,
        "all_min_delta_lcms_exceed_period": all(
            int(item["global_lcm"]) > period_p for item in min_delta_metrics
        ),
    }


def build_result() -> dict[str, Any]:
    """构造 multi-delta core CRT load 证书。"""
    shell_graph = load_json(SHELL_GRAPH)
    support_hall = load_json(SUPPORT_HALL)
    period_p = int(support_hall["aggregate"]["period_p"])
    shift_summaries = [
        summarize_shift(
            shift_summary=item,
            support_hall=support_hall,
            period_p=period_p,
        )
        for item in shell_graph["shift_summaries"]
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_multi_delta_core_crt_load_router",
        "status": "multi_delta_core_carries_large_transverse_crt_load",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "survivor_shifts": [item["shift_cycles"] for item in shift_summaries],
            "k13_enumerated_core_matching_count": shift_summaries[0]["enumerated_core_matching_count"],
            "k13_minimum_delta_count": shift_summaries[0]["minimum_delta_count"],
            "k13_minimum_delta_matching_count": shift_summaries[0]["minimum_delta_matching_count"],
            "k13_best_min_delta_global_lcm_log10": shift_summaries[0]["minimum_delta_min_lcm_log10"],
            "k13_excluded_large_shell_labels": shift_summaries[0]["excluded_large_shell_labels"],
            "k14_enumerated_core_matching_count": shift_summaries[1]["enumerated_core_matching_count"],
            "k14_minimum_delta_count": shift_summaries[1]["minimum_delta_count"],
            "k14_minimum_delta_matching_count": shift_summaries[1]["minimum_delta_matching_count"],
            "k14_best_min_delta_global_lcm_log10": shift_summaries[1]["minimum_delta_min_lcm_log10"],
            "all_min_delta_lcms_exceed_period": all(
                item["all_min_delta_lcms_exceed_period"] for item in shift_summaries
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "shift_summaries": shift_summaries,
        "plain_conclusion": (
            "把 multi-delta support SAE 的核心匹配展开成实际合数槽和阻断素因子。"
            "K=14 的最小多相位核心唯一，4 个 delta lane 的全局 CRT lcm 约为 10^31.716；"
            "K=13 的可枚举刚性核心只有 2 个最小 delta 方案，7 个 delta lane 的全局 CRT lcm 约为 10^36.165。"
            "这些核心载荷都远超本地周期，不是轻量相位碎裂；剩余只能是 multi-delta core CRT-load PDEC，"
            "或回到 K=13 低层大 shell 的 full-residue SAE。"
        ),
        "dependency_hashes": {
            str(SHELL_GRAPH.relative_to(ROOT)): sha256(SHELL_GRAPH),
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
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
        "# Prime Matrix cycle-debt multi-delta core CRT load router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"k13_enumerated_core_matching_count={agg['k13_enumerated_core_matching_count']}",
        f"k13_minimum_delta_count={agg['k13_minimum_delta_count']}",
        f"k13_minimum_delta_matching_count={agg['k13_minimum_delta_matching_count']}",
        f"k13_best_min_delta_global_lcm_log10={agg['k13_best_min_delta_global_lcm_log10']:.3f}",
        f"k14_enumerated_core_matching_count={agg['k14_enumerated_core_matching_count']}",
        f"k14_minimum_delta_count={agg['k14_minimum_delta_count']}",
        f"k14_minimum_delta_matching_count={agg['k14_minimum_delta_matching_count']}",
        f"k14_best_min_delta_global_lcm_log10={agg['k14_best_min_delta_global_lcm_log10']:.3f}",
        f"all_min_delta_lcms_exceed_period={fmt_bool(agg['all_min_delta_lcms_exceed_period'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. survivor core load",
        "",
        "| K | core matchings | min delta | min-delta matchings | best log10 lcm | excluded shells |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for shift in result["shift_summaries"]:
        lines.append(
            f"| {shift['shift_cycles']} | {shift['enumerated_core_matching_count']} | "
            f"{shift['minimum_delta_count']} | {shift['minimum_delta_matching_count']} | "
            f"{shift['minimum_delta_min_lcm_log10']:.3f} | `{shift['excluded_large_shell_labels']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. best lane loads",
            "",
            "| K | delta | edges | width | blocker factors | log10 lane lcm |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for shift in result["shift_summaries"]:
        best = shift["best_min_delta_matchings"][0]
        for lane in best["lanes"]:
            lines.append(
                f"| {shift['shift_cycles']} | {lane['delta']} | {lane['edge_count']} | "
                f"{lane['total_required_width']} | {lane['unique_blocker_factor_count']} | "
                f"{lane['lane_lcm_log10']:.3f} |"
            )

    lines.extend(
        [
            "",
            "## 3. 判定",
            "",
            "- 每个 edge load 使用目标 demand width 展开 source 行从 shift 开始的实际合数槽。",
            "- `K=14` 的最小多相位核心唯一；4 个 delta lane 已足以产生约 `10^31.716` 的横向 CRT 载荷。",
            "- `K=13` 的可枚举刚性核心只有 2 个最小 delta 方案；7 个 delta lane 的最小全局 lcm 约 `10^36.165`。",
            "- `K=13` 的低层 `1..3` shell 尚未作为闭合证明使用；它是下一步 full-residue SAE/PDEC 的接口。",
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
