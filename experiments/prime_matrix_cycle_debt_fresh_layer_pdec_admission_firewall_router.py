#!/usr/bin/env python3
"""生成 cycle-debt fresh-layer PDEC 准入防火墙证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_fresh_layer_pdec_admission_firewall_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json

输出：
  data/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json
  docs/monograph/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.json
  docs/monograph/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

REMOTE_FEEDBACK = DATA / "prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json"
LOCAL_COLLISION = DATA / "prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json"
PDEC_BOUNDARY = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
NEWLAYER_SCHEMA = DOCS / "prime-matrix-newlayer-pdec-schema-admission-router.json"
NEWLAYER_RANKTWO = DOCS / "prime-matrix-newlayer-ranktwo-budget-ledger-router.json"
SPARSE_BOUNDARY = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.md"

PREVIOUS_TARGET = "MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter"
NEXT_TARGET = "FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 fresh-layer PDEC 准入防火墙证书。"""
    remote = load_json(REMOTE_FEEDBACK)
    local = load_json(LOCAL_COLLISION)
    pdec = load_json(PDEC_BOUNDARY)
    schema = load_json(NEWLAYER_SCHEMA)
    ranktwo = load_json(NEWLAYER_RANKTWO)
    sparse = load_json(SPARSE_BOUNDARY)

    remote_by_label = {item["label"]: item for item in remote["remote_blocks"]}
    local_blocks = sorted(local["blocks"], key=lambda item: item["label"])
    blocks: list[dict[str, Any]] = []
    for item in local_blocks:
        remote_item = remote_by_label[item["label"]]
        max_window = max(int(item["support_width"]), int(item["audit_slot_count"]))
        locally_injective = bool(item["local_affine_projection_injective_for_sample"])
        local_materialization_forbidden = locally_injective and int(item["first_fresh_prime"]) > max_window
        blocks.append(
            {
                "label": item["label"],
                "support_width": int(item["support_width"]),
                "audit_slot_count": int(item["audit_slot_count"]),
                "first_fresh_prime": int(item["first_fresh_prime"]),
                "first_fresh_minus_max_window": int(item["first_fresh_prime"]) - max_window,
                "local_affine_projection_injective": locally_injective,
                "local_materialized_pdec_forbidden": local_materialization_forbidden,
                "remote_pspace_columncrt_modulus_log10": remote_item[
                    "p_space_columncrt_modulus_log10"
                ],
                "remote_plus_first_fresh_log10": remote_item["remote_plus_first_fresh_log10"],
                "future_schema_required_if_materialized": True,
            }
        )

    local_registered_materialization_closed = all(
        item["local_materialized_pdec_forbidden"] for item in blocks
    )
    current_materialized_pdec_frontier_closed = bool(
        pdec["current_materialized_pdec_frontier_closed"]
    )
    pdec_boundary_closed = bool(pdec["pdec_family_explicit_input_boundary_closed"])
    newlayer_schema_closed = bool(schema["newlayer_schema_admission_closed"])
    newlayer_ranktwo_independent_removed = bool(
        ranktwo["newlayer_ranktwo_budget_independent_input_removed"]
    )
    future_sparse_boundary_closed = bool(sparse["future_sparse_packet_schema_boundary_closed"])
    materialized_branch_imported = not bool(remote["materialized_fresh_layer_pdec_columncrt_excluded"])

    current_corpus_materialized_fresh_pdec_closed = (
        materialized_branch_imported
        and local_registered_materialization_closed
        and current_materialized_pdec_frontier_closed
        and pdec_boundary_closed
        and newlayer_schema_closed
        and newlayer_ranktwo_independent_removed
    )

    gates = [
        gate(
            "MaterializedFreshLayerBranchImported",
            materialized_branch_imported,
            True,
            "上一证书把裸 remote ColumnCRT 删除后，只留下材料化 fresh-layer PDEC/ColumnCRT 或未登记 moving family。",
            PREVIOUS_TARGET,
        ),
        gate(
            "RegisteredLocalFreshMaterializationForbidden",
            local_registered_materialization_closed,
            True,
            "registered support 内 fresh prime 均大于窗口，且仿射投影单射；本地相位复用不能材料化为 PDEC。",
            "closed for registered blocks",
        ),
        gate(
            "CurrentMaterializedPDECFrontierClosed",
            current_materialized_pdec_frontier_closed,
            True,
            "广义 PDEC 边界证书记录当前已物化合法非二点 primitive PDEC 候选为零。",
            "future explicit primitive schema only",
        ),
        gate(
            "ColumnCRTAbsorbedBeforeAdmission",
            pdec_boundary_closed,
            True,
            "PDEC family 边界规定 ColumnCRT/位移不能直接准入；必须先转成 displacement/refined PDEC 或 SAE。",
            "closed as unnamed ColumnCRT terminal",
        ),
        gate(
            "NewLayerSchemaAdmissionClosed",
            newlayer_schema_closed,
            True,
            "若 fresh-layer PDEC 真正作为 new-layer 候选出现，其 formal-unit schema 准入层已闭合。",
            "rank-two cap-stable or named return",
        ),
        gate(
            "NewLayerRankTwoIndependentGateRemoved",
            newlayer_ranktwo_independent_removed,
            True,
            "new-layer 二秩预算失败不再是独立输入；它会材料化为有限弧 cap 并回流命名出口或 flat gate。",
            "NewLayerNoConcentrationImpliesFlatAdmission if a future schema reaches it",
        ),
        gate(
            "SparseFallbackSchemaBoundaryClosed",
            future_sparse_boundary_closed,
            True,
            "若所谓材料化只是 sparse packet 或局部幸存者失败，则未来 sparse schema 边界已要求完整 extractor。",
            "future sparse schema if new",
        ),
        gate(
            "CurrentCorpusMaterializedFreshPDECClosed",
            current_corpus_materialized_fresh_pdec_closed,
            True,
            "当前 cycle-debt 语料中没有可准入的材料化 fresh-layer PDEC/ColumnCRT；无名材料化口径被删除。",
            NEXT_TARGET,
        ),
        gate(
            "FutureExplicitPrimitiveFreshLayerPDECSchemaIfNew",
            False,
            False,
            "未来若真新增 fresh-layer PDEC family，必须提交同 formal unit、三物理原子以上、二秩 cap-stable 的全集 schema。",
            "FutureExplicitPrimitiveFreshLayerPDECSchema",
        ),
        gate(
            "UnregisteredMovingFamilyStillOpen",
            False,
            False,
            "阻断包、shape、source family 或 phase map 变化仍需单独 moving-family 路由。",
            "UnregisteredMovingFamilyRouter",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只关闭当前语料中的无名材料化 PDEC 口径；没有证明未来 schema 不存在，也没有排斥 moving family。",
            NEXT_TARGET,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_fresh_layer_pdec_admission_firewall_router",
        "status": "current_materialized_fresh_layer_pdec_frontier_closed_future_schema_or_unregistered_moving_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "registered_block_count": len(blocks),
        "minimum_first_fresh_minus_max_window": min(
            item["first_fresh_minus_max_window"] for item in blocks
        ),
        "minimum_remote_plus_first_fresh_log10": min(
            item["remote_plus_first_fresh_log10"] for item in blocks
        ),
        "local_registered_materialized_pdec_closed": local_registered_materialization_closed,
        "current_materialized_pdec_frontier_closed": current_materialized_pdec_frontier_closed,
        "pdec_family_explicit_input_boundary_closed": pdec_boundary_closed,
        "newlayer_schema_admission_closed": newlayer_schema_closed,
        "newlayer_ranktwo_budget_independent_gate_removed": newlayer_ranktwo_independent_removed,
        "future_sparse_packet_schema_boundary_closed": future_sparse_boundary_closed,
        "current_corpus_materialized_fresh_layer_pdec_closed": current_corpus_materialized_fresh_pdec_closed,
        "future_explicit_primitive_fresh_layer_pdec_schema_submitted": False,
        "future_explicit_primitive_fresh_layer_pdec_schema_excluded": False,
        "unregistered_moving_family_excluded": False,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "blocks": blocks,
        "required_future_schema_fields": [
            "同一个 formal_unit_id 与一个固定 phase map",
            "全部去重后至少三个物理 primitive atoms",
            "不是二点 Fourier tautology 或单列 displacement",
            "商去 shell/column 退化后相位秩至少为 2",
            "对每个有限循环弧 localization 均 cap-stable",
            "若 cap 失败，必须回流 SAE/refined PDEC/ColumnCRT/multiplicity",
            "若转成 sparse/local survivor，必须提交有限 packet extractor schema",
            "给出全集账本、哈希、open_obligation_count=0",
        ],
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "当前 cycle-debt fresh-layer PDEC/ColumnCRT 没有可保留的无名材料化实例：registered 本地投影单射排除"
            "本地材料化，广义 PDEC 边界记录当前合法 primitive 候选为零，ColumnCRT 必须先被吸收到 PDEC/SAE，"
            "new-layer schema 与二秩预算独立门也已给出准入/回流纪律。因此剩余只能是未来新增的显式 primitive "
            "fresh-layer PDEC schema，或阻断包变化形成的未登记 moving family。"
        ),
        "dependency_hashes": {
            str(REMOTE_FEEDBACK.relative_to(ROOT)): sha256(REMOTE_FEEDBACK),
            str(LOCAL_COLLISION.relative_to(ROOT)): sha256(LOCAL_COLLISION),
            str(PDEC_BOUNDARY.relative_to(ROOT)): sha256(PDEC_BOUNDARY),
            str(NEWLAYER_SCHEMA.relative_to(ROOT)): sha256(NEWLAYER_SCHEMA),
            str(NEWLAYER_RANKTWO.relative_to(ROOT)): sha256(NEWLAYER_RANKTWO),
            str(SPARSE_BOUNDARY.relative_to(ROOT)): sha256(SPARSE_BOUNDARY),
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix cycle-debt fresh-layer PDEC admission firewall router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"registered_block_count={result['registered_block_count']}",
        f"minimum_first_fresh_minus_max_window={result['minimum_first_fresh_minus_max_window']}",
        f"minimum_remote_plus_first_fresh_log10={result['minimum_remote_plus_first_fresh_log10']:.3f}",
        "local_registered_materialized_pdec_closed="
        f"{fmt_bool(result['local_registered_materialized_pdec_closed'])}",
        "current_materialized_pdec_frontier_closed="
        f"{fmt_bool(result['current_materialized_pdec_frontier_closed'])}",
        "pdec_family_explicit_input_boundary_closed="
        f"{fmt_bool(result['pdec_family_explicit_input_boundary_closed'])}",
        f"newlayer_schema_admission_closed={fmt_bool(result['newlayer_schema_admission_closed'])}",
        "newlayer_ranktwo_budget_independent_gate_removed="
        f"{fmt_bool(result['newlayer_ranktwo_budget_independent_gate_removed'])}",
        "current_corpus_materialized_fresh_layer_pdec_closed="
        f"{fmt_bool(result['current_corpus_materialized_fresh_layer_pdec_closed'])}",
        "future_explicit_primitive_fresh_layer_pdec_schema_submitted="
        f"{fmt_bool(result['future_explicit_primitive_fresh_layer_pdec_schema_submitted'])}",
        f"unregistered_moving_family_excluded={fmt_bool(result['unregistered_moving_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 防火墙逻辑",
        "",
        "材料化 fresh-layer PDEC/ColumnCRT 不能作为无名口径保留。registered support 内，fresh prime 投影在窗口中单射，不能形成本地相位复用；跨窗口或远程材料化若要成为 PDEC，必须通过已经登记的 PDEC family 准入边界。",
        "",
        "该准入边界要求同一 formal unit、固定相位映射、三物理原子以上、非二点 tautology、二秩以上且 cap-stable。若任一条件失败，事件回流 ColumnCRT/SAE/refined PDEC/sparse extractor/multiplicity，而不是成为新的终端。",
        "",
        "## 2. registered block 审计",
        "",
        "| block | support | audit | first fresh | fresh-window margin | local PDEC forbidden | remote+fresh log10 |",
        "| --- | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for block in result["blocks"]:
        lines.append(
            "| `{label}` | {support_width} | {audit_slot_count} | {first_fresh_prime} | "
            "{first_fresh_minus_max_window} | `{local_closed}` | "
            "{remote_plus_first_fresh_log10:.3f} |".format(
                local_closed=fmt_bool(block["local_materialized_pdec_forbidden"]),
                **block,
            )
        )

    lines.extend(
        [
            "",
            "## 3. 未来 schema 字段",
            "",
        ]
    )
    for item in result["required_future_schema_fields"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 5. 剩余接口",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书不证明未来 primitive fresh-layer PDEC schema 不存在，也不排斥未登记 moving family；它只关闭当前语料中的无名材料化 PDEC/ColumnCRT 口径。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "current_corpus_materialized_fresh_layer_pdec_closed": result[
            "current_corpus_materialized_fresh_layer_pdec_closed"
        ],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
