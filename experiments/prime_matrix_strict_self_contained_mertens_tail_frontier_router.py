#!/usr/bin/env python3
"""生成 strict 自足 Mertens 尾段当前前沿路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_self_contained_mertens_tail_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-self-contained-mertens-tail-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-self-contained-mertens-tail-frontier-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-b3-self-contained-mertens-tail-router.md",
    MONOGRAPH / "prime-matrix-b3-zero-free-constants-router.md",
    MONOGRAPH / "prime-matrix-b3-zero-repulsion-parameter-optimization-router.md",
    MONOGRAPH / "prime-matrix-b3-pnt-contour-constant-router.md",
    MONOGRAPH / "prime-matrix-b3-zero-sum-contour-budget-router.md",
    MONOGRAPH / "prime-matrix-b3-trivial-tail-prime-power-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.md",
]

TARGET = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
UNSMOOTHED = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
ZERO_SUM_INTERNAL = "InternalZeroSumDyadicContourBudgetLedger"
THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW = "FiniteLowHeightZeroCheckLedger"
FINITE_THETA = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
B1_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def frontier_items() -> list[dict[str, str]]:
    """列出自足 Mertens 尾段前沿。"""
    return [
        {
            "name": "finite_prime_steps_to_20000",
            "status": "closed",
            "meaning": "286<=x<10372 与 10372<=x<20000 的素数倒数跳点作为精确 Stieltjes 原子保留。",
            "remaining": "无。",
        },
        {
            "name": "partial_summation_interface",
            "status": "closed",
            "meaning": "一旦有 theta/psi 包络和 B1 常数区间，素数倒数尾段由分部求和接口推出。",
            "remaining": "等待 theta/B1 输入。",
        },
        {
            "name": "dvp_symbolic_and_numeric_region",
            "status": "partly_closed",
            "meaning": "DVP 符号零点排斥与 C=64 参数优化给出 beta<=1-1/(1280 log(|gamma|+3)), |gamma|>=14。",
            "remaining": f"{FINITE_LOW} AND {UNSMOOTHED} AND {ZERO_SUM_INTERNAL}",
        },
        {
            "name": "trivial_tail_prime_power",
            "status": "closed",
            "meaning": "平凡零点、端点半权、素数幂和截断尾项已有初等归账。",
            "remaining": "不能替代 theta@20000 小误差。",
        },
        {
            "name": "theta_20000_and_finite_bridge",
            "status": "open_self_contained",
            "meaning": "普通 C=1280 零点自由区常数不能自动达到 Dusart 级 theta@20000 目标。",
            "remaining": f"{THETA_TARGET} AND {FINITE_THETA}",
        },
        {
            "name": "meissel_mertens_b1_interval",
            "status": "open_self_contained",
            "meaning": "B1 常数区间与 x=20000 基点核验仍需自足算术账本。",
            "remaining": B1_INTERVAL,
        },
        {
            "name": "external_route",
            "status": "conditional_external_closed_to_dstructure",
            "meaning": "接受 Dusart theta/reciprocal-prime Mertens 外部定理后，B3 解析链推进到 DStructure/Rankin 守门项。",
            "remaining": DSTRUCTURE,
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "该解析前沿只作为早期零行反例链的 B3/TV 输入，不使用真实缺席样本。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "MertensTailFiniteAndFormalLayersClosed",
            "closed": True,
            "proved": True,
            "meaning": "有限跳点、分部求和接口、DVP 符号链、C=1280/T0=14 参数和初等尾项均已登记。",
            "remaining": f"{UNSMOOTHED} AND {ZERO_SUM_INTERNAL} AND {THETA_TARGET} AND {FINITE_THETA} AND {B1_INTERVAL}",
        },
        {
            "gate": "UnsmoothedPerronStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "平滑显式公式不能自动替代非平滑 Chebyshev/Perron 常数账本。",
            "remaining": UNSMOOTHED,
        },
        {
            "gate": "InternalZeroSumStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "外部零点和预算可条件关闭；自足线仍需文内 dyadic 零点和预算。",
            "remaining": ZERO_SUM_INTERNAL,
        },
        {
            "gate": "ThetaAndBridgeStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "x=20000 的小 theta 误差和有限桥不能由普通零点自由区粗常数自动推出。",
            "remaining": f"{THETA_TARGET} AND {FINITE_THETA}",
        },
        {
            "gate": "B1IntervalStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "Meissel-Mertens 常数区间自足算术仍未完成。",
            "remaining": B1_INTERVAL,
        },
        {
            "gate": "SelfContainedMertensTailProved",
            "closed": False,
            "proved": False,
            "meaning": "自足 reciprocal-prime Mertens 尾段仍未闭合。",
            "remaining": TARGET,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_self_contained_mertens_tail_frontier_router",
        "status": "self_contained_mertens_tail_frontier_compressed_to_unsmoothed_perron_internal_zerosum_theta_bridge_b1_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_prime_steps_to_20000_closed": True,
        "partial_summation_interface_closed": True,
        "dvp_symbolic_repulsion_closed": True,
        "zero_repulsion_c1280_t14_registered": True,
        "trivial_tail_prime_power_closed": True,
        "external_mertens_theta_route_closed_to_dstructure": True,
        "unsmoothed_perron_constant_proved": False,
        "internal_zero_sum_budget_proved": False,
        "theta_target_self_contained_proved": False,
        "finite_theta_bridge_proved": False,
        "meissel_mertens_b1_interval_proved": False,
        "self_contained_mertens_tail_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": UNSMOOTHED,
        "parallel_attack_targets": [ZERO_SUM_INTERNAL, THETA_TARGET, FINITE_LOW, FINITE_THETA, B1_INTERVAL],
        "frontier_items": frontier_items(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "自足 Mertens 尾段已经压到显式 PNT 机器的当前真实前沿：有限素数倒数跳点、"
            "分部求和接口、DVP 符号排斥、C=1280/T0=14 参数和初等尾项均可复用；"
            "剩余不再是零行几何，而是非平滑 Perron 常数、内部零点和预算、theta@20000/有限桥、"
            "以及 Meissel-Mertens B1 常数区间。外部 Dusart/Mertens 路线可条件推进到 DStructure/Rankin，"
            "但严格自足线仍未闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 自足 Mertens 尾段当前前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_prime_steps_to_20000_closed={fmt_bool(result['finite_prime_steps_to_20000_closed'])}",
        f"partial_summation_interface_closed={fmt_bool(result['partial_summation_interface_closed'])}",
        f"dvp_symbolic_repulsion_closed={fmt_bool(result['dvp_symbolic_repulsion_closed'])}",
        f"zero_repulsion_c1280_t14_registered={fmt_bool(result['zero_repulsion_c1280_t14_registered'])}",
        f"trivial_tail_prime_power_closed={fmt_bool(result['trivial_tail_prime_power_closed'])}",
        f"external_mertens_theta_route_closed_to_dstructure={fmt_bool(result['external_mertens_theta_route_closed_to_dstructure'])}",
        f"unsmoothed_perron_constant_proved={fmt_bool(result['unsmoothed_perron_constant_proved'])}",
        f"internal_zero_sum_budget_proved={fmt_bool(result['internal_zero_sum_budget_proved'])}",
        f"theta_target_self_contained_proved={fmt_bool(result['theta_target_self_contained_proved'])}",
        f"finite_theta_bridge_proved={fmt_bool(result['finite_theta_bridge_proved'])}",
        f"meissel_mertens_b1_interval_proved={fmt_bool(result['meissel_mertens_b1_interval_proved'])}",
        f"self_contained_mertens_tail_proved={fmt_bool(result['self_contained_mertens_tail_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿表",
        "",
        "| name | status | meaning | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["frontier_items"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
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
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步不证明自足 Mertens 尾段；只把其当前真实前沿压缩为可逐项攻击的解析账本。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
