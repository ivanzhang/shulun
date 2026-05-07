#!/usr/bin/env python3
"""闭合 canonical-source 自足版并隔离 unrestricted generic 反证版。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_self_contained_final_closure_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_TAXONOMY = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
)
DEFAULT_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_PROVENANCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_BRANCH_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.md"
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


def build_rows(
    taxonomy: dict[str, Any],
    antiatom_nogo: dict[str, Any],
    provenance: dict[str, Any],
    branch_coverage: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造最终自足闭合账本。"""
    canonical_source_closed = all(
        [
            taxonomy["canonical_restricted_self_contained_version_closed"],
            provenance["actual_source_provenance_closed"],
            provenance["terminal_gap_after_router"] == "NoFurtherActualSourceProvenanceGap",
            not provenance["open_provenance_gates"],
        ]
    )
    generic_unrestricted_refuted = all(
        [
            antiatom_nogo["self_contained_generic_version_refuted"],
            not antiatom_nogo["self_contained_generic_version_closed_as_proof"],
            not taxonomy["original_unrestricted_self_contained_version_closed"],
        ]
    )
    branch_boundary_closed = all(
        [
            branch_coverage["canonical_source_branch_internal_gap_closed"],
            branch_coverage["generic_complement_statement_adopted"],
            branch_coverage["coverage_no_overlap_no_gap"],
            branch_coverage["generic_wfd_self_contained_gap_closed"] is False,
        ]
    )
    no_external_dependency_for_canonical = canonical_source_closed and (
        provenance["selected_direction"] == "ProveActualSourceIsCanonicalRIWBuchstab"
    )
    final_closed = all(
        [
            canonical_source_closed,
            generic_unrestricted_refuted,
            branch_boundary_closed,
            no_external_dependency_for_canonical,
        ]
    )
    return [
        {
            "gate": "CanonicalSourceSelfContainedTheoremClosed",
            "closed": canonical_source_closed,
            "evidence": (
                "frontier terminal is NoFurtherActualSourceProvenanceGap and provenance "
                "has no open gates."
            ),
            "remaining": "none for canonical-source self-contained theorem",
            "next_target": "SelfContainedBoundary",
        },
        {
            "gate": "UnrestrictedGenericSelfContainedRefuted",
            "closed": generic_unrestricted_refuted,
            "evidence": (
                "moving-delta no-go refutes the current generic full-S WFD anti-atom "
                "under recorded formal hypotheses."
            ),
            "remaining": "do not claim unrestricted generic self-contained proof",
            "next_target": "SelfContainedBoundary",
        },
        {
            "gate": "BranchBoundaryNoOverlapNoGap",
            "closed": branch_boundary_closed,
            "evidence": (
                "branch coverage separates canonical source branch from generic noncanonical "
                "WFD complement."
            ),
            "remaining": "none at statement-boundary level",
            "next_target": "SelfContainedBoundary",
        },
        {
            "gate": "CanonicalClosureUsesInternalSourcePath",
            "closed": no_external_dependency_for_canonical,
            "evidence": (
                "selected source path is canonical RIW/Buchstab; FullS-KLS-ext is not needed "
                "for this branch."
            ),
            "remaining": "none for canonical-source internal path",
            "next_target": "FinalSelfContainedClosureCertificate",
        },
        {
            "gate": "FinalSelfContainedClosureCertificate",
            "closed": final_closed,
            "evidence": (
                "The exact self-contained theorem boundary is closed: canonical-source version "
                "is proved by the internal chain; unrestricted generic version is refuted, not open."
            ),
            "remaining": "none, provided the theorem statement is canonical-source self-contained",
            "next_target": "NoFurtherCanonicalSourceSelfContainedGap",
        },
    ]


def run(
    taxonomy_path: Path,
    antiatom_nogo_path: Path,
    provenance_path: Path,
    branch_coverage_path: Path,
) -> dict[str, Any]:
    """运行最终自足闭合路由。"""
    # 最终证书只读取独立上游账本，避免与总前沿 router 形成循环哈希依赖。
    taxonomy = load_json(taxonomy_path)
    antiatom_nogo = load_json(antiatom_nogo_path)
    provenance = load_json(provenance_path)
    branch_coverage = load_json(branch_coverage_path)
    rows = build_rows(
        taxonomy,
        antiatom_nogo,
        provenance,
        branch_coverage,
    )
    final_closed = all(row["closed"] for row in rows)
    return {
        "certificate_type": "triad_a1_dibfi_self_contained_final_closure_router",
        "status": (
            "canonical_source_self_contained_final_closed_generic_unrestricted_refuted"
            if final_closed
            else "self_contained_final_closure_incomplete"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "taxonomy_json": file_sha256(taxonomy_path),
            "antiatom_nogo_json": file_sha256(antiatom_nogo_path),
            "provenance_json": file_sha256(provenance_path),
            "branch_coverage_json": file_sha256(branch_coverage_path),
        },
        "final_rows": rows,
        "closed_final_gates": [row["gate"] for row in rows if row["closed"]],
        "open_final_gates": [row["gate"] for row in rows if not row["closed"]],
        "canonical_source_self_contained_closed": final_closed,
        "unrestricted_generic_self_contained_closed": False,
        "unrestricted_generic_self_contained_refuted": antiatom_nogo[
            "self_contained_generic_version_refuted"
        ],
        "external_contract_version_closed": all(
            [
                taxonomy["external_contract_version_closed"],
                antiatom_nogo["external_contract_version_closed"],
            ]
        ),
        "terminal_gap_after_router": (
            "NoFurtherCanonicalSourceSelfContainedGap_GenericUnrestrictedRefuted"
            if final_closed
            else "FinalSelfContainedClosureCertificateOpen"
        ),
        "theorem_boundary": {
            "closed_self_contained_statement": (
                "Triad-A1 same-set capacity / full-S terminal on the canonical "
                "RIW/Buchstab source branch."
            ),
            "not_claimed_statement": (
                "Unrestricted generic full-S well-factorable WFD self-contained theorem."
            ),
            "not_claimed_reason": "moving-delta no-go refutes the generic anti-atom input.",
        },
        "structural_law": (
            "The final self-contained closure is a theorem-boundary closure. The canonical-source "
            "branch is fully internal after source provenance is closed. The unrestricted generic "
            "WFD branch is not an open self-contained gap; it is false under the current formal "
            "hypotheses. Therefore the only honest final statement is canonical-source "
            "self-contained closure plus explicit generic-unrestricted refutation."
        ),
        "review_conclusion": (
            "完整自足版的可闭合陈述已闭合：canonical RIW/Buchstab source branch 走内部链条，"
            "来源账本无剩余缺口；unrestricted generic WFD 自足版被 moving-delta 反证，"
            "不能被写成自足闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI self-contained final closure 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 最终边界律",
        "",
        result["structural_law"],
        "",
        "```text",
        "closed self-contained statement:",
        f"  {result['theorem_boundary']['closed_self_contained_statement']};",
        "",
        "not claimed:",
        f"  {result['theorem_boundary']['not_claimed_statement']};",
        "",
        "reason:",
        f"  {result['theorem_boundary']['not_claimed_reason']};",
        "",
        "terminal:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `canonical_source_self_contained_closed={fmt_bool(result['canonical_source_self_contained_closed'])}`。",
        f"- `unrestricted_generic_self_contained_closed={fmt_bool(result['unrestricted_generic_self_contained_closed'])}`。",
        f"- `unrestricted_generic_self_contained_refuted={fmt_bool(result['unrestricted_generic_self_contained_refuted'])}`。",
        f"- `external_contract_version_closed={fmt_bool(result['external_contract_version_closed'])}`。",
        f"- `closed_final_gates={result['closed_final_gates']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 最终闭合表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["final_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "canonical-source 自足版已经无剩余终端：",
            "",
            "```text",
            "NoFurtherCanonicalSourceSelfContainedGap_GenericUnrestrictedRefuted",
            "```",
            "",
            "这不是 unrestricted generic WFD 自足证明；后者已被反证，必须保持为未声明命题。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--taxonomy-json", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--antiatom-nogo-json", type=Path, default=DEFAULT_ANTIATOM_NOGO)
    parser.add_argument("--provenance-json", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument(
        "--branch-coverage-json",
        type=Path,
        default=DEFAULT_BRANCH_COVERAGE,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        taxonomy_path=args.taxonomy_json,
        antiatom_nogo_path=args.antiatom_nogo_json,
        provenance_path=args.provenance_json,
        branch_coverage_path=args.branch_coverage_json,
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
                "open_final_gates": result["open_final_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
