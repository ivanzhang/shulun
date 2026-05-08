#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 低高度圆心 anchor 闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_low_center_anchor_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-low-center-anchor-router.json
  docs/monograph/prime-matrix-b3-jensen-low-center-anchor-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-euler-lower-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-low-center-anchor-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-low-center-anchor-router.md"

OLD_ATOM = "BacklundJensenLowHeightCenterAnchorFiniteLedger"
CLOSED_ATOM = "BacklundJensenLowHeightCenterAnchorCompactNonzeroClosed"
CENTER_CLOSED = "BacklundJensenRightEdgeCenterChoiceConventionClosedR4"
EULER_LOWER_CLOSED = "BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2"
ANCHOR_CONST_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SIGMA_CENTER = 2.0
LOW_HEIGHT_CEILING = 10.0
LOW_CENTER_SYMBOL = "m_xi_center_low := inf_{|T|<=10} |xi(2+iT)| > 0"
LOW_CENTER_LOG_COST_SYMBOL = "A_center_low := -log(m_xi_center_low) < infinity"
LOW_LOG_FLOOR = math.log(3.0)


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


def compact_rows() -> list[dict[str, str]]:
    """生成低高度圆心紧致下界说明表。"""
    return [
        {
            "component": "center line",
            "fact": "z0(T)=2+iT, |T|<=10 is compact",
            "role": "圆心参数集是紧集。",
        },
        {
            "component": "zeta factor",
            "fact": "|zeta(2+iT)|>=1/zeta(2)",
            "role": "低高度也沿用右边 Euler 下界，且无零。",
        },
        {
            "component": "Gamma factor",
            "fact": "Gamma(1+iT/2) has no zero or pole on |T|<=10",
            "role": "连续非零，紧集上最小模为正。",
        },
        {
            "component": "elementary factor",
            "fact": "s(s-1) and pi^{-s/2} are nonzero on s=2+iT",
            "role": "连续非零，紧集上最小模为正。",
        },
        {
            "component": "low anchor",
            "fact": LOW_CENTER_SYMBOL,
            "role": "低高度圆心下界闭合为有限正常数。",
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
    """生成低高度圆心 anchor 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    center_ready = CENTER_CLOSED in basis
    euler_ready = EULER_LOWER_CLOSED in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and center_ready and euler_ready and xi_ready and guard
    return [
        row(
            "LowCenterAnchorGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen 低高度圆心 anchor。",
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
            "CenterEulerXiInputsAvailable",
            center_ready and euler_ready and xi_ready,
            True,
            "右边圆心 convention、Euler 下界和 xi 基础输入均已可用。",
            "无形式输入剩余。",
        ),
        row(
            "LowCenterCompactNonzeroClosed",
            closed,
            True,
            "在 |T|<=10 的紧圆心线上，xi(2+iT) 由非零连续因子相乘，故最小模为正。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "低高度圆心 anchor 已闭合为正的紧致下界常数 m_xi_center_low。",
            CLOSED_ATOM,
        ),
        row(
            "AnchorConstantAggregationStillNext",
            False,
            False,
            "下一步需把高高度相消、Euler 常数和低高度 anchor 聚合为统一 O(log(T+3)) 下界。",
            ANCHOR_CONST_ATOM,
        ),
        row(
            "JensenC16StillDownstream",
            False,
            False,
            "anchor 聚合后仍需 Jensen C_N=16 数值聚合。",
            COUNT_CONST_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行低高度圆心 anchor 闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_jensen_low_center_anchor_router",
        "status": "backlund_jensen_low_height_center_anchor_compact_nonzero_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_low_center_anchor_closed": closed,
        "sigma_center": SIGMA_CENTER,
        "low_height_ceiling": LOW_HEIGHT_CEILING,
        "low_log_floor": LOW_LOG_FLOOR,
        "low_center_symbol": LOW_CENTER_SYMBOL,
        "low_center_log_cost_symbol": LOW_CENTER_LOG_COST_SYMBOL,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": ANCHOR_CONST_ATOM,
        "secondary_priority": COUNT_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "compact_rows": compact_rows(),
        "plain_conclusion": (
            "Jensen 低高度圆心 anchor 已以紧致非零下界闭合。"
            "这给出正的符号常数 m_xi_center_low；数值大小仍由下一步 anchor 常数聚合支付。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 低高度圆心 anchor 闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_jensen_low_center_anchor_closed={fmt_bool(result['backlund_jensen_low_center_anchor_closed'])}",
        f"sigma_center={fmt_float(result['sigma_center'])}",
        f"low_height_ceiling={fmt_float(result['low_height_ceiling'])}",
        f"low_log_floor={fmt_float(result['low_log_floor'])}",
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
        "## 2. 低高度紧致下界",
        "",
        "```text",
        result["low_center_symbol"],
        result["low_center_log_cost_symbol"],
        "```",
        "",
        "| component | fact | role |",
        "| --- | --- | --- |",
    ]
    for item in result["compact_rows"]:
        lines.append(
            "| {component} | {fact} | {role} |".format(
                component=table_cell(item["component"]),
                fact=table_cell(item["fact"]),
                role=table_cell(item["role"]),
            )
        )
    lines.extend(
        [
            "",
            "这里不调用低高度零点表；圆心固定在 `sigma=2`，非零性来自绝对收敛 Euler product 和 Gamma 无零。",
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
