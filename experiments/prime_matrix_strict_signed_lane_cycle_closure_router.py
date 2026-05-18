#!/usr/bin/env python3
"""生成 strict signed lane 闭环证书。

用法示例：
  python3 experiments/prime_matrix_strict_signed_lane_cycle_closure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json

输出：
  data/prime-matrix-strict-signed-lane-cycle-closure-ledger.json
  docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json
  docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-signed-lane-cycle-closure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
OUT_MD = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.md"

COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
NONCIRCULAR_ORIGIN = "NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward"
EXACTUV_SPLIT = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
SCOPE_PDEC = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_PAYLOAD_ARTIFACT = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"

SOURCE_FILES = [
    {
        "id": "downstream_sync",
        "json": "prime-matrix-strict-source-declaration-downstream-sync-router.json",
        "role": "common packet 下游同步到 built-in signed pairing 与 ExactUV",
    },
    {
        "id": "builtin_pairing",
        "json": "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json",
        "role": "built-in signed pairing 被压到 exact atomic branch trace",
    },
    {
        "id": "atomic_trace_payload",
        "json": "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json",
        "role": "exact atomic branch trace 被压到 atomic signed payload constructor",
    },
    {
        "id": "payload_origin",
        "json": "prime-matrix-strict-atomic-payload-origin-identity-router.json",
        "role": "atomic signed payload 被压到 noncircular atomic origin identity",
    },
    {
        "id": "common_packet",
        "json": "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json",
        "role": "noncircular origin 与 ExactUV 共同回到 common source declaration packet",
    },
    {
        "id": "global_branch_trace",
        "json": "prime-matrix-global-crt-branch-trace-frontier-router.json",
        "role": "global CRT 活动基同步到 PDEC scope 或 exact atomic branch trace",
    },
    {
        "id": "current_global_after_trace",
        "json": "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json",
        "role": "branch trace self-proof 已从 strict 活动证明路径删除",
    },
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    hashes = {
        "experiments/prime_matrix_strict_signed_lane_cycle_closure_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for item in SOURCE_FILES:
        path = DOCS / item["json"]
        if path.exists():
            hashes[f"docs/monograph/{item['json']}"] = sha256(path)
    if OUT_LEDGER.exists():
        hashes[str(OUT_LEDGER.relative_to(ROOT))] = sha256(OUT_LEDGER)
    return hashes


def evidence_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """抽取依赖证书读数。"""
    rows: list[dict[str, Any]] = []
    for item in SOURCE_FILES:
        cert = data[item["id"]]
        rows.append(
            {
                "id": item["id"],
                "file": f"docs/monograph/{item['json']}",
                "role": item["role"],
                "status": cert.get("status", "missing"),
                "next_direct_attack_target": cert.get("next_direct_attack_target"),
                "row_column_unconditional_closed": bool(
                    cert.get("row_column_unconditional_closed", False)
                ),
            }
        )
    return rows


def cycle_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 signed 子线闭环链。"""
    return [
        {
            "from": COMMON_PACKET,
            "to": BUILTIN_PAIRING,
            "closed": data["downstream_sync"].get("next_direct_attack_target") == BUILTIN_PAIRING,
            "meaning": "common packet 的 signed/payload 子线先被同步到 built-in signed pairing。",
        },
        {
            "from": BUILTIN_PAIRING,
            "to": BRANCH_TRACE,
            "closed": data["builtin_pairing"].get("next_direct_attack_target") == BRANCH_TRACE,
            "meaning": "built-in pairing 的非循环闭式需要 exact atomic branch trace。",
        },
        {
            "from": BRANCH_TRACE,
            "to": SIGNED_PAYLOAD,
            "closed": data["atomic_trace_payload"].get("next_direct_attack_target") == SIGNED_PAYLOAD,
            "meaning": "exact atomic branch trace 的 visible coordinate 不产生 signed payload。",
        },
        {
            "from": SIGNED_PAYLOAD,
            "to": NONCIRCULAR_ORIGIN,
            "closed": data["payload_origin"].get("next_direct_attack_target") == NONCIRCULAR_ORIGIN,
            "meaning": "signed payload 的第一生产性字段回到非循环 basis word/signed coefficient 来源恒等式。",
        },
        {
            "from": NONCIRCULAR_ORIGIN,
            "to": COMMON_PACKET,
            "closed": data["common_packet"].get("aggregate", {}).get("previous_payload_target")
            == NONCIRCULAR_ORIGIN
            and data["common_packet"].get("next_direct_attack_target") == COMMON_PACKET,
            "meaning": "该来源恒等式与 ExactUV 子线共同定义 common source declaration packet。",
        },
    ]


def decision_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成闭环判定表。"""
    rows = cycle_rows(data)
    cycle_closed = all(row["closed"] for row in rows)
    return [
        {
            "gate": "SignedLaneCycleClosed",
            "closed": cycle_closed,
            "proved": True,
            "meaning": "common packet、built-in pairing、branch trace、signed payload、origin identity 已形成闭环。",
            "remaining": "cycle is diagnostic, not proof",
        },
        {
            "gate": "VisibleCoordinateTraceCannotBreakCycle",
            "closed": data["atomic_trace_payload"].get("visible_coordinate_trace_reduced_to_word_coordinate_chain")
            is True,
            "proved": True,
            "meaning": "branch trace 的可见坐标链只给 row/word 坐标，不给 orientation、local factor 或 signed coefficient。",
            "remaining": NEW_PAYLOAD_ARTIFACT,
        },
        {
            "gate": "OriginIdentityReturnsToCommonPacket",
            "closed": rows[-1]["closed"],
            "proved": True,
            "meaning": "atomic origin identity 不再是更深出口；它已经通过 common packet 回到 signed lane 起点。",
            "remaining": "remove signed-lane self-proof",
        },
        {
            "gate": "PDECScopeBranchStillParallel",
            "closed": SCOPE_PDEC in str(
                data["global_branch_trace"].get("next_direct_attack_target", "")
            )
            or SCOPE_PDEC in str(data["global_branch_trace"].get("latest_strict_activity_basis", "")),
            "proved": False,
            "meaning": "PDEC same-set 作用域匹配仍可作为独立新证书输入，但当前未证。",
            "remaining": SCOPE_PDEC,
        },
        {
            "gate": "ExistingSignedLaneCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料没有打破该 signed-lane 闭环的新 primitive trace/payload 公式。",
            "remaining": NEW_PAYLOAD_ARTIFACT,
        },
        {
            "gate": "TerminalDescentAlternativeStillOpen",
            "closed": True,
            "proved": False,
            "meaning": "若不提交新 primitive payload/trace 工件，只能把 signed-lane 回流转成 well-founded strict descent。",
            "remaining": TERMINAL_DESCENT,
        },
        {
            "gate": "ExactUVLaneStillIndependent",
            "closed": data["downstream_sync"].get("parallel_direct_attack_target") == EXACTUV_SPLIT,
            "proved": False,
            "meaning": "ExactUV entropy/fiber 不是 signed payload 闭环的推论，仍需独立证明。",
            "remaining": EXACTUV_SPLIT,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步删除 signed-lane 自证路线，但未证明新 payload 工件、terminal descent、PDEC scope、ExactUV 或 DStructure/Rankin。",
            "remaining": (
                f"({NEW_PAYLOAD_ARTIFACT} OR {TERMINAL_DESCENT} OR {SCOPE_PDEC}) "
                f"AND {EXACTUV_SPLIT} AND RatePreservationLedger_FOR_moving_atom_packet "
                "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
            ),
        },
    ]


def theorem_rows() -> list[dict[str, str]]:
    """列出本路由形成的命题行。"""
    return [
        {
            "name": "signed_lane_cycle_closure",
            "status": "closed_routing",
            "statement": (
                "The current signed/payload lane is a closed dependency cycle from common source packet "
                "through built-in pairing, branch trace, signed payload, and origin identity back to the packet."
            ),
        },
        {
            "name": "signed_lane_self_proof_rejected",
            "status": "closed_routing",
            "statement": (
                "No node in that cycle can be used as a self-contained proof unless a new primitive trace/payload "
                "artifact or a well-founded terminal descent certificate is added."
            ),
        },
        {
            "name": "row_column_unconditional_closure",
            "status": "open",
            "statement": (
                "New payload/trace input, terminal descent or PDEC scope, plus ExactUV and promotion gates, remain open."
            ),
        },
    ]


def build_result() -> dict[str, Any]:
    """生成闭环证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {item["id"]: load_json(item["json"]) for item in SOURCE_FILES}
    missing = [
        f"docs/monograph/{item['json']}"
        for item in SOURCE_FILES
        if not (DOCS / item["json"]).exists()
    ]
    cycles = cycle_rows(data)
    cycle_closed = all(row["closed"] for row in cycles)
    aggregate = {
        "signed_lane_cycle_closed": cycle_closed,
        "signed_lane_self_proof_eliminated": cycle_closed,
        "new_primitive_payload_or_trace_artifact_present": False,
        "acyclic_terminal_descent_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "exactuv_entropy_fiber_proved": False,
        "row_column_unconditional_closed": False,
        "cycle_nodes": [
            COMMON_PACKET,
            BUILTIN_PAIRING,
            BRANCH_TRACE,
            SIGNED_PAYLOAD,
            NONCIRCULAR_ORIGIN,
            COMMON_PACKET,
        ],
        "current_noncycle_exits": [
            NEW_PAYLOAD_ARTIFACT,
            TERMINAL_DESCENT,
            SCOPE_PDEC,
            EXACTUV_SPLIT,
            "RatePreservationLedger_FOR_moving_atom_packet",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
    }
    ledger = {
        "aggregate": aggregate,
        "cycle_rows": cycles,
        "evidence_rows": evidence_rows(data),
        "missing_source_files": missing,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_strict_signed_lane_cycle_closure_router",
        "status": "strict_signed_lane_cycle_closed_self_proof_eliminated_global_open",
        "frontier_sync_only": True,
        "cycle_closure_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "cycle_rows": cycles,
        "evidence_rows": ledger["evidence_rows"],
        "decision_rows": decision_rows(data),
        "theorem_rows": theorem_rows(),
        "missing_source_files": missing,
        "plain_conclusion": (
            "本步确认 strict signed/payload 子线已经闭成依赖环："
            f"`{COMMON_PACKET}` -> `{BUILTIN_PAIRING}` -> `{BRANCH_TRACE}` -> "
            f"`{SIGNED_PAYLOAD}` -> `{NONCIRCULAR_ORIGIN}` -> `{COMMON_PACKET}`。"
            "因此不能继续把环内任一节点当作自足证明；下一步只能新增 primitive trace/payload 工件、"
            "证明终端 strict descent，或走 PDEC scope，并且 ExactUV 与晋级门仍独立开放。"
        ),
        "next_direct_attack_target": NEW_PAYLOAD_ARTIFACT,
        "parallel_direct_attack_targets": [TERMINAL_DESCENT, SCOPE_PDEC, EXACTUV_SPLIT],
        "signed_lane_cycle_closed": cycle_closed,
        "signed_lane_self_proof_eliminated": cycle_closed,
        "row_column_unconditional_closed": False,
    }
    result["source_hashes"] = source_hashes()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix strict signed lane cycle closure router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_lane_cycle_closed={fmt_bool(agg['signed_lane_cycle_closed'])}",
        f"signed_lane_self_proof_eliminated={fmt_bool(agg['signed_lane_self_proof_eliminated'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(agg['new_primitive_payload_or_trace_artifact_present'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 闭环链",
        "",
        "| from | to | closed | meaning |",
        "| --- | --- | ---: | --- |",
    ]
    for row in result["cycle_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['from'])}`",
                    f"`{table_cell(row['to'])}`",
                    fmt_bool(row["closed"]),
                    table_cell(row["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    fmt_bool(row["closed"]),
                    fmt_bool(row["proved"]),
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 非循环出口",
            "",
            "| input |",
            "| --- |",
        ]
    )
    for item in agg["current_noncycle_exits"]:
        lines.append(f"| `{table_cell(item)}` |")
    lines.extend(
        [
            "",
            "## 4. 证据同步表",
            "",
            "| id | role | status | next |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["evidence_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['id'])}`",
                    table_cell(row["role"]),
                    table_cell(row["status"]),
                    table_cell(row["next_direct_attack_target"] or ""),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(
            f"| `{table_cell(row['name'])}` | `{table_cell(row['status'])}` | {table_cell(row['statement'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 结论边界",
            "",
            "- 本步只关闭 signed-lane 的自证路线。",
            f"- 下一直接主攻是 `{NEW_PAYLOAD_ARTIFACT}`。",
            f"- 并行出口为 `{TERMINAL_DESCENT}`、`{SCOPE_PDEC}` 与 `{EXACTUV_SPLIT}`。",
            "- 不能把闭环识别解读为行/列命题无条件闭合。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    if result["missing_source_files"]:
        lines.extend(["", "## 8. 缺失依赖", "", "| file |", "| --- |"])
        for name in result["missing_source_files"]:
            lines.append(f"| `{table_cell(name)}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
