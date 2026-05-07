#!/usr/bin/env python3
"""把 full-S 支撑+容量兼容终端压成源头反原子合同。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_full_s_source_antiatom_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_FULL_S_SUPPORT_RANGE = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
)
DEFAULT_SOURCE_BLOCK_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
)
DEFAULT_EXACT_FACTOR_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
)
DEFAULT_FACTOR_RESIDUE_INCIDENCE = (
    DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
)
DEFAULT_BRANCH_STATEMENT_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.md"


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


def source_gate_open(source_block_entropy: dict[str, Any], gate: str) -> bool:
    """核查 source entropy 指定门控是否未闭合。"""
    return any(
        row["gate"] == gate and not row["closed"]
        for row in source_block_entropy["gate_rows"]
    )


def build_rows(
    full_s_support_range: dict[str, Any],
    source_block_entropy: dict[str, Any],
    exact_factor_support: dict[str, Any],
    factor_residue_incidence: dict[str, Any],
    branch_statement_coverage: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 full-S source anti-atom 路由账本。"""
    prior_ready = (
        full_s_support_range["terminal_gap_after_router"]
        == "FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov"
        and full_s_support_range["open_range_gates"]
        == [
            "FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov"
        ]
    )
    support_capacity_pair_pinned = full_s_support_range[
        "remaining_support_package_clauses"
    ] == [
        "FullSNonAPExactFactorSupportLowerBound",
        "FullSNonAPTypeFourierCapacityCompatibility",
    ]
    formal_wfd_not_enough = (
        source_block_entropy["source_entropy_gap_exists"]
        and not source_block_entropy["current_internal_source_entropy_closed"]
        and source_gate_open(source_block_entropy, "WellFactorableConvolution")
        and source_gate_open(source_block_entropy, "TypeITypeIIDecomposition")
        and source_gate_open(source_block_entropy, "FourierSmoothing")
    )
    k4_k6_not_enough = (
        exact_factor_support["k4_k6_imply_exact_factor_support"] is False
        and exact_factor_support["current_internal_exact_factor_support_closed"]
        is False
    )
    naive_incidence_blocked = (
        factor_residue_incidence["naive_incidence_bridge_valid"] is False
        and factor_residue_incidence["factor_residue_incidence_bridge_closed"]
        is False
    )
    canonical_import_blocked = (
        branch_statement_coverage["canonical_source_branch_internal_gap_closed"]
        and not branch_statement_coverage["generic_wfd_self_contained_gap_closed"]
        and branch_statement_coverage["terminal_gap_after_router"]
        == "ExternalDIBFIOriginalDispersionForGenericWFDBranchOnly"
    )
    antiatom_is_exact_combination = all(
        [
            prior_ready,
            support_capacity_pair_pinned,
            formal_wfd_not_enough,
            k4_k6_not_enough,
            naive_incidence_blocked,
            canonical_import_blocked,
        ]
    )
    return [
        {
            "gate": "PriorSupportCapacityTerminalPinned",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={full_s_support_range['terminal_gap_after_router']}; "
                f"open={full_s_support_range['open_range_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "FullSNonAPSourceAntiAtomContract",
        },
        {
            "gate": "SupportCapacityPairPinned",
            "closed": support_capacity_pair_pinned,
            "evidence": (
                "After range closure the remaining clauses are exact u/v factor support "
                "and Type/Fourier capacity compatibility."
            ),
            "remaining": "combine them into one source-level capacity anti-atom statement",
            "next_target": "FullSNonAPSourceAntiAtomContract",
        },
        {
            "gate": "FormalWFDTypeFourierDoNotForceAntiAtom",
            "closed": formal_wfd_not_enough,
            "evidence": (
                "SourceBlockEntropy records that well-factorable convolution, Type decomposition, "
                "and Fourier smoothing can all pass while capacity concentrates on one moving block."
            ),
            "remaining": "anti-atom must be an additional exact source theorem",
            "next_target": "FullSNonAPSourceAntiAtomContract",
        },
        {
            "gate": "K4K6DoNotForceMovingFactorSupport",
            "closed": k4_k6_not_enough,
            "evidence": (
                "ExactFactorSupport records residue-flat but factor-concentrated models."
            ),
            "remaining": "cannot infer the source anti-atom from K4/K6 projection data",
            "next_target": "FullSNonAPSourceAntiAtomContract",
        },
        {
            "gate": "NaiveFactorResidueIncidenceBlocked",
            "closed": naive_incidence_blocked,
            "evidence": (
                "FactorResidueIncidence is blocked by the internal h, ell, x, z fiber inside one (u,v) block."
            ),
            "remaining": "no bounded-multiplicity incidence shortcut remains",
            "next_target": "FullSNonAPSourceAntiAtomContract",
        },
        {
            "gate": "CanonicalSourceImportBlocked",
            "closed": canonical_import_blocked,
            "evidence": (
                "Branch coverage closes only the canonical RIW/Buchstab branch; generic WFD self-contained closure remains false."
            ),
            "remaining": "full-S non-AP generic WFD needs its own source anti-atom or an external theorem",
            "next_target": "FullSNonAPSourceAntiAtomContract",
        },
        {
            "gate": "SupportCapacityReducedToSourceAntiAtom",
            "closed": antiatom_is_exact_combination,
            "evidence": (
                "Exact support plus Type/Fourier capacity compatibility is precisely a statement "
                "that the final source capacity measure has no moving same-(u,v) atom."
            ),
            "remaining": "none at reduction level",
            "next_target": "FullSNonAPStrengthenedSourceAntiAtomContractOrExternal",
        },
        {
            "gate": "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
            "closed": False,
            "evidence": (
                "The repository has not proved a source-level anti-atom theorem for the full-S non-AP "
                "generic WFD capacity measure, and has not fully matched an external dispersion theorem."
            ),
            "remaining": "prove source anti-atom before dispersion, strengthen the source contract, or cite/match external dispersion",
            "next_target": "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
        },
    ]


def run(
    full_s_support_range_path: Path,
    source_block_entropy_path: Path,
    exact_factor_support_path: Path,
    factor_residue_incidence_path: Path,
    branch_statement_coverage_path: Path,
) -> dict[str, Any]:
    """运行 full-S source anti-atom 路由。"""
    full_s_support_range = load_json(full_s_support_range_path)
    source_block_entropy = load_json(source_block_entropy_path)
    exact_factor_support = load_json(exact_factor_support_path)
    factor_residue_incidence = load_json(factor_residue_incidence_path)
    branch_statement_coverage = load_json(branch_statement_coverage_path)
    rows = build_rows(
        full_s_support_range,
        source_block_entropy,
        exact_factor_support,
        factor_residue_incidence,
        branch_statement_coverage,
    )
    return {
        "certificate_type": "triad_a1_dibfi_full_s_source_antiatom_router",
        "status": "full_s_support_capacity_reduced_to_source_antiatom_or_external_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "full_s_support_range_json": file_sha256(full_s_support_range_path),
            "source_block_entropy_json": file_sha256(source_block_entropy_path),
            "exact_factor_support_json": file_sha256(exact_factor_support_path),
            "factor_residue_incidence_json": file_sha256(
                factor_residue_incidence_path
            ),
            "branch_statement_coverage_json": file_sha256(
                branch_statement_coverage_path
            ),
        },
        "previous_terminal_gap": full_s_support_range["terminal_gap_after_router"],
        "antiatom_rows": rows,
        "closed_antiatom_gates": [row["gate"] for row in rows if row["closed"]],
        "open_antiatom_gates": [row["gate"] for row in rows if not row["closed"]],
        "source_antiatom_reduction_closed": False,
        "terminal_gap_after_router": (
            "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
        ),
        "terminal_gap_expansion": [
            "FullSNonAPStrengthenedSourceAntiAtomContract",
            "ExternalDIBFIKuznetsovDispersionTheoremMatch",
        ],
        "antiatom_contract": (
            "For the final full-S non-AP WFD source capacity measure M_{u,v}, "
            "prove max_{u,v} M_{u,v}/sum_{u,v}M_{u,v} <= log^{-2A} for every A."
        ),
        "blocked_shortcuts": [
            "formal well-factorable convolution",
            "Type-I/II algebraic decomposition",
            "Fourier h-smoothing",
            "K4/K6 residue/tail projections",
            "naive factor-residue incidence",
            "silent canonical source import",
        ],
        "structural_law": (
            "After range closure, exact factor support and Type/Fourier capacity compatibility "
            "are not two independent analytic estimates. Together they are exactly a source-level "
            "anti-atom condition for the final moving same-(u,v) capacity measure. Existing ledgers "
            "show this condition is not forced by formal WFD inputs, K4/K6, naive incidence, or "
            "canonical branch import."
        ),
        "review_conclusion": (
            "`FullSNonAPExactFactorSupportAndCapacityCompatibility` 已压成 "
            "`FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov`："
            "必须证明最终 source capacity measure 无 moving atom，或匹配外部 dispersion 定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI full-S source anti-atom 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 反原子合同",
        "",
        f"`{result['antiatom_contract']}`",
        "",
        "## 2. 结构律",
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
        "## 3. 被排除的捷径",
        "",
    ]
    for item in result["blocked_shortcuts"]:
        lines.append(f"- `{item}`。")
    lines.extend(
        [
            "",
            "## 4. 汇总",
            "",
            f"- `source_antiatom_reduction_closed={fmt_bool(result['source_antiatom_reduction_closed'])}`。",
            f"- `closed_antiatom_gates={result['closed_antiatom_gates']}`。",
            f"- `open_antiatom_gates={result['open_antiatom_gates']}`。",
            f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
            "",
            "## 5. 路由账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["antiatom_rows"]:
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
            "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov:",
            "  prove the final full-S non-AP WFD source capacity measure",
            "  has no moving same-(u,v) atom, or precisely match an external",
            "  DI/BFI/Kuznetsov dispersion theorem.",
            "```",
            "",
            "这一步没有证明反原子合同；它排除了把支撑/容量兼容从形式 WFD、K4/K6、"
            "朴素 incidence 或 canonical 分支中免费推出的路线。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full-s-support-range-json",
        type=Path,
        default=DEFAULT_FULL_S_SUPPORT_RANGE,
    )
    parser.add_argument(
        "--source-block-entropy-json",
        type=Path,
        default=DEFAULT_SOURCE_BLOCK_ENTROPY,
    )
    parser.add_argument(
        "--exact-factor-support-json", type=Path, default=DEFAULT_EXACT_FACTOR_SUPPORT
    )
    parser.add_argument(
        "--factor-residue-incidence-json",
        type=Path,
        default=DEFAULT_FACTOR_RESIDUE_INCIDENCE,
    )
    parser.add_argument(
        "--branch-statement-coverage-json",
        type=Path,
        default=DEFAULT_BRANCH_STATEMENT_COVERAGE,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        full_s_support_range_path=args.full_s_support_range_json,
        source_block_entropy_path=args.source_block_entropy_json,
        exact_factor_support_path=args.exact_factor_support_json,
        factor_residue_incidence_path=args.factor_residue_incidence_json,
        branch_statement_coverage_path=args.branch_statement_coverage_json,
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
                "open_antiatom_gates": result["open_antiatom_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
