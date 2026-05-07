#!/usr/bin/env python3
"""硬攻 A1CleanBranchCanonicalSourceAdmission 的分支陈述硬点。

用法示例：
  python3 experiments/prime_matrix_triad_a1_canonical_branch_admission_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-canonical-branch-admission-router.json
  docs/monograph/prime-matrix-triad-a1-canonical-branch-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SOURCE_LOCK = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-canonical-branch-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-canonical-branch-admission-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 canonical 分支准入门控。"""
    return [
        {
            "gate": "CurrentKZEStatementIsGenericWFD",
            "available": "KZ-E/WFD-core states lambda_c is well-factorable",
            "needed": "recognize this is broader than canonical RIW/Buchstab source",
            "gap": "none; current upstream text is generic in lambda_c",
            "route": "do not claim canonical admission from the generic statement",
            "closed": True,
        },
        {
            "gate": "CanonicalSourceBranchIsLegalSubcase",
            "available": "RIW/Buchstab weights are valid well-factorable weights",
            "needed": "the canonical branch is a legal subcase of KZ-E inputs",
            "gap": "none; legality follows from the well-factorable algebra already recorded",
            "route": "restrict internal proof branch to lambda_c^RIW-tree",
            "closed": True,
        },
        {
            "gate": "InternalCanonicalBranchClosedConditionally",
            "available": "previous routers close support chain on the canonical source branch",
            "needed": "canonical admission feeds the A1 chain",
            "gap": "none after canonical branch statement is adopted",
            "route": "canonical source branch => support chain => A1 clean internal branch",
            "closed": True,
        },
        {
            "gate": "OriginalCleanObjectCoveredByBranchSplit",
            "available": "generic complement can go to external DI/BFI or PDEC/SAE",
            "needed": "the proof statement explicitly covers both canonical and noncanonical clean objects",
            "gap": "current ledger still needs a branch-statement update",
            "route": "state: canonical source branch uses internal proof; generic source branch uses external DI/BFI",
            "closed": False,
        },
        {
            "gate": "CanonicalBranchStatementAdopted",
            "available": "all ingredients for the branch statement are now present",
            "needed": "A1 theorem/ledger states the internal no-black-box branch is canonical-source only",
            "gap": "this is a documentation/theorem-contract obligation, not a density estimate",
            "route": "update A1 clean theorem statement before claiming internal closure",
            "closed": False,
        },
        {
            "gate": "NoSilentGenericClosure",
            "available": "generic WFD source was already shown insufficient for support",
            "needed": "do not mark generic WFD branch internally closed",
            "gap": "none after branch statement",
            "route": "generic branch remains ExternalDIBFIOriginalDispersion",
            "closed": True,
        },
    ]


def run(source_lock_path: Path) -> dict[str, Any]:
    """运行 canonical 分支准入路由。"""
    source_lock = load_json(source_lock_path)
    return {
        "certificate_type": "triad_a1_canonical_branch_admission_router",
        "status": "canonical_branch_admission_reduced_to_branch_statement_and_coverage",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "source_lock_contract_json": file_sha256(source_lock_path),
        },
        "source_lock_input_status": source_lock["status"],
        "source_lock_input_next_target": source_lock["next_internal_target"],
        "gate_rows": build_gate_rows(),
        "current_kze_statement_is_generic_wfd": True,
        "canonical_source_branch_is_legal_subcase": True,
        "internal_canonical_branch_closed_conditionally": True,
        "original_clean_object_covered_by_branch_split": False,
        "canonical_branch_statement_adopted": False,
        "no_silent_generic_closure": True,
        "reduction_law": (
            "A1 clean branch canonical admission is not a numerical lemma. The current KZ-E/WFD "
            "statement is generic in well-factorable lambda_c, while the internal support chain "
            "is valid only for the canonical RIW/Buchstab source subcase. Therefore the proof must "
            "make an explicit branch statement: canonical-source clean branch is handled internally; "
            "generic noncanonical clean branch is handled only by external DI/BFI or returned to "
            "PDEC/SAE. This preserves the original target without silently claiming generic closure."
        ),
        "next_internal_target": "A1CanonicalSourceBranchStatementAndCoverage",
        "terminal_gap_after_router": (
            "A1CanonicalSourceBranchStatementAndCoverageOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "A1CleanBranchCanonicalSourceAdmission 已被压成分支陈述与覆盖合同：canonical RIW/Buchstab "
            "源头是合法子分支，且该子分支可接入内部支撑链；但当前 KZ-E 仍是 generic WFD 口径，"
            "所以必须明确声明 canonical 内部分支与 generic 外部分支的覆盖关系，不能静默把 generic "
            "分支也标为内部闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Canonical Branch Admission 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 分支陈述覆盖律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "current KZ-E/WFD statement: generic well-factorable lambda_c;",
        "internal support proof: canonical RIW/Buchstab lambda_c only;",
        "therefore:",
        "  canonical source branch => internal support chain;",
        "  generic noncanonical branch => external DI/BFI or PDEC/SAE;",
        "no silent generic internal closure.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `source_lock_input_status={result['source_lock_input_status']}`。",
        f"- `source_lock_input_next_target={result['source_lock_input_next_target']}`。",
        f"- `current_kze_statement_is_generic_wfd={result['current_kze_statement_is_generic_wfd']}`。",
        f"- `canonical_source_branch_is_legal_subcase={result['canonical_source_branch_is_legal_subcase']}`。",
        f"- `internal_canonical_branch_closed_conditionally={result['internal_canonical_branch_closed_conditionally']}`。",
        f"- `original_clean_object_covered_by_branch_split={result['original_clean_object_covered_by_branch_split']}`。",
        f"- `canonical_branch_statement_adopted={result['canonical_branch_statement_adopted']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            "新最窄内部目标为：",
            "",
            "```text",
            "A1CanonicalSourceBranchStatementAndCoverage:",
            "  state the canonical RIW/Buchstab clean branch as the internal no-black-box branch;",
            "  state the generic noncanonical WFD branch as external DI/BFI or PDEC/SAE;",
            "  then the canonical internal support chain is eligible for closure.",
            "```",
            "",
            "这仍不是行命题最终闭合；但它把分支准入硬点压成了主定理/账本陈述合同。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-lock-json", type=Path, default=DEFAULT_SOURCE_LOCK)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.source_lock_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_internal_target": result["next_internal_target"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
