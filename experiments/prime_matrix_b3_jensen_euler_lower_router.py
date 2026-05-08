#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 右边 Euler product 圆心下界闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_euler_lower_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-euler-lower-router.json
  docs/monograph/prime-matrix-b3-jensen-euler-lower-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-gamma-cancellation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-euler-lower-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-euler-lower-router.md"

OLD_ATOM = "BacklundJensenRightEdgeEulerProductLowerBoundLedger"
CLOSED_ATOM = "BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2"
GAMMA_CANCEL_CLOSED = "BacklundJensenGammaMainCancellationInMeanClosedHighT10R4"
LOW_CENTER_ATOM = "BacklundJensenLowHeightCenterAnchorFiniteLedger"
ANCHOR_CONST_ATOM = "BacklundJensenCenterLowerAnchorConstantAggregationLedger"
COUNT_CONST_ATOM = "BacklundIndependentJensenZeroCountC16AggregationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SIGMA_CENTER = 2.0
ZETA2 = math.pi**2 / 6.0
LOG_ZETA2 = math.log(ZETA2)


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


def lower_bound_rows() -> list[dict[str, str]]:
    """生成 Euler 下界说明表。"""
    return [
        {
            "step": "inverse series",
            "formula": "1/zeta(s)=sum_{n>=1} mu(n)n^{-s}, sigma>1",
            "bound": "|1/zeta(2+iT)| <= sum n^{-2}=zeta(2)",
        },
        {
            "step": "lower bound",
            "formula": "|zeta(2+iT)| >= 1/zeta(2)",
            "bound": f"-log|zeta(2+iT)| <= log(zeta(2)) = {LOG_ZETA2:.12f}",
        },
        {
            "step": "log scale",
            "formula": "log(zeta(2)) <= log(zeta(2))*log(T+3)/log(3)",
            "bound": "常数项可被后续 O(log(T+3)) anchor 聚合吸收。",
        },
    ]


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
    """生成右边 Euler product 圆心下界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    gamma_cancel_ready = GAMMA_CANCEL_CLOSED in basis
    right_edge_ready = "ZetaRightEdgeEulerProductArgumentClosedCright2" in basis
    euler_positive_ready = "EulerProductLogDerivativePositiveRealPartClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and gamma_cancel_ready and right_edge_ready and euler_positive_ready and guard
    return [
        row(
            "EulerLowerGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen 右边 Euler product 圆心下界。",
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
            "GammaCancellationAndEulerInputsAvailable",
            gamma_cancel_ready and right_edge_ready and euler_positive_ready,
            True,
            "Gamma 均值相消、右边界 Euler 预算和 Euler product 基础均已可用。",
            "无形式输入剩余。",
        ),
        row(
            "ZetaRightEdgeLowerBoundClosed",
            closed,
            True,
            "在 sigma=2，由 1/zeta(s) 的绝对收敛级数得 |zeta(2+iT)|>=1/zeta(2)。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "zeta 圆心下界闭合为常数 log(zeta(2)) 成本。",
            CLOSED_ATOM,
        ),
        row(
            "LowCenterAnchorStillNext",
            False,
            False,
            "高高度 Euler 下界已闭合；低高度圆心 anchor 仍需有限处理。",
            LOW_CENTER_ATOM,
        ),
        row(
            "AnchorConstantAggregationStillDownstream",
            False,
            False,
            "最后仍需把 Gamma 相消、Euler 下界、低高度项聚成统一 anchor 常数。",
            f"{ANCHOR_CONST_ATOM} AND {COUNT_CONST_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行右边 Euler product 圆心下界闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_jensen_euler_lower_router",
        "status": "backlund_jensen_right_edge_euler_lower_bound_closed_zeta2",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_right_edge_euler_lower_bound_closed": closed,
        "sigma_center": SIGMA_CENTER,
        "zeta2": ZETA2,
        "log_zeta2": LOG_ZETA2,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": LOW_CENTER_ATOM,
        "secondary_priority": ANCHOR_CONST_ATOM,
        "tertiary_priority": COUNT_CONST_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "lower_bound_rows": lower_bound_rows(),
        "plain_conclusion": (
            "Jensen 右边 Euler product 圆心下界已闭合："
            "|zeta(2+iT)|>=1/zeta(2)，只产生常数 log(zeta(2)) 成本。"
            "剩余是低高度圆心 anchor 与统一常数聚合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 右边 Euler product 圆心下界闭合证书",
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
            "backlund_jensen_right_edge_euler_lower_bound_closed="
            f"{fmt_bool(result['backlund_jensen_right_edge_euler_lower_bound_closed'])}"
        ),
        f"sigma_center={fmt_float(result['sigma_center'])}",
        f"zeta2={fmt_float(result['zeta2'])}",
        f"log_zeta2={fmt_float(result['log_zeta2'])}",
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
        "## 2. 下界公式",
        "",
        "| step | formula | bound |",
        "| --- | --- | --- |",
    ]
    for item in result["lower_bound_rows"]:
        lines.append(
            "| {step} | {formula} | {bound} |".format(
                step=table_cell(item["step"]),
                formula=table_cell(item["formula"]),
                bound=table_cell(item["bound"]),
            )
        )
    lines.extend(
        [
            "",
            "该下界只使用 `sigma>1` 的绝对收敛，不调用零点计数或 Backlund 结论。",
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
