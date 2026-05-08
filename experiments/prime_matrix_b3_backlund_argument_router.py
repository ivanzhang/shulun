#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund/arg zeta 显式上界路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_argument_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-argument-router.json
  docs/monograph/prime-matrix-b3-backlund-argument-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-gamma-main-local-diff-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-argument-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-argument-router.md"

OLD_ATOM = "BacklundZetaArgumentBoundNumericalLedger"
RECT_ATOM = "BacklundLittlewoodRectangleArgumentLedger"
RIGHT_ATOM = "ZetaRightEdgeEulerProductArgumentNumericalLedger"
HORIZONTAL_ATOM = "CriticalStripHorizontalVariationNumericalLedger"
LEFT_ATOM = "FunctionalEquationLeftEdgeArgumentLedger"
CONST_ATOM = "BacklundArgumentConstantAggregationLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

CS_CANDIDATE = 8.0


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
    """写出 Backlund/arg zeta 的替换包。"""
    return f"({RECT_ATOM} AND {RIGHT_ATOM} AND {HORIZONTAL_ATOM} AND {LEFT_ATOM} AND {CONST_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 Backlund 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def candidate_budget() -> list[dict[str, float]]:
    """给候选 C_S=8 生成预算表。"""
    rows: list[dict[str, float]] = []
    for t in [2.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        logv = math.log(t + 3.0)
        rows.append(
            {
                "t": t,
                "log_t_plus_3": logv,
                "CS_log_bound": CS_CANDIDATE * logv,
                "two_endpoint_argument_budget": 2.0 * CS_CANDIDATE * logv,
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
    """生成 Backlund/arg zeta 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    gamma_main_closed = "GammaMainTermLocalDifferenceNumericalClosedCmain4" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and gamma_main_closed and guard
    return [
        row(
            "BacklundArgumentGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Backlund/arg zeta 显式上界。",
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
            "GammaMainAvailable",
            gamma_main_closed,
            True,
            "Gamma 主项局部差分已由 C_main=4 闭合。",
            "无 Gamma 主项剩余。",
        ),
        row(
            "BacklundLittlewoodRectangleMissing",
            False,
            False,
            "还需把 arg zeta 变化转成 Littlewood 矩形内 log|zeta| 边界积分。",
            RECT_ATOM,
        ),
        row(
            "RightEdgeEulerProductArgumentMissing",
            False,
            False,
            "还需在 sigma=1+eta 右边界用 Euler product 控制 arg/log|zeta|。",
            RIGHT_ATOM,
        ),
        row(
            "HorizontalVariationMissing",
            False,
            False,
            "还需控制矩形上下水平边的 log|zeta| 变化和零点附近绕行成本。",
            HORIZONTAL_ATOM,
        ),
        row(
            "LeftEdgeFunctionalEquationMissing",
            False,
            False,
            "还需用函数方程把左边界归还给右边界与 Gamma 主项。",
            LEFT_ATOM,
        ),
        row(
            "BacklundConstantAggregationMissing",
            False,
            False,
            "还需把各边贡献聚合为 |S(T)|<=C_S log(T+3)，候选 C_S=8。",
            CONST_ATOM,
        ),
        row(
            "BacklundArgumentReducedToFiveMicroLedgers",
            reduced,
            False,
            "旧 Backlund 原子已压成 Littlewood 矩形、右边 Euler、水平边、左边函数方程、常数聚合五包。",
            replacement_pair(),
        ),
        row(
            "EndpointAndCN16StillDownstream",
            False,
            False,
            "Backlund 完成后还需端点 convention 与 CN16 合并。",
            f"{ENDPOINT_ATOM} AND {RVM_CN_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Backlund/arg zeta 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "BacklundArgumentReducedToFiveMicroLedgers")
    return {
        "certificate_type": "b3_backlund_argument_router",
        "status": "backlund_argument_reduced_to_five_micro_ledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_argument_reduced": reduced,
        "backlund_argument_self_contained_proved": False,
        "C_S_candidate": CS_CANDIDATE,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": RECT_ATOM,
        "secondary_priority": RIGHT_ATOM,
        "tertiary_priority": HORIZONTAL_ATOM,
        "quaternary_priority": LEFT_ATOM,
        "quinary_priority": CONST_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_budget": candidate_budget(),
        "plain_conclusion": (
            "Backlund/arg zeta 显式上界尚未自足闭合。它已压成五个微账本；"
            "候选 C_S=8 只是预算目标，必须由 Littlewood 矩形和边界积分逐项支撑。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund/arg zeta 显式上界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_argument_reduced={fmt_bool(result['backlund_argument_reduced'])}",
        f"backlund_argument_self_contained_proved={fmt_bool(result['backlund_argument_self_contained_proved'])}",
        f"C_S_candidate={fmt_float(result['C_S_candidate'])}",
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
        "## 2. 候选预算",
        "",
        "| T | log(T+3) | C_S log bound | two-endpoint budget |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in result["candidate_budget"]:
        lines.append(
            "| {t:.6g} | `{logv}` | `{bound}` | `{two}` |".format(
                t=item["t"],
                logv=fmt_float(item["log_t_plus_3"]),
                bound=fmt_float(item["CS_log_bound"]),
                two=fmt_float(item["two_endpoint_argument_budget"]),
            )
        )
    lines.extend(
        [
            "",
            "候选 `C_S=8` 只用于预算排布；未完成前不能作为定理输入。",
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
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
                f"`{result['quaternary_priority']}`、`{result['quinary_priority']}`。"
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
