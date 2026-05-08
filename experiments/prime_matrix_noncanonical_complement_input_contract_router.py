#!/usr/bin/env python3
"""固定 noncanonical full-S 补集的必要输入合同。

用法示例：
  python3 experiments/prime_matrix_noncanonical_complement_input_contract_router.py

输出：
  docs/monograph/prime-matrix-noncanonical-complement-input-contract-router.json
  docs/monograph/prime-matrix-noncanonical-complement-input-contract-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_RECONCILIATION = (
    DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
)
DEFAULT_TAXONOMY = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"
)
DEFAULT_OBSTRUCTION = (
    DOCS / "prime-matrix-global-unconditional-self-contained-obstruction-router.json"
)
DEFAULT_PROVENANCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_SOURCE_LOCK = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_FINAL_THEOREM = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
DEFAULT_MD = DOCS / "prime-matrix-noncanonical-complement-input-contract-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_gate(gates: list[str], gate: str) -> bool:
    """检查阻断门是否存在。"""
    return gate in gates


def contract_row(
    gate: str,
    verdict: str,
    closed: bool,
    evidence: str,
    consequence: str,
    required_input: str,
) -> dict[str, Any]:
    """构造合同审查行。"""
    return {
        "gate": gate,
        "verdict": verdict,
        "closed": closed,
        "evidence": evidence,
        "consequence": consequence,
        "required_input": required_input,
    }


def build_rows(
    reconciliation: dict[str, Any],
    taxonomy: dict[str, Any],
    obstruction: dict[str, Any],
    provenance: dict[str, Any],
    source_lock: dict[str, Any],
    final_theorem: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 noncanonical 补集输入合同表。"""
    updated_gates = reconciliation["updated_global_blocking_gates"]
    blocking_gates = obstruction["blocking_gates_for_full_global_closure"]
    provenance_closed = (
        provenance["actual_source_provenance_closed"]
        and provenance["open_provenance_gates"] == []
    )
    source_lock_closed = (
        source_lock["source_lock_contract_closed_for_canonical_branch"]
        and source_lock["branch_split_preserves_original_target"]
    )
    final_closed = (
        final_theorem["canonical_source_self_contained_theorem_closed"]
        and final_theorem["open_self_contained_gates"] == []
    )
    generic_refuted = (
        taxonomy["generic_self_contained_version_refuted"]
        and not taxonomy["original_unrestricted_self_contained_version_closed"]
    )
    actual_source_theorem_open = not taxonomy["actual_source_bridge_theorem_closed"]

    return [
        contract_row(
            gate="CanonicalBranchSubtracted",
            verdict="closed",
            closed=(
                reconciliation["actual_source_bridge_closed_for_canonical_branch"]
                and provenance_closed
                and source_lock_closed
                and final_closed
            ),
            evidence="actual-source provenance + source-lock + final theorem boundary",
            consequence="canonical 分支不再属于全局剩余。",
            required_input="none inside canonical branch",
        ),
        contract_row(
            gate="GenericWFDSelfContainedTemplate",
            verdict="refuted_not_available",
            closed=generic_refuted,
            evidence=taxonomy["terminal_gap_after_router"],
            consequence="不能把 unrestricted generic WFD 当作可补局部引理继续使用。",
            required_input="replace by actual-source theorem or external DI/BFI",
        ),
        contract_row(
            gate="OldActualFullSSourceBridge",
            verdict="superseded",
            closed=(
                reconciliation["old_blocker_superseded"] == "ActualFullSSourceBridge"
                and "ActualFullSSourceBridge" not in updated_gates
                and has_gate(updated_gates, "NoncanonicalFullSComplementAntiAtomOrExternalDIBFI")
            ),
            evidence="actual-source bridge global reconciliation",
            consequence="旧宽阻断门应改写成 noncanonical 补集输入合同。",
            required_input="NoncanonicalFullSComplementAntiAtomOrExternalDIBFI",
        ),
        contract_row(
            gate="SourceIdentityOption",
            verdict="open_input",
            closed=False,
            evidence="taxonomy.actual_source_bridge_theorem_closed=false",
            consequence="若能证明实际 full-S non-AP 源等于 canonical RIW/Buchstab 源，则补集回流已闭合边界。",
            required_input="ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab",
        ),
        contract_row(
            gate="StrengthenedAntiAtomOption",
            verdict="open_input",
            closed=False,
            evidence="terminal gap includes ProveActualSourceStrengthenedAntiAtom",
            consequence="若不能证明源恒等，必须直接证明实际 noncanonical 源的强化反原子。",
            required_input="FullSNonAPStrengthenedSourceAntiAtomForActualSource",
        ),
        contract_row(
            gate="ExternalDIBFIOption",
            verdict="open_external_or_new_proof",
            closed=False,
            evidence="DIBFIQuantifiedNoProjectionWindowCertificate remains in global blockers",
            consequence="外部/generic 路线需要无投影未中心化 dispersion 恒等式和量化窗口代入。",
            required_input="NoProjectionUncenteredDispersionIdentity + QuantifiedDIBFIWindowSubstitution",
        ),
        contract_row(
            gate="DStructureFinalPromotion",
            verdict="referee_block",
            closed=False,
            evidence="DStructureTailLog4FiniteRankinPromotion remains in global blockers",
            consequence="即便补集输入完成，完整行/列无条件晋级仍需 D-structure/Rankin 独立接受。",
            required_input="DStructureTailLog4FiniteRankinIndependentAcceptance",
        ),
        contract_row(
            gate="NoHiddenFourthRoute",
            verdict="contract_closed",
            closed=(
                actual_source_theorem_open
                and has_gate(updated_gates, "NoncanonicalFullSComplementAntiAtomOrExternalDIBFI")
                and has_gate(blocking_gates, "FullSNonAPStrengthenedSourceAntiAtom")
            ),
            evidence="taxonomy routes: canonical, refuted generic, external, actual-source",
            consequence="当前材料下没有第四条可自足偷渡路线。",
            required_input="choose source identity, strengthened anti-atom, or external DI/BFI",
        ),
    ]


def run(
    reconciliation_path: Path,
    taxonomy_path: Path,
    obstruction_path: Path,
    provenance_path: Path,
    source_lock_path: Path,
    final_theorem_path: Path,
) -> dict[str, Any]:
    """运行 noncanonical 补集输入合同判定。"""
    reconciliation = load_json(reconciliation_path)
    taxonomy = load_json(taxonomy_path)
    obstruction = load_json(obstruction_path)
    provenance = load_json(provenance_path)
    source_lock = load_json(source_lock_path)
    final_theorem = load_json(final_theorem_path)

    rows = build_rows(
        reconciliation=reconciliation,
        taxonomy=taxonomy,
        obstruction=obstruction,
        provenance=provenance,
        source_lock=source_lock,
        final_theorem=final_theorem,
    )
    contract_closed = all(row["closed"] for row in rows[:3]) and rows[-1]["closed"]
    open_inputs = [
        "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab",
        "FullSNonAPStrengthenedSourceAntiAtomForActualSource",
        "NoProjectionUncenteredDispersionIdentity",
        "QuantifiedDIBFIWindowSubstitution",
        "DStructureTailLog4FiniteRankinIndependentAcceptance",
    ]

    return {
        "certificate_type": "prime_matrix_noncanonical_complement_input_contract_router",
        "status": "noncanonical_complement_input_contract_pinned_global_unconditional_still_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "reconciliation": file_sha256(reconciliation_path),
            "taxonomy": file_sha256(taxonomy_path),
            "obstruction": file_sha256(obstruction_path),
            "provenance": file_sha256(provenance_path),
            "source_lock": file_sha256(source_lock_path),
            "final_theorem": file_sha256(final_theorem_path),
        },
        "contract_boundary_closed": contract_closed,
        "canonical_branch_removed_from_remainder": rows[0]["closed"],
        "generic_wfd_template_available": False,
        "noncanonical_complement_closed_by_current_corpus": False,
        "row_column_unconditional_closed": False,
        "necessary_input_family": [
            "Actual source identity with canonical RIW/Buchstab source",
            "Strengthened anti-atom for the actual noncanonical full-S source",
            "External or newly proved quantified no-projection DI/BFI route",
            "Independent D-structure/Tail-log4/finite Rankin promotion",
        ],
        "open_inputs": open_inputs,
        "rows": rows,
        "contract_law": (
            "After the canonical RIW/Buchstab branch is subtracted, the remaining full-S "
            "problem is not a generic WFD self-contained lemma: that template is refuted by "
            "the moving-delta model. The remaining noncanonical complement can only be "
            "closed by proving actual source identity, proving a strengthened anti-atom for "
            "the actual source, or by taking the quantified no-projection DI/BFI route. "
            "Final row-column promotion still separately requires the D-structure/Rankin "
            "acceptance gate."
        ),
        "review_conclusion": (
            "Noncanonical full-S 补集的必要输入合同已经固定；当前材料不能自足闭合完整全局行/列命题。"
            "下一步不是继续攻击 generic WFD 模板，而是证明实际源恒等、实际源强化反原子，或提交外部/量化 DI/BFI。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix noncanonical full-S 补集输入合同路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 合同律",
        "",
        result["contract_law"],
        "",
        "```text",
        f"contract_boundary_closed={fmt_bool(result['contract_boundary_closed'])}",
        (
            "canonical_branch_removed_from_remainder="
            f"{fmt_bool(result['canonical_branch_removed_from_remainder'])}"
        ),
        f"generic_wfd_template_available={fmt_bool(result['generic_wfd_template_available'])}",
        (
            "noncanonical_complement_closed_by_current_corpus="
            f"{fmt_bool(result['noncanonical_complement_closed_by_current_corpus'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 必要输入族",
        "",
    ]
    for item in result["necessary_input_family"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 3. 审查表",
            "",
            "| gate | verdict | closed | evidence | consequence | required input |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{verdict}` | `{closed}` | {evidence} | {consequence} | {required} |".format(
                gate=table_cell(row["gate"]),
                verdict=table_cell(row["verdict"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                consequence=table_cell(row["consequence"]),
                required=table_cell(row["required_input"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "该路由器闭合的是“必要输入边界”：canonical 分支已扣除，generic WFD 模板不可用，"
            "noncanonical 补集必须由实际源恒等、实际源强化反原子或外部/量化 DI/BFI 处理。"
            "它不证明这些输入本身，也不把完整行/列无条件命题升级为已证定理。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reconciliation-json", type=Path, default=DEFAULT_RECONCILIATION)
    parser.add_argument("--taxonomy-json", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--obstruction-json", type=Path, default=DEFAULT_OBSTRUCTION)
    parser.add_argument("--provenance-json", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--source-lock-json", type=Path, default=DEFAULT_SOURCE_LOCK)
    parser.add_argument("--final-theorem-json", type=Path, default=DEFAULT_FINAL_THEOREM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        reconciliation_path=args.reconciliation_json,
        taxonomy_path=args.taxonomy_json,
        obstruction_path=args.obstruction_json,
        provenance_path=args.provenance_json,
        source_lock_path=args.source_lock_json,
        final_theorem_path=args.final_theorem_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["open_inputs"])


if __name__ == "__main__":
    main()
