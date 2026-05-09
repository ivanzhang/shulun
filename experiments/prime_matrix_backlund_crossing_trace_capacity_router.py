#!/usr/bin/env python3
"""Prime Matrix Backlund crossing trace 容量收缩路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_crossing_trace_capacity_router.py

输出：
  docs/monograph/prime-matrix-backlund-crossing-trace-capacity-router.json
  docs/monograph/prime-matrix-backlund-crossing-trace-capacity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-indent-internal-attack-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_VARIATION = MONO / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-crossing-trace-capacity-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-crossing-trace-capacity-router.md"

TRACE_ATOM = "BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger"
PAIRING_ATOM = "BacklundSignedCrossingPairingInvolutionLedger"
CLUSTER_ATOM = "BacklundCanonicalNearZeroClusterBoxLedger"
RESIDUAL_ATOM = "BacklundResidualIndentCoefficientZeroLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
CS8 = "BacklundCS8SlackAfterBridgeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """输出固定精度浮点数。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


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


def build_capacity_numbers(indent: dict[str, Any], variation: dict[str, Any]) -> dict[str, float]:
    """汇总 crossing trace 的系数级容量数字。"""
    naive = float(indent["naive_indentation_coefficient"])
    margin = float(indent.get("available_stability_margin", variation["stability_margin"]))
    per_zero = math.pi
    zero_count = naive / per_zero
    max_unpaired_coeff = margin / per_zero
    allowed_fraction_of_jensen = max_unpaired_coeff / zero_count
    return {
        "zero_count_coefficient": zero_count,
        "per_unpaired_crossing_cost": per_zero,
        "naive_indentation_coefficient": naive,
        "available_stability_margin": margin,
        "max_unpaired_crossing_coefficient": max_unpaired_coeff,
        "allowed_fraction_of_jensen_count": allowed_fraction_of_jensen,
        "naive_margin_deficit": naive - margin,
    }


def lower_atoms() -> list[dict[str, str]]:
    """写出 trace 原子压缩后的下层输入基。"""
    return [
        {
            "atom": CLUSTER_ATOM,
            "role": "把 eta=1/16 内所有近零点按窗口和重数做 canonical box 账本。",
        },
        {
            "atom": PAIRING_ATOM,
            "role": "在同一 formal unit 内给出带符号 crossing 的配对 involution。",
        },
        {
            "atom": RESIDUAL_ATOM,
            "role": "由配对证明未配对 crossing 的 log(T) 系数为 0，而不是小的正数。",
        },
    ]


def build_rows(previous: dict[str, Any], numbers: dict[str, float]) -> list[dict[str, Any]]:
    """生成 crossing trace 容量判定表。"""
    active = previous.get("next_priority") == TRACE_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    naive_fails = numbers["naive_margin_deficit"] > 0.0
    positive_fraction_forbidden = numbers["allowed_fraction_of_jensen_count"] < 0.01
    return [
        row(
            "CrossingTraceCapacityGateActive",
            active,
            True,
            "上一层已把凹口成本二选一压成局部 crossing trace 单原子。",
            TRACE_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在早期零行反例假设链条内做解析容量收缩，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "NaiveResidualBudgetImpossible",
            naive_fails,
            True,
            "若允许 Jensen C16 规模的未配对 crossing 粗付 pi 成本，系数缺口约 50.187。",
            PAIRING_ATOM,
        ),
        row(
            "PositiveCoefficientResidualForbidden",
            positive_fraction_forbidden,
            True,
            "余量只允许不到 Jensen 近零数量上界的 0.2% 留作未配对成本；这不是稳健闭合路径。",
            PAIRING_ATOM,
        ),
        row(
            "ExactCancellationIsNecessary",
            True,
            True,
            "自足路线若不调用外部 Backlund 凹口引理，就必须证明 log(T) 级未配对 crossing 系数为 0。",
            f"{PAIRING_ATOM} AND {RESIDUAL_ATOM}",
        ),
        row(
            "ClusterBoxSchemaAvailable",
            True,
            True,
            "上一层 trace schema 已指定 window_id、zero_cluster_box、homotopy_arc、branch_jump 等字段。",
            CLUSTER_ATOM,
        ),
        row(
            CLUSTER_ATOM,
            False,
            False,
            "尚未生成每个近零窗口的 canonical cluster box 与 multiplicity hash。",
            CLUSTER_ATOM,
        ),
        row(
            PAIRING_ATOM,
            False,
            False,
            "尚未证明所有 branch_jump 都在同一 formal unit 中成对抵消。",
            PAIRING_ATOM,
        ),
        row(
            RESIDUAL_ATOM,
            False,
            False,
            "只有配对 involution 完成后，残余凹口系数才能降为 0 并落入 5/64 余量。",
            RESIDUAL_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 crossing trace 容量收缩。"""
    previous = load_json(paths["previous"])
    indent = load_json(paths["indent"])
    variation = load_json(paths["variation"])
    numbers = build_capacity_numbers(indent, variation)
    rows = build_rows(previous, numbers)
    reduction_closed = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "CrossingTraceCapacityGateActive",
            "CounterexampleBranchGuardPreserved",
            "NaiveResidualBudgetImpossible",
            "PositiveCoefficientResidualForbidden",
            "ExactCancellationIsNecessary",
            "ClusterBoxSchemaAvailable",
        }
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_crossing_trace_capacity_router",
        "status": "backlund_crossing_trace_capacity_reduced_to_signed_pairing_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "trace_capacity_reduction_closed": reduction_closed,
        "backlund_local_crossing_trace_closed": False,
        "backlund_indent_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "numbers": numbers,
        "lower_atoms": lower_atoms(),
        "replacement_self_contained": {
            TRACE_ATOM: f"({CLUSTER_ATOM} AND {PAIRING_ATOM} AND {RESIDUAL_ATOM})"
        },
        "next_priority": PAIRING_ATOM,
        "support_priority": CLUSTER_ATOM,
        "post_pairing_priority": RESIDUAL_ATOM,
        "external_escape": EXTERNAL_ATOM,
        "post_trace_priority": CS8,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "crossing trace 的下层最窄目标已从“付凹口成本”收缩为“证明带符号 crossing 精确配对”。"
            "原因是剩余稳定余量只有 5/64，而 Jensen C16 规模的未配对零点按 pi 粗付会产生约 50.187 的系数缺口。"
            "所以自足路线不能再走正比例残留预算，只能证明未配对 crossing 的 log(T) 系数为 0，"
            "或明确接受外部经典 Backlund 凹口引理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    numbers = result["numbers"]
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund crossing trace 容量收缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"trace_capacity_reduction_closed={fmt_bool(result['trace_capacity_reduction_closed'])}",
        f"backlund_local_crossing_trace_closed={fmt_bool(result['backlund_local_crossing_trace_closed'])}",
        f"backlund_indent_self_contained_closed={fmt_bool(result['backlund_indent_self_contained_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 系数容量",
        "",
        "| item | value |",
        "| --- | ---: |",
    ]
    for key in [
        "zero_count_coefficient",
        "per_unpaired_crossing_cost",
        "naive_indentation_coefficient",
        "available_stability_margin",
        "max_unpaired_crossing_coefficient",
        "allowed_fraction_of_jensen_count",
        "naive_margin_deficit",
    ]:
        lines.append(f"| `{key}` | `{fmt_float(numbers[key])}` |")
    lines.extend(
        [
            "",
            "核心不等式：",
            "",
            "```text",
            "unpaired_crossing_coefficient * pi <= 5/64",
            "so unpaired_crossing_coefficient <= 0.024867959858",
            "but Jensen near-zero coefficient available is 16.",
            "```",
            "",
            "这说明：若未配对 crossing 仍有任何 Jensen 规模的正比例残留，预算立即失败；自足路线必须把残余 log(T) 系数压到 0。",
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "| atom | role |",
            "| --- | --- |",
        ]
    )
    for item in result["lower_atoms"]:
        lines.append(f"| `{table_cell(item['atom'])}` | {table_cell(item['role'])} |")
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
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一步",
            "",
            f"当前下层最窄点：`{result['next_priority']}`。",
            f"支撑账本：`{result['support_priority']}`。",
            f"配对完成后验收：`{result['post_pairing_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            f"并行保留晋级门：`{result['parallel_priority']}`。",
            "",
            "判定：trace 容量收缩已完成；命题尚未自足闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--variation-json", type=Path, default=DEFAULT_VARIATION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "indent": args.indent_json,
        "variation": args.variation_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
