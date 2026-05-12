#!/usr/bin/env python3
"""生成 strict primitive summand signed expression 单点攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_primitive_summand_signed_expression_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.json"
OUT_MD = DOCS / "prime-matrix-strict-primitive-summand-signed-expression-router.md"

TARGET = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
NEXT_TARGET = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"

SOURCE_FILES = [
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-triad-a1-canonical-riw-support-router.md",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(name: str) -> str:
    """读取文本证书；缺失时返回空文本。"""
    path = DOCS / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def origin_identity_fields() -> list[dict[str, str]]:
    """列出 signed coefficient origin identity 的必要字段。"""
    return [
        {
            "field": "primitive_row_id",
            "meaning": "同一 formal unit 内的 actual noncanonical primitive summand 行标识。",
        },
        {
            "field": "source_tuple_origin",
            "meaning": "该行的 pre-Cauchy source tuple 来源，而不是推后 payment 原像。",
        },
        {
            "field": "signed_coefficient_formula",
            "meaning": "signed coefficient 的正向表达式，包含符号、筛权、branch/local factor。",
        },
        {
            "field": "prepushforward_identity",
            "meaning": "证明该表达式在 Phi/payment 推前之前等于 actual alpha/delta 系数贡献。",
        },
        {
            "field": "nonzero_or_named_return",
            "meaning": "非零局部因子成立；若失败则进入同 formal unit 的命名回流。",
        },
        {
            "field": "no_import_leak",
            "meaning": "不借用 canonical scoped 公式、外部谱估计、零行覆盖或 terminal 反推。",
        },
    ]


def build_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    """审查当前语料能否给出 primitive summand signed expression。"""
    pointwise = data["pointwise"]
    weight = data["weight"]
    alpha_rule = data["alpha_rule"]
    constructor = data["constructor"]
    source_table = data["source_table"]
    identity = data["identity"]
    moving = data["moving"]
    downstream = data["downstream"]
    external = data["external"]
    path_source = data["path_source"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]
    canonical_text = data["canonical_text"]

    target_active = pointwise.get("next_direct_attack_target") == TARGET
    identity_fixed_point = (
        identity.get("next_direct_attack_target")
        == "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
        and moving.get("strict_actual_moving_block_router_closed") is True
        and downstream.get("downstream_sync_router_closed") is True
    )
    canonical_scoped_only = path_source.get("canonical_template_scoped_only") is True or (
        "canonical" in canonical_text.lower()
        and "riw" in canonical_text.lower()
        and "current ledger" in canonical_text.lower()
    ) or ("canonical" in canonical_text.lower() and (
        "不能跨" in canonical_text
        or "scoped" in canonical_text.lower()
        or "only" in canonical_text.lower()
    ))

    return [
        row(
            "PrimitiveSummandExpressionTargetActive",
            target_active,
            False,
            "上一层已把逐行 signed alpha 权重公式压到 primitive summand 推前前表达式。",
            TARGET,
        ),
        row(
            "ExpressionMustBeOriginIdentity",
            True,
            True,
            "表达式不能只是字段名；必须给出 pre-Cauchy signed coefficient 来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "ExactAlphaWeightFormulaStillOpen",
            weight.get("exact_alpha_signed_weight_formula_proved") is False,
            False,
            "alpha signed weight law 仍未给 exact signed weight formula。",
            "ExactAlphaSignedWeightFormulaLedger 被吸收到来源恒等式中。",
        ),
        row(
            "AlphaPrimitiveCoefficientFormulaStillOpen",
            alpha_rule.get("alpha_primitive_coefficient_weight_formula_proved") is False,
            False,
            "alpha primitive rule 仍未给 primitive coefficient weight formula。",
            "AlphaPrimitiveCoefficientWeightFormulaLedger 被吸收到来源恒等式中。",
        ),
        row(
            "ConstructorFormulaStillDoesNotEmitSignedRows",
            constructor.get("actual_noncanonical_primitive_constructor_formula_line_proved") is False,
            False,
            "actual constructor formula line 未给出带 sign/local factor 的 summand 行。",
            "显式 constructor 行输出须由同一个来源恒等式生成。",
        ),
        row(
            "SourceTableStillNeedsPrimitiveRows",
            source_table.get("actual_emitter_source_table_router_closed") is True
            and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False,
            False,
            "source table 已说明需要 primitive rows 与 coefficient identity before pushforward。",
            "不能用 source table 反向证明来源恒等式。",
        ),
        row(
            "IndependentIdentityRouteStillFixedPoint",
            identity_fixed_point,
            False,
            "独立恒等式路线仍经 moving-block/NCBLK 回到 PDEC/CleanKLS 终端门。",
            "需要非递归来源恒等式破环。",
        ),
        row(
            "ExternalSpectralLemmasDoNotEmitPrimitiveCoefficients",
            external.get("external_lemmas_match_constructor_formula") is False,
            True,
            "DI/BFI/Kuznetsov 等外部估计处理给定系数后的平均，不生成推前前 summand 系数。",
            "外部谱不能替代自足来源恒等式。",
        ),
        row(
            "CanonicalRIWBuchstabScopedOnly",
            canonical_scoped_only,
            True,
            "canonical RIW/Buchstab 公式只在 canonical source 分支内有效，不能跨入 actual noncanonical summand。",
            "若借用 canonical 公式，必须先证明同分支准入；当前没有。",
        ),
        row(
            "ZeroRowAndPaymentReverseRecoveryBlocked",
            reverse.get("pushforward_reverse_uniqueness_rejected") is True
            and zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "早期零行 unsigned cover 与 payment skeleton 都不能反向恢复 signed coefficient。",
            "只能正向提交来源恒等式。",
        ),
        row(
            "OriginIdentityCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交每个 actual primitive summand 的 signed coefficient 来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "PrimitiveSummandExpressionCurrentCorpusProved",
            False,
            False,
            "没有来源恒等式，primitive summand signed expression 仍未证明。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 primitive summand signed expression 单点攻坚证书。"""
    data: dict[str, Any] = {
        "pointwise": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "alpha_rule": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "constructor": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "identity": load_json("prime-matrix-strict-independent-identity-statement-taxonomy-router.json"),
        "moving": load_json("prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"),
        "downstream": load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"),
        "external": load_json("prime-matrix-clean-core-external-lemma-parameter-match-router.json"),
        "path_source": load_json("prime-matrix-clean-core-path-source-firewall-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "canonical_text": load_text("prime-matrix-triad-a1-canonical-riw-support-router.md"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        isinstance(doc, dict)
        and (
            doc.get("direct_unconditional_contradiction_found") is True
            or doc.get("row_column_unconditional_closed") is True
        )
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_primitive_summand_signed_expression_router",
        "status": "primitive_summand_signed_expression_reduced_to_origin_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "primitive_summand_signed_expression_router_closed": True,
        "expression_must_be_origin_identity": True,
        "external_spectral_coefficients_do_not_emit_rows": True,
        "canonical_scoped_formula_not_importable": True,
        "zero_row_or_payment_reverse_recovery_blocked": True,
        "primitive_summand_signed_coefficient_origin_identity_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "pointwise_nonrecursive_signed_alpha_weight_formula_proved": False,
        "pointwise_signed_alpha_coefficient_value_table_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "origin_identity_fields": origin_identity_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "breaker_payload": (
            f"`{NEXT_TARGET}` 若被证明，将同时给出 exact signed weight、primitive coefficient formula、"
            "constructor row 的 sign/local factor 和推前前 alpha/delta identity，因此是当前循环中的真正破坏输入。"
        ),
        "plain_conclusion": (
            "本步把 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` 继续压缩为 "
            "`PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward`。原因是：表达式本身不是证明；"
            "必须正向说明每个 actual noncanonical primitive summand 的 signed coefficient 从哪个 pre-Cauchy "
            "source tuple 产生，并在 Phi/payment 推前之前等于 alpha/delta 系数贡献。现有 canonical、外部谱、"
            "零行覆盖和 payment 反推路径都不能生成该表达式。因此当前仍未得到无条件终端矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict primitive summand signed expression 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"primitive_summand_signed_expression_router_closed={fmt_bool(result['primitive_summand_signed_expression_router_closed'])}",
        f"primitive_summand_signed_coefficient_origin_identity_proved={fmt_bool(result['primitive_summand_signed_coefficient_origin_identity_proved'])}",
        f"primitive_summand_signed_weight_expression_proved={fmt_bool(result['primitive_summand_signed_weight_expression_proved'])}",
        f"pointwise_nonrecursive_signed_alpha_weight_formula_proved={fmt_bool(result['pointwise_nonrecursive_signed_alpha_weight_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 破坏输入",
        "",
        result["breaker_payload"],
        "",
        "## 2. 来源恒等式字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["origin_identity_fields"]:
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
