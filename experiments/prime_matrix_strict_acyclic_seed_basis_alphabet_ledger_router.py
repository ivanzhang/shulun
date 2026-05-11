#!/usr/bin/env python3
"""生成 strict acyclic seed basis alphabet 账本攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_basis_alphabet_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.md"

TARGET = "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"
NEXT_TARGET = "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def word_generation_fields() -> list[dict[str, str]]:
    """列出 primitive basis word 生成规则必须提交的字段。"""
    return [
        {
            "field": "word_constructor",
            "meaning": "从 actual noncanonical seed/source tuple 正向生成 basis word 的规则。",
        },
        {
            "field": "admissible_word_predicate",
            "meaning": "判断 word 是否属于 pre-Cauchy basis alphabet 的算术条件。",
        },
        {
            "field": "word_to_row_anchor",
            "meaning": "word 到 carry-shell row、phase 和 primitive summand 的锚定。",
        },
        {
            "field": "scope_and_noncanonical_lock",
            "meaning": "排除 canonical scoped import、post-payment 选择和零行反推。",
        },
        {
            "field": "finite_complexity_bound",
            "meaning": "字母表复杂度、分支数和截断层数量的可收费上界。",
        },
        {
            "field": "missing_word_return",
            "meaning": "缺字母、未登记 word 或超预算 word 的命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 basis alphabet 账本的最小首字段。"""
    previous = data["previous"]
    constructor = data["constructor"]
    path_source = data["path_source"]
    origin = data["origin"]
    source_law = data["source_law"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    unsigned = data["unsigned"]
    explicit_rule = data["explicit_rule"]
    key_partition = data["key_partition"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    containers_closed = (
        formal_record.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    source_generation_open = (
        constructor.get("actual_noncanonical_primitive_constructor_formula_proved") is False
        or origin.get("clean_core_primitive_source_constructor_admission_proved") is not True
        or source_law.get("clean_core_original_coefficient_generation_ledger_proved") is not True
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        or reverse.get("pushforward_reverse_uniqueness_rejected") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
    )

    return [
        row(
            "BasisAlphabetTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已证明内部算术基展开首先缺 noncanonical pre-Cauchy basis alphabet。",
            TARGET,
        ),
        row(
            "AlphabetLedgerRequiresGeneratedWordSet",
            True,
            True,
            "字母表不是标签名集合；必须给出 actual seed 在 Cauchy 前正向生成的 basis word 集。",
            NEXT_TARGET,
        ),
        row(
            "ContainersDoNotGenerateWords",
            containers_closed,
            False,
            "formal unit/source tuple 只是容器；没有 word_constructor 和 admissible_word_predicate。",
            NEXT_TARGET,
        ),
        row(
            "SourceGenerationStillOpen",
            source_generation_open,
            False,
            "actual noncanonical primitive source constructor 与原始系数生成账本仍未证明，不能导出 basis word 集。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedPhaseAlphabetNotBasisWordSet",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
            and unsigned.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "unsigned phase wheel/carry-shell 字母是几何相位，不是带 signed local factor 的算术 basis word。",
            NEXT_TARGET,
        ),
        row(
            "ExplicitRuleAndKeyAreDownstream",
            explicit_rule.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False
            and key_partition.get("actual_noncanonical_primitive_emitter_source_table_proved") is False,
            False,
            "alpha/delta rule 和 complete key partition 都要求已存在 primitive basis words，不能倒置为字母表来源。",
            NEXT_TARGET,
        ),
        row(
            "ReverseRecoveryBlocked",
            reverse_blocked,
            True,
            "payment、推前后投影和早期零行覆盖不能反向选择 basis words，否则会形成后验循环。",
            NEXT_TARGET,
        ),
        row(
            "PrimitiveBasisWordSetGenerationRuleCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出 word_constructor、admissible predicate、row anchor、复杂度上界和缺字母回流。",
            NEXT_TARGET,
        ),
        row(
            "BasisAlphabetLedgerCurrentCorpusProved",
            False,
            False,
            "没有正向生成的 basis word 集，basis alphabet 账本仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 basis alphabet 账本证书。"""
    data = {
        "previous": load_json(
            "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"
        ),
        "constructor": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
        "path_source": load_json("prime-matrix-clean-core-path-source-firewall-router.json"),
        "origin": load_json("prime-matrix-clean-core-origin-source-admission-router.json"),
        "source_law": load_json("prime-matrix-clean-core-precauchy-source-law-atom-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "key_partition": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
        if isinstance(doc, dict)
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_basis_alphabet_ledger_router",
        "status": "acyclic_seed_basis_alphabet_reduced_to_generated_primitive_basis_word_set_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "acyclic_seed_basis_alphabet_ledger_router_closed": True,
        "alphabet_ledger_requires_generated_word_set": True,
        "formal_unit_source_tuple_containers_do_not_generate_words": True,
        "unsigned_phase_alphabet_not_basis_word_set": True,
        "explicit_rule_and_key_partition_are_downstream": True,
        "reverse_recovery_blocked": True,
        "primitive_basis_word_set_generation_rule_proved": False,
        "noncanonical_precauchy_basis_alphabet_ledger_proved": False,
        "acyclic_seed_internal_arithmetic_basis_expansion_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedBasisWordAdmissibilityPredicateLedger",
            "AcyclicSeedBasisWordFiniteComplexityBoundLedger",
            "AcyclicSeedMissingBasisWordNamedReturnLedger",
        ],
        "terminal_return_if_no_word_set_generation_rule": TERMINAL_RETURN,
        "word_generation_fields": word_generation_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 继续压缩为 `{NEXT_TARGET}`："
            "basis alphabet 账本的首要内容不是命名一个 alphabet，而是正向生成实际可用的 primitive basis word 集。"
            "容器、unsigned phase alphabet、下游 key partition 或 payment/零行反推都不能替代这个生成规则。"
        ),
        "plain_conclusion": (
            "本步继续保持同一个反例链目标，把 basis alphabet 账本压到 primitive basis word set generation rule。"
            "也就是说，下一步必须给出从 actual noncanonical seed/source tuple 到 basis word 的正向构造、准入谓词、"
            "row anchor、复杂度收费和缺字母回流；否则 signed coefficient assignment 仍无定义域。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed basis alphabet ledger 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_seed_basis_alphabet_ledger_router_closed={fmt_bool(result['acyclic_seed_basis_alphabet_ledger_router_closed'])}",
        f"primitive_basis_word_set_generation_rule_proved={fmt_bool(result['primitive_basis_word_set_generation_rule_proved'])}",
        f"noncanonical_precauchy_basis_alphabet_ledger_proved={fmt_bool(result['noncanonical_precauchy_basis_alphabet_ledger_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. word 生成规则字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["word_generation_fields"]:
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
            "",
            "并行依赖：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_word_set_generation_rule"],
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
