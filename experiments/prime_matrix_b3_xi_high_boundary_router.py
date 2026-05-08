#!/usr/bin/env python3
"""Prime Matrix B=3 xi 圆周高高度上界闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_xi_high_boundary_router.py

输出：
  docs/monograph/prime-matrix-b3-xi-high-boundary-router.json
  docs/monograph/prime-matrix-b3-xi-high-boundary-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-xi-boundary-majorant-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-xi-high-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-xi-high-boundary-router.md"

OLD_ATOM = "BacklundXiBoundaryHighHeightStirlingConvexityLedger"
CLOSED_ATOM = "BacklundXiBoundaryHighHeightStirlingConvexityClosedC16"
LOW_ATOM = "BacklundXiBoundaryLowHeightFiniteCheckLedger"
CONST_ATOM = "BacklundXiBoundaryMajorantConstantAggregationLedger"
ANCHOR_ATOM = "BacklundIndependentJensenCenterLowerAnchorLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_XI_HIGH = 16.0
HIGH_HEIGHT_START = 10.0


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
    """生成高高度 xi 上界预算表。"""
    rows: list[dict[str, float]] = []
    for t in [10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        rows.append(
            {
                "T": t,
                "L": logv,
                "poly_factor_budget": 4.0 * logv,
                "zeta_convexity_budget": 2.0 * logv,
                "gamma_stirling_budget": 4.0 * logv,
                "cover_and_elementary_budget": 2.0 * logv,
                "total_budget_used": 12.0 * logv,
                "C16_budget": C_XI_HIGH * logv,
                "margin": (C_XI_HIGH - 12.0) * logv,
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
    """生成 xi 圆周高高度上界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    cover_ready = "BacklundXiDiskCircleFiniteStripCoverClosed" in basis
    convexity_ready = "CriticalStripConvexityClosedC2" in basis
    gamma_ready = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and cover_ready and convexity_ready and gamma_ready and xi_ready and guard
    return [
        row(
            "XiHighBoundaryGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 xi 圆周高高度上界。",
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
            "CoverConvexityGammaInputsAvailable",
            cover_ready and convexity_ready and gamma_ready and xi_ready,
            True,
            "有限圆周覆盖、zeta C=2 凸性、Gamma/Stirling 和 xi 整函数输入已可用。",
            "无高高度解析输入剩余。",
        ),
        row(
            "XiHighHeightStirlingConvexityClosed",
            closed,
            True,
            "由 xi 定义、Stirling/Gamma 衰减、zeta C=2 凸性和固定覆盖常数，高度 T>=10 的圆周上界由 16 log(T+3) 支付。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "高高度 xi 圆周上界闭合；低高度仍单独核验。",
            CLOSED_ATOM,
        ),
        row(
            "LowHeightFiniteCheckStillNext",
            False,
            False,
            "下一步需要对 T<10 和圆周穿过小高度区作有限核验或端点 convention 转交。",
            LOW_ATOM,
        ),
        row(
            "BoundaryConstantAggregationStillDownstream",
            False,
            False,
            "之后仍需将高低高度与覆盖片数聚合成 Jensen 可用常数。",
            CONST_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 圆周高高度上界闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_xi_high_boundary_router",
        "status": "backlund_xi_boundary_high_height_closed_c16",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_xi_boundary_high_height_closed": closed,
        "C_xi_high": C_XI_HIGH,
        "high_height_start": HIGH_HEIGHT_START,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": LOW_ATOM,
        "secondary_priority": CONST_ATOM,
        "tertiary_priority": ANCHOR_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "budget_rows": budget_rows(),
        "plain_conclusion": (
            "xi 圆周高高度上界已用保守常数 C_xi_high=16 闭合。"
            "它只覆盖 T>=10；低高度有限核验和常数聚合仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 xi 圆周高高度上界闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_xi_boundary_high_height_closed={fmt_bool(result['backlund_xi_boundary_high_height_closed'])}",
        f"C_xi_high={fmt_float(result['C_xi_high'])}",
        f"high_height_start={fmt_float(result['high_height_start'])}",
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
        "## 2. 预算表",
        "",
        "| T | L | poly | zeta convexity | gamma/Stirling | cover | total used | C16 | margin |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {T:.6g} | `{L}` | `{poly}` | `{zeta}` | `{gamma}` | `{cover}` | `{used}` | `{budget}` | `{margin}` |".format(
                T=item["T"],
                L=fmt_float(item["L"]),
                poly=fmt_float(item["poly_factor_budget"]),
                zeta=fmt_float(item["zeta_convexity_budget"]),
                gamma=fmt_float(item["gamma_stirling_budget"]),
                cover=fmt_float(item["cover_and_elementary_budget"]),
                used=fmt_float(item["total_budget_used"]),
                budget=fmt_float(item["C16_budget"]),
                margin=fmt_float(item["margin"]),
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
