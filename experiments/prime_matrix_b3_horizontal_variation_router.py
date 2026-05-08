#!/usr/bin/env python3
"""Prime Matrix B=3 临界带水平边变化路由器。

用法示例：
  python3 experiments/prime_matrix_b3_horizontal_variation_router.py

输出：
  docs/monograph/prime-matrix-b3-horizontal-variation-router.json
  docs/monograph/prime-matrix-b3-horizontal-variation-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zeta-right-edge-euler-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-horizontal-variation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-horizontal-variation-router.md"

OLD_ATOM = "CriticalStripHorizontalVariationNumericalLedger"
INDENT_CLOSED = "HorizontalZeroIndentationConventionClosed"
POLE_CLOSED = "HorizontalPoleRemovalBudgetClosed"
CONVEXITY_ATOM = "CriticalStripConvexityLogZetaBoundNumericalLedger"
AGG_ATOM = "HorizontalVariationConstantAggregationLedger"
LEFT_ATOM = "FunctionalEquationLeftEdgeArgumentLedger"
BACKLUND_CONST_ATOM = "BacklundArgumentConstantAggregationLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_CONVEXITY_CANDIDATE = 2.0
C_HORIZONTAL_CANDIDATE = 8.0


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
    """写出水平边账本替换包。"""
    return f"({INDENT_CLOSED} AND {POLE_CLOSED} AND {CONVEXITY_ATOM} AND {AGG_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧水平边原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def candidate_budget_rows() -> list[dict[str, float]]:
    """生成候选水平边预算表。"""
    rows: list[dict[str, float]] = []
    for t in [2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        eta = 1.0 / logv
        strip_width = 1.0 + 2.0 * eta
        convexity_integral = C_CONVEXITY_CANDIDATE * strip_width * logv
        pole_integral = strip_width * logv
        total_candidate = convexity_integral + pole_integral
        rows.append(
            {
                "T": t,
                "L": logv,
                "eta": eta,
                "strip_width": strip_width,
                "convexity_integral_candidate": convexity_integral,
                "pole_integral_candidate": pole_integral,
                "total_candidate": total_candidate,
                "C_horizontal_L": C_HORIZONTAL_CANDIDATE * logv,
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
    """生成临界带水平边变化判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    rectangle_ready = "BacklundLittlewoodRectangleArgumentClosed" in basis
    right_edge_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and rectangle_ready and right_edge_ready and guard
    return [
        row(
            "CriticalStripHorizontalGateActive",
            active,
            False,
            "上一层唯一内部最窄点是临界带水平边变化预算。",
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
            "RectangleAndRightEdgeAvailable",
            rectangle_ready and right_edge_ready,
            True,
            "Littlewood 矩形转移和右边界 Euler product 预算已闭合。",
            "无右边界形式剩余。",
        ),
        row(
            "HorizontalZeroIndentationConventionClosed",
            reduced,
            True,
            "水平边若穿过零点，采用 epsilon 平移或小凹口；缩进贡献按重数进入端点/零点 convention。",
            INDENT_CLOSED,
        ),
        row(
            "HorizontalPoleRemovalBudgetClosed",
            reduced,
            True,
            "F=(s-1)zeta(s) 的去极点因子在宽度 1+2/L 的水平边上贡献至多初等 O(L)。",
            POLE_CLOSED,
        ),
        row(
            "CriticalStripConvexityLogZetaBoundMissing",
            False,
            False,
            "仍需自足证明临界带内 log|zeta(s)| 的显式凸性/三线型 O(log(T+3)) 上界。",
            CONVEXITY_ATOM,
        ),
        row(
            "HorizontalVariationConstantAggregationMissing",
            False,
            False,
            "仍需把凸性上界、去极点项、上下两条水平边和缩进成本聚合为指定水平边常数。",
            AGG_ATOM,
        ),
        row(
            "CriticalStripHorizontalVariationReduced",
            reduced,
            False,
            "旧水平边原子已压成两个闭合 convention 和两个真正数值剩余。",
            replacement_pair(),
        ),
        row(
            "LeftAndBacklundAggregationStillDownstream",
            False,
            False,
            "水平边之后还需左边函数方程与 Backlund 总常数聚合。",
            f"{LEFT_ATOM} AND {BACKLUND_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行临界带水平边变化路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "CriticalStripHorizontalVariationReduced")
    return {
        "certificate_type": "b3_horizontal_variation_router",
        "status": "critical_strip_horizontal_variation_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "critical_strip_horizontal_variation_reduced": reduced,
        "critical_strip_horizontal_variation_self_contained_proved": False,
        "C_convexity_candidate": C_CONVEXITY_CANDIDATE,
        "C_horizontal_candidate": C_HORIZONTAL_CANDIDATE,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": CONVEXITY_ATOM,
        "secondary_priority": AGG_ATOM,
        "tertiary_priority": LEFT_ATOM,
        "quaternary_priority": BACKLUND_CONST_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_budget_rows": candidate_budget_rows(),
        "plain_conclusion": (
            "临界带水平边账本尚未自足闭合。"
            "本步已闭合避零缩进 convention 与去极点初等预算，并把真正硬点压成："
            "临界带 log|zeta| 显式凸性上界，以及把该上界聚合进水平边常数。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 临界带水平边变化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"critical_strip_horizontal_variation_reduced={fmt_bool(result['critical_strip_horizontal_variation_reduced'])}",
        (
            "critical_strip_horizontal_variation_self_contained_proved="
            f"{fmt_bool(result['critical_strip_horizontal_variation_self_contained_proved'])}"
        ),
        f"C_convexity_candidate={fmt_float(result['C_convexity_candidate'])}",
        f"C_horizontal_candidate={fmt_float(result['C_horizontal_candidate'])}",
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
        "## 2. 候选预算",
        "",
        (
            "下面只审计若能证明 `log|zeta(s)|<=2 log(T+3)` 型临界带凸性上界时，"
            "水平边常数的量级是否还有余量；该表不是凸性定理证明。"
        ),
        "",
        "| T | L | eta | strip width | convexity integral | pole integral | total candidate | 8L budget |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["candidate_budget_rows"]:
        lines.append(
            "| {T:.6g} | `{L}` | `{eta}` | `{width}` | `{conv}` | `{pole}` | `{total}` | `{budget}` |".format(
                T=item["T"],
                L=fmt_float(item["L"]),
                eta=fmt_float(item["eta"]),
                width=fmt_float(item["strip_width"]),
                conv=fmt_float(item["convexity_integral_candidate"]),
                pole=fmt_float(item["pole_integral_candidate"]),
                total=fmt_float(item["total_candidate"]),
                budget=fmt_float(item["C_horizontal_L"]),
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
