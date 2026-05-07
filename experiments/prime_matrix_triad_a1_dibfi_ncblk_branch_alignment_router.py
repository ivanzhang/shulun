#!/usr/bin/env python3
"""把 full-S non-AP WFD 的 NC-BLK 终端对齐到 source-entropy/外部定理二分。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_ncblk_branch_alignment_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_C_DEPENDENT_REDUCTION = (
    DOCS
    / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
)
DEFAULT_NEW_FULL_S_INPUT = (
    DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
)
DEFAULT_AP_SOURCE_LIFT_NO_GO = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json"
)
DEFAULT_BRANCH_STATEMENT_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_SOURCE_BLOCK_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.md"


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
    c_dependent_reduction: dict[str, Any],
    new_full_s_input: dict[str, Any],
    ap_source_lift_no_go: dict[str, Any],
    branch_statement_coverage: dict[str, Any],
    source_block_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 NC-BLK 分支对齐账本。"""
    prior_ready = (
        c_dependent_reduction["terminal_gap_after_router"]
        == "NCBLKActualBlockNonConcentrationOrExternalDIBFI"
        and c_dependent_reduction["open_reduction_gates"]
        == ["NCBLKActualBlockNonConcentrationOrExternalDIBFI"]
    )
    full_s_generic_pinned = (
        new_full_s_input["terminal_gap_after_router"]
        == "FullSNonAPWFDKLSTheoremInput"
        and "object: current non-AP uncentered no-projection WFD window"
        in new_full_s_input["required_theorem_clauses"]
    )
    ap_lift_rejected = (
        ap_source_lift_no_go["terminal_gap_after_router"] == "NewFullSTheoremInput"
        and "APSourceLift" in ap_source_lift_no_go["rejected_gates"]
    )
    canonical_not_free = (
        branch_statement_coverage["canonical_source_branch_internal_gap_closed"]
        and not branch_statement_coverage["generic_wfd_self_contained_gap_closed"]
        and branch_statement_coverage["terminal_gap_after_router"]
        == "ExternalDIBFIOriginalDispersionForGenericWFDBranchOnly"
    )
    source_entropy_sufficient = (
        source_block_entropy["conditional_source_entropy_implies_ncblk"]
        and source_block_entropy["next_internal_target"] == "ExactWFDSourceEntropy"
    )
    formal_inputs_not_enough = source_block_entropy[
        "current_internal_source_entropy_closed"
    ] is False
    alignment_closed = all(
        [
            prior_ready,
            full_s_generic_pinned,
            ap_lift_rejected,
            canonical_not_free,
            source_entropy_sufficient,
            formal_inputs_not_enough,
        ]
    )
    return [
        {
            "gate": "PriorNCBLKTerminalPinned",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={c_dependent_reduction['terminal_gap_after_router']}; "
                f"open={c_dependent_reduction['open_reduction_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "FullSNonAPGenericObjectAdmission",
        },
        {
            "gate": "FullSNonAPGenericObjectPinned",
            "closed": full_s_generic_pinned,
            "evidence": (
                "NewFullSTheoremInput is pinned as the current full-S, non-AP, "
                "uncentered, no-projection WFD window."
            ),
            "remaining": "cannot replace this by AP-source or a centered object",
            "next_target": "NoSilentCanonicalSourceImport",
        },
        {
            "gate": "APSourceLiftStillRejected",
            "closed": ap_lift_rejected,
            "evidence": "APSourceLift is already rejected; the full-S non-AP object cannot be reclassified as AP-source.",
            "remaining": "none; this blocks the AP-source shortcut",
            "next_target": "NoSilentCanonicalSourceImport",
        },
        {
            "gate": "NoSilentCanonicalSourceImport",
            "closed": canonical_not_free,
            "evidence": (
                "Branch coverage closes the canonical RIW/Buchstab source branch, "
                "but explicitly leaves generic WFD self-contained closure false."
            ),
            "remaining": "full-S non-AP generic WFD must prove its own source entropy or use external DI/BFI",
            "next_target": "ExactFullSNonAPWFDSourceEntropy",
        },
        {
            "gate": "SourceEntropyImpliesNCBLK",
            "closed": source_entropy_sufficient,
            "evidence": (
                "SourceBlockEntropy gives max_b M_b/M <= log^{-2A}, hence "
                "sum_b |S_b|^2 <= log^{-2A} M^2 and implies NC-BLK."
            ),
            "remaining": "source entropy itself is not proved for the exact full-S non-AP source",
            "next_target": "ExactFullSNonAPWFDSourceEntropy",
        },
        {
            "gate": "FormalWFDInputsDoNotForceSourceEntropy",
            "closed": formal_inputs_not_enough,
            "evidence": (
                "The source entropy router records moving-delta well-factorable "
                "models that pass formal templates while concentrating on one moving block."
            ),
            "remaining": "must use exact coefficient generation, not the formal WFD template alone",
            "next_target": "ExactFullSNonAPWFDSourceEntropy",
        },
        {
            "gate": "AlignmentToExactSourceEntropyOrExternal",
            "closed": alignment_closed,
            "evidence": (
                "The full-S non-AP NC-BLK terminal is aligned with the same valid "
                "sufficient condition as the KZ-E NC-BLK route, but without silent "
                "canonical-source import."
            ),
            "remaining": "none at branch-alignment level",
            "next_target": "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
        },
        {
            "gate": "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
            "closed": False,
            "evidence": (
                "The repository has not proved scale-uniform moving-block entropy "
                "for the exact full-S non-AP WFD coefficients, and has not completed "
                "a primary-source theorem match for this exact object."
            ),
            "remaining": "prove exact source entropy for the full-S non-AP coefficients, or cite/match external dispersion",
            "next_target": "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
        },
    ]


def run(
    c_dependent_reduction_path: Path,
    new_full_s_input_path: Path,
    ap_source_lift_no_go_path: Path,
    branch_statement_coverage_path: Path,
    source_block_entropy_path: Path,
) -> dict[str, Any]:
    """运行 NC-BLK 分支对齐路由。"""
    c_dependent_reduction = load_json(c_dependent_reduction_path)
    new_full_s_input = load_json(new_full_s_input_path)
    ap_source_lift_no_go = load_json(ap_source_lift_no_go_path)
    branch_statement_coverage = load_json(branch_statement_coverage_path)
    source_block_entropy = load_json(source_block_entropy_path)
    rows = build_rows(
        c_dependent_reduction,
        new_full_s_input,
        ap_source_lift_no_go,
        branch_statement_coverage,
        source_block_entropy,
    )
    return {
        "certificate_type": "triad_a1_dibfi_ncblk_branch_alignment_router",
        "status": "ncblk_branch_alignment_reduced_to_exact_full_s_source_entropy_or_external_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "c_dependent_reduction_json": file_sha256(c_dependent_reduction_path),
            "new_full_s_input_json": file_sha256(new_full_s_input_path),
            "ap_source_lift_no_go_json": file_sha256(ap_source_lift_no_go_path),
            "branch_statement_coverage_json": file_sha256(
                branch_statement_coverage_path
            ),
            "source_block_entropy_json": file_sha256(source_block_entropy_path),
        },
        "previous_terminal_gap": c_dependent_reduction["terminal_gap_after_router"],
        "alignment_rows": rows,
        "closed_alignment_gates": [row["gate"] for row in rows if row["closed"]],
        "open_alignment_gates": [row["gate"] for row in rows if not row["closed"]],
        "ncblk_branch_alignment_closed": False,
        "terminal_gap_after_router": "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
        "terminal_gap_expansion": [
            "ExactFullSNonAPWFDSourceEntropy",
            "ExternalDIBFIKuznetsovDispersionTheoremMatch",
        ],
        "blocked_shortcuts": [
            "silent canonical RIW/Buchstab source import",
            "APSourceLift",
            "formal WFD template implies moving-block entropy",
        ],
        "structural_law": (
            "NC-BLK is a block-energy statement. SourceBlockEntropy is a valid "
            "sufficient condition, but branch coverage forbids importing the "
            "canonical RIW/Buchstab source chain into the broader full-S non-AP "
            "generic WFD object. Therefore the honest next target is exact "
            "moving-block source entropy for this full-S non-AP coefficient "
            "generation, or a matched external DI/BFI/Kuznetsov theorem."
        ),
        "review_conclusion": (
            "`NCBLKActualBlockNonConcentrationOrExternalDIBFI` 已被分支对齐为 "
            "`ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov`："
            "canonical source branch 不能静默借用，形式 WFD 模板也不能推出 moving-block 熵。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI NC-BLK branch alignment 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "expansion:",
        f"  {result['terminal_gap_expansion']}.",
        "```",
        "",
        "## 2. 被排除的捷径",
        "",
    ]
    for item in result["blocked_shortcuts"]:
        lines.append(f"- `{item}`。")
    lines.extend(
        [
            "",
            "## 3. 汇总",
            "",
            f"- `ncblk_branch_alignment_closed={fmt_bool(result['ncblk_branch_alignment_closed'])}`。",
            f"- `closed_alignment_gates={result['closed_alignment_gates']}`。",
            f"- `open_alignment_gates={result['open_alignment_gates']}`。",
            f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
            "",
            "## 4. 分支对齐账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["alignment_rows"]:
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
            "## 5. 当前结论",
            "",
            "唯一剩余继续变窄为：",
            "",
            "```text",
            "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov:",
            "  prove scale-uniform moving-block source entropy for the exact",
            "  full-S non-AP WFD coefficient generation, or precisely match",
            "  an external DI/BFI/Kuznetsov dispersion theorem.",
            "```",
            "",
            "这一步没有证明 exact source entropy；它只关闭了“把 full-S generic WFD "
            "静默并入 canonical source branch”的错误路线。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--c-dependent-reduction-json",
        type=Path,
        default=DEFAULT_C_DEPENDENT_REDUCTION,
    )
    parser.add_argument(
        "--new-full-s-input-json", type=Path, default=DEFAULT_NEW_FULL_S_INPUT
    )
    parser.add_argument(
        "--ap-source-lift-no-go-json",
        type=Path,
        default=DEFAULT_AP_SOURCE_LIFT_NO_GO,
    )
    parser.add_argument(
        "--branch-statement-coverage-json",
        type=Path,
        default=DEFAULT_BRANCH_STATEMENT_COVERAGE,
    )
    parser.add_argument(
        "--source-block-entropy-json", type=Path, default=DEFAULT_SOURCE_BLOCK_ENTROPY
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        c_dependent_reduction_path=args.c_dependent_reduction_json,
        new_full_s_input_path=args.new_full_s_input_json,
        ap_source_lift_no_go_path=args.ap_source_lift_no_go_json,
        branch_statement_coverage_path=args.branch_statement_coverage_json,
        source_block_entropy_path=args.source_block_entropy_json,
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
                "open_alignment_gates": result["open_alignment_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
