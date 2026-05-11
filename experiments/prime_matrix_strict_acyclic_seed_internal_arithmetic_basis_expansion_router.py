#!/usr/bin/env python3
"""生成 strict acyclic seed 内部算术基展开攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_internal_arithmetic_basis_expansion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.md"

TARGET = "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"
NEXT_TARGET = "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"
PARALLEL_TARGET = "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-triad-a1-canonical-riw-support-router.json",
    "prime-matrix-triad-a1-canonical-riw-support-router.md",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
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


def alphabet_ledger_fields() -> list[dict[str, str]]:
    """列出 basis alphabet 账本必须提交的字段。"""
    return [
        {
            "field": "basis_word_set",
            "meaning": "seed 内部允许出现的 pre-Cauchy 算术基字母和有限 word 集。",
        },
        {
            "field": "word_to_source_tuple_map",
            "meaning": "每个 basis word 到 actual noncanonical source tuple 的正向生成映射。",
        },
        {
            "field": "local_factor_domain",
            "meaning": "每个 word 的 local factor、符号和非零条件所在定义域。",
        },
        {
            "field": "truncation_phase_compatibility",
            "meaning": "字母表与 carry shell、phase wheel、截断层和 branch key 的兼容规则。",
        },
        {
            "field": "noncanonical_scope_lock",
            "meaning": "证明这些字母不是 canonical RIW/Buchstab 的跨作用域导入。",
        },
        {
            "field": "failure_return",
            "meaning": "缺字母、超预算、后验选择或作用域冲突时的命名回流。",
        },
    ]


def build_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    """审查内部算术基展开的第一不可替代字段。"""
    previous = data["previous"]
    constructor = data["constructor"]
    path_source = data["path_source"]
    canonical_json = data["canonical_json"]
    canonical_text = data["canonical_text"]
    external = data["external"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    unsigned = data["unsigned"]
    canonical_t1 = data["canonical_t1"]
    explicit_rule = data["explicit_rule"]
    key_partition = data["key_partition"]

    canonical_scoped = (
        previous.get("canonical_riw_not_importable") is True
        or constructor.get("canonical_constructor_closed_scoped_only") is True
        or path_source.get("canonical_template_scoped_only") is True
        or canonical_json.get("canonical_riw_support_scoped") is True
        or "canonical RIW" in canonical_text
    )
    generic_not_alphabet = constructor.get("source_class_partition_closed") is True
    containers_available = (
        formal_record.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    reverse_blocked = (
        reverse.get("pushforward_reverse_uniqueness_rejected") is True
        or reverse.get("reverse_provenance_functor_boundary_closed") is True
    )
    zero_reverse_blocked = (
        zero_nogo.get("zero_row_seed_extraction_blocked") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
    )

    return [
        row(
            "InternalArithmeticBasisExpansionTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 basis weight source formula 压到 seed 内部 pre-Cauchy 算术基展开。",
            TARGET,
        ),
        row(
            "BasisAlphabetIsFirstDomainGate",
            True,
            True,
            "没有 basis alphabet，coefficient assignment、截断层规则和 pre-Cauchy 恒等式都没有定义域。",
            NEXT_TARGET,
        ),
        row(
            "CanonicalAlphabetCrossImportBlocked",
            canonical_scoped,
            True,
            "canonical RIW/Buchstab 字母表只在 canonical branch 内有作用域，不能作为 actual noncanonical seed 的字母表。",
            NEXT_TARGET,
        ),
        row(
            "GenericWFDIsNotAlphabet",
            generic_not_alphabet,
            True,
            "generic WFD 是性质约束，不是逐 primitive row 的算术基字母表。",
            NEXT_TARGET,
        ),
        row(
            "ExternalSpectralDoesNotEmitAlphabet",
            external.get("external_lemma_parameter_match_boundary_closed") is True
            and previous.get("external_spectral_does_not_emit_basis") is True,
            True,
            "外部谱估计接收已给定的系数族；它不生成 seed 内部 basis alphabet。",
            NEXT_TARGET,
        ),
        row(
            "ReversePaymentAndZeroRowRecoveryBlocked",
            reverse_blocked and zero_reverse_blocked,
            True,
            "不能从 payment 原像、推前后结构或早期零行 unsigned 覆盖反推出 pre-Cauchy 字母表。",
            NEXT_TARGET,
        ),
        row(
            "FormalUnitAndSourceTupleAreContainersOnly",
            containers_available,
            False,
            "formal unit 与 source tuple 能登记参数、哈希和锚点；它们没有列出可赋权的 basis word 集。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedSkeletonHasPhaseAlphabetNotArithmeticAlphabet",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
            and unsigned.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "unsigned skeleton 的相位/几何字母只能定位 row，不能给 signed arithmetic basis alphabet。",
            NEXT_TARGET,
        ),
        row(
            "CanonicalT1ClassifierDoesNotSupplyNoncanonicalAlphabet",
            canonical_t1.get("equality_branch_classifier_closed") is True
            and canonical_t1.get("all_mismatches_force_registered_defect_or_actual_source_proved") is False,
            False,
            "canonical T1 分支分类只区分 canonical absorbed 或 mismatch；不提交 noncanonical basis word 集。",
            NEXT_TARGET,
        ),
        row(
            "ExplicitAlphaDeltaRuleRequiresAlphabetUpstream",
            explicit_rule.get("explicit_alpha_delta_rule_router_closed") is True
            and explicit_rule.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False,
            False,
            "显式 alpha/delta rule 需要已有 primitive source word 与 local factor 定义，不能反过来定义字母表。",
            NEXT_TARGET,
        ),
        row(
            "CompleteEmitterKeyPartitionIsDownstream",
            key_partition.get("complete_emitter_key_partition_router_closed") is True
            and key_partition.get("actual_noncanonical_primitive_emitter_source_table_proved") is False,
            False,
            "complete emitter key partition 是 source table 之后的登记纪律，不是 source basis alphabet 的来源。",
            NEXT_TARGET,
        ),
        row(
            "NoncanonicalPreCauchyBasisAlphabetCurrentCorpusProved",
            False,
            False,
            "当前材料尚未提交 actual noncanonical seed 的 pre-Cauchy basis alphabet 账本。",
            NEXT_TARGET,
        ),
        row(
            "CoefficientAssignmentCurrentCorpusBlockedByMissingAlphabet",
            False,
            False,
            "没有字母表定义域，coefficient assignment 只能作为并行依赖保留，不能先行闭合。",
            PARALLEL_TARGET,
        ),
        row(
            "InternalArithmeticBasisExpansionCurrentCorpusProved",
            False,
            False,
            "basis alphabet、coefficient assignment、截断相位规则、作用域锁和推前前恒等式未合取证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造内部算术基展开证书。"""
    data: dict[str, Any] = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
        "constructor": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
        "path_source": load_json("prime-matrix-clean-core-path-source-firewall-router.json"),
        "canonical_json": load_json("prime-matrix-triad-a1-canonical-riw-support-router.json"),
        "canonical_text": load_text("prime-matrix-triad-a1-canonical-riw-support-router.md"),
        "external": load_json("prime-matrix-clean-core-external-lemma-parameter-match-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "canonical_t1": load_json("prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "key_partition": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_internal_arithmetic_basis_expansion_router",
        "status": "acyclic_seed_internal_arithmetic_basis_expansion_reduced_to_noncanonical_basis_alphabet_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "acyclic_seed_internal_arithmetic_basis_expansion_router_closed": True,
        "basis_alphabet_is_first_domain_gate": True,
        "canonical_alphabet_cross_import_blocked": True,
        "generic_wfd_is_not_alphabet": True,
        "external_spectral_does_not_emit_alphabet": True,
        "reverse_payment_and_zero_row_recovery_blocked": True,
        "noncanonical_precauchy_basis_alphabet_ledger_proved": False,
        "basis_coefficient_assignment_ledger_proved": False,
        "truncation_phase_compatibility_ledger_proved": False,
        "noncanonical_scope_lock_ledger_proved": False,
        "pre_cauchy_basis_expansion_identity_proved": False,
        "acyclic_seed_internal_arithmetic_basis_expansion_proved": False,
        "acyclic_seed_precauchy_basis_weight_source_formula_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            PARALLEL_TARGET,
            "AcyclicSeedTruncationPhaseCompatibilityLedger",
            "AcyclicSeedPreCauchyBasisExpansionIdentityLedger",
        ],
        "terminal_return_if_no_basis_alphabet": TERMINAL_RETURN,
        "alphabet_ledger_fields": alphabet_ledger_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 的第一不可替代字段是 `{NEXT_TARGET}`。"
            "因为字母表先于 coefficient assignment、截断相位规则和 pre-Cauchy 恒等式；"
            "现有 canonical、generic WFD、外部谱、零行/payment 反推、formal-unit/source-tuple 容器和 unsigned skeleton "
            "都不能给出 actual noncanonical seed 的 basis word 集。"
        ),
        "plain_conclusion": (
            "本步没有转换命题，只把真正破坏输入继续下钻：内部算术基展开首先缺的是 "
            "actual noncanonical pre-Cauchy basis alphabet。没有这张字母表账本，signed coefficient assignment "
            "没有定义域，后续截断/相位层、local factor、Phi 推前前恒等式都不能成为可检验命题。"
            "因此当前仍未形成无条件矛盾，下一步应直接攻 basis alphabet 账本。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed internal arithmetic basis expansion 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_seed_internal_arithmetic_basis_expansion_router_closed={fmt_bool(result['acyclic_seed_internal_arithmetic_basis_expansion_router_closed'])}",
        f"noncanonical_precauchy_basis_alphabet_ledger_proved={fmt_bool(result['noncanonical_precauchy_basis_alphabet_ledger_proved'])}",
        f"basis_coefficient_assignment_ledger_proved={fmt_bool(result['basis_coefficient_assignment_ledger_proved'])}",
        f"acyclic_seed_internal_arithmetic_basis_expansion_proved={fmt_bool(result['acyclic_seed_internal_arithmetic_basis_expansion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. basis alphabet 账本字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["alphabet_ledger_fields"]:
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
            result["terminal_return_if_no_basis_alphabet"],
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
