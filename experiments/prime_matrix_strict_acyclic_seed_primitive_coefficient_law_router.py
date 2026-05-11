#!/usr/bin/env python3
"""生成 strict acyclic seed primitive row signed coefficient law 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_primitive_coefficient_law_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.md"

TARGET = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
NEXT_TARGET = "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
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


def law_decomposition() -> list[dict[str, str]]:
    """列出 signed coefficient law 的内部拆分。"""
    return [
        {
            "component": "basis_weight_source",
            "role": "给出 seed 内部的 pre-Cauchy 算术基函数/筛权来源。",
            "status": "first open component",
        },
        {
            "component": "sign_rule",
            "role": "由 basis weight 与 branch key 决定每行符号。",
            "status": "depends on basis_weight_source",
        },
        {
            "component": "local_factor_rule",
            "role": "给出 local factor 闭式公式、非零条件和失败回流。",
            "status": "depends on basis_weight_source",
        },
        {
            "component": "truncation_phase_charge",
            "role": "登记截断、相位过滤和 signed branch 变差收费。",
            "status": "depends on row coefficient value",
        },
        {
            "component": "alpha_delta_prepushforward_sum_identity",
            "role": "证明 primitive rows 在推前前求和等于 actual alpha/delta 系数。",
            "status": "depends on all previous components",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 signed coefficient law 的最小首字段。"""
    previous = data["previous"]
    weight = data["weight"]
    alpha_rule = data["alpha_rule"]
    pointwise = data["pointwise"]
    lift = data["lift"]
    key = data["key"]
    unsigned = data["unsigned"]
    disintegration = data["disintegration"]
    zero_nogo = data["zero_nogo"]
    reverse = data["reverse"]

    return [
        row(
            "PrimitiveCoefficientLawTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把合法 seed 分支内的 signed row emitter 压到 primitive row signed coefficient law。",
            TARGET,
        ),
        row(
            "CoefficientLawDecomposed",
            True,
            True,
            "signed coefficient law 可拆为 basis weight source、sign/local factor、收费和推前前求和恒等式。",
            NEXT_TARGET,
        ),
        row(
            "BasisWeightSourceIsFirstOpenComponent",
            True,
            True,
            "没有 seed 内部 pre-Cauchy basis weight 来源，后续符号、local factor 和求和恒等式无从定义。",
            NEXT_TARGET,
        ),
        row(
            "AlphaSignedWeightLawStillOpen",
            weight.get("exact_alpha_signed_weight_formula_proved") is False
            and weight.get("independent_noncanonical_precauchy_arithmetic_identity_statement_proved") is False,
            False,
            "alpha signed weight law 仍缺 exact formula 与独立 pre-Cauchy 算术恒等式。",
            NEXT_TARGET,
        ),
        row(
            "AlphaPrimitiveCoefficientFormulaStillOpen",
            alpha_rule.get("alpha_primitive_coefficient_weight_formula_proved") is False,
            False,
            "alpha primitive rule 仍缺 primitive coefficient weight formula。",
            NEXT_TARGET,
        ),
        row(
            "PointwisePrimitiveExpressionStillOpen",
            pointwise.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "逐行 signed weight 公式仍缺 primitive summand 推前前表达式。",
            NEXT_TARGET,
        ),
        row(
            "SignedValueTableStillOpen",
            lift.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "signed lift 仍缺逐 skeleton row signed value table。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedSkeletonCannotSupplyBasisWeight",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
            and unsigned.get("alpha_formula_signed_coefficient_lift_proved") is False,
            True,
            "unsigned skeleton 只给几何 row 位置和相位字母表，不含 basis weight 来源。",
            NEXT_TARGET,
        ),
        row(
            "KeyAndDisintegrationAreAfterCoefficient",
            key.get("complete_emitter_key_partition_router_closed") is True
            and (
                disintegration.get("signed_fiber_disintegration_formal") is True
                or disintegration.get("status")
                == "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open"
            ),
            False,
            "branch key、ExactUV 和解积分只能在 signed coefficient 已登记后验证。",
            "不能反向生成 basis weight source。",
        ),
        row(
            "ReverseRecoveryBlocked",
            zero_nogo.get("zero_row_seed_extraction_blocked") is True
            and reverse.get("pushforward_reverse_uniqueness_rejected") is True,
            True,
            "不能从早期零行覆盖或 payment 原像选择反推 basis weight source。",
            NEXT_TARGET,
        ),
        row(
            "AcyclicSeedPreCauchyBasisWeightSourceFormulaCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出 seed 内部的 pre-Cauchy basis weight 来源公式。",
            NEXT_TARGET,
        ),
        row(
            "AcyclicSeedPrimitiveRowSignedCoefficientLawCurrentCorpusProved",
            False,
            False,
            "没有 basis weight 来源公式，primitive row signed coefficient law 仍未证明。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 primitive coefficient law 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "alpha_rule": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "key": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_primitive_coefficient_law_router",
        "status": "acyclic_seed_primitive_coefficient_law_reduced_to_basis_weight_source_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "acyclic_seed_primitive_coefficient_law_router_closed": True,
        "coefficient_law_decomposition_closed": True,
        "basis_weight_source_is_first_open_component": True,
        "acyclic_seed_precauchy_basis_weight_source_formula_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "acyclic_seed_signed_row_emitter_rule_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "terminal_return_if_no_basis_weight_source": TERMINAL_RETURN,
        "law_decomposition": law_decomposition(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 的首个不可替代字段是 `{NEXT_TARGET}`。没有 basis weight source，"
            "sign/local factor、变差收费和推前前求和恒等式都不能成为数学陈述。"
        ),
        "plain_conclusion": (
            "本步把 acyclic seed primitive row signed coefficient law 压到最前置字段："
            "seed 内部 pre-Cauchy basis weight 来源公式。unsigned skeleton、branch key、ExactUV、解积分和 "
            "payment 原像选择都只能在系数给定后验证，不能生成该来源公式。当前材料没有这条 basis weight "
            "source formula，所以仍未得到无条件终端矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed primitive coefficient law 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_seed_primitive_coefficient_law_router_closed={fmt_bool(result['acyclic_seed_primitive_coefficient_law_router_closed'])}",
        f"acyclic_seed_precauchy_basis_weight_source_formula_proved={fmt_bool(result['acyclic_seed_precauchy_basis_weight_source_formula_proved'])}",
        f"acyclic_seed_primitive_row_signed_coefficient_law_proved={fmt_bool(result['acyclic_seed_primitive_row_signed_coefficient_law_proved'])}",
        f"acyclic_seed_signed_row_emitter_rule_proved={fmt_bool(result['acyclic_seed_signed_row_emitter_rule_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. coefficient law 拆分",
        "",
        "| component | role | status |",
        "| --- | --- | --- |",
    ]
    for item in result["law_decomposition"]:
        lines.append(
            "| `{component}` | {role} | {status} |".format(
                component=table_cell(item["component"]),
                role=table_cell(item["role"]),
                status=table_cell(item["status"]),
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
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_basis_weight_source"],
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
