#!/usr/bin/env python3
"""生成 strict 中段 psi 细网格节点余量/hash 守门证书。

用法示例：
  python3 experiments/prime_matrix_strict_middle_psi_fine_mesh_node_slack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-slack-router.md"

SHORT_INCREMENT = MONOGRAPH / "prime-matrix-strict-short-interval-psi-increment-router.json"
MIDDLE_COVER = MONOGRAPH / "prime-matrix-strict-middle-finite-interval-psi-cover-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [SHORT_INCREMENT, MIDDLE_COVER, CLAIM_STATUS]

TARGET = "MiddlePsiFineMeshNodeSlackFloorAndHashLedger"
NODE_DATA = "DelegliseRivatPsiNodeDataOrEquivalentComputationHashLedger"
NODE_AUDIT = "NodeSlackFloorAuditLedger"
MESH_HASH = "MeshCompletenessAndIndexHashLedger"
ROUNDING = "MiddlePsiUpperDirectedRoundingLedger"
BT_INPUT = "BrunTitchmarshShortIntervalPrimeCountUpperLedger"
PRIME_POWER = "PrimePowerShortIntervalCorrectionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TARGET_RATIO = 1.00002841
X_LEFT = 8.0e11
X_RIGHT = math.exp(28)
MESH_H = 1_000_000.0

POINTS = [
    (8.0e11, 799_999_133_776.084743 + 904_203.190001),
    (9.0e11, 899_998_818_628.952024 + 958_602.924046),
    (1.0e12, 999_999_030_333.096225 + 1_009_803.669232),
    (2.0e12, 1_999_998_755_521.470649 + 1_427_105.865316),
]

NODE_TABLE_CANDIDATES = [
    MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-table.json",
    MONOGRAPH / "prime-matrix-strict-middle-psi-fine-mesh-node-table.jsonl",
    ROOT / "data" / "middle-psi-fine-mesh-node-table.jsonl",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
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


def mesh_id(payload: dict[str, Any]) -> str:
    """为网格定义生成稳定哈希。"""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def mesh_profile(required_node_slack_floor: float) -> dict[str, Any]:
    """给出百万网格的端点、节点数和证书格式。"""
    interval_count = math.ceil((X_RIGHT - X_LEFT) / MESH_H)
    last_start = X_LEFT + (interval_count - 1) * MESH_H
    final_interval_length = X_RIGHT - last_start
    regular_endpoint = X_LEFT + interval_count * MESH_H
    payload = {
        "x_left": X_LEFT,
        "x_right": X_RIGHT,
        "mesh_h": MESH_H,
        "target_ratio": TARGET_RATIO,
        "required_node_slack_floor": required_node_slack_floor,
        "start_node_rule": "x_i=x_left+i*h for 0<=i<ceil((x_right-x_left)/h), final interval clipped at x_right",
    }
    return {
        **payload,
        "mesh_id_sha256": mesh_id(payload),
        "start_node_count": interval_count,
        "first_start_node": X_LEFT,
        "last_start_node": last_start,
        "final_interval_length": final_interval_length,
        "regular_endpoint_overshoot": regular_endpoint - X_RIGHT,
        "required_record_fields": [
            "i",
            "x_i",
            "psi_upper_or_exact",
            "target_ratio_x_i_minus_psi_lower_slack",
            "slack_ge_required_floor",
            "computation_method",
            "directed_rounding_mode",
            "source_or_chunk_hash",
        ],
    }


def anchor_propagation_rows(required_node_slack_floor: float) -> list[dict[str, Any]]:
    """审计 Table 6.2 稀疏锚点能覆盖多少百万网格。"""
    in_range_points = [(x, psi) for x, psi in POINTS if X_LEFT <= x <= X_RIGHT]
    rows: list[dict[str, Any]] = []
    for index, (x, psi) in enumerate(in_range_points):
        slack = TARGET_RATIO * x - psi
        slack_units = slack / required_node_slack_floor
        certified_start_nodes = max(0, math.floor(slack_units))
        next_x = in_range_points[index + 1][0] if index + 1 < len(in_range_points) else X_RIGHT
        gap_start_nodes = math.ceil((next_x - x) / MESH_H)
        rows.append(
            {
                "anchor_x": x,
                "anchor_psi": psi,
                "anchor_slack": slack,
                "slack_in_required_floor_units": slack_units,
                "certified_start_nodes_by_worst_increment": certified_start_nodes,
                "certified_length": certified_start_nodes * MESH_H,
                "next_boundary": next_x,
                "gap_start_nodes_to_next_boundary": gap_start_nodes,
                "uncovered_start_nodes_to_next_boundary": max(0, gap_start_nodes - certified_start_nodes),
                "anchor_aligned_to_mesh": abs((x - X_LEFT) % MESH_H) < 1e-6,
            }
        )
    return rows


def node_table_presence() -> dict[str, Any]:
    """检查仓库是否已有可复算细网格节点表。"""
    existing = [path for path in NODE_TABLE_CANDIDATES if path.exists()]
    return {
        "candidate_paths": [str(path.relative_to(ROOT)) for path in NODE_TABLE_CANDIDATES],
        "existing_paths": [str(path.relative_to(ROOT)) for path in existing],
        "machine_readable_node_table_present": bool(existing),
    }


def build_result() -> dict[str, Any]:
    """构造细网格节点余量/hash 证书。"""
    short = load_json(SHORT_INCREMENT)
    cover = load_json(MIDDLE_COVER)
    required_floor = float(short["arithmetic_profile"]["required_node_slack_floor"])
    mesh = mesh_profile(required_floor)
    anchors = anchor_propagation_rows(required_floor)
    presence = node_table_presence()
    active = short.get("next_direct_attack_target") == TARGET
    sparse_anchor_cannot_close = all(item["uncovered_start_nodes_to_next_boundary"] > 0 for item in anchors)
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            short.get("counterexample_assumption_only") is True
            and short.get("row_column_unconditional_closed") is False,
            True,
            "本步只补中段解析输入证书，不用真实零行缺席来替代假设反例链。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "MiddlePsiFineMeshNodeSlackGateActive",
            active and cover.get("middle_finite_interval_psi_cover_closed") is False,
            True,
            "短区间增量账本已把百万网格路线的主要缺口压成节点余量和 hash。",
            TARGET,
        ),
        row(
            "MeshDefinitionAndEndpointLedger",
            True,
            True,
            "百万网格端点、起始节点数、最后截断区间和记录字段已经固定。",
            "none",
        ),
        row(
            "RequiredNodeSlackFloorImported",
            required_floor > 0,
            True,
            "从短区间增量账本继承每个起始节点至少约 3.073386e6 的绝对余量门槛。",
            "node table must certify every start node above this floor",
        ),
        row(
            "SparseDusartAnchorsCannotReplaceFineMesh",
            sparse_anchor_cannot_close,
            True,
            "Table 6.2 的 8e11、9e11、1e12 稀疏锚点在最坏增量传播下只能覆盖个位数百万网格，不能跨越十万级缺口。",
            NODE_DATA,
        ),
        row(
            "NodeTableSchemaContractClosed",
            True,
            True,
            "节点表必须逐行给出 i、x_i、psi 上界或精确值、余量、舍入模式和分块 hash。",
            MESH_HASH,
        ),
        row(
            "MachineReadableNodeTablePresent",
            presence["machine_readable_node_table_present"],
            presence["machine_readable_node_table_present"],
            "仓库当前未发现覆盖 646258 个起始节点的机器可读 psi 节点表。",
            NODE_DATA,
        ),
        row(
            NODE_DATA,
            False,
            False,
            "需要 Deléglise-Rivat 数据或等价可复算算法输出，并绑定版本、端点、舍入和 hash。",
            "external data archive or internal exact psi computation certificate",
        ),
        row(
            NODE_AUDIT,
            False,
            False,
            "需要逐节点检查 target*x_i-psi(x_i) >= required_node_slack_floor。",
            "requires machine-readable node table",
        ),
        row(
            MESH_HASH,
            False,
            False,
            "需要证明索引 0..646257 无缺行、无重复、端点截断一致，并给出整体 hash。",
            "requires canonical table serialization",
        ),
        row(
            ROUNDING,
            False,
            False,
            "需要外向舍入规则，防止浮点/十进制表值把 4.46e-11 级拼接余量吃掉。",
            "directed rounding proof",
        ),
        row(
            TARGET,
            False,
            False,
            "本步关闭了网格合同和稀疏锚点失败审计，但没有节点数据/hash，故节点余量守门仍开放。",
            f"{NODE_DATA} AND {NODE_AUDIT} AND {MESH_HASH} AND {ROUNDING}",
        ),
        row(
            "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger",
            False,
            False,
            "即使节点余量未来闭合，短区间总包仍还要 BT 输入和素数幂修正。",
            f"{BT_INPUT} AND {PRIME_POWER} AND {TARGET}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "细网格节点合同不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_middle_psi_fine_mesh_node_slack_router",
        "status": "fine_mesh_node_contract_closed_sparse_anchors_rejected_node_data_hash_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "mesh_definition_endpoint_closed": True,
        "required_node_slack_floor_imported": True,
        "sparse_dusart_anchors_cannot_replace_fine_mesh": sparse_anchor_cannot_close,
        "node_table_schema_contract_closed": True,
        "machine_readable_node_table_present": presence["machine_readable_node_table_present"],
        "deleglise_rivat_psi_node_data_or_equivalent_hash_closed": False,
        "node_slack_floor_audit_closed": False,
        "mesh_completeness_and_index_hash_closed": False,
        "middle_psi_upper_directed_rounding_closed": False,
        "middle_psi_fine_mesh_node_slack_floor_hash_closed": False,
        "certified_short_interval_psi_increment_upper_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "mesh_profile": mesh,
        "anchor_propagation_rows": anchors,
        "node_table_presence": presence,
        "replacement_self_contained": {
            TARGET: f"{NODE_DATA} AND {NODE_AUDIT} AND {MESH_HASH} AND {ROUNDING}",
            NODE_DATA: "machine-readable psi node table or reproducible exact psi computation over the certified mesh",
        },
        "next_direct_attack_target": NODE_DATA,
        "parallel_attack_targets": [BT_INPUT, PRIME_POWER, NODE_AUDIT, MESH_HASH, ROUNDING],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "细网格节点余量/hash 的边界现在清楚了：需要覆盖 646258 个百万网格起始节点。"
            "Dusart Table 6.2 的稀疏点值虽然强，但在最坏短区间增量传播下只能从每个锚点推出个位数"
            "百万网格的安全余量，无法跨越十万级点间缺口。因此节点表或等价可复算 psi 算法/hash 是不可省略输入。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    mesh = result["mesh_profile"]
    lines = [
        "# Prime Matrix strict 中段 psi 细网格节点余量/hash 守门器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"mesh_definition_endpoint_closed={fmt_bool(result['mesh_definition_endpoint_closed'])}",
        f"sparse_dusart_anchors_cannot_replace_fine_mesh={fmt_bool(result['sparse_dusart_anchors_cannot_replace_fine_mesh'])}",
        f"node_table_schema_contract_closed={fmt_bool(result['node_table_schema_contract_closed'])}",
        f"machine_readable_node_table_present={fmt_bool(result['machine_readable_node_table_present'])}",
        f"middle_psi_fine_mesh_node_slack_floor_hash_closed={fmt_bool(result['middle_psi_fine_mesh_node_slack_floor_hash_closed'])}",
        f"certified_short_interval_psi_increment_upper_closed={fmt_bool(result['certified_short_interval_psi_increment_upper_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 网格合同",
        "",
        "```text",
    ]
    for key, value in mesh.items():
        if isinstance(value, bool):
            lines.append(f"{key}={fmt_bool(value)}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}={fmt_float(float(value))}")
        else:
            lines.append(f"{key}={value}")
    lines.extend(
        [
            "```",
            "",
            "## 2. 稀疏锚点传播审计",
            "",
            "| anchor_x | slack | slack/floor | certified_start_nodes | gap_to_next | uncovered |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["anchor_propagation_rows"]:
        lines.append(
            f"| `{fmt_float(float(item['anchor_x']))}` | `{fmt_float(float(item['anchor_slack']))}` | "
            f"`{fmt_float(float(item['slack_in_required_floor_units']))}` | "
            f"`{item['certified_start_nodes_by_worst_increment']}` | "
            f"`{item['gap_start_nodes_to_next_boundary']}` | "
            f"`{item['uncovered_start_nodes_to_next_boundary']}` |"
        )
    lines.extend(["", "## 3. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
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
