#!/usr/bin/env python3
"""生成 strict 同参数每层冷支撑指数表路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_parameter_per_level_support_exponent_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-parameter-per-level-support-exponent-router.json

输出：
  docs/monograph/prime-matrix-strict-same-parameter-per-level-support-exponent-router.json
  docs/monograph/prime-matrix-strict-same-parameter-per-level-support-exponent-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-same-parameter-per-level-support-exponent-router.json"
OUT_MD = DOCS / "prime-matrix-strict-same-parameter-per-level-support-exponent-router.md"

PER_LEVEL = "SameParameterPerLevelColdSupportExponentTable"
ACTIVE_PACKING = "ActivePrefixLevelPackingExponentTable"
COLLAR_SUM = "SameParameterSiblingCollarWidthFiniteSumTable"
TPDEC_TABLE = "SameParameterPDECThresholdNumericTable"
LOAD_LOWER = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
DEPTH_TELESCOPE = "ColdSupportDepthTelescopingContractionOrLogAbsorptionTable"
SUPPORT_TABLE = "CoreHistoryWeightedSupportMeasureTable"
PARENT_SUPPORT = "ParentScaledChildUnionSupportNumericEnvelope"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
COLLAR_LCM = "SiblingCollarWidthLCMKernelCompressionLedger"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG_EPSILON = 0.25
RESIDUAL_EXPONENT = ALPHA - LOG_EPSILON

SOURCE_FILES = [
    "prime-matrix-strict-cold-support-depth-telescoping-router.json",
    "prime-matrix-strict-core-history-weighted-support-measure-router.json",
    "prime-matrix-strict-sibling-numeric-envelope-attack-router.json",
    "prime-matrix-strict-parent-support-numeric-envelope-router.json",
    "prime-matrix-strict-sibling-collar-cap-table-router.json",
    "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_same_parameter_per_level_support_exponent_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decomposition_rows() -> list[dict[str, str]]:
    """列出每层支撑的分解。"""
    return [
        {
            "piece": "active prefix set",
            "formula": "A_j={U: depth(U)=j, U remains cold and nonpersistent}",
            "status": "closed_definition",
            "meaning": "每层支撑必须先按活动父前缀集合打包。",
        },
        {
            "piece": "base projected support",
            "formula": "B_j=sum_{U in A_j} |pi(F_U)|",
            "status": "geometry_closed_numeric_open",
            "meaning": "同父兄弟支撑投影到父扩张窗口，但跨父前缀求和仍需打包。",
        },
        {
            "piece": "collar debit",
            "formula": "C_j=sum_{U in A_j} C_col(U)",
            "status": "cap_closed_sum_open",
            "meaning": "单 collar cap 已闭合，跨层/同层总和仍需有限和或 LCM 压缩。",
        },
        {
            "piece": "overlap and persistence",
            "formula": "E_j=sum_U E_overlap(U)+E_persistent(U)",
            "status": "named_return_registered",
            "meaning": "重复收费或持久历史不留在非持久冷支撑，进入命名回流。",
        },
        {
            "piece": "per-level exponent target",
            "formula": "S_j=B_j+C_j <= P^beta with beta+tau<0.18",
            "status": "open",
            "meaning": "这是深度对数吸收后剩下的真正指数表。",
        },
    ]


def obstruction_rows() -> list[dict[str, Any]]:
    """给出同层活动前缀过多的阻塞样本。"""
    rows: list[dict[str, Any]] = []
    for gamma in [0.10, 0.18, 0.20, 0.30]:
        for tau in [0.00, 0.05]:
            total = gamma + tau
            rows.append(
                {
                    "active_prefix_exponent_gamma": gamma,
                    "unit_support_per_prefix": 1,
                    "tpdec_exponent_tau": tau,
                    "required_gamma_plus_tau_lt": round(RESIDUAL_EXPONENT, 6),
                    "passes_residual_budget": total < RESIDUAL_EXPONENT,
                    "margin": round(RESIDUAL_EXPONENT - total, 6),
                }
            )
    return rows


def route_rows() -> list[dict[str, str]]:
    """列出每层指数表的路线拆分。"""
    return [
        {
            "route": ACTIVE_PACKING,
            "task": "证明同层活动父前缀的投影支撑不会以超过 P^(0.18-tau) 的指数增长。",
            "status": "open",
        },
        {
            "route": COLLAR_SUM,
            "task": "证明 collar 宽度总和可直接有限求和吸收；否则沿 LCM/共同核回流。",
            "status": "open_or_routed",
        },
        {
            "route": LOW_KERNEL,
            "task": "若活动前缀密集来自低乘子共同核，必须进入有界小商 SAE/PDEC 或固定历史。",
            "status": "registered_not_final_excluded",
        },
        {
            "route": TPDEC_TABLE,
            "task": "给出同参数持久阈值指数 tau；tau 越大，每层支撑可用指数越小。",
            "status": "open",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "PerLevelSupportTargetImported",
            result["per_level_support_target_imported"],
            result["per_level_support_target_imported"],
            "深度伸缩已把剩余压成每层冷支撑指数表。",
            PER_LEVEL,
        ),
        row(
            "ResidualExponentBudgetComputed",
            result["residual_exponent_budget_computed"],
            result["residual_exponent_budget_computed"],
            "对数因子 P^1/4 已扣除，alpha=0.43 剩余指数预算为 0.18。",
            f"{PER_LEVEL} AND {TPDEC_TABLE}",
        ),
        row(
            "PerLevelChargeDecompositionClosed",
            result["per_level_charge_decomposition_closed"],
            result["per_level_charge_decomposition_closed"],
            "每层支撑可分解为活动前缀投影支撑、collar debit 与命名回流。",
            f"{ACTIVE_PACKING} AND {COLLAR_SUM}",
        ),
        row(
            "TrivialActivePrefixBoundRejected",
            result["trivial_active_prefix_bound_rejected"],
            result["trivial_active_prefix_bound_rejected"],
            "若同层活动前缀数达到 P^0.2，即使每个只贡献 1 也超过剩余预算。",
            ACTIVE_PACKING,
        ),
        row(
            "CollarRouteImported",
            result["collar_route_imported"],
            result["collar_route_imported"],
            "collar 单项 cap 与宽度 LCM/共同核压缩已可调用，但直接同层有限总和仍未给出。",
            f"{COLLAR_SUM} OR {COLLAR_LCM}",
        ),
        row(
            "SameParameterPerLevelColdSupportExponentTableProved",
            False,
            False,
            "尚未证明活动前缀打包指数和 collar 同层总和满足 beta+tau<0.18。",
            f"{ACTIVE_PACKING} AND {COLLAR_SUM} AND {TPDEC_TABLE}",
        ),
        row(
            "DepthTelescopingTableProved",
            False,
            False,
            "每层指数表未闭合，因此深度伸缩无法升级为全深度加权支撑界。",
            f"{PER_LEVEL} AND {TPDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{ACTIVE_PACKING} AND {TPDEC_TABLE} AND {LOAD_LOWER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造每层冷支撑指数表证书。"""
    depth = load_json("prime-matrix-strict-cold-support-depth-telescoping-router.json")
    support = load_json("prime-matrix-strict-core-history-weighted-support-measure-router.json")
    sibling = load_json("prime-matrix-strict-sibling-numeric-envelope-attack-router.json")
    parent = load_json("prime-matrix-strict-parent-support-numeric-envelope-router.json")
    collar_cap = load_json("prime-matrix-strict-sibling-collar-cap-table-router.json")
    collar_lcm = load_json("prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json")

    target = depth.get("next_direct_attack_target") == PER_LEVEL
    residual_ok = (
        depth.get("explicit_log_quarter_absorption_closed") is True
        and abs(float(depth.get("remaining_exponent_after_log_absorption", 0.0)) - RESIDUAL_EXPONENT) < 1e-9
    )
    decomposition = (
        support.get("single_layer_support_envelope_closed") is True
        and sibling.get("sibling_multiset_projection_identity_proved") is True
        and parent.get("projected_support_to_dilated_parent_window_proved") is True
    )
    collar_route = (
        collar_cap.get("same_parameter_collar_short_divisor_cap_table_proved") is True
        and collar_lcm.get("width_lcm_kernel_compression_proved") is True
    )
    obstruction = any(
        (not item["passes_residual_budget"])
        for item in obstruction_rows()
        if item["active_prefix_exponent_gamma"] >= 0.2 and item["tpdec_exponent_tau"] == 0.0
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_same_parameter_per_level_support_exponent_router",
        "status": "per_level_support_exponent_reduced_to_active_prefix_packing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha": ALPHA,
        "log_absorption_epsilon": LOG_EPSILON,
        "residual_exponent_after_log_absorption": round(RESIDUAL_EXPONENT, 6),
        "per_level_support_target_imported": target,
        "residual_exponent_budget_computed": residual_ok,
        "per_level_charge_decomposition_closed": decomposition,
        "trivial_active_prefix_bound_rejected": obstruction,
        "collar_route_imported": collar_route,
        "active_prefix_level_packing_exponent_table_proved": False,
        "same_parameter_sibling_collar_width_finite_sum_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "same_parameter_per_level_cold_support_exponent_table_proved": False,
        "cold_support_depth_telescoping_contraction_or_log_absorption_table_proved": False,
        "core_history_weighted_support_measure_table_proved": False,
        "core_threshold_summation_dominance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PER_LEVEL,
        "hardpoint_after_router": f"{ACTIVE_PACKING} AND {COLLAR_SUM} AND {TPDEC_TABLE}",
        "next_direct_attack_target": ACTIVE_PACKING,
        "parallel_attack_targets": [
            COLLAR_SUM,
            TPDEC_TABLE,
            LOAD_LOWER,
            NAMED_RETURN,
            HOT_CORE,
            FIXED_HISTORY,
            DSTRUCTURE,
        ],
        "decomposition_rows": decomposition_rows(),
        "obstruction_rows": obstruction_rows(),
        "route_rows": route_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SameParameterPerLevelColdSupportExponentTable` 继续下钻后，真正困难集中在同层活动前缀打包。"
            "对数深度已经消耗 `P^(1/4)`，`alpha=0.43` 只剩 `0.18` 的指数预算给"
            "每层冷支撑和 `T_PDEC` 权重；因此需要 `beta+tau<0.18`。"
            "现有材料能把单父兄弟收费分解为父投影支撑、collar debit 和命名回流，"
            "但不能阻止同层活动父前缀数本身达到 `P^0.2` 这类超预算规模。"
            "最新最窄点是 `ActivePrefixLevelPackingExponentTable`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 同参数每层冷支撑指数表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"per_level_support_target_imported={fmt_bool(result['per_level_support_target_imported'])}",
        f"residual_exponent_budget_computed={fmt_bool(result['residual_exponent_budget_computed'])}",
        f"per_level_charge_decomposition_closed={fmt_bool(result['per_level_charge_decomposition_closed'])}",
        f"trivial_active_prefix_bound_rejected={fmt_bool(result['trivial_active_prefix_bound_rejected'])}",
        f"collar_route_imported={fmt_bool(result['collar_route_imported'])}",
        f"same_parameter_per_level_cold_support_exponent_table_proved={fmt_bool(result['same_parameter_per_level_cold_support_exponent_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 每层支撑分解",
        "",
        "| piece | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["decomposition_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['piece'])}`",
                    table_cell(item["formula"]),
                    f"`{table_cell(item['status'])}`",
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 活动前缀阻塞",
            "",
            "| gamma active prefixes | unit support | tau T_PDEC | required gamma+tau < | passes | margin |",
            "| ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in result["obstruction_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["active_prefix_exponent_gamma"]),
                    str(item["unit_support_per_prefix"]),
                    str(item["tpdec_exponent_tau"]),
                    str(item["required_gamma_plus_tau_lt"]),
                    f"`{fmt_bool(item['passes_residual_budget'])}`",
                    str(item["margin"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 路线拆分",
            "",
            "| route | task | status |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["route_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['route'])}`",
                    table_cell(item["task"]),
                    f"`{table_cell(item['status'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行：`{COLLAR_SUM}`、`{TPDEC_TABLE}`、`{LOAD_LOWER}`。",
            "- 边界：本步关闭每层支撑的结构分解和指数预算门槛；未证明活动前缀打包指数。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """入口函数。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"per_level_charge_decomposition_closed={fmt_bool(result['per_level_charge_decomposition_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
