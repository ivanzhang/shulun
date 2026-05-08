#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 独立局部零点倒距离和路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_zero_distance_sum_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-zero-distance-sum-router.json
  docs/monograph/prime-matrix-b3-backlund-zero-distance-sum-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-logder-variation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-zero-distance-sum-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-zero-distance-sum-router.md"

OLD_ATOM = "BacklundIndependentLocalZeroDistanceSumLedger"
JENSEN_ATOM = "BacklundIndependentJensenDiskZeroCountLedger"
DYADIC_CLOSED = "BacklundZeroDistanceDyadicSummationClosed"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
CONST_ATOM = "BacklundZeroDistanceSumConstantAggregationLedger"
WINDOW_ATOM = "BacklundVariationWindowScaleLedger"
INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
SLACK_ATOM = "BacklundCS8SlackAfterBridgeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_ZERO_COUNT_TARGET = 16.0
C_DISTANCE_TARGET = 64.0


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


def replacement_pair() -> str:
    """写出零点倒距离和替换包。"""
    return f"({JENSEN_ATOM} AND {DYADIC_CLOSED} AND {NEAR_ZERO_ATOM} AND {CONST_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧零点倒距离和原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def dyadic_budget_rows() -> list[dict[str, float]]:
    """生成 dyadic 倒距离求和预算表。"""
    rows: list[dict[str, float]] = []
    for radius in [1.0, 0.5, 0.25, 0.125, 0.0625]:
        shells = math.ceil(math.log2(1.0 / radius)) + 1
        rows.append(
            {
                "inner_radius": radius,
                "shell_count": float(shells),
                "zero_count_constant": C_ZERO_COUNT_TARGET,
                "distance_sum_constant_candidate": C_ZERO_COUNT_TARGET * (2.0 * shells + 2.0),
            }
        )
    return rows


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
    """生成局部零点倒距离和判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    hadamard_ready = "BacklundHadamardLogDerivativeVariationFormulaClosed" in basis
    no_circular_ready = "BacklundSpikeNoRVMCircularityDisciplineClosed" in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and hadamard_ready and no_circular_ready and xi_ready and guard
    return [
        row(
            "ZeroDistanceSumGateActive",
            active,
            False,
            "上一层唯一内部最窄点是独立局部零点倒距离和。",
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
            "HadamardNoCircularXiInputsAvailable",
            hadamard_ready and no_circular_ready and xi_ready,
            True,
            "Hadamard 变差公式、非循环纪律和 xi 整函数增长输入均已可用。",
            "无形式输入剩余。",
        ),
        row(
            "IndependentJensenDiskZeroCountMissing",
            False,
            False,
            "仍需独立 Jensen 圆盘零点计数；不得调用 RVM/Backlund 导出的局部零点计数。",
            JENSEN_ATOM,
        ),
        row(
            "ZeroDistanceDyadicSummationClosed",
            reduced,
            True,
            "一旦每个 dyadic 环的零点数有 O(log(T+3)) 上界，倒距离和由 dyadic 环求和转为常数聚合。",
            DYADIC_CLOSED,
        ),
        row(
            "NearZeroIndentSeparationMissing",
            False,
            False,
            "离中心过近的零点不能直接进倒距离和，必须切给凹口/端点成本账本。",
            NEAR_ZERO_ATOM,
        ),
        row(
            "ZeroDistanceConstantAggregationMissing",
            False,
            False,
            "仍需把 Jensen 计数常数、dyadic 层数和近零截断合并为局部变差可用常数。",
            CONST_ATOM,
        ),
        row(
            "IndependentLocalZeroDistanceSumReduced",
            reduced,
            False,
            "旧零点倒距离和原子已压成独立 Jensen 计数、dyadic 求和、近零分离、常数聚合四包。",
            replacement_pair(),
        ),
        row(
            "WindowIndentSlackStillDownstream",
            False,
            False,
            "之后还需窗口尺度、凹口成本和 C_S=8 余量验收。",
            f"{WINDOW_ATOM} AND {INDENT_ATOM} AND {SLACK_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行局部零点倒距离和路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "IndependentLocalZeroDistanceSumReduced")
    return {
        "certificate_type": "b3_backlund_zero_distance_sum_router",
        "status": "backlund_independent_local_zero_distance_sum_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_independent_local_zero_distance_sum_reduced": reduced,
        "backlund_independent_local_zero_distance_sum_self_contained_proved": False,
        "C_zero_count_target": C_ZERO_COUNT_TARGET,
        "C_distance_target": C_DISTANCE_TARGET,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": JENSEN_ATOM,
        "secondary_priority": NEAR_ZERO_ATOM,
        "tertiary_priority": CONST_ATOM,
        "post_zero_distance_priority": WINDOW_ATOM,
        "post_window_priority": INDENT_ATOM,
        "post_indent_priority": SLACK_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "dyadic_budget_rows": dyadic_budget_rows(),
        "plain_conclusion": (
            "独立局部零点倒距离和尚未闭合。"
            "本步闭合了 dyadic 求和形式层，但真正硬点是独立 Jensen 圆盘零点计数；"
            "它必须不依赖 Backlund/RVM。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 独立局部零点倒距离和路由器",
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
            "backlund_independent_local_zero_distance_sum_reduced="
            f"{fmt_bool(result['backlund_independent_local_zero_distance_sum_reduced'])}"
        ),
        (
            "backlund_independent_local_zero_distance_sum_self_contained_proved="
            f"{fmt_bool(result['backlund_independent_local_zero_distance_sum_self_contained_proved'])}"
        ),
        f"C_zero_count_target={fmt_float(result['C_zero_count_target'])}",
        f"C_distance_target={fmt_float(result['C_distance_target'])}",
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
        "## 2. dyadic 预算压力",
        "",
        "| inner radius | shell count | zero-count constant | distance-sum candidate |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in result["dyadic_budget_rows"]:
        lines.append(
            "| `{radius}` | `{shells}` | `{zero}` | `{dist}` |".format(
                radius=fmt_float(item["inner_radius"]),
                shells=fmt_float(item["shell_count"]),
                zero=fmt_float(item["zero_count_constant"]),
                dist=fmt_float(item["distance_sum_constant_candidate"]),
            )
        )
    lines.extend(
        [
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
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`。"
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
