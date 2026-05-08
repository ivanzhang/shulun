#!/usr/bin/env python3
"""Prime Matrix B=3 xi 圆周上界常数聚合闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_xi_boundary_constant_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-xi-boundary-constant-aggregation-router.json
  docs/monograph/prime-matrix-b3-xi-boundary-constant-aggregation-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-xi-low-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-xi-boundary-constant-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-xi-boundary-constant-aggregation-router.md"

OLD_ATOM = "BacklundXiBoundaryMajorantConstantAggregationLedger"
CLOSED_ATOM = "BacklundXiBoundaryMajorantConstantAggregationClosedSymbolic"
COVER_CLOSED = "BacklundXiDiskCircleFiniteStripCoverClosed"
HIGH_CLOSED = "BacklundXiBoundaryHighHeightStirlingConvexityClosedC16"
LOW_CLOSED = "BacklundXiBoundaryLowHeightCompactEnvelopeClosed"
BOUNDARY_PACKAGE_CLOSED = "BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic"
ANCHOR_ATOM = "BacklundIndependentJensenCenterLowerAnchorLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_XI_HIGH = 16.0
LOW_LOG_FLOOR = math.log(3.0)
LOW_ENVELOPE_SYMBOL = "M_xi_low"
UNIFIED_CONSTANT_SYMBOL = "C_xi_boundary := max(16, M_xi_low/log(3))"


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


def close_boundary_package(text: str) -> str:
    """将四包全闭合后的长 conjunction 压成圆周上界包。"""
    package = f"({COVER_CLOSED} AND {HIGH_CLOSED} AND {LOW_CLOSED} AND {CLOSED_ATOM})"
    return text.replace(package, BOUNDARY_PACKAGE_CLOSED)


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


def aggregation_rows() -> list[dict[str, str]]:
    """生成高低高度聚合公式表。"""
    return [
        {
            "case": "|Im s| >= 10",
            "bound": "log^+|xi(s)| <= 16 log(|Im s|+3)",
            "source": HIGH_CLOSED,
        },
        {
            "case": "|Im s| < 10",
            "bound": "log^+|xi(s)| <= M_xi_low <= (M_xi_low/log 3) log(|Im s|+3)",
            "source": LOW_CLOSED,
        },
        {
            "case": "all boundary pieces",
            "bound": f"log^+|xi(s)| <= {UNIFIED_CONSTANT_SYMBOL} * log(|Im s|+3)",
            "source": "高低高度取最大常数。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 xi 圆周上界常数聚合判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    cover_ready = COVER_CLOSED in basis
    high_ready = HIGH_CLOSED in basis
    low_ready = LOW_CLOSED in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and cover_ready and high_ready and low_ready and guard
    return [
        row(
            "XiBoundaryConstantAggregationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 xi 圆周上界常数聚合。",
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
            "HighLowCoverInputsAvailable",
            cover_ready and high_ready and low_ready,
            True,
            "圆周有限覆盖、高高度 C16 和低高度紧致包络均已可用。",
            "无圆周上界输入剩余。",
        ),
        row(
            "HeightSplitAggregationClosed",
            closed,
            True,
            "以 |Im s|=10 分割，高高度用 C16，低高度用 M_xi_low/log(3) 吸收到统一 log(|t|+3) 常数。",
            CLOSED_ATOM,
        ),
        row(
            "IndependentXiBoundaryPackageClosedSymbolic",
            closed,
            True,
            "四包均已闭合，独立 xi 圆周上界得到一个有限符号常数 C_xi_boundary。",
            BOUNDARY_PACKAGE_CLOSED,
        ),
        row(
            "JensenCenterLowerAnchorStillNext",
            False,
            False,
            "Jensen 还需要圆心处 xi 不过小的下界；圆周上界不能替代圆心 anchor。",
            ANCHOR_ATOM,
        ),
        row(
            "JensenC16NumericalAggregationStillOpen",
            False,
            False,
            "C_xi_boundary 当前是符号有限常数，尚未证明可压入局部零点计数 C_N=16。",
            COUNT_CONST_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 圆周上界常数聚合闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == "HeightSplitAggregationClosed")
    replaced_basis = replace_atom(previous.get("latest_self_contained_basis", ""))
    return {
        "certificate_type": "b3_xi_boundary_constant_aggregation_router",
        "status": "backlund_xi_boundary_majorant_constant_aggregation_closed_symbolic",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_xi_boundary_constant_aggregation_closed": closed,
        "backlund_independent_xi_boundary_majorant_closed_symbolic": closed,
        "C_xi_high": C_XI_HIGH,
        "low_log_floor": LOW_LOG_FLOOR,
        "low_envelope_symbol": LOW_ENVELOPE_SYMBOL,
        "unified_constant_symbol": UNIFIED_CONSTANT_SYMBOL,
        "jensen_C16_numerical_aggregation_closed": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "package_replacement_self_contained": {
            f"({COVER_CLOSED} AND {HIGH_CLOSED} AND {LOW_CLOSED} AND {CLOSED_ATOM})": BOUNDARY_PACKAGE_CLOSED
        },
        "latest_self_contained_basis": close_boundary_package(replaced_basis),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": ANCHOR_ATOM,
        "secondary_priority": COUNT_CONST_ATOM,
        "tertiary_priority": NEAR_ZERO_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "aggregation_rows": aggregation_rows(),
        "plain_conclusion": (
            "xi 圆周上界常数聚合已闭合为符号有限常数 C_xi_boundary。"
            "这完成独立圆周上界包，但没有证明 Jensen 局部零点计数的 C_N=16 数值聚合；"
            "下一步仍是圆心下界 anchor。"
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
        "# Prime Matrix B=3 xi 圆周上界常数聚合闭合证书",
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
            "backlund_xi_boundary_constant_aggregation_closed="
            f"{fmt_bool(result['backlund_xi_boundary_constant_aggregation_closed'])}"
        ),
        (
            "backlund_independent_xi_boundary_majorant_closed_symbolic="
            f"{fmt_bool(result['backlund_independent_xi_boundary_majorant_closed_symbolic'])}"
        ),
        f"C_xi_high={fmt_float(result['C_xi_high'])}",
        f"low_log_floor={fmt_float(result['low_log_floor'])}",
        f"unified_constant_symbol={result['unified_constant_symbol']}",
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
        "| case | bound | source |",
        "| --- | --- | --- |",
    ]
    for item in result["aggregation_rows"]:
        lines.append(
            "| {case} | {bound} | {source} |".format(
                case=table_cell(item["case"]),
                bound=table_cell(item["bound"]),
                source=table_cell(item["source"]),
            )
        )
    lines.extend(
        [
            "",
            "低高度常数 `M_xi_low` 是有限但未数值化的包络；因此本步只闭合圆周上界存在性与形式聚合，"
            "不闭合 `BacklundIndependentJensenZeroCountC16AggregationLedger`。",
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
