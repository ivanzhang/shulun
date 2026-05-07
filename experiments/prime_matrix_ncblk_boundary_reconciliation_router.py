#!/usr/bin/env python3
"""核查 NC-BLK 与 canonical-source 边界闭合之间的关系。

用法示例：
  python3 experiments/prime_matrix_ncblk_boundary_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-ncblk-boundary-reconciliation-router.json
  docs/monograph/prime-matrix-ncblk-boundary-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_ROW_FRONTIER = DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
DEFAULT_SAME_SET = DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
DEFAULT_BOUNDARY_REVIEW = DOCS / "prime-matrix-triad-a1-self-contained-theorem-boundary-review.json"
DEFAULT_BOUNDARY_MERGE = DOCS / "prime-matrix-row-theorem-boundary-merge-audit.json"
DEFAULT_NCBLK_ALIGNMENT = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    row_frontier: dict[str, Any],
    same_set: dict[str, Any],
    boundary_review: dict[str, Any],
    boundary_merge: dict[str, Any],
    ncblk_alignment: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成边界核查行。"""
    return [
        {
            "gate": "RowFrontierPinsNCBLK",
            "closed": row_frontier["narrowest_next_hardpoint"]["name"]
            == "NonTautologicalPDECOrNCBLK",
            "evidence": row_frontier["narrowest_next_hardpoint"]["name"],
            "meaning": "总前沿已把 CleanKLS 宽口径压到 NC-BLK 或非二点 PDEC。",
        },
        {
            "gate": "CanonicalSameSetBoundaryClosed",
            "closed": bool(
                same_set["status"]
                == "same_set_capacity_frontier_final_self_contained_boundary_closed"
                and same_set["canonical_restricted_self_contained_version_closed"]
                and same_set["self_contained_final_boundary_closed"]
            ),
            "evidence": same_set["terminal_dual_gap"],
            "meaning": "canonical RIW/Buchstab source branch 的同集容量/Full-S 终端已闭合。",
        },
        {
            "gate": "BoundaryReviewNoOpenGate",
            "closed": bool(
                boundary_review["status"]
                == "self_contained_theorem_boundary_review_passed"
                and not boundary_review["open_review_gates"]
            ),
            "evidence": boundary_review["status"],
            "meaning": "定理边界审查无剩余门。",
        },
        {
            "gate": "GenericUnrestrictedNotImported",
            "closed": bool(same_set["unrestricted_generic_self_contained_refuted"]),
            "evidence": same_set["not_claimed_self_contained_statement"],
            "meaning": "generic WFD 自足版保持反证，不能偷渡进 canonical 闭合。",
        },
        {
            "gate": "NCBLKGenericBranchStillExternal",
            "closed": bool(
                ncblk_alignment["terminal_gap_after_router"]
                == "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov"
                and ncblk_alignment["open_alignment_gates"]
            ),
            "evidence": ncblk_alignment["terminal_gap_after_router"],
            "meaning": "full-S non-AP generic NC-BLK 仍只能走 exact source entropy 或外部定理。",
        },
        {
            "gate": "NoGlobalRowColumnUpgrade",
            "closed": bool(
                boundary_merge["merged_boundary_verdict"]
                == "CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM"
                and boundary_merge["remaining_global_obligations"]
            ),
            "evidence": ", ".join(boundary_merge["remaining_global_obligations"]),
            "meaning": "完整行/列无条件定理仍需独立终端证书，不能由 canonical 边界替代。",
        },
    ]


def run(
    row_frontier_path: Path,
    same_set_path: Path,
    boundary_review_path: Path,
    boundary_merge_path: Path,
    ncblk_alignment_path: Path,
) -> dict[str, Any]:
    """运行 NC-BLK 边界核查。"""
    row_frontier = load_json(row_frontier_path)
    same_set = load_json(same_set_path)
    boundary_review = load_json(boundary_review_path)
    boundary_merge = load_json(boundary_merge_path)
    ncblk_alignment = load_json(ncblk_alignment_path)
    rows = build_rows(
        row_frontier=row_frontier,
        same_set=same_set,
        boundary_review=boundary_review,
        boundary_merge=boundary_merge,
        ncblk_alignment=ncblk_alignment,
    )
    all_reconciled = all(row["closed"] for row in rows)
    return {
        "certificate_type": "prime_matrix_ncblk_boundary_reconciliation_router",
        "status": "ncblk_reconciled_with_canonical_boundary_global_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "row_frontier": file_sha256(row_frontier_path),
            "same_set_capacity_frontier": file_sha256(same_set_path),
            "boundary_review": file_sha256(boundary_review_path),
            "boundary_merge": file_sha256(boundary_merge_path),
            "ncblk_branch_alignment": file_sha256(ncblk_alignment_path),
        },
        "all_reconciliation_gates_passed": all_reconciled,
        "canonical_ncblk_absorbed_by_existing_boundary": True,
        "generic_ncblk_self_contained_not_claimed": True,
        "row_column_unconditional_closed": False,
        "row_frontier_before_reconciliation": row_frontier["narrowest_next_hardpoint"][
            "name"
        ],
        "canonical_closed_statement": same_set["closed_self_contained_statement"],
        "not_claimed_statement": same_set["not_claimed_self_contained_statement"],
        "remaining_global_obligations": boundary_merge["remaining_global_obligations"],
        "rows": rows,
        "reconciliation_law": (
            "NC-BLK must be read through the theorem boundary. On the canonical "
            "RIW/Buchstab source branch, the existing same-set capacity frontier and final "
            "boundary review have already absorbed the NC-BLK clean-KLS chain. On the broader "
            "full-S non-AP generic WFD branch, NC-BLK is still an external/exact-source-entropy "
            "route and must not be imported into the self-contained claim. Therefore this "
            "reconciles the NC-BLK label but does not close the full row/column theorem."
        ),
        "review_conclusion": (
            "NC-BLK 不是新的无名 CleanKLS 出口：在 canonical-source A1 分支中，它已经被既有"
            "同集容量最终边界吸收；在 generic full-S non-AP 分支中，它仍保持外部/精确源熵路线，"
            "不能冒充自足闭合。完整行/列无条件定理仍未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix NC-BLK 边界核查路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 边界核查律",
        "",
        result["reconciliation_law"],
        "",
        "```text",
        "canonical source branch:",
        "  NC-BLK clean-KLS chain is absorbed by the existing same-set capacity boundary;",
        "generic full-S non-AP branch:",
        "  NC-BLK remains exact source entropy or external DI/BFI/Kuznetsov;",
        "therefore:",
        "  no unnamed CleanKLS exit remains, but the global row/column theorem is not closed.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_reconciliation_gates_passed={fmt_bool(result['all_reconciliation_gates_passed'])}`。",
        f"- `canonical_ncblk_absorbed_by_existing_boundary={fmt_bool(result['canonical_ncblk_absorbed_by_existing_boundary'])}`。",
        f"- `generic_ncblk_self_contained_not_claimed={fmt_bool(result['generic_ncblk_self_contained_not_claimed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `row_frontier_before_reconciliation={result['row_frontier_before_reconciliation']}`。",
        "",
        "## 3. 核查表",
        "",
        "| gate | closed | evidence | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {meaning} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 剩余全局义务",
            "",
        ]
    )
    for obligation in result["remaining_global_obligations"]:
        lines.append(f"- `{obligation}`")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--row-frontier-json", type=Path, default=DEFAULT_ROW_FRONTIER)
    parser.add_argument("--same-set-json", type=Path, default=DEFAULT_SAME_SET)
    parser.add_argument(
        "--boundary-review-json", type=Path, default=DEFAULT_BOUNDARY_REVIEW
    )
    parser.add_argument("--boundary-merge-json", type=Path, default=DEFAULT_BOUNDARY_MERGE)
    parser.add_argument("--ncblk-alignment-json", type=Path, default=DEFAULT_NCBLK_ALIGNMENT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        row_frontier_path=args.row_frontier_json,
        same_set_path=args.same_set_json,
        boundary_review_path=args.boundary_review_json,
        boundary_merge_path=args.boundary_merge_json,
        ncblk_alignment_path=args.ncblk_alignment_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["all_reconciliation_gates_passed"])


if __name__ == "__main__":
    main()
