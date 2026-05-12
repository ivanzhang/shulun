#!/usr/bin/env python3
"""生成 strict 统一终端预算方程路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_unified_terminal_budget_equation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unified-terminal-budget-equation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md",
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.md",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
]

B3_MAIN = "B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError"
B3_TV = "B3RemainderTotalVariationBudgetForLengthP"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
TYPE_THRESHOLD = "FormalUnitTypeThresholdLedger"
ANTICOLLAPSE = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
COLD_SUPPLY = "ColdCoreNonpersistentSupplyUpperBound"
LAMBDA_BALANCE = "AdaptiveLambdaBalanceForIteratedCoreDensity"
FINAL_GAP = "UnifiedTerminalBudgetStrictInequality"


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


def equations() -> list[dict[str, str]]:
    """列出统一预算方程的组成部分。"""
    return [
        {
            "name": "prefix_rough_lower_bound",
            "formula": "|R_{x,z}| >= (P-1)W^-(z,D)-TV(lambda^-).",
            "status": "closed_as_reduction",
            "depends_on": f"{B3_MAIN} AND {B3_TV} AND {FINITE_PREFIX}",
        },
        {
            "name": "capacity_multiplier_normalization",
            "formula": "M#_{x,z} >= |R_{x,z}|/ceil(P/z).",
            "status": "closed",
            "depends_on": "RegisteredPrefixCapacityMultiplierDiscipline",
        },
        {
            "name": "terminal_projection_balance",
            "formula": "L_forced >= M#_{x,z}-E_named.",
            "status": "closed_as_no_loss_or_named_return",
            "depends_on": f"{ANTICOLLAPSE} AND {NAMED_RETURN}",
        },
        {
            "name": "cold_core_supply_bound",
            "formula": "U_cold <= sum_W (T_PDEC(W)-1)C_core(W).",
            "status": "closed_as_upper_bound",
            "depends_on": f"{COLD_SUPPLY} AND {LAMBDA_BALANCE}",
        },
        {
            "name": "unified_terminal_budget_gap",
            "formula": "((P-1)W^- - TV)/ceil(P/z) - E_named > sum_W (T_PDEC(W)-1)C_core(W).",
            "status": "open_strict_inequality",
            "depends_on": FINAL_GAP,
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "统一方程只在假设早期零行反例链内使用，不借真实缺席样本。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "AlgebraicCompositionClosed",
            "closed": True,
            "proved": True,
            "meaning": "粗筛余、容量乘子、终端负载、冷供给四段不等式可以无损合成为一个终端预算缺口。",
            "remaining": FINAL_GAP,
        },
        {
            "gate": "B3PrefixMassInputsOpen",
            "closed": False,
            "proved": False,
            "meaning": "prefix 残洞质量仍依赖 B3 主项、TV 预算和有限边界证书。",
            "remaining": f"{B3_MAIN} AND {B3_TV} AND {FINITE_PREFIX}",
        },
        {
            "gate": "TerminalProjectionInputsOpen",
            "closed": False,
            "proved": False,
            "meaning": "终端投影仍需抗塌缩和命名回流排斥，不能把加权质量直接当作终端实例数。",
            "remaining": f"{ANTICOLLAPSE} AND {NAMED_RETURN}",
        },
        {
            "gate": "ColdSupplyParameterInputsOpen",
            "closed": False,
            "proved": False,
            "meaning": "冷供给上界的具体反超还需要 Lambda 平衡与核心阈值供给预算比较。",
            "remaining": f"{COLD_SUPPLY} AND {LAMBDA_BALANCE}",
        },
        {
            "gate": "UnifiedTerminalBudgetContradictionProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明统一严格不等式，因此没有最终直接矛盾。",
            "remaining": FINAL_GAP,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_unified_terminal_budget_equation_router",
        "status": "unified_terminal_budget_equation_built_strict_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "algebraic_composition_closed": True,
        "prefix_rough_lower_reduction_imported": True,
        "capacity_multiplier_normalization_imported": True,
        "terminal_projection_balance_imported": True,
        "cold_core_supply_bound_imported": True,
        "unified_terminal_budget_strict_inequality_proved": False,
        "b3_prefix_mass_inputs_proved": False,
        "terminal_projection_inputs_proved": False,
        "cold_supply_parameter_inputs_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": B3_TV,
        "parallel_attack_targets": [
            B3_MAIN,
            FINITE_PREFIX,
            ANTICOLLAPSE,
            NAMED_RETURN,
            COLD_SUPPLY,
            LAMBDA_BALANCE,
        ],
        "equations": equations(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "统一终端预算方程已经建立：在早期零行反例链内，prefix 粗筛余质量经容量乘子转成 M#，"
            "M# 经终端投影守恒转成 L_forced，冷核心历史给出 U_cold 上界。"
            "因此最终矛盾只需证明一个严格不等式："
            "((P-1)W^- - TV)/ceil(P/z) - E_named > sum_W (T_PDEC(W)-1)C_core(W)。"
            "该式失败时，失败源只能落入 B3/TV/有限证书、终端抗塌缩/命名回流、冷供给/Lambda 平衡三组输入。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 统一终端预算方程路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"algebraic_composition_closed={fmt_bool(result['algebraic_composition_closed'])}",
        f"prefix_rough_lower_reduction_imported={fmt_bool(result['prefix_rough_lower_reduction_imported'])}",
        f"capacity_multiplier_normalization_imported={fmt_bool(result['capacity_multiplier_normalization_imported'])}",
        f"terminal_projection_balance_imported={fmt_bool(result['terminal_projection_balance_imported'])}",
        f"cold_core_supply_bound_imported={fmt_bool(result['cold_core_supply_bound_imported'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"b3_prefix_mass_inputs_proved={fmt_bool(result['b3_prefix_mass_inputs_proved'])}",
        f"terminal_projection_inputs_proved={fmt_bool(result['terminal_projection_inputs_proved'])}",
        f"cold_supply_parameter_inputs_proved={fmt_bool(result['cold_supply_parameter_inputs_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 统一方程",
        "",
        "```text",
        "|R_{x,z}| >= (P-1)W^-(z,D)-TV(lambda^-)",
        "M#_{x,z} >= |R_{x,z}|/ceil(P/z)",
        "L_forced >= M#_{x,z}-E_named",
        "U_cold <= sum_W (T_PDEC(W)-1)C_core(W)",
        "```",
        "",
        "合成得到终局预算判据：",
        "",
        "```text",
        "((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)",
        "    - E_named",
        "  > sum_W (T_PDEC(W)-1)C_core(W)",
        "```",
        "",
        "若该不等式成立，则 `L_forced>U_cold`，非持久冷核心供给无法支付早期零行反例链。",
        "",
        "## 2. 方程表",
        "",
        "| name | formula | status | depends_on |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["equations"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    table_cell(row["formula"]),
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["depends_on"]),
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
            "## 4. 下一最窄点",
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
            "审稿边界：本步只完成统一终端预算方程的代数组合；尚未证明该严格不等式，不能升级为无条件闭合。",
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
