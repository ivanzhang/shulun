#!/usr/bin/env python3
"""生成 LPF candidate-row map 到 alpha-side primitive rule 的桥接证书。

用法示例：
  python3 experiments/prime_matrix_lpf_candidate_row_map_alpha_rule_router.py
  python3 -m json.tool docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json

输出：
  data/prime-matrix-lpf-candidate-row-map-alpha-rule-ledger.json
  docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json
  docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-lpf-candidate-row-map-alpha-rule"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LPF_DECLARATION_CERT = DOCS / "prime-matrix-lpf-ownership-sieve-source-declaration-router.json"
ALPHA_SIDE_RULE_CERT = DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json"
SIGNED_VALUE_TABLE_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"
SIGNED_WEIGHT_FORMULA_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
UNSIGNED_SKELETON_CERT = DOCS / "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"

ALPHA_SIDE_RULE = "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
DETERMINISTIC_MAP = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
LPF_CANDIDATE_MAP = "LPFOwnershipAlphaCandidateRowEmissionMapLedger"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
WEIGHT_FORMULA = "AlphaPrimitiveCoefficientWeightFormulaLedger"
UV_KEY_OUTPUT = "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger"
FAILURE_RETURN = "AlphaPrimitiveRuleFailureNamedReturnLedger"

MAP_REPLACEMENT = f"{LPF_CANDIDATE_MAP} AND {SIGNED_EXPR}"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LPF_DECLARATION_CERT,
        ALPHA_SIDE_RULE_CERT,
        SIGNED_VALUE_TABLE_CERT,
        SIGNED_WEIGHT_FORMULA_CERT,
        UNSIGNED_SKELETON_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def replace_map_target(alpha_rule: dict[str, Any]) -> str:
    """把 alpha-side rule 中的 deterministic map 替换为 LPF candidate map 与 signed expression。"""
    basis = alpha_rule.get("terminal_gap_after_router", "")
    if DETERMINISTIC_MAP in basis:
        return basis.replace(DETERMINISTIC_MAP, MAP_REPLACEMENT)
    return (
        "ActualNoncanonicalAlphaSourceTupleDomainLedger AND "
        f"{MAP_REPLACEMENT} AND {WEIGHT_FORMULA} AND {UV_KEY_OUTPUT} AND {FAILURE_RETURN}"
    )


def build_rows(
    lpf_declaration: dict[str, Any],
    alpha_rule: dict[str, Any],
    signed_value: dict[str, Any],
    signed_formula: dict[str, Any],
    unsigned_skeleton: dict[str, Any],
    after_target: str,
) -> list[dict[str, Any]]:
    """生成 LPF candidate-row map 判定表。"""
    lpf_closed = lpf_declaration.get("lpf_ownership_unsigned_declaration_line_closed") is True
    alpha_rule_closed = alpha_rule.get("alpha_side_primitive_rule_router_closed") is True
    unsigned_closed = unsigned_skeleton.get("alpha_row_unsigned_skeleton_router_closed") is True
    signed_value_open = signed_value.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
    signed_expr_open = signed_formula.get("primitive_summand_signed_weight_expression_proved") is False
    return [
        row(
            "AlphaSidePrimitiveRuleTargetImported",
            alpha_rule_closed,
            False,
            "显式 alpha/delta 规则的当前首个侧向硬点是 alpha-side primitive rule。",
            ALPHA_SIDE_RULE,
        ),
        row(
            "DeterministicAlphaMapGapImported",
            alpha_rule.get("next_direct_attack_target") == DETERMINISTIC_MAP,
            False,
            "alpha-side rule 内部首缺口是 source tuple 到 alpha primitive rows 的确定性发射映射。",
            DETERMINISTIC_MAP,
        ),
        row(
            "LPFOwnershipDeclarationImported",
            lpf_closed,
            True,
            "上一层已证明升序最小素因子 ownership 分桶和 pre-Cauchy unsigned declaration 字段。",
            "LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger",
        ),
        row(
            "LPFCompositeBucketToCandidateRowsClosed",
            lpf_closed,
            True,
            "每个候选合数行可由唯一 p 层和 cofactor m 索引；不同 p 层不重叠，不需要 payment 反推选原像。",
            LPF_CANDIDATE_MAP,
        ),
        row(
            "UnsignedSkeletonCompatibilityImported",
            unsigned_closed,
            True,
            "carry-shell、P 列锚、phase rule 与 layered-wheel 可承接 LPF candidate row 的几何坐标。",
            "AlphaRowUnsignedSkeletonLedger",
        ),
        row(
            "LPFCandidateMapIsNotSignedPrimitiveMap",
            lpf_closed,
            True,
            "LPF candidate map 只确定候选 row ownership 和几何索引；它不赋 signed weight、local factor 或 primitive summand 表达式。",
            SIGNED_EXPR,
        ),
        row(
            "SignedValueTableStillOpen",
            signed_value_open,
            False,
            "逐 skeleton row 的 signed alpha value table 仍未证明。",
            "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
        ),
        row(
            "PrimitiveSummandSignedExpressionStillOpen",
            signed_expr_open,
            False,
            "逐行 signed 权重公式已压到 actual noncanonical primitive summand signed expression before pushforward。",
            SIGNED_EXPR,
        ),
        row(
            "DeterministicAlphaMapReducedToLPFCandidateAndSignedExpression",
            lpf_closed and alpha_rule_closed,
            False,
            "确定性发射映射的非后验候选索引由 LPF ownership 支付；要成为 actual alpha primitive row，还必须给 signed summand expression。",
            after_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步不证明 signed expression、delta-side rule、pairing compatibility、ExactUV fixed-key 或终端排斥。",
            after_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 LPF candidate-row map 证书。"""
    lpf_declaration = load_json(LPF_DECLARATION_CERT)
    alpha_rule = load_json(ALPHA_SIDE_RULE_CERT)
    signed_value = load_json(SIGNED_VALUE_TABLE_CERT)
    signed_formula = load_json(SIGNED_WEIGHT_FORMULA_CERT)
    unsigned_skeleton = load_json(UNSIGNED_SKELETON_CERT)
    after_target = replace_map_target(alpha_rule)
    rows = build_rows(
        lpf_declaration=lpf_declaration,
        alpha_rule=alpha_rule,
        signed_value=signed_value,
        signed_formula=signed_formula,
        unsigned_skeleton=unsigned_skeleton,
        after_target=after_target,
    )
    lpf_candidate_closed = any(
        item["gate"] == "LPFCompositeBucketToCandidateRowsClosed" and item["closed"]
        for item in rows
    )
    return {
        "certificate_type": "prime_matrix_lpf_candidate_row_map_alpha_rule_router",
        "status": "lpf_candidate_row_map_closed_signed_summand_expression_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "alpha_side_primitive_rule_imported": rows[0]["closed"],
        "deterministic_alpha_map_gap_imported": rows[1]["closed"],
        "lpf_ownership_declaration_imported": rows[2]["closed"],
        "lpf_candidate_row_emission_map_closed": lpf_candidate_closed,
        "unsigned_skeleton_compatibility_imported": rows[4]["closed"],
        "lpf_candidate_map_not_signed_primitive_map": True,
        "pointwise_signed_alpha_value_table_proved": False,
        "primitive_summand_signed_weight_expression_proved": False,
        "actual_noncanonical_alpha_side_primitive_rule_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": DETERMINISTIC_MAP,
        "hardpoint_after_router": after_target,
        "next_direct_attack_target": SIGNED_EXPR,
        "parallel_open_exits": [
            "ActualNoncanonicalAlphaSourceTupleDomainLedger",
            WEIGHT_FORMULA,
            UV_KEY_OUTPUT,
            FAILURE_RETURN,
            "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger",
            "AlphaDeltaPairingCompatibilityBeforeCauchyLedger",
            "PrimitiveRuleNonzeroSignLocalFactorLedger",
        ],
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "LPF ownership 进一步支付 alpha-side primitive rule 中的非后验候选 row 发射映射："
            "每个候选合数 row 由唯一最小素因子层 p 与 cofactor m 索引，且与已闭合 unsigned skeleton 兼容。"
            "但 candidate row map 仍不是 actual signed primitive row map；最新硬点转为 "
            "`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix LPF candidate-row map alpha-rule 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"alpha_side_primitive_rule_imported={fmt_bool(cert['alpha_side_primitive_rule_imported'])}",
        f"deterministic_alpha_map_gap_imported={fmt_bool(cert['deterministic_alpha_map_gap_imported'])}",
        f"lpf_ownership_declaration_imported={fmt_bool(cert['lpf_ownership_declaration_imported'])}",
        f"lpf_candidate_row_emission_map_closed={fmt_bool(cert['lpf_candidate_row_emission_map_closed'])}",
        f"pointwise_signed_alpha_value_table_proved={fmt_bool(cert['pointwise_signed_alpha_value_table_proved'])}",
        f"primitive_summand_signed_weight_expression_proved={fmt_bool(cert['primitive_summand_signed_weight_expression_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 桥接公式",
        "",
        "```text",
        f"{DETERMINISTIC_MAP}",
        "  ->",
        f"{LPF_CANDIDATE_MAP}",
        f"AND {SIGNED_EXPR}",
        "```",
        "",
        "含义：LPF ownership 只关闭候选 row 的唯一来源索引；actual alpha primitive row 仍需要前推前 signed summand 表达式。",
        "",
        "## 2. 新 alpha-side 剩余基",
        "",
        "```text",
        cert["hardpoint_after_router"],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 诚实边界",
            "",
            "- 本证书没有证明 signed alpha value table。",
            "- 本证书没有证明 actual noncanonical primitive summand signed weight expression before pushforward。",
            "- 本证书没有证明 delta-side primitive rule、alpha/delta pairing compatibility 或 ExactUV fixed-key multiplicity。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
