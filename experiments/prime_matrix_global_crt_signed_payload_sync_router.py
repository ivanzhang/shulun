#!/usr/bin/env python3
"""生成 global CRT 到 signed payload 前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_global_crt_signed_payload_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json

输出：
  data/prime-matrix-global-crt-signed-payload-sync-ledger.json
  docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json
  docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-global-crt-signed-payload-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-global-crt-signed-payload-sync-router.json"
OUT_MD = DOCS / "prime-matrix-global-crt-signed-payload-sync-router.md"

GLOBAL_BRANCH_TRACE = "prime-matrix-global-crt-branch-trace-frontier-router.json"
ATOMIC_PAYLOAD = "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"
PDEC_SCOPE = "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
DIRECT_PDEC = "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"

PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"

SOURCE_FILES = [
    GLOBAL_BRANCH_TRACE,
    ATOMIC_PAYLOAD,
    PDEC_SCOPE,
    DIRECT_PDEC,
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能视为证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def sync_chain() -> list[dict[str, str]]:
    """列出从 global CRT branch trace 到 signed payload 的同步链。"""
    return [
        {
            "from": "global CRT branch trace frontier",
            "to": f"{PDEC_SCOPE_ATOM} OR {BRANCH_TRACE}",
        },
        {
            "from": BRANCH_TRACE,
            "to": SIGNED_PAYLOAD,
        },
        {
            "from": "internal PDEC same-set arm",
            "to": NEW_JOINT,
        },
        {
            "from": NEW_JOINT,
            "to": f"{BRANCH_TRACE} then {SIGNED_PAYLOAD}",
        },
        {
            "from": "external/new PDEC scope certificate",
            "to": "retained as independent unproved input",
        },
    ]


def build_rows(
    global_latest: dict[str, Any],
    payload: dict[str, Any],
    pdec_scope: dict[str, Any],
    direct_pdec: dict[str, Any],
) -> list[dict[str, Any]]:
    """把当前 global CRT 活动基同步到 signed payload 层。"""
    global_basis_imported = (
        global_latest.get("next_direct_attack_target") == f"{PDEC_SCOPE_ATOM}_OR_{BRANCH_TRACE}"
        and global_latest.get("row_column_unconditional_closed") is False
    )
    payload_reduction_imported = (
        payload.get("target_input_before_router") == BRANCH_TRACE
        and payload.get("next_direct_attack_target") == SIGNED_PAYLOAD
        and payload.get("atomic_trace_payload_frontier_router_closed") is True
    )
    pdec_internal_saturated = (
        pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
        and pdec_scope.get("next_direct_attack_target") == NEW_JOINT
        and pdec_scope.get("pdec_scope_proved") is False
    )
    direct_scope_open = (
        direct_pdec.get("acyclic_same_set_scope_match_proved") is False
        and direct_pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is False
    )

    return [
        row(
            "GlobalCRTBranchTraceBasisImported",
            global_basis_imported,
            False,
            "上一层已把 global CRT/Q1-Q2 路线压成 PDEC scope 或 exact atomic branch trace。",
            f"{PDEC_SCOPE_ATOM} OR {BRANCH_TRACE}",
        ),
        row(
            "ExactAtomicTraceReducedToSignedPayload",
            payload_reduction_imported,
            False,
            "branch trace 一侧已被 strict payload 前沿压到 pre-assignment signed payload constructor。",
            SIGNED_PAYLOAD,
        ),
        row(
            "FiniteCRTCannotGenerateSignedPayload",
            True,
            True,
            "CRT 周期扩张只复制零同余类和可见坐标 trace；orientation、local factor 和 signed coefficient 不是纯位置相位数据。",
            SIGNED_PAYLOAD,
        ),
        row(
            "PDECInternalArmSaturatedToNewJoint",
            pdec_internal_saturated,
            False,
            "PDEC same-set 手臂在当前内部语料中已饱和；若不提交新 scope 证书，它回到新 joint 公式线。",
            NEW_JOINT,
        ),
        row(
            "InternalNewJointLineAlsoReturnsToPayload",
            global_basis_imported and payload_reduction_imported and pdec_internal_saturated,
            False,
            "内部自足线中，PDEC 饱和后的新 joint 公式已经经 branch-trace 链压到 signed payload。",
            SIGNED_PAYLOAD,
        ),
        row(
            "ExternalOrNewPDECScopeStillOpen",
            direct_scope_open,
            False,
            "新 acyclic same-set scope 证书或外部 DI/BFI 无投影窗口证书仍可作为独立输入，但当前未证。",
            f"{PDEC_SCOPE_ATOM} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "StrictInternalSelfContainedBasisSharpened",
            global_basis_imported and payload_reduction_imported and pdec_internal_saturated,
            False,
            "若不引入新的外部/scope PDEC 输入，global CRT 路线的内部自足硬点已经只剩 signed payload。",
            f"{SIGNED_PAYLOAD} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
        row(
            "ActualEmitterExactUVStillParallel",
            payload.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "payload 可登记 exact UV/key，但 bounded multiplicity incidence 仍是并行未证门。",
            EXACT_UV,
        ),
        row(
            "AtomicSignedPayloadConstructorCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出不经 assignment/origin 环的 atomic signed payload 正向构造公式。",
            SIGNED_PAYLOAD,
        ),
        row(
            "GlobalStructuralCRTContradictionCurrentCorpusFound",
            False,
            False,
            "本步识别了 CRT 坐标层与 signed payload 层的结构断点，但尚未从中推出终端矛盾。",
            f"{SIGNED_PAYLOAD} OR new {PDEC_SCOPE_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少 signed payload 或新 PDEC scope 证书，同时 ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍未合取闭合。",
            f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 global CRT signed payload 同步证书。"""
    global_latest = load_json(GLOBAL_BRANCH_TRACE)
    payload = load_json(ATOMIC_PAYLOAD)
    pdec_scope = load_json(PDEC_SCOPE)
    direct_pdec = load_json(DIRECT_PDEC)
    rows = build_rows(global_latest, payload, pdec_scope, direct_pdec)

    strict_internal_basis = (
        f"{SIGNED_PAYLOAD} AND {EXACT_UV} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    scope_retained_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD}) AND {EXACT_UV} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    external_basis = (
        f"({PDEC_SCOPE_ATOM} OR {EXTERNAL_DIBFI} OR {SIGNED_PAYLOAD}) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    global_basis_imported = rows[0]["closed"]
    payload_reduction_imported = rows[1]["closed"]
    pdec_internal_saturated = rows[3]["closed"]

    return {
        "certificate_type": "prime_matrix_global_crt_signed_payload_sync_router",
        "status": "global_crt_internal_route_reduced_to_signed_payload_with_external_pdec_retained",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "global_crt_branch_trace_basis_imported": global_basis_imported,
        "exact_atomic_trace_reduced_to_signed_payload": payload_reduction_imported,
        "finite_crt_cannot_generate_signed_payload": True,
        "pdec_internal_arm_saturated_to_new_joint": pdec_internal_saturated,
        "external_or_new_pdec_scope_still_open": rows[5]["closed"],
        "strict_internal_self_contained_basis_sharpened": rows[6]["closed"],
        "atomic_signed_payload_constructor_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": f"({PDEC_SCOPE_ATOM} OR {BRANCH_TRACE}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        "strict_internal_basis_after_router": strict_internal_basis,
        "scope_retained_basis_after_router": scope_retained_basis,
        "external_or_new_scope_basis_after_router": external_basis,
        "next_direct_attack_target": SIGNED_PAYLOAD,
        "next_scope_attack_target": PDEC_SCOPE_ATOM,
        "latest_strict_activity_basis": scope_retained_basis,
        "sync_chain": sync_chain(),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步把 global CRT/Q1-Q2 最新前沿继续同步到 signed payload 层。"
            "`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` 已由 strict payload 前沿压成 "
            "`AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`。同时，PDEC same-set 手臂在当前内部"
            "自足语料中已饱和到新 joint 公式线，而该线也已回到 branch-trace/payload。"
            "因此，在不引入新的外部或 scope-PDEC 证书时，内部自足路线的最新最窄硬点是 signed payload。"
            "但新 acyclic same-set scope 证书和外部 DI/BFI 输入仍保留为独立未证入口；ExactUV、模型余量、"
            "RatePreservation 与 DStructure/Rankin 也仍需合取闭合。行/列命题尚未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix global CRT signed payload 同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"global_crt_branch_trace_basis_imported={fmt_bool(result['global_crt_branch_trace_basis_imported'])}",
        f"exact_atomic_trace_reduced_to_signed_payload={fmt_bool(result['exact_atomic_trace_reduced_to_signed_payload'])}",
        f"finite_crt_cannot_generate_signed_payload={fmt_bool(result['finite_crt_cannot_generate_signed_payload'])}",
        f"pdec_internal_arm_saturated_to_new_joint={fmt_bool(result['pdec_internal_arm_saturated_to_new_joint'])}",
        f"external_or_new_pdec_scope_still_open={fmt_bool(result['external_or_new_pdec_scope_still_open'])}",
        f"strict_internal_self_contained_basis_sharpened={fmt_bool(result['strict_internal_self_contained_basis_sharpened'])}",
        f"atomic_signed_payload_constructor_proved={fmt_bool(result['atomic_signed_payload_constructor_proved'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` |")

    lines += [
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 3. 活动基",
        "",
        "内部自足线：",
        "",
        "```text",
        result["strict_internal_basis_after_router"],
        "```",
        "",
        "保留新 scope/PDEC 输入的总活动基：",
        "",
        "```text",
        result["scope_retained_basis_after_router"],
        "```",
        "",
        "外部/新 scope 扩展口径：",
        "",
        "```text",
        result["external_or_new_scope_basis_after_router"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "审稿边界：本文件只完成 global CRT 最新前沿与 signed payload 前沿的同步；",
        "它没有证明 signed payload constructor、PDEC scope、ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    if result["missing_sources"]:
        lines += [
            "",
            "缺失依赖：",
            "",
        ]
        for name in result["missing_sources"]:
            lines.append(f"- `{name}`")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出同步证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "strict_internal_basis_after_router": result["strict_internal_basis_after_router"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
