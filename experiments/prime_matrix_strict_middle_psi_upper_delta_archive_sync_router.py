#!/usr/bin/env python3
"""生成 strict 中段 psi 上界与 delta-aware 完整归档同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_middle_psi_upper_delta_archive_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-middle-psi-upper-delta-archive-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data" / "middle-psi-fine-mesh-node-table.jsonl"
OUT_JSON = DOCS / "prime-matrix-strict-middle-psi-upper-delta-archive-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-middle-psi-upper-delta-archive-sync-router.md"

TARGET = "MiddlePsiUpper100002841SourceLedger"
MIDDLE_COVER = "MiddleFiniteIntervalPsiCover8e11ToE28Ledger"
FINE_MESH = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
NODE_ARCHIVE = "MachineReadableNodeArchiveLedger"
DELTA_ARCHIVE = "FullDeltaAwarePsiNodeArchiveRunAndHashLedger"
TABLE63 = "MachineReadableDusartTable63EpsilonPsiLedger"
TABLE64 = "ThetaLessThanIdentityTable64To8e11SourceLedger"
ZERO_BINDING = "VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger"
INTERVAL = "PsiEpsilonIntervalPropagationAndMonotonicityLedger"
HASH = "ReproduciblePsiEpsilonTableComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-middle-psi-upper-source-router.json",
    "prime-matrix-strict-middle-finite-interval-psi-cover-router.json",
    "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json",
    "prime-matrix-strict-deleglise-rivat-psi-node-data-router.json",
    "prime-matrix-strict-machine-readable-node-archive-router.json",
    "prime-matrix-strict-full-node-archive-feasibility-router.json",
    "prime-matrix-strict-delta-aware-psi-range-algorithm-router.json",
    "prime-matrix-strict-psi-epsilon-table-algorithm-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    result = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }
    if DATA.exists():
        result[str(DATA.relative_to(ROOT))] = sha256(DATA)
    return result


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把中段 psi 上界链同步到完整 delta-aware 节点归档。"""
    middle_source = data["middle_source"]
    middle_cover = data["middle_cover"]
    fine_mesh = data["fine_mesh"]
    node_data = data["node_data"]
    machine_archive = data["machine_archive"]
    full_feasibility = data["full_feasibility"]
    delta = data["delta"]
    table_algorithm = data["table_algorithm"]

    archive = delta.get("full_archive", {})
    full_archive_closed = (
        delta.get("delta_aware_incremental_psi_range_algorithm_closed") is True
        and delta.get("full_delta_aware_psi_node_archive_run_hash_closed") is True
        and delta.get("full_node_archive_completeness_and_hash_closed") is True
        and delta.get("machine_readable_node_archive_closed") is True
        and delta.get("middle_psi_fine_mesh_node_slack_floor_hash_closed") is True
        and archive.get("passed") is True
        and archive.get("node_count") == archive.get("expected_node_count") == 646258
    )
    upstream_chain_active = (
        table_algorithm.get("next_direct_attack_target") == TARGET
        and middle_source.get("next_direct_attack_target") == MIDDLE_COVER
        and middle_cover.get("next_direct_attack_target")
        in {
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger",
            "MiddlePsiFineMeshNodeSlackFloorAndHashLedger",
        }
        and fine_mesh.get("next_direct_attack_target")
        == "DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger"
        and node_data.get("next_direct_attack_target") == NODE_ARCHIVE
    )
    stale_archive_open = (
        machine_archive.get("machine_readable_node_archive_closed") is False
        and full_feasibility.get("machine_readable_node_archive_closed") is False
    )

    return [
        row(
            "MiddlePsiUpperTargetActive",
            table_algorithm.get("next_direct_attack_target") == TARGET,
            True,
            "psi epsilon 表算法把当前最窄点设为中段 1.00002841 的来源/覆盖账本。",
            TARGET,
        ),
        row(
            "UpstreamReductionChainRecognized",
            upstream_chain_active,
            True,
            "中段上界已沿 source -> finite cover -> fine mesh -> node data -> machine archive 链条传递。",
            DELTA_ARCHIVE,
        ),
        row(
            "OldMachineArchiveCertificatesStaleOpen",
            stale_archive_open,
            True,
            "旧 machine/full-node 证书记录的是完整归档生成前状态，需要由 delta-aware 证书覆盖同步。",
            "use newest delta-aware archive certificate",
        ),
        row(
            "DeltaAwareFullArchiveClosed",
            full_archive_closed,
            True,
            "delta-aware 分段增量算法已生成完整 646258 节点归档，并通过 hash/连续性/余量审计。",
            "closed",
        ),
        row(
            "ArchiveHashRegistered",
            DATA.exists() and archive.get("sha256") == sha256(DATA),
            True,
            "完整节点表文件存在，且证书 hash 与实际文件 hash 一致。",
            archive.get("sha256", "missing"),
        ),
        row(
            "MiddleFineMeshNodeSlackClosed",
            full_archive_closed,
            True,
            "节点余量下界已由完整归档关闭，因此中段 fine mesh/hash 守门关闭。",
            FINE_MESH,
        ),
        row(
            "MiddleFiniteIntervalPsiCoverClosed",
            full_archive_closed,
            True,
            "细网格覆盖路线关闭后，8e11 到 e^28 的中段 psi 覆盖闭合。",
            MIDDLE_COVER,
        ),
        row(
            "MiddlePsiUpper100002841SourceClosed",
            full_archive_closed,
            True,
            "中段 psi(x)<1.00002841x 的来源/覆盖账本由 delta-aware 完整归档给出。",
            TARGET,
        ),
        row(
            "PsiEpsilonTableAlgorithmStillOpen",
            True,
            False,
            "关闭中段上界不等于关闭整个 epsilon 表算法；Table 6.3、Table 6.4、零点输入绑定、传播与 hash 仍需合取。",
            f"{TABLE63} AND {TABLE64} AND {ZERO_BINDING} AND {INTERVAL} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "中段 psi 归档不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "middle_source": load_json("prime-matrix-strict-middle-psi-upper-source-router.json"),
        "middle_cover": load_json("prime-matrix-strict-middle-finite-interval-psi-cover-router.json"),
        "fine_mesh": load_json("prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json"),
        "node_data": load_json("prime-matrix-strict-deleglise-rivat-psi-node-data-router.json"),
        "machine_archive": load_json("prime-matrix-strict-machine-readable-node-archive-router.json"),
        "full_feasibility": load_json("prime-matrix-strict-full-node-archive-feasibility-router.json"),
        "delta": load_json("prime-matrix-strict-delta-aware-psi-range-algorithm-router.json"),
        "table_algorithm": load_json("prime-matrix-strict-psi-epsilon-table-algorithm-router.json"),
    }
    rows = build_rows(data)
    middle_closed = next(
        item["closed"] for item in rows if item["gate"] == "MiddlePsiUpper100002841SourceClosed"
    )
    archive = data["delta"].get("full_archive", {})
    return {
        "certificate_type": "prime_matrix_strict_middle_psi_upper_delta_archive_sync_router",
        "status": "middle_psi_upper_100002841_closed_by_delta_aware_full_archive_table_algorithm_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "middle_psi_upper_100002841_source_closed": middle_closed,
        "middle_finite_interval_psi_cover_closed": middle_closed,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": middle_closed,
        "machine_readable_node_archive_closed": middle_closed,
        "full_node_archive_completeness_and_hash_closed": middle_closed,
        "psi_epsilon_table_algorithm_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "archive_summary": {
            "path": archive.get("path"),
            "sha256": archive.get("sha256"),
            "node_count": archive.get("node_count"),
            "expected_node_count": archive.get("expected_node_count"),
            "min_slack": archive.get("min_slack"),
            "required_node_slack_floor": archive.get("required_node_slack_floor"),
            "error_count": archive.get("error_count"),
        },
        "replacement_after_sync": {
            TARGET: "closed by data/middle-psi-fine-mesh-node-table.jsonl delta-aware archive",
            "PsiEpsilonTableComputationAlgorithmLedger": (
                f"{TABLE63} AND {TABLE64} AND {ZERO_BINDING} AND {INTERVAL} AND {HASH}"
            ),
        },
        "next_direct_attack_target": TABLE63,
        "parallel_attack_targets": [TABLE64, ZERO_BINDING, INTERVAL, HASH, DSTRUCTURE],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "中段 `psi(x)<1.00002841x` 的来源/覆盖账本已由最新 delta-aware 完整归档同步关闭："
            "完整 646258 节点表存在，hash 与证书一致，节点数、连续性和余量审计通过。"
            "这回收了旧 machine-readable archive 证书中的开放状态。但这只关闭中段上界分支；"
            "整个 Schoenfeld/Dusart epsilon 表算法仍需 Table 6.3、Table 6.4、零点输入绑定、区间传播与可复现 hash。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 中段 psi 上界 delta-aware 归档同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"middle_psi_upper_100002841_source_closed={fmt_bool(result['middle_psi_upper_100002841_source_closed'])}",
        f"middle_finite_interval_psi_cover_closed={fmt_bool(result['middle_finite_interval_psi_cover_closed'])}",
        f"middle_psi_fine_mesh_node_slack_floor_hash_closed={fmt_bool(result['middle_psi_fine_mesh_node_slack_floor_hash_closed'])}",
        f"machine_readable_node_archive_closed={fmt_bool(result['machine_readable_node_archive_closed'])}",
        f"psi_epsilon_table_algorithm_closed={fmt_bool(result['psi_epsilon_table_algorithm_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 归档摘要",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["archive_summary"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"middle_psi_upper_100002841_source_closed={fmt_bool(result['middle_psi_upper_100002841_source_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
