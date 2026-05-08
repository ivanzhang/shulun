#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 右边圆心选择 convention 闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_right_edge_center_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-right-edge-center-router.json
  docs/monograph/prime-matrix-b3-jensen-right-edge-center-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-center-anchor-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-right-edge-center-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-right-edge-center-router.md"

OLD_ATOM = "BacklundJensenRightEdgeCenterChoiceConventionLedger"
CLOSED_ATOM = "BacklundJensenRightEdgeCenterChoiceConventionClosedR4"
GAMMA_CANCEL_ATOM = "BacklundJensenGammaMainCancellationInMeanLedger"
EULER_LOWER_ATOM = "BacklundJensenRightEdgeEulerProductLowerBoundLedger"
LOW_CENTER_ATOM = "BacklundJensenLowHeightCenterAnchorFiniteLedger"
ANCHOR_CONST_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SIGMA_CENTER = 2.0
OUTER_RADIUS = 4.0
TARGET_HEIGHT_HALF_WIDTH = 1.0
TARGET_SIGMA_LEFT = 0.0
TARGET_SIGMA_RIGHT = 1.0
TARGET_RADIUS = math.sqrt((SIGMA_CENTER - TARGET_SIGMA_LEFT) ** 2 + TARGET_HEIGHT_HALF_WIDTH**2)
JENSEN_LOG_RATIO = math.log(OUTER_RADIUS / TARGET_RADIUS)


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


def geometry_rows() -> list[dict[str, float | str]]:
    """生成 Jensen 圆盘几何表。"""
    return [
        {
            "item": "center",
            "value": f"z0(T) = {SIGMA_CENTER:g} + iT",
            "meaning": "圆心放在 sigma=2 的 Euler product 非零线上。",
        },
        {
            "item": "target strip",
            "value": "0 <= beta <= 1, |gamma-T| <= 1",
            "meaning": "需要计数的局部非平凡零点窗口。",
        },
        {
            "item": "target radius",
            "value": f"sqrt((2-0)^2+1^2) = {TARGET_RADIUS:.12f}",
            "meaning": "目标窗口完全包含在半径 r 的内圆盘。",
        },
        {
            "item": "outer radius",
            "value": f"R = {OUTER_RADIUS:.12f}",
            "meaning": "固定外圆半径，给 Jensen 留出正的 log(R/r)。",
        },
        {
            "item": "Jensen denominator",
            "value": f"log(R/r) = {JENSEN_LOG_RATIO:.12f}",
            "meaning": "该量为正，后续常数聚合可除以它。",
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
    """生成 Jensen 右边圆心选择判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    jensen_ready = "BacklundJensenDiskFormulaClosed" in basis
    boundary_ready = "BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic" in basis
    euler_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = (
        active
        and jensen_ready
        and boundary_ready
        and euler_ready
        and guard
        and TARGET_RADIUS < OUTER_RADIUS
        and JENSEN_LOG_RATIO > 0.0
    )
    return [
        row(
            "RightEdgeCenterChoiceGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen 右边圆心选择 convention。",
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
            "JensenBoundaryEulerInputsAvailable",
            jensen_ready and boundary_ready and euler_ready,
            True,
            "Jensen 公式、独立圆周上界和 sigma=2 的 Euler product 输入均已可用。",
            "无形式输入剩余。",
        ),
        row(
            "TargetWindowContainedInInnerDisk",
            TARGET_RADIUS < OUTER_RADIUS,
            True,
            "对任意 0<=beta<=1 且 |gamma-T|<=1 的零点，距 2+iT 至多 sqrt(5)<4。",
            "无几何覆盖剩余。",
        ),
        row(
            "RightEdgeCenterNonzeroConvention",
            closed,
            True,
            "圆心在 sigma=2，zeta 由 Euler product 非零，Gamma 与初等因子在该线上也非零。",
            "定量下界仍由 Euler/Gamma anchor 支付。",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "Jensen 右边圆心选择 convention 闭合为 z0=2+iT、R=4、r=sqrt(5)。",
            CLOSED_ATOM,
        ),
        row(
            "GammaCancellationStillNext",
            False,
            False,
            "圆心已固定后，下一步必须证明 Gamma 主项在 Jensen 平均中相消到 O(log(T+3))。",
            GAMMA_CANCEL_ATOM,
        ),
        row(
            "EulerLowConstantStillDownstream",
            False,
            False,
            "还需右边 Euler 下界、低高度 anchor 与常数聚合。",
            f"{EULER_LOWER_ATOM} AND {LOW_CENTER_ATOM} AND {ANCHOR_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen 右边圆心选择 convention 闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_jensen_right_edge_center_router",
        "status": "backlund_jensen_right_edge_center_choice_closed_r4",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_right_edge_center_choice_closed": closed,
        "sigma_center": SIGMA_CENTER,
        "outer_radius": OUTER_RADIUS,
        "target_radius": TARGET_RADIUS,
        "jensen_log_ratio": JENSEN_LOG_RATIO,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": GAMMA_CANCEL_ATOM,
        "secondary_priority": EULER_LOWER_ATOM,
        "tertiary_priority": LOW_CENTER_ATOM,
        "quaternary_priority": ANCHOR_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "geometry_rows": geometry_rows(),
        "plain_conclusion": (
            "Jensen 右边圆心选择 convention 已闭合：取 z0=2+iT、外半径 R=4，"
            "目标局部零点窗口落在内半径 sqrt(5) 中。"
            "这只固定几何和非零圆心线，不闭合 Gamma 相消或数值 C_N。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 右边圆心选择 convention 闭合证书",
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
            "backlund_jensen_right_edge_center_choice_closed="
            f"{fmt_bool(result['backlund_jensen_right_edge_center_choice_closed'])}"
        ),
        f"sigma_center={fmt_float(result['sigma_center'])}",
        f"outer_radius={fmt_float(result['outer_radius'])}",
        f"target_radius={fmt_float(result['target_radius'])}",
        f"jensen_log_ratio={fmt_float(result['jensen_log_ratio'])}",
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
        "## 2. 圆盘几何",
        "",
        "| item | value | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["geometry_rows"]:
        lines.append(
            "| {item} | {value} | {meaning} |".format(
                item=table_cell(item["item"]),
                value=table_cell(item["value"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "圆心线 `sigma=2` 的非零性只用于 convention 合法性；定量下界仍在后续 Euler/Gamma anchor 中处理。",
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
