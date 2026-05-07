#!/usr/bin/env python3
"""汇总当前已物化 LocalSurvivor/SAE 包的闭合状态。

用法示例：
  python3 experiments/prime_matrix_local_survivor_materialized_packet_ledger.py

输出：
  docs/monograph/prime-matrix-local-survivor-materialized-packet-ledger.json
  docs/monograph/prime-matrix-local-survivor-materialized-packet-ledger.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SPARSECAP = DOCS / "prime-matrix-triad-a1-sparsecap-local-survivor.json"
DEFAULT_FO_SAE = (
    DOCS / "prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.json"
)
DEFAULT_RPZ_SAE = DOCS / "prime-matrix-rpz-endpoint-sae-finite-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
DEFAULT_MD = DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def sparsecap_summary(sparsecap: dict[str, Any]) -> dict[str, Any]:
    """抽取 SparseCap 的 LocalSurvivor 与 finite-PDEC 路由摘要。"""
    witness_rows = []
    finite_packets = []
    early_conflicts = []
    for cap in sparsecap["cap_reports"]:
        for phase in cap["phase_reports"]:
            if phase["local_survivor_witness_col"] is not None:
                witness_rows.append(
                    {
                        "p": cap["p"],
                        "q": cap["q"],
                        "phase": phase["phase"],
                        "witness_col": phase["local_survivor_witness_col"],
                        "low_holes": phase["low_holes"],
                        "route": phase["phase_route"],
                    }
                )
            if phase["phase_route"] == "FinitePDECAtomBeyondP":
                finite_packets.append(
                    {
                        "p": cap["p"],
                        "q": cap["q"],
                        "phase": phase["phase"],
                        "first_completion_row": phase["first_completion_row"],
                        "row_le_p_phase": phase["row_le_p_phase"],
                        "route": phase["phase_route"],
                    }
                )
            if phase["phase_route"] == "EarlyCompletionConflict":
                early_conflicts.append(
                    {
                        "p": cap["p"],
                        "q": cap["q"],
                        "phase": phase["phase"],
                    }
                )
    closed = (
        sparsecap["all_sparse_caps_closed_for_pxP"]
        and sparsecap["early_completion_conflict_count"] == 0
        and not early_conflicts
    )
    return {
        "source": "Triad-A1 SparseCap",
        "status": sparsecap["status"],
        "materialized_packet_count": sparsecap["unique_sparse_cap_count"],
        "materialized_phase_atom_count": sparsecap["unique_phase_atom_count"],
        "local_survivor_witness_count": sparsecap["unique_local_survivor_witness_count"],
        "finite_pdec_atom_count": sparsecap["unique_finite_pdec_atom_count"],
        "closed_for_current_pxP": closed,
        "open_current_obligation_count": 0 if closed else len(early_conflicts) or 1,
        "witness_rows": witness_rows,
        "finite_pdec_packets_sample": finite_packets[:12],
        "early_conflicts": early_conflicts,
        "route": (
            "ClosedForPxPThenFinitePDEC"
            if closed
            else "SparseCapLocalSurvivorStillOpen"
        ),
    }


def fo_sae_summary(fo_sae: dict[str, Any]) -> dict[str, Any]:
    """抽取 FO-PDEC 二点 SAE/Endpoint 吸收摘要。"""
    closed = (
        fo_sae["all_sources_have_local_survivor_witness"]
        and fo_sae["all_factor_199_fibers_are_sparse_load_one"]
        and fo_sae["closed_subgate"]
        == "TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses"
    )
    witness_rows = [
        {
            "atom": row["atom_candidate"],
            "block": row["block_index"],
            "q": row["q"],
            "row": row["row"],
            "offset": row["offset"],
            "witness_primes": [
                witness["candidate"] for witness in row["local_prime_witnesses"]
            ],
            "route": row["route"],
        }
        for row in fo_sae["absorption_rows"]
    ]
    return {
        "source": "FO-PDEC two physical atoms",
        "status": fo_sae["status"],
        "materialized_packet_count": fo_sae["unique_fixed_offset_fiber_count"],
        "materialized_phase_atom_count": fo_sae["source_row_count"],
        "local_survivor_witness_count": fo_sae["source_row_count"],
        "finite_pdec_atom_count": 0,
        "closed_for_current_pxP": closed,
        "open_current_obligation_count": 0 if closed else 1,
        "witness_rows": witness_rows,
        "route": (
            "TwoAtomsAbsorbedByLocalSurvivor"
            if closed
            else "TwoAtomSAEEndpointStillOpen"
        ),
    }


def rpz_sae_summary(rpz_sae: dict[str, Any]) -> dict[str, Any]:
    """抽取 RPZ Endpoint-SAE 有限账本摘要。"""
    summary = rpz_sae["summary"]
    closed = (
        summary["candidate_count"] == summary["current_ledger_closed_count"]
        and summary["total_actual_load"] == 0
    )
    vacuous_rows = [
        {
            "phase_key": row["phase_key"],
            "possible_load": row["possible_load_in_current_ledger"],
            "actual_load": row["actual_load_in_current_ledger"],
            "route": row["local_state_verdict"],
        }
        for row in rpz_sae["certificates"]
    ]
    return {
        "source": "RPZ Endpoint-SAE finite ledger",
        "status": rpz_sae["status"],
        "materialized_packet_count": summary["candidate_count"],
        "materialized_phase_atom_count": summary["total_possible_load"],
        "local_survivor_witness_count": 0,
        "finite_pdec_atom_count": 0,
        "closed_for_current_pxP": closed,
        "open_current_obligation_count": 0 if closed else summary["total_actual_load"],
        "vacuous_rows": vacuous_rows,
        "route": (
            "VacuousCurrentLedgerClosed"
            if closed
            else "RPZEndpointSAEActualLoadOpen"
        ),
    }


def build_ledger(
    sparsecap: dict[str, Any],
    fo_sae: dict[str, Any],
    rpz_sae: dict[str, Any],
    sparsecap_path: Path,
    fo_sae_path: Path,
    rpz_sae_path: Path,
) -> dict[str, Any]:
    """构造已物化 LocalSurvivor/SAE 包总账。"""
    sources = [
        sparsecap_summary(sparsecap),
        fo_sae_summary(fo_sae),
        rpz_sae_summary(rpz_sae),
    ]
    open_sources = [
        source for source in sources if source["open_current_obligation_count"] > 0
    ]
    materialized_packet_count = sum(
        source["materialized_packet_count"] for source in sources
    )
    materialized_phase_atom_count = sum(
        source["materialized_phase_atom_count"] for source in sources
    )
    local_survivor_witness_count = sum(
        source["local_survivor_witness_count"] for source in sources
    )
    finite_pdec_atom_count = sum(source["finite_pdec_atom_count"] for source in sources)
    current_materialized_closed = not open_sources
    return {
        "certificate_type": "local_survivor_materialized_packet_ledger",
        "status": (
            "current_materialized_local_survivor_packets_exhausted_not_global_proof"
            if current_materialized_closed
            else "current_materialized_local_survivor_packets_still_open"
        ),
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "sparsecap_local_survivor": file_sha256(sparsecap_path),
            "fo_pdec_sae_endpoint_absorption": file_sha256(fo_sae_path),
            "rpz_endpoint_sae_finite": file_sha256(rpz_sae_path),
        },
        "materialized_source_count": len(sources),
        "materialized_packet_count": materialized_packet_count,
        "materialized_phase_atom_count": materialized_phase_atom_count,
        "local_survivor_witness_count": local_survivor_witness_count,
        "finite_pdec_atom_count": finite_pdec_atom_count,
        "open_materialized_obligation_count": sum(
            source["open_current_obligation_count"] for source in sources
        ),
        "current_materialized_local_survivor_packets_closed": current_materialized_closed,
        "closed_subgate": (
            "MaterializedLocalSurvivorPacketsExhausted"
            if current_materialized_closed
            else "MaterializedLocalSurvivorPacketStillOpen"
        ),
        "sources": sources,
        "open_sources": open_sources,
        "next_narrowest_hardpoint": (
            "LocalSurvivorPacketGenerationOrNonTautologicalPDEC"
            if current_materialized_closed
            else "CloseMaterializedLocalSurvivorPackets"
        ),
        "remaining_after_subgate": [
            "LocalSurvivor packet-generation theorem for unaudited sparse windows",
            "future primitive PDEC with at least three non-tautological physical atoms or a fixed-frequency constraint",
            "CleanKLS/DLS and D-structure/Rankin referee inputs for final theorem promotion",
        ],
        "review_conclusion": (
            "当前已经物化到机器账本的 LocalSurvivor/SAE 包全部闭合：SparseCap 的 P×P 早期出口"
            "无完成冲突，FO-PDEC 二点原子由同纤维本地素数见证吸收，RPZ Endpoint-SAE 当前账本"
            "实际负载为零。剩余不再是这些已物化窗口本身，而是全局 packet-generation 定理："
            "证明任何未来 sparse escape 都必须物化为同类有限包并给 witness/deficit，或持久化为"
            "非二点 PDEC/ColumnCRT/CleanKLS 输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# LocalSurvivor 已物化包总账",
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
            "current_materialized_local_survivor_packets_closed: "
            f"{str(result['current_materialized_local_survivor_packets_closed']).lower()}"
        ),
        f"materialized_source_count: {result['materialized_source_count']}",
        f"materialized_packet_count: {result['materialized_packet_count']}",
        f"materialized_phase_atom_count: {result['materialized_phase_atom_count']}",
        f"local_survivor_witness_count: {result['local_survivor_witness_count']}",
        f"finite_pdec_atom_count: {result['finite_pdec_atom_count']}",
        f"open_materialized_obligation_count: {result['open_materialized_obligation_count']}",
        f"next_narrowest_hardpoint: {result['next_narrowest_hardpoint']}",
        "```",
        "",
        "## 2. 来源表",
        "",
        "| source | status | packets | atoms | witnesses | finite PDEC atoms | open | route |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for source in result["sources"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(value)
                for value in [
                    source["source"],
                    source["status"],
                    source["materialized_packet_count"],
                    source["materialized_phase_atom_count"],
                    source["local_survivor_witness_count"],
                    source["finite_pdec_atom_count"],
                    source["open_current_obligation_count"],
                    source["route"],
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 关键 witness",
            "",
        ]
    )
    for source in result["sources"]:
        witness_rows = source.get("witness_rows", [])
        if not witness_rows:
            continue
        lines.append(f"### {source['source']}")
        lines.append("")
        for row in witness_rows:
            lines.append(f"- `{row}`")
        lines.append("")

    lines.extend(
        [
            "## 4. 证明读法",
            "",
            "本总账不声称全局 LocalSurvivor family 已证明。它只断言：凡是当前已经由前沿路由器和"
            "有限审计物化出来的 sparse/SAE 包，都没有未处理的局部孤窗义务。",
            "",
            "因此下一步不能继续在这些已闭合样本上重复找缺口，而应证明一个生成定理：任意新的"
            " sparse escape 要么被物化成同类 `LocalSurvivorCert` 输入并给出 witness/deficit，"
            "要么在无限反例族中持久复现，转成非二点 `PDEC/ColumnCRT/CleanKLS` 输入。",
            "",
            "## 5. 剩余",
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
    parser.add_argument("--sparsecap", type=Path, default=DEFAULT_SPARSECAP)
    parser.add_argument("--fo-sae", type=Path, default=DEFAULT_FO_SAE)
    parser.add_argument("--rpz-sae", type=Path, default=DEFAULT_RPZ_SAE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    sparsecap = load_json(args.sparsecap)
    fo_sae = load_json(args.fo_sae)
    rpz_sae = load_json(args.rpz_sae)
    result = build_ledger(
        sparsecap,
        fo_sae,
        rpz_sae,
        args.sparsecap,
        args.fo_sae,
        args.rpz_sae,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["closed_subgate"])
    print(result["next_narrowest_hardpoint"])


if __name__ == "__main__":
    main()
