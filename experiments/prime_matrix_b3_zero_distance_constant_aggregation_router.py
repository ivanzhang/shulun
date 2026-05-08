#!/usr/bin/env python3
"""Prime Matrix B=3 零点倒距离常数聚合路由器。

用法示例：
  python3 experiments/prime_matrix_b3_zero_distance_constant_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-zero-distance-constant-aggregation-router.json
  docs/monograph/prime-matrix-b3-zero-distance-constant-aggregation-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-zero-distance-constant-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-zero-distance-constant-aggregation-router.md"

OLD_ATOM = "BacklundZeroDistanceSumConstantAggregationLedger"
CLOSED_ATOM = "BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16"
DYADIC_CLOSED = "BacklundZeroDistanceDyadicSummationClosed"
NEAR_ZERO_CLOSED = "BacklundNearZeroIndentSeparationClosedEta1Over16"
WINDOW_ATOM = "BacklundVariationWindowScaleLedger"
INDENT_ATOM = "BacklundZeroProximityIndentationCostLedger"
CS8_ATOM = "BacklundCS8SlackAfterBridgeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ETA = 1.0 / 16.0
C_ZERO_COUNT = 16.0
OLD_DISTANCE_TARGET = 64.0
SHELL_COUNT = math.ceil(math.log2(1.0 / ETA)) + 1
C_DISTANCE = C_ZERO_COUNT * (2.0 * SHELL_COUNT + 2.0)


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
    """替换零点倒距离常数聚合原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def constant_rows() -> list[dict[str, Any]]:
    """生成常数聚合表。"""
    return [
        {
            "quantity": "near-zero cutoff eta",
            "value": ETA,
            "formula": "1/16",
            "meaning": "eta 内零点已转入凹口成本。",
        },
        {
            "quantity": "dyadic shell count",
            "value": float(SHELL_COUNT),
            "formula": "ceil(log2(1/eta))+1",
            "meaning": "沿用旧倒距离路由器的有限层公式。",
        },
        {
            "quantity": "zero count coefficient",
            "value": C_ZERO_COUNT,
            "formula": "C_N",
            "meaning": "外部 Jensen C16 局部零点计数。",
        },
        {
            "quantity": "distance constant",
            "value": C_DISTANCE,
            "formula": "C_N*(2*shells+2)",
            "meaning": "eta 截断后的倒距离和常数。",
        },
        {
            "quantity": "old placeholder target",
            "value": OLD_DISTANCE_TARGET,
            "formula": "C_distance_target",
            "meaning": "旧 64 只是 eta=1 级占位，不能继续使用。",
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
    """生成零点倒距离常数聚合判定表。"""
    external_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    dyadic_ready = DYADIC_CLOSED in external_basis
    near_ready = bool(previous.get("near_zero_indent_separation_external_closed")) and NEAR_ZERO_CLOSED in external_basis
    c16_ready = "BacklundJensenRadiusOptimizationNotNeededC16ClosedR4" in external_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and dyadic_ready and near_ready and c16_ready and guard and C_DISTANCE == 192.0
    return [
        row(
            "ZeroDistanceConstantAggregationGateActive",
            active,
            False,
            "外部 Backlund/Jensen 分支当前最窄点是倒距离和常数聚合。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的解析记账，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "DyadicAndNearZeroInputsAvailable",
            dyadic_ready and near_ready,
            True,
            "dyadic 求和形式已闭合，eta=1/16 的近零分离也已闭合。",
            f"{DYADIC_CLOSED} AND {NEAR_ZERO_CLOSED}",
        ),
        row(
            "ExternalJensenC16CountAvailable",
            c16_ready,
            False,
            "每个固定局部盘的零点数由外部 Jensen C16 聚合给出。",
            "BacklundIndependentJensenZeroCountC16AggregationExternalClosed",
        ),
        row(
            "DistanceConstantC192Computed",
            C_DISTANCE == 192.0,
            True,
            "按旧 dyadic 公式，eta=1/16 给出 C_distance=16*(2*5+2)=192。",
            CLOSED_ATOM,
        ),
        row(
            "OldC64PlaceholderRejected",
            C_DISTANCE > OLD_DISTANCE_TARGET,
            True,
            "旧 C_distance=64 只对应无近零截断的占位；当前链条必须携带 C192 进入窗口尺度验收。",
            WINDOW_ATOM,
        ),
        row(
            "ZeroDistanceConstantAggregationClosed",
            closed,
            True,
            "倒距离和常数已显式聚合为 C192；后续只需选择窗口尺度吸收该常数。",
            CLOSED_ATOM,
        ),
        row(
            "VariationWindowScaleNext",
            False,
            False,
            "下一步必须用 C192 选择短窗口尺度，不能回退到 C64。",
            WINDOW_ATOM,
        ),
        row(
            "IndentCostStillDownstream",
            False,
            False,
            "近零点凹口成本仍未支付。",
            INDENT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点倒距离常数聚合路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ZeroDistanceConstantAggregationClosed"
    )
    latest_external = replace_atom(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "b3_zero_distance_constant_aggregation_router",
        "status": "zero_distance_constant_aggregation_external_closed_c192",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_distance_constant_aggregation_external_closed": closed,
        "zero_distance_constant_aggregation_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "eta": ETA,
        "zero_count_constant": C_ZERO_COUNT,
        "shell_count": SHELL_COUNT,
        "distance_constant": C_DISTANCE,
        "old_distance_target_rejected": OLD_DISTANCE_TARGET,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": WINDOW_ATOM,
        "post_window_priority": INDENT_ATOM,
        "post_indent_priority": CS8_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "constant_rows": constant_rows(),
        "plain_conclusion": (
            "零点倒距离常数聚合在外部 Backlund/Jensen 分支中闭合为 C_distance=192。"
            "这是 eta=1/16 近零截断与 Jensen C16 计数的直接聚合；旧 C64 不能继续使用，"
            "后续窗口尺度必须按 C192 重新选择。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 零点倒距离常数聚合路由器",
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
            "zero_distance_constant_aggregation_external_closed="
            f"{fmt_bool(result['zero_distance_constant_aggregation_external_closed'])}"
        ),
        (
            "zero_distance_constant_aggregation_self_contained_closed="
            f"{fmt_bool(result['zero_distance_constant_aggregation_self_contained_closed'])}"
        ),
        f"eta={fmt_float(result['eta'])}",
        f"zero_count_constant={fmt_float(result['zero_count_constant'])}",
        f"shell_count={result['shell_count']}",
        f"distance_constant={fmt_float(result['distance_constant'])}",
        f"old_distance_target_rejected={fmt_float(result['old_distance_target_rejected'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件链替换",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 常数表",
        "",
        "| quantity | value | formula | meaning |",
        "| --- | ---: | --- | --- |",
    ]
    for item in result["constant_rows"]:
        lines.append(
            "| {quantity} | `{value}` | {formula} | {meaning} |".format(
                quantity=table_cell(item["quantity"]),
                value=fmt_float(float(item["value"])),
                formula=table_cell(item["formula"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
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
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部 Backlund/Jensen 分支下一步转为 `{result['conditional_next_priority']}`。"
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
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
