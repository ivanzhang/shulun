#!/usr/bin/env python3
"""Prime Matrix Backlund 凹口成本零点权重吸收审查路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_indent_weight_absorption_router.py

输出：
  docs/monograph/prime-matrix-backlund-indent-weight-absorption-router.json
  docs/monograph/prime-matrix-backlund-indent-weight-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_STATUS = MONO / "prime-matrix-backlund-final-branch-status-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_LITTLEWOOD = MONO / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_HORIZONTAL = MONO / "prime-matrix-b3-horizontal-variation-router.json"
DEFAULT_NEAR = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_VARIATION = MONO / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-indent-weight-absorption-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-indent-weight-absorption-router.md"

INDENT_COST = "BacklundZeroProximityIndentationCostLedger"
INTERNALIZATION = "ClassicalBacklundIndentationLemmaInternalizationLedger"
WEIGHT_ABSORB = "BacklundLittlewoodZeroWeightAbsorptionForIndentCoresLedger"
NO_DOUBLE = "BacklundZeroWeightNoDoubleCountingLedger"
POINTWISE_TRANSFER = "BacklundPointwiseNearZeroCoreTransferLedger"
CONSTANT_REAGG = "BacklundC8BudgetPreservingIndentReaggregationLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def absorption_domains() -> list[dict[str, str]]:
    """区分零点权重吸收可用和不可直接可用的域。"""
    return [
        {
            "domain": "Littlewood rectangle boundary",
            "verdict": "closed",
            "reason": "边界碰零可由 epsilon/小凹口取极限，零点按重数进入 Littlewood 零点横向权重项。",
        },
        {
            "domain": "horizontal variation convention",
            "verdict": "closed",
            "reason": "水平边缩进 convention 已作为形式层闭合，并进入 C_horizontal=8 聚合。",
        },
        {
            "domain": "pointwise bridge near-zero cores",
            "verdict": "open",
            "reason": "当前剩余来自短窗口点态桥/log-derivative 变差中的 eta 内近零核心，不是原始 Littlewood 平均恒等式的边界缩进。",
        },
        {
            "domain": "C_S=8 reaggregation",
            "verdict": "open",
            "reason": "C_S=8 为紧等号；若把近零核心再交给零点权重项，必须证明不重复扣 Jensen/RVM 零点预算。",
        },
    ]


def internalization_atoms() -> list[dict[str, str]]:
    """经典 Backlund 缩进引理内部化的必要子账本。"""
    return [
        {
            "atom": WEIGHT_ABSORB,
            "role": "证明缩进弧贡献与 Littlewood 零点横向权重在同一恒等式中精确配平。",
        },
        {
            "atom": POINTWISE_TRANSFER,
            "role": "证明这种配平可从矩形平均层转移到短窗口点态桥的近零核心。",
        },
        {
            "atom": NO_DOUBLE,
            "role": "证明近零核心不会同时在 Jensen C16、RVM CN16 和凹口成本中重复扣费。",
        },
        {
            "atom": CONSTANT_REAGG,
            "role": "重新聚合常数，证明吸收后仍保持 C_S=8 与 5/64 稳定余量纪律。",
        },
    ]


def build_rows(
    status: dict[str, Any],
    indent: dict[str, Any],
    littlewood: dict[str, Any],
    horizontal: dict[str, Any],
    near: dict[str, Any],
    variation: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成零点权重吸收审查判定表。"""
    active = status.get("self_contained_remaining") == INDENT_COST
    guard = (
        status.get("counterexample_assumption_only") is True
        and status.get("empirical_absence_not_used") is True
        and status.get("hypothetical_chain_only") is True
    )
    littlewood_closed = littlewood.get("backlund_littlewood_rectangle_argument_closed") is True
    horizontal_convention_closed = "HorizontalZeroIndentationConventionClosed" in "\n".join(
        str(item) for item in horizontal.get("closed_gates", [])
    ) or horizontal.get("critical_strip_horizontal_variation_reduced") is True
    near_assigned = near.get("near_zero_indent_separation_external_closed") is True
    c8_tight_margin = float(variation.get("stability_margin", 0.0)) == 0.078125
    naive_fails = float(indent.get("naive_margin_deficit", 0.0)) > 0.0
    absorption_reduction_closed = (
        active
        and guard
        and littlewood_closed
        and horizontal_convention_closed
        and near_assigned
        and c8_tight_margin
        and naive_fails
    )
    return [
        row(
            "IndentWeightAbsorptionGateActive",
            active,
            True,
            "当前严格自足唯一剩余是 Backlund 近零凹口成本。",
            INDENT_COST,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析记账，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "LittlewoodZeroWeightAbsorptionAvailableOnlyInRectangle",
            littlewood_closed,
            True,
            "Littlewood 矩形恒等式已含零点横向权重；边界缩进可在该恒等式中按重数取极限。",
            WEIGHT_ABSORB,
        ),
        row(
            "HorizontalIndentConventionAlreadySpent",
            horizontal_convention_closed,
            True,
            "水平边缩进 convention 已进入水平边常数聚合，不能再作为近零核心的额外免费预算。",
            NO_DOUBLE,
        ),
        row(
            "NearZeroCoresAssignedDownstream",
            near_assigned,
            True,
            "eta=1/16 内近零点已从倒距离和中剥出，明确交给凹口成本账本。",
            POINTWISE_TRANSFER,
        ),
        row(
            "NaiveCostStillFails",
            naive_fails,
            True,
            "逐零点付费仍有约 50.187 的 log(T) 系数缺口；吸收必须是恒等式级，不是新预算。",
            CONSTANT_REAGG,
        ),
        row(
            "C8AndStabilityBudgetTight",
            c8_tight_margin,
            True,
            "窗口稳定余量只有 5/64；任何正比例未吸收项都会破坏点态桥。",
            CONSTANT_REAGG,
        ),
        row(
            "DirectLittlewoodAbsorptionBlockedForPointwiseCore",
            True,
            True,
            "Littlewood 零点权重吸收只在矩形平均恒等式内闭合，尚未转移到短窗口点态桥的近零核心。",
            POINTWISE_TRANSFER,
        ),
        row(
            "IndentCostReducedToClassicalLemmaInternalization",
            absorption_reduction_closed,
            False,
            "唯一剩余被压成经典 Backlund 缩进引理的内部化：权重吸收、点态转移、无重复扣费和 C8 重聚合。",
            INTERNALIZATION,
        ),
        row(
            INTERNALIZATION,
            False,
            False,
            "尚未给出完整内部证明；外部引理仍可接受但不是严格自足闭合。",
            f"{WEIGHT_ABSORB} AND {POINTWISE_TRANSFER} AND {NO_DOUBLE} AND {CONSTANT_REAGG}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行零点权重吸收审查。"""
    status = load_json(paths["status"])
    indent = load_json(paths["indent"])
    littlewood = load_json(paths["littlewood"])
    horizontal = load_json(paths["horizontal"])
    near = load_json(paths["near"])
    variation = load_json(paths["variation"])
    rows = build_rows(status, indent, littlewood, horizontal, near, variation)
    reduction_closed = next(
        item["closed"] for item in rows if item["gate"] == "IndentCostReducedToClassicalLemmaInternalization"
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_indent_weight_absorption_router",
        "status": "backlund_indent_weight_absorption_reduced_to_classical_lemma_internalization_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "indent_weight_absorption_reduction_closed": reduction_closed,
        "indent_cost_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "absorption_domains": absorption_domains(),
        "internalization_atoms": internalization_atoms(),
        "replacement_self_contained": {INDENT_COST: INTERNALIZATION},
        "next_priority": POINTWISE_TRANSFER,
        "support_priority": WEIGHT_ABSORB,
        "discipline_priority": NO_DOUBLE,
        "constant_priority": CONSTANT_REAGG,
        "external_escape": EXTERNAL_ATOM,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "零点权重吸收方向不能直接关闭 Backlund 近零凹口成本。"
            "Littlewood 矩形层确实已把边界缩进按零点横向权重吸收；"
            "但当前唯一剩余来自短窗口点态桥/log-derivative 变差中的 eta 内近零核心。"
            "要严格自足闭合，必须内部化经典 Backlund 缩进引理，证明矩形平均层的零点权重吸收可无损转移到点态近零核心，"
            "且不重复扣 Jensen/RVM 零点预算，并保持 C_S=8 与 5/64 稳定余量。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix Backlund 凹口成本零点权重吸收审查路由器",
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
            "indent_weight_absorption_reduction_closed="
            f"{fmt_bool(result['indent_weight_absorption_reduction_closed'])}"
        ),
        f"indent_cost_self_contained_closed={fmt_bool(result['indent_cost_self_contained_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 吸收适用域",
        "",
        "| domain | verdict | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["absorption_domains"]:
        lines.append(
            f"| `{table_cell(item['domain'])}` | `{table_cell(item['verdict'])}` | {table_cell(item['reason'])} |"
        )
    lines.extend(
        [
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
    for item in result["internalization_atoms"]:
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
            f"当前真正最窄点：`{result['next_priority']}`。",
            f"支撑吸收账本：`{result['support_priority']}`。",
            f"无重复扣费纪律：`{result['discipline_priority']}`。",
            f"常数重聚合：`{result['constant_priority']}`。",
            f"外部可接受逃逸门：`{result['external_escape']}`。",
            "",
            "判定：发现并阻断了直接吸收伪闭合；剩余压成经典 Backlund 缩进引理内部化。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status-json", type=Path, default=DEFAULT_STATUS)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--littlewood-json", type=Path, default=DEFAULT_LITTLEWOOD)
    parser.add_argument("--horizontal-json", type=Path, default=DEFAULT_HORIZONTAL)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--variation-json", type=Path, default=DEFAULT_VARIATION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "status": args.status_json,
        "indent": args.indent_json,
        "littlewood": args.littlewood_json,
        "horizontal": args.horizontal_json,
        "near": args.near_json,
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
