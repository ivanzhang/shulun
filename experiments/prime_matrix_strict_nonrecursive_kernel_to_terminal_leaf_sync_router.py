#!/usr/bin/env python3
"""生成 strict 非递归核表到终端叶子前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_nonrecursive_kernel_to_terminal_leaf_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.md"

FIELD_TARGET = "NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn"
JOINT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
JOINT_ALPHA = "JointAlphaSidePrimitiveWordCoefficientRuleLedger"
SAME_ROW = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json",
    "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json",
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json",
    "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记引用证据哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def route_chain() -> list[dict[str, str]]:
    """展示从非递归核表到当前终端叶子的同步链。"""
    return [
        {"from": FIELD_TARGET, "to": JOINT_RULE},
        {"from": JOINT_RULE, "to": JOINT_ALPHA},
        {"from": JOINT_ALPHA, "to": SAME_ROW},
        {"from": SAME_ROW, "to": ROW_TABLE},
        {"from": ROW_TABLE, "to": "signed-source fixed point"},
        {"from": "signed-source fixed point", "to": TERMINAL_DESCENT},
        {"from": TERMINAL_DESCENT, "to": "TerminalLeafFirewallInputs_OR_CanonicalLock"},
        {"from": "TerminalLeafFirewallInputs_OR_CanonicalLock", "to": f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}"},
    ]


def build_result() -> dict[str, Any]:
    """同步非递归核表缺口与已知终端叶子前沿。"""
    field = load_json("prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json")
    joint_rule = load_json("prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json")
    joint_alpha = load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json")
    same_row = load_json("prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json")
    fixed_point = load_json("prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json")
    descent = load_json("prime-matrix-strict-acyclic-terminal-descent-firewall-router.json")
    leaf = load_json("prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json")
    legal = load_json("prime-matrix-strict-noncanonical-legal-closure-mode-router.json")
    uv_rank = load_json("prime-matrix-strict-exact-uv-map-rank-incidence-router.json")
    dstructure = load_json("prime-matrix-dstructure-rankin-promotion-acceptance-router.json")

    field_imported = (
        field.get("field_contract_boundary_closed") is True
        and field.get("next_direct_attack_target") == JOINT_RULE
    )
    joint_rule_to_alpha = (
        joint_rule.get("joint_explicit_alpha_delta_rule_sync_router_closed") is True
        and joint_rule.get("next_direct_attack_target") == JOINT_ALPHA
        and joint_rule.get("explicit_joint_alpha_delta_constructor_rule_proved") is False
    )
    alpha_to_same_row = (
        joint_alpha.get("joint_alpha_side_word_coefficient_rule_router_closed") is True
        and joint_alpha.get("next_direct_attack_target") == SAME_ROW
        and joint_alpha.get("joint_alpha_side_primitive_word_coefficient_rule_proved") is False
    )
    same_row_to_row_table = (
        same_row.get("joint_alpha_same_row_origin_identity_router_closed") is True
        and same_row.get("next_direct_attack_target") == ROW_TABLE
        and same_row.get("joint_alpha_same_row_word_coefficient_origin_identity_proved") is False
    )
    fixed_point_to_terminal = (
        fixed_point.get("joint_alpha_signed_source_fixed_point_sync_router_closed") is True
        and fixed_point.get("cycle_cut_joint_route_returns_to_row_level_fixed_point") is True
        and fixed_point.get("next_direct_attack_target") == TERMINAL_DESCENT
    )
    descent_schema_to_leaf = (
        descent.get("terminal_return_well_founded_descent_schema_closed") is True
        and descent.get("acyclic_terminal_return_well_founded_descent_proved") is False
    )
    leaf_to_current_terminal = (
        leaf.get("current_leaf_firewall_active_basis_reduced") is True
        and leaf.get("terminal_gap_after_current_instance_router") == f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}"
    )
    noncanonical_open = (
        legal.get("noncanonical_legal_closure_mode_proved") is False
        and legal.get("actual_source_bridge_theorem_closed") is False
    )
    uv_open = (
        uv_rank.get("exact_uv_map_rank_incidence_router_closed") is True
        and uv_rank.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    sync_closed = all(
        [
            field_imported,
            joint_rule_to_alpha,
            alpha_to_same_row,
            same_row_to_row_table,
            fixed_point_to_terminal,
            descent_schema_to_leaf,
            leaf_to_current_terminal,
            noncanonical_open,
            uv_open,
            dstructure_open,
        ]
    )

    rows = [
        row(
            "NonrecursiveFieldContractImported",
            field_imported,
            True,
            "非递归逐点核表字段边界已闭合，第一生产性原子钉为 joint constructor rule。",
            JOINT_RULE,
        ),
        row(
            "JointConstructorRouteReducesToAlphaSide",
            joint_rule_to_alpha,
            False,
            "显式 joint alpha/delta rule 继续压成 joint alpha-side word/coefficient rule，未给公式。",
            JOINT_ALPHA,
        ),
        row(
            "JointAlphaSideReducesToSameRow",
            alpha_to_same_row,
            False,
            "joint alpha-side 的硬点是 unsigned word skeleton 与 signed coefficient 同行同源。",
            SAME_ROW,
        ),
        row(
            "SameRowBridgeReturnsToRowLevelTable",
            same_row_to_row_table,
            False,
            "same-row 桥接回收到逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "JointRouteHitsSignedSourceFixedPoint",
            fixed_point_to_terminal,
            True,
            "joint-alpha/cycle-cut 线已证明会回到 signed-source 固定点，不能作为非循环证明。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalDescentSchemaClosedLeafOpen",
            descent_schema_to_leaf,
            False,
            "终端 well-founded 下降的无隐藏循环 schema 已闭合，但叶子防火墙未全排斥。",
            "TerminalLeafFirewallInputs_OR_CanonicalLock",
        ),
        row(
            "CurrentLeafFirewallReduced",
            leaf_to_current_terminal,
            False,
            "当前已物化 PDEC/sparse 前沿清零后，活动终端剩 canonical-lock 或 noncanonical legal mode。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        row(
            "NoncanonicalLegalModeStillOpen",
            noncanonical_open,
            False,
            "noncanonical full-S 合法模式仍需实际源恒等、强化反原子或外部合同；strict 自足线未闭合。",
            NONCANONICAL_MODE,
        ),
        row(
            "ExactUVIncidenceStillParallel",
            uv_open,
            False,
            "非递归核表的 rank/multiplicity 口径仍需 actual exact-UV bounded multiplicity incidence。",
            UV_INCIDENCE,
        ),
        row(
            "RatePreservationStillOpen",
            False,
            False,
            "moving-atom packet 的 log-power 速率保持仍未由当前同步证明。",
            RATE,
        ),
        row(
            "DStructureGateStillOpen",
            dstructure_open,
            False,
            "DStructure/Rankin 晋级门仍只完成边界命名，未独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前同步只删除 joint constructor 伪出口并定位终端二选一，尚未得到反例矛盾。",
            f"({CANONICAL_LOCK} OR {NONCANONICAL_MODE}) AND {UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]

    strict_active_basis = (
        f"({CANONICAL_LOCK} OR {NONCANONICAL_MODE}) AND {UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_nonrecursive_kernel_to_terminal_leaf_sync_router",
        "status": "nonrecursive_kernel_joint_route_synced_to_terminal_leaf_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "sync_closed": sync_closed,
        "field_contract_boundary_closed": field.get("field_contract_boundary_closed") is True,
        "joint_constructor_path_is_fixed_point_without_new_formula": fixed_point_to_terminal,
        "terminal_descent_schema_closed": descent.get("terminal_return_well_founded_descent_schema_closed") is True,
        "current_leaf_firewall_active_basis_reduced": leaf_to_current_terminal,
        "noncanonical_legal_closure_mode_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        "strict_active_basis_after_sync": strict_active_basis,
        "route_chain": route_chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{FIELD_TARGET}` 的第一生产性原子 `{JOINT_RULE}` 已由既有 joint-alpha 链同步到 signed-source 固定点；"
            "除非提交新的 actual joint constructor 公式工件，否则该正向构造线不能闭合。"
            f"因此当前内部自足硬点回到终端叶子前沿：`{CANONICAL_LOCK} OR {NONCANONICAL_MODE}`，"
            f"同时保留 `{UV_INCIDENCE}`、`{RATE}` 与 `{DSTRUCTURE}` 并行验收。"
        ),
        "plain_conclusion": (
            "本步把新非递归核表合同与旧 joint-alpha 固定点、终端叶子防火墙接通。结论是："
            "刚钉出的 joint constructor rule 若没有新的显式公式，只会沿 joint alpha-side/same-row/row-level 表回到 signed-source 固定点。"
            "终端下降 schema 已去掉无名自循环，但当前活动叶子仍是 canonical-lock 或 noncanonical full-S 合法模式；"
            "二者均未证明，所以行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 非递归核表到终端叶子同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sync_closed={fmt_bool(result['sync_closed'])}",
        f"field_contract_boundary_closed={fmt_bool(result['field_contract_boundary_closed'])}",
        f"joint_constructor_path_is_fixed_point_without_new_formula={fmt_bool(result['joint_constructor_path_is_fixed_point_without_new_formula'])}",
        f"terminal_descent_schema_closed={fmt_bool(result['terminal_descent_schema_closed'])}",
        f"current_leaf_firewall_active_basis_reduced={fmt_bool(result['current_leaf_firewall_active_basis_reduced'])}",
        f"noncanonical_legal_closure_mode_proved={fmt_bool(result['noncanonical_legal_closure_mode_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿同步",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 同步链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["route_chain"]:
        lines.append(
            "| {from_} | {to} |".format(
                from_=table_cell(item["from"]),
                to=table_cell(item["to"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 当前严格活动基",
            "",
            "```text",
            result["strict_active_basis_after_sync"],
            "```",
            "",
            "下一主攻点：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
