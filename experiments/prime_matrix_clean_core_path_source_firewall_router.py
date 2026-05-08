#!/usr/bin/env python3
"""Prime Matrix clean-core 路径来源防火墙路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_path_source_firewall_router.py

输出：
  docs/monograph/prime-matrix-clean-core-path-source-firewall-router.json
  docs/monograph/prime-matrix-clean-core-path-source-firewall-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PATH = DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json"
DEFAULT_CANON_DECISION = DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
DEFAULT_SOURCE_ID = DOCS / "prime-matrix-triad-a1-source-identification-router.json"
DEFAULT_PROVENANCE = DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
DEFAULT_COMPLEMENT = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-path-source-firewall-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-path-source-firewall-router.md"


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


def rows(
    path_router: dict[str, Any],
    canon_decision: dict[str, Any],
    source_id: dict[str, Any],
    provenance: dict[str, Any],
    complement: dict[str, Any],
    spectral: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成路径来源防火墙判定表。"""
    return [
        {
            "gate": "PriorPathPartitionPinned",
            "closed": path_router.get("latest_internal_subinput")
            == "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn",
            "proved": False,
            "meaning": "上一层已把 clean-core 层转移压成 actual 系数路径分割账本。",
            "remaining": "判断该路径账本需要什么最小来源输入。",
        },
        {
            "gate": "PathPartitionNeedsPreCauchySourceLaw",
            "closed": True,
            "proved": False,
            "meaning": "路径签名、无抵消和路径数预算必须作用在 Cauchy/dispersion 前的 actual 系数公式上。",
            "remaining": "写出 clean-core pre-Cauchy actual coefficient source law。",
        },
        {
            "gate": "CanonicalDecisionTreeAvailableOnlyAsTemplate",
            "closed": canon_decision.get("recursive_formula_closed_algebraically") is True
            and provenance.get("actual_source_provenance_closed") is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 决策树和来源账本已闭合，但作用域只限 canonical-source 分支。",
            "remaining": "不能把该模板导入 noncanonical clean-core。",
        },
        {
            "gate": "WellFactorableTemplateRejected",
            "closed": source_id.get("formal_wfd_source_rejected") is True,
            "proved": True,
            "meaning": "仅有 well-factorable/generic WFD 形式不提供路径分割或 source entropy。",
            "remaining": "clean-core 必须有 actual 来源公式，而非形式可分解性。",
        },
        {
            "gate": "NoncanonicalComplementFirewallClosed",
            "closed": complement.get("contract_boundary_closed") is True
            and complement.get("generic_wfd_template_available") is False,
            "proved": True,
            "meaning": "canonical 分支已扣除，generic WFD 自足模板被 moving-delta 阻断。",
            "remaining": "noncanonical clean-core 只能走 actual-source 定理或外部谱输入。",
        },
        {
            "gate": "CleanCorePreCauchySourceLawCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有 clean-core actual alpha/delta 的 pre-Cauchy 来源公式、路径分割和失败回流账本。",
            "remaining": "证明 CleanCorePreCauchyCoefficientSourceLawAndReturn。",
        },
        {
            "gate": "ExternalSpectralAtomPinned",
            "closed": spectral.get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            "proved": False,
            "meaning": "外部 completed KLS 路线已进一步压成 c-dependent residue weight 谱抵消。",
            "remaining": "证明或引用 CDependentResidueWeightSpectralCancellationInput。",
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
    path_router_path: Path,
    canon_decision_path: Path,
    source_id_path: Path,
    provenance_path: Path,
    complement_path: Path,
    spectral_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 路径来源防火墙路由。"""
    source_paths = [
        path_router_path,
        canon_decision_path,
        source_id_path,
        provenance_path,
        complement_path,
        spectral_path,
        dstructure_path,
    ]
    path_router = load_json(path_router_path)
    canon_decision = load_json(canon_decision_path)
    source_id = load_json(source_id_path)
    provenance = load_json(provenance_path)
    complement = load_json(complement_path)
    spectral = load_json(spectral_path)
    dstructure = load_json(dstructure_path)

    gate_rows = rows(
        path_router=path_router,
        canon_decision=canon_decision,
        source_id=source_id,
        provenance=provenance,
        complement=complement,
        spectral=spectral,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"] for row in gate_rows if row["gate"] != "CleanCorePreCauchySourceLawCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_path_source_firewall_router",
        "status": "clean_core_path_partition_reduced_to_precauchy_source_law_open",
        "clean_core_path_source_firewall_boundary_closed": boundary_closed,
        "canonical_template_scoped_only": True,
        "generic_wfd_template_blocked": True,
        "clean_core_precauchy_source_law_proved": False,
        "clean_core_path_partition_proved": False,
        "external_spectral_atom_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_input": "CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn",
        "latest_internal_subinput": "CleanCorePreCauchyCoefficientSourceLawAndReturn",
        "latest_external_subinput": "CDependentResidueWeightSpectralCancellationInput",
        "latest_conditional_basis": (
            "(CleanCorePreCauchyCoefficientSourceLawAndReturn OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "CleanCorePreCauchyCoefficientSourceLawAndReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "source_law": (
            "路径分割账本必须在 Cauchy/dispersion 前的 actual clean-core alpha/delta 系数上建立："
            "给出 exact 来源公式、polylog 路径签名、同路径非零/无抵消、路径超预算或薄块的命名回流。"
        ),
        "firewall_law": (
            "canonical 决策树可作为模板但不能跨分支导入；generic WFD 形式被 moving-delta 阻断。"
            "因此 clean-core noncanonical 残余的自足闭合只能来自自己的 pre-Cauchy coefficient source law，"
            "否则走 c-dependent completed residue spectral input 或命名回流。"
        ),
        "plain_conclusion": (
            "最新真正剩余继续压缩为 clean-core pre-Cauchy 系数来源律：先写出 actual alpha/delta 的来源公式，"
            "才能审查路径分割、无抵消和薄块回流。当前材料尚未证明该来源律。"
        ),
        "rows": gate_rows,
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
        "# Prime Matrix clean-core 路径来源防火墙路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_path_source_firewall_boundary_closed={fmt_bool(result['clean_core_path_source_firewall_boundary_closed'])}",
        f"clean_core_precauchy_source_law_proved={fmt_bool(result['clean_core_precauchy_source_law_proved'])}",
        f"clean_core_path_partition_proved={fmt_bool(result['clean_core_path_partition_proved'])}",
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
            "## 2. 来源律",
            "",
            result["source_law"],
            "",
            "## 3. 防火墙律",
            "",
            result["firewall_law"],
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
            "`CleanCorePreCauchyCoefficientSourceLawAndReturn` 要求：",
            "",
            "- 在 Cauchy、Type/Fourier、completion 之前写出 actual clean-core `alpha/delta` 来源公式；",
            "- 从该公式得到 polylog exact path signatures；",
            "- 证明同路径非零且无抵消，或继续细分直到互斥；",
            "- source-law 失败、路径超预算、thin/rejected block 必须回流到 PDEC/SAE/ColumnCRT/CleanKLS，或进入外部谱输入。",
            "",
            "## 5. 当前结论",
            "",
            "本步没有证明 clean-core 来源律。它关闭的是两个偷渡方向：canonical 决策树不能导入 noncanonical",
            "clean-core，generic WFD 形式不能替代 actual coefficient source law。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Route clean-core path partition to pre-Cauchy source law."
    )
    parser.add_argument("--path-router", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--canon-decision", type=Path, default=DEFAULT_CANON_DECISION)
    parser.add_argument("--source-id", type=Path, default=DEFAULT_SOURCE_ID)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--complement", type=Path, default=DEFAULT_COMPLEMENT)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        path_router_path=args.path_router,
        canon_decision_path=args.canon_decision,
        source_id_path=args.source_id,
        provenance_path=args.provenance,
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
