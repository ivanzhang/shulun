#!/usr/bin/env python3
"""Prime Matrix Backlund sign-change 吸收障碍路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_signchange_absorption_obstruction_router.py

输出：
  docs/monograph/prime-matrix-backlund-signchange-absorption-obstruction-router.json
  docs/monograph/prime-matrix-backlund-signchange-absorption-obstruction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_SPINE = MONO / "prime-matrix-backlund-classical-indent-spine-router.json"
DEFAULT_JENSEN_ZERO = MONO / "prime-matrix-b3-jensen-radius-contingency-router.json"
DEFAULT_LITTLEWOOD = MONO / "prime-matrix-b3-backlund-littlewood-rectangle-router.json"
DEFAULT_EXTERNAL_INDEX = MONO / "external-theorem-index.md"
DEFAULT_JSON = MONO / "prime-matrix-backlund-signchange-absorption-obstruction-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-signchange-absorption-obstruction-router.md"

OLD_REMAINING = "BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger"
NEW_REMAINING = "BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger"
FALSE_INJECTION = "BacklundSignChangeZerosInjectIntoXiZeroJensenLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def obstruction_examples() -> list[dict[str, str]]:
    """给出 sign-change 零点不是解析零点的局部模型。"""
    return [
        {
            "model": "F(x)=x+i",
            "sign_change_event": "Re F(0)=0 且 F(0)=i != 0",
            "meaning": "实部过零只说明曲线穿过虚轴，不说明 F 有零点。",
        },
        {
            "model": "F(x)=e^{ix}",
            "sign_change_event": "Re F(x)=0 在 x=pi/2+k*pi 出现，但 F(x) 从不为 0",
            "meaning": "sign-change 数可与解析零点数完全脱钩。",
        },
        {
            "model": "F(s)=(s-rho)^m g(s)",
            "sign_change_event": "若路径命中 rho，则缩进 jump 按 m 登记；但非零穿轴事件仍可能存在",
            "meaning": "重数登记只处理真零点；经典 Backlund 还必须计数非零的实部过零。",
        },
    ]


def build_rows(spine: dict[str, Any], jensen_zero: dict[str, Any], littlewood: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 sign-change 吸收障碍判定表。"""
    guard = (
        spine.get("counterexample_assumption_only") is True
        and spine.get("empirical_absence_not_used") is True
        and spine.get("hypothetical_chain_only") is True
    )
    spine_remaining = spine.get("new_unique_internal_remaining") == OLD_REMAINING
    external_c16_available = jensen_zero.get("jensen_c16_aggregation_external_closed") is True
    littlewood_closed = littlewood.get("backlund_littlewood_rectangle_argument_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只检查假设链条里的解析计数对象，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "SignChangeAbsorptionGateActive",
            spine_remaining,
            True,
            "上一层把内部剩余压成 sign-change 登记表对 Jensen C16 的无重复吸收。",
            OLD_REMAINING,
        ),
        row(
            "XiZeroJensenC16AvailableExternally",
            external_c16_available,
            False,
            "外部低高度输入下，xi 真零点的 Jensen C16 计数可作为参照。",
            "BacklundIndependentJensenZeroCountC16AggregationExternalClosed",
        ),
        row(
            "LittlewoodZeroWeightIdentityAvailable",
            littlewood_closed,
            True,
            "Littlewood 矩形恒等式登记的是解析零点横向权重，不是所有实部过零。",
            "BacklundLittlewoodRectangleArgumentClosed",
        ),
        row(
            "SignChangeNotXiZeroObstructionClosed",
            True,
            True,
            "Re(e^{-i theta}F) 的零点通常只是曲线穿过一条直线；F 本身可以非零。",
            FALSE_INJECTION,
        ),
        row(
            "DirectInjectionIntoXiZeroJensenRejected",
            True,
            True,
            "不能把 sign-change 事件逐项注入 xi 零点 Jensen 计数；这会漏掉非零穿轴事件。",
            NEW_REMAINING,
        ),
        row(
            "AuxiliaryRealPartAnalyticFunctionNeeded",
            True,
            True,
            "经典 Backlund 必须为实部/旋转实部构造辅助解析计数对象，并对该对象应用 Jensen。",
            NEW_REMAINING,
        ),
        row(
            "NoDoubleCountConditionStillNeeded",
            False,
            False,
            "辅助实部 Jensen 计数完成后，还需证明它与 xi 真零点、端点重数和缩进登记不重复扣费。",
            NEW_REMAINING,
        ),
        row(
            "SelfContainedBacklundIndentStillOpen",
            False,
            False,
            "内部经典 Backlund 缩进证明仍未闭合；现在精确剩余是辅助实部 Jensen 计数和无重复扣费。",
            NEW_REMAINING,
        ),
        row(
            "ExternalBacklundStillClosesThisPackage",
            True,
            False,
            "外部经典 Backlund 引理正是对该辅助实部计数和缩进 convention 的整体引用。",
            EXTERNAL_ACCEPTED,
        ),
        row(
            "ExternalRouteStillNeedsDStructure",
            False,
            False,
            "接受外部 Backlund 后仍不能跳过 DStructure/Rankin 独立验收门。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 sign-change 吸收障碍路由。"""
    spine = load_json(paths["spine"])
    jensen_zero = load_json(paths["jensen_zero"])
    littlewood = load_json(paths["littlewood"])
    rows = build_rows(spine, jensen_zero, littlewood)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_signchange_absorption_obstruction_router",
        "status": "backlund_signchange_absorption_reduced_to_auxiliary_realpart_jensen_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "previous_unique_remaining": OLD_REMAINING,
        "rejected_false_route": FALSE_INJECTION,
        "new_unique_internal_remaining": NEW_REMAINING,
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_backlund_escape": EXTERNAL_ACCEPTED,
        "dstructure_rankin_gate": DSTRUCTURE,
        "obstruction_examples": obstruction_examples(),
        "plain_conclusion": (
            "sign-change 吸收不能直接使用 xi 真零点的 Jensen C16 计数："
            "实部过零是曲线穿过一条直线，通常不等于 F=0。"
            "因此上一层的无重复吸收命题被进一步压成：必须构造经典 Backlund 的辅助实部解析计数对象，"
            "对该对象建立 Jensen 计数，并证明它与真零点、端点重数和缩进登记不重复扣费。"
            "这正是外部经典 Backlund 引理可整体接受的内容；严格自足版仍未闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund sign-change 吸收障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"previous_unique_remaining={result['previous_unique_remaining']}",
        f"rejected_false_route={result['rejected_false_route']}",
        f"new_unique_internal_remaining={result['new_unique_internal_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"row_column_external_route_closed={fmt_bool(result['row_column_external_route_closed'])}",
        "```",
        "",
        "## 1. 结构障碍",
        "",
        "| model | sign-change event | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["obstruction_examples"]:
        lines.append(
            f"| `{table_cell(item['model'])}` | {table_cell(item['sign_change_event'])} | {table_cell(item['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "结论：`Re(e^{-i theta}F)=0` 是一维实方程，`F=0` 是二维解析零点条件；"
            "前者不能注入后者。旧的 xi 真零点 Jensen C16 只能计真零点，不能自动计所有 Backlund sign-change。",
            "",
            "## 2. 新的精确剩余",
            "",
            "```text",
            f"{result['previous_unique_remaining']}",
            "  =>",
            f"NOT {result['rejected_false_route']}",
            "  AND",
            f"{result['new_unique_internal_remaining']}",
            "```",
            "",
            f"新的内部硬点：`{result['new_unique_internal_remaining']}`。",
            "",
            "它要求构造辅助实部函数、证明 Jensen 计数、再证明无重复扣费；这比“直接注入 xi 零点计数”严格得多。",
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
            f"外部路线最终仍需：`{result['dstructure_rankin_gate']}`。",
            "",
            "判定：自足版不能用 xi 真零点 Jensen 计数伪闭合；必须重证经典 Backlund 辅助实部 Jensen 包，或接受外部 Backlund 引理。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spine-json", type=Path, default=DEFAULT_SPINE)
    parser.add_argument("--jensen-zero-json", type=Path, default=DEFAULT_JENSEN_ZERO)
    parser.add_argument("--littlewood-json", type=Path, default=DEFAULT_LITTLEWOOD)
    parser.add_argument("--external-index", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "spine": args.spine_json,
        "jensen_zero": args.jensen_zero_json,
        "littlewood": args.littlewood_json,
        "external_index": args.external_index,
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
