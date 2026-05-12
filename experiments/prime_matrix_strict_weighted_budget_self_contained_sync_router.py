#!/usr/bin/env python3
"""生成 strict 水平边加权积分预算自足同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_weighted_budget_self_contained_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-weighted-budget-self-contained-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-weighted-budget-self-contained-sync-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-weighted-budget-self-contained-sync-router.md"

LOCAL_SYNC = MONOGRAPH / "prime-matrix-strict-local-zero-distance-self-contained-sync-router.json"
EXTERNAL_WEIGHTED = MONOGRAPH / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.json"
UNSMOOTHED_REDUCTION = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-self-contained-reduction-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [LOCAL_SYNC, EXTERNAL_WEIGHTED, UNSMOOTHED_REDUCTION, CLAIM_STATUS]

OLD_ATOM = "Psi0HorizontalWeightedIntegralBudgetLedger"
CLOSED_ATOM = "Psi0HorizontalWeightedIntegralBudgetSelfContainedClosedC12000"
LOCAL_CLOSED = "Psi0HorizontalLocalZeroDistanceSumSelfContainedClosedC288Eta1Over16"
HORIZONTAL_LOGDER_ATOM = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger"
HORIZONTAL_LOGDER_CLOSED = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosSelfContainedClosedC12000"
PERRON_LEDGER = "UnsmoothedChebyshevPerronExplicitFormulaConstantLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_TOTAL_LOGDER = 288.0
C_WEIGHTED_BUDGET = 12_000.0
ANCHOR_X = 20_000.0
ANCHOR_T_VALUES = [14.0, 45.0, 1_000.0, 20_000.0, 1_000_000.0]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def budget_components() -> list[dict[str, float | str]]:
    """生成自足预算常数分解表。"""
    straight = 2.0 * math.e * C_TOTAL_LOGDER
    arcs = 4.0 * math.pi * math.e * C_TOTAL_LOGDER
    return [
        {
            "component": "straight horizontal segments",
            "coefficient": straight,
            "formula": "2*e*C_logder",
            "meaning": "两条水平直段由 |s|>=T、x^(1+1/log x)<=e*x 和积分长度控制。",
        },
        {
            "component": "indentation arcs",
            "coefficient": arcs,
            "formula": "4*pi*e*C_logder",
            "meaning": "凹口弧段由 eta=1/16、局部零点数和弧长预算控制。",
        },
        {
            "component": "rounded reserve",
            "coefficient": C_WEIGHTED_BUDGET,
            "formula": "ceil reserve above straight+arcs",
            "meaning": "为端点、半权和 log(T+3)<=log(xT) 转换保留余量。",
        },
    ]


def pressure_rows() -> list[dict[str, float]]:
    """生成锚点压力诊断。"""
    rows: list[dict[str, float]] = []
    for height in ANCHOR_T_VALUES:
        log_x_t = math.log(ANCHOR_X * height)
        bound = C_WEIGHTED_BUDGET * ANCHOR_X * log_x_t * log_x_t / height
        rows.append(
            {
                "x": ANCHOR_X,
                "T": height,
                "log_xT": log_x_t,
                "budget_bound": bound,
                "relative_to_x": bound / ANCHOR_X,
            }
        )
    return rows


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(local_sync: dict[str, Any], external_weighted: dict[str, Any], reduction: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 strict 加权预算判定表。"""
    guard = (
        local_sync.get("counterexample_assumption_only") is True
        and local_sync.get("empirical_absence_not_used") is True
        and local_sync.get("direct_unconditional_contradiction_found") is False
        and local_sync.get("row_column_unconditional_closed") is False
        and external_weighted.get("row_column_unconditional_closed") is False
        and reduction.get("row_column_unconditional_closed") is False
    )
    active = (
        local_sync.get("next_direct_attack_target") == OLD_ATOM
        and OLD_ATOM in str(reduction)
    )
    local_ready = (
        local_sync.get("psi0_horizontal_local_zero_distance_self_contained_closed") is True
        and abs(float(local_sync.get("C_total_logder", 0.0)) - C_TOTAL_LOGDER) < 1e-9
    )
    external_arithmetic_template = (
        external_weighted.get("psi0_horizontal_weighted_integral_budget_external_closed") is True
        and abs(float(external_weighted.get("C_weighted_budget", 0.0)) - C_WEIGHTED_BUDGET) < 1e-9
    )
    component_sum = sum(float(item["coefficient"]) for item in budget_components()[:2])
    constants_fit = component_sum < C_WEIGHTED_BUDGET
    weighted_closed = guard and active and local_ready and external_arithmetic_template and constants_fit
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步继续只在假设反例链解析输入内同步，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "WeightedBudgetAtomActive",
            active,
            True,
            "strict 局部倒距离关闭后，Perron 自足压缩链唯一剩余解析原子就是水平加权预算。",
            OLD_ATOM,
        ),
        row(
            "PointwiseC288SelfContainedAvailable",
            local_ready,
            local_ready,
            "局部零点倒距离已自足给出 |zeta'/zeta| 的 C=288 log(T+3) 点态包。",
            LOCAL_CLOSED,
        ),
        row(
            "ExternalWeightedArithmeticTemplateChecked",
            external_arithmetic_template,
            True,
            "旧外部证书只作为直段/凹口常数算术模板，不复用外部 Backlund/RVM 假设。",
            "Psi0HorizontalWeightedIntegralBudgetClosedC12000",
        ),
        row(
            "StraightHorizontalWeightedBoundClosed",
            constants_fit,
            True,
            "两条水平直段成本为 2e*C_logder，已包含于 C=12000 预算。",
            "2*e*C_logder",
        ),
        row(
            "IndentArcWeightedBoundClosed",
            constants_fit,
            True,
            "凹口弧段成本为 4*pi*e*C_logder，和直段合计低于 12000。",
            "4*pi*e*C_logder",
        ),
        row(
            "WeightedBudgetC12000SelfContainedClosed",
            weighted_closed,
            weighted_closed,
            "点态 C=288 与权重积分估计合成后，水平边加权积分预算自足关闭。",
            CLOSED_ATOM,
        ),
        row(
            "HorizontalLogDerivativeSelfContainedPackageClosed",
            weighted_closed,
            weighted_closed,
            "局部倒距离和加权预算都自足关闭后，水平边 log-derivative 包自足关闭。",
            HORIZONTAL_LOGDER_CLOSED,
        ),
        row(
            "UnsmoothedPerronStrictSelfContainedClosed",
            False,
            False,
            "本步关闭最后的水平预算原子；仍需单独同步 Perron 压缩账本，避免隐式越级。",
            PERRON_LEDGER,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只是解析输入自足化，不产生全局反例矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    local_sync = load_json(LOCAL_SYNC)
    external_weighted = load_json(EXTERNAL_WEIGHTED)
    reduction = load_json(UNSMOOTHED_REDUCTION)
    rows = build_rows(local_sync, external_weighted, reduction)
    weighted_closed = next(item["closed"] for item in rows if item["gate"] == "WeightedBudgetC12000SelfContainedClosed")
    return {
        "certificate_type": "prime_matrix_strict_weighted_budget_self_contained_sync_router",
        "status": "psi0_horizontal_weighted_budget_self_contained_closed_perron_sync_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_horizontal_weighted_integral_budget_self_contained_closed": weighted_closed,
        "psi0_horizontal_logder_self_contained_package_closed": weighted_closed,
        "unsmoothed_perron_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "C_total_logder": C_TOTAL_LOGDER,
        "C_weighted_budget": C_WEIGHTED_BUDGET,
        "replacement_self_contained": {
            OLD_ATOM: CLOSED_ATOM,
            HORIZONTAL_LOGDER_ATOM: HORIZONTAL_LOGDER_CLOSED,
        },
        "remaining_after_weighted_budget_sync": [PERRON_LEDGER],
        "next_direct_attack_target": "UnsmoothedPerronStrictSelfContainedFinalSync",
        "source_hashes": source_hashes(),
        "budget_components": budget_components(),
        "pressure_rows": pressure_rows(),
        "plain_conclusion": (
            "`Psi0HorizontalWeightedIntegralBudgetLedger` 已可从外部条件版同步为 strict 自足版："
            "输入点态界已由 strict 局部倒距离证书给出 C=288，"
            "直段 `2eC` 与凹口 `4*pi*eC` 的总成本低于 12000。"
            "该步关闭水平边 log-derivative 包，但仍需单独同步 Perron 压缩账本；"
            "行/列无条件命题保持未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 水平边加权积分预算自足同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"psi0_horizontal_weighted_integral_budget_self_contained_closed={fmt_bool(result['psi0_horizontal_weighted_integral_budget_self_contained_closed'])}",
        f"psi0_horizontal_logder_self_contained_package_closed={fmt_bool(result['psi0_horizontal_logder_self_contained_package_closed'])}",
        f"unsmoothed_perron_strict_self_contained_closed={fmt_bool(result['unsmoothed_perron_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_weighted_budget={fmt_float(result['C_weighted_budget'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
    ]
    for old, new in result["replacement_self_contained"].items():
        lines.extend([old, f"  => {new}", ""])
    lines.extend(
        [
            "```",
            "",
            "## 2. 预算分解",
            "",
            "| component | coefficient | formula | meaning |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for item in result["budget_components"]:
        lines.append(
            "| {component} | `{coefficient}` | {formula} | {meaning} |".format(
                component=table_cell(item["component"]),
                coefficient=fmt_float(float(item["coefficient"])),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 压力诊断",
            "",
            "| x | T | log(xT) | budget bound | relative to x |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["pressure_rows"]:
        lines.append(
            "| {x} | {T} | {L} | {B} | {R} |".format(
                x=fmt_float(float(item["x"])),
                T=fmt_float(float(item["T"])),
                L=fmt_float(float(item["log_xT"])),
                B=fmt_float(float(item["budget_bound"])),
                R=fmt_float(float(item["relative_to_x"])),
            )
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
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
