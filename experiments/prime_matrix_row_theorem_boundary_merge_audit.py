#!/usr/bin/env python3
"""审查行命题最终边界闭合是否已并入合著主稿。

用法示例：
  python3 experiments/prime_matrix_row_theorem_boundary_merge_audit.py

输出：
  docs/monograph/prime-matrix-row-theorem-boundary-merge-audit.json
  docs/monograph/prime-matrix-row-theorem-boundary-merge-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph"
DEFAULT_REVIEW = (
    DOCS / "prime-matrix-triad-a1-self-contained-theorem-boundary-review.json"
)
DEFAULT_FINAL = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json"
)
DEFAULT_MAIN_TEX = PAPER / "contradiction-field-monograph.tex"
DEFAULT_COMBINED = DOCS / "combined-monograph-directory-and-theory-system.md"
DEFAULT_STATUS = DOCS / "claim-status-table.md"
DEFAULT_PLAIN = DOCS / "prime-matrix-row-theorem-final-boundary-plain-language.md"
DEFAULT_JSON = DOCS / "prime-matrix-row-theorem-boundary-merge-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-row-theorem-boundary-merge-audit.md"

APPROVED = "Triad-A1 same-set capacity / full-S terminal on the canonical RIW/Buchstab source branch."
REJECTED = "Unrestricted generic full-S well-factorable WFD self-contained theorem."


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """格式化布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    review: dict[str, Any],
    final: dict[str, Any],
    main_tex: str,
    combined: str,
    status_table: str,
    plain: str,
) -> list[dict[str, Any]]:
    """生成合并审查行。"""
    review_closed = (
        review["status"] == "self_contained_theorem_boundary_review_passed"
        and review["theorem_review_verdict"]
        == "APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY"
        and review["terminal_gap_after_review"] == "NoFurtherTheoremBoundaryReviewGap"
        and not review["open_review_gates"]
    )
    final_closed = (
        final["status"]
        == "canonical_source_self_contained_final_closed_generic_unrestricted_refuted"
        and final["canonical_source_self_contained_closed"]
        and final["unrestricted_generic_self_contained_refuted"]
        and not final["unrestricted_generic_self_contained_closed"]
        and not final["open_final_gates"]
    )
    main_absorbed = has_all(
        main_tex,
        [
            "Triad-A1 Self-Contained Theorem-Boundary Closure",
            "Canonical-source self-contained boundary",
            "Unrestricted generic WFD self-contained theorem",
            "not as a final unconditional prime-matrix theorem",
        ],
    )
    combined_absorbed = has_all(
        combined,
        [
            "Triad-A1 自足边界最终评审并入",
            "NoFurtherTheoremBoundaryReviewGap",
            "unrestricted generic WFD 自足版已反证",
        ],
    )
    status_absorbed = has_all(
        status_table,
        [
            "Triad-A1 canonical-source 自足边界",
            "Triad-A1 unrestricted generic WFD 自足版",
            "行命题最终边界合并审查",
        ],
    )
    plain_absorbed = has_all(
        plain,
        [
            "一句话结论",
            "canonical-source 自足边界已完全闭合",
            "unrestricted generic 自足版已反证",
        ],
    )
    no_overclaim_guard = has_all(
        main_tex,
        [
            "It does not assert that the Riemann Hypothesis or the prime-matrix row/column theorem",
            "does not close the final unconditional theorem status",
        ],
    )
    return [
        {
            "gate": "BoundaryReviewPassed",
            "passed": review_closed,
            "evidence": review["theorem_review_verdict"],
            "remaining": "none for theorem-boundary review",
        },
        {
            "gate": "FinalClosureCertificateStillClosed",
            "passed": final_closed,
            "evidence": final["terminal_gap_after_router"],
            "remaining": "none for canonical-source final closure",
        },
        {
            "gate": "MainTexAbsorbsBoundary",
            "passed": main_absorbed,
            "evidence": "main TeX contains theorem-boundary section and no-overclaim wording",
            "remaining": "none if passed",
        },
        {
            "gate": "CombinedOverviewAbsorbsBoundary",
            "passed": combined_absorbed,
            "evidence": "combined overview contains section 17 and terminal review gap",
            "remaining": "none if passed",
        },
        {
            "gate": "ClaimStatusAbsorbsBoundary",
            "passed": status_absorbed,
            "evidence": "claim-status table records closed canonical boundary and refuted generic branch",
            "remaining": "none if passed",
        },
        {
            "gate": "PlainLanguageExplanationPresent",
            "passed": plain_absorbed,
            "evidence": "plain-language boundary note distinguishes closed and not-claimed statements",
            "remaining": "none if passed",
        },
        {
            "gate": "NoGlobalOverclaimGuardPresent",
            "passed": no_overclaim_guard,
            "evidence": "main TeX still blocks promotion to final unconditional row/column theorem",
            "remaining": "global terminal certificates remain separate obligations",
        },
    ]


def run(
    review_path: Path,
    final_path: Path,
    main_tex_path: Path,
    combined_path: Path,
    status_path: Path,
    plain_path: Path,
) -> dict[str, Any]:
    """运行合并审查。"""
    review = load_json(review_path)
    final = load_json(final_path)
    main_tex = read_text(main_tex_path)
    combined = read_text(combined_path)
    status_table = read_text(status_path)
    plain = read_text(plain_path)
    rows = build_rows(review, final, main_tex, combined, status_table, plain)
    passed = all(row["passed"] for row in rows)
    return {
        "certificate_type": "prime_matrix_row_theorem_boundary_merge_audit",
        "status": "row_theorem_boundary_merge_audit_passed" if passed else "row_theorem_boundary_merge_audit_failed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "review_json": file_sha256(review_path),
            "final_closure_json": file_sha256(final_path),
            "main_tex": file_sha256(main_tex_path),
            "combined_overview": file_sha256(combined_path),
            "claim_status_table": file_sha256(status_path),
            "plain_language_note": file_sha256(plain_path),
        },
        "audit_rows": rows,
        "passed_gates": [row["gate"] for row in rows if row["passed"]],
        "open_gates": [row["gate"] for row in rows if not row["passed"]],
        "approved_self_contained_theorem": APPROVED,
        "not_claimed_theorem": REJECTED,
        "merged_boundary_verdict": (
            "CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM"
            if passed
            else "BOUNDARY_MERGE_INCOMPLETE"
        ),
        "remaining_global_obligations": [
            "PDEC family certificates",
            "LocalSurvivorCert family",
            "CleanKLS/DLS certificates or explicit ExternalKLS input",
            "D-structure/Tail-log4/Rankin/referee-block interfaces",
        ],
        "review_conclusion": (
            "合并审查通过：canonical-source 自足边界已经并入主稿、总览、状态表和通俗说明；"
            "unrestricted generic WFD 自足版保持反证且不声明；完整行/列无条件定理仍需单独终端证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审查报告。"""
    lines = [
        "# Prime Matrix 行命题边界闭合合并审查",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 合并裁定",
        "",
        "```text",
        f"verdict: {result['merged_boundary_verdict']}",
        "",
        "approved theorem:",
        f"  {result['approved_self_contained_theorem']}",
        "",
        "not claimed theorem:",
        f"  {result['not_claimed_theorem']}",
        "```",
        "",
        "## 2. 审查门控",
        "",
        "| gate | passed | evidence | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["audit_rows"]:
        lines.append(
            "| `{gate}` | `{passed}` | {evidence} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                passed=fmt_bool(bool(row["passed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 仍未升级为全局无条件定理的义务",
            "",
        ]
    )
    for item in result["remaining_global_obligations"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            "当前没有“边界闭合并入合著”的剩余门；剩余是完整 Prime Matrix 行/列定理的终端证书排斥，"
            "不属于 canonical-source 自足边界闭合本身。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-json", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--final-json", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--main-tex", type=Path, default=DEFAULT_MAIN_TEX)
    parser.add_argument("--combined-md", type=Path, default=DEFAULT_COMBINED)
    parser.add_argument("--status-md", type=Path, default=DEFAULT_STATUS)
    parser.add_argument("--plain-md", type=Path, default=DEFAULT_PLAIN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        review_path=args.review_json,
        final_path=args.final_json,
        main_tex_path=args.main_tex,
        combined_path=args.combined_md,
        status_path=args.status_md,
        plain_path=args.plain_md,
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
                "verdict": result["merged_boundary_verdict"],
                "open_gates": result["open_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
