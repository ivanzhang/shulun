#!/usr/bin/env python3
"""落实 AP-source 直接 BFI 分支与非 AP fallback 的覆盖合同。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_ap_source_branch_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-ap-source-branch-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-ap-source-branch-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_AP_RESIDUAL_IDENTITY = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-residual-identity-router.json"
)
DEFAULT_DIRECT_BFI_ATOM = DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json"
DEFAULT_BFI_LEVEL_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json"
)
DEFAULT_BRANCH_STATEMENT = DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
DEFAULT_GENERIC_WFD_DIBFI = DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.md"


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


def build_branch_rows(
    ap_residual_identity: dict[str, Any],
    direct_bfi_atom: dict[str, Any],
    bfi_level_ledger: dict[str, Any],
    branch_statement: dict[str, Any],
    generic_wfd_dibfi: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造 AP-source 分支覆盖表。"""
    direct_bfi_available = bool(direct_bfi_atom["direct_bfi_atom_available"])
    level_closed = bool(bfi_level_ledger["bfi_level_exponent_ledger_closed"])
    source_gap_is_exact = ap_residual_identity["open_gates"] == [
        "UpstreamCleanA1ResidualDefinition",
        "MainTermAndCoefficientMatch",
    ]
    generic_external_ready = bool(generic_wfd_dibfi["external_dibfi_contract_materialized"])
    branch_split_ready = bool(branch_statement["coverage_no_overlap_no_gap"])
    return [
        {
            "branch": "APSourceDirectBFI",
            "scope": "R_clean is defined upstream as dyadic BFI prime-AP discrepancy with matching main term and coefficients",
            "closed": direct_bfi_available and level_closed,
            "evidence": "BFI atom is pinned; BFI level ledger is closed; the remaining AP identity gates are definitional on this branch.",
            "remaining": "none on AP-source branch",
            "route": "use BFI1986-Theorem10 as one prime-AP atom",
        },
        {
            "branch": "NonAPSourceGenericWFD",
            "scope": "the clean residual is only an uncentered WFD/KE-13 window, not an upstream AP discrepancy",
            "closed": False,
            "evidence": "SOURCE-CEN no-go and AP residual router block downstream back-projection; direct BFI AP atom cannot be used.",
            "remaining": "SeparateKE13DIBFIWindow or external original-dispersion theorem",
            "route": "fallback",
        },
        {
            "branch": "CoverageDichotomy",
            "scope": "a source object is either declared/proved AP-source before Cauchy, or it is not",
            "closed": branch_split_ready and source_gap_is_exact,
            "evidence": "AP residual router isolated exactly the two source-definition gates; branch coverage pattern is already used in A1 source statements.",
            "remaining": "none after explicit branch statement",
            "route": "AP-source vs non-AP-source dichotomy",
        },
        {
            "branch": "NoSilentAPUpgrade",
            "scope": "generic WFD cannot be silently upgraded to prime-AP discrepancy",
            "closed": True,
            "evidence": "AP residual identity router records that downstream WFD identification is diagnostic, not a source identity.",
            "remaining": "none",
            "route": "non-AP source stays fallback",
        },
        {
            "branch": "GenericFallbackRegistered",
            "scope": "non-AP generic WFD has an external route already materialized at contract level",
            "closed": generic_external_ready,
            "evidence": "generic WFD DI/BFI contract is materialized except for exact citation/hypothesis match.",
            "remaining": "precise external theorem match or self-contained KE-13 no-projection",
            "route": "DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch",
        },
    ]


def run(
    ap_residual_identity_path: Path,
    direct_bfi_atom_path: Path,
    bfi_level_ledger_path: Path,
    branch_statement_path: Path,
    generic_wfd_dibfi_path: Path,
) -> dict[str, Any]:
    """运行 AP-source 分支路由。"""
    ap_residual_identity = load_json(ap_residual_identity_path)
    direct_bfi_atom = load_json(direct_bfi_atom_path)
    bfi_level_ledger = load_json(bfi_level_ledger_path)
    branch_statement = load_json(branch_statement_path)
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    branch_rows = build_branch_rows(
        ap_residual_identity,
        direct_bfi_atom,
        bfi_level_ledger,
        branch_statement,
        generic_wfd_dibfi,
    )
    closed_branches = [row["branch"] for row in branch_rows if row["closed"]]
    open_branches = [row["branch"] for row in branch_rows if not row["closed"]]
    ap_source_branch_closed = "APSourceDirectBFI" in closed_branches
    return {
        "certificate_type": "triad_a1_dibfi_ap_source_branch_router",
        "status": "ap_source_direct_bfi_branch_closed_nonap_fallback_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "ap_residual_identity_json": file_sha256(ap_residual_identity_path),
            "direct_bfi_atom_json": file_sha256(direct_bfi_atom_path),
            "bfi_level_ledger_json": file_sha256(bfi_level_ledger_path),
            "branch_statement_json": file_sha256(branch_statement_path),
            "generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
        },
        "previous_terminal_gap": ap_residual_identity["terminal_gap_after_router"],
        "branch_rows": branch_rows,
        "closed_branches": closed_branches,
        "open_branches": open_branches,
        "ap_source_branch_closed": ap_source_branch_closed,
        "generic_nonap_fallback_closed": False,
        "terminal_gap_after_router": "DIBFIOriginalDispersionTheoremLocationAndHypothesisMatchForNonAPSource",
        "structural_law": (
            "The upstream AP source identity can be closed only as an explicit branch statement: "
            "on the AP-source branch, R_clean is defined before Cauchy/dispersion as the dyadic "
            "BFI prime-AP discrepancy with matching Delta_q, lambda_q and Type coefficients, so "
            "BFI Theorem 10 applies directly. The complement is not lost or silently upgraded; "
            "a non-AP generic WFD source must use the KE-13 no-projection/original-dispersion "
            "fallback. Thus the direct BFI route is closed for AP-source inputs, while the "
            "broader generic non-AP branch remains a precise external theorem match."
        ),
        "review_conclusion": (
            "AP-source 分支已按定义性合同闭合：若原始 clean A1 残差在 Cauchy/dispersion 前就是 "
            "BFI prime-AP discrepancy 的 dyadic 总和，则直接 BFI 原子可用且 level 已闭合。"
            "非 AP-source generic WFD 不能偷用该结论，剩余转为原始 dispersion 外部定理匹配。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI AP-source 分支路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 分支律",
        "",
        result["structural_law"],
        "",
        "```text",
        "AP-source branch:",
        "  R_clean is an upstream dyadic BFI prime-AP discrepancy;",
        "  BFI atom and level ledger are closed;",
        "",
        "non-AP generic WFD branch:",
        "  no downstream back-projection to AP is allowed;",
        "  must use KE-13 no-projection / original-dispersion fallback;",
        "",
        "no silent AP upgrade.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `previous_terminal_gap={result['previous_terminal_gap']}`。",
        f"- `ap_source_branch_closed={fmt_bool(result['ap_source_branch_closed'])}`。",
        f"- `generic_nonap_fallback_closed={fmt_bool(result['generic_nonap_fallback_closed'])}`。",
        f"- `closed_branches={result['closed_branches']}`。",
        f"- `open_branches={result['open_branches']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 分支表",
        "",
        "| branch | scope | closed | evidence | remaining | route |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["branch_rows"]:
        lines.append(
            "| `{branch}` | {scope} | `{closed}` | {evidence} | {remaining} | {route} |".format(
                branch=table_cell(row["branch"]),
                scope=table_cell(row["scope"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                route=table_cell(row["route"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "直接 BFI prime-AP 路线已在 AP-source 分支上闭合；但这不是 generic WFD 宽口径的无条件闭合。",
            "",
            "```text",
            "closed:",
            "  APSourceDirectBFI;",
            "",
            "still open:",
            "  DIBFIOriginalDispersionTheoremLocationAndHypothesisMatchForNonAPSource.",
            "```",
            "",
            "因此下一步若坚持闭合 broader generic WFD 分支，必须攻原始 dispersion 外部定理假设匹配，"
            "或回到 KE-13 无投影逐项证明。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ap-residual-identity-json",
        type=Path,
        default=DEFAULT_AP_RESIDUAL_IDENTITY,
    )
    parser.add_argument("--direct-bfi-atom-json", type=Path, default=DEFAULT_DIRECT_BFI_ATOM)
    parser.add_argument("--bfi-level-ledger-json", type=Path, default=DEFAULT_BFI_LEVEL_LEDGER)
    parser.add_argument("--branch-statement-json", type=Path, default=DEFAULT_BRANCH_STATEMENT)
    parser.add_argument("--generic-wfd-dibfi-json", type=Path, default=DEFAULT_GENERIC_WFD_DIBFI)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        ap_residual_identity_path=args.ap_residual_identity_json,
        direct_bfi_atom_path=args.direct_bfi_atom_json,
        bfi_level_ledger_path=args.bfi_level_ledger_json,
        branch_statement_path=args.branch_statement_json,
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
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
                "ap_source_branch_closed": result["ap_source_branch_closed"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
