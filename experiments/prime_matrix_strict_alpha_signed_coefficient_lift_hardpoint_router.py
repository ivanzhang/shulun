#!/usr/bin/env python3
"""生成 strict alpha signed coefficient lift 终端硬点证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_signed_coefficient_lift_hardpoint_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.md"

TARGET = "AlphaFormulaSignedCoefficientLiftLedger"
NEXT_TARGET = "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton"
OVERLOAD_RETURN = "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-clean-core-geometric-phi-budget-bridge-router.json",
    "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
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


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def value_table_fields() -> list[dict[str, str]]:
    """列出 signed 系数值表必须携带的字段。"""
    return [
        {
            "field": "skeleton_row_id",
            "meaning": "来自已闭合 unsigned carry-shell/P列/phase skeleton 的规范 row 编号。",
        },
        {
            "field": "source_tuple_hash",
            "meaning": "绑定同一 formal unit 的 A、D0/K/Omega、phase_rule 和 anchor payload。",
        },
        {
            "field": "signed_alpha_weight",
            "meaning": "pre-Cauchy 阶段正向给出的 signed alpha 系数值。",
        },
        {
            "field": "arithmetic_identity_ref",
            "meaning": "该系数值来自哪个独立算术恒等式，而不是来自零行覆盖或 payment 反推。",
        },
        {
            "field": "phi_payment_atom",
            "meaning": "该 row 推前到的 payment/Phi atom，含重数和符号。",
        },
        {
            "field": "absolute_variation_charge",
            "meaning": "该 row 在 signed 总变差/branch 预算中的收费。",
        },
        {
            "field": "local_factor_nonzero",
            "meaning": "local factor 非零证明；失败时必须给 return_tag。",
        },
        {
            "field": "return_tag",
            "meaning": "无法赋值、Phi 不兼容、变差超预算、canonical 泄漏或 terminal-dependent key 的命名出口。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 signed coefficient lift 判定表。"""
    skeleton = data["skeleton"]
    signed_lift = data["signed_lift"]
    failure = data["failure"]
    weight = data["weight"]
    phi = data["phi"]
    phi_reduction = data["phi_reduction"]
    disintegration = data["disintegration"]
    source_loop = data["source_loop"]
    zero_nogo = data["zero_nogo"]

    target_active = (
        skeleton.get("next_direct_attack_target") == TARGET
        or signed_lift.get("terminal_gap_before_router") == TARGET
        or signed_lift.get("certificate_type") == "prime_matrix_strict_alpha_formula_signed_lift_router"
    )
    unsigned_closed = (
        skeleton.get("unsigned_source_tuple_carry_shell_binding_closed") is True
        and skeleton.get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
        and skeleton.get("unsigned_phase_wheel_compatibility_closed") is True
    )
    failure_named = failure.get("alpha_signed_lift_failure_named_return_ledger_closed") is True

    return [
        row(
            "SignedLiftTargetActive",
            target_active,
            False,
            "当前真正最窄点是把已闭合 unsigned skeleton 提升为 pre-Cauchy signed alpha coefficient。",
            TARGET,
        ),
        row(
            "UnsignedSkeletonClosedImported",
            unsigned_closed,
            True,
            "source tuple、carry-shell、P列锚、层叠轮和 anchor-collar 已给出 row skeleton。",
            "row skeleton 不含 signed coefficient value。",
        ),
        row(
            "FailureNamingDisciplineClosedImported",
            failure_named,
            True,
            "signed lift 缺失、Phi 不兼容、变差超预算和 terminal-dependent key 都已有命名出口。",
            "命名出口登记不等于排斥出口。",
        ),
        row(
            "WeightLawStillOpen",
            weight.get("alpha_signed_weight_law_router_closed") is True
            and weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False,
            False,
            "signed 权重律已被压到独立 pre-Cauchy 算术恒等式和精确权重公式。",
            weight.get("next_direct_attack_target", "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"),
        ),
        row(
            "SignedSourceMeasureStillOpen",
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "当前材料没有在 carry-shell skeleton rows 上定义 actual signed alpha source measure。",
            "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger。",
        ),
        row(
            "PhiPushforwardStillOpen",
            signed_lift.get("alpha_rows_phi_pushforward_compatibility_proved") is False
            and phi.get("geometric_payment_base_available") is True,
            False,
            "几何 Phi/payment base 可用，但 Phi_*nu 等于 payment-side 系数仍需逐 row signed 值表求和。",
            "AlphaRowsPhiPushforwardCompatibilityLedger。",
        ),
        row(
            "VariationBudgetStillOpen",
            signed_lift.get("alpha_signed_lift_variation_branch_budget_proved") is False,
            False,
            "unsigned 支撑预算不能控制 signed 总变差和 branch key 复杂度。",
            "AlphaSignedLiftVariationBranchBudgetLedger。",
        ),
        row(
            "EmitterReductionDoesNotCreateValues",
            phi_reduction.get("registered_primitive_prepushforward_fiber_emitter_proved") is False
            or phi_reduction.get("status") == "actual_signed_phi_budget_reduced_to_prepushforward_emitter_open",
            False,
            "actual signed/Phi/预算路线被压到 prepushforward emitter，但 emitter 也需要同一 signed row 值表。",
            "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。",
        ),
        row(
            "DisintegrationFormalAfterValuesOnly",
            disintegration.get("status") == "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open"
            or disintegration.get("signed_fiber_disintegration_formal") is True,
            False,
            "逐纤维解积分只能在 signed source measure 已给定后使用。",
            "先提交 signed coefficient value table。",
        ),
        row(
            "ReverseRecoveryBlocked",
            source_loop.get("circular_reverse_derivation_rejected") is True
            and zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "不能从 downstream payment skeleton 或早期零行 unsigned cover 反推 signed source。",
            "必须正向给出 pre-Cauchy 系数值。",
        ),
        row(
            "SignedCoefficientLiftCurrentCorpusProved",
            False,
            False,
            "当前材料缺少逐 skeleton row 的 signed coefficient value table。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 signed coefficient lift 终端硬点证书。"""
    data = {
        "skeleton": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "failure": load_json("prime-matrix-strict-alpha-signed-lift-failure-return-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "phi": load_json("prime-matrix-clean-core-geometric-phi-budget-bridge-router.json"),
        "phi_reduction": load_json("prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_signed_coefficient_lift_hardpoint_router",
        "status": "alpha_signed_coefficient_lift_reduced_to_pointwise_signed_value_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "alpha_signed_coefficient_lift_hardpoint_router_closed": True,
        "unsigned_skeleton_imported_closed": True,
        "failure_naming_discipline_imported_closed": True,
        "pointwise_signed_alpha_coefficient_value_table_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "actual_signed_alpha_source_measure_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "alpha_rows_phi_pushforward_compatibility_proved": False,
        "alpha_signed_lift_variation_branch_budget_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_required_inputs": [OVERLOAD_RETURN],
        "value_table_fields": value_table_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 在 unsigned skeleton 已闭合后，等价于提交 `{NEXT_TARGET}`："
            "逐 skeleton row 正向给出 signed alpha weight、算术恒等式来源、Phi atom、变差收费、"
            "local factor 非零和命名回流。"
        ),
        "plain_conclusion": (
            "本步继续硬攻 signed lift。结论是：unsigned carry-shell/P列/phase skeleton 和失败命名纪律已经够用，"
            "真正缺口不是再找 row 形状，而是逐 skeleton row 的 signed 系数值表。没有这张表，actual signed source、"
            "pre-Cauchy 权重律、Phi 推前和 signed 变差预算四项不能合取；从零行覆盖或 payment skeleton 反推仍被禁止。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha signed coefficient lift 硬点路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"alpha_signed_coefficient_lift_hardpoint_router_closed={fmt_bool(result['alpha_signed_coefficient_lift_hardpoint_router_closed'])}",
        f"unsigned_skeleton_imported_closed={fmt_bool(result['unsigned_skeleton_imported_closed'])}",
        f"failure_naming_discipline_imported_closed={fmt_bool(result['failure_naming_discipline_imported_closed'])}",
        f"pointwise_signed_alpha_coefficient_value_table_proved={fmt_bool(result['pointwise_signed_alpha_coefficient_value_table_proved'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"actual_signed_alpha_source_measure_proved={fmt_bool(result['actual_signed_alpha_source_measure_proved'])}",
        f"alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved={fmt_bool(result['alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved'])}",
        f"alpha_rows_phi_pushforward_compatibility_proved={fmt_bool(result['alpha_rows_phi_pushforward_compatibility_proved'])}",
        f"alpha_signed_lift_variation_branch_budget_proved={fmt_bool(result['alpha_signed_lift_variation_branch_budget_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. signed 系数值表字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["value_table_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
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
            "## 4. 下一真正硬点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行必要输入：",
            "",
            "```text",
            *result["parallel_required_inputs"],
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
