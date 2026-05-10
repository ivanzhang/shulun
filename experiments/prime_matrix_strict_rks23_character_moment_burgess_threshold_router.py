#!/usr/bin/env python3
"""把四短区间非主角色乘积矩拆成 Burgess 大边长分支与薄包分支。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_character_moment_burgess_threshold_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-character-moment-burgess-threshold-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-character-moment-burgess-threshold-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-character-moment-burgess-threshold-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-product-ratio-character-moment-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving"
NEXT_ATOM = "BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment"
BURGESS_ATOM = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"
THIN_ATOM = "ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale"


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
    """构造 Burgess 阈值分解证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    character_moment_ready = previous.get("centered_l2_equals_nonprincipal_four_interval_moment") is True

    # 对每个 dyadic 矩形包对，有四个区间 A0,A1,B0,B1。
    # 若四个边长都超过 Burgess 阈值 P^(1/4+epsilon)，经典 Burgess 点态界会给
    # |S_I(chi)| <= |I| P^(-delta(epsilon))，从而四重乘积矩有固定幂节省。
    # 这是“充分输入推导”，不是把 Burgess 本身当作仓库内部证明。
    side_length_ledger_closed = active and character_moment_ready
    large_packet_implication_closed = side_length_ledger_closed
    dichotomy_closed = side_length_ledger_closed

    burgess_internalized = False
    thin_packet_absorbed = False
    full_character_moment_closed = burgess_internalized and thin_packet_absorbed

    threshold = {
        "four_intervals": "A0,A1,B0,B1 from one dyadic rectangular packet pair",
        "side_lengths": "H_A0,H_A1,H_B0,H_B1",
        "burgess_threshold": "H_i >= P^(1/4+epsilon_B) for all four sides",
        "large_packet_branch": "all four intervals are above the Burgess threshold",
        "thin_packet_branch": "at least one side is below P^(1/4+epsilon_B)",
        "dichotomy": "every packet pair lies in exactly one of these branches",
        "polylog_loss": "dyadic packet counting contributes only P^o(1), harmless after any fixed power saving",
    }

    large_branch = {
        "assumed_pointwise_input": "for every nonprincipal chi and every interval I with |I|>=P^(1/4+epsilon_B), |S_I(chi)|<=|I| P^(-delta_B)",
        "moment": "sum_{chi!=chi0}|S_A0 S_A1 S_B0 S_B1|^2",
        "direct_sup_bound": "using the pointwise input on all four factors gives <= P * prod_i |I_i|^2 * P^(-8 delta_B)",
        "normalized_l2": "after the 1/(P-1) Plancherel factor this gives prod_i |I_i|^2 * P^(-8 delta_B+o(1))",
        "consequence": "large packets satisfy the fixed-power centered convolution L2 saving",
        "not_yet_internal": "the current corpus has not supplied a self-contained Burgess proof with constants for all packet intervals",
    }

    thin_branch = {
        "definition": "some side length H_i<P^(1/4+epsilon_B)",
        "why_not_automatic": "a thin side reduces packet mass, but without an explicit Cauchy-scale mass ledger it cannot be discarded",
        "needed_ledger": "sum all thin packet-pair contributions and prove they are below the required centered L2 scale by a fixed power",
        "possible_routes": "geometric packing of Whitney boundary boxes OR a direct small-side divisor/energy estimate",
        "current_status": "not proved in the current corpus",
    }

    rows = [
        row(
            "FourIntervalCharacterMomentHardpointActive",
            active,
            True,
            "上一证书已把剩余固定为非主角色四短区间乘积矩。",
            TARGET,
        ),
        row(
            "DyadicSideLengthLedgerClosed",
            side_length_ledger_closed,
            True,
            "每个矩形包对有四个边长，可按 Burgess 阈值做互斥分支。",
            NEXT_ATOM,
        ),
        row(
            "BurgessLargePacketImplicationClosed",
            large_packet_implication_closed,
            True,
            "若四个边长均超过 `P^(1/4+epsilon)` 且 Burgess 点态界可用，则该包对的角色矩有固定幂节省。",
            BURGESS_ATOM,
        ),
        row(
            "BurgessPointwiseInputInternalized",
            burgess_internalized,
            burgess_internalized,
            "仓库内尚未给出适配全部 dyadic 包的自足 Burgess 点态证明与常数账本。",
            BURGESS_ATOM,
        ),
        row(
            "ThinPacketBranchIsOnlyNonBurgessBranch",
            dichotomy_closed,
            True,
            "不满足大边长条件的包对必含一个 Burgess 阈值以下的短边。",
            THIN_ATOM,
        ),
        row(
            "ThinDyadicPacketMassAbsorptionProved",
            thin_packet_absorbed,
            thin_packet_absorbed,
            "仓库内尚未证明所有薄包对总贡献在 Cauchy 尺度下可固定幂吸收。",
            THIN_ATOM,
        ),
        row(
            NEXT_ATOM,
            full_character_moment_closed,
            full_character_moment_closed,
            "需要同时内部化大包 Burgess 输入并完成薄包质量吸收，才能闭合四区间角色矩。",
            f"{BURGESS_ATOM} AND {THIN_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是 Burgess 阈值分解和大包充分推导，不是最终角色矩节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_character_moment_burgess_threshold_router",
        "status": "four_interval_character_moment_split_into_large_burgess_packets_and_thin_packets",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "four_interval_character_moment_hardpoint_active": active,
        "dyadic_side_length_ledger_closed": side_length_ledger_closed,
        "burgess_large_packet_implication_closed": large_packet_implication_closed,
        "burgess_pointwise_input_internalized": burgess_internalized,
        "thin_packet_branch_is_only_non_burgess_branch": dichotomy_closed,
        "thin_dyadic_packet_mass_absorption_proved": thin_packet_absorbed,
        "four_interval_character_moment_power_saving_proved": full_character_moment_closed,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "required_subatoms": [BURGESS_ATOM, THIN_ATOM],
        "threshold": threshold,
        "large_branch": large_branch,
        "thin_branch": thin_branch,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "四短区间非主角色乘积矩进一步压成 Burgess 阈值二分。"
            "在四个区间都长于 `P^(1/4+epsilon)` 的大包分支中，"
            "只要内部化 Burgess 点态角色和节省，就可直接推出固定幂矩节省。"
            "所有剩余包对必含一个短于 Burgess 阈值的薄边；这部分不能凭直觉丢弃，"
            "还需要一个 Cauchy 尺度下的薄包总质量吸收账本。"
            "因此当前自足闭合还剩两个具体子输入：大包 Burgess 内部化与薄包质量吸收。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 角色矩 Burgess 阈值分解证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dyadic_side_length_ledger_closed={fmt_bool(result['dyadic_side_length_ledger_closed'])}",
        f"burgess_large_packet_implication_closed={fmt_bool(result['burgess_large_packet_implication_closed'])}",
        f"burgess_pointwise_input_internalized={fmt_bool(result['burgess_pointwise_input_internalized'])}",
        f"thin_dyadic_packet_mass_absorption_proved={fmt_bool(result['thin_dyadic_packet_mass_absorption_proved'])}",
        f"four_interval_character_moment_power_saving_proved={fmt_bool(result['four_interval_character_moment_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 阈值二分",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["threshold"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 大包 Burgess 分支",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["large_branch"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 薄包分支",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["thin_branch"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
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
