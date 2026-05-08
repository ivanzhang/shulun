#!/usr/bin/env python3
"""Prime Matrix B=3 临界带凸性上界路由器。

用法示例：
  python3 experiments/prime_matrix_b3_convexity_router.py

输出：
  docs/monograph/prime-matrix-b3-convexity-router.json
  docs/monograph/prime-matrix-b3-convexity-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-horizontal-variation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-convexity-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-convexity-router.md"

OLD_ATOM = "CriticalStripConvexityLogZetaBoundNumericalLedger"
PL_CLOSED = "CriticalStripPhragmenLindelofThreeLinesClosed"
RIGHT_CLOSED = "ZetaRightEdgeEulerProductArgumentClosedCright2"
LEFT_ATOM = "FunctionalEquationLeftEdgeArgumentLedger"
CONST_ATOM = "CriticalStripConvexityC2ConstantOptimizationLedger"
HORIZONTAL_AGG_ATOM = "HorizontalVariationConstantAggregationLedger"
BACKLUND_CONST_ATOM = "BacklundArgumentConstantAggregationLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_CONVEXITY_TARGET = 2.0


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
    """写出凸性账本替换包。"""
    return f"({PL_CLOSED} AND {RIGHT_CLOSED} AND {LEFT_ATOM} AND {CONST_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧凸性原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def interpolation_rows() -> list[dict[str, float]]:
    """生成三线插值候选表。"""
    rows: list[dict[str, float]] = []
    for t in [2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        eta = 1.0 / logv
        width = 1.0 + 2.0 * eta
        rows.append(
            {
                "T": t,
                "L": logv,
                "eta": eta,
                "strip_width": width,
                "right_edge_target": C_CONVEXITY_TARGET * logv,
                "left_edge_target": C_CONVEXITY_TARGET * logv,
                "interior_target": C_CONVEXITY_TARGET * logv,
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
    """生成临界带凸性判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    right_ready = RIGHT_CLOSED in basis
    zeta_ready = "ThetaMellinZetaContinuationFunctionalEquationClosed" in basis
    pole_ready = "HorizontalPoleRemovalBudgetClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and right_ready and zeta_ready and pole_ready and guard
    return [
        row(
            "CriticalStripConvexityGateActive",
            active,
            False,
            "上一层唯一内部最窄点是临界带 log|zeta|/log|F| 的显式凸性上界。",
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
            "AnalyticEntireFAndPoleBudgetAvailable",
            zeta_ready and pole_ready,
            True,
            "用 F=(s-1)zeta(s) 避开 s=1 极点；去极点水平预算已在上一层闭合。",
            "无 pole obstruction。",
        ),
        row(
            "PhragmenLindelofThreeLinesClosed",
            reduced,
            True,
            "对整函数 F 在有限竖带内应用三线定理：log sup 在 sigma 方向由两侧边界对数凸控制。",
            PL_CLOSED,
        ),
        row(
            "RightBoundaryInputAvailable",
            right_ready,
            True,
            "右边界 sigma=1+1/L 已有 Euler product 点态预算。",
            RIGHT_CLOSED,
        ),
        row(
            "LeftBoundaryFunctionalEquationMissing",
            False,
            False,
            "仍需用函数方程和 Gamma/Stirling 预算给左边界 F 的 O(log(T+3)) 上界。",
            LEFT_ATOM,
        ),
        row(
            "ConvexityC2ConstantOptimizationMissing",
            False,
            False,
            "即使左右边界都有 O(L)，仍需核算最小高度、eta=1/L、去极点项后是否能保住 C=2 目标。",
            CONST_ATOM,
        ),
        row(
            "CriticalStripConvexityReduced",
            reduced,
            False,
            "旧凸性原子已压成三线形式原理、右边界已证输入、左边界函数方程和常数优化。",
            replacement_pair(),
        ),
        row(
            "HorizontalAggregationStillDownstream",
            False,
            False,
            "凸性常数完成后，还需回到水平边聚合，再进入 Backlund 总常数。",
            f"{HORIZONTAL_AGG_ATOM} AND {BACKLUND_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行临界带凸性路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "CriticalStripConvexityReduced")
    return {
        "certificate_type": "b3_convexity_router",
        "status": "critical_strip_convexity_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "critical_strip_convexity_reduced": reduced,
        "critical_strip_convexity_self_contained_proved": False,
        "C_convexity_target": C_CONVEXITY_TARGET,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": LEFT_ATOM,
        "secondary_priority": CONST_ATOM,
        "tertiary_priority": HORIZONTAL_AGG_ATOM,
        "quaternary_priority": BACKLUND_CONST_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "interpolation_rows": interpolation_rows(),
        "plain_conclusion": (
            "临界带凸性账本尚未闭合。"
            "本步闭合了三线/PL 形式原理并确认右边界输入可用；"
            "真正剩余回到左边函数方程预算和 C=2 常数优化。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 临界带凸性上界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"critical_strip_convexity_reduced={fmt_bool(result['critical_strip_convexity_reduced'])}",
        (
            "critical_strip_convexity_self_contained_proved="
            f"{fmt_bool(result['critical_strip_convexity_self_contained_proved'])}"
        ),
        f"C_convexity_target={fmt_float(result['C_convexity_target'])}",
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
        "## 2. 三线结构",
        "",
        (
            "对 `F=(s-1)zeta(s)` 使用三线定理，而不是直接对有极点的 `zeta` 使用。"
            "若左右边界都给出 `log|F|<=2L`，则竖带内部也给出同一 `2L` 目标；"
            "但左边界和低高度常数尚未核算，所以本层仍是 open。"
        ),
        "",
        "| T | L | eta | strip width | right target | left target | interior target |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["interpolation_rows"]:
        lines.append(
            "| {T:.6g} | `{L}` | `{eta}` | `{width}` | `{right}` | `{left}` | `{inside}` |".format(
                T=item["T"],
                L=fmt_float(item["L"]),
                eta=fmt_float(item["eta"]),
                width=fmt_float(item["strip_width"]),
                right=fmt_float(item["right_edge_target"]),
                left=fmt_float(item["left_edge_target"]),
                inside=fmt_float(item["interior_target"]),
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
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
                f"`{result['quaternary_priority']}`。"
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
