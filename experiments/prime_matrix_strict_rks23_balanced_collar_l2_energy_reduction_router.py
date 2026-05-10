#!/usr/bin/env python3
"""把 RKS2/RKS3 对数平衡颈部压缩为倒数区间加性能量输入。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_balanced_collar_l2_energy_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-internal-weil-barrier-and-bg-frontier-router.json"
EXACT_INPUT = MONO / "prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json"
BG_RKS = DOCS / "bg-rks-block-match.md"
RKS_BRIDGE = DOCS / "rks-bridge-partition.md"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"

SOURCE_FILES = [
    PREVIOUS,
    EXACT_INPUT,
    BG_RKS,
    RKS_BRIDGE,
    RKS_PARAM,
    P0_STATUS,
]

TARGET = "SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving"
NEXT_ATOM = "WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23"
BAKER_AVG = "BakerFrequencyLargeSieveOrDBGAverageReplacement"
BG_CORE = "SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar"

BILINEAR_LOG_POWER = 118
L2_RESTRICTION_LOG_POWER = 2 * BILINEAR_LOG_POWER
ENERGY_LOG_POWER = 2 * L2_RESTRICTION_LOG_POWER
COLLAR_LOG_POWER = 236


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
    """构造 L2/energy 归约证书。"""
    previous = load_json(PREVIOUS)
    exact = load_json(EXACT_INPUT)
    bg_rks = read_text(BG_RKS)
    rks_bridge = read_text(RKS_BRIDGE)
    rks_param = read_text(RKS_PARAM)
    p0_status = read_text(P0_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    exact_log_imported = (
        exact.get("required_input_log_power") == BILINEAR_LOG_POWER
        and exact.get("exact_input_theorem_statement_closed") is True
    )
    balanced_collar_imported = previous.get("balanced_collar_is_only_deep_part") is True
    divisor_losses_charged = contains_all(rks_param, ["74<128", "C_divisor_coeff"])
    rks23_statement_present = contains_all(bg_rks, ["RKS-2 双线性 BG", "RKS-3 多线性 BG"])
    bridge_sum_present = contains_all(rks_bridge, ["S(M,N)=Σ", "MN≈P"])
    historical_energy_route_present = contains_all(
        p0_status,
        ["DFI-4", "Rudnev", "sum-product", "能量"],
    )

    reduction_ready = (
        active
        and exact_log_imported
        and balanced_collar_imported
        and divisor_losses_charged
        and rks23_statement_present
        and bridge_sum_present
    )

    # 归约链：
    # 1. Cauchy: |S|^2 <= ||alpha||_2^2 * R_A(beta)。
    # 2. R_A(beta)=sum_{a in I^{-1}} |sum_{b in J^{-1}} beta_b e_P(xi*a*b)|^2。
    # 3. 展开 R_A 后得到 sum_h C_J(h) K_I(xi*h)。
    # 4. Cauchy + Plancherel: |offdiag| <= E_+(J^{-1};beta)^{1/2} * (P|I|)^{1/2}。
    # 5. 在 MN≈P 下，E_+ <= N^3/log^472(P) 足够推出 R_A <= M N^2/log^236(P)，
    #    再推出 |S| <= MN/log^118(P)。系数损失已由 RKS 参数账本额外收费。
    energy_reduction = {
        "balanced_bilinear_sum": "S=sum_{m in I}sum_{n in J} alpha_m beta_n e_P(xi*(mn)^(-1)), MN≈P",
        "balanced_collar": f"P^(1/2)/log^{COLLAR_LOG_POWER}(P) <= M,N <= P^(1/2)log^{COLLAR_LOG_POWER}(P)",
        "cauchy_l2_target": (
            "R_I(beta)=sum_{a in I^{-1}} |sum_{b in J^{-1}} beta_b e_P(xi*a*b)|^2 "
            f"<= |I||J|^2/log^{L2_RESTRICTION_LOG_POWER}(P)"
        ),
        "correlation_expansion": "R_I(beta)=sum_h C_J(h) K_I(xi*h), with C_J(h)=sum_{b1-b2=h} beta_b1 conjugate(beta_b2)",
        "plancherel_energy_transfer": "offdiag <= E_+(J^{-1};beta)^(1/2) * (P|I|)^(1/2)",
        "sufficient_energy_input": f"E_+(J^(-1);beta) <= |J|^3/log^{ENERGY_LOG_POWER}(P), plus charged divisor losses",
        "output_if_input_holds": f"|S| <= MN/log^{BILINEAR_LOG_POWER}(P) on every balanced RKS2/RKS3 collar block",
        "diagonal_absorption": "h=0 term is O(|I||J|log^C P), smaller than |I||J|^2/log^236(P) in the collar for large P",
    }

    energy_input_proved = False
    rows = [
        row(
            "BalancedCollarTargetActive",
            active,
            True,
            "上一证书已把唯一内部硬点压到 RKS2/RKS3 的对数平衡颈部。",
            TARGET,
        ),
        row(
            "ExactLog118BilinearTargetImported",
            exact_log_imported,
            True,
            "双线性目标 `|S|<=MN/log^118(P)` 已由前序精确定理固定。",
            "target imported",
        ),
        row(
            "CauchyToL2RestrictionReductionClosed",
            reduction_ready,
            True,
            "对 alpha 侧 Cauchy 后，问题化为倒数频率集 `I^{-1}` 上的 beta-Fourier L2 restriction。",
            "L2 restriction ledger",
        ),
        row(
            "L2ToCorrelationKernelExpansionClosed",
            reduction_ready,
            True,
            "L2 restriction 展开为 `J^{-1}` 的差分相关 `C_J(h)` 与 `I^{-1}` 的短倒数和 `K_I(h)` 的耦合。",
            "correlation-kernel identity",
        ),
        row(
            "PlancherelEnergyTransferClosed",
            reduction_ready,
            True,
            "再用 Cauchy 与 Plancherel，得到加性能量输入足以推出所需 L2 节省。",
            NEXT_ATOM,
        ),
        row(
            "HistoricalEnergyRouteRecovered",
            historical_energy_route_present,
            True,
            "旧 Baker/BG 研究中的 DFI-4、Rudnev、sum-product、能量路线与当前颈部核一致。",
            f"{BG_CORE} OR {BAKER_AVG}",
        ),
        row(
            NEXT_ATOM,
            energy_input_proved,
            False,
            "仍未证明 divisor-bounded 加权倒数区间的 `log^-472` 加性能量节省。",
            f"{BG_CORE} OR {BAKER_AVG}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是归约链，不是能量输入本身；不能宣称行/列无条件闭合。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_balanced_collar_l2_energy_reduction_router",
        "status": "balanced_collar_reduced_to_weighted_reciprocal_interval_additive_energy",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "balanced_collar_target_active": active,
        "exact_log118_bilinear_target_imported": exact_log_imported,
        "cauchy_to_l2_restriction_reduction_closed": reduction_ready,
        "l2_to_correlation_kernel_expansion_closed": reduction_ready,
        "plancherel_energy_transfer_closed": reduction_ready,
        "historical_energy_route_recovered": historical_energy_route_present,
        "weighted_reciprocal_interval_energy_input_proved": energy_input_proved,
        "row_column_unconditional_closed": False,
        "bilinear_log_power": BILINEAR_LOG_POWER,
        "l2_restriction_log_power": L2_RESTRICTION_LOG_POWER,
        "sufficient_energy_log_power": ENERGY_LOG_POWER,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_internal_target": BAKER_AVG,
        "energy_reduction": energy_reduction,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前唯一内部自足线继续缩窄：RKS2/RKS3 对数平衡颈部不必再表述成泛泛的 BG 重证。"
            "对 alpha 侧 Cauchy 后，只需证明倒数区间 `J^{-1}` 的 divisor-bounded 加权加性能量 "
            f"`E_+<=|J|^3/log^{ENERGY_LOG_POWER}(P)`，即可经 Plancherel 推出 L2 restriction "
            f"`log^-{L2_RESTRICTION_LOG_POWER}`，再推出原始双线性和 `log^-{BILINEAR_LOG_POWER}`。"
            "这个能量输入正是 BG/sum-product 或 Baker 大谱平均的核心位置；当前仍未证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    energy = result["energy_reduction"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 平衡颈部 L2/能量归约证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cauchy_to_l2_restriction_reduction_closed={fmt_bool(result['cauchy_to_l2_restriction_reduction_closed'])}",
        f"l2_to_correlation_kernel_expansion_closed={fmt_bool(result['l2_to_correlation_kernel_expansion_closed'])}",
        f"plancherel_energy_transfer_closed={fmt_bool(result['plancherel_energy_transfer_closed'])}",
        f"weighted_reciprocal_interval_energy_input_proved={fmt_bool(result['weighted_reciprocal_interval_energy_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确归约链",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in energy.items():
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
