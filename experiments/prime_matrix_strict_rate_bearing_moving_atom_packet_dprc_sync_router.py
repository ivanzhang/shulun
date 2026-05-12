#!/usr/bin/env python3
"""Prime Matrix strict 速率型 moving-atom 终端包 / DPRC 同步路由器。

用法示例：
  python3 experiments/prime_matrix_strict_rate_bearing_moving_atom_packet_dprc_sync_router.py

输出：
  docs/monograph/prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json
  docs/monograph/prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_GLOBAL_FRONTIER = DOCS / "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json"
DEFAULT_PACKET_FRONTIER = DOCS / "prime-matrix-strict-moving-atom-terminal-packet-frontier-router.json"
DEFAULT_MOVING_BLOCK = DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"
DEFAULT_DPRC_COMPAT = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"
DEFAULT_MODEL_GAP = DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json"
DEFAULT_HIGH_SEGMENT = DOCS / "prime-matrix-high-segment-model-gap-factorization-router.json"
DEFAULT_TERMINAL = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
DEFAULT_CYCLE = DOCS / "prime-matrix-strict-self-contained-cycle-obstruction-router.json"
DEFAULT_RKS = DOCS / "prime-matrix-strict-rks-log-rnrs-transfer-closure-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json"
DEFAULT_MD = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.md"

PACKET = "RateBearingMovingAtomTerminalPacketExclusionWithExplicitDPRC"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
PDEC_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
CYCLE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希，固定本次同步引用。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写成小写形式。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造路由判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def guard_preserved(*certs: dict[str, Any]) -> bool:
    """确认本步仍只使用假设反例链条，不调用真实样本缺席。"""
    guarded: list[bool] = []
    for cert in certs:
        if "counterexample_assumption_only" in cert:
            guarded.append(bool(cert.get("counterexample_assumption_only")))
        if "empirical_absence_not_used" in cert:
            guarded.append(bool(cert.get("empirical_absence_not_used")))
        if "hypothetical_chain_only" in cert:
            guarded.append(bool(cert.get("hypothetical_chain_only")))
        guarded.append(not bool(cert.get("row_column_unconditional_closed")))
    return all(guarded)


def build_rows(certs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总各接口的闭合与开放状态。"""
    global_frontier = certs["global_frontier"]
    packet = certs["packet_frontier"]
    moving_block = certs["moving_block"]
    dprc = certs["dprc_compat"]
    model_gap = certs["model_gap"]
    high_segment = certs["high_segment"]
    terminal = certs["terminal"]
    cycle = certs["cycle"]
    rks = certs["rks"]

    guard = guard_preserved(
        packet, moving_block, dprc, model_gap, high_segment, terminal, cycle, rks
    )
    rks_closed = (
        rks.get("rks_log_rnrs_transfer_closed") is True
        and rks.get("self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed") is True
    )
    packet_active = (
        packet.get("next_direct_attack_target") == PACKET
        and packet.get("rate_bearing_terminal_packet_exclusion_proved") is False
    )
    moving_no_unnamed = (
        moving_block.get("strict_actual_moving_block_router_closed") is True
        and PDEC_KLS in moving_block.get("terminal_gap_after_router", "")
        and MODEL_GAP in moving_block.get("terminal_gap_after_router", "")
    )
    dprc_compat_removed = (
        dprc.get("exact_model_gap_dprc_compatibility_proved") is True
        and dprc.get("no_additional_dprc_ledger_gap_after_terminal_promotion") is True
        and dprc.get("explicit_model_gap_and_finite_dprc_ledger_proved") is False
    )
    model_split = (
        model_gap.get("explicit_model_gap_and_finite_dprc_ledger_split_closed") is True
        and model_gap.get("finite_dprc_alpha043_p_below_2003_certificate_closed") is True
        and model_gap.get("high_segment_model_gap_alpha043_c3_analytic_ledger_proved") is False
    )
    high_factorized = (
        high_segment.get("high_segment_model_gap_factorized") is True
        and high_segment.get("bridge_finite_model_gap_certificate_closed") is True
        and high_segment.get("tail_harmonic_upper_0850_proved") is False
        and high_segment.get("tail_skeleton_lower_401_proved") is False
    )
    terminal_split_open = (
        terminal.get("terminal_split_router_closed") is True
        and terminal.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    cycle_obstruction = (
        cycle.get("self_contained_cycle_obstruction_proved") is True
        and cycle.get("current_internal_route_is_fixed_point") is True
        and cycle.get("cycle_returns_to_pdec_clean_kls_terminal_gate") is True
    )
    global_three_atoms = (
        global_frontier.get("strict_current_frontier_three_atoms") is True
        and MOVING_ATOM in global_frontier.get("three_atoms", [])
    )

    return [
        row(
            "SameTheoremAndCounterexampleGuardPreserved",
            guard,
            True,
            "所有导入证书仍在假设早期零行反例链条内同步，不使用真实零行缺席，也不转换命题。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "RKSLogTailLog4NoLongerActiveBlocker",
            rks_closed,
            True,
            "RKS-log/Tail-log4 自足替代包已由 RNRS/Rudnev 倒数能量链回填，不再作为当前活动阻断。",
            "不能替代 moving atom / ExactUV 源侧支撑下界。",
        ),
        row(
            "MovingAtomFrontierStillActive",
            global_three_atoms,
            False,
            "删除 branch-trace、signed-source 与 pair-mass 循环后，actual noncanonical moving atom 仍是三原子前沿之一。",
            MOVING_ATOM,
        ),
        row(
            "RateBearingPacketTargetPinned",
            packet_active,
            False,
            "moving atom 已压到带速率要求的同一 (u,v) 终端包；质性投影二分不足以闭合。",
            PACKET,
        ),
        row(
            "MovingAtomLowDimOrNoSignatureInterfaceClosed",
            moving_no_unnamed,
            True,
            "moving-block/NC-BLK 不能再作为无名出口：有低维签名进 PDEC/SAE/ColumnCRT，无签名进终端包。",
            "这只消除无名出口，不证明终端排斥。",
        ),
        row(
            "DPRCCompatibilityRemovedButLedgerRetained",
            dprc_compat_removed,
            True,
            "moving-block 替换未新增 DPRC 口径缺口；兼容性门可删，但模型余量账本仍保留。",
            MODEL_GAP,
        ),
        row(
            "ExplicitModelGapSplitImported",
            model_split,
            False,
            "P<2003 有限 DPRC 已闭合；P>=2003 的模型余量仍需解析账本。",
            HIGH_SEGMENT,
        ),
        row(
            "HighSegmentModelGapFactorized",
            high_factorized,
            False,
            "高段模型余量已拆成 2003<=P<3001 有限桥与 P>=3001 的两个尾段解析输入。",
            f"{HARMONIC} AND {SKELETON}",
        ),
        row(
            "PDECCapOrInternalCleanKLSRatePacketGateOpen",
            False,
            False,
            "速率型终端包若落入 PDEC/CleanKLS，仍需同口径 PDEC 作用域匹配或自足 CleanKLS/DLS 大筛证明。",
            PDEC_KLS_PACKET,
        ),
        row(
            "InternalExpansionCycleObstructionImported",
            cycle_obstruction,
            True,
            "从 PDEC/CleanKLS 继续内部展开会回到同一终端门；该循环是障碍，不是证明。",
            CYCLE_BREAKER,
        ),
        row(
            "RatePreservationLedgerOpen",
            False,
            False,
            "终端排斥还必须保存 moving atom 所需的 log-power 速率字段，不能只给定性非集中。",
            RATE,
        ),
        row(
            "DStructureIndependentAcceptanceStillOpen",
            False,
            False,
            "即使前述数学包都闭合，DStructure/Tail-log4/finite Rankin 仍需独立晋级验收或自足替代验收。",
            DSTRUCTURE,
        ),
        row(
            PACKET,
            False,
            False,
            "本同步只关闭接口与开放原子定位，不证明速率型 moving atom 终端包排斥。",
            f"{PDEC_KLS_PACKET} AND {HIGH_SEGMENT} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前尚未得到反例链与真实结构链之间足以排除早期零行的终端矛盾。",
            "继续攻 PDEC/CleanKLS 速率包、高段模型余量尾段账本、速率保持和 DStructure 验收。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行同步路由并返回机器证书。"""
    certs = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(certs)
    row_map = {item["gate"]: item for item in rows}
    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]
    expanded_high_segment = f"{HARMONIC} AND {SKELETON}"
    interface_sync_closed = all(
        row_map[name]["closed"]
        for name in [
            "SameTheoremAndCounterexampleGuardPreserved",
            "RKSLogTailLog4NoLongerActiveBlocker",
            "MovingAtomFrontierStillActive",
            "RateBearingPacketTargetPinned",
            "MovingAtomLowDimOrNoSignatureInterfaceClosed",
            "DPRCCompatibilityRemovedButLedgerRetained",
            "ExplicitModelGapSplitImported",
            "HighSegmentModelGapFactorized",
            "InternalExpansionCycleObstructionImported",
        ]
    )
    remaining_atoms = [
        PDEC_KLS_PACKET,
        HIGH_SEGMENT,
        HARMONIC,
        SKELETON,
        RATE,
        DSTRUCTURE,
    ]
    return {
        "certificate_type": "prime_matrix_strict_rate_bearing_moving_atom_packet_dprc_sync_router",
        "status": "rate_bearing_moving_atom_packet_sync_closed_terminal_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "interface_sync_closed": interface_sync_closed,
        "moving_atom_low_dim_or_no_signature_interface_closed": row_map[
            "MovingAtomLowDimOrNoSignatureInterfaceClosed"
        ]["closed"],
        "dprc_compatibility_removed": row_map["DPRCCompatibilityRemovedButLedgerRetained"]["closed"],
        "explicit_model_gap_split_imported": row_map["ExplicitModelGapSplitImported"]["closed"],
        "high_segment_model_gap_factorized": row_map["HighSegmentModelGapFactorized"]["closed"],
        "rate_bearing_moving_atom_packet_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "active_target_before_router": PACKET,
        "compressed_remaining_basis": (
            f"{PDEC_KLS_PACKET} AND {HIGH_SEGMENT} AND {RATE} AND {DSTRUCTURE}"
        ),
        "expanded_remaining_basis": (
            f"{PDEC_KLS_PACKET} AND ({expanded_high_segment}) AND {RATE} AND {DSTRUCTURE}"
        ),
        "cycle_breaker_alternative": CYCLE_BREAKER,
        "remaining_atoms": remaining_atoms,
        "next_direct_attack_target": PDEC_KLS_PACKET,
        "parallel_attack_targets": [HARMONIC, SKELETON, RATE, DSTRUCTURE],
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "rows": rows,
        "source_hashes": {str(path.relative_to(ROOT)): sha256(path) for path in paths.values()},
        "plain_conclusion": (
            "本步关闭的是速率型 moving atom 终端包的接口同步：RKS-log 已移出活动阻断，"
            "moving-block 无名出口被消除，DPRC 兼容性门已删除，模型余量被拆到高段尾段账本。"
            "但终端排斥仍未证明；当前严格自足剩余为 PDEC/CleanKLS 速率包、高段模型余量、"
            "RatePreservation 和 DStructure 独立验收。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写出人类可读归档。"""
    lines = [
        "# Prime Matrix strict 速率型 moving-atom 终端包 / DPRC 同步路由器",
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
        f"interface_sync_closed={fmt_bool(result['interface_sync_closed'])}",
        (
            "rate_bearing_moving_atom_packet_exclusion_proved="
            f"{fmt_bool(result['rate_bearing_moving_atom_packet_exclusion_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步后的剩余基",
        "",
        "压缩形式：",
        "",
        "```text",
        result["compressed_remaining_basis"],
        "```",
        "",
        "高段模型余量展开后：",
        "",
        "```text",
        result["expanded_remaining_basis"],
        "```",
        "",
        "非循环破环备用输入：",
        "",
        "```text",
        result["cycle_breaker_alternative"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
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
            "## 3. 当前最窄推进顺序",
            "",
            "1. 先攻 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet`，因为没有终端排斥，moving atom 终端包不能转成矛盾。",
            "2. 并行补 `HarmonicWindowAlpha043PGe3001Upper0850Ledger` 与 `DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger`，把高段模型余量从审计支持升级为解析账本。",
            "3. 补 `RatePreservationLedger_FOR_moving_atom_packet`，确保终端排斥保留所需 log-power 速率。",
            "4. 最后仍需 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 或其严格自足替代验收。",
            "",
            "本证书不把 `CurrentMaterializedFutureSchema=0`、外部 KLS/DI-BFI、RKS-log 回填或 PDEC/CleanKLS 标签本身当作无条件证明。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-frontier", type=Path, default=DEFAULT_GLOBAL_FRONTIER)
    parser.add_argument("--packet-frontier", type=Path, default=DEFAULT_PACKET_FRONTIER)
    parser.add_argument("--moving-block", type=Path, default=DEFAULT_MOVING_BLOCK)
    parser.add_argument("--dprc-compat", type=Path, default=DEFAULT_DPRC_COMPAT)
    parser.add_argument("--model-gap", type=Path, default=DEFAULT_MODEL_GAP)
    parser.add_argument("--high-segment", type=Path, default=DEFAULT_HIGH_SEGMENT)
    parser.add_argument("--terminal", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--cycle", type=Path, default=DEFAULT_CYCLE)
    parser.add_argument("--rks", type=Path, default=DEFAULT_RKS)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "global_frontier": args.global_frontier,
        "packet_frontier": args.packet_frontier,
        "moving_block": args.moving_block,
        "dprc_compat": args.dprc_compat,
        "model_gap": args.model_gap,
        "high_segment": args.high_segment,
        "terminal": args.terminal,
        "cycle": args.cycle,
        "rks": args.rks,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
