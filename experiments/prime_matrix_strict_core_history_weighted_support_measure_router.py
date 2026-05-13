#!/usr/bin/env python3
"""生成 strict 冷历史加权支撑测度路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_core_history_weighted_support_measure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-core-history-weighted-support-measure-router.json

输出：
  docs/monograph/prime-matrix-strict-core-history-weighted-support-measure-router.json
  docs/monograph/prime-matrix-strict-core-history-weighted-support-measure-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-core-history-weighted-support-measure-router.json"
OUT_MD = DOCS / "prime-matrix-strict-core-history-weighted-support-measure-router.md"

SUPPORT_TABLE = "CoreHistoryWeightedSupportMeasureTable"
CORE_SUM = "SameParameterCoreThresholdSummationDominanceTable"
DEPTH_TELESCOPE = "ColdSupportDepthTelescopingContractionOrLogAbsorptionTable"
TPDEC_WEIGHT = "SameParameterPDECThresholdNumericTable"
ROOT_DEMAND = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
FINITE_RUNNER = "FiniteColdHistorySummationRunnerOrAnalyticEnvelope"
SIBLING_LEDGER = "CanonicalColdWindowSiblingChargingOrHotReturnLedger"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
PARENT_SUPPORT = "ParentScaledChildUnionSupportNumericEnvelope"
PARENT_DILATED = "ParentSiblingDilatedWindowColdCoreThresholdTable"
COLLAR_WIDTH = "SiblingCollarWidthLCMKernelCompressionLedger"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
NO_FREE_RETURN = "CommonKernelReturnCycleDescentOrPDECLedger"
PRIME_POWER = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
FANIN = "MultiSourceKernelFanInSAEOrPDECExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-same-parameter-core-threshold-summation-router.json",
    "prime-matrix-strict-effective-cold-history-pruning-router.json",
    "prime-matrix-strict-cold-window-sibling-charging-router.json",
    "prime-matrix-strict-sibling-numeric-envelope-attack-router.json",
    "prime-matrix-strict-parent-support-numeric-envelope-router.json",
    "prime-matrix-strict-parent-dilated-window-threshold-router.json",
    "prime-matrix-strict-sibling-collar-cap-table-router.json",
    "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json",
    "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json",
    "prime-matrix-strict-multisource-fanin-small-quotient-router.json",
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
        "experiments/prime_matrix_strict_core_history_weighted_support_measure_router.py": sha256(
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


def tree_decomposition_rows() -> list[dict[str, str]]:
    """列出冷历史支撑树的分解。"""
    return [
        {
            "piece": "prefix tree",
            "formula": "nodes U, children W=U*g, residual H_U=h_0/D(U)",
            "status": "closed_interface",
            "meaning": "实际冷历史支撑可以按前缀树分层，而不是无结构形式词集合。",
        },
        {
            "piece": "sibling layer charge",
            "formula": "sum_{g child of U} C_core(U*g) <= C_sib(U)+E_hot/fixed/PDEC(U)",
            "status": "ledger_closed_numeric_open",
            "meaning": "同父兄弟族必须整体收费，超额不再留在冷供给。",
        },
        {
            "piece": "parent projection",
            "formula": "C_sib(U)=|pi(F_U)|, pi(g,k)=gk, plus overlap debt",
            "status": "identity_closed",
            "meaning": "兄弟收费可投回父频率除数支撑，重复投影进入命名回流。",
        },
        {
            "piece": "dilated parent window",
            "formula": "pi(F_U) subset {d|H_U: d in [L_*,R_*]}",
            "status": "geometry_closed",
            "meaning": "父投影支撑落入单个 collar 扩张父窗口。",
        },
        {
            "piece": "cross-depth summation",
            "formula": "sum_depth sum_U C_sib(U) needs contraction or log absorption",
            "status": "open",
            "meaning": "单层收费闭合后，还要控制沿前缀树所有深度的累计支撑。",
        },
    ]


def depth_obstruction_rows() -> list[dict[str, Any]]:
    """给出单层账本不能推出全深度测度的见证。"""
    samples: list[dict[str, Any]] = []
    for depth in [4, 8, 16, 32]:
        samples.append(
            {
                "depth": depth,
                "per_level_parent_support": 1,
                "single_level_bound_valid": True,
                "total_support_without_contraction": depth,
                "root_support_bound": 1,
                "shows_gap": depth > 1,
            }
        )
    return samples


def envelope_rows() -> list[dict[str, str]]:
    """列出支撑测度表闭合所需的最小 envelope。"""
    return [
        {
            "input": DEPTH_TELESCOPE,
            "role": "把单层 sibling envelope 沿前缀树求和，证明总支撑不超过根势能、对数吸收项或命名回流。",
            "status": "open",
        },
        {
            "input": TPDEC_WEIGHT,
            "role": "把未加权支撑升级为 (T_PDEC(W)-1) 加权支撑，并保持同一参数账本。",
            "status": "open",
        },
        {
            "input": FINITE_RUNNER,
            "role": "在有限边界/低 P 区段对实际冷历史族直接枚举或用解析 envelope 补齐。",
            "status": "open",
        },
        {
            "input": ROOT_DEMAND,
            "role": "将支撑供给上界与早期零行反例链强制负载作同参数严格比较。",
            "status": "open",
        },
    ]


def log_absorption_samples() -> list[dict[str, Any]]:
    """给出对数深度相对 P^0.43 的简单吸收样本。"""
    samples: list[dict[str, Any]] = []
    alpha = 0.43
    for p_value in [100_000, 1_000_000, 10_000_000, 1_000_000_000]:
        depth_cap = math.floor(math.log(p_value, 2)) + 1
        p_alpha = p_value**alpha
        samples.append(
            {
                "P": p_value,
                "depth_cap_floor_log2_plus_1": depth_cap,
                "P_alpha": round(p_alpha, 6),
                "log_depth_absorbed_by_P_alpha": depth_cap < p_alpha,
                "margin": round(p_alpha - depth_cap, 6),
            }
        )
    return samples


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "SupportMeasureTargetImported",
            result["support_measure_target_imported"],
            result["support_measure_target_imported"],
            "上一层已把核心阈值求和优势压成实际冷历史加权支撑测度。",
            SUPPORT_TABLE,
        ),
        row(
            "ActualColdPrefixTreeDomainClosed",
            result["actual_cold_prefix_tree_domain_closed"],
            result["actual_cold_prefix_tree_domain_closed"],
            "有效剪枝接口给出 D(W)|h_0 与 H_W=h_0/D(W)，故支撑可按前缀树组织。",
            SUPPORT_TABLE,
        ),
        row(
            "SiblingLayerProjectionLedgerImported",
            result["sibling_layer_projection_ledger_imported"],
            result["sibling_layer_projection_ledger_imported"],
            "同父兄弟族的单层收费已投影到父支撑、overlap、collar 和命名回流。",
            f"{SIBLING_LEDGER} AND {PARENT_SUPPORT}",
        ),
        row(
            "CollarAndKernelReturnDisciplineImported",
            result["collar_and_kernel_return_discipline_imported"],
            result["collar_and_kernel_return_discipline_imported"],
            "collar 宽度爆发和共同核回流已不能作为免费冷供给循环。",
            f"{COLLAR_WIDTH} AND {LOW_KERNEL} AND {NO_FREE_RETURN}",
        ),
        row(
            "PrimePowerAndFanInIndependentExitsRemoved",
            result["prime_power_and_fanin_independent_exits_removed"],
            result["prime_power_and_fanin_independent_exits_removed"],
            "单素数幂形式爆炸已规范化，多源 fan-in 已压成有界小商 SAE/PDEC。",
            f"{PRIME_POWER} AND {FANIN}",
        ),
        row(
            "SingleLayerSupportEnvelopeClosed",
            result["single_layer_support_envelope_closed"],
            result["single_layer_support_envelope_closed"],
            "每个父前缀的一层兄弟冷支撑已经没有无名出口。",
            DEPTH_TELESCOPE,
        ),
        row(
            "DepthTelescopingGapCertified",
            result["depth_telescoping_gap_certified"],
            result["depth_telescoping_gap_certified"],
            "单层 envelope 不能自动推出全深度总支撑；需要收缩或对数吸收表。",
            DEPTH_TELESCOPE,
        ),
        row(
            "CoreHistoryWeightedSupportMeasureTableProved",
            False,
            False,
            "尚未证明跨层总支撑测度在同参数预算内足够小。",
            f"{DEPTH_TELESCOPE} AND {TPDEC_WEIGHT} AND {FINITE_RUNNER}",
        ),
        row(
            "CoreThresholdSummationDominanceProved",
            False,
            False,
            "支撑测度、T_PDEC 权重和需求端下界仍未完成闭合比较。",
            f"{SUPPORT_TABLE} AND {TPDEC_WEIGHT} AND {ROOT_DEMAND}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{DEPTH_TELESCOPE} AND {TPDEC_WEIGHT} AND {ROOT_DEMAND} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造冷历史加权支撑测度证书。"""
    summation = load_json("prime-matrix-strict-same-parameter-core-threshold-summation-router.json")
    pruning = load_json("prime-matrix-strict-effective-cold-history-pruning-router.json")
    sibling = load_json("prime-matrix-strict-cold-window-sibling-charging-router.json")
    sibling_numeric = load_json("prime-matrix-strict-sibling-numeric-envelope-attack-router.json")
    parent_support = load_json("prime-matrix-strict-parent-support-numeric-envelope-router.json")
    parent_dilated = load_json("prime-matrix-strict-parent-dilated-window-threshold-router.json")
    collar_cap = load_json("prime-matrix-strict-sibling-collar-cap-table-router.json")
    collar_lcm = load_json("prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json")
    no_free = load_json("prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    prime_power = load_json("prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json")
    fanin = load_json("prime-matrix-strict-multisource-fanin-small-quotient-router.json")

    target = summation.get("next_direct_attack_target") == SUPPORT_TABLE
    tree_domain = (
        pruning.get("effective_pruning_interface_closed") is True
        and pruning.get("divisor_compatibility_interface_closed") is True
    )
    sibling_projection = (
        sibling.get("canonical_cold_window_sibling_charging_ledger_closed") is True
        and sibling_numeric.get("sibling_multiset_projection_identity_proved") is True
        and parent_support.get("scaled_child_union_single_interval_geometry_proved") is True
        and parent_support.get("projected_support_to_dilated_parent_window_proved") is True
    )
    collar_kernel = (
        parent_dilated.get("dilated_threshold_schema_closed") is True
        and collar_cap.get("same_parameter_collar_short_divisor_cap_table_proved") is True
        and collar_lcm.get("width_lcm_kernel_compression_proved") is True
        and no_free.get("common_kernel_return_cycle_descent_or_pdec_proved") is True
    )
    prime_fanin = (
        prime_power.get("small_prime_power_cascade_table_proved") is True
        and fanin.get("multisource_fanin_independent_hardpoint_removed") is True
    )
    single_layer = all([target, tree_domain, sibling_projection, collar_kernel, prime_fanin])
    depth_gap = all(item["shows_gap"] for item in depth_obstruction_rows())

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_core_history_weighted_support_measure_router",
        "status": "weighted_support_measure_reduced_to_depth_telescoping_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "support_measure_target_imported": target,
        "actual_cold_prefix_tree_domain_closed": tree_domain,
        "sibling_layer_projection_ledger_imported": sibling_projection,
        "collar_and_kernel_return_discipline_imported": collar_kernel,
        "prime_power_and_fanin_independent_exits_removed": prime_fanin,
        "single_layer_support_envelope_closed": single_layer,
        "depth_telescoping_gap_certified": depth_gap,
        "log_depth_sample_absorption_checked": True,
        "cold_support_depth_telescoping_contraction_or_log_absorption_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "finite_cold_history_summation_runner_or_analytic_envelope_proved": False,
        "sparse_terminal_forced_load_lower_bound_proved": False,
        "core_history_weighted_support_measure_table_proved": False,
        "core_threshold_summation_dominance_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SUPPORT_TABLE,
        "hardpoint_after_router": f"{DEPTH_TELESCOPE} AND {TPDEC_WEIGHT} AND {ROOT_DEMAND}",
        "next_direct_attack_target": DEPTH_TELESCOPE,
        "parallel_attack_targets": [
            TPDEC_WEIGHT,
            ROOT_DEMAND,
            FINITE_RUNNER,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "tree_decomposition_rows": tree_decomposition_rows(),
        "depth_obstruction_rows": depth_obstruction_rows(),
        "log_absorption_samples": log_absorption_samples(),
        "envelope_rows": envelope_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`CoreHistoryWeightedSupportMeasureTable` 的单层结构可以下钻到前缀树兄弟收费："
            "同父兄弟冷收费投影到父除数支撑，父支撑落入单个扩张父窗口，collar/LCM/共同核爆发不能免费回流，"
            "单素数幂和多源 fan-in 也不再是独立无名出口。"
            "但这仍不是全深度加权支撑测度证明：单层 envelope 只能控制每个父节点的一层孩子，"
            "不能自动控制沿前缀树所有深度的累计支撑，也不能处理 `T_PDEC` 权重。"
            "因此最新最窄剩余是 `ColdSupportDepthTelescopingContractionOrLogAbsorptionTable`："
            "必须证明跨层总支撑可由根势能、可吸收对数因子或命名回流控制。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 冷历史加权支撑测度路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"support_measure_target_imported={fmt_bool(result['support_measure_target_imported'])}",
        f"actual_cold_prefix_tree_domain_closed={fmt_bool(result['actual_cold_prefix_tree_domain_closed'])}",
        f"sibling_layer_projection_ledger_imported={fmt_bool(result['sibling_layer_projection_ledger_imported'])}",
        f"collar_and_kernel_return_discipline_imported={fmt_bool(result['collar_and_kernel_return_discipline_imported'])}",
        f"prime_power_and_fanin_independent_exits_removed={fmt_bool(result['prime_power_and_fanin_independent_exits_removed'])}",
        f"single_layer_support_envelope_closed={fmt_bool(result['single_layer_support_envelope_closed'])}",
        f"depth_telescoping_gap_certified={fmt_bool(result['depth_telescoping_gap_certified'])}",
        f"cold_support_depth_telescoping_contraction_or_log_absorption_table_proved={fmt_bool(result['cold_support_depth_telescoping_contraction_or_log_absorption_table_proved'])}",
        f"core_history_weighted_support_measure_table_proved={fmt_bool(result['core_history_weighted_support_measure_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前缀树分解",
        "",
        "| piece | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["tree_decomposition_rows"]:
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
            "## 2. 深度缺口见证",
            "",
            "| depth | per level parent support | single level valid | total support | root support | shows gap |",
            "| ---: | ---: | --- | ---: | ---: | --- |",
        ]
    )
    for item in result["depth_obstruction_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["depth"]),
                    str(item["per_level_parent_support"]),
                    f"`{fmt_bool(item['single_level_bound_valid'])}`",
                    str(item["total_support_without_contraction"]),
                    str(item["root_support_bound"]),
                    f"`{fmt_bool(item['shows_gap'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 对数吸收样本",
            "",
            "| P | floor(log2 P)+1 | P^0.43 | absorbed | margin |",
            "| ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in result["log_absorption_samples"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["P"]),
                    str(item["depth_cap_floor_log2_plus_1"]),
                    str(item["P_alpha"]),
                    f"`{fmt_bool(item['log_depth_absorbed_by_P_alpha'])}`",
                    str(item["margin"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 剩余 envelope",
            "",
            "| input | role | status |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["envelope_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['input'])}`",
                    table_cell(item["role"]),
                    f"`{table_cell(item['status'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行：`{TPDEC_WEIGHT}`、`{ROOT_DEMAND}`、`{FINITE_RUNNER}`。",
            "- 边界：本步关闭的是单层支撑 envelope 与深度缺口定位，不提交最终全深度加权测度证明。",
            "",
            "## 7. 依赖哈希",
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
    print(f"single_layer_support_envelope_closed={fmt_bool(result['single_layer_support_envelope_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
