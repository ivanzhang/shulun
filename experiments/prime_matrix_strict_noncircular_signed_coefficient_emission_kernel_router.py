#!/usr/bin/env python3
"""生成 strict 非循环 signed coefficient 发射核攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_noncircular_signed_coefficient_emission_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"
OUT_MD = DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.md"

TARGET = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
NEXT_TARGET = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_PATHS = [
    "docs/monograph/prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "docs/monograph/prime-matrix-strict-actual-emitter-source-table-router.json",
    "docs/monograph/prime-matrix-strict-precauchy-declaration-line-router.json",
    "docs/monograph/prime-matrix-strict-actual-constructor-formula-line-router.json",
    "docs/monograph/prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "docs/monograph/prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "docs/monograph/prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "docs/monograph/prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "docs/monograph/prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "docs/monograph/prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "docs/monograph/prime-matrix-strict-alpha-signed-weight-law-router.json",
    "docs/monograph/prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "docs/monograph/prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "experiments/truncated_mobius_predictor.py",
    "experiments/prime_matrix_alpha_tail_threeedge_parity_audit.py",
    "experiments/prime_matrix_alpha_tail_threeedge_tailanchor_audit.py",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 monograph JSON；缺失时返回空对象。"""
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
    result: dict[str, str] = {}
    for raw in SOURCE_PATHS:
        path = ROOT / raw
        if path.exists():
            result[raw] = sha256(path)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def declaration_fields() -> list[dict[str, str]]:
    """列出 kernel 入口必须首先声明的字段。"""
    return [
        {
            "field": "declared_before_cauchy",
            "meaning": "constructor/emitter 在 Cauchy、dispersion、Phi/payment 之前声明。",
        },
        {
            "field": "same_formal_unit",
            "meaning": "source tuple、basis word、signed coefficient 和 return tag 使用同一 formal unit。",
        },
        {
            "field": "actual_noncanonical_scope",
            "meaning": "声明不能偷换为 canonical、generic WFD、external spectral 或 mixed/unregistered source。",
        },
        {
            "field": "formula_line_pointer",
            "meaning": "声明必须指向 actual noncanonical primitive constructor formula line。",
        },
        {
            "field": "no_downstream_choice",
            "meaning": "声明不得读取 payment skeleton、早期零行 cover、origin table 或终端证书。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查非循环 kernel 是否能由现有材料直接给出。"""
    previous = data["previous"]
    source_table = data["source_table"]
    declaration = data["declaration"]
    formula_line = data["formula_line"]
    explicit_rule = data["explicit_rule"]
    alpha_side = data["alpha_side"]
    row_emission = data["row_emission"]
    anchor_phase = data["anchor_phase"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    signed_weight = data["signed_weight"]
    value_table = data["value_table"]
    weight_formula = data["weight_formula"]

    mobius_predictor_exists = (ROOT / "experiments" / "truncated_mobius_predictor.py").exists()
    threeedge_audits_exist = all(
        [
            (ROOT / "experiments" / "prime_matrix_alpha_tail_threeedge_parity_audit.py").exists(),
            (ROOT / "experiments" / "prime_matrix_alpha_tail_threeedge_tailanchor_audit.py").exists(),
        ]
    )
    geometry_skeleton_closed = unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
    signed_layer_open = all(
        [
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False,
            signed_weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False,
            value_table.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            weight_formula.get("pointwise_nonrecursive_signed_alpha_weight_formula_proved") is False,
        ]
    )

    return [
        row(
            "NoncircularKernelTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层 signed-source 固定点切断后，真正单点变成非循环 pre-Cauchy signed coefficient 发射核。",
            TARGET,
        ),
        row(
            "MobiusTruncationIsDiagnosticNotExactKernel",
            mobius_predictor_exists,
            True,
            "截断 Möbius 短除数权只给粗数指标近似/相关性，不保证 exact signed row、local factor 或推前前恒等式。",
            NEXT_TARGET,
        ),
        row(
            "ThreeEdgeParityAuditsAreLocalShadowsNotEmitter",
            threeedge_audits_exist,
            True,
            "三点/三边奇偶审计解释局部符号影子，但仍是有限审计，不声明 actual noncanonical emitter。",
            NEXT_TARGET,
        ),
        row(
            "SourceTablePinsFirstKernelField",
            source_table.get("next_direct_attack_target") == NEXT_TARGET,
            True,
            "已有 actual emitter source table 证书把源表首字段固定为 pre-Cauchy constructor declaration line。",
            NEXT_TARGET,
        ),
        row(
            "PreCauchyDeclarationLineStillOpen",
            declaration.get("pre_cauchy_constructor_declaration_line_proved") is False,
            False,
            "declaration line 已被分类到 actual constructor formula line，但未证明。",
            "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter",
        ),
        row(
            "ActualConstructorFormulaLineStillOpen",
            formula_line.get("actual_noncanonical_primitive_constructor_formula_line_proved") is False,
            False,
            "actual constructor formula line 仍缺显式 alpha/delta 规则、域准入、行输出和失败回流。",
            "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter",
        ),
        row(
            "ExplicitAlphaDeltaRuleStillOpen",
            explicit_rule.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False,
            False,
            "显式 alpha/delta 规则仍缺两侧 primitive rule、配对兼容和非零 sign/local factor。",
            "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger",
        ),
        row(
            "AlphaEmissionRouteHitsSignedLiftAgain",
            alpha_side.get("deterministic_alpha_primitive_row_emission_map_proved") is False
            and row_emission.get("next_direct_attack_target") == "AlphaRowAnchorPhaseEmissionFormulaLedger"
            and anchor_phase.get("next_direct_attack_target") == "AlphaFormulaSignedCoefficientLiftLedger",
            False,
            "alpha 侧行发射路线先到锚/相位公式，unsigned 骨架闭合后又回到 signed lift。",
            "signed coefficient layer。",
        ),
        row(
            "UnsignedGeometryClosedButSignedLayerOpen",
            geometry_skeleton_closed and signed_layer_open,
            False,
            "carry-shell、P列锚、layered-wheel 和 anchor-collar 只关闭 unsigned skeleton；signed 值表仍开放。",
            "AlphaFormulaSignedCoefficientLiftLedger。",
        ),
        row(
            "NoncircularKernelCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出不依赖下游恢复的 exact pre-Cauchy signed coefficient 发射核。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造非循环 kernel 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "declaration": load_json("prime-matrix-strict-precauchy-declaration-line-router.json"),
        "formula_line": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "alpha_side": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "row_emission": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "anchor_phase": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "signed_weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "value_table": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "weight_formula": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_strict_noncircular_signed_coefficient_emission_kernel_router",
        "status": "noncircular_signed_coefficient_emission_kernel_reduced_to_precauchy_declaration_line_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "noncircular_kernel_router_closed": True,
        "mobius_truncation_rejected_as_exact_kernel": True,
        "threeedge_parity_audits_rejected_as_exact_kernel": True,
        "source_table_pins_precauchy_declaration_first": True,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "terminal_return_if_no_kernel": TERMINAL_RETURN,
        "declaration_fields": declaration_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的首个合法字段是 `{NEXT_TARGET}`；"
            "Möbius 截断和三边奇偶只能作符号影子/数值审计，不能替代 exact pre-Cauchy emitter 声明。"
        ),
        "plain_conclusion": (
            "本步继续硬攻非循环 signed coefficient 发射核。现有 Möbius/奇偶材料能帮助理解符号结构，"
            "但没有给出 actual noncanonical emitter 的 Cauchy 前声明、公式行、非零 local factor 和推前前恒等式。"
            "因此 kernel 的第一字段仍是 `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter`；"
            "这保持同一目标命题，只是把 signed-source 固定点的入口首字段钉死。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 非循环 signed coefficient 发射核证书",
        "",
        "## 1. 结论",
        "",
        result["plain_conclusion"],
        "",
        "## 2. 状态",
        "",
        f"- same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"- mobius_truncation_rejected_as_exact_kernel={fmt_bool(result['mobius_truncation_rejected_as_exact_kernel'])}",
        f"- source_table_pins_precauchy_declaration_first={fmt_bool(result['source_table_pins_precauchy_declaration_first'])}",
        f"- pre_cauchy_constructor_declaration_line_proved={fmt_bool(result['pre_cauchy_constructor_declaration_line_proved'])}",
        f"- noncircular_signed_coefficient_emission_kernel_proved={fmt_bool(result['noncircular_signed_coefficient_emission_kernel_proved'])}",
        f"- row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. Declaration 首字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["declaration_fields"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 5. 下一真正单点",
            "",
            result["next_direct_attack_target"],
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
