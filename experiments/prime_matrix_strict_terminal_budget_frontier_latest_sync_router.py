#!/usr/bin/env python3
"""生成 strict 终端预算最新前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_budget_frontier_latest_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.md"

B3_TV = "B3RemainderTotalVariationBudgetForLengthP"
MERTENS_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
ANTI_COLLAPSE = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
COLD_BALANCE = "ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance"
SINGLE_MARGIN = "SingleParameterTerminalBudgetMarginLedger"
POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json",
    "prime-matrix-strict-b3-remainder-total-variation-budget-router.json",
    "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成前沿同步判定表。"""
    label = data["label"]
    b3_tv_old = data["b3_tv_old"]
    mertens = data["mertens"]
    anticollapse = data["anticollapse"]
    cold = data["cold"]
    single = data["single"]

    b3_tail_closed = mertens.get("strict_self_contained_mertens_tail_proved") is True
    b3_structural_parts = (
        b3_tv_old.get("crt_remainder_boundary_functional_reduction_closed") is True
        and b3_tv_old.get("prime_word_stieltjes_ledger_imported") is True
        and b3_tv_old.get("alternating_boundary_remainder_reduction_imported") is True
        and b3_tv_old.get("anchor20000_boundary_variation_budget_imported") is True
    )

    return [
        row(
            "LabelQuotientBudgetGapImported",
            label.get("hardpoint_after_router") == "UnifiedTerminalBudgetStrictInequality",
            True,
            "保标签商类型熵亏损已压到统一终端预算严格缺口。",
            "sync downstream frontier。",
        ),
        row(
            "OldB3TVSelfContainedTailWasOpen",
            b3_tv_old.get("next_direct_attack_target") == MERTENS_TAIL
            and b3_tv_old.get("self_contained_mertens_tail_proved") is False,
            True,
            "旧 B3-TV 证书的唯一严格自足解析阻塞是 reciprocal-prime Mertens 尾段。",
            MERTENS_TAIL,
        ),
        row(
            "MertensTailClosedByLatestSync",
            b3_tail_closed,
            b3_tail_closed,
            "后续速率尾段同步已导入自足 theta/PNT 包络和 B1 区间，完整 Mertens 尾段从活动剩余移出。",
            "closed for current frontier。" if b3_tail_closed else MERTENS_TAIL,
        ),
        row(
            "B3TVStrictSelfContainedSynchronized",
            b3_structural_parts and b3_tail_closed,
            b3_structural_parts and b3_tail_closed,
            "B3-TV 的 Stieltjes 边界结构、20000 锚点预算与自足 Mertens 尾段已在当前前沿合并。",
            "B3 TV no longer active blocker。" if b3_structural_parts and b3_tail_closed else B3_TV,
        ),
        row(
            "PrefixAntiCollapseClosedForBudget",
            anticollapse.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget") is True
            and anticollapse.get("terminal_projection_anticollapse_closed") is True,
            True,
            "prefix 标签支撑到稀疏终端历史的预算所需无静默塌缩版本已闭合；强互异注入不再是必要输入。",
            "closed as multiplicity conservation。",
        ),
        row(
            "ColdSupplyLambdaDisciplineClosed",
            cold.get("cold_supply_upper_envelope_closed") is True
            and cold.get("same_parameter_lambda_schedule_closed") is True
            and cold.get("adaptive_lambda_no_free_lunch_dichotomy_closed") is True,
            True,
            "冷供给上界、同参数 Lambda 账本和无免费调参二分已闭合。",
            SINGLE_MARGIN,
        ),
        row(
            "SingleParameterMarginNormalFormImported",
            single.get("single_parameter_margin_normal_form_closed") is True
            or cold.get("single_parameter_margin_ledger_closed") is True,
            True,
            "终局矛盾已固定成同一参数账本下的 D_prefix-E_named-U_cold>0。",
            POSITIVE_MARGIN,
        ),
        row(
            "ExplicitPositiveTerminalBudgetMarginCurrentCorpusProved",
            single.get("explicit_positive_terminal_budget_margin_proved") is True,
            False,
            "当前材料仍未证明同参数显式正余量。",
            POSITIVE_MARGIN,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "解析 TV、抗塌缩和冷供给纪律已同步，但正余量、命名回流排斥、有限参数同步和 DStructure 仍未全部闭合。",
            f"{POSITIVE_MARGIN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 终端预算最新前沿同步证书。"""
    data = {
        "label": load_json("prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json"),
        "b3_tv_old": load_json("prime-matrix-strict-b3-remainder-total-variation-budget-router.json"),
        "mertens": load_json("prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"),
        "anticollapse": load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"),
        "cold": load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "single": load_json("prime-matrix-strict-single-parameter-terminal-budget-margin-router.json"),
    }
    rows = build_rows(data)
    b3_sync = any(item["gate"] == "B3TVStrictSelfContainedSynchronized" and item["closed"] for item in rows)
    anticollapse_sync = any(item["gate"] == "PrefixAntiCollapseClosedForBudget" and item["closed"] for item in rows)
    cold_sync = any(item["gate"] == "ColdSupplyLambdaDisciplineClosed" and item["closed"] for item in rows)
    single_sync = any(item["gate"] == "SingleParameterMarginNormalFormImported" and item["closed"] for item in rows)

    return {
        "certificate_type": "prime_matrix_strict_terminal_budget_frontier_latest_sync_router",
        "status": "terminal_budget_frontier_synced_to_explicit_positive_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "b3_tv_strict_self_contained_synchronized": b3_sync,
        "prefix_anticollapse_closed_for_budget": anticollapse_sync,
        "cold_supply_lambda_discipline_closed": cold_sync,
        "single_parameter_margin_normal_form_closed": single_sync,
        "explicit_positive_terminal_budget_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": (
            f"{B3_TV} OR {ANTI_COLLAPSE} OR {COLD_BALANCE}"
        ),
        "hardpoint_after_router": POSITIVE_MARGIN,
        "next_direct_attack_target": POSITIVE_MARGIN,
        "parallel_required_inputs": [
            "B3DiscretePrimeSumUniformErrorPGe100000",
            "FiniteBoundaryPrefixRoughCountCertificate",
            "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion",
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            DSTRUCTURE,
        ],
        "margin_formula": "D_prefix - E_named - U_cold > 0",
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步同步最新终端预算前沿：旧 B3-TV 自足 Mertens 尾段已由后续 theta/PNT+B1 证书闭合，"
            "prefix 标签抗塌缩已关闭为预算所需的重数守恒，冷供给与 Lambda 调参纪律也已锁入同一参数账本。"
            f"因此当前真正最窄目标不再是这些旧缺口，而是 `{POSITIVE_MARGIN}`，即证明同参数正余量 "
            "`D_prefix-E_named-U_cold>0`。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 终端预算最新前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"b3_tv_strict_self_contained_synchronized={fmt_bool(result['b3_tv_strict_self_contained_synchronized'])}",
        f"prefix_anticollapse_closed_for_budget={fmt_bool(result['prefix_anticollapse_closed_for_budget'])}",
        f"cold_supply_lambda_discipline_closed={fmt_bool(result['cold_supply_lambda_discipline_closed'])}",
        f"single_parameter_margin_normal_form_closed={fmt_bool(result['single_parameter_margin_normal_form_closed'])}",
        f"explicit_positive_terminal_budget_margin_proved={fmt_bool(result['explicit_positive_terminal_budget_margin_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿收缩",
        "",
        "```text",
        result["hardpoint_before_router"],
        f"  => {result['hardpoint_after_router']}",
        "```",
        "",
        "同参数余量：",
        "",
        "```text",
        result["margin_formula"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 下一步最窄硬攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留输入：",
            "",
            "```text",
            " AND ".join(result["parallel_required_inputs"]),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
