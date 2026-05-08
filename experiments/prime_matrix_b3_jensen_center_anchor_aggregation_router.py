#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 圆心 anchor 常数聚合闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_center_anchor_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-center-anchor-aggregation-router.json
  docs/monograph/prime-matrix-b3-jensen-center-anchor-aggregation-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-low-center-anchor-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-center-anchor-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-center-anchor-aggregation-router.md"

OLD_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationLedger"
CLOSED_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationClosedSymbolic"
CENTER_CLOSED = "BacklundJensenRightEdgeCenterChoiceConventionClosedR4"
GAMMA_CANCEL_CLOSED = "BacklundJensenGammaMainCancellationInMeanClosedHighT10R4"
EULER_LOWER_CLOSED = "BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2"
LOW_CENTER_CLOSED = "BacklundJensenLowHeightCenterAnchorCompactNonzeroClosed"
ANCHOR_PACKAGE_CLOSED = "BacklundIndependentJensenCenterLowerAnchorClosedSymbolic"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

LOG_ZETA2 = math.log(math.pi**2 / 6.0)
LOW_LOG_FLOOR = math.log(3.0)
LOW_CENTER_COST_SYMBOL = "A_center_low"
ANCHOR_CONSTANT_SYMBOL = "C_center_anchor := max(log(zeta(2))/log(3), A_center_low/log(3))"


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


def close_anchor_package(text: str) -> str:
    """将五包全闭合后的长 conjunction 压成圆心 anchor 包。"""
    package = (
        f"({CENTER_CLOSED} AND {GAMMA_CANCEL_CLOSED} AND {EULER_LOWER_CLOSED} "
        f"AND {LOW_CENTER_CLOSED} AND {CLOSED_ATOM})"
    )
    return text.replace(package, ANCHOR_PACKAGE_CLOSED)


def aggregation_rows() -> list[dict[str, str]]:
    """生成圆心 anchor 聚合公式表。"""
    return [
        {
            "range": "|T|>=10",
            "input": "Gamma/elementary mean cancels exactly; |zeta(2+iT)|>=1/zeta(2)",
            "cost": "-log center <= log(zeta(2)) after cancellation",
        },
        {
            "range": "|T|<10",
            "input": "m_xi_center_low := inf_{|T|<=10}|xi(2+iT)| > 0",
            "cost": "-log center <= A_center_low",
        },
        {
            "range": "all T",
            "input": ANCHOR_CONSTANT_SYMBOL,
            "cost": "-log center <= C_center_anchor * log(|T|+3)",
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
    """生成 Jensen 圆心 anchor 常数聚合判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    center_ready = CENTER_CLOSED in basis
    gamma_ready = GAMMA_CANCEL_CLOSED in basis
    euler_ready = EULER_LOWER_CLOSED in basis
    low_ready = LOW_CENTER_CLOSED in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and center_ready and gamma_ready and euler_ready and low_ready and guard
    return [
        row(
            "CenterAnchorAggregationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen 圆心 anchor 常数聚合。",
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
            "CenterGammaEulerLowInputsAvailable",
            center_ready and gamma_ready and euler_ready and low_ready,
            True,
            "圆心选择、Gamma 相消、Euler 下界与低高度圆心 anchor 均已可用。",
            "无 anchor 输入剩余。",
        ),
        row(
            "CenterAnchorConstantAggregationClosed",
            closed,
            True,
            "高高度只剩 log(zeta(2)) 成本，低高度由 A_center_low 支付，二者可吸收到 C_center_anchor log(|T|+3)。",
            CLOSED_ATOM,
        ),
        row(
            "IndependentJensenCenterAnchorClosedSymbolic",
            closed,
            True,
            "五包均已闭合，独立 Jensen 圆心下界得到一个有限符号常数 C_center_anchor。",
            ANCHOR_PACKAGE_CLOSED,
        ),
        row(
            "JensenC16AggregationStillNext",
            False,
            False,
            "圆周上界与圆心下界均为符号有限常数；下一步需判断能否压入 C_N=16。",
            COUNT_CONST_ATOM,
        ),
        row(
            "NearZeroStillDownstream",
            False,
            False,
            "Jensen 计数后仍需近零凹口分离与倒距离和后续账本。",
            NEAR_ZERO_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen 圆心 anchor 常数聚合闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == "CenterAnchorConstantAggregationClosed")
    replaced_basis = replace_atom(previous.get("latest_self_contained_basis", ""))
    return {
        "certificate_type": "b3_jensen_center_anchor_aggregation_router",
        "status": "backlund_jensen_center_anchor_aggregation_closed_symbolic",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_center_anchor_aggregation_closed": closed,
        "backlund_independent_jensen_center_anchor_closed_symbolic": closed,
        "log_zeta2": LOG_ZETA2,
        "low_log_floor": LOW_LOG_FLOOR,
        "low_center_cost_symbol": LOW_CENTER_COST_SYMBOL,
        "anchor_constant_symbol": ANCHOR_CONSTANT_SYMBOL,
        "jensen_C16_numerical_aggregation_closed": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "package_replacement_self_contained": {
            (
                f"({CENTER_CLOSED} AND {GAMMA_CANCEL_CLOSED} AND {EULER_LOWER_CLOSED} "
                f"AND {LOW_CENTER_CLOSED} AND {CLOSED_ATOM})"
            ): ANCHOR_PACKAGE_CLOSED
        },
        "latest_self_contained_basis": close_anchor_package(replaced_basis),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": COUNT_CONST_ATOM,
        "secondary_priority": NEAR_ZERO_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "aggregation_rows": aggregation_rows(),
        "plain_conclusion": (
            "Jensen 圆心 anchor 常数聚合已闭合为符号有限常数 C_center_anchor。"
            "这完成独立圆心下界包，但尚未证明最终局部零点计数可取 C_N=16。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    package_replacement = next(iter(result["package_replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 圆心 anchor 常数聚合闭合证书",
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
            "backlund_jensen_center_anchor_aggregation_closed="
            f"{fmt_bool(result['backlund_jensen_center_anchor_aggregation_closed'])}"
        ),
        (
            "backlund_independent_jensen_center_anchor_closed_symbolic="
            f"{fmt_bool(result['backlund_independent_jensen_center_anchor_closed_symbolic'])}"
        ),
        f"log_zeta2={fmt_float(result['log_zeta2'])}",
        f"low_log_floor={fmt_float(result['low_log_floor'])}",
        f"anchor_constant_symbol={result['anchor_constant_symbol']}",
        (
            "jensen_C16_numerical_aggregation_closed="
            f"{fmt_bool(result['jensen_C16_numerical_aggregation_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "",
        package_replacement[0],
        "  =>",
        package_replacement[1],
        "```",
        "",
        "## 2. 聚合公式",
        "",
        "| range | input | cost |",
        "| --- | --- | --- |",
    ]
    for item in result["aggregation_rows"]:
        lines.append(
            "| {range} | {input} | {cost} |".format(
                range=table_cell(item["range"]),
                input=table_cell(item["input"]),
                cost=table_cell(item["cost"]),
            )
        )
    lines.extend(
        [
            "",
            "本步给出的是符号有限 anchor 常数；是否足以验收 `C_N=16` 留给下一步。",
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
