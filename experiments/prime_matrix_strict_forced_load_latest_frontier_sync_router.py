#!/usr/bin/env python3
"""生成 strict 强制负载最新前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_forced_load_latest_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-forced-load-latest-frontier-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-forced-load-latest-frontier-sync-router.json
  docs/monograph/prime-matrix-strict-forced-load-latest-frontier-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-forced-load-latest-frontier-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-forced-load-latest-frontier-sync-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json",
    MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json",
    MONOGRAPH / "prime-matrix-b3-prime-word-stieltjes-integral-router.json",
    MONOGRAPH / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json",
    MONOGRAPH / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json",
    MONOGRAPH / "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
]

FORCED_LOAD = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
NORMALIZED = "NormalizedPrefixResidualPotentialLowerBound"
UNIFORM_ROUGH = "UniformPrefixRoughCountLowerBound"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE_ANTICOLLAPSE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
SPARSE_HISTORY_ANTICOLLAPSE = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取证书 JSON，缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证书哈希，方便复核同步来源。"""
    result = {"script": sha256(Path(__file__).resolve())}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def decision_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成本轮最新前沿同步判定表。"""
    positive = data["positive"]
    forced = data["forced"]
    sparse_anti = data["sparse_anti"]
    normalized = data["normalized"]
    uniform = data["uniform"]
    continuous = data["continuous"]
    stieltjes = data["stieltjes"]
    signed_delay = data["signed_delay"]
    mertens_sync = data["mertens_sync"]
    terminal_sync = data["terminal_sync"]

    b3_analytic_synced = (
        continuous.get("continuous_beta_sieve_surplus_proved") is True
        and stieltjes.get("prime_word_stieltjes_integral_ledger_closed") is True
        and signed_delay.get("b3_boundary_variation_one_percent_conditional_closed") is True
        and terminal_sync.get("b3_tv_strict_self_contained_synchronized") is True
        and mertens_sync.get("strict_self_contained_mertens_tail_proved") is True
    )

    return [
        {
            "gate": "PositiveMarginDrilldownImported",
            "closed": positive.get("explicit_positive_terminal_budget_margin_imported") is True,
            "proved": False,
            "meaning": "最新正余量目标已下钻到 finite prefix、强制负载、命名回流、moving atom 和 DStructure。",
            "remaining": f"{FINITE_PREFIX} AND {FORCED_LOAD} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
        {
            "gate": "ForcedLoadConservationImported",
            "closed": forced.get("forced_load_criterion_closed") is True,
            "proved": True,
            "meaning": "早期零行反例链给出 M# 扣除命名回流后的终端负载守恒。",
            "remaining": f"{NORMALIZED} AND {NAMED_RETURN}",
        },
        {
            "gate": "SparseHistoryAntiCollapseClosedForBudget",
            "closed": sparse_anti.get("multiplicity_conservation_anticollapse_closed") is True,
            "proved": True,
            "meaning": "预算所需的无静默塌缩/重数守恒已经关闭；强互异历史注入不是必要输入。",
            "remaining": "strong distinct injection not needed for current budget",
        },
        {
            "gate": "NormalizedPotentialReduced",
            "closed": normalized.get("multiplier_to_rough_count_reduction_closed") is True,
            "proved": False,
            "meaning": "M# 势下界已化为 prefix 粗筛余下界、formal-unit 类型阈值和有限段证书。",
            "remaining": f"{UNIFORM_ROUGH} AND {TYPE_LEDGER} AND {FINITE_PREFIX}",
        },
        {
            "gate": "UniformRoughCountFormulaImported",
            "closed": uniform.get("main_error_split_closed") is True,
            "proved": False,
            "meaning": "prefix 粗筛余已接到 lower weights 主项减边界余项公式。",
            "remaining": f"B3 analytic budget AND {FINITE_PREFIX}",
        },
        {
            "gate": "B3AnalyticBudgetLatestSynced",
            "closed": b3_analytic_synced,
            "proved": b3_analytic_synced,
            "meaning": "连续主项、Stieltjes 精确表示、20000 锚点 delay 乘子和最新 Mertens 尾段同步后，旧 B3-TV/离散误差不再是本前沿活动最窄阻塞。",
            "remaining": "auditable sync only; reviewer may still audit B3 certificates independently",
        },
        {
            "gate": "FiniteBoundaryPrefixCertificateStillAbsent",
            "closed": False,
            "proved": False,
            "meaning": "有限边界 prefix 粗筛余证书同时卡住 D0 hash 和 UniformPrefixRoughCount 的有限段。",
            "remaining": FINITE_PREFIX,
        },
        {
            "gate": "FormalUnitTypeThresholdStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "即使粗筛余数量有统一下界，还需同一 row-free type alphabet 的阈值比较。",
            "remaining": f"{TYPE_LEDGER} AND {ROW_FREE_ANTICOLLAPSE}",
        },
        {
            "gate": "NamedReturnAndTerminalAtomsStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "PDEC/SAE/ColumnCRT、热核心、固定历史和 actual noncanonical moving atom 仍未排斥。",
            "remaining": f"{NAMED_RETURN} AND ({HOT_CORE} OR {FIXED_HISTORY}) AND {MOVING_ATOM}",
        },
        {
            "gate": "SparseTerminalForcedLoadCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "强制负载下界尚未完成，因为有限 prefix、类型阈值、row-free 抗塌缩和命名回流仍未同时闭合。",
            "remaining": f"{FINITE_PREFIX} AND {TYPE_LEDGER} AND {ROW_FREE_ANTICOLLAPSE} AND {NAMED_RETURN}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步是最新前沿同步，不是终局矛盾；仍未得到排除早期零行反例链的无条件闭合。",
            "remaining": f"{FINITE_PREFIX} AND {TYPE_LEDGER} AND {NAMED_RETURN} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 强制负载最新前沿同步证书。"""
    data = {
        "positive": load_json(MONOGRAPH / "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json"),
        "forced": load_json(MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json"),
        "sparse_anti": load_json(MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"),
        "normalized": load_json(MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json"),
        "uniform": load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json"),
        "continuous": load_json(MONOGRAPH / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json"),
        "stieltjes": load_json(MONOGRAPH / "prime-matrix-b3-prime-word-stieltjes-integral-router.json"),
        "signed_delay": load_json(MONOGRAPH / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"),
        "mertens_sync": load_json(MONOGRAPH / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"),
        "terminal_sync": load_json(MONOGRAPH / "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"),
    }
    rows = decision_rows(data)
    b3_row = next(row for row in rows if row["gate"] == "B3AnalyticBudgetLatestSynced")

    return {
        "certificate_type": "prime_matrix_strict_forced_load_latest_frontier_sync_router",
        "status": "forced_load_frontier_synced_to_finite_prefix_type_threshold_named_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "positive_margin_drilldown_imported": rows[0]["closed"],
        "forced_load_conservation_imported": rows[1]["closed"],
        "sparse_history_anticollapse_closed_for_budget": rows[2]["closed"],
        "normalized_potential_reduced": rows[3]["closed"],
        "uniform_rough_count_formula_imported": rows[4]["closed"],
        "b3_analytic_budget_latest_synced": b3_row["closed"],
        "finite_boundary_prefix_certificate_proved": False,
        "formal_unit_type_threshold_ledger_proved": False,
        "row_free_type_anticollapse_proved": False,
        "named_return_exclusion_proved": False,
        "sparse_terminal_forced_load_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": FINITE_PREFIX,
        "parallel_attack_targets": [
            TYPE_LEDGER,
            ROW_FREE_ANTICOLLAPSE,
            NAMED_RETURN,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "latest_forced_load_basis": (
            f"{FINITE_PREFIX} AND {TYPE_LEDGER} AND {ROW_FREE_ANTICOLLAPSE} "
            f"AND {NAMED_RETURN} AND ({HOT_CORE} OR {FIXED_HISTORY}) "
            f"AND {MOVING_ATOM} AND {DSTRUCTURE}"
        ),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow 同步到最新前沿："
            "强制负载守恒和稀疏历史预算抗塌缩已经可用；B3 解析预算不再作为本前沿的活动最窄阻塞。"
            "真正剩余收缩为有限边界 prefix 粗筛余证书、formal-unit 类型阈值/row-free 抗塌缩、"
            "命名回流与 actual noncanonical moving atom 排斥，以及 DStructure/Rankin 独立门。"
            "因此下一最窄可攻点是 FiniteBoundaryPrefixRoughCountCertificate。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 强制负载最新前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"positive_margin_drilldown_imported={fmt_bool(result['positive_margin_drilldown_imported'])}",
        f"forced_load_conservation_imported={fmt_bool(result['forced_load_conservation_imported'])}",
        f"sparse_history_anticollapse_closed_for_budget={fmt_bool(result['sparse_history_anticollapse_closed_for_budget'])}",
        f"normalized_potential_reduced={fmt_bool(result['normalized_potential_reduced'])}",
        f"uniform_rough_count_formula_imported={fmt_bool(result['uniform_rough_count_formula_imported'])}",
        f"b3_analytic_budget_latest_synced={fmt_bool(result['b3_analytic_budget_latest_synced'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"formal_unit_type_threshold_ledger_proved={fmt_bool(result['formal_unit_type_threshold_ledger_proved'])}",
        f"row_free_type_anticollapse_proved={fmt_bool(result['row_free_type_anticollapse_proved'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"sparse_terminal_forced_load_lower_bound_proved={fmt_bool(result['sparse_terminal_forced_load_lower_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步后收缩",
        "",
        "```text",
        f"{FORCED_LOAD}",
        "  =>",
        result["latest_forced_load_basis"],
        "```",
        "",
        "其中 B3 解析预算只作为可审查同步输入导入；本证书不把外部条件、数值样本或旧 runner 结果当作终局证明。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]

    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    cell(row["meaning"]),
                    cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步完成的是最新前沿校准。行/列命题仍未无条件闭合；"
            "只有有限 prefix、类型阈值、命名回流、moving atom 与 DStructure 门都关闭后，"
            "才可把早期零行反例链推进为终端矛盾。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
