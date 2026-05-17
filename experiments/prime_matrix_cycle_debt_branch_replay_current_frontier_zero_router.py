#!/usr/bin/env python3
"""生成 cycle-debt branch-replay 当前物化前沿清零证书。

用法示例：
  python3 experiments/prime_matrix_cycle_debt_branch_replay_current_frontier_zero_router.py
  python3 -m json.tool data/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-ledger.json

输出：
  data/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-ledger.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json
  docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

FRESH_PDEC_FIREWALL = DATA / "prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json"
FINAL_FIREWALL = DOCS / "prime-matrix-final-input-firewall-boundary-router.json"
LEAF_FIREWALL = DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"
PDEC_BOUNDARY = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
SPARSE_BOUNDARY = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"

OUT_LEDGER = DATA / "prime-matrix-cycle-debt-branch-replay-current-frontier-zero-ledger.json"
OUT_JSON = DOCS / "prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json"
OUT_MD = DOCS / "prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.md"

PREVIOUS_TARGET = "FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter"
NEXT_TARGET = (
    "CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall;"
    "GlobalFinalInputsStillOpen"
)


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
    """构造当前前沿清零证书。"""
    fresh = load_json(FRESH_PDEC_FIREWALL)
    final = load_json(FINAL_FIREWALL)
    leaf = load_json(LEAF_FIREWALL)
    pdec = load_json(PDEC_BOUNDARY)
    sparse = load_json(SPARSE_BOUNDARY)

    current_fresh_pdec_closed = bool(fresh["current_corpus_materialized_fresh_layer_pdec_closed"])
    future_fresh_pdec_submitted = bool(
        fresh["future_explicit_primitive_fresh_layer_pdec_schema_submitted"]
    )
    unregistered_moving_family_excluded = bool(fresh["unregistered_moving_family_excluded"])
    future_pdec_discipline_closed = bool(leaf["future_pdec_schema_admission_discipline_closed"])
    future_sparse_discipline_closed = bool(leaf["future_sparse_schema_admission_discipline_closed"])
    pdec_boundary_closed = bool(pdec["pdec_family_explicit_input_boundary_closed"])
    sparse_boundary_closed = bool(sparse["future_sparse_packet_schema_boundary_closed"])
    final_firewall_closed = bool(final["final_input_firewall_boundary_closed"])
    no_hidden_terminal = bool(final["no_hidden_terminal_remaining"])

    # 当前仓库没有提交 branch-replay 专属的 unregistered moving-family schema；
    # 因而它只能保留为未来准入纪律，而不是当前已物化终端。
    unregistered_moving_family_schema_submitted = False
    future_schema_firewall_closed = (
        not future_fresh_pdec_submitted
        and not unregistered_moving_family_schema_submitted
        and future_pdec_discipline_closed
        and future_sparse_discipline_closed
        and pdec_boundary_closed
        and sparse_boundary_closed
    )
    current_materialized_frontier_zero = (
        current_fresh_pdec_closed
        and future_schema_firewall_closed
        and final_firewall_closed
        and no_hidden_terminal
    )

    gates = [
        gate(
            "FreshLayerPDECCurrentCorpusClosed",
            current_fresh_pdec_closed,
            True,
            "上一证书已关闭当前 cycle-debt 语料中的无名材料化 fresh-layer PDEC/ColumnCRT。",
            "closed",
        ),
        gate(
            "FutureFreshPDECSchemaNotSubmitted",
            not future_fresh_pdec_submitted,
            True,
            "未来 fresh-layer PDEC schema 尚未提交；它是准入纪律，不是当前已出现的数学障碍。",
            "future schema firewall",
        ),
        gate(
            "UnregisteredMovingFamilySchemaNotSubmitted",
            not unregistered_moving_family_schema_submitted,
            True,
            "未登记 moving family 没有提交完整 source/shape/phase/persistence schema；不能作为当前终端保留。",
            "future moving-family schema firewall",
        ),
        gate(
            "FuturePDECSchemaAdmissionDisciplineClosed",
            future_pdec_discipline_closed and pdec_boundary_closed,
            True,
            "未来 PDEC family 若新增，必须通过显式 primitive same-formal-unit schema 边界。",
            "reopen only with explicit schema",
        ),
        gate(
            "FutureSparseMovingPacketDisciplineClosed",
            future_sparse_discipline_closed and sparse_boundary_closed,
            True,
            "未来 sparse/local-survivor 型 moving packet 若新增，必须提交有限 packet extractor schema。",
            "reopen only with explicit extractor",
        ),
        gate(
            "NoHiddenTerminalBoundaryImported",
            final_firewall_closed and no_hidden_terminal,
            True,
            "最终输入防火墙已说明当前语料无隐藏终端；未来输入只能按命名 schema 重开。",
            "global final inputs remain",
        ),
        gate(
            "CycleDebtBranchReplayCurrentFrontierZero",
            current_materialized_frontier_zero,
            True,
            "在当前已物化 cycle-debt branch-replay 语料内，PDEC/ColumnCRT/future-schema/moving-family 均无活动终端实例。",
            "closed for current materialized branch-replay corpus",
        ),
        gate(
            "FutureSchemaMayReopen",
            False,
            False,
            "本步不证明未来 primitive fresh-layer PDEC schema 或 moving-family schema 永不存在。",
            "FutureExplicitPrimitivePDECSchema or FutureExplicitMovingFamilySchema if submitted",
        ),
        gate(
            "GlobalFinalInputsStillOpen",
            False,
            False,
            "行/列命题仍受全局最终输入约束，尤其 noncanonical 合法闭合模式与 DStructure/Rankin 晋级门。",
            "NoncanonicalFullSComplementLegalClosureMode and DStructureRankinPromotion",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只清零当前 cycle-debt branch-replay 物化前沿，不关闭完整行/列无条件定理。",
            NEXT_TARGET,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_cycle_debt_branch_replay_current_frontier_zero_router",
        "status": "cycle_debt_branch_replay_current_materialized_frontier_zero_future_schema_firewall_global_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_TARGET,
        "current_fresh_layer_pdec_frontier_closed": current_fresh_pdec_closed,
        "future_explicit_primitive_fresh_layer_pdec_schema_submitted": future_fresh_pdec_submitted,
        "unregistered_moving_family_schema_submitted": unregistered_moving_family_schema_submitted,
        "future_pdec_schema_admission_discipline_closed": future_pdec_discipline_closed,
        "future_sparse_schema_admission_discipline_closed": future_sparse_discipline_closed,
        "pdec_family_explicit_input_boundary_closed": pdec_boundary_closed,
        "future_sparse_packet_schema_boundary_closed": sparse_boundary_closed,
        "final_input_firewall_boundary_closed": final_firewall_closed,
        "no_hidden_terminal_remaining": no_hidden_terminal,
        "future_schema_firewall_closed_for_current_branch_replay": future_schema_firewall_closed,
        "cycle_debt_branch_replay_current_materialized_frontier_zero": current_materialized_frontier_zero,
        "future_explicit_schema_global_nonexistence_proved": False,
        "unregistered_moving_family_excluded": unregistered_moving_family_excluded,
        "row_column_unconditional_closed": False,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "future_moving_family_schema_required": [
            "source_family_id 与 formal_unit_id",
            "blocker_package、shape_key、phase_map 与去重规则",
            "支撑窗口、candidate set 与 exact bad-window count function",
            "同签名持久性测试；若持久则回流 PDEC/ColumnCRT",
            "签名漂移测试；若漂移则回流 SAE/CleanKLS/DLS 或 noncanonical final input",
            "可复现实验或证明账本、哈希与 open_obligation_count=0",
        ],
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "cycle-debt branch-replay 的当前物化前沿已清零：fresh-layer PDEC/ColumnCRT 当前实例已关闭，"
            "FutureExplicitPrimitiveFreshLayerPDECSchema 与 unregistered moving family 均未提交具体 schema，"
            "只能作为未来准入纪律保留。该结论不证明未来 schema 永不存在，也不关闭行/列全局无条件定理；"
            "全局仍需处理最终输入防火墙后的 noncanonical 与 DStructure/Rankin 门。"
        ),
        "dependency_hashes": {
            str(FRESH_PDEC_FIREWALL.relative_to(ROOT)): sha256(FRESH_PDEC_FIREWALL),
            str(FINAL_FIREWALL.relative_to(ROOT)): sha256(FINAL_FIREWALL),
            str(LEAF_FIREWALL.relative_to(ROOT)): sha256(LEAF_FIREWALL),
            str(PDEC_BOUNDARY.relative_to(ROOT)): sha256(PDEC_BOUNDARY),
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
        "# Prime Matrix cycle-debt branch-replay current frontier zero router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        "current_fresh_layer_pdec_frontier_closed="
        f"{fmt_bool(result['current_fresh_layer_pdec_frontier_closed'])}",
        "future_explicit_primitive_fresh_layer_pdec_schema_submitted="
        f"{fmt_bool(result['future_explicit_primitive_fresh_layer_pdec_schema_submitted'])}",
        "unregistered_moving_family_schema_submitted="
        f"{fmt_bool(result['unregistered_moving_family_schema_submitted'])}",
        "future_pdec_schema_admission_discipline_closed="
        f"{fmt_bool(result['future_pdec_schema_admission_discipline_closed'])}",
        "future_sparse_schema_admission_discipline_closed="
        f"{fmt_bool(result['future_sparse_schema_admission_discipline_closed'])}",
        f"final_input_firewall_boundary_closed={fmt_bool(result['final_input_firewall_boundary_closed'])}",
        f"no_hidden_terminal_remaining={fmt_bool(result['no_hidden_terminal_remaining'])}",
        "cycle_debt_branch_replay_current_materialized_frontier_zero="
        f"{fmt_bool(result['cycle_debt_branch_replay_current_materialized_frontier_zero'])}",
        "future_explicit_schema_global_nonexistence_proved="
        f"{fmt_bool(result['future_explicit_schema_global_nonexistence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 当前实例与未来准入",
        "",
        "`FutureExplicitPrimitiveFreshLayerPDECSchemaIfNew` 不是当前已出现的反例对象；它是未来新增 PDEC family 的准入纪律。同理，未登记 moving family 若没有提交 source、shape、phase 与 persistence schema，也不能作为当前终端保留。",
        "",
        "因此在当前 cycle-debt branch-replay 语料内，活动终端实例已经清零；未来若新增对象，只能按显式 schema 重开审查。",
        "",
        "## 2. moving-family 未来 schema 字段",
        "",
    ]
    for item in result["future_moving_family_schema_required"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 剩余接口",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书不关闭全局行/列命题；它只说明 cycle-debt branch-replay 的当前物化前沿不再含活动终端实例。",
            "",
            "## 5. 依赖哈希",
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
        "cycle_debt_branch_replay_current_materialized_frontier_zero": result[
            "cycle_debt_branch_replay_current_materialized_frontier_zero"
        ],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
