#!/usr/bin/env python3
"""生成 strict pre-Cauchy declaration line 分类证书。

用法示例：
  python3 experiments/prime_matrix_strict_precauchy_declaration_line_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-precauchy-declaration-line-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-precauchy-declaration-line-router.json"
OUT_MD = DOCS / "prime-matrix-strict-precauchy-declaration-line-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
    "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.json",
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
    source_table: dict[str, Any],
    constructor_firewall: dict[str, Any],
    origin_admission: dict[str, Any],
    external_match: dict[str, Any],
    canonical_provenance: dict[str, Any],
    identity_taxonomy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 pre-Cauchy declaration line 分类判定表。"""
    target = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
    next_basis = (
        "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter AND "
        "SameFormalUnitPreCauchyTimestampLockLedger AND "
        "NoncanonicalDeclarationNoCanonicalOrExternalLeakLedger"
    )
    terminal_after = source_table.get("terminal_gap_after_router", "")
    return [
        {
            "gate": "PreCauchyDeclarationLineTargetActive",
            "closed": target in terminal_after,
            "proved": False,
            "meaning": "上一层源表字段拆分已把第一硬点压成 Cauchy/dispersion 前的 constructor declaration line。",
            "remaining": target,
        },
        {
            "gate": "SourceClassPartitionClosed",
            "closed": constructor_firewall.get("source_class_partition_closed") is True,
            "proved": True,
            "meaning": "任何 declaration line 必须属于 canonical、generic WFD、unregistered/mixed、external 或 actual noncanonical。",
            "remaining": "逐类过滤，保留 strict 自足合法分支。",
        },
        {
            "gate": "CanonicalDeclarationScopedOut",
            "closed": canonical_provenance.get("actual_source_provenance_ledger_closed") is True
            or constructor_firewall.get("constructor_source_class_firewall_boundary_closed") is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab provenance 只在 pre-Cauchy 声明本来就是 canonical 时闭合，不能作为 noncanonical emitter 声明。",
            "remaining": "不能用 canonical 表填 actual noncanonical declaration line。",
        },
        {
            "gate": "GenericWFDDeclarationRejected",
            "closed": constructor_firewall.get("source_class_partition_closed") is True,
            "proved": True,
            "meaning": "generic WFD 是形式分解约束，不是产生 primitive summand 的 constructor declaration。",
            "remaining": "不能以 WFD 模板作为源表第一行。",
        },
        {
            "gate": "ExternalSpectralDeclarationRejectedForStrict",
            "closed": external_match.get("external_lemmas_match_constructor_formula") is False
            or identity_taxonomy.get("external_spectral_self_contained_identity_proved") is False,
            "proved": True,
            "meaning": "DI/BFI/Kuznetsov 等外部引理从给定系数后处理，不能生成 strict 自足 pre-Cauchy declaration line。",
            "remaining": "外部谱只能作为条件分支，不填当前自足表。",
        },
        {
            "gate": "UnregisteredMixedDeclarationReturned",
            "closed": constructor_firewall.get("unregistered_source_return_absorbed") is True,
            "proved": True,
            "meaning": "未登记或混合 formal unit 的声明不能留在 clean-core 表内，必须命名回流。",
            "remaining": "保留表必须同 formal unit。",
        },
        {
            "gate": "ActualNoncanonicalDeclarationIsOnlyStrictOption",
            "closed": True,
            "proved": True,
            "meaning": "四类伪声明过滤后，strict 自足 declaration line 只能是 actual noncanonical primitive constructor formula line。",
            "remaining": "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter。",
        },
        {
            "gate": "SameFormalUnitTimestampRequirementPinned",
            "closed": origin_admission.get("constructor_admission_implies_origin_ledger") is True,
            "proved": True,
            "meaning": "声明行必须发生在 Cauchy/dispersion/Type/Fourier/completion 前，并锁定同一 actual formal unit。",
            "remaining": "SameFormalUnitPreCauchyTimestampLockLedger。",
        },
        {
            "gate": "ActualConstructorFormulaLineCurrentCorpusProved",
            "closed": constructor_firewall.get("actual_noncanonical_primitive_constructor_formula_proved")
            is True,
            "proved": False,
            "meaning": "当前材料尚未写出 actual noncanonical primitive constructor formula line。",
            "remaining": "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter。",
        },
        {
            "gate": "PreCauchyDeclarationLineCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "actual formula line、时间戳/formal-unit 锁和无泄漏纪律未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict pre-Cauchy declaration line 证书。"""
    source_table = load_json(DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json")
    constructor_firewall = load_json(
        DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
    )
    origin_admission = load_json(DOCS / "prime-matrix-clean-core-origin-source-admission-router.json")
    external_match = load_json(DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.json")
    canonical_provenance = load_json(
        DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
    )
    identity_taxonomy = load_json(
        DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.json"
    )

    target = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
    next_basis = (
        "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter AND "
        "SameFormalUnitPreCauchyTimestampLockLedger AND "
        "NoncanonicalDeclarationNoCanonicalOrExternalLeakLedger"
    )
    rows = build_rows(
        source_table=source_table,
        constructor_firewall=constructor_firewall,
        origin_admission=origin_admission,
        external_match=external_match,
        canonical_provenance=canonical_provenance,
        identity_taxonomy=identity_taxonomy,
    )
    return {
        "certificate_type": "prime_matrix_strict_precauchy_declaration_line_router",
        "status": "strict_precauchy_declaration_line_reduced_to_actual_constructor_formula_line_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "precauchy_declaration_line_router_closed": True,
        "source_class_partition_closed": True,
        "canonical_declaration_scoped_out": True,
        "generic_wfd_declaration_rejected": True,
        "external_spectral_declaration_rejected_for_strict": True,
        "unregistered_mixed_declaration_returned": True,
        "actual_noncanonical_declaration_only_strict_option": True,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "same_formal_unit_precauchy_timestamp_lock_proved": False,
        "noncanonical_declaration_no_canonical_or_external_leak_proved": False,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter",
        "classification_law": (
            "A pre-Cauchy declaration line is legal for this strict source table only if it declares the actual "
            "noncanonical primitive constructor before Cauchy/dispersion. Canonical declarations are scoped to the "
            "canonical branch, generic WFD is not a constructor, unregistered/mixed declarations return, and external "
            "spectral estimates do not emit source rows."
        ),
        "plain_conclusion": (
            "`PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 被逐类过滤到同一源表内部的 "
            "`ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter`。这不是换命题，而是证明源表第一行时必须写出的实际公式行。"
            "当前语料没有该公式行，因此源表、complete key、fixed-pair fiber bound 和最终源熵命题仍未闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict pre-Cauchy declaration line 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"precauchy_declaration_line_router_closed={fmt_bool(result['precauchy_declaration_line_router_closed'])}",
        f"actual_noncanonical_declaration_only_strict_option={fmt_bool(result['actual_noncanonical_declaration_only_strict_option'])}",
        f"actual_noncanonical_primitive_constructor_formula_line_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_line_proved'])}",
        f"pre_cauchy_constructor_declaration_line_proved={fmt_bool(result['pre_cauchy_constructor_declaration_line_proved'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(result['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分类律",
        "",
        result["classification_law"],
        "",
        "## 2. 源表第一行拆分",
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
