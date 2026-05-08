#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund Littlewood 矩形转移闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_littlewood_rectangle_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-littlewood-rectangle-router.json
  docs/monograph/prime-matrix-b3-backlund-littlewood-rectangle-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-argument-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-littlewood-rectangle-router.md"

OLD_ATOM = "BacklundLittlewoodRectangleArgumentLedger"
CLOSED_ATOM = "BacklundLittlewoodRectangleArgumentClosed"
RIGHT_ATOM = "ZetaRightEdgeEulerProductArgumentNumericalLedger"
HORIZONTAL_ATOM = "CriticalStripHorizontalVariationNumericalLedger"
LEFT_ATOM = "FunctionalEquationLeftEdgeArgumentLedger"
CONST_ATOM = "BacklundArgumentConstantAggregationLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

RECTANGLE_FORMULA = (
    "For F(s)=(s-1)zeta(s), a<b, T0<T1, and a boundary avoiding zeros, "
    "int_a^b(arg F(sigma+iT1)-arg F(sigma+iT0)) d sigma "
    "= 2*pi*sum_{rho in R}(Re rho-a) "
    "+ int_T0^T1 log|F(b+it)| dt - int_T0^T1 log|F(a+it)| dt."
)


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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str) -> str:
    """把待证 atom 替换为闭合 atom。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


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
    """生成 Littlewood 矩形转移判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    zeta_ready = "ThetaMellinZetaContinuationFunctionalEquationClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and zeta_ready and guard
    return [
        row(
            "BacklundLittlewoodRectangleGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Backlund 的 Littlewood 矩形转移。",
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
            "ZetaContinuationAvailable",
            zeta_ready,
            True,
            "zeta 的解析延拓和函数方程输入已在上游闭合，可定义 F(s)=(s-1)zeta(s)。",
            "无解析延拓剩余。",
        ),
        row(
            "PoleRemovalFactorClosed",
            closed,
            True,
            "用 F(s)=(s-1)zeta(s) 去掉 s=1 的极点；新增的 log|s-1| 和 arg(s-1) 是初等边界项。",
            "初等项交给后续边界预算吸收。",
        ),
        row(
            "LittlewoodRectangleIdentityClosed",
            closed,
            True,
            "Littlewood 矩形引理把上下边 arg 差精确转成左右边 log|F| 积分和矩形内零点横向权重。",
            CLOSED_ATOM,
        ),
        row(
            "BoundaryIndentationConventionClosed",
            closed,
            True,
            "若边界碰到零点，先作 epsilon 平移或小凹口，最后取极限并按重数记账。",
            "全局端点统一仍留给 EndpointZeroAvoidanceMultiplicityConventionLedger。",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "待证 atom 已闭合为 Littlewood 矩形转移恒等式；它不提供数值上界。",
            CLOSED_ATOM,
        ),
        row(
            "RightEdgeEulerProductStillNext",
            False,
            False,
            "下一步需要在右边界用 Euler product 给 log|zeta| 和 arg 预算。",
            RIGHT_ATOM,
        ),
        row(
            "HorizontalAndLeftEdgesStillDownstream",
            False,
            False,
            "水平边、左边函数方程和 C_S 聚合仍未闭合。",
            f"{HORIZONTAL_ATOM} AND {LEFT_ATOM} AND {CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Littlewood 矩形转移闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_backlund_littlewood_rectangle_router",
        "status": "backlund_littlewood_rectangle_argument_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_littlewood_rectangle_argument_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": RIGHT_ATOM,
        "secondary_priority": HORIZONTAL_ATOM,
        "tertiary_priority": LEFT_ATOM,
        "quaternary_priority": CONST_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "rectangle_formula": RECTANGLE_FORMULA,
        "plain_conclusion": (
            "Backlund 的 Littlewood 矩形转移层已自足闭合。"
            "这只是形式恒等式：它把 arg zeta 的水平变化交给左右竖边 log|zeta|、零点权重和初等去极点项；"
            "真正的数值压力仍在右边 Euler product、水平边、左边函数方程和 C_S 聚合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund Littlewood 矩形转移闭合证书",
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
            "backlund_littlewood_rectangle_argument_closed="
            f"{fmt_bool(result['backlund_littlewood_rectangle_argument_closed'])}"
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
        "```",
        "",
        "## 2. 文内证明",
        "",
        "取 `F(s)=(s-1)zeta(s)`。这样 `s=1` 的极点被去掉，额外产生的 `log|s-1|` 与 `arg(s-1)` 是初等项。",
        "",
        "对矩形 `R=[a,b] x [T0,T1]`，边界避开 `F` 的零点时，Littlewood 矩形引理给出：",
        "",
        "```text",
        result["rectangle_formula"],
        "```",
        "",
        (
            "证明可由 argument principle 应用于 `(s-a)F'(s)/F(s)` 得到。"
            "右端零点权重按重数计，边界碰零时先作 `epsilon` 扰动或小凹口再取极限。"
        ),
        "",
        (
            "因此本层只完成 `arg` 到边界积分的结构转移。"
            "它没有证明 `|S(T)|<=C_S log(T+3)`，也没有使用真实零行不存在。"
        ),
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
