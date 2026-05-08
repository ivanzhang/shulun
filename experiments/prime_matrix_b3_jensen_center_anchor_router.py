#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 独立 Jensen 圆心下界 anchor 路由器。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_center_anchor_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-center-anchor-router.json
  docs/monograph/prime-matrix-b3-jensen-center-anchor-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-xi-boundary-constant-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-center-anchor-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-center-anchor-router.md"

OLD_ATOM = "BacklundIndependentJensenCenterLowerAnchorLedger"
CENTER_ATOM = "BacklundJensenRightEdgeCenterChoiceConventionLedger"
GAMMA_CANCEL_ATOM = "BacklundJensenGammaMainCancellationInMeanLedger"
EULER_LOWER_ATOM = "BacklundJensenRightEdgeEulerProductLowerBoundLedger"
LOW_CENTER_ATOM = "BacklundJensenLowHeightCenterAnchorFiniteLedger"
ANCHOR_CONST_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_XI_BOUNDARY_SYMBOL = "C_xi_boundary"


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
    """写出圆心 anchor 的替换包。"""
    return (
        f"({CENTER_ATOM} AND {GAMMA_CANCEL_ATOM} AND {EULER_LOWER_ATOM} "
        f"AND {LOW_CENTER_ATOM} AND {ANCHOR_CONST_ATOM})"
    )


def replace_atom(text: str) -> str:
    """替换旧圆心 anchor 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def obstruction_rows() -> list[dict[str, float]]:
    """量化只用正上界会产生的线性 Gamma 假成本。"""
    rows: list[dict[str, float]] = []
    for t in [10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        gamma_decay = math.pi * t / 4.0
        rows.append(
            {
                "T": t,
                "log_T_plus_3": logv,
                "gamma_center_decay_size": gamma_decay,
                "decay_over_log": gamma_decay / logv,
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
    """生成独立 Jensen 圆心下界 anchor 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    boundary_ready = "BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic" in basis
    jensen_ready = "BacklundJensenDiskFormulaClosed" in basis
    gamma_ready = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    euler_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and boundary_ready and jensen_ready and gamma_ready and euler_ready and guard
    return [
        row(
            "JensenCenterAnchorGateActive",
            active,
            False,
            "上一层唯一内部最窄点是独立 Jensen 圆心下界 anchor。",
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
            "BoundaryJensenGammaEulerInputsAvailable",
            boundary_ready and jensen_ready and gamma_ready and euler_ready,
            True,
            "Jensen 公式、独立圆周上界、Gamma/digamma 和右边 Euler 输入均已可用。",
            "无形式输入剩余。",
        ),
        row(
            "PositiveMajorantAloneInsufficient",
            reduced,
            True,
            "若只用 log^+ 圆周上界再减圆心下界，xi 的 Gamma 主衰减会制造约 pi*T/4 的线性假成本。",
            GAMMA_CANCEL_ATOM,
        ),
        row(
            "CenterChoiceConventionMissing",
            False,
            False,
            "必须固定 Jensen 圆心与半径，使圆盘覆盖目标窗口且圆心落在可控非零锚线上。",
            CENTER_ATOM,
        ),
        row(
            "GammaMeanCancellationMissing",
            False,
            False,
            "必须在 Jensen 平均中保留 Gamma/初等因子的有符号调和相消，不能只取 log^+ 上界。",
            GAMMA_CANCEL_ATOM,
        ),
        row(
            "RightEdgeEulerLowerBoundMissing",
            False,
            False,
            "若圆心选在 sigma>1，需要 Euler product 给出 zeta 圆心下界。",
            EULER_LOWER_ATOM,
        ),
        row(
            "LowHeightCenterAnchorStillFinite",
            False,
            False,
            "低高度圆心还需有限非零 anchor 或 compact lower-bound 账本。",
            LOW_CENTER_ATOM,
        ),
        row(
            "CenterAnchorConstantAggregationMissing",
            False,
            False,
            "最后要把圆心选择、Gamma 相消、Euler 下界和低高度 anchor 聚成 O(log(T+3)) 下界。",
            ANCHOR_CONST_ATOM,
        ),
        row(
            "IndependentJensenCenterAnchorReduced",
            reduced,
            False,
            "旧圆心 anchor 原子已压成圆心选择、Gamma 均值相消、右边 Euler 下界、低高度 anchor、常数聚合五包。",
            replacement_pair(),
        ),
        row(
            "JensenC16StillDownstream",
            False,
            False,
            "anchor 完成后仍需把圆周上界和圆心下界压入局部零点计数 C_N=16。",
            f"{COUNT_CONST_ATOM} AND {NEAR_ZERO_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行独立 Jensen 圆心下界 anchor 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "IndependentJensenCenterAnchorReduced")
    return {
        "certificate_type": "b3_jensen_center_anchor_router",
        "status": "backlund_independent_jensen_center_anchor_reduced_gamma_cancellation_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_independent_jensen_center_anchor_reduced": reduced,
        "backlund_independent_jensen_center_anchor_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": CENTER_ATOM,
        "secondary_priority": GAMMA_CANCEL_ATOM,
        "tertiary_priority": EULER_LOWER_ATOM,
        "quaternary_priority": LOW_CENTER_ATOM,
        "post_anchor_priority": ANCHOR_CONST_ATOM,
        "post_anchor_aggregation_priority": COUNT_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "obstruction_rows": obstruction_rows(),
        "plain_conclusion": (
            "独立 Jensen 圆心下界 anchor 尚未闭合。"
            "本步确认关键障碍：不能用正的 xi 圆周上界直接扣圆心下界，"
            "必须先建立圆心选择和 Gamma 主项在 Jensen 平均中的有符号相消。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 独立 Jensen 圆心下界 anchor 路由器",
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
            "backlund_independent_jensen_center_anchor_reduced="
            f"{fmt_bool(result['backlund_independent_jensen_center_anchor_reduced'])}"
        ),
        (
            "backlund_independent_jensen_center_anchor_self_contained_proved="
            f"{fmt_bool(result['backlund_independent_jensen_center_anchor_self_contained_proved'])}"
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
        "## 2. 当前障碍",
        "",
        (
            "xi 含有 Gamma 因子。若圆心在固定高度 `T`，`log|Gamma|` 的主衰减约为 "
            "`-pi*T/4`。Jensen 中正确做法是让圆周平均与圆心的 Gamma 主项有符号相消；"
            "只用 `log^+|xi|` 圆周上界会把这项变成线性假成本。"
        ),
        "",
        "| T | log(T+3) | pi*T/4 | (pi*T/4)/log(T+3) |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in result["obstruction_rows"]:
        lines.append(
            "| {T:.6g} | `{logv}` | `{decay}` | `{ratio}` |".format(
                T=item["T"],
                logv=fmt_float(item["log_T_plus_3"]),
                decay=fmt_float(item["gamma_center_decay_size"]),
                ratio=fmt_float(item["decay_over_log"]),
            )
        )
    lines.extend(
        [
            "",
            f"因此下一步不能直接用 `{C_XI_BOUNDARY_SYMBOL}`；必须先闭合圆心选择与 Gamma 均值相消。",
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
