#!/usr/bin/env python3
"""Prime Matrix B=3 psi_0 水平边加权积分预算路由器。

用法示例：
  python3 experiments/prime_matrix_b3_psi0_horizontal_weighted_budget_router.py

输出：
  docs/monograph/prime-matrix-b3-psi0-horizontal-weighted-budget-router.json
  docs/monograph/prime-matrix-b3-psi0-horizontal-weighted-budget-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-psi0-horizontal-local-zero-distance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-psi0-horizontal-weighted-budget-router.md"

OLD_ATOM = "Psi0HorizontalWeightedIntegralBudgetLedger"
CLOSED_ATOM = "Psi0HorizontalWeightedIntegralBudgetClosedC12000"
LOCAL_DISTANCE_CLOSED = "Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16"
HORIZONTAL_LOGDER_ATOM = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger"
HORIZONTAL_LOGDER_CLOSED = "Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosClosedByTitchmarshCN16C12000"
CONTOUR_ATOM = "Psi0ZetaLogDerivativeContourShiftBoundLedger"
CONTOUR_AGGREGATION = "Psi0ZetaLogDerivativeContourShiftExternalAggregationLedger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"

ANCHOR_X = 20_000.0
ANCHOR_T_VALUES = [14.0, 45.0, 1_000.0, 20_000.0, 1_000_000.0]
C_TOTAL_LOGDER = 288.0
C_WEIGHTED_BUDGET = 12_000.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def replace_atom(text: str) -> str:
    """把待证预算原子替换为闭合原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def replace_horizontal_logder(text: str) -> str:
    """把整条水平边 log-derivative 包替换为闭合原子。"""
    text = text.replace(f"TitchmarshLocalZeroExpansionExternalRegistered AND {LOCAL_DISTANCE_CLOSED} AND {OLD_ATOM}", HORIZONTAL_LOGDER_CLOSED)
    return replace_atom(text)


def budget_components() -> list[dict[str, float | str]]:
    """生成预算常数分解表。"""
    straight = 2.0 * math.e * C_TOTAL_LOGDER
    arcs = 4.0 * math.pi * math.e * C_TOTAL_LOGDER
    return [
        {
            "component": "straight horizontal segments",
            "coefficient": straight,
            "formula": "2*e*C_logder",
            "meaning": "两条水平直段，使用 integral x^sigma d sigma <= e*x/log x，并粗吸收到 x*log^2(xT)/T。",
        },
        {
            "component": "indentation arcs",
            "coefficient": arcs,
            "formula": "4*pi*e*C_logder",
            "meaning": "上下两侧凹口弧长用 2*pi*eta*N(T,1) 和 C_N log(T+3) 粗付。",
        },
        {
            "component": "rounded reserve",
            "coefficient": C_WEIGHTED_BUDGET,
            "formula": "ceil reserve above straight+arcs",
            "meaning": "给端点、半权和 log(T+3)<=log(xT) 的口径转换留余量。",
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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成水平边加权积分预算判定表。"""
    basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    local_distance_ready = previous.get("psi0_horizontal_local_zero_distance_external_closed") is True
    constants_fit = sum(float(item["coefficient"]) for item in budget_components()[:2]) < C_WEIGHTED_BUDGET
    closed = active and guard and local_distance_ready and constants_fit
    return [
        row(
            "Psi0HorizontalWeightedBudgetGateActive",
            active,
            True,
            "上一层已给出 pointwise C=288 log(T+3)，当前任务是把 x^s/s 权重积分纳入 Perron 余项。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条解析输入，不使用真实零行缺席或数值实验替代证明。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LocalZeroDistanceC288Available",
            local_distance_ready,
            False,
            "外部 Backlund/RVM 条件路线已给出水平边 pointwise log-derivative 系数 C=288。",
            LOCAL_DISTANCE_CLOSED,
        ),
        row(
            "StraightHorizontalWeightedBoundClosed",
            constants_fit,
            True,
            "两条水平直段由 |s|>=T、x^(1+1/log x)<=e*x 和 integral x^sigma d sigma 控制。",
            "2*e*C_logder",
        ),
        row(
            "IndentArcWeightedBoundClosed",
            constants_fit,
            True,
            "凹口弧段由 eta=1/16、局部零点计数和弧长 2*pi*eta*N 控制，统一吸收到 x log^2(xT)/T。",
            "4*pi*e*C_logder",
        ),
        row(
            "WeightedBudgetC12000MarginClosed",
            constants_fit,
            True,
            "直段与弧段总系数低于 12000，端点和口径转换留在余量内。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "外部 Titchmarsh+CN16+Backlund 条件路线下，水平边加权积分预算闭合为 C=12000。",
            CLOSED_ATOM,
        ),
        row(
            "HorizontalLogDerivativeExternalPackageClosed",
            closed,
            False,
            "局部零点倒距离和与加权预算都关闭后，水平边 log-derivative 包可在该条件路线下关闭。",
            HORIZONTAL_LOGDER_CLOSED,
        ),
        row(
            "SelfContainedWeightedBudgetStillOpen",
            False,
            False,
            "严格自足路线仍缺自足 Backlund 缩进和自足 C_N=16，因此不能同步关闭。",
            BACKLUND_INTERNAL,
        ),
        row(
            "ContourShiftAggregationNext",
            False,
            False,
            "下一步需要把留数左边界、fixed-T 缩进和水平边包合并，关闭外部条件轮廓移线。",
            CONTOUR_AGGREGATION,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行水平边加权积分预算路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    horizontal_closed = next(item["closed"] for item in rows if item["gate"] == "HorizontalLogDerivativeExternalPackageClosed")
    latest_external = replace_horizontal_logder(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    return {
        "certificate_type": "b3_psi0_horizontal_weighted_budget_router",
        "status": "psi0_horizontal_weighted_budget_external_closed_c12000",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "psi0_horizontal_weighted_integral_budget_external_closed": closed,
        "psi0_horizontal_logder_external_package_closed": horizontal_closed,
        "psi0_horizontal_weighted_integral_budget_self_contained_closed": False,
        "zeta_logder_contour_shift_closed": False,
        "row_column_unconditional_closed": False,
        "C_total_logder": C_TOTAL_LOGDER,
        "C_weighted_budget": C_WEIGHTED_BUDGET,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "replacement_horizontal_logder": {HORIZONTAL_LOGDER_ATOM: HORIZONTAL_LOGDER_CLOSED},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "next_priority": CONTOUR_AGGREGATION,
        "secondary_priority": ZERO_SUM_ATOM,
        "parallel_self_contained_priority": BACKLUND_INTERNAL,
        "contour_shift_atom": CONTOUR_ATOM,
        "budget_components": budget_components(),
        "pressure_rows": pressure_rows(),
        "plain_conclusion": (
            "`Psi0HorizontalWeightedIntegralBudgetLedger` 在外部 Titchmarsh+CN16+Backlund 条件路线下闭合。"
            "使用 pointwise `|-zeta'/zeta| <= 288 log(T+3)`，水平直段和凹口弧段统一吸收到 "
            "`12000*x*log^2(xT)/T`。这关闭水平边包，但仍只是一个很粗的 Perron 余项形状；"
            "后续还要聚合完整 `Psi0ZetaLogDerivativeContourShiftBoundLedger`，并进入零点和/PNT 数值预算。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    repl = next(iter(result["replacement_external"].items()))
    h_repl = next(iter(result["replacement_horizontal_logder"].items()))
    lines = [
        "# Prime Matrix B=3 psi_0 水平边加权积分预算路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "psi0_horizontal_weighted_integral_budget_external_closed="
            f"{fmt_bool(result['psi0_horizontal_weighted_integral_budget_external_closed'])}"
        ),
        (
            "psi0_horizontal_logder_external_package_closed="
            f"{fmt_bool(result['psi0_horizontal_logder_external_package_closed'])}"
        ),
        (
            "psi0_horizontal_weighted_integral_budget_self_contained_closed="
            f"{fmt_bool(result['psi0_horizontal_weighted_integral_budget_self_contained_closed'])}"
        ),
        f"zeta_logder_contour_shift_closed={fmt_bool(result['zeta_logder_contour_shift_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"C_weighted_budget={fmt_float(result['C_weighted_budget'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
        repl[0],
        "  =>",
        repl[1],
        "",
        h_repl[0],
        "  =>",
        h_repl[1],
        "```",
        "",
        "## 2. 预算分解",
        "",
        "| component | coefficient | formula | meaning |",
        "| --- | ---: | --- | --- |",
    ]
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 5. 最新输入基",
            "",
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            f"下一步攻 `{result['next_priority']}`，随后进入 `{result['secondary_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
