#!/usr/bin/env python3
"""Prime Matrix clean-core 原始来源准入路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_origin_source_admission_router.py

输出：
  docs/monograph/prime-matrix-clean-core-origin-source-admission-router.json
  docs/monograph/prime-matrix-clean-core-origin-source-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json"
DEFAULT_SOURCE_LOCK = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_BRANCH = DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_COMPLEMENT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_PACKET_RETURN = DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-origin-source-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-origin-source-admission-router.md"


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


def constructor_requirements() -> list[dict[str, str]]:
    """列出原始来源构造器准入所需字段。"""
    return [
        {
            "field": "source_constructor",
            "requirement": "在 Cauchy/dispersion 前声明系数由哪个原始构造器生成。",
            "why": "没有构造器就没有可审查的 summand 表。",
        },
        {
            "field": "formal_unit_id",
            "requirement": "构造器输出必须落在同一个 actual formal unit。",
            "why": "避免把不同口径的系数拼成一张伪账本。",
        },
        {
            "field": "branch_admission",
            "requirement": "标明 canonical、noncanonical actual、external spectral 或 named return。",
            "why": "canonical 账本不能跨分支导入，generic WFD 不能冒充来源。",
        },
        {
            "field": "emitted_summand_schema",
            "requirement": "给出 summand、branch key、u/v map、符号和 local factor 的生成规则。",
            "why": "该 schema 才能展开成原始生成账本。",
        },
        {
            "field": "failure_return_tag",
            "requirement": "构造器缺失、口径冲突、超预算或 thin block 必须带回流标签。",
            "why": "未登记来源不能成为新的隐藏终端。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    source_lock: dict[str, Any],
    branch: dict[str, Any],
    provenance: dict[str, Any],
    complement: dict[str, Any],
    packet_return: dict[str, Any],
    spectral: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成原始来源准入判定表。"""
    return [
        {
            "gate": "PriorOriginGenerationLedgerPinned",
            "closed": previous.get("latest_internal_subinput")
            == "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
            "proved": False,
            "meaning": "上一层已把 pre-Cauchy 来源律压到 actual 原始生成账本。",
            "remaining": "继续判断生成账本最小入口是什么。",
        },
        {
            "gate": "OriginLedgerNeedsSourceConstructorAdmission",
            "closed": True,
            "proved": True,
            "meaning": "一张 summand 表必须先有 pre-Cauchy 原始构造器；否则无法审查其来源。",
            "remaining": "证明 clean-core 候选都有合法构造器，或未登记来源回流。",
        },
        {
            "gate": "ConstructorAdmissionImpliesOriginLedger",
            "closed": True,
            "proved": True,
            "meaning": "若构造器准入并给出 emitted summand schema，原始生成账本由有限展开得到。",
            "remaining": "该推出不证明 clean-core 构造器存在。",
        },
        {
            "gate": "CanonicalConstructorAlreadyScoped",
            "closed": provenance.get("actual_source_provenance_closed") is True
            and branch.get("canonical_source_branch_internal_gap_closed") is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 构造器已闭合，但只在 canonical-source 分支内有效。",
            "remaining": "noncanonical clean-core 不能使用该构造器偷渡。",
        },
        {
            "gate": "GenericWFDNotAConstructor",
            "closed": source_lock.get("source_lock_contract_closed_for_canonical_branch") is True
            and complement.get("generic_wfd_template_available") is False,
            "proved": True,
            "meaning": "well-factorable 性质是形式约束，不是生成 summand 的原始构造器。",
            "remaining": "必须提交 actual noncanonical 构造器或外部谱输入。",
        },
        {
            "gate": "ReturnAlphabetCanAbsorbUnregisteredSource",
            "closed": packet_return.get("support_failure_packet_return_dichotomy_closed") is True,
            "proved": False,
            "meaning": "非 clean-core packet 的回流字母表已闭合，但未登记来源是否总能落入这些出口仍需准入账本标注。",
            "remaining": "把 unregistered source 具体标到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。",
        },
        {
            "gate": "CleanCorePrimitiveSourceConstructorAdmissionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 noncanonical clean-core 候选都有 pre-Cauchy primitive source constructor。",
            "remaining": "证明 CleanCorePrimitiveSourceConstructorAdmissionAndReturn。",
        },
        {
            "gate": "ExternalSpectralAtomStillOpen",
            "closed": spectral.get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            "proved": False,
            "meaning": "外部路线仍是 c-dependent residue weight 谱抵消输入。",
            "remaining": "证明或接受 CDependentResidueWeightSpectralCancellationInput。",
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
    source_lock_path: Path,
    branch_path: Path,
    provenance_path: Path,
    complement_path: Path,
    packet_return_path: Path,
    spectral_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 原始来源准入路由。"""
    source_paths = [
        previous_path,
        source_lock_path,
        branch_path,
        provenance_path,
        complement_path,
        packet_return_path,
        spectral_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    source_lock = load_json(source_lock_path)
    branch = load_json(branch_path)
    provenance = load_json(provenance_path)
    complement = load_json(complement_path)
    packet_return = load_json(packet_return_path)
    spectral = load_json(spectral_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(
        previous=previous,
        source_lock=source_lock,
        branch=branch,
        provenance=provenance,
        complement=complement,
        packet_return=packet_return,
        spectral=spectral,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "CleanCorePrimitiveSourceConstructorAdmissionCurrentCorpusProved",
            "ReturnAlphabetCanAbsorbUnregisteredSource",
        }
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_origin_source_admission_router",
        "status": "clean_core_origin_ledger_reduced_to_primitive_source_constructor_admission_open",
        "clean_core_origin_source_admission_boundary_closed": boundary_closed,
        "origin_ledger_needs_constructor_admission": True,
        "constructor_admission_implies_origin_ledger": True,
        "canonical_constructor_scoped_only": True,
        "generic_wfd_constructor_blocked": True,
        "unregistered_source_return_absorbed": False,
        "clean_core_primitive_source_constructor_admission_proved": False,
        "clean_core_original_coefficient_generation_ledger_proved": False,
        "external_spectral_atom_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_input": "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        "latest_internal_subinput": "CleanCorePrimitiveSourceConstructorAdmissionAndReturn",
        "latest_external_subinput": "CDependentResidueWeightSpectralCancellationInput",
        "latest_conditional_basis": (
            "(CleanCorePrimitiveSourceConstructorAdmissionAndReturn OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "CleanCorePrimitiveSourceConstructorAdmissionAndReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "compression_law": (
            "原始生成账本的入口不是估计，而是来源准入：必须先证明 actual clean-core "
            "alpha/delta 由某个 pre-Cauchy primitive source constructor 生成。构造器准入后，"
            "emitted summand schema 可展开为原始生成账本；构造器缺失则必须作为未登记来源回流，"
            "不能继续当作 clean-core 终端。"
        ),
        "plain_conclusion": (
            "最新完全自足剩余继续压缩为 clean-core primitive source constructor 准入："
            "先找到并登记实际来源构造器，才能生成 alpha/delta 原始账本。canonical 构造器已闭合但作用域有限，"
            "generic WFD 不是构造器；当前材料尚未证明 noncanonical clean-core 的构造器准入或未登记来源吸收。"
        ),
        "constructor_requirements": constructor_requirements(),
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
        "# Prime Matrix clean-core 原始来源准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_origin_source_admission_boundary_closed={fmt_bool(result['clean_core_origin_source_admission_boundary_closed'])}",
        f"constructor_admission_implies_origin_ledger={fmt_bool(result['constructor_admission_implies_origin_ledger'])}",
        f"unregistered_source_return_absorbed={fmt_bool(result['unregistered_source_return_absorbed'])}",
        f"clean_core_primitive_source_constructor_admission_proved={fmt_bool(result['clean_core_primitive_source_constructor_admission_proved'])}",
        f"clean_core_original_coefficient_generation_ledger_proved={fmt_bool(result['clean_core_original_coefficient_generation_ledger_proved'])}",
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
            "## 2. 压缩律",
            "",
            result["compression_law"],
            "",
            "## 3. 构造器准入字段",
            "",
            "| field | requirement | why |",
            "| --- | --- | --- |",
        ]
    )
    for req in result["constructor_requirements"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(req['field'])}`",
                    table_cell(req["requirement"]),
                    table_cell(req["why"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 最新输入基",
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
            "`CleanCorePrimitiveSourceConstructorAdmissionAndReturn` 要求：",
            "",
            "- 在 Cauchy/dispersion 前给出 actual clean-core `alpha/delta` 的 primitive source constructor；",
            "- 证明该构造器输出落在同一个 actual formal unit；",
            "- 给出 emitted summand schema，使其可展开为原始生成账本；",
            "- 证明该构造器不是 canonical 跨分支导入，也不是 generic WFD 形式冒充；",
            "- 构造器缺失、口径冲突或未登记来源必须回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。",
            "",
            "## 5. 当前结论",
            "",
            "本步没有证明 primitive source constructor 准入，也没有吸收未登记来源。它只把原始生成账本的",
            "最小入口压成来源构造器准入：没有构造器，就没有合法 clean-core 原始账本。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Route clean-core origin ledger to primitive source constructor admission."
    )
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--source-lock", type=Path, default=DEFAULT_SOURCE_LOCK)
    parser.add_argument("--branch", type=Path, default=DEFAULT_BRANCH)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--complement", type=Path, default=DEFAULT_COMPLEMENT)
    parser.add_argument("--packet-return", type=Path, default=DEFAULT_PACKET_RETURN)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        previous_path=args.previous,
        source_lock_path=args.source_lock,
        branch_path=args.branch,
        provenance_path=args.provenance,
        complement_path=args.complement,
        packet_return_path=args.packet_return,
        spectral_path=args.spectral,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_internal_subinput"])


if __name__ == "__main__":
    main()
