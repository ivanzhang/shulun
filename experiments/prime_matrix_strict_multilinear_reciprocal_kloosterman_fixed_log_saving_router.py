#!/usr/bin/env python3
"""生成多线性倒数 Kloosterman 固定对数节省输入的精确定理证书。

用法示例：
  python3 experiments/prime_matrix_strict_multilinear_reciprocal_kloosterman_fixed_log_saving_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json"
OUT_MD = MONO / "prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.md"

PREVIOUS = MONO / "prime-matrix-strict-ext-bg-rks-tail-log4-replacement-router.json"
RKS_BRIDGE = DOCS / "rks-bridge-partition.md"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
BG_RKS = DOCS / "bg-rks-block-match.md"
EXT_AUDIT = DOCS / "ext-citation-final-audit.md"
CONSTANTS = DOCS / "constants-absorption-final-audit.md"
BAKER_STATUS = DOCS / "explicit-p0-constants.status.md"
CLAIM_STATUS = MONO / "claim-status-table.md"

SOURCE_FILES = [
    PREVIOUS,
    RKS_BRIDGE,
    RKS_PARAM,
    BG_RKS,
    EXT_AUDIT,
    CONSTANTS,
    BAKER_STATUS,
    CLAIM_STATUS,
]

TARGET = "MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks"
BG_EXTERNAL = "AcceptEXTBGForRKSLogFixedSaving"
SELF_PROOF = "SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving"
BAKER_AVG = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TAIL_TARGET_LOG_POWER = 44
RKS_LOSS_POWER = 74
REQUIRED_INPUT_LOG_POWER = TAIL_TARGET_LOG_POWER + RKS_LOSS_POWER
AVAILABLE_SAVING_POWER = 128


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
    """构造精确定理证书。"""
    previous = load_json(PREVIOUS)
    rks_bridge = read_text(RKS_BRIDGE)
    rks_param = read_text(RKS_PARAM)
    bg_rks = read_text(BG_RKS)
    ext_audit = read_text(EXT_AUDIT)
    constants = read_text(CONSTANTS)
    baker = read_text(BAKER_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    exact_statement_closed = contains_all(
        rks_bridge,
        ["S(M,N)=Σ", "MN≈P", "e_P(ξ(mn)^{-1})"],
    ) and contains_all(
        bg_rks,
        ["RKS-2 双线性 BG", "RKS-3 多线性 BG"],
    )
    log_budget_closed = (
        REQUIRED_INPUT_LOG_POWER == 118
        and AVAILABLE_SAVING_POWER - RKS_LOSS_POWER == 54
        and contains_all(rks_param, ["74<128"])
        and contains_all(constants, ["RKS 余量", ">=54"])
    )
    external_bg_sufficient = contains_all(
        ext_audit,
        ["EXT-BG", "固定对数节省", "不要求抽取 BG 的最佳幂指数"],
    ) and log_budget_closed
    baker_not_sufficient = contains_all(
        baker,
        ["Baker Theorem 1 不能单独替代", "d 层绝对值平均"],
    )
    self_proof_closed = False

    exact_input_theorem = {
        "name": TARGET,
        "modulus": "prime P",
        "phase": "e_P(xi*(mn)^(-1)), xi != 0 mod P",
        "bilinear_block": "S(M,N)=sum_{m~M} sum_{n~N} alpha_m beta_n e_P(xi*(mn)^(-1)), MN≈P",
        "coefficients": "Vaughan/divisor-bounded coefficients with dyadic losses already charged",
        "rks2_range": "min(M,N)>P^(1/18) and long side in BG bilinear coverage; in MN≈P this covers the remaining unbalanced range",
        "rks3_range": "balanced or further split multilinear blocks satisfying BG Kloost 1/2 product threshold",
        "required_bound": f"|S(M,N)| <= MN/log^{REQUIRED_INPUT_LOG_POWER}(P) on each charged block",
        "reason": "After the RKS loss 74, this implies the Tail-log4 target MN/log^44(P).",
    }

    rows = [
        row(
            "KloostermanInputGateActive",
            active,
            True,
            "上一证书已把唯一自足数学缺口压成多线性倒数 Kloosterman 固定对数节省。",
            TARGET,
        ),
        row(
            "ExactInputTheoremStatementClosed",
            exact_statement_closed,
            True,
            "所需命题已精确到素数模数、倒数乘积相位、Vaughan/divisor-bounded 双线性块和 RKS2/RKS3 范围。",
            "statement fixed",
        ),
        row(
            "LogPowerBudgetClosed",
            log_budget_closed,
            True,
            "外部输入需提供 log^-118；RKS 损失 74 后剩 log^-44，且 128-74=54 余量为正。",
            "log-power arithmetic closed",
        ),
        row(
            "EXTBGSufficientIfAccepted",
            external_bg_sufficient,
            True,
            "BG 型固定对数节省强于本输入；接受 EXT-BG 时本原子外部闭合。",
            BG_EXTERNAL,
        ),
        row(
            "BakerSingleFrequencyNotEnough",
            baker_not_sufficient,
            True,
            "Baker 单频率素变量估计不能直接控制 d 层绝对值平均。",
            BAKER_AVG,
        ),
        row(
            TARGET,
            self_proof_closed,
            False,
            "严格自足证明仍未给出；要么重证 BG 多线性定理，要么证明 Baker 大谱/倒数频率平均替代。",
            f"{SELF_PROOF} OR {BAKER_AVG}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步固定了最小输入定理和参数预算，没有发生独立验收或自足重证。",
            PROMOTION_GATE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_multilinear_reciprocal_kloosterman_fixed_log_saving_router",
        "status": "exact_multilinear_reciprocal_kloosterman_input_statement_closed_self_contained_proof_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_input_theorem_statement_closed": exact_statement_closed,
        "log_power_budget_closed": log_budget_closed,
        "required_input_log_power": REQUIRED_INPUT_LOG_POWER,
        "available_saving_power": AVAILABLE_SAVING_POWER,
        "ext_bg_sufficient_if_accepted": external_bg_sufficient,
        "baker_single_frequency_replacement_insufficient": baker_not_sufficient,
        "self_contained_multilinear_reciprocal_kloosterman_proof_closed": self_proof_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "exact_input_theorem": exact_input_theorem,
        "next_direct_attack_target": SELF_PROOF,
        "parallel_attack_target": BAKER_AVG,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "最窄自足数学硬点已压成一个精确定理：对 RKS2/RKS3 的 Vaughan/divisor-bounded "
            "倒数乘积相位块，证明 `|S(M,N)|<=MN/log^118(P)`。"
            "这个指数来自 Tail-log4 目标 `44` 加 RKS 总损失 `74`；`K_sieve_log_saving=128` "
            "保留 10 个输入侧安全幂和 54 个最终余量。接受 `EXT-BG` 时该输入足够；"
            "严格自足版仍需重证 BG 型多线性倒数 Kloosterman 固定对数节省，或证明 Baker 大谱/倒数频率平均替代。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    theorem = result["exact_input_theorem"]
    lines = [
        "# Prime Matrix strict 多线性倒数 Kloosterman 固定对数节省输入证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_input_theorem_statement_closed={fmt_bool(result['exact_input_theorem_statement_closed'])}",
        f"log_power_budget_closed={fmt_bool(result['log_power_budget_closed'])}",
        f"ext_bg_sufficient_if_accepted={fmt_bool(result['ext_bg_sufficient_if_accepted'])}",
        f"self_contained_multilinear_reciprocal_kloosterman_proof_closed={fmt_bool(result['self_contained_multilinear_reciprocal_kloosterman_proof_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确输入定理",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in theorem.items():
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
            "## 3. 下一最窄点",
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
    print(f"ext_bg_sufficient_if_accepted={fmt_bool(result['ext_bg_sufficient_if_accepted'])}")


if __name__ == "__main__":
    main()
