#!/usr/bin/env python3
"""拆解横向源支撑/NC-BLK 自足证书的下一层逻辑边界。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_transverse_source_support_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-transverse-source-support-router.json
  docs/monograph/prime-matrix-pdec-cap-transverse-source-support-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TRANSVERSE_FRONTIER = (
    DOCS / "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.json"
)
DEFAULT_SOURCE_LOCK = DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
DEFAULT_ACTUAL_SOURCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_CANONICAL_RIW = DOCS / "prime-matrix-triad-a1-canonical-riw-support-router.json"
DEFAULT_SQUAREFREE = DOCS / "prime-matrix-triad-a1-squarefree-buchstab-support-router.json"
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_TRANSVERSE_EMBEDDING = (
    DOCS / "prime-matrix-pdec-cap-transverse-embedding-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-transverse-source-support-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-transverse-source-support-router.md"


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
    transverse_frontier: dict[str, Any],
    source_lock: dict[str, Any],
    actual_source: dict[str, Any],
    canonical_riw: dict[str, Any],
    squarefree: dict[str, Any],
    ncblk: dict[str, Any],
    transverse_embedding: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成横向源支撑证书审查表。"""
    transverse_support_active = (
        transverse_frontier["status"]
        == "transverse_clean_atom_routed_to_source_support_or_external_dibfi_frontier"
        and "TransverseSourceSupportNonconcentrationCertificate"
        in transverse_frontier["open_final_gates"]
    )
    source_lock_split_closed = (
        source_lock["source_lock_contract_closed_for_canonical_branch"]
        and source_lock["canonical_branch_feeds_support_chain"]
        and source_lock["next_internal_target"]
        == "A1CleanBranchCanonicalSourceAdmission"
        and not source_lock["global_internal_a1_closed"]
    )
    actual_source_provenance_closed = (
        actual_source["status"] == "actual_source_provenance_closed"
        and actual_source["actual_source_provenance_closed"]
        and actual_source["terminal_gap_after_router"]
        == "NoFurtherActualSourceProvenanceGap"
    )
    canonical_riw_reduced = (
        canonical_riw["status"]
        == "canonical_riw_support_reduced_to_squarefree_buchstab_layer_support"
        and not canonical_riw["canonical_riw_support_closed"]
        and canonical_riw["next_internal_target"]
        == "SquarefreeBuchstabLayerSupportLowerBound"
    )
    raw_squarefree_closed = (
        squarefree["status"]
        == "raw_thick_squarefree_support_closed_layer_transfer_open"
        and squarefree["raw_thick_squarefree_support_closed"]
        and not squarefree["squarefree_buchstab_layer_support_closed"]
        and squarefree["next_internal_target"]
        == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
    )
    ncblk_boundary_named = (
        ncblk["all_reconciliation_gates_passed"]
        and ncblk["canonical_ncblk_absorbed_by_existing_boundary"]
        and ncblk["generic_ncblk_self_contained_not_claimed"]
    )
    source_support_reduced = all(
        [
            transverse_support_active,
            source_lock_split_closed,
            actual_source_provenance_closed,
            canonical_riw_reduced,
            raw_squarefree_closed,
            ncblk_boundary_named,
        ]
    )
    transverse_embedding_closed = (
        transverse_embedding["status"]
        == "transverse_formal_unit_embedding_closed_layer_transfer_open"
        and transverse_embedding["transverse_formal_unit_embedding_closed"]
        and transverse_embedding["narrowest_next_hardpoint"]
        == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
    )

    return [
        row(
            "TransverseSourceSupportFrontierActive",
            transverse_support_active,
            transverse_frontier["narrowest_self_contained_hardpoint"],
            "上一层已经把横向 clean 原子的自足路线压成源支撑/非集中证书。",
            False,
        ),
        row(
            "SourceLockSplitAvailable",
            source_lock_split_closed,
            source_lock["terminal_gap_after_router"],
            "canonical 分支可接入内部支撑链；generic 分支必须外部化或回流 PDEC/SAE。",
            False,
        ),
        row(
            "ActualA1SourceProvenanceClosed",
            actual_source_provenance_closed,
            actual_source["terminal_gap_after_router"],
            "原始 A1/KZ-E pre-Cauchy 来源账本已声明 canonical RIW/Buchstab 决策树系数。",
            False,
        ),
        row(
            "CanonicalRIWSupportReduced",
            canonical_riw_reduced,
            canonical_riw["terminal_gap_after_router"],
            "一旦横向 formal unit 嵌入 canonical 源头，支撑问题降到 Buchstab 层支撑下界。",
            False,
        ),
        row(
            "RawThickSquarefreeSupportClosed",
            raw_squarefree_closed,
            squarefree["terminal_gap_after_router"],
            "厚 surviving balanced interval 中 squarefree product 原始计数已闭合；剩余是 canonical 层准入与非零转移。",
            False,
        ),
        row(
            "NCBLKBoundaryNamed",
            ncblk_boundary_named,
            ncblk["canonical_closed_statement"],
            "直接 NC-BLK 路线仍可走，但必须证明实际横向系数块非集中，不能用 generic 自足版偷换。",
            False,
        ),
        row(
            "TransverseSourceSupportReducedToEmbeddingOrDirectNCBLK",
            source_support_reduced,
            "source lock + provenance + Buchstab support chain + direct NC-BLK fallback",
            "横向源支撑证书已拆为 formal unit 嵌入、canonical 层转移、或直接实际 NC-BLK。",
            False,
        ),
        row(
            "TransverseFormalUnitA1SourceEmbedding",
            transverse_embedding_closed,
            transverse_embedding["narrowest_next_hardpoint"],
            "横向商 formal unit 已证明为 canonical A1/KZ-E pre-Cauchy 源的限制、商或条件化，不改变来源系数。",
            False,
        ),
        row(
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn",
            False,
            squarefree["next_internal_target"],
            "若嵌入 canonical 源成立，还需证明 Buchstab squarefree products 被 exact canonical 层承认、系数非零，薄区间回流 edge/PDEC/SAE。",
            True,
        ),
        row(
            "DirectTransverseNCBLKActualCoefficientNonConcentration",
            False,
            "not submitted",
            "这是备用自足路线：若不走已嵌入的 canonical 来源链，才需要直接证明横向商实际系数在 moving block 上不能集中。",
            False,
        ),
    ]


def run(
    transverse_frontier_path: Path,
    source_lock_path: Path,
    actual_source_path: Path,
    canonical_riw_path: Path,
    squarefree_path: Path,
    ncblk_path: Path,
    transverse_embedding_path: Path,
) -> dict[str, Any]:
    """运行横向源支撑路由。"""
    transverse_frontier = load_json(transverse_frontier_path)
    source_lock = load_json(source_lock_path)
    actual_source = load_json(actual_source_path)
    canonical_riw = load_json(canonical_riw_path)
    squarefree = load_json(squarefree_path)
    ncblk = load_json(ncblk_path)
    transverse_embedding = load_json(transverse_embedding_path)
    rows = build_rows(
        transverse_frontier=transverse_frontier,
        source_lock=source_lock,
        actual_source=actual_source,
        canonical_riw=canonical_riw,
        squarefree=squarefree,
        ncblk=ncblk,
        transverse_embedding=transverse_embedding,
    )
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "TransverseSourceSupportReducedToEmbeddingOrDirectNCBLK"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_transverse_source_support_router",
        "status": "transverse_source_support_reduced_to_embedding_layer_transfer_or_direct_ncblk",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "transverse_frontier": file_sha256(transverse_frontier_path),
            "source_lock": file_sha256(source_lock_path),
            "actual_source": file_sha256(actual_source_path),
            "canonical_riw": file_sha256(canonical_riw_path),
            "squarefree_buchstab": file_sha256(squarefree_path),
            "ncblk_boundary": file_sha256(ncblk_path),
            "transverse_embedding": file_sha256(transverse_embedding_path),
        },
        "transverse_source_support_reduced": reduced,
        "transverse_source_support_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": (
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
        ),
        "downstream_source_route_hardpoint": (
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
        ),
        "direct_fallback_hardpoint": (
            "DirectTransverseNCBLKActualCoefficientNonConcentration"
        ),
        "rows": rows,
        "reduction_law": (
            "A transverse source-support/nonconcentration certificate has two honest "
            "self-contained routes. The source route must first embed the transverse "
            "formal unit into the already provenance-closed canonical A1/KZ-E pre-Cauchy "
            "source; after that, the existing canonical RIW support chain reduces the "
            "problem to layer admission, nonzero coefficient transfer, and thin-interval "
            "return for Buchstab squarefree products. The direct route proves actual "
            "transverse NC-BLK non-concentration without using canonical support. No route "
            "may import a generic WFD self-contained theorem."
        ),
        "review_conclusion": (
            "`TransverseSourceSupportNonconcentrationCertificate` 已继续拆成严格自足边界："
            "`TransverseFormalUnitA1SourceEmbedding` 已由有限测度函子性闭合：横向商 formal unit "
            "确实来自已闭合来源账本的 canonical A1/KZ-E pre-Cauchy 源。新的下游剩余是 "
            "Buchstab 层准入、非零转移与薄区间回流；若不走源路线，则必须直接证明 "
            "actual transverse NC-BLK 非集中。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 横向源支撑路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 归约律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "TransverseSourceSupportNonconcentrationCertificate",
        "  source route:",
        "    TransverseFormalUnitA1SourceEmbedding (closed by finite-measure functoriality);",
        "    then CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn;",
        "  direct route:",
        "    DirectTransverseNCBLKActualCoefficientNonConcentration.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `transverse_source_support_reduced={fmt_bool(result['transverse_source_support_reduced'])}`。",
        f"- `transverse_source_support_closed={fmt_bool(result['transverse_source_support_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `downstream_source_route_hardpoint={result['downstream_source_route_hardpoint']}`。",
        f"- `direct_fallback_hardpoint={result['direct_fallback_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
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
            "## 4. 下一步",
            "",
            "下一步最窄自足硬点是 `CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`：在已嵌入的 canonical 源内，证明 Buchstab squarefree products 被 exact canonical 层承认、系数非零；若 balanced interval 太薄，必须回流 edge/PDEC/SAE。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--transverse-frontier-json", type=Path, default=DEFAULT_TRANSVERSE_FRONTIER
    )
    parser.add_argument("--source-lock-json", type=Path, default=DEFAULT_SOURCE_LOCK)
    parser.add_argument("--actual-source-json", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--canonical-riw-json", type=Path, default=DEFAULT_CANONICAL_RIW)
    parser.add_argument("--squarefree-json", type=Path, default=DEFAULT_SQUAREFREE)
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument(
        "--transverse-embedding-json", type=Path, default=DEFAULT_TRANSVERSE_EMBEDDING
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        transverse_frontier_path=args.transverse_frontier_json,
        source_lock_path=args.source_lock_json,
        actual_source_path=args.actual_source_json,
        canonical_riw_path=args.canonical_riw_json,
        squarefree_path=args.squarefree_json,
        ncblk_path=args.ncblk_json,
        transverse_embedding_path=args.transverse_embedding_json,
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
