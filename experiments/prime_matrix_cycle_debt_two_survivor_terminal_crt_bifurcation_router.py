#!/usr/bin/env python3
"""生成 K13/K14 two-survivor terminal CRT bifurcation 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_two_survivor_terminal_crt_bifurcation_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json

输出：
  data/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json
  docs/monograph/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.json
  docs/monograph/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.md
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
K13_LOW_SHELL = DATA / "prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json"
K13_TAIL = DATA / "prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json"
K13_GATE_DRIFT = DATA / "prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json"
K14_FULL = DATA / "prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.md"

PREVIOUS_TARGET = "K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC"
NEXT_TARGET = "TwoSurvivorTerminalCRTBifurcationPDECExclusion"


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


def lcm_many(values: set[int] | list[int]) -> int:
    """计算若干整数的最小公倍数。"""
    value = 1
    for item in values:
        value = value * int(item) // math.gcd(value, int(item))
    return value


def log10_int(value: int) -> float:
    """计算正整数的十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def extract_k13_edges(k13_low_shell: dict[str, Any]) -> list[dict[str, int]]:
    """从 K13 full-load summary 还原 source-target-delta 边。"""
    edges = []
    for lane in k13_low_shell["full_k13_load_summary"]["lanes"]:
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


def extract_k14_edges(k14_full: dict[str, Any]) -> list[dict[str, int]]:
    """从 K14 best full-load summary 还原 source-target-delta 边。"""
    edges = []
    for lane in k14_full["best_candidate"]["full_load_summary"]["lanes"]:
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


def branch_summary(
    *,
    shift: int,
    edges: list[dict[str, int]],
    support_hall: dict[str, Any],
) -> dict[str, Any]:
    """展开一个 survivor 分支的实际 CRT 载荷。"""
    period_p = int(support_hall["aggregate"]["period_p"])
    audit = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift
    )
    cap_by_residue = {int(item["residue"]): item for item in audit["candidate_capacities"]}
    need_by_residue = {int(item["residue"]): item for item in support_hall["needs_sorted_desc"]}

    used_factors: set[int] = set()
    tail_factors: set[int] = set()
    sources: set[int] = set()
    targets: set[int] = set()
    pairs: set[tuple[int, int]] = set()
    lanes: dict[int, dict[str, Any]] = {}

    total_width = 0
    total_tail_slots = 0
    for edge in edges:
        source = int(edge["source_residue"])
        target = int(edge["target_residue"])
        delta = int(edge["delta"])
        capacity = int(cap_by_residue[source]["capacity"])
        width = int(need_by_residue[target]["required_width"])
        first_formal_p = int(cap_by_residue[source]["first_formal_p"])
        sources.add(source)
        targets.add(target)
        pairs.add((source, target))
        total_width += width
        total_tail_slots += capacity - width
        lanes.setdefault(
            delta,
            {
                "delta": delta,
                "edge_count": 0,
                "total_required_width": 0,
                "tail_slots": 0,
                "factors": set(),
            },
        )
        lanes[delta]["edge_count"] += 1
        lanes[delta]["total_required_width"] += width
        lanes[delta]["tail_slots"] += capacity - width
        for offset in range(capacity):
            p_value = first_formal_p + (shift + offset) * period_p
            factor = smallest_factor(p_value)
            if offset < width:
                used_factors.add(factor)
                lanes[delta]["factors"].add(factor)
            else:
                tail_factors.add(factor)

    lcm_value = lcm_many(used_factors)
    tail_lcm = lcm_many(tail_factors)
    lane_summaries = []
    for delta, lane in sorted(lanes.items()):
        lane_lcm = lcm_many(lane["factors"])
        lane_summaries.append(
            {
                "delta": delta,
                "edge_count": int(lane["edge_count"]),
                "total_required_width": int(lane["total_required_width"]),
                "tail_slots": int(lane["tail_slots"]),
                "unique_blocker_factor_count": len(lane["factors"]),
                "lane_lcm_log10": log10_int(lane_lcm),
            }
        )

    return {
        "shift_cycles": shift,
        "edge_count": len(edges),
        "source_count": len(sources),
        "target_count": len(targets),
        "demand_width": total_width,
        "tail_slots": total_tail_slots,
        "deltas": sorted({int(edge["delta"]) for edge in edges}),
        "delta_count": len({int(edge["delta"]) for edge in edges}),
        "sources": sorted(sources),
        "targets": sorted(targets),
        "pairs": sorted([{"source_residue": source, "target_residue": target} for source, target in pairs], key=lambda item: (item["source_residue"], item["target_residue"])),
        "used_factor_count": len(used_factors),
        "used_factors": sorted(used_factors),
        "global_lcm": lcm_value,
        "global_lcm_log10": log10_int(lcm_value),
        "global_lcm_exceeds_period_p": lcm_value > period_p,
        "tail_factor_count": len(tail_factors),
        "tail_factors": sorted(tail_factors),
        "tail_lcm": tail_lcm,
        "tail_lcm_log10": log10_int(tail_lcm),
        "tail_lcm_exceeds_period_p": tail_lcm > period_p,
        "lanes": lane_summaries,
    }


def pair_set(summary: dict[str, Any]) -> set[tuple[int, int]]:
    """把 pair 字典列表转成集合。"""
    return {
        (int(item["source_residue"]), int(item["target_residue"]))
        for item in summary["pairs"]
    }


def build_result() -> dict[str, Any]:
    """构造 two-survivor terminal CRT bifurcation 证书。"""
    support_hall = load_json(SUPPORT_HALL)
    k13_low_shell = load_json(K13_LOW_SHELL)
    k13_tail = load_json(K13_TAIL)
    k13_gate_drift = load_json(K13_GATE_DRIFT)
    k14_full = load_json(K14_FULL)
    period_p = int(support_hall["aggregate"]["period_p"])

    k13 = branch_summary(
        shift=13,
        edges=extract_k13_edges(k13_low_shell),
        support_hall=support_hall,
    )
    k14 = branch_summary(
        shift=14,
        edges=extract_k14_edges(k14_full),
        support_hall=support_hall,
    )

    k13_deltas = set(k13["deltas"])
    k14_deltas = set(k14["deltas"])
    k13_sources = set(k13["sources"])
    k14_sources = set(k14["sources"])
    k13_targets = set(k13["targets"])
    k14_targets = set(k14["targets"])
    k13_pairs = pair_set(k13)
    k14_pairs = pair_set(k14)
    k13_factors = set(k13["used_factors"])
    k14_factors = set(k14["used_factors"])
    k13_tail_factors = set(k13["tail_factors"])
    k14_tail_factors = set(k14["tail_factors"])
    union_factors = k13_factors | k14_factors
    union_tail_factors = k13_tail_factors | k14_tail_factors
    union_lcm = lcm_many(union_factors)
    union_tail_lcm = lcm_many(union_tail_factors)

    result = {
        "certificate_type": "prime_matrix_cycle_debt_two_survivor_terminal_crt_bifurcation_router",
        "status": "two_survivor_terminal_crt_bifurcation_named",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "period_p": period_p,
            "survivor_shifts": [13, 14],
            "k13_hardpoint_in": k13_tail["aggregate"]["hardpoint_after_router"],
            "k13_gate_drift_hardpoint_in": k13_gate_drift["aggregate"]["hardpoint_after_router"],
            "k14_hardpoint_in": k14_full["aggregate"]["hardpoint_after_router"],
            "k13_delta_count": k13["delta_count"],
            "k14_delta_count": k14["delta_count"],
            "common_delta_count": len(k13_deltas & k14_deltas),
            "common_deltas": sorted(k13_deltas & k14_deltas),
            "delta_union_count": len(k13_deltas | k14_deltas),
            "delta_union": sorted(k13_deltas | k14_deltas),
            "delta_symmetric_difference_count": len(k13_deltas ^ k14_deltas),
            "delta_symmetric_difference": sorted(k13_deltas ^ k14_deltas),
            "source_intersection_count": len(k13_sources & k14_sources),
            "source_symmetric_difference_count": len(k13_sources ^ k14_sources),
            "source_symmetric_difference": sorted(k13_sources ^ k14_sources),
            "target_intersection_count": len(k13_targets & k14_targets),
            "pair_intersection_count": len(k13_pairs & k14_pairs),
            "pair_intersection": [
                {"source_residue": source, "target_residue": target}
                for source, target in sorted(k13_pairs & k14_pairs)
            ],
            "k13_lcm_log10": k13["global_lcm_log10"],
            "k14_lcm_log10": k14["global_lcm_log10"],
            "union_factor_count": len(union_factors),
            "union_lcm_log10": log10_int(union_lcm),
            "union_lcm_exceeds_period": union_lcm > period_p,
            "factor_intersection_count": len(k13_factors & k14_factors),
            "tail_union_factor_count": len(union_tail_factors),
            "tail_union_lcm_log10": log10_int(union_tail_lcm),
            "k13_tail_slots": k13["tail_slots"],
            "k14_tail_slots": k14["tail_slots"],
            "k14_tail_slot_increase_over_k13": int(k14["tail_slots"]) - int(k13["tail_slots"]),
            "k13_hall_tail_balance": k13_tail["aggregate"]["unavoidable_tail_slot_count"],
            "k14_hall_tail_balance": k13_gate_drift["aggregate"]["k14_tail_balance"],
            "k14_hall_tail_balance_increase_over_k13": (
                int(k13_gate_drift["aggregate"]["k14_tail_balance"])
                - int(k13_tail["aggregate"]["unavoidable_tail_slot_count"])
            ),
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "branch_summaries": {
            "k13": k13,
            "k14": k14,
        },
        "plain_conclusion": (
            "K13 与 K14 两个 survivor 已不再是可互相吸收的同一支撑运动。"
            "两者覆盖同一 27 个需求 target，但 source 支撑只重合 19 行，实际 source-target 边只重合 1 条。"
            "delta lane 只共同保留 54 与 58，其余 13 条 lane 位于对称差中。"
            "两分支阻断素因子联合 lcm 约为 10^57.156，tail 因子联合 lcm 约为 10^24.632，"
            "均远超本地周期 5680。因此剩余不再是未命名 SAE，而是两 survivor 终端 CRT 分叉 PDEC 的排斥问题。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(K13_LOW_SHELL.relative_to(ROOT)): sha256(K13_LOW_SHELL),
            str(K13_TAIL.relative_to(ROOT)): sha256(K13_TAIL),
            str(K13_GATE_DRIFT.relative_to(ROOT)): sha256(K13_GATE_DRIFT),
            str(K14_FULL.relative_to(ROOT)): sha256(K14_FULL),
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
        "# Prime Matrix cycle-debt two-survivor terminal CRT bifurcation router",
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
        f"k13_delta_count={agg['k13_delta_count']}",
        f"k14_delta_count={agg['k14_delta_count']}",
        f"common_deltas={agg['common_deltas']}",
        f"delta_union_count={agg['delta_union_count']}",
        f"delta_symmetric_difference_count={agg['delta_symmetric_difference_count']}",
        f"source_intersection_count={agg['source_intersection_count']}",
        f"source_symmetric_difference_count={agg['source_symmetric_difference_count']}",
        f"target_intersection_count={agg['target_intersection_count']}",
        f"pair_intersection_count={agg['pair_intersection_count']}",
        f"pair_intersection={agg['pair_intersection']}",
        f"k13_lcm_log10={agg['k13_lcm_log10']:.3f}",
        f"k14_lcm_log10={agg['k14_lcm_log10']:.3f}",
        f"union_factor_count={agg['union_factor_count']}",
        f"union_lcm_log10={agg['union_lcm_log10']:.3f}",
        f"tail_union_lcm_log10={agg['tail_union_lcm_log10']:.3f}",
        f"k13_tail_slots={agg['k13_tail_slots']}",
        f"k14_tail_slots={agg['k14_tail_slots']}",
        f"k14_tail_slot_increase_over_k13={agg['k14_tail_slot_increase_over_k13']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. branch load comparison",
        "",
        "| branch | deltas | edges | width | tail slots | factors | log10 lcm |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for label in ["k13", "k14"]:
        item = result["branch_summaries"][label]
        lines.append(
            f"| `{label}` | {item['delta_count']} | {item['edge_count']} | "
            f"{item['demand_width']} | {item['tail_slots']} | "
            f"{item['used_factor_count']} | {item['global_lcm_log10']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## 2. lane comparison",
            "",
            "| item | value |",
            "| --- | --- |",
            f"| common deltas | `{agg['common_deltas']}` |",
            f"| delta union | `{agg['delta_union']}` |",
            f"| delta symmetric difference | `{agg['delta_symmetric_difference']}` |",
            f"| source symmetric difference | `{agg['source_symmetric_difference']}` |",
            "",
            "## 3. branch lanes",
        ]
    )
    for label in ["k13", "k14"]:
        lines.extend(
            [
                "",
                f"### {label}",
                "",
                "| delta | edges | width | tail slots | factors | log10 lane lcm |",
                "| ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for lane in result["branch_summaries"][label]["lanes"]:
            lines.append(
                f"| {lane['delta']} | {lane['edge_count']} | {lane['total_required_width']} | "
                f"{lane['tail_slots']} | {lane['unique_blocker_factor_count']} | "
                f"{lane['lane_lcm_log10']:.3f} |"
            )

    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "- K13 与 K14 覆盖同一 target 需求集合，但实际匹配边只重合 `13->67` 一条。",
            "- lane 交集只有 `54,58`，13 条 lane 位于对称差，不能解释为单一相位的小扰动。",
            "- 两分支联合 CRT lcm 约 `10^57.156`；tail 因子联合 lcm 约 `10^24.632`。",
            "- 因此剩余压成 two-survivor terminal CRT bifurcation PDEC 排斥问题。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
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
