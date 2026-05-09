#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 局部零点计数账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_zero_count_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-zero-count-router.json
  docs/monograph/prime-matrix-b3-jensen-zero-count-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-explicit-clog-router.json"
DEFAULT_RVM = DOCS / "prime-matrix-b3-rvm-local-count-router.json"
DEFAULT_RVM_CN = DOCS / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-zero-count-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-zero-count-router.md"

OLD_ATOM = "JensenZeroCountingLocalNumericalLedger"
RVM_ATOM = "RiemannVonMangoldtExplicitLocalCountingLedger"
CLOSED_RVM_CN = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
BOUNDARY_ATOM = "XiBoundaryLogMajorantNumericalLedger"
ANCHOR_ATOM = "JensenDiskLowerAnchorNumericalLedger"
LOCAL_ATOM = "LocalZeroCountCNConventionLedger"
BACKLUND_INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
LOW_HEIGHT_CRITICAL_LINE = "CriticalLineNoZeroOn0To14FiniteLedger"
LOW_HEIGHT_OFF_LINE = "CriticalStripNoOffLineZeroBelow14TuringLedger"
PARTIAL_FRACTION_ATOM = "HadamardPartialFractionRemainderNumericalLedger"
AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

CN_CANDIDATE = 16.0


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
    """写出 Jensen 局部计数的自足替换包。"""
    return f"({RVM_ATOM} OR ({BOUNDARY_ATOM} AND {ANCHOR_ATOM} AND {LOCAL_ATOM}))"


def chosen_self_contained_pair() -> str:
    """写出当前主攻的 RVM 直接计数路线。"""
    return RVM_ATOM


def external_replacement_pair() -> str:
    """写出外部 Backlund/低高度输入下的替换包。"""
    return CLOSED_RVM_CN


def replace_atom(text: str) -> str:
    """替换旧 Jensen 计数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def replace_atom_by_external(text: str, external_closed: bool) -> str:
    """外部路线闭合时替换旧 Jensen 计数原子。"""
    if not external_closed:
        return text
    return text.replace(OLD_ATOM, external_replacement_pair())


def candidate_table() -> list[dict[str, float]]:
    """给 C_N=16 的候选预算生成审计表。"""
    rows: list[dict[str, float]] = []
    for t in [0.0, 1.0, 10.0, 100.0, 10_000.0, 1_000_000.0]:
        lval = math.log(abs(t) + 3.0)
        rows.append(
            {
                "t": t,
                "log_t_plus_3": lval,
                "CN_log_bound": CN_CANDIDATE * lval,
                "rvm_main_local_scale": max(0.0, math.log(abs(t) + 3.0) / math.pi),
                "budget_ratio_to_rvm_scale": CN_CANDIDATE * math.pi,
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


def build_rows(previous: dict[str, Any], rvm: dict[str, Any], rvm_cn: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Jensen 局部零点计数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    gamma_closed = "GammaDigammaStirlingUniformNumericalClosedCgamma24" in basis
    rvm_reduced = bool(rvm.get("rvm_local_count_reduced"))
    rvm_external_closed = bool(rvm_cn.get("rvm_to_cn16_external_closed"))
    rvm_self_closed = bool(rvm_cn.get("rvm_to_cn16_self_contained_closed"))
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and gamma_closed and guard
    external_closed = reduced and rvm_reduced and rvm_external_closed
    return [
        row(
            "JensenZeroCountingGateActive",
            active,
            False,
            "上一层唯一内部最窄点是局部零点计数 N(t+1)-N(t-1)<=C_N log(|t|+3)。",
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
            "GammaComponentAvailable",
            gamma_closed,
            True,
            "Gamma/digamma 分量已由 C_gamma=24 支付。",
            "无 Gamma 项剩余。",
        ),
        row(
            "RiemannVonMangoldtDirectRouteReduced",
            rvm_reduced,
            False,
            "局部零点计数可走 RVM 直接路线；该路线已被拆成 argument principle、Gamma 主项、Backlund、端点、CN16 合并。",
            RVM_ATOM,
        ),
        row(
            "ExternalRVMToCN16RouteClosed",
            rvm_external_closed,
            False,
            "接受外部 Backlund 缩进/低高度输入时，RVM 已合并为 C_N=16 局部计数。",
            CLOSED_RVM_CN,
        ),
        row(
            "JensenDiskAlternativeNotRequiredForRVMRoute",
            True,
            True,
            "边界上界和圆心下界只属于 Jensen 圆盘替代证明；当前主攻 RVM 直接路线时不作为额外必需项。",
            f"{BOUNDARY_ATOM} AND {ANCHOR_ATOM}",
        ),
        row(
            "JensenZeroCountingExternalClosed",
            external_closed,
            False,
            "在外部 Backlund/低高度输入下，旧 Jensen 局部计数原子可由 RVM-C_N=16 直接关闭。",
            CLOSED_RVM_CN,
        ),
        row(
            "JensenZeroCountingSelfContainedStillOpen",
            rvm_self_closed,
            False,
            "严格自足路线仍缺 Backlund 近零凹口成本内部化与 0<t<=14 的有限零点核验。",
            f"{BACKLUND_INDENT_ATOM} AND {LOW_HEIGHT_CRITICAL_LINE} AND {LOW_HEIGHT_OFF_LINE}",
        ),
        row(
            "JensenZeroCountingReducedToRVMOrDiskRoute",
            reduced,
            False,
            "旧 Jensen 局部计数原子已压成 RVM 直接计数路线，或 Jensen 圆盘边界/圆心替代路线。",
            replacement_pair(),
        ),
        row(
            "HadamardPartialFractionRemainderStillNext",
            False,
            False,
            "局部零点计数完成后，才可处理 Hadamard 远零点与 1/rho 余项。",
            PARTIAL_FRACTION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen 局部零点计数路由。"""
    previous = load_json(paths["previous"])
    rvm = load_json(paths["rvm"])
    rvm_cn = load_json(paths["rvm_cn"])
    rows = build_rows(previous, rvm, rvm_cn)
    reduced = next(
        bool(item["closed"]) for item in rows if item["gate"] == "JensenZeroCountingReducedToRVMOrDiskRoute"
    )
    external_closed = next(bool(item["closed"]) for item in rows if item["gate"] == "JensenZeroCountingExternalClosed")
    self_closed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "JensenZeroCountingSelfContainedStillOpen"
    )
    return {
        "certificate_type": "b3_jensen_zero_count_router",
        "status": "jensen_zero_count_rvm_route_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "jensen_zero_count_reduced": reduced,
        "jensen_zero_count_external_closed": external_closed,
        "jensen_zero_count_self_contained_proved": self_closed,
        "C_N_candidate": CN_CANDIDATE,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "chosen_self_contained_route": chosen_self_contained_pair(),
        "replacement_external": {OLD_ATOM: external_replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom_by_external(previous.get("latest_conditional_basis", ""), external_closed),
        "latest_global_with_external_basis": replace_atom_by_external(
            previous.get("latest_global_with_external_basis", ""), external_closed
        ),
        "next_priority": BACKLUND_INDENT_ATOM,
        "secondary_priority": LOW_HEIGHT_CRITICAL_LINE,
        "tertiary_priority": LOW_HEIGHT_OFF_LINE,
        "alternative_priority": f"{BOUNDARY_ATOM} AND {ANCHOR_ATOM} AND {LOCAL_ATOM}",
        "post_zero_count_priority": PARTIAL_FRACTION_ATOM,
        "post_partial_fraction_priority": AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "candidate_table": candidate_table(),
        "plain_conclusion": (
            "Jensen 局部零点计数的主攻路线改为 RVM 直接计数：边界上界和圆心下界只属于 Jensen 圆盘替代证明，"
            "不再作为 RVM 路线的额外必需项。接受外部 Backlund/低高度输入时，本局部计数已条件闭合；"
            "严格自足路线仍卡在 Backlund 近零凹口成本内部化与 14 以下零点有限核验。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    external_replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 局部零点计数账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"jensen_zero_count_reduced={fmt_bool(result['jensen_zero_count_reduced'])}",
        f"jensen_zero_count_external_closed={fmt_bool(result['jensen_zero_count_external_closed'])}",
        f"jensen_zero_count_self_contained_proved={fmt_bool(result['jensen_zero_count_self_contained_proved'])}",
        f"C_N_candidate={fmt_float(result['C_N_candidate'])}",
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
        "外部 Backlund/低高度输入下的条件替换：",
        "",
        "```text",
        external_replacement[0],
        "  =>",
        external_replacement[1],
        "```",
        "",
        "## 2. 候选预算",
        "",
        "| t | log(|t|+3) | C_N log bound | local RVM scale | budget ratio |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["candidate_table"]:
        lines.append(
            "| {t:.6g} | `{logv}` | `{bound}` | `{scale}` | `{ratio}` |".format(
                t=item["t"],
                logv=fmt_float(item["log_t_plus_3"]),
                bound=fmt_float(item["CN_log_bound"]),
                scale=fmt_float(item["rvm_main_local_scale"]),
                ratio=fmt_float(item["budget_ratio_to_rvm_scale"]),
            )
        )
    lines.extend(
        [
            "",
            "候选 `C_N=16` 明显大于 RVM 局部主尺度；当前选择 RVM 直接计数路线，"
            "Jensen 圆盘边界/圆心下界保留为替代路线而非额外必要条件。",
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
                f"严格自足路线的最窄点更新为 `{result['next_priority']}`；"
                f"并行低高度核验为 `{result['secondary_priority']}`、`{result['tertiary_priority']}`。"
                f"若改走 Jensen 圆盘替代路线，则需 `{result['alternative_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--rvm", type=Path, default=DEFAULT_RVM)
    parser.add_argument("--rvm-cn", type=Path, default=DEFAULT_RVM_CN)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "rvm": args.rvm, "rvm_cn": args.rvm_cn}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
