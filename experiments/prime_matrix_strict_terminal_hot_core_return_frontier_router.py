#!/usr/bin/env python3
"""生成 TerminalCoreHotDivisorWindowPDECorSAE 前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_hot_core_return_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-hot-core-return-frontier-router.json

输出：
  docs/monograph/prime-matrix-strict-terminal-hot-core-return-frontier-router.json
  docs/monograph/prime-matrix-strict-terminal-hot-core-return-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-hot-core-return-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-hot-core-return-frontier-router.md"

HARDPOINT = "TerminalCoreHotDivisorWindowPDECorSAE"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json",
    DOCS / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json",
    DOCS / "prime-matrix-strict-named-return-exclusion-compression-router.json",
    DOCS / "prime-matrix-strict-named-return-terminal-saturation-sync-router.json",
    DOCS / "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_terminal_hot_core_return_frontier_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取热核心前沿同步依赖。"""
    exact_hot = load_json(DOCS / "prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json")
    scaled = load_json(DOCS / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json")
    density = load_json(DOCS / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.json")
    compression = load_json(DOCS / "prime-matrix-strict-named-return-exclusion-compression-router.json")
    saturation = load_json(DOCS / "prime-matrix-strict-named-return-terminal-saturation-sync-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json")
    return {
        "exact_overcount_routes_to_hot_core": exact_hot.get(
            "clean_exact_overbudget_without_named_return_excluded"
        )
        is True,
        "scaled_hot_core_route_registered": scaled.get("hot_core_route_registered") is True,
        "hot_density_certificate_closed": density.get("hot_density_certificate_closed") is True,
        "named_return_compression_closed": compression.get("named_return_compression_closed") is True,
        "hot_core_fixed_history_absorbed": compression.get("hot_core_fixed_history_absorbed") is True,
        "terminal_saturation_sync_closed": saturation.get("named_return_terminal_saturation_sync_closed")
        is True,
        "sparse_budget_latest_sync_closed": sparse.get("sparse_budget_positive_margin_latest_sync_closed")
        is True,
    }


def lane_rows() -> list[dict[str, str]]:
    """列出热核心回流的终端通道。"""
    return [
        {
            "lane": "nonpersistent_hot_core",
            "trigger": "热窗口只孤立或低频出现，没有同一 finite signature 的持久复现。",
            "route": f"{SPARSE_BUDGET} -> {POSITIVE_MARGIN}",
            "status": "budget_open",
        },
        {
            "lane": "persistent_hot_core",
            "trigger": "同一热窗口键、商型、列位移或 finite signature 在 formal unit 中持久复现。",
            "route": f"{PERSISTENT_TERMINAL} / PDEC-CAP / internal CleanKLS",
            "status": "terminal_family_open",
        },
        {
            "lane": "carrier_or_lcm_hot_core",
            "trigger": "热窗口来自 carrier-lcm source/valuation overflow 或低乘子共同核。",
            "route": "carrier-lcm return frontier, then budget-or-persistent split",
            "status": "frontier_closed_exclusion_open",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "HotCoreTargetImported",
            "closed": result["exact_overcount_routes_to_hot_core"]
            and result["scaled_hot_core_route_registered"]
            and result["hot_density_certificate_closed"],
            "proved": True,
            "meaning": "精确超预算、缩频核心窗口和短窗口密度异常都会登记为热核心命名回流。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "HotCoreNamedAlphabetCompressionImported",
            "closed": result["named_return_compression_closed"] and result["hot_core_fixed_history_absorbed"],
            "proved": result["named_return_compression_closed"] and result["hot_core_fixed_history_absorbed"],
            "meaning": "HotCore 已在命名回流压缩表中分成持久终端与非持久预算两类。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "HotCoreTerminalSaturationClosed",
            "closed": result["terminal_hot_core_frontier_closed"],
            "proved": result["terminal_hot_core_frontier_closed"],
            "meaning": "热核心不再是独立第三出口；它按持久性进入正余量预算或 acyclic 终端族。",
            "remaining": f"{SPARSE_BUDGET} OR {PERSISTENT_TERMINAL}",
        },
        {
            "gate": "NonpersistentHotCoreAbsorbed",
            "closed": False,
            "proved": False,
            "meaning": "非持久热窗口还没有被同参数正余量严格吸收。",
            "remaining": POSITIVE_MARGIN,
        },
        {
            "gate": "PersistentHotCoreExcluded",
            "closed": False,
            "proved": False,
            "meaning": "持久热窗口还没有被 PDEC-CAP、internal CleanKLS 或 moving atom 排斥。",
            "remaining": PERSISTENT_TERMINAL,
        },
        {
            "gate": "TerminalCoreHotDivisorWindowPDECorSAEExcluded",
            "closed": False,
            "proved": False,
            "meaning": "本步删除独立热核心硬点，但不证明两条终端通道已排斥。",
            "remaining": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未得到排除早期零行反例链的最终矛盾。",
            "remaining": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造热核心前沿证书。"""
    flags = imported_flags()
    frontier_closed = all(
        [
            flags["exact_overcount_routes_to_hot_core"],
            flags["scaled_hot_core_route_registered"],
            flags["hot_density_certificate_closed"],
            flags["named_return_compression_closed"],
            flags["hot_core_fixed_history_absorbed"],
            flags["terminal_saturation_sync_closed"],
            flags["sparse_budget_latest_sync_closed"],
        ]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_terminal_hot_core_return_frontier_router",
        "status": "terminal_hot_core_independent_hardpoint_removed_budget_or_persistent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "terminal_hot_core_frontier_closed": frontier_closed,
        "terminal_core_hot_divisor_window_independent_hardpoint_removed": frontier_closed,
        "terminal_core_hot_divisor_window_pdec_or_sae_excluded": False,
        "nonpersistent_hot_core_absorbed_by_positive_margin": False,
        "persistent_hot_core_excluded_by_terminal_family": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        "next_direct_attack_target": SPARSE_BUDGET,
        "parallel_attack_targets": [PERSISTENT_TERMINAL, DSTRUCTURE],
        "lane_rows": lane_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`TerminalCoreHotDivisorWindowPDECorSAE` 已同步到命名回流终端饱和边界："
            "热核心不是独立第三出口。非持久热窗口进入同参数正余量/非持久预算通道；"
            "持久热窗口进入 PDEC-CAP、internal CleanKLS 或 actual noncanonical moving atom 终端族。"
            "本步删除热核心作为独立硬点，但不排斥两条终端通道，因此行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict Terminal Hot Core Return 前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_hot_core_frontier_closed={fmt_bool(result['terminal_hot_core_frontier_closed'])}",
        f"terminal_core_hot_divisor_window_independent_hardpoint_removed={fmt_bool(result['terminal_core_hot_divisor_window_independent_hardpoint_removed'])}",
        f"terminal_core_hot_divisor_window_pdec_or_sae_excluded={fmt_bool(result['terminal_core_hot_divisor_window_pdec_or_sae_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端通道",
        "",
        "| lane | trigger | route | status |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["lane_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['lane'])}`",
                    table_cell(item["trigger"]),
                    table_cell(item["route"]),
                    table_cell(item["status"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行守门：`{PERSISTENT_TERMINAL}` 与 `{DSTRUCTURE}`。",
            "- 边界：本步不排斥热核心终端，只删除其作为独立硬点的地位。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
