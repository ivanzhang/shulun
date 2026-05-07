#!/usr/bin/env python3
"""分类 full-S 自足闭合路线并钉住实际源头桥输入。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_self_contained_closure_taxonomy_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_TERMINAL_SPLIT = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json"
)
DEFAULT_FULL_S_KLS_EXT = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json"
)
DEFAULT_SELF_CONTAINED_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_BRANCH_STATEMENT_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_SOURCE_LOCK_CONTRACT = (
    DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
)
DEFAULT_MD = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.md"
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


def build_rows(
    terminal_split: dict[str, Any],
    full_s_kls_ext: dict[str, Any],
    self_contained_antiatom_nogo: dict[str, Any],
    branch_statement_coverage: dict[str, Any],
    source_lock_contract: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造自足闭合分类账本。"""
    external_closed = (
        terminal_split["external_contract_version_closed"]
        and full_s_kls_ext["external_theorem_contract_closed"]
    )
    canonical_restricted_closed = (
        branch_statement_coverage["canonical_source_branch_internal_gap_closed"]
        and branch_statement_coverage["next_internal_target"]
        == "NoFurtherInternalGapForCanonicalSourceBranch"
    )
    generic_refuted = (
        self_contained_antiatom_nogo["self_contained_generic_version_refuted"]
        and not self_contained_antiatom_nogo[
            "self_contained_generic_version_closed_as_proof"
        ]
    )
    no_silent_upgrade = (
        source_lock_contract["terminal_gap_after_router"]
        == "A1CleanBranchCanonicalSourceAdmissionOrExternalDIBFIOriginalDispersion"
        and branch_statement_coverage["generic_wfd_self_contained_gap_closed"]
        is False
    )
    taxonomy_closed = all(
        [
            external_closed,
            canonical_restricted_closed,
            generic_refuted,
            no_silent_upgrade,
        ]
    )
    actual_source_bridge_pinned = taxonomy_closed
    return [
        {
            "gate": "ExternalGenericContractClosed",
            "closed": external_closed,
            "evidence": (
                f"terminal_split.external={terminal_split['external_contract_version_closed']}; "
                f"FullS-KLS-ext={full_s_kls_ext['external_theorem_contract_closed']}."
            ),
            "remaining": "none for the external-contract theorem",
            "next_target": "DoNotConfuseWithSelfContainedProof",
        },
        {
            "gate": "CanonicalRestrictedSelfContainedClosed",
            "closed": canonical_restricted_closed,
            "evidence": (
                "Branch coverage records no further internal source-lock gap for the "
                "canonical RIW/Buchstab source branch."
            ),
            "remaining": "only the statement must remain branch-restricted",
            "next_target": "ActualSourceBridge",
        },
        {
            "gate": "GenericSelfContainedRefuted",
            "closed": generic_refuted,
            "evidence": (
                "The moving-delta capacity model violates the required source anti-atom "
                "while passing the current formal generic WFD templates."
            ),
            "remaining": "unrestricted generic WFD cannot be closed as a self-contained proof",
            "next_target": "ActualSourceBridge",
        },
        {
            "gate": "NoSilentCanonicalUpgrade",
            "closed": no_silent_upgrade,
            "evidence": (
                "Source-lock and branch-coverage ledgers forbid importing the canonical "
                "support chain into the generic WFD branch without proving source identity."
            ),
            "remaining": "actual source must be locked, not assumed",
            "next_target": "ActualSourceBridge",
        },
        {
            "gate": "RouteTaxonomyClosed",
            "closed": taxonomy_closed,
            "evidence": (
                "The routes are now exhaustive: external generic theorem is closed; "
                "canonical-restricted self-contained branch is closed; unrestricted "
                "generic self-contained branch is refuted."
            ),
            "remaining": "none at classification level",
            "next_target": "ActualA1FullSSourceLockOrStrengthenedAntiAtom",
        },
        {
            "gate": "ActualSourceBridgePinned",
            "closed": actual_source_bridge_pinned,
            "evidence": (
                "To convert the conditional canonical closure into the desired self-contained "
                "full-S closure, the actual source must either be canonical RIW/Buchstab "
                "or satisfy a strengthened source anti-atom theorem."
            ),
            "remaining": "prove one of the two actual-source bridge theorems",
            "next_target": "ActualA1FullSSourceLockOrStrengthenedAntiAtom",
        },
        {
            "gate": "ActualSourceBridgeTheoremClosed",
            "closed": False,
            "evidence": (
                "No current ledger proves that the actual full-S non-AP WFD source is "
                "canonical RIW/Buchstab, and no current ledger proves the strengthened "
                "source anti-atom bound for the actual noncanonical source."
            ),
            "remaining": "this is the new narrowest self-contained theorem input",
            "next_target": "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
        },
    ]


def run(
    terminal_split_path: Path,
    full_s_kls_ext_path: Path,
    self_contained_antiatom_nogo_path: Path,
    branch_statement_coverage_path: Path,
    source_lock_contract_path: Path,
) -> dict[str, Any]:
    """运行 full-S 自足闭合分类路由。"""
    terminal_split = load_json(terminal_split_path)
    full_s_kls_ext = load_json(full_s_kls_ext_path)
    self_contained_antiatom_nogo = load_json(self_contained_antiatom_nogo_path)
    branch_statement_coverage = load_json(branch_statement_coverage_path)
    source_lock_contract = load_json(source_lock_contract_path)
    rows = build_rows(
        terminal_split,
        full_s_kls_ext,
        self_contained_antiatom_nogo,
        branch_statement_coverage,
        source_lock_contract,
    )
    closed_by_gate = {row["gate"]: bool(row["closed"]) for row in rows}
    taxonomy_closed = closed_by_gate["RouteTaxonomyClosed"]
    actual_source_bridge_pinned = closed_by_gate["ActualSourceBridgePinned"]
    actual_source_bridge_closed = closed_by_gate["ActualSourceBridgeTheoremClosed"]
    status = (
        "self_contained_closure_taxonomy_closed_actual_source_bridge_open"
        if taxonomy_closed and actual_source_bridge_pinned
        else "self_contained_closure_taxonomy_incomplete"
    )
    terminal_gap = (
        "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
        if not actual_source_bridge_closed
        else "NoFurtherSelfContainedFullSSourceGap"
    )
    return {
        "certificate_type": "triad_a1_dibfi_self_contained_closure_taxonomy_router",
        "status": status,
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "terminal_split_json": file_sha256(terminal_split_path),
            "full_s_kls_ext_json": file_sha256(full_s_kls_ext_path),
            "self_contained_antiatom_nogo_json": file_sha256(
                self_contained_antiatom_nogo_path
            ),
            "branch_statement_coverage_json": file_sha256(
                branch_statement_coverage_path
            ),
            "source_lock_contract_json": file_sha256(source_lock_contract_path),
        },
        "taxonomy_rows": rows,
        "closed_taxonomy_gates": [row["gate"] for row in rows if row["closed"]],
        "open_taxonomy_gates": [row["gate"] for row in rows if not row["closed"]],
        "external_contract_version_closed": closed_by_gate[
            "ExternalGenericContractClosed"
        ],
        "canonical_restricted_self_contained_version_closed": closed_by_gate[
            "CanonicalRestrictedSelfContainedClosed"
        ],
        "generic_self_contained_version_refuted": closed_by_gate[
            "GenericSelfContainedRefuted"
        ],
        "original_unrestricted_self_contained_version_closed": False,
        "actual_source_bridge_pinned": actual_source_bridge_pinned,
        "actual_source_bridge_theorem_closed": actual_source_bridge_closed,
        "terminal_gap_after_router": terminal_gap,
        "terminal_gap_expansion": [
            "ProveActualSourceIsCanonicalRIWBuchstab",
            "ProveActualSourceStrengthenedAntiAtom",
            "AcceptExternalFullSKLSExtForGenericBranch",
        ],
        "actual_source_bridge_contract": (
            "For the actual full-S non-AP A1/KZ-E source entering the dispersion step, "
            "prove either lambda_c equals the canonical RIW/Buchstab decision-tree source, "
            "or prove the strengthened anti-atom bound "
            "max_{u,v} M_{u,v}/sum M_{u,v} <= log^{-2A} for that actual source."
        ),
        "structural_law": (
            "The self-contained problem has changed type. It is no longer an unrestricted "
            "generic WFD dispersion estimate, because that statement is refuted by the "
            "moving-delta model. It is also not an external-theorem problem, because FullS-KLS-ext "
            "already closes that version. The only honest self-contained bridge is an actual-source "
            "theorem: identify the actual source as canonical RIW/Buchstab, or prove that the "
            "actual noncanonical source has the strengthened anti-atom property."
        ),
        "review_conclusion": (
            "自足闭合路线已完成分类：外部 generic 合同版闭合；canonical-restricted 自足分支闭合；"
            "unrestricted generic 自足版被 moving-delta 反证。真正剩余不是继续攻击 generic WFD，"
            "而是证明实际 full-S non-AP 源头满足 canonical source lock 或 strengthened source anti-atom。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI self-contained closure taxonomy 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 实际源头桥合同",
        "",
        f"`{result['actual_source_bridge_contract']}`",
        "",
        "## 2. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "external generic theorem:",
        f"  closed = {fmt_bool(result['external_contract_version_closed'])};",
        "",
        "canonical-restricted self-contained theorem:",
        f"  closed = {fmt_bool(result['canonical_restricted_self_contained_version_closed'])};",
        "",
        "unrestricted generic self-contained theorem:",
        f"  refuted = {fmt_bool(result['generic_self_contained_version_refuted'])};",
        "",
        "new actual-source terminal:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 3. 汇总",
        "",
        f"- `external_contract_version_closed={fmt_bool(result['external_contract_version_closed'])}`。",
        f"- `canonical_restricted_self_contained_version_closed={fmt_bool(result['canonical_restricted_self_contained_version_closed'])}`。",
        f"- `generic_self_contained_version_refuted={fmt_bool(result['generic_self_contained_version_refuted'])}`。",
        f"- `original_unrestricted_self_contained_version_closed={fmt_bool(result['original_unrestricted_self_contained_version_closed'])}`。",
        f"- `actual_source_bridge_pinned={fmt_bool(result['actual_source_bridge_pinned'])}`。",
        f"- `actual_source_bridge_theorem_closed={fmt_bool(result['actual_source_bridge_theorem_closed'])}`。",
        f"- `terminal_gap_expansion={result['terminal_gap_expansion']}`。",
        "",
        "## 4. 分类账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["taxonomy_rows"]:
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
            "完全自足版不能再以 unrestricted generic WFD 原命题形式推进；该形式已被反例阻断。"
            "可继续硬攻的最窄目标是：",
            "",
            "```text",
            "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
            "```",
            "",
            "它有且只有两个自足证明方向：证明实际源头等于 canonical RIW/Buchstab 决策树源头，"
            "或直接证明实际源头的 strengthened anti-atom。"
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--terminal-split-json", type=Path, default=DEFAULT_TERMINAL_SPLIT
    )
    parser.add_argument(
        "--full-s-kls-ext-json", type=Path, default=DEFAULT_FULL_S_KLS_EXT
    )
    parser.add_argument(
        "--self-contained-antiatom-nogo-json",
        type=Path,
        default=DEFAULT_SELF_CONTAINED_ANTIATOM_NOGO,
    )
    parser.add_argument(
        "--branch-statement-coverage-json",
        type=Path,
        default=DEFAULT_BRANCH_STATEMENT_COVERAGE,
    )
    parser.add_argument(
        "--source-lock-contract-json",
        type=Path,
        default=DEFAULT_SOURCE_LOCK_CONTRACT,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        terminal_split_path=args.terminal_split_json,
        full_s_kls_ext_path=args.full_s_kls_ext_json,
        self_contained_antiatom_nogo_path=args.self_contained_antiatom_nogo_json,
        branch_statement_coverage_path=args.branch_statement_coverage_json,
        source_lock_contract_path=args.source_lock_contract_json,
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
                "actual_source_bridge_theorem_closed": result[
                    "actual_source_bridge_theorem_closed"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
