#!/usr/bin/env python3
"""生成 two-survivor 终端分叉的 switch-pressure 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_two_survivor_pdec_exclusion_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json

输出：
  data/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json
  docs/monograph/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.json
  docs/monograph/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.md
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
K13_LOW_SHELL = DATA / "prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json"
K14_FULL = DATA / "prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json"
TWO_SURVIVOR = DATA / "prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.md"

PREVIOUS_TARGET = "TwoSurvivorTerminalCRTBifurcationPDECExclusion"
NEXT_TARGET = "TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    """计算一组整数的最小公倍数。"""
    value = 1
    for item in values:
        value = value * int(item) // math.gcd(value, int(item))
    return value


def log10_int(value: int) -> float:
    """计算正整数的十进对数。"""
    return math.log10(value) if value > 0 else 0.0


def factor_block(edges: list[dict[str, Any]], predicate: Callable[[dict[str, Any]], bool]) -> dict[str, Any]:
    """按边筛选后汇总宽度、因子和 CRT lcm。"""
    selected = [edge for edge in edges if predicate(edge)]
    factors = {int(factor) for edge in selected for factor in edge["factors"]}
    lcm_value = lcm_many(factors)
    return {
        "edge_count": len(selected),
        "width": sum(int(edge["width"]) for edge in selected),
        "factor_count": len(factors),
        "factors": sorted(factors),
        "lcm_log10": log10_int(lcm_value),
    }


def capacity_map(support_hall: dict[str, Any], shift: int) -> dict[int, dict[str, Any]]:
    """读取指定 shift 的候选行容量。"""
    audit = next(item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift)
    return {int(item["residue"]): item for item in audit["candidate_capacities"]}


def extract_edges(
    *,
    label: str,
    lanes: list[dict[str, Any]],
    shift: int,
    support_hall: dict[str, Any],
    need_by_residue: dict[int, int],
) -> list[dict[str, Any]]:
    """把分支 lane 展开成带 assigned factors 的 source-target 边。"""
    period_p = int(support_hall["aggregate"]["period_p"])
    cap = capacity_map(support_hall, shift)
    edges: list[dict[str, Any]] = []
    for lane in lanes:
        delta = int(lane["delta"])
        for edge in lane["edges"]:
            source = int(edge["source_residue"])
            target = int(edge["target_residue"])
            width = int(need_by_residue[target])
            first_formal_p = int(cap[source]["first_formal_p"])
            factors = [
                smallest_factor(first_formal_p + (shift + offset) * period_p)
                for offset in range(width)
            ]
            edges.append(
                {
                    "branch": label,
                    "shift_cycles": shift,
                    "source_residue": source,
                    "target_residue": target,
                    "delta": delta,
                    "width": width,
                    "capacity": int(cap[source]["capacity"]),
                    "factors": factors,
                }
            )
    return sorted(edges, key=lambda item: (item["target_residue"], item["source_residue"], item["delta"]))


def source_capacity_sum(
    support_hall: dict[str, Any],
    *,
    shift: int,
    sources: set[int],
) -> int:
    """计算一组 source 在某个 shift 的总容量。"""
    cap = capacity_map(support_hall, shift)
    return sum(int(cap.get(source, {"capacity": 0})["capacity"]) for source in sources)


def source_capacity_rows(
    support_hall: dict[str, Any],
    *,
    shift: int,
    sources: set[int],
) -> list[dict[str, int]]:
    """列出 source 容量，便于审计 arrival/departure。"""
    cap = capacity_map(support_hall, shift)
    return [
        {
            "source_residue": source,
            "capacity": int(cap.get(source, {"capacity": 0})["capacity"]),
        }
        for source in sorted(sources)
    ]


def width_by_delta(edges: list[dict[str, Any]]) -> dict[int, int]:
    """按 delta 汇总需求宽度。"""
    result: dict[int, int] = {}
    for edge in edges:
        result[int(edge["delta"])] = result.get(int(edge["delta"]), 0) + int(edge["width"])
    return dict(sorted(result.items()))


def build_result() -> dict[str, Any]:
    """构造 two-survivor switch-pressure 证书。"""
    support_hall = load_json(SUPPORT_HALL)
    k13_low_shell = load_json(K13_LOW_SHELL)
    k14_full = load_json(K14_FULL)
    two_survivor = load_json(TWO_SURVIVOR)

    period_p = int(support_hall["aggregate"]["period_p"])
    need_by_residue = {
        int(item["residue"]): int(item["required_width"])
        for item in support_hall["needs_sorted_desc"]
    }

    k13_edges = extract_edges(
        label="k13",
        lanes=k13_low_shell["full_k13_load_summary"]["lanes"],
        shift=13,
        support_hall=support_hall,
        need_by_residue=need_by_residue,
    )
    k14_edges = extract_edges(
        label="k14",
        lanes=k14_full["best_candidate"]["full_load_summary"]["lanes"],
        shift=14,
        support_hall=support_hall,
        need_by_residue=need_by_residue,
    )

    k13_sources = {int(edge["source_residue"]) for edge in k13_edges}
    k14_sources = {int(edge["source_residue"]) for edge in k14_edges}
    k13_targets = {int(edge["target_residue"]) for edge in k13_edges}
    k14_targets = {int(edge["target_residue"]) for edge in k14_edges}
    k13_pairs = {(int(edge["source_residue"]), int(edge["target_residue"])) for edge in k13_edges}
    k14_pairs = {(int(edge["source_residue"]), int(edge["target_residue"])) for edge in k14_edges}

    common_pairs = k13_pairs & k14_pairs
    common_pair_targets = {target for _, target in common_pairs}
    forced_rematched_targets = sorted((k13_targets | k14_targets) - common_pair_targets)
    forced_rematched_width = sum(need_by_residue[target] for target in forced_rematched_targets)
    common_pair_width = sum(need_by_residue[target] for target in common_pair_targets)

    common_deltas = set(two_survivor["aggregate"]["common_deltas"])
    k13_delta_set = {int(edge["delta"]) for edge in k13_edges}
    k14_delta_set = {int(edge["delta"]) for edge in k14_edges}
    k13_exclusive_deltas = k13_delta_set - common_deltas
    k14_exclusive_deltas = k14_delta_set - common_deltas

    is_anchor = lambda edge: (int(edge["source_residue"]), int(edge["target_residue"])) in common_pairs
    k13_exclusive_block = factor_block(k13_edges, lambda edge: int(edge["delta"]) in k13_exclusive_deltas)
    k14_exclusive_block = factor_block(k14_edges, lambda edge: int(edge["delta"]) in k14_exclusive_deltas)
    k13_common_nonanchor_block = factor_block(
        k13_edges,
        lambda edge: int(edge["delta"]) in common_deltas and not is_anchor(edge),
    )
    k14_common_nonanchor_block = factor_block(
        k14_edges,
        lambda edge: int(edge["delta"]) in common_deltas and not is_anchor(edge),
    )
    k13_anchor_block = factor_block(k13_edges, is_anchor)
    k14_anchor_block = factor_block(k14_edges, is_anchor)

    k13_only_sources = k13_sources - k14_sources
    k14_only_sources = k14_sources - k13_sources
    common_sources = k13_sources & k14_sources
    k13_by_source = {int(edge["source_residue"]): edge for edge in k13_edges}
    k14_by_source = {int(edge["source_residue"]): edge for edge in k14_edges}
    common_source_changes = []
    for source in sorted(common_sources):
        left = k13_by_source[source]
        right = k14_by_source[source]
        same_edge = (
            int(left["target_residue"]) == int(right["target_residue"])
            and int(left["delta"]) == int(right["delta"])
        )
        common_source_changes.append(
            {
                "source_residue": source,
                "k13_target": int(left["target_residue"]),
                "k13_delta": int(left["delta"]),
                "k13_width": int(left["width"]),
                "k14_target": int(right["target_residue"]),
                "k14_delta": int(right["delta"]),
                "k14_width": int(right["width"]),
                "same_edge": same_edge,
            }
        )

    k13_departure_block = factor_block(
        k13_edges,
        lambda edge: int(edge["source_residue"]) in k13_only_sources,
    )
    k14_arrival_block = factor_block(
        k14_edges,
        lambda edge: int(edge["source_residue"]) in k14_only_sources,
    )

    k13_only_cap_13 = source_capacity_sum(support_hall, shift=13, sources=k13_only_sources)
    k13_only_cap_14 = source_capacity_sum(support_hall, shift=14, sources=k13_only_sources)
    k14_only_cap_13 = source_capacity_sum(support_hall, shift=13, sources=k14_only_sources)
    k14_only_cap_14 = source_capacity_sum(support_hall, shift=14, sources=k14_only_sources)
    k13_source_cap_at_14 = source_capacity_sum(support_hall, shift=14, sources=k13_sources)

    aggregate = {
        "row_column_unconditional_closed": False,
        "previous_hardpoint": PREVIOUS_TARGET,
        "period_p": period_p,
        "survivor_shifts": [13, 14],
        "common_pair_count": len(common_pairs),
        "common_pairs": [
            {"source_residue": source, "target_residue": target}
            for source, target in sorted(common_pairs)
        ],
        "common_pair_width": common_pair_width,
        "forced_rematched_target_count": len(forced_rematched_targets),
        "forced_rematched_target_width": forced_rematched_width,
        "forced_rematched_targets": forced_rematched_targets,
        "common_deltas": sorted(common_deltas),
        "k13_exclusive_delta_width": k13_exclusive_block["width"],
        "k14_exclusive_delta_width": k14_exclusive_block["width"],
        "minimum_branch_exclusive_delta_width": min(
            int(k13_exclusive_block["width"]),
            int(k14_exclusive_block["width"]),
        ),
        "k13_exclusive_delta_lcm_log10": k13_exclusive_block["lcm_log10"],
        "k14_exclusive_delta_lcm_log10": k14_exclusive_block["lcm_log10"],
        "minimum_branch_exclusive_delta_lcm_log10": min(
            float(k13_exclusive_block["lcm_log10"]),
            float(k14_exclusive_block["lcm_log10"]),
        ),
        "k13_common_delta_nonanchor_width": k13_common_nonanchor_block["width"],
        "k14_common_delta_nonanchor_width": k14_common_nonanchor_block["width"],
        "k13_anchor_width": k13_anchor_block["width"],
        "k14_anchor_width": k14_anchor_block["width"],
        "k13_only_source_count": len(k13_only_sources),
        "k14_only_source_count": len(k14_only_sources),
        "k13_only_sources": sorted(k13_only_sources),
        "k14_only_sources": sorted(k14_only_sources),
        "k13_only_assigned_width": k13_departure_block["width"],
        "k14_only_assigned_width": k14_arrival_block["width"],
        "k13_only_capacity_at_k13": k13_only_cap_13,
        "k13_only_capacity_at_k14": k13_only_cap_14,
        "k13_only_capacity_loss": k13_only_cap_13 - k13_only_cap_14,
        "k14_only_capacity_at_k13": k14_only_cap_13,
        "k14_only_capacity_at_k14": k14_only_cap_14,
        "k14_only_capacity_gain": k14_only_cap_14 - k14_only_cap_13,
        "k14_arrival_tail_capacity_after_assigned": k14_only_cap_14 - int(k14_arrival_block["width"]),
        "k13_same_support_capacity_at_k14": k13_source_cap_at_14,
        "k13_same_support_capacity_deficit_at_k14": sum(need_by_residue.values()) - k13_source_cap_at_14,
        "k14_arrival_lcm_log10": k14_arrival_block["lcm_log10"],
        "k13_departure_lcm_log10": k13_departure_block["lcm_log10"],
        "common_source_count": len(common_sources),
        "common_source_same_edge_count": sum(1 for row in common_source_changes if row["same_edge"]),
        "common_source_changed_count": sum(1 for row in common_source_changes if not row["same_edge"]),
        "common_source_changed_k13_width": sum(
            int(row["k13_width"]) for row in common_source_changes if not row["same_edge"]
        ),
        "common_source_changed_k14_width": sum(
            int(row["k14_width"]) for row in common_source_changes if not row["same_edge"]
        ),
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
    }

    result = {
        "certificate_type": "prime_matrix_cycle_debt_two_survivor_pdec_exclusion_router",
        "status": "two_survivor_terminal_switch_pressure_registered",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "width_by_delta": {
            "k13": width_by_delta(k13_edges),
            "k14": width_by_delta(k14_edges),
        },
        "factor_blocks": {
            "k13_branch_exclusive_deltas": k13_exclusive_block,
            "k14_branch_exclusive_deltas": k14_exclusive_block,
            "k13_common_delta_nonanchor": k13_common_nonanchor_block,
            "k14_common_delta_nonanchor": k14_common_nonanchor_block,
            "k13_common_anchor": k13_anchor_block,
            "k14_common_anchor": k14_anchor_block,
            "k13_departing_sources": k13_departure_block,
            "k14_arriving_sources": k14_arrival_block,
        },
        "source_transition": {
            "k13_only_capacity_rows_at_k13": source_capacity_rows(
                support_hall, shift=13, sources=k13_only_sources
            ),
            "k13_only_capacity_rows_at_k14": source_capacity_rows(
                support_hall, shift=14, sources=k13_only_sources
            ),
            "k14_only_capacity_rows_at_k13": source_capacity_rows(
                support_hall, shift=13, sources=k14_only_sources
            ),
            "k14_only_capacity_rows_at_k14": source_capacity_rows(
                support_hall, shift=14, sources=k14_only_sources
            ),
            "common_source_changes": common_source_changes,
        },
        "plain_conclusion": (
            "Two-survivor 终端分叉不能只靠共同 anchor 或共同 delta 吸收。"
            "唯一共同实际边 13->67 只承载宽度 15，剩余 26 个 target 仍有宽度 86 必须重路由。"
            "每个终端分支至少有 70 宽度落在 branch-exclusive delta 上，相关 CRT lcm 至少约 10^32.582。"
            "若从 K13 切到 K14，K14 还必须调用 8 个在 K13 时容量为 0 的新 source，承载 29 宽度，"
            "其 arrival 因子 lcm 约 10^20.205。因此剩余已压成 terminal switch-arrival ColumnCRT/PDEC，"
            "或 branch-exclusive CRT-load 排斥，而不是局部相位微调。"
        ),
        "dependency_hashes": {
            str(SUPPORT_HALL.relative_to(ROOT)): sha256(SUPPORT_HALL),
            str(K13_LOW_SHELL.relative_to(ROOT)): sha256(K13_LOW_SHELL),
            str(K14_FULL.relative_to(ROOT)): sha256(K14_FULL),
            str(TWO_SURVIVOR.relative_to(ROOT)): sha256(TWO_SURVIVOR),
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
        "# Prime Matrix cycle-debt two-survivor PDEC exclusion router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={str(agg['row_column_unconditional_closed']).lower()}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"period_p={agg['period_p']}",
        f"common_pair_count={agg['common_pair_count']}",
        f"common_pair_width={agg['common_pair_width']}",
        f"forced_rematched_target_count={agg['forced_rematched_target_count']}",
        f"forced_rematched_target_width={agg['forced_rematched_target_width']}",
        f"minimum_branch_exclusive_delta_width={agg['minimum_branch_exclusive_delta_width']}",
        f"minimum_branch_exclusive_delta_lcm_log10={agg['minimum_branch_exclusive_delta_lcm_log10']:.3f}",
        f"k14_only_assigned_width={agg['k14_only_assigned_width']}",
        f"k14_only_capacity_at_k13={agg['k14_only_capacity_at_k13']}",
        f"k14_only_capacity_at_k14={agg['k14_only_capacity_at_k14']}",
        f"k14_arrival_lcm_log10={agg['k14_arrival_lcm_log10']:.3f}",
        f"k13_same_support_capacity_deficit_at_k14={agg['k13_same_support_capacity_deficit_at_k14']}",
        f"common_source_changed_count={agg['common_source_changed_count']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. switch pressure",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| common actual edge width | {agg['common_pair_width']} |",
        f"| forced rematched target width | {agg['forced_rematched_target_width']} |",
        f"| K13 branch-exclusive delta width | {agg['k13_exclusive_delta_width']} |",
        f"| K14 branch-exclusive delta width | {agg['k14_exclusive_delta_width']} |",
        f"| K14 fresh-arrival assigned width | {agg['k14_only_assigned_width']} |",
        f"| K14 fresh-arrival capacity gain | {agg['k14_only_capacity_gain']} |",
        f"| common source changed count | {agg['common_source_changed_count']} |",
        "",
        "## 2. width by delta",
        "",
        "| branch | width by delta |",
        "| --- | --- |",
        f"| `k13` | `{result['width_by_delta']['k13']}` |",
        f"| `k14` | `{result['width_by_delta']['k14']}` |",
        "",
        "## 3. factor blocks",
        "",
        "| block | width | factors | log10 lcm |",
        "| --- | ---: | ---: | ---: |",
    ]
    for label, block in result["factor_blocks"].items():
        lines.append(
            f"| `{label}` | {block['width']} | {block['factor_count']} | {block['lcm_log10']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "- 共同实际边只有 `13->67`，它无法承载除 target `67` 以外的 `86` 宽度需求。",
            "- 共同 delta `54,58` 的非 anchor 容量很小；每个分支仍至少有 `70` 宽度必须落在 branch-exclusive delta。",
            "- K14 的 8 个新增 source 在 K13 时容量全为 `0`，到 K14 才出现 `39` 容量并承载 `29` 宽度。",
            "- 因此 terminal bifurcation 的下一硬点是 arrival ColumnCRT/PDEC 或 branch-exclusive CRT-load 排斥。",
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
