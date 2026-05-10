#!/usr/bin/env python3
"""生成 strict 单参数终端预算正余量主攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_single_parameter_terminal_budget_margin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-single-parameter-terminal-budget-margin-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-single-parameter-terminal-budget-margin-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    MONOGRAPH / "prime-matrix-strict-unified-budget-inequality-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json",
    MONOGRAPH / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json",
    MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json",
]

MARGIN = "SingleParameterTerminalBudgetMarginLedger"
POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
PREFIX = "NormalizedPrefixResidualPotentialLowerBound"
DISCRETE_B3 = "B3DiscretePrimeSumUniformErrorPGe100000"
TV_SELF = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
PDEC_CLEAN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


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


def margin_formula_rows() -> list[dict[str, str]]:
    """列出同参数正余量公式的四个输入。"""
    return [
        {
            "slot": "prefix demand",
            "formula": "D_prefix=((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)",
            "needed": "explicit lower bound D_prefix >= D0(P,z)>0",
            "status": "open: rough count/finite boundary not fully proved",
        },
        {
            "slot": "terminal projection",
            "formula": "L_forced>=D_prefix-E_named",
            "needed": "no silent collapse and bounded named returns",
            "status": "no-silent-collapse closed; named exclusion open",
        },
        {
            "slot": "cold supply",
            "formula": "U_cold<=sum_W (T_PDEC(W)-1)C_core(W)",
            "needed": "explicit same-parameter upper bound U_cold<=U0(P,z)",
            "status": "envelope and lambda discipline closed; numeric dominance open",
        },
        {
            "slot": "strict margin",
            "formula": "D0(P,z)-E0(P,z)-U0(P,z)>0",
            "needed": "one signed inequality under one parameter ledger",
            "status": "not proved in current corpus",
        },
    ]


def obstruction_rows(
    uniform_prefix: dict[str, Any],
    b3_tv: dict[str, Any],
    beta: dict[str, Any],
    named: dict[str, Any],
) -> list[dict[str, Any]]:
    """列出当前阻塞点。"""
    return [
        {
            "obstruction": DISCRETE_B3,
            "closed": beta.get("discrete_prime_sum_uniform_error_proved") is True,
            "why_it_matters": "连续 beta 主项有 1% 余量，但离散素和误差未内联证明。",
            "effect_on_margin": "D_prefix 不能升级为严格自足显式 D0。",
        },
        {
            "obstruction": "B3RemainderTotalVariationBudgetForLengthP",
            "closed": b3_tv.get("b3_remainder_total_variation_budget_proved") is True,
            "why_it_matters": "外部 Mertens/Dusart 可条件关闭 TV；严格自足尾段仍开放。",
            "effect_on_margin": "TV(lambda^-) 的自足扣除项未定。",
        },
        {
            "obstruction": FINITE_PREFIX,
            "closed": uniform_prefix.get("finite_boundary_prefix_rough_count_certificate_proved") is True,
            "why_it_matters": "显式常数路线留下有限 P 段；没有证书就不能宣称全局。",
            "effect_on_margin": "D0(P,z)>0 不能覆盖所有 P。",
        },
        {
            "obstruction": NAMED_RETURN,
            "closed": named.get("named_return_exclusion_proved") is True,
            "why_it_matters": "E_named 目前被压缩但未排斥；它可吞掉正余量。",
            "effect_on_margin": "无法证明 D_prefix-E_named 仍为正。",
        },
        {
            "obstruction": "ColdPositiveDominance",
            "closed": False,
            "why_it_matters": "冷供给有上界公式，但还没有同参数数值反超 D_prefix-E_named。",
            "effect_on_margin": "无法证明 D_prefix-E_named-U_cold>0。",
        },
    ]


def theorem_rows() -> list[dict[str, Any]]:
    """给出本轮定理边界。"""
    return [
        {
            "name": "SingleParameterMarginNormalForm",
            "proved": True,
            "statement": "早期零行反例链的终端矛盾等价于同参数正余量 D_prefix-E_named-U_cold>0。",
            "role": "这是必要且充分的终端供需闭合口。",
        },
        {
            "name": "NoConditionalInputPromotion",
            "proved": True,
            "statement": "外部 B3/TV 条件、命名回流压缩、冷供给纪律不能自动合成为无条件正余量。",
            "role": "防止把条件接口误认为最终证明。",
        },
        {
            "name": "TerminalContradictionCurrentCorpus",
            "proved": False,
            "statement": "当前语料尚未证明 D_prefix-E_named-U_cold>0。",
            "role": "行/列命题仍未作者侧无条件闭合。",
        },
    ]


def decision_rows(
    cold: dict[str, Any],
    anticollapse: dict[str, Any],
    unified: dict[str, Any],
    uniform_prefix: dict[str, Any],
    b3_tv: dict[str, Any],
    beta: dict[str, Any],
    named: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    external_b3_lane = unified.get("external_b3_prefix_demand_lane_available") is True
    terminal_anticollapse = anticollapse.get("terminal_projection_anticollapse_closed") is True
    cold_discipline = cold.get("single_parameter_margin_ledger_closed") is True
    continuous_beta = beta.get("continuous_beta_sieve_surplus_proved") is True
    strict_prefix = uniform_prefix.get("uniform_prefix_rough_count_lower_bound_proved") is True
    named_excluded = named.get("named_return_exclusion_proved") is True
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍只在 Assume EarlyZeroRowWithinP 的反例链内比较终端需求与供给。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "MarginNormalFormClosed",
            "closed": True,
            "proved": True,
            "meaning": "终局矛盾已固定为 D_prefix-E_named-U_cold>0。",
            "remaining": POSITIVE_MARGIN,
        },
        {
            "gate": "ContinuousBetaDemandClosed",
            "closed": continuous_beta,
            "proved": continuous_beta,
            "meaning": "alpha=0.43 的连续线性下界筛主项余量已闭合。",
            "remaining": DISCRETE_B3,
        },
        {
            "gate": "ExternalB3TVLaneAvailable",
            "closed": external_b3_lane,
            "proved": False,
            "meaning": "接受外部 Mertens/Dusart 时，B3/TV 需求链有条件可用；严格自足仍缺尾段。",
            "remaining": TV_SELF,
        },
        {
            "gate": "StrictPrefixDemandProved",
            "closed": strict_prefix,
            "proved": strict_prefix,
            "meaning": "当前尚未完成统一 prefix 粗筛余下界和有限边界证书。",
            "remaining": f"{PREFIX} AND {FINITE_PREFIX}",
        },
        {
            "gate": "TerminalNoSilentCollapseClosed",
            "closed": terminal_anticollapse,
            "proved": terminal_anticollapse,
            "meaning": "prefix 标签到稀疏终端历史的重数守恒已闭合。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "NamedReturnExcluded",
            "closed": named_excluded,
            "proved": named_excluded,
            "meaning": "命名回流已压缩成持久全局终端包与非持久预算，但未全部排斥。",
            "remaining": f"{PDEC_CLEAN} AND {POSITIVE_MARGIN}",
        },
        {
            "gate": "ColdSupplySameParameterDisciplineClosed",
            "closed": cold_discipline,
            "proved": cold_discipline,
            "meaning": "冷供给和 Lambda 调参纪律已锁入同一余量账本。",
            "remaining": "ColdPositiveDominance",
        },
        {
            "gate": "ExplicitPositiveMarginProved",
            "closed": False,
            "proved": False,
            "meaning": "没有同参数数值不等式证明 D_prefix-E_named-U_cold>0。",
            "remaining": (
                f"{DISCRETE_B3} AND {FINITE_PREFIX} AND {NAMED_RETURN} "
                f"AND {HOT_CORE} AND {FIXED_HISTORY}"
            ),
        },
        {
            "gate": "RowColumnUnconditionalClosed",
            "closed": False,
            "proved": False,
            "meaning": "终端正余量和 DStructure/Rankin 晋级门尚未同时完成。",
            "remaining": f"{POSITIVE_MARGIN} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造单参数终端预算正余量证书。"""
    cold = load_json(MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json")
    anticollapse = load_json(MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    unified = load_json(MONOGRAPH / "prime-matrix-strict-unified-budget-inequality-attack-router.json")
    uniform_prefix = load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json")
    b3_tv = load_json(MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json")
    beta = load_json(MONOGRAPH / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json")
    named = load_json(MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json")
    return {
        "certificate_type": "prime_matrix_strict_single_parameter_terminal_budget_margin_router",
        "status": "single_parameter_margin_normal_form_closed_positive_margin_not_proved",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "single_parameter_margin_normal_form_closed": True,
        "continuous_beta_demand_closed": beta.get("continuous_beta_sieve_surplus_proved") is True,
        "external_b3_tv_lane_available": unified.get("external_b3_prefix_demand_lane_available") is True,
        "strict_prefix_demand_proved": uniform_prefix.get("uniform_prefix_rough_count_lower_bound_proved") is True,
        "terminal_no_silent_collapse_closed": anticollapse.get("terminal_projection_anticollapse_closed") is True,
        "cold_supply_same_parameter_discipline_closed": cold.get("single_parameter_margin_ledger_closed") is True,
        "named_return_exclusion_proved": named.get("named_return_exclusion_proved") is True,
        "explicit_positive_terminal_budget_margin_proved": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MARGIN,
        "hardpoint_after_router": (
            f"{POSITIVE_MARGIN} AND {DISCRETE_B3} AND {FINITE_PREFIX} "
            f"AND {NAMED_RETURN} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": POSITIVE_MARGIN,
        "parallel_attack_targets": [DISCRETE_B3, FINITE_PREFIX, NAMED_RETURN, HOT_CORE, FIXED_HISTORY, TV_SELF, DSTRUCTURE],
        "margin_formula_rows": margin_formula_rows(),
        "obstruction_rows": obstruction_rows(uniform_prefix, b3_tv, beta, named),
        "theorem_rows": theorem_rows(),
        "decision_rows": decision_rows(cold, anticollapse, unified, uniform_prefix, b3_tv, beta, named),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "单参数终端预算正余量已被严格固定为 D_prefix-E_named-U_cold>0。"
            "现有材料关闭了标准形、终端无静默塌缩和冷供给调参纪律；连续 beta 主项已闭合，"
            "B3/TV 有外部条件路线。但当前没有证明同参数显式正余量：离散 B3 误差、"
            "有限 prefix 证书、命名回流排斥、热核心/固定历史出口与 DStructure/Rankin 晋级仍未全部完成。"
            "因此还不能声明反例链与真实链产生无条件终端矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 单参数终端预算正余量路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"single_parameter_margin_normal_form_closed={fmt_bool(result['single_parameter_margin_normal_form_closed'])}",
        f"continuous_beta_demand_closed={fmt_bool(result['continuous_beta_demand_closed'])}",
        f"external_b3_tv_lane_available={fmt_bool(result['external_b3_tv_lane_available'])}",
        f"strict_prefix_demand_proved={fmt_bool(result['strict_prefix_demand_proved'])}",
        f"terminal_no_silent_collapse_closed={fmt_bool(result['terminal_no_silent_collapse_closed'])}",
        f"cold_supply_same_parameter_discipline_closed={fmt_bool(result['cold_supply_same_parameter_discipline_closed'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"explicit_positive_terminal_budget_margin_proved={fmt_bool(result['explicit_positive_terminal_budget_margin_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端余量",
        "",
        "唯一可闭合口是同参数不等式：",
        "",
        "```text",
        "D_prefix - E_named - U_cold > 0.",
        "```",
        "",
        "其中所有项必须使用同一个 `z,D,Lambda,T_PDEC` 账本。",
        "",
        "## 2. 公式槽位",
        "",
        "| slot | formula | needed | status |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["margin_formula_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['slot'])}`",
                    table_cell(row["formula"]),
                    table_cell(row["needed"]),
                    table_cell(row["status"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 阻塞点",
            "",
            "| obstruction | closed | why_it_matters | effect_on_margin |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["obstruction_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['obstruction'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    table_cell(row["why_it_matters"]),
                    table_cell(row["effect_on_margin"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 定理边界",
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
            "## 5. 判定表",
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
            "## 6. 下一真正最窄点",
            "",
            "首攻：",
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
            "审稿边界：本文件关闭单参数终端余量标准形，但不证明正余量。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"status={result['status']}")


if __name__ == "__main__":
    main()
