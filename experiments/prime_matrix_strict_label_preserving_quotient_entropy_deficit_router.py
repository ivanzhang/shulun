#!/usr/bin/env python3
"""生成 strict 保标签商类型熵亏损同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_label_preserving_quotient_entropy_deficit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json"
OUT_MD = DOCS / "prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.md"

TARGET = "BoundaryCapLabelPreservingQuotientEntropyDeficit"
UNIFIED_GAP = "UnifiedTerminalBudgetStrictInequality"
B3_TV = "B3RemainderTotalVariationBudgetForLengthP"
B3_SURPLUS = "B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
ANTI_COLLAPSE = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
COLD_SUPPLY = "ColdCoreNonpersistentSupplyUpperBound"
LAMBDA_BALANCE = "AdaptiveLambdaBalanceForIteratedCoreDensity"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-boundary-cap-type-compression-router.json",
    "prime-matrix-strict-forced-obligation-lower-bound-router.json",
    "prime-matrix-strict-boundary-residual-mass-lower-bound-router.json",
    "prime-matrix-strict-prefix-residual-transfer-router.json",
    "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json",
    "prime-matrix-strict-unified-terminal-budget-equation-router.json",
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
    """生成保标签商类型熵亏损判定表。"""
    boundary = data["boundary"]
    forced = data["forced"]
    residual = data["residual"]
    transfer = data["transfer"]
    capacity = data["capacity"]
    unified = data["unified"]

    return [
        row(
            "LabelPreservingQuotientEntropyDeficitTargetActive",
            boundary.get("next_direct_attack_target") == TARGET,
            False,
            "上一层把类型压缩的新增最窄输入钉为保标签商类型熵亏损。",
            TARGET,
        ),
        row(
            "ForcedWeightedInjectionImported",
            forced.get("clb_residual_to_weighted_obligation_injection_closed") is True
            and forced.get("no_loss_weighted_accounting_imported") is True,
            True,
            "早期零行残洞到加权 obligation 的注入和 no-loss 账本已闭合。",
            "仍需有效不同实例下界。",
        ),
        row(
            "NaturalResidualMassNonfreeImported",
            residual.get("natural_cutoff_mass_not_free_diagnosed") is True,
            True,
            "自然 cutoff 残洞质量会撞上短区间素数/平方根窗口屏障，不能当作免费输入。",
            "转用 adaptive prefix 残洞势。",
        ),
        row(
            "PrefixWeightedTransferImported",
            transfer.get("prefix_residual_to_weighted_formal_unit_obligation_transfer_proved") is True,
            True,
            "prefix 残洞可用最小覆盖标签 tau_z(c) 注入同一 formal-unit 加权义务域。",
            "加权转移闭合，但有效类型实例仍未自动闭合。",
        ),
        row(
            "CapacityMultiplierDisciplineImported",
            capacity.get("registered_prefix_capacity_multiplier_discipline_proved") is True
            and capacity.get("distinct_label_lower_bound_closed") is True,
            True,
            "容量乘子纪律已闭合：M# 下界不同标签数，标签复用不能免费制造实例。",
            "仍需 M# 势下界和标签到类型抗塌缩。",
        ),
        row(
            "UnifiedTerminalBudgetEquationImported",
            unified.get("algebraic_composition_closed") is True,
            True,
            "prefix 粗筛余、容量乘子、终端投影守恒和冷核心供给上界已合成为统一预算方程。",
            UNIFIED_GAP,
        ),
        row(
            "LabelQuotientDeficitReducedToBudgetGap",
            unified.get("algebraic_composition_closed") is True
            and capacity.get("registered_prefix_capacity_multiplier_discipline_proved") is True,
            False,
            "保标签商类型熵亏损的非循环版本等价于证明统一终端预算严格缺口，并排除命名回流吞噬。",
            UNIFIED_GAP,
        ),
        row(
            "B3PrefixMassInputsCurrentCorpusProved",
            unified.get("b3_prefix_mass_inputs_proved") is True,
            False,
            "prefix 残洞势仍依赖 B3 主项、TV 预算和有限边界证书。",
            f"{B3_SURPLUS} AND {B3_TV} AND {FINITE_PREFIX}",
        ),
        row(
            "TerminalProjectionInputsCurrentCorpusProved",
            unified.get("terminal_projection_inputs_proved") is True,
            False,
            "终端投影仍需标签支撑抗塌缩和命名回流热核心排斥。",
            f"{ANTI_COLLAPSE} AND {NAMED_RETURN}",
        ),
        row(
            "ColdSupplyInputsCurrentCorpusProved",
            unified.get("cold_supply_parameter_inputs_proved") is True,
            False,
            "冷供给上界仍需非持久供给上界与自适应 Lambda 平衡。",
            f"{COLD_SUPPLY} AND {LAMBDA_BALANCE}",
        ),
        row(
            "UnifiedTerminalBudgetStrictInequalityCurrentCorpusProved",
            unified.get("unified_terminal_budget_strict_inequality_proved") is True,
            False,
            "尚未证明统一严格不等式，因此保标签商类型熵亏损不能升级为终端矛盾。",
            UNIFIED_GAP,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未得到早期零行反例链与真实结构链之间的终端直接矛盾。",
            f"{UNIFIED_GAP} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造保标签商类型熵亏损同步证书。"""
    data = {
        "boundary": load_json("prime-matrix-strict-boundary-cap-type-compression-router.json"),
        "forced": load_json("prime-matrix-strict-forced-obligation-lower-bound-router.json"),
        "residual": load_json("prime-matrix-strict-boundary-residual-mass-lower-bound-router.json"),
        "transfer": load_json("prime-matrix-strict-prefix-residual-transfer-router.json"),
        "capacity": load_json("prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json"),
        "unified": load_json("prime-matrix-strict-unified-terminal-budget-equation-router.json"),
    }
    rows = build_rows(data)
    terminal_inputs = [
        B3_SURPLUS,
        B3_TV,
        FINITE_PREFIX,
        ANTI_COLLAPSE,
        NAMED_RETURN,
        COLD_SUPPLY,
        LAMBDA_BALANCE,
    ]
    return {
        "certificate_type": "prime_matrix_strict_label_preserving_quotient_entropy_deficit_router",
        "status": "label_preserving_quotient_entropy_deficit_reduced_to_unified_terminal_budget_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": TARGET,
        "hardpoint_after_router": UNIFIED_GAP,
        "forced_weighted_injection_imported": any(
            item["gate"] == "ForcedWeightedInjectionImported" and item["closed"] for item in rows
        ),
        "prefix_weighted_transfer_imported": any(
            item["gate"] == "PrefixWeightedTransferImported" and item["closed"] for item in rows
        ),
        "capacity_multiplier_discipline_imported": any(
            item["gate"] == "CapacityMultiplierDisciplineImported" and item["closed"] for item in rows
        ),
        "unified_terminal_budget_equation_imported": any(
            item["gate"] == "UnifiedTerminalBudgetEquationImported" and item["closed"] for item in rows
        ),
        "label_quotient_deficit_current_corpus_proved": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": B3_TV,
        "parallel_required_inputs": [
            B3_SURPLUS,
            FINITE_PREFIX,
            ANTI_COLLAPSE,
            NAMED_RETURN,
            COLD_SUPPLY,
            LAMBDA_BALANCE,
            DSTRUCTURE,
        ],
        "budget_gap_formula": (
            "((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z) - E_named "
            "> sum_W (T_PDEC(W)-1)C_core(W)"
        ),
        "terminal_inputs": terminal_inputs,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"`{TARGET}` 已与 prefix 加权转移、容量乘子纪律和统一终端预算方程对齐。"
            "现有材料已经闭合 residual->weighted obligation、prefix atom 注入、容量乘子归一化和预算方程的代数组合；"
            "但保标签商类型熵亏损本身尚未证明，因为还缺统一严格不等式及其 B3/TV、终端抗塌缩、命名回流和冷供给输入。"
            f"当前最窄可攻点同步为 `{B3_TV}`。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 保标签商类型熵亏损同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"forced_weighted_injection_imported={fmt_bool(result['forced_weighted_injection_imported'])}",
        f"prefix_weighted_transfer_imported={fmt_bool(result['prefix_weighted_transfer_imported'])}",
        f"capacity_multiplier_discipline_imported={fmt_bool(result['capacity_multiplier_discipline_imported'])}",
        f"unified_terminal_budget_equation_imported={fmt_bool(result['unified_terminal_budget_equation_imported'])}",
        f"label_quotient_deficit_current_corpus_proved={fmt_bool(result['label_quotient_deficit_current_corpus_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["hardpoint_before_router"],
        "  => prefix weighted transfer + capacity normalization + terminal projection",
        f"  => {result['hardpoint_after_router']}",
        "```",
        "",
        "统一预算缺口：",
        "",
        "```text",
        result["budget_gap_formula"],
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
