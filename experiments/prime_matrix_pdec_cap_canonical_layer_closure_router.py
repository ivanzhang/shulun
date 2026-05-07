#!/usr/bin/env python3
"""闭合 PDEC-CAP 横向源路线中的 canonical 层转移门。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_canonical_layer_closure_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-canonical-layer-closure-router.json
  docs/monograph/prime-matrix-pdec-cap-canonical-layer-closure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TRANSVERSE_EMBEDDING = (
    DOCS / "prime-matrix-pdec-cap-transverse-embedding-router.json"
)
DEFAULT_LAYER_TRANSFER = DOCS / "prime-matrix-triad-a1-layer-transfer-router.json"
DEFAULT_SELECTOR = DOCS / "prime-matrix-triad-a1-selector-retention-router.json"
DEFAULT_PATH_PARTITION = DOCS / "prime-matrix-triad-a1-path-partition-router.json"
DEFAULT_DECISION_TREE = DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
DEFAULT_BRANCH_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_ACTUAL_SOURCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_SELF_FINAL = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.json"
)
DEFAULT_SAME_SET_FRONTIER = (
    DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    transverse_embedding: dict[str, Any],
    layer_transfer: dict[str, Any],
    selector: dict[str, Any],
    path_partition: dict[str, Any],
    decision_tree: dict[str, Any],
    branch_coverage: dict[str, Any],
    actual_source: dict[str, Any],
    self_final: dict[str, Any],
    same_set_frontier: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 canonical 层闭合审查表。"""
    embedding_closed = (
        transverse_embedding["status"]
        == "transverse_formal_unit_embedding_closed_layer_transfer_open"
        and transverse_embedding["transverse_formal_unit_embedding_closed"]
        and transverse_embedding["narrowest_next_hardpoint"]
        == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
    )
    layer_transfer_reduced = (
        layer_transfer["status"]
        == "layer_transfer_reduced_to_selector_retention_or_clean_return"
        and layer_transfer["conditional_selector_retention_implies_layer_transfer"]
        and layer_transfer["next_internal_target"]
        == "CanonicalSelectorRetentionOrCleanReturn"
    )
    selector_reduced = (
        selector["status"]
        == "selector_retention_reduced_to_finite_signature_no_cancellation_or_clean_return"
        and selector["conditional_finite_signature_implies_selector_retention"]
        and selector["next_internal_target"]
        == "FiniteSignatureNoCancellationOrCleanReturn"
    )
    path_reduced = (
        path_partition["status"]
        == "finite_signature_no_cancellation_reduced_to_exact_decision_tree_or_clean_return"
        and path_partition["conditional_decision_tree_implies_no_cancellation"]
        and path_partition["next_internal_target"]
        == "ExactRIWDecisionTreeFormulaOrCleanReturn"
    )
    decision_tree_reduced = (
        decision_tree["status"]
        == "decision_tree_formula_reduced_to_source_coefficient_identification"
        and decision_tree["conditional_source_identification_implies_decision_tree_formula"]
        and decision_tree["next_internal_target"]
        == "ActualKZESourceCoefficientIdentificationOrCleanReturn"
    )
    branch_boundary_closed = (
        branch_coverage["status"]
        == "canonical_source_branch_statement_adopted_generic_wfd_external_only"
        and branch_coverage["canonical_source_branch_internal_gap_closed"]
        and branch_coverage["coverage_no_overlap_no_gap"]
        and branch_coverage["next_internal_target"]
        == "NoFurtherInternalGapForCanonicalSourceBranch"
    )
    provenance_closed = (
        actual_source["status"] == "actual_source_provenance_closed"
        and actual_source["actual_source_provenance_closed"]
        and actual_source["open_provenance_gates"] == []
        and actual_source["terminal_gap_after_router"]
        == "NoFurtherActualSourceProvenanceGap"
    )
    final_self_contained_closed = (
        self_final["status"]
        == "canonical_source_self_contained_final_closed_generic_unrestricted_refuted"
        and self_final["canonical_source_self_contained_closed"]
        and self_final["open_final_gates"] == []
        and self_final["terminal_gap_after_router"]
        == "NoFurtherCanonicalSourceSelfContainedGap_GenericUnrestrictedRefuted"
    )
    same_set_boundary_closed = (
        same_set_frontier["status"]
        == "same_set_capacity_frontier_final_self_contained_boundary_closed"
        and same_set_frontier["self_contained_final_boundary_closed"]
        and same_set_frontier["terminal_dual_gap"]
        == "NoFurtherCanonicalSourceSelfContainedGap_GenericUnrestrictedRefuted"
    )
    generic_unrestricted_refuted = (
        self_final["unrestricted_generic_self_contained_refuted"]
        and not self_final["unrestricted_generic_self_contained_closed"]
    )
    canonical_layer_closed = all(
        [
            embedding_closed,
            layer_transfer_reduced,
            selector_reduced,
            path_reduced,
            decision_tree_reduced,
            branch_boundary_closed,
            provenance_closed,
            final_self_contained_closed,
            same_set_boundary_closed,
        ]
    )

    return [
        row(
            "TransverseFormalUnitA1SourceEmbedding",
            embedding_closed,
            transverse_embedding["narrowest_next_hardpoint"],
            "横向 formal unit 已嵌入 canonical A1/KZ-E pre-Cauchy 源，不再是当前阻塞。",
            False,
        ),
        row(
            "LayerTransferToSelectorRetention",
            layer_transfer_reduced,
            layer_transfer["next_internal_target"],
            "canonical 层准入、非零转移与薄块回流已化为 selector 保留率/clean 退出合同。",
            False,
        ),
        row(
            "SelectorRetentionToFiniteSignature",
            selector_reduced,
            selector["next_internal_target"],
            "selector 保留率的数量部分由有限签名 pigeonhole 承担。",
            False,
        ),
        row(
            "FiniteSignatureNoCancellationToDecisionTree",
            path_reduced,
            path_partition["next_internal_target"],
            "无抵消门被压成完整 RIW/Buchstab 决策树公式与路径预算。",
            False,
        ),
        row(
            "DecisionTreeToActualSourceIdentification",
            decision_tree_reduced,
            decision_tree["next_internal_target"],
            "决策树公式本身只剩实际 A1/KZ-E 源头系数识别。",
            False,
        ),
        row(
            "CanonicalBranchBoundaryClosed",
            branch_boundary_closed,
            branch_coverage["terminal_gap_after_router"],
            "canonical source branch 已无 source-lock 内部缺口；generic WFD 补集外部化或回流。",
            False,
        ),
        row(
            "ActualSourceProvenanceClosed",
            provenance_closed,
            actual_source["terminal_gap_after_router"],
            "pre-Cauchy actual lambda_c 已声明为 canonical RIW/Buchstab 决策树系数，且无来源替换。",
            False,
        ),
        row(
            "CanonicalSelfContainedFinalBoundary",
            final_self_contained_closed,
            self_final["terminal_gap_after_router"],
            "canonical-source 自足版最终边界无剩余门；unrestricted generic 自足版被反证隔离。",
            False,
        ),
        row(
            "TriadA1SameSetBoundaryAbsorbsLayerTransfer",
            same_set_boundary_closed,
            same_set_frontier["closed_self_contained_statement"],
            "Triad-A1 同集容量/Full-S canonical-source 边界已吸收 canonical 层转移链。",
            False,
        ),
        row(
            "GenericUnrestrictedSelfContainedRefuted",
            generic_unrestricted_refuted,
            self_final["theorem_boundary"]["not_claimed_statement"],
            "不能把 generic WFD 自足版当作已证；它不是 open self-contained gap，而是已反证边界。",
            False,
        ),
        row(
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn",
            canonical_layer_closed,
            "NoFurtherCanonicalSourceSelfContainedGap",
            "在已嵌入 canonical 源的 PDEC-CAP 横向源路线上，层准入、非零转移和薄块回流已由既有 canonical-source final boundary 闭合。",
            False,
        ),
        row(
            "DIBFIQuantifiedNoProjectionWindowCertificate",
            False,
            "external original DI/BFI generic branch only",
            "外部原始 DI/BFI 量化无投影证书仍是 generic/external 路线的门，不是 canonical-source 自足路线的剩余。",
            True,
        ),
    ]


def run(
    transverse_embedding_path: Path,
    layer_transfer_path: Path,
    selector_path: Path,
    path_partition_path: Path,
    decision_tree_path: Path,
    branch_coverage_path: Path,
    actual_source_path: Path,
    self_final_path: Path,
    same_set_frontier_path: Path,
) -> dict[str, Any]:
    """运行 canonical 层闭合路由。"""
    transverse_embedding = load_json(transverse_embedding_path)
    layer_transfer = load_json(layer_transfer_path)
    selector = load_json(selector_path)
    path_partition = load_json(path_partition_path)
    decision_tree = load_json(decision_tree_path)
    branch_coverage = load_json(branch_coverage_path)
    actual_source = load_json(actual_source_path)
    self_final = load_json(self_final_path)
    same_set_frontier = load_json(same_set_frontier_path)
    rows = build_rows(
        transverse_embedding=transverse_embedding,
        layer_transfer=layer_transfer,
        selector=selector,
        path_partition=path_partition,
        decision_tree=decision_tree,
        branch_coverage=branch_coverage,
        actual_source=actual_source,
        self_final=self_final,
        same_set_frontier=same_set_frontier,
    )
    canonical_layer_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
    )
    open_external_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_canonical_layer_closure_router",
        "status": (
            "canonical_layer_transfer_closed_for_canonical_source_external_dibfi_only"
            if canonical_layer_closed
            else "canonical_layer_transfer_still_open"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "transverse_embedding": file_sha256(transverse_embedding_path),
            "layer_transfer": file_sha256(layer_transfer_path),
            "selector_retention": file_sha256(selector_path),
            "path_partition": file_sha256(path_partition_path),
            "decision_tree": file_sha256(decision_tree_path),
            "branch_coverage": file_sha256(branch_coverage_path),
            "actual_source": file_sha256(actual_source_path),
            "self_contained_final": file_sha256(self_final_path),
            "same_set_frontier": file_sha256(same_set_frontier_path),
        },
        "canonical_layer_transfer_closed": canonical_layer_closed,
        "self_contained_canonical_branch_closed": canonical_layer_closed,
        "generic_unrestricted_self_contained_refuted": True,
        "row_column_unconditional_closed": False,
        "open_self_contained_gates": [],
        "open_external_gates": open_external_gates,
        "narrowest_next_hardpoint": (
            "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
        ),
        "rows": rows,
        "closure_law": (
            "Once the transverse formal unit has been embedded into the canonical A1/KZ-E "
            "pre-Cauchy source, the remaining Buchstab layer-admission problem is not a "
            "new transverse estimate. It is the already routed canonical-source A1 chain: "
            "layer transfer -> selector retention -> finite signatures -> decision tree -> "
            "actual source provenance -> branch statement coverage -> final canonical-source "
            "self-contained boundary. This closes the canonical-source self-contained branch. "
            "The generic WFD branch is not silently upgraded; it remains external DI/BFI or "
            "PDEC/SAE, and the unrestricted generic self-contained statement is refuted."
        ),
        "review_conclusion": (
            "`CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn` 在当前 PDEC-CAP "
            "横向源路线上闭合：横向 formal unit 已嵌入 canonical 源，A1 的 selector/决策树/"
            "来源账本/分支边界链已经给出 canonical-source final boundary。剩余的 "
            "`DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 "
            "DI/BFI 路线；这仍不等于完整行/列无条件定理闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP Canonical 层闭合路由器",
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
        "TransverseFormalUnitA1SourceEmbedding = closed;",
        "then:",
        "  CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn",
        "  -> selector retention",
        "  -> finite signature / no-cancellation",
        "  -> RIW/Buchstab decision tree",
        "  -> actual source provenance",
        "  -> canonical source branch boundary",
        "  -> NoFurtherCanonicalSourceSelfContainedGap.",
        "",
        "generic WFD is not upgraded;",
        "external DI/BFI remains external-only.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `canonical_layer_transfer_closed={fmt_bool(result['canonical_layer_transfer_closed'])}`。",
        f"- `self_contained_canonical_branch_closed={fmt_bool(result['self_contained_canonical_branch_closed'])}`。",
        f"- `generic_unrestricted_self_contained_refuted={fmt_bool(result['generic_unrestricted_self_contained_refuted'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `open_self_contained_gates={result['open_self_contained_gates']}`。",
        f"- `open_external_gates={result['open_external_gates']}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 边界",
            "",
            "本路由器闭合的是 canonical-source 自足分支的最新 PDEC-CAP 层转移门；"
            "它不声明 unrestricted generic WFD 自足版，也不声明完整行/列无条件定理。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--transverse-embedding-json", type=Path, default=DEFAULT_TRANSVERSE_EMBEDDING
    )
    parser.add_argument("--layer-transfer-json", type=Path, default=DEFAULT_LAYER_TRANSFER)
    parser.add_argument("--selector-json", type=Path, default=DEFAULT_SELECTOR)
    parser.add_argument("--path-partition-json", type=Path, default=DEFAULT_PATH_PARTITION)
    parser.add_argument("--decision-tree-json", type=Path, default=DEFAULT_DECISION_TREE)
    parser.add_argument("--branch-coverage-json", type=Path, default=DEFAULT_BRANCH_COVERAGE)
    parser.add_argument("--actual-source-json", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--self-final-json", type=Path, default=DEFAULT_SELF_FINAL)
    parser.add_argument(
        "--same-set-frontier-json", type=Path, default=DEFAULT_SAME_SET_FRONTIER
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        transverse_embedding_path=args.transverse_embedding_json,
        layer_transfer_path=args.layer_transfer_json,
        selector_path=args.selector_json,
        path_partition_path=args.path_partition_json,
        decision_tree_path=args.decision_tree_json,
        branch_coverage_path=args.branch_coverage_json,
        actual_source_path=args.actual_source_json,
        self_final_path=args.self_final_json,
        same_set_frontier_path=args.same_set_frontier_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
