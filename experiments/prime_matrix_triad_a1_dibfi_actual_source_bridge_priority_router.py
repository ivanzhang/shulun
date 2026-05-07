#!/usr/bin/env python3
"""选择 actual-source bridge 的最优自足硬攻方向。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_actual_source_bridge_priority_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-actual-source-bridge-priority-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-actual-source-bridge-priority-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_CLOSURE_TAXONOMY = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
)
DEFAULT_SOURCE_IDENTIFICATION = (
    DOCS / "prime-matrix-triad-a1-source-identification-router.json"
)
DEFAULT_SOURCE_LOCK_CONTRACT = (
    DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
)
DEFAULT_BRANCH_STATEMENT_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_SOURCE_ANTIATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
)
DEFAULT_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-bridge-priority-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-bridge-priority-router.md"
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


def build_direction_rows(
    closure_taxonomy: dict[str, Any],
    source_identification: dict[str, Any],
    source_lock_contract: dict[str, Any],
    branch_statement_coverage: dict[str, Any],
    source_antiatom: dict[str, Any],
    antiatom_nogo: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造两个 actual-source bridge 方向的优先级表。"""
    canonical_chain_ready = all(
        [
            closure_taxonomy["canonical_restricted_self_contained_version_closed"],
            source_lock_contract["source_lock_contract_closed_for_canonical_branch"],
            branch_statement_coverage["canonical_source_branch_internal_gap_closed"],
            source_identification[
                "conditional_source_lock_implies_internal_support_chain"
            ],
        ]
    )
    canonical_remaining_is_provenance = (
        source_identification["next_internal_target"]
        == "CanonicalRIWBuchstabSourceLockContract"
        and source_lock_contract["next_internal_target"]
        == "A1CleanBranchCanonicalSourceAdmission"
    )
    antiatom_generic_refuted = antiatom_nogo[
        "self_contained_generic_version_refuted"
    ]
    antiatom_contract_still_open = source_antiatom["open_antiatom_gates"] == [
        "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
    ]
    return [
        {
            "direction": "ProveActualSourceIsCanonicalRIWBuchstab",
            "selected": canonical_chain_ready and canonical_remaining_is_provenance,
            "score": 3,
            "evidence": (
                "canonical-restricted branch is already internally closed; source lock "
                "feeds the support chain; the remaining proof is a coefficient-provenance "
                "identity before Cauchy/dispersion."
            ),
            "obstruction": "actual A1/KZ-E lambda_c provenance is not yet written as a ledger",
            "next_target": "ActualKZESourceCoefficientProvenanceLedgerInput",
        },
        {
            "direction": "ProveActualSourceStrengthenedAntiAtom",
            "selected": False,
            "score": 1,
            "evidence": (
                f"generic anti-atom refuted={antiatom_generic_refuted}; "
                f"source anti-atom contract still open={antiatom_contract_still_open}."
            ),
            "obstruction": (
                "without first proving actual-source structure, this collapses back to the "
                "moving-delta no-go for generic WFD"
            ),
            "next_target": "ActualSourceStructureFirstOrNewAntiAtomAxiom",
        },
    ]


def run(
    closure_taxonomy_path: Path,
    source_identification_path: Path,
    source_lock_contract_path: Path,
    branch_statement_coverage_path: Path,
    source_antiatom_path: Path,
    antiatom_nogo_path: Path,
) -> dict[str, Any]:
    """运行 actual-source bridge 优先级路由。"""
    closure_taxonomy = load_json(closure_taxonomy_path)
    source_identification = load_json(source_identification_path)
    source_lock_contract = load_json(source_lock_contract_path)
    branch_statement_coverage = load_json(branch_statement_coverage_path)
    source_antiatom = load_json(source_antiatom_path)
    antiatom_nogo = load_json(antiatom_nogo_path)
    rows = build_direction_rows(
        closure_taxonomy,
        source_identification,
        source_lock_contract,
        branch_statement_coverage,
        source_antiatom,
        antiatom_nogo,
    )
    selected_rows = [row for row in rows if row["selected"]]
    selected_direction = (
        selected_rows[0]["direction"] if selected_rows else "NoDirectionSelected"
    )
    next_target = (
        selected_rows[0]["next_target"]
        if selected_rows
        else "ActualSourceBridgeDirectionSelectionIncomplete"
    )
    priority_closed = selected_direction == "ProveActualSourceIsCanonicalRIWBuchstab"
    return {
        "certificate_type": "triad_a1_dibfi_actual_source_bridge_priority_router",
        "status": "actual_source_bridge_best_direction_selected"
        if priority_closed
        else "actual_source_bridge_priority_incomplete",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "closure_taxonomy_json": file_sha256(closure_taxonomy_path),
            "source_identification_json": file_sha256(source_identification_path),
            "source_lock_contract_json": file_sha256(source_lock_contract_path),
            "branch_statement_coverage_json": file_sha256(
                branch_statement_coverage_path
            ),
            "source_antiatom_json": file_sha256(source_antiatom_path),
            "antiatom_nogo_json": file_sha256(antiatom_nogo_path),
        },
        "previous_terminal_gap": closure_taxonomy["terminal_gap_after_router"],
        "direction_rows": rows,
        "selected_direction": selected_direction,
        "rejected_or_deferred_direction": "ProveActualSourceStrengthenedAntiAtom",
        "priority_selection_closed": priority_closed,
        "terminal_gap_after_router": next_target,
        "provenance_ledger_required_clauses": [
            "OriginalA1KZESourceDefinition",
            "PreCauchyLambdaEquality",
            "NoCoefficientReplacementBeforeDispersion",
            "DyadicAndBranchBookkeepingPreserved",
            "NoncanonicalComplementRoutedExternally",
        ],
        "priority_law": (
            "The canonical-source route is the optimal self-contained direction because it "
            "turns the actual-source bridge into a deterministic provenance identity for "
            "lambda_c. The strengthened anti-atom route is not abandoned forever, but it is "
            "not the next best move: without first proving actual-source structure it repeats "
            "the generic WFD anti-atom statement already refuted by the moving-delta model."
        ),
        "review_conclusion": (
            "两个自足方向中，最优硬攻方向是证明实际 full-S non-AP 源头为 canonical "
            "RIW/Buchstab。该方向可直接接入已闭合的 canonical-restricted 链；"
            "strengthened anti-atom 方向必须先获得实际源头结构，否则回到已反证的 generic WFD 反原子。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI actual-source bridge priority 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 优先级律",
        "",
        result["priority_law"],
        "",
        "```text",
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "selected direction:",
        f"  {result['selected_direction']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 下一账本必备条款",
        "",
    ]
    for clause in result["provenance_ledger_required_clauses"]:
        lines.append(f"- `{clause}`。")
    lines.extend(
        [
            "",
            "## 3. 方向比较表",
            "",
            "| direction | selected | score | evidence | obstruction | next target |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["direction_rows"]:
        lines.append(
            "| `{direction}` | `{selected}` | `{score}` | {evidence} | {obstruction} | `{next}` |".format(
                direction=table_cell(row["direction"]),
                selected=fmt_bool(bool(row["selected"])),
                score=row["score"],
                evidence=table_cell(row["evidence"]),
                obstruction=table_cell(row["obstruction"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "下一步不应继续攻击 unrestricted generic anti-atom。最窄可攻输入是：",
            "",
            "```text",
            "ActualKZESourceCoefficientProvenanceLedgerInput",
            "```",
            "",
            "这一步要证明的是实际 lambda_c 的来源等式，而不是新的统计逼近。"
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--closure-taxonomy-json",
        type=Path,
        default=DEFAULT_CLOSURE_TAXONOMY,
    )
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
        "--source-antiatom-json",
        type=Path,
        default=DEFAULT_SOURCE_ANTIATOM,
    )
    parser.add_argument(
        "--antiatom-nogo-json",
        type=Path,
        default=DEFAULT_ANTIATOM_NOGO,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        closure_taxonomy_path=args.closure_taxonomy_json,
        source_identification_path=args.source_identification_json,
        source_lock_contract_path=args.source_lock_contract_json,
        branch_statement_coverage_path=args.branch_statement_coverage_json,
        source_antiatom_path=args.source_antiatom_json,
        antiatom_nogo_path=args.antiatom_nogo_json,
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
                "selected_direction": result["selected_direction"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
