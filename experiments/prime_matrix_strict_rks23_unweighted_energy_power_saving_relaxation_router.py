#!/usr/bin/env python3
"""把倒数区间加性能量的固定对数节省放松为任意固定幂节省。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_unweighted_energy_power_saving_relaxation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
RKS_PARAM = DOCS / "rks-parameter-audit.md"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"

SOURCE_FILES = [PREVIOUS, RKS_PARAM, P0_STATUS]

TARGET = "UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23"
NEXT_ATOM = "UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23"
MOBIUS_OVERLAP = "OneParameterMobiusIntervalOverlapPowerSavingForReciprocalEnergy"
INCIDENCE_ROUTE = "RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving"

COLLAR_LOG_POWER = 236
REQUIRED_LOG_POWER = 472


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
    """构造固定幂节省放松证书。"""
    previous = load_json(PREVIOUS)
    rks_param = read_text(RKS_PARAM)
    p0_status = read_text(P0_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    unweighted_core_fixed = previous.get("divisor_weighted_to_unweighted_reduction_closed") is True
    log_power_imported = previous.get("required_weighted_energy_log_power") == REQUIRED_LOG_POWER
    rks_log_budget_charged = contains_all(rks_param, ["74<128"])
    incidence_route_known = contains_all(p0_status, ["Rudnev", "sum-product", "能量"])

    # 若 N >= P^(1/2)/log^236(P)，则 N^delta >= P^(delta/2)/log^(236delta)(P)，
    # 因而对任意固定 delta>0，N^delta 最终压过 log^(472+C_weight)(P)。
    relaxation_closed = active and unweighted_core_fixed and log_power_imported and rks_log_budget_charged
    fixed_power_saving_proved = False

    relaxation = {
        "old_required_bound": "E_+(J^{-1}) <= |J|^3/log^(472+C_weight)(P)",
        "collar_lower_bound": f"|J| >= P^(1/2)/log^{COLLAR_LOG_POWER}(P)",
        "sufficient_new_bound": "there exists fixed delta_E>0 such that E_+(J^{-1}) <= |J|^(3-delta_E)",
        "absorption_check": (
            "|J|^delta_E >= P^(delta_E/2)/log^(236 delta_E)(P), "
            "which dominates every fixed log power for sufficiently large P"
        ),
        "finite_transition": "large-P transition can be delegated to the existing finite/P0 verification lane once constants are supplied",
        "new_core_advantage": "the remaining input is power saving, not a huge explicit log^472 saving",
    }

    rows = [
        row(
            "LogEnergyTargetActive",
            active,
            True,
            "上一证书已把唯一剩余写成纯倒数区间加性能量对数节省。",
            TARGET,
        ),
        row(
            "FixedPowerSavingImpliesRequiredLogSaving",
            relaxation_closed,
            True,
            "在平方根对数颈部，任何固定幂节省最终压过固定对数损失。",
            NEXT_ATOM,
        ),
        row(
            "IncidenceSumProductRouteStillAligned",
            incidence_route_known,
            True,
            "Rudnev/RNRS/sum-product 路线自然提供的正是固定幂节省形态。",
            INCIDENCE_ROUTE,
        ),
        row(
            NEXT_ATOM,
            fixed_power_saving_proved,
            False,
            "仓库内尚未给出 `E_+(J^{-1}) <= |J|^(3-delta_E)` 的自足证明。",
            f"{MOBIUS_OVERLAP} OR {INCIDENCE_ROUTE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只把目标从固定对数节省放松为固定幂节省；行/列无条件闭合仍不能声明。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_unweighted_energy_power_saving_relaxation_router",
        "status": "unweighted_reciprocal_energy_log_saving_reduced_to_any_fixed_power_saving",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "log_energy_target_active": active,
        "fixed_power_saving_implies_required_log_saving": relaxation_closed,
        "incidence_sum_product_route_still_aligned": incidence_route_known,
        "fixed_power_saving_energy_proved": fixed_power_saving_proved,
        "row_column_unconditional_closed": False,
        "old_required_log_power": REQUIRED_LOG_POWER,
        "collar_log_power": COLLAR_LOG_POWER,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_mobius_overlap_target": MOBIUS_OVERLAP,
        "relaxation": relaxation,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前唯一内部自足剩余继续压窄：无需直接证明 `log^-472` 级加性能量节省。"
            "由于平衡颈部满足 `|J|>=P^(1/2)/log^236(P)`，任意固定正幂节省 "
            "`E_+(J^{-1})<=|J|^(3-delta_E)` 都会在大 P 区间压过全部固定对数损失；"
            "小 P 端仍交给既有有限验证/P0 通道。于是下一真正硬点变为固定幂节省版倒数区间能量。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    relaxation = result["relaxation"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 能量目标固定幂节省放松证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fixed_power_saving_implies_required_log_saving={fmt_bool(result['fixed_power_saving_implies_required_log_saving'])}",
        f"fixed_power_saving_energy_proved={fmt_bool(result['fixed_power_saving_energy_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 放松公式",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in relaxation.items():
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
