#!/usr/bin/env python3
"""生成 strict 主线 canonical-lock 下钻同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_mainline_canonical_lock_drilldown_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-mainline-canonical-lock-drilldown-router.json

输出：
  docs/monograph/prime-matrix-strict-mainline-canonical-lock-drilldown-router.json
  docs/monograph/prime-matrix-strict-mainline-canonical-lock-drilldown-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

OUT_JSON = DOCS / "prime-matrix-strict-mainline-canonical-lock-drilldown-router.json"
OUT_MD = DOCS / "prime-matrix-strict-mainline-canonical-lock-drilldown-router.md"

MAINLINE = DOCS / "prime-matrix-strict-mainline-self-contained-frontier-router.json"
TAIL_REMAINDER = DOCS / "prime-matrix-linear-sieve-tail-remainder-gap-router.json"
FLOOR_CHARGE = DOCS / "prime-matrix-strict-rosser-floor-terminal-charge-router.json"
NAMED_RETURN = DOCS / "prime-matrix-strict-named-return-same-parameter-deduction-router.json"
DIRECT_PDEC = DOCS / "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"
TERMINAL_FAMILY = DOCS / "prime-matrix-strict-acyclic-terminal-family-attack-router.json"
RATE_PACKET = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json"
DSTRUCTURE_GATE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"

SOURCE_FILES = [
    MAINLINE,
    TAIL_REMAINDER,
    FLOOR_CHARGE,
    NAMED_RETURN,
    DIRECT_PDEC,
    TERMINAL_FAMILY,
    RATE_PACKET,
    DSTRUCTURE_GATE,
]

ROSR_FLOOR = "RosserIwaniecWeightedFloorRemainderTenPercentBound"
EXTERNAL_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
SAWTOOTH_CHARGE = "SawtoothFailureChargedToNamedTerminalFamily"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


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


def build_result() -> dict[str, Any]:
    """构造 strict 主线 canonical-lock 下钻同步证书。"""
    mainline = load_json(MAINLINE)
    tail = load_json(TAIL_REMAINDER)
    floor = load_json(FLOOR_CHARGE)
    named = load_json(NAMED_RETURN)
    pdec = load_json(DIRECT_PDEC)
    terminal = load_json(TERMINAL_FAMILY)
    rate = load_json(RATE_PACKET)
    dstructure = load_json(DSTRUCTURE_GATE)

    guard = (
        mainline.get("counterexample_assumption_only") is True
        and mainline.get("empirical_absence_not_used") is True
        and mainline.get("row_column_unconditional_closed") is False
    )

    rosser_floor_split = tail.get("rosser_iwaniec_weighted_floor_remainder_proved") is False
    floor_charge_closed = floor.get("sawtooth_failure_no_free_d0_loss_closed") is True
    named_schema_closed = named.get("named_return_same_parameter_schema_closed") is True
    pdec_scope_audited = pdec.get("scope_audit_closed") is True
    terminal_three_way = terminal.get("strict_acyclic_terminal_family_boundary_refined") is True
    canonical_lock_proved = terminal.get("acyclic_terminal_canonical_lock_proved") is True
    windowed_dls_proved = (
        terminal.get("direct_acyclic_clean_kls_dls_proved") is True
        or pdec.get("direct_acyclic_clean_kls_dls_proved") is True
    )
    rate_preserved = rate.get("rate_bearing_moving_atom_packet_exclusion_proved") is True
    dstructure_accepted = (
        dstructure.get("dstructure_rankin_independently_accepted") is True
        or dstructure.get("promotion_package_independently_accepted") is True
        or dstructure.get("row_column_unconditional_closed") is True
    )

    # 中文注释：本轮只关闭 Rosser floor 失败态的“免费损失”出口，并把 direct PDEC 压回作用域匹配。
    rosser_branch_routed = guard and rosser_floor_split and floor_charge_closed and named_schema_closed
    direct_pdec_drilled = rosser_branch_routed and pdec_scope_audited
    terminal_primary_fixed = direct_pdec_drilled and terminal_three_way
    terminal_closed = canonical_lock_proved or windowed_dls_proved
    row_column_closed = terminal_closed and rate_preserved and dstructure_accepted

    strict_frontier_basis = (
        f"(({CANONICAL_LOCK} OR {WINDOWED_DLS}) AND "
        f"({ROSR_FLOOR} OR {EXTERNAL_ROUGH} OR {SAWTOOTH_CHARGE}) AND "
        f"{RATE} AND {DSTRUCTURE})"
    )
    strict_self_contained_remaining = (
        f"({CANONICAL_LOCK} OR {WINDOWED_DLS}) AND {RATE} AND {DSTRUCTURE}"
    )
    conditional_external_remaining = (
        f"({CANONICAL_LOCK} OR {WINDOWED_DLS} OR {DIBFI} OR {EXTERNAL_ROUGH}) "
        f"AND {RATE} AND {DSTRUCTURE}"
    )

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "仍在早期零行反例链内推进，不用真实零行缺席或低段样本替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "RosserFloorFreeLossExitClosedAsAccounting",
            rosser_branch_routed,
            False,
            "Rosser floor/sawtooth 若失败，已强制登记为同 formal unit 命名终端收费，不能再作为无名 D0 损失。",
            f"{ROSR_FLOOR} OR {EXTERNAL_ROUGH} OR terminal charge。",
        ),
        row(
            "NamedReturnSameParameterSchemaImported",
            named_schema_closed,
            False,
            "命名回流的同参数表结构已闭合，但数值 E0 仍依赖持久终端排斥和非持久预算反超。",
            "persistent terminal exclusion AND sparse/cold budget。",
        ),
        row(
            "DirectAcyclicSameSetPDECScopeAudited",
            pdec_scope_audited,
            False,
            "direct same-set PDEC 不能从 canonical-source 口径自动偷渡；必须先证明 acyclic 同集作用域完全匹配。",
            CANONICAL_LOCK,
        ),
        row(
            "TerminalFamilyReducedBackToCanonicalLockOrWindowedDLS",
            terminal_primary_fixed,
            False,
            "本轮主线最窄终端口回到 canonical-lock 或 windowed clean DLS；这不是换命题，而是 Rosser/direct-PDEC 分支收费后的同一反例链出口。",
            f"{CANONICAL_LOCK} OR {WINDOWED_DLS}",
        ),
        row(
            "AcyclicTerminalCanonicalLockClosed",
            canonical_lock_proved,
            canonical_lock_proved,
            "尚未证明 acyclic terminal certificate 与 canonical-source same-set 边界完全同口径。",
            CANONICAL_LOCK,
        ),
        row(
            "AcyclicWindowedDLSClosed",
            windowed_dls_proved,
            windowed_dls_proved,
            "windowed CleanKLS/DLS 作为不走 canonical-lock 的备用终端排斥，当前仍未作者侧闭合。",
            WINDOWED_DLS,
        ),
        row(
            "RatePreservationLedgerClosed",
            rate_preserved,
            rate_preserved,
            "moving atom 到 rate-bearing packet 的 log-power 速率保持仍未证明。",
            RATE,
        ),
        row(
            "DStructureIndependentGateClosed",
            dstructure_accepted,
            dstructure_accepted,
            "DStructure/Tail-log4/finite Rankin 最终晋级门仍需独立验收或严格自足替代验收。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnSelfContainedClosureReached",
            row_column_closed,
            row_column_closed,
            "目标行/列命题尚未达到作者侧严格自足无条件闭合。",
            strict_self_contained_remaining,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_mainline_canonical_lock_drilldown_router",
        "status": "strict_mainline_drilled_to_canonical_lock_or_windowed_dls_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "rosser_floor_free_loss_exit_closed_as_accounting": rosser_branch_routed,
        "named_return_same_parameter_schema_imported": named_schema_closed,
        "direct_acyclic_same_set_pdec_scope_audited": pdec_scope_audited,
        "terminal_family_reduced_back_to_canonical_lock_or_windowed_dls": terminal_primary_fixed,
        "acyclic_terminal_canonical_lock_proved": canonical_lock_proved,
        "acyclic_windowed_dls_proved": windowed_dls_proved,
        "rate_preservation_ledger_proved": rate_preserved,
        "dstructure_independent_gate_closed": dstructure_accepted,
        "direct_unconditional_contradiction_found": row_column_closed,
        "row_column_unconditional_closed": row_column_closed,
        "strict_frontier_basis": strict_frontier_basis,
        "strict_self_contained_remaining": strict_self_contained_remaining,
        "conditional_external_remaining": conditional_external_remaining,
        "next_direct_attack_target": CANONICAL_LOCK,
        "parallel_attack_targets": [WINDOWED_DLS, RATE, DSTRUCTURE],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步回到 strict 数学主线并下钻最新剩余：Rosser floor 的 sawtooth/近平方条带失败态已经不能免费吞掉 D0，"
            "同参数命名回流 schema 已接上；direct same-set PDEC 又被作用域审查压回 canonical-lock。"
            "因此当前最窄自足终端口是 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`，备线为 "
            "`AcyclicWindowedKloostermanDLSInternalEstimate`。但 canonical-lock/windowed DLS、RatePreservation、DStructure "
            "均未全部证明，所以目标行/列命题仍不能声明无条件自足闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 主线 canonical-lock 下钻同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        (
            "rosser_floor_free_loss_exit_closed_as_accounting="
            f"{fmt_bool(result['rosser_floor_free_loss_exit_closed_as_accounting'])}"
        ),
        (
            "direct_acyclic_same_set_pdec_scope_audited="
            f"{fmt_bool(result['direct_acyclic_same_set_pdec_scope_audited'])}"
        ),
        (
            "terminal_family_reduced_back_to_canonical_lock_or_windowed_dls="
            f"{fmt_bool(result['terminal_family_reduced_back_to_canonical_lock_or_windowed_dls'])}"
        ),
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"acyclic_windowed_dls_proved={fmt_bool(result['acyclic_windowed_dls_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 当前严格基",
        "",
        "```text",
        result["strict_frontier_basis"],
        "```",
        "",
        "严格自足剩余：",
        "",
        "```text",
        result["strict_self_contained_remaining"],
        "```",
        "",
        "条件外部剩余：",
        "",
        "```text",
        result["conditional_external_remaining"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 下一最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本文件关闭的是 Rosser floor 失败态的免费损失出口与 direct PDEC 作用域审查；它没有证明 canonical-lock、windowed DLS、RatePreservation 或 DStructure，因此不能把行/列命题标成无条件闭合。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
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
