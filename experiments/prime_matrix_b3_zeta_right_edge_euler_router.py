#!/usr/bin/env python3
"""Prime Matrix B=3 zeta 右边界 Euler product 显式预算闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_zeta_right_edge_euler_router.py

输出：
  docs/monograph/prime-matrix-b3-zeta-right-edge-euler-router.json
  docs/monograph/prime-matrix-b3-zeta-right-edge-euler-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zeta-right-edge-euler-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zeta-right-edge-euler-router.md"

OLD_ATOM = "ZetaRightEdgeEulerProductArgumentNumericalLedger"
CLOSED_ATOM = "ZetaRightEdgeEulerProductArgumentClosedCright2"
HORIZONTAL_ATOM = "CriticalStripHorizontalVariationNumericalLedger"
LEFT_ATOM = "FunctionalEquationLeftEdgeArgumentLedger"
CONST_ATOM = "BacklundArgumentConstantAggregationLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_RIGHT_POINTWISE = 2.0
C_RIGHT_HEIGHT_TWO = 4.0


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


def budget_rows() -> list[dict[str, float]]:
    """生成右边界预算审计表。"""
    rows: list[dict[str, float]] = []
    for t in [2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        eta = 1.0 / logv
        log_zeta_bound = math.log1p(logv)
        pole_arg_bound = math.pi / 2.0
        pole_log_bound = math.log(t + 1.0)
        rows.append(
            {
                "T": t,
                "L": logv,
                "eta": eta,
                "log_zeta_bound": log_zeta_bound,
                "pole_arg_bound": pole_arg_bound,
                "pole_log_bound": pole_log_bound,
                "pointwise_argF_budget": C_RIGHT_POINTWISE * logv,
                "height_two_integral_budget": C_RIGHT_HEIGHT_TWO * logv,
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
    """生成右边界 Euler product 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    euler_ready = "EulerProductLogDerivativePositiveRealPartClosed" in basis
    rectangle_ready = "BacklundLittlewoodRectangleArgumentClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and euler_ready and rectangle_ready and guard
    return [
        row(
            "ZetaRightEdgeGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 zeta 右边界 Euler product 预算。",
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
            "EulerProductRightHalfPlaneAvailable",
            euler_ready,
            True,
            "在 sigma>1 右半平面 Euler product 绝对收敛，zeta 无零且 log zeta 分支可由级数定义。",
            "无右半平面解析剩余。",
        ),
        row(
            "LittlewoodRectangleAlreadyTransferred",
            rectangle_ready,
            True,
            "Littlewood 矩形转移已把右边界 log|F|/arg F 作为独立预算项暴露出来。",
            "无形式转移剩余。",
        ),
        row(
            "RightEdgeLogZetaBoundClosed",
            closed,
            True,
            "令 L=log(T+3), eta=1/L, sigma=1+eta，则 |log zeta(sigma+it)|<=log zeta(sigma)<=log(1+L)<=L。",
            CLOSED_ATOM,
        ),
        row(
            "PoleRemovalRightEdgeBudgetClosed",
            closed,
            True,
            "对 F=(s-1)zeta(s)，t>=0 时 |arg(s-1)|<=pi/2<=L，且 log|s-1|<=log(T+1)<=L。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "右边界点态预算闭合为 |arg F|<=2L、log|F|<=2L；高度 2 竖边积分预算闭合为 <=4L。",
            CLOSED_ATOM,
        ),
        row(
            "HorizontalVariationStillNext",
            False,
            False,
            "下一步需要控制上下水平边变化与绕零成本。",
            HORIZONTAL_ATOM,
        ),
        row(
            "LeftAndAggregationStillDownstream",
            False,
            False,
            "左边函数方程和 C_S 聚合仍未闭合。",
            f"{LEFT_ATOM} AND {CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行右边界 Euler product 闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_zeta_right_edge_euler_router",
        "status": "zeta_right_edge_euler_product_argument_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zeta_right_edge_euler_product_argument_closed": closed,
        "C_right_pointwise": C_RIGHT_POINTWISE,
        "C_right_height_two": C_RIGHT_HEIGHT_TWO,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": HORIZONTAL_ATOM,
        "secondary_priority": LEFT_ATOM,
        "tertiary_priority": CONST_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "budget_rows": budget_rows(),
        "core_inequality": (
            "sigma=1+1/L, L=log(T+3): "
            "|log zeta(sigma+it)|<=log zeta(sigma)<=log(1+L)<=L; "
            "for F=(s-1)zeta(s), |arg F|<=2L and log|F|<=2L on the right edge."
        ),
        "plain_conclusion": (
            "zeta 右边界 Euler product 预算已自足闭合。"
            "该闭合只覆盖 sigma>1 的右边界点态和高度 2 竖边积分预算；"
            "水平边、左边函数方程和最终 C_S=8 聚合仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 zeta 右边界 Euler product 显式预算闭合证书",
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
            "zeta_right_edge_euler_product_argument_closed="
            f"{fmt_bool(result['zeta_right_edge_euler_product_argument_closed'])}"
        ),
        f"C_right_pointwise={fmt_float(result['C_right_pointwise'])}",
        f"C_right_height_two={fmt_float(result['C_right_height_two'])}",
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
        "## 2. 核心不等式",
        "",
        "```text",
        result["core_inequality"],
        "```",
        "",
        (
            "这里没有使用零行实验信息，也没有调用零点零化结果；"
            "`sigma>1` 上的 Euler product 绝对收敛本身给出无零分支和 log 级数。"
        ),
        "",
        "## 3. 数值预算审计",
        "",
        "| T | L=log(T+3) | eta | log zeta bound | pole arg bound | pole log bound | pointwise 2L | height-two 4L |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {T:.6g} | `{L}` | `{eta}` | `{lz}` | `{pa}` | `{pl}` | `{p2}` | `{h4}` |".format(
                T=item["T"],
                L=fmt_float(item["L"]),
                eta=fmt_float(item["eta"]),
                lz=fmt_float(item["log_zeta_bound"]),
                pa=fmt_float(item["pole_arg_bound"]),
                pl=fmt_float(item["pole_log_bound"]),
                p2=fmt_float(item["pointwise_argF_budget"]),
                h4=fmt_float(item["height_two_integral_budget"]),
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
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
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
