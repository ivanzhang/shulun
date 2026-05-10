#!/usr/bin/env python3
"""用最短边 Plancherel 吸收非微观薄包，并隔离微薄边剩余。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_thin_packet_plancherel_floor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-thin-packet-plancherel-floor-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-thin-packet-plancherel-floor-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-thin-packet-plancherel-floor-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-character-moment-burgess-threshold-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale"
GLOBAL_TARGET = "BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment"
NEXT_ATOM = "MicroscopicThinSidePacketMassAbsorptionAtCauchyScale"
BURGESS_ATOM = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


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
    """构造薄包 Plancherel 地板证书。"""
    previous = load_json(PREVIOUS)
    thin_required = TARGET in previous.get("required_subatoms", [])
    global_active = previous.get("next_direct_attack_target") == GLOBAL_TARGET
    side_ledger = previous.get("dyadic_side_length_ledger_closed") is True
    thin_branch_ready = previous.get("thin_packet_branch_is_only_non_burgess_branch") is True

    active = thin_required and global_active and side_ledger and thin_branch_ready

    # 对四个区间 I1,I2,I3,I4 的非主角色矩：
    # M=sum_{chi!=chi0} prod |S_Ij(chi)|^2。
    # 若最短边 H_min >= P^kappa，则对最短边用 Plancherel：
    # sum_chi |S_min(chi)|^2 <= (P-1)H_min；
    # 其余三边用 |S_I|<=H_I。除以 Plancherel 的 1/(P-1) 后，
    # L2 <= H_min * prod_{j!=min} H_j^2 = (prod H_j^2)/H_min，
    # 因而得到 P^-kappa 的固定幂节省。
    shortest_side_plancherel_closed = active
    nonmicroscopic_absorbed = active
    microscopic_remaining = active

    thin_branch_fully_absorbed = False
    burgess_still_open = previous.get("burgess_pointwise_input_internalized") is not True

    floor = {
        "four_intervals": "I1,I2,I3,I4 = A0,A1,B0,B1",
        "side_lengths": "H_j=|I_j| and H_min=min_j H_j",
        "burgess_upper_thin_condition": "thin branch has H_min<P^(1/4+epsilon_B)",
        "new_power_floor": "choose fixed kappa>0; split thin packets by H_min>=P^kappa or H_min<P^kappa",
        "nonmicroscopic_thin_packet": "P^kappa <= H_min < P^(1/4+epsilon_B)",
        "microscopic_thin_packet": "H_min<P^kappa",
        "why_this_is_narrower": "all fixed-power-length thin packets are absorbed by Plancherel; only microscopic side packets remain",
    }

    estimate = {
        "moment": "M=sum_{chi!=chi0}|S_I1(chi)S_I2(chi)S_I3(chi)S_I4(chi)|^2",
        "plancherel_on_shortest_side": "sum_chi |S_min(chi)|^2 <= (P-1)H_min",
        "trivial_on_other_sides": "|S_I(chi)|<=H_I",
        "raw_bound": "M <= (P-1) H_min * prod_{j!=min} H_j^2",
        "normalized_l2_bound": "(1/(P-1))M <= H_min * prod_{j!=min} H_j^2",
        "relative_to_natural_packet_scale": "H_min * prod_{j!=min} H_j^2 = (prod_j H_j^2)/H_min",
        "fixed_power_saving": "if H_min>=P^kappa then normalized L2 <= prod_j H_j^2 * P^(-kappa)",
        "conclusion": "nonmicroscopic thin packets satisfy the Cauchy-scale fixed-power saving without Burgess",
    }

    remaining = {
        "microscopic_side_problem": "prove the total contribution of packet pairs with H_min<P^kappa is absorbable",
        "why_not_closed_here": "when H_min is below every fixed power, the Plancherel gain 1/H_min is not a fixed power",
        "possible_next_routes": "Whitney packing mass ledger, endpoint strip counting, or divisor-energy estimate for microscopic sides",
        "global_parallel_open": BURGESS_ATOM if burgess_still_open else "none",
    }

    rows = [
        row(
            "ThinPacketSubatomActive",
            active,
            True,
            "上一证书已把闭合义务之一固定为薄包总质量吸收。",
            TARGET,
        ),
        row(
            "ShortestSidePlancherelEstimateClosed",
            shortest_side_plancherel_closed,
            True,
            "对最短边用角色 Plancherel，其余边用平凡上界，得到 `prod H_j^2/H_min`。",
            "nonmicroscopic thin packets",
        ),
        row(
            "NonmicroscopicThinPacketsAbsorbed",
            nonmicroscopic_absorbed,
            True,
            "若 `H_min>=P^kappa`，则相对自然包尺度得到 `P^-kappa` 固定幂节省。",
            "absorbed",
        ),
        row(
            "MicroscopicThinPacketsIsolated",
            microscopic_remaining,
            True,
            "薄包中唯一未被该初等 Plancherel 估计吸收的是 `H_min<P^kappa` 的微薄边包。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明微薄边包对的总贡献可在 Cauchy 尺度下固定幂吸收。",
            "WhitneyBoundaryPacking OR MicroscopicSideDivisorEnergy",
        ),
        row(
            "BurgessPointwiseInputStillOpen",
            burgess_still_open,
            False,
            "大包分支仍需自足 Burgess 点态角色和输入；本证书只推进薄包分支。",
            BURGESS_ATOM,
        ),
        row(
            "ThinDyadicPacketMassAbsorptionProved",
            thin_branch_fully_absorbed,
            thin_branch_fully_absorbed,
            "薄包分支已去掉非微观部分，但微薄边总质量账本尚未完成。",
            NEXT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是非微观薄包吸收，不是 Burgess 阈值总闭合。",
            f"{BURGESS_ATOM} AND {NEXT_ATOM}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_thin_packet_plancherel_floor_router",
        "status": "nonmicroscopic_thin_packets_absorbed_microscopic_side_packets_remain",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "thin_packet_subatom_active": active,
        "shortest_side_plancherel_estimate_closed": shortest_side_plancherel_closed,
        "nonmicroscopic_thin_packets_absorbed": nonmicroscopic_absorbed,
        "microscopic_thin_packets_isolated": microscopic_remaining,
        "microscopic_thin_side_packet_mass_absorption_proved": False,
        "burgess_pointwise_input_still_open": burgess_still_open,
        "thin_dyadic_packet_mass_absorption_proved": thin_branch_fully_absorbed,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_required_target": BURGESS_ATOM,
        "floor": floor,
        "estimate": estimate,
        "remaining": remaining,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "薄包分支已经进一步缩窄。设四个边长为 `H_j`，最短边为 `H_min`。"
            "对最短边用乘法角色 Plancherel、其余三边用平凡上界，得到归一化 L2 "
            "`<= (prod H_j^2)/H_min`。因此只要 `H_min>=P^kappa`，"
            "就有 `P^-kappa` 固定幂节省，非微观薄包可内部吸收。"
            "真正剩余只剩 `H_min<P^kappa` 的微薄边包总质量账本；"
            "同时大包分支的 Burgess 点态输入仍需单独内部化。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 薄包 Plancherel 地板证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"shortest_side_plancherel_estimate_closed={fmt_bool(result['shortest_side_plancherel_estimate_closed'])}",
        f"nonmicroscopic_thin_packets_absorbed={fmt_bool(result['nonmicroscopic_thin_packets_absorbed'])}",
        f"microscopic_thin_packets_isolated={fmt_bool(result['microscopic_thin_packets_isolated'])}",
        f"microscopic_thin_side_packet_mass_absorption_proved={fmt_bool(result['microscopic_thin_side_packet_mass_absorption_proved'])}",
        f"burgess_pointwise_input_still_open={fmt_bool(result['burgess_pointwise_input_still_open'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 薄包地板分解",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["floor"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 最短边 Plancherel 估计",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["estimate"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 剩余",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["remaining"].items():
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
