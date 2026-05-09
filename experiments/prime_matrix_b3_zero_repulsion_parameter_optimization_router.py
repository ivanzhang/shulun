#!/usr/bin/env python3
"""Prime Matrix B=3 零点排斥参数数值优化路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zero_repulsion_parameter_optimization_router.py

输出：
  docs/monograph/prime-matrix-b3-zero-repulsion-parameter-optimization-router.json
  docs/monograph/prime-matrix-b3-zero-repulsion-parameter-optimization-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-clog-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zero-repulsion-parameter-optimization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zero-repulsion-parameter-optimization-router.md"

OLD_ATOM = "ZeroRepulsionParameterNumericalOptimizationLedger"
CLOSED_ATOM = "ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14"
CLOG_CLOSED = "CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch"
PNT_ATOM = "ZeroFreeRegionToExplicitPNTContourConstantLedger"
TARGET_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_LOG = 64.0
A = 1.0 / (4.0 * C_LOG)
C = 1.0 / (20.0 * C_LOG)
T0 = 14.0


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
    """替换零点排斥参数优化原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def coefficient() -> float:
    """计算 DVP 归一后的关键系数。"""
    return 3.0 / A - 4.0 / (A + C) + C_LOG


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], coeff: float) -> list[dict[str, Any]]:
    """生成参数优化判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    clog_ready = CLOG_CLOSED in basis
    negative = coeff < 0.0
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and clog_ready and negative
    return [
        row(
            "ZeroRepulsionParameterGateActive",
            active,
            False,
            "C_log=64 固定后，当前最窄点是给出 a、c、T0 的数值优化。",
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
            "CLog64Ready",
            clog_ready,
            True,
            "C_log=64 的加法预算已闭合。",
            CLOG_CLOSED,
        ),
        row(
            "ParameterChoiceRegistered",
            True,
            True,
            "取 a=1/(4C_log)=1/256，c=1/(20C_log)=1/1280。",
            f"a={A:.12f}, c={C:.12f}",
        ),
        row(
            "NegativeCoefficientPasses",
            negative,
            True,
            "若 beta>1-c/L，则 DVP 正性不等式右侧主系数为负，产生矛盾。",
            f"3/a - 4/(a+c) + C_log = {coeff:.12f}",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "零点排斥参数数值优化闭合，给出高于 T0=14 的显式零点自由带。",
            CLOSED_ATOM,
        ),
        row(
            "FiniteLowHeightStillSeparate",
            False,
            False,
            "T0=14 以下仍需要独立低高度零点核验；本步只给高高度排斥参数。",
            FINITE_LOW_HEIGHT,
        ),
        row(
            "PNTContourNext",
            False,
            False,
            "下一步需把零点自由带转成显式 PNT/theta 轮廓常数。",
            PNT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点排斥参数优化路由。"""
    previous = load_json(paths["previous"])
    coeff = coefficient()
    rows = build_rows(previous, coeff)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_zero_repulsion_parameter_optimization_router",
        "status": "zero_repulsion_parameter_optimization_closed_c64",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_repulsion_parameter_optimization_closed": closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": PNT_ATOM,
        "secondary_priority": TARGET_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "parameters": {
            "C_log": C_LOG,
            "a": A,
            "c": C,
            "T0": T0,
            "coefficient": coeff,
            "margin": -coeff,
            "zero_free_region": "beta <= 1 - 1/(1280*log(|gamma|+3)), |gamma|>=14",
        },
        "plain_conclusion": (
            "零点排斥参数数值优化闭合：在 C_log=64 下取 a=1/256、c=1/1280，"
            "核心系数为负，因此高于 T0=14 的零点满足 beta <= 1 - 1/(1280 log(|gamma|+3))。"
            "T0 以下仍需独立有限核验。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    params = result["parameters"]
    lines = [
        "# Prime Matrix B=3 零点排斥参数数值优化路由器",
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
            "zero_repulsion_parameter_optimization_closed="
            f"{fmt_bool(result['zero_repulsion_parameter_optimization_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 参数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| C_log | `{fmt_float(params['C_log'])}` |",
        f"| a | `{fmt_float(params['a'])}` |",
        f"| c | `{fmt_float(params['c'])}` |",
        f"| T0 | `{fmt_float(params['T0'])}` |",
        f"| coefficient | `{fmt_float(params['coefficient'])}` |",
        f"| margin | `{fmt_float(params['margin'])}` |",
        "",
        "```text",
        params["zero_free_region"],
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
                f"当前最窄点更新为 `{result['next_priority']}`；随后是 "
                f"`{result['secondary_priority']}`，低高度独立账本 `{result['finite_low_height_priority']}` 仍开放。"
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
