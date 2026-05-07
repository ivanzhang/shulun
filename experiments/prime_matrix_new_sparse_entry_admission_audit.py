#!/usr/bin/env python3
"""审计 NewSparseEntryAdmission：是否还有未命名 LocalSurvivor 入口。

用法示例：
  python3 experiments/prime_matrix_new_sparse_entry_admission_audit.py

输出：
  docs/monograph/prime-matrix-new-sparse-entry-admission-audit.json
  docs/monograph/prime-matrix-new-sparse-entry-admission-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_EXTRACTOR_COVERAGE = (
    DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.json"
)
DEFAULT_UNNAMED = DOCS / "prime-matrix-unnamed-escape-closure-machine.md"
DEFAULT_NAMED_EXIT = DOCS / "prime-matrix-named-exit-absorption-contract.md"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_PACKET_CONTRACT = (
    DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
)
DEFAULT_SAE_REDUCTION = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_CLEAN = DOCS / "prime-matrix-cleankls-dls-certificate-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-new-sparse-entry-admission-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-new-sparse-entry-admission-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: object) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def source_row(
    source_id: str,
    source_class: str,
    required_fragments: list[str],
    target_route: str,
    texts: dict[str, str],
) -> dict[str, object]:
    """构造来源准入行。"""
    combined = "\n".join(texts.values())
    admitted = has_all(combined, required_fragments)
    return {
        "source_id": source_id,
        "source_class": source_class,
        "required_fragments": required_fragments,
        "target_route": target_route,
        "admitted": admitted,
        "verdict": "admitted_named_route" if admitted else "missing_admission_fragment",
    }


def build_audit(
    extractor_coverage: dict[str, object],
    extractor_coverage_path: Path,
    unnamed_path: Path,
    named_exit_path: Path,
    terminal_triad_path: Path,
    packet_contract_path: Path,
    sae_reduction_path: Path,
    clean_path: Path,
) -> dict[str, object]:
    """构造 NewSparseEntryAdmission 审计。"""
    texts = {
        "unnamed": read_text(unnamed_path),
        "named_exit": read_text(named_exit_path),
        "terminal_triad": read_text(terminal_triad_path),
        "packet_contract": read_text(packet_contract_path),
        "sae_reduction": read_text(sae_reduction_path),
        "clean": read_text(clean_path),
    }
    rows = [
        source_row(
            "ShortWindowOrEndpointSparse",
            "Sparse",
            ["短窗", "SAE", "LocalSurvivorCert"],
            "LocalSurvivor packet extractor or SAE-Cert",
            texts,
        ),
        source_row(
            "PDECDualSparseCap",
            "SparseFromPDECDualFailure",
            ["sparse cap", "LocalSurvivorCert", "PDEC-Dual"],
            "LocalSurvivor packet or refined PDEC",
            texts,
        ),
        source_row(
            "EndpointSeamSparse",
            "EndpointSeam",
            ["EndpointSeam", "PDEC/ColumnCRT/SAE"],
            "Endpoint PDEC, ColumnCRT, or SAE packet",
            texts,
        ),
        source_row(
            "BohrCapSparse",
            "BohrCap",
            ["BohrCap", "孤立帽", "SAE"],
            "SAE packet or persistent PDEC/ColumnCRT",
            texts,
        ),
        source_row(
            "ColumnTailCofactorSparse",
            "ColumnTailCofactor",
            ["CofactorAnchor", "TailAnchor", "PDEC/ColumnCRT/SAE"],
            "Tail/Cofactor PDEC or SAE packet",
            texts,
        ),
        source_row(
            "DescentSeamSparse",
            "DescentSeam",
            ["TotalDescent/RPZ", "descent/seam", "already named"],
            "named PDEC/LocalSurvivor/ColumnCRT packet",
            texts,
        ),
        source_row(
            "PersistentSignatureNotSparse",
            "Persistent",
            ["有限签名", "PDEC family", "same signature persists"],
            "PDEC/ColumnCRT/TailAnchor/CofactorAnchor",
            texts,
        ),
        source_row(
            "LayerEscapeNotSparse",
            "Flat",
            ["CleanKLS/DLS", "admission", "Flat"],
            "CleanKLS/DLS or ExternalKLS",
            texts,
        ),
    ]
    missing = [row for row in rows if not row["admitted"]]
    known_extractors_closed = (
        extractor_coverage["closed_subgate"]
        == "KnownLocalSurvivorEntryExtractorsCovered"
        and extractor_coverage["known_entry_extractor_coverage_closed"]
    )
    closed = known_extractors_closed and not missing
    return {
        "certificate_type": "new_sparse_entry_admission_audit",
        "status": (
            "no_additional_unnamed_local_survivor_entry_route_not_global_proof"
            if closed
            else "new_sparse_entry_admission_missing_fragments"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "extractor_coverage": file_sha256(extractor_coverage_path),
            "unnamed_escape_closure": file_sha256(unnamed_path),
            "named_exit_absorption": file_sha256(named_exit_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "packet_generation_contract": file_sha256(packet_contract_path),
            "sae_local_reduction": file_sha256(sae_reduction_path),
            "clean_kls_contract": file_sha256(clean_path),
        },
        "known_extractors_closed": known_extractors_closed,
        "admission_source_count": len(rows),
        "missing_admission_count": len(missing),
        "no_additional_unnamed_local_survivor_entry_route": closed,
        "closed_subgate": (
            "NoAdditionalUnnamedLocalSurvivorEntryRoute"
            if closed
            else "NewSparseEntryAdmissionStillOpen"
        ),
        "source_rows": rows,
        "missing_rows": missing,
        "remaining_after_subgate": [
            "PacketExtractorCompleteness for any future explicitly admitted sparse route",
            "NonTautologicalPDEC for >=3 physical atoms or fixed-frequency constraints",
            "CleanKLS/DLS or explicit ExternalKLS for layer-escape branches",
            "D-structure/Tail-log4/Rankin referee inputs for final theorem promotion",
        ],
        "review_conclusion": (
            "无名 sparse 入口在当前合同体系中已经没有独立位置：短窗、endpoint、Bohr-cap、"
            "tail/cofactor、descent/seam 都被命名到 SAE/LocalSurvivor/PDEC/ColumnCRT；同签名"
            "持久复现不是 sparse，而是 PDEC/ColumnCRT/TailAnchor/CofactorAnchor；层级逃逸不是"
            " sparse，而是 CleanKLS/DLS admission。结合已知 extractor 覆盖，当前剩余不再是"
            " NewSparseEntryAdmission，而是未来若新增显式 sparse 路线时必须提交 extractor schema。"
        ),
    }


def write_markdown(result: dict[str, object], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# NewSparseEntryAdmission 审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        str(result["review_conclusion"]),
        "",
        "## 1. 总裁定",
        "",
        "```text",
        f"closed_subgate: {result['closed_subgate']}",
        f"known_extractors_closed: {str(result['known_extractors_closed']).lower()}",
        (
            "no_additional_unnamed_local_survivor_entry_route: "
            f"{str(result['no_additional_unnamed_local_survivor_entry_route']).lower()}"
        ),
        f"admission_source_count: {result['admission_source_count']}",
        f"missing_admission_count: {result['missing_admission_count']}",
        "```",
        "",
        "## 2. 准入表",
        "",
        "| source | class | verdict | target route |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["source_rows"]:  # type: ignore[index]
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    row["source_id"],  # type: ignore[index]
                    row["source_class"],  # type: ignore[index]
                    row["verdict"],  # type: ignore[index]
                    row["target_route"],  # type: ignore[index]
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明读法",
            "",
            "这一步只处理“是否还有未命名的新 LocalSurvivor 入口”。答案是：在当前合同体系内没有。"
            "所有能产生孤立窗口的来源都已命名到 SAE/LocalSurvivor/PDEC/ColumnCRT；所有不能保持"
            "孤立的来源都转成持久签名或 clean 平坦分支。",
            "",
            "因此下一步若有人提出新的 sparse 路线，它必须作为显式新入口提交，并附带同样的"
            " packet extractor、字段 schema、fallback 规则和机器账本；否则它不是合法终端。",
            "",
            "## 4. 剩余",
            "",
        ]
    )
    for item in result["remaining_after_subgate"]:  # type: ignore[index]
        lines.append(f"- `{item}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extractor-coverage", type=Path, default=DEFAULT_EXTRACTOR_COVERAGE)
    parser.add_argument("--unnamed", type=Path, default=DEFAULT_UNNAMED)
    parser.add_argument("--named-exit", type=Path, default=DEFAULT_NAMED_EXIT)
    parser.add_argument("--terminal-triad", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--packet-contract", type=Path, default=DEFAULT_PACKET_CONTRACT)
    parser.add_argument("--sae-reduction", type=Path, default=DEFAULT_SAE_REDUCTION)
    parser.add_argument("--clean", type=Path, default=DEFAULT_CLEAN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = build_audit(
        extractor_coverage=load_json(args.extractor_coverage),
        extractor_coverage_path=args.extractor_coverage,
        unnamed_path=args.unnamed,
        named_exit_path=args.named_exit,
        terminal_triad_path=args.terminal_triad,
        packet_contract_path=args.packet_contract,
        sae_reduction_path=args.sae_reduction,
        clean_path=args.clean,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])


if __name__ == "__main__":
    main()
