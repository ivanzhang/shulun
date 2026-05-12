#!/usr/bin/env python3
"""生成行/列命题严格自足主线前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_mainline_self_contained_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-mainline-self-contained-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-mainline-self-contained-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-mainline-self-contained-frontier-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-rks-log-rnrs-transfer-closure-router.json",
    "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json",
    "prime-matrix-strict-moving-atom-terminal-packet-frontier-router.json",
    "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json",
    "prime-matrix-strict-rate-bearing-frontier-drilldown-router.json",
    "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-acyclic-clean-kls-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
    "prime-matrix-linear-sieve-tail-remainder-gap-router.json",
    "prime-matrix-strict-table012-x87-y-ln2-applicability-router.json",
]

CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
NCBLK_ANTIATOM = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
PDEC_CLEAN_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
ROSR_FLOOR = "RosserIwaniecWeightedFloorRemainderTenPercentBound"
EXTERNAL_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
RATE_PRESERVATION = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
EXTERNAL_FULLS = "AcceptExternalFullSKLSExtWithNoProjectionCompatibility"


def load_json(name: str) -> dict[str, Any]:
    """读取证据 JSON；缺失时返回空对象，避免破坏旧工作树。"""
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


def evidence_hashes() -> dict[str, str]:
    """登记本同步证书引用的证据哈希。"""
    hashes: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            hashes[f"docs/monograph/{name}"] = sha256(path)
    return hashes


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
    """合并最新主线证据，生成当前严格自足前沿。"""
    rks = load_json("prime-matrix-strict-rks-log-rnrs-transfer-closure-router.json")
    trace_frontier = load_json("prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json")
    moving_packet = load_json("prime-matrix-strict-moving-atom-terminal-packet-frontier-router.json")
    rate_sync = load_json("prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json")
    rate_drill = load_json("prime-matrix-strict-rate-bearing-frontier-drilldown-router.json")
    terminal_split = load_json("prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json")
    direct_pdec = load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json")
    clean_kls = load_json("prime-matrix-strict-acyclic-clean-kls-router.json")
    windowed_dls = load_json("prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    kz_atom = load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json")
    rough_tail = load_json("prime-matrix-linear-sieve-tail-remainder-gap-router.json")
    table012 = load_json("prime-matrix-strict-table012-x87-y-ln2-applicability-router.json")

    strict_basis = (
        f"(({CANONICAL_LOCK} OR {WINDOWED_DLS}) "
        f"AND {ROSR_FLOOR} "
        f"AND {RATE_PRESERVATION} "
        f"AND {DSTRUCTURE})"
    )
    conditional_basis = (
        f"(({CANONICAL_LOCK} OR {WINDOWED_DLS} OR {EXTERNAL_DIBFI} OR {EXTERNAL_FULLS}) "
        f"AND ({ROSR_FLOOR} OR {EXTERNAL_ROUGH}) "
        f"AND {RATE_PRESERVATION} "
        f"AND {DSTRUCTURE})"
    )
    terminal_reduction = (
        f"{PDEC_CLEAN_RATE} => "
        f"({CANONICAL_LOCK} OR {WINDOWED_DLS}); "
        f"{WINDOWED_DLS} => {KUZNETSOV_DLS} => {NCBLK_ANTIATOM}, "
        "whose failure returns to moving-atom/global terminal rather than proving the theorem."
    )

    rows = [
        row(
            "RKSLogAndTable012RemovedFromActiveBlockers",
            rks.get("self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed") is True
            and table012.get("theta_less_than_identity_to_8e11_self_contained_closed") is True,
            True,
            "RKS-log/Tail-log4 替代包与 table_012 低段 theta 自足计算输入已关闭，不再是当前主线活动阻断。",
            "仍不能替代 ExactUV/source/terminal 侧终端矛盾。",
        ),
        row(
            "TraceAndSignedSourceCyclesEliminated",
            trace_frontier.get("branch_trace_self_proof_eliminated") is True
            and trace_frontier.get("signed_source_fixed_point_eliminated_as_proof") is True,
            True,
            "branch-trace 与 signed-source 路线已识别为自回流，不能作为证明链。",
            "主线必须走 moving atom 终端包、canonical-lock 或 clean DLS。",
        ),
        row(
            "MovingAtomReducedToRateBearingPacket",
            moving_packet.get("direct_moving_block_terminal_route_active") is True
            and rate_sync.get("interface_sync_closed") is True,
            False,
            "actual noncanonical moving atom 已压成带 log-power 速率的终端 packet；接口同步关闭，但 packet 排斥未证。",
            f"{PDEC_CLEAN_RATE} AND {RATE_PRESERVATION}",
        ),
        row(
            "HighSegmentModelGapCompressedToRoughTailRemainder",
            rate_drill.get("frontier_drilldown_closed") is True
            and rough_tail.get("tail_ten_percent_margin_split") is True,
            False,
            "高段模型余量已删去调和窗口并压到动态骨架尾段；尾段又压成 Rosser-Iwaniec floor 余项或外部粗数下界。",
            f"{ROSR_FLOOR} OR {EXTERNAL_ROUGH}",
        ),
        row(
            "PDECCleanRateGateSplitButNotClosed",
            terminal_split.get("terminal_split_router_closed") is True
            and direct_pdec.get("scope_audit_closed") is True
            and clean_kls.get("direct_acyclic_clean_kls_dls_proved") is not True,
            False,
            "PDEC/CleanKLS 速率门已拆开：PDEC 需 strict 同集作用域匹配；不匹配则回到 canonical-lock 或 clean DLS。",
            f"{CANONICAL_LOCK} OR {WINDOWED_DLS}",
        ),
        row(
            "WindowedDLSReducedToKuznetsovNCBLKButLoops",
            (
                clean_kls.get("windowed_kloosterman_template_registered") is True
                or windowed_dls.get("acyclic_windowed_bilinear_normal_form_closed") is True
            )
            and kz_atom.get("kz_e_reduced_to_ncblk_or_external") is True,
            False,
            "windowed DLS 形式层已压尽；KZ-E 又压到 acyclic NC-BLK/source anti-atom，失败会回到 moving atom/global terminal。",
            f"{WINDOWED_DLS} or new nonrecursive source/anti-atom input.",
        ),
        row(
            "RatePreservationStillOpen",
            False,
            False,
            "速率型终端排斥还必须保存 moving atom 所需的 log-power 阈值，不能只给定性二分。",
            RATE_PRESERVATION,
        ),
        row(
            "DStructureIndependentGateStillOpen",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 的最终晋级仍需独立验收或严格自足替代验收。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前还没有得到排除早期零行反例链的完整终端矛盾。",
            strict_basis,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_mainline_self_contained_frontier_router",
        "status": "strict_mainline_frontier_synced_open_not_unconditionally_closed",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "rks_log_tail_log4_input_closed": rows[0]["closed"],
        "table012_low_theta_input_closed": table012.get("theta_less_than_identity_to_8e11_self_contained_closed") is True,
        "trace_signed_source_cycles_eliminated": rows[1]["closed"],
        "moving_atom_rate_packet_interface_synced": rows[2]["closed"],
        "rough_tail_remainder_frontier_synced": rows[3]["closed"],
        "pdec_clean_rate_gate_split": rows[4]["closed"],
        "row_column_unconditional_closed": False,
        "direct_unconditional_contradiction_found": False,
        "strict_self_contained_basis": strict_basis,
        "conditional_external_basis": conditional_basis,
        "terminal_reduction_summary": terminal_reduction,
        "next_primary_terminal_target": f"{CANONICAL_LOCK} OR {WINDOWED_DLS}",
        "next_nonrecursive_side_target": ROSR_FLOOR,
        "next_rate_target": RATE_PRESERVATION,
        "final_gate": DSTRUCTURE,
        "attack_order": [
            ROSR_FLOOR,
            RATE_PRESERVATION,
            f"{CANONICAL_LOCK} OR {WINDOWED_DLS}",
            DSTRUCTURE,
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "source_hashes": evidence_hashes(),
        "plain_conclusion": (
            "主线已回到严格证明边界：RKS-log 与 table_012 不再阻塞；"
            "signed-source/branch-trace/ExactUV pair-mass 的循环证明已删除。"
            "当前自足闭合还需要 terminal 侧 canonical-lock 或 windowed DLS、"
            "Rosser-Iwaniec floor 余项、moving packet 速率保持和 DStructure 独立门。"
            "因此行/列命题仍不能标为无条件闭合。"
        ),
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict 主线自足前沿同步证书",
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
        f"trace_signed_source_cycles_eliminated={fmt_bool(result['trace_signed_source_cycles_eliminated'])}",
        f"moving_atom_rate_packet_interface_synced={fmt_bool(result['moving_atom_rate_packet_interface_synced'])}",
        f"rough_tail_remainder_frontier_synced={fmt_bool(result['rough_tail_remainder_frontier_synced'])}",
        f"pdec_clean_rate_gate_split={fmt_bool(result['pdec_clean_rate_gate_split'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 当前严格基",
        "",
        "```text",
        result["strict_self_contained_basis"],
        "```",
        "",
        "条件外部基：",
        "",
        "```text",
        result["conditional_external_basis"],
        "```",
        "",
        "终端压缩摘要：",
        "",
        "```text",
        result["terminal_reduction_summary"],
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
            "## 3. 下一推进顺序",
            "",
            "| order | target | role |",
            "| ---: | --- | --- |",
        ]
    )
    roles = [
        "先关闭一维尾段粗筛余项，移除模型余量侧非循环缺口。",
        "证明 moving atom 到终端 packet 的 log-power 速率不丢失。",
        "排斥 terminal 侧 canonical-lock 或 windowed DLS 残余。",
        "完成最终 DStructure/Tail-log4/finite Rankin 独立门或自足替代验收。",
    ]
    for idx, (target, role) in enumerate(zip(result["attack_order"], roles, strict=True), start=1):
        lines.append(f"| {idx} | `{table_cell(target)}` | {role} |")
    lines.append("")
    lines.append("## 4. 结论")
    lines.append("")
    lines.append(
        "当前主线严格边界已经清楚：不能再用 signed-source、branch trace、pair-mass 或 generic WFD 作为闭合证明。"
        "若要真正闭合，必须在上表四个方向中给出新的正证明或验收记录。"
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
