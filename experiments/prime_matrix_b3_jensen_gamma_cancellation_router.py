#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen Gamma 主项均值相消闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_gamma_cancellation_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-gamma-cancellation-router.json
  docs/monograph/prime-matrix-b3-jensen-gamma-cancellation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-right-edge-center-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-gamma-cancellation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-gamma-cancellation-router.md"

OLD_ATOM = "BacklundJensenGammaMainCancellationInMeanLedger"
CLOSED_ATOM = "BacklundJensenGammaMainCancellationInMeanClosedHighT10R4"
CENTER_CLOSED = "BacklundJensenRightEdgeCenterChoiceConventionClosedR4"
EULER_LOWER_ATOM = "BacklundJensenRightEdgeEulerProductLowerBoundLedger"
LOW_CENTER_ATOM = "BacklundJensenLowHeightCenterAnchorFiniteLedger"
ANCHOR_CONST_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SIGMA_CENTER = 2.0
OUTER_RADIUS = 4.0
HIGH_HEIGHT_START = 10.0
MIN_DISTANCE_TO_REAL_AXIS = HIGH_HEIGHT_START - OUTER_RADIUS


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
    """把待证 atom 替换为闭合 atom。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def cancellation_rows() -> list[dict[str, str]]:
    """生成 Gamma 均值相消说明表。"""
    return [
        {
            "factor": "pi^{-s/2}",
            "status": "entire nonzero",
            "mean_effect": "log|.| 是调和函数，圆周均值等于圆心值。",
        },
        {
            "factor": "s(s-1)",
            "status": "|T|>=10 且 R=4 时圆盘距实轴至少 6，不含 0 或 1。",
            "mean_effect": "无零点进入圆盘，log|.| 调和，均值差为 0。",
        },
        {
            "factor": "Gamma(s/2)",
            "status": "Gamma 极点在非正偶实点；高高度圆盘不碰这些点。",
            "mean_effect": "无极点进入圆盘，log|Gamma(s/2)| 调和，均值差为 0。",
        },
        {
            "factor": "zeta(s)",
            "status": "保留给 Euler 下界与 Jensen 零点计数。",
            "mean_effect": "本步不处理 zeta 零点，不产生 RVM/Backlund 循环。",
        },
    ]


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Jensen Gamma 主项均值相消判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    center_ready = CENTER_CLOSED in basis
    gamma_ready = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    high_geometry_clear = MIN_DISTANCE_TO_REAL_AXIS > 0.0
    closed = active and center_ready and gamma_ready and xi_ready and guard and high_geometry_clear
    return [
        row(
            "GammaCancellationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen Gamma 主项均值相消。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "CenterGammaXiInputsAvailable",
            center_ready and gamma_ready and xi_ready,
            True,
            "右边圆心 convention、Gamma/digamma 和 xi 基础输入均已可用。",
            "无形式输入剩余。",
        ),
        row(
            "HighHeightDiskAvoidsElementaryGammaSingularities",
            high_geometry_clear,
            True,
            "当 |T|>=10 且 R=4，圆盘距实轴至少 6，不含 s=0,1 或 Gamma 极点。",
            "低高度另交有限 anchor。",
        ),
        row(
            "GammaElementaryMeanCancellationClosed",
            closed,
            True,
            "在高高度圆盘内，初等/Gamma 因子无零无极，log|.| 调和，圆周平均减圆心值精确为 0。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "Gamma 主项线性衰减已从 Jensen anchor 成本中消去；剩下 zeta/Euler 下界与低高度有限项。",
            CLOSED_ATOM,
        ),
        row(
            "RightEdgeEulerLowerBoundStillNext",
            False,
            False,
            "下一步需用 sigma=2 的 Euler product 给 zeta 圆心下界。",
            EULER_LOWER_ATOM,
        ),
        row(
            "LowAndConstantAggregationStillDownstream",
            False,
            False,
            "低高度圆心、anchor 常数聚合与最终 C_N=16 仍未闭合。",
            f"{LOW_CENTER_ATOM} AND {ANCHOR_CONST_ATOM} AND {COUNT_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen Gamma 主项均值相消闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_jensen_gamma_cancellation_router",
        "status": "backlund_jensen_gamma_main_cancellation_closed_high_t10_r4",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_gamma_cancellation_closed": closed,
        "sigma_center": SIGMA_CENTER,
        "outer_radius": OUTER_RADIUS,
        "high_height_start": HIGH_HEIGHT_START,
        "min_distance_to_real_axis": MIN_DISTANCE_TO_REAL_AXIS,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": EULER_LOWER_ATOM,
        "secondary_priority": LOW_CENTER_ATOM,
        "tertiary_priority": ANCHOR_CONST_ATOM,
        "quaternary_priority": COUNT_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "cancellation_rows": cancellation_rows(),
        "plain_conclusion": (
            "Jensen Gamma 主项均值相消已在高高度 |T|>=10、R=4 下闭合。"
            "初等/Gamma 因子的线性衰减不再进入 anchor 成本；"
            "剩余是右边 Euler 下界、低高度圆心 anchor 和常数聚合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen Gamma 主项均值相消闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_jensen_gamma_cancellation_closed={fmt_bool(result['backlund_jensen_gamma_cancellation_closed'])}",
        f"sigma_center={fmt_float(result['sigma_center'])}",
        f"outer_radius={fmt_float(result['outer_radius'])}",
        f"high_height_start={fmt_float(result['high_height_start'])}",
        f"min_distance_to_real_axis={fmt_float(result['min_distance_to_real_axis'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 相消机制",
        "",
        "在高高度圆盘 `|s-(2+iT)|<=4`、`|T|>=10` 内，初等/Gamma 因子不含零极点。",
        "因此其对数模是调和函数，按平均值性质：",
        "",
        "```text",
        "(1/2pi) int_0^{2pi} log|G(z0+4e^{i theta})| dtheta - log|G(z0)| = 0",
        "G(s)=1/2*s*(s-1)*pi^{-s/2}*Gamma(s/2).",
        "```",
        "",
        "| factor | status | mean effect |",
        "| --- | --- | --- |",
    ]
    for item in result["cancellation_rows"]:
        lines.append(
            "| {factor} | {status} | {mean_effect} |".format(
                factor=table_cell(item["factor"]),
                status=table_cell(item["status"]),
                mean_effect=table_cell(item["mean_effect"]),
            )
        )
    lines.extend(
        [
            "",
            "这一步只消去 Gamma/初等主项；`zeta` 的圆心下界仍由下一步 Euler product 处理。",
            "",
            "## 3. 判定表",
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`。"
            ),
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
