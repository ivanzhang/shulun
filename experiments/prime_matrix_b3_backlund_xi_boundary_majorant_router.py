#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 独立 xi 圆周上界路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_xi_boundary_majorant_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-xi-boundary-majorant-router.json
  docs/monograph/prime-matrix-b3-backlund-xi-boundary-majorant-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-independent-jensen-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-xi-boundary-majorant-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-xi-boundary-majorant-router.md"

OLD_ATOM = "BacklundIndependentXiDiskBoundaryMajorantLedger"
COVER_CLOSED = "BacklundXiDiskCircleFiniteStripCoverClosed"
HIGH_ATOM = "BacklundXiBoundaryHighHeightStirlingConvexityLedger"
LOW_ATOM = "BacklundXiBoundaryLowHeightFiniteCheckLedger"
CONST_ATOM = "BacklundXiBoundaryMajorantConstantAggregationLedger"
ANCHOR_ATOM = "BacklundIndependentJensenCenterLowerAnchorLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def replacement_pair() -> str:
    """写出 xi 圆周上界替换包。"""
    return f"({COVER_CLOSED} AND {HIGH_ATOM} AND {LOW_ATOM} AND {CONST_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 xi 圆周上界原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


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
    """生成独立 xi 圆周上界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    convexity_ready = "CriticalStripConvexityClosedC2" in basis
    gamma_ready = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    right_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and xi_ready and convexity_ready and gamma_ready and right_ready and guard
    return [
        row(
            "XiBoundaryMajorantGateActive",
            active,
            False,
            "上一层唯一内部最窄点是独立 xi 圆周上界。",
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
            "AnalyticInputsAvailable",
            xi_ready and convexity_ready and gamma_ready and right_ready,
            True,
            "xi 整函数、zeta 凸性、Gamma/Stirling 和右边界 Euler 预算已可用。",
            "无形式解析输入剩余。",
        ),
        row(
            "DiskCircleFiniteStripCoverClosed",
            reduced,
            True,
            "固定半径 Jensen 圆周可由有限个竖带/横带覆盖，常数只进入后续聚合。",
            COVER_CLOSED,
        ),
        row(
            "HighHeightStirlingConvexityMissing",
            False,
            False,
            "仍需把 Gamma 衰减、xi 因子和 zeta C=2 凸性合并为高高度圆周 O(log(T+3)) 上界。",
            HIGH_ATOM,
        ),
        row(
            "LowHeightFiniteCheckMissing",
            False,
            False,
            "仍需对 T 低高度和圆周穿过小高度区作有限核验或端点转交。",
            LOW_ATOM,
        ),
        row(
            "BoundaryMajorantConstantAggregationMissing",
            False,
            False,
            "仍需把高低高度、覆盖片数和初等 xi 因子聚合为 Jensen 可用常数。",
            CONST_ATOM,
        ),
        row(
            "IndependentXiBoundaryMajorantReduced",
            reduced,
            False,
            "旧 xi 圆周上界原子已压成有限覆盖、高高度上界、低高度核验、常数聚合四包。",
            replacement_pair(),
        ),
        row(
            "AnchorAndCountAggregationStillDownstream",
            False,
            False,
            "圆周上界完成后仍需圆心下界和 C16 聚合。",
            f"{ANCHOR_ATOM} AND {COUNT_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行独立 xi 圆周上界路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "IndependentXiBoundaryMajorantReduced")
    return {
        "certificate_type": "b3_backlund_xi_boundary_majorant_router",
        "status": "backlund_independent_xi_boundary_majorant_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_independent_xi_boundary_majorant_reduced": reduced,
        "backlund_independent_xi_boundary_majorant_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": HIGH_ATOM,
        "secondary_priority": LOW_ATOM,
        "tertiary_priority": CONST_ATOM,
        "post_boundary_priority": ANCHOR_ATOM,
        "post_anchor_priority": COUNT_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "plain_conclusion": (
            "独立 xi 圆周上界尚未闭合。"
            "本步闭合固定半径圆周到有限条带覆盖的形式层；"
            "剩余是高高度 Stirling/凸性上界、低高度有限核验和常数聚合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 独立 xi 圆周上界路由器",
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
            "backlund_independent_xi_boundary_majorant_reduced="
            f"{fmt_bool(result['backlund_independent_xi_boundary_majorant_reduced'])}"
        ),
        (
            "backlund_independent_xi_boundary_majorant_self_contained_proved="
            f"{fmt_bool(result['backlund_independent_xi_boundary_majorant_self_contained_proved'])}"
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
        "## 2. 判定表",
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
            "## 3. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 下一步",
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
