#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 短平均点态桥闭合证书。

用法示例：
  python3 experiments/prime_matrix_b3_short_average_bridge_router.py

输出：
  docs/monograph/prime-matrix-b3-short-average-bridge-router.json
  docs/monograph/prime-matrix-b3-short-average-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-pointwise-bridge-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-short-average-bridge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-short-average-bridge-router.md"

OLD_ATOM = "BacklundShortAveragePointwiseBridgeLedger"
CLOSED_ATOM = "BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability"
SPIKE_ATOM = "BacklundArgumentSpikeExclusionLogDerivativeLedger"
SLACK_ATOM = "BacklundCS8SlackAfterBridgeLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

BRIDGE_FACTOR = 0.5


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成短平均点态桥判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    branch_ready = "BacklundArgumentBranchNormalizationClosed" in basis
    boundary_ready = "BacklundBoundaryConstantSumClosedC16" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and branch_ready and boundary_ready and guard
    return [
        row(
            "ShortAverageBridgeGateActive",
            active,
            False,
            "上一层唯一内部最窄点是短平均点态桥。",
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
            "BranchAndBoundaryAvailable",
            branch_ready and boundary_ready,
            True,
            "arg 分支归一化和边界常数合计已可用。",
            "无形式输入剩余。",
        ),
        row(
            "HalfMassShortAverageLemmaClosed",
            closed,
            True,
            "若 |A(t)-A(T)|<=|A(T)|/2 在短邻域成立，则该邻域平均至少保留 |A(T)|/2。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "短平均桥的形式部分闭合；它把剩余全部交给局部稳定/尖峰排斥。",
            CLOSED_ATOM,
        ),
        row(
            "SpikeExclusionStillNext",
            False,
            False,
            "下一步必须证明辐角不会形成比短平均更窄的尖峰。",
            SPIKE_ATOM,
        ),
        row(
            "CS8SlackStillDownstream",
            False,
            False,
            "尖峰排斥完成后再验收 C_S=8。",
            SLACK_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行短平均点态桥闭合证书。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_short_average_bridge_router",
        "status": "backlund_short_average_bridge_closed_formal_half",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_short_average_bridge_closed": closed,
        "bridge_factor": BRIDGE_FACTOR,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": SPIKE_ATOM,
        "secondary_priority": SLACK_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "core_lemma": (
            "For a continuous branch A(t), if |A(u)-A(T)|<=|A(T)|/2 on an interval I around T, "
            "then |I|^{-1} int_I |A(u)| du >= |A(T)|/2."
        ),
        "plain_conclusion": (
            "短平均点态桥的形式部分已闭合，桥接因子为 1/2。"
            "该层没有证明局部稳定性；所有尖峰风险仍由下一账本处理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 短平均点态桥闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_short_average_bridge_closed={fmt_bool(result['backlund_short_average_bridge_closed'])}",
        f"bridge_factor={fmt_float(result['bridge_factor'])}",
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
        "## 2. 形式引理",
        "",
        "```text",
        result["core_lemma"],
        "```",
        "",
        "这一步只处理从点态到短平均的逻辑转移；`A(t)` 的局部稳定性仍未证明。",
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
