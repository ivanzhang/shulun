#!/usr/bin/env python3
"""生成 strict alpha 公式 signed lift 字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_formula_signed_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-formula-signed-lift-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-clean-core-disintegration-automaticity-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
    "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


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


def build_rows(
    formula: dict[str, Any],
    disintegration: dict[str, Any],
    geometric_budget: dict[str, Any],
    phi_reduction: dict[str, Any],
    seed_nogo: dict[str, Any],
    source_law: dict[str, Any],
    reverse_functor: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 alpha signed lift 判定表。"""
    target = "AlphaFormulaSignedCoefficientLiftLedger"
    next_basis = (
        "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND "
        "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND "
        "AlphaRowsPhiPushforwardCompatibilityLedger AND "
        "AlphaSignedLiftVariationBranchBudgetLedger AND "
        "AlphaSignedLiftFailureNamedReturnLedger"
    )
    terminal_after = formula.get("terminal_gap_after_router", "")
    disintegration_formal = disintegration.get("signed_fiber_disintegration_formal") is True
    pushforward_gate = disintegration.get("pushforward_identity_is_real_gate") is True
    geometric_shape_only = geometric_budget.get("geometry_ledger_alphabet_closed") is True
    signed_variation_open = geometric_budget.get("signed_variation_branch_lift_proved") is False
    phi_reduced_to_emitter = (
        phi_reduction.get("terminal_gap_after_router") == "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn"
        or phi_reduction.get("registered_primitive_prepushforward_fiber_emitter_proved") is False
    )
    seed_blocked = seed_nogo.get("zero_row_seed_extraction_blocked") is True
    source_fields = source_law.get("origin_generation_ledger_implication_closed") is True
    reverse_blocked = reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True
    return [
        {
            "gate": "AlphaFormulaSignedLiftTargetActive",
            "closed": target in terminal_after or formula.get("next_direct_attack_target") == target,
            "proved": False,
            "meaning": "上一层已把当前最窄点固定为 unsigned row 形状到 signed alpha 系数行的提升。",
            "remaining": target,
        },
        {
            "gate": "DisintegrationFormalButNeedsSourceImported",
            "closed": disintegration_formal and pushforward_gate,
            "proved": True,
            "meaning": "给定 signed source 后逐纤维解积分形式闭合；真正硬点是 actual source 与 Phi 推前恒等式。",
            "remaining": "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaRowsPhiPushforwardCompatibilityLedger。",
        },
        {
            "gate": "GeometricLedgerUnsignedOnlyImported",
            "closed": geometric_shape_only and signed_variation_open,
            "proved": True,
            "meaning": "斜线、P列锚、carry-shell 和 layered-wheel 给出支撑/相位字母表，但不控制 signed 变差。",
            "remaining": "AlphaSignedLiftVariationBranchBudgetLedger。",
        },
        {
            "gate": "PhiBudgetReductionToEmitterImported",
            "closed": phi_reduced_to_emitter,
            "proved": True,
            "meaning": "actual signed/Phi 兼容预算已被压成 pre-pushforward primitive emitter；但 emitter 尚未证明。",
            "remaining": "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger。",
        },
        {
            "gate": "UnsignedZeroRowCannotSupplySignedSeedImported",
            "closed": seed_blocked,
            "proved": True,
            "meaning": "早期零行假设只给 unsigned covering data，不能作为 signed alpha source seed。",
            "remaining": "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger。",
        },
        {
            "gate": "PreCauchyFieldContractImported",
            "closed": source_fields and reverse_blocked,
            "proved": True,
            "meaning": "pre-Cauchy 来源律和反向来源 no-go 已固定：必须正向给出 signed 行、权重、branch key 和回流。",
            "remaining": next_basis,
        },
        {
            "gate": "ActualSignedAlphaSourceMeasureCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未定义同一 formal unit 内 actual noncanonical carry-shell alpha rows 上的 signed 源测度。",
            "remaining": "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger。",
        },
        {
            "gate": "AlphaSignedWeightLawCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出 signed alpha 权重来自独立 pre-Cauchy 算术恒等式的公式。",
            "remaining": "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger。",
        },
        {
            "gate": "AlphaRowsPhiPushforwardCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 alpha rows 沿 Phi 推前后等于目标 payment-side alpha 系数。",
            "remaining": "AlphaRowsPhiPushforwardCompatibilityLedger。",
        },
        {
            "gate": "AlphaSignedLiftVariationBranchBudgetCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 signed lift 的总变差、绝对支撑和 branch key 复杂度由几何账本支配。",
            "remaining": "AlphaSignedLiftVariationBranchBudgetLedger。",
        },
        {
            "gate": "AlphaSignedLiftFailureReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出 signed 源缺失、Phi 不兼容、变差超预算或 branch 爆炸的命名回流。",
            "remaining": "AlphaSignedLiftFailureNamedReturnLedger。",
        },
        {
            "gate": "AlphaFormulaSignedCoefficientLiftCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "signed 源测度、权重律、Phi 推前、变差预算和失败回流五项尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 alpha signed lift 证书。"""
    formula = load_json(DOCS / "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json")
    disintegration = load_json(DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.json")
    geometric_budget = load_json(DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json")
    phi_reduction = load_json(DOCS / "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json")
    seed_nogo = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    source_law = load_json(DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json")
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")

    target = "AlphaFormulaSignedCoefficientLiftLedger"
    next_basis = (
        "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND "
        "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND "
        "AlphaRowsPhiPushforwardCompatibilityLedger AND "
        "AlphaSignedLiftVariationBranchBudgetLedger AND "
        "AlphaSignedLiftFailureNamedReturnLedger"
    )
    rows = build_rows(
        formula=formula,
        disintegration=disintegration,
        geometric_budget=geometric_budget,
        phi_reduction=phi_reduction,
        seed_nogo=seed_nogo,
        source_law=source_law,
        reverse_functor=reverse_functor,
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_formula_signed_lift_router",
        "status": "strict_alpha_formula_signed_lift_reduced_to_source_weight_phi_budget_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "alpha_formula_signed_lift_router_closed": True,
        "disintegration_formal_not_source_imported": True,
        "geometric_ledger_unsigned_only_imported": True,
        "phi_budget_reduction_to_emitter_imported": True,
        "zero_row_signed_seed_extraction_blocked_imported": True,
        "actual_signed_alpha_source_measure_for_carry_shell_rows_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "alpha_rows_phi_pushforward_compatibility_proved": False,
        "alpha_signed_lift_variation_branch_budget_proved": False,
        "alpha_signed_lift_failure_named_return_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "deterministic_alpha_primitive_row_emission_map_proved": False,
        "actual_noncanonical_alpha_side_primitive_rule_proved": False,
        "actual_noncanonical_delta_side_primitive_rule_proved": False,
        "alpha_delta_pairing_compatibility_before_cauchy_proved": False,
        "primitive_rule_nonzero_sign_local_factor_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger",
        "signed_lift_law": (
            "The signed lift cannot be obtained by naming carry-shell hits. It must define an actual signed alpha source "
            "measure before Cauchy/dispersion, give an arithmetic weight law, prove Phi pushforward compatibility, control "
            "absolute variation and branch keys, and return every failed lift by name."
        ),
        "plain_conclusion": (
            "`AlphaFormulaSignedCoefficientLiftLedger` 被压成 actual signed alpha 源测度、pre-Cauchy 算术权重律、"
            "Phi 推前兼容、signed 变差/branch 预算和失败命名回流五项。上游早期零行刚性能显著缩小候选 row 形状，"
            "但仍不能把 unsigned 覆盖数据变成 signed alpha 系数；当前最窄点为 "
            "`AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger`。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha 公式 signed lift 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"alpha_formula_signed_lift_router_closed={fmt_bool(result['alpha_formula_signed_lift_router_closed'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"actual_noncanonical_alpha_side_primitive_rule_proved={fmt_bool(result['actual_noncanonical_alpha_side_primitive_rule_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed lift 律",
        "",
        result["signed_lift_law"],
        "",
        "## 2. signed lift 内部拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
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
