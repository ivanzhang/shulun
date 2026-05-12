#!/usr/bin/env python3
"""生成 strict 迭代阈值坍缩账本路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_iterated_threshold_collapse_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-iterated-threshold-collapse-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-iterated-scaled-core-density-router.md",
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-density-transfer-router.md",
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-large-pair-kernel-difference-router.md",
]

THRESHOLD_COLLAPSE = "IteratedThresholdCollapseExclusionLedger"
SPARSE_HISTORY = "SparseTerminalHistorySAEAbsorptionOrPDECExclusion"
FIXED_HISTORY_PDEC = "FixedTypeHistoryPDECExclusion"
SPARSE_SAE = "SparseTerminalDescentSAEAbsorptionLedger"
ADAPTIVE_LAMBDA = "AdaptiveLambdaBalanceForIteratedCoreDensity"
DEPTH_LCM = "DepthwiseLCMExplosionAgainstScaledFrequencyHeight"


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
    """列出阈值坍缩账本引理。"""
    return [
        {
            "name": "effective_core_lower_bound",
            "formula": "M_r >= rho_0 Y_0 / prod_{i<=r}(A_i M_i), where A_i<=8Lambda_i^2 and M_i=max(b_i,c_i)<2Lambda_i.",
            "status": "closed",
            "meaning": "核心数量下界同时登记密度损耗和窗口缩短。",
        },
        {
            "name": "collapse_inequality",
            "formula": "Threshold collapse at depth r means prod_{i<=r}(A_i M_i) > rho_0 Y_0.",
            "status": "closed",
            "meaning": "阈值坍缩等价于显式乘积账本超出初始质量预算。",
        },
        {
            "name": "coarse_lambda_sufficient_collapse_condition",
            "formula": "Since A_i M_i <=16 Lambda_i^3, survival is guaranteed if prod_i 16Lambda_i^3 <= rho_0 Y_0.",
            "status": "closed_sufficient",
            "meaning": "给出可调 Lambda 纪律；粗界只作充分条件，不当作最终证明。",
        },
        {
            "name": "minimal_collapse_sparse_terminal",
            "formula": "At the first depth r with M_r<1, any actual surviving branch is a sparse terminal history, not a dense window.",
            "status": "closed_reduction",
            "meaning": "阈值坍缩不再是第四种高密度出口，而是稀疏终端历史。",
        },
        {
            "name": "persistent_history_to_pdec",
            "formula": "A sparse terminal history recurring for the same quotient-type history across formal units is a fixed-type-history PDEC.",
            "status": "registered_route_open",
            "meaning": "同一历史若持久，必须进入 PDEC/ColumnCRT，不可作为自由残留。",
        },
        {
            "name": "nonpersistent_history_to_sae",
            "formula": "Nonpersistent terminal histories are counted by finite depth and finite quotient alphabet, hence route to SAE.",
            "status": "registered_route_open",
            "meaning": "不持久残留是稀疏异常，需由 SAE 总量账本吸收。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的迭代缩频阈值分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "CollapseInequalityClosed",
            "closed": True,
            "proved": True,
            "meaning": "阈值坍缩已写成显式乘积不等式。",
            "remaining": ADAPTIVE_LAMBDA,
        },
        {
            "gate": "SparseTerminalReductionClosed",
            "closed": True,
            "proved": True,
            "meaning": "最早坍缩层后的实际残留只能是稀疏终端历史。",
            "remaining": SPARSE_HISTORY,
        },
        {
            "gate": "PersistentHistoryPDECRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "同一商型历史持久复现应进入 PDEC/ColumnCRT。",
            "remaining": FIXED_HISTORY_PDEC,
        },
        {
            "gate": "NonpersistentHistorySAERouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "非持久终端历史应由有限深度/有限字母表 SAE 账本吸收。",
            "remaining": SPARSE_SAE,
        },
        {
            "gate": "ThresholdCollapseExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未排斥持久历史 PDEC，也未闭合非持久历史 SAE 总量吸收。",
            "remaining": f"{FIXED_HISTORY_PDEC} AND {SPARSE_SAE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_iterated_threshold_collapse_router",
        "status": "iterated_threshold_collapse_reduced_to_sparse_terminal_history_pdec_or_sae_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "effective_core_lower_bound_closed": True,
        "collapse_inequality_closed": True,
        "adaptive_lambda_balance_registered": True,
        "sparse_terminal_reduction_closed": True,
        "persistent_history_pdec_route_registered": True,
        "nonpersistent_history_sae_route_registered": True,
        "threshold_collapse_excluded": False,
        "sparse_terminal_history_absorbed": False,
        "fixed_type_history_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SPARSE_HISTORY,
        "secondary_attack_target": ADAPTIVE_LAMBDA,
        "parallel_targets": [DEPTH_LCM, FIXED_HISTORY_PDEC, SPARSE_SAE],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "阈值坍缩已经从模糊缺口压成显式乘积账本。第 r 层有效核心数下界为 "
            "M_r >= rho_0 Y_0 / prod(A_i M_i)，其中 A_i<=8Lambda_i^2、"
            "M_i=max(b_i,c_i)<2Lambda_i。故坍缩等价于 prod(A_i M_i)>rho_0 Y_0。"
            "若实际反例链在最早坍缩层后仍有残留，它已不再是高密度窗口，只能是稀疏终端历史。"
            "同一历史持久复现进入固定历史 PDEC/ColumnCRT；不持久历史进入 SAE 总量账本。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 迭代阈值坍缩账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"effective_core_lower_bound_closed={fmt_bool(result['effective_core_lower_bound_closed'])}",
        f"collapse_inequality_closed={fmt_bool(result['collapse_inequality_closed'])}",
        f"adaptive_lambda_balance_registered={fmt_bool(result['adaptive_lambda_balance_registered'])}",
        f"sparse_terminal_reduction_closed={fmt_bool(result['sparse_terminal_reduction_closed'])}",
        f"persistent_history_pdec_route_registered={fmt_bool(result['persistent_history_pdec_route_registered'])}",
        f"nonpersistent_history_sae_route_registered={fmt_bool(result['nonpersistent_history_sae_route_registered'])}",
        f"threshold_collapse_excluded={fmt_bool(result['threshold_collapse_excluded'])}",
        f"sparse_terminal_history_absorbed={fmt_bool(result['sparse_terminal_history_absorbed'])}",
        f"fixed_type_history_pdec_excluded={fmt_bool(result['fixed_type_history_pdec_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 坍缩不等式",
        "",
        "第 `r` 层核心窗口的有效数量下界为",
        "",
        "```text",
        "M_r >= rho_0 Y_0 / prod_{i<=r}(A_i M_i),",
        "A_i <= 8 Lambda_i^2,",
        "M_i=max(b_i,c_i)<2 Lambda_i.",
        "```",
        "",
        "所以阈值坍缩的精确账本形式是",
        "",
        "```text",
        "prod_{i<=r}(A_i M_i) > rho_0 Y_0.",
        "```",
        "",
        "粗略充分生存条件为",
        "",
        "```text",
        "prod_{i<=r} 16 Lambda_i^3 <= rho_0 Y_0.",
        "```",
        "",
        "这个条件只是参数纪律，不作为无条件闭合证明。",
        "",
        "## 2. 稀疏终端历史",
        "",
        "在最早坍缩层之后，密度账本已不能提供高密度窗口；若假设反例链仍留下实际对象，它只能是一个有限深度、有限商型字母表中的稀疏终端历史。",
        "",
        "持久的同一历史是 `PDEC/ColumnCRT`；不持久历史是 `SAE`。",
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
            "并列参数纪律：",
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
            "审稿边界：本步闭合阈值坍缩的乘积账本与稀疏终端归约；未排斥 PDEC，也未完成 SAE 总量吸收。",
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
