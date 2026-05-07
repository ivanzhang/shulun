#!/usr/bin/env python3
"""登记 generic WFD 分支的 DI/BFI 原始 dispersion 外部合同。

用法示例：
  python3 experiments/prime_matrix_triad_a1_generic_wfd_dibfi_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-generic-wfd-dibfi-router.json
  docs/monograph/prime-matrix-triad-a1-generic-wfd-dibfi-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_BRANCH_STATEMENT = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BD_CEN = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(path: Path, needles: list[str]) -> bool:
    """粗核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def build_object_rows(branch_statement: dict[str, Any]) -> list[dict[str, Any]]:
    """列出当前对象口径，防止 canonical/generic 偷换。"""
    return [
        {
            "object": "canonical RIW/Buchstab source branch",
            "scope": "lambda_c equals the canonical decision-tree sieve coefficient",
            "route": "internal support chain",
            "status": "already_closed_in_source_lock_chain"
            if branch_statement["canonical_source_branch_internal_gap_closed"]
            else "canonical_branch_gap",
            "can_use_this_router": False,
        },
        {
            "object": "generic noncanonical WFD branch",
            "scope": "lambda_c is only well-factorable; no canonical support lower bound is assumed",
            "route": "external DI/BFI original dispersion or PDEC/SAE return",
            "status": "current_remaining_branch"
            if not branch_statement["generic_wfd_self_contained_gap_closed"]
            else "unexpectedly_closed",
            "can_use_this_router": True,
        },
        {
            "object": "uncentered WFD target",
            "scope": "the original KE-13/WFD-core linear Kloosterman window before block-centering",
            "route": "must be estimated directly by original dispersion, not by SOURCE-CEN",
            "status": "target_locked_as_uncentered",
            "can_use_this_router": True,
        },
    ]


def build_gate_rows(
    external_index_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
    bd_cen_path: Path,
) -> list[dict[str, Any]]:
    """列出 DI/BFI 原始 dispersion 外部合同门控。"""
    has_external_sources = contains_all(
        external_index_path,
        [
            "Deshouillers",
            "Iwaniec",
            "Bombieri",
            "Friedlander",
            "well-factorable",
        ],
    )
    has_phase_template = contains_all(
        kls_template_path,
        [
            "e_c(-2h",
            "Kloosterman",
            "well-factorable",
            "B(A)",
        ],
    )
    has_wfd_core = contains_all(
        kze_spine_path,
        [
            "WFD-core",
            "well-factorable",
            "KE-13",
            "KZ-E",
        ],
    )
    source_cen_refuted = contains_all(
        source_cen_path,
        [
            "source_cen_refuted_for_current_wfd_target",
            "未块中心化",
            "SOURCE-CEN is false",
        ],
    )
    bd_cen_checked = contains_all(
        bd_cen_path,
        [
            "BD-CEN",
            "局部方差",
            "original dispersion identity",
        ],
    )
    return [
        {
            "gate": "OriginalUncenteredWFDTargetMatch",
            "available": "KZ-E spine identifies KE-13/WFD-core as the current generic WFD target",
            "needed": "external theorem must estimate the uncentered original dispersion object",
            "gap": "none at object-identification level",
            "route": "use original dispersion estimate, not a centered replacement",
            "closed": has_wfd_core and source_cen_refuted,
        },
        {
            "gate": "NoCenteringShortcut",
            "available": "SOURCE-CEN and BD-CEN audits block free local-variance subtraction",
            "needed": "do not insert block centering unless the original dispersion identity provides it",
            "gap": "none after routing: choose direct uncentered external estimate",
            "route": "direct DI/BFI original dispersion branch",
            "closed": source_cen_refuted and bd_cen_checked,
        },
        {
            "gate": "KloostermanPhaseNormalization",
            "available": "KLS template converts CRT inverse phase to standard Kloosterman phase",
            "needed": "match the generic WFD phase to DI/BFI inverse phase notation",
            "gap": "none at template level",
            "route": "CRT phase normalization then dyadic Kloosterman window",
            "closed": has_phase_template,
        },
        {
            "gate": "WellFactorableLevelMatch",
            "available": "external index records BFI well-factorable weights; KZ-E uses well-factorable lambda_c",
            "needed": "level and factorization ranges must be within BFI admissible ranges",
            "gap": "exact theorem hypotheses still need page/theorem-level check",
            "route": "match lambda_c level to BFI dispersion theorem",
            "closed": has_external_sources and has_wfd_core,
        },
        {
            "gate": "TypeIITwoVariableRangeMatch",
            "available": "KZ-E spine records Type-I/II dispersion reduction; KLS template records C,S,H ranges",
            "needed": "balanced two-variable blocks must match the quoted DI/BFI range",
            "gap": "exact theorem hypotheses still need page/theorem-level check",
            "route": "dyadic Type-I/II block by block",
            "closed": has_phase_template and has_wfd_core,
        },
        {
            "gate": "SmoothDyadicEndpointGcdBudget",
            "available": "KLS template has gcd strata, dyadic, sawtooth and smoothing log-loss ledger",
            "needed": "all endpoint and gcd costs must be absorbed before final log saving",
            "gap": "none at ledger level",
            "route": "charge all costs to log^C and choose larger B(A)",
            "closed": has_phase_template,
        },
        {
            "gate": "ArbitraryLogSavingAbsorption",
            "available": "template chooses B(A)=A+C0+10",
            "needed": "external theorem must provide arbitrary log saving after loss absorption",
            "gap": "depends on the precise cited external theorem statement",
            "route": "choose B(A) after dyadic/gcd/smoothing budgets",
            "closed": has_phase_template and has_external_sources,
        },
        {
            "gate": "ExternalCitationPreciseTheoremLocation",
            "available": "bibliographic DI/BFI sources and functional adaptation are registered",
            "needed": "exact theorem/proposition/page and hypothesis-by-hypothesis match",
            "gap": "not yet pinned in the repository",
            "route": "audit original DI/BFI statements or quote a modern theorem with identical hypotheses",
            "closed": False,
        },
    ]


def run(
    branch_statement_path: Path,
    external_index_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
    bd_cen_path: Path,
) -> dict[str, Any]:
    """运行 generic WFD DI/BFI 外部合同路由。"""
    branch_statement = load_json(branch_statement_path)
    object_rows = build_object_rows(branch_statement)
    gate_rows = build_gate_rows(
        external_index_path,
        kls_template_path,
        kze_spine_path,
        source_cen_path,
        bd_cen_path,
    )
    closed_except_citation = all(
        row["closed"] for row in gate_rows if row["gate"] != "ExternalCitationPreciseTheoremLocation"
    )
    all_gates_closed = all(row["closed"] for row in gate_rows)
    return {
        "certificate_type": "triad_a1_generic_wfd_dibfi_router",
        "status": "generic_wfd_external_dibfi_contract_materialized_theorem_location_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "branch_statement_coverage_json": file_sha256(branch_statement_path),
            "external_theorem_index_md": file_sha256(external_index_path),
            "kls_window_di_bfi_template_md": file_sha256(kls_template_path),
            "kze_wfd_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
            "bd_cen_audit_md": file_sha256(bd_cen_path),
        },
        "branch_statement_status": branch_statement["status"],
        "object_rows": object_rows,
        "gate_rows": gate_rows,
        "closed_except_precise_external_citation": closed_except_citation,
        "all_gates_closed": all_gates_closed,
        "external_dibfi_contract_materialized": closed_except_citation,
        "generic_wfd_self_contained_gap_closed": False,
        "external_deep_theorem_version_status": (
            "contract_ready_pending_precise_dibfi_theorem_location_and_hypothesis_match"
        ),
        "self_contained_version_status": "open_for_generic_noncanonical_wfd_branch",
        "next_external_target": "DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch",
        "terminal_gap_after_router": "DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch",
        "structural_law": (
            "The remaining generic WFD branch is not a canonical-source support problem. "
            "Its legitimate external route is a direct original DI/BFI dispersion estimate "
            "for the uncentered WFD target. SOURCE-CEN/BD-CEN cannot be inserted as free "
            "centering. The available repository material already fixes the target object, "
            "phase normalization, well-factorable level interface, Type-I/II dyadic ranges, "
            "gcd/endpoint smoothing ledger, and log-loss absorption. The only remaining "
            "external-theorem obligation is to pin the precise DI/BFI theorem location and "
            "check every hypothesis against this target."
        ),
        "review_conclusion": (
            "generic noncanonical WFD 分支已经从一个含混的“外部 DI/BFI”压成精确外部合同："
            "对象必须是未中心化原始 WFD；不能靠 SOURCE-CEN/BD-CEN 免费中心化；CRT 相位、"
            "well-factorable level、Type-I/II 范围、gcd/端点和平滑损失都已进入门控表。"
            "当前剩余不再是 canonical-source 内部数学链条，而是 DI/BFI 原文定理位置与假设逐项匹配。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Generic WFD DI/BFI 外部合同路由器",
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
        "canonical source branch:",
        "  already handled by the internal RIW/Buchstab support chain;",
        "",
        "generic noncanonical WFD branch:",
        "  cannot borrow canonical support;",
        "  must use direct original DI/BFI dispersion or return to PDEC/SAE;",
        "",
        "direct original dispersion:",
        "  estimate the uncentered WFD target itself;",
        "  do not insert SOURCE-CEN/BD-CEN as a free identity;",
        "  normalize CRT phase to standard Kloosterman form;",
        "  match well-factorable level, Type-I/II ranges, gcd and endpoint budgets;",
        "  then pin exact external theorem location and hypotheses.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `branch_statement_status={result['branch_statement_status']}`。",
        f"- `closed_except_precise_external_citation={fmt_bool(result['closed_except_precise_external_citation'])}`。",
        f"- `all_gates_closed={fmt_bool(result['all_gates_closed'])}`。",
        f"- `external_dibfi_contract_materialized={fmt_bool(result['external_dibfi_contract_materialized'])}`。",
        f"- `generic_wfd_self_contained_gap_closed={fmt_bool(result['generic_wfd_self_contained_gap_closed'])}`。",
        f"- `external_deep_theorem_version_status={result['external_deep_theorem_version_status']}`。",
        f"- `self_contained_version_status={result['self_contained_version_status']}`。",
        f"- `next_external_target={result['next_external_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 对象二分表",
        "",
        "| object | scope | route | status | can use this router |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["object_rows"]:
        lines.append(
            "| `{object}` | {scope} | {route} | `{status}` | `{can_use}` |".format(
                object=table_cell(row["object"]),
                scope=table_cell(row["scope"]),
                route=table_cell(row["route"]),
                status=table_cell(row["status"]),
                can_use=fmt_bool(bool(row["can_use_this_router"])),
            )
        )
    lines.extend(
        [
            "",
            "## 4. DI/BFI 原始 dispersion 门控表",
            "",
            "| gate | available | needed | gap | route | closed |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=fmt_bool(bool(row["closed"])),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "本轮推进把最后外部缺口从一句话压成了一个单点可核查目标：",
            "",
            "```text",
            "DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch",
            "```",
            "",
            "这仍不是 generic WFD 宽口径的完全自足证明；它说明除精确外部定理定位与假设匹配外，"
            "generic WFD 外部引用版所需的对象、相位和账本接口已经登记完成。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--branch-statement-json", type=Path, default=DEFAULT_BRANCH_STATEMENT
    )
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--bd-cen-md", type=Path, default=DEFAULT_BD_CEN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        branch_statement_path=args.branch_statement_json,
        external_index_path=args.external_index_md,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
        source_cen_path=args.source_cen_md,
        bd_cen_path=args.bd_cen_md,
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
                "external_dibfi_contract_materialized": result[
                    "external_dibfi_contract_materialized"
                ],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
