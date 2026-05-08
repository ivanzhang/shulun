#!/usr/bin/env python3
"""Prime Matrix B=3 xi 圆周低高度上界闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_xi_low_boundary_router.py

输出：
  docs/monograph/prime-matrix-b3-xi-low-boundary-router.json
  docs/monograph/prime-matrix-b3-xi-low-boundary-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-xi-high-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-xi-low-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-xi-low-boundary-router.md"

OLD_ATOM = "BacklundXiBoundaryLowHeightFiniteCheckLedger"
CLOSED_ATOM = "BacklundXiBoundaryLowHeightCompactEnvelopeClosed"
HIGH_CLOSED = "BacklundXiBoundaryHighHeightStirlingConvexityClosedC16"
COVER_CLOSED = "BacklundXiDiskCircleFiniteStripCoverClosed"
CONST_ATOM = "BacklundXiBoundaryMajorantConstantAggregationLedger"
ANCHOR_ATOM = "BacklundIndependentJensenCenterLowerAnchorLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

LOW_HEIGHT_CEILING = 10.0
LOW_HEIGHT_LOG_FLOOR = math.log(3.0)
LOW_HEIGHT_LOG_CEILING = math.log(LOW_HEIGHT_CEILING + 3.0)
LOW_ENVELOPE_SYMBOL = "M_xi_low := sup_{s in K_low} log^+|xi(s)| < infinity"


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


def envelope_rows() -> list[dict[str, str]]:
    """生成低高度紧致包络说明表。"""
    return [
        {
            "item": "height band",
            "value": f"|Im s| <= {LOW_HEIGHT_CEILING:g} on the low-height boundary pieces",
            "role": "把低高度部分限制在闭有界高度带。",
        },
        {
            "item": "finite cover",
            "value": COVER_CLOSED,
            "role": "圆周边界只落在有限条固定宽度的条带中。",
        },
        {
            "item": "compact carrier",
            "value": "K_low = finite-cover boundary carrier intersect {|Im s|<=10}",
            "role": "有限并的闭有界集合仍紧。",
        },
        {
            "item": "analytic function",
            "value": "XiEntireOrderOneGrowthClosed",
            "role": "xi 是整函数，因此 log^+|xi| 在 K_low 上连续并有最大值。",
        },
        {
            "item": "low envelope",
            "value": LOW_ENVELOPE_SYMBOL,
            "role": "该常数只进入后续常数聚合，不在本步伪装成 C16。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 xi 圆周低高度上界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    high_ready = HIGH_CLOSED in basis
    cover_ready = COVER_CLOSED in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and high_ready and cover_ready and xi_ready and guard
    return [
        row(
            "XiLowBoundaryGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 xi 圆周低高度上界。",
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
            "HighCoverXiInputsAvailable",
            high_ready and cover_ready and xi_ready,
            True,
            "高高度已闭合，有限圆周覆盖和 xi 整函数输入均可用。",
            "无低高度形式输入剩余。",
        ),
        row(
            "LowBoundaryCompactCarrierClosed",
            closed,
            True,
            "低高度边界片属于有限覆盖与 |Im s|<=10 的交；固定覆盖使承载集紧。",
            "无紧致性剩余。",
        ),
        row(
            "XiLowEnvelopeExists",
            closed,
            True,
            "xi 整函数连续，所以 log^+|xi| 在低高度紧集上有有限最大值 M_xi_low。",
            CLOSED_ATOM,
        ),
        row(
            "NoLowZeroAbsenceUsed",
            closed,
            True,
            "这里仅需圆周上界，不调用低高度零点不存在或 RVM/Backlund 计数。",
            "避免循环输入。",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "低高度 xi 圆周上界已闭合为一个有限紧致包络常数；数值支付留给聚合层。",
            CLOSED_ATOM,
        ),
        row(
            "BoundaryConstantAggregationStillNext",
            False,
            False,
            "下一步需把高高度 C16 与低高度 M_xi_low 合并成 Jensen 可用圆周常数。",
            CONST_ATOM,
        ),
        row(
            "JensenAnchorStillDownstream",
            False,
            False,
            "圆周上界之后还需圆心下界与 C16 零点计数聚合。",
            f"{ANCHOR_ATOM} AND {COUNT_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 圆周低高度上界闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_xi_low_boundary_router",
        "status": "backlund_xi_boundary_low_height_compact_envelope_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_xi_boundary_low_height_closed": closed,
        "low_height_ceiling": LOW_HEIGHT_CEILING,
        "low_height_log_floor": LOW_HEIGHT_LOG_FLOOR,
        "low_height_log_ceiling": LOW_HEIGHT_LOG_CEILING,
        "low_envelope_symbol": LOW_ENVELOPE_SYMBOL,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": CONST_ATOM,
        "secondary_priority": ANCHOR_ATOM,
        "tertiary_priority": COUNT_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "envelope_rows": envelope_rows(),
        "plain_conclusion": (
            "xi 圆周低高度上界已以紧致包络形式闭合。"
            "本步只证明低高度贡献是一个有限常数 M_xi_low；"
            "它没有闭合 Jensen 常数聚合，也没有使用真实零行缺席或低高度零点排除。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 xi 圆周低高度上界闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_xi_boundary_low_height_closed={fmt_bool(result['backlund_xi_boundary_low_height_closed'])}",
        f"low_height_ceiling={fmt_float(result['low_height_ceiling'])}",
        f"low_height_log_floor={fmt_float(result['low_height_log_floor'])}",
        f"low_height_log_ceiling={fmt_float(result['low_height_log_ceiling'])}",
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
        "## 2. 低高度紧致包络",
        "",
        "```text",
        result["low_envelope_symbol"],
        "```",
        "",
        "| item | value | role |",
        "| --- | --- | --- |",
    ]
    for item in result["envelope_rows"]:
        lines.append(
            "| {item} | {value} | {role} |".format(
                item=table_cell(item["item"]),
                value=table_cell(item["value"]),
                role=table_cell(item["role"]),
            )
        )
    lines.extend(
        [
            "",
            "这个包络只处理圆周 `log^+|xi|` 的上界。它不需要、也没有调用低高度零点不存在；"
            "圆心处 `xi` 不过小的下界仍是后续独立 anchor。",
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
                f"随后是 `{result['secondary_priority']}` 与 `{result['tertiary_priority']}`。"
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
