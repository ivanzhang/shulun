#!/usr/bin/env python3
"""生成 strict actual emitter source table 字段拆分证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_emitter_source_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-emitter-source-table-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-prepushforward-emitter-origin-ledger-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
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
    complete_key: dict[str, Any],
    prepush: dict[str, Any],
    source_loop: dict[str, Any],
    zero_seed: dict[str, Any],
    identity_taxonomy: dict[str, Any],
    constructor_firewall: dict[str, Any],
    origin_admission: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 actual emitter source table 字段判定表。"""
    target = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
    next_basis = (
        "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter AND "
        "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND "
        "AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND "
        "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
    )
    terminal_after = complete_key.get("terminal_gap_after_router", "")
    return [
        {
            "gate": "ActualEmitterSourceTableTargetActive",
            "closed": target in terminal_after,
            "proved": False,
            "meaning": "上一层 complete key 分区已经把首要实际字段压成 actual noncanonical primitive emitter 源表。",
            "remaining": target,
        },
        {
            "gate": "SourceTableIsOriginLedgerRestrictedToEmitter",
            "closed": prepush.get("terminal_gap_after_router")
            == "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
            "proved": True,
            "meaning": "pre-pushforward emitter 的源表本质就是 clean-core 原始生成账本在当前 emitter 支撑上的限制。",
            "remaining": "这只是对象识别，不证明源表存在。",
        },
        {
            "gate": "SourceLoopCutImported",
            "closed": source_loop.get("source_loop_cut_closed") is True,
            "proved": True,
            "meaning": "origin ledger、constructor、formula、registered emitter 之间只形成等价环；不能用该环自证源表。",
            "remaining": "必须给无环 pre-Cauchy declaration line。",
        },
        {
            "gate": "ZeroRowCannotSupplySourceTable",
            "closed": zero_seed.get("zero_row_seed_extraction_blocked") is True,
            "proved": True,
            "meaning": "假设早期零行只给 unsigned 覆盖/CRT/payment 数据，不能生成 signed pre-Cauchy source table。",
            "remaining": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter。",
        },
        {
            "gate": "SourceClassFirewallImported",
            "closed": constructor_firewall.get("constructor_source_class_firewall_boundary_closed")
            is True,
            "proved": True,
            "meaning": "canonical、generic WFD、unregistered 与 external 类已分流；strict 自足表只能来自 actual noncanonical declaration。",
            "remaining": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter。",
        },
        {
            "gate": "IndependentIdentityTaxonomyImported",
            "closed": identity_taxonomy.get("identity_taxonomy_closed") is True,
            "proved": True,
            "meaning": "独立 pre-Cauchy 来源恒等式的伪来源已穷尽；外部谱不能作为自足 source table。",
            "remaining": "actual noncanonical source declaration 或命名回流。",
        },
        {
            "gate": "SourceTableFieldDecompositionPinned",
            "closed": True,
            "proved": True,
            "meaning": "一个合法源表必须包含 declaration line、primitive summand rows、推前前系数恒等式和命名回流栏。",
            "remaining": next_basis,
        },
        {
            "gate": "PreCauchyDeclarationLineCurrentCorpusProved",
            "closed": origin_admission.get("clean_core_primitive_source_constructor_admission_proved")
            is True,
            "proved": False,
            "meaning": "当前材料尚未在 Cauchy/dispersion 前声明 actual noncanonical emitter 的 primitive constructor 来源。",
            "remaining": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter。",
        },
        {
            "gate": "PrimitiveSummandRowsCurrentCorpusProved",
            "closed": constructor_firewall.get("actual_noncanonical_primitive_constructor_formula_proved")
            is True,
            "proved": False,
            "meaning": "没有 declaration line，就不能合法列出 summand、branch key、u/v、sign/local factor 的实际行。",
            "remaining": "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable。",
        },
        {
            "gate": "CoefficientIdentityBeforePushforwardCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明这些 primitive rows 在推前前求和等于 actual alpha/delta 系数。",
            "remaining": "AlphaDeltaCoefficientIdentityBeforePushforwardLedger。",
        },
        {
            "gate": "NoDownstreamRecoveryReturnLedgerCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "未提交源表、后验补表、超预算、thin/rejected 或抵消情形仍需逐项命名回流。",
            "remaining": "SourceTableNoDownstreamRecoveryAndNamedReturnLedger。",
        },
        {
            "gate": "ActualEmitterSourceTableCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "四个源表字段尚未合取证明，所以 actual primitive emitter 源表仍开放。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict actual emitter source table 证书。"""
    complete_key = load_json(
        DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
    )
    prepush = load_json(DOCS / "prime-matrix-prepushforward-emitter-origin-ledger-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    zero_seed = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    identity_taxonomy = load_json(
        DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.json"
    )
    constructor_firewall = load_json(
        DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
    )
    origin_admission = load_json(DOCS / "prime-matrix-clean-core-origin-source-admission-router.json")

    target = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
    next_basis = (
        "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter AND "
        "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND "
        "AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND "
        "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
    )
    rows = build_rows(
        complete_key=complete_key,
        prepush=prepush,
        source_loop=source_loop,
        zero_seed=zero_seed,
        identity_taxonomy=identity_taxonomy,
        constructor_firewall=constructor_firewall,
        origin_admission=origin_admission,
    )
    return {
        "certificate_type": "prime_matrix_strict_actual_emitter_source_table_router",
        "status": "strict_actual_emitter_source_table_reduced_to_precauchy_declaration_rows_identity_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "actual_emitter_source_table_router_closed": True,
        "source_table_field_decomposition_pinned": True,
        "source_loop_cut_imported": True,
        "zero_row_source_table_extraction_blocked": True,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "primitive_summand_emitter_formula_rows_proved": False,
        "alpha_delta_coefficient_identity_before_pushforward_proved": False,
        "source_table_no_downstream_recovery_return_ledger_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter",
        "field_law": (
            "The actual emitter source table is not a name for downstream payment data. Its first line must be a "
            "pre-Cauchy constructor declaration for the actual noncanonical emitter. Only after that declaration may "
            "one list primitive summand rows, prove the alpha/delta coefficient identity before pushforward, and attach "
            "return tags for over-budget, unregistered, thin, rejected or cancelling rows."
        ),
        "hard_law": (
            "若没有 pre-Cauchy declaration line，后面的 summand rows 都只是从 Gamma/覆盖图反推的后验标签；"
            "这正是来源环切断和早期零行 seed no-go 已排除的伪证明路径。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActualNoncanonicalPrimitiveEmitterSourceTableLedger` 没有被换成别的命题；它被拆成同一源表内部的四个字段："
            "`PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter`、"
            "`PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable`、"
            "`AlphaDeltaCoefficientIdentityBeforePushforwardLedger`、"
            "`SourceTableNoDownstreamRecoveryAndNamedReturnLedger`。当前最窄点是第一行 declaration，"
            "因为没有它，源表不能合法开始。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict actual emitter source table 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"actual_emitter_source_table_router_closed={fmt_bool(result['actual_emitter_source_table_router_closed'])}",
        f"source_table_field_decomposition_pinned={fmt_bool(result['source_table_field_decomposition_pinned'])}",
        f"pre_cauchy_constructor_declaration_line_proved={fmt_bool(result['pre_cauchy_constructor_declaration_line_proved'])}",
        f"primitive_summand_emitter_formula_rows_proved={fmt_bool(result['primitive_summand_emitter_formula_rows_proved'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(result['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"registered_complete_primitive_emitter_key_partition_polylog_proved={fmt_bool(result['registered_complete_primitive_emitter_key_partition_polylog_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 字段律",
        "",
        result["field_law"],
        "",
        "## 2. 硬约束",
        "",
        result["hard_law"],
        "",
        "## 3. 源表内部拆分",
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
        "## 4. 判定表",
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
            "## 5. 下一主攻点",
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
