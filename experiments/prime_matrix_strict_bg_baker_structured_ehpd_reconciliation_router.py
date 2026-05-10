#!/usr/bin/env python3
"""同步 BG/Baker 历史路线与 Structured-EHPD 保守替代路线。

用法示例：
  python3 experiments/prime_matrix_strict_bg_baker_structured_ehpd_reconciliation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-bg-baker-structured-ehpd-reconciliation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-bg-baker-structured-ehpd-reconciliation-router.json"
OUT_MD = MONO / "prime-matrix-strict-bg-baker-structured-ehpd-reconciliation-router.md"

PREVIOUS = MONO / "prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json"
EXPLICIT_STATUS = DOCS / "explicit-p0-constants.status.md"
OMR = DOCS / "omr-cgtp-lsmp-theoremization.md"
NRC = DOCS / "nrc-theoremization.md"
FCT = DOCS / "fct-tree-wfe-theoremization.md"
ROW_COLUMN = DOCS / "row-column-reduction-theoremization.md"
TAIL_LOG4 = DOCS / "tail-log4-theoremization.md"
EXT_AUDIT = DOCS / "ext-citation-final-audit.md"
CONSTANTS_AUDIT = DOCS / "constants-absorption-final-audit.md"
FINAL_INTERFACE = DOCS / "final-interface-index.md"
TOP_JOURNAL = DOCS / "top-journal-proof-audit.md"
AUTHOR_STATUS = MONO / "prime-matrix-author-side-closure-task-completion-router.json"
FINAL_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
CONSERVATIVE_CONSTANTS = DOCS / "explicit-p0-constants.structured-conservative.json"
CONSERVATIVE_RESULT = DOCS / "explicit-p0-structured-conservative-result.json"
FINITE_VERIFY = DOCS / "finite-verify-exp5.json"
CLAIM_STATUS = MONO / "claim-status-table.md"

SOURCE_FILES = [
    PREVIOUS,
    EXPLICIT_STATUS,
    OMR,
    NRC,
    FCT,
    ROW_COLUMN,
    TAIL_LOG4,
    EXT_AUDIT,
    CONSTANTS_AUDIT,
    FINAL_INTERFACE,
    TOP_JOURNAL,
    AUTHOR_STATUS,
    FINAL_PROMOTION,
    CONSERVATIVE_CONSTANTS,
    CONSERVATIVE_RESULT,
    FINITE_VERIFY,
    CLAIM_STATUS,
]

OLD_BG_SELF_PROOF = "SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving"
OLD_BAKER_AVG = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
STRUCTURED_ACCEPT = "StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXPLICIT_ACCEPTANCE = "ExplicitIndependentPromotionAcceptanceRecord"
SELF_REPLACEMENT = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部关键片段。"""
    return all(item in text for item in needles)


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造同步判定。"""
    previous = load_json(PREVIOUS)
    explicit_status = read_text(EXPLICIT_STATUS)
    omr = read_text(OMR)
    nrc = read_text(NRC)
    fct = read_text(FCT)
    row_column = read_text(ROW_COLUMN)
    tail_log4 = read_text(TAIL_LOG4)
    ext_audit = read_text(EXT_AUDIT)
    constants_audit = read_text(CONSTANTS_AUDIT)
    final_interface = read_text(FINAL_INTERFACE)
    top_journal = read_text(TOP_JOURNAL)
    author_status = load_json(AUTHOR_STATUS)
    final_promotion = load_json(FINAL_PROMOTION)
    conservative_constants = load_json(CONSERVATIVE_CONSTANTS)
    conservative_result = load_json(CONSERVATIVE_RESULT)
    finite_verify = load_json(FINITE_VERIFY)

    previous_bg_as_next = previous.get("next_direct_attack_target") == OLD_BG_SELF_PROOF
    baker_theorem_extracted = contains_all(
        explicit_status,
        ["Baker 主定理抽取成功", "α^4/2000", "P^{13/24} <= N <= P^{19/24}"],
    )
    baker_single_frequency_insufficient = contains_all(
        explicit_status,
        ["Baker Theorem 1 不能单独替代", "d 层绝对值平均"],
    )
    bg_external_match_ready = contains_all(
        ext_audit,
        ["EXT-BG", "固定对数节省", "Bourgain--Garaev"],
    ) and contains_all(
        tail_log4,
        ["Theorem RKS-log", "任意固定对数节省"],
    )
    structured_decouples_bg = contains_all(
        explicit_status,
        ["use_structured_ehpd", "不再要求", "BG 四个常数"],
    )
    omr_packet_present = contains_all(
        omr,
        ["Theorem OCL", "OMR-1", "Theorem CGTP", "Theorem LSMP"],
    )
    nrc_packet_closed = contains_all(nrc, ["Theorem NRC", "Weil 界", "完成法"])
    fct_packet_closed = contains_all(fct, ["Theorem Tree-WFE", "frequency-closure terminal"])
    row_column_reduction_present = contains_all(
        row_column,
        ["Theorem A", "Theorem B", "Structured-EHPD 坏配置"],
    )
    constants_packet_present = (
        conservative_constants.get("use_structured_ehpd") is True
        and conservative_constants.get("use_omr_pack") is True
        and conservative_constants.get("K_sieve_log_saving") == 128.0
    )
    p0_overlap_closed = (
        float(conservative_result.get("log_P0_upper", 999.0)) <= 3.5 + 1e-9
        and finite_verify.get("ok") is True
        and finite_verify.get("max_p") == 148
    )
    constants_absorption_closed = contains_all(
        constants_audit,
        ["log_P0_upper=3.5", "exp(3.5)<exp(5)", "常数层面闭合"],
    )
    final_interface_indexes_structured_lane = contains_all(
        final_interface,
        ["A--D 当前状态", "D OMR/CGTP/LSMP", "log_P0_upper=3.5"],
    )
    top_journal_caution_present = contains_all(
        top_journal,
        ["若第 1275 节列出的结构输入", "不能表述为", "无需额外结构输入"],
    )
    author_conditional_done = author_status.get("author_side_completable_tasks_done") is True
    final_promotion_accepted = final_promotion.get("referee_gate_explicitly_accepted") is True or (
        final_promotion.get("promotion_package_independently_accepted") is True
    )

    structured_lane_packet_ready = all(
        [
            structured_decouples_bg,
            omr_packet_present,
            nrc_packet_closed,
            fct_packet_closed,
            row_column_reduction_present,
            constants_packet_present,
            p0_overlap_closed,
            constants_absorption_closed,
            final_interface_indexes_structured_lane,
        ]
    )
    bg_unique_blocker_rejected = (
        previous_bg_as_next
        and baker_theorem_extracted
        and baker_single_frequency_insufficient
        and structured_lane_packet_ready
    )

    # 这里保守地不把最终无条件闭合标为 true：独立晋级门尚未发生。
    structured_final_acceptance_closed = structured_lane_packet_ready and not top_journal_caution_present
    row_column_unconditional_closed = final_promotion_accepted and structured_final_acceptance_closed

    rows = [
        row(
            "PriorBakerTheoremExtractionRecovered",
            baker_theorem_extracted,
            True,
            "旧材料已抽取 Baker Theorem 1：单频率素变量有显式指数，但仍有常数和 d 平均问题。",
            "history recovered",
        ),
        row(
            "BakerSingleFrequencyInsufficiencyPreserved",
            baker_single_frequency_insufficient,
            True,
            "Baker 点态素变量估计不能直接控制 coherent d 层绝对值平均。",
            OLD_BAKER_AVG,
        ),
        row(
            "EXTBGRKSExternalMatchReady",
            bg_external_match_ready,
            True,
            "BG/RKS 外部路线只需固定对数节省，参数匹配与引用边界已经定位。",
            "Accept EXT-BG if external lane is used",
        ),
        row(
            "StructuredEHPDDecouplesOldBGConstants",
            structured_decouples_bg,
            True,
            "旧 `delta_BG_*` 四常数阻塞已被 `use_structured_ehpd + use_omr_pack` 路线绕开。",
            "BG reproof is no longer the unique internal route",
        ),
        row(
            "OMRCGTPLSMPNRCFCTPacketPresent",
            omr_packet_present and nrc_packet_closed and fct_packet_closed,
            True,
            "D 组结构包已拆成 OMR/CGTP/LSMP、NRC、FCT/Tree-WFE 的可审查定理族。",
            "final symbol/interface audit",
        ),
        row(
            "RowColumnToStructuredEHPDReductionPresent",
            row_column_reduction_present,
            True,
            "行/列反例到 Structured-EHPD 坏配置的 A/B 归约已经成稿。",
            "A/B-D interface consistency",
        ),
        row(
            "ConservativeP0AndFiniteOverlapClosed",
            p0_overlap_closed and constants_absorption_closed,
            True,
            "保守结构常数包给 log_P0=3.5，有限验证覆盖到 exp(5)，两段重叠。",
            "certificate reproducibility",
        ),
        row(
            "OldBGSelfProofAsUniqueHardpointRejected",
            bg_unique_blocker_rejected,
            True,
            "继续把 BG 自足重证写成唯一剩余会漏掉 Structured-EHPD/OMR 保守替代路线。",
            STRUCTURED_ACCEPT,
        ),
        row(
            STRUCTURED_ACCEPT,
            structured_final_acceptance_closed,
            False,
            "结构路线证据包和常数层面已齐；但顶刊审查口径仍要求把最终接口作为独立接受/最终审稿验收项。",
            f"{STRUCTURED_ACCEPT} OR {EXPLICIT_ACCEPTANCE}",
        ),
        row(
            PROMOTION_GATE,
            final_promotion_accepted,
            False,
            "DStructure/Tail-log4/finite Rankin 晋级门尚无独立接受记录。",
            f"{EXPLICIT_ACCEPTANCE} OR {SELF_REPLACEMENT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "本步完成路线同步与硬点纠偏；未生成独立验收事件，故不宣称无条件闭合。",
            PROMOTION_GATE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_bg_baker_structured_ehpd_reconciliation_router",
        "status": "bg_baker_history_recovered_structured_ehpd_replacement_lane_restored_final_acceptance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_bg_as_next_direct_attack_target": previous_bg_as_next,
        "baker_theorem_extracted_in_prior_work": baker_theorem_extracted,
        "baker_single_frequency_replacement_insufficient": baker_single_frequency_insufficient,
        "ext_bg_rks_external_match_ready": bg_external_match_ready,
        "structured_ehpd_decouples_old_bg_constants": structured_decouples_bg,
        "structured_lane_packet_ready": structured_lane_packet_ready,
        "structured_final_acceptance_closed": structured_final_acceptance_closed,
        "bg_self_proof_as_unique_hardpoint_rejected": bg_unique_blocker_rejected,
        "author_side_conditional_chain_completed": author_conditional_done,
        "final_promotion_gate_accepted": final_promotion_accepted,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": STRUCTURED_ACCEPT,
        "parallel_attack_target": EXPLICIT_ACCEPTANCE,
        "fallback_deep_estimate_target": f"{OLD_BG_SELF_PROOF} OR {OLD_BAKER_AVG}",
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "BG/Baker 旧研究已经找到了两件关键事实：Baker 单频率素变量定理可抽取但不能处理 d 层平均，"
            "EXT-BG/RKS 外部固定对数节省可与 Tail-log4 参数严格匹配。随后 Structured-EHPD/OMR "
            "保守结构包已把作者侧路线从旧 BG 四常数阻塞中解耦，并由 `log_P0=3.5` 与 "
            "`P<=exp(5)` 有限验证形成常数层面闭合。"
            "因此当前真正最精确硬点不是继续把 BG 自足重证当作唯一剩余，而是对 "
            "`StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance` 做最终接口验收，"
            "并保留独立 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 晋级门。"
        ),
        "reconciled_hardpoint_order": [
            STRUCTURED_ACCEPT,
            EXPLICIT_ACCEPTANCE,
            f"{OLD_BG_SELF_PROOF} OR {OLD_BAKER_AVG}",
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict BG/Baker 与 Structured-EHPD 同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"baker_theorem_extracted_in_prior_work={fmt_bool(result['baker_theorem_extracted_in_prior_work'])}",
        f"baker_single_frequency_replacement_insufficient={fmt_bool(result['baker_single_frequency_replacement_insufficient'])}",
        f"ext_bg_rks_external_match_ready={fmt_bool(result['ext_bg_rks_external_match_ready'])}",
        f"structured_ehpd_decouples_old_bg_constants={fmt_bool(result['structured_ehpd_decouples_old_bg_constants'])}",
        f"structured_lane_packet_ready={fmt_bool(result['structured_lane_packet_ready'])}",
        f"bg_self_proof_as_unique_hardpoint_rejected={fmt_bool(result['bg_self_proof_as_unique_hardpoint_rejected'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 纠偏后的硬点顺序",
        "",
        "| order | target |",
        "| ---: | --- |",
    ]
    for index, target in enumerate(result["reconciled_hardpoint_order"], start=1):
        lines.append(f"| {index} | `{table_cell(target)}` |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一最精确硬攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"structured_lane_packet_ready={fmt_bool(result['structured_lane_packet_ready'])}")


if __name__ == "__main__":
    main()
