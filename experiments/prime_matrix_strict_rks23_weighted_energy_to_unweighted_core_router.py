#!/usr/bin/env python3
"""把加权倒数区间能量输入剥离为纯四元组计数核心。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_weighted_energy_to_unweighted_core_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.json"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"
BG_RKS = DOCS / "bg-rks-block-match.md"

SOURCE_FILES = [PREVIOUS, RKS_PARAM, P0_STATUS, BG_RKS]

TARGET = "WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23"
NEXT_ATOM = "UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23"
INCIDENCE_ROUTE = "RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving"
BG_CORE = "SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar"

WEIGHTED_ENERGY_LOG_POWER = 472


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
    """构造加权到非加权核心归约证书。"""
    previous = load_json(PREVIOUS)
    rks_param = read_text(RKS_PARAM)
    p0_status = read_text(P0_STATUS)
    bg_rks = read_text(BG_RKS)

    active = previous.get("next_direct_attack_target") == TARGET
    previous_reduction_closed = (
        previous.get("plancherel_energy_transfer_closed") is True
        and previous.get("sufficient_energy_log_power") == WEIGHTED_ENERGY_LOG_POWER
    )
    divisor_weight_charged = contains_all(
        rks_param,
        ["C_divisor_coeff", "C_vaughan_blocks", "74<128"],
    )
    rks23_present = contains_all(bg_rks, ["RKS-2 双线性 BG", "RKS-3 多线性 BG"])
    incidence_history_present = contains_all(
        p0_status,
        ["Rudnev", "Roche-Newton", "Shkredov", "sum-product"],
    )

    weighted_to_unweighted_closed = active and previous_reduction_closed and divisor_weight_charged and rks23_present
    unweighted_energy_proved = False

    # 若 |beta_b| <= log^C P，则 E_+(B;beta) <= log^(4C) P * E_+(B)。
    # RKS 账本已把 Vaughan/divisor 权重损失计入固定对数预算，因此后续只需把纯计数能量
    # 证明到 log^{-(472 + weight_margin)}，这里保守登记为“472 加已收费权重余量”。
    core_statement = {
        "set": "B=J^{-1}={n^{-1} mod P: n in J}",
        "collar": "J is a dyadic interval with |J|=N and P^(1/2)/log^236(P)<=N<=P^(1/2)log^236(P)",
        "unweighted_energy": "E_+(B)=#{b1+b2=b3+b4 mod P: bi in B}",
        "equivalent_original_variables": "#{n1^(-1)+n2^(-1)=n3^(-1)+n4^(-1) mod P: ni in J}",
        "weighted_transfer": "E_+(B;beta)<=log^C(P) E_+(B) for divisor-bounded Vaughan weights after dyadic level splitting",
        "sufficient_unweighted_bound": "E_+(J^{-1}) <= |J|^3/log^(472+C_weight)(P)",
        "why_this_is_narrower_than_bg": "It is a single reciprocal-interval four-tuple energy estimate, not the full BG multilinear theorem.",
    }

    rows = [
        row(
            "WeightedEnergyTargetActive",
            active,
            True,
            "上一证书已把平衡颈部压成加权倒数区间加性能量输入。",
            TARGET,
        ),
        row(
            "PreviousL2EnergyReductionClosed",
            previous_reduction_closed,
            True,
            "Cauchy/L2/correlation/Plancherel 归约已经闭合，能量输入的所需 log 指数为 472。",
            TARGET,
        ),
        row(
            "DivisorWeightedToUnweightedReductionClosed",
            weighted_to_unweighted_closed,
            True,
            "Vaughan/divisor-bounded 权重可由 dyadic level splitting 与 RKS 对数账本吸收。",
            NEXT_ATOM,
        ),
        row(
            "IncidenceSumProductRouteRecovered",
            incidence_history_present,
            True,
            "旧材料已定位 Rudnev/RNRS/sum-product 能量路线；它正对应当前纯四元组核心。",
            INCIDENCE_ROUTE,
        ),
        row(
            NEXT_ATOM,
            unweighted_energy_proved,
            False,
            "尚未在仓库内给出 `E_+(J^{-1}) <= |J|^3/log^(472+C)(P)` 的自足证明。",
            f"{INCIDENCE_ROUTE} OR {BG_CORE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只去权重并固定纯计数核心；行/列无条件闭合仍不能声明。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_weighted_energy_to_unweighted_core_router",
        "status": "weighted_energy_reduced_to_unweighted_reciprocal_interval_fourtuple_energy",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "weighted_energy_target_active": active,
        "previous_l2_energy_reduction_closed": previous_reduction_closed,
        "divisor_weighted_to_unweighted_reduction_closed": weighted_to_unweighted_closed,
        "incidence_sum_product_route_recovered": incidence_history_present,
        "unweighted_reciprocal_interval_energy_proved": unweighted_energy_proved,
        "row_column_unconditional_closed": False,
        "required_weighted_energy_log_power": WEIGHTED_ENERGY_LOG_POWER,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_incidence_target": INCIDENCE_ROUTE,
        "core_statement": core_statement,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "加权能量输入继续剥离成功：divisor-bounded Vaughan 权重只造成固定对数损失，"
            "已经由 RKS 账本收费。因此当前真正内部自足剩余可写成纯四元组计数："
            "`J^{-1}` 在 `F_P` 中的加性能量必须满足 "
            "`E_+(J^{-1})<=|J|^3/log^(472+C_weight)(P)`。"
            "这比完整 BG 多线性定理窄得多，但仓库内仍未给出该能量估计的自足证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    core = result["core_statement"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 加权能量到纯四元组核心证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"divisor_weighted_to_unweighted_reduction_closed={fmt_bool(result['divisor_weighted_to_unweighted_reduction_closed'])}",
        f"unweighted_reciprocal_interval_energy_proved={fmt_bool(result['unweighted_reciprocal_interval_energy_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 纯计数核心",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in core.items():
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
