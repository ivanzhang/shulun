#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 辐角尖峰排斥路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_spike_exclusion_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-spike-exclusion-router.json
  docs/monograph/prime-matrix-b3-backlund-spike-exclusion-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-short-average-bridge-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-spike-exclusion-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-spike-exclusion-router.md"

OLD_ATOM = "BacklundArgumentSpikeExclusionLogDerivativeLedger"
NO_CIRCULAR_CLOSED = "BacklundSpikeNoRVMCircularityDisciplineClosed"
LOGDER_ATOM = "BacklundIndependentLogDerivativeLocalVariationLedger"
INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
SLACK_ATOM = "BacklundCS8SlackAfterBridgeLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
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
    """写出尖峰排斥替换包。"""
    return f"({NO_CIRCULAR_CLOSED} AND {LOGDER_ATOM} AND {INDENT_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧尖峰排斥原子。"""
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
    """生成辐角尖峰排斥判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    short_bridge_ready = "BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability" in basis
    branch_ready = "BacklundArgumentBranchNormalizationClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and short_bridge_ready and branch_ready and guard
    return [
        row(
            "BacklundSpikeExclusionGateActive",
            active,
            False,
            "上一层唯一内部最窄点是辐角尖峰排斥。",
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
            "ShortAverageAndBranchAvailable",
            short_bridge_ready and branch_ready,
            True,
            "短平均形式桥和 arg 分支归一化均已闭合。",
            "无形式桥剩余。",
        ),
        row(
            "NoRVMCircularityDisciplineClosed",
            reduced,
            True,
            "尖峰排斥不能调用由 Backlund 自身推出的 RVM 局部零点计数，否则形成循环证明。",
            NO_CIRCULAR_CLOSED,
        ),
        row(
            "IndependentLogDerivativeLocalVariationMissing",
            False,
            False,
            "仍需独立于 Backlund/RVM 的 log-derivative 局部变差界，用来证明辐角短区间内不丢半。",
            LOGDER_ATOM,
        ),
        row(
            "ZeroProximityIndentationCostMissing",
            False,
            False,
            "仍需对短区间靠近零点时的凹口成本作独立记账，不能把成本推给待证 RVM。",
            INDENT_ATOM,
        ),
        row(
            "BacklundSpikeExclusionReduced",
            reduced,
            False,
            "旧尖峰排斥原子已压成非循环纪律、独立 log-derivative 变差界和零点邻近凹口成本三包。",
            replacement_pair(),
        ),
        row(
            "CS8SlackStillDownstream",
            False,
            False,
            "尖峰排斥闭合后才能最终验收 C_S=8。",
            SLACK_ATOM,
        ),
        row(
            "EndpointAndCN16StillDownstream",
            False,
            False,
            "Backlund 完成后仍需端点 convention 与 RVM->CN16 合并。",
            f"{ENDPOINT_ATOM} AND {RVM_CN_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Backlund 辐角尖峰排斥路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "BacklundSpikeExclusionReduced")
    return {
        "certificate_type": "b3_backlund_spike_exclusion_router",
        "status": "backlund_spike_exclusion_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_spike_exclusion_reduced": reduced,
        "backlund_spike_exclusion_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": LOGDER_ATOM,
        "secondary_priority": INDENT_ATOM,
        "tertiary_priority": SLACK_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "forbidden_shortcut": "Do not use RiemannVonMangoldtExplicitLocalCountingLedger to prove this Backlund spike exclusion.",
        "plain_conclusion": (
            "Backlund 尖峰排斥尚未闭合。"
            "本步闭合的是非循环纪律：不能用待由 Backlund 推出的 RVM 局部零点计数来反过来证明 Backlund。"
            "真正剩余是独立 log-derivative 局部变差界和零点邻近凹口成本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 辐角尖峰排斥路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_spike_exclusion_reduced={fmt_bool(result['backlund_spike_exclusion_reduced'])}",
        (
            "backlund_spike_exclusion_self_contained_proved="
            f"{fmt_bool(result['backlund_spike_exclusion_self_contained_proved'])}"
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
        "## 2. 非循环纪律",
        "",
        "```text",
        result["forbidden_shortcut"],
        "```",
        "",
        "这条纪律是必要的：当前 RVM 局部零点计数链条本身依赖 Backlund/arg zeta 上界。",
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
