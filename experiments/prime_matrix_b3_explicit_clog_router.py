#!/usr/bin/env python3
"""Prime Matrix B=3 显式 C_log 常数账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_explicit_clog_router.py

输出：
  docs/monograph/prime-matrix-b3-explicit-clog-router.json
  docs/monograph/prime-matrix-b3-explicit-clog-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-explicit-zero-free-constants-router.json"
DEFAULT_GAMMA = DOCS / "prime-matrix-b3-gamma-digamma-clog-router.json"
DEFAULT_ZERO_COUNT = DOCS / "prime-matrix-b3-jensen-zero-count-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-explicit-clog-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-explicit-clog-router.md"

OLD_ATOM = "ExplicitCLogHadamardStirlingJensenNumericalLedger"
GAMMA_ATOM = "GammaDigammaStirlingUniformNumericalLedger"
GAMMA_CLOSED = "GammaDigammaStirlingUniformNumericalClosedCgamma24"
ZERO_COUNT_ATOM = "JensenZeroCountingLocalNumericalLedger"
ZERO_COUNT_EXTERNAL_CLOSED = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
BACKLUND_INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
LOW_HEIGHT_CRITICAL_LINE = "CriticalLineNoZeroOn0To14FiniteLedger"
LOW_HEIGHT_OFF_LINE = "CriticalStripNoOffLineZeroBelow14TuringLedger"
PARTIAL_FRACTION_ATOM = "HadamardPartialFractionRemainderNumericalLedger"
AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
OPT_ATOM = "ZeroRepulsionParameterNumericalOptimizationLedger"
PNT_ATOM = "ZeroFreeRegionToExplicitPNTContourConstantLedger"
TARGET_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

CLOG_CANDIDATE = 64.0
ANCHOR_X = 20_000
DUSART_THETA_DENOMINATOR = 36_260


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
    """写出 C_log 的数值子账本替换包。"""
    return f"({GAMMA_ATOM} AND {ZERO_COUNT_ATOM} AND {PARTIAL_FRACTION_ATOM} AND {AGGREGATION_ATOM})"


def current_replacement_pair(gamma_closed: bool) -> str:
    """写出吸收当前已证 Gamma 账本后的替换包。"""
    gamma = GAMMA_CLOSED if gamma_closed else GAMMA_ATOM
    return f"({gamma} AND {ZERO_COUNT_ATOM} AND {PARTIAL_FRACTION_ATOM} AND {AGGREGATION_ATOM})"


def current_external_replacement_pair(gamma_closed: bool, zero_count_external_closed: bool) -> str:
    """写出外部 Backlund/低高度分支吸收后的替换包。"""
    gamma = GAMMA_CLOSED if gamma_closed else GAMMA_ATOM
    zero_count = ZERO_COUNT_EXTERNAL_CLOSED if zero_count_external_closed else ZERO_COUNT_ATOM
    return f"({gamma} AND {zero_count} AND {PARTIAL_FRACTION_ATOM} AND {AGGREGATION_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧 C_log 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def replace_atom_with_current(text: str, gamma_closed: bool) -> str:
    """用当前已证状态替换旧 C_log 原子。"""
    return text.replace(OLD_ATOM, current_replacement_pair(gamma_closed))


def replace_atom_with_external(text: str, gamma_closed: bool, zero_count_external_closed: bool) -> str:
    """用外部条件分支当前状态替换旧 C_log 原子。"""
    return text.replace(OLD_ATOM, current_external_replacement_pair(gamma_closed, zero_count_external_closed))


def candidate_budget() -> dict[str, float]:
    """计算保守候选 C_log 对下游参数的影响。"""
    c = 1.0 / (20.0 * CLOG_CANDIDATE)
    a = 1.0 / (4.0 * CLOG_CANDIDATE)
    log_x = math.log(ANCHOR_X)
    sqrt_log_x = math.sqrt(log_x)
    target_a = math.log(DUSART_THETA_DENOMINATOR) / sqrt_log_x
    return {
        "C_log_candidate": CLOG_CANDIDATE,
        "a_candidate": a,
        "c_candidate": c,
        "anchor_x": float(ANCHOR_X),
        "log_anchor": log_x,
        "sqrt_log_anchor": sqrt_log_x,
        "target_a_for_C1_at_anchor": target_a,
        "candidate_vs_target_a_ratio": a / target_a,
    }


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


def build_rows(previous: dict[str, Any], gamma: dict[str, Any], zero_count: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 C_log 数值账本判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    symbolic_available = "DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants" in basis
    gamma_closed = gamma.get("gamma_digamma_stirling_uniform_closed") is True
    zero_count_external_closed = bool(zero_count.get("jensen_zero_count_external_closed"))
    zero_count_self_closed = bool(zero_count.get("jensen_zero_count_self_contained_proved"))
    reduced = active and guard and symbolic_available and gamma_closed
    return [
        row(
            "ExplicitCLogGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Hadamard/Stirling/Jensen 剩余项的 C_log 数值上界。",
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
            "SymbolicRepulsionInputAvailable",
            symbolic_available,
            True,
            "符号排斥不等式已闭合，C_log 只负责把 O(log T) 剩余项数值化。",
            "无符号层剩余。",
        ),
        row(
            "GammaDigammaNumericalLedgerClosed",
            gamma_closed,
            True,
            "Gamma/digamma/Stirling 项已由 C_gamma=24 的统一 log 上界支付。",
            GAMMA_CLOSED if gamma_closed else GAMMA_ATOM,
        ),
        row(
            "JensenZeroCountingExternalClosed",
            zero_count_external_closed,
            False,
            "接受外部 Backlund/低高度输入时，局部零点计数已由 RVM-C_N=16 条件关闭。",
            ZERO_COUNT_EXTERNAL_CLOSED,
        ),
        row(
            "JensenZeroCountingSelfContainedStillOpen",
            zero_count_self_closed,
            False,
            "严格自足路线仍缺 Backlund 近零凹口成本内部化和 14 以下零点有限核验。",
            f"{BACKLUND_INDENT_ATOM} AND {LOW_HEIGHT_CRITICAL_LINE} AND {LOW_HEIGHT_OFF_LINE}",
        ),
        row(
            "HadamardPartialFractionRemainderMissing",
            False,
            False,
            "还需把远零点和 1/rho 项在 de la Vallee Poussin 组合中压入同一 C_log。",
            PARTIAL_FRACTION_ATOM,
        ),
        row(
            "CLogAggregationConventionMissing",
            False,
            False,
            "还需固定 sigma、t 范围、低高度交界和总 C_log 的加法预算。",
            AGGREGATION_ATOM,
        ),
        row(
            "ExplicitCLogReducedToFourMicroLedgers",
            reduced,
            False,
            "旧 C_log 原子已吸收 Gamma 数值账本；剩余为局部零点计数、Hadamard 余项与总常数聚合。",
            current_replacement_pair(gamma_closed),
        ),
        row(
            "ExplicitCLogExternalFrontierAdvanced",
            reduced and zero_count_external_closed,
            False,
            "外部条件分支已越过局部零点计数，当前推进点是 Hadamard 余项与总常数聚合。",
            current_external_replacement_pair(gamma_closed, zero_count_external_closed),
        ),
        row(
            "ZeroRepulsionParameterNumericalOptimizationStillNext",
            False,
            False,
            "C_log 聚合后，才能数值推出 c、T0 与零点自由带。",
            OPT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 C_log 数值账本路由。"""
    previous = load_json(paths["previous"])
    gamma = load_json(paths["gamma"])
    zero_count = load_json(paths["zero_count"])
    rows = build_rows(previous, gamma, zero_count)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "ExplicitCLogReducedToFourMicroLedgers")
    external_advanced = next(
        bool(item["closed"]) for item in rows if item["gate"] == "ExplicitCLogExternalFrontierAdvanced"
    )
    budget = candidate_budget()
    gamma_closed = gamma.get("gamma_digamma_stirling_uniform_closed") is True
    zero_count_external_closed = bool(zero_count.get("jensen_zero_count_external_closed"))
    zero_count_self_closed = bool(zero_count.get("jensen_zero_count_self_contained_proved"))
    return {
        "certificate_type": "b3_explicit_clog_router",
        "status": "explicit_clog_external_frontier_at_hadamard_self_contained_zero_count_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_clog_reduced": reduced,
        "explicit_clog_external_frontier_advanced": external_advanced,
        "explicit_clog_self_contained_proved": False,
        "jensen_zero_count_external_closed": zero_count_external_closed,
        "jensen_zero_count_self_contained_proved": zero_count_self_closed,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "current_replacement_self_contained": {
            OLD_ATOM: current_replacement_pair(gamma_closed)
        },
        "current_replacement_external": {
            OLD_ATOM: current_external_replacement_pair(gamma_closed, zero_count_external_closed)
        },
        "latest_self_contained_basis": replace_atom_with_current(
            previous.get("latest_self_contained_basis", ""), gamma_closed
        ),
        "latest_conditional_basis": replace_atom_with_external(
            previous.get("latest_conditional_basis", ""), gamma_closed, zero_count_external_closed
        ),
        "latest_global_with_external_basis": replace_atom_with_external(
            previous.get("latest_global_with_external_basis", ""), gamma_closed, zero_count_external_closed
        ),
        "next_priority": PARTIAL_FRACTION_ATOM if external_advanced else ZERO_COUNT_ATOM,
        "self_contained_next_priority": BACKLUND_INDENT_ATOM,
        "self_contained_low_height_priorities": [LOW_HEIGHT_CRITICAL_LINE, LOW_HEIGHT_OFF_LINE],
        "secondary_priority": AGGREGATION_ATOM,
        "tertiary_priority": OPT_ATOM,
        "quaternary_priority": OPT_ATOM,
        "post_clog_priority": OPT_ATOM,
        "post_optimization_priority": PNT_ATOM,
        "post_pnt_priority": TARGET_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_budget": budget,
        "proved_route_audit": {
            "gamma_closed": gamma_closed,
            "jensen_zero_count_external_closed": zero_count_external_closed,
            "jensen_zero_count_self_contained_proved": zero_count_self_closed,
        },
        "plain_conclusion": (
            "C_log 数值账本尚未完整闭合。Gamma/digamma/Stirling 分量已由 C_gamma=24 支付；"
            "局部零点计数在接受外部 Backlund/低高度输入时已条件关闭，因此外部条件分支下一步推进到 "
            "Hadamard 余项和总常数聚合。严格自足分支仍卡在 Backlund 近零凹口成本内部化与 14 以下零点核验。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    current_replacement = next(iter(result["current_replacement_self_contained"].items()))
    external_replacement = next(iter(result["current_replacement_external"].items()))
    budget = result["candidate_budget"]
    lines = [
        "# Prime Matrix B=3 显式 C_log 常数账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"explicit_clog_reduced={fmt_bool(result['explicit_clog_reduced'])}",
        f"explicit_clog_external_frontier_advanced={fmt_bool(result['explicit_clog_external_frontier_advanced'])}",
        f"explicit_clog_self_contained_proved={fmt_bool(result['explicit_clog_self_contained_proved'])}",
        f"jensen_zero_count_external_closed={fmt_bool(result['jensen_zero_count_external_closed'])}",
        f"jensen_zero_count_self_contained_proved={fmt_bool(result['jensen_zero_count_self_contained_proved'])}",
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
        "当前已证状态吸收后：",
        "",
        "```text",
        current_replacement[0],
        "  =>",
        current_replacement[1],
        "```",
        "",
        "外部 Backlund/低高度分支吸收后：",
        "",
        "```text",
        external_replacement[0],
        "  =>",
        external_replacement[1],
        "```",
        "",
        "## 2. 候选预算",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| C_log candidate | `{fmt_float(budget['C_log_candidate'])}` |",
        f"| a=1/(4C_log) | `{fmt_float(budget['a_candidate'])}` |",
        f"| c=1/(20C_log) | `{fmt_float(budget['c_candidate'])}` |",
        f"| target a for x=20000,C=1 | `{fmt_float(budget['target_a_for_C1_at_anchor'])}` |",
        f"| a/target_a | `{fmt_float(budget['candidate_vs_target_a_ratio'])}` |",
        "",
        (
            "候选 `C_log=64` 只用于预算排布。它给出的零点自由带常数极小，"
            "不能单独支撑 `x=20000` 的 theta 目标；后续仍需要 PNT 轮廓常数、低高度零点核验和有限桥。"
        ),
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
                f"外部条件分支最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`。严格自足分支仍需先攻 "
                f"`{result['self_contained_next_priority']}` 与低高度核验 "
                f"`{' AND '.join(result['self_contained_low_height_priorities'])}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--gamma", type=Path, default=DEFAULT_GAMMA)
    parser.add_argument("--zero-count", type=Path, default=DEFAULT_ZERO_COUNT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "gamma": args.gamma, "zero_count": args.zero_count}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
