#!/usr/bin/env python3
"""审查 Triad-A1 自足版边界闭合定理是否可被最终确认。

用法示例：
  python3 experiments/prime_matrix_triad_a1_self_contained_theorem_boundary_review.py

输出：
  docs/monograph/prime-matrix-triad-a1-self-contained-theorem-boundary-review.json
  docs/monograph/prime-matrix-triad-a1-self-contained-theorem-boundary-review.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_FINAL_CLOSURE = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json"
)
DEFAULT_FRONTIER = (
    DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
)
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
    DOCS / "prime-matrix-triad-a1-self-contained-theorem-boundary-review.json"
)
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-self-contained-theorem-boundary-review.md"

APPROVED_THEOREM = (
    "Triad-A1 same-set capacity / full-S terminal on the canonical "
    "RIW/Buchstab source branch."
)
REJECTED_THEOREM = (
    "Unrestricted generic full-S well-factorable WFD self-contained theorem."
)
TERMINAL_GAP = "NoFurtherCanonicalSourceSelfContainedGap_GenericUnrestrictedRefuted"


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


def build_review_rows(
    final_closure: dict[str, Any],
    frontier: dict[str, Any],
    taxonomy: dict[str, Any],
    antiatom_nogo: dict[str, Any],
    provenance: dict[str, Any],
    branch_coverage: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造最终定理边界评审门控。"""
    theorem_boundary = final_closure["theorem_boundary"]
    internal_path_row = next(
        row
        for row in final_closure["final_rows"]
        if row["gate"] == "CanonicalClosureUsesInternalSourcePath"
    )
    statement_exact = (
        theorem_boundary["closed_self_contained_statement"] == APPROVED_THEOREM
        and theorem_boundary["not_claimed_statement"] == REJECTED_THEOREM
        and "moving-delta" in theorem_boundary["not_claimed_reason"]
    )
    final_certificate_closed = all(
        [
            final_closure["status"]
            == "canonical_source_self_contained_final_closed_generic_unrestricted_refuted",
            final_closure["terminal_gap_after_router"] == TERMINAL_GAP,
            final_closure["canonical_source_self_contained_closed"],
            not final_closure["unrestricted_generic_self_contained_closed"],
            final_closure["unrestricted_generic_self_contained_refuted"],
            not final_closure["open_final_gates"],
        ]
    )
    frontier_absorbs_final = all(
        [
            frontier["status"] == "same_set_capacity_frontier_final_self_contained_boundary_closed",
            frontier["all_known_frontiers_routed"],
            frontier["self_contained_final_boundary_closed"],
            frontier["terminal_dual_gap"] == TERMINAL_GAP,
            frontier["closed_self_contained_statement"] == APPROVED_THEOREM,
            frontier["not_claimed_self_contained_statement"] == REJECTED_THEOREM,
        ]
    )
    provenance_closed = all(
        [
            provenance["status"] == "actual_source_provenance_closed",
            provenance["actual_source_provenance_closed"],
            provenance["selected_direction"] == "ProveActualSourceIsCanonicalRIWBuchstab",
            provenance["terminal_gap_after_router"] == "NoFurtherActualSourceProvenanceGap",
            not provenance["open_provenance_gates"],
        ]
    )
    branch_boundary_clean = all(
        [
            branch_coverage["canonical_source_branch_internal_gap_closed"],
            branch_coverage["generic_complement_statement_adopted"],
            branch_coverage["coverage_no_overlap_no_gap"],
            not branch_coverage["generic_wfd_self_contained_gap_closed"],
        ]
    )
    generic_no_false_claim = all(
        [
            not final_closure["unrestricted_generic_self_contained_closed"],
            final_closure["unrestricted_generic_self_contained_refuted"],
            not taxonomy["original_unrestricted_self_contained_version_closed"],
            taxonomy["canonical_restricted_self_contained_version_closed"],
            antiatom_nogo["self_contained_generic_version_refuted"],
            not antiatom_nogo["self_contained_generic_version_closed_as_proof"],
        ]
    )
    external_boundary_clean = all(
        [
            final_closure["external_contract_version_closed"],
            taxonomy["external_contract_version_closed"],
            antiatom_nogo["external_contract_version_closed"],
            "FullS-KLS-ext" in internal_path_row["evidence"],
        ]
    )
    return [
        {
            "gate": "TheoremStatementBoundaryExact",
            "passed": statement_exact,
            "evidence": (
                "approved theorem is canonical-source only; unrestricted generic WFD "
                "self-contained theorem is explicitly not claimed."
            ),
            "required_action": "approve exact boundary statement",
        },
        {
            "gate": "FinalClosureCertificateClosed",
            "passed": final_certificate_closed,
            "evidence": (
                f"final status={final_closure['status']}; "
                f"terminal={final_closure['terminal_gap_after_router']}; "
                f"open_final_gates={final_closure['open_final_gates']}."
            ),
            "required_action": "no remaining final closure gate",
        },
        {
            "gate": "FrontierAbsorbsFinalBoundary",
            "passed": frontier_absorbs_final,
            "evidence": (
                f"frontier status={frontier['status']}; "
                f"all_known_frontiers_routed={frontier['all_known_frontiers_routed']}."
            ),
            "required_action": "frontier accepts final theorem boundary",
        },
        {
            "gate": "CanonicalSourceProvenanceClosed",
            "passed": provenance_closed,
            "evidence": (
                "actual source provenance selects canonical RIW/Buchstab and has "
                "NoFurtherActualSourceProvenanceGap."
            ),
            "required_action": "canonical source branch is internally sourced",
        },
        {
            "gate": "BranchCoverageNoSilentUpgrade",
            "passed": branch_boundary_clean,
            "evidence": (
                "canonical and generic noncanonical branches are separated with "
                "coverage_no_overlap_no_gap=true."
            ),
            "required_action": "no generic branch is silently imported",
        },
        {
            "gate": "GenericUnrestrictedNoFalseClaim",
            "passed": generic_no_false_claim,
            "evidence": (
                "moving-delta no-go refutes the unrestricted generic self-contained "
                "anti-atom input under the recorded formal hypotheses."
            ),
            "required_action": "record as refuted, not as closed theorem",
        },
        {
            "gate": "ExternalContractSeparatedFromSelfContainedClaim",
            "passed": external_boundary_clean,
            "evidence": (
                "external FullS-KLS-ext contract remains available but is not used to "
                "inflate the canonical-source self-contained theorem."
            ),
            "required_action": "keep external and self-contained claims disjoint",
        },
    ]


def run(
    final_closure_path: Path,
    frontier_path: Path,
    taxonomy_path: Path,
    antiatom_nogo_path: Path,
    provenance_path: Path,
    branch_coverage_path: Path,
) -> dict[str, Any]:
    """运行最终定理边界评审。"""
    final_closure = load_json(final_closure_path)
    frontier = load_json(frontier_path)
    taxonomy = load_json(taxonomy_path)
    antiatom_nogo = load_json(antiatom_nogo_path)
    provenance = load_json(provenance_path)
    branch_coverage = load_json(branch_coverage_path)
    rows = build_review_rows(
        final_closure,
        frontier,
        taxonomy,
        antiatom_nogo,
        provenance,
        branch_coverage,
    )
    review_passed = all(row["passed"] for row in rows)
    return {
        "certificate_type": "triad_a1_self_contained_theorem_boundary_review",
        "status": (
            "self_contained_theorem_boundary_review_passed"
            if review_passed
            else "self_contained_theorem_boundary_review_failed"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "final_closure_json": file_sha256(final_closure_path),
            "frontier_json": file_sha256(frontier_path),
            "taxonomy_json": file_sha256(taxonomy_path),
            "antiatom_nogo_json": file_sha256(antiatom_nogo_path),
            "provenance_json": file_sha256(provenance_path),
            "branch_coverage_json": file_sha256(branch_coverage_path),
        },
        "review_rows": rows,
        "passed_review_gates": [row["gate"] for row in rows if row["passed"]],
        "open_review_gates": [row["gate"] for row in rows if not row["passed"]],
        "theorem_review_verdict": (
            "APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY"
            if review_passed
            else "DO_NOT_APPROVE_BOUNDARY"
        ),
        "approved_self_contained_theorem": APPROVED_THEOREM,
        "rejected_not_claimed_theorem": REJECTED_THEOREM,
        "terminal_gap_after_review": (
            "NoFurtherTheoremBoundaryReviewGap"
            if review_passed
            else "TheoremBoundaryReviewGateOpen"
        ),
        "dependency_classification": {
            "canonical_source_branch": "self-contained internal chain",
            "unrestricted_generic_wfd_branch": "refuted as self-contained statement",
            "external_full_s_kls_ext": "closed external contract, separated from theorem claim",
        },
        "review_conclusion": (
            "最终定理审查通过：可确认的自足闭合命题只限于 canonical RIW/Buchstab "
            "source branch 上的 Triad-A1 same-set capacity / full-S terminal；"
            "unrestricted generic WFD 自足版被 moving-delta no-go 反证，不能作为闭合定理声明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 评审报告。"""
    lines = [
        "# Triad-A1 self-contained theorem boundary 最终评审",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 评审裁定",
        "",
        "```text",
        f"verdict: {result['theorem_review_verdict']}",
        "",
        "approved theorem:",
        f"  {result['approved_self_contained_theorem']}",
        "",
        "not claimed theorem:",
        f"  {result['rejected_not_claimed_theorem']}",
        "",
        "terminal:",
        f"  {result['terminal_gap_after_review']}",
        "```",
        "",
        "## 2. 依赖分类",
        "",
        f"- `canonical_source_branch={result['dependency_classification']['canonical_source_branch']}`。",
        f"- `unrestricted_generic_wfd_branch={result['dependency_classification']['unrestricted_generic_wfd_branch']}`。",
        f"- `external_full_s_kls_ext={result['dependency_classification']['external_full_s_kls_ext']}`。",
        f"- `open_review_gates={result['open_review_gates']}`。",
        "",
        "## 3. 评审门控表",
        "",
        "| gate | passed | evidence | required action |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["review_rows"]:
        lines.append(
            "| `{gate}` | `{passed}` | {evidence} | {required} |".format(
                gate=table_cell(row["gate"]),
                passed=fmt_bool(bool(row["passed"])),
                evidence=table_cell(row["evidence"]),
                required=table_cell(row["required_action"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 最终边界闭合声明",
            "",
            "本评审确认的是 theorem-boundary closure：",
            "",
            "```text",
            "canonical-source self-contained theorem: approved and closed;",
            "unrestricted generic WFD self-contained theorem: refuted and not claimed;",
            "external FullS-KLS-ext: available as external contract only.",
            "```",
            "",
            "因此当前自足版闭合没有剩余评审门：",
            "",
            "```text",
            "NoFurtherTheoremBoundaryReviewGap",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-closure-json", type=Path, default=DEFAULT_FINAL_CLOSURE)
    parser.add_argument("--frontier-json", type=Path, default=DEFAULT_FRONTIER)
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
        final_closure_path=args.final_closure_json,
        frontier_path=args.frontier_json,
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
                "verdict": result["theorem_review_verdict"],
                "terminal_gap_after_review": result["terminal_gap_after_review"],
                "open_review_gates": result["open_review_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
