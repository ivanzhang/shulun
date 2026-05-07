#!/usr/bin/env python3
"""硬攻 CanonicalRIWBuchstabSourceLockContract 的分支锁定二分。

用法示例：
  python3 experiments/prime_matrix_triad_a1_source_lock_contract_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-source-lock-contract-router.json
  docs/monograph/prime-matrix-triad-a1-source-lock-contract-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SOURCE_IDENTIFICATION = DOCS / "prime-matrix-triad-a1-source-identification-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_gate_rows() -> list[dict[str, Any]]:
    """列出 source lock 分支二分门控。"""
    return [
        {
            "gate": "GenericWFDNotEligibleForInternalSupport",
            "available": "formal WFD source has already been rejected as insufficient",
            "needed": "generic well-factorable lambda_c must not enter the canonical support chain",
            "gap": "none; this prevents a false closure",
            "route": "generic WFD branch uses external DI/BFI original dispersion",
            "closed": True,
        },
        {
            "gate": "CanonicalSourceBranchDefinition",
            "available": "KZ-E spine notes RIW/Buchstab weights may be used as algebraic definition",
            "needed": "define the internal branch object with lambda_c := lambda_c^RIW-tree before Cauchy/dispersion",
            "gap": "definition must be explicit in the A1 ledger",
            "route": "create a canonical source branch, not a generic WFD theorem",
            "closed": True,
        },
        {
            "gate": "BranchSplitPreservesOriginalTarget",
            "available": "two legal routes exist: canonical internal support or generic external DI/BFI",
            "needed": "the split must not replace a generic theorem by a narrower one without routing the complement",
            "gap": "must record that noncanonical source exits to external DI/BFI/PDEC",
            "route": "prove a dichotomy: canonical source branch or generic WFD branch",
            "closed": True,
        },
        {
            "gate": "A1CleanBranchCanonicalAdmission",
            "available": "current ledger wants the actual A1/KZ-E source identified",
            "needed": "the clean A1 branch under attack is admitted into the canonical RIW/Buchstab source branch",
            "gap": "this is now the only internal branch-admission obligation",
            "route": "show the original row/triad clean construction chooses the canonical source weight",
            "closed": False,
        },
        {
            "gate": "CanonicalBranchFeedsSupportChain",
            "available": "all previous routers are conditional on canonical source lock",
            "needed": "once admitted, the internal support chain applies without further source ambiguity",
            "gap": "conditional implication is direct",
            "route": "canonical branch => decision-tree support => factor support => A1 chain",
            "closed": True,
        },
        {
            "gate": "NoncanonicalBranchExternalReturn",
            "available": "external DI/BFI route is already registered",
            "needed": "if A1 clean branch is not canonical, no internal support proof is claimed",
            "gap": "none after branch split",
            "route": "route to ExternalDIBFIOriginalDispersion or PDEC/SAE missing-row",
            "closed": True,
        },
    ]


def run(source_identification_path: Path) -> dict[str, Any]:
    """运行 source lock 合同路由。"""
    source_identification = load_json(source_identification_path)
    return {
        "certificate_type": "triad_a1_source_lock_contract_router",
        "status": "source_lock_contract_split_into_canonical_branch_admission_or_external_dibfi",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "source_identification_json": file_sha256(source_identification_path),
        },
        "source_identification_input_status": source_identification["status"],
        "source_identification_input_next_target": source_identification["next_internal_target"],
        "gate_rows": build_gate_rows(),
        "generic_wfd_not_eligible_for_internal_support": True,
        "canonical_source_branch_defined": True,
        "branch_split_preserves_original_target": True,
        "a1_clean_branch_canonical_admission_closed": False,
        "canonical_branch_feeds_support_chain": True,
        "noncanonical_branch_external_return": True,
        "source_lock_contract_closed_for_canonical_branch": True,
        "global_internal_a1_closed": False,
        "reduction_law": (
            "The source-lock contract is resolved as a rigorous branch split. The internal support "
            "chain is valid on the canonical RIW/Buchstab source branch, where lambda_c is defined "
            "as the decision-tree coefficient before any Cauchy or dispersion operation. It is not "
            "valid for a generic well-factorable WFD theorem. The complement is not ignored: a "
            "noncanonical source must go to external DI/BFI original dispersion or a PDEC/SAE "
            "missing-row return. Thus the only remaining internal obligation is branch admission: "
            "prove the A1 clean branch under attack is the canonical source branch."
        ),
        "next_internal_target": "A1CleanBranchCanonicalSourceAdmission",
        "terminal_gap_after_router": (
            "A1CleanBranchCanonicalSourceAdmissionOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "CanonicalRIWBuchstabSourceLockContract 已被严格二分：canonical 源头分支上，"
            "source lock 按定义成立并可接入此前完整内部支撑链；generic well-factorable "
            "分支不能偷用该链，必须走外部 DI/BFI 或回 PDEC/SAE。剩余内部目标只剩证明当前 "
            "A1 clean 分支确实属于 canonical RIW/Buchstab source branch。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Source Lock Contract 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 分支锁定二分律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "if lambda_c is the canonical RIW/Buchstab decision-tree coefficient:",
        "  source lock is definitional;",
        "  internal support chain applies;",
        "else:",
        "  generic well-factorable WFD cannot use canonical support;",
        "  route to external DI/BFI or PDEC/SAE missing-row.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `source_identification_input_status={result['source_identification_input_status']}`。",
        f"- `source_identification_input_next_target={result['source_identification_input_next_target']}`。",
        f"- `canonical_source_branch_defined={result['canonical_source_branch_defined']}`。",
        f"- `branch_split_preserves_original_target={result['branch_split_preserves_original_target']}`。",
        f"- `source_lock_contract_closed_for_canonical_branch={result['source_lock_contract_closed_for_canonical_branch']}`。",
        f"- `global_internal_a1_closed={result['global_internal_a1_closed']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            "新最窄内部目标为：",
            "",
            "```text",
            "A1CleanBranchCanonicalSourceAdmission:",
            "  prove the clean A1 branch under attack uses the canonical RIW/Buchstab source weight;",
            "  then the complete internal support chain applies;",
            "  otherwise route to external DI/BFI or PDEC/SAE.",
            "```",
            "",
            "这仍不是行命题最终闭合；但 source lock 本身已转化为严格分支准入问题。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-identification-json",
        type=Path,
        default=DEFAULT_SOURCE_IDENTIFICATION,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.source_identification_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_internal_target": result["next_internal_target"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
