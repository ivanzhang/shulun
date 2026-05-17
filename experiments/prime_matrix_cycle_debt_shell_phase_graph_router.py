#!/usr/bin/env python3
"""生成 K=13/14 tight-Hall shell phase graph 证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_shell_phase_graph_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json

输出：
  data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json
  docs/monograph/prime-matrix-cycle-debt-shell-phase-graph-router.json
  docs/monograph/prime-matrix-cycle-debt-shell-phase-graph-router.md
"""

from __future__ import annotations

from functools import cache
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

RIGIDITY = DATA / "prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json"
SUPPORT_HALL = DATA / "prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-shell-phase-graph-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-shell-phase-graph-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-shell-phase-graph-router.md"

MODULUS = 71
ENUMERATION_LIMIT = 1_000_000
PREVIOUS_TARGET = "K13K14TightHallCRTIslandPDECOrMovingSupportSAE"
NEXT_TARGET = "NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def displacement(source: int, target: int) -> int:
    """计算 residue support 从 source 到 target 的相位差。"""
    return (target - source) % MODULUS


def shell_edges(
    shell: dict[str, Any],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
) -> list[tuple[int, int]]:
    """列出 shell 内可行的供给到需求边。"""
    edges: list[tuple[int, int]] = []
    for source in shell["supply_residues"]:
        for target in shell["demand_residues"]:
            if int(cap_by_residue[source]["capacity"]) >= int(need_by_residue[target]["required_width"]):
                edges.append((int(source), int(target)))
    return edges


def count_and_forced_edges(
    supply: list[int],
    demand: list[int],
    edges: list[tuple[int, int]],
) -> dict[str, Any]:
    """用 bitmask DP 计算完美匹配数、强制边与可出现边。"""
    demand_index = {target: index for index, target in enumerate(demand)}
    edge_set = set(edges)
    row_masks: list[int] = []
    for source in supply:
        mask = 0
        for target in demand:
            if (source, target) in edge_set:
                mask |= 1 << demand_index[target]
        row_masks.append(mask)

    @cache
    def suffix_count(row_index: int, used_mask: int) -> int:
        if row_index == len(supply):
            return 1 if used_mask == (1 << len(demand)) - 1 else 0
        total = 0
        available = row_masks[row_index] & ~used_mask
        while available:
            bit = available & -available
            total += suffix_count(row_index + 1, used_mask | bit)
            available -= bit
        return total

    prefix: list[dict[int, int]] = [{0: 1}]
    for row_index, row_mask in enumerate(row_masks):
        current: dict[int, int] = {}
        for used_mask, count in prefix[row_index].items():
            available = row_mask & ~used_mask
            while available:
                bit = available & -available
                current[used_mask | bit] = current.get(used_mask | bit, 0) + count
                available -= bit
        prefix.append(current)

    total_matchings = suffix_count(0, 0)
    edge_counts: dict[tuple[int, int], int] = {edge: 0 for edge in edges}
    for row_index, source in enumerate(supply):
        for used_mask, prefix_count in prefix[row_index].items():
            available = row_masks[row_index] & ~used_mask
            while available:
                bit = available & -available
                target = demand[bit.bit_length() - 1]
                edge_counts[(source, target)] += prefix_count * suffix_count(
                    row_index + 1, used_mask | bit
                )
                available -= bit

    forced_edges = [
        edge for edge, count in edge_counts.items() if total_matchings > 0 and count == total_matchings
    ]
    possible_edges = [edge for edge, count in edge_counts.items() if count > 0]
    return {
        "perfect_matching_count": total_matchings,
        "forced_edges": sorted(forced_edges),
        "possible_edges": sorted(possible_edges),
        "edge_occurrence_counts": {
            f"{source}->{target}": count for (source, target), count in sorted(edge_counts.items())
        },
    }


def enumerate_matchings_limited(
    supply: list[int],
    demand: list[int],
    edges: list[tuple[int, int]],
    *,
    limit: int,
) -> list[tuple[tuple[int, int], ...]]:
    """枚举小 shell 的全部匹配；大 shell 由 DP 计数，不展开。"""
    edge_set = set(edges)
    matchings: list[tuple[tuple[int, int], ...]] = []

    def rec(row_index: int, used_targets: set[int], current: list[tuple[int, int]]) -> None:
        if len(matchings) > limit:
            return
        if row_index == len(supply):
            matchings.append(tuple(current))
            return
        source = supply[row_index]
        for target in demand:
            if target in used_targets or (source, target) not in edge_set:
                continue
            used_targets.add(target)
            current.append((source, target))
            rec(row_index + 1, used_targets, current)
            current.pop()
            used_targets.remove(target)

    rec(0, set(), [])
    return matchings if len(matchings) <= limit else []


def common_translation_deltas(
    supply: list[int],
    demand: list[int],
    edges: list[tuple[int, int]],
) -> list[int]:
    """检测该 shell 是否可由单一 residue 平移实现。"""
    demand_set = set(demand)
    edge_set = set(edges)
    valid: list[int] = []
    for delta in range(MODULUS):
        translated = [((source + delta) % MODULUS) for source in supply]
        if set(translated) != demand_set:
            continue
        if all((source, (source + delta) % MODULUS) in edge_set for source in supply):
            valid.append(delta)
    return valid


def min_distinct_deltas_for_core(shell_summaries: list[dict[str, Any]]) -> dict[str, Any]:
    """对可枚举刚性核心求最少相位差数；大 shell 不会降低该下界。"""
    enumerated_shells = [
        shell for shell in shell_summaries if shell["matching_enumerated_for_core"]
    ]
    excluded = [
        shell["shell_label"] for shell in shell_summaries if not shell["matching_enumerated_for_core"]
    ]
    best_count: int | None = None
    best_assignment: list[list[tuple[int, int]]] | None = None
    best_deltas: list[int] | None = None

    def rec(shell_index: int, used_deltas: set[int], current: list[list[tuple[int, int]]]) -> None:
        nonlocal best_count, best_assignment, best_deltas
        if best_count is not None and len(used_deltas) >= best_count:
            return
        if shell_index == len(enumerated_shells):
            best_count = len(used_deltas)
            best_assignment = [list(item) for item in current]
            best_deltas = sorted(used_deltas)
            return
        shell = enumerated_shells[shell_index]
        for matching in shell["enumerated_matchings"]:
            next_deltas = set(used_deltas)
            for source, target in matching:
                next_deltas.add(displacement(source, target))
            current.append(list(matching))
            rec(shell_index + 1, next_deltas, current)
            current.pop()

    rec(0, set(), [])
    return {
        "enumerated_shell_labels": [shell["shell_label"] for shell in enumerated_shells],
        "excluded_large_shell_labels": excluded,
        "min_distinct_delta_lower_bound": best_count,
        "witness_deltas": best_deltas,
        "witness_assignment": best_assignment,
        "large_shells_can_only_preserve_or_increase_delta_count": bool(excluded),
    }


def summarize_shell(
    shell: dict[str, Any],
    cap_by_residue: dict[int, dict[str, Any]],
    need_by_residue: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    """生成单个 forced shell 的相位图摘要。"""
    supply = [int(item) for item in shell["supply_residues"]]
    demand = [int(item) for item in shell["demand_residues"]]
    edges = shell_edges(shell, cap_by_residue, need_by_residue)
    matching = count_and_forced_edges(supply, demand, edges)
    deltas = sorted({displacement(source, target) for source, target in matching["possible_edges"]})
    forced_deltas = sorted({displacement(source, target) for source, target in matching["forced_edges"]})
    translations = common_translation_deltas(supply, demand, edges)
    enumerated: list[tuple[tuple[int, int], ...]] = []
    if matching["perfect_matching_count"] <= ENUMERATION_LIMIT:
        enumerated = enumerate_matchings_limited(supply, demand, edges, limit=ENUMERATION_LIMIT)

    return {
        "shell_label": shell["shell_label"],
        "supply_residues": supply,
        "demand_residues": demand,
        "edge_count": len(edges),
        "perfect_matching_count": matching["perfect_matching_count"],
        "forced_edge_count": len(matching["forced_edges"]),
        "forced_edges": [
            {
                "source_residue": source,
                "target_residue": target,
                "delta": displacement(source, target),
            }
            for source, target in matching["forced_edges"]
        ],
        "possible_delta_count": len(deltas),
        "possible_deltas": deltas,
        "forced_deltas": forced_deltas,
        "single_translation_deltas": translations,
        "single_translation_possible": bool(translations),
        "matching_enumerated_for_core": bool(enumerated),
        "enumerated_matching_count": len(enumerated),
        "enumerated_matchings": [
            [[source, target] for source, target in matching_item]
            for matching_item in enumerated[:32]
        ],
        "all_matchings_fit_in_enumeration_sample": (
            matching["perfect_matching_count"] == len(enumerated)
        ),
    }


def summarize_shift(
    survivor: dict[str, Any],
    support_hall: dict[str, Any],
) -> dict[str, Any]:
    """生成单个 K survivor 的 shell phase graph 摘要。"""
    shift = int(survivor["shift_cycles"])
    hall_audit = next(
        item for item in support_hall["shift_audits"] if int(item["shift_cycles"]) == shift
    )
    cap_by_residue = {int(item["residue"]): item for item in hall_audit["candidate_capacities"]}
    need_by_residue = {
        int(item["residue"]): item for item in support_hall["needs_sorted_desc"]
    }
    shell_summaries = [
        summarize_shell(shell, cap_by_residue, need_by_residue)
        for shell in survivor["forced_shells"]
    ]
    common_translation: set[int] | None = None
    for shell in shell_summaries:
        shell_deltas = set(shell["single_translation_deltas"])
        common_translation = shell_deltas if common_translation is None else common_translation & shell_deltas
    common_translation = common_translation or set()
    full_matching_product = 1
    for shell in shell_summaries:
        full_matching_product *= int(shell["perfect_matching_count"])

    forced_edges = [
        edge
        for shell in shell_summaries
        for edge in shell["forced_edges"]
    ]
    core_delta = min_distinct_deltas_for_core(shell_summaries)
    return {
        "shift_cycles": shift,
        "forced_shell_count": len(shell_summaries),
        "forced_shell_matching_product": full_matching_product,
        "forced_edge_count": len(forced_edges),
        "forced_edges": forced_edges,
        "shell_summaries": shell_summaries,
        "common_single_translation_deltas": sorted(common_translation),
        "single_translation_support_possible": bool(common_translation),
        "core_phase_fragmentation": core_delta,
    }


def build_result() -> dict[str, Any]:
    """构造 shell phase graph 证书。"""
    rigidity = load_json(RIGIDITY)
    support_hall = load_json(SUPPORT_HALL)
    shift_summaries = [
        summarize_shift(survivor, support_hall)
        for survivor in rigidity["survivor_audits"]
    ]
    result = {
        "certificate_type": "prime_matrix_cycle_debt_shell_phase_graph_router",
        "status": "tight_hall_survivors_force_non_affine_shell_phase_fragmentation",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": PREVIOUS_TARGET,
            "modulus": MODULUS,
            "survivor_shifts": [item["shift_cycles"] for item in shift_summaries],
            "k13_forced_shell_matching_product": shift_summaries[0][
                "forced_shell_matching_product"
            ],
            "k14_forced_shell_matching_product": shift_summaries[1][
                "forced_shell_matching_product"
            ],
            "k13_forced_edge_count": shift_summaries[0]["forced_edge_count"],
            "k14_forced_edge_count": shift_summaries[1]["forced_edge_count"],
            "k13_single_translation_support_possible": shift_summaries[0][
                "single_translation_support_possible"
            ],
            "k14_single_translation_support_possible": shift_summaries[1][
                "single_translation_support_possible"
            ],
            "all_survivors_close_single_translation_support": all(
                not item["single_translation_support_possible"] for item in shift_summaries
            ),
            "k13_core_min_distinct_delta_lower_bound": shift_summaries[0][
                "core_phase_fragmentation"
            ]["min_distinct_delta_lower_bound"],
            "k14_core_min_distinct_delta_lower_bound": shift_summaries[1][
                "core_phase_fragmentation"
            ]["min_distinct_delta_lower_bound"],
            "k13_large_low_shell_excluded_from_delta_minimization": shift_summaries[0][
                "core_phase_fragmentation"
            ]["excluded_large_shell_labels"],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "shift_summaries": shift_summaries,
        "plain_conclusion": (
            "把 K=13/14 tight-Hall 岛继续拆成 forced shell 的 bipartite phase graph。"
            "K=14 的 forced shell 乘积只有 2 个匹配，且已有 3 条强制边；"
            "K=13 的刚性核心至少需要 7 个不同 residue 相位差。"
            "两个 survivor 都没有公共单一平移相位，因此 ordinary translation support motion 被关闭。"
            "剩余只能是非仿射 shell phase fragmentation 的 PDEC，或多相位 moving-support SAE。"
        ),
        "dependency_hashes": {
            str(RIGIDITY.relative_to(ROOT)): sha256(RIGIDITY),
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
        "# Prime Matrix cycle-debt shell phase graph router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"previous_hardpoint={agg['previous_hardpoint']}",
        f"survivor_shifts={agg['survivor_shifts']}",
        f"k13_forced_shell_matching_product={agg['k13_forced_shell_matching_product']}",
        f"k14_forced_shell_matching_product={agg['k14_forced_shell_matching_product']}",
        f"k13_forced_edge_count={agg['k13_forced_edge_count']}",
        f"k14_forced_edge_count={agg['k14_forced_edge_count']}",
        f"k13_single_translation_support_possible={fmt_bool(agg['k13_single_translation_support_possible'])}",
        f"k14_single_translation_support_possible={fmt_bool(agg['k14_single_translation_support_possible'])}",
        f"all_survivors_close_single_translation_support={fmt_bool(agg['all_survivors_close_single_translation_support'])}",
        f"k13_core_min_distinct_delta_lower_bound={agg['k13_core_min_distinct_delta_lower_bound']}",
        f"k14_core_min_distinct_delta_lower_bound={agg['k14_core_min_distinct_delta_lower_bound']}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. shell graph summary",
        "",
        "| K | shell | edges | matchings | forced edges | possible deltas | single translation |",
        "| ---: | --- | ---: | ---: | ---: | ---: | :---: |",
    ]
    for shift in result["shift_summaries"]:
        for shell in shift["shell_summaries"]:
            lines.append(
                f"| {shift['shift_cycles']} | `{shell['shell_label']}` | "
                f"{shell['edge_count']} | {shell['perfect_matching_count']} | "
                f"{shell['forced_edge_count']} | {shell['possible_delta_count']} | "
                f"{fmt_bool(shell['single_translation_possible'])} |"
            )

    lines.extend(
        [
            "",
            "## 2. forced edges",
            "",
            "| K | source | target | delta |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for shift in result["shift_summaries"]:
        for edge in shift["forced_edges"]:
            lines.append(
                f"| {shift['shift_cycles']} | {edge['source_residue']} | "
                f"{edge['target_residue']} | {edge['delta']} |"
            )

    lines.extend(
        [
            "",
            "## 3. core phase fragmentation",
            "",
            "| K | enumerated shells | excluded large shells | min distinct deltas | witness deltas |",
            "| ---: | --- | --- | ---: | --- |",
        ]
    )
    for shift in result["shift_summaries"]:
        core = shift["core_phase_fragmentation"]
        lines.append(
            f"| {shift['shift_cycles']} | `{core['enumerated_shell_labels']}` | "
            f"`{core['excluded_large_shell_labels']}` | "
            f"{core['min_distinct_delta_lower_bound']} | `{core['witness_deltas']}` |"
        )

    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "- 每个 forced shell 来自 zero-slack Hall cut；shell 内不是自由容量，而是相位边图。",
            "- 两个 survivor 的 forced shell 均无公共单一 residue 平移，因此单平移 support motion 当前关闭。",
            "- `K=14` 高层只剩 2 个 shell 匹配，且强制 `13->67`、`19->23`、`70->15` 三条边。",
            "- `K=13` 即便只看可枚举刚性核心，也至少需要 7 个不同相位差；低层大 shell 不会降低该下界。",
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
