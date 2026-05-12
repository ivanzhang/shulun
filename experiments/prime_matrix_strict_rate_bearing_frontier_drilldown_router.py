#!/usr/bin/env python3
"""Prime Matrix strict 速率型前沿下钻路由器。

用法示例：
  python3 experiments/prime_matrix_strict_rate_bearing_frontier_drilldown_router.py

输出：
  docs/monograph/prime-matrix-strict-rate-bearing-frontier-drilldown-router.json
  docs/monograph/prime-matrix-strict-rate-bearing-frontier-drilldown-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SYNC = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json"
DEFAULT_HARMONIC = DOCS / "prime-matrix-harmonic-window-dusart-ledger-router.json"
DEFAULT_SKELETON = DOCS / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"
DEFAULT_TERMINAL = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
DEFAULT_FIREWALL = DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-strict-rate-bearing-frontier-drilldown-router.json"
DEFAULT_MD = DOCS / "prime-matrix-strict-rate-bearing-frontier-drilldown-router.md"

PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"
HARMONIC = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
TAIL = "LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
CYCLE_ALT = "AcyclicTerminalCanonicalLockSubatoms_OR_NewIndependentSourceEntropyProof"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


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


def replace_high_segment(basis: str) -> str:
    """把高段双输入替换成已压缩的尾段输入。"""
    expanded = f"({HARMONIC} AND {SKELETON})"
    return basis.replace(HIGH_SEGMENT, TAIL).replace(expanded, TAIL)


def guard_preserved(*certs: dict[str, Any]) -> bool:
    """确认仍在假设反例链内同步，不调用真实零行缺席。"""
    checks: list[bool] = []
    for cert in certs:
        checks.append(bool(cert.get("counterexample_assumption_only", True)))
        checks.append(bool(cert.get("empirical_absence_not_used", True)))
        checks.append(bool(cert.get("hypothetical_chain_only", True)))
        checks.append(not bool(cert.get("row_column_unconditional_closed")))
    return all(checks)


def build_rows(certs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成前沿下钻判定表。"""
    sync = certs["sync"]
    harmonic = certs["harmonic"]
    skeleton = certs["skeleton"]
    terminal = certs["terminal"]
    firewall = certs["firewall"]

    guard = guard_preserved(sync, harmonic, skeleton, terminal, firewall)
    sync_active = (
        sync.get("interface_sync_closed") is True
        and sync.get("rate_bearing_moving_atom_packet_exclusion_proved") is False
        and sync.get("next_direct_attack_target") == PDEC_KLS_PACKET
    )
    harmonic_closed = harmonic.get("harmonic_window_alpha043_upper0850_closed") is True
    skeleton_tail_open = (
        skeleton.get("dynamic_skeleton_lower_factorized") is True
        and skeleton.get("finite_dynamic_skeleton_certificate_closed") is True
        and skeleton.get("tail_linear_lower_sieve_ledger_proved") is False
    )
    pdec_gate_open = terminal.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    recurrence_guard = (
        firewall.get("row_column_unconditional_closed") is False
        and firewall.get("next_direct_attack_target") == CYCLE_ALT
    )
    high_compressed = sync_active and harmonic_closed and skeleton_tail_open

    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍同步假设早期零行反例链，不使用真实零行缺席，也不转换命题。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "RateBearingPacketFrontierActive",
            sync_active,
            False,
            "速率型 moving-atom 终端包已定位，但终端排斥尚未证明。",
            PDEC_KLS_PACKET,
        ),
        row(
            "HarmonicWindowRemovedFromActiveBasis",
            harmonic_closed,
            True,
            "调和窗口上界已有 Dusart/有限段证书，不能继续作为活动硬点重复攻击。",
            "从高段模型余量中删除该原子。",
        ),
        row(
            "DynamicSkeletonReducedToTailLinearSieve",
            skeleton_tail_open,
            False,
            "动态粗骨架有限段已闭合，P>=100000 被压成一维 lower-sieve 尾段账本。",
            TAIL,
        ),
        row(
            "HighSegmentModelGapCompressed",
            high_compressed,
            False,
            "高段模型余量不再是调和窗口加骨架双硬点；活动剩余只保留骨架尾段筛下界。",
            TAIL,
        ),
        row(
            "PDECCleanKLSRatePacketGateStillOpen",
            pdec_gate_open,
            False,
            "速率型终端包的 PDEC/CleanKLS 速率门仍未证明，不能由标签命名本身闭合。",
            PDEC_KLS_PACKET,
        ),
        row(
            "DirectTerminalExpansionRecurrenceBlocked",
            recurrence_guard,
            True,
            "裸展开 PDEC/CleanKLS 终端标签会回流到 canonical-lock 或新的独立 source-entropy 输入；这是防火墙，不是证明。",
            CYCLE_ALT,
        ),
        row(
            "RatePreservationLedgerStillOpen",
            False,
            False,
            "终端排斥还必须保存 moving atom 所需的 log-power 速率字段。",
            RATE,
        ),
        row(
            "DStructureIndependentAcceptanceStillOpen",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍需独立验收或自足替代。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未得到足以排除早期零行反例链的终端矛盾。",
            f"{PDEC_KLS_PACKET} AND {TAIL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行前沿下钻。"""
    certs = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(certs)
    row_map = {item["gate"]: item for item in rows}
    old_compressed = certs["sync"].get("compressed_remaining_basis", "")
    old_expanded = certs["sync"].get("expanded_remaining_basis", "")
    new_basis = f"{PDEC_KLS_PACKET} AND {TAIL} AND {RATE} AND {DSTRUCTURE}"
    external_or_conditional_basis = new_basis.replace(TAIL, "ExternalShortIntervalRoughNumberLowerBoundForAlpha043_OR_StandardBetaSieveMertensTail")

    return {
        "certificate_type": "prime_matrix_strict_rate_bearing_frontier_drilldown_router",
        "status": "rate_bearing_frontier_drilled_high_segment_to_tail_sieve_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "frontier_drilldown_closed": row_map["HighSegmentModelGapCompressed"]["closed"],
        "harmonic_window_removed_from_active_basis": row_map["HarmonicWindowRemovedFromActiveBasis"]["closed"],
        "dynamic_skeleton_tail_linear_sieve_open": True,
        "rate_bearing_moving_atom_packet_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "previous_compressed_remaining_basis": old_compressed,
        "previous_expanded_remaining_basis": old_expanded,
        "compressed_remaining_basis": new_basis,
        "external_or_conditional_basis": external_or_conditional_basis,
        "next_direct_attack_target": PDEC_KLS_PACKET,
        "next_nonrecursive_attack_target": TAIL,
        "parallel_attack_targets": [TAIL, RATE, DSTRUCTURE],
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
        "source_hashes": {str(path.relative_to(ROOT)): sha256(path) for path in paths.values()},
        "plain_conclusion": (
            "本步完成前沿同步下钻：调和窗口上界已从活动剩余基中删除；动态粗骨架下界只剩 "
            "P>=100000 的一维 lower-sieve 尾段账本。速率型 moving-atom 终端排斥仍未证明，"
            "PDEC/CleanKLS 速率门、RatePreservation 与 DStructure 验收仍开放。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写出 Markdown 归档。"""
    lines = [
        "# Prime Matrix strict 速率型前沿下钻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"frontier_drilldown_closed={fmt_bool(result['frontier_drilldown_closed'])}",
        f"harmonic_window_removed_from_active_basis={fmt_bool(result['harmonic_window_removed_from_active_basis'])}",
        f"dynamic_skeleton_tail_linear_sieve_open={fmt_bool(result['dynamic_skeleton_tail_linear_sieve_open'])}",
        f"rate_bearing_moving_atom_packet_exclusion_proved={fmt_bool(result['rate_bearing_moving_atom_packet_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 剩余基更新",
        "",
        "旧压缩基：",
        "",
        "```text",
        result["previous_compressed_remaining_basis"],
        "```",
        "",
        "旧展开基：",
        "",
        "```text",
        result["previous_expanded_remaining_basis"],
        "```",
        "",
        "新活动基：",
        "",
        "```text",
        result["compressed_remaining_basis"],
        "```",
        "",
        "允许外部或标准筛输入时的旁路基：",
        "",
        "```text",
        result["external_or_conditional_basis"],
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
            "## 3. 下一步",
            "",
            f"主硬点仍是 `{result['next_direct_attack_target']}`；可独立下钻的非循环账本是 `{result['next_nonrecursive_attack_target']}`。",
            "",
            "本证书只删除已闭合的调和窗口并同步尾段骨架账本，不声明行/列无条件闭合。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", type=Path, default=DEFAULT_SYNC)
    parser.add_argument("--harmonic", type=Path, default=DEFAULT_HARMONIC)
    parser.add_argument("--skeleton", type=Path, default=DEFAULT_SKELETON)
    parser.add_argument("--terminal", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "sync": args.sync,
        "harmonic": args.harmonic,
        "skeleton": args.skeleton,
        "terminal": args.terminal,
        "firewall": args.firewall,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")
    print(f"next_nonrecursive_attack_target={result['next_nonrecursive_attack_target']}")


if __name__ == "__main__":
    main()
