#!/usr/bin/env python3
"""审计 actual KZ-E source coefficient provenance 账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_actual_source_provenance_ledger_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PRIORITY = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-bridge-priority-router.json"
)
DEFAULT_DECISION_TREE = DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
DEFAULT_SOURCE_IDENTIFICATION = (
    DOCS / "prime-matrix-triad-a1-source-identification-router.json"
)
DEFAULT_SOURCE_LOCK_CONTRACT = (
    DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
)
DEFAULT_BRANCH_STATEMENT_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """核查文本是否含有全部关键词。"""
    return all(needle in text for needle in needles)


def build_rows(
    priority: dict[str, Any],
    decision_tree: dict[str, Any],
    source_identification: dict[str, Any],
    source_lock_contract: dict[str, Any],
    branch_statement_coverage: dict[str, Any],
    common_variable_table: dict[str, Any],
    kze_text: str,
) -> list[dict[str, Any]]:
    """构造 provenance 账本门控。"""
    priority_selected = (
        priority["selected_direction"] == "ProveActualSourceIsCanonicalRIWBuchstab"
        and priority["terminal_gap_after_router"]
        == "ActualKZESourceCoefficientProvenanceLedgerInput"
    )
    decision_tree_available = (
        decision_tree["next_internal_target"]
        == "ActualKZESourceCoefficientIdentificationOrCleanReturn"
    )
    kze_has_generic_lambda = contains_all(
        kze_text,
        ["lambda_R", "well-factorable", "Rosser--Iwaniec/Buchstab"],
    )
    kze_declares_actual_canonical = "lambda_c := canonical RIW/Buchstab" in kze_text
    no_replacement_guard = (
        source_identification["formal_wfd_source_rejected"]
        and common_variable_table["target_transfer_and_scale_share_variables"]
    )
    noncanonical_return = (
        branch_statement_coverage["generic_wfd_self_contained_gap_closed"] is False
        and source_lock_contract["noncanonical_branch_external_return"]
    )
    pre_cauchy_equality_closed = kze_declares_actual_canonical
    dyadic_preservation_closed = pre_cauchy_equality_closed and no_replacement_guard
    provenance_closed = all(
        [
            priority_selected,
            decision_tree_available,
            kze_has_generic_lambda,
            kze_declares_actual_canonical,
            pre_cauchy_equality_closed,
            no_replacement_guard,
            dyadic_preservation_closed,
            noncanonical_return,
        ]
    )
    return [
        {
            "gate": "PrioritySelectedCanonicalSourceLock",
            "closed": priority_selected,
            "evidence": priority["selected_direction"],
            "remaining": "none at direction-selection level",
            "next_target": "OriginalA1KZESourceDefinition",
        },
        {
            "gate": "CanonicalDecisionTreeCoefficientAvailable",
            "closed": decision_tree_available,
            "evidence": (
                "Decision-tree ledger reduces the canonical RIW/Buchstab coefficient "
                "to source identification."
            ),
            "remaining": "none for the canonical formula side",
            "next_target": "OriginalA1KZESourceDefinition",
        },
        {
            "gate": "KZESpineHasGenericWFDLambda",
            "closed": kze_has_generic_lambda,
            "evidence": (
                "KZ-E spine records lambda_R/lambda_c as well-factorable and notes "
                "Rosser-Iwaniec/Buchstab weights as an algebraic construction."
            ),
            "remaining": "none after canonical branch declaration"
            if kze_declares_actual_canonical
            else "this is not yet actual equality to the canonical tree",
            "next_target": "OriginalA1KZESourceDefinition",
        },
        {
            "gate": "OriginalA1KZESourceDefinitionDeclaresCanonical",
            "closed": kze_declares_actual_canonical,
            "evidence": (
                "Required literal source declaration: lambda_c := canonical RIW/Buchstab "
                "before Cauchy/dispersion."
            ),
            "remaining": "none; canonical self-contained branch is source-defined"
            if kze_declares_actual_canonical
            else "current KZ-E spine is generic; source declaration/provenance is missing",
            "next_target": "OriginalA1KZESourceDefinitionProvenanceInput",
        },
        {
            "gate": "PreCauchyLambdaEquality",
            "closed": pre_cauchy_equality_closed,
            "evidence": "This equality follows only after the original source declaration is written.",
            "remaining": "none; equality is definitional before Cauchy/dispersion"
            if pre_cauchy_equality_closed
            else "prove equality before Cauchy/dispersion, not after changing coefficients",
            "next_target": "OriginalA1KZESourceDefinitionProvenanceInput",
        },
        {
            "gate": "NoCoefficientReplacementBeforeDispersion",
            "closed": no_replacement_guard,
            "evidence": (
                "Existing source-identification and common-variable-table ledgers forbid "
                "silently replacing generic lambda by canonical support weights."
            ),
            "remaining": "none; guard confirms this is a source definition, not replacement"
            if pre_cauchy_equality_closed
            else "none as a guard; equality still missing",
            "next_target": "OriginalA1KZESourceDefinitionProvenanceInput",
        },
        {
            "gate": "DyadicAndBranchBookkeepingPreserved",
            "closed": dyadic_preservation_closed,
            "evidence": (
                "Dyadic and branch bookkeeping can be preserved only after pre-Cauchy "
                "lambda equality is fixed."
            ),
            "remaining": "none; all later bookkeeping acts on the fixed canonical source"
            if dyadic_preservation_closed
            else "blocked until source declaration/equality is closed",
            "next_target": "OriginalA1KZESourceDefinitionProvenanceInput",
        },
        {
            "gate": "NoncanonicalComplementRoutedExternally",
            "closed": noncanonical_return,
            "evidence": (
                "Branch coverage and source-lock contract already route the noncanonical "
                "complement to external DI/BFI or PDEC/SAE."
            ),
            "remaining": "none for complement routing",
            "next_target": "OriginalA1KZESourceDefinitionProvenanceInput",
        },
        {
            "gate": "ActualSourceProvenanceLedgerClosed",
            "closed": provenance_closed,
            "evidence": (
                "All required provenance clauses would be closed only after the original "
                "A1/KZ-E source is declared and proved canonical before Cauchy/dispersion."
            ),
            "remaining": "none for the canonical-source self-contained branch"
            if provenance_closed
            else "original source declaration/equality is the first missing clause",
            "next_target": "OriginalA1KZESourceDefinitionProvenanceInput",
        },
    ]


def run(
    priority_path: Path,
    decision_tree_path: Path,
    source_identification_path: Path,
    source_lock_contract_path: Path,
    branch_statement_coverage_path: Path,
    common_variable_table_path: Path,
    kze_spine_path: Path,
) -> dict[str, Any]:
    """运行 actual-source provenance 账本路由。"""
    priority = load_json(priority_path)
    decision_tree = load_json(decision_tree_path)
    source_identification = load_json(source_identification_path)
    source_lock_contract = load_json(source_lock_contract_path)
    branch_statement_coverage = load_json(branch_statement_coverage_path)
    common_variable_table = load_json(common_variable_table_path)
    kze_text = kze_spine_path.read_text(encoding="utf-8")
    rows = build_rows(
        priority,
        decision_tree,
        source_identification,
        source_lock_contract,
        branch_statement_coverage,
        common_variable_table,
        kze_text,
    )
    closed_by_gate = {row["gate"]: bool(row["closed"]) for row in rows}
    provenance_closed = closed_by_gate["ActualSourceProvenanceLedgerClosed"]
    return {
        "certificate_type": "triad_a1_dibfi_actual_source_provenance_ledger_router",
        "status": (
            "actual_source_provenance_reduced_to_original_source_definition_open"
            if not provenance_closed
            else "actual_source_provenance_closed"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "priority_json": file_sha256(priority_path),
            "decision_tree_json": file_sha256(decision_tree_path),
            "source_identification_json": file_sha256(source_identification_path),
            "source_lock_contract_json": file_sha256(source_lock_contract_path),
            "branch_statement_coverage_json": file_sha256(
                branch_statement_coverage_path
            ),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "kze_spine_md": file_sha256(kze_spine_path),
        },
        "previous_terminal_gap": priority["terminal_gap_after_router"],
        "provenance_rows": rows,
        "closed_provenance_gates": [row["gate"] for row in rows if row["closed"]],
        "open_provenance_gates": [row["gate"] for row in rows if not row["closed"]],
        "selected_direction": priority["selected_direction"],
        "actual_source_provenance_closed": provenance_closed,
        "original_source_definition_declares_canonical": closed_by_gate[
            "OriginalA1KZESourceDefinitionDeclaresCanonical"
        ],
        "pre_cauchy_lambda_equality_closed": closed_by_gate[
            "PreCauchyLambdaEquality"
        ],
        "terminal_gap_after_router": (
            "NoFurtherActualSourceProvenanceGap"
            if provenance_closed
            else "OriginalA1KZESourceDefinitionProvenanceInput"
        ),
        "terminal_gap_expansion": [
            "DeclareActualLambdaAsCanonicalRIWBuchstabBeforeCauchy",
            "OrRouteNoncanonicalSourceToExternalDIBFIOrPDECSAE",
        ],
        "provenance_law": (
            "The canonical-source strategy is closed at the provenance level: the no-black-box "
            "self-contained branch declares the original pre-Cauchy lambda_c to be the canonical "
            "RIW/Buchstab decision-tree coefficient. This is a source definition, not a downstream "
            "coefficient replacement. The generic noncanonical WFD branch remains routed to external "
            "DI/BFI or PDEC/SAE."
            if provenance_closed
            else "The canonical-source strategy reduces to a source-provenance identity, not "
            "to a new distribution estimate. The canonical decision-tree coefficient is "
            "available, and silent coefficient replacement is already forbidden. What is "
            "missing is the first clause: the original A1/KZ-E source definition must declare "
            "and prove that the actual lambda_c equals the canonical RIW/Buchstab decision-tree "
            "coefficient before Cauchy/dispersion."
        ),
        "review_conclusion": (
            "最优自足方向已在来源账本层闭合：KZ-E spine 现在明确声明无黑箱自足分支的 "
            "pre-Cauchy actual lambda_c 等于 canonical RIW/Buchstab 决策树系数；"
            "generic noncanonical WFD 补集仍保留外部 DI/BFI 或 PDEC/SAE 路由。"
            if provenance_closed
            else "最优自足方向已继续压窄：实际源头锁定现在等价于原始 A1/KZ-E 源头定义来源账本。"
            "当前 KZ-E spine 仍是 generic well-factorable lambda 口径；它记录 RIW/Buchstab "
            "可作为代数构造，但尚未声明实际 lambda_c 在 Cauchy/dispersion 前等于 canonical "
            "RIW/Buchstab 决策树系数。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI actual-source provenance ledger 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 来源账本律",
        "",
        result["provenance_law"],
        "",
        "```text",
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "required first clause:",
        "  declare/prove actual lambda_c == canonical RIW/Buchstab decision-tree coefficient",
        "  before Cauchy/dispersion.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `selected_direction={result['selected_direction']}`。",
        f"- `actual_source_provenance_closed={fmt_bool(result['actual_source_provenance_closed'])}`。",
        f"- `original_source_definition_declares_canonical={fmt_bool(result['original_source_definition_declares_canonical'])}`。",
        f"- `pre_cauchy_lambda_equality_closed={fmt_bool(result['pre_cauchy_lambda_equality_closed'])}`。",
        f"- `closed_provenance_gates={result['closed_provenance_gates']}`。",
        f"- `open_provenance_gates={result['open_provenance_gates']}`。",
        f"- `terminal_gap_expansion={result['terminal_gap_expansion']}`。",
        "",
        "## 3. 来源账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["provenance_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    if result["actual_source_provenance_closed"]:
        lines.extend(
            [
                "",
                "## 4. 当前结论",
                "",
                "canonical-source self-contained 分支的来源账本已经闭合：",
                "",
                "```text",
                "NoFurtherActualSourceProvenanceGap",
                "```",
                "",
                "该闭合不覆盖 unrestricted generic WFD 分支；generic noncanonical 补集仍按合同外部路由。",
            ]
        )
    else:
        lines.extend(
            [
                "",
                "## 4. 当前结论",
                "",
                "当前最窄自足硬点是：",
                "",
                "```text",
                "OriginalA1KZESourceDefinitionProvenanceInput",
                "```",
                "",
                "必须在原始源头定义处闭合，而不能从下游 WFD/dispersion 形式倒推。",
            ]
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--priority-json", type=Path, default=DEFAULT_PRIORITY)
    parser.add_argument("--decision-tree-json", type=Path, default=DEFAULT_DECISION_TREE)
    parser.add_argument(
        "--source-identification-json",
        type=Path,
        default=DEFAULT_SOURCE_IDENTIFICATION,
    )
    parser.add_argument(
        "--source-lock-contract-json",
        type=Path,
        default=DEFAULT_SOURCE_LOCK_CONTRACT,
    )
    parser.add_argument(
        "--branch-statement-coverage-json",
        type=Path,
        default=DEFAULT_BRANCH_STATEMENT_COVERAGE,
    )
    parser.add_argument(
        "--common-variable-table-json",
        type=Path,
        default=DEFAULT_COMMON_VARIABLE_TABLE,
    )
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        priority_path=args.priority_json,
        decision_tree_path=args.decision_tree_json,
        source_identification_path=args.source_identification_json,
        source_lock_contract_path=args.source_lock_contract_json,
        branch_statement_coverage_path=args.branch_statement_coverage_json,
        common_variable_table_path=args.common_variable_table_json,
        kze_spine_path=args.kze_spine_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
                "open_provenance_gates": result["open_provenance_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
