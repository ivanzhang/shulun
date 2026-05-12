#!/usr/bin/env python3
"""生成 strict 中段 psi 机器可读节点归档路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_machine_readable_node_archive_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-machine-readable-node-archive-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-machine-readable-node-archive-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-machine-readable-node-archive-router.md"

NODE_DATA = MONOGRAPH / "prime-matrix-strict-deleglise-rivat-psi-node-data-router.json"
NODE_SLACK = MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"
NATIVE_RANGE_SOURCE = ROOT / "experiments" / "prime_matrix_middle_psi_native_range_runner.cpp"

SOURCE_FILES = [NODE_DATA, NODE_SLACK, CLAIM_STATUS, NATIVE_RANGE_SOURCE]

TARGET = "MachineReadableNodeArchiveLedger"
NATIVE_RANGE = "NativeRangePsiThetaBatchExecutableLedger"
EXTERNAL_ARCHIVE = "ExternalPrecomputedPsiNodeArchiveWithHashLedger"
ARCHIVE_HASH = "FullNodeArchiveCompletenessAndHashLedger"
CONVENTION = "SourceAlgorithmToDusartConventionMatch"
NODE_AUDIT = "NodeSlackFloorAuditLedger"
NODE_HASH = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

X_LEFT = 8.0e11
X_RIGHT = math.exp(28)
MESH_H = 1_000_000.0
EXPECTED_NODE_COUNT = math.ceil((X_RIGHT - X_LEFT) / MESH_H)
SAMPLE_NODE_TABLE = Path("/tmp/middle-psi-nodes-sample.jsonl")
NATIVE_RANGE_EXECUTABLE = Path("/tmp/PsiTheta/psi_range_jsonl")
NATIVE_RANGE_SAMPLE = Path("/tmp/middle-psi-native-range-sample.jsonl")


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


def sample_profile() -> dict[str, Any]:
    """读取目标区间样本节点。"""
    records: list[dict[str, Any]] = []
    if SAMPLE_NODE_TABLE.exists():
        with SAMPLE_NODE_TABLE.open("r", encoding="utf-8") as handle:
            records = [json.loads(line) for line in handle if line.strip()]
    return {
        "sample_path": str(SAMPLE_NODE_TABLE),
        "sample_present": SAMPLE_NODE_TABLE.exists(),
        "sample_sha256": sha256(SAMPLE_NODE_TABLE) if SAMPLE_NODE_TABLE.exists() else None,
        "sample_count": len(records),
        "sample_all_slack_ok": bool(records) and all(record.get("slack_ge_required_floor") for record in records),
        "sample_records": records[:3],
    }


def native_range_profile() -> dict[str, Any]:
    """读取原生 range runner 的样本状态。"""
    records: list[dict[str, Any]] = []
    if NATIVE_RANGE_SAMPLE.exists():
        with NATIVE_RANGE_SAMPLE.open("r", encoding="utf-8") as handle:
            records = [json.loads(line) for line in handle if line.strip()]
    sample_ok = bool(records) and all(record.get("slack_ge_required_floor") for record in records)
    return {
        "native_source": str(NATIVE_RANGE_SOURCE.relative_to(ROOT)),
        "native_source_present": NATIVE_RANGE_SOURCE.exists(),
        "native_source_sha256": sha256(NATIVE_RANGE_SOURCE) if NATIVE_RANGE_SOURCE.exists() else None,
        "native_executable": str(NATIVE_RANGE_EXECUTABLE),
        "native_executable_present": NATIVE_RANGE_EXECUTABLE.exists(),
        "native_executable_sha256": sha256(NATIVE_RANGE_EXECUTABLE) if NATIVE_RANGE_EXECUTABLE.exists() else None,
        "native_sample": str(NATIVE_RANGE_SAMPLE),
        "native_sample_present": NATIVE_RANGE_SAMPLE.exists(),
        "native_sample_sha256": sha256(NATIVE_RANGE_SAMPLE) if NATIVE_RANGE_SAMPLE.exists() else None,
        "native_sample_count": len(records),
        "native_sample_all_slack_ok": sample_ok,
        "native_sample_records": records[:3],
    }


def archive_spec() -> dict[str, Any]:
    """给出完整归档必须满足的机械规格。"""
    return {
        "expected_node_count": EXPECTED_NODE_COUNT,
        "x_left": X_LEFT,
        "x_right": X_RIGHT,
        "mesh_h": MESH_H,
        "first_index": 0,
        "last_index": EXPECTED_NODE_COUNT - 1,
        "min_records_per_required_archive": EXPECTED_NODE_COUNT,
        "canonical_serialization": "JSONL sorted by i, UTF-8, LF, one record per start node",
        "minimum_required_fields": [
            "i",
            "x_i",
            "psi_value",
            "psi_upper_for_slack",
            "slack_lower_bound",
            "slack_ge_required_floor",
            "psi_exe_sha256",
            "source_commit",
        ],
    }


def build_result() -> dict[str, Any]:
    """构造机器可读节点归档路由证书。"""
    node_data = load_json(NODE_DATA)
    node_slack = load_json(NODE_SLACK)
    sample = sample_profile()
    native_range = native_range_profile()
    spec = archive_spec()
    sample_ready = sample["sample_present"] and sample["sample_all_slack_ok"]
    native_range_ready = (
        native_range["native_source_present"]
        and native_range["native_executable_present"]
        and native_range["native_sample_all_slack_ok"]
    )
    audit_ready = node_data.get("canonical_node_table_audit_checker_closed") is True
    runner_ready = node_data.get("canonical_batch_psi_node_runner_closed") is True
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            node_data.get("counterexample_assumption_only") is True
            and node_data.get("row_column_unconditional_closed") is False,
            True,
            "本步只处理 psi 节点归档的机器可读性，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ArchiveSpecificationLedger",
            True,
            True,
            "完整归档必须覆盖 646258 个百万网格起始节点，并采用稳定 JSONL/hash 口径。",
            ARCHIVE_HASH,
        ),
        row(
            "TargetScaleSingleNodeSampleLedger",
            sample_ready,
            sample_ready,
            "目标区间首节点样本已生成并过余量门槛，但样本不是完整归档。",
            TARGET,
        ),
        row(
            "AuditCheckerAvailable",
            audit_ready,
            audit_ready,
            "已有节点表验收器可检查节点数、索引、x_i、余量和 SHA256。",
            "requires full archive as input",
        ),
        row(
            "PerNodeCliArchiveRouteRejected",
            True,
            True,
            "原单点 CLI 即使可运行，也不能作为完整归档策略；需要原生 range 批量程序或外部预计算归档。",
            f"{NATIVE_RANGE} OR {EXTERNAL_ARCHIVE}",
        ),
        row(
            NATIVE_RANGE,
            native_range_ready,
            native_range_ready,
            "已新增并编译 C++ 原生 range runner，目标首节点样本输出通过余量门槛。",
            "full archive generation still required",
        ),
        row(
            EXTERNAL_ARCHIVE,
            False,
            False,
            "或者导入外部已计算的完整节点表，并登记来源、版本和整体 SHA256。",
            "precomputed full archive",
        ),
        row(
            ARCHIVE_HASH,
            False,
            False,
            "需要完整 646258 行通过 audit 脚本，并固定整体 hash。",
            "full archive must exist",
        ),
        row(
            TARGET,
            False,
            False,
            "归档规格、样本和验收器已就绪，但完整机器可读节点归档仍未生成。",
            f"({NATIVE_RANGE} OR {EXTERNAL_ARCHIVE}) AND {ARCHIVE_HASH}",
        ),
        row(
            "DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger",
            False,
            False,
            "节点归档未闭合时，等价计算数据/hash 仍不能升级。",
            f"{TARGET} AND {CONVENTION}",
        ),
        row(
            NODE_HASH,
            False,
            False,
            "节点归档未闭合时，节点余量/hash 守门仍开放。",
            f"{TARGET} AND {NODE_AUDIT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "节点归档路由不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_machine_readable_node_archive_router",
        "status": "node_archive_spec_sample_audit_ready_full_archive_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "archive_specification_closed": True,
        "target_scale_single_node_sample_closed": sample_ready,
        "node_table_audit_checker_available": audit_ready,
        "canonical_batch_psi_node_runner_closed": runner_ready,
        "per_node_cli_archive_route_rejected": True,
        "native_range_psi_theta_batch_executable_closed": native_range_ready,
        "external_precomputed_psi_node_archive_with_hash_closed": False,
        "machine_readable_node_archive_closed": False,
        "full_node_archive_completeness_and_hash_closed": False,
        "deleglise_rivat_psi_node_data_or_equivalent_hash_closed": False,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "archive_spec": spec,
        "sample_profile": sample,
        "native_range_profile": native_range,
        "replacement_after_this": {
            TARGET: f"({NATIVE_RANGE} OR {EXTERNAL_ARCHIVE}) AND {ARCHIVE_HASH}",
            "DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger": f"{TARGET} AND {CONVENTION}",
        },
        "next_direct_attack_target": ARCHIVE_HASH if native_range_ready else NATIVE_RANGE,
        "parallel_attack_targets": [EXTERNAL_ARCHIVE, CONVENTION, ARCHIVE_HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "机器可读节点归档已经压成一个明确的工程-数学证书：规格、目标首节点样本和验收器就绪，"
            "但完整 646258 行表尚未生成。单点 CLI 路线不能作为完整归档策略；原生 range "
            "批量可执行文件已跑通样本，下一步应生成完整归档并验收 hash，或导入外部完整归档。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 机器可读 psi 节点归档路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"archive_specification_closed={fmt_bool(result['archive_specification_closed'])}",
        f"target_scale_single_node_sample_closed={fmt_bool(result['target_scale_single_node_sample_closed'])}",
        f"node_table_audit_checker_available={fmt_bool(result['node_table_audit_checker_available'])}",
        f"native_range_psi_theta_batch_executable_closed={fmt_bool(result['native_range_psi_theta_batch_executable_closed'])}",
        f"machine_readable_node_archive_closed={fmt_bool(result['machine_readable_node_archive_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 归档规格",
        "",
        "```text",
    ]
    for key, value in result["archive_spec"].items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}={fmt_float(float(value))}")
        else:
            lines.append(f"{key}={value}")
    lines.extend(["```", "", "## 2. 样本", "", "```text"])
    for key, value in result["sample_profile"].items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        else:
            lines.append(f"{key}={value}")
    lines.append("")
    lines.append("[native_range_profile]")
    for key, value in result["native_range_profile"].items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        else:
            lines.append(f"{key}={value}")
    lines.extend(["```", "", "## 3. 剩余替换", "", "```text"])
    for key, value in result["replacement_after_this"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 4. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 5. 下一最窄点",
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
