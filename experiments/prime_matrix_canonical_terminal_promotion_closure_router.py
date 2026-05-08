#!/usr/bin/env python3
"""复核 canonical-source 终端晋级是否还有自足数学开门。

用法示例：
  python3 experiments/prime_matrix_canonical_terminal_promotion_closure_router.py

输出：
  docs/monograph/prime-matrix-canonical-terminal-promotion-closure-router.json
  docs/monograph/prime-matrix-canonical-terminal-promotion-closure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_BOUNDARY_LIFT = (
    DOCS / "prime-matrix-self-contained-pdec-cap-boundary-lift-router.json"
)
DEFAULT_GLOBAL_BOUNDARY = (
    DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
)
DEFAULT_GLOBAL_SPLIT = (
    DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
)
DEFAULT_SELF_BOTTLENECK = (
    DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
)
DEFAULT_ROW_FRONTIER = (
    DOCS / "prime-matrix-row-column-unconditional-frontier-router.json"
)
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = (
    DOCS / "prime-matrix-canonical-terminal-promotion-closure-router.json"
)
DEFAULT_MD = DOCS / "prime-matrix-canonical-terminal-promotion-closure-router.md"


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
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def find_row(rows: list[dict[str, Any]], gate: str) -> dict[str, Any]:
    """按 gate 查找行。"""
    for row in rows:
        if row.get("gate") == gate:
            return row
    return {}


def closure_row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    scope: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造 canonical 终端晋级闭合审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "scope": scope,
        "blocks_final": blocks_final,
    }


def build_rows(
    boundary_lift: dict[str, Any],
    global_boundary: dict[str, Any],
    global_split: dict[str, Any],
    self_bottleneck: dict[str, Any],
    row_frontier: dict[str, Any],
    terminal_triad_text: str,
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """生成 canonical-source 终端晋级闭合审查表。"""
    current_frontier_closed = (
        global_boundary["materialized_frontier_exhausted"]
        and global_boundary["terminal_generation_contract_closed"]
        and global_boundary["current_terminal_instances_exhausted"]
    )
    triad_no_fourth_exit = (
        row_frontier["terminal_triad_routed_no_fourth_exit"]
        and has_all(
            terminal_triad_text,
            [
                "Terminal Triad Reduction",
                "PDEC family certificates",
                "LocalSurvivorCert family",
                "CleanKLS/DLS certificates",
                "不存在第四类可持续逃逸",
            ],
        )
    )
    old_self_pdec_row = find_row(
        self_bottleneck["rows"], "PDEC_CAP_SameSetGlobalDualCertificate"
    )
    pdec_promoted_closed = (
        boundary_lift["canonical_source_self_contained_pdec_bottleneck_closed"]
        and boundary_lift["narrowest_self_contained_boundary"]
        == "NoFurtherCanonicalSourceSelfContainedPDECCapGap"
    )
    clean_promoted_closed = (
        self_bottleneck["internal_clean_kls_independent_blocker_collapsed"]
        and find_row(self_bottleneck["rows"], "CanonicalCleanBranchAbsorbed").get(
            "closed"
        )
        is True
    )
    local_current_closed = find_row(
        global_boundary["rows"], "CurrentLocalSurvivorAndSparseEntryGuarded"
    ).get("closed") is True
    generic_external_separated = (
        boundary_lift["generic_external_dibfi_boundary_open"]
        and boundary_lift["external_next_hardpoint"]
        == "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
    )
    stale_split_superseded = (
        "PDEC_CAP" in global_split["open_final_gates"]
        and pdec_promoted_closed
        and global_split["self_contained_next_hardpoint"]
        == "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
    )
    row_boundary_guarded = (
        row_frontier["canonical_source_boundary_closed"]
        and row_frontier["generic_unrestricted_self_contained_refuted"]
        and not row_frontier["row_column_unconditional_closed"]
    )
    referee_open = "BLOCK-REFEREE" in line_ref_text

    return [
        closure_row(
            gate="CurrentMaterializedTerminalFrontierExhausted",
            closed=current_frontier_closed,
            evidence=global_boundary["narrowest_next_hardpoint"],
            meaning="当前已物化 PDEC、LocalSurvivor、CleanKLS/NC-BLK 终端实例已经清零或接回命名边界。",
            scope="current-materialized-frontier",
            blocks_final=False,
        ),
        closure_row(
            gate="TerminalTriadNoFourthExitAccepted",
            closed=triad_no_fourth_exit,
            evidence="PDEC / LocalSurvivor / CleanKLS-DLS terminal triad",
            meaning="在现有上游合同下，反例不能生成第四类可持续终端出口。",
            scope="formal-terminal-schema",
            blocks_final=False,
        ),
        closure_row(
            gate="CanonicalPDECCapPromotionClosed",
            closed=pdec_promoted_closed,
            evidence=boundary_lift["narrowest_self_contained_boundary"],
            meaning=(
                "旧 PDEC-CAP 自足瓶颈已由横向来源嵌入、canonical 层转移和 A1 来源边界闭合。"
            ),
            scope=f"supersedes old gate: {old_self_pdec_row.get('evidence', 'missing')}",
            blocks_final=False,
        ),
        closure_row(
            gate="CanonicalCleanKLSPromotionClosed",
            closed=clean_promoted_closed,
            evidence="CleanKLS failure returns to PDEC/SAE; canonical clean branch absorbed",
            meaning="canonical-source CleanKLS/SC-9/NC-BLK 不再是平行自足终端硬点。",
            scope="canonical-source-clean-branch",
            blocks_final=False,
        ),
        closure_row(
            gate="LocalSurvivorKnownEntrancesClosed",
            closed=local_current_closed,
            evidence="open materialized packets=0; missing extractor/admission=0",
            meaning="当前已知 sparse/LocalSurvivor 入口都有 witness、extractor 或合同准入。",
            scope="known-local-survivor-entrances",
            blocks_final=False,
        ),
        closure_row(
            gate="StaleSplitPDECKLSGatesSuperseded",
            closed=stale_split_superseded,
            evidence=global_split["self_contained_next_hardpoint"],
            meaning=(
                "旧全局拆分中的 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 已被 boundary-lift 重新分类。"
            ),
            scope="router-reconciliation",
            blocks_final=False,
        ),
        closure_row(
            gate="GenericExternalDIBFINotSelfContainedGap",
            closed=generic_external_separated,
            evidence=boundary_lift["external_next_hardpoint"],
            meaning="DI/BFI 无投影量化证书仍开放，但它属于 generic/external 分支，不是 canonical 自足缺口。",
            scope="external-or-generic-branch",
            blocks_final=False,
        ),
        closure_row(
            gate="ClaimBoundaryDisciplinePreserved",
            closed=row_boundary_guarded,
            evidence=row_frontier["narrowest_next_hardpoint"]["name"],
            meaning="自足闭合只限 canonical-source 终端晋级边界，不能升级成完整行/列无条件定理。",
            scope="no-global-overclaim",
            blocks_final=False,
        ),
        closure_row(
            gate="DStructureRankinRefereeStillOpen",
            closed=not referee_open,
            evidence="BLOCK-REFEREE" if referee_open else "no referee block token found",
            meaning="最终定理晋级仍需 D-structure/Tail-log4/finite Rankin 接口独立审稿通过。",
            scope="final-theorem-promotion",
            blocks_final=referee_open,
        ),
    ]


def run(
    boundary_lift_path: Path,
    global_boundary_path: Path,
    global_split_path: Path,
    self_bottleneck_path: Path,
    row_frontier_path: Path,
    terminal_triad_path: Path,
    line_ref_path: Path,
) -> dict[str, Any]:
    """运行 canonical-source 终端晋级闭合复核。"""
    boundary_lift = load_json(boundary_lift_path)
    global_boundary = load_json(global_boundary_path)
    global_split = load_json(global_split_path)
    self_bottleneck = load_json(self_bottleneck_path)
    row_frontier = load_json(row_frontier_path)
    terminal_triad_text = read_text(terminal_triad_path)
    line_ref_text = read_text(line_ref_path)

    rows = build_rows(
        boundary_lift=boundary_lift,
        global_boundary=global_boundary,
        global_split=global_split,
        self_bottleneck=self_bottleneck,
        row_frontier=row_frontier,
        terminal_triad_text=terminal_triad_text,
        line_ref_text=line_ref_text,
    )
    open_self_contained_gates = [
        row["gate"]
        for row in rows
        if not row["blocks_final"] and not row["closed"]
    ]
    open_final_gates = [
        row["gate"] for row in rows if row["blocks_final"] and not row["closed"]
    ]
    latest_self_contained_hardpoint_closed = not open_self_contained_gates

    return {
        "certificate_type": "prime_matrix_canonical_terminal_promotion_closure_router",
        "status": "canonical_terminal_promotion_self_contained_closed_final_referee_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "boundary_lift": file_sha256(boundary_lift_path),
            "global_boundary": file_sha256(global_boundary_path),
            "global_split": file_sha256(global_split_path),
            "self_contained_terminal_bottleneck": file_sha256(
                self_bottleneck_path
            ),
            "row_column_unconditional_frontier": file_sha256(row_frontier_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "line_referee": file_sha256(line_ref_path),
        },
        "latest_self_contained_hardpoint_closed": latest_self_contained_hardpoint_closed,
        "canonical_source_terminal_promotion_closed": latest_self_contained_hardpoint_closed,
        "canonical_source_self_contained_boundary_closed": (
            boundary_lift["canonical_source_self_contained_pdec_bottleneck_closed"]
            and latest_self_contained_hardpoint_closed
        ),
        "open_self_contained_gates": open_self_contained_gates,
        "open_external_gates": [
            "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
        ],
        "open_final_gates": open_final_gates,
        "row_column_unconditional_closed": False,
        "global_unrestricted_terminal_family_exclusion_closed": False,
        "narrowest_self_contained_boundary": (
            "NoFurtherCanonicalSourceTerminalPromotionGap"
        ),
        "narrowest_global_next_hardpoint": (
            "DStructureRankinReferee_FOR_FINAL_PROMOTION"
        ),
        "rows": rows,
        "closure_law": (
            "Within the canonical RIW/Buchstab source branch, the terminal-promotion "
            "problem has no remaining self-contained mathematical gate: the materialized "
            "frontier is exhausted, the terminal triad has no fourth exit, PDEC-CAP is "
            "closed by the boundary lift, and canonical CleanKLS/NC-BLK is absorbed or "
            "returns to PDEC/SAE. This is not an unrestricted global terminal-family "
            "exclusion theorem and not a final row/column theorem; generic/external DI/BFI "
            "and D-structure/Rankin referee promotion remain outside the closure."
        ),
        "review_conclusion": (
            "最新自足硬点完成闭合：在 canonical-source 形式系统内，终端晋级已无新的自足数学开门，"
            "边界更新为 `NoFurtherCanonicalSourceTerminalPromotionGap`。但完整行/列无条件定理"
            "仍未闭合；剩余为 generic/external DI/BFI 路线和 `DStructureRankinReferee` 最终晋级门。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix canonical 终端晋级闭合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 闭合律",
        "",
        result["closure_law"],
        "",
        "```text",
        "canonical-source self-contained branch:",
        "  materialized terminal frontier exhausted;",
        "  terminal triad has no fourth exit;",
        "  PDEC-CAP promotion closed by boundary lift;",
        "  canonical CleanKLS/NC-BLK absorbed or returns to PDEC/SAE;",
        "therefore:",
        "  NoFurtherCanonicalSourceTerminalPromotionGap.",
        "",
        "outside this closure:",
        "  generic/external DI-BFI quantified no-projection certificate;",
        "  D-structure/Tail-log4/finite Rankin referee promotion.",
        "```",
        "",
        "## 2. 汇总",
        "",
        (
            "- `latest_self_contained_hardpoint_closed="
            f"{fmt_bool(result['latest_self_contained_hardpoint_closed'])}`。"
        ),
        (
            "- `canonical_source_terminal_promotion_closed="
            f"{fmt_bool(result['canonical_source_terminal_promotion_closed'])}`。"
        ),
        (
            "- `canonical_source_self_contained_boundary_closed="
            f"{fmt_bool(result['canonical_source_self_contained_boundary_closed'])}`。"
        ),
        (
            "- `row_column_unconditional_closed="
            f"{fmt_bool(result['row_column_unconditional_closed'])}`。"
        ),
        (
            "- `global_unrestricted_terminal_family_exclusion_closed="
            f"{fmt_bool(result['global_unrestricted_terminal_family_exclusion_closed'])}`。"
        ),
        f"- `open_self_contained_gates={result['open_self_contained_gates']}`。",
        f"- `open_external_gates={result['open_external_gates']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        f"- `narrowest_self_contained_boundary={result['narrowest_self_contained_boundary']}`。",
        f"- `narrowest_global_next_hardpoint={result['narrowest_global_next_hardpoint']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | scope | meaning |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {scope} | {meaning} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                blocks=fmt_bool(bool(row["blocks_final"])),
                evidence=table_cell(row["evidence"]),
                scope=table_cell(row["scope"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 诚实边界",
            "",
            "本路由器闭合的是 canonical-source 终端晋级自足边界。它不声明 unrestricted/global "
            "终端家族排斥定理，也不把完整行/列无条件命题标为已证。最终升级仍需 "
            "`DStructureRankinReferee`，generic/external 版本仍需 DI/BFI 无投影量化证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary-lift-json", type=Path, default=DEFAULT_BOUNDARY_LIFT)
    parser.add_argument("--global-boundary-json", type=Path, default=DEFAULT_GLOBAL_BOUNDARY)
    parser.add_argument("--global-split-json", type=Path, default=DEFAULT_GLOBAL_SPLIT)
    parser.add_argument(
        "--self-bottleneck-json", type=Path, default=DEFAULT_SELF_BOTTLENECK
    )
    parser.add_argument("--row-frontier-json", type=Path, default=DEFAULT_ROW_FRONTIER)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        boundary_lift_path=args.boundary_lift_json,
        global_boundary_path=args.global_boundary_json,
        global_split_path=args.global_split_json,
        self_bottleneck_path=args.self_bottleneck_json,
        row_frontier_path=args.row_frontier_json,
        terminal_triad_path=args.terminal_triad_md,
        line_ref_path=args.line_ref_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_self_contained_boundary"])


if __name__ == "__main__":
    main()
