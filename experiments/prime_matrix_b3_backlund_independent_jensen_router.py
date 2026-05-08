#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 独立 Jensen 圆盘零点计数路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_independent_jensen_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-independent-jensen-router.json
  docs/monograph/prime-matrix-b3-backlund-independent-jensen-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-zero-distance-sum-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-independent-jensen-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-independent-jensen-router.md"

OLD_ATOM = "BacklundIndependentJensenDiskZeroCountLedger"
JENSEN_FORMULA_CLOSED = "BacklundJensenDiskFormulaClosed"
BOUNDARY_ATOM = "BacklundIndependentXiDiskBoundaryMajorantLedger"
ANCHOR_ATOM = "BacklundIndependentJensenCenterLowerAnchorLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DIST_CONST_ATOM = "BacklundZeroDistanceSumConstantAggregationLedger"
WINDOW_ATOM = "BacklundVariationWindowScaleLedger"
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
    """写出独立 Jensen 计数替换包。"""
    return f"({JENSEN_FORMULA_CLOSED} AND {BOUNDARY_ATOM} AND {ANCHOR_ATOM} AND {COUNT_CONST_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧独立 Jensen 原子。"""
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
    """生成独立 Jensen 圆盘零点计数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    xi_ready = "XiEntireOrderOneGrowthClosed" in basis
    no_circular_ready = "BacklundSpikeNoRVMCircularityDisciplineClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and xi_ready and no_circular_ready and guard
    return [
        row(
            "IndependentJensenGateActive",
            active,
            False,
            "上一层唯一内部最窄点是独立 Jensen 圆盘零点计数。",
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
            "XiEntireAndNoCircularAvailable",
            xi_ready and no_circular_ready,
            True,
            "xi 整函数增长与非循环纪律已可用。",
            "无形式输入剩余。",
        ),
        row(
            "JensenDiskFormulaClosed",
            reduced,
            True,
            "Jensen 公式把圆盘内零点数控制为圆周 log|xi| 上界减圆心 log|xi| 下界。",
            JENSEN_FORMULA_CLOSED,
        ),
        row(
            "IndependentBoundaryMajorantMissing",
            False,
            False,
            "仍需独立圆周上界，不能从待证 Backlund/RVM 取零点计数。",
            BOUNDARY_ATOM,
        ),
        row(
            "IndependentCenterLowerAnchorMissing",
            False,
            False,
            "仍需圆心处 xi 不过小的显式下界，避免 Jensen 只给上界不计数。",
            ANCHOR_ATOM,
        ),
        row(
            "JensenC16AggregationMissing",
            False,
            False,
            "仍需把圆周上界和圆心下界合并成局部零点计数常数 C_N=16。",
            COUNT_CONST_ATOM,
        ),
        row(
            "IndependentJensenReduced",
            reduced,
            False,
            "旧独立 Jensen 原子已压成 Jensen 公式、圆周上界、圆心下界、C16 聚合四包。",
            replacement_pair(),
        ),
        row(
            "ZeroDistanceDownstreamStillOpen",
            False,
            False,
            "Jensen 计数完成后仍需近零分离、倒距离常数聚合和窗口尺度。",
            f"{NEAR_ZERO_ATOM} AND {DIST_CONST_ATOM} AND {WINDOW_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行独立 Jensen 圆盘零点计数路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "IndependentJensenReduced")
    return {
        "certificate_type": "b3_backlund_independent_jensen_router",
        "status": "backlund_independent_jensen_disk_zero_count_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_independent_jensen_reduced": reduced,
        "backlund_independent_jensen_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": BOUNDARY_ATOM,
        "secondary_priority": ANCHOR_ATOM,
        "tertiary_priority": COUNT_CONST_ATOM,
        "post_jensen_priority": NEAR_ZERO_ATOM,
        "post_near_zero_priority": DIST_CONST_ATOM,
        "post_distance_priority": WINDOW_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "core_formula": "N(r) log(R/r) <= (1/2pi) int_0^{2pi} log|xi(z0+R e^{i theta})| dtheta - log|xi(z0)|",
        "plain_conclusion": (
            "独立 Jensen 圆盘零点计数尚未闭合。"
            "本步闭合 Jensen 公式形式层，剩余是独立圆周上界、圆心下界和 C16 常数聚合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 独立 Jensen 圆盘零点计数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_independent_jensen_reduced={fmt_bool(result['backlund_independent_jensen_reduced'])}",
        (
            "backlund_independent_jensen_self_contained_proved="
            f"{fmt_bool(result['backlund_independent_jensen_self_contained_proved'])}"
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
        "## 2. Jensen 公式",
        "",
        "```text",
        result["core_formula"],
        "```",
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
