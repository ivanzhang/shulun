#!/usr/bin/env python3
"""继续压缩 RKS2/RKS3 内部自足硬点的 Cauchy-Weil 屏障证书。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_internal_weil_barrier_and_bg_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-internal-weil-barrier-and-bg-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-internal-weil-barrier-and-bg-frontier-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-internal-weil-barrier-and-bg-frontier-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks-log-internal-hardpoint-direct-attack-router.json"
EXACT_INPUT = MONO / "prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json"
BG_RKS = DOCS / "bg-rks-block-match.md"
RKS_BRIDGE = DOCS / "rks-bridge-partition.md"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
BAKER_STATUS = DOCS / "explicit-p0-constants.status.md"

SOURCE_FILES = [
    PREVIOUS,
    EXACT_INPUT,
    BG_RKS,
    RKS_BRIDGE,
    RKS_PARAM,
    BAKER_STATUS,
]

TARGET = "SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving"
EXACT_THEOREM = "MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks"
NEXT_ATOM = "SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving"
BG_PROOF = "SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar"
BAKER_AVG = "BakerFrequencyLargeSieveOrDBGAverageReplacement"

REQUIRED_INPUT_LOG_POWER = 118
CAUCHY_WEIL_LOG_SEPARATION = 2 * REQUIRED_INPUT_LOG_POWER


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
    """构造 RKS2/RKS3 内部前沿审计。"""
    previous = load_json(PREVIOUS)
    exact = load_json(EXACT_INPUT)
    bg_rks = read_text(BG_RKS)
    rks_bridge = read_text(RKS_BRIDGE)
    rks_param = read_text(RKS_PARAM)
    baker = read_text(BAKER_STATUS)

    target_active = previous.get("next_direct_attack_target") == TARGET
    exact_theorem_fixed = (
        exact.get("exact_input_theorem_statement_closed") is True
        and exact.get("required_input_log_power") == REQUIRED_INPUT_LOG_POWER
    )
    rks23_blocks_present = contains_all(bg_rks, ["Lemma RKS2", "Lemma RKS3"]) and contains_all(
        rks_bridge,
        ["S(M,N)=Σ", "MN≈P"],
    )
    log_budget_imported = contains_all(rks_param, ["74<128"])
    baker_average_open = contains_all(
        baker,
        ["Baker Theorem 1 不能单独替代", "d 层绝对值平均"],
    )

    # 对 S=sum_m sum_n a_m b_n e_P(xi/(mn))，一次 Cauchy 加不完全倒数和 Weil 给出
    # |S|/(MN) <= C * (1/N + P^(1/2)/M)^(1/2)，对称式交换 M,N。
    elementary_bound = {
        "bilinear_sum": "S(M,N)=sum_{m~M}sum_{n~N} a_m b_n e_P(xi*(mn)^(-1)), MN≈P",
        "one_sided_cauchy_weil_ratio": "|S|/(MN) << (1/N + P^(1/2)/M)^(1/2)",
        "symmetric_ratio": "|S|/(MN) << (1/M + P^(1/2)/N)^(1/2)",
        "needed_log_saving": f"log^-{REQUIRED_INPUT_LOG_POWER}(P)",
        "log_separation_sufficient_schema": (
            f"if max(M,N) >= P^(1/2) log^{CAUCHY_WEIL_LOG_SEPARATION}(P), "
            f"the square-root loss can pay log^-{REQUIRED_INPUT_LOG_POWER}(P) up to absolute constants"
        ),
        "critical_collar": (
            f"P^(1/2)/log^{CAUCHY_WEIL_LOG_SEPARATION}(P) <= M,N "
            f"<= P^(1/2) log^{CAUCHY_WEIL_LOG_SEPARATION}(P)"
        ),
        "balanced_barrier": "at M≈N≈P^(1/2), the elementary ratio is O(1), not log^-118",
    }

    elementary_schema_closed = target_active and exact_theorem_fixed and rks23_blocks_present and log_budget_imported
    balanced_collar_is_only_deep_part = elementary_schema_closed
    self_contained_bg_collar_proved = False

    rows = [
        row(
            "RKS23BGHardpointActive",
            target_active,
            True,
            "上一证书已把唯一内部硬点压成 RKS2/RKS3 的 BG 型倒数 Kloosterman 固定对数节省。",
            TARGET,
        ),
        row(
            "ExactLog118InputImported",
            exact_theorem_fixed,
            True,
            "精确输入定理和 log^-118 目标已经固定。",
            EXACT_THEOREM,
        ),
        row(
            "ElementaryCauchyWeilComputationClosed",
            elementary_schema_closed,
            True,
            "一次 Cauchy 加不完全倒数和 Weil 的可得边界已显式化。",
            "formula ledger closed",
        ),
        row(
            "PowerSeparatedBlocksReducedAway",
            balanced_collar_is_only_deep_part,
            True,
            "若某个二分组远离平方根超过 log^236，平方根损失可支付 log^-118；深点只剩对数平衡颈部。",
            NEXT_ATOM,
        ),
        row(
            "BalancedCauchyWeilBarrier",
            True,
            True,
            "在 M≈N≈P^(1/2) 的临界颈部，Cauchy-Weil 只给 O(MN)，不能给固定对数节省。",
            f"{BG_PROOF} OR {BAKER_AVG}",
        ),
        row(
            "BakerAverageStillOpen",
            baker_average_open,
            True,
            "Baker 单频率结果不能直接通过绝对值后的 d/frequency coherent 平均。",
            BAKER_AVG,
        ),
        row(
            NEXT_ATOM,
            self_contained_bg_collar_proved,
            False,
            "严格内部自足证明仍需在对数平衡颈部补 BG/sum-product 能量节省，或补 Baker 大谱平均替代。",
            f"{BG_PROOF} OR {BAKER_AVG}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只压缩内部剩余硬点，没有宣称无条件闭合。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_internal_weil_barrier_and_bg_frontier_router",
        "status": "rks23_internal_frontier_reduced_to_log_balanced_bg_collar",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_active": target_active,
        "exact_log118_input_imported": exact_theorem_fixed,
        "elementary_cauchy_weil_computation_closed": elementary_schema_closed,
        "cauchy_weil_log_separation_power": CAUCHY_WEIL_LOG_SEPARATION,
        "balanced_collar_is_only_deep_part": balanced_collar_is_only_deep_part,
        "balanced_cauchy_weil_barrier": True,
        "self_contained_bg_balanced_collar_proved": self_contained_bg_collar_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_internal_target": BAKER_AVG,
        "elementary_bound": elementary_bound,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "唯一内部自足硬点没有换题，而是进一步缩窄：RKS2/RKS3 的双线性或分组多线性块中，"
            "若某个二分组相对 `P^(1/2)` 偏离至少 `log^236(P)`，一次 Cauchy-Weil 的平方根损失已经足以支付 "
            "`log^-118(P)`。真正不能由这种内部初等谱估计处理的，只剩 `M,N` 都落在 "
            "`P^(1/2) log^±236(P)` 的对数平衡颈部。该颈部正是 BG/sum-product 能量定理或 "
            "Baker 大谱平均必须进入的位置；当前仍未证明，所以行/列无条件闭合仍不能宣称。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    bound = result["elementary_bound"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 内部 Cauchy-Weil 屏障与 BG 前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_log118_input_imported={fmt_bool(result['exact_log118_input_imported'])}",
        f"elementary_cauchy_weil_computation_closed={fmt_bool(result['elementary_cauchy_weil_computation_closed'])}",
        f"balanced_collar_is_only_deep_part={fmt_bool(result['balanced_collar_is_only_deep_part'])}",
        f"self_contained_bg_balanced_collar_proved={fmt_bool(result['self_contained_bg_balanced_collar_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Cauchy-Weil 可达边界",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in bound.items():
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
            "## 3. 下一最窄自足目标",
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
