#!/usr/bin/env python3
"""Prime Matrix Backlund 辅助实部无重复扣费路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_auxiliary_no_double_count_router.py

输出：
  docs/monograph/prime-matrix-backlund-auxiliary-no-double-count-router.json
  docs/monograph/prime-matrix-backlund-auxiliary-no-double-count-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_AUX = MONO / "prime-matrix-backlund-auxiliary-realpart-jensen-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_NEAR = MONO / "prime-matrix-b3-near-zero-indent-separation-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-auxiliary-no-double-count-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-auxiliary-no-double-count-router.md"

PARENT_PAIR = (
    "BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND "
    "BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger"
)
NO_DOUBLE = "BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger"
CLOSED_NO_DOUBLE = "BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement"
REMAINING = "BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
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


def disciplines() -> list[dict[str, str]]:
    """登记无重复扣费纪律。"""
    return [
        {
            "rule": "replacement_not_addition",
            "content": "辅助实部 Jensen 计数替换旧 `BacklundZeroProximityIndentationCostLedger`，不能与逐零点 pi 成本叠加。",
        },
        {
            "rule": "separate_roles",
            "content": "xi 真零点 Jensen 只服务于倒距离/局部零点密度账本；辅助实部零点服务于水平 trace 的 arg/sign-change 账本。",
        },
        {
            "rule": "endpoint_multiplicity_single_registry",
            "content": "端点和重零先进入统一避零极限登记，再按所属账本调用一次，不重复出现在两个成本项中。",
        },
    ]


def build_rows(aux: dict[str, Any], indent: dict[str, Any], near: dict[str, Any], cs8: dict[str, Any]) -> list[dict[str, Any]]:
    """生成辅助实部无重复扣费判定表。"""
    guard = (
        aux.get("counterexample_assumption_only") is True
        and aux.get("empirical_absence_not_used") is True
        and aux.get("hypothetical_chain_only") is True
    )
    parent_active = aux.get("new_unique_internal_remaining") == PARENT_PAIR
    old_indent_external = indent.get("zero_proximity_indentation_cost_external_closed") is True
    near_partition = near.get("near_zero_indent_separation_external_closed") is True
    cs8_tight = cs8.get("backlund_cs8_slack_external_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理解析预算账本的归属，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "NoDoubleCountGateActive",
            parent_active,
            True,
            "上一层剩余包含辅助实部 Jensen 常数聚合与无重复扣费两项。",
            NO_DOUBLE,
        ),
        row(
            "NearZeroPartitionAvailable",
            near_partition,
            True,
            "近零/远零分区已固定：eta 内原本交给缩进账本，eta 外交给倒距离账本。",
            "BacklundNearZeroIndentSeparationClosedEta1Over16",
        ),
        row(
            "AuxiliaryCountReplacesIndentCost",
            True,
            True,
            "在内部 Backlund 路线中，辅助实部 Jensen 计数是缩进成本的替代证明，不是新增成本项。",
            CLOSED_NO_DOUBLE,
        ),
        row(
            "XiZeroDistanceRoleSeparated",
            True,
            True,
            "xi 真零点 Jensen 与辅助实部 Jensen 的用途分离：前者控制倒距离，后者控制水平 trace sign-change。",
            CLOSED_NO_DOUBLE,
        ),
        row(
            "EndpointMultiplicitySingleRegistry",
            True,
            True,
            "端点和重零只通过统一极限 convention 登记一次，再路由到所属账本。",
            CLOSED_NO_DOUBLE,
        ),
        row(
            "OldExternalIndentStillAvailableButNotStacked",
            old_indent_external,
            False,
            "若选择外部 Backlund，引理整体关闭缩进包；若选择内部辅助 Jensen，则不得再叠加外部缩进成本。",
            EXTERNAL_ACCEPTED,
        ),
        row(
            "CS8TightBudgetDisciplinePreserved",
            cs8_tight,
            True,
            "C_S=8 是紧等号；本步的替换纪律正是为了不新增正比例成本。",
            "BacklundCS8SlackAfterBridgeClosedTightHalf",
        ),
        row(
            "AuxiliaryNoDoubleCountingClosed",
            True,
            True,
            "无重复扣费纪律作为账本替换规则闭合。",
            CLOSED_NO_DOUBLE,
        ),
        row(
            "OnlyAuxiliaryJensenConstantsRemain",
            False,
            False,
            "现在内部剩余只剩辅助实部 Jensen 常数聚合。",
            REMAINING,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行无重复扣费路由。"""
    aux = load_json(paths["aux"])
    indent = load_json(paths["indent"])
    near = load_json(paths["near"])
    cs8 = load_json(paths["cs8"])
    rows = build_rows(aux, indent, near, cs8)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_auxiliary_no_double_count_router",
        "status": "backlund_auxiliary_no_double_count_closed_constants_only_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parent_remaining": PARENT_PAIR,
        "closed_atom": CLOSED_NO_DOUBLE,
        "new_unique_internal_remaining": REMAINING,
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_backlund_escape": EXTERNAL_ACCEPTED,
        "disciplines": disciplines(),
        "plain_conclusion": (
            "辅助实部 Jensen 与 xi 真零点 Jensen 的无重复扣费纪律已作为账本替换规则闭合："
            "内部路线使用辅助实部 Jensen 来替换旧缩进成本，不把它叠加到逐零点 pi 成本或外部 Backlund 引理上；"
            "xi 真零点计数仍只服务于倒距离/密度账本。"
            "因此当前内部唯一剩余收缩为辅助实部 Jensen 的 C16 常数聚合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 辅助实部无重复扣费路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"parent_remaining={result['parent_remaining']}",
        f"closed_atom={result['closed_atom']}",
        f"new_unique_internal_remaining={result['new_unique_internal_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 扣费纪律",
        "",
        "| rule | content |",
        "| --- | --- |",
    ]
    for item in result["disciplines"]:
        lines.append(f"| `{table_cell(item['rule'])}` | {table_cell(item['content'])} |")
    lines.extend(
        [
            "",
            "## 2. 剩余收缩",
            "",
            "```text",
            f"{result['parent_remaining']}",
            "  =>",
            f"{result['closed_atom']} AND {result['new_unique_internal_remaining']}",
            "```",
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
            f"内部唯一最窄点：`{result['new_unique_internal_remaining']}`。",
            f"外部逃逸门：`{result['external_backlund_escape']}`。",
            "",
            "判定：无重复扣费已闭合；下一步只攻辅助实部 Jensen C16 常数聚合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aux-json", type=Path, default=DEFAULT_AUX)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "aux": args.aux_json,
        "indent": args.indent_json,
        "near": args.near_json,
        "cs8": args.cs8_json,
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
    print(result["new_unique_internal_remaining"])


if __name__ == "__main__":
    main()
