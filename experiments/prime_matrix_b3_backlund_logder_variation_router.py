#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 独立 log-derivative 局部变差路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_logder_variation_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-logder-variation-router.json
  docs/monograph/prime-matrix-b3-backlund-logder-variation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-spike-exclusion-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-logder-variation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-logder-variation-router.md"

OLD_ATOM = "BacklundIndependentLogDerivativeLocalVariationLedger"
HADAMARD_CLOSED = "BacklundHadamardLogDerivativeVariationFormulaClosed"
ZERO_SUM_ATOM = "BacklundIndependentLocalZeroDistanceSumLedger"
WINDOW_ATOM = "BacklundVariationWindowScaleLedger"
INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
SLACK_ATOM = "BacklundCS8SlackAfterBridgeLedger"
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
    """写出独立 log-derivative 变差替换包。"""
    return f"({HADAMARD_CLOSED} AND {ZERO_SUM_ATOM} AND {WINDOW_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 log-derivative 变差原子。"""
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
    """生成独立 log-derivative 局部变差判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    hadamard_ready = "HadamardFactorizationLogDerivativeClosed" in basis
    gamma_ready = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    no_circular_ready = "BacklundSpikeNoRVMCircularityDisciplineClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and hadamard_ready and gamma_ready and no_circular_ready and guard
    return [
        row(
            "IndependentLogDerivativeVariationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是独立 log-derivative 局部变差界。",
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
            "HadamardAndGammaInputsAvailable",
            hadamard_ready and gamma_ready,
            True,
            "Hadamard log-derivative 公式和 Gamma/digamma 粗界已可用。",
            "无形式解析输入剩余。",
        ),
        row(
            "NoRVMCircularityAvailable",
            no_circular_ready,
            True,
            "已禁止用待证 RVM 局部零点计数来证明本层。",
            "无循环纪律剩余。",
        ),
        row(
            "HadamardVariationFormulaClosed",
            reduced,
            True,
            "沿短高度区间的 arg 变差由 Gamma 项和 sum_rho int |s-rho|^{-1} 控制。",
            HADAMARD_CLOSED,
        ),
        row(
            "IndependentLocalZeroDistanceSumMissing",
            False,
            False,
            "仍需独立证明局部零点倒距离和为 O(log(T+3))，且不能调用 Backlund/RVM。",
            ZERO_SUM_ATOM,
        ),
        row(
            "VariationWindowScaleMissing",
            False,
            False,
            "仍需选择短窗口尺度，使 log-derivative 变差最多吃掉点态 arg 的一半。",
            WINDOW_ATOM,
        ),
        row(
            "IndependentLogDerivativeVariationReduced",
            reduced,
            False,
            "旧独立变差原子已压成 Hadamard 变差公式、独立零点倒距离和、窗口尺度三包。",
            replacement_pair(),
        ),
        row(
            "IndentAndSlackStillDownstream",
            False,
            False,
            "随后还需零点邻近凹口成本和 C_S=8 余量验收。",
            f"{INDENT_ATOM} AND {SLACK_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行独立 log-derivative 局部变差路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "IndependentLogDerivativeVariationReduced")
    return {
        "certificate_type": "b3_backlund_logder_variation_router",
        "status": "backlund_independent_logder_variation_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_independent_logder_variation_reduced": reduced,
        "backlund_independent_logder_variation_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": ZERO_SUM_ATOM,
        "secondary_priority": WINDOW_ATOM,
        "tertiary_priority": INDENT_ATOM,
        "quaternary_priority": SLACK_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "plain_conclusion": (
            "独立 log-derivative 局部变差账本尚未闭合。"
            "形式 Hadamard 变差公式已闭合；真正剩余是独立零点倒距离和，"
            "这不能借用由 Backlund 推出的 RVM 局部零点计数。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 独立 log-derivative 局部变差路由器",
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
            "backlund_independent_logder_variation_reduced="
            f"{fmt_bool(result['backlund_independent_logder_variation_reduced'])}"
        ),
        (
            "backlund_independent_logder_variation_self_contained_proved="
            f"{fmt_bool(result['backlund_independent_logder_variation_self_contained_proved'])}"
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
