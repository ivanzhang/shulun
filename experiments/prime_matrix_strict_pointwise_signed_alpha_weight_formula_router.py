#!/usr/bin/env python3
"""生成 strict 逐行 signed alpha 权重公式攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_pointwise_signed_alpha_weight_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.md"

TARGET = "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow"
NEXT_TARGET = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"

SOURCE_FILES = [
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
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


def expression_fields() -> list[dict[str, str]]:
    """列出 primitive summand signed weight expression 的字段。"""
    return [
        {
            "field": "primitive_summand_row",
            "meaning": "pre-pushforward、pre-Cauchy 的 actual noncanonical primitive summand 行。",
        },
        {
            "field": "alpha_delta_side",
            "meaning": "标明该行属于 alpha 侧或 delta 侧，并给出配对规则。",
        },
        {
            "field": "signed_weight_expression",
            "meaning": "该 summand 的 signed coefficient 的闭式表达式或有限递推式。",
        },
        {
            "field": "local_factor_product",
            "meaning": "符号、筛因子、截断因子、branch local factor 的乘积口径。",
        },
        {
            "field": "uv_key_output",
            "meaning": "同一行同时输出 exact `(u,v)` 与 branch key。",
        },
        {
            "field": "identity_before_pushforward",
            "meaning": "证明表达式在 Phi/payment 推前之前已经成立。",
        },
        {
            "field": "no_canonical_or_external_leak",
            "meaning": "证明没有借用 canonical scoped 模板、外部谱黑箱或 terminal 反推。",
        },
        {
            "field": "failure_return",
            "meaning": "公式不适用、local factor 为零、符号冲突或超预算时的命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成逐行 signed alpha 权重公式判定表。"""
    value_table = data["value_table"]
    weight = data["weight"]
    alpha_rule = data["alpha_rule"]
    constructor = data["constructor"]
    declaration = data["declaration"]
    source_table = data["source_table"]
    source_loop = data["source_loop"]
    zero_nogo = data["zero_nogo"]
    identity = data["identity"]
    moving = data["moving"]

    target_active = value_table.get("next_direct_attack_target") == TARGET
    identity_fixed_point = (
        identity.get("next_direct_attack_target")
        == "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
        and moving.get("strict_actual_moving_block_router_closed") is True
    )
    source_table_needs_rows = (
        source_table.get("actual_emitter_source_table_router_closed") is True
        and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
    )

    return [
        row(
            "PointwiseWeightFormulaTargetActive",
            target_active,
            False,
            "上一层已把 signed value table 的首字段压成逐行 signed alpha 权重公式。",
            TARGET,
        ),
        row(
            "ExactWeightFormulaStillOpen",
            weight.get("exact_alpha_signed_weight_formula_proved") is False,
            False,
            "alpha signed weight law 已明确需要 ExactAlphaSignedWeightFormulaLedger。",
            "ExactAlphaSignedWeightFormulaLedger。",
        ),
        row(
            "PrimitiveCoefficientFormulaStillOpen",
            alpha_rule.get("alpha_primitive_coefficient_weight_formula_proved") is False,
            False,
            "alpha primitive rule 仍缺 coefficient weight formula 和 row/output/local factor 同步。",
            "AlphaPrimitiveCoefficientWeightFormulaLedger。",
        ),
        row(
            "ConstructorFormulaLineStillOpen",
            constructor.get("actual_noncanonical_primitive_constructor_formula_line_proved") is False,
            False,
            "actual constructor formula line 尚未给出可发射 signed row 的原始公式。",
            constructor.get("next_direct_attack_target", "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"),
        ),
        row(
            "PreCauchyDeclarationStillOpen",
            declaration.get("pre_cauchy_constructor_declaration_line_proved") is False,
            False,
            "pre-Cauchy declaration line 尚未锁定同 formal-unit 时间戳、noncanonical 来源和无泄漏。",
            declaration.get("next_direct_attack_target", "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter"),
        ),
        row(
            "SourceTableNeedsSamePrimitiveRows",
            source_table_needs_rows,
            False,
            "actual emitter source table 需要 primitive summand rows 和 alpha/delta coefficient identity before pushforward。",
            "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger。",
        ),
        row(
            "IndependentIdentityRouteNotProof",
            identity_fixed_point,
            False,
            "独立恒等式陈述已被分类到 actual moving-block/NC-BLK，并回到终端门，不能证明逐行权重公式。",
            "需要非递归 primitive summand expression。",
        ),
        row(
            "ReverseRecoveryBlocked",
            source_loop.get("circular_reverse_derivation_rejected") is True
            and zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "不能从 payment skeleton、零行覆盖或 terminal certificate 反向恢复 signed weight。",
            "必须在 pushforward 前正向给出表达式。",
        ),
        row(
            "PrimitiveSummandSignedWeightExpressionCurrentCorpusProved",
            False,
            False,
            "当前材料没有 actual noncanonical primitive summand 的 signed weight expression before pushforward。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseSignedWeightFormulaCurrentCorpusProved",
            False,
            False,
            "没有 primitive summand signed expression，就无法给每条 carry-shell skeleton row 赋权。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造逐行 signed alpha 权重公式证书。"""
    data = {
        "value_table": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "alpha_rule": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "constructor": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "declaration": load_json("prime-matrix-strict-precauchy-declaration-line-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "identity": load_json("prime-matrix-strict-independent-identity-statement-taxonomy-router.json"),
        "moving": load_json("prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_pointwise_signed_alpha_weight_formula_router",
        "status": "pointwise_signed_alpha_weight_formula_reduced_to_primitive_summand_expression_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "pointwise_signed_alpha_weight_formula_router_closed": True,
        "exact_alpha_signed_weight_formula_proved": False,
        "alpha_primitive_coefficient_weight_formula_proved": False,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "pointwise_nonrecursive_signed_alpha_weight_formula_proved": False,
        "pointwise_signed_alpha_coefficient_value_table_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "expression_fields": expression_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 不能由权重律名称、source table 名称或独立恒等式分类自动推出；"
            f"它必须先提交 `{NEXT_TARGET}`，也就是在 Phi/payment 推前之前给出 actual noncanonical "
            "primitive summand 的 signed coefficient 表达式。"
        ),
        "plain_conclusion": (
            "本步继续硬攻逐行 signed 权重公式。结论是：当前材料只有权重律的字段分解和反推禁令，"
            "没有 primitive summand 级 signed coefficient 表达式。source table、constructor formula 和"
            " pre-Cauchy declaration 都指向同一个前推前原始表达式缺口；独立恒等式路线则回到终端固定点。"
            "因此最新最精确单点是 actual noncanonical primitive summand signed weight expression before pushforward。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 逐行 signed alpha 权重公式路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pointwise_signed_alpha_weight_formula_router_closed={fmt_bool(result['pointwise_signed_alpha_weight_formula_router_closed'])}",
        f"exact_alpha_signed_weight_formula_proved={fmt_bool(result['exact_alpha_signed_weight_formula_proved'])}",
        f"alpha_primitive_coefficient_weight_formula_proved={fmt_bool(result['alpha_primitive_coefficient_weight_formula_proved'])}",
        f"actual_noncanonical_primitive_constructor_formula_line_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_line_proved'])}",
        f"primitive_summand_signed_weight_expression_proved={fmt_bool(result['primitive_summand_signed_weight_expression_proved'])}",
        f"pointwise_nonrecursive_signed_alpha_weight_formula_proved={fmt_bool(result['pointwise_nonrecursive_signed_alpha_weight_formula_proved'])}",
        f"pointwise_signed_alpha_coefficient_value_table_proved={fmt_bool(result['pointwise_signed_alpha_coefficient_value_table_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. primitive summand 表达式字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["expression_fields"]:
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
            "## 4. 下一真正单点",
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
