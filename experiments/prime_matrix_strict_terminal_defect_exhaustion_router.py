#!/usr/bin/env python3
"""生成 strict 终端缺陷耗尽路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_defect_exhaustion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-defect-exhaustion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-terminal-defect-exhaustion-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-terminal-defect-exhaustion-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-terminal-contradiction-hard-attack-router.md",
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.md",
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-signed-endpoint-defect-split-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-dyadic-endpoint-pdec-hdl-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-deficit-fourier-pdec-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-fourier-upper-router.md",
    MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.md",
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
    MONOGRAPH / "prime-matrix-strict-low-multiplier-common-kernel-router.md",
    MONOGRAPH / "prime-matrix-strict-fixed-quotient-type-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.md",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md",
    MONOGRAPH / "claim-status-table.md",
]

ALPHA_DEFECT = "AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_GAP = "UnifiedTerminalBudgetStrictInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def exhaustion_chain() -> list[dict[str, str]]:
    """列出容量失败缺陷的耗尽链。"""
    return [
        {
            "layer": "capacity failure",
            "input": "No alpha-capacity surplus under EarlyZeroRowWithinP",
            "forced": "TV_alpha >= (P-1)W^-_alpha-2(pi(P)-pi(alpha P))",
            "exit": "signed endpoint defect",
            "status": "closed",
        },
        {
            "layer": "signed endpoint",
            "input": "E_alpha<=-G_alpha",
            "forced": "low / dyadic / far-tail split; middle mass gives dyadic PDEC certificate",
            "exit": "LowMod OR DyadicEndpointPDEC OR FarTailCore/SAE",
            "status": "closed_as_split",
        },
        {
            "layer": "dyadic endpoint",
            "input": "positive endpoint hit deficit or negative hit surplus",
            "forced": "centered zero-mean CRT test function and nonzero Fourier energy",
            "exit": "Fourier/PDEC or isolated SAE",
            "status": "closed_as_inputization",
        },
        {
            "layer": "Fourier upper",
            "input": "large nonzero endpoint spectrum",
            "forced": "low effective modulus, large-effective geometric decay, or Bohr-cap large spectrum",
            "exit": "LowEffectiveMod PDEC/ColumnCRT OR decay budget OR Bohr-cap PDEC",
            "status": "closed_as_three_way_route",
        },
        {
            "layer": "low effective modulus",
            "input": "many active d with small d/gcd(h,d)",
            "forced": "weighted reciprocal common-divisor envelope and hot short divisor window",
            "exit": "short-window divisor density",
            "status": "closed_as_reduction",
        },
        {
            "layer": "short divisor window",
            "input": "many g in (Y,2Y] divide the same frequency h",
            "forced": "LCM explosion or low-multiplier common-kernel recurrence",
            "exit": "ColumnCRT/PDEC/SAE or dense LCM pressure",
            "status": "closed_as_dichotomy",
        },
        {
            "layer": "threshold collapse",
            "input": "kernel recursion loses dense-window mass",
            "forced": "finite sparse terminal history word",
            "exit": "fixed-history PDEC or nonpersistent SAE budget",
            "status": "closed_as_sparse_terminal",
        },
        {
            "layer": "cold-core supply",
            "input": "nonpersistent sparse terminal histories",
            "forced": "U_cold <= sum_W (T_PDEC(W)-1)C_core(W)",
            "exit": "unified terminal budget gap",
            "status": "closed_as_budget_upper",
        },
    ]


def theorem_rows() -> list[dict[str, Any]]:
    """给出本轮可审查的定理边界。"""
    return [
        {
            "name": "TerminalDefectNoFreeExitTheorem",
            "proved": True,
            "statement": (
                "在假设早期零行且容量反超没有发生时，强 TV/端点缺陷不能作为第四类自由逃逸；"
                "它必沿低模、dyadic Fourier、共同核、固定历史、SAE 或冷核心预算之一登记。"
            ),
            "role": "把反例链与真实结构链的终端交点从抽象缺陷压成命名出口集合。",
        },
        {
            "name": "ConditionalTerminalContradictionAfterExhaustion",
            "proved": True,
            "statement": (
                f"若 {NAMED_RETURN} 被排斥，且 {UNIFIED_GAP} 成立，"
                "则容量失败分支也无法支付早期零行义务，故早期零行反例不存在。"
            ),
            "role": "这是本轮新增的条件闭合口，直接接到统一终端预算方程。",
        },
        {
            "name": "UnconditionalTerminalDefectExclusion",
            "proved": False,
            "statement": (
                f"要把 {ALPHA_DEFECT} 升级为无条件排斥，仍必须证明命名回流排斥和统一预算严格不等式，"
                f"或取得 {DSTRUCTURE} 独立晋级。"
            ),
            "role": "这是仍未闭合的作者侧全局命题边界。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "只在假设早期零行反例链内追踪容量失败后的缺陷，不使用真实零行缺席。",
            "remaining": "无。",
        },
        {
            "gate": "TerminalDefectNoFreeExitClosed",
            "closed": True,
            "proved": True,
            "meaning": "强 TV/端点缺陷已被耗尽到低模、dyadic、共同核、固定历史、SAE、冷核心预算等命名出口。",
            "remaining": f"{NAMED_RETURN} OR {UNIFIED_GAP}",
        },
        {
            "gate": "NamedReturnAlphabetClosed",
            "closed": True,
            "proved": False,
            "meaning": "所有逃逸口都已命名，不存在未登记第四出口；但命名出口本身尚未全部排斥。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "UnifiedBudgetConditionalContradictionClosed",
            "closed": True,
            "proved": True,
            "meaning": "若命名回流消失且统一预算严格反超，则得到 L_forced>U_cold 的终端供需矛盾。",
            "remaining": UNIFIED_GAP,
        },
        {
            "gate": "AlphaPrefixTVOrPDECDefectExcluded",
            "closed": False,
            "proved": False,
            "meaning": "缺陷已耗尽为命名出口，但尚未证明所有命名出口或预算失败不可能发生。",
            "remaining": f"{NAMED_RETURN} AND {UNIFIED_GAP}",
        },
        {
            "gate": "DirectUnconditionalContradictionFound",
            "closed": False,
            "proved": False,
            "meaning": "当前仍没有单点无条件终端矛盾；全局行/列命题不能升级。",
            "remaining": f"({NAMED_RETURN} AND {UNIFIED_GAP}) OR {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造终端缺陷耗尽证书。"""
    return {
        "certificate_type": "prime_matrix_strict_terminal_defect_exhaustion_router",
        "status": "terminal_defect_no_free_exit_closed_unconditional_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "terminal_defect_no_free_exit_closed": True,
        "alpha_prefix_tv_endpoint_defect_exhausted_to_named_exits": True,
        "conditional_terminal_contradiction_after_exhaustion_closed": True,
        "named_return_exclusion_proved": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "alpha_prefix_tv_or_pdec_defect_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NAMED_RETURN,
        "parallel_attack_target": UNIFIED_GAP,
        "referee_gate": DSTRUCTURE,
        "exhaustion_chain": exhaustion_chain(),
        "theorem_rows": theorem_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本次硬攻关闭的是“缺陷是否还有自由逃逸”这一层：容量失败后的强 TV/端点缺陷，"
            "沿现有真实结构链必进入低模、dyadic Fourier、共同核、固定历史、SAE 或冷核心预算，"
            "不存在未命名第四出口。"
            "但这不是无条件排斥缺陷；真正剩余压成命名回流排斥与统一终端预算严格不等式。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 终端缺陷耗尽路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_defect_no_free_exit_closed={fmt_bool(result['terminal_defect_no_free_exit_closed'])}",
        f"alpha_prefix_tv_endpoint_defect_exhausted_to_named_exits={fmt_bool(result['alpha_prefix_tv_endpoint_defect_exhausted_to_named_exits'])}",
        f"conditional_terminal_contradiction_after_exhaustion_closed={fmt_bool(result['conditional_terminal_contradiction_after_exhaustion_closed'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"alpha_prefix_tv_or_pdec_defect_excluded={fmt_bool(result['alpha_prefix_tv_or_pdec_defect_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 缺陷耗尽链",
        "",
        "| layer | input | forced | exit | status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["exhaustion_chain"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['layer'])}`",
                    table_cell(row["input"]),
                    table_cell(row["forced"]),
                    table_cell(row["exit"]),
                    f"`{table_cell(row['status'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 定理边界",
            "",
            "| name | proved | statement | role |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["statement"]),
                    table_cell(row["role"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
            "独立晋级门：",
            "",
            "```text",
            result["referee_gate"],
            "```",
            "",
            "审稿边界：本文件证明的是终端缺陷没有自由逃逸，并给出条件矛盾口；"
            "它没有证明命名回流排斥，也没有证明统一预算严格不等式，因此不能声明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"status={result['status']}")


if __name__ == "__main__":
    main()
