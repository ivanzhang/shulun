#!/usr/bin/env python3
"""生成 strict 缩频终端核心除数窗口上界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
]

CORE_CAP = "ScaledTerminalCoreDivisorWindowCountCap"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
COLD_BUDGET = "ColdCoreThresholdBudgetGapComparison"
FORCED_LOAD = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
LCM_HEIGHT = "TerminalCoreLCMHeightContradictionOrPDEC"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def lemmas() -> list[dict[str, str]]:
    """列出终端核心窗口引理。"""
    return [
        {
            "name": "scaled_core_frequency",
            "formula": "H_W=h_0/D(W), and every terminal core counted for W divides H_W.",
            "status": "closed",
            "meaning": "终端核心除数窗口有明确缩频频率。",
        },
        {
            "name": "terminal_core_window",
            "formula": "Cores lie in I_W=(Y_W^-,Y_W^+] with endpoints inherited from the product window ledger.",
            "status": "closed",
            "meaning": "终端核心落在明确窗口内。",
        },
        {
            "name": "cold_hot_split",
            "formula": "N_{H_W}(I_W)<=C_core(W) or N_{H_W}(I_W)>C_core(W).",
            "status": "closed_dichotomy",
            "meaning": "单历史容量被拆成冷核心预算或热核心异常。",
        },
        {
            "name": "cold_core_insert",
            "formula": "In the cold case, Cap(W)<=C_core(W) is valid in the SAE budget.",
            "status": "closed_conditional",
            "meaning": "冷核心阈值可直接进入供给上界。",
        },
        {
            "name": "hot_core_to_lcm_or_pdec",
            "formula": "Hot terminal core windows route to LCM-height contradiction, fixed-history PDEC, or SAE.",
            "status": "registered_route_open",
            "meaning": "热核心窗口不是新黑箱，回流到已有矛盾场。",
        },
        {
            "name": "budget_gap_after_cold_insert",
            "formula": "After cold insertion, prove L_forced > sum_W (T_PDEC(W)-1) C_core(W).",
            "status": "open_input",
            "meaning": "剩余供需比较转为冷核心阈值预算缺口。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的单历史重数上界分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ScaledCoreFrequencyAndWindowClosed",
            "closed": True,
            "proved": True,
            "meaning": "终端核心窗口已写成 `H_W` 上的除数窗口。",
            "remaining": "无。",
        },
        {
            "gate": "ColdHotSplitClosed",
            "closed": True,
            "proved": True,
            "meaning": "核心窗口计数被拆成冷阈值或热异常。",
            "remaining": f"{COLD_BUDGET} OR {HOT_CORE}",
        },
        {
            "gate": "ColdCoreBudgetInsertionClosed",
            "closed": True,
            "proved": True,
            "meaning": "冷核心阈值可替换 `Cap(W)` 插入 SAE 预算。",
            "remaining": COLD_BUDGET,
        },
        {
            "gate": "HotCoreRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "热核心窗口进入 LCM/PDEC/SAE，但尚未排斥。",
            "remaining": f"{HOT_CORE} AND {LCM_HEIGHT}",
        },
        {
            "gate": "ScaledTerminalCoreDivisorWindowCountCapProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有核心窗口均冷，也未排斥热核心回流。",
            "remaining": f"{HOT_CORE} AND {COLD_BUDGET}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_scaled_terminal_core_divisor_window_router",
        "status": "scaled_terminal_core_divisor_window_split_to_cold_budget_or_hot_core_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "scaled_core_frequency_closed": True,
        "terminal_core_window_closed": True,
        "cold_hot_split_closed": True,
        "cold_core_budget_insertion_closed": True,
        "hot_core_route_registered": True,
        "scaled_terminal_core_divisor_window_count_cap_proved": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "cold_core_threshold_budget_gap_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": COLD_BUDGET,
        "secondary_attack_target": HOT_CORE,
        "parallel_targets": [FORCED_LOAD, LCM_HEIGHT],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "缩频终端核心除数窗口已被拆成冷预算和热异常两类。对历史词 W，"
            "令 H_W=h_0/D(W)，终端核心必须整除 H_W 并落在窗口 I_W。"
            "若 N_{H_W}(I_W)<=C_core(W)，则 Cap(W)<=C_core(W) 可直接插入 SAE 供给预算；"
            "若超过该阈值，则它是 TerminalCoreHotDivisorWindow，必须回流到 LCM 高度矛盾、"
            "固定历史 PDEC 或 SAE，而不能作为自由容量保留。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 缩频终端核心除数窗口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"scaled_core_frequency_closed={fmt_bool(result['scaled_core_frequency_closed'])}",
        f"terminal_core_window_closed={fmt_bool(result['terminal_core_window_closed'])}",
        f"cold_hot_split_closed={fmt_bool(result['cold_hot_split_closed'])}",
        f"cold_core_budget_insertion_closed={fmt_bool(result['cold_core_budget_insertion_closed'])}",
        f"hot_core_route_registered={fmt_bool(result['hot_core_route_registered'])}",
        f"scaled_terminal_core_divisor_window_count_cap_proved={fmt_bool(result['scaled_terminal_core_divisor_window_count_cap_proved'])}",
        f"terminal_core_hot_divisor_window_excluded={fmt_bool(result['terminal_core_hot_divisor_window_excluded'])}",
        f"cold_core_threshold_budget_gap_proved={fmt_bool(result['cold_core_threshold_budget_gap_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 核心窗口",
        "",
        "对历史词 `W`，定义",
        "",
        "```text",
        "H_W = h_0 / D(W).",
        "```",
        "",
        "终端核心计数是",
        "",
        "```text",
        "N_{H_W}(I_W)=#{k: k|H_W, k in I_W}.",
        "```",
        "",
        "## 2. 冷/热分裂",
        "",
        "对每个 `W` 固定阈值 `C_core(W)`：",
        "",
        "```text",
        "cold: N_{H_W}(I_W)<=C_core(W);",
        "hot:  N_{H_W}(I_W)> C_core(W).",
        "```",
        "",
        "冷分支进入 SAE 预算，热分支回流到 LCM/PDEC/SAE。",
        "",
        "## 3. 引理表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["lemmas"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一步最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并列需要补齐：",
            "",
            "```text",
            result["secondary_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步闭合核心窗口的冷/热分裂；未证明冷预算缺口，也未排斥热核心回流。",
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
