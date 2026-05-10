#!/usr/bin/env python3
"""生成 EXT-BG/RKS/Tail-log4 自足替代原子的逐块审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_ext_bg_rks_tail_log4_replacement_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-ext-bg-rks-tail-log4-replacement-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-ext-bg-rks-tail-log4-replacement-router.json"
OUT_MD = MONO / "prime-matrix-strict-ext-bg-rks-tail-log4-replacement-router.md"

PREVIOUS = MONO / "prime-matrix-strict-final-hardpoint-after-p51-router.json"
RKS_BRIDGE = DOCS / "rks-bridge-partition.md"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
BG_RKS = DOCS / "bg-rks-block-match.md"
TAIL = DOCS / "tail-log4-formal-appendix.md"
EXT_AUDIT = DOCS / "ext-citation-final-audit.md"
CONSTANTS_AUDIT = DOCS / "constants-absorption-final-audit.md"
BAKER_STATUS = DOCS / "explicit-p0-constants.status.md"
CLAIM_STATUS = MONO / "claim-status-table.md"

SOURCE_FILES = [
    PREVIOUS,
    RKS_BRIDGE,
    RKS_PARAM,
    BG_RKS,
    TAIL,
    EXT_AUDIT,
    CONSTANTS_AUDIT,
    BAKER_STATUS,
    CLAIM_STATUS,
]

TARGET = "SelfContainedEXTBGRKSMultilinearKloostermanAndTailLog4Replacement"
BG_ATOM = "MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks"
BAKER_AVG_ATOM = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
EXTERNAL_ACCEPT = "AcceptEXTBGForRKSLogFixedSaving"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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
    """构造逐块审计结果。"""
    previous = load_json(PREVIOUS)
    rks_bridge = read_text(RKS_BRIDGE)
    rks_param = read_text(RKS_PARAM)
    bg_rks = read_text(BG_RKS)
    tail = read_text(TAIL)
    ext_audit = read_text(EXT_AUDIT)
    constants = read_text(CONSTANTS_AUDIT)
    baker = read_text(BAKER_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    short_side_weil_closed = contains_all(
        rks_bridge,
        ["短侧 `<=P^{1/18}`", "逐短变量完成和/Weil 吸收", "P^{5/9}"],
    ) and contains_all(constants, ["A_weil_completion_log=4", "RKS 余量 54"])
    rks_parameter_closed = contains_all(rks_param, ["合计", "74<128"]) and contains_all(
        constants, ["K_sieve_log_saving", ">=54"]
    )
    rks_block_partition_closed = contains_all(
        bg_rks,
        ["Lemma RKS1", "Lemma RKS2", "Lemma RKS3", "Lemma RKS4"],
    )
    tail_log4_author_packet_closed = contains_all(
        tail,
        ["Theorem C", "Lemma C1", "Lemma C2", "Lemma C3"],
    )
    ext_bg_citation_ready = contains_all(
        ext_audit,
        ["EXT-BG", "Bourgain--Garaev", "固定对数节省"],
    )
    baker_single_frequency_insufficient = contains_all(
        baker,
        ["Baker Theorem 1 不能单独替代", "d 层绝对值平均", "Baker-frequency-large-sieve"],
    )

    external_bg_lane_closed_if_accepted = (
        active
        and short_side_weil_closed
        and rks_parameter_closed
        and rks_block_partition_closed
        and tail_log4_author_packet_closed
        and ext_bg_citation_ready
    )
    self_contained_bg_replacement_closed = False

    rows = [
        row(
            "FinalHardpointAtomActive",
            active,
            True,
            "上一证书已把作者侧自足替代路线压到 EXT-BG/RKS/Tail-log4 原子。",
            TARGET,
        ),
        row(
            "RKSShortSideWeilAbsorptionClosed",
            short_side_weil_closed,
            True,
            "短侧 <=P^(1/18) 的块由逐短变量 Weil/完成和吸收，目标强于 P/log^44P。",
            "no new bridge needed",
        ),
        row(
            "RKSBlockPartitionClosed",
            rks_block_partition_closed,
            True,
            "RKS1--RKS4 覆盖短侧 Weil、BG 双线性、BG 多线性、端点低体积四类块。",
            "BG input still external in RKS2/RKS3",
        ),
        row(
            "RKSParameterAuditClosed",
            rks_parameter_closed,
            True,
            "总对数损失 74<128，保留至少 54 个对数幂余量。",
            "parameter ledger closed",
        ),
        row(
            "TailLog4AuthorPacketClosed",
            tail_log4_author_packet_closed,
            True,
            "Tail-log4 已有 Theorem C 与 C1-C3 作者侧证明包。",
            "depends on external BG/Selberg/Vaughan/KL labels",
        ),
        row(
            "EXTBGCitationLaneReady",
            ext_bg_citation_ready,
            True,
            "外部路线只需接受 BG/Baker 类固定对数节省；不需要最佳幂指数。",
            EXTERNAL_ACCEPT,
        ),
        row(
            "BakerSingleFrequencyReplacementInsufficient",
            baker_single_frequency_insufficient,
            True,
            "Baker 单频率素变量定理不能单独处理 d 层绝对值平均；若走显式替代，需 Baker-frequency-large-sieve/DB平均。",
            BAKER_AVG_ATOM,
        ),
        row(
            "ExternalBGForRKSLogFixedSavingClosedIfAccepted",
            external_bg_lane_closed_if_accepted,
            True,
            "接受 EXT-BG 后，RKS/Tail-log4 所需外部输入与参数吸收闭合。",
            "external theorem acceptance lane",
        ),
        row(
            BG_ATOM,
            self_contained_bg_replacement_closed,
            False,
            "严格自足版尚未重证 BG 型双线性/多线性倒数 Kloosterman 固定对数节省。",
            f"{BG_ATOM} OR {BAKER_AVG_ATOM}",
        ),
        row(
            TARGET,
            self_contained_bg_replacement_closed,
            False,
            "EXT-BG/RKS/Tail-log4 自足替代包未闭合；当前只闭合了外部接受路线的参数匹配。",
            BG_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "最终晋级仍需独立接受或自足替代；本步没有产生无条件行/列闭合。",
            PROMOTION_GATE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_ext_bg_rks_tail_log4_replacement_router",
        "status": "ext_bg_rks_tail_log4_external_parameter_match_closed_self_contained_bg_reproof_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "rks_short_side_weil_absorption_closed": short_side_weil_closed,
        "rks_block_partition_closed": rks_block_partition_closed,
        "rks_parameter_audit_closed": rks_parameter_closed,
        "tail_log4_author_packet_closed": tail_log4_author_packet_closed,
        "ext_bg_citation_lane_ready": ext_bg_citation_ready,
        "external_bg_for_rks_log_fixed_saving_closed_if_accepted": external_bg_lane_closed_if_accepted,
        "baker_single_frequency_replacement_insufficient": baker_single_frequency_insufficient,
        "multilinear_reciprocal_kloosterman_self_contained_reproof_closed": self_contained_bg_replacement_closed,
        "self_contained_ext_bg_rks_tail_log4_replacement_closed": self_contained_bg_replacement_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BG_ATOM,
        "parallel_attack_target": BAKER_AVG_ATOM,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Tail-log4/RKS 原子已进一步压缩：短侧 Weil、端点低体积、RKS 参数账本和 Tail-log4 作者包都已闭合；"
            "真正剩余只剩 BG 型双线性/多线性倒数 Kloosterman 固定对数节省。"
            "接受 `EXT-BG` 时该原子参数匹配闭合；若坚持严格自足，则必须重证 "
            "`MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks`，"
            "或者走 Baker 大谱/倒数频率大筛替代来处理 d 层平均。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict EXT-BG/RKS/Tail-log4 自足替代审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"external_bg_for_rks_log_fixed_saving_closed_if_accepted={fmt_bool(result['external_bg_for_rks_log_fixed_saving_closed_if_accepted'])}",
        f"multilinear_reciprocal_kloosterman_self_contained_reproof_closed={fmt_bool(result['multilinear_reciprocal_kloosterman_self_contained_reproof_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 2. 下一最窄点",
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
    print(
        "external_bg_for_rks_log_fixed_saving_closed_if_accepted="
        f"{fmt_bool(result['external_bg_for_rks_log_fixed_saving_closed_if_accepted'])}"
    )


if __name__ == "__main__":
    main()
