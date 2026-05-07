#!/usr/bin/env python3
"""把 exact full-S non-AP source entropy 压成精确因子支撑包。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_exact_full_s_source_entropy_reduction_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_NCBLK_BRANCH_ALIGNMENT = (
    DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
)
DEFAULT_EXACT_WFD_SOURCE_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
)
DEFAULT_EXACT_FACTOR_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
)
DEFAULT_NEW_FULL_S_INPUT = (
    DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json"
)
DEFAULT_JSON = (
    DOCS
    / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json"
)
DEFAULT_MD = (
    DOCS
    / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.md"
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


def gate_closed(rows: list[dict[str, Any]], gate: str) -> bool:
    """读取指定门控的 closed 状态。"""
    return any(row["gate"] == gate and row["closed"] for row in rows)


def gate_open(rows: list[dict[str, Any]], gate: str) -> bool:
    """读取指定门控是否仍未闭合。"""
    return any(row["gate"] == gate and not row["closed"] for row in rows)


def build_rows(
    ncblk_branch_alignment: dict[str, Any],
    exact_wfd_source_entropy: dict[str, Any],
    exact_factor_support: dict[str, Any],
    new_full_s_input: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 exact full-S source entropy reduction 账本。"""
    prior_ready = (
        ncblk_branch_alignment["terminal_gap_after_router"]
        == "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov"
        and ncblk_branch_alignment["open_alignment_gates"]
        == ["ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov"]
    )
    full_s_object_pinned = (
        new_full_s_input["terminal_gap_after_router"]
        == "FullSNonAPWFDKLSTheoremInput"
        and "boundary: no AP-source lift, no Maynard-W4 compression, no hidden centering/projection"
        in new_full_s_input["required_theorem_clauses"]
    )
    support_implies_entropy = (
        exact_wfd_source_entropy[
            "conditional_factor_support_implies_exact_source_entropy"
        ]
        and exact_wfd_source_entropy["all_model_rows_support_bound_suffices"]
    )
    divisor_bound_ready = gate_closed(
        exact_wfd_source_entropy["gate_rows"], "DivisorBoundedFactors"
    )
    support_lower_bound_open = gate_open(
        exact_wfd_source_entropy["gate_rows"], "ExactFactorSupportLowerBound"
    )
    range_threshold_open = gate_open(
        exact_wfd_source_entropy["gate_rows"], "BalancedRangeSize"
    )
    type_fourier_open = gate_open(
        exact_wfd_source_entropy["gate_rows"], "TypeFourierCapacityCompatibility"
    )
    k4_k6_not_enough = (
        exact_factor_support["k4_k6_imply_exact_factor_support"] is False
        and exact_factor_support["current_internal_exact_factor_support_closed"] is False
    )
    canonical_not_free = "silent canonical RIW/Buchstab source import" in ncblk_branch_alignment[
        "blocked_shortcuts"
    ]
    reduction_closed = all(
        [
            prior_ready,
            full_s_object_pinned,
            support_implies_entropy,
            divisor_bound_ready,
            support_lower_bound_open,
            range_threshold_open,
            type_fourier_open,
            k4_k6_not_enough,
            canonical_not_free,
        ]
    )
    return [
        {
            "gate": "PriorExactFullSSourceEntropyPinned",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={ncblk_branch_alignment['terminal_gap_after_router']}; "
                f"open={ncblk_branch_alignment['open_alignment_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "ExactFullSFactorSupportPackage",
        },
        {
            "gate": "FullSNonAPObjectBoundaryPinned",
            "closed": full_s_object_pinned,
            "evidence": (
                "The full-S non-AP WFD object remains uncentered, no-projection, "
                "and cannot use AP-source lift or Maynard-W4 compression."
            ),
            "remaining": "the factor-support package must apply to this exact object",
            "next_target": "ExactFullSFactorSupportPackage",
        },
        {
            "gate": "SupportLowerBoundImpliesEntropyImported",
            "closed": support_implies_entropy,
            "evidence": (
                "Existing ExactWFDSourceEntropy ledger proves the elementary "
                "max-pair-share bound: broad factor support plus divisor bounds "
                "implies moving-block entropy."
            ),
            "remaining": "support hypotheses are not yet proved for full-S non-AP coefficients",
            "next_target": "ExactFullSFactorSupportPackage",
        },
        {
            "gate": "DivisorBoundedFactorBudgetAvailable",
            "closed": divisor_bound_ready,
            "evidence": "Divisor-bounded alpha_u and delta_v cost only a fixed log power.",
            "remaining": "none at divisor-bound level",
            "next_target": "ExactFullSFactorSupportPackage",
        },
        {
            "gate": "ExactFactorSupportLowerBoundStillOpen",
            "closed": support_lower_bound_open,
            "evidence": (
                "The source-entropy ledger records no exact factor support theorem "
                "for the surviving balanced full-S blocks."
            ),
            "remaining": "prove lower absolute support in u and v for exact full-S non-AP factors",
            "next_target": "FullSNonAPExactFactorSupportLowerBound",
        },
        {
            "gate": "BalancedRangeThresholdStillOpen",
            "closed": range_threshold_open,
            "evidence": (
                "Balanced U,V ranges are plausible but exact log-power lower "
                "thresholds and small-range returns are not recorded for this branch."
            ),
            "remaining": "record U,V >= log^B or route small ranges to PDEC/SAE/external",
            "next_target": "FullSNonAPBalancedRangeThreshold",
        },
        {
            "gate": "TypeFourierCapacityCompatibilityStillOpen",
            "closed": type_fourier_open,
            "evidence": (
                "Type-I/II splitting and h/Fourier smoothing must not hide a "
                "single factor pair behind an unrecorded capacity multiplier."
            ),
            "remaining": "prove capacity compatibility or include it in exact factor support",
            "next_target": "FullSNonAPTypeFourierCapacityCompatibility",
        },
        {
            "gate": "K4K6ProjectionMismatchStillBlocks",
            "closed": k4_k6_not_enough,
            "evidence": (
                "ExactFactorSupport ledger shows K4 residue flatness and K6 "
                "dyadic bookkeeping do not imply moving factor-pair support."
            ),
            "remaining": "need factor-residue incidence, direct exact support, or external theorem",
            "next_target": "FullSNonAPFactorResidueIncidenceOrDirectSupport",
        },
        {
            "gate": "NoCanonicalBranchImport",
            "closed": canonical_not_free,
            "evidence": (
                "The branch-alignment router explicitly blocks silent import of "
                "canonical RIW/Buchstab support into generic full-S non-AP WFD."
            ),
            "remaining": "direct support must be proved for this exact full-S source",
            "next_target": "FullSNonAPExactFactorSupportPackageOrExternal",
        },
        {
            "gate": "ReductionToExactFactorSupportPackage",
            "closed": reduction_closed,
            "evidence": (
                "Exact source entropy has been reduced to its necessary support "
                "package: factor support, range threshold, and Type/Fourier capacity compatibility."
            ),
            "remaining": "none at reduction level",
            "next_target": "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov",
        },
        {
            "gate": "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov",
            "closed": False,
            "evidence": (
                "The repository still lacks this full-S non-AP exact support "
                "package and still lacks a fully matched external dispersion theorem."
            ),
            "remaining": "prove exact support package or cite/match external DI/BFI/Kuznetsov dispersion",
            "next_target": "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov",
        },
    ]


def run(
    ncblk_branch_alignment_path: Path,
    exact_wfd_source_entropy_path: Path,
    exact_factor_support_path: Path,
    new_full_s_input_path: Path,
) -> dict[str, Any]:
    """运行 exact full-S source entropy reduction 路由。"""
    ncblk_branch_alignment = load_json(ncblk_branch_alignment_path)
    exact_wfd_source_entropy = load_json(exact_wfd_source_entropy_path)
    exact_factor_support = load_json(exact_factor_support_path)
    new_full_s_input = load_json(new_full_s_input_path)
    rows = build_rows(
        ncblk_branch_alignment,
        exact_wfd_source_entropy,
        exact_factor_support,
        new_full_s_input,
    )
    return {
        "certificate_type": "triad_a1_dibfi_exact_full_s_source_entropy_reduction_router",
        "status": "exact_full_s_source_entropy_reduced_to_factor_support_package_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "ncblk_branch_alignment_json": file_sha256(ncblk_branch_alignment_path),
            "exact_wfd_source_entropy_json": file_sha256(
                exact_wfd_source_entropy_path
            ),
            "exact_factor_support_json": file_sha256(exact_factor_support_path),
            "new_full_s_input_json": file_sha256(new_full_s_input_path),
        },
        "previous_terminal_gap": ncblk_branch_alignment["terminal_gap_after_router"],
        "reduction_rows": rows,
        "closed_reduction_gates": [row["gate"] for row in rows if row["closed"]],
        "open_reduction_gates": [row["gate"] for row in rows if not row["closed"]],
        "exact_full_s_source_entropy_reduction_closed": False,
        "terminal_gap_after_router": (
            "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov"
        ),
        "terminal_gap_expansion": [
            "FullSNonAPExactFactorSupportLowerBound",
            "FullSNonAPBalancedRangeThreshold",
            "FullSNonAPTypeFourierCapacityCompatibility",
            "ExternalDIBFIKuznetsovDispersionTheoremMatch",
        ],
        "support_package_clauses": [
            "sum_u |alpha_u| >= U/log^C on every surviving full-S non-AP balanced block",
            "sum_v |delta_v| >= V/log^C on every surviving full-S non-AP balanced block",
            "U,V >= log^B or small ranges return to PDEC/SAE/external route",
            "Type/Fourier capacity does not concentrate on one moving factor pair",
        ],
        "blocked_shortcuts": [
            "canonical RIW/Buchstab support imported into generic full-S WFD",
            "K4 residue flatness implies moving factor support without incidence",
            "K6 dyadic bookkeeping implies internal block support",
        ],
        "structural_law": (
            "Exact full-S source entropy is no longer a spectral problem at this "
            "level. With divisor-bounded factors, it follows from broad support "
            "of the exact u and v factors plus range and capacity compatibility. "
            "The full-S non-AP branch cannot silently borrow canonical support, "
            "so the next honest atom is a support package for this exact source "
            "or a matched external DI/BFI/Kuznetsov dispersion theorem."
        ),
        "review_conclusion": (
            "`ExactFullSNonAPWFDSourceEntropy` 已压成 "
            "`FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov`："
            "需要同时证明精确 u/v 因子支撑、balanced range 阈值和 Type/Fourier 容量兼容。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI exact full-S source entropy reduction 路由器",
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
        "## 2. 支撑包条款",
        "",
    ]
    for clause in result["support_package_clauses"]:
        lines.append(f"- `{clause}`。")
    lines.extend(
        [
            "",
            "## 3. 被排除的捷径",
            "",
        ]
    )
    for item in result["blocked_shortcuts"]:
        lines.append(f"- `{item}`。")
    lines.extend(
        [
            "",
            "## 4. 汇总",
            "",
            f"- `exact_full_s_source_entropy_reduction_closed={fmt_bool(result['exact_full_s_source_entropy_reduction_closed'])}`。",
            f"- `closed_reduction_gates={result['closed_reduction_gates']}`。",
            f"- `open_reduction_gates={result['open_reduction_gates']}`。",
            f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
            "",
            "## 5. 路由账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["reduction_rows"]:
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
            "## 6. 当前结论",
            "",
            "唯一剩余继续变窄为：",
            "",
            "```text",
            "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov:",
            "  prove exact u/v factor support, balanced range threshold,",
            "  and Type/Fourier capacity compatibility for the full-S non-AP",
            "  WFD source; or precisely match an external dispersion theorem.",
            "```",
            "",
            "这一步没有证明支撑包；它把 source entropy 的证明义务降成更初等、"
            "可逐项审计的 exact support/capacity 包。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ncblk-branch-alignment-json",
        type=Path,
        default=DEFAULT_NCBLK_BRANCH_ALIGNMENT,
    )
    parser.add_argument(
        "--exact-wfd-source-entropy-json",
        type=Path,
        default=DEFAULT_EXACT_WFD_SOURCE_ENTROPY,
    )
    parser.add_argument(
        "--exact-factor-support-json", type=Path, default=DEFAULT_EXACT_FACTOR_SUPPORT
    )
    parser.add_argument(
        "--new-full-s-input-json", type=Path, default=DEFAULT_NEW_FULL_S_INPUT
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        ncblk_branch_alignment_path=args.ncblk_branch_alignment_json,
        exact_wfd_source_entropy_path=args.exact_wfd_source_entropy_json,
        exact_factor_support_path=args.exact_factor_support_json,
        new_full_s_input_path=args.new_full_s_input_json,
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
                "open_reduction_gates": result["open_reduction_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
