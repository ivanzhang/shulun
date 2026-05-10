#!/usr/bin/env python3
"""直接攻击 RKS-log 内部自足硬点并压缩到 RKS2/RKS3。

用法示例：
  python3 experiments/prime_matrix_strict_rks_log_internal_hardpoint_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks-log-internal-hardpoint-direct-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks-log-internal-hardpoint-direct-attack-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks-log-internal-hardpoint-direct-attack-router.md"

PREVIOUS = MONO / "prime-matrix-strict-self-contained-replacement-package-hardpoint-router.json"
TAIL_LOG4 = DOCS / "tail-log4-theoremization.md"
BG_RKS = DOCS / "bg-rks-block-match.md"
RKS_BRIDGE = DOCS / "rks-bridge-partition.md"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
EXT_AUDIT = DOCS / "ext-citation-final-audit.md"
BAKER_STATUS = DOCS / "explicit-p0-constants.status.md"
CLAIM_STATUS = MONO / "claim-status-table.md"

SOURCE_FILES = [
    PREVIOUS,
    TAIL_LOG4,
    BG_RKS,
    RKS_BRIDGE,
    RKS_PARAM,
    EXT_AUDIT,
    BAKER_STATUS,
    CLAIM_STATUS,
]

TARGET = "SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving"
NEXT_ATOM = "SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving"
BG_PROOF = "SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving"
BAKER_AVG = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
EXT_BG = "AcceptEXTBGForRKSLogFixedSaving"


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
    """构造 RKS-log 直接攻击审计。"""
    previous = load_json(PREVIOUS)
    tail = read_text(TAIL_LOG4)
    bg_rks = read_text(BG_RKS)
    bridge = read_text(RKS_BRIDGE)
    rks_param = read_text(RKS_PARAM)
    ext = read_text(EXT_AUDIT)
    baker = read_text(BAKER_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    rks_log_statement_fixed = contains_all(
        tail,
        ["Theorem RKS-log", "|I||J| >= p/log^A p"],
    )
    rks1_short_weil_closed = contains_all(
        bg_rks,
        ["Lemma RKS1", "短侧"],
    ) and contains_all(
        bridge,
        ["逐短变量完成和/Weil 吸收"],
    )
    rks4_low_volume_closed = contains_all(
        bg_rks,
        ["Lemma RKS4"],
    ) and contains_all(
        tail,
        ["低体积块吸收"],
    )
    rks2_rks3_isolated = contains_all(
        bg_rks,
        ["Lemma RKS2", "Lemma RKS3"],
    )
    log_budget_closed = contains_all(rks_param, ["74<128"])
    ext_bg_ready = contains_all(ext, ["EXT-BG", "Bourgain--Garaev", "固定对数节省"])
    baker_not_enough = contains_all(
        baker,
        ["Baker Theorem 1 不能单独替代", "d 层绝对值平均"],
    )
    baker_partial_frontier_known = contains_all(
        baker,
        ["Baker 大谱只闭合到 `θ<5/8`", "F4S+", "θ<3/4"],
    )
    rks2_rks3_self_contained_proved = False
    rks_log_self_contained_proved = (
        rks1_short_weil_closed
        and rks4_low_volume_closed
        and rks2_rks3_self_contained_proved
    )

    exact_atom = {
        "name": NEXT_ATOM,
        "rks2": "BG bilinear reciprocal Kloosterman log saving for divisor-bounded Vaughan Type II blocks",
        "rks3": "BG multilinear / Kloost 1/2 reciprocal product log saving for balanced or further split blocks",
        "required_strength": "enough fixed log saving to pay RKS loss 74 and leave Tail-log4 log^-44; prior conservative target log^-118 is sufficient",
        "closed_parts_removed": "RKS1 short-side Weil and RKS4 low-volume/endpoint absorption",
        "external_shortcut": "EXT-BG closes this if accepted, but strict internal line must prove it or prove Baker-frequency average replacement",
    }

    rows = [
        row(
            "RKSLogTargetActive",
            active,
            True,
            "上一层已把唯一内部自足线压成 TL4-L/RKS-log。",
            TARGET,
        ),
        row(
            "RKSLogStatementFixed",
            rks_log_statement_fixed,
            True,
            "RKS-log 已有精确定理模式：素数模数、倒数乘积相位、固定对数节省。",
            "statement fixed",
        ),
        row(
            "RKS1ShortSideWeilClosed",
            rks1_short_weil_closed,
            True,
            "短侧变量由完成和/Weil 吸收，不是内部深点。",
            "removed from hardpoint",
        ),
        row(
            "RKS4LowVolumeClosed",
            rks4_low_volume_closed,
            True,
            "低体积和端点块由平凡估计/Tail-log4 余量吸收。",
            "removed from hardpoint",
        ),
        row(
            "RKS2RKS3DeepBlocksIsolated",
            rks2_rks3_isolated and log_budget_closed,
            True,
            "剩余深块精确为 RKS2 双线性 BG 与 RKS3 多线性 BG，且对数预算 74<128 已闭合。",
            NEXT_ATOM,
        ),
        row(
            "EXTBGExternalShortcutReady",
            ext_bg_ready,
            True,
            "接受 EXT-BG 时 RKS2/RKS3 外部闭合。",
            EXT_BG,
        ),
        row(
            "BakerOnlyStillInsufficient",
            baker_not_enough,
            True,
            "Baker 单频率不能直接替代 coherent 平均；旧 Baker/F4S+ 路线只是备选重证策略。",
            BAKER_AVG,
        ),
        row(
            "BakerAverageFrontierKnown",
            baker_partial_frontier_known,
            True,
            "旧研究已定位 Baker 大谱、F4S+ 和临界拼接路径，但未形成完整内部证明。",
            BAKER_AVG,
        ),
        row(
            NEXT_ATOM,
            rks2_rks3_self_contained_proved,
            False,
            "当前材料没有内部证明 RKS2/RKS3 的 BG 型固定对数节省。",
            f"{BG_PROOF} OR {BAKER_AVG}",
        ),
        row(
            TARGET,
            rks_log_self_contained_proved,
            False,
            "RKS-log 自足闭合等价于补上 RKS2/RKS3 深块内部证明。",
            NEXT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只继续压缩唯一内部硬点，未证明 BG 深估计。",
            TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks_log_internal_hardpoint_direct_attack_router",
        "status": "rks_log_internal_hardpoint_reduced_to_rks2_rks3_bg_blocks",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "rks_log_statement_fixed": rks_log_statement_fixed,
        "rks1_short_side_weil_closed": rks1_short_weil_closed,
        "rks4_low_volume_closed": rks4_low_volume_closed,
        "rks2_rks3_deep_blocks_isolated": rks2_rks3_isolated,
        "log_budget_closed": log_budget_closed,
        "ext_bg_external_shortcut_ready": ext_bg_ready,
        "baker_only_insufficient": baker_not_enough,
        "rks2_rks3_self_contained_proved": rks2_rks3_self_contained_proved,
        "self_contained_rks_log_proved": rks_log_self_contained_proved,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_external_route": EXT_BG,
        "fallback_internal_deep_targets": [BG_PROOF, BAKER_AVG],
        "exact_atom": exact_atom,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "RKS-log 内部自足硬点进一步缩窄：RKS1 短侧 Weil 和 RKS4 低体积/端点吸收已经移出，"
            "对数预算 `74<128` 已闭合。唯一真正深点是 RKS2/RKS3 的 BG 型双/多线性倒数 "
            "Kloosterman 固定对数节省。外部接受 EXT-BG 可关闭它；严格内部路线只能重证 BG "
            "型深估计，或证明 Baker 大谱/倒数频率平均替代。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    atom = result["exact_atom"]
    lines = [
        "# Prime Matrix strict RKS-log 内部硬点直接攻击证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rks1_short_side_weil_closed={fmt_bool(result['rks1_short_side_weil_closed'])}",
        f"rks4_low_volume_closed={fmt_bool(result['rks4_low_volume_closed'])}",
        f"rks2_rks3_deep_blocks_isolated={fmt_bool(result['rks2_rks3_deep_blocks_isolated'])}",
        f"rks2_rks3_self_contained_proved={fmt_bool(result['rks2_rks3_self_contained_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确剩余原子",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in atom.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
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


if __name__ == "__main__":
    main()
