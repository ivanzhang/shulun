#!/usr/bin/env python3
"""生成 strict 完整 psi 节点归档可行性路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_full_node_archive_feasibility_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-full-node-archive-feasibility-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-full-node-archive-feasibility-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-full-node-archive-feasibility-router.md"

ARCHIVE_ROUTER = MONOGRAPH / "prime-matrix-strict-machine-readable-node-archive-router.json"
NODE_DATA = MONOGRAPH / "prime-matrix-strict-deleglise-rivat-psi-node-data-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [ARCHIVE_ROUTER, NODE_DATA, CLAIM_STATUS]

TARGET = "FullNodeArchiveCompletenessAndHashLedger"
INCREMENTAL = "DeltaAwareIncrementalPsiRangeAlgorithmLedger"
EXTERNAL_ARCHIVE = "ExternalPrecomputedPsiNodeArchiveWithHashLedger"
CONVENTION = "SourceAlgorithmToDusartConventionMatch"
NODE_HASH = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

EXPECTED_NODE_COUNT = 646_258
OBSERVED_SECONDS_PER_NODE = 56.39
TIMING_SAMPLE = Path("/tmp/middle-psi-native-range-timing-sample.jsonl")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """稳定输出浮点。"""
    return f"{value:.15e}"


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


def cost_profile() -> dict[str, float | bool]:
    """估算逐节点重算方案的完整归档成本。"""
    total_seconds = OBSERVED_SECONDS_PER_NODE * EXPECTED_NODE_COUNT
    return {
        "expected_node_count": EXPECTED_NODE_COUNT,
        "observed_seconds_per_node": OBSERVED_SECONDS_PER_NODE,
        "estimated_total_seconds": total_seconds,
        "estimated_total_hours": total_seconds / 3600.0,
        "estimated_total_days": total_seconds / 86400.0,
        "single_node_recompute_full_archive_practical": total_seconds < 7 * 86400.0,
    }


def build_result() -> dict[str, Any]:
    """构造完整节点归档可行性证书。"""
    archive = load_json(ARCHIVE_ROUTER)
    node_data = load_json(NODE_DATA)
    profile = cost_profile()
    timing_sample_present = TIMING_SAMPLE.exists()
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            archive.get("counterexample_assumption_only") is True
            and archive.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计节点归档生成可行性，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "TimingSampleLedger",
            timing_sample_present,
            timing_sample_present,
            "原生 range runner 的目标首节点计时样本已经取得。",
            "single-node timing only",
        ),
        row(
            "SingleNodeRecomputeArchiveRouteRejected",
            not bool(profile["single_node_recompute_full_archive_practical"]),
            True,
            "按当前逐节点重算速度，完整 646258 节点归档估计需要数百天，不能作为现实闭合路线。",
            f"{INCREMENTAL} OR {EXTERNAL_ARCHIVE}",
        ),
        row(
            INCREMENTAL,
            False,
            False,
            "需要真正利用相邻 x_i=x_0+i h 的增量结构，避免每个节点从零重算 psi。",
            "incremental segmented prime-power update or library-level range API",
        ),
        row(
            EXTERNAL_ARCHIVE,
            False,
            False,
            "或者导入外部已经计算完成的全节点归档，并用现有 audit 脚本验收。",
            "external full JSONL archive and hash",
        ),
        row(
            TARGET,
            False,
            False,
            "完整节点表尚未存在；当前逐节点重算方案被成本审计排除。",
            f"{INCREMENTAL} OR {EXTERNAL_ARCHIVE}",
        ),
        row(
            "MachineReadableNodeArchiveLedger",
            False,
            False,
            "完整归档/hash 未闭合时，机器可读节点归档仍不能升级。",
            TARGET,
        ),
        row(
            NODE_HASH,
            False,
            False,
            "节点表未闭合时，节点余量/hash 守门仍开放。",
            f"{TARGET} AND {CONVENTION}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "完整归档可行性审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_full_node_archive_feasibility_router",
        "status": "full_archive_single_node_recompute_rejected_incremental_or_external_archive_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "timing_sample_present": timing_sample_present,
        "native_range_psi_theta_batch_executable_closed": archive.get(
            "native_range_psi_theta_batch_executable_closed"
        )
        is True,
        "single_node_recompute_archive_route_rejected": not bool(
            profile["single_node_recompute_full_archive_practical"]
        ),
        "delta_aware_incremental_psi_range_algorithm_closed": False,
        "external_precomputed_psi_node_archive_with_hash_closed": False,
        "full_node_archive_completeness_and_hash_closed": False,
        "machine_readable_node_archive_closed": False,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "timing_sample_sha256": sha256(TIMING_SAMPLE) if timing_sample_present else None,
        "cost_profile": profile,
        "replacement_after_this": {
            TARGET: f"{INCREMENTAL} OR {EXTERNAL_ARCHIVE}",
            "MachineReadableNodeArchiveLedger": f"{TARGET} AND audit pass",
        },
        "next_direct_attack_target": INCREMENTAL,
        "parallel_attack_targets": [EXTERNAL_ARCHIVE, CONVENTION],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "完整节点归档的最窄点进一步明确：当前原生 range runner 仍是逐节点重算。目标首节点约 "
            "56.39 秒，外推 646258 个节点约 421.8 天，因此不能作为现实闭合路线。下一步必须写"
            "真正增量/分段的 range 算法，或导入外部完整节点归档并验收 hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 完整 psi 节点归档可行性路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"timing_sample_present={fmt_bool(result['timing_sample_present'])}",
        f"native_range_psi_theta_batch_executable_closed={fmt_bool(result['native_range_psi_theta_batch_executable_closed'])}",
        f"single_node_recompute_archive_route_rejected={fmt_bool(result['single_node_recompute_archive_route_rejected'])}",
        f"full_node_archive_completeness_and_hash_closed={fmt_bool(result['full_node_archive_completeness_and_hash_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 成本画像",
        "",
        "```text",
    ]
    for key, value in result["cost_profile"].items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        else:
            lines.append(f"{key}={fmt_float(float(value))}")
    lines.extend(["```", "", "## 2. 剩余替换", "", "```text"])
    for key, value in result["replacement_after_this"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
