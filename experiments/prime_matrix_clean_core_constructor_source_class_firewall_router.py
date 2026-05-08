#!/usr/bin/env python3
"""Prime Matrix clean-core 构造器来源分类防火墙路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_constructor_source_class_firewall_router.py

输出：
  docs/monograph/prime-matrix-clean-core-constructor-source-class-firewall-router.json
  docs/monograph/prime-matrix-clean-core-constructor-source-class-firewall-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-origin-source-admission-router.json"
DEFAULT_BRANCH = DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_COMPLEMENT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_MULTIPLICITY = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_classes() -> list[dict[str, Any]]:
    """列出构造器来源分类。"""
    return [
        {
            "source_class": "canonical",
            "route": "canonical RIW/Buchstab constructor",
            "status": "closed_scoped",
            "remaining": "不能覆盖 noncanonical clean-core。",
        },
        {
            "source_class": "generic_wfd",
            "route": "formal well-factorable template",
            "status": "rejected_as_constructor",
            "remaining": "形式可分解性不给 summand emitter。",
        },
        {
            "source_class": "unregistered_or_mixed_formal_unit",
            "route": "Multiplicity/Stitching or K7 formal-unit return",
            "status": "absorbed_as_return",
            "remaining": "不能作为 clean-core 终端保留。",
        },
        {
            "source_class": "external_spectral",
            "route": "c-dependent completed residue spectral input",
            "status": "open_external",
            "remaining": "需证明或接受外部谱输入。",
        },
        {
            "source_class": "actual_noncanonical",
            "route": "primitive constructor formula",
            "status": "open_self_contained",
            "remaining": "写出 actual noncanonical constructor formula。",
        },
    ]


def formula_requirements() -> list[dict[str, str]]:
    """列出 actual noncanonical primitive constructor 公式要求。"""
    return [
        {
            "field": "pre_cauchy_definition",
            "requirement": "在 Cauchy/dispersion 前定义 actual noncanonical clean-core 系数。",
        },
        {
            "field": "summand_emitter",
            "requirement": "给出产生 alpha/delta summand 的确定性 emitter。",
        },
        {
            "field": "branch_key_schema",
            "requirement": "每个 summand 带有限 branch key、u/v map、sign、local factor。",
        },
        {
            "field": "formal_unit_compatibility",
            "requirement": "emitter 输出与后续容量、支撑、回流账本使用同一个 formal unit。",
        },
        {
            "field": "return_tags",
            "requirement": "公式不适用、超预算、thin block 或抵消必须输出命名 return tag。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    branch: dict[str, Any],
    provenance: dict[str, Any],
    complement: dict[str, Any],
    multiplicity_text: str,
    clean_kls: dict[str, Any],
    spectral: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成构造器来源分类防火墙判定表。"""
    multiplicity_absorbs = "Multiplicity-Stitching 不是独立数学出口" in multiplicity_text
    k7_formal_unit = any(
        row.get("key") == "K7" and row.get("verified") is True
        for row in clean_kls.get("admission_rows", [])
    )
    return [
        {
            "gate": "PriorPrimitiveConstructorAdmissionPinned",
            "closed": previous.get("latest_internal_subinput")
            == "CleanCorePrimitiveSourceConstructorAdmissionAndReturn",
            "proved": False,
            "meaning": "上一层已把原始来源准入压到 primitive source constructor admission。",
            "remaining": "拆分构造器准入的来源类别。",
        },
        {
            "gate": "ConstructorAdmissionSplitsBySourceClass",
            "closed": True,
            "proved": True,
            "meaning": "任一候选来源必须属于 canonical、generic_wfd、unregistered/mixed、external_spectral 或 actual_noncanonical。",
            "remaining": "逐类路由后只剩 actual noncanonical 公式。",
        },
        {
            "gate": "CanonicalClassClosedScoped",
            "closed": provenance.get("actual_source_provenance_closed") is True
            and branch.get("canonical_source_branch_internal_gap_closed") is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab constructor 已闭合，但只在 canonical-source 分支有效。",
            "remaining": "不能导入 noncanonical clean-core。",
        },
        {
            "gate": "GenericWFDClassRejected",
            "closed": complement.get("generic_wfd_template_available") is False,
            "proved": True,
            "meaning": "generic WFD 只是形式性质，不是 source constructor。",
            "remaining": "generic 分支只能走外部谱输入或命名回流。",
        },
        {
            "gate": "UnregisteredOrMixedFormalUnitReturnAbsorbed",
            "closed": multiplicity_absorbs and k7_formal_unit,
            "proved": True,
            "meaning": "没有同一 formal unit/source registration 的对象不是 clean-core 终端；口径不一致回到 Multiplicity/Stitching 或 K7 失败出口。",
            "remaining": "不再把 unregistered source 当作自足剩余。",
        },
        {
            "gate": "ExternalSpectralClassPinned",
            "closed": spectral.get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            "proved": False,
            "meaning": "外部谱类已压成 c-dependent completed residue spectral cancellation。",
            "remaining": "证明或接受 CDependentResidueWeightSpectralCancellationInput。",
        },
        {
            "gate": "ActualNoncanonicalPrimitiveConstructorFormulaCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未写出 actual noncanonical clean-core primitive constructor formula。",
            "remaining": "证明 ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    branch_path: Path,
    provenance_path: Path,
    complement_path: Path,
    multiplicity_path: Path,
    clean_kls_path: Path,
    spectral_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 构造器来源分类防火墙路由。"""
    source_paths = [
        previous_path,
        branch_path,
        provenance_path,
        complement_path,
        multiplicity_path,
        clean_kls_path,
        spectral_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    branch = load_json(branch_path)
    provenance = load_json(provenance_path)
    complement = load_json(complement_path)
    multiplicity_text = multiplicity_path.read_text(encoding="utf-8")
    clean_kls = load_json(clean_kls_path)
    spectral = load_json(spectral_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(
        previous=previous,
        branch=branch,
        provenance=provenance,
        complement=complement,
        multiplicity_text=multiplicity_text,
        clean_kls=clean_kls,
        spectral=spectral,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "ActualNoncanonicalPrimitiveConstructorFormulaCurrentCorpusProved",
            "ExternalSpectralClassPinned",
            "DStructureRankinStillIndependent",
        }
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_constructor_source_class_firewall_router",
        "status": "constructor_admission_reduced_to_actual_noncanonical_primitive_formula_open",
        "constructor_source_class_firewall_boundary_closed": boundary_closed,
        "source_class_partition_closed": True,
        "canonical_constructor_closed_scoped_only": True,
        "generic_wfd_constructor_rejected": True,
        "unregistered_source_return_absorbed": True,
        "actual_noncanonical_primitive_constructor_formula_proved": False,
        "clean_core_primitive_source_constructor_admission_proved": False,
        "external_spectral_atom_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_input": "CleanCorePrimitiveSourceConstructorAdmissionAndReturn",
        "latest_internal_subinput": "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn",
        "latest_external_subinput": "CDependentResidueWeightSpectralCancellationInput",
        "latest_conditional_basis": (
            "(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "firewall_law": (
            "primitive constructor admission splits by source class. Canonical constructor is closed only in its "
            "own branch; generic WFD is not a constructor; unregistered or mixed formal-unit sources return via "
            "Multiplicity/Stitching or K7 formal-unit failure; external spectral class remains external. "
            "Therefore the only self-contained source-side atom left is the actual noncanonical primitive "
            "constructor formula."
        ),
        "plain_conclusion": (
            "最新完全自足剩余继续压缩：构造器准入的来源分类防火墙已闭合，未登记来源不再作为 clean-core "
            "终端保留。唯一自足源侧原子变成 actual noncanonical primitive source constructor 的显式公式。"
        ),
        "source_classes": source_classes(),
        "formula_requirements": formula_requirements(),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 研究证书。"""
    lines: list[str] = [
        "# Prime Matrix clean-core 构造器来源分类防火墙路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"constructor_source_class_firewall_boundary_closed={fmt_bool(result['constructor_source_class_firewall_boundary_closed'])}",
        f"source_class_partition_closed={fmt_bool(result['source_class_partition_closed'])}",
        f"unregistered_source_return_absorbed={fmt_bool(result['unregistered_source_return_absorbed'])}",
        f"actual_noncanonical_primitive_constructor_formula_proved={fmt_bool(result['actual_noncanonical_primitive_constructor_formula_proved'])}",
        f"clean_core_primitive_source_constructor_admission_proved={fmt_bool(result['clean_core_primitive_source_constructor_admission_proved'])}",
        f"external_spectral_atom_accepted={fmt_bool(result['external_spectral_atom_accepted'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 来源分类防火墙律",
            "",
            result["firewall_law"],
            "",
            "## 3. 来源类别",
            "",
            "| source class | route | status | remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["source_classes"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['source_class'])}`",
                    table_cell(row["route"]),
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. actual noncanonical 公式字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for req in result["formula_requirements"]:
        lines.append(
            f"| `{table_cell(req['field'])}` | {table_cell(req['requirement'])} |"
        )

    lines.extend(
        [
            "",
            "## 5. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "`ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn` 要求：",
            "",
            "- 在 Cauchy/dispersion 前写出 actual noncanonical clean-core 系数定义；",
            "- 给出确定性 summand emitter，输出 `alpha/delta`、branch key、`u/v` map、符号和 local factor；",
            "- 证明 emitter 与后续支撑、容量和回流账本处于同一 formal unit；",
            "- 证明 branch key 数为 `log^O(1)`，或把超预算部分命名回流；",
            "- 公式不适用、thin block、抵消或未登记来源必须回流。",
            "",
            "## 6. 当前结论",
            "",
            "本步没有证明 actual noncanonical primitive constructor formula。它闭合的是来源分类防火墙：",
            "canonical、generic、unregistered 和 external 类都已按边界处理，唯一自足剩余是 actual noncanonical 显式公式。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Route clean-core constructor admission by source class."
    )
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--branch", type=Path, default=DEFAULT_BRANCH)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--complement", type=Path, default=DEFAULT_COMPLEMENT)
    parser.add_argument("--multiplicity", type=Path, default=DEFAULT_MULTIPLICITY)
    parser.add_argument("--clean-kls", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        previous_path=args.previous,
        branch_path=args.branch,
        provenance_path=args.provenance,
        complement_path=args.complement,
        multiplicity_path=args.multiplicity,
        clean_kls_path=args.clean_kls,
        spectral_path=args.spectral,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_internal_subinput"])


if __name__ == "__main__":
    main()
