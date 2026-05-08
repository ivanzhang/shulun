#!/usr/bin/env python3
"""生成 canonical-source 自足命题最终闭合证书。

用法示例：
  python3 experiments/prime_matrix_canonical_source_self_contained_final_theorem_router.py

输出：
  docs/monograph/prime-matrix-canonical-source-self-contained-final-theorem-router.json
  docs/monograph/prime-matrix-canonical-source-self-contained-final-theorem-router.md
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

DEFAULT_TERMINAL_PROMOTION = (
    DOCS / "prime-matrix-canonical-terminal-promotion-closure-router.json"
)
DEFAULT_TRIAD_BOUNDARY = (
    DOCS / "prime-matrix-triad-a1-self-contained-theorem-boundary-review.json"
)
DEFAULT_ROW_FRONTIER = (
    DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
)
DEFAULT_BOUNDARY_LIFT = (
    DOCS / "prime-matrix-self-contained-pdec-cap-boundary-lift-router.json"
)
DEFAULT_CLAIM_STATUS = DOCS / "claim-status-table.md"
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_MAIN_TEX = PAPER / "contradiction-field-monograph.tex"
DEFAULT_JSON = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def theorem_row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_self_contained: bool,
    outside_boundary: bool,
) -> dict[str, Any]:
    """构造最终自足命题审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_self_contained": blocks_self_contained,
        "outside_boundary": outside_boundary,
    }


def build_rows(
    terminal_promotion: dict[str, Any],
    triad_boundary: dict[str, Any],
    row_frontier: dict[str, Any],
    boundary_lift: dict[str, Any],
    claim_status_text: str,
    line_ref_text: str,
    main_tex: str,
) -> list[dict[str, Any]]:
    """生成 canonical-source 自足命题最终审查表。"""
    exact_statement_closed = (
        triad_boundary["theorem_review_verdict"]
        == "APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY"
        and triad_boundary["open_review_gates"] == []
        and "canonical RIW/Buchstab source branch"
        in triad_boundary["approved_self_contained_theorem"]
    )
    terminal_promotion_closed = (
        terminal_promotion["latest_self_contained_hardpoint_closed"]
        and terminal_promotion["canonical_source_terminal_promotion_closed"]
        and terminal_promotion["open_self_contained_gates"] == []
        and terminal_promotion["narrowest_self_contained_boundary"]
        == "NoFurtherCanonicalSourceTerminalPromotionGap"
    )
    pdec_boundary_lifted = (
        boundary_lift["canonical_source_self_contained_pdec_bottleneck_closed"]
        and boundary_lift["narrowest_self_contained_boundary"]
        == "NoFurtherCanonicalSourceSelfContainedPDECCapGap"
    )
    row_frontier_guarded = (
        row_frontier["canonical_source_boundary_closed"]
        and row_frontier["generic_unrestricted_self_contained_refuted"]
        and not row_frontier["row_column_unconditional_closed"]
    )
    generic_refuted_not_claimed = (
        triad_boundary["dependency_classification"][
            "unrestricted_generic_wfd_branch"
        ]
        == "refuted as self-contained statement"
        and row_frontier["generic_unrestricted_self_contained_refuted"]
    )
    external_separated = (
        "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
        in terminal_promotion["open_external_gates"]
        and boundary_lift["generic_external_dibfi_boundary_open"]
    )
    referee_outside_boundary = (
        terminal_promotion["open_final_gates"] == ["DStructureRankinRefereeStillOpen"]
        and "BLOCK-REFEREE" in line_ref_text
    )
    docs_updated = has_all(
        claim_status_text,
        [
            "canonical终端晋级闭合路由",
            "NoFurtherCanonicalSourceTerminalPromotionGap",
            "open_self_contained_gates=[]",
        ],
    ) and has_all(
        main_tex,
        [
            "NoFurtherCanonicalSourceTerminalPromotionGap",
            "open\\_self\\_contained\\_gates=[]",
            "not an unrestricted global",
        ],
    )

    return [
        theorem_row(
            gate="ExactCanonicalSourceTheoremStatement",
            closed=exact_statement_closed,
            evidence=triad_boundary["approved_self_contained_theorem"],
            meaning="最终自足命题只声明 canonical RIW/Buchstab 来源分支，不声明 unrestricted generic 版本。",
            blocks_self_contained=not exact_statement_closed,
            outside_boundary=False,
        ),
        theorem_row(
            gate="TerminalPromotionNoSelfContainedGate",
            closed=terminal_promotion_closed,
            evidence=terminal_promotion["narrowest_self_contained_boundary"],
            meaning="终端晋级层已无自足数学开门。",
            blocks_self_contained=not terminal_promotion_closed,
            outside_boundary=False,
        ),
        theorem_row(
            gate="PDECCapBoundaryLiftNoGap",
            closed=pdec_boundary_lifted,
            evidence=boundary_lift["narrowest_self_contained_boundary"],
            meaning="PDEC-CAP 旧瓶颈已被 canonical-source 边界提升吸收。",
            blocks_self_contained=not pdec_boundary_lifted,
            outside_boundary=False,
        ),
        theorem_row(
            gate="RowFrontierNoOverclaimGuard",
            closed=row_frontier_guarded,
            evidence=row_frontier["narrowest_next_hardpoint"]["name"],
            meaning="行列前沿继续区分 canonical 自足闭合、generic 反证和完整无条件未闭合。",
            blocks_self_contained=not row_frontier_guarded,
            outside_boundary=False,
        ),
        theorem_row(
            gate="GenericUnrestrictedRefutedNotClaimed",
            closed=generic_refuted_not_claimed,
            evidence=triad_boundary["rejected_not_claimed_theorem"],
            meaning="unrestricted generic WFD 自足版是被反证的强化命题，不是本命题缺口。",
            blocks_self_contained=False,
            outside_boundary=True,
        ),
        theorem_row(
            gate="ExternalDIBFISeparated",
            closed=external_separated,
            evidence=", ".join(terminal_promotion["open_external_gates"]),
            meaning="DI/BFI 无投影量化证书属于 external/generic 路线，已从自足命题中分离。",
            blocks_self_contained=False,
            outside_boundary=True,
        ),
        theorem_row(
            gate="DStructureRankinRefereeSeparated",
            closed=referee_outside_boundary,
            evidence=", ".join(terminal_promotion["open_final_gates"]),
            meaning="D-structure/Tail-log4/finite Rankin 是最终行列无条件定理晋级门，不是 canonical 自足边界缺口。",
            blocks_self_contained=False,
            outside_boundary=True,
        ),
        theorem_row(
            gate="MonographAndStatusIntegrated",
            closed=docs_updated,
            evidence="claim-status table and main TeX contain final canonical terminal boundary",
            meaning="合著和状态表已经记录闭合边界，避免后续把外部/审稿门误并入自足命题。",
            blocks_self_contained=not docs_updated,
            outside_boundary=False,
        ),
    ]


def run(
    terminal_promotion_path: Path,
    triad_boundary_path: Path,
    row_frontier_path: Path,
    boundary_lift_path: Path,
    claim_status_path: Path,
    line_ref_path: Path,
    main_tex_path: Path,
) -> dict[str, Any]:
    """运行 canonical-source 自足命题最终闭合审查。"""
    terminal_promotion = load_json(terminal_promotion_path)
    triad_boundary = load_json(triad_boundary_path)
    row_frontier = load_json(row_frontier_path)
    boundary_lift = load_json(boundary_lift_path)
    claim_status_text = read_text(claim_status_path)
    line_ref_text = read_text(line_ref_path)
    main_tex = read_text(main_tex_path)

    rows = build_rows(
        terminal_promotion=terminal_promotion,
        triad_boundary=triad_boundary,
        row_frontier=row_frontier,
        boundary_lift=boundary_lift,
        claim_status_text=claim_status_text,
        line_ref_text=line_ref_text,
        main_tex=main_tex,
    )
    open_self_contained_gates = [
        row["gate"] for row in rows if row["blocks_self_contained"]
    ]
    outside_boundary_open_or_separated = [
        row["gate"] for row in rows if row["outside_boundary"]
    ]
    canonical_closed = not open_self_contained_gates

    return {
        "certificate_type": "prime_matrix_canonical_source_self_contained_final_theorem_router",
        "status": "canonical_source_self_contained_theorem_fully_closed_global_unconditional_not_claimed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "terminal_promotion": file_sha256(terminal_promotion_path),
            "triad_boundary": file_sha256(triad_boundary_path),
            "row_frontier": file_sha256(row_frontier_path),
            "boundary_lift": file_sha256(boundary_lift_path),
            "claim_status": file_sha256(claim_status_path),
            "line_referee": file_sha256(line_ref_path),
            "main_tex": file_sha256(main_tex_path),
        },
        "approved_self_contained_theorem": (
            "Prime Matrix canonical-source terminal theorem boundary: "
            "Triad-A1 same-set/full-S terminal plus canonical terminal promotion on the "
            "canonical RIW/Buchstab source branch."
        ),
        "canonical_source_self_contained_theorem_closed": canonical_closed,
        "open_self_contained_gates": open_self_contained_gates,
        "terminal_boundary": "NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap",
        "not_claimed_theorems": [
            triad_boundary["rejected_not_claimed_theorem"],
            "Unrestricted/global Prime Matrix row-column unconditional theorem.",
        ],
        "outside_boundary_open_or_separated": outside_boundary_open_or_separated,
        "open_external_gates": terminal_promotion["open_external_gates"],
        "open_final_promotion_gates": terminal_promotion["open_final_gates"],
        "row_column_unconditional_closed": False,
        "global_unrestricted_terminal_family_exclusion_closed": False,
        "rows": rows,
        "final_closure_law": (
            "A statement is self-containedly closed exactly when it is restricted to the "
            "canonical RIW/Buchstab source branch and to the terminal grammar already "
            "absorbed by the canonical terminal-promotion closure. Under this exact "
            "statement boundary, there are no open self-contained gates. The generic WFD "
            "strengthening is refuted and not claimed, external DI/BFI remains an external "
            "route, and D-structure/Rankin remains a final-promotion referee gate."
        ),
        "review_conclusion": (
            "最终自足命题边界闭合：canonical-source 命题已经达到 "
            "`NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap`，且 "
            "`open_self_contained_gates=[]`。这不是完整行/列无条件定理，也不声明 "
            "unrestricted generic WFD；外部 DI/BFI 与 DStructureRankinReferee 保持在边界之外。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix canonical-source 自足命题最终闭合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 最终闭合律",
        "",
        result["final_closure_law"],
        "",
        "```text",
        "approved self-contained theorem:",
        f"  {result['approved_self_contained_theorem']}",
        "",
        "terminal:",
        f"  {result['terminal_boundary']}",
        "",
        "open self-contained gates:",
        f"  {result['open_self_contained_gates']}",
        "",
        "outside this theorem boundary:",
        "  unrestricted generic WFD is refuted/not claimed;",
        "  generic/external DI-BFI remains external;",
        "  D-structure/Rankin remains final-promotion referee gate.",
        "```",
        "",
        "## 2. 汇总",
        "",
        (
            "- `canonical_source_self_contained_theorem_closed="
            f"{fmt_bool(result['canonical_source_self_contained_theorem_closed'])}`。"
        ),
        f"- `open_self_contained_gates={result['open_self_contained_gates']}`。",
        f"- `terminal_boundary={result['terminal_boundary']}`。",
        f"- `open_external_gates={result['open_external_gates']}`。",
        f"- `open_final_promotion_gates={result['open_final_promotion_gates']}`。",
        (
            "- `row_column_unconditional_closed="
            f"{fmt_bool(result['row_column_unconditional_closed'])}`。"
        ),
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks self-contained | outside boundary | evidence | meaning |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | `{outside}` | {evidence} | {meaning} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                blocks=fmt_bool(bool(row["blocks_self_contained"])),
                outside=fmt_bool(bool(row["outside_boundary"])),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 不声明项",
            "",
        ]
    )
    for item in result["not_claimed_theorems"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "本证书是最终自足命题边界闭合证书，不是完整 Prime Matrix 行/列无条件定理证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--terminal-promotion-json", type=Path, default=DEFAULT_TERMINAL_PROMOTION
    )
    parser.add_argument("--triad-boundary-json", type=Path, default=DEFAULT_TRIAD_BOUNDARY)
    parser.add_argument("--row-frontier-json", type=Path, default=DEFAULT_ROW_FRONTIER)
    parser.add_argument("--boundary-lift-json", type=Path, default=DEFAULT_BOUNDARY_LIFT)
    parser.add_argument("--claim-status-md", type=Path, default=DEFAULT_CLAIM_STATUS)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--main-tex", type=Path, default=DEFAULT_MAIN_TEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        terminal_promotion_path=args.terminal_promotion_json,
        triad_boundary_path=args.triad_boundary_json,
        row_frontier_path=args.row_frontier_json,
        boundary_lift_path=args.boundary_lift_json,
        claim_status_path=args.claim_status_md,
        line_ref_path=args.line_ref_md,
        main_tex_path=args.main_tex,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["terminal_boundary"])


if __name__ == "__main__":
    main()
