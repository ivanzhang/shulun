#!/usr/bin/env python3
"""Prime Matrix clean-core pre-Cauchy 来源律原子化路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_precauchy_source_law_atom_router.py

输出：
  docs/monograph/prime-matrix-clean-core-precauchy-source-law-atom-router.json
  docs/monograph/prime-matrix-clean-core-precauchy-source-law-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-path-source-firewall-router.json"
DEFAULT_SOURCE_ID = DOCS / "prime-matrix-triad-a1-source-identification-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_BRANCH = DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
DEFAULT_COMPLEMENT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.md"


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


def implication_clauses() -> list[dict[str, Any]]:
    """给出原始生成账本推出来源律的条款。"""
    return [
        {
            "clause": "SameFormalUnitBeforeCauchy",
            "ledger_requirement": "所有 actual alpha/delta summand 在 Cauchy、Type/Fourier、completion 前登记到同一 formal unit。",
            "source_law_output": "来源公式不是后验替换，而是原始系数恒等式。",
        },
        {
            "clause": "PrimitivePathKey",
            "ledger_requirement": "每个 summand 记录 source class、branch key、u/v map、dyadic/truncation state、sign 和 local factor。",
            "source_law_output": "branch key 直接给出 exact path signature。",
        },
        {
            "clause": "PolylogPathBudget",
            "ledger_requirement": "branch alphabet 和 truncation depth 均为 K6/tail-label 已登记的 log^O 成本。",
            "source_law_output": "路径数预算可用于 selector pigeonhole。",
        },
        {
            "clause": "PrimitiveNonzeroOrSignSplit",
            "ledger_requirement": "同一完整 branch key 的 local factors 非零；若同一 key 有相反号，必须先按 sign/refinement 细分。",
            "source_law_output": "同路径非零、无抵消，或抵消被命名回流。",
        },
        {
            "clause": "NamedReturnDiscipline",
            "ledger_requirement": "缺失来源、路径超预算、thin/rejected block、未消除抵消均带 return tag。",
            "source_law_output": "失败回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    source_id: dict[str, Any],
    provenance: dict[str, Any],
    branch: dict[str, Any],
    complement: dict[str, Any],
    spectral: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 pre-Cauchy 来源律原子化判定表。"""
    return [
        {
            "gate": "PriorPreCauchySourceLawPinned",
            "closed": previous.get("latest_internal_subinput")
            == "CleanCorePreCauchyCoefficientSourceLawAndReturn",
            "proved": False,
            "meaning": "上一层已把路径来源防火墙压到 clean-core pre-Cauchy 来源律。",
            "remaining": "判断该来源律还能否继续拆成更小的必要账本。",
        },
        {
            "gate": "SourceLawIsOriginLedgerBundle",
            "closed": True,
            "proved": False,
            "meaning": "pre-Cauchy 来源律的四项内容等价于原始生成账本：公式、路径、非零和回流。",
            "remaining": "提交 actual clean-core alpha/delta 的原始生成账本。",
        },
        {
            "gate": "OriginLedgerImpliesPreCauchySourceLaw",
            "closed": True,
            "proved": True,
            "meaning": "若同一 formal unit 的原始生成表存在，branch key 给出路径签名，非零/回流由表项纪律推出。",
            "remaining": "该推出只处理逻辑结构，不证明生成表存在。",
        },
        {
            "gate": "CanonicalLedgerClosedButScoped",
            "closed": provenance.get("actual_source_provenance_closed") is True
            and branch.get("canonical_source_branch_internal_gap_closed") is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 原始来源账本已闭合，但只服务 canonical-source 分支。",
            "remaining": "不能把 canonical 账本导入 noncanonical clean-core。",
        },
        {
            "gate": "GenericWFDOriginLedgerRejected",
            "closed": source_id.get("formal_wfd_source_rejected") is True
            and complement.get("generic_wfd_template_available") is False,
            "proved": True,
            "meaning": "well-factorable/generic WFD 只给形式分解，不给 actual 原始生成表。",
            "remaining": "clean-core 必须给出自己的 actual source ledger 或走外部。",
        },
        {
            "gate": "NoncanonicalComplementNeedsOwnActualSource",
            "closed": complement.get("contract_boundary_closed") is True
            and complement.get("noncanonical_complement_closed_by_current_corpus") is False,
            "proved": True,
            "meaning": "canonical 分支扣除后，noncanonical 补集只剩实际源定理、强化反原子或外部谱路线。",
            "remaining": "当前 clean-core 来源律必须落到自己的原始生成账本。",
        },
        {
            "gate": "CleanCoreOriginalCoefficientGenerationLedgerCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未列出 actual clean-core alpha/delta 的完整 pre-Cauchy 原始生成表。",
            "remaining": "证明 CleanCoreOriginalCoefficientGenerationLedgerAndReturn。",
        },
        {
            "gate": "ExternalSpectralAtomStillOpen",
            "closed": spectral.get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            "proved": False,
            "meaning": "外部 completed KLS 路线仍压在 c-dependent residue weight 谱抵消输入上。",
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
    source_id_path: Path,
    provenance_path: Path,
    branch_path: Path,
    complement_path: Path,
    spectral_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core pre-Cauchy 来源律原子化路由。"""
    source_paths = [
        previous_path,
        source_id_path,
        provenance_path,
        branch_path,
        complement_path,
        spectral_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    source_id = load_json(source_id_path)
    provenance = load_json(provenance_path)
    branch = load_json(branch_path)
    complement = load_json(complement_path)
    spectral = load_json(spectral_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(
        previous=previous,
        source_id=source_id,
        provenance=provenance,
        branch=branch,
        complement=complement,
        spectral=spectral,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"] != "CleanCoreOriginalCoefficientGenerationLedgerCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_precauchy_source_law_atom_router",
        "status": "clean_core_precauchy_source_law_reduced_to_origin_generation_ledger_open",
        "clean_core_precauchy_source_law_atom_boundary_closed": boundary_closed,
        "origin_generation_ledger_implication_closed": True,
        "clean_core_original_coefficient_generation_ledger_proved": False,
        "clean_core_precauchy_source_law_proved": False,
        "canonical_origin_ledger_scoped_only": True,
        "generic_wfd_origin_ledger_blocked": True,
        "external_spectral_atom_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_input": "CleanCorePreCauchyCoefficientSourceLawAndReturn",
        "latest_internal_subinput": "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        "latest_external_subinput": "CDependentResidueWeightSpectralCancellationInput",
        "latest_conditional_basis": (
            "(CleanCoreOriginalCoefficientGenerationLedgerAndReturn OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "compression_theorem": (
            "CleanCorePreCauchyCoefficientSourceLawAndReturn 的真正原子是 "
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn：若在 Cauchy/dispersion 前列出 "
            "actual clean-core alpha/delta 的同一 formal unit 原始生成表，则路径签名、polylog 路径预算、"
            "同路径非零/无抵消和失败回流都由账本纪律推出；反过来，任何来源律证明都必须至少给出这张表。"
        ),
        "plain_conclusion": (
            "最新真正剩余继续压缩：pre-Cauchy 来源律不是一个新的统计估计，而是 actual clean-core "
            "alpha/delta 的原始生成账本问题。canonical 账本只闭合 canonical-source 分支，generic WFD "
            "不给原始来源；当前材料尚未提交 noncanonical clean-core 的完整生成表。"
        ),
        "clauses": implication_clauses(),
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
        "# Prime Matrix clean-core pre-Cauchy 来源律原子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_precauchy_source_law_atom_boundary_closed={fmt_bool(result['clean_core_precauchy_source_law_atom_boundary_closed'])}",
        f"origin_generation_ledger_implication_closed={fmt_bool(result['origin_generation_ledger_implication_closed'])}",
        f"clean_core_original_coefficient_generation_ledger_proved={fmt_bool(result['clean_core_original_coefficient_generation_ledger_proved'])}",
        f"clean_core_precauchy_source_law_proved={fmt_bool(result['clean_core_precauchy_source_law_proved'])}",
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
            "## 2. 压缩定理",
            "",
            result["compression_theorem"],
            "",
            "## 3. 原始生成账本条款",
            "",
            "| clause | ledger requirement | source-law output |",
            "| --- | --- | --- |",
        ]
    )
    for clause in result["clauses"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(clause['clause'])}`",
                    table_cell(clause["ledger_requirement"]),
                    table_cell(clause["source_law_output"]),
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
            "`CleanCoreOriginalCoefficientGenerationLedgerAndReturn` 要求：",
            "",
            "- 在 Cauchy、dispersion、Type/Fourier、completion 之前固定同一 actual formal unit；",
            "- 列出 clean-core `alpha/delta` 的所有原始 summand、branch key、u/v map、符号和 local factor；",
            "- 证明 branch key 数为 `log^O(1)`，或把路径超预算回流到 K6/PDEC/SAE；",
            "- 同一完整 key 非零且无抵消；若有抵消，必须进一步细分或输出命名回流；",
            "- 缺失来源、thin/rejected block 或外部谱需求必须带 return tag。",
            "",
            "## 5. 当前结论",
            "",
            "本步没有证明 clean-core 原始生成账本。它闭合的是逻辑压缩：pre-Cauchy 来源律若要成立，",
            "最小自足证据就是这张 actual 生成表；canonical 表不能跨分支导入，generic WFD 也不能替代它。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Atomize clean-core pre-Cauchy source law to origin generation ledger."
    )
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--source-id", type=Path, default=DEFAULT_SOURCE_ID)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--branch", type=Path, default=DEFAULT_BRANCH)
    parser.add_argument("--complement", type=Path, default=DEFAULT_COMPLEMENT)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        previous_path=args.previous,
        source_id_path=args.source_id,
        provenance_path=args.provenance,
        branch_path=args.branch,
        complement_path=args.complement,
        spectral_path=args.spectral,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_internal_subinput"])


if __name__ == "__main__":
    main()
