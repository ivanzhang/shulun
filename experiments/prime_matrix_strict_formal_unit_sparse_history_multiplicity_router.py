#!/usr/bin/env python3
"""生成 strict formal-unit 稀疏历史重数上界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md",
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.md",
]

MULTIPLICITY_CAP = "FormalUnitSparseHistoryMultiplicityCap"
CORE_DIVISOR_CAP = "ScaledTerminalCoreDivisorWindowCountCap"
HISTORY_PDEC = "FixedTypeHistoryPDECExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FORCED_LOAD = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"


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
    """列出单历史重数上界引理。"""
    return [
        {
            "name": "history_product_identity",
            "formula": "For W=((b_i,c_i)), D(W)=prod_i b_i c_i and terminal cores divide h_0/D(W).",
            "status": "closed",
            "meaning": "历史词决定唯一缩频分母。",
        },
        {
            "name": "terminal_core_interval",
            "formula": "Terminal cores k lie in an explicit interval I_W inherited from the product window ledger.",
            "status": "closed",
            "meaning": "单历史容量变成缩频上的窗口除数计数。",
        },
        {
            "name": "multiplicity_to_divisor_count",
            "formula": "Mult_U(W) <= N_{h_0/D(W)}(I_W).",
            "status": "closed",
            "meaning": "同一 formal unit 内同一历史词的重数不超过缩频终端核心除数数。",
        },
        {
            "name": "hot_core_route",
            "formula": "If N_{h_0/D(W)}(I_W) exceeds the cap, it is a terminal core hot divisor window and routes to PDEC/SAE.",
            "status": "registered_route_open",
            "meaning": "单历史容量过大不是自由预算，而是回流到热除数/PDEC/SAE。",
        },
        {
            "name": "cold_core_capacity",
            "formula": "If no hot core window occurs, Cap(W) is bounded by the registered cold-core threshold C_core(W).",
            "status": "closed_conditional",
            "meaning": "在排除热核心出口后，单历史容量有可插入 SAE 预算的上界。",
        },
        {
            "name": "cap_to_budget_gap",
            "formula": "Insert Cap(W)<=C_core(W) into U_sparse <= sum_W (T_PDEC(W)-1)Cap(W).",
            "status": "closed_reduction",
            "meaning": "单历史重数上界已接回供需预算缺口。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的稀疏历史 SAE 预算分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "HistoryProductIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "历史词给出缩频分母 `D(W)`。",
            "remaining": "无。",
        },
        {
            "gate": "MultiplicityToDivisorCountClosed",
            "closed": True,
            "proved": True,
            "meaning": "单历史重数已压成缩频终端核心窗口除数计数。",
            "remaining": CORE_DIVISOR_CAP,
        },
        {
            "gate": "HotCoreRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "核心窗口计数过大时回流 PDEC/SAE。",
            "remaining": HOT_CORE,
        },
        {
            "gate": "ColdCoreCapacityInserted",
            "closed": True,
            "proved": False,
            "meaning": "无热核心时可把冷核心阈值插回 SAE 预算，但阈值比较未完成。",
            "remaining": f"{CORE_DIVISOR_CAP} AND {FORCED_LOAD}",
        },
        {
            "gate": "FormalUnitSparseHistoryMultiplicityCapProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥热核心窗口，也未给出足够强的冷核心容量阈值。",
            "remaining": f"{HOT_CORE} AND {CORE_DIVISOR_CAP}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_formal_unit_sparse_history_multiplicity_router",
        "status": "formal_unit_sparse_history_multiplicity_reduced_to_scaled_core_divisor_cap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "history_product_identity_closed": True,
        "terminal_core_interval_closed": True,
        "multiplicity_to_divisor_count_closed": True,
        "hot_core_route_registered": True,
        "cold_core_capacity_inserted": True,
        "formal_unit_sparse_history_multiplicity_cap_proved": False,
        "scaled_terminal_core_divisor_window_count_cap_proved": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": CORE_DIVISOR_CAP,
        "parallel_targets": [HOT_CORE, HISTORY_PDEC, FORCED_LOAD],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "formal-unit 稀疏历史重数已经压成缩频终端核心除数窗口计数。"
            "对历史词 W，令 D(W)=prod b_i c_i，则同一 formal unit 内该历史的终端核心 "
            "都必须整除 h_0/D(W)，并落在由窗口乘积账本给出的区间 I_W。"
            "因此 Mult_U(W)<=N_{h_0/D(W)}(I_W)。若该窗口计数过大，就回流为 "
            "TerminalCoreHotDivisorWindowPDECorSAE；若不过大，冷核心阈值可插入 SAE 预算。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict formal-unit 稀疏历史重数上界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"history_product_identity_closed={fmt_bool(result['history_product_identity_closed'])}",
        f"terminal_core_interval_closed={fmt_bool(result['terminal_core_interval_closed'])}",
        f"multiplicity_to_divisor_count_closed={fmt_bool(result['multiplicity_to_divisor_count_closed'])}",
        f"hot_core_route_registered={fmt_bool(result['hot_core_route_registered'])}",
        f"cold_core_capacity_inserted={fmt_bool(result['cold_core_capacity_inserted'])}",
        f"formal_unit_sparse_history_multiplicity_cap_proved={fmt_bool(result['formal_unit_sparse_history_multiplicity_cap_proved'])}",
        f"scaled_terminal_core_divisor_window_count_cap_proved={fmt_bool(result['scaled_terminal_core_divisor_window_count_cap_proved'])}",
        f"terminal_core_hot_divisor_window_excluded={fmt_bool(result['terminal_core_hot_divisor_window_excluded'])}",
        f"fixed_type_history_pdec_excluded={fmt_bool(result['fixed_type_history_pdec_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单历史容量",
        "",
        "对历史词",
        "",
        "```text",
        "W=((b_1,c_1),...,(b_r,c_r)),",
        "D(W)=prod_i b_i c_i.",
        "```",
        "",
        "同一 formal unit 内的终端核心必须满足",
        "",
        "```text",
        "k | h_0/D(W),  k in I_W.",
        "```",
        "",
        "所以",
        "",
        "```text",
        "Mult_U(W) <= N_{h_0/D(W)}(I_W).",
        "```",
        "",
        "这把抽象 `Cap(W)` 改写为缩频终端核心除数窗口计数。",
        "",
        "## 2. 出口",
        "",
        "若该除数窗口热，则进入 `TerminalCoreHotDivisorWindowPDECorSAE`；若不热，则用冷核心阈值 `C_core(W)` 进入 SAE 预算。",
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
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步闭合单历史重数到缩频除数窗口的改写；未排斥热核心窗口，也未证明冷核心阈值足以闭合 SAE 预算。",
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
