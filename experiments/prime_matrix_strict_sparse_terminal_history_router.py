#!/usr/bin/env python3
"""生成 strict 稀疏终端历史 SAE/PDEC 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_sparse_terminal_history_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sparse-terminal-history-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.md",
    MONOGRAPH / "prime-matrix-strict-iterated-scaled-core-density-router.md",
    MONOGRAPH / "prime-matrix-strict-large-pair-kernel-difference-router.md",
    MONOGRAPH / "h4-pdec-admissible-constraint-table.md",
]

SPARSE_HISTORY = "SparseTerminalHistorySAEAbsorptionOrPDECExclusion"
SPARSE_SAE_BUDGET = "SparseTerminalHistorySAEBudgetComparison"
FIXED_HISTORY_PDEC = "FixedTypeHistoryPDECExclusion"
HISTORY_MULTIPLICITY = "FormalUnitSparseHistoryMultiplicityCap"
ADAPTIVE_LAMBDA = "AdaptiveLambdaBalanceForIteratedCoreDensity"


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
    """列出稀疏历史编码引理。"""
    return [
        {
            "name": "history_word_encoding",
            "formula": "A terminal sparse branch is encoded by W=((b_1,c_1),...,(b_r,c_r)) plus orientation metadata.",
            "status": "closed",
            "meaning": "稀疏终端对象有规范有限词编码。",
        },
        {
            "name": "depth_cap",
            "formula": "r<=floor(log_2 |h_0|), because each b_i c_i>=2.",
            "status": "closed",
            "meaning": "历史词长度有限，不能无限增长。",
        },
        {
            "name": "alphabet_cap",
            "formula": "At depth i, #{(b_i,c_i)}<=A_{Lambda_i}<=8Lambda_i^2.",
            "status": "closed",
            "meaning": "每层商型字母表已由上一层闭合。",
        },
        {
            "name": "history_count_cap",
            "formula": "#Histories(depth<=R)<=sum_{r<=R} prod_{i<=r} A_{Lambda_i}.",
            "status": "closed",
            "meaning": "非持久稀疏历史总类型数有显式上界。",
        },
        {
            "name": "persistent_history_pdec",
            "formula": "If the same W recurs above the persistence threshold across formal units, it is FixedTypeHistoryPDEC.",
            "status": "registered_route_open",
            "meaning": "历史词持久化就是命名 PDEC/ColumnCRT 证书。",
        },
        {
            "name": "nonpersistent_history_sae_budget",
            "formula": "If every W has multiplicity <T_PDEC, total sparse mass <=T_PDEC sum_W cap(W).",
            "status": "open_budget",
            "meaning": "非持久分支剩余为 SAE 总量预算比较。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的阈值坍缩稀疏历史分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "HistoryWordEncodingClosed",
            "closed": True,
            "proved": True,
            "meaning": "稀疏终端历史可规范编码为有限商型词。",
            "remaining": "无。",
        },
        {
            "gate": "DepthAndAlphabetCapClosed",
            "closed": True,
            "proved": True,
            "meaning": "历史深度与每层字母表均有显式上界。",
            "remaining": ADAPTIVE_LAMBDA,
        },
        {
            "gate": "PersistentHistoryPDECRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "同一历史词持久复现应进入 PDEC/ColumnCRT。",
            "remaining": FIXED_HISTORY_PDEC,
        },
        {
            "gate": "NonpersistentHistorySAEReductionClosed",
            "closed": True,
            "proved": False,
            "meaning": "非持久历史已压成 SAE 总量预算，但预算比较未完成。",
            "remaining": f"{SPARSE_SAE_BUDGET} AND {HISTORY_MULTIPLICITY}",
        },
        {
            "gate": "SparseTerminalHistoryAbsorbed",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥持久历史 PDEC，也未证明非持久历史总量小于 SAE 预算。",
            "remaining": f"{FIXED_HISTORY_PDEC} AND {SPARSE_SAE_BUDGET}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_sparse_terminal_history_router",
        "status": "sparse_terminal_history_encoded_pdec_or_sae_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "history_word_encoding_closed": True,
        "depth_cap_closed": True,
        "alphabet_cap_closed": True,
        "history_count_cap_closed": True,
        "persistent_history_pdec_route_registered": True,
        "nonpersistent_history_sae_reduction_closed": True,
        "fixed_type_history_pdec_excluded": False,
        "sparse_terminal_history_sae_budget_proved": False,
        "sparse_terminal_history_absorbed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SPARSE_SAE_BUDGET,
        "secondary_attack_target": FIXED_HISTORY_PDEC,
        "parallel_targets": [HISTORY_MULTIPLICITY, ADAPTIVE_LAMBDA],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "稀疏终端历史已经被压成有限词编码。每条终端分支由商型历史 "
            "W=((b_1,c_1),...,(b_r,c_r)) 加有限方向元数据确定；深度 "
            "r<=floor(log_2|h_0|)，每层字母表大小 A_{Lambda_i}<=8Lambda_i^2。"
            "若同一 W 跨 formal unit 持久复现，则进入固定历史 PDEC/ColumnCRT；"
            "若都不持久，则总质量由有限历史数与单历史重数上界控制，进入 SAE 预算比较。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 稀疏终端历史 SAE/PDEC 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"history_word_encoding_closed={fmt_bool(result['history_word_encoding_closed'])}",
        f"depth_cap_closed={fmt_bool(result['depth_cap_closed'])}",
        f"alphabet_cap_closed={fmt_bool(result['alphabet_cap_closed'])}",
        f"history_count_cap_closed={fmt_bool(result['history_count_cap_closed'])}",
        f"persistent_history_pdec_route_registered={fmt_bool(result['persistent_history_pdec_route_registered'])}",
        f"nonpersistent_history_sae_reduction_closed={fmt_bool(result['nonpersistent_history_sae_reduction_closed'])}",
        f"fixed_type_history_pdec_excluded={fmt_bool(result['fixed_type_history_pdec_excluded'])}",
        f"sparse_terminal_history_sae_budget_proved={fmt_bool(result['sparse_terminal_history_sae_budget_proved'])}",
        f"sparse_terminal_history_absorbed={fmt_bool(result['sparse_terminal_history_absorbed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有限历史词",
        "",
        "稀疏终端历史可写成",
        "",
        "```text",
        "W=((b_1,c_1),...,(b_r,c_r))",
        "```",
        "",
        "以及有限方向元数据。深度和字母表满足",
        "",
        "```text",
        "r <= floor(log_2 |h_0|),",
        "#{(b_i,c_i)} <= A_{Lambda_i} <= 8 Lambda_i^2.",
        "```",
        "",
        "所以历史类型数有显式上界：",
        "",
        "```text",
        "#Histories(depth<=R) <= sum_{r<=R} prod_{i<=r} A_{Lambda_i}.",
        "```",
        "",
        "## 2. PDEC/SAE 二分",
        "",
        "同一历史词若跨 formal unit 持久复现，就形成固定历史 `PDEC/ColumnCRT`。若每个历史词都不持久，则总残留质量被历史类型数和单历史重数上界控制，进入 `SAE` 预算。",
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
            "审稿边界：本步闭合稀疏历史的有限编码与 PDEC/SAE 二分；未证明 SAE 预算小于允许阈值，也未排斥固定历史 PDEC。",
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
