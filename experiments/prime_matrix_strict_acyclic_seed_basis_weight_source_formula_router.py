#!/usr/bin/env python3
"""生成 strict acyclic seed basis weight source formula 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_basis_weight_source_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.md"

TARGET = "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"
NEXT_TARGET = "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-triad-a1-canonical-riw-support-router.md",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
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


def basis_expansion_fields() -> list[dict[str, str]]:
    """列出内部算术基展开的必要字段。"""
    return [
        {
            "field": "basis_alphabet",
            "meaning": "seed 内部允许的 pre-Cauchy 算术基函数/筛权字母表。",
        },
        {
            "field": "coefficient_assignment",
            "meaning": "每个 basis word 到 primitive row signed coefficient 的赋值公式。",
        },
        {
            "field": "truncation_layer_rule",
            "meaning": "截断层、相位层和 branch layer 的确定性规则。",
        },
        {
            "field": "noncanonical_scope_certificate",
            "meaning": "证明该展开属于 actual noncanonical seed，不偷用 canonical RIW/Buchstab。",
        },
        {
            "field": "pre_cauchy_identity",
            "meaning": "展开在 Cauchy/dispersion/Phi 前已经等于目标 alpha/delta 系数。",
        },
        {
            "field": "failure_return",
            "meaning": "缺字母、零赋值、作用域冲突或超预算时命名回流。",
        },
    ]


def build_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    """审查 basis weight source formula 的真正原子。"""
    previous = data["previous"]
    constructor_firewall = data["constructor_firewall"]
    path_source = data["path_source"]
    canonical_text = data["canonical_text"]
    external = data["external"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    unsigned = data["unsigned"]

    canonical_scoped = (
        path_source.get("canonical_template_scoped_only") is True
        or "canonical RIW" in canonical_text
        or "canonical-source" in canonical_text
    )
    generic_blocked = (
        constructor_firewall.get("constructor_source_class_firewall_boundary_closed") is True
        and constructor_firewall.get("actual_noncanonical_primitive_constructor_formula_proved") is False
    )

    return [
        row(
            "BasisWeightSourceTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 primitive coefficient law 压到 seed 内部 basis weight source formula。",
            TARGET,
        ),
        row(
            "BasisSourceRequiresInternalArithmeticExpansion",
            True,
            True,
            "basis weight source 不能只是 source tuple 字段名；必须给出 seed 内部 pre-Cauchy 算术基展开。",
            NEXT_TARGET,
        ),
        row(
            "CanonicalRIWNotImportable",
            canonical_scoped,
            True,
            "canonical RIW/Buchstab 只在 canonical-source 分支内有作用域，不能跨入 actual noncanonical seed。",
            NEXT_TARGET,
        ),
        row(
            "GenericWFDNotBasisSource",
            generic_blocked,
            True,
            "generic WFD 或形式 well-factorable 条件不是 primitive row 的原始 basis weight source。",
            NEXT_TARGET,
        ),
        row(
            "ExternalSpectralDoesNotEmitBasis",
            external.get("external_lemmas_match_constructor_formula") is False,
            True,
            "外部谱估计处理给定系数后的平均，不生成 seed 内部 basis expansion。",
            NEXT_TARGET,
        ),
        row(
            "ZeroRowAndPaymentReverseBlocked",
            zero_nogo.get("zero_row_seed_extraction_blocked") is True
            and reverse.get("pushforward_reverse_uniqueness_rejected") is True,
            True,
            "早期零行覆盖和 payment 原像都不能反向产生 basis expansion。",
            NEXT_TARGET,
        ),
        row(
            "FormalUnitSourceTupleContainersInsufficient",
            formal_record.get("formal_unit_source_record_schema_closed") is True
            and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True,
            False,
            "formal-unit/source-tuple 容器只给参数与哈希，不给 basis alphabet 或 coefficient assignment。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedSkeletonInsufficientForBasisExpansion",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            False,
            "unsigned row skeleton 可定位候选几何行，但不定义 seed 的算术基展开。",
            NEXT_TARGET,
        ),
        row(
            "AcyclicSeedInternalArithmeticBasisExpansionCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 actual noncanonical seed 的内部 pre-Cauchy 算术基展开。",
            NEXT_TARGET,
        ),
        row(
            "BasisWeightSourceFormulaCurrentCorpusProved",
            False,
            False,
            "没有内部算术基展开，basis weight source formula 仍未证明。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 basis weight source formula 证书。"""
    data: dict[str, Any] = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "constructor_firewall": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
        "path_source": load_json("prime-matrix-clean-core-path-source-firewall-router.json"),
        "canonical_text": load_text("prime-matrix-triad-a1-canonical-riw-support-router.md"),
        "external": load_json("prime-matrix-clean-core-external-lemma-parameter-match-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_basis_weight_source_formula_router",
        "status": "acyclic_seed_basis_weight_source_reduced_to_internal_arithmetic_basis_expansion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "acyclic_seed_basis_weight_source_formula_router_closed": True,
        "basis_source_requires_internal_arithmetic_expansion": True,
        "canonical_riw_not_importable": True,
        "generic_wfd_not_basis_source": True,
        "external_spectral_does_not_emit_basis": True,
        "acyclic_seed_internal_arithmetic_basis_expansion_proved": False,
        "acyclic_seed_precauchy_basis_weight_source_formula_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "terminal_return_if_no_basis_expansion": TERMINAL_RETURN,
        "basis_expansion_fields": basis_expansion_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 不能从 canonical、generic WFD、外部谱、零行覆盖、payment 原像或 source tuple 容器导出；"
            f"它必须提交 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把 basis weight source formula 继续压到 seed 内部 pre-Cauchy 算术基展开。"
            "这张展开必须给出 basis alphabet、coefficient assignment、截断/相位层规则、noncanonical 作用域证书、"
            "推前前恒等式和失败回流。当前材料没有该内部基展开，因此当前仍只是更精确地定位破坏输入，"
            "还没有形成无条件矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed basis weight source formula 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_seed_basis_weight_source_formula_router_closed={fmt_bool(result['acyclic_seed_basis_weight_source_formula_router_closed'])}",
        f"acyclic_seed_internal_arithmetic_basis_expansion_proved={fmt_bool(result['acyclic_seed_internal_arithmetic_basis_expansion_proved'])}",
        f"acyclic_seed_precauchy_basis_weight_source_formula_proved={fmt_bool(result['acyclic_seed_precauchy_basis_weight_source_formula_proved'])}",
        f"acyclic_seed_primitive_row_signed_coefficient_law_proved={fmt_bool(result['acyclic_seed_primitive_row_signed_coefficient_law_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 内部算术基展开字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["basis_expansion_fields"]:
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
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_basis_expansion"],
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
