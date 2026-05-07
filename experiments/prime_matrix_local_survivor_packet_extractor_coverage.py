#!/usr/bin/env python3
"""审计 LocalSurvivor packet-generation 的已知入口 extractor 覆盖。

用法示例：
  python3 experiments/prime_matrix_local_survivor_packet_extractor_coverage.py

输出：
  docs/monograph/prime-matrix-local-survivor-packet-extractor-coverage.json
  docs/monograph/prime-matrix-local-survivor-packet-extractor-coverage.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
EXPERIMENTS = ROOT / "experiments"

DEFAULT_MATERIALIZED_LEDGER = (
    DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
)
DEFAULT_SPARSECAP = DOCS / "prime-matrix-triad-a1-sparsecap-local-survivor.json"
DEFAULT_FO_SAE = (
    DOCS / "prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.json"
)
DEFAULT_RPZ_SAE = DOCS / "prime-matrix-rpz-endpoint-sae-finite-certificate.json"
DEFAULT_PACKET_CONTRACT = (
    DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
)
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_SAE_REDUCTION = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_JSON = DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.json"
DEFAULT_MD = DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.md"

SPARSECAP_SCRIPT = EXPERIMENTS / "prime_matrix_triad_a1_sparsecap_local_survivor_audit.py"
FO_SAE_SCRIPT = (
    EXPERIMENTS / "prime_matrix_wsh_fo_pdec_sae_endpoint_absorption_audit.py"
)
RPZ_SAE_SCRIPT = EXPERIMENTS / "prime_matrix_rpz_endpoint_sae_finite_certificate.py"
MATERIALIZED_LEDGER_SCRIPT = (
    EXPERIMENTS / "prime_matrix_local_survivor_materialized_packet_ledger.py"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def script_entry(
    entry_id: str,
    entry_route: str,
    script_path: Path,
    ledger_path: Path,
    closed: bool,
    packet_fields: list[str],
    route_if_not_packet: str,
) -> dict[str, Any]:
    """构造机器 extractor 入口行。"""
    return {
        "entry_id": entry_id,
        "entry_type": "materialized_script_extractor",
        "entry_route": entry_route,
        "script": str(script_path.relative_to(ROOT)),
        "ledger": str(ledger_path.relative_to(ROOT)),
        "script_exists": script_path.exists(),
        "ledger_exists": ledger_path.exists(),
        "closed_for_current_materialized_input": closed,
        "packet_fields": packet_fields,
        "route_if_not_packet": route_if_not_packet,
        "coverage_status": (
            "covered_closed"
            if script_path.exists() and ledger_path.exists() and closed
            else "missing_or_open"
        ),
    }


def contract_entry(
    entry_id: str,
    entry_route: str,
    contract_paths: list[Path],
    required_phrases: list[str],
    route_if_not_packet: str,
) -> dict[str, Any]:
    """构造合同型入口行。"""
    texts = [read_text(path) for path in contract_paths]
    combined = "\n".join(texts)
    contract_present = all(path.exists() for path in contract_paths) and has_all(
        combined, required_phrases
    )
    return {
        "entry_id": entry_id,
        "entry_type": "contract_route_not_materialized_packet",
        "entry_route": entry_route,
        "contracts": [str(path.relative_to(ROOT)) for path in contract_paths],
        "contract_present": contract_present,
        "required_phrases": required_phrases,
        "route_if_not_packet": route_if_not_packet,
        "coverage_status": (
            "covered_by_contract_route" if contract_present else "contract_missing"
        ),
    }


def build_coverage(
    materialized: dict[str, Any],
    sparsecap: dict[str, Any],
    fo_sae: dict[str, Any],
    rpz_sae: dict[str, Any],
    materialized_path: Path,
    sparsecap_path: Path,
    fo_sae_path: Path,
    rpz_sae_path: Path,
    packet_contract_path: Path,
    terminal_triad_path: Path,
    sae_reduction_path: Path,
) -> dict[str, Any]:
    """构造 LocalSurvivor 已知入口覆盖审计。"""
    entries: list[dict[str, Any]] = [
        script_entry(
            entry_id="TriadA1SparseCapExtractor",
            entry_route="DualCap SparseCap -> LocalSurvivor or finite PDEC",
            script_path=SPARSECAP_SCRIPT,
            ledger_path=sparsecap_path,
            closed=(
                sparsecap["all_sparse_caps_closed_for_pxP"]
                and sparsecap["early_completion_conflict_count"] == 0
            ),
            packet_fields=[
                "phase",
                "low_holes",
                "completion_rows",
                "local_survivor_witness_col",
                "finite_pdec_packet",
            ],
            route_if_not_packet="FinitePDECAtomBeyondP or LocalSurvivorWitnessAtRowLeP",
        ),
        script_entry(
            entry_id="FOPDECTwoAtomSAEEndpointExtractor",
            entry_route="physical two-point PDEC tautology -> SAE/Endpoint",
            script_path=FO_SAE_SCRIPT,
            ledger_path=fo_sae_path,
            closed=(
                fo_sae["closed_subgate"]
                == "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses"
                and fo_sae["all_sources_have_local_survivor_witness"]
            ),
            packet_fields=[
                "fixed_offset_fiber",
                "atom_candidate",
                "local_prime_witnesses",
                "factor_load",
            ],
            route_if_not_packet="PDEC if persistent, LocalSurvivor witness if sparse",
        ),
        script_entry(
            entry_id="RPZEndpointSAEFiniteExtractor",
            entry_route="RPZ endpoint low-load candidate -> SAE finite ledger",
            script_path=RPZ_SAE_SCRIPT,
            ledger_path=rpz_sae_path,
            closed=(
                rpz_sae["summary"]["total_actual_load"] == 0
                and rpz_sae["summary"]["candidate_count"]
                == rpz_sae["summary"]["current_ledger_closed_count"]
            ),
            packet_fields=[
                "phase_key",
                "possible_load",
                "actual_load",
                "candidate_windows",
            ],
            route_if_not_packet="Endpoint PDEC or ColumnCRT if global load appears",
        ),
        script_entry(
            entry_id="MaterializedPacketLedgerAggregator",
            entry_route="known materialized packets -> combined LocalSurvivor ledger",
            script_path=MATERIALIZED_LEDGER_SCRIPT,
            ledger_path=materialized_path,
            closed=(
                materialized["closed_subgate"]
                == "MaterializedLocalSurvivorPacketsExhausted"
                and materialized["open_materialized_obligation_count"] == 0
            ),
            packet_fields=[
                "materialized_packet_count",
                "local_survivor_witness_count",
                "open_materialized_obligation_count",
            ],
            route_if_not_packet="Close materialized packet before global generation",
        ),
        contract_entry(
            entry_id="GenericSAELocalWindowContract",
            entry_route="generic sparse/single-window escape",
            contract_paths=[packet_contract_path, sae_reduction_path],
            required_phrases=[
                "LocalSurvivorCert",
                "same signature persists",
                "PDEC family",
            ],
            route_if_not_packet="packet extractor, persistent PDEC, smaller SAE, or CleanKLS/DLS",
        ),
        contract_entry(
            entry_id="PersistentSignatureFallbackContract",
            entry_route="same finite signature repeats in an infinite family",
            contract_paths=[packet_contract_path, terminal_triad_path],
            required_phrases=[
                "有限签名",
                "PDEC family",
                "无第四出口",
            ],
            route_if_not_packet="PDEC/ColumnCRT/TailAnchor/CofactorAnchor",
        ),
        contract_entry(
            entry_id="LayerEscapeCleanKLSContract",
            entry_route="signature layer escapes every finite packet",
            contract_paths=[packet_contract_path, terminal_triad_path],
            required_phrases=[
                "CleanKLS/DLS",
                "admission",
                "Flat",
            ],
            route_if_not_packet="CleanKLS/DLS or explicit ExternalKLS",
        ),
        contract_entry(
            entry_id="DescentSeamReturnContract",
            entry_route="descent/seam route lowers to named packet",
            contract_paths=[packet_contract_path, terminal_triad_path],
            required_phrases=[
                "descent/seam",
                "already named PDEC/LocalSurvivor/ColumnCRT packet",
                "TotalDescent/RPZ",
            ],
            route_if_not_packet="PDEC/LocalSurvivor/ColumnCRT packet after descent",
        ),
    ]
    missing_or_open = [
        entry
        for entry in entries
        if entry["coverage_status"] in {"missing_or_open", "contract_missing"}
    ]
    materialized_script_entries = [
        entry for entry in entries if entry["entry_type"] == "materialized_script_extractor"
    ]
    contract_entries = [
        entry for entry in entries if entry["entry_type"] == "contract_route_not_materialized_packet"
    ]
    closed = not missing_or_open
    return {
        "certificate_type": "local_survivor_packet_extractor_coverage",
        "status": (
            "known_local_survivor_entry_extractors_covered_not_global_proof"
            if closed
            else "known_local_survivor_entry_extractors_missing_or_open"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "materialized_packet_ledger": file_sha256(materialized_path),
            "sparsecap_ledger": file_sha256(sparsecap_path),
            "fo_sae_endpoint_ledger": file_sha256(fo_sae_path),
            "rpz_endpoint_sae_ledger": file_sha256(rpz_sae_path),
            "packet_generation_contract": file_sha256(packet_contract_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "sae_local_reduction": file_sha256(sae_reduction_path),
        },
        "entry_count": len(entries),
        "materialized_script_entry_count": len(materialized_script_entries),
        "contract_entry_count": len(contract_entries),
        "missing_or_open_count": len(missing_or_open),
        "known_entry_extractor_coverage_closed": closed,
        "closed_subgate": (
            "KnownLocalSurvivorEntryExtractorsCovered"
            if closed
            else "KnownLocalSurvivorEntryExtractorMissing"
        ),
        "entries": entries,
        "missing_or_open_entries": missing_or_open,
        "remaining_after_subgate": [
            "NewSparseEntryAdmission: prove no additional unnamed LocalSurvivor entry route exists",
            "PacketExtractorCompleteness for any newly admitted sparse route",
            "NonTautologicalPDEC for >=3 physical atoms or fixed-frequency constraints",
            "CleanKLS/DLS or explicit ExternalKLS for layer-escape branches",
        ],
        "review_conclusion": (
            "当前所有已知 LocalSurvivor packet 入口均有覆盖：三个机器 extractor 分别处理 "
            "Triad-A1 SparseCap、FO-PDEC 二点 SAE/Endpoint、RPZ Endpoint-SAE，聚合总账已清零"
            "物化义务；generic SAE、持久签名、升层 clean 和 descent/seam 入口均有合同回流到"
            " PDEC/ColumnCRT/LocalSurvivor/CleanKLS。该子门只关闭已知入口覆盖，不证明未来不会"
            "出现新 sparse 入口；剩余是 NewSparseEntryAdmission。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# LocalSurvivor packet extractor 覆盖审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 总裁定",
        "",
        "```text",
        f"closed_subgate: {result['closed_subgate']}",
        (
            "known_entry_extractor_coverage_closed: "
            f"{str(result['known_entry_extractor_coverage_closed']).lower()}"
        ),
        f"entry_count: {result['entry_count']}",
        f"materialized_script_entry_count: {result['materialized_script_entry_count']}",
        f"contract_entry_count: {result['contract_entry_count']}",
        f"missing_or_open_count: {result['missing_or_open_count']}",
        "```",
        "",
        "## 2. 覆盖表",
        "",
        "| entry | type | route | coverage | fallback |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in result["entries"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    entry["entry_id"],
                    entry["entry_type"],
                    entry["entry_route"],
                    entry["coverage_status"],
                    entry["route_if_not_packet"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明读法",
            "",
            "这一步把 `packet-generation` 的已知入口从口头列表变成可审计覆盖表。"
            "凡是已经物化到机器账本的入口，都必须有脚本、JSON 账本和当前闭合状态；"
            "凡是尚未物化为具体窗口的入口，必须有合同把失败回流到 PDEC、ColumnCRT、"
            "LocalSurvivor 或 CleanKLS/DLS。",
            "",
            "因此当前不能再把已知入口本身当作开放缺口。真正剩余是：证明不存在新的未命名"
            " sparse 入口；或者若新入口出现，必须给出同样的 extractor 和有限 packet schema。",
            "",
            "## 4. 剩余",
            "",
        ]
    )
    for item in result["remaining_after_subgate"]:
        lines.append(f"- `{item}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--materialized", type=Path, default=DEFAULT_MATERIALIZED_LEDGER)
    parser.add_argument("--sparsecap", type=Path, default=DEFAULT_SPARSECAP)
    parser.add_argument("--fo-sae", type=Path, default=DEFAULT_FO_SAE)
    parser.add_argument("--rpz-sae", type=Path, default=DEFAULT_RPZ_SAE)
    parser.add_argument("--packet-contract", type=Path, default=DEFAULT_PACKET_CONTRACT)
    parser.add_argument("--terminal-triad", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--sae-reduction", type=Path, default=DEFAULT_SAE_REDUCTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = build_coverage(
        materialized=load_json(args.materialized),
        sparsecap=load_json(args.sparsecap),
        fo_sae=load_json(args.fo_sae),
        rpz_sae=load_json(args.rpz_sae),
        materialized_path=args.materialized,
        sparsecap_path=args.sparsecap,
        fo_sae_path=args.fo_sae,
        rpz_sae_path=args.rpz_sae,
        packet_contract_path=args.packet_contract,
        terminal_triad_path=args.terminal_triad,
        sae_reduction_path=args.sae_reduction,
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
